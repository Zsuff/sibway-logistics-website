import { FC } from 'react';
import './Services.css';

interface ServiceItem {
  title: string;
  description: string;
}

interface ServicesProps {
  title: string;
  items: ServiceItem[];
}

export const Services: FC<ServicesProps> = ({ title, items }) => {
  return (
    <section className="services">
      <h2 className="section-title">{title}</h2>
      <div className="services-grid">
        {items.map((service, index) => (
          <div key={index} className="service-card">
            <h3 className="service-title">{service.title}</h3>
            <p className="service-description">{service.description}</p>
          </div>
        ))}
      </div>
    </section>
  );
};
