import { Link } from 'react-router-dom';

export const NotFoundPage = () => {
  return (
    <div style={{
      minHeight: '100vh',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      flexDirection: 'column',
      textAlign: 'center',
      padding: '20px',
      background: 'linear-gradient(135deg, #0066cc 0%, #004999 100%)',
      color: 'white'
    }}>
      <h1 style={{ fontSize: '72px', fontWeight: '700', margin: '0 0 20px 0' }}>404</h1>
      <h2 style={{ fontSize: '32px', margin: '0 0 20px 0' }}>Сторінку не знайдено</h2>
      <p style={{ fontSize: '18px', marginBottom: '30px', opacity: 0.9 }}>
        Вибачте, сторінка, яку ви шукаєте, не існує або була переміщена.
      </p>
      <Link
        to="/"
        style={{
          padding: '14px 28px',
          backgroundColor: 'white',
          color: '#0066cc',
          textDecoration: 'none',
          borderRadius: '6px',
          fontWeight: '600',
          fontSize: '16px',
          transition: 'all 0.3s'
        }}
      >
        Повернутися на головну
      </Link>
    </div>
  );
};
