/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{vue,js}'],
  theme: {
    extend: {
      fontFamily: {
        ubuntu: ['Ubuntu', 'Helvetica', 'Arial', 'sans-serif'],
      },
      // All used colors should be declared here!
      colors: {
        primary: '#2EC4B6',
        'primary-light': '#CBF3F0',
        'primary-dark': '#19B5A7',
        'simple-gray': '#4A4A4A',
        'dark-text': '#232A42',
        'light-text': '#696E7E',
        'section-secondary': '#F4F6FC',
      },
      screens: {
        xs: '472px',
      },
    },
  },
  plugins: [],
};
