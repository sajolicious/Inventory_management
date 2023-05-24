import MyComponent from "./pages/suppliers";
import SupplierLogin from "./supplierLogin/supplierLogin";
function App() {
  return (  
    <div >
      <header>
        <p>
          <MyComponent/>
          <SupplierLogin/>
        </p>
      </header>
    </div>
  
  );
}

export default App;
