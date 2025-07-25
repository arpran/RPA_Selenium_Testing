# 🧪 Saucedemo Automation Testing with Selenium 🛒

Welcome to the **end-to-end Selenium automation testing project** for the demo e-commerce site [https://www.saucedemo.com](https://www.saucedemo.com).  
This project automates all major user workflows using Python and Selenium WebDriver.

---

## 🚀 Features Covered

1. 🔐 **Login Functionality** – Valid login using `standard_user`
2. 🛍️ **Add to Cart** – Adds all available items
3. 🧹 **Remove Items** – Removes selected items from cart
4. 🛒 **View Cart** – Verifies cart contents after modifications
5. 📝 **Checkout Process** – Fills customer info and submits
6. ✅ **Order Completion** – Finishes the purchase
7. 🔚 **Logout** – Closes the session via menu

---

## 🧰 Tech Stack

| Tool        | Version       | Purpose                 |
|-------------|---------------|-------------------------|
| 🐍 Python   | 3.7+           | Scripting language      |
| 🧪 Selenium | 4.x            | Browser automation      |
| 🌐 Chrome   | Latest Stable | Browser for test runs   |
| 🧠 WebDriver | ChromeDriver  | Controls the browser    |

---

## 📦 Installation

1. Clone the repo  
```bash
git clone https://github.com/your-username/saucedemo-selenium-automation.git
cd saucedemo-selenium-automation
Create a virtual environment (optional but recommended)

bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
Install dependencies

bash
pip install selenium

🖥️ How to Run the Script
bash
python saucedemo_test.py

Make sure:

✅ Chrome browser is installed

✅ ChromeDriver is added to system PATH or in your project folder

🧪 Demo Accounts on SauceDemo
You can use these predefined accounts:

Username	Password	Note
standard_user	secret_sauce	✅ Fully functional
locked_out_user	secret_sauce	❌ Locked account
problem_user	secret_sauce	⚠️ UI issues simulated
performance_glitch_user	secret_sauce	🐢 Slow response test case

🧪 Test Flow Summary
mermaid
graph TD
    A[Login to Saucedemo] --> B[Add All Items to Cart]
    B --> C[Remove 2 Items]
    C --> D[Go to Cart Page]
    D --> E[Proceed to Checkout]
    E --> F[Fill Checkout Info]
    F --> G[Finish Order]
    G --> H[Logout from Sidebar]
📸 Screenshots (Optional)
You can enable screenshots by modifying the script like:

python
driver.save_screenshot("step-name.png")
🧠 Best Practices Used
✅ Explicit Waits with WebDriverWait

✅ Element visibility before interaction

✅ JavaScript click for tricky elements (e.g., logout)

✅ Clean terminal output for test logs

🤝 Contributing
Contributions, improvements, and test cases for other users (problem_user, etc.) are welcome!

bash
Fork → Improve → Pull Request 🚀
📃 License
This project is licensed under the MIT License.

💬 Connect with Me
LinkedIn: Your Name

GitHub: @your-username

Email: your.email@example.com

🎯 Final Thoughts
This project is a perfect starting point for:

Practicing automation with real-world workflows

Learning test design for e-commerce applications

Preparing for QA and automation interviews 🧑‍💻

Happy Testing! 💻🧪✅

---

Would you like me to:
- Export this as a `.md` file?
- Add screenshots or a video demo link?
- Include instructions for GitHub Actions or CI tools?

Let me know and I’ll tailor it further!
