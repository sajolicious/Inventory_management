// store.ts
import { configureStore } from '@reduxjs/toolkit';
import supplierReducer from '../fetures/supplierSlice';

const store = configureStore({
  reducer: {
    suppliers: supplierReducer,
  },
});

export default store;
