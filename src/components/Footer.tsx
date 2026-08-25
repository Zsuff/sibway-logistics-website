import type { FC } from 'react';
import { Link } from 'react-router-dom';

export const Footer: FC = () => {
  return (
    <footer className="footer">
      <div className="footer-container">
        <div className="footer-section">
          <h3>Sibway Logistics</h3>
          <p>Ваш надійний партнер у світі логістики</p>
        </div>
        <div className="footer-section">
          <h4>Навігація</h4>
          <nav>
            <Link to="/">Головна</Link>
            <Link to="/about">Про нас</Link>
            <Link to="/services">Послуги</Link>
            <Link to="/contacts">Контакти</Link>
          </nav>
        </div>
        <div className="footer-section">
          <h4>Контакти</h4>
          <p>м. Київ, вул. Логістична, 1</p>
          <p>+38 (0XX) XXX-XX-XX</p>
          <p>info@sibway.com.ua</p>
        </div>
      </div>
      <div className="footer-bottom">
        <p>&copy; 2026 Sibway Logistics. Всі права захищено.</p>
      </div>
    </footer>
  );
};
