import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import axios from 'axios';
import { RootState } from '../store/store';
interface Supplier {
  id: string;
  name: string;
  phone: string;
  address: string;
  email: string;
}

interface SupplierState {
  suppliers: Supplier[];
  loading: boolean;
  error: string | null;
}

const initialState: SupplierState = {
  suppliers: [],
  loading: false,
  error: null,
};

export const fetchSuppliers = createAsyncThunk('suppliers/fetchSuppliers', async () => {
  try {
    const response = await axios.get<Supplier[]>('http://127.0.0.1:8000/suppliers/1/');
    return response.data;
  } catch (error) {
    throw new Error('Failed to fetch suppliers.');
  }
});

const supplierSlice = createSlice({
  name: 'supplier',
  initialState,
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(fetchSuppliers.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(fetchSuppliers.fulfilled, (state, action) => {
        state.loading = false;
        state.suppliers = action.payload;
      })
      .addCase(fetchSuppliers.rejected, (state, action) => {
        state.loading = false;
        state.error = action.error.message ?? 'Failed to fetch suppliers.';
      });
  },
});

export const selectSuppliers = (state: RootState) => state.supplier.suppliers;
export const selectLoading = (state: RootState) => state.supplier.loading;
export const selectError = (state: RootState) => state.supplier.error;

export default supplierSlice.reducer;
