- Decision: Reject
- Scores: 3, 5, 5

## Merged Review

### Summary
The paper proposes IsoCLR, a contrastive learning method for RNA representation learning that uses functional similarities between alternatively spliced isoforms and homologous genes to construct positive pairs (adapted from SimCLR). It is validated on three downstream tasks (RNA half-life, mean ribosome load, Gene ontology) via linear probing, showing strong performance especially in low-data regimes.

### Strengths
- The paper is well written and easy to follow.
- The idea of using functional similarities from alternative splicing and gene duplication to form positive pairs for contrastive learning is sound and novel in the application domain.
- Simple yet effective, achieving strong empirical performance compared to baselines (e.g., up to two-fold Pearson correlation improvement in low-data settings).
- Potential application in biomedicine for RNA property prediction.

### Weaknesses
- Limited novelty: the key contribution is applying contrastive learning (SimCLR) to RNA with a specific positive pair construction; there is little innovation in the machine learning algorithm itself. The work is more suitable for a biomedicine audience than the general ML community.
- The evaluation is narrow:
  - Only three downstream datasets are used, with Gene ontology results partially reported in the appendix.
  - The tasks (half-life, ribosome load) are relatively easier; more crucial tasks such as RNA secondary structure, contact prediction, or 3D structure prediction are not evaluated, whereas baselines like RNA-FM have demonstrated effectiveness on structural predictions.
- The practical utility of the learned representations is questionable: if all downstream tasks can be solved with standard fine-tuning, better embeddings do not provide a clear advantage (no retrieval-style application shown). It is unclear what benefit the proposed model offers over specialized predictors like Saluki, given that it has more parameters yet performs comparably (or worse in linear probing) than Saluki.
- Several experimental concerns weaken the empirical analysis:
  - The comparison with pre-trained DNA models (NT, DNA-BERT2) may be unfair if sequences are simply converted (U→T) without accounting for different training corpora.
  - The proposed model and Saluki may use additional information beyond the sequence (e.g., splicing patterns), making comparisons with sequence-only baselines potentially unfair.
  - Baselines such as RNA-FM, NT, and DNA-BERT2 are evaluated only via linear probing; fine-tuning results are missing. Since these models are not too large to fine-tune, this omission weakens the claim of superiority.
- There is disagreement among reviewers: one reviewer (score 3) found the contributions limited and the tasks less impactful, while two reviewers (score 5) were more positive on the empirical results and idea.