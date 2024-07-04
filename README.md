# GEMINI
Generative AI: Everything You need to know about Gemini Pro LLM Models - 2024 [Video](https://www.youtube.com/watch?v=JrTZJMU0KK4)

[Tutorial: Get started with the Gemini API ](https://ai.google.dev/gemini-api/docs/get-started/tutorial?lang=python&authuser=1)
> **python.ipynb** downloaded(modified) from the above website (key 是 GOOGLE_API_KEY)

conda create -p venv python==3.10 -y
conda activate venv/

* requirements.txt

* <font color="red">.env (Github不會保存此檔，clone 此 reposiotry 一定要重新建立)</font>
> ```python
> GOOGLE_API_KEY = '...'
> ```

```bash
pip install -r requiremetns.txt
```

* app.py

```bash
streamlit run app.py
```

`"sample invoice""Click to edit` 用 **e6331dbe479349413d652cd20_invoice-lp-sample-click-to-edit.png**

What is the Desposit requested (第1問--應該是`Deposit'，但不影響答案)

Who is this invoice billed to (第2問)

`"hindi invoice format"` 用 **GST-Invoice-Template-In-Hindi.jpg**

What is the HSN of Lenovo 5125-I (第3問)

What is the Billing address (第4問) 

What is the date of the invoice (第5問)

What is the CGST (第6問)

What is the total bill (第7問)
