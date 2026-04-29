## Human Reviewer 1

### Questions
The authors point out that forgetting certain training data points remains limited in real-world applications and advocate for knowledge-tracing unlearning. However, the unlearning of knowledge, rather than specific data points, has already been explored in the context of language foundation models. For example, Qiu et al. [1] highlight that real data are not always independent and propose unlearning inter-connected knowledge, which extends beyond simple deletion to structural deletion. Similarly, Liu et al. [2] expand LLM unlearning to include the removal of unwanted model capabilities, going beyond the traditional focus on privacy-related data removal. For instance, unlearning knowledge in English-only examples should also ensure the same knowledge is forgotten when conveyed in other languages. In summary, advocating for unlearning knowledge instead of specific data is no longer a novel idea.

Instead, the interesting aspect is that the boundaries of unlearning knowledge are unlimited and difficult to quantify. This is because we cannot collect all the knowledge or examples related to a specific concept, such as "ImageNetDogs" mentioned in the paper. Therefore, rather than merely advocating for knowledge-tracing unlearning, a more fascinating position would be to explore how to quantify the knowledge or capabilities that should be unlearned.

References

[1] PISTOL: Dataset Compilation Pipeline for Structural Unlearning of LLMs. Xinchi Qiu et al.

[2] Rethinking Machine Unlearning for Large Language Models. Sijia Liu et al.

### Rating
2

### Confidence
4

---

## Human Reviewer 2

### Questions
1. What's the authors' opinion about the potential of repeated unlearning of overlapping concepts degrading model performance in unintended ways?
2. What would the knowledge-level evaluation metrics be like?

### Rating
3

### Confidence
3

---

## Human Reviewer 3

### Questions
- Could the authors elaborate on how the exemplar images for the forgetting set are selected and validated? Specifically, how do they ensure they accurately capture the targeted knowledge for unlearning?
- Could the authors clarify any limitations or scenarios where the knowledge-tracing approach might be less effective compared to traditional data-tracing methods?

### Rating
3

### Confidence
4

---

## Human Reviewer 4

### Questions
In the current discussion, it seems at the core of machine unlearner with a knowledge-tracing interface, still lies data-tracing machine unlearning techniques. Do the authors expect to see techniques that are "natively" designed for knowledge-tracing machine unlearning, without relying on selecting proper f/r datasets and applying data-tracing MU techniques?

### Rating
3

### Confidence
3