import { Services } from '../components/Services';
import { CtaBanner } from '../components/CtaBanner';

export const TransportPage = () => {
  return (
    <>
      <section className="transport-hero">
        <h1>Транспортні послуги</h1>
        <p>Надійні перевезення для вашого бізнесу</p>
      </section>

      <Services
        title="Наші транспортні послуги"
        items={[
          { title: 'Вантажні перевезення', description: 'Перевезення вантажів будь-якої складності' },
          { title: 'Контейнерні перевезення', description: 'Доставка вантажів у контейнерах' },
          { title: 'Негабаритні перевезення', description: 'Транспортування великогабаритних вантажів' },
        ]}
      />

      <CtaBanner
        title="Потрібен розрахунок вартості?"
        subtitle="Залиште заявку та отримайте безкоштовну консультацію"
        button="Замовити розрахунок"
      />
    </>
  );
};
