import React from 'react';
import {
  SafeAreaView,
  TouchableOpacity,
  StyleSheet,
  Platform,
} from 'react-native';
import { MaterialIcons } from '@expo/vector-icons';

export default function OptionButtons({
  handleCancel,
  leftIcon,
  righIcon,
  mainIcon,
}) {
  const righIconOpacity = righIcon && righIcon.disabled ? 0.5 : 1;

  return (
    <SafeAreaView style={styles.buttons}>
      {leftIcon && (
        <TouchableOpacity onPress={leftIcon.action}>
          <MaterialIcons name={leftIcon.name} size={48} color="#FFF" />
        </TouchableOpacity>
      )}
      <TouchableOpacity
        style={[
          styles.mainButton,
          {
            backgroundColor: mainIcon.color || '#511991',
            opacity: mainIcon.disabled ? 0.5 : 1,
          },
        ]}
        disabled={mainIcon.disabled}
        onPress={mainIcon.action}
      >
        <MaterialIcons name={mainIcon.name} size={48} color="#FFF" />
      </TouchableOpacity>
      {righIcon && (
        <TouchableOpacity
          disabled={righIcon.disabled}
          onPress={righIcon.action}
        >
          <MaterialIcons
            name={righIcon.name}
            size={48}
            color={righIcon.disabled ? '#aaa' : '#fff'}
            style={{ opacity: righIconOpacity }}
          />
        </TouchableOpacity>
      )}
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  buttons: {
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'flex-end',
    flex: 1,
    backgroundColor: 'transparent',
    flexDirection: 'row',
    marginBottom: Platform.OS === 'android' ? 15 : 0,
  },
  mainButton: {
    backgroundColor: '#511991',
    height: 84,
    width: 84,
    borderRadius: 50,
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    marginRight: 18,
    marginLeft: 18,
  },
});
