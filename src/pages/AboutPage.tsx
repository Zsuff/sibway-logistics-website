import React from 'react';
import { Link } from 'react-router-dom';
import { Header } from '../components/Header';
import { About } from '../components/About';
import { Stats } from '../components/Stats';
import { WhyUs } from '../components/WhyUs';
import { CtaBanner } from '../components/CtaBanner';
import { Footer } from '../components/Footer';

export const AboutPage: React.FC = () => {
  return (
    <div className="min-h-screen flex flex-col bg-[#F8F9FA] dark:bg-[#0F172A] text-slate-900 dark:text-slate-100">
      <Header />
      <main className="flex-grow pt-28">
        {/* Breadcrumbs */}
        <div className="bg-white dark:bg-slate-900 border-b border-slate-200 dark:border-slate-800 py-4">
          <div className="container mx-auto px-6 flex items-center gap-2 text-sm text-slate-500 dark:text-slate-400">
            <Link to="/" className="hover:text-[#189CD9] transition-colors">
              Головна
            </Link>
            <span className="material-icons text-xs">chevron_right</span>
            <span className="text-slate-900 dark:text-white font-medium">
              Про компанію
            </span>
          </div>
        </div>

        <About />
        <Stats />
        <WhyUs />
        <CtaBanner />
      </main>
      <Footer />
    </div>
  );
};
