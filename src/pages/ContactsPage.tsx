import { CtaBanner } from '../components/CtaBanner';

export const ContactsPage = () => {
  return (
    <>
      <section className="contacts-hero">
        <h1>Контакти</h1>
        <p>Зв'яжіться з нами для консультації або розрахунку вартості перевезення</p>
      </section>

      <section className="contacts-content">
        <div className="contact-info">
          <h2>Наші контакти</h2>
          <div className="contact-item">
            <strong>Адреса:</strong>
            <p>м. Київ, вул. Логістична, 1</p>
          </div>
          <div className="contact-item">
            <strong>Телефон:</strong>
            <p>+38 (0XX) XXX-XX-XX</p>
          </div>
          <div className="contact-item">
            <strong>Email:</strong>
            <p>info@sibway.com.ua</p>
          </div>
          <div className="contact-item">
            <strong>Графік роботи:</strong>
            <p>Пн-Пт: 9:00 - 18:00</p>
          </div>
        </div>

        <div className="contact-form">
          <h2>Напишіть нам</h2>
          <form>
            <input type="text" placeholder="Ваше ім'я" className="form-input" />
            <input type="email" placeholder="Email" className="form-input" />
            <input type="tel" placeholder="Телефон" className="form-input" />
            <textarea placeholder="Повідомлення" className="form-textarea" />
            <button type="submit" className="btn btn-primary">
              Відправити
            </button>
          </form>
        </div>
      </section>

      <CtaBanner
        title="Потрібна термінова консультація?"
        subtitle="Зателефонуйте нам просто зараз"
        button="Зателефонувати"
      />
    </>
  );
};
