import React from 'react';
import { Link } from 'react-router-dom';

export const Footer: React.FC = () => {
  return (
    <footer className="bg-[#29265B] text-white pt-20 pb-10 relative">
      <div className="container mx-auto px-6">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12 mb-16">
          {/* Column 1: Company Name */}
          <div className="flex flex-col gap-6">
            <Link to="/" className="text-xl font-extrabold text-white hover:text-[#189CD9] transition-colors">
              Sibway Logistics
            </Link>
          </div>

          {/* Column 2: Navigation */}
          <div>
            <h4 className="text-white font-bold text-lg mb-4">Навігація</h4>
            <ul className="space-y-3">
              <li>
                <Link
                  to="/"
                  className="text-[#D9DDE3] hover:text-white transition-colors hover:underline"
                >
                  Головна
                </Link>
              </li>
              <li>
                <Link
                  to="/services"
                  className="text-[#D9DDE3] hover:text-white transition-colors hover:underline"
                >
                  Послуги
                </Link>
              </li>
              <li>
                <Link
                  to="/about"
                  className="text-[#D9DDE3] hover:text-white transition-colors hover:underline"
                >
                  Про компанію
                </Link>
              </li>
              <li>
                <Link
                  to="/contacts"
                  className="text-[#D9DDE3] hover:text-white transition-colors hover:underline"
                >
                  Контакти
                </Link>
              </li>
            </ul>
          </div>

          {/* Column 3: Contacts */}
          <div id="contacts">
            <h4 className="text-white font-bold text-lg mb-4">Контакти</h4>
            <ul className="space-y-3 text-[#D9DDE3] text-base">
              <li className="hover:text-white transition-colors leading-relaxed">
                Україна, 33028, м. Рівне, вулиця Литовська 75
              </li>
              <li>
                <a
                  href="tel:+380638767270"
                  className="text-[#D9DDE3] hover:text-white transition-colors hover:underline"
                >
                  +380 63 876 72 70
                </a>
              </li>
              <li>
                <a
                  href="mailto:sibway@ukr.net"
                  className="text-[#D9DDE3] hover:text-white transition-colors hover:underline"
                >
                  sibway@ukr.net
                </a>
              </li>
            </ul>
          </div>

          {/* Column 4: Legal */}
          <div>
            <h4 className="text-white font-bold text-lg mb-4">Юридична інформація</h4>
            <ul className="space-y-3">
              <li>
                <a href="#privacy" className="text-[#D9DDE3] hover:text-white transition-colors hover:underline">
                  Політика конфіденційності
                </a>
              </li>
              <li>
                <a href="#terms" className="text-[#D9DDE3] hover:text-white transition-colors hover:underline">
                  Умови використання
                </a>
              </li>
            </ul>
          </div>
        </div>

        {/* Bottom Section */}
        <div className="border-t border-white/20 pt-10 text-center">
          <p className="text-[#D9DDE3] text-sm hover:text-white transition-colors">
            © 2026 Sibway Logistics. Всі права захищені.
          </p>
        </div>
      </div>
    </footer>
  );
};
