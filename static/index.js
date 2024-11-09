(function () {
  tailwind.config = {
    content: ["./*.html"],
    darkMode: "class",
  };

  const updateHightlightTheme = (theme) => {
    const link = document.querySelector("#highlightjs-theme");
    if (link) {
      const themeName = theme === "dark" ? "atom-one-dark" : "atom-one-light";
      link.href = `https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.10.0/styles/${themeName}.css`;
    }
  };

  const updateGithubMarkdownTheme = (theme) => {
    const link = document.querySelector("#github-markdown-css-theme");
    if (link) {
      const themeName =
        theme === "dark" ? "github-markdown-dark" : "github-markdown-light";
      link.href = `https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.7.0/${themeName}.min.css`;
    }
  };

  document.addEventListener("DOMContentLoaded", function () {
    const theme = localStorage.theme || "dark";
    if (
      theme === "dark" ||
      (!("theme" in localStorage) &&
        window.matchMedia("(prefers-color-scheme: dark)").matches)
    ) {
      document.documentElement.classList.remove("light");
      document.documentElement.classList.add("dark");
    } else {
      document.documentElement.classList.remove("dark");
      document.documentElement.classList.add("light");
    }

    updateHightlightTheme(theme);
    updateGithubMarkdownTheme(theme);

    document.querySelector("#menu-toggle").addEventListener("click", () => {
      const menu = document.getElementById("mobile-menu");
      menu.classList.toggle("hidden");
    });

    document
      .querySelector("#theme-toggle")
      .addEventListener("click", function () {
        const htmlClasses = document.documentElement.classList;
        if (htmlClasses.contains("dark")) {
          htmlClasses.remove("dark");
          htmlClasses.add("light");
          localStorage.theme = "light";
          this.querySelector("i").classList.replace("fa-moon", "fa-sun");
        } else {
          htmlClasses.remove("light");
          htmlClasses.add("dark");
          localStorage.theme = "dark";
          this.querySelector("i").classList.replace("fa-sun", "fa-moon");
        }
        updateHightlightTheme(localStorage.theme);
        updateGithubMarkdownTheme(localStorage.theme);
      });
  });
})();
