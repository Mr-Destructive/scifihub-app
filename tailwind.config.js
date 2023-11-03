/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
  ],
  darkMode: 'class',

  theme: {
    extend: {
      colors: {
          'orange': '#e67e22',
        night: {
          primary: '#2c3e50',
          secondary: '#34495e',
          // Add more colors as needed
        },
        evening: {
          primary: 'orange-500',
          secondary: '#e67e22',
          // Add more colors as needed
        },
        noon: {
          primary: '#f1c40f',
          secondary: '#f39c12',
          // Add more colors as needed
        },
        day: {
          primary: '#2ecc71',
          secondary: '#27ae60',
          // Add more colors as needed
        },
      },
    },
  },
  plugins: [],
};
