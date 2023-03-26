import React, { useState, useEffect } from "react";
import axios from "axios";
import { View, Text } from "react-native";
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

  const completedOrders = orders.filter((order) => order.status === "completed");

  return (
    <View>
      <Text>Completed Orders</Text>
      {completedOrders.length > 0 ? (
        completedOrders.map((order) => <OrderItem key={order.id} order={order} />)
      ) : (
        <Text>No completed orders found.</Text>
      )}
    </View>
  );
};

export default CompletedOrders;