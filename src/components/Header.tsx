import React, { useState, useEffect } from 'react';
import { NavLink, Link, useNavigate } from 'react-router-dom';
import logoImg from '../assets/logo.png';

export const Header: React.FC = () => {
  const [scrolled, setScrolled] = useState(false);
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const navigate = useNavigate();

  useEffect(() => {
    const handleScroll = () => {
      setScrolled(window.scrollY > 50);
    };
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const closeMenu = () => {
    setMobileMenuOpen(false);
  };

  const navLinkClass = ({ isActive }: { isActive: boolean }) =>
    `transition-colors focus:outline-none focus:text-[#189CD9] ${
      isActive
        ? 'text-[#189CD9] font-bold border-b-2 border-[#189CD9] pb-0.5'
        : 'text-slate-700 dark:text-slate-200 hover:text-[#189CD9]'
    }`;

  const mobileNavLinkClass = ({ isActive }: { isActive: boolean }) =>
    `transition-colors py-1 block ${
      isActive
        ? 'text-[#189CD9] font-bold'
        : 'text-slate-700 dark:text-slate-200 hover:text-[#189CD9]'
    }`;

  return (
    <header
      id="main-header"
      className={`fixed top-0 w-full z-50 transition-all duration-300 border-b ${
        scrolled
          ? 'bg-white/95 dark:bg-slate-900/95 shadow-md border-slate-200 dark:border-slate-800 py-3'
          : 'bg-white/90 dark:bg-slate-900/90 backdrop-blur-md border-slate-200/80 dark:border-slate-800/80 py-5'
      }`}
    >
      <div className="container mx-auto px-6 flex items-center justify-between">
        {/* Brand Logo */}
        <Link
          to="/"
          onClick={closeMenu}
          className="flex items-center focus:outline-none focus:ring-2 focus:ring-sky-500 rounded-md"
        >
          <img
            src={logoImg}
            alt="Sibway Logistics Logo"
            className="h-[32px] md:h-[36px] lg:h-[40px] w-auto object-contain transition-transform duration-300 hover:scale-105"
          />
        </Link>

        {/* Desktop Navigation */}
        <nav className="hidden md:flex items-center gap-8 font-medium">
          <NavLink to="/" end className={navLinkClass}>
            Головна
          </NavLink>
          <NavLink to="/services" className={navLinkClass}>
            Послуги
          </NavLink>
          <NavLink to="/about" className={navLinkClass}>
            Про компанію
          </NavLink>
          <NavLink to="/contacts" className={navLinkClass}>
            Контакти
          </NavLink>
        </nav>

        {/* Header Action Button & Direct Call Link */}
        <div className="hidden md:flex items-center gap-6">
          <a
            href="tel:+380638767270"
            className="hidden xl:flex items-center gap-2 font-bold text-slate-800 dark:text-white hover:text-[#189CD9] transition-colors focus:outline-none focus:ring-2 focus:ring-sky-500 rounded-md px-2 py-1"
          >
            <span className="material-icons text-[#189CD9] text-base">call</span>
            +380 63 876 72 70
          </a>
          <button
            onClick={() => navigate('/contacts')}
            className="bg-[#189CD9] hover:bg-sky-600 text-white px-6 py-2.5 rounded-lg font-semibold transition-all duration-300 shadow-lg shadow-sky-500/20 hover:shadow-sky-500/40 hover:scale-105 active:scale-95 focus:outline-none focus:ring-2 focus:ring-sky-400 focus:ring-offset-2 cursor-pointer"
          >
            Отримати розрахунок
          </button>
        </div>

        {/* Mobile Hamburger Button */}
        <button
          onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
          aria-label="Перемикач меню"
          aria-expanded={mobileMenuOpen}
          className="md:hidden text-slate-800 dark:text-slate-100 p-2 focus:outline-none focus:ring-2 focus:ring-sky-500 rounded-lg"
        >
          <span className="material-icons text-3xl">
            {mobileMenuOpen ? 'close' : 'menu'}
          </span>
        </button>
      </div>

      {/* Mobile Dropdown Menu */}
      {mobileMenuOpen && (
        <div className="md:hidden bg-white dark:bg-slate-900 border-b border-slate-200 dark:border-slate-800 px-6 py-6 space-y-4 shadow-xl">
          <nav className="flex flex-col gap-4 font-medium">
            <NavLink to="/" end onClick={closeMenu} className={mobileNavLinkClass}>
              Головна
            </NavLink>
            <NavLink to="/services" onClick={closeMenu} className={mobileNavLinkClass}>
              Послуги
            </NavLink>
            <NavLink to="/about" onClick={closeMenu} className={mobileNavLinkClass}>
              Про компанію
            </NavLink>
            <NavLink to="/contacts" onClick={closeMenu} className={mobileNavLinkClass}>
              Контакти
            </NavLink>
          </nav>
          <div className="pt-3 border-t border-slate-100 dark:border-slate-800 space-y-3">
            <a
              href="tel:+380638767270"
              className="flex items-center gap-2 font-bold text-slate-800 dark:text-white hover:text-[#189CD9] transition-colors"
            >
              <span className="material-icons text-[#189CD9] text-base">call</span>
              +380 63 876 72 70
            </a>
            <a
              href="mailto:sibway@ukr.net"
              className="flex items-center gap-2 text-sm text-slate-600 dark:text-slate-300 hover:text-[#189CD9] transition-colors"
            >
              <span className="material-icons text-[#189CD9] text-base">email</span>
              sibway@ukr.net
            </a>
            <button
              onClick={() => {
                closeMenu();
                navigate('/contacts');
              }}
              className="w-full bg-[#189CD9] hover:bg-sky-600 text-white px-6 py-3 rounded-lg font-semibold transition-all duration-300 shadow-md mt-2 cursor-pointer"
            >
              Отримати розрахунок
            </button>
          </div>
        </div>
      )}
    </header>
  );
};
