# Rethinking Evaluation of Sparse Autoencoders through the Representation of Polysemous Words

- Decision: Accept
- Scores: 6, 5, 6, 6

## Abstract
Sparse autoencoders (SAEs) have gained a lot of attention as a promising tool to improve the interpretability of large language models (LLMs) by mapping the complex superposition of *polysemantic* neurons into *monosemantic* features and composing a sparse dictionary of words.

However, traditional performance metrics like Mean Squared Error and $\mathrm{L}_{0}$ sparsity ignore the evaluation of the semantic representational power of SAEs - whether they can acquire interpretable monosemantic features while preserving the semantic relationship of words.For instance, it is not obvious whether a learned sparse feature could distinguish different meanings in one word.

In this paper, we propose a suite of evaluations for SAEs to analyze the quality of monosemantic features by focusing on polysemous words.
Our findings reveal that SAEs developed to improve the MSE-$\mathrm{L}_0$ Pareto frontier may confuse interpretability, which does not necessarily enhance the extraction of monosemantic features.
The analysis of SAEs with polysemous words can also figure out the internal mechanism of LLMs; deeper layers and the Attention module contribute to distinguishing polysemy in a word.

Our semantics-focused evaluation offers new insights into the polysemy and the existing SAE objective and contributes to the development of more practical SAEs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a new framework, called PS-Eval, for evaluating Sparse Autoencoders (SAEs), which are widely used to interpret LLMs. The framework repurposes the WiC dataset (Pilehvar & Camacho-Collados, 2019), originally designed as a binary classification task. Specifically, the paper proposes using a subset of WiC to evaluate the extent to which the features learned by SAEs are monosemantic (the ideal case for SAEs). With this dataset, the authors suggest evaluating SAEs using metrics like precision, recall, and specificity. The paper provides a detailed analysis of SAE performance across different layers and transformer components (e.g., residual, MLP, and attention) and compares activation functions such as ReLU, TopK, and JumpReLU.

### Strengths
I really enjoyed reading this paper, as it addresses a well-known issue with SAEs that has been overlooked for a long time. It does so by introducing a context-sensitive metric for monosemantic representation, making the paper timely and addressing a current gap in interpretability research. I also appreciated the depth of the experiments, which cover different transformer modules and layers. The analysis is insightful, clearly demonstrating that standard metrics (MSE and sparsity ratio) can be insufficient for capturing monosemantic features. I believe such analyses are very valuable for future SAE design and application. Overall, the paper is well-organized, well-motivated, easy to read, and offers insightful conclusions.

### Weaknesses
Even though I enjoyed reading this paper, my main issue is that there is no baseline for comparison. For example, in Table 4, it is hard to conclude which values of accuracy/precision/recall/specificity signify a good SAE. In other words, even with this new framework, it is unclear whether these SAEs can be trusted. Having a good baseline (e.g., a random SAE or fully dense SAE) could help clarify this issue.

### Questions
Can the PS-Eval framework be extended to other models or applications outside of NLP, or is it fundamentally tied to the context-sensitive nature of language?

Figure 3: Could you explain why LLM activations are considered less interpretable than SAE features in Figure 3? For me, the fact that LLM activations are squished into the [0, 0.2] interval doesn't make them less interpretable. Instead, it seems like a matter of finding a different cutoff value for LLM activations. Also, how many bins were used for the plot?

---

Minor comments:

In line 316, you say, "Specificity measures how often the different meaning words have the same SAE features." The correct wording should be "different SAE features," as per Table 2.

In line 96: "In our evaluation across different Transformer components, specifically the residual layers, MLPs, and self-attention." I believe a part of the sentence is missing.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a new interpretability metric to substitute the origin reconstruction and sparsity loss in sparse autoencoders. This metric evaluates whether the words of two meanings are the same in features and vice versa. This paper has two findings with this metric: 1. the objective of maximizing reconstruction and sparsity loss does not increase this metric. 2. high layers and attention modules play an essential role in modeling specific semantics of words.

### Strengths
1. This paper first examines the ability to identify polysemantics in the interpreter tool of sparse autoencoders. 

2. This paper provides a tool to inspect semantic specificity in the transformers.

### Weaknesses
This paper lacks several justifications. Refer to the Questions.

### Questions
1. What is the bar for the features to be the same and different? How do you tune this bar?

2. Why do late or large language models perform worse in identifying semantic similarity, although they got significantly higher scores on challenging benchmarks?  The performance of this metric does not align with the performance on benchmarks. Could you please discuss potential reasons for this misalignment between their metric and benchmark performance or provide additional analysis exploring this phenomenon?

3. In your setting, recall and specificity are more valuable than other metrics.

4. Why do we need to calculate this metric on the representations of the intermediate layer of SAE  but not AE or the origin representations? Can you provide a comparison?

5. Which layer of the transformer do you test as default?

6. Does this metric generalize better to other interpretability than the origin reconstruction and sparsity loss?

---Post Rebuttal Review---
I have had a discussion with the authors; I think the authors have clarified several issues and promise to add more details and comparisons in the revised version. Thus, I decided to raise the score from 3 to 5.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces PS-Eval, a new method for assessing whether SAEs can extract monosemantic features from transformer models by examining their handling of polysemous words. While the paper offers valuable contributions through its evaluation methods, empirical analysis across different architectures, and interesting findings about layer depth and attention mechanisms, it suffers from significant conceptual limitations. My core concern is the paper's unexamined assumption that SAE features should directly map to word meanings, along with questions about whether insights from polysemous words can generalise to broader SAE evaluation. The empirical work is relatively thorough and the findings are interesting, particularly regarding the role of attention in handling polysemy and the logit lens analysis, but the theoretical framework needs strengthening and the scope may be too narrow. I recommend rejection in its current form while strongly encouraging resubmission after addressing these conceptual issues, improving the theoretical framework, and clarifying the presentation.

### Strengths
__Novel evaluation methodology__:
* Clear metrics based on confusion matrix approach
* Well-defined dataset construction from WiC
* Systematic evaluation framework that could be extended to other models


__Experimental analysis__:
* Thorough comparison across different activation functions
* Valuable insights about layer depth and transformer components
* Interesting findings about attention's role in handling polysemy
* Useful logit lens analysis demonstrating semantic differentiation


__Technical contributions__:
* Model-independent evaluation metric
* Practical insights for SAE deployment
* Clear demonstration of limitations in current MSE-$L_0$ optimisation

### Weaknesses
__Core conceptual concerns__: The paper assumes SAE features should directly map to word meanings. This is a strong assumption that needs more justification. It's possible that effective SAEs might represent meaning through other feature combinations. The focus on polysemous words, while interesting, may be too narrow to support broad conclusions about SAE quality.


__Methodology limitations__:
* The evaluation method could benefit from more discussion of edge cases and failure modes
* Limited exploration of how results generalise beyond the specific test cases
* Need for clearer discussion of how PS-Eval relates to existing SAE objectives


__Presentation issues__:
* Some key terms need clearer definition, particularly in the introduction (e.g. "semantics-focused evaluation", "polysemous words")
* Several figures would benefit from more detailed captions
* Some sections (particularly the transformer component analysis) need more thorough explanation
* Quite a few typos (e.g. "assesse", "spolysemantic", and incomplete sentences e.g. "In our evaluation across different transformer components, specifically the residual layers, MLPs and self-attention.")

### Questions
1. How do you justify the assumption that SAE features should directly correspond to word meanings? Could you discuss alternative feature organisations that might be equally valid? 
* For instance, it's easy to imagine an SAE feature that fires on a particular word (e.g. "tweet") regardless of context, and another SAE feature fires on sentences regarding birds and another fires on sentences regarding social media (e.g. "Twitter"), distinguishing the two. It's not clear to me that this is a strong failure mode of an SAE. 
* I don't know if we should expect SAEs to learn features directly corresponding to meaning (the strong linear representation hypothesis) because we don't know what the atomic units (i.e., features) of a model's computation actually are.
2. Could you elaborate on how insights from polysemous word evaluation might generalise to other aspects of SAE quality?
3. The logit lens analysis shows promising results - could you expand on how this validates your evaluation method?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
In the literature, SAEs are often evaluated on MSE and L0. The paper introduces a new metric for evaluation of SAEs that directly measures whether SAEs learn separate features for the different meanings of polysemous words (words which have different meanings based on the context). The metric is constructed from the WiC dataset (filtering for words which tokenize to single tokens). The paper finds that improving the MSE-L0 frontier does not necessarily lead to improvements on this newly introduced metric. The paper also shows that eventually, scaling SAEs no longer improves score on this metric, that alternative activation functions are not always better, and that later layers

### Strengths
- Well motivated metric. Correct in identifying problems with MSE/L0 as a metric of SAE quality. Using polysemy as a source of eval is a good idea.
- Confusion matrix approach is reasonable and consideration of metrics like F1 provides more granularity.

### Weaknesses
- k=384 is an extremely high k for TopK. Gao et al. (2024) recommends using d_model / 2 for the _maxk_ hyperparameter, not themain k hyperparameter. Ideally, a much smaller k is used for $k$. Using a value of k equal to or larger than d_model doesn't make much sense.
- JumpReLU comparison would be stronger if the STE variant from Rajamanoharan et al. (2024) were used.

### Questions
- Normalized L0 (L0 / N) is less informative as a metric than L0 because the amount of information in the latents is roughly proportional to L0 * log N, so across different N's, L0 is roughly comparable, whereas L0 / N is not very comparable.
- How are the SAEs initialized? Prior work (Conerly et al., 2024; Gao et al., 2024) has found that initializing the encoder to the transpose of the decoder is very important for scaling SAEs.
- What are the L0 values attained by the SAEs for each activation function? Are they in a similar range? Are they less than d_model?
- How many dead latents are there in the SAEs?

### Soundness
2

### Presentation
2

### Contribution
3
