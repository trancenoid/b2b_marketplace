import { AppRegistry } from 'react-native';
import App from './App';
import name from './app.json';
const appName = name;
AppRegistry.registerComponent(appName, () => App);