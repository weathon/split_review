## Human Reviewer 1

### Questions
- Given the difficulty of obtaining high-quality causal graphs, how do you propose to scale causal integration in machine learning systems where ground truth causal structures are unknown?
- While causality can help disentangle bias sources, do you foresee scenarios where causal fairness approaches still fail to reconcile competing fairness notions?
- Is it possible that sufficiently large models implicitly learn causal structures without explicit causal modeling?

### Rating
4

### Confidence
3

---

## Human Reviewer 2

### Questions
1) In discussing how causal approaches might scale to foundation models, the paper acknowledges “the difficulty of validating causal structures” given large, high-dimensional data. Do the authors have insights into what kind of techniques or verification steps shall be taken to validate causal structures in foundation models?

2) Regarding techniques such as "Causally Fair Language Models," is it feasible (and easy) to be generalized for a wide range of fairness issues, or are they limited to a very specific design target (e.g., demographic neutral)?

3) It is curious for the reviewer whether the term "accuracy" used throughout the manuscript needs to be re-defined differently between traditional ML models and causality models, especially with the author's discussion on "prediction accuracy vs. intervention accuracy"

### Rating
2

### Confidence
5

---

## Human Reviewer 3

### Questions
Can the paper include empirical studies or data to support its theoretical claims, and discussion on real-world implementations?

### Rating
2

### Confidence
3

---

## Human Reviewer 4

### Questions
What are the key challenges in effectively integrating causality in ML models? If the causal structure is not available and the inferred causal structures are not accurate, what are the effective ways to utilize the inaccurate causality in the ML models?

### Rating
1

### Confidence
4