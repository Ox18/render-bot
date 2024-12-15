const btnSendMessage = document.getElementById("btnSendMessage");
const inputMessage = document.getElementById("input-message");
const iframeReceptor = document.getElementById("iframe-receptor");
const rootContainer = document.getElementById("root");
var visibleIframe = false;

const scrollToBottom = () => {
  const messages = document.getElementById("messages");
  messages.scrollTop = messages.scrollHeight;
};

const addMessage = (message, isBot) => {
  const messages = document.getElementById("messages");

  const messageElement = document.createElement("div");
  messageElement.classList.add(isBot ? "message-bot" : "message");
  messageElement.innerHTML = `
          <div class="message-content">
            ${message}
          </div>
        `;

  messages.appendChild(messageElement);
};

const addMessageBot = (message) => {
  addMessage(message, true);
};

const addMessageUser = (message) => {
  addMessage(message, false);
};

const renderContent = (responseBot) => {
  iframeReceptor.src = iframeReceptor.src;

  if (!visibleIframe) {
    rootContainer.classList.toggle("show-iframe");
    visibleIframe = true;
  }
  iframeReceptor.style.display = "block";
  iframeReceptor.onload = function () {
    iframeReceptor.contentWindow.postMessage(responseBot, "*");
  };
};

// Add event listener to the button
btnSendMessage.addEventListener("click", async () => {
  const message = inputMessage.value;

  if (message.trim() === "" || message.length === 0) {
    inputMessage.focus();
    return;
  }

  inputMessage.value = "";
  addMessageUser(message);

  const response = await question(message);

  renderContent(response);

  addMessageBot("se ha procesado tu mensaje");
  scrollToBottom();
});

// enter tab message
inputMessage.addEventListener("keyup", (event) => {
  if (event.key === "Enter") {
    btnSendMessage.click();
  }
});

const question = (message) => {
  return new Promise((resolve, reject) => {
    fetch("/api/question", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ message }),
    })
      .then((response) => response.json())
      .then((data) => {
        resolve(data);
      })
      .catch((error) => {
        reject(error);
      });
  });
};

const historyMessages = async () => {
  const response = await fetch("/api/messages/history");

  const data = await response.json();

  return data;
};

const recopileHistoryMessage = async () => {
  const history = await historyMessages();

  history.forEach((history) => {
    addMessageUser(history.message);
    addMessageBot("se ha procesado tu mensaje");
  });

  if (history.length > 0) {
    const lastHistory = history[history.length - 1];

    renderContent(lastHistory.response);
  }
};

recopileHistoryMessage();
