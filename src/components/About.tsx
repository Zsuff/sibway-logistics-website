import React from 'react';
import aboutWarehouseImg from '../assets/about-warehouse.webp';

export const About: React.FC = () => {
  return (
    <section className="py-24 overflow-hidden bg-white dark:bg-slate-900 reveal-init active" id="about">
      <div className="container mx-auto px-6 grid lg:grid-cols-2 gap-20 items-center">
        <div className="relative order-2 lg:order-1 image-overlay group animate-float">
          <img
            src={aboutWarehouseImg}
            alt="Логістичний склад"
            className="rounded-xl shadow-lg relative z-10 w-full transition-transform duration-700 group-hover:scale-105"
          />
        </div>
        <div className="order-1 lg:order-2">
          <h2 className="text-3xl lg:text-4xl font-extrabold text-[#29265B] dark:text-white mb-8">
            Sibway Logistics — ваш надійний логістичний партнер
          </h2>
          <div className="space-y-6 text-lg text-slate-600 dark:text-slate-400 leading-relaxed">
            <p className="text-slate-600 dark:text-slate-400 text-base leading-relaxed">
              Ми організовуємо міжнародні вантажні перевезення між Україною та країнами Європи. Підбираємо маршрут, формат доставки та тип транспорту відповідно до специфіки вантажу, термінів і бюджету.
            </p>
            <p className="text-slate-600 dark:text-slate-400 text-base leading-relaxed">
              Наш менеджер супроводжує перевезення на всіх етапах — від першого запиту до доставки вантажу.
            </p>
          </div>
        </div>
      </div>
    </section>
  );
};
