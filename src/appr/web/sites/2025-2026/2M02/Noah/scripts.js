/*
  - theme et langages sauvegardés dans localStorage
  - Theme toggle: #themeToggle echange body class theme-modern <-> theme-jp
  - Translation toggle: #translateToggle echange elements entre [data-ja][data-en]

  le stockage des theme et langue ne marche parfois pas. Il marche quand on choisit un theme/langue dans la page 4 par ex, 
  mais il revient parfois au theme par defaut lorsqu'on ouvre une nouvelle page et nous devons rechoisir le theme/langue. 
  Mais en revenant sur la page 4, le theme/langue choisi est bien sauvegardé.
  Les developpeurs sont au courant de ce bug, et ils sont entrain de chercher une solution.
*/

(() => {
  const THEME_KEY = "goth-theme"; // "modern" | "jp"
  const LANG_KEY = "goth-lang";   // "ja" | "en"

  const body = document.body;
  const themeBtn = document.getElementById("themeToggle");
  const translateBtn = document.getElementById("translateToggle");

  // charge les préférences sauvegardées ou valeurs par défaut
  let theme = localStorage.getItem(THEME_KEY) || "modern";
  let lang = localStorage.getItem(LANG_KEY) || "ja";

 //CHATGPT COMMENCE
  function applyTheme() {
    body.classList.toggle("theme-jp", theme === "jp");
    body.classList.toggle("theme-modern", theme !== "jp");

    if (themeBtn) {
      const isJP = theme === "jp";
      themeBtn.textContent = isJP ? "Modern mode" : "J-Web mode";
      themeBtn.setAttribute("aria-pressed", String(isJP));
    }

    // bouton uniquement visible en thème "jp"
    if (translateBtn) {
      translateBtn.style.display = theme === "jp" ? "" : "none";
    }
  }

  function applyTranslation() {
    const nodes = document.querySelectorAll("[data-ja][data-en]");
    nodes.forEach((el) => {
      el.textContent = lang === "en" ? el.dataset.en : el.dataset.ja;
    });

    if (translateBtn) {
      const toEnglish = lang === "en";
      translateBtn.textContent = toEnglish ? "EN→JP" : "JP→EN";
      translateBtn.setAttribute("aria-pressed", String(toEnglish));
    }
  }

  function save() {
    localStorage.setItem(THEME_KEY, theme);
    localStorage.setItem(LANG_KEY, lang);
  }
  //CHATGPT FIN

  // synchronisation a chaque chargement de page
  applyTheme();
  applyTranslation();

  if (themeBtn) {
    themeBtn.addEventListener("click", () => {
      theme = theme === "jp" ? "modern" : "jp";
      save();
      applyTheme();
      applyTranslation();
    });
  }

  if (translateBtn) {
    translateBtn.addEventListener("click", () => {
      lang = lang === "en" ? "ja" : "en";
      save();
      applyTranslation();
    });
  }
})();
