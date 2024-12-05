from langchain_community.document_loaders import CSVLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

def initialize_chatbot():
    """Initialize all components of the chatbot."""
    # Load CSV data
    loader = CSVLoader(file_path="preprocessed_sales_data.csv")
    print("Valid")
    documents = loader.load()

    # Initialize embeddings
    embeddings_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    print("created")
    # Create FAISS index
    vectorstore = FAISS.from_documents(documents, embeddings_model)
    retriever = vectorstore.as_retriever(
        search_type="similarity", 
        search_kwargs={"k": 3}
    )
    print("Vector")
    # Initialize LLM
    model_name = "google/flan-t5-base"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    generator = pipeline(
        "text2text-generation", 
        model=model, 
        tokenizer=tokenizer
    )

    print("loader loaded")
    return retriever, generator
def generate_chatbot_response(retriever, generator, question):
    """Generate a response using the RAG system."""
    # Retrieve relevant documents
    results = retriever.get_relevant_documents(question)
    context = " ".join([doc.page_content for doc in results])

    # Generate response
    input_text = f"Context: {context}\n\nQuestion: {question}\n\nAnswer:"
    response = generator(
        input_text, 
        max_length=200, 
        num_return_sequences=1
    )
    return response[0]["generated_text"]