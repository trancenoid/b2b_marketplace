import React from "react";
import { ActiveOrders, CompletedOrders } from "../components/Orders";

const OrdersScreen = () => {
  return (
    <div>
      <ActiveOrders />
      <CompletedOrders />
    </div>
  );
};

export default OrdersScreen;