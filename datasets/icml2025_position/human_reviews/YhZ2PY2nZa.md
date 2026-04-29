## Human Reviewer 1

### Questions
No further questions.

### Rating
4

### Confidence
4

---

## Human Reviewer 2

### Questions
- Can you explain more about how different priors affect Bayesian credible intervals in LLM evaluations?
- How do the new methods work with bigger data and more complex models? What problems might come up; how can we fix them?
- In your tests, did you find any cases different from your claims where even the suggested methods didn't work well? (If yes, how can these issues be solved?)

### Rating
3

### Confidence
3

---

## Human Reviewer 3

### Questions
1. Explore the sensitivity of the proposed methods to different hyperparameter choices, especially for the Bayesian models. A more detailed sensitivity analysis would help readers understand how robust the methods are under various prior specifications.

2. A comprehensive table summarizing the pros, cons, and performance metrics (e.g., coverage, interval width, computational cost) of each method across different scenarios would provide a clear comparative overview for practitioners.

### Rating
3

### Confidence
2

---

## Human Reviewer 4

### Questions
In practice, I rarely see people report confidence intervals (or credible intervals) and compare their performance only with the sample average of metrics like accuracy. This paper shows a good direction for improving results reporting and offers a simple formula and code. Could you provide a concrete application of the proposed position in LLM evaluation benchmarks?

What would be the limitation of applying this kind of statistical inference on LLM evaluations? 

There is a popular metric that reports accuracy up to K results. Namely, if a model contains a correct output with K generations. In this scenario, what would be a good way to apply the proposed approach?

### Rating
5

### Confidence
4