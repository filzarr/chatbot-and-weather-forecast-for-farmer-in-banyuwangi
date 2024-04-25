/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./static/src/**/*.js"
  ],
  theme: {
    extend: {
      fontFamily: { 
        "sans": ['Open Sans', 'sans-serif'] 
    } 
    },
  },
  plugins: [],
}