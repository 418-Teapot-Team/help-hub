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
        'dark-text': '#232A42',
      },
    },
  },
  plugins: [],
};
