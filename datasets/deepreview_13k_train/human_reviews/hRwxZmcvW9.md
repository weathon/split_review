# Bridging and Modeling Correlations in Pairwise Data for Direct Preference Optimization

- Decision: Accept
- Scores: 6, 6, 6

## Abstract
Direct preference optimization (DPO), a widely adopted offline preference optimization algorithm, aims to align large language models (LLMs) with human-desired behaviors using pairwise preference data.
However, the winning response and the losing response within pairwise data are generated isolatedly, leading to weak correlations between them as well as suboptimal alignment performance.
To address this issue, we propose an effective framework for Bridging and Modeling Correlations in pairwise data, named \textbf{BMC}.
Firstly, we increase the consistency and informativeness of the pairwise preference signals through \textit{targeted modifications}, synthesizing a pseudo-winning response by improving the losing response with the winning response as a reference. 
Secondly, we identify that DPO alone is insufficient to model these correlations and capture nuanced variations. Therefore, we propose learning token-level correlations by \textit{dynamically} leveraging the policy model's confidence during training.
Comprehensive experiments on QA, math, and instruction-following tasks demonstrate the effectiveness of our approach, significantly surpassing competitive baselines, including DPO.
Additionally, our in-depth quantitative analysis reveals the reasons behind our method's superior performance over DPO and showcases its versatility to other DPO variants.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes an effective framework for Bridging and Modeling Correlations in pairwise data, named BMC. It leverages a commercial LLM to rewrite the winning response and defines confidence-based token-level weighting to improve the original DPO. The experiments are extensive.

### Strengths
- The idea of using commercial LLM to rewrite the winning response for DPO is interesting. 

- The experiments are extensive.

### Weaknesses
 - Regarding the motivation, the authors state that "yw and yl are generated isolatedly, the correlation between yw and yl can be weak during pairwise preference optimization", but this is not usually the case in practice. For example, a common practice is to let an LLM continue writing a prefix of the winning response to get the losing one. I mean, the correlation between these two responses can be easily established during data collection. 

 - It is not well explained why "this weak correlation poses a challenge, as the winning response yw may not provide sufficiently informative gradients for adjusting the model’s parameters in relation to yl". This argument is too high-level. Can you delve into the details? Despite the results that have proven this point, I still wonder about the reason behind it. 

 - The token confidence should not be always reliable and then the loss weighting trick hinges on intensive hyper-parameter tuning. This undermines the promise of the method. 

 - To what extent does the final performance depend on the rewriting quality of the commercial LLM? Can some open-source ones be leveraged for this and what is their performance?

### Questions
See above

### Soundness
2

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
This paper identifies the important role of the correlation between chosen & rejected responses for LLM alignment with DPO-style algorithms. They propose a suite of solutions including (1): rephrasing the chosen response into the style closer to the rejected response to enhance their correlation; (2): adding a token-level weighting in the DPO loss based on the policy model's confidence on the different tokens between the (rephrased) chosen and rejected responses. Extensive experimental results demonstrate that the proposed BMC pipeline could improve the model's performance on QA, math reasoning, and instruction following benchmarks, as well as exhibiting better and more reasonable token-level and sequence-level reward behaviors.

### Strengths
* This paper is written with high quality.
* The improvement to the current DPO-style alignment pipeline is well-motivated, with a simple and effective solution.
* The experiment part of this paper is well conducted, showing clear empirical significance with detailed ablation studies.

### Weaknesses
 * Regarding the "Bridging Phase", I feel it does not necessarily address every aspect of the initial annotations. For example, despite the semantic aspects (i.e., the chosen response is correct while the rejected one is not), the preferred syntax, or linguistic aspects, such as how to better organize the response, might be neglected. If the original chosen response is better in terms of aspects other than correctness, then the Bridging phase may "erase" such useful information.
* The scalability of rephrasing every chosen response is somewhat limited, which can be improved by investigating the effect of executing the BMC for a specific portion of the dataset or considering how to identify the crucial tokens during the DPO training (i.e., based on confidence pattern demonstrated in line 228-245 and Sec 5.3), i.e., designing a better token-level weighting criterion for DPO-MC.
* I think the overall computation overhead introduced by the BMC pipeline should be discussed.

### Questions
* Regarding the first point in the weakness part, could the model still be able to learn some preferred linguistic aspect (such as organizing the answer with a CoT style) when the chosen & rejected responses overlap largely in terms of syntax? Does the shared linguistic structure matter or we can achieve a similar effect by identifying the token span that is critical to the semantic (which could be an improved version of DPO-MC with better token weighting criterion)?
* It would be interesting to see why LMs are bad at rephrasing a win response into a lose response. Do you have some observations other than Table 3, such as checking the difference of the result semantic equivalence between $(y_w, \tilde y_w)$ and $(y_l, \tilde y_l)$?
* Do you have some thoughts about why BMC can not boost SimPO?

### Soundness
3

### Presentation
4

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
The paper introduces a novel framework called **Bridging and Modeling Correlations (BMC)** to enhance Direct Preference Optimization (DPO) in aligning large language models (LLMs) with human preferences using pairwise preference data. The framework consists of two phases:

1. **Bridging Phase**: Enhances the correlation between winning and losing responses by generating a pseudo-winning response (ỹ_w) through targeted modifications of the losing response (y_l), referencing the winning response (y_w).

2. **Modeling Phase**: Improves token-level credit assignment by dynamically adjusting token rewards based on the policy model's confidence during training. This is formalized in their proposed objective function with adaptable weights.

Despite these new methods, the paper's experimental results show **modest performance improvements** compared to the computational and resource costs involved in the data modification process with stronger LLMs. I would like to understand these aspects further during the rebuttal period.

### Strengths
1. **New Approach**: Introducing the Bridging Phase to enhance correlations in preference data is a new solution to a recognized problem in DPO methods.

2. **Dynamic Token-Level Adjustment**: Adjusting token rewards based on model confidence is a novel idea that could potentially improve fine-grained learning.

3. **Comprehensive Evaluation**: The authors conduct extensive experiments across multiple tasks, including question answering, mathematical reasoning, and instruction following.

4. **Versatility**: The framework is adaptable to various DPO variants, demonstrating its potential applicability in different contexts.

### Weaknesses
1. **Marginal Performance Improvement vs. Cost**: The reported performance gains, while present, are relatively modest (e.g., 3.8 percentage points improvement in QA tasks), considering the significant effort and computational resources required for data synthesis and modification. Modifying 60-70% of the dataset introduces substantial overhead. The paper does not adequately address the computational cost of the Bridging Phase, specifically the token-level comparison using dynamic programming (edit distance) and the subsequent reward weighting calculations. While these operations might seem lightweight, their cumulative impact on training time and resource utilization needs to be thoroughly analyzed, especially when scaling to larger datasets and models. Furthermore, the paper should include a detailed breakdown of the time complexity of these operations. The marginal gains observed need to be explicitly justified against the added computational burden. 

2. **Dependency on Large LLMs for Data Synthesis**: The Bridging Phase relies on powerful LLMs (e.g., GPT-4) for targeted modifications, which may not be feasible or cost-effective for many practitioners. The paper lacks a discussion on the potential impact of using different LLMs for the data synthesis process. The quality of the pseudo-winning responses is likely to be heavily dependent on the capabilities of the LLM used for modification. A sensitivity analysis of the impact of different LLMs on the final performance would be beneficial. The paper should also explore the potential for bias introduction during the data synthesis process by the LLM, which could skew the results.

3. **Insufficient Analysis of Trade-offs**: The paper lacks a detailed discussion on the trade-off between the cost of data modification and the performance gains achieved. The paper should include a more comprehensive analysis of the cost-benefit ratio, considering both computational resources and time. It is crucial to understand under which conditions the proposed approach is most beneficial, and when simpler methods might be more appropriate. The paper should also discuss the sensitivity of the performance gains to the proportion of data modified in the Bridging Phase, as modifying a large portion of the dataset may not always be necessary or cost-effective. 

4. **Limited Improvement Over Baselines**: Given the additional complexity and cost, the improvements over standard DPO and other baselines are insufficient to justify the added effort. The paper needs to provide a more thorough comparison with other state-of-the-art methods, including those that do not rely on data modification. The paper should also investigate if the performance gains are consistent across different types of tasks and datasets, or if they are limited to specific scenarios.

### Questions
1. **Cost-Benefit Justification**: Can the authors provide a more detailed analysis of the computational and resource costs associated with the Bridging Phase relative to the performance gains? How do the authors justify the added complexity and cost?

2. **Impact of Data Modification Proportion**: Did the authors investigate the relationship between the proportion of data modified in the Bridging Phase and the resulting performance? Is there a point of diminishing returns?

3. **Baseline LLM Limitations**: Is the modest performance improvement partly due to inherent limitations of the baseline LLM used in the authors' experiments? Would using a more capable baseline model lead to greater improvements, or are there fundamental constraints in the proposed approach? It would be beneficial to elaborate on the capabilities of larger baseline models as well, if possible.

### Soundness
3

### Presentation
3

### Contribution
2
