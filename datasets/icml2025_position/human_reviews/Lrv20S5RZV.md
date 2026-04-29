## Human Reviewer 1

### Questions
Please see the weakness section.

### Rating
2

### Confidence
4

---

## Human Reviewer 2

### Questions
I don't have any question.

### Rating
4

### Confidence
3

---

## Human Reviewer 3

### Questions
This position paper is very timely and addresses important research directions for uncertainty quantification in LLM applications. From a practical viewpoint, applying the concept of data and model uncertainty in everyday use cases is difficult. Say we observed multiple samples from LLMs while solving a QA problem. How can we quantify uncertainty? 

If we walk away from a very well-defined theoretical research setting and if we see papers published in recent application-oriented conferences, each research paper defines uncertainty quantification in its way per use case. Sometimes, it is confidence, which is not well-defined, entropy measured in a certain way, probability estimate of correct outcome, calibration error, etc. The lack of a unified view of "what we are solving" is a big problem. This paper addresses this issue, and I agree with this view. It is implied from many existing researches. For example, the underspecification uncertainty is closely related to selective generation. The interactive learning is well connected to RAG. The output uncertainty is also well connected to judge or the conformal prediction research.

Let's say that we want to re-assess UQ for LLM agents.
What will be the scope of such consideration?
Is this mainly applicable to a conversational setting? Do we apply it to comprehension tasks? Do we use it for long-form generation tasks?

Many recent papers consider hallucination, which is also a term that is not well defined. Could you make some connections to the research directions for hallucination and uncertainty quantification?

For each research direction, how can we measure the degree of uncertainty? What are the criteria that we can use to improve or reduce uncertainty?

As mentioned above, the literature addresses those research topics, at least partially, under different categorizations. Should we re-group such problems under the three proposed directions? Could you further justify this position?

### Rating
2

### Confidence
4

---

## Human Reviewer 4

### Questions
How should underspecification uncertainty be quantified? What are the trade-offs between interactive learning and efficiency? How do different user types perceive uncertainty explanations? Could underspecification uncertainty be addressed through prompt engineering?

### Rating
3

### Confidence
3