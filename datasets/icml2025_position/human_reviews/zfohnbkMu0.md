## Human Reviewer 1

### Questions
1) What are the risks that Sigstore can completely or partially mitigate? What are its limitations?

2) What are the requirements to apply the training dataset verifiability method proposed in Section 5 and in which practical contexts can it be applied?

3) Following the previous question, it would be good to know more about the robustness of the method against minor manipulations on the training data points to evade detection.


***************** POST-REBUTTAL COMMENTS **********************
Thank you very much for your responses and clarifications. They've been very helpful and clarified some of my concerns. Thus, I'm increasing my score.

### Rating
3

### Confidence
3

---

## Human Reviewer 2

### Questions
1. How does Sigstore compare to other potential solutions for ML supply chain security in terms of robustness, scalability, and ease of adoption?

2. Can the authors provide a more detailed analysis of how Sigstore mitigates each of the attacks outlined in Figure 1 and Section 2?

### Rating
3

### Confidence
4

---

## Human Reviewer 3

### Questions
1. Presumably, hugging face implemented commit signing instead of model signing because the latter was more complex to implement. What exactly were the main hurdles with traditional ways of implementing model signing in a pre-Sigstore model?
2. What scaling hurdles would Sigstore signing primarily face when dealing with models even larger than Llama-3.1-405B?

### Rating
5

### Confidence
3

---

## Human Reviewer 4

### Questions
- While your approach allows for dataset verification, how can we enforce data transparency without violating privacy laws?
- Could an attacker circumvent the signing process by creating convincing fake models with seemingly valid signatures?

### Rating
3

### Confidence
3