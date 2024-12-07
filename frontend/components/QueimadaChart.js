import { useState, useEffect } from "react";
import { Line } from "react-chartjs-2";
import { Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend } from "chart.js";

ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend);

export default function Graph() {
  const [municipios, setMunicipios] = useState([]); // Para armazenar os municípios
  const [selectedMunicipio, setSelectedMunicipio] = useState(""); // Município selecionado
  const [graphData, setGraphData] = useState({}); // Dados para o gráfico

  // Função para buscar os municípios disponíveis
  useEffect(() => {
    const fetchMunicipios = async () => {
      const response = await fetch('http://localhost:8000/api/municipios/');
      const data = await response.json();
      setMunicipios(data);
    };
    fetchMunicipios();
  }, []);

  // Função para buscar dados do município selecionado
  useEffect(() => {
    if (selectedMunicipio) {
      const fetchData = async () => {
        const response = await fetch(`http://localhost:8000/api/queimadas/?municipio=${selectedMunicipio}`);
        const data = await response.json();

        const riscoFogo = data.map(d => d.risco_fogo); // Dados de risco de fogo
        const frp = data.map(d => d.frp); // Dados de FRP

        setGraphData({
          labels: ["risco_fogo", "frp"],
          datasets: [
            {
              label: "Risco de Fogo",
              data: riscoFogo,
              borderColor: "red",
              backgroundColor: "rgba(255, 0, 0, 0.1)",
              fill: true,
            },
            {
              label: "FRP",
              data: frp,
              borderColor: "green",
              backgroundColor: "rgba(0, 255, 0, 0.1)",
              fill: true,
            },
          ],
        });
      };

      fetchData();
    }
  }, [selectedMunicipio]);

  return (
    <div>
      <h1>Gráficos de Queimadas</h1>
      
      {/* Seletor de Município */}
      <select onChange={(e) => setSelectedMunicipio(e.target.value)} value={selectedMunicipio}>
        <option value="">Selecione o Município</option>
        {municipios.map(municipio => (
          <option key={municipio.estado} value={municipio.nome}>
            {municipio.nome}
          </option>
        ))}
      </select>

      {/* Gráfico */} 
      {selectedMunicipio && graphData.labels && (
        <div className="chart-container">
            <Line data={graphData} />
        </div>
      )}
    </div>
  );
}