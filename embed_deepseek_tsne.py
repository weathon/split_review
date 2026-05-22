import os
import pickle
import numpy as np
from dotenv import load_dotenv
from datasets import load_from_disk
from openai import OpenAI
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

load_dotenv()

ds = load_from_disk("datasets/iclr2026_model_reviews_hf")
ds = ds.filter(lambda x: x["review_model"] == "deepseek_flash")
reviews = [str(r) for r in ds["paper_review"]]
scores = np.array(ds["gt_avg_score"], dtype=float)
print(f"{len(reviews)} deepseek reviews")

client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=os.environ["OPENROUTER_API_KEY"])

cache = "deepseek_embeddings.pkl"
if os.path.exists(cache):
    with open(cache, "rb") as f:
        embeddings = pickle.load(f)
    print(f"loaded {len(embeddings)} cached embeddings")
else:
    embeddings = []
    B = 32
    for i in range(0, len(reviews), B):
        batch = reviews[i:i + B]
        resp = client.embeddings.create(model="google/gemini-embedding-2-preview", input=batch, encoding_format="float")
        embeddings.extend([d.embedding for d in resp.data])
        print(f"embedded {len(embeddings)}/{len(reviews)}")
    embeddings = np.array(embeddings)
    with open(cache, "wb") as f:
        pickle.dump(embeddings, f)

embeddings = np.array(embeddings)
print("embeddings shape:", embeddings.shape)

xy = TSNE(n_components=2, random_state=0, perplexity=30, init="pca").fit_transform(embeddings)

plt.figure(figsize=(9, 7))
sc = plt.scatter(xy[:, 0], xy[:, 1], c=scores, cmap="viridis", s=18)
plt.colorbar(sc, label="gt_avg_score")
plt.title("t-SNE of DeepSeek review embeddings")
plt.xlabel("t-SNE 1")
plt.ylabel("t-SNE 2")
plt.tight_layout()
plt.savefig("deepseek_tsne.png", dpi=150)
print("saved deepseek_tsne.png")
