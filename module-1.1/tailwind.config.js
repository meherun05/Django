/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templetes/**/*.html", // **/ mean every folder inside the temp folder for temp project level
    "./**/templetes/**/*.html", // this is for app level folder for other app like user,task
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};
