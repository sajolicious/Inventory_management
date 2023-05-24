import { createSlice, PayloadAction } from '@reduxjs/toolkit';
import { AppThunk } from '../store/store';
import axios from 'axios';
interface Supplier {
    name: string;
    phone: string;
    address:string;
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

const suppliesRegistrationSlice = createSlice({
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
} = suppliesRegistrationSlice.actions;

export default suppliesRegistrationSlice.reducer;

export const loginSupplier = (supplier: Supplier): AppThunk => async (
    dispatch
) => {
    try {
        // Make the API request to the Django backend
        const response = await axios.post('http://127.0.0.1:8000/suppliers/1/', supplier);

        // Handle successful login
        dispatch(loginSupplierSuccess(response.data));
    } catch (error:any) {
        dispatch(loginSupplierFailure(error.message));
    }
};
