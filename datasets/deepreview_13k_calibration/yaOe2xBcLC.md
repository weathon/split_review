# NoVo: Norm Voting off Hallucinations with Attention Heads in Large Language Models

- Decision: Accept
- Avg Score: 6.00
- Scores: 5, 8, 5

## Abstract
Hallucinations in Large Language Models (LLMs) remain a major obstacle, particularly in high-stakes applications where factual accuracy is critical. While representation editing and reading methods have made strides in reducing hallucinations, their heavy reliance on specialised tools and training on in-domain samples, makes them difficult to scale and prone to overfitting. This limits their accuracy gains and generalizability  to diverse datasets. This paper presents a lightweight method, Norm Voting (NoVo), which harnesses the untapped potential of attention head norms to dramatically enhance factual accuracy in zero-shot multiple-choice questions (MCQs). NoVo begins by automatically selecting truth-correlated head norms with an efficient, inference-only algorithm using only 30 random samples, allowing NoVo to effortlessly scale to diverse datasets. Afterwards, selected head norms are employed in a simple voting algorithm, which yields significant gains in prediction accuracy. On TruthfulQA MC1, NoVo surpasses the current state-of-the-art and all previous methods by an astounding margin---at least 19 accuracy points. NoVo demonstrates exceptional generalization to 20 diverse datasets, with significant gains in over 90\% of them, far exceeding all current representation editing and reading methods. NoVo also reveals promising gains to finetuning strategies and building textual adversarial defence. NoVo's effectiveness with head norms opens new frontiers in LLM interpretability, robustness and reliability.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces Norm Voting (NoVo), a lightweight method designed to reduce hallucinations in LLMs using attention head norms. 

- Norm Voting automatically selects attention head norms that correlate with truth using a simple, inference-only algorithm that operates efficiently with just 30 random samples.
- These selected norms are then used in a straightforward voting algorithm, enhancing the model's prediction accuracy by treating head norms as an ensemble of weak learners.

NoVo's approach avoids reliance on specialized tools or in-domain training, making it scalable and generalizable. The method achieves state-of-the-art performance on the TruthfulQA MC1 benchmark, surpassing previous methods by at least 19 accuracy points. Additionally, NoVo demonstrates strong generalization across 20 diverse datasets, significantly outperforming existing representation editing and reading techniques, and showcasing its robustness in improving LLM factual accuracy.

### Strengths
- NoVo is designed to be lightweight and does not require specialized tools, in-domain training, or external resources. This simplicity allows it to scale effortlessly across diverse datasets and applications, making it practical for real-world deployment.

- The method achieves remarkable accuracy gains, notably setting a new state-of-the-art on the TruthfulQA MC1 benchmark with a 19-point improvement over existing approaches. This demonstrates the effectiveness of NoVo in addressing the critical issue of hallucinations in LLMs.

- NoVo exhibits exceptional generalizability, achieving significant accuracy improvements on over 90% of the 20 diverse datasets evaluated. This indicates the method’s robustness and versatility in handling a wide range of tasks beyond just one specific dataset or domain.

### Weaknesses
 - While the paper presents detailed analysis and shows impressive gains across benchmarks, the applicability of the solution beyond the MCQ type of problems is not obvious.
- The motivation to solve MCQ type questions is not clear. Why is it very important to solve?

- Authors claim "Hallucinations in Large Language Models (LLMs) remain a major obstacle, particularly in high-stakes applications where factual accuracy is critical". Are the benchmarks used in this study representative of the same?

We see models being adopted to simple applications that involve RAG, QnA etc. or more complex Agentic use cases that involve abilities like function calling, planning etc.

It is not very clear how the benchmarks help in high-stakes applications and it i very difficult assess the impact of the work.

Another question that arises is - how critical is MCQ based tasks? should we even solve it?

### Questions
Authors claim "Hallucinations in Large Language Models (LLMs) remain a major obstacle, particularly in high-stakes applications where factual accuracy is critical". Are the benchmarks used in this study representative of the same?

We see models being adopted to simple applications that involve RAG, QnA etc. or more complex Agentic use cases that involve abilities like function calling, planning etc.

It is not very clear how the benchmarks help in high-stakes applications and it i very difficult assess the impact of the work.

Another question that arises is - how critical is MCQ based tasks? should we even solve it?

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
* The authors propose a simple, novel technique to improve LLM factual accuracy. They first find truth-correlated attention head norms, then ensemble these with majority voting at inference time to choose answers to MC questions.  
* The authors conduct comprehensive experiments on a diverse range of datasets and use several different models. On many datasets they find massive effects from their intervention, improving on sota by 20+ percentage points in some cases.

### Strengths
* Empirical results are strong and consistent across models, with substantial improvements over previous methods
* The method is simple and cheap, requiring no specialized training or tools.
* Experimental evaluation is comprehensive, testing across 20 diverse datasets. The authors also evaluate generalizability through finetuning and adversarial robustness tests
* Good error analysis that helps understand the method's capabilities and limitations, including detailed investigation of how different voter types contribute and where/why the method fails

### Weaknesses
 * While the method is simple, I find the conceptual motivation unclear. The authors posit that for some heads, the L2 norm is correlated to the truthfulness of a sequence. Why? What makes this a reasonable thing to expect, conceptually?  Specifically, the paper lacks a clear explanation of why the L2 norm of attention head outputs should correlate with truthfulness. Is it simply capturing the magnitude of activation, and if so, why would higher magnitude imply truth?  The connection between the norm and the underlying semantic content is not well-established.
* These experiments are done exclusively on multiple-choice QA datasets, and it seems that it would not be possible to use this method to reduce hallucination in open-ended generation. The method relies on having a set of discrete options to choose from, making it unclear how it would be applied to free-form text generation where there are no pre-defined choices. The paper does not discuss how the norm selection process would work in such a scenario.
* Evaluating on a wider range of models would help provide more confidence in the method, especially testing on currently popular models like Llama 3. The current evaluation is limited to a relatively small set of models, and it's unclear if the results would generalize to other architectures or model sizes. Testing on more diverse models, including those with different training regimes, would be beneficial.

### Questions
* In Table 2, very different results are obtained for CICv1 and CICv2. Is there any explanation for why the results differ so much here, or in general why the results vary so much across datasets?  
* What is the variability of results when using different sets of randomly drawn samples for norm selection?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors propose a novel multiple-choice output strategy named NoVo. NoVo identifies correlations between the norms of attention heads at the choice token position and the the accuracy using a small calibration dataset. They leverage this information to make multiple-choice predictions without relying on log-probabilities. The proposed method outperforms various existing hallucination detection methods across different datasets and models. The authors further analyze the voting heads for deeper insights.

### Strengths
- The authors did a good job of observing the behavior between attention heads and multiple-choice accuracy.
- The figures are well-designed, and the experiments are comprehensive.
- The hallucination detection task is highly relevant and important today.
- NoVo shows impressive results in multiple-choice benchmarks.

### Weaknesses
 - This approach has very limited applicability, being useful only for multiple-choice tasks. Therefore, it should be noted that this is not a generic hallucination reduction technique like existing methods such as Truthx.
- It is unclear what makes attention heads special in this context. Similar experiments could potentially be conducted using MLP layers. 

- The authors only found a correlation between the norms of the heads and truthfulness. However, it is not explained why such a correlation exists or if there is any causal relationship between the two. 
- The direct relationship between the norm of a head and truthfulness is not well-explained. Why should a correlation be expected in the first place? And why use the L2 norm? 
- Out-of-distribution experiments are missing. The authors should conduct experiments where NoVo is calibrated on one dataset and tested on another. 
- I think the authors should choose between two options. They can either convert their observation about norms and truthfulness into a generic algorithm that works for open-ended generations, or they can deeply explore the reasons behind the observed correlation and write an interpretability paper. Another option might be to reformulate the problem as addressing selection bias or improving multi-choice scenarios, similar to [1].

### Questions
see Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2
