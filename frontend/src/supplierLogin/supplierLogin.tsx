import React, { useState } from 'react';
import { useDispatch } from 'react-redux';
import { loginSuppliers } from '../features/supplierLoginSlice';
import { AppDispatch } from '../store/store';
import { Typography, TextField, Button, Grid } from '@mui/material';
import { useNavigate} from 'react-router-dom';

const SupplierLogIn: React.FC = () => {
  const dispatch: AppDispatch = useDispatch();
  const navigate= useNavigate();
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');

  const handleLogin = () => {
    dispatch(loginSuppliers({ name, email }));
    console.log('hello');
    navigate('/navbar'); // Redirect to the dashboard page after successful login
  };

  return (
    <div>
      <Typography variant="h2" gutterBottom>
        Supplier Login
      </Typography>
      <Grid container spacing={2}>
        <Grid item xs={12} lg={4}>
          <TextField
            id="name"
            label="Name"
            variant="outlined"
            value={name}
            onChange={(e) => setName(e.target.value)}
            fullWidth
          />
        </Grid>
        <Grid item xs={12} lg={4}>
          <TextField
            id="email"
            label="email"
            variant="outlined"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            fullWidth
          />
        </Grid>
        <Grid item xs={12} lg={4}>
          <Button variant="contained" color="primary" onClick={handleLogin}>
            Login
          </Button>
        </Grid>
      </Grid>
    </div>
  );
};

export default SupplierLogIn;
