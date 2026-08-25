import Hero from '../components/Hero';
import Services from '../components/Services';
import BenefitsAndQuoteForm from '../components/BenefitsAndQuoteForm';
import CtaBanner from '../components/CtaBanner';
import Stats from '../components/Stats';
import WhyUs from '../components/WhyUs';

// Контент з ua_homepage.md
const homepageContent = {
  hero: {
    title: "Міжнародна логістика для вашого бізнесу",
    subtitle: "Надійні вантажні перевезення Україна-ЄС. Повний супровід: від забору вантажу до митного оформлення.",
    ctaPrimary: "Розрахувати вартість",
    ctaSecondary: "Замовити дзвінок"
  },
  services: {
    title: "Наші послуги",
    items: [
      {
        icon: "🚛",
        title: "Транспортні перевезення",
        description: "Автомобільні, залізничні, авіа та морські перевезення будь-якої складності"
      },
      {
        icon: "🏭",
        title: "Складські послуги",
        description: "Зберігання, обробка, комплектація та розподіл вантажів на сучасних складах"
      },
      {
        icon: "📋",
        title: "Митне оформлення",
        description: "Повний супровід митних процедур: декларації, сертифікати, дозволи"
      },
      {
        icon: "📊",
        title: "Аудит і консалтинг",
        description: "Оптимізація логістичних ланцюжків, аналіз витрат, пошук резервів"
      }
    ]
  },
  benefits: {
    title: "Чому обирають SIBWAY",
    items: [
      { icon: "⏱️", text: "Швидке оформлення документів" },
      { icon: "🛡️", text: "Гарантія безпеки вантажу" },
      { icon: "💰", text: "Прозоре ціноутворення" },
      { icon: "🌍", text: "Міжнародна мережа партнерів" },
      { icon: "📞", text: "Персональний менеджер 24/7" },
      { icon: "📦", text: "Страхування вантажів" }
    ]
  },
  cta: {
    title: "Готові обговорити ваш проєкт?",
    subtitle: "Залиште заявку — отримайте безкоштовну консультацію та розрахунок вартості",
    button: "Отримати консультацію"
  },
  stats: {
    items: [
      { value: "10+", label: "років на ринку" },
      { value: "500+", label: "задоволених клієнтів" },
      { value: "10 000+", label: "успішних доставок" },
      { value: "24/7", label: "підтримка клієнтів" }
    ]
  },
  whyUs: {
    title: "Чому ми",
    items: [
      {
        title: "Досвід",
        description: "Більше 10 років успішної роботи на ринку міжнародної логістики"
      },
      {
        title: "Надійність",
        description: "Гарантуємо безпеку вантажу та дотримання термінів доставки"
      },
      {
        title: "Професіоналізм",
        description: "Команда кваліфікованих фахівців з глибоким розумінням логістики"
      }
    ]
  }
};

export default function HomePage() {
  return (
    <div className="home-page">
      <Hero
        title={homepageContent.hero.title}
        subtitle={homepageContent.hero.subtitle}
        ctaPrimary={homepageContent.hero.ctaPrimary}
        ctaSecondary={homepageContent.hero.ctaSecondary}
      />
      
      <Services
        title={homepageContent.services.title}
        items={homepageContent.services.items}
      />
      
      <BenefitsAndQuoteForm
        title={homepageContent.benefits.title}
        benefits={homepageContent.benefits.items}
      />
      
      <WhyUs
        title={homepageContent.whyUs.title}
        items={homepageContent.whyUs.items}
      />
      
      <Stats items={homepageContent.stats.items} />
      
      <CtaBanner
        title={homepageContent.cta.title}
        subtitle={homepageContent.cta.subtitle}
        button={homepageContent.cta.button}
      />
    </div>
  );
}
