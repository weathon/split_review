# PyramidKV: Dynamic KV Cache Compression based on Pyramidal Information Funneling

- Decision: Reject
- Scores: 3, 6, 6, 5, 8

## Abstract
In this study, we investigate whether attention-based information flow inside large language models (LLMs) is aggregated through noticeable patterns for long context processing.  Our observations reveal that LLMs aggregate information through 
\textbf{Pyramidal} Information Funneling where attention is scattering widely in lower layers, progressively consolidating within specific contexts, and ultimately focusing on critical tokens (a.k.a massive activation or attention sink) in higher layers. Motivated by these insights, we developed \method, a novel and effective KV cache compression method. This approach dynamically adjusts the KV cache size across different layers, allocating more cache in lower layers and less in higher ones, diverging from traditional methods that maintain a uniform KV cache size.
Our experimental evaluations, utilizing the LongBench benchmark, show that \method matches the performance of models with a full KV cache while retaining only 12\% of the KV cache, thus significantly reducing memory usage. In scenarios emphasizing memory efficiency, where only 0.7\% of the KV cache is maintained, \method surpasses other KV cache compression techniques, achieving up to a 20.5 absolute accuracy improvement on TREC dataset. In the Needle-in-a-Haystack experiment, \method outperforms competing methods in maintaining long-context comprehension in LLMs; notably, retaining just 128 KV cache entries enables the LLAMA-3-70B model to achieve 100.0 Acc. performance, matching that of a full KV cache.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes PyramidKV to conduct KV cache compression for LLM inference. The insight is that the attention scores are more uniform in the first layers but become more skewed in the last layers. As such, PyramidKV selects more tokens for the first layers and fewer tokens for the final layers. Experiments are conducted on two sets of tasks.

### Strengths
1.	Key cache compression is an important topic.

2.	The idea of PyramidKV is explained clearly.

### Weaknesses
1. The observation that the attention scores are more uniform in the first layers but become more skewed in the last layers is NOT new, see [1][2] for example. With the observation, it is straightforward to extend existing KV cache selection methods to use different sampling ratios for different layers. This limits the novelty of the paper.

[1] InfiniGen: Efficient Generative Inference of Large Language Models with Dynamic KV Cache Management
[2] MagicPIG: LSH Sampling for Efficient LLM Generation

2. The choice of sampling rate schedule, i.e., how many tokens to sample for each layer, is not discussed clearly? Why use an arithmetic sequence? What are the observations driving this choice? Will also schedule also work?

3. The empirical results are not impressive. As shown in Table 1, PyramidKV does not outperform the baselines in many cases.

4. The presentation needs to be significantly improved. (a) Most figures are not vector illustrations and become blurred when enlarged. Figure 3 is repetitive w.r.t. to Figure 1, where the idea of PyramidKV is already illustrated. (b) Figure 2 is difficult to understand, to show the skewness of attention scores, histogram or CDF (see [1][2]) may be used. (c) Section 5 is partitioned into too many subsections. You can present the experiment settings in one subsection, the main experiment result in one subsection, and some insight experiment in one subsection. (d) I failed to understand what the grids mean in Figure 5, and the axis is too small to read. (e) What is the right half of Table 2 reporting?

### Questions
See weakness part

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The study proposes a new KV cache compression method, called PyramidKV, based on its empirical study on the pyramid pattern of attention scores across layers of language models. The proposed method dynamically allocate KV cache budget to each layer based on the identified pyramid pattern. PyramidKV shows superior performance, especially under resource-intensive circumstances, against other baselines.

### Strengths
1. The observation on the pyramid pattern of attention scores across layers is valuable.
2. Based on the observed pattern, the proposed method is straight-forward and performant under resource-intensive circumstances.
3. The experiment is comprehensive.

### Weaknesses
1. The proposed method works really well under extreme condition, i.e.e KV cache size = 128. However, under not-so-extreme cases, i.e. KV cache size = 2048, the performance is not comparable to other baselines according to Table 1 in the paper. Is there any explanation to this phenomenon? I think the paper worth a small section of ablation study to explain this phenomenon.
2. In [1], Wu et al. claims that "retrieval heads" exist across models, functioning similarly to the submission's patterns ("massive attention") seen in higher layers—such as layer 30 in Figure 2—to retrieve essential contextual information. Given this, I wonder if retrieval heads are primarily found in the higher layers or if they might also be present in lower layers but are obscured due to the study's averaging of attention scores across heads within each layer. This averaging might be masking the presence of "massive attention" in the lower layers, leading to more-than-enough allocation of KV cache for some heads in the lower layers.  Could the authors conduct additional experiments to address my concern?
3. There are many variations of NIAH tasks, e.g. haystack formed from repetitive sentences or haystack formed from a long corpus. Can the authors elaborate which setting used in the study?

### Questions
Please see weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
When LLMs process long texts for inference, KV Cache becomes the main bottleneck. The purpose of this paper is to reduce the GPU memory usage and computation required for KV Cache. PyramidKV is introduced as a novel approach, varying cache sizes across layers based on information flow patterns. It allocates more cache to lower layers, where information is dispersed, and less to higher layers, where it's concentrated. Experiments on LongBench demonstrate that PyramidKV maintains performance with only 12% of the KV cache and excels in extreme conditions, even with just 0.7% cache.

### Strengths
1）The paper analyzes Attention data from different layers of LLM and discovers that LLMs aggregate information through Pyramidal Information Funneling patterns.
2）The paper is the first to propose an algorithm using different compression rates for KV Cache at different layers, which can be used with other KV Cache algorithms.
3）In scenarios with extremely high KV Cache compression rates(like 99.3%), this method can achieve better accuracy compared to other existing algorithm.

### Weaknesses
1）When the KV budget is retained at 2k, the accuracy of the proposed method does not show significant advantages.
2）The paper mainly tests models with an 8k context length, lacking accuracy tests for models with sequence lengths above 128k.
3）In cases of extremely low compression ratios, it is recommended to include comparisons with new technologies such as Minference.

### Questions
1）Besides Llama-like models, do other models also exhibit the Pyramidal Information Funneling phenomenon?
2）When determining the KV Cache budget for different layers, how should hyperparameters be selected to ensure optimal accuracy?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper explores the mechanism by which Large Language Models (LLMs) handle the aggregation of information across different layers, identifying a pattern termed Pyramidal Information Funneling. The authors observe that lower layers in LLMs tend to distribute attention scores more uniformly across all tokens, whereas higher layers exhibit more peaked attention distributions. Based on this observation, the authors propose a strategy for Key-Value (KV) cache allocation where more cache budget is allocated to lower layers, while higher layers receive a reduced budget.

### Strengths
* The paper is well-written, easy  to follow and understand the experimental setup and results.
* The paper provides a thorough experimental evaluation, showcasing various baselines and scenarios.

### Weaknesses
Lack of Novelty: The main contribution of the paper, i.e., allocating a higher KV cache budget to lower layers and a smaller budget to higher layers, is not entirely new. Similar observations have already been made in prior work, such as [1], which also discussed a linearly decreasing budget allocation across layers and yielded comparable conclusions.

[1] PyramidInfer: Pyramid KV Cache Compression for High-throughput LLM Inference (https://arxiv.org/pdf/2405.12532)

### Questions
1. The experiments indicate that the proposed pyramid KV cache allocation does not consistently surpass other baselines across all tasks. Do the authors have insights into which types of tasks this pyramidal allocation performs best and where it tends to underperform?

2. The authors propose a linear distribution for the KV cache budget, defined as k0 = 2 * k_total / m and k_{m-1} = k_total / (beta * m) - k0. My question is: by summing the budgets across all layers and setting this sum equal to the total budget, can beta be directly calculated instead of being treated as a hyperparameter? Is there a misunderstanding in my interpretation of this allocation scheme?

3. Was the decision to use a linear allocation strategy for the pyramid KV cache budget empirically validated as the most effective approach? Did the authors conduct experiments comparing various pyramidal allocation strategies to confirm that a linear strategy is indeed optimal or preferable? Including insights from such comparisons would strengthen the rationale for choosing this specific allocation method.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper proposes to dynamically adjusts the KV cache size across different layers through the depth of transformers, which is motivated by the fact that attention is denser in the initial layers and sparser in the later layers.

### Strengths
1. The observation on the attention pattern across layers is insightful.
2. Performance, especially, long context capabilities are preserved much better compared to methods in the class.
3. Experiments are quite through, examining a few challenging tasks in the long context scenarios.

### Weaknesses
1. It's not clear if this method can be implemented in real systems like vLLM/SGLang, as the memory management is still very arbitrary and frequent, which go against the hardware design.

### Questions
1. How does the speed-up change wrt tensor parallel and pipeline parallel? 
2. How does the memory allocation and release be implemented? I would assume there will be significant memory fragmentation during the process.

### Soundness
3

### Presentation
3

### Contribution
3
