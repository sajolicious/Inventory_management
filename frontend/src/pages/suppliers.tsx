import React, { useEffect, useState } from 'react';
import axios from 'axios';

interface Supplier {
  id: string;
  name: string;
  phone: string;
  address: string;
  email: string;
}

const MyComponent: React.FC = () => {
  const [suppliers, setSuppliers] = useState<Supplier[]>([]);

  useEffect(() => {
    const fetchSuppliers = async () => {
      try {
        const response = await axios.get<Supplier[]>('http://127.0.0.1:8000/suppliers/1/');
        setSuppliers(response.data);
      } catch (error) {
        console.log('Failed to fetch suppliers:', error);
      }
    };

    fetchSuppliers();
  }, []);

  return (
    <div>
      <h1>Suppliers</h1>
      {suppliers.map((supplier) => (
        <div key={supplier.id}>
          <h3>{supplier.name}</h3>
          <p>{supplier.phone}</p>
          <p>{supplier.address}</p>
          <p>{supplier.email}</p>
        </div>
      ))}
    </div>
  );
};

export default MyComponent;
