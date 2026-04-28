# HShare: Fast LLM Decoding by Hierarchical Key-Value Sharing

- Decision: Accept
- Avg Score: 6.80
- Scores: 6, 6, 6, 8, 8

## Abstract
The frequent retrieval of Key-Value (KV) cache data has emerged as a significant factor contributing to the inefficiency of the inference process in large language models. Previous research has demonstrated that a small subset of critical KV cache tokens largely influences attention outcomes, leading to methods that either employ fixed sparsity patterns or dynamically select critical tokens based on the query. While dynamic sparse patterns have proven to be more effective, they introduce significant computational overhead, as critical tokens must be reselected for each self-attention computation. In this paper, we reveal substantial similarities in KV cache token criticality across neighboring queries, layers, and heads. Motivated by this insight, we propose HShare, a hierarchical KV sharing framework. HShare facilitates the sharing of critical KV cache token indices across layers, heads, and queries, which significantly reduces the computational overhead associated with query-aware dynamic token sparsity. In addition, we introduce a greedy algorithm that dynamically determines the optimal layer-level and head-level sharing configuration for the decoding phase. We evaluate the effectiveness and efficiency of HShare across various tasks using three models: LLaMA2-7b, LLaMA3-70b, and Mistral-7b. Experimental results demonstrate that HShare maintains accuracy with an additional sharing ratio of $1/8$, while delivering up to an $8.6\times$ speedup in self-attention operations and a $2.7\times$ improvement in end-to-end throughput. The source code will be made publicly available upon publication.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper explores the similarities in the KV cache tokens across neighboring queries, layers, and heads. Building on this finding, the paper introduces an advanced solution named HShare, which leverage a hierarchical framework for KV cache sharing. HShare enables the sharing of critical KV cache token indices across layers, heads, and queries, substantially reducing the computational load associated with query-aware dynamic token sparsity. Additionally, we propose a greedy algorithm that dynamically selects the optimal layer-level and head-level sharing configurations during the decoding phase. Emprical study was conducted to assess HShare's effectiveness and efficiency on various tasks using three models—LLaMA2-7b, LLaMA3-70b, and Mistral-7b. Experimental results reveal that HShare preserves accuracy while enhancing system efficiency.

### Strengths
- S1. This paper addresses a crucial and cutting-edge problem in the field, tackling the computational challenges associated with managing KV cache in long-context LLMs. 

- S2.  The techique solution is well-desgined. By optimizing the reuse and sharing of critical KV cache token indices across queries, layers, and heads, the proposed solution significantly reduces computational overhead without compromising accuracy.

### Weaknesses
 - W1. The main concern I have is about the system-efficiency evaluation in Section 5.2. Concretely, I think the baseline is a little weak; we know FlashAttention could be the state-of-the-art implementation, but it is not equipped with advanced algorithm design for selective KV-cache usage. As motivated in the introduction, other methods also attempt to reduce the computation budget based on sparsity; I think the author should report the corresponding system efficiency with the same set of baselines in Section 5.1 to fully reveal the trade-offs introduced in Table 1. Specifically, the comparison lacks a thorough analysis against other sparsity-based methods that dynamically manage the KV cache, such as those employing learned masks or adaptive token selection. The current baseline, while strong in terms of raw performance, doesn't adequately address the specific problem of dynamic sparsity in KV cache management. This makes it difficult to assess the true advantage of the proposed HShare method in the context of other similar approaches.

- W2. There are some trivial presentation issues. For example, on page 6, line 270, there is no space between "across" and "layers".

### Questions
Please address the corresponding problem listed in the Weaknesses Section.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors conducted systematic experiments to analyze the similarity of KV cache selection among queries, heads, and layers. Capitalizing on these findings, they proposed a method that shares KV selection across the dimensions of query, head, and layer, thereby reducing the overhead of KV selection.

### Strengths
The sharing-based method proposed in this paper seems novel.

### Weaknesses
1.	The experiments only selected 6 out of the 16 commonly used English datasets from Longbench for evaluation, which may not be sufficient to draw solid conclusions. For example, the performance of H2O and Quest on these 6 datasets in Table 3 appears similar, whereas in the Quest paper, H2O showed significantly lower accuracy. This discrepancy may suggest that specific methods perform better on these six datasets. To clarify, the authors are encouraged to provide results across all datasets.

2.	In terms of speedup, the authors analyzed the theoretical complexity of KV cache selection in Table 2. However, this analysis alone is insufficient to demonstrate that the proposed method significantly reduces computational overhead, as the selection cost may only account for a small portion of the entired decoding process. To strengthen this claim, the authors could provide direct evidence of decoding speed in experiments. Additionally, an experimental study on the trade-off between accuracy and speed would be valuable.

3.	The authors provided only a speed comparison with FlashAttention. To better demonstrate the effectiveness of their method, comparisons with other query-aware dynamic token sparsity methods are necessary.

4.	The authors mention using an approximate computation approach from Double Sparse ('Following the approach in Yang et al. (2024)') to calculate approximate attention weights in their implementation. As a result, it is unclear how much of the observed speed gain is attributable to HShare specifically versus the query-aware dynamic token sparsity method itself.

### Questions
Please refer to weakness points 1-4

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces HShare, a hierarchical key-value (KV) sharing framework to accelerate inference in large language models (LLMs). HShare exploits observed similarities in critical KV cache token usage across layers, heads, and adjacent queries to reduce the computational overhead of selecting query-specific tokens repeatedly. It introduces a method to share critical KV cache token indices within and across layers, heads, and queries and proposes a greedy algorithm to optimize layer- and head-level sharing configurations. Experiments demonstrate that HShare maintains accuracy while providing up to 8.6× speedup in self-attention and a 2.7× improvement in end-to-end throughput across various LLM architectures, including LLaMA and Mistral models.

### Strengths
The hierarchical sharing of KV cache tokens across heads, layers, and queries is an innovative approach to reducing latency in self-attention. HShare's observation of token reuse across different levels of attention blocks offers a new angle to address computational efficiency in LLM decoding. HShare's ability to maintain high accuracy while delivering substantial improvements in self-attention latency and throughput makes it significant for practical deployment scenarios. The method's compatibility with several model types suggests its value for LLM inference optimization.

### Weaknesses
While HShare achieves substantial speedup, the layer- and head-level sharing configurations are tested only on a few model architectures, leaving broader applicability unexplored. Specifically, the paper lacks a thorough investigation into how the sharing strategy would perform with models that have different attention mechanisms or varying numbers of layers and heads. Additionally, its performance in tasks that demand highly dynamic attention, such as document summarization with varying context lengths, could be tested to reveal any potential trade-offs. The current evaluation primarily focuses on tasks with relatively uniform context lengths, which might not fully expose the limitations of the proposed sharing approach. Minor computational overhead remains from online calculation in the prefill phase, though this appears manageable, but the impact of this overhead on overall performance, especially for very short sequences, is not fully quantified.

### Questions
Can HShare effectively support transformer variants such as convolutional or graph neural networks? A brief discussion on potential adaptations would help generalize its usability.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
HShare aims to reduce computation complexity of key value caches of transformer-based LLMs by sharing theses caches between attention heads within a layer, the layers themselves and queries within a batch. They identify critical tokens from three areas: initial/sink tokens, most recent window and significant tokens in the middle. For each of three dimensions (head, layer, query) they identify elements in these dimensions that are similar (based on a self-defined metric: overlap of cached key-value pairs) and only compute the respective key-value cache once, which is then shared between the respective elements. The resulting reduction in computation improves the latency and throughput for most configurations while maintaining the accuracy.

### Strengths
* A big strength is the evaluation. There is a wide variety of datasets used with a reasonable number of models, which show some variance in model size and architecture. Four additional framework are chosen to serve as baseline for comparison. The evaluation not only focuses on accuracy, but on compute performance (latency, throughput) as well. The provided ablation study is also fair.
* The main idea is presented clearly for the most part and is reasonable motivated with examples/microbenchmarks.
* The reduction in computation complexity with a subsequent performance improvement seems like a relevant contribution.

### Weaknesses
 * The language is a big issue. I had to read several sentences multiple times to make sense of them. So I suggest to improve the writing, so that language reads well.
* The cache hierarchy is not discussed, i.e. the order in which the three dimensions are applied, which data they might share and so on. The individual levels are discussed in how they are constructed and their details, but not how they are applied together apart from that they are independent from each other (in their memory benefits), which contradicts the initial hierarchy claim. It is unclear how the sharing decisions are made across the different levels (head, layer, query) and if there is a priority or dependency between them. For example, if a query shares its cache, does that preclude layer or head sharing? The paper states they are independent in memory benefits, but the initial claim is a hierarchy, which is not explained in detail.
* some of the equations do not add much (eq. 4 and 5)
* The performance of the original models without modification is kind of missing as a baseline for the evaluation. This makes it difficult to assess the true impact of the proposed method. It's crucial to see the performance of the unmodified models to understand the overhead and benefits of the proposed sharing approach.

more specific issues:
* line 64: "Although these two methods only load critical tokens, they retain all the KV cache"
  * That seems like a contradiction. The statement suggests that while only critical tokens are loaded, the entire KV cache is still retained, which is confusing. It would be beneficial to clarify what is meant by 'loading' in this context, and how it differs from 'retaining'.
* 2.1: recent efforts are from 2023 and 2024, but their downsides are discussed in a paper from 2022 - seems counterinituitive
* line 248: "Fig. 1(c) and Fig. 1(d)" - I think these are not the correct subfigures: it should be 1e and 1f. I think "Fig. 1(e) and Fig. 1(f)" in line 250 is similarly wrong.
* line 404: first time that the full name "DoubleSparse (DS)" was introduced; all previous mentions just refer to DS
* table 3: I question the validity of computing an average from different types of scores (similarity, F1 and rouge). Averaging these metrics, which measure different aspects of performance, may not provide a meaningful overall score. It would be more informative to report these scores separately.
* I think the table and figure placement for the evaluation can be improved, i.e. moved closer to where they are discussed.

detailed/minor issues:
* language:
  * line 40/41: "since the context length expands" - probably better "since as the context length expands"
  * line 43: "to addressing this issue" - I think it should either be "to address this issue" or "for addressing this issue".
  * line 45: "many works manage to only load these critical KV cache tokens" - I think "manage" is the wrong word here, maybe better: "many works choose to only load these critical tokens into the KV cache"
  * line 135: "make efforts" - should probably be past tense: "made efforts"
  * line 136: "Jiang et al. (2023b) trains" - train (multiple authors as subject), or even better "trained"
  * line 186: "also the same operation for value matrix and form a new value" - missing verb and general improvement: "also apply the same operation to the value matrix to form a new value matrix ..."
  * line 265: "layers of attention blocks" - I think it should be "layers of the attention blocks"
* typos:
  * line 46: "tokens(also" - missing whitespace
  * line 85: "GSM8K Cobbe et al. (2021)" - missing brackets around the reference, probably the wrong cite command is used
  * line 120: "scenarios.Decoder-only" - missing whitespace
  * line 143: "MInference(Jiang et al., 2024)" - missing whitespace
  * line 182: "i-th head(layer) and the j-th head(layer)" - missing whitespace between "head(layer)", two times; alternatively you could also use "head/layer" or "head|layer" (also applies to other occurences of the same phrase)
  * line 186: "S}corresponding" - missing whitespace
  * line 210: "HSahre" -> "HShare"
  * line 363: "Sec.4.1" - missing whitespace
  * line 408: "We use LM-Eval framework" - missing "the" before "LM-Eval"
  * Figure 6: x-axis label for TrivialQA is "Sparsity Level", when "Sharing ratio" is used for all other subfigures
* references:
  * "Anze Xie Ying Sheng Lianmin Zheng Joseph E. Gonzalez Ion Stoica Xuezhe Ma Dacheng Li*, Rulin Shao* and Hao Zhang" - author list is broken: wrong order, missing commas between the authors and please also remove the asterisks
  * consider using title case for the titles

### Questions
* line 49: What are "heavy tokens"?
* line 137: "However, such a compression strategy ... and also increases the overhead during inference." - In what regard? Wasn't the 
 compression of prompts applied to reduce certain types of overheads, for example memory complexity?
* Figure 2: On what query sequence is the figure based?
* 5.2.2 Where does the query data come from?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper discusses HShare, a hierarchical framework that facilitates the sharing of critical KV cache token indices across layers, heads, and queries. From observed similarities in KV token criticality across different levels, HShare enables a more efficient sharing strategy. The paper also introduces a greedy algorithm to dynamically determine the optimal sharing configuration for the decoding phase. The experimental results demonstrate that HShare can maintain similar accuracy and improve the end-to-end throughput.

### Strengths
1. The problem is very practical and of high interest to the community, especially with limited computation resources
2. A very comprehensive set of experiments to showcase the performance (latency and accuracy) on different datasets.
3. Well-organized paper with adequate discussions on other existing methods.

### Weaknesses
1. The paper should have some figures that discuss the tradeoff between accuracy and efficiency

### Questions
1. What would be your suspected reason for the performance gain by enabling KV sharing in Figure 6?
2. The sharing ratio can be more finely tuned. Do you think the sharing ratios would be dependent on the dataset and the task?

### Soundness
4

### Presentation
3

### Contribution
4
