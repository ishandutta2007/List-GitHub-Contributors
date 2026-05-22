# 🚀 GitHub Contributor Fetcher & Analyzer

[![Python Version](https://img.shields.io/badge/python-3.11.4-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.108.0-05998b.svg)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An automated tool to fetch, list, and analyze contributors for multiple GitHub repositories using the GitHub REST API. Features a **Modern Web UI** for batch processing and a **Powerful CLI** for quick lookups.

---

## 📺 Project Demo

![Project Showcase](https://via.placeholder.com/800x400?text=GitHub+Contributor+Fetcher+Demo+GIF)
*Place your project GIF here to showcase the beautiful UI!*

---

## ✨ Key Features

- 📦 **Batch Processing:** Fetch contributors for multiple repositories simultaneously.
- 🎨 **Professional Web UI:** Clean, glassmorphism-inspired interface with real-time animations.
- 🐚 **Command Line Interface:** Fast and lightweight CLI for terminal power users.
- 📝 **File Persistence:** Automatically saves/appends usernames to `contributors.txt`.
- ⚙️ **Smart Fallbacks:** Defaults to pre-configured repositories if no input is provided.
- 🔑 **Rate Limit Friendly:** Supports GitHub PAT (Personal Access Tokens) for high-volume requests.

---

## 🛠️ Tech Stack

- **Backend:** [Python 3.11+](https://www.python.org/) + [FastAPI](https://fastapi.tiangolo.com/)
- **Frontend:** [Vanilla JS](http://vanilla-js.com/), [CSS3 Custom Properties](https://developer.mozilla.org/en-US/docs/Web/CSS), [HTML5](https://developer.mozilla.org/en-US/docs/Web/HTML)
- **API:** [GitHub REST API v3](https://docs.github.com/en/rest)
- **Styling:** GitHub-inspired professional aesthetic with responsive design.

---

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/List-GitHub-Contributors.git
cd List-GitHub-Contributors
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
# or manually
pip install requests python-dotenv fastapi uvicorn
```

### 3. Configure Environment
Create a `.env` file from the example:
```bash
cp .env.example .env
```
Add your **GitHub Personal Access Token** to `.env`:
```env
ADMIN_TOKEN=your_github_pat_here
```

---

## 🎮 Usage

### 🌐 Web Interface (Recommended)
Launch the professional dashboard:
```bash
python app.py
```
Visit `http://localhost:8000` to start analyzing!

### 💻 CLI Mode
For quick terminal operations:
```bash
# Overwrite mode
python fetch_github_contributors.py

# Append mode
python fetch_github_contributors.py --append
```

---

## 📂 Project Structure

- `app.py` - FastAPI server & REST API logic.
- `fetch_github_contributors.py` - Core GitHub API engine.
- `static/` - Professional frontend assets (HTML, CSS, JS).
- `contributors.txt` - Generated/Appended list of usernames.

---

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

Developed with ❤️ by [ishandutta2007](https://github.com/ishandutta2007)
