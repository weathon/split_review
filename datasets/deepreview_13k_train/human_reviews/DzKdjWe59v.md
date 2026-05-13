# Hint Marginalization for Improved Reasoning in Large Language Models

- Decision: Reject
- Scores: 6, 6, 6, 5

## Abstract
Large Language Models (LLMs) have exhibited an impressive capability to perform reasoning tasks, especially if they are encouraged to generate a sequence of intermediate steps. Reasoning performance can be improved by suitably combining multiple LLM responses, generated either in parallel in a single query, or via sequential interactions with LLMs throughout the reasoning process. Existing strategies for combination, such as self-consistency and progressive-hint-prompting, make inefficient usage of the LLM responses. We present Hint Marginalization, a novel and principled algorithmic framework to enhance the reasoning capabilities of LLMs. Our approach can be viewed as an iterative sampling strategy for forming a Monte Carlo approximation of an underlying distribution of answers, with the goal of identifying the mode the most likely answer. Empirical evaluation on several benchmark datasets for arithmetic reasoning demonstrates the superiority of the proposed approach.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper presents a new method called hint marginalisation to improve the reasoning capability of a large language model. The basic idea is to generate multiple responses (possibly in parallel) from the same model or from multiple models and combine in order to steer the model towards the most likely response. Therefore, the proposed approach can be viewed as an iterative sampling scheme to produce a Monte-Carlo approximation of a probability distribution over the responses where the mode of the distribution corresponds to the most likely response. The empirical evaluation is carried out on several reasoning tasks using OpenAI GPT models. The results demonstrate conclusively that the proposed hint marginalisation scheme improves the reasoning capabilities of the models considered.

### Strengths
- Improving the reasoning capabilities of existing language models is definitely a topic of considerable interest in the AI community. The proposed approach seems to address this issue in a principled manner. 

- The quality of the presentation is overall quite good and therefore the paper is relatively easy to follow even by readers outside this research area. Most of the technical details presented in the paper are discussed in a relatively clear manner. The examples provided throughout the paper help to get a better understanding of the proposed scheme.

### Weaknesses
 - Most modern LLMs, especially those from the OpenAI GPT family do fairly well on arithmetic reasoning problems and therefore the improvements shown in Table 1 are marginal (typically less than 1%). Perhaps considering other reasoning tasks would better highlight the benefits of the proposed approach.

- I was surprised to see that only  the GPT models were considered in the experimental evaluation. They already demonstrated strong reasoning capabilities. Therefore, maybe the proposed approach would be more appropriate for weaker models.

### Questions
- Can you comment on applying the hint marginalisation scheme to open models like the Llama family? And if you already experimented with the open models, what kind of results did you obtain?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a new protocol for iteratively prompting an LLM to solve reasoning problems. 

The protocol is based on the hypothesis that, when the prompt to the LLM contains a candidate answer as a "hint" (e.g., "The answer is probably close to $y$"), the LLM will: (1) output $y$ with high probability if it is in fact the correct answer, and (2) still have some chance of outputting the correct answer even if the hint $y$ is not correct. If this hypothesis holds, then we can iteratively concentrate probability on the correct answer by repeatedly prompting the LLM with its previous answer as a "hint." More formally, we can estimate a sequence of distributions $p_r(y \mid x) = \sum_{y' \in \mathcal{Y}} p_{r-1}(y' \mid x) \cdot p_{LM}(y \mid \text{question}=x, \text{hint}=y')$, where each $p_r$ concentrates more probability on the correct answer than $p_{r-1}$. The paper's proposed method is a particular Monte Carlo scheme for estimating $p_r$, which works by iteratively estimating $p_0, p_1, p_2,$ and so on, with a different sampling budget at each step. The steps of the algorithm must be performed in sequence, but within each step, approximation can be done in parallel.

The paper compares the proposed method to other prompting protocols on six benchmarks with three OpenAI LLMs, and shows that it achieves slightly higher accuracy overall.

### Strengths
1. The paper is clearly written and was easy to follow.

2. The paper clearly states the reasons that the technique might be expected to work.

3. The empirical evidence does seem to show that the proposed technique delivers some performance gains on well-studied benchmarks.

### Weaknesses
1. I don't really work in this area, and am unfamiliar with ICLR's norms for papers that essentially present a new prompting technique with benchmark results. But I believe the paper does not currently contribute a significant advance to scientific knowledge in this area. For example:

- After reading the paper, I still have very little intuition for why this sort of "hinting" ("The answer is close to X") is supposed to be beneficial. In the example few-shot prompts, the rationales do not appear to use the hint at all. In practice, do LLM rationales use the hints? How? There is no real empirical analysis beyond the overall "our strategy does better" benchmark results. The paper lacks a detailed analysis of how the hint influences the model's reasoning process. It's unclear if the model is truly integrating the hint into its reasoning or simply using it as a starting point for its answer. The lack of ablation studies to isolate the effect of the hint makes it difficult to assess its true contribution.

- The theory of the paper is based on the availability of some iterative-refinement strategy that has high "in-flow" of probability to the correct answer and low "out-flow" of probability away from the correct answer. But there is no systematic study of what sorts of iterative refinement strategies have this property. For example, do the various critique-based prompting strategies satisfy this property? Does "hinting" as you do actually satisfy this property on a wide range of examples? Why? The paper does not explore alternative iterative refinement strategies, such as those based on critique or self-correction. It's not clear if the proposed hinting method is the most effective way to achieve the desired in-flow/out-flow property. A more systematic analysis of different refinement strategies and their properties is needed.

2. I don't have a sense of the difficulty of the tasks for GPT-4-caliber language models--GPT-4 seems to score in the mid-to-high 90s. What sorts of problems does this technique really help to solve? On harder reasoning benchmarks where GPT-4 still does very poorly (e.g., Chollet's Abstraction and Reasoning Challenge) does this technique actually help? If not, how do the authors view the limitations of this technique? The paper does not adequately address the limitations of the proposed method on more challenging reasoning tasks. It's unclear if the method would be effective on problems where the initial performance of the LLM is significantly lower. The lack of evaluation on more difficult benchmarks makes it hard to assess the practical applicability of the method.

### Questions
1. Some results are starred in your table but I could not find any description of what stars indicate. Can you clarify?

2. What exactly is PHP+HM? I didn't see PHP clearly described, and it was unclear to me how you were using PHP within HM.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Hinting has proved itself as a viable approach to improve the reasoning capabilities of an LLM. A common approach is to incorporate a potential answer into the prompt, e.g. by adding "the solution might be close to X" at the end. The submission proposes a simple yet principled approach to leverage the initial answers of an LLM as hints, defining an iterative refinement of the answer distribution. More precisely, given an initial query $q$, one defines probability distributions $p_n(x\mid q)$ recursively by
\begin{align*}
p_0(x\mid q) &= p_{\text{LLM}}(x\mid q) \\\\
p_{n+1}(x\mid q) &= \int p_n(x_0\mid c)p_{\text{LLM}}(x\mid q, \mathrm{HINT}(x_0)])d x_0
\end{align*}
The main motivation behind this definition is the empirical observation that in many cases across the possible hints the flow of probability to the correct answer will be larger than the one incorrect one. As an intuition, one can state that that giving a correct answer as hint will often make the correct answer much more likely while an incorrect answer as hint will often be ignored by the model. 

The authors conduct extensive experiments both with multiple datasets and multiple SOTA LLMs and compare hint marginalization against other reasoning frameworks such as self consistency, chain of thought, and progressive hint prompting. Throughout the experiments, hint marginalization consistently shows that it is able to outperform previous methods. 

Overall, I think this is a good submission. The proposed idea might be simple but it is also sound and effective. Hence, I can recommend the paper for acceptance.
*Update*: After discussion I decided to downgrade the rating due to the rather weak motivation of the method.

### Strengths
- Independent of underlying task.
- Can be combined with other advanced prompting strategies.
- Defines a sound stochastic process as basis for combining answers from multiple hints.
- Provides a simple sampling based algorithm to estimate marginal probabilities iteratively.
- Takes great care to ensure fair evaluation in the experiments.
- Impressive experimental results.

### Weaknesses
 - Justification of the methods stems only from intuition and a few empirical evidences.

### Questions
- Is there any clustering of equivalent answers (e.g. 0.5, 1/2, \frac{1}/{2}, ...) during sampling?
- In the methodology section you define the output of the LLM to consist of the answer $y$ and an additional rationale $z$. Is $z$ used in any way in your procedure?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents Hint Marginalization (HM), an iterative prompting framework for refining for certain kinds of LLM tasks. The paper introduces the method of Hint Marginalization in a general algorithmic way. Intuitively the method can be understood as first sampling an output distribution from multiple attempts of the first prompt, which is then iteratively refined by sampling answer hints from this initial distribution, which are then provided as an additional information in the next round of prompts. This is then supplemented with an experimental evaluation on a number of standard arithmetic reasoning benchmarks for GPT-3.5 Turbo, GPT-4 Turbo and GPT-4o mini.

### Strengths
- The empirical evaluation does show some improvements, most importantly in comparision to self-consistency methods.

- The paper proposes a general model for refining LLM answers. Although the type of task seems to implicitly be limited to tasks that have "atomic" answers (e.g., numbers).

- Following the initial distribution of answers in sampling hints is an interesting idea and framing the problem as iteratively refining distributions is a robust foundation for the technique.

### Weaknesses
For the presentation as a general method, the experimental evaluation is too narrow. Only arithmetic reasoning benchmarks are tested, which is problematic in two ways.

- For one, within the category of math benchmarks the most challenging benchmarks (such as MATH) are left out. For the chosen benchmarks, state-of-the-art models already perform very well (see e.g., [1]). The reference to Patel et al. 2021 that motivates their choice does not seem timely here either. Employing such extensive prompting regimes for mild improvements in weak models is not a strong motivation. It would be important to see how the method performs also on more challening tasks where there is actually headroom to see improvements over current models. Specifically, the lack of evaluation on the MATH dataset, which includes problems requiring more complex mathematical reasoning, limits the assessment of the method's true potential. The current benchmarks, while standard, do not fully capture the range of mathematical reasoning abilities that the method purports to address.

- Second, a limitation to arithmetic benchmarks seems arbitrary when presenting a general method. Are there limitations that make the application of HM problematic in those other seetings? In particular it seems that the method is limited to reasoning tasks that output a singular (discrete) answer. In more complex settings it is unclear how the hint distribution can be reasonably formed. For instance, tasks involving multi-step reasoning with intermediate textual outputs, or tasks requiring the generation of structured outputs like code or proofs, are not addressed, and it is unclear how the iterative hint marginalization approach would apply. The method's reliance on a single, discrete answer limits its applicability to a broader range of reasoning tasks.

- There no experiments with state-of-the-art models such as GPT-4o or any models not by OpenAI. It is unclear to what degree the observed improvements for weaker/old models translate in any meaningful way also to new models or to alternative architectures. Already in the provided experimental data (Table 1) we see that the improvement gains from HM diminish significantly with GPT-4 Turbo. Strikingly, on AQuA self-consistency becomes stronger than HM, wheras the situation was flipped for the weaker GPT-3.5.

### Questions
- From the algorithm and the mathemaical exposition it is unclear to me if HM can work for continuous distributions. Could you please elaborate on whether there is any consideration for this setting?

- Is there any intution for why hints regarding proximity to other numbers are helpful to the LLM in arithmetic tasks? For example referring to the first prompt example in 8.2, why would knowledge of the answer being near 4, 7 be helpful in reasoning? There is no causal way to arrive at the answer from this knowledge and the output of the prompt does not seem to take this into account. I understand that the hints condition the LLM, but it is unclear to me why such conditioning would be helpful in general.

### Soundness
2

### Presentation
3

### Contribution
1
