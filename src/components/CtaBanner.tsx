import type { FC } from 'react';

export interface CtaBannerProps {
  title: string;
  subtitle: string;
  button: string;
}

export const CtaBanner: FC<CtaBannerProps> = ({ title, subtitle, button }) => {
  return (
    <section className="cta-banner">
      <div className="cta-content">
        <h2 className="cta-title">{title}</h2>
        <p className="cta-subtitle">{subtitle}</p>
        <button className="btn btn-primary">{button}</button>
      </div>
    </section>
  );
};
