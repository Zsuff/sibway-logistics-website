import React from 'react';
import { Header } from '../components/Header';
import { Hero } from '../components/Hero';
import { Stats } from '../components/Stats';
import { About } from '../components/About';
import { Services } from '../components/Services';
import { WhyUs } from '../components/WhyUs';
import { BenefitsAndQuoteForm } from '../components/BenefitsAndQuoteForm';
import { CtaBanner } from '../components/CtaBanner';
import { Footer } from '../components/Footer';

export const HomePage: React.FC = () => {
  return (
    <div className="min-h-screen flex flex-col bg-[#F8F9FA] dark:bg-[#0F172A] text-slate-900 dark:text-slate-100">
      <Header />
      <main className="flex-grow">
        <Hero />
        <Stats />
        <About />
        <Services />
        <WhyUs />
        <BenefitsAndQuoteForm />
        <CtaBanner />
      </main>
      <Footer />
    </div>
  );
};
