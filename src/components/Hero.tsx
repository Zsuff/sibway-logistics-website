import React from 'react';
import { Link } from 'react-router-dom';
import heroTruckImg from '../assets/hero-truck.webp';

export const Hero: React.FC = () => {
  return (
    <section className="relative pt-32 pb-20 lg:pt-48 lg:pb-32 overflow-hidden bg-white dark:bg-slate-900 reveal-init active">
      <div className="container mx-auto px-6 grid lg:grid-cols-2 gap-12 items-center relative z-10">
        <div className="max-w-2xl">
          <h1 className="text-4xl lg:text-6xl font-extrabold text-[#29265B] dark:text-white mb-6 leading-[1.1]">
            Міжнародні вантажні перевезення між{' '}
            <span className="text-[#189CD9]">Україною та Європою</span>
          </h1>
          <p className="text-lg text-slate-600 dark:text-slate-400 mb-10 leading-relaxed max-w-xl">
            Організовуємо доставку вантажів для бізнесу — від 1 палети до повного завантаження. Підберемо маршрут і формат перевезення відповідно до вашого вантажу, термінів і бюджету
          </p>
          <div className="flex flex-col sm:flex-row gap-4">
            <Link
              to="/contacts"
              className="bg-[#189CD9] hover:bg-sky-600 text-white px-8 py-4 rounded-lg font-bold text-lg text-center transition-all duration-300 shadow-xl shadow-sky-500/30 hover:shadow-sky-500/50 hover:-translate-y-1 active:scale-95 focus:outline-none focus:ring-2 focus:ring-sky-400"
            >
              Отримати розрахунок
            </Link>
            <Link
              to="/services"
              className="bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 text-slate-800 dark:text-slate-200 text-center hover:bg-slate-50 dark:hover:bg-slate-700 px-8 py-4 rounded-lg font-bold text-lg transition-all duration-300 hover:-translate-y-1 hover:shadow-lg active:scale-95 focus:outline-none focus:ring-2 focus:ring-slate-400"
            >
              Детальніше про послуги
            </Link>
          </div>
        </div>
        <div className="relative lg:pl-10">
          <div className="rounded-3xl overflow-hidden shadow-2xl relative image-overlay group animate-float">
            <img
              src={heroTruckImg}
              alt="Сучасна вантажівка на європейській магістралі"
              className="w-full h-full object-cover aspect-[4/3] transition-transform duration-700 group-hover:scale-105"
            />
          </div>
        </div>
      </div>
    </section>
  );
};
