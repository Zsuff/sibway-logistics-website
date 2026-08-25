import { CtaBanner } from '../components/CtaBanner';

// Контент з ua_contacts.md
const contactsContent = {
  hero: {
    title: "Контакти",
    subtitle: "Зв'яжіться з нами для консультації або розрахунку вартості"
  },
  contactInfo: {
    title: "Наші контакти",
    items: [
      { icon: "📍", title: "Адреса", text: "Україна, м. Київ, вул. Логістична, 1" },
      { icon: "📞", title: "Телефон", text: "+380 (44) 123-45-67" },
      { icon: "📧", title: "Email", text: "info@sibway.com.ua" },
      { icon: "🕐", title: "Режим роботи", text: "Пн-Пт: 9:00-18:00, Сб-Нд: вихідний" }
    ]
  },
  form: {
    title: "Напишіть нам",
    fields: [
      { name: "name", label: "Ваше ім'я", type: "text", required: true },
      { name: "email", label: "Email", type: "email", required: true },
      { name: "phone", label: "Телефон", type: "tel", required: false },
      { name: "service", label: "Тип послуги", type: "select", required: false, options: ["Транспортні перевезення", "Складські послуги", "Митне оформлення", "Аудит і консалтинг", "Інше"] },
      { name: "message", label: "Повідомлення", type: "textarea", required: true }
    ],
    button: "Відправити"
  },
  cta: {
    title: "Готові розпочати співпрацю?",
    subtitle: "Залиште заявку — ми зв'яжемось з вами протягом 15 хвилин",
    button: "Замовити дзвінок"
  }
};

export default function ContactsPage() {
  return (
    <div className="contacts-page">
      <section className="contacts-hero">
        <h1>{contactsContent.hero.title}</h1>
        <p className="subtitle">{contactsContent.hero.subtitle}</p>
      </section>
      <section className="contact-info">
        <h2>{contactsContent.contactInfo.title}</h2>
        <div className="contact-grid">
          {contactsContent.contactInfo.items.map((item) => (
            <div key={item.title} className="contact-item">
              <span className="icon">{item.icon}</span>
              <h3>{item.title}</h3>
              <p>{item.text}</p>
            </div>
          ))}
        </div>
      </section>
      <section className="contact-form">
        <h2>{contactsContent.form.title}</h2>
        <form className="form">
          {contactsContent.form.fields.map((field) => (
            <div key={field.name} className="form-group">
              <label htmlFor={field.name}>{field.label}</label>
              {field.type === 'select' ? (
                <select id={field.name} name={field.name} required={field.required}>
                  <option value="">Оберіть...</option>
                  {field.options?.map((option) => <option key={option} value={option}>{option}</option>)}
                </select>
              ) : field.type === 'textarea' ? (
                <textarea id={field.name} name={field.name} rows={5} required={field.required} />
              ) : (
                <input type={field.type} id={field.name} name={field.name} required={field.required} />
              )}
            </div>
          ))}
          <button type="submit" className="btn-primary">{contactsContent.form.button}</button>
        </form>
      </section>
      <CtaBanner title={contactsContent.cta.title} subtitle={contactsContent.cta.subtitle} button={contactsContent.cta.button} />
    </div>
  );
}
