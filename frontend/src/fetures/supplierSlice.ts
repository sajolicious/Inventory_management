import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import axios from 'axios';

interface Suppliers {
  id:string;
  name: string;
  phone: string;
  address: string;
  email: string;
}

interface SupplierState {
  data: Suppliers[];
  loading: boolean;
  error: string | null;
}

const initialState: SupplierState = {
  data: [],
  loading: false,
  error: null,
};

export const fetchSuppliers = createAsyncThunk('suppliers/fetchSuppliers', async () => {
  try {
    const response = await axios.get('http://127.0.0.1:8000/suppliers/1/'); 
    return response.data;
    
  } catch (error) {
    throw new Error('Failed to fetch suppliers.');
  }
  
});

const supplierSlice = createSlice({
  name: 'suppliers',
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
        state.data = action.payload;
      })
      .addCase(fetchSuppliers.rejected, (state, action) => {
        state.loading = false;
        state.error = action.error.message ?? 'Failed to fetch suppliers.';
      });
  },
});

export default supplierSlice.reducer;
