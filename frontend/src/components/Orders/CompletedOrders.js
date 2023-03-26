import React, { useState, useEffect } from "react";
import axios from "axios";
import OrderItem from "./OrderItem";

const CompletedOrders = () => {
  const [orders, setOrders] = useState([]);

  useEffect(() => {
    const fetchOrders = async () => {
      const response = await axios.get("/api/orders");
      setOrders(response.data);
    };
    fetchOrders();
  }, []);

  const completedOrders = orders.filter(order => order.status === "completed");

  return (
    <div>
      <h2>Completed Orders</h2>
      {completedOrders.length > 0 ? (
        completedOrders.map(order => <OrderItem key={order.id} order={order} />)
      ) : (
        <p>No completed orders found.</p>
      )}
    </div>
  );
};

export default CompletedOrders;