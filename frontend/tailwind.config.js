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
        black: '#000',
        white: '#fff',
        footerBg: '#4A4A4A',
        foterBg2: '#FF0000',
        primary: 'TODO: add primary color!', // Example!
      },
    },
  },
  plugins: [],
};
