import React from 'react';
import { Link } from 'react-router-dom';
import { Header } from '../components/Header';
import { BenefitsAndQuoteForm } from '../components/BenefitsAndQuoteForm';
import { CtaBanner } from '../components/CtaBanner';
import { Footer } from '../components/Footer';

export const ContactsPage: React.FC = () => {
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
              Контакти
            </span>
          </div>
        </div>

        {/* Contact Info Header */}
        <section className="py-16 bg-white dark:bg-slate-900 reveal-init active">
          <div className="container mx-auto px-6 text-center max-w-3xl">
            <h1 className="text-4xl lg:text-5xl font-extrabold text-[#29265B] dark:text-white mb-6">
              Зв’яжіться з нами
            </h1>
            <p className="text-lg text-slate-600 dark:text-slate-400 leading-relaxed mb-12">
              Ми завжди на зв’язку, щоб відповісти на ваші запитання та розрахувати вартість перевезення
            </p>

            <div className="grid md:grid-cols-3 gap-6 text-left">
              <div className="p-6 bg-slate-50 dark:bg-slate-800/60 rounded-2xl border border-slate-200 dark:border-slate-700">
                <div className="w-12 h-12 bg-sky-50 dark:bg-sky-900/30 text-[#189CD9] rounded-xl flex items-center justify-center mb-4">
                  <span className="material-icons text-2xl">location_on</span>
                </div>
                <h3 className="font-bold text-slate-900 dark:text-white text-lg mb-2">Адреса</h3>
                <p className="text-slate-600 dark:text-slate-400 text-sm leading-relaxed">
                  Україна, 33028, м. Рівне, вулиця Литовська 75
                </p>
              </div>

              <div className="p-6 bg-slate-50 dark:bg-slate-800/60 rounded-2xl border border-slate-200 dark:border-slate-700">
                <div className="w-12 h-12 bg-sky-50 dark:bg-sky-900/30 text-[#189CD9] rounded-xl flex items-center justify-center mb-4">
                  <span className="material-icons text-2xl">call</span>
                </div>
                <h3 className="font-bold text-slate-900 dark:text-white text-lg mb-2">Телефон</h3>
                <a
                  href="tel:+380638767270"
                  className="text-[#189CD9] font-semibold hover:underline text-base block"
                >
                  +380 63 876 72 70
                </a>
              </div>

              <div className="p-6 bg-slate-50 dark:bg-slate-800/60 rounded-2xl border border-slate-200 dark:border-slate-700">
                <div className="w-12 h-12 bg-sky-50 dark:bg-sky-900/30 text-[#189CD9] rounded-xl flex items-center justify-center mb-4">
                  <span className="material-icons text-2xl">email</span>
                </div>
                <h3 className="font-bold text-slate-900 dark:text-white text-lg mb-2">Email</h3>
                <a
                  href="mailto:sibway@ukr.net"
                  className="text-[#189CD9] font-semibold hover:underline text-base block"
                >
                  sibway@ukr.net
                </a>
              </div>
            </div>
          </div>
        </section>

        {/* Benefits & Quote Form */}
        <BenefitsAndQuoteForm />

        {/* Shared CTA Banner */}
        <CtaBanner />
      </main>
      <Footer />
    </div>
  );
};
