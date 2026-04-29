## Human Reviewer 1

### Questions
There are no further questions.

### Rating
4

### Confidence
3

---

## Human Reviewer 2

### Questions
N/A

### Rating
1

### Confidence
4

---

## Human Reviewer 3

### Questions
Could you address the issue mentioned in the detailed review?

### Rating
2

### Confidence
4

---

## Human Reviewer 4

### Questions
•	In the Hyperbolic HKG pipeline, the knowledge entities are embedded into hyperbolic space, how are they applied to LLM queries? Figure 1 indicates that the LLM invokes the Vector DB for query retrieval. However, the LLM itself employs Euclidean space embedding for token training and learning, and the output results are natural text sequences; whereas hyperbolic embedding represents standardized knowledge entities. So, how does the entire pipeline establish the association from natural text sequences to standardized knowledge entities? If the encoder for hyperbolic embedding is reused, how does the pipeline achieve the transition from Euclidean space embedding to hyperbolic space embedding?

•	In the Vector DB query retrieval section, the similarity calculation is not clearly explained. Is it based on hyperbolic space geodesic distance, or does it still use Euclidean space cosine distance? Furthermore, in hyperbolic space, the entailment relationship can more intuitively depict the hierarchy among knowledge entities and measure the semantic correlation between entities. Has this aspect been considered?

•	In the hyperbolic embedding section, the paper introduces the hyperbolic manifold of the Poincaré disk, but it exhibits numerical instability during modeling and learning. In recent years, many studies have adopted the Lorentzian manifold for embedding learning. It is suggested that the authors include more discussions on hyperbolic embedding.

•	In medical knowledge graphs, there exist complex relationships among various entities, such as those between major diseases and subgroups, relationships within the same subgroup of diseases, causal relationships between diseases, and relationships between diseases and symptoms. From the perspective of semantic relationships, these can be viewed as hyponymy, synonymy, entailment, etc. Current hyperbolic embedding primarily focus on modeling entailment relationships. In the face of the challenges posed by knowledge graphs with complex semantic relationships, have the limitations and opportunities of hyperbolic modeling been considered and discussed?

•	In recent years, hyperbolic modelling has also been used in the modeling of medical data, such as image-text representation learning and knowledge enhancement. Compared to these works, have the differences and innovations of this work been discussed?"

### Rating
3

### Confidence
5