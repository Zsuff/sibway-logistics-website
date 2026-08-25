import { Hero } from '../components/Hero';
import { Stats } from '../components/Stats';
import { WhyUs } from '../components/WhyUs';
import { Services } from '../components/Services';
import { BenefitsAndQuoteForm } from '../components/BenefitsAndQuoteForm';
import { CtaBanner } from '../components/CtaBanner';

export const HomePage = () => {
  return (
    <>
      <Hero
        title="Логістичні рішення для вашого бізнесу"
        subtitle="Швидка та надійна доставка вантажів по Україні та Європі"
        ctaPrimary="Розрахувати вартість"
        ctaSecondary="Зв'язатися з нами"
      />
      <Stats
        items={[
          { value: '10+', label: 'років досвіду' },
          { value: '5000+', label: 'довезених вантажів' },
          { value: '98%', label: 'задоволених клієнтів' },
        ]}
      />
      <WhyUs
        title="Чому обирають нас"
        items={[
          { icon: '🚚', title: 'Швидка доставка', description: 'Оптимальні маршрути та терміни' },
          { icon: '🛡️', title: 'Надійність', description: 'Повне страхування вантажів' },
          { icon: '💰', title: 'Вигідні ціни', description: 'Гнучка система знижок' },
        ]}
      />
      <Services
        title="Наші послуги"
        items={[
          { title: 'Автомобільні перевезення', description: 'Доставка вантажів автотранспортом по Україні та Європі' },
          { title: 'Залізничні перевезення', description: 'Економічне рішення для великих обсягів' },
          { title: 'Складські послуги', description: 'Зберігання та обробка вантажів' },
        ]}
      />
      <BenefitsAndQuoteForm
        title="Переваги роботи з нами"
        benefits={[
          { icon: '✓', text: 'Індивідуальний підхід до кожного клієнта' },
          { icon: '✓', text: 'Прозора система розрахунків' },
          { icon: '✓', text: 'Підтримка 24/7' },
        ]}
      />
      <CtaBanner
        title="Готові до співпраці?"
        subtitle="Залиште заявку та отримайте безкоштовну консультацію"
        button="Замовити дзвінок"
      />
    </>
  );
};
