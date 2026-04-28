# Do LLMs estimate uncertainty well in instruction-following?

- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 8, 1, 8

## Abstract
Large language models (LLMs) could be valuable personal AI agents across various domains, provided they can precisely follow user instructions. However, recent studies have shown significant limitations in LLMs' instruction-following capabilities, raising concerns about their reliability in high-stakes applications. 
Accurately estimating LLMs' uncertainty in adhering to instructions is critical to mitigating deployment risks. We present, to our knowledge, the first systematic evaluation of uncertainty estimation abilities of LLMs in the context of instruction-following.
Our study identifies key challenges with existing instruction-following benchmarks, where multiple factors are entangled with uncertainty stemming from instruction-following, complicating the isolation and comparison across methods and models.
To address these issues, we introduce a controlled evaluation setup with two benchmark versions of data, enabling comprehensive comparison of uncertainty estimation methods under various conditions.
Our findings show that existing uncertainty methods struggle, particularly when models make subtle errors in instruction following. While internal model states provide some improvement, they remain inadequate in more complex scenarios. 
The insights from our controlled evaluation setups provide crucial understanding of LLMs' limitations and potential for uncertainty estimation in instruction-following tasks, paving the way for more trustworthy AI agents.\footnote{We will release the data and code on GitHub upon publication.}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper evaluates how well LLMs can estimate uncertainty when tasked with instruction following, given that existing research largely focuses on uncertainty in factuality. The authors systematically evaluate the uncertainty estimation methods using the IFEval dataset and further introduce a new benchmark to disentangle the multiple factors. Experimental results highlight the potential of self-evaluation and probing methods, though they still fall short under difficult conditions, underscoring the need for further research on uncertainty estimation.

### Strengths
1. The authors provide a systematic evaluation, identifying multiple factors that affect uncertainty estimation and are entangled within naturally generated responses, which helps isolate the influence of various factors and allows for a more accurate assessment of estimation methods' capabilities.
2. The study offers thorough comparisons between different uncertainty estimation methods, various LLMs, and distinct datasets.

### Weaknesses
1. The Probe method is mentioned in Table 4 and highlighted as the best-performing method. However, it is not introduced or discussed in Section 3, leading to some confusion when comparing results in Section 3.2.1. A clearer explanation of this method earlier in the paper would improve the comprehensibility of the findings. Or at least keep the scope of methods consistent when discussing "best-performing".
2. As noted by the authors in their limitations section, the types of instructions included in the benchmark may not comprehensively reflect real-world tasks. Additionally, the dataset size is relatively small, potentially impacting the reliability of the benchmark.

### Questions
1. Could you please provide more details in benchmark data generation process? For example, what's the prompt for generating correct response in controlled version, and natural response in realistic version? What are the domains for the arguments (e.g., Type, Kwargs) in the prompts? Are these parameters inherited from IFEval?
2. It seems that all the token length distributions are not normalized by the total number of total number of responses in each class (Figure 2, 3, and 10). Or to say, the total numbers of correct and incorrect responses are not the same, which means you may not draw a conclusion that incorrect responses tend to be longer than correct ones when only seeing that the orange curve is significantly higher than the blue curve on larger tokens. Normalizing the distribution would be better, though it may not affect the conclusions that token lengths introduce biases.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents a first of its kind systematic evaluation of uncertainty estimation methods in instruction-following tasks, identifies key challenges in existing datasets and introduce two new benchmark datasets created to address those challenges. The results indicate that there is still a gap in the uncertainty estimation performance of common LLMs, especially when the errors made by the model are subtle. On top of this, internal model states, particularly the middle hidden layers, show an improvement but still remain unsatisfactory in complex scenarios. The main contributions and the motivation are presented clearly, with experiments performed on multiple LLMs and datasets.

### Strengths
- the paper introduces new benchmark datasets (Controlled and Realistic versions) that isolate factors influencing uncertainty estimation in instruction-following, filling an existing research gap.
- the methodologies employed are rigorous, with comprehensive experimental setups involving multiple LLMs and uncertainty estimation techniques.
- the writing is clear, and the results are presented in a way that is easy to follow, supported by well-designed figures and tables.
- the findings offer valuable insights for advancing the field, particularly the observation that models’ internal states can be leveraged for improved uncertainty estimation.

### Weaknesses
 - the analysis might benefit from extending the scope of instruction types and domains included in the benchmark to cover more diverse real-world tasks
- while the paper identifies the use of internal states for uncertainty estimation as promising, it falls short in exploring more sophisticated methods that could leverage this information in nuanced tasks
- the use of GPT-4 for task quality assessment introduces a potential risk of pre-training overlap affecting the evaluation, though this is acknowledged as a limitation

### Questions
1. Can the authors elaborate on how training procedures like RLHF can affect the models' performance in uncertainty estimation, especially in Controlled-Hard tasks?
2. Are there potential methods beyond linear probing that could better utilize internal model states for uncertainty estimation in nuanced tasks?
3. Would expanding the evaluation to include LLM agents provide more comprehensive insights?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
3

### Summary
This paper evaluates the uncertainty estimation abilities of LLMs in instruction-following tasks. It introduces a controlled evaluation setup with two benchmark versions to isolate and compare methods under various conditions. Findings reveal that existing uncertainty methods struggle, especially with subtle errors, and that internal model states provide some improvement but remain inadequate in complex scenarios.

### Strengths
The study provides crucial insights into LLMs's uncertainty estimation in instruction-following problems.

### Weaknesses
1. The paper relies on a single IFEval for its initial evaluation. It would be beneficial to include additional datasets to validate the findings across different contexts and domains.
2. The paper raises many novel concepts and findings, but it does not seem to provide much direct help in enhancing instruction-following capabilities.
3. The article did not use LLMs larger than 13B in its tests, so the conclusions may not be sufficient.

### Questions
The study provides valuable insights into the limitations of LLMs in estimating uncertainty during instruction-following tasks. Given these findings, could you elaborate on specific strategies or methodologies that could be implemented to enhance the instruction-following accuracy of LLMs?

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper studies uncertainty in instruction following, an important topic for interpretability and trustworthiness. It reveals the discrepancy between accuracy and uncertainty estimation, and among different uncertainty estimation methods themselves. It also accentuates the entanglement problem between instruction following and task completion.

Then the paper proposed a new benchmark separating control and realistic inferences, and shared more findings. IMO the most crucial one is that probe-based method provides the best estimation.

### Strengths
This paper reveals the uncertainty challenges faced by today's LLMs and presents new methods to better gauge LLM ability to estimate its own uncertainty. I think this is a timely work raising awareness to the community.

I'm not surprised by the top performance of probe-based method because internal states do not lie. Unclaimed by the authors, but the paper hints at open models' advantages to critical tasks, because its white box properties welcome scrutiny and checking by anyone. IMO internal states should be accessible by read APIs.

### Weaknesses
The poor uncertainty estimation by modern LLM is also not surprising because of its strong alliance with MLE methodology instead of MAP. Therefore, besides future directions outlined by authors, I strongly suggest trying more inference methods other than greedy, e.g. setting temperature, beam search, etc. These are also tunable parameters to closed-source models. This way you can measure closed models although the insights will be limited.

Besides trying more inference method, please also consider impact of regularization such as dropout rate if you plan to do any pre- or post-training works. This reveals another problem which is training details are not sufficiently exposed even for open LLMs.

### Questions
Besides trying more inference method, please also consider impact of regularization such as dropout rate if you plan to do any pre- or post-training works. This reveals another problem which is training details are not sufficiently exposed even for open LLMs.

### Soundness
4

### Presentation
3

### Contribution
3
