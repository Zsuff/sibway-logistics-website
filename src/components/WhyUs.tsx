import React from 'react';

export const WhyUs: React.FC = () => {
  const reasons = [
    {
      icon: 'schedule',
      title: 'Дотримання термінів',
      description: 'Організовуємо доставку відповідно до погодженого графіка.',
    },
    {
      icon: 'payments',
      title: 'Прозорі тарифи',
      description: 'Заздалегідь узгоджуємо вартість і склад послуг.',
    },
    {
      icon: 'person_pin',
      title: 'Персональний менеджер',
      description: 'Менеджер супроводжує ваше перевезення на всіх етапах.',
    },
    {
      icon: 'location_on',
      title: 'Контроль перевезення',
      description: 'Відстежуємо процес доставки та інформуємо про статус вантажу.',
    },
    {
      icon: 'handshake',
      title: 'Надійні партнери',
      description: 'Працюємо з перевіреними перевізниками та підрядниками.',
    },
  ];

  return (
    <section className="py-24 relative overflow-hidden bg-slate-50 dark:bg-slate-900 reveal-init active">
      <div className="container mx-auto px-6 relative z-10">
        <h2 className="text-3xl lg:text-4xl font-extrabold text-[#29265B] dark:text-white mb-16 text-center">
          Чому обирають Sibway
        </h2>
        <div className="grid md:grid-cols-3 lg:grid-cols-5 gap-10">
          {reasons.map((reason, index) => (
            <div key={index} className="flex flex-col items-center text-center group">
              <div className="text-[#189CD9] mb-6 transition-transform duration-300 group-hover:-translate-y-2 group-hover:scale-110">
                <span className="material-icons text-5xl">{reason.icon}</span>
              </div>
              <h3 className="font-bold mb-2 text-slate-900 dark:text-white text-base">
                {reason.title}
              </h3>
              <p className="text-sm text-slate-500 dark:text-slate-400">
                {reason.description}
              </p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};
