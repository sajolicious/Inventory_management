import supplierReducer from '../fetures/supplierSlice';
import { configureStore, ThunkAction, Action,getDefaultMiddleware } from '@reduxjs/toolkit';
import supplierLoginReducer from '../fetures/supplierLoginSlice';
const store = configureStore({
  reducer: {
    supplier: supplierReducer,
    supplierLogin:supplierLoginReducer
  },
  middleware: getDefaultMiddleware({
    // Add any additional middleware here
  }),
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;
export type AppThunk<ReturnType = void> = ThunkAction<
  ReturnType,
  RootState,
  unknown,
  Action<string>
>;
export default store;
