"use client";
import { AgChartsReact } from "ag-charts-react";
import { useState } from "react";

const Home = () => {
  const [stockTickerSymbol, setStockTickerSymbol] = useState("AAPL");
  const [chart, setChart] = useState({} as any);
  const getStockData = async () => {
    const response = await fetch(
      `http://localhost:5001/api/stock/${stockTickerSymbol}`
    );
    const data = await response.json();
    data ? console.log(data) : alert("Stock not found");
  };

  return (
    <div style={{ width: "100%", height: "500px" }}>
      <h1>Chart</h1>
      <input
        value={stockTickerSymbol}
        onChange={(e) => setStockTickerSymbol(e.target.value)}
      />
      <button onClick={getStockData}>Get Stock Data</button>
      <AgChartsReact options={chart} />
    </div>
  );
};

export default Home;
