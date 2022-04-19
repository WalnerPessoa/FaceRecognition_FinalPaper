import React, { useState, useEffect } from 'react';
import {
  View,
  Text,
  Animated,
  StyleSheet,
  Dimensions,
  TouchableOpacity,
  ScrollView,
} from 'react-native';
import { MaterialIcons } from '@expo/vector-icons';

const { width, height } = Dimensions.get('window');

const Drawer = ({ isOpen, close, names }) => {
  const [animatedContent] = useState(new Animated.Value(isOpen ? 0 : height));

  useEffect(() => {
    Animated.timing(animatedContent, {
      toValue: isOpen ? 0 : height,
      duration: 250,
    }).start();
  }, [isOpen]);

  return (
    <Animated.View style={[styles.container, { zIndex: isOpen ? 1 : -1 }]}>
      <Animated.View
        style={[
          styles.content,
          { transform: [{ translateY: animatedContent }, { translateX: 0 }] },
        ]}
      >
        <TouchableOpacity style={styles.icon} onPress={close}>
          <MaterialIcons name="close" size={48} color="#511991" />
        </TouchableOpacity>
        <ScrollView>
          {names.map(name => {
            const nameArray = name
              .split('_')
              .map(n => n.charAt(0).toUpperCase() + n.slice(1));

            return (
              <Text key={name} style={styles.text}>
                {nameArray.join(' ')}
              </Text>
            );
          })}
        </ScrollView>
      </Animated.View>
    </Animated.View>
  );
};

const styles = StyleSheet.create({
  container: {
    ...StyleSheet.absoluteFillObject,
    backgroundColor: 'transparent',
    display: 'flex',
    justifyContent: 'flex-end',
  },
  content: {
    backgroundColor: '#FFF',
    height: height / 2,
    borderTopLeftRadius: 38,
    borderTopRightRadius: 38,

    display: 'flex',
    padding: 18,
  },
  icon: {
    alignSelf: 'flex-end',
  },
  text: {
    fontSize: 28,
    marginBottom: 12,
  },
});

export default Drawer;
