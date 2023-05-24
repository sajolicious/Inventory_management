import MyComponent from "./pages/suppliers";
import Navbar from "./pages/HomePage";
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import SupplierLogIn from "./supplierLogin/supplierLogin";
import SupplierLogin from "./supplierLogin/supplierRegistration";
function App() {
  return (  
    <Router> 
      <Routes>
        <Route path="/" element={<SupplierLogIn />} />
        <Route path="/MyComponent" element={<MyComponent />} />
        <Route path="/SupplierLogin" element={<SupplierLogIn />} />
        <Route path="/SupplierLogIn" element={<SupplierLogin />} />
        <Route path="/navbar" element={<Navbar />} />
      </Routes>
    </Router>
  
  );
}



export default App;
