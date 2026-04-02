#!/usr/bin/env python3
"""
Daily price updater for honesttom.ai / Mr. Tight portfolio tracker.
Runs via GitHub Actions after US market close (Mon–Fri).
Writes prices.json to repo root.
"""

import json
import yfinance as yf
from datetime import datetime

# ── Portfolio tickers ──────────────────────────────────────────────────────────
STOCK_MAP = {
    "AA":   "AA",
    "MSFT": "MSFT",
    "AMZN": "AMZN",
    "BTC":  "BTC-USD",
    "NVDA": "NVDA",
    "VOO":  "VOO",
    "VONG": "VONG",
    "EXE":  "EXE",
    "ETH":  "ETH-USD",
    "ARKK": "ARKK",
}

# ── Index tickers ──────────────────────────────────────────────────────────────
INDEX_MAP = {
    "S&P 500": "^GSPC",
    "DOW":     "^DJI",
    "NASDAQ":  "^IXIC",
}

def safe_price(sym):
    """Return (price, prev_close) or (None, None) on error."""
    try:
        t = yf.Ticker(sym)
        fi = t.fast_info
        price = round(float(fi.last_price), 2)
        prev  = round(float(fi.previous_close), 2)
        return price, prev
    except Exception as e:
        print(f"  WARN {sym}: {e}")
        return None, None

# ── Stock prices ───────────────────────────────────────────────────────────────
print("Fetching stock prices...")
prices = {}
for key, sym in STOCK_MAP.items():
    price, _ = safe_price(sym)
    if price is not None:
        prices[key] = price
        print(f"  {key}: {price}")

# ── Indices ────────────────────────────────────────────────────────────────────
print("Fetching indices...")
indices = {}
for name, sym in INDEX_MAP.items():
    price, prev = safe_price(sym)
    if price is not None and prev is not None and prev > 0:
        chg = round(price - prev, 2)
        pct = round((price - prev) / prev * 100, 2)
        indices[name] = {"value": price, "change": chg, "pct": pct}
        print(f"  {name}: {price}  ({pct:+.2f}%)")

# ── Oil (WTI) ──────────────────────────────────────────────────────────────────
print("Fetching WTI crude...")
oil_price, oil_prev = safe_price("CL=F")
oil = None
if oil_price is not None and oil_prev is not None and oil_prev > 0:
    oil_pct = round((oil_price - oil_prev) / oil_prev * 100, 2)
    oil = {"price": oil_price, "pct": oil_pct}
    print(f"  WTI: {oil_price}  ({oil_pct:+.2f}%)")

# ── Write prices.json ──────────────────────────────────────────────────────────
today = datetime.utcnow().strftime("%B %d, %Y")

output = {
    "prices":  prices,
    "indices": indices,
    "updated": today,
}
if oil:
    output["oil"] = oil

with open("prices.json", "w") as f:
    json.dump(output, f, indent=2)
    f.write("\n")

print(f"\nWrote prices.json ({today})")
print(json.dumps(output, indent=2))
