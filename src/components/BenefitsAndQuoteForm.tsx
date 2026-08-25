import type { FC } from 'react';
import { useState } from 'react';

export interface Benefit {
  icon: string;
  text: string;
}

export interface BenefitsAndQuoteFormProps {
  title: string;
  benefits: Benefit[];
}

export const BenefitsAndQuoteForm: FC<BenefitsAndQuoteFormProps> = ({ title, benefits }) => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    phone: '',
    message: '',
  });

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    console.log('Form submitted:', formData);
  };

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  return (
    <section className="benefits-and-quote">
      <div className="benefits-section">
        <h2 className="section-title">{title}</h2>
        <div className="benefits-grid">
          {benefits.map((benefit, index) => (
            <div key={index} className="benefit-item">
              <div className="benefit-icon">{benefit.icon}</div>
              <p className="benefit-text">{benefit.text}</p>
            </div>
          ))}
        </div>
      </div>

      <div className="quote-form-section">
        <form className="quote-form" onSubmit={handleSubmit}>
          <h3 className="form-title">Отримати консультацію</h3>
          <input
            type="text"
            name="name"
            placeholder="Ваше ім'я"
            value={formData.name}
            onChange={handleChange}
            className="form-input"
          />
          <input
            type="email"
            name="email"
            placeholder="Email"
            value={formData.email}
            onChange={handleChange}
            className="form-input"
          />
          <input
            type="tel"
            name="phone"
            placeholder="Телефон"
            value={formData.phone}
            onChange={handleChange}
            className="form-input"
          />
          <textarea
            name="message"
            placeholder="Повідомлення"
            value={formData.message}
            onChange={handleChange}
            className="form-textarea"
          />
          <button type="submit" className="btn btn-primary">
            Відправити
          </button>
        </form>
      </div>
    </section>
  );
};
