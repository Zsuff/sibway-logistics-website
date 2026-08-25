import { CtaBanner } from '../components/CtaBanner';

// Контент з ua_services-transport.md
const transportContent = {
  hero: {
    title: "Транспортні перевезення",
    subtitle: "Міжнародні вантажні перевезення всіма видами транспорту"
  },
  description: "Забезпечуємо повний цикл транспортних послуг: від забору вантажу у відправника до доставки отримувачу. Автомобільні, залізничні, авіа та морські перевезення будь-якої складності.",
  transportTypes: {
    title: "Види транспорту",
    items: [
      { icon: "🚛", title: "Автомобільні перевезення", description: "Швидка доставка вантажів по Україні та Європі. Збірні вантажі, повні завантаження, експрес-доставка.", features: ["Доставка від 1 дня", "Відстеження вантажу", "Страхування"] },
      { icon: "🚂", title: "Залізничні перевезення", description: "Економічне перевезення великих обсягів на далекі відстані. Контейнерні та вагонні відправки.", features: ["Великі обсяги", "Низька вартість", "Надійність"] },
      { icon: "✈️", title: "Авіаперевезення", description: "Найшвидша доставка вантажів по всьому світу. Ідеально для термінових та цінних вантажів.", features: ["Доставка 1-3 дні", "Глобальне покриття", "Безпека"] },
      { icon: "🚢", title: "Морські перевезення", description: "Економічне перевезення великогабаритних вантажів морськими контейнерами по всьому світу.", features: ["Найнижча ціна", "Великі обсяги", "Міжнародні маршрути"] }
    ]
  },
  advantages: {
    title: "Переваги роботи з нами",
    items: ["Оптимальний маршрут та вид транспорту", "Повне митне оформлення", "Страхування вантажу", "Відстеження на всіх етапах", "Гарантія термінів доставки"]
  },
  cta: {
    title: "Потрібен розрахунок вартості?",
    subtitle: "Надішліть запит — отримайте комерційну пропозицію протягом 15 хвилин",
    button: "Розрахувати вартість"
  }
};

export default function TransportPage() {
  return (
    <div className="transport-page">
      <section className="transport-hero">
        <h1>{transportContent.hero.title}</h1>
        <p className="subtitle">{transportContent.hero.subtitle}</p>
        <p className="description">{transportContent.description}</p>
      </section>
      <section className="transport-types">
        <h2>{transportContent.transportTypes.title}</h2>
        <div className="transport-grid">
          {transportContent.transportTypes.items.map((item) => (
            <div key={item.title} className="transport-card">
              <span className="icon">{item.icon}</span>
              <h3>{item.title}</h3>
              <p>{item.description}</p>
              <ul className="features">{item.features.map((feature) => <li key={feature}>{feature}</li>)}</ul>
            </div>
          ))}
        </div>
      </section>
      <section className="advantages">
        <h2>{transportContent.advantages.title}</h2>
        <ul className="advantages-list">{transportContent.advantages.items.map((item) => <li key={item}>✓ {item}</li>)}</ul>
      </section>
      <CtaBanner title={transportContent.cta.title} subtitle={transportContent.cta.subtitle} button={transportContent.cta.button} />
    </div>
  );
}
