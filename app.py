import streamlit as st
import chromadb
import ollama
from sentence_transformers import SentenceTransformer

st.set_page_config(
    page_title="Bank Chatbot",
    page_icon="🏦",
    layout="wide"
)

# =========================
# DESIGN
# =========================

st.markdown("""
<style>
.main-title {
    color: #1565C0;
    font-size: 42px;
    font-weight: 800;
}

.subtitle {
    color: #455A64 !important;
    font-size: 18px;
    margin-bottom: 25px;
}

.hero {
    background: linear-gradient(135deg, #E3F2FD, #E8F5E9);
    padding: 28px;
    border-radius: 18px;
    border-left: 6px solid #1976D2;
    margin-bottom: 25px;
}

.hero h2 {
    color: #0D47A1 !important;
}

.hero h1 {
    color: #1565C0 !important;
}

.hero p {
    color: #37474F !important;
}

.box {
    background: #F5F9FF;
    padding: 22px;
    border-radius: 16px;
    border: 1px solid #BBDEFB;
    min-height: 160px;
}

.box h3 {
    color: #1565C0 !important;
}

.box p {
    color: #455A64 !important;
    line-height: 1.6;
}

h1 {
    color: #0D47A1 !important;
}

h2 {
    color: #1565C0 !important;
}

h3 {
    color: #1976D2 !important;
}

p {
    color: #37474F !important;
}

label {
    color: #263238 !important;
    font-weight: 600 !important;
}

/* SELECTBOX */

div[data-baseweb="select"] > div {
    background-color: #F5F9FF !important;
    border: 1px solid #90CAF9 !important;
    border-radius: 10px !important;
}

div[data-baseweb="select"] span {
    color: #263238 !important;
    font-weight: 500 !important;
}

div[data-baseweb="select"] svg {
    fill: #1565C0 !important;
}

div[role="listbox"] {
    background-color: #FFFFFF !important;
}

div[role="option"] {
    color: #263238 !important;
    background-color: #FFFFFF !important;
}

div[role="option"]:hover {
    background-color: #E3F2FD !important;
    color: #0D47A1 !important;
}

/* INPUTS */

div[data-baseweb="input"] > div {
    background-color: #F5F9FF !important;
    border: 1px solid #90CAF9 !important;
    border-radius: 10px !important;
}

div[data-baseweb="input"] input {
    color: #263238 !important;
    font-weight: 500 !important;
}

/* METRICS */

div[data-testid="stMetric"] {
    background: #F5F9FF;
    padding: 18px;
    border-radius: 14px;
    border: 1px solid #BBDEFB;
}

div[data-testid="stMetricLabel"] {
    color: #455A64 !important;
}

div[data-testid="stMetricValue"] {
    color: #1565C0 !important;
}

/* BUTTON */

.stButton > button {
    background: #1976D2 !important;
    color: #FFFFFF !important;
    border-radius: 10px;
    border: none;
    font-weight: 600;
}

.stButton > button:hover {
    background: #0D47A1 !important;
}

/* SIDEBAR */

section[data-testid="stSidebar"] {
    background-color: #F5F9FF;
}

section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] label {
    color: #263238 !important;
}

/* AI ANSWER */

.ai-answer {
    background-color: #F5F9FF;
    border: 1px solid #BBDEFB;
    border-left: 5px solid #1976D2;
    padding: 20px;
    border-radius: 12px;
}

.ai-title {
    color: #1565C0 !important;
    font-size: 18px;
    font-weight: 700;
    margin-bottom: 10px;
}

.ai-text {
    color: #263238 !important;
    font-size: 16px;
    line-height: 1.7;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================

st.markdown(
    '<div class="main-title">🏦 Bank Chatbot</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Your simple and intelligent digital banking assistant</div>',
    unsafe_allow_html=True
)

# =========================
# SIDEBAR
# =========================

st.sidebar.title("🏦 Bank Chatbot")
st.sidebar.write("### Banking Services")

menu = st.sidebar.radio(
    "Select a service",
    [
        "🏠 Dashboard",
        "🏦 Loan Assistant",
        "💰 Account Balance",
        "💳 EMI Calculator",
        "📄 AI Document Assistant"
    ]
)

st.sidebar.markdown("---")
st.sidebar.success("🔐 Safe • Simple • Smart")
st.sidebar.caption("College Project Demo")

# =========================
# DASHBOARD
# =========================

if menu == "🏠 Dashboard":

    st.markdown("""
    <div class="hero">
        <h2>👋 Welcome to Bank Chatbot</h2>
        <p>
        One simple place to explore loans, calculate EMI,
        view account information and ask questions from bank documents.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("✨ What can you do?")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="box">
            <h3>🏦 Loan Assistant</h3>
            <p>
            Check basic loan eligibility using your income,
            age and required loan amount.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="box">
            <h3>💳 EMI Calculator</h3>
            <p>
            Calculate monthly EMI, total interest and
            total repayment.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="box">
            <h3>📄 AI Documents</h3>
            <p>
            Upload a banking document and ask questions
            using Smart Bank AI.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.subheader("📊 Quick Overview")

    a, b, c, d = st.columns(4)

    a.metric("💰 Demo Balance", "₹42,500")
    b.metric("🏦 Loan Service", "Available")
    c.metric("💳 EMI Tool", "Ready")
    d.metric("🤖 AI Assistant", "Active")

    st.info(
        "💡 This is a college project demonstration. "
        "It is not connected to a real bank account."
    )

# =========================
# LOAN ASSISTANT
# =========================

if menu == "🏦 Loan Assistant":

    st.header("🏦 Loan Eligibility Assistant")

    st.write(
        "Enter your details to check basic project eligibility."
    )

    left, right = st.columns(2)

    with left:

        loan_type = st.selectbox(
            "🏷️ Loan Type",
            [
                "Personal Loan",
                "Home Loan",
                "Car Loan",
                "Education Loan"
            ]
        )

        age = st.number_input(
            "🎂 Your Age",
            min_value=18,
            max_value=70,
            value=25
        )

        income = st.number_input(
            "💵 Monthly Income (₹)",
            min_value=5000,
            max_value=1000000,
            value=30000,
            step=5000
        )

    with right:

        employment = st.selectbox(
            "💼 Employment Type",
            [
                "Salaried",
                "Self Employed",
                "Business",
                "Student"
            ]
        )

        amount = st.number_input(
            "💰 Required Loan Amount (₹)",
            min_value=10000,
            max_value=10000000,
            value=300000,
            step=10000
        )

        credit = st.selectbox(
            "📊 Credit Score",
            [
                "700 or above",
                "650 - 699",
                "600 - 649",
                "Below 600"
            ]
        )

    if st.button(
        "🔍 Check My Eligibility",
        use_container_width=True
    ):

        good_credit = credit in [
            "700 or above",
            "650 - 699"
        ]

        eligible = (
            age >= 21
            and income >= 20000
            and amount <= income * 20
            and good_credit
        )

        if eligible:
            st.success(
                "✅ You may be eligible for "
                + loan_type
            )
            st.write(
                "Your basic income, age and credit range "
                "meet the project criteria."
            )
        else:
            st.error(
                "❌ You may not meet the basic eligibility criteria."
            )
            st.write(
                "Try reducing the loan amount or check "
                "your income and credit information."
            )

    st.warning(
        "⚠️ This is an educational project. "
        "Actual loan approval depends on the bank, "
        "credit history, income and documents."
    )

# =========================
# ACCOUNT BALANCE
# =========================

if menu == "💰 Account Balance":

    st.header("💰 Account Overview")

    st.markdown("""
    <div class="hero">
        <h2>💳 Savings Account</h2>
        <p>Account Status: 🟢 Active</p>
        <h1>₹42,500</h1>
        <p>Available Balance</p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("📋 Recent Transactions")

    transactions = [
        "🟢 Salary Credit ............ +₹30,000",
        "🔴 Shopping ................. -₹2,500",
        "🔴 Electricity Bill ......... -₹1,200",
        "🔴 Food ..................... -₹800",
        "🟢 Cashback ................. +₹500"
    ]

    for transaction in transactions:
        st.write(transaction)

    st.info(
        "🔐 Demo account information. "
        "No real bank account is connected."
    )

# =========================
# EMI CALCULATOR
# =========================

if menu == "💳 EMI Calculator":

    st.header("💳 Loan EMI Calculator")

    st.write(
        "Find out how much you may need to pay every month."
    )

    amount = st.number_input(
        "💰 Loan Amount (₹)",
        min_value=10000,
        max_value=10000000,
        value=300000,
        step=10000
    )

    rate = st.number_input(
        "📈 Annual Interest Rate (%)",
        min_value=1.0,
        max_value=30.0,
        value=8.5,
        step=0.5
    )

    years = st.number_input(
        "📅 Loan Duration (Years)",
        min_value=1,
        max_value=30,
        value=5
    )

    if st.button(
        "🧮 Calculate EMI",
        use_container_width=True
    ):

        monthly_rate = rate / 1200
        months = years * 12

        emi = (
            amount
            * monthly_rate
            * (1 + monthly_rate) ** months
            / ((1 + monthly_rate) ** months - 1)
        )

        total_payment = emi * months
        total_interest = total_payment - amount

        st.subheader("📊 Your Loan Summary")

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "💳 Monthly EMI",
            f"₹{emi:,.0f}"
        )

        c2.metric(
            "📈 Total Interest",
            f"₹{total_interest:,.0f}"
        )

        c3.metric(
            "💰 Total Payment",
            f"₹{total_payment:,.0f}"
        )

        st.success(
            f"🎯 Estimated monthly payment: ₹{emi:,.0f}"
        )

# =========================
# AI DOCUMENT ASSISTANT
# =========================

if menu == "📄 AI Document Assistant":

    st.header("📄 AI Bank Document Assistant")

    st.write(
        "Upload a banking document and ask questions about it."
    )

    file = st.file_uploader(
        "📤 Upload a TXT document",
        type=["txt"]
    )

    if file is not None:

        document = file.read().decode("utf-8")

        st.success(
            f"✅ {file.name} uploaded successfully!"
        )

        if st.button(
            "⚙️ Process Document",
            use_container_width=True
        ):

            with st.spinner("Processing document..."):

                model = SentenceTransformer(
                    "all-MiniLM-L6-v2"
                )

                database = chromadb.PersistentClient(
                    path="banking_database"
                )

                collection = database.get_or_create_collection(
                    name="banking_documents"
                )

                chunks = []

                for i in range(0, len(document), 800):
                    chunks.append(
                        document[i:i + 800]
                    )

                embeddings = model.encode(
                    chunks
                ).tolist()

                ids = [
                    file.name + "_" + str(i)
                    for i in range(len(chunks))
                ]

                collection.upsert(
                    documents=chunks,
                    embeddings=embeddings,
                    ids=ids
                )

            st.success(
                "✅ Document processed successfully!"
            )

        st.markdown("---")

        question = st.text_input(
            "🔎 What would you like to know?"
        )

        if st.button(
            "🤖 Ask AI",
            use_container_width=True
        ):

            if not question.strip():

                st.warning(
                    "⚠️ Please enter a question."
                )

            else:

                with st.spinner(
                    "🤖 AI is finding the answer..."
                ):

                    model = SentenceTransformer(
                        "all-MiniLM-L6-v2"
                    )

                    database = chromadb.PersistentClient(
                        path="banking_database"
                    )

                    collection = database.get_or_create_collection(
                        name="banking_documents"
                    )

                    embedding = model.encode(
                        [question]
                    ).tolist()

                    result = collection.query(
                        query_embeddings=embedding,
                        n_results=3
                    )

                    context = "\n".join(
                        result["documents"][0]
                    )

                    prompt = (
                        "You are a helpful banking assistant. "
                        "Answer only using the document information. "
                        "Do not invent information. "
                        "If the answer is unavailable, say so.\n\n"
                        "DOCUMENT:\n"
                        + context
                        + "\n\nQUESTION:\n"
                        + question
                    )

                    response = ollama.chat(
                        model="llama3.2:3b",
                        messages=[
                            {
                                "role": "user",
                                "content": prompt
                            }
                        ]
                    )

                st.subheader("🤖 AI Answer")

                st.markdown(
                    f"""
                    <div class="ai-answer">
                        <div class="ai-title">
                            🤖 SmartBank AI
                        </div>
                        <div class="ai-text">
                            {response["message"]["content"]}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

    else:

        st.info(
            "📤 Upload a TXT banking document to begin."
        )

# =========================
# FOOTER
# =========================

st.markdown("---")

st.caption(
    "🏦 SmartBank | Streamlit + ChromaDB + "
    "Sentence Transformers + Ollama 🤖"
)