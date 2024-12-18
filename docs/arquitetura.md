# Arquitetura do Sistema - A+zônia

## Introdução


**A+zônia** é uma plataforma que busca facilitar o acesso da população a dados atualizados sobre desmatamento e queimadas na Amazônia Legal. Com uma interface intuitiva, promove a conscientização ambiental ao apresentar informações relevantes de forma prática e acessível, incentivando o monitoramento e a divulgação de questões cruciais para a preservação da região.

## Diagrama de Arquitetura

<iframe
  src="https://www.figma.com/embed?embed_host=share&url=https://www.figma.com/design/Qwr0wSu0u54PdgBDXFdI1A/Protótipo-de-Arquitetura"
  width="800"
  height="600"
  style="border: none;"
  allowfullscreen
></iframe>


## Principais Componentes

O sistema é dividido em 3 camadas principais:

1. **Front-end**  
2. **Back-end**  
3. **Banco de Dados**  

Cada camada possui subcomponentes específicos, descritos a seguir.

### 1. Banco de Dados

- **SQLite**: Banco de dados utilizado para armazenar informações sobre queimadas, estados e sugestões.  

### 2. Front-end

- **Client (Web)**: O front-end é responsável por fornecer a interface do usuário (UI), permitindo a interação dos usuários com o sistema. No Amaiszonia, o cliente web facilita a visualização e busca das informações desejadas. O design da interface é elaborado com **Figma** e frameworks para estilização e responsividade.  

### 3. Back-end

O back-end, embora não visível aos usuários finais, é essencial para gerenciar a lógica de negócios, interações com o banco de dados e comunicação com o front-end. No projeto Amaiszonia, o back-end é composto pelos seguintes subcomponentes:

- **Django**: Framework principal do sistema, responsável por gerenciar requisições HTTP, autenticação de usuários e rotas de API. O Django orquestra chamadas aos módulos da API e coordena o acesso ao banco de dados.  
- **API**: A API expõe endpoints que permitem ao front-end interagir com o sistema.  

## Conclusão

A arquitetura do projeto Amaiszonia foi projetada para ser modular, escalável e de fácil manutenção, utilizando tecnologias amplamente adotadas no mercado. Com o uso do **Django**, **SQLite** e **Docker**, o sistema oferece robustez para lidar com o volume esperado de usuários e flexibilidade para evoluir conforme as necessidades. A separação clara entre front-end, API e banco de dados possibilita um desenvolvimento colaborativo eficiente e facilita a expansão futura da plataforma.