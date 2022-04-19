import { createSlice } from '@reduxjs/toolkit';

const INITIAL_STATE = { page: 'home', loading: false };

const setScreen = (state = INITIAL_STATE, action) => ({
  ...state,
  page: action.payload.screen,
});

const setLoading = (state = INITIAL_STATE, action) => ({
  ...state,
  loading: action.payload.loading,
});

export const { reducer, actions } = createSlice({
  name: 'screen',
  initialState: INITIAL_STATE,
  reducers: {
    setScreen,
    setLoading,
  },
});
