# RotPruner: Large Language Model Pruning in Rotated Space

- Decision: Reject
- Scores: 5, 5, 6

## Abstract
Network pruning is a crucial technique for compressing large language models with billions of parameters, aiming to reduce memory and computational costs with minimal performance degradation. However, existing pruning methods for LLMs often focus on heuristic metrics or layer-wise reconstruction losses, neglecting the impact on the overall model output, which can lead to suboptimal result. Additionally, these methods operate directly on the original weight and activation spaces, which may not be ideal for pruning. In this paper, we propose that the original parameter space is not optimal for pruning and present a novel training-based pruning framework called RotPruner. RotPruner rotates the spaces of weight matrices and activations in linear layers, and applies existing pruning methods in a rotated space that is more suitable for pruning. We introduce an efficient algorithm to identify an appropriate rotation that preserves the performance of pruned LLMs. RotPruner is capable of integrating with other pruning methods and supporting unstructured, semi-structured, and structured pruning. We evaluate RotPruner on several large language models, including OPT, LLaMA-2, and LLaMA-3, and demonstrate state-of-the-art performance on both language modeling and zero-shot tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces RotPruner, an adaptable pruning framework for LLMs that prunes model parameters in the rotated representation space. RotPruner adds orthonormal matrices to LLMs and converts model hidden states to a rotated spade for parameter pruning, thus preserving more model outliers and keeping the LLM's knowledge learned in pretraining. The method is adaptable to existing LLM pruning methods with structured, semi-structured, and unstructured pruning strategies. Experimental results show that RotPruner outperforms existing pruning baselines.

### Strengths
- This paper presents a novel idea of pruning LLM parameters in a rotated space, thus preserving more outlier parameters with learned capabilities.
- The RotPruner method is compatible with existing pruning methods on a wide range of setups (structured, semi-structured, and unstructured)

### Weaknesses
 - There is no strong motivation for pruning LLM parameters in the rotated space. I feel like the author should have a better discussion of this in the introduction section.
- As RotPruner adds orthonormal matrices to the LLM to facilitate pruning, there should be a model latency and memory consumption overhead compared to traditional pruning methods, but the authors didn't include these comparisons in the paper.
- The authors imply that RotPruner is a post-training pruning method, yet Algorithm 1 shows that the pruned model needs to be further re-trained (approx. 1.5 hours) to recover the model performance. It makes the comparison to SparseGPT and Wanda (few-shot and tuning-free pruning methods) unfair. 
- There are a lot of typos and confusion in this paper (details in the following Questions section)

### Questions
Questions:
- What is the author's motivation for pruning LLMs in the rotated space? Is there a theoretical analysis that could demonstrate that pruning in the rotated space is better than doing it in the original model parameter space?
- Why does pruning LLM parameters in the rotated space preserve more outliers?
- What is the latency and memory consumption of RotPruner-pruned models? How is it compared to those models pruned with traditional pruning methods?
Typos and confusions:
- Please add citations to SparseGPT, Wanda, and SliceGPT when they first occur in the last paragraph of the introduction section.
- Figure 2 is distracting as the audience of this paper should already know what unstructured, semi-structured, and structured pruning methods are. Since they are not this paper's main contributions, I recommend the author remove this figure.
- line 256: "in 4", and I suspect that it should be "in Figure 4"
- line 208: "see table 1" (and lots of the same typos in the following). Please capitalize the words "Table," "Figure," etc. Consider using "\cref".
- Table 2 and Table 3: I suspect that 50% sparsity corresponds to the unstructured pruning setup and 30% to the structured pruning setup, yet this information is missing from both tables.
- Table 4: Using ticks to represent ablations is super confusing. I don't know if a tick means a module/functionality is removed or preserved.

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
The paper systematically proposes that the original weight space of a large model is not necessarily the optimal pruning space, and proposes to find the optimal pruning space by rotating matrix Q. The pruning operation is carried out in the rotated weight space, and to the greatest extent, the performance of the original model is retained under the same sparsity of the pruning operation.

### Strengths
1. Innovative thinking on pruning space: The paper systematically proposes that the original weight space of a large model is not necessarily the optimal pruning space, and proposes to find the optimal pruning space by rotating matrix Q. The pruning operation is carried out in the rotated weight space, and to the greatest extent, the performance of the original model is retained under the same sparsity of the pruning operation. 
2. Outstanding algorithm performance: The algorithm used in the paper has excellent performance in the experiments listed in the text. 
3. concise language and clear logic: the text is presented in a concise and logical manner, and the experimental results are well organized to help readers clearly understand its research contributions.

### Weaknesses
1. Limited model and dataset, too few comparison algorithms: the experiment only compares two pruning algorithms, Wanda and SparseGPT, and the model only chooses OPT and LLAMA series, which is not convincing enough
2. Single evaluation index: only PERPLEXITY was used as the performance index of the large model after pruning, more indexes can be introduced to verify the effectiveness of the evaluation algorithm.
3. ablation experiment design cannot verify the effectiveness of the algorithm: ablation experiments evaluate the effect of different losses on the algorithm, but the losses themselves are not the focus of the article's discussion. 
4. Missing reasonableness analysis to choose compare the zero-shot learning ability : the experiments assess the performance of the algorithm when comparing the different pruning algorithms in the zero-sample learning ability of the difference, but the text does not mention at all the reasonableness analysis of the choice of the index, and does not mention the algorithm in the pruning of the model after the zero-sample learning ability of the performance of the explanation.
5, the experimental design is insufficient: the experimental part is missing the analysis of the effect of pruning in the rotated weight space and the original weight space, resulting in a lack of rigor in the experimental verification of the effectiveness of the algorithm and a lack of explanatory power.

### Questions
I don't have questions.

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
3

### Summary
This paper presents RotPruner, a novel framework designed to improve the pruning of large language models (LLMs) by rotating weight and activation spaces to optimize pruning performance. Unlike traditional pruning techniques that operate directly in the original parameter space, RotPruner transforms this space into a rotated version that enhances pruning effectiveness. Tested on models such as OPT, LLaMA-2, and LLaMA-3, RotPruner achieves superior results over state-of-the-art pruning methods across multiple language benchmarks.

### Strengths
1. The paper introduces a simple yet effective method, RotPruner, which enhances model pruning by rotating the weight and activation spaces in linear layers, significantly improving pruning performance.
2. Extensive experiments validate the general effectiveness of RotPruner, with tests conducted on three different LLM series and across eight benchmarks.
3. The theoretical derivations are well-structured and accessible, making the methodology easy to understand.
4. The authors provide complete experimental code, ensuring reproducibility and facilitating future research in this area.

### Weaknesses
1. The authors do not provide experiments to assess whether RotPruner introduces additional overhead in training or inference.

2. Although the authors claim that RotPruner is orthogonal to other pruning methods, the paper lacks detailed discussion or evidence to substantiate this claim.

### Questions
1. How would different methods of learning the rotation matrices affect the results?

### Soundness
3

### Presentation
3

### Contribution
3
