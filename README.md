
# IntentGraph

> **Natural Language → GraphQL Query Generator**  
> Built for developers, powered by AI.

![GraphQL](https://img.shields.io/badge/GraphQL-Driven-ff4081.svg)
![LLM](https://img.shields.io/badge/OpenAI%20%7C%20LangChain-Enabled-blueviolet)
![Status](https://img.shields.io/badge/Status-Alpha-orange)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 🚀 Overview

**IntentGraph** transforms natural language queries into executable GraphQL using large language models. It accelerates backend exploration by enabling engineers to speak directly to their data layer — no manual query writing required.

This project explores the intersection of AI reasoning, schema introspection, and intent disambiguation to streamline modern API development workflows.

---

## 🎯 Key Features

- 🧠 **Natural Language Interface**: Converts user prompts to GraphQL using LLMs
- 📘 **Schema-Aware**: Leverages introspection to tailor queries to your API
- 🔁 **Conversational Memory**: Understands multi-turn inputs with history (via LangChain)
- ⚡ **Live Preview**: Generates syntax-highlighted query output
- 🔐 **Secure Execution**: (Optional) Execute queries against real endpoints with authentication

---

## 🧱 Architecture

```
┌────────────────────┐
│  Natural Language  │
└────────┬───────────┘
         ▼
┌────────────────────┐
│    Intent Parser   │ ← LLM (OpenAI / LangChain)
└────────┬───────────┘
         ▼
┌────────────────────┐
│  GraphQL Generator │ ← Uses schema introspection
└────────┬───────────┘
         ▼
┌────────────────────┐
│   Query Preview UI │ ← React + Tailwind
└────────────────────┘
```

---

## 🔧 Tech Stack

| Layer          | Tech                      |
|----------------|---------------------------|
| Frontend       | React + Tailwind CSS      |
| Backend        | Node.js or Python (TBD)   |
| LLM Interface  | OpenAI / LangChain        |
| GraphQL Engine | Apollo / GraphQL.js       |
| Hosting        | Vercel (UI) / Render (API)|
| Dev Tools      | Postman, Insomnia, VSCode |

---

## 📦 Installation (WIP)

```bash
# Clone the repo
git clone https://github.com/ayushgoyal09/intent-graph.git
cd intent-graph

# Install dependencies (for frontend and backend separately)
npm install
# or
pip install -r requirements.txt
```

---

## 🛣️ Roadmap

- [x] Project initialization
- [x] Define scope and use cases
- [ ] MVP: Prompt → GraphQL output
- [ ] Schema file upload / live introspection
- [ ] Conversational memory
- [ ] Optional: LLM provider fallback
- [ ] Live hosted demo (Vercel + serverless API)

---

## 🧪 Example Prompt

> _“Get first 10 products with id, name and price where price is above 50”_

### ➤ Output:

```graphql
query {
  products(limit: 10, filter: { price_gt: 50 }) {
    id
    name
    price
  }
}
```

---

## 👨‍💻 About the Author

**Ayush Goyal**  
Principal Software Engineer | AI Explorer | System Design Enthusiast  
🔗 [LinkedIn](https://www.linkedin.com/in/ayushgoyal09) • [GitHub](https://github.com/ayushgoyal09)

---

## 📄 License

This project is licensed under the MIT License.
