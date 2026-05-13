# Length Desensitization in Direct Preference Optimization

- Decision: Reject
- Scores: 5, 5, 5

## Abstract
Direct Preference Optimization (DPO) is widely utilized in the Reinforcement Learning from Human Feedback (RLHF) phase to align Large Language Models (LLMs) with human preferences, thereby enhancing both their harmlessness and efficacy. However, it has been observed that DPO tends to over-optimize for verbosity, which can detrimentally affect both performance and user experience. In this paper, we conduct an in-depth theoretical analysis of DPO's optimization objective and reveal a strong correlation between its implicit reward and data length. This correlation misguides the optimization direction, resulting in \textit{length sensitivity} during the DPO training and leading to verbosity. 
To address this issue, we propose a length-desensitization improvement method for DPO, termed LD-DPO. The proposed method aims to desensitize DPO to data length by decoupling explicit length preference, which is relatively insignificant, from the other implicit preferences, thereby enabling more effective learning of the intrinsic preferences. We utilized two settings (Base and Instruct) of Llama2-13B, Llama3-8B, and Qwen2-7B for experimental validation on various benchmarks including MT-Bench and AlpacaEval 2. The experimental results indicate that LD-DPO consistently outperforms DPO and other baseline methods, achieving more concise responses with a 10-40\% reduction in length compared to DPO. We conducted in-depth experimental analyses to demonstrate that LD-DPO can indeed achieve length desensitization and align the model more closely with human-like preferences.
\\
\\
\textit{``Brevity is the Soul of Wit.''}
\begin{flushright}
\textit{—William Shakespeare}
\end{flushright}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors demonstrate the existence of length sensitivity in the DPO algorithm and analyze this issue theoretically. They propose the LD-DPO algorithm to address this sensitivity. Experiments on three open-source language models show the effectiveness of LD-DPO.

### Strengths
- The logic flow is clear.
- The authors identify the reason for length sensitivity in the DPO algorithm.
- Based on their analysis, the authors propose the LD-DPO algorithm, which performs well in terms of length control and alignment.
- Experiments with three models across two datasets demonstrate the generalizability of LD-DPO.
- LD-DPO is a simple yet effective method.

### Weaknesses
 - Although the authors claim to have theoretically proven the sensitivity of DPO to length, the description is still insufficiently rigorous. For example, from Equation 4 to Equation 5, the expectation sign is omitted without further explanation. The justification for approximating the expectation with a single sample is not clearly stated, and the implications of this approximation on the analysis are not discussed.
- The explanation from lines 211 to 215 is vague and overly intuitive, especially regarding the relationship between length and probability. The argument that longer sequences have lower probabilities is presented without sufficient mathematical backing. The connection between this probability difference and the optimization direction of DPO is not made explicit, leaving the reader to infer the mechanism.
- In Equation 7, the authors take the absolute value of the ratio of two Jacobians, a less clear motivation that complicates the analysis. The use of the absolute value obscures the directional information of the gradients, which is crucial for understanding the optimization dynamics. The justification for focusing on the magnitude rather than the sign of the gradient ratio is missing.
- The term "probability bias" in line 416 is unclear.
- The effect of the hyperparameter \alpha remains unclear. In lines 497-500, the authors state, "Conversely, when \alpha is too small, excessive length decoupling leads to a loss of human-like preferences in the text, thereby reducing the optimization effectiveness." Figure 4 shows that different selections for \alpha lead to varied effects across different experiments. In AlpacaEval 2, choosing either 1 or 0 results in similar LC-win rates; however, in MT-Bench, choosing 0 (i.e., strong desensitization to length) leads to significantly lower performance compared to the original DPO. The authors do not provide further explanation for this. The lack of a clear relationship between \alpha and the model's performance makes it difficult to apply the method effectively.
    
- The design of the hyperparameter \alpha has a relatively strong impact on LD-DPO performance, as reflected by the results in Figure 4. The sensitivity of the method to this hyperparameter raises concerns about its practical applicability and the need for careful tuning.
    
- A minor issue: the color differentiation of the lines within the same subfigure in Figure 3 makes it difficult for readers to distinguish them.

### Questions
Are lines 808-810 correct? Should both $\frac{\partial \mathcal{L}{DPO}(\chi_1; \chi_2)}{\partial \chi_1}$ and $\frac{\partial \mathcal{L}{DPO}(\chi_1; \chi_2)}{\partial \chi_2}$ increase when $\chi_2$ decreases? Should $\frac{\partial \mathcal{L}{DPO}(\chi_1; \chi_2)}{\partial \chi_1}$ decrease and $\frac{\partial \mathcal{L}{DPO}(\chi_1; \chi_2)}{\partial \chi_2}$ increase when $\chi_1$ decreases?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper addresses the issue that DPO tends to over-optimize for verbosity and proposes a method to desensitize DPO to data length. Evaluations show the proposed LD-DPO algorithm consistently outperforms existing algorithms with less average tokens than DPO.

### Strengths
1. Addresses a popular issue of DPO's sensitivity to length.
2. Good presentation and easy to read.
3. Good empirical performance.

### Weaknesses
1. Although theoretical insights on why DPO favors longer response is provided, the proposed LD-DPO is a heuristic method. It directly cuts off the importance of the tokens exceeding the public length. It is disappointing to see the solution to the well-formulated length sensitivity problem is just a code-level heuristic method. Why not try to modify the DPO loss for a loss landscape[1] that is length-desensitized? The current approach, by truncating the influence of tokens beyond a certain length, risks losing valuable information contained in those later tokens, which could be crucial in more complex reasoning or detailed explanations. This truncation is a crude approximation and may not generalize well to diverse tasks where longer responses are necessary.
2. The description for eq.(10) is not rigorous. Why $p^\alpha$ is "human-like preferences" and  $p^{1-\alpha}$ is "verbosity preference"? Just by definition? The justification for decoupling the likelihood into these two multiplicative components is not clearly explained. It's unclear why a multiplicative approach is chosen over an additive one, and how this specific formulation effectively separates the desired "human-like" preferences from the undesired "verbosity" preference. The role of the hyperparameter $\alpha$ is also not well-defined, as it requires prior knowledge to determine the relative importance of each component, which is not always available or intuitive.

### Questions
See weekness.

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes LD-DPO, a DPO-based method to desensitize LLMs from length bias during preference optimization. The authors first gave analysis on why DPO methods are sensitive to the length bias in the response pairs. Based on the analysis, LD-DPO decays  the probability of the excessively long  part of responses to attenuate the sensitivity of DPO to longer responses. Results on several benchmarks demonstrate that compared to DPO, LD-DPO sucessfully reduces the length of generated responses after preference optimization.

### Strengths
1. Length bias widely exists in a wide range of LLM alignment methods and should be disentangled from real human preferences,

2. Motivation of LD-DPO is clearly expressed by the theoretical analysis.

3. Proposed method is evaluated on multiple benchmarks and base models.

### Weaknesses
1. Redundant symbol definitions. I do not think the definitions of $\mathcal{X}_1$, $\mathcal{X}_2$,$\mathcal{K}_1$,$\mathcal{K}_2$ are necessary. It just adds to the diffculty to understanding.

2. The colors in the fig. 3 are difficult to distinguish. And this figure is also a bit hard to comprehend.

3.Some spelling and grammartical mistakes, e.g. "Length **Desentsitization** of DPO, termed LD-DPO"

### Questions
1. The analysis of length bias in DPO is interesting. However, it seems this analysis only applies to DPO-based methods. Since RLHF-based methods also tend to increase generation length after training, how is it different from the length bias in DPO? Is it possible to apply your analysis to length bias in RLHF?

2. In LD-DPO, probabilities of excessively long portions (response after $l_p$) are decayed by $\alpha$ to close the gaps between the magnitudes of chosen and rejected responses' probabilities, which inevitbaly introduces information losses. And you also admitted that "additional text can convey more human-like preferences"; "$\alpha$ is actually the result of a compromise to achieve desensitization of DPO based on model capabilities and to prevent the loss of human-like preferences"

Therefore, the decrease of generation length is reasonable, but it is weird that LD-DPO consistently demonstrate better scores than DPO even with this information loss. Is there any reasonable explanation?

3. LD-DPO seems to be very sensitive to hyperparameter $\alpha$ (the values are different for all models in your experiments). Is there any way to improve it?

To be honest, I'm currently undecided between 5 and 6. Considering the issues mentioned above, I'll give this paper a 5 for now and reconsider it upon seeing authors' feedback.

### Soundness
2

### Presentation
4

### Contribution
3
