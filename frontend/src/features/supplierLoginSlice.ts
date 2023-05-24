import { createSlice, PayloadAction } from '@reduxjs/toolkit';
import { AppThunk } from '../store/store';
import axios from 'axios';
interface Supplier {
    name: string;
    email:string
    // Include other relevant supplier data
}

interface SupplierState {
    loggedIn: boolean;
    supplier: Supplier | null;
    error: string | null;
}

const initialState: SupplierState = {
    loggedIn: false,
    supplier: null,
    error: null,
};

const supplierLogSlice = createSlice({
    name: 'supplier',
    initialState,
    reducers: {
        loginSupplierSuccess(state, action: PayloadAction<Supplier>) {
            state.loggedIn = true;
            state.supplier = action.payload;
            state.error = null;
        },
        loginSupplierFailure(state, action: PayloadAction<string>) {
            state.loggedIn = false;
            state.supplier = null;
            state.error = action.payload;
        },
        logoutSupplier(state) {
            state.loggedIn = false;
            state.supplier = null;
            state.error = null;
        },
    },
});

export const {
    loginSupplierSuccess,
    loginSupplierFailure,
    logoutSupplier,
} = supplierLogSlice.actions;

export default supplierLogSlice.reducer;

export const loginSuppliers = (supplier: Supplier): AppThunk => async (
    dispatch
) => {
    try {
        // Make the API request to the Django backend
        const response = await axios.post('http://127.0.0.1:8000/suppliers/login/', supplier);

        // Handle successful login
        dispatch(loginSupplierSuccess(response.data));
    } catch (error:any) {
        dispatch(loginSupplierFailure(error.message));
    }
};
