import React from 'react';
import { Link } from 'react-router-dom';

export const Services: React.FC = () => {
  const servicesList = [
    {
      icon: 'local_shipping',
      title: 'Міжнародні вантажні перевезення',
      description:
        'Організовуємо доставку вантажів між Україною та країнами Європи — від однієї палети до повного завантаження.',
      link: '/services/transport',
    },
    {
      icon: 'gavel',
      title: 'Митно-брокерські послуги',
      description:
        'Супроводжуємо документи та митні процедури для міжнародних перевезень.',
      link: '/services',
    },
    {
      icon: 'warehouse',
      title: 'Складські послуги',
      description:
        'Зберігання, консолідація та обробка вантажів на складських майданчиках.',
      link: '/services',
    },
    {
      icon: 'insights',
      title: 'Логістичний аудит',
      description:
        'Аналізуємо та оптимізуємо логістичні процеси для вашого бізнесу.',
      link: '/services',
    },
  ];

  return (
    <section className="py-24 bg-slate-50 dark:bg-slate-900/50 reveal-init active" id="services">
      <div className="container mx-auto px-6 text-center mb-16">
        <h2 className="text-3xl lg:text-4xl font-extrabold text-[#29265B] dark:text-white mb-4">
          Які послуги ми надаємо
        </h2>
        <div className="w-20 h-1.5 bg-[#189CD9] mx-auto rounded-full"></div>
      </div>
      <div className="container mx-auto px-6 grid md:grid-cols-2 lg:grid-cols-4 gap-8">
        {servicesList.map((service, index) => (
          <div
            key={index}
            className="bg-white dark:bg-slate-800 p-8 rounded-2xl shadow-sm hover:shadow-xl transition-all duration-300 hover:-translate-y-2 border border-slate-100 dark:border-slate-700 group flex flex-col justify-between"
          >
            <div>
              <div className="w-14 h-14 bg-sky-50 dark:bg-sky-900/20 text-[#189CD9] rounded-xl flex items-center justify-center mb-6 group-hover:scale-110 group-hover:bg-[#189CD9] group-hover:text-white transition-all duration-300">
                <span className="material-icons text-3xl">{service.icon}</span>
              </div>
              <h3 className="text-xl font-bold mb-4 text-slate-900 dark:text-white group-hover:text-[#189CD9] transition-colors">
                {service.title}
              </h3>
              <p className="text-slate-500 dark:text-slate-400 text-sm mb-6 leading-relaxed">
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
    </section>
  );
};
