# Cut Your Losses in Large-Vocabulary Language Models

- Decision: Accept
- Scores: 10, 6, 8, 10

## Abstract
As language models grow ever larger, so do their vocabularies.
This has shifted the memory footprint of LLMs during training disproportionately to one single layer: the cross-entropy in the loss computation.
Cross-entropy builds up a logit matrix with entries for each pair of input tokens and vocabulary items and, for small models, consumes an order of magnitude more memory than the rest of the LLM combined.
We propose Cut Cross-Entropy (\ours), a method that computes the cross-entropy loss without materializing the logits for all tokens into global memory.
Rather, \ours only computes the logit for the correct token and evaluates the log-sum-exp over all logits on the fly.
We implement a custom kernel that performs the matrix multiplications and the log-sum-exp reduction over the vocabulary in flash memory, making global memory consumption for the cross-entropy computation negligible. This has a dramatic effect. Taking the Gemma 2 (2B) model as an example, \ours reduces the memory footprint of the loss computation from 24 GB to 1 MB, and the total training-time memory consumption of the classifier head from 28 GB to 1 GB.
To improve the throughput of \ours, we leverage the inherent sparsity of softmax and propose to skip elements of the gradient computation that have a negligible (i.e., below numerical precision) contribution to the gradient.
Experiments demonstrate that the dramatic reduction in memory consumption is accomplished without sacrificing training speed or convergence

## Human Reviews

## Human Reviewer 1

### Rating
10

### Rating Number
10

### Confidence
4

### Summary
This paper proposes "Cut cross-entropy" (CCE), a method that reduces the memory footprint of computing the cross-entropy loss during LM training dramatically, by never materializing the full matrix of logits/probabilities (which can be huge: batch * sequence_length * vocab_size).  To accomplish this, it realizes that the cross-entropy loss can be broken down into two components: (1) the logit for the correct next token, and (2) the log-sum-exp (log of softmax denominator) --- both of these terms are scalars, and can be computed without materializing the full logit tensor. In particular, (1) is computed via simple vector dot-products (Algorithm 1), while (2) can be computed by accumulating partial sums of the log-sum-exp, without every materializing all elements of the sum at once (Algorithm 2).  For the backward pass (Algorithm 3), the paper proposes two methods --- gradient filtering and vocabulary sorting --- that reduce the backward pass time by skipping gradient computations for blocks of the softmax matrix where all values are < 2^(-12).

Putting all these pieces together, CCE is able to match the speed and quality of existing implementations of the cross-entropy loss, while only requiring a very small percentage of HBM memory (e.g., 1 MB instead of 1GB->24 GB).

### Strengths
- Reducing the memory requirement for computing the CE loss in LLMs is a strong contribution, especially as the vocabulary sizes, batch sizes, and sequence lengths of LLMs continue to grow.  This custom kernel could save many people lots of time trying to get around OOM errors during training, and make it easier to train models with larger sequence lengths/batch sizes/vocab sizes.
- The algorithm is clever and elegant, taking inspiration from FlashAttention, which avoids materializing full attention score matrix during attention computation.
- The experiments demonstrate that CCE can reduce training memory requirements without impacting quality/convergence during training, or training speed, relative to strong baselines (e.g., torch.compile).

### Weaknesses
 - I think the section about the backward pass could be explained more clearly (see my questions below for points of confusion that could be clarified).
- I think there could have been additional experiments to explore how CCE performs relative to baselines as different hyperparameters vary (e.g., relative size of vocabulary vs sequence length vs. hidden dim, sparsity of S, etc.).
- Are there regimes where CCE is meaningfully slower than the torch.compile method?
- There were a few elements of the backward computation that I think could be explained more clearly:
  - What is the "v" index in the lines 339-341 (Algorithm 3)?
  - Why doesn't recomputing the large $C^T E$ matrix multiplication in the backward pass (Algorithm 3) lead to slow-downs? If I understand correctly, this is because although much extra time is spent on this recomputation, less time is spent on the subsequent matrix multiplications, due to the gradient filtering/vocab sorting? Can you break down more granularly how much time each component of CCE (especially the backward pass) takes, and compare this to the naive implementations, so that it becomes clear what is happening here?
  - Can you explain this paragraph in more detail please: "We implement the second matrix multiplication in the main memory of the GPU, as a blockwise implementation would require storing or synchronizing S..."? Here, is "main memory" HBM?
  - I think there may be mistakes in the backward pass equations at the bottom of page 5 (lines 266-269).  Letting V be vocab size, L be sequence length, and D be hidden dimension, we can see that C is [D,V], E is [D,L], and S is [V,L].  Then for the matrix shapes to be correct, shouldn't it be:
    - $d/dE = C (S \cdot LSE_{grad})$ --- which is a [D,V] * [V,L] multiplication, which gives [D,L], which is the correct shape of E,
    - $d/dC = E (S \cdot LSE_{grad})^T$ --- which is a [D,L] * [L,V] multiplication, which gives [D,V], which is the correct shape of C.
  - Can you include, at least in the appendix, a version of algorithm 3 that also includes the backward pass of the indexed matrix multiplication? 
  - NIT: I think it could be clearer to update the notation to be something like the following, to make Algorithms 2 and 3 easier to follow. For example, you could use $V$, $L$, $D$ to denote vocab size, sequence length, and hidden dim, and correspondingly $V_B$, $L_B$, and $D_B$ to denote the dimensions of the blocks, and $B_V = V/V_B$, $B_L = L/L_B$, $B_D = D/D_B$ to denote the number of blocks, and v, l, d to index into these blocks.
- Can you add a discussion around sequence parallelism approaches, which can also reduce logit memory per GPU by splitting logits along sequence dimensions?

### Questions
- Are there regimes where CCE is meaningfully slower than the torch.compile method?
- There were a few elements of the backward computation that I think could be explained more clearly:
  - What is the "v" index in the lines 339-341 (Algorithm 3)?
  - Why doesn't recomputing the large $C^T E$ matrix multiplication in the backward pass (Algorithm 3) lead to slow-downs? If I understand correctly, this is because although much extra time is spent on this recomputation, less time is spent on the subsequent matrix multiplications, due to the gradient filtering/vocab sorting? Can you break down more granularly how much time each component of CCE (especially the backward pass) takes, and compare this to the naive implementations, so that it becomes clear what is happening here?
  - Can you explain this paragraph in more detail please: "We implement the second matrix multiplication in the main memory of the GPU, as a blockwise implementation would require storing or synchronizing S..."? Here, is "main memory" HBM?
  - I think there may be mistakes in the backward pass equations at the bottom of page 5 (lines 266-269).  Letting V be vocab size, L be sequence length, and D be hidden dimension, we can see that C is [D,V], E is [D,L], and S is [V,L].  Then for the matrix shapes to be correct, shouldn't it be:
    - $d/dE = C (S \cdot LSE_{grad})$ --- which is a [D,V] * [V,L] multiplication, which gives [D,L], which is the correct shape of E,
    - $d/dC = E (S \cdot LSE_{grad})^T$ --- which is a [D,L] * [L,V] multiplication, which gives [D,V], which is the correct shape of C.
  - Can you include, at least in the appendix, a version of algorithm 3 that also includes the backward pass of the indexed matrix multiplication? 
  - NIT: I think it could be clearer to update the notation to be something like the following, to make Algorithms 2 and 3 easier to follow. For example, you could use $V$, $L$, $D$ to denote vocab size, sequence length, and hidden dim, and correspondingly $V_B$, $L_B$, and $D_B$ to denote the dimensions of the blocks, and $B_V = V/V_B$, $B_L = L/L_B$, $B_D = D/D_B$ to denote the number of blocks, and v, l, d to index into these blocks.
- Can you add a discussion around sequence parallelism approaches, which can also reduce logit memory per GPU by splitting logits along sequence dimensions?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper proposes a novel method of skipping most of the unneeded computation inside LM heads during training when using cross-entropy loss. It's key contributions are:
- A memory efficient indexed matrix multiplication method, which employs sparsity to accelerate the computation.
- A memory efficient linear-log-sum-exp method, which employs dynamic chunking to reduce memory requirements.
- Gradient filtering, which further improves sparsity of the gradient computation.
- Vocabulary sorting, which allows entire chunks to be skipped during computation.

The method is evaulated on both speed, memory usage and convergence, where it shows massive improvements in memory usage for computing losses compared to alternative methods, marginal improvements in speed and negligible degradation in convergence and training quality.

### Strengths
- Well motivated problem. Reducing the memory footprint of LLMs during training is important.
- Method generalizes beyond transformer LLMs.
- Demonstrates convergence guarantees compared to cross entropy.
- Extensive benchmark results.

### Weaknesses
 - Preliminaries (section 3) does not adequately prepare the reader for the complexity of the notation in section 4. 

- Section 4 is particularly hard to understand if the reader does not have a deep understanding of GPU kernels and the architecture of modern LLMs. 
  - There is a lack of key insights, CCE seems like an arbitrary monolithic algorithm that came out of nowhere.

  - Prehaps decoupling the theoretical reasoning from the actual GPU implementation could make the explanation clearer. For example, in line 201, it says "section 4.2 describes how to compute the [...] operation efficiently", but it is initially unclear to the reader why that operation might be efficient unless the reader can fully understand the intricacies of creating an efficient GPU kernel as described in section 4.2. Same goes for section 4.1 and 4.3.

  - Otherwise, starting from an already efficient GPU implementation of standard CE and focusing on the steps needed to modify it into the CCE method could further improve readability and clarity.

- A lack of ablation studies for the extensive modifications brought on by CCE
  - Section 4.1, 4.2 and 4.3 makes a large number of significant assumptions, modifications and improvements to the traditional CE algorithm, it is not clear whether each modification is actually necessary or which are the most important ones.
  - Unclear whether CCE's improvements is GPU dependent or not. Would it work in non-parallel cases such as on a single-threaded CPU?

### Questions
- What are the theoretical justifications on why CCE might be much more computationally and memory efficient compared to traditional CE? For example, why can't you apply the same chunking strategies used in CCE for traditional CE? 
- What are the key insights that make CCE work? It seems to me currently that all of the contributions are mixed together, where CCE is an all or nothing monolithic algorithm.
- How does CCE compare to CE on the CPU, or non-parallel cases? Are the improvements algorithmic or does it need to take advantage of GPU parallelization strategies?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes Cut Cross-Entropy(CCE) to reduce the memory consumption of Classifier Head and CrossEntropy Loss. They find that the vocabulary of LLMs continuously to grows, and under the gradient checkpointing setting, these part takes more than 50% of the memory consumption. CCE reduce the memory overhead by fusing the classifier head and the calculation of cross entropy loss into 1 kernel, and not materializing the intermediate logits in the forward process. In the backward pass they re-compute the intermediate values to avoid this additional memory overhead (which is quite similar to FlashAttention's design). They further propose to leverage the sparsity pattern in the gradient of classifier head to reduce the amount of computation. CCE reduce the memory overhead by 20x for "Loss+Gradient" part and their loss curve matches the BF16 training baseline.

### Strengths
1. The problem this paper trying to solve is well-motivated.
2. The solution to avoid the materialization of the large logit tensor is clear and easy to understand
3. The CCE component is easy to deploy in realistic setting.
4. The performance do not degrade (since the algorithm is nearly lossless considering the high sparsity level)
5. The paper writing is very clear and easy to follow (represent C, E, and LSE in different colors)

### Weaknesses
1. "The probabilities materialized by the cross-entropy layer account for 89% of the memory consumption of Gemma 2 for single sequence x with length N = 80000". Can you provide details about how the 89% number is calculated and include a brief calculation or breakdown of the memory usage in the paper or appendix? It would be beneficial to see a breakdown of memory usage for the logits, activations, and other components, specifying the data types (e.g., float32, bfloat16) and how these contribute to the overall 89% figure. This should include the memory footprint of the intermediate tensors involved in the cross-entropy calculation.
2. Does this assumption still hold true when gradient checkpointing = False? I think most of the analysis in this paper is based on the assumption that gradient checkpointing = True. Include a subsection to discuss or analysis of how your method performs when gradient checkpointing is disabled is appreciated. It would be useful to understand the memory consumption of the logits and activations without gradient checkpointing, and how CCE's memory savings compare in that scenario.
3. Similar to 2, In Table 1, can you explain where 1477MB, 8000MB, 4000MB, and 24000MB come from? If I understand correctly, the logits.shape is (8192, 256000) in float32, which should take 8000MB memory in total. A detailed explanation of how these memory numbers are derived, including the specific operations and data types involved, is needed. It's unclear why the memory usage varies so much across different implementations.
4. In Section 4.3, the Gradient filtering paragraph, "If stored in bfloat16 with a 7-bit fraction, any value below 2^{-12} will likely be ignored due to truncation in the summation or rounding in the normalization." Can you explain this in detail? Providing a brief explanation of the numerical precision issues in bfloat16 and how they relate to the gradient filtering threshold is appreciated. Specifically, how the 7-bit mantissa of bfloat16 leads to the 2^-12 threshold needs clarification. A more detailed explanation of how the limited precision affects the summation and normalization steps would be beneficial.

### Questions
Please see weakness.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
10

### Rating Number
10

### Confidence
3

### Summary
This work proposes Cut Cross-Entropy (CCE) to address the massive memory footprint of the standard cross-entropy loss calculation in LLM training. CCE tiles and fuses the logits indexing and the matmul between tiles of `lm_head` and embeddings in the forward pass. In backward propagation, CCE introduces gradient filtering and vocabulary sorting to optimize memory access pattern with negligible approximation errors. CCE presents experiments showing the effectively reduced memory footprint and indistinguishable influence on fine-tuning.

### Strengths
- This paper identifies a new challenge brought by the large size of vocabulary of language models, especially LLMs, i.e., the massive memory footprint consumed by the cross-entropy loss computation.
- The tricks of gradient filtering and vocabulary sorting in the proposed method are enlightening.
- The author implemented CUDA kernels to support the algorithm and provides experiments to verify the reduced memory footprint and latency.

### Weaknesses
 - The symbols in the derivation of CCE can be clearer. For example, the symbols in page 4 between line 186 and 215, such as $C^T$, $C_{x_i}^T$, $C_X$, and $(C^T E)_X$, look confusing at first glance. It may be helpful to have a table of symbol definition in the appendix.
- Experiments on how the memory and latency of CCE kernel varies with the vocab size & model family can be added. 
  - Current Tab 1 presents the memory and latency results of Gemma-2-2B.  The vocab size of Gemma-2-2B is 256000, which is larger than other LLMs. For example, the vocab size is 128256 for Llama-3-8B/70B/405B, 32768 for mistral-7B-v0.3, and 32064 for Phi-3.5. If the size of `lm_head` is `(model_hidden_size, vocab_size)`. When the `model_hidden_size` increases, do we expect a diminishing benefit of CCE? The evaluation will be more comprehensive if the author could discuss:
  - Compared to the baselines, how the memory and latency change if CCE is applied to Gemma-2-27B training (same vocab size as Tab 1, but larger model hidden size)
  - Compared to the baselines, how the memory and latency change if CCE is applied to training of the models like Phi3.5-mini (smaller vocab size, similar model size).



### Questions
- Current Fig. 4 verifies that CCE has negligible influence on LLM fine-tuning. I am also curious about the impact of CCE on LLM pretraining. If an LLM is trained from scratch using CCE, how will the randomly initialized weights influence the gradient filtering and vocab sorting? 

For other questions, please refer to my concerns in the Weakness section.

### Soundness
3

### Presentation
3

### Contribution
4
