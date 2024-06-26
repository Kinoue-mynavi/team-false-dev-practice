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
const pageInfoDiv = document.querySelector(".pagination-page-info");
const pageInfo = pageInfoDiv.querySelectorAll("b");
document.querySelector(".pagination-page-info").innerText = pageInfo[1].innerText + " 件中 " + pageInfo[0].innerText + " 件目を表示";

// アラート
const confirmBooking = (elem) => {
  if(confirm("キャンセルしますか")) {
      alert("registed: " + elem); 
      document.getElementById("userInput").value = "True";
  } else { 
       document.getElementById("userInput").value = "False";
       return 0;
  }          
}