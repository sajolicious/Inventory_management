import supplierReducer from '../features/supplierSlice';
import { configureStore, ThunkAction, Action,getDefaultMiddleware } from '@reduxjs/toolkit';
import supplierLoginReducer from '../features/supplierRegSlice';
import supplierLogReducer from '../features/supplierRegSlice';
const store = configureStore({
  reducer: {
    supplier: supplierReducer,
    supplierLogin:supplierLoginReducer,
    supplierLog:supplierLogReducer
    
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
