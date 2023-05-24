import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { fetchSuppliers, selectSuppliers, selectLoading, selectError } from '../features/supplierSlice';

const SupplierList: React.FC = () => {
  const dispatch = useDispatch();
  const suppliers = useSelector(selectSuppliers);
  const loading = useSelector(selectLoading);
  const error = useSelector(selectError);

  useEffect(() => {
    dispatch(fetchSuppliers() as any);
  }, [dispatch]);

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error: {error}</div>;
  }

  return (
    <div>
      <h1>Supplier List</h1>
      {suppliers.map((supplier) => (
        <div key={supplier.id}>
          <h3>{supplier.name}</h3>
          <p>Phone: {supplier.phone}</p>
          <p>Address: {supplier.address}</p>
          <p>Email: {supplier.email}</p>
        </div>
      ))}
    </div>
  );
};

export default SupplierList;
