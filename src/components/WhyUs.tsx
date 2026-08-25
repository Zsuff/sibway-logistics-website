import type { FC } from 'react';

export interface WhyUsItem {
  icon: string;
  title: string;
  description: string;
}

export interface WhyUsProps {
  title: string;
  items: WhyUsItem[];
}

export const WhyUs: FC<WhyUsProps> = ({ title, items }) => {
  return (
    <section className="why-us">
      <h2 className="section-title">{title}</h2>
      <div className="why-us-grid">
        {items.map((item, index) => (
          <div key={index} className="why-us-card">
            <div className="why-us-icon">{item.icon}</div>
            <h3 className="why-us-card-title">{item.title}</h3>
            <p className="why-us-description">{item.description}</p>
          </div>
        ))}
      </div>
    </section>
  );
};
