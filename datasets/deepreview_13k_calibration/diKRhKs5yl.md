# Large Language Models are Demonstration Pre-Selectors for Themselves

- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 6, 3, 6

## Abstract
In-context learning with large language models (LLMs) delivers strong few-shot performance by choosing few-shot demonstrations from the entire training dataset. However, previous few-shot in-context learning methods, which calculate similarity scores for choosing demonstrations, incur high computational costs by repeatedly retrieving large-scale datasets for each query. This is due to their failure to recognize that not all demonstrations are equally informative, and many less informative demonstrations can be inferred from a core set of highly informative ones. To this end, we propose FEEDER (FEw yet Essential Demonstration prE-selectoR), a novel \emph{pre-selection} framework that identifies a core subset of demonstrations containing the most informative examples. This subset, referred to as the FEEDER set, consists of demonstrations that capture both the ''sufficiency'' and ''necessity'' information to infer the entire dataset. Notice that FEEDER is selected before the few-shot in-context learning, enabling more efficient few-shot demonstrations choosing in a smaller set. To identify FEEDER, we propose a novel effective tree based algorithm. Once selected, it can replace the original dataset, leading to improved efficiency and prediction accuracy in few-shot in-context learning. Additionally, FEEDER also benefit fine-tuning LLMs, we propose a bi-level optimization method enabling more efficient training without sacrificing performance when datasets become smaller. 
Our experiments are on 6 text classification datasets, 1 reasoning dataset, and 1 semantic-parsing dataset, across 6 LLMs (ranging from 335M to 7B parameters), demonstrate that: (i) In few-shot inference, FEEDER achieves superior (or comparable) performance while utilizing only half the input training data. (ii) In fine-tuning, FEEDER significantly boosts the performance of LLMs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a demonstration pre-selection framework. Specifically, it considers both sufficiency and necessity conditions and introduces an approximate tree-based selection method. The author conducts extensive experimental validation under both in-context learning and fine-tuning settings.

### Strengths
1. The paper is well written and easy to follow;
2. The idea of iterative optimization is reasonable;
3. The extension from instance level to set level and the approximation method based on transitivity are novel.

### Weaknesses
1. Lack of experiments with larger-scale models. For example, the  original metrics on GSM8k is quite low. Although Section 5.3 mentions this issue, the scale of the models used in the corresponding experiments is still too small. The performance of few-shot selection for larger-scale models may differ from that of smaller models, and it is uncertain whether this method can be scaled up to larger models.
2. Regarding sufficiency and necessity, more ablation studies are needed to prove that both aspects are important.
3. In the implementation of tree construction, the different design choices of merging nodes among adjacent layers requires more experimental comparisons.

### Questions
Please see the weaknesses.

### Soundness
2

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
4

### Summary
This paper addresses examples (a.k.a. demonstrations) selection for in-context learning (ICL) and Fine-tuning. The authors build on the hypothesis that a small set of highly informative examples can often encapsulate enough information to infer many less informative examples. This allows for the use of these smaller, more informative samples in ICL (or fine-tuning). The authors then propose a framework that defines "sufficient" and "necessary" samples for model prediction, where "sufficiency" implies that a sample enhances model prediction accuracy, and "necessity" means that a sample is required for the model to make correct predictions. The authors introduce a pre-selection framework to “select” necessary and sufficient samples from a training set (termed the "FEEDER set"), using a tree-based merging mechanism at each tree layer. Moreover, the authors propose a bi-level optimization method for fine-tuning based on FEEDER using a frozen LLM in the outer loop and optimizing LLM training in the inner loop.

Finally, authors demonstrate that the FEEDER set, across six different classification tasks, reasoning and semantic-parsing datasets and six large language models (LLMs), consistently provides superior performance.

### Strengths
Considering that LLMs are resource-intensive, selecting the most effective samples from a large training set is a reasonable approach to improve "efficiency and accuracy" in inference (for few-shot learning) and training (for fine-tuning). To find the right selector, the authors first define "necessary" and "sufficient" instances, extending these definitions to necessary and sufficient sets. Based on this concept, they define $D_{\text{FEEDER}}$ as a subset of $D_{\text{TRAIN}}$ that is both sufficient and necessary. A brute-force approach to find $D_{\text{FEEDER}}$ would be expensive, so the authors propose a tree-based merge technique that builds from the bottom up, merging examples into nodes based on their sufficient and necessary characteristics at each tree layer. They also claim that the approach has low complexity, yielding $D_{\text{FEEDER}}$ in a reasonable number of iterations. ICL evaluation results suggest that FEEDER is an effective pre-selector (or "compressor") of demonstrations and can benefit from various demonstration selectors. Additionally, for fine-tuning, the authors formulate sample selection as a bi-level optimization problem. In the outer layer, it identifies a “high-quality” sample set using a frozen LLM, while in the inner layer, it optimizes LLM training. In experimentation, authors show that FEEDER achieves improvements compared to fine-tuning with entire training set.

### Weaknesses
While the paper’s motivation is reasonable and the argument flow is sound, there are some gaps in the authors' reasoning throughout. 

**Ambiguous Goal (Accuracy vs. Efficiency)**: It's unclear whether the authors are primarily focused on improving model accuracy or throughput (cost) with FEEDER. Throughout, they claim the approach improves efficiency and prediction accuracy, but for ICL, there is no evidence provided for how FEEDER enhances model efficiency. Specifically, the paper lacks a clear definition of 'efficiency' in the context of ICL. Is it the reduction in the number of tokens processed, the time taken for inference, or some other metric? The authors need to clarify this and provide empirical evidence to support their claims. For instance, if the claim is about reduced inference time, they should report the actual time taken with and without FEEDER for a fair comparison.

**Computation cost for FEEDER discovery**: The FEEDER discovery algorithm requires calling the LLM at each stage to assess the sufficiency relationship between datapoints in $\mathscr{W}_{k-1}$, which appears computationally expensive and potentially impractical. The authors do not provide a detailed analysis of the computational cost associated with this process. It's not sufficient to state that the algorithm has a low complexity without quantifying the actual time and resources required. The number of LLM calls, the size of the input prompts, and the model size all contribute to the overall computational burden, and these factors should be explicitly discussed.

**Complexity and Scalability Concerns**: While the authors state that the FEEDER algorithm requires $O(K \log_2 |D_{\text{TRAIN}}|)$ iterations, each iteration involves comparing sufficient and necessary criteria between "every pair," resulting in an overall complexity of $O(K |D_{\text{TRAIN}}| \log_2 |D_{\text{TRAIN}}|)$. The authors need to clarify how the tree-based merging mechanism avoids pairwise comparisons at each level. The current description implies that every data point is compared with every other data point at each level of the tree, which would lead to the stated $O(K |D_{\text{TRAIN}}| \log_2 |D_{\text{TRAIN}}|)$ complexity. This is a significant concern, especially for large datasets, and needs to be addressed with a more detailed explanation of the algorithm's implementation and its actual complexity.

### Questions
Q1: In definitions 1 and 2, can  $(x_n, y_n)$ be $(x_m, y_m)$? In other words, can a sample be considered its own sufficient and necessary sample?

Q2: Since the ICL is limited to 5 to 10 examples, could author provide the results based on brute-force approach where we search across $plug$ and $unplug$ (as defined in Definition 1 and 2) for entire $D_\text{TRAIN}$

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a novel pre-selection framework called FEEDER, designed to identify a core subset of examples that exhibit the highest levels of "sufficiency" and "necessity." By using only this subset, FEEDER can effectively replace the original dataset, improving both efficiency and predictive accuracy in few-shot in-context learning.

### Strengths
1. This paper presents a new metric system based on "sufficiency" and "necessity" to evaluate the importance of each example.
2. This paper proposes a tree-based search method to identify the core subset, which is novel to the existing literature.

### Weaknesses
1. Even in the APPROXIMATION version presented in Section 4.2, achieving precise accuracy with terms like $1_{|W_{in}|}$ and $1_{|W_{out}|}$ in Equations 7 and 8 seems challenging. The current benchmark may very struggle to achieve 100% accuracy, raising questions about this method’s effectiveness and feasibility.

2. As the number of samples within each node grows, conducting few-shot tests on these samples becomes increasingly difficult. For instance, if the limit for few-shot samples is set to n=5, handling a node containing 1,000 samples would be problematic.

3. Most of the benchmarks used in this study, aside from GSM8k, are based on sentiment classification and linguistic analysis, which are proposed before 2018. These benchmarks are somewhat outdated and do not adequately represent the benchmarks currently prioritized by the research community.

4. Besides Llama 7B and Gemma-2 2B, the models tested are relatively outdated (before 2020) and have limited parameter sizes. This choice of models and benchmarks may reduce the impact and relevance of the paper’s conclusions for the present-day community.

### Questions
N/A

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper presents FEEDER, a framework for improving in-context learning with large language models by pre-selecting a core subset of essential demonstrations. Through the concepts of "sufficiency" and "necessity," FEEDER effectively reduces dataset size, leading to enhanced efficiency in both few-shot inference and fine-tuning settings while maintaining or improving model performance.

### Strengths
1. The paper introduces FEEDER, a demonstration pre-selector that optimizes in-context learning by identifying a core set of examples that capture "sufficiency" and "necessity." This subset enhances efficiency by reducing data size without sacrificing performance.
2.  Experiments on various datasets (text classification, reasoning, and semantic parsing) demonstrate the framework's effectiveness across multiple LLMs.

### Weaknesses
1. The paper's explanations lack clarity and specificity in certain areas. For instance:
(1) When describing the poor demonstration of some examples, the authors provide general statements without detailing specific cases or examples. Adding concrete instances, such as specific input-output pairs that lead to poor performance, would help readers better understand and contextualize the problem. For example, what types of input features or relationships between input and output are poorly represented by certain demonstrations?
(2) The terms "sufficiency" and "necessity" lack clear, formal definitions. While the paper uses these terms, it does not provide a rigorous explanation of how these properties are measured or determined in the context of in-context learning. This lack of precision makes it difficult to assess the theoretical soundness of the approach.
2. Although the paper frequently emphasizes the tree-based approximation algorithm, the selection process remains time-consuming. It would be beneficial for the authors to include a comparison of computational efficiency, including time costs and accuracy, between FEEDER-selected samples and randomly selected samples of the same size in an in-context learning setting. This could help justify the trade-offs between computational efficiency and the benefits gained from the FEEDER method. Specifically, the paper should quantify the time complexity of the tree-based algorithm and compare it to the time required for random selection, as well as the impact of these selection methods on inference time.
3. The paper lacks an in-depth analysis of certain observations from the experimental results. For example, Table 1 shows that some datasets perform better with larger sample sizes (i.e. n), while others achieve better results with fewer samples. It is unclear whether these discrepancies arise from dataset characteristics such as the complexity of the input space, the distribution of labels, or the presence of noisy data. A more detailed analysis of these factors and their impact on the optimal number of demonstrations is needed. 
4. The experimental results indicate that the FEEDER set and direct sample selection from the training set yield similar performance trends with respect to changes in n, which is inconsistent with the "necessity" mentioned by the authors. Given that FEEDER sets are meant to fulfill "necessity," it would be logical for performance to improve as the number of examples increases, or at least plateau. However, this anticipated trend is not clearly reflected in the results. Further investigation into this issue is warranted, particularly to clarify why the FEEDER set’s performance does not show a clear improvement with increasing sample sizes. This includes analyzing whether the selected examples are truly non-redundant and how the selection process interacts with the inherent limitations of the in-context learning mechanism.

### Questions
1. Although the paper frequently emphasizes the tree-based approximation algorithm, the selection process remains time-consuming. It would be beneficial for the authors to include a comparison of computational efficiency, including time costs and accuracy, between FEEDER-selected samples and randomly selected samples of the same size in an in-context learning setting. This could help justify the trade-offs between computational efficiency and the benefits gained from the FEEDER method.
2. The paper lacks an in-depth analysis of certain observations from the experimental results. For example, Table 1 shows that some datasets perform better with larger sample sizes (i.e. n), while others achieve better results with fewer samples. It is unclear whether these discrepancies arise from dataset characteristics or other factors. 
3. The experimental results indicate that the FEEDER set and direct sample selection from the training set yield similar performance trends with respect to changes in n, which is inconsistent with the "necessity" mentioned by the authors. Given that FEEDER sets are meant to fulfill "necessity," it would be logical for performance to improve as the number of examples increases. However, this anticipated trend is not clearly reflected in the results. Further investigation into this issue is warranted, particularly to clarify why the FEEDER set’s performance does not show a clear improvement with increasing sample sizes.

### Soundness
3

### Presentation
3

### Contribution
2
