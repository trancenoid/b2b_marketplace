import React, { useState } from 'react';
import { View, Text, TextInput, TouchableOpacity, StyleSheet } from 'react-native';

export default function AuthScreen() {
  const [loginForm, setLoginForm] = useState({ username: '', password: '' });
  const [registerForm, setRegisterForm] = useState({ username: '', password: '' });

  const handleLoginSubmit = () => {
    // Handle login form submission
    console.log('Submitting login form', loginForm);
  };

  const handleRegisterSubmit = () => {
    // Handle registration form submission
    console.log('Submitting registration form', registerForm);
  };

  return (
    <View style={styles.container}>
      <View style={styles.formContainer}>
        <Text style={styles.header}>Log In</Text>
        <TextInput
          style={styles.input}
          placeholder="Username"
          onChangeText={text => setLoginForm({ ...loginForm, username: text })}
          value={loginForm.username}
        />
        <TextInput
          style={styles.input}
          placeholder="Password"
          secureTextEntry
          onChangeText={text => setLoginForm({ ...loginForm, password: text })}
          value={loginForm.password}
        />
        <TouchableOpacity style={styles.button} onPress={handleLoginSubmit}>
          <Text style={styles.buttonText}>Log In</Text>
        </TouchableOpacity>
      </View>
      <View style={styles.formContainer}>
        <Text style={styles.header}>Register</Text>
        <TextInput
          style={styles.input}
          placeholder="Username"
          onChangeText={text => setRegisterForm({ ...registerForm, username: text })}
          value={registerForm.username}
        />
        <TextInput
          style={styles.input}
          placeholder="Password"
          secureTextEntry
          onChangeText={text => setRegisterForm({ ...registerForm, password: text })}
          value={registerForm.password}
        />
        <TouchableOpacity style={styles.button} onPress={handleRegisterSubmit}>
          <Text style={styles.buttonText}>Register</Text>
        </TouchableOpacity>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  formContainer: {
    marginBottom: 30,
  },
  header: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 10,
  },
  input: {
    height: 40,
    borderColor: 'gray',
    borderWidth: 1,
    marginBottom: 10,
    paddingHorizontal: 10,
    borderRadius: 5,
  },
  button: {
    backgroundColor: 'blue',
    padding: 10,
    borderRadius: 5,
  },
  buttonText: {
    color: 'white',
    textAlign: 'center',
    fontWeight: 'bold',
  },
});