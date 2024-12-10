// pages/dado.js
import Navbar from '../components/Navbar';
import QueimadaChart from '../components/QueimadaChart';

const Home = () => {
  return (
    <div>
      <Navbar/>
      <h1>Portal A+zonia - Gráficos de Queimadas</h1>
      <QueimadaChart />
    </div>
  );
};

export default Home;
