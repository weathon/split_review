# Calibrating Expressions of Certainty

- Decision: Accept
- Scores: 5, 6, 8, 6

## Abstract
We present a novel approach to calibrating linguistic expressions of certainty, e.g., ``Maybe'' and ``Likely''. Unlike prior work that assigns a single score to each certainty phrase, we model uncertainty as distributions over the simplex to capture their semantics more accurately. To accommodate this new representation of certainty, we generalize existing measures of miscalibration and introduce a novel post-hoc calibration method. Leveraging these tools, we analyze the calibration of both humans (e.g., radiologists) and computational models (e.g., language models) and provide interpretable suggestions to improve their calibration.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper proposed a method to calibrate expressions of uncertainty in LLM generations. Instead of treating each uncertainty phrase as a probabilistic score between $[0, 1]$, this paper proposed that they be mapped to a distribution, expressed as a probability simplex. Under this formulation, calibration is reduced to a problem of learning an optimal transport. The authors conducted experiments over a curated dataset of radiologists, finding that their proposed method is comparable to baseline methods.

### Strengths
- By considering confidence as a probabilistic simplex, the formulation of calibration as an instance of optimal transport is interesting.

### Weaknesses
 - Some experimental setup are unclear. See below.
 - Table 1: The proposed method's improvement is marginal, or even non-existent as compared to baseline calibration methods such as Platt scaling and histogram binning. This does not justify the usefulness of your proposed method.

### Questions
- L265: $\triangle_{K-1}$: The general notation for the probabilistic simplex should be $\Delta^{K-1}$.
 - L420: I am dubious of LLMs' ability to generate a sequence like `Beta(2, 3)` that accurately reflects its internal belief. How many exemplars are used in the in-context learning? This is not spelled out clearly in the Appendix. (It seems that only 1 example is used?)

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a novel miscalibration measure that incorporates a flexible, user-defined distribution for each bin, enabling a supervised "soft binning" approach. The authors propose this generalization to address the ambiguity in verbalized uncertainty levels, such as "unlikely" or "likely," which may not correspond to specific probability values. Additionally, the paper presents a post-hoc calibration method to adjust the use of uncertainty phrases based on the true distribution associated with each phrase. Experimental results on CT reports and outputs from language models demonstrate that the proposed miscalibration metric offers additional information of both human and language model usage of uncertainty phrases, and that the post-hoc calibration technique effectively refines the usage of these uncertainty phrases.

### Strengths
- Interesting proposal that uncertainty phrases could be associated with a distribution instead of a single confidence score.
- Very clear presentation of the method and insightful comparison against existing work.

### Weaknesses
 - The link to uncertainty phrases seems superficial, as they serve merely as names for distributions without strong justification for this treatment.
- The motivation to represent uncertainty phrases as distributions is unclear; individual users often interpret these phrases in consistent orders, making scalar values (or simple binning) potentially sufficient. At a population level, it’s unclear why uncertainty phrases should align with complex empirical distributions rather than a straightforward rubric. In fact, it seems that using scalar values or distinct, non-overlapping probability regions might be a simpler and more operational approach.
- Limited Application: Only works for fixed uncertainty phrases in isolation, does not work with free-form generation with flexible uncertainty quantifiers.
- From table 1, the method does not seem to perform better than simpler post-hoc calibration methods that do not require confidence distribution.
- **NOTE** formula 6 is well outside the margin limit, please fix.

### Questions
- In the captions for Figure 4 and Table 1, the authors highlight the interpretability and informativeness of their calibration methods. However, the proposed post-hoc calibration method seems to make the calibration map less intuitive (e.g., Figure 3). Could the authors clarify how their methods enhance human interpretability, given the challenges of conceptualizing uncertainty as a distribution?
- It’s unclear how the ground truth uncertainty distribution is determined. The authors experimented with various methods to derive density functions for each confidence distribution, but it remains unclear which is best. Table 3 and Figure 5 suggest that the choice of ground truth density function impacts evaluation results. How can these ground truth density functions be reliably collected?
- In the "Calibrating Radiologists" experiments, confidence labels are extracted using Llama 3 (line 320 - 321), rather than from the radiologists' own report-level confidence labels. If this is correct, the analysis in Section 4.2 attributing uncertainty phrases to radiologists seems problematic. Could the authors clarify how this experiment was conducted?

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper measures and calibrate expressions of certainty made in natural language (e.g., likely, unlikely). By treating certainty phrases
as distributions over the probability simplex, the authors generalize existing estimators for miscalibration metrics, such as the expected calibration error. The work has real-world implications in fields like radiology.

### Strengths
- A good understanding and presentation of the existing literature on calibration.
- Using confidence distributions makes the proposed estimator more robust to increasing the number of bins.
- Propose a novel framing of calibration as a composition of source confidence distributions, an optimal transport map to target confidence distributions, and an indexing function.
- Provides potential real-world use cases, such as calibrating human expressions of uncertainty in medicine and LLM expressions of uncertainty.

### Weaknesses
 - The paper focuses on binary classification, which could make its impact limited.
- Conversely, the relative complexity of the approach to non-statisticians could limit its adoption.
- The candidate confidence distributions could in practice be very large, which could make some of the optimization problems very slow to solve.

### Questions
In practice, if humans are already mentally correcting for the under/over-estimation of expressed uncertainty (either by a doctor or LLM), couldn't such calibration lead to worse outcomes, since their mental models no longer apply while the calibrated expressions are still not perfect? This is more of a human problem than a technical one, but just a thought.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper describes a novel approach to calibrate certainty phrases directly instead of first mapping these phrases to an explicitly confidence score and next calibrating these scores. The method uses probability distributions from a data set with expressions and confidence scores to find a “translation” mapping. The model is tested on radiology reports with human descriptions and on Q&A tasks for LLMs. Their approach performs similar to the traditional methods that use indirect mappings. The main advantage is that their approach uses a direct mapping from certainty phrase to certainty phrase representing global value ranges.

### Strengths
- calibration method that does not require an explicit mapping from phrase to score
- intuitively models peoples use of uncertainty expressions to calibrate for populations
- strong mathematical modeling (as far as I can judge as a non-expert on this)

### Weaknesses
 - the model does not outperform standard SOTA approaches
- the model seems to remove outlier expressions and calibrates to the middle area
- the mathematical modeling is dense and difficult to understand for non-experts
- misses a deeper analysis and clarifying examples about the semantics and use of uncertainty phrases
- introduction promises that it can help radiologists to report more consistently but cannot find and evidence of this in the paper.

### Questions
- the model does not outperform standard SOTA approaches
- the model seems to remove outlier expressions and calibrates to the middle area
- the mathematical modeling is dense and difficult to understand for non-experts
- misses a deeper analysis and clarifying examples about the semantics and use of uncertainty phrases
- introduction promises that it can help radiologists to report more consistently but cannot find and evidence of this in the paper.

### Soundness
3

### Presentation
3

### Contribution
3
