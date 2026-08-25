import About from '../components/About';
import Stats from '../components/Stats';
import CtaBanner from '../components/CtaBanner';

// Контент з ua_about.md
const aboutContent = {
  hero: {
    title: "Про компанію SIBWAY",
    subtitle: "Міжнародна логістична компанія з повним циклом послуг"
  },
  description: "SIBWAY — це надійний партнер у сфері міжнародних вантажних перевезень та логістики. Ми забезпечуємо повний цикл послуг: від забору вантажу у відправника до доставки отримувачу з повним митним оформленням.",
  mission: {
    title: "Наша місія",
    text: "Забезпечувати бізнес швидкими, надійними та економно ефективними логістичними рішеннями, що дозволяють нашим клієнтам зосередитись на розвитку свого основного бізнесу."
  },
  values: {
    title: "Наші цінності",
    items: [
      { title: "Надійність", text: "Гарантуємо безпеку вантажу та дотримання термінів" },
      { title: "Професіоналізм", text: "Команда досвідчених фахівців у сфері логістики" },
      { title: "Прозорість", text: "Чітке ціноутворення без прихованих платежів" },
      { title: "Клієнтоорієнтованість", text: "Індивідуальний підхід до кожного клієнта" }
    ]
  },
  stats: {
    items: [
      { value: "10+", label: "років на ринку" },
      { value: "500+", label: "задоволених клієнтів" },
      { value: "10 000+", label: "успішних доставок" },
      { value: "24/7", label: "підтримка клієнтів" }
    ]
  },
  cta: {
    title: "Хочете дізнатись більше?",
    subtitle: "Зв'яжіться з нами для консультації або співпраці",
    button: "Контакти"
  }
};

export default function AboutPage() {
  return (
    <div className="about-page">
      <About
        title={aboutContent.hero.title}
        subtitle={aboutContent.hero.subtitle}
        description={aboutContent.description}
        mission={aboutContent.mission}
        values={aboutContent.values}
      />
      <Stats items={aboutContent.stats.items} />
      <CtaBanner
        title={aboutContent.cta.title}
        subtitle={aboutContent.cta.subtitle}
        button={aboutContent.cta.button}
      />
    </div>
  );
}
