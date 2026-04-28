# Sparsing Law: Towards Large Language Models with Greater Activation Sparsity

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 6, 5

## Abstract
Activation sparsity denotes the existence of substantial weakly-contributed elements within activation outputs that can be eliminated, benefiting many important applications concerned with large language models (LLMs), such as computation acceleration and model interpretability. Although promoting greater activation sparsity within LLMs deserves deep studies, existing works lack comprehensive and quantitative research on the correlation between activation sparsity and potentially influential factors. In this paper, we present a comprehensive study on the quantitative scaling properties and influential factors of the activation sparsity within decoder-only Transformer-based LLMs. Specifically, we propose PPL-$p\%$ sparsity, a precise and performance-aware activation sparsity metric that is applicable to any activation function. Through extensive experiments, we find several important phenomena. Firstly, different activation functions (i.e., ReLU and SiLU) exhibit comparable performance but opposite training-time sparsity trends. The activation ratio (i.e., $1-\mathrm{sparsity\ ratio}$) evolves as a convergent increasing power-law and decreasing logspace power-law with the amount of training data for SiLU-activated and ReLU-activated LLMs, respectively. These demonstrate that ReLU is more efficient as the activation function than SiLU and can leverage more training data to improve activation sparsity. Secondly, the activation ratio linearly increases with the width-depth ratio below a certain bottleneck point, indicating the potential advantage of a deeper architecture at a fixed parameter scale. Finally, at similar width-depth ratios, we surprisingly find that the limit value of activation sparsity varies weakly with the parameter scale, i.e., the activation patterns within LLMs are insensitive to the parameter scale. These empirical laws towards LLMs with greater activation sparsity have important implications for making LLMs more efficient and interpretable.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a study on the activation sparsity in large language models (LLMs), particularly focusing on decoder-only Transformer-based models. The authors propose a new metric called PPL-p% sparsity, which is a performance-aware measure of activation sparsity. The paper contributes to the understanding of how to design and pretrain LLMs for greater activation sparsity, which has implications for efficiency and interpretability.

### Strengths
1. The paper introduces a novel metric for measuring activation sparsity (PPL-p% sparsity) and uncovers empirical laws regarding the scaling properties of activation sparsity in LLMs.
2. The paper is well-written, and the findings are presented clearly with the aid of visualizations.
3. The insights gained from this study can inform the design and training of future LLMs, potentially leading to more efficient and interpretable models.

### Weaknesses
1. The paper could benefit from additional experiments on larger-scale models (which is more commonly seen in applications) to confirm the generalizability of the findings. Specifically, the current experiments are limited to models up to 1.2B parameters, while many state-of-the-art models now exceed 10B or even 100B parameters. The scaling behavior of activation sparsity may not be consistent across such a wide range of model sizes, and it is crucial to validate the proposed metric and empirical laws on these larger models.
2. The paper compares ReLU and SiLU activation functions, but in practical applications, a variety of activation functions such as SwiGLU may be used. The performance of these activation functions in terms of activation sparsity may differ, affecting the efficiency and performance of the model. Furthermore, the paper does not explore the impact of different gating mechanisms within the FFN layers, which can significantly influence activation patterns. For example, variations in the gating function or the dimensionality of the gate can lead to different sparsity levels and should be considered in a comprehensive study.

### Questions
1. The paper mentions the calculation of PPL-p% using a binary search method, but does the PPL change monotonically with CETT? Is this an assumption, an intuition, or is there a rigorous proof to support this relationship?
2. The paper mentions that activation sparsity can improve the interpretability of models; are there specific examples or methods to demonstrate how this sparsity helps explain the model's decision-making process?

### Soundness
2

### Presentation
3

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
This paper aims to analyze the relationship between activation sparsity and various other features of transformer-based LLMs. The authors introduce a novel metric, PPL-p% sparsity, based on a previous metric called CETT, that identifies a sparsity level at which perplexity is only increased by p% relative to a dense baseline. They study how several features relate to sparsity: amount of training data, choice of activation function, width-depth ratio of the network, and parameter scale. There are several findings, including that ReLU networks can achieve lower sparsity ratios than SiLU networks at the same performance level and convergence rates of activation (1-sparsity) ratios as the aforementioned features are varied.

### Strengths
- This paper introduces a new metric, PPL-p%, that builds upon a previous metric, CETT, by finding a sparsity level for a desired perplexity score. 
- The paper demonstrates that using PPL-p% as a metric for measuring activation ratio resuilts in a lower perplexity score relative to other metrics for measuring sparsity. 
- The set of analyses are interesting and provide some valuable, albeit limited, insights into the behavior of some LLMs.

### Weaknesses
 - I believe that there is not enough evidence showing that PPL-p% is a better metric. The main comparison point between PPL-p% and other metrics evalutates the methods on perplexity of the resultant model. This seems a bit like the metric is simply overfitting to the downstream evaluation criterion. How do each of these methods do on other tasks such as the commonsense reasoning and reading comprehension tasks?
- A significant part of this paper involved identifying various relationships between aspects of the model and the activation sparsity. It seems like a reasonable next step would be to create a model that embodies all of these takeaways, ie has an optimal activation function, amount of training data, etc, and show the results of the activation sparsity and downstream performance relative to some baseline. This would demonstrate the practical value of the observations discussed in the paper. 
- It is not clear if the results generalize to other LLMs. It would be nice to see results on other models. 
- The authors state that the goal of this paper is to produce an LLM with greater activation sparsity, but I feel like this question is not quite answered. It seems as if the authors have conducted several (interesting and thorough) ablation studies, but do not tie all of their insights together to produce one most sparse model. 

Overall, this is a decent exploration of some phenomenology around activation ratios in neural networks, but the findings are not comprehensive or cohesive enough to warrant acceptance.

### Questions
- I would recommend mentioning some more dataset details in the main paper rather than just “commonsense reasoning” and “reading comprehension”.

### Soundness
3

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
5

### Summary
This paper addresses activation sparsity in large language models (LLMs), where a significant portion of elements in activation outputs have minimal contributions to the final output. The authors aim to enhance activation sparsity to improve computational efficiency, interpretability, and training dynamics. They propose a new metric, PPL-p% sparsity, which is performance-aware and adaptable across various architectures. Through extensive experiments, the paper studies factors influencing activation sparsity, including activation functions, width-depth ratios, and parameter scales, revealing patterns and scaling properties that can inform the design and training of efficient, sparse LLMs.

### Strengths
1. Novel Metric for Performance-Aware Sparsity: The introduction of PPL-p% sparsity is a key contribution, offering a more performance-sensitive measurement of activation sparsity that is adaptable across model architectures. This metric brings a practical perspective to sparsity evaluation in LLMs.
2. Insightful Scaling Laws for Activation Sparsity: The proposed scaling laws establish patterns in activation sparsity across varying model parameters, helping to guide model design for optimized efficiency and sparsity. These scaling laws are particularly valuable for practitioners focused on resource-efficient model scaling.
3. Practical Design Guidelines for Sparse LLMs: The paper’s findings offer actionable design guidelines, such as optimal width-depth ratios, for promoting activation sparsity without compromising model performance. This provides a practical framework for building more efficient LLMs.

### Weaknesses
1. Limited Exploration of Sparsity Effects on Downstream Tasks: While the paper extensively analyzes activation sparsity during training, it lacks exploration of how increased sparsity impacts downstream task performance. This leaves uncertainty about whether the sparsity benefits hold in real-world applications. Specifically, the paper does not provide a clear picture of how the proposed PPL-p% metric correlates with performance on tasks such as question answering, text summarization, or other common benchmarks. Without this, it's difficult to assess the practical utility of the proposed sparsity metric.
2. Inconsistency in Performance Across Different Width-Depth Ratios: Although the paper highlights optimal width-depth ratios, it lacks a detailed examination of potential performance trade-offs when deviating from these ratios. This makes it difficult to understand the flexibility of the proposed guidelines for diverse architectures. The paper should investigate how varying width-depth ratios affect model convergence, training stability, and final task performance, not just sparsity. This would provide a more comprehensive understanding of the design space.
3. Scalability Concerns for Very Large Models: The paper’s experiments are conducted on specific model scales, but it is unclear how well the findings scale to extremely large models (e.g., hundreds of billions of parameters). Additional validation on larger LLMs would enhance the paper’s applicability to state-of-the-art models. The scaling laws derived from the experiments may not hold true for models with significantly larger parameter counts, and this needs to be empirically verified.
4. Unverified Claims on Sparsity Ratios and Performance Degradation: The paper mentions that overly high or low sparsity ratios may lead to severe performance degradation or unnecessary computation. However, this claim lacks experimental validation. Empirically, in many kinds of MoE models, higher sparsity levels generally correlate with improved performance, which contradicts the paper’s statement. The paper should provide a more nuanced discussion of the relationship between sparsity levels and performance, considering different types of models and training regimes.
5. Insufficient Training Tokens and Overreliance on Predicted Curves: The experiments use an insufficient number of training tokens, relying heavily on predicted scaling curves (e.g., Figure 4). For larger models (e.g., 0.8B and above), training up to 200B tokens is typically required to observe convergence. The lack of experiments on larger scales raises doubts about the reliability of the proposed scaling laws and their applicability to state-of-the-art models. The paper needs to demonstrate that the observed trends hold with more extensive training.
6. Limited Practicality in Reducing Computational Load: The proposed method may face challenges in reducing computational load in real applications. Empirically, different tokens activate different channels, making it difficult to apply a uniform activation pattern across all tokens. Since the method relies on precomputed PPL and activation patterns, these patterns may not generalize well to other tokens. In extreme cases, this would require all tokens to activate all channels to achieve their unique activation pattern, negating the intended efficiency gains. The paper needs to address how the proposed sparsity method can be effectively implemented in real-world scenarios where token-specific activation patterns are prevalent.

### Questions
1. Applicability of Scaling Laws to Extremely Large Models: The current experiments are conducted on a specific range of model scales. Do the authors plan to validate the proposed scaling laws on much larger models (e.g., hundreds of billions of parameters)? Such validation would enhance the reliability of the scaling laws for the latest state-of-the-art LLMs.
2.  Memory and Computational Efficiency Gains: Could the authors provide quantitative results on memory and computational efficiency improvements achieved through increased activation sparsity? Detailed comparisons would strengthen the practical impact of promoting sparsity in LLMs.
3. Broader Exploration of Activation Functions: The paper mainly discusses ReLU and SiLU activations. Have the authors considered examining other commonly used activation functions, such as GELU and Swish? Exploring a broader range of activations could help generalize the findings to a wider variety of LLM architectures
4.  Scaling Law Reliability with Limited Training Tokens: Given the limited number of training tokens used in the experiments, could the authors discuss the potential impact of this on the accuracy of the scaling laws? Would they consider conducting larger-scale experiments, ideally with 200B tokens for models above 0.8B parameters, to validate these scaling patterns more robustly?

### Soundness
4

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
2

### Summary
The paper identifies architectural choices that influence activation sparsity, which is measured by there own metric. They find that the ReLU activation function promotes sparsity more than SiLU, and propose relations that model activation sparsity as a function of training data. The influence of model depth and width is also analysed.

### Strengths
1) The paper raises an interesting question, that is: when is a model sparse?

2) The paper points out potential influences that can lead to sparsity.

### Weaknesses
1) The paper claims that creating sparse LLMs is of broad interest to the community, but the cited papers are mainly interested in removing sparse parts of the network to speed up e.g. inference of large models. The question of where sparse networks perform worse/better, or how the modifications in general affect performance, is not adequately addressed.

2) The paper claims "empirical laws", but they are not sufficiently motivated and validated. Even if the parameters of a model can be determined empirically, the generality of the results must be questioned when a function with four parameters (Eq. 4) is fitted to a curve.

3) One of the key results of the paper is that ReLU produces sparser networks than SiLU, which is not at all surprising given the "dying ReLU" problem.

### Questions
See Weaknesses

### Soundness
1

### Presentation
3

### Contribution
2
