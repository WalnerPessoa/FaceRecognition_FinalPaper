import React, { useState, useContext } from 'react';
import { StyleSheet, Text, View, StatusBar } from 'react-native';
import { Provider } from 'react-redux';

import { store } from './store';

import Screen from './screen';

export default function App() {
  return (
    <Provider store={store}>
      <Screen />
    </Provider>
  );
}
