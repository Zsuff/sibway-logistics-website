import { Stats } from '../components/Stats';
import { CtaBanner } from '../components/CtaBanner';

export const AboutPage = () => {
  return (
    <>
      <section className="about-hero">
        <h1>Про компанію Sibway Logistics</h1>
        <p>Ваш надійний партнер у світі логістики</p>
      </section>

      <section className="about-content">
        <div className="about-section">
          <h2>Наша місія</h2>
          <p>
            Забезпечувати швидку, надійну та економічно вигідну доставку вантажів,
            допомагаючи бізнесу розвиватися та виходити на нові ринки.
          </p>
        </div>

        <div className="about-section">
          <h2>Наші цінності</h2>
          <ul className="values-list">
            <li>
              <strong>Надійність</strong> — ми завжди виконуємо свої зобов'язання
            </li>
            <li>
              <strong>Професіоналізм</strong> — команда досвідчених фахівців
            </li>
            <li>
              <strong>Клієнтоорієнтованість</strong> — індивідуальний підхід до кожного
            </li>
            <li>
              <strong>Інновації</strong> — постійне вдосконалення процесів
            </li>
          </ul>
        </div>
      </section>

      <Stats
        items={[
          { value: '10+', label: 'років на ринку' },
          { value: '50+', label: 'міст покриття' },
          { value: '1000+', label: 'задоволених клієнтів' },
        ]}
      />

      <CtaBanner
        title="Долучайтеся до наших клієнтів"
        subtitle="Разом ми зробимо ваш бізнес успішнішим"
        button="Зв'язатися з нами"
      />
    </>
  );
};
