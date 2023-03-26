import React from "react";
import { ActiveOrders, CompletedOrders } from "../components/Orders";

const OrdersScreen = () => {
  return (
    <View>
      <ActiveOrders />
      <CompletedOrders />
    </View>
  );
};

export default OrdersScreen;