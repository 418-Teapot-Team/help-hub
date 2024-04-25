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
        primary: 'TODO: add primary color!', // Example!
        'simple-gray': '#4A4A4A',
        // bg-primary:
      },
    },
  },
  plugins: [],
};
