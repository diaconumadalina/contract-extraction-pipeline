from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")


def semantic_similarity(a: str, b: str):
    emb_a = model.encode(a, convert_to_tensor=True)
    emb_b = model.encode(b, convert_to_tensor=True)
    return float(util.cos_sim(emb_a, emb_b)[0][0])
