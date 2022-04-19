import { configureStore } from '@reduxjs/toolkit';

import reducers from './ducks';

export const store = configureStore({
  reducer: reducers,
});
