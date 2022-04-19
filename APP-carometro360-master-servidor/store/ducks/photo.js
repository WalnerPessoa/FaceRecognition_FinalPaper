import { createSlice } from '@reduxjs/toolkit';

const INITIAL_STATE = { photo: {}, processedPhoto: {} };

const setPhoto = (state = INITIAL_STATE, action) => ({
  ...state,
  photo: action.payload.photo,
});

const setProcessedPhoto = (state = INITIAL_STATE, action) => ({
  ...state,
  processedPhoto: action.payload.photo,
});

export const { reducer, actions } = createSlice({
  name: 'photos',
  initialState: INITIAL_STATE,
  reducers: {
    setPhoto,
    setProcessedPhoto,
  },
});
