import React from 'react';
import { Link } from 'react-router-dom';
import { Header } from '../components/Header';
import { BenefitsAndQuoteForm } from '../components/BenefitsAndQuoteForm';
import { CtaBanner } from '../components/CtaBanner';
import { Footer } from '../components/Footer';
import heroTruckImg from '../assets/hero-truck.webp';

export const TransportPage: React.FC = () => {
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
            <Link to="/services" className="hover:text-[#189CD9] transition-colors">
              Послуги
            </Link>
            <span className="material-icons text-xs">chevron_right</span>
            <span className="text-slate-900 dark:text-white font-medium">
              Міжнародні вантажні перевезення
            </span>
          </div>
        </div>

        {/* Detail Hero Section */}
        <section className="py-16 bg-white dark:bg-slate-900 reveal-init active">
          <div className="container mx-auto px-6 grid lg:grid-cols-2 gap-12 items-center">
            <div>
              <span className="inline-block bg-sky-50 dark:bg-sky-950/60 text-[#189CD9] px-4 py-1.5 rounded-full text-sm font-semibold mb-6 border border-[#189CD9]/20">
                Послуга №1
              </span>
              <h1 className="text-3xl lg:text-5xl font-extrabold text-[#29265B] dark:text-white mb-6 leading-tight">
                Міжнародні вантажні перевезення (LTL & FTL)
              </h1>
              <p className="text-slate-600 dark:text-slate-400 text-lg leading-relaxed mb-8">
                Організовуємо доставку вантажів будь-якої складності між Україною та 40+ країнами Європи. Забезпечуємо повне завантаження (FTL) та збірні вантажі (LTL).
              </p>
              <div className="flex flex-col sm:flex-row gap-4">
                <Link
                  to="/contacts"
                  className="bg-[#189CD9] hover:bg-sky-600 text-white px-8 py-4 rounded-lg font-bold text-lg text-center transition-all shadow-lg"
                >
                  Розрахувати вартість
                </Link>
                <a
                  href="tel:+380638767270"
                  className="bg-slate-100 dark:bg-slate-800 text-slate-800 dark:text-slate-200 px-8 py-4 rounded-lg font-bold text-lg text-center hover:bg-slate-200 dark:hover:bg-slate-700 transition-colors flex items-center justify-center gap-2"
                >
                  <span className="material-icons text-[#189CD9]">call</span>
                  Зателефонувати
                </a>
              </div>
            </div>
            <div>
              <div className="rounded-2xl overflow-hidden shadow-xl">
                <img
                  src={heroTruckImg}
                  alt="Вантажні перевезення Sibway Logistics"
                  className="w-full h-auto object-cover"
                />
              </div>
            </div>
          </div>
        </section>

        {/* Form section */}
        <BenefitsAndQuoteForm selectedService="Міжнародні автоперевезення" />

        {/* CTA */}
        <CtaBanner />
      </main>
      <Footer />
    </div>
  );
};
