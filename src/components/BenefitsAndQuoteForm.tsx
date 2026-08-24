import React, { useState } from 'react';

interface BenefitsAndQuoteFormProps {
  selectedService?: string;
}

export const BenefitsAndQuoteForm: React.FC<BenefitsAndQuoteFormProps> = ({
  selectedService,
}) => {
  const [formData, setFormData] = useState({
    name: '',
    phone: '',
    service: selectedService || 'Міжнародні автоперевезення',
    details: '',
  });

  const [errors, setErrors] = useState<{ name?: string; phone?: string }>({});
  const [submitted, setSubmitted] = useState(false);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [serverError, setServerError] = useState<string | null>(null);

  // Update selected service if passed from outside
  React.useEffect(() => {
    if (selectedService) {
      setFormData((prev) => ({ ...prev, service: selectedService }));
    }
  }, [selectedService]);

  const handleChange = (
    e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement | HTMLTextAreaElement>
  ) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
    if (errors[name as keyof typeof errors]) {
      setErrors((prev) => ({ ...prev, [name]: undefined }));
    }
    if (serverError) {
      setServerError(null);
    }
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setServerError(null);
    const newErrors: { name?: string; phone?: string } = {};

    if (!formData.name.trim()) {
      newErrors.name = 'Будь ласка, вкажіть ваше ім’я';
    }

    if (!formData.phone.trim()) {
      newErrors.phone = 'Будь ласка, вкажіть ваш номер телефону';
    } else if (!/^[+\d\s()-]{7,20}$/.test(formData.phone.trim())) {
      newErrors.phone = 'Введіть коректний номер телефону (наприклад: +380...)';
    }

    if (Object.keys(newErrors).length > 0) {
      setErrors(newErrors);
      return;
    }

    setIsSubmitting(true);

    try {
      const response = await fetch('https://formspree.io/f/mdenbzro', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json',
        },
        body: JSON.stringify({
          'Ім’я': formData.name,
          'Телефон': formData.phone,
          'Тип послуги': formData.service,
          'Коротко про вантаж': formData.details,
        }),
      });

      if (response.ok) {
        setSubmitted(true);
      } else {
        setServerError(
          'Виникла помилка при відправці заявки. Будь ласка, спробуйте ще раз або зателефонуйте нам.'
        );
      }
    } catch {
      setServerError(
        'Виникла помилка при відправці заявки. Будь ласка, перевірте інтернет-з’єднання та спробуйте ще раз.'
      );
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <section className="py-24 bg-white dark:bg-slate-900 border-t border-slate-100 dark:border-slate-800 reveal-init active" id="quote-form">
      <div className="container mx-auto px-6">
        <div className="dark:bg-slate-800 rounded-[32px] p-8 lg:p-16 flex flex-col lg:flex-row gap-16 items-center border border-slate-200 dark:border-slate-700 bg-white shadow-xl hover:shadow-2xl transition-shadow duration-300">
          {/* Left Column: Benefits & Info */}
          <div className="lg:w-1/2">
            <h2 className="text-3xl lg:text-4xl font-extrabold text-[#29265B] dark:text-white mb-6">
              Що ви отримаєте
            </h2>
            <p className="text-lg text-slate-600 dark:text-slate-400 mb-8">
              Наші спеціалісти проаналізують ваш запит та запропонують оптимальний варіант доставки вашого вантажу.
            </p>
            <ul className="space-y-4 mb-8">
              <li className="flex items-start gap-3 text-slate-700 dark:text-slate-300 transform transition-transform hover:translate-x-2">
                <span className="material-icons text-[#189CD9]">check_circle</span>
                <span>Попередню оцінку маршруту та формату перевезення</span>
              </li>
              <li className="flex items-start gap-3 text-slate-700 dark:text-slate-300 transform transition-transform hover:translate-x-2">
                <span className="material-icons text-[#189CD9]">check_circle</span>
                <span>Підбір рішення відповідно до типу вантажу</span>
              </li>
              <li className="flex items-start gap-3 text-slate-700 dark:text-slate-300 transform transition-transform hover:translate-x-2">
                <span className="material-icons text-[#189CD9]">check_circle</span>
                <span>Консультацію менеджера щодо наступних кроків</span>
              </li>
            </ul>
            <a
              href="tel:+380638767270"
              className="flex items-center gap-4 text-[#29265B] dark:text-white font-bold group cursor-pointer hover:text-[#189CD9] transition-colors focus:outline-none focus:ring-2 focus:ring-sky-500 rounded-md p-1"
            >
              <span className="material-icons text-[#189CD9] transition-transform group-hover:scale-110 group-hover:rotate-12">
                call
              </span>
              <span className="group-hover:text-[#189CD9] transition-colors">
                +380 63 876 72 70
              </span>
            </a>
          </div>

          {/* Right Column: Form */}
          <div className="lg:w-1/2 w-full">
            {submitted ? (
              <div className="bg-sky-50 dark:bg-sky-950/50 border border-[#189CD9]/30 rounded-2xl p-8 text-center space-y-4">
                <div className="w-16 h-16 bg-[#189CD9] text-white rounded-full flex items-center justify-center mx-auto text-3xl shadow-lg">
                  <span className="material-icons text-3xl">check</span>
                </div>
                <h3 className="text-2xl font-bold text-[#29265B] dark:text-white">
                  Заявку успішно відправлено!
                </h3>
                <p className="text-slate-600 dark:text-slate-300">
                  Дякуємо! Наш менеджер зв’яжеться з вами найближчим часом для уточнення деталей.
                </p>
                <button
                  onClick={() => {
                    setSubmitted(false);
                    setFormData({
                      name: '',
                      phone: '',
                      service: 'Міжнародні автоперевезення',
                      details: '',
                    });
                  }}
                  className="mt-4 inline-block bg-[#189CD9] text-white px-6 py-2.5 rounded-lg font-semibold hover:bg-sky-600 transition-colors"
                >
                  Надіслати ще один запит
                </button>
              </div>
            ) : (
              <form onSubmit={handleSubmit} className="space-y-4" noValidate>
                <div className="grid sm:grid-cols-2 gap-4">
                  <div>
                    <label className="block text-sm font-bold text-slate-700 dark:text-slate-300 mb-2">
                      Ім’я <span className="text-red-500">*</span>
                    </label>
                    <input
                      type="text"
                      name="name"
                      value={formData.name}
                      onChange={handleChange}
                      placeholder="Ваше ім’я"
                      aria-invalid={!!errors.name}
                      className={`w-full rounded-xl border ${
                        errors.name ? 'border-red-500 focus:ring-red-500' : 'border-slate-200 dark:border-slate-600'
                      } bg-white dark:bg-slate-900 focus:ring-2 focus:ring-[#189CD9] focus:border-[#189CD9] px-4 py-3 transition-colors text-slate-900 dark:text-white`}
                    />
                    {errors.name && (
                      <p className="text-red-500 text-xs mt-1 font-medium">{errors.name}</p>
                    )}
                  </div>
                  <div>
                    <label className="block text-sm font-bold text-slate-700 dark:text-slate-300 mb-2">
                      Телефон <span className="text-red-500">*</span>
                    </label>
                    <input
                      type="tel"
                      name="phone"
                      value={formData.phone}
                      onChange={handleChange}
                      placeholder="+380..."
                      aria-invalid={!!errors.phone}
                      className={`w-full rounded-xl border ${
                        errors.phone ? 'border-red-500 focus:ring-red-500' : 'border-slate-200 dark:border-slate-600'
                      } bg-white dark:bg-slate-900 focus:ring-2 focus:ring-[#189CD9] focus:border-[#189CD9] px-4 py-3 transition-colors text-slate-900 dark:text-white`}
                    />
                    {errors.phone && (
                      <p className="text-red-500 text-xs mt-1 font-medium">{errors.phone}</p>
                    )}
                  </div>
                </div>
                <div>
                  <label className="block text-sm font-bold text-slate-700 dark:text-slate-300 mb-2">
                    Тип послуги
                  </label>
                  <select
                    name="service"
                    value={formData.service}
                    onChange={handleChange}
                    className="w-full rounded-xl border border-slate-200 dark:border-slate-600 bg-white dark:bg-slate-900 focus:ring-2 focus:ring-[#189CD9] focus:border-[#189CD9] px-4 py-3 transition-colors text-slate-900 dark:text-white"
                  >
                    <option value="Міжнародні автоперевезення">Міжнародні автоперевезення</option>
                    <option value="Митно-брокерські послуги">Митно-брокерські послуги</option>
                    <option value="Складські послуги">Складські послуги</option>
                    <option value="Логістичний аудит">Логістичний аудит</option>
                  </select>
                </div>
                <div>
                  <label className="block text-sm font-bold text-slate-700 dark:text-slate-300 mb-2">
                    Коротко про вантаж
                  </label>
                  <textarea
                    name="details"
                    rows={3}
                    value={formData.details}
                    onChange={handleChange}
                    placeholder="Габарити, вага, напрямок..."
                    className="w-full rounded-xl border border-slate-200 dark:border-slate-600 bg-white dark:bg-slate-900 focus:ring-2 focus:ring-[#189CD9] focus:border-[#189CD9] px-4 py-3 transition-colors text-slate-900 dark:text-white"
                  />
                </div>

                {serverError && (
                  <div className="p-3 bg-red-50 dark:bg-red-950/40 border border-red-200 dark:border-red-800 rounded-xl text-red-600 dark:text-red-400 text-sm font-medium">
                    {serverError}
                  </div>
                )}

                <button
                  type="submit"
                  disabled={isSubmitting}
                  className="w-full bg-[#189CD9] hover:bg-sky-600 disabled:bg-sky-400 text-white font-bold py-4 rounded-xl shadow-lg shadow-sky-500/30 hover:shadow-sky-500/50 hover:-translate-y-1 active:scale-95 transition-all text-lg focus:outline-none focus:ring-2 focus:ring-sky-400 flex items-center justify-center gap-2 cursor-pointer disabled:cursor-not-allowed"
                >
                  {isSubmitting ? (
                    <>
                      <span className="material-icons animate-spin text-xl">progress_activity</span>
                      <span>Надсилання...</span>
                    </>
                  ) : (
                    'Надіслати заявку'
                  )}
                </button>
              </form>
            )}
          </div>
        </div>
      </div>
    </section>
  );
};
