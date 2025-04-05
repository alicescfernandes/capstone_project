// store.js
import { configureStore } from '@reduxjs/toolkit';
import { quarterApi } from './endpoints';

export const store = configureStore({
  reducer: {
    [quarterApi.reducerPath]: quarterApi.reducer,
    // outros reducers se quiseres
  },
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware().concat(quarterApi.middleware),
});



