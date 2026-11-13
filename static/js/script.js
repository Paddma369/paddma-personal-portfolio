/* ==========================================================================
   Portfolio behaviour. Small and dependency-free.
   1. Mobile menu
   2. Highlight the current section in the menu
   3. Fade-in on scroll
   4. Contact form (opens the visitor's email app, no server needed)
   ========================================================================== */

(function () {
  "use strict";

  /* 1. MOBILE MENU ------------------------------------------------------- */
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.getElementById("primary-nav");

  function setMenu(open) {
    if (!toggle || !nav) return;
    toggle.setAttribute("aria-expanded", String(open));
    toggle.setAttribute("aria-label", open ? "Close menu" : "Open menu");
    nav.classList.toggle("is-open", open);
  }

  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      setMenu(toggle.getAttribute("aria-expanded") !== "true");
    });

    // Close after choosing a link
    nav.addEventListener("click", function (e) {
      if (e.target.closest("a")) setMenu(false);
    });

    // Close with the Escape key
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && toggle.getAttribute("aria-expanded") === "true") {
        setMenu(false);
        toggle.focus();
      }
    });

    // Reset if the window is resized up to desktop width
    window.matchMedia("(min-width: 960px)").addEventListener("change", function (e) {
      if (e.matches) setMenu(false);
    });
  }

  /* 2. ACTIVE LINK ON SCROLL --------------------------------------------- */
  var links = Array.prototype.slice.call(document.querySelectorAll(".nav__list a"));
  var sections = links
    .map(function (a) { return document.querySelector(a.getAttribute("href")); })
    .filter(Boolean);

  if ("IntersectionObserver" in window && sections.length) {
    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        links.forEach(function (a) {
          var active = a.getAttribute("href") === "#" + entry.target.id;
          a.classList.toggle("is-active", active);
          if (active) a.setAttribute("aria-current", "true");
          else a.removeAttribute("aria-current");
        });
      });
    }, { rootMargin: "-45% 0px -50% 0px" });

    sections.forEach(function (s) { spy.observe(s); });
  }

  /* 3. FADE-IN ON SCROLL ------------------------------------------------- */
  var revealItems = document.querySelectorAll(".reveal");

  if ("IntersectionObserver" in window) {
    var revealer = new IntersectionObserver(function (entries, obs) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          obs.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -40px 0px" });

    revealItems.forEach(function (el) { revealer.observe(el); });
  } else {
    // Very old browsers: just show everything
    revealItems.forEach(function (el) { el.classList.add("is-visible"); });
  }

  /* 4. CONTACT FORM ------------------------------------------------------ */
  var form = document.getElementById("contact-form");
  var status = document.getElementById("form-status");

  function showStatus(message, type) {
    if (!status) return;
    status.textContent = message;
    status.className = "form__status" + (type ? " is-" + type : "");
  }

  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();

      var name = form.elements.name;
      var email = form.elements.email;
      var message = form.elements.message;
      var firstInvalid = null;

      [name, email, message].forEach(function (field) {
        var ok = field.value.trim() !== "" && (field !== email || /^\S+@\S+\.\S+$/.test(field.value.trim()));
        field.classList.toggle("is-invalid", !ok);
        field.setAttribute("aria-invalid", String(!ok));
        if (!ok && !firstInvalid) firstInvalid = field;
      });

      if (firstInvalid) {
        showStatus("Please fill in all fields with a valid email address.", "error");
        firstInvalid.focus();
        return;
      }

      var to = form.getAttribute("data-email");
      if (!to) {
        showStatus("The site owner has not added an email address yet.", "error");
        return;
      }

      var subject = "Portfolio enquiry from " + name.value.trim();
      var body = message.value.trim() + "\n\n-- \n" + name.value.trim() + "\n" + email.value.trim();

      window.location.href =
        "mailto:" + encodeURIComponent(to).replace("%40", "@") +
        "?subject=" + encodeURIComponent(subject) +
        "&body=" + encodeURIComponent(body);

      showStatus("Opening your email app. If nothing opens, please email me directly.", "ok");
    });
  }
})();
