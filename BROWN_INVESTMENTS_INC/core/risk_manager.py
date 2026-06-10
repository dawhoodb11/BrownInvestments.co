class RiskManager:
    def position_size(self, balance, risk_percent, sl):
        return round((balance * risk_percent/100)/sl, 2)

    def drawdown(self, equity, peak):
        return ((peak-equity)/peak)*100
