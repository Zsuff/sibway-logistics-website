import React from 'react';
import { Link } from 'react-router-dom';

export const CtaBanner: React.FC = () => {
  return (
    <section className="py-24 relative overflow-hidden bg-[#29265B] reveal-init active">
      <div className="container mx-auto px-6 py-12 text-center relative z-10">
        <h2 className="text-4xl lg:text-5xl font-extrabold text-white mb-6">
          Обговоримо ваше перевезення?
        </h2>
        <p className="text-xl text-[#D9DDE3] mb-10 max-w-2xl mx-auto leading-relaxed">
          Залиште заявку на розрахунок або зв'яжіться з нами телефоном чи через месенджери. Ми підберемо оптимальний маршрут і формат перевезення під ваш вантаж, терміни та бюджет.
        </p>
        <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
          <Link
            to="/contacts"
            className="bg-[#189CD9] hover:bg-sky-600 text-white px-10 py-4 rounded-lg font-bold text-xl transition-all duration-300 shadow-lg hover:shadow-sky-500/50 hover:-translate-y-1 active:scale-95 focus:outline-none focus:ring-2 focus:ring-sky-400"
          >
            Отримати розрахунок
          </Link>
          <a
            href="tel:+380638767270"
            className="bg-transparent border-2 border-white/30 text-white hover:bg-white/10 px-8 py-4 rounded-lg font-bold text-xl transition-all duration-300 hover:-translate-y-1 active:scale-95 focus:outline-none focus:ring-2 focus:ring-white/50 flex items-center justify-center gap-2"
          >
            <span className="material-icons text-xl">call</span>
            Зателефонувати
          </a>
        </div>
      </div>
    </section>
  );
};
