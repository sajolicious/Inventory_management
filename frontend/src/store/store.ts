import { configureStore } from '@reduxjs/toolkit';
import supplierReducer from '../fetures/supplierSlice';

const store = configureStore({
  reducer: {
    supplier: supplierReducer,
  },
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;

export default store;
