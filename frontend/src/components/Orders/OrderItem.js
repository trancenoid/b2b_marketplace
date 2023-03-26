import React from 'react';
import { Text, View, StyleSheet } from 'react-native';

const OrderItem = ({ order }) => {
  const { product_id, buyer_id, quantity, comments, order_date, order_status } = order;

  return (
    <View style={styles.orderContainer}>
      <View style={styles.rowContainer}>
        <Text style={styles.label}>Product ID: </Text>
        <Text style={styles.value}>{product_id}</Text>
      </View>
      <View style={styles.rowContainer}>
        <Text style={styles.label}>Buyer ID: </Text>
        <Text style={styles.value}>{buyer_id}</Text>
      </View>
      <View style={styles.rowContainer}>
        <Text style={styles.label}>Quantity: </Text>
        <Text style={styles.value}>{quantity}</Text>
      </View>
      {comments && (
        <View style={styles.rowContainer}>
          <Text style={styles.label}>Comments: </Text>
          <Text style={styles.value}>{comments}</Text>
        </View>
      )}
      <View style={styles.rowContainer}>
        <Text style={styles.label}>Order Date: </Text>
        <Text style={styles.value}>{order_date ? new Date(order_date).toDateString() : 'N/A'}</Text>
      </View>
      <View style={styles.rowContainer}>
        <Text style={styles.label}>Order Status: </Text>
        <Text style={styles.value}>{order_status || 'N/A'}</Text>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  orderContainer: {
    backgroundColor: '#fff',
    borderRadius: 10,
    padding: 10,
    margin: 10,
    borderWidth: 1,
    borderColor: '#ccc',
  },
  rowContainer: {
    flexDirection: 'row',
    marginVertical: 5,
  },
  label: {
    fontWeight: 'bold',
    marginRight: 5,
  },
  value: {
    flex: 1,
  },
});

export default OrderItem;