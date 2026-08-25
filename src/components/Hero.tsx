import { FC } from 'react';
import './Hero.css';

export interface HeroProps {
  title: string;
  subtitle: string;
  ctaPrimary: string;
  ctaSecondary: string;
}

export const Hero: FC<HeroProps> = ({ title, subtitle, ctaPrimary, ctaSecondary }) => {
  return (
    <section className="hero">
      <div className="hero-content">
        <h1 className="hero-title">{title}</h1>
        <p className="hero-subtitle">{subtitle}</p>
        <div className="hero-cta">
          <button className="btn btn-primary">{ctaPrimary}</button>
          <button className="btn btn-secondary">{ctaSecondary}</button>
        </div>
      </div>
    </section>
  );
};
