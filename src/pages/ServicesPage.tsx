import { Services } from '../components/Services';
import { CtaBanner } from '../components/CtaBanner';

export const ServicesPage = () => {
  return (
    <>
      <section className="services-hero">
        <h1>Наші послуги</h1>
        <p>Комплексні логістичні рішення для вашого бізнесу</p>
      </section>

      <Services
        title="Що ми пропонуємо"
        items={[
          { title: 'Автомобільні перевезення', description: 'Швидка та надійна доставка вантажів автотранспортом' },
          { title: 'Залізничні перевезення', description: 'Економічне рішення для великих обсягів вантажів' },
          { title: 'Складські послуги', description: 'Зберігання, обробка та комплектація вантажів' },
          { title: 'Міжнародні перевезення', description: 'Доставка вантажів по всій Європі' },
        ]}
      />

      <CtaBanner
        title="Потрібна допомога з вибором послуги?"
        subtitle="Наші фахівці допоможуть підібрати оптимальне рішення"
        button="Зв'язатися з нами"
      />
    </>
  );
};
