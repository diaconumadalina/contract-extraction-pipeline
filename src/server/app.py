from fastapi import FastAPI, UploadFile, File
from src.extraction.extractor import ContractExtractor
from src.loaders.pdf_loader import load_pdf_text

app = FastAPI(title="Contract Extraction API")

extractor = ContractExtractor()


@app.get("/")
def root():
    return {"message": "Contract Extraction API is running"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/extract-pdf")
async def extract_pdf(file: UploadFile = File(...)):
    content = await file.read()

    import tempfile
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(content)
        tmp_path = tmp.name

    text = load_pdf_text(tmp_path)

    result = extractor.extract(text)
    return result.model_dump()

app = FastAPI(
    title="Contract Extraction API",
    description="Extracts title, parties, clauses and structured metadata from contracts.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)
