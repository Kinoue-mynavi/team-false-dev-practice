"use strict";

const ACTIVATED_MODAL_CLASS_NAME = "is-visible";

const modal = document.querySelector(".modal-container");
const toggleMenuButton = document.querySelector(".toggle-menu-button");

const toggleClass = ({ element, className = "" }) => {
  element.classList.toggle(className);
};

const handleClickMenuButton = () => {
  toggleClass({
    element: modal,
    className: ACTIVATED_MODAL_CLASS_NAME,
  });
  toggleClass({
    element: toggleMenuButton,
    className: ACTIVATED_MODAL_CLASS_NAME,
  });
};

toggleMenuButton.addEventListener("click", handleClickMenuButton);