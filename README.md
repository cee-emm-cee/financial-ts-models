# financial-ts-models

Time series and volatility modeling applied to financial data. Built as part of MFE application preparation and research groundwork.

## Notebooks

### 01_arima.ipynb
ARIMA modeling on SPY daily returns (2019-2025).
- ADF testing, differencing, ACF/PACF analysis
- ARIMA(1,1,1) model fit
- Residual diagnostics: Ljung-Box (p=0.96), Jarque-Bera (skew=-0.59, kurtosis=6.81)
- Key finding: AR and MA coefficients nearly cancel, confirming weak mean predictability in daily returns

### 02_garch.ipynb
Conditional volatility modeling on SPY returns.
- GARCH(1,1): persistence 0.9658, half-life ~20 days
- EGARCH(1,1): log-variance specification, highest AIC/BIC
- GJR-GARCH(1,1): gamma=0.2009 (significant), negative shocks have 4.6x variance impact
- GJR-GARCH wins on both AIC (4174.9) and BIC (4201.5)
- Out-of-sample forecasting: train/test split at 2024, one-step-ahead forecasts vs 21-day realized vol
- Multi-step variance term structure (10-day horizon)

### 03_volatility_models.ipynb
Realized vs conditional volatility comparison.
- Three realized vol estimators: close-to-close, Parkinson (1980), Garman-Klass (1980)
- Window length comparison: 5-day, 21-day, 63-day
- GARCH/GJR-GARCH conditional vol vs Garman-Klass realized vol
- Correlation matrix: realized estimators 0.96-0.99, conditional vol 0.86-0.91 against realized
- Vol-of-vol analysis: rolling std of realized vol

### 04_cointegration.ipynb (in progress)
Engle-Granger cointegration test on ETF pairs. Foundation for statistical arbitrage backtester.
- ETF pair candidates: GLD/GDX, EWA/EWC, XLE/XOP
- Stationarity testing, spread construction, half-life estimation

## Data

SPY OHLC daily data via yfinance (2019-2025).

## Tools

Python, pandas, numpy, statsmodels, arch, matplotlib
