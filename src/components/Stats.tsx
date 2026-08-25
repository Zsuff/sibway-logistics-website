import type { FC } from 'react';

export interface StatItem {
  value: string;
  label: string;
}

export interface StatsProps {
  items: StatItem[];
}

export const Stats: FC<StatsProps> = ({ items }) => {
  return (
    <section className="stats">
      <div className="stats-container">
        {items.map((stat, index) => (
          <div key={index} className="stat-item">
            <div className="stat-value">{stat.value}</div>
            <div className="stat-label">{stat.label}</div>
          </div>
        ))}
      </div>
    </section>
  );
};
