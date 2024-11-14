const form = document.getElementById("write-form");

const handleSubmitForm = async (e) => {
  e.preventDefault();
  await fetch("/items", {
    method: "POST",
    body: new FormData(form),
  });
  console.log("제출 완료입니다");
};

form.addEventListener("submit", handleSubmitForm);
