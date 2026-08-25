import type { FC } from 'react';
import './About.css';

export const About: FC = () => {
  return (
    <section className="about">
      <div className="about-content">
        <h2>Про компанію</h2>
        <p>
          Sibway Logistics — ваш надійний партнер у світі логістики.
          Ми забезпечуємо швидку та надійну доставку вантажів по Україні та Європі.
        </p>
      </div>
    </section>
  );
};
