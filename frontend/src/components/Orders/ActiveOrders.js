import React, { useState, useEffect } from "react";
import axios from "axios";
import OrderItem from "./OrderItem";

const ActiveOrders = () => {
  const [orders, setOrders] = useState([]);

  useEffect(() => {
    const fetchOrders = async () => {
      const response = await axios.get("/api/orders");
      setOrders(response.data);
    };
    fetchOrders();
  }, []);

  const activeOrders = orders.filter(order => order.status !== "completed");

  return (
    <div>
      <h2>Active Orders</h2>
      {activeOrders.length > 0 ? (
        activeOrders.map(order => <OrderItem key={order.id} order={order} />)
      ) : (
        <p>No active orders found.</p>
      )}
    </div>
  );
};

export default ActiveOrders;