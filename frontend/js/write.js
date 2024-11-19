const form = document.getElementById("write-form");

const handleSubmitForm = async (e) => {
  e.preventDefault();
  try {
    const res = await fetch("/items", {
      method: "POST",
      body: new FormData(form),
    });
    const data = await res.json();

    if (data === "200") window.location.pathname = "/";
  } catch (error) {
    console.error(error);
  }
};

form.addEventListener("submit", handleSubmitForm);
