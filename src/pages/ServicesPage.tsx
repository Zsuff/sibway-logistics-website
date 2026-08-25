import Services from '../components/Services';
import CtaBanner from '../components/CtaBanner';

// Контент з ua_services.md
const servicesContent = {
  hero: {
    title: "Наші послуги",
    subtitle: "Повний спектр логістичних рішень для вашого бізнесу"
  },
  description: "SIBWAY пропонує комплексні логістичні послуги: міжнародні вантажні перевезення, складське зберігання, митне оформлення та аудит логістичних процесів. Кожен напрямок має свою спеціалізацію та гарантує високу якість обслуговування.",
  services: {
    title: "Основні напрямки",
    items: [
      {
        icon: "🚛",
        title: "Транспортні перевезення",
        description: "Автомобільні, залізничні, авіа та морські перевезення будь-якої складності",
        link: "/transport"
      },
      {
        icon: "🏭",
        title: "Складські послуги",
        description: "Зберігання, обробка, комплектація та розподіл вантажів на сучасних складах",
        link: "/warehouse"
      },
      {
        icon: "📋",
        title: "Митне оформлення",
        description: "Повний супровід митних процедур: декларації, сертифікати, дозволи",
        link: "/customs"
      },
      {
        icon: "📊",
        title: "Аудит і консалтинг",
        description: "Оптимізація логістичних ланцюжків, аналіз витрат, пошук резервів",
        link: "/audit"
      }
    ]
  },
  cta: {
    title: "Потрібна допомога з вибором послуги?",
    subtitle: "Наші фахівці допоможуть підібрати оптимальне рішення для вашого бізнесу",
    button: "Зв'язатися з нами"
  }
};

export default function ServicesPage() {
  return (
    <div className="services-page">
      <section className="services-hero">
        <h1>{servicesContent.hero.title}</h1>
        <p className="subtitle">{servicesContent.hero.subtitle}</p>
        <p className="description">{servicesContent.description}</p>
      </section>
      <Services
        title={servicesContent.services.title}
        items={servicesContent.services.items}
      />
      <CtaBanner
        title={servicesContent.cta.title}
        subtitle={servicesContent.cta.subtitle}
        button={servicesContent.cta.button}
      />
    </div>
  );
}
