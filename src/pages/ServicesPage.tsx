import React from 'react';
import { Link } from 'react-router-dom';
import { Header } from '../components/Header';
import { CtaBanner } from '../components/CtaBanner';
import { Footer } from '../components/Footer';
import heroTruckImg from '../assets/hero-truck.webp';

export const ServicesPage: React.FC = () => {
  const servicesCards = [
    {
      icon: 'local_shipping',
      title: 'Міжнародні вантажні перевезення',
      description:
        'LTL та FTL перевезення між Україною та Європою для палетних, непалетних, небезпечних і температурних вантажів',
      link: '/services/transport',
    },
    {
      icon: 'gavel',
      title: 'Митне оформлення',
      description:
        'Супровід документів, консультації з митних питань, допомога в оформленні вантажів на кордоні',
      link: '/contacts',
    },
    {
      icon: 'warehouse',
      title: 'Складські послуги',
      description:
        'Індивідуальні рішення для складних вантажів, консолідація, складське зберігання, страхування',
      link: '/contacts',
    },
    {
      icon: 'insights',
      title: 'Логістичний аудит',
      description:
        'Аналіз вашої логістики, оптимізація маршрутів і витрат, рекомендації щодо покращення процесів',
      link: '/contacts',
    },
  ];

  return (
    <div className="min-h-screen flex flex-col bg-[#F8F9FA] dark:bg-[#0F172A] text-slate-900 dark:text-slate-100">
      <Header />
      <main className="flex-grow">
        {/* Services Hero Section */}
        <section className="relative pt-32 pb-20 lg:pt-48 lg:pb-32 overflow-hidden bg-white dark:bg-slate-900 reveal-init active">
          <div className="container mx-auto px-6 grid lg:grid-cols-2 gap-12 items-center relative z-10">
            <div className="max-w-2xl">
              <h1 className="text-4xl lg:text-6xl font-extrabold text-[#29265B] dark:text-white mb-6 leading-[1.1]">
                Наші послуги
              </h1>
              <p className="text-lg text-slate-600 dark:text-slate-400 mb-10 leading-relaxed max-w-xl">
                Комплексні логістичні рішення для вашого бізнесу — від міжнародних перевезень до митного оформлення
              </p>
              <div className="flex flex-col sm:flex-row gap-4">
                <Link
                  to="/contacts"
                  className="bg-[#189CD9] hover:bg-sky-600 text-white px-8 py-4 rounded-lg font-bold text-lg text-center transition-all duration-300 shadow-xl shadow-sky-500/30 hover:shadow-sky-500/50 hover:-translate-y-1 active:scale-95 focus:outline-none focus:ring-2 focus:ring-sky-400"
                >
                  Отримати розрахунок
                </Link>
                <a
                  href="tel:+380638767270"
                  className="bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 text-slate-800 dark:text-slate-200 text-center hover:bg-slate-50 dark:hover:bg-slate-700 px-8 py-4 rounded-lg font-bold text-lg transition-all duration-300 hover:-translate-y-1 hover:shadow-lg active:scale-95 focus:outline-none focus:ring-2 focus:ring-slate-400 flex items-center justify-center gap-2"
                >
                  <span className="material-icons text-xl text-[#189CD9]">call</span>
                  Зателефонувати
                </a>
              </div>
            </div>
            <div className="relative lg:pl-10">
              <div className="rounded-3xl overflow-hidden shadow-2xl relative image-overlay group animate-float">
                <img
                  src={heroTruckImg}
                  alt="Сучасна вантажівка Sibway Logistics"
                  className="w-full h-full object-cover aspect-[4/3] transition-transform duration-700 group-hover:scale-105"
                />
              </div>
            </div>
          </div>
        </section>

        {/* Services Cards Section (2x2 Desktop Grid) */}
        <section className="py-24 bg-slate-50 dark:bg-slate-900/50 reveal-init active" id="services-list">
          <div className="container mx-auto px-6 text-center mb-16">
            <h2 className="text-3xl lg:text-4xl font-extrabold text-[#29265B] dark:text-white mb-4">
              Які послуги ми надаємо
            </h2>
            <div className="w-20 h-1.5 bg-[#189CD9] mx-auto rounded-full"></div>
          </div>

          <div className="container mx-auto px-6 max-w-6xl">
            <div className="grid md:grid-cols-2 lg:grid-cols-2 gap-8">
              {servicesCards.map((service, index) => (
                <div
                  key={index}
                  className="bg-white dark:bg-slate-800 p-8 rounded-2xl shadow-sm hover:shadow-xl transition-all duration-300 hover:-translate-y-2 border border-slate-100 dark:border-slate-700 group flex flex-col justify-between"
                >
                  <div>
                    <div className="w-14 h-14 bg-sky-50 dark:bg-sky-900/20 text-[#189CD9] rounded-xl flex items-center justify-center mb-6 group-hover:scale-110 group-hover:bg-[#189CD9] group-hover:text-white transition-all duration-300">
                      <span className="material-icons text-3xl">{service.icon}</span>
                    </div>
                    <h3 className="text-2xl font-bold mb-4 text-slate-900 dark:text-white group-hover:text-[#189CD9] transition-colors">
                      {service.title}
                    </h3>
                    <p className="text-slate-600 dark:text-slate-400 text-base mb-6 leading-relaxed">
                      {service.description}
                    </p>
                  </div>
                  <div>
                    <Link
                      to={service.link}
                      className="text-[#189CD9] font-bold inline-flex items-center gap-2 hover:gap-3 transition-all focus:outline-none focus:ring-2 focus:ring-sky-400 rounded-md p-1"
                    >
                      Детальніше <span className="material-icons text-sm">arrow_forward</span>
                    </Link>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </section>

        {/* Shared CTA Banner */}
        <CtaBanner />
      </main>
      <Footer />
    </div>
  );
};
