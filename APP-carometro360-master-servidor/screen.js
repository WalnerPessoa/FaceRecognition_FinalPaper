import React from 'react';
import { StatusBar } from 'react-native';

import Home from './screens/Home';
import AppCamera from './screens/AppCamera';
import Preview from './screens/Preview';
import ProcessedPhoto from './screens/ProcessedPhoto';

import { useSelector } from 'react-redux';

const screenMap = {
  home: Home,
  camera: AppCamera,
  preview: Preview,
  processedPhoto: ProcessedPhoto,
};

export default function Screen() {
  const screen = useSelector(state => state.screen);
  const CurrentScreen = screenMap[screen.page];

  return (
    <>
      <StatusBar barStyle="dark-content" />
      <CurrentScreen />
    </>
  );
}
