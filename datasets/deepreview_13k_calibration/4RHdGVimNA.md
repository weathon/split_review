# StagFormer:  A Staggered Transformer for Decoding Layers in Parallel

- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 3, 3, 5

## Abstract
Standard decoding in a Transformer based language model is inherently sequential as we wait for a token’s embedding to pass through all the layers in the network before starting the generation of the next token. In this work, we propose anew architecture StagFormer (Staggered Transformer), which staggered execution along the time axis and thereby enables parallelizing the decoding process along the depth of the model. We achieve this by breaking the dependency of the token representation at time step $i$ in layer $l$ upon the representations of tokens until time step $i$ from layer $l−1$. Instead, we stagger the execution and only allow a dependency on token representations until time step $i−1$. The later sections of the Transformer still get access to the ”rich” representations from the prior section but only from those token positions which are one time step behind. StagFormer allows for different sections of the model to be executed in parallel yielding up to 33% speedup in decoding while being quality neutral. We also explore many natural variants of this idea.  We present how weight-sharing across the different sections being staggered can be more practical in settings with limited memory. We show how one can approximate a recurrent model during inference using such weight-sharing. We explore the efficacy of using a bounded window attention to pass information from one section to another which helps drive further latency gains for some applications. We also explore demonstrate the scalability of the staggering idea over more than 2 sections of the Transformer.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposed a new architecture StagFormer, which stagger the time dependency between the lower and upper layers. The overall design seems a little non-intuitive, but has a lot of potential for throughput and performance. For example, parameter sharing or local cross-attention could yield better throughput.

### Strengths
- StagFormer architecture is interesting, and has very good potential for both performance and throughput.
- The idea of parameter sharing and recurrent decoding looks good.

### Weaknesses
 - I like the concept and potential of this paper, but I believe that this paper is not well-organized, and looks like unfinished work yet. For example, there is missing reference in L.267 (I guess this refers to Table 3), there are a few results for proof of concept.
- Table 3 is showing few-shot results for gray, blue, red lines in Figure 4 (correct me if I’m wrong.) I wonder why shared-weights StagFormer (blue) outperforms Baseline 2.8B params (red) in some benchmarks, even though it shows higher loss values.
- What makes StagFormer 2.9B to outperform Baseline 2.8B params in Table 1? Is it due to cross-attention in upper layers? This looks somewhat interesting and also confusing because I thought the changed structure (using previous timestep’s intermediate activations) could degrade performance a lot.
- How did the authors measure the decoding time in Table 2? Running separate parameters in parallel is not trivial, I believe. Is it actual time or hypothetical time by assuming parallel execution of them?

### Questions
- For KV-caches, the total KV caches are a little increased by the amount of one layer for cross-attention in upper layers, rights?

### Soundness
2

### Presentation
1

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors present the Staggered Transformer (StagFormer) and its variants which relieve sequential dependancies in the decoding pipeline to enable higher levels of parallel execution.

Consider a transformer with two stacks of layers, A (bottom half) and B (upper half). In vanilla transformers, the input token embedding is passed to stack A. Then, the output of stack A is passed to stack B. All layers apply self-attention on outputs of the previous layer.

In the baseline StagFormer (`Separate-Weights`), stack A is the same. However, stack B takes in the input token embedding rather than the output of stack A.
To supplement this, stack B applies cross-attention on the final outputs of stack A, up until the previous token. In other words, stack B cross-attends to the outputs of *all previous input tokens* from stack A, instead of directly inputting that of the *current* input token. This relieves the dependency of stack B on stack A, within a single decoding step, thus both A and B can be computed simultaneously.

The authors investigate many variants of this design:
1. `Shared-Weights`: this is where stack A and stack B share the same model parameters (excluding the cross-attention layers which are unique to stack B).
2. `Recurrent, Shared-Weights`: this is a unique decoding method for the `Shared-Weights` trained model. In `Shared-Weights` stack A and B are identical, except that stack B applies cross-attention to outputs from stack A. Essentially, the shared stack S (= A = B) is first forwarded without cross-attention, and then forwarded a second time *with* cross-attention, attending to outputs from the first forward pass. The `Recurrent` setting refers to that where the first forward pass is skipped, and cross-attention in the second pass attends to outputs of the "second" pass from the previous decoding step.
3. `p > 2`: this is where more than two stacks are considered.

When compared to vanilla transformers pretrained from scratch, StagFormers show various advantages, mainly:
- `Shared-Weights 2x18L`: StagFormer outperforms the vanilla 18L baseline (with roughly same parameters) in both perplexity and average task performance. Using recurrent decoding (roughly matching 18L baseline computation), average task performance lies between the two. StagFormer underperforms the vanilla 36L baseline with roughly same computation in perplexity, but performs comparably on tasks.
- `Separate-Weights 2x18L`: StagFormer outperforms the vanilla 36L baseline (with roughly same parameters and compute) in both perplexity and task performance.

### Strengths
1. The idea and architecture design are very novel
1. The authors propose numerous variants which showcase the potential extension of the idea across various axes–parallel execution, weight sharing, recurrent computation.
1. The architecture shows clear advantages over vanilla transformers across its variants
1. The writing is easy to follow and visual depiction of the architecture and its variants are superb.

### Weaknesses
 1. **Memory  bottlenecks during decoding may hinder benefits of parallel execution, which is not discussed**: LM decoding is typically bottlenecked by memory rather than compute (see references below). When batch size x context length is small, memory access is dominated by model parameter access. Otherwise, memory access is dominated by KV cache access. While StagFormer can conceptually *parallelize* execution of layers, the associated memory access load cannot be parallelized. In fact, the cross-attention layer will add additional KV cache access overhead. These are critical to assessing the actual wallclock time benefits of decoding with StagFormers compared to vanilla transformers, but is not discussed.
    1. Different variants of StagFormers will have different memory bottlenecks. Examples:
        1. All variants: cross-attention is added in half of layers. Therefore, the overall KV cache access overhead will increase by 50% (relative to that of self-attention, used in all layers). This will have a larger effect on decoding time as batch size x sequence length becomes large.
        1. `Separate-Weights`: both stacks can be executed in parallel, but the memory load is identical as the parameters of both stacks must be retrieved from memory. This means that wall-clock time should typically be identical to vanilla transformers, as decoding is bottlenecked by memory access. `Shared-Weights` can solve this issue.
    1. **It is unclear which StagFormer variant is used in Table 2, raising questions on the performance vs latency comparison**: While Table 2 states that a "comparable quality StagFormer" is 33% faster than baseline transformer during decoding, the exact variant is unclear. Given the reasons above, it seems likely that this is the `Shared-Weights 2x18L` variant. While its average task performance is comparable to baseline 36L, its PPL is in the middle of that between vanilla 18L and 36L. It would be misleading to describe this variant as "comparable quality" to vanilla 36L.
    1. **Missing comparison of performance vs latency across model variants**: Expanding on the point above, a comparison of prefill/decode time across model variants will provide a clear picture on the performance vs latency benefits of each model variant. This could take the form of a single table that lists the PPL, task performance, and prefill/decode time for each model. In the case of  `p > 2, Shared-Weight` variants, I believe this may actually reveal some advantages in terms of latency.
    1. **The additional KV cache overhead of cross attention may slow down decoding for longer contexts**: Since KV cache overhead is quadratic to context length, the decode time advantages as shown in Table 2 will likely diminish with longer contexts, especially in batch decoding. Given the relatively short context length of 1024 tokens considered in this study, compared to modern LLMs with 8K+ context, measurement on longer contexts and larger batch sizes can help gauge the potential of the architecture.
 2. **Misleading task performance of `Recurrent` variant**: In Table 3 (for example), the performance of various tasks are identical between the `Shared-Weights 18L` model and its `Recurrent` counterpart. This is likely because the tasks are measured in a teacher-forcing setting, where the outputs of the prefill stage are used for evaluation. This does not represent the task performance of the `Recurrent` setting, as recurrence is only applied to decoding, as explained in Section 3.2. Only evaluations that use decode-stage outputs should be attributed to the recurrent decoding variant.
 3. **Experimental results on model variants are hard to follow**: The organization of the results section could be improved to make the comparison between different model variants more clear.
    1. Within tables, variations could be better indicated with separate columns, task names could be shortened for space, latency metrics could be included, etc.
    1. Results on different variants are presented in multiple tables without a clear organization.
 4. **Incomplete writing**: "(TODO)" in Line 385, the reference error "??" in Line 267, and numerous typos suggest that this is an incomplete manuscript that is not ready for review.

### Questions
1. Can you describe the architecture shape (vocab size, qkv heads, embedding dimensions) and its justification? The vocab size of 256K is quite high for models of this size.
1. In Lines ~499-501, the authors mention that cross-attention is linear to input length instead of quadratic with window size 1. Isn't it linear with any fixed window size? Considering that the cost of attention mainly stems from KV cache IO during decoding, I think the constant factor with a window size as small as 128 makes the cost of cross-attention negligible compared to self-attention (especially when expanding to modern context lengths of 8K or more).
    1. However, the *increase* in performance when going from full cross-attention (1024) to windowed attention with window size 512 and 128 is strange. Can the authors justify this increase in performance?

### Soundness
2

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
This paper proposes a novel Transformer architecture called StagFormer designed to improve the efficiency of decoding in Transformer-based language models by enabling the parallel execution of layers along the depth axis.

### Strengths
1. StagFormer introduces a unique method to break the sequential dependency of layers in Transformers, enabling parallel execution.
2. Experiments demonstrate significant latency reduction while maintaining or even exceeding the quality of a standard Transformer.
3. The paper investigates different StagFormer variants, offering flexibility and adaptability to various scenarios and resource constraints.
4. The paper effectively explains the StagFormer concept and its variants, supported by clear diagrams and algorithms.

### Weaknesses
1. Limited exploration of p > 2. While the paper explores StagFormer with more than two stacks, it acknowledges performance degradation and the need for further research in this area. The paper does not provide sufficient analysis on the specific causes of this degradation, such as whether it stems from the increased difficulty of predicting further into the future or from the reduced depth of individual stacks. A more detailed investigation into the trade-offs between the number of stacks, their individual depths, and the overall model performance is needed.
2. The paper mentions the communication cost associated with parallel execution but doesn't offer concrete solutions to mitigate it. The communication overhead between parallel stacks, especially when implemented across multiple GPUs or TPUs, can significantly impact the actual speedup achieved. The paper lacks a quantitative analysis of this overhead and how it scales with the number of stacks and the model size. It should also explore potential optimization strategies, such as pipelined execution or optimized data transfer methods.
3. While the Pile dataset is comprehensive, evaluating on additional datasets would strengthen the generalizability of the findings. The Pile dataset, while large, may not fully represent the diversity of real-world text data. Evaluating StagFormer on datasets with different characteristics, such as those with specific domain knowledge or different linguistic styles, would provide a more robust assessment of its performance. This is especially important given that the parallel decoding approach might interact differently with various data distributions.
4. Comparing StagFormer with other methods for efficient Transformer inference, such as speculative decoding, would provide a more comprehensive perspective. The paper should benchmark StagFormer against other state-of-the-art techniques for efficient Transformer inference to better understand its relative strengths and weaknesses. This would help to contextualize the contribution of StagFormer and identify scenarios where it is most beneficial. For example, a comparison with speculative decoding would be particularly relevant, as both aim to reduce decoding latency.

### Questions
1. How does varying the depth of individual stacks in StagFormer affect the trade-off between decoding speed and model quality?
2. What factors determine the optimal number of stacks for a given application, balancing computational efficiency and performance?
3. Could the staggering concept be extended to encoder-decoder Transformers, like those used in machine translation?
4. How well could StagFormer be combined with other techniques, like quantization or knowledge distillation, to further enhance decoding efficiency?

### Soundness
2

### Presentation
2

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
This paper proposes a novel transformer architecture that effectively reduces the number of sequential steps (layers) during the decoding process by staggering the computation across different time-steps. This allows for improved parallelism during decoding individual sequences, providing speedups during inference.

### Strengths
- staggered computation leads to significant improvements in per-time-step decoding speeds while slightly improving performance
- provides results and analysis of different variants of staggered transformers that further explores the architecture's efficacy

### Weaknesses
 - Biggest critique is that it lacks comparative analysis of staggering computation vs. simply increasing the width of the model and lowering the number of layers, as this increases per layer parallelism while decreasing the number of layers leading to a similar improvement in decoding speed. The authors should provide a more thorough analysis of the trade-offs between model depth, width, and staggering, particularly in the context of downstream task performance, as a wider model with fewer layers might achieve similar perplexity scores during training but could exhibit different behavior on downstream tasks.
- This technique is possibly only useful for speeding up decoding when only a single sequence is being decoded. A non-staggered model could in theory process twice the batch size as it has half the parallelism (and hence half the per layer memory requirement) of a model staggered with p=2. This is a crucial point that needs further clarification. The authors should explicitly discuss the memory implications of their approach and how it compares to non-staggered models when considering batch processing capabilities, especially when memory is a constraint.
- StagFormer is possibly slower to train (as inferred by its slower pre-filling speed)
- Paper could be further refined (minor critique): 
    - Some references are configured incorrectly (Table ?? in page 5, "TODO" in page 8)
    - Plots have unnecessary information (Figure 4 doesn't need texts like /1/summarize/train)

### Questions
Addressing the weaknesses outlined above would improve the paper.

### Soundness
3

### Presentation
2

### Contribution
3
