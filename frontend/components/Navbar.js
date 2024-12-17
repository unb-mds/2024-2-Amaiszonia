import Link from 'next/link';

const Navbar = () => {
  return (
    <nav className="navbar navbar-expand-lg navbar-light bg-light navbar-container">
      <img src='/images/logo2.png' id='logo-home' className="navbar-brand" href="#"/>
        <ul className="navbar-nav mr-auto">
          <li className="nav-item">
            <a className="nav-link" href="/">Home</a>
          </li>
          <li className="nav-item">
            <Link className="nav-link" href="/dados">Dados</Link>
          </li>
          <li className="nav-item">
            <Link className="nav-link" href="/feedback">Sugestões</Link>
          </li>
        </ul>
    </nav>
  );
};

export default Navbar;
