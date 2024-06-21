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


// ページネーション用
const page_info_div = document.querySelector(".pagination-page-info");
const page_info = page_info_div.querySelectorAll("b");
document.querySelector(".pagination-page-info").innerText = page_info[1].innerText + " 件中 " + page_info[0].innerText + " 件目を表示";