import type { FC } from 'react';
import { useState } from 'react';
import { Link, useLocation } from 'react-router-dom';

export const Header: FC = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const location = useLocation();

  const toggleMenu = () => {
    setIsMenuOpen(!isMenuOpen);
  };

  const isActive = (path: string) => {
    return location.pathname === path;
  };

  return (
    <header className="header">
      <div className="header-container">
        <Link to="/" className="logo">
          Sibway
        </Link>
        <nav className={`nav ${isMenuOpen ? 'nav-open' : ''}`}>
          <Link
            to="/"
            className={`nav-link ${isActive('/') ? 'active' : ''}`}
            onClick={() => setIsMenuOpen(false)}
          >
            Головна
          </Link>
          <Link
            to="/about"
            className={`nav-link ${isActive('/about') ? 'active' : ''}`}
            onClick={() => setIsMenuOpen(false)}
          >
            Про нас
          </Link>
          <Link
            to="/services"
            className={`nav-link ${isActive('/services') ? 'active' : ''}`}
            onClick={() => setIsMenuOpen(false)}
          >
            Послуги
          </Link>
          <Link
            to="/transport"
            className={`nav-link ${isActive('/transport') ? 'active' : ''}`}
            onClick={() => setIsMenuOpen(false)}
          >
            Транспорт
          </Link>
          <Link
            to="/contacts"
            className={`nav-link ${isActive('/contacts') ? 'active' : ''}`}
            onClick={() => setIsMenuOpen(false)}
          >
            Контакти
          </Link>
        </nav>
        <button className="menu-toggle" onClick={toggleMenu}>
          <span></span>
          <span></span>
          <span></span>
        </button>
      </div>
    </header>
  );
};
