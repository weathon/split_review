# Few Heads are Enough

- Decision: Reject
- Avg Score: 5.67
- Scores: 6, 5, 6

## Abstract
The costly self-attention layers in modern Transformers require memory and compute quadratic in sequence length. Existing approximation methods usually underperform and fail to obtain significant speedups in practice. The recently proposed Flash-Attention reduces both compute and memory through a *hardware*-aware implementation. Can we achieve this also through *algorithmic* improvements? Here we present Expert Projection Attention (EPA) - a novel method that reduces both compute and memory requirements, while matching the language modeling performance of baseline Transformers using the same parameter budget. EPA uses Mixture-of-Experts (MoE) layers for the value and output projections and requires 4 to 8 times fewer attention matrices than standard Transformers. Our novel attention can also be combined with MoE MLP layers, resulting in an efficient "Fast Transformer".

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces a modification to the attention mechanism by incorporating a mixture of experts in both the source (K, Q) and destination (V, O) projections. This modification enables the selection of fewer active heads, thereby reducing computational and memory costs during both training and inference. The paper is based on the premise that not all attention heads are necessary for a given task. By utilizing an expert to select the required heads, it is possible to decrease computation and memory expenses. The effectiveness of this algorithm is demonstrated by comparing its accuracy to that of the dense counterpart and by visualizing the attention matrices.

### Strengths
1. The paper is well-written and effectively highlights the issues with the current attention architecture in terms of computational and memory demands.
2. The paper conducts experiments on various datasets and compares its results with existing baseline methods, including MOA.
3. The paper conducts a thorough analysis of attention maps to facilitate a qualitative study and comparisons with conventional attention matrices.

### Weaknesses
1. The paper refers to FlashAttention multiple times and compares against their CUDA kernel (SW designed to exploit HW efficiently) optimization vs algorithmic insight in this paper. I am not sure if its an apple-to-apple comparison since there are tons of other literature for transformers which aim to reduce computation/memory cost (like quantization/sparsity methods) and the paper doesn’t compare against these. Specifically, the paper lacks comparison against methods that explore structured sparsity in attention matrices or low-rank approximations of attention, which are also algorithmic approaches to reducing computational cost, not just hardware optimizations. These methods could provide a more relevant baseline for comparison.
2. While authors compare against FlashAttention custom kernel implementation and mention that as a drawback, EPA algorithm itself requires a custom CUDA kernel with its own set of restrictions (pointed in the results section). This dependence on a custom kernel limits the generalizability and ease of adoption of the method, as it requires specific hardware and software configurations. The paper should more clearly discuss the limitations imposed by this custom kernel, such as the specific hardware it is optimized for and the potential difficulties in porting it to other platforms.
3. For the EPA algorithm, the paper mentions that K/Q source experts are not necessary for good results and only output/value experts are required, which seems to contradict the disadvantages shown in 2.2 naive algorithm. The paper does not adequately explain why the naive approach fails with K/Q experts but the proposed method succeeds with only output/value experts. This lack of clarity makes it difficult to understand the core mechanism of the algorithm and its limitations.

### Questions
1. Can the authors compare against architectures other than TransformerXL? It is not evident from the text why only 1 architecture is chosen for comparison?
2. It is not evident from the paper how nHead is chosen for a task. Most results demonstrated fixed the nHead to be 2 or 4. Did the authors perform smaller experiments to first search for optimal nHead before scaling up?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a method for selecting one head but keeping a small number of Q,K and V matrix.
I really feel this paper is quite poorly written. First of all, the notations are extremely unclear especially in the method section. The authors have a schematic in
Figure 1 but it's unclear what this schematic means. There is no explanation of different boxes.

The authors constantly compare to FlashAttention, they have not even a single run time comparison. 
I think the paper needs a complete re-write. The method section is using non-standard notation where is unclear what dimensions they are reducing to. The experiments do not talk about fine-tuning overheads, do not have a single timing results.

### Strengths
The idea at a high level looks decent. However, the poor writing and underwhelming evaluation really makes it hard to appreciate it.

### Weaknesses
 The authors propose a method for selecting one head but keeping a small number of Q,K and V matrix. 
I really feel this paper is quite poorly written. First of all, the notations are extremely unclear especially in the method section. The authors have a schematic in
Figure 1 but it's unclear what this schematic means. There is no explanation of different boxes.

The authors constantly compare to FlashAttention, they have not even a single run time comparison. 
I think the paper needs a complete re-write. The method section is using non-standard notation where is unclear what dimensions they are reducing to. The experiments do not talk about fine-tuning overheads, do not have a single timing results.

### Questions
Please see the summary.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents Expert Projection Attention (EPA). It reduces compute and memory requirement for attention by using MoE layers for values and output projections.

### Strengths
the method is clearly illustrated and the analysis in 2.3 is helpful for understanding the difference.

### Weaknesses
1. The author seems to misunderstand the position of flash-attention, see questions below.
2. the scale of experiment is small, how would this method generalize to larger models such as llama?
3. Some experiments have not been finished (Table 4).

### Questions
(1) In what sense flash-attention reduces compute. Do you mean FLOP or wall clock time? FA is exact attention and does not reduce FLOP, it is just a series of clever fusion. If it is wall clock time, then this paper should keep the definition consistent, and provide wall clock time analysis instead of MAC.
(2) "Unlike FlashAttention (Dao et al., 2022), it is research-friendly, because it does not hide the internal details of the attention mechanism inside a CUDA kernel." is an either arguably wrong or highly subjective judgement to flash-attention.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
