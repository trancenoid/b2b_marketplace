import React, { useState, useEffect } from "react";
import axios from "axios";
import { Text, View, StyleSheet } from 'react-native';
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
    <View>
      <Text style={styles.heading}>Active Orders</Text>
      {activeOrders.length > 0 ? (
        activeOrders.map(order => <OrderItem key={order.id} order={order} />)
      ) : (
        <Text>No active orders found.</Text>
      )}
    </View>
  );
};

const styles = StyleSheet.create({
  heading: {
    fontSize: 20,
    fontWeight: 'bold',
    marginBottom: 10,
  },
});

export default ActiveOrders;