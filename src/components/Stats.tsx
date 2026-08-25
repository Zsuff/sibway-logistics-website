import React from 'react';

export const Stats: React.FC = () => {
  return (
    <section className="bg-white dark:bg-slate-900 py-16 border-y border-slate-100 dark:border-slate-800 reveal-init active">
      <div className="container mx-auto px-6">
        <div className="grid grid-cols-2 lg:grid-cols-4 gap-8">
          <div className="text-center p-6 rounded-2xl bg-slate-50 dark:bg-slate-800/50 transition-all duration-300 hover:-translate-y-2 hover:shadow-lg border border-slate-100 dark:border-slate-800">
            <div className="text-4xl lg:text-5xl font-extrabold text-[#29265B] dark:text-white mb-2">
              7+
            </div>
            <div className="text-slate-500 dark:text-slate-400 font-medium">
              років на ринку
            </div>
          </div>

          <div className="text-center p-6 rounded-2xl bg-slate-50 dark:bg-slate-800/50 transition-all duration-300 hover:-translate-y-2 hover:shadow-lg border border-slate-100 dark:border-slate-800">
            <div className="text-4xl lg:text-5xl font-extrabold text-[#189CD9] mb-2">
              7500+
            </div>
            <div className="text-slate-500 dark:text-slate-400 font-medium">
              виконаних перевезень
            </div>
          </div>

          <div className="text-center p-6 rounded-2xl bg-slate-50 dark:bg-slate-800/50 transition-all duration-300 hover:-translate-y-2 hover:shadow-lg border border-slate-100 dark:border-slate-800">
            <div className="text-4xl lg:text-5xl font-extrabold text-[#29265B] dark:text-white mb-2">
              4000+
            </div>
            <div className="text-slate-500 dark:text-slate-400 font-medium">
              клієнтів
            </div>
          </div>

          <div className="text-center p-6 rounded-2xl bg-slate-50 dark:bg-slate-800/50 transition-all duration-300 hover:-translate-y-2 hover:shadow-lg border border-slate-100 dark:border-slate-800">
            <div className="text-4xl lg:text-5xl font-extrabold text-[#189CD9] mb-2">
              40+
            </div>
            <div className="text-slate-500 dark:text-slate-400 font-medium">
              країн Європи
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};
