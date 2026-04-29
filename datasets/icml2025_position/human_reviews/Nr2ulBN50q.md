## Human Reviewer 1

### Questions
•	Should the initial causal assumptions, such as ignorability, independence, and diffeomorphism, also be explicitly stated in advance, in addition to the five elements that need to be clarified in synthetic experiments in Section 4.2?

•	Regarding Sections 4.2 and 4.3, are there any open-source repositories that enable researchers to specify any causal DAG structures along with generation algorithms to model causal relationships and generate synthetic data accordingly? If not, this could be a promising direction for future research.

### Rating
4

### Confidence
3

---

## Human Reviewer 2

### Questions
- The main challenge might be that real world scenarious are quite complicated and it is difficult to capture this in an experiment. What would be your recomendations for this?
- Currently methods for sensitivity analysis in causal models are developed. Could this be an alternative to support the adoption of causal ML?

### Rating
3

### Confidence
5

---

## Human Reviewer 3

### Questions
- Why did you only choose RealCause and not consider other generative algorithms?
- Did you evaluate the MSE of the estimators across different monte carlo iterations from RealCause? 
- RealCause asks authors to ensure the generated data distribution is not different than the original empirical data distribution: did you do this? I did not see it reported anywhere, and this behavior could explain why RealCause's geneated ATEs are vastly different than the true ATE.

### Rating
3

### Confidence
3

---

## Human Reviewer 4

### Questions
Questions:
- Within the ICML community, who do the authors consider to be the primary audience for this position paper?
- Could you please clarify precisely *by whom* the broader adoption of causal ML methods is desired, and how the paper substantiates why the proposed principles will lead to broader adoption?
- The paper argues that one should focus on synthetic benchmarks because e.g. semi-synthetic benchmarks have factors fundamentally outside the control of the experimentalist. However, the design space identified by the authors is massive. Thus, a counter-argument could be that semi-synthetic setups “make some of the choices” for the designer based on real data, allowing the user to focus on fewer aspects. The consequences of those ‘choices by nature’ can still be analysed as done in prior works and this paper. Given this and the context of needing to incorporate sufficient realism, why do the authors take the position of focusing on only synthetic experiments?

### Rating
3

### Confidence
4