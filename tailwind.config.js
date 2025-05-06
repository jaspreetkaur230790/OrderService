/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
        './templates/**/*.html', // Scan all Flask templates
        './static/js/**/*.js',   // (optional) scan JS files if you use them  
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
