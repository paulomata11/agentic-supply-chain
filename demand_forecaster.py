import numpy as np
from datetime import datetime, timedelta

class DemandForecasterAgent:
    """
    Agentic Demand Forecasting for MENA Supply Chain Optimization.
    Integrates external market signals with historical P&L data.
    """
    def __init__(self):
        self.region_weights = {"Dubai": 1.2, "Abu Dhabi": 1.1, "Riyadh": 1.3}

    def predict_demand(self, product_id: str, days: int = 30):
        print(f"Generating predictive forecast for {product_id}...")
        # Mocking a stochastic demand curve influenced by regional growth
        base_demand = np.random.normal(100, 15, days)
        forecast = base_demand * self.region_weights.get("Dubai", 1.0)
        
        return {
            "product_id": product_id,
            "forecast_horizon": f"{days} days",
            "confidence_interval": 0.95,
            "mean_expected_units": int(np.mean(forecast))
        }

if __name__ == "__main__":
    agent = DemandForecasterAgent()
    results = agent.predict_demand("HPC-Server-Cluster-X1")
    print(results)
