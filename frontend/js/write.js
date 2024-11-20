const form = document.getElementById("write-form");

const handleSubmitForm = async (e) => {
  e.preventDefault();
  const formbody = new FormData(form);
  formbody.append("insertAt", new Date().getTime());
  try {
    const res = await fetch("/items", {
      method: "POST",
      body: formbody,
    });
    const data = await res.json();

    if (data === "200") window.location.pathname = "/";
  } catch (error) {
    console.error(error);
  }
};

form.addEventListener("submit", handleSubmitForm);
