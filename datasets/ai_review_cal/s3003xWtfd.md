- Decision: Reject
- Avg Score: 6.25
- Scores: 3, 8, 6, 8
Now I have all the information needed to produce the consolidated review. Let me write the final output.

## Summary

This paper proposes CoreInfer, a sentence-level adaptive sparse activation method for LLM inference. It defines "sentence-wise core neurons" as the most-frequently-activated subset of neurons across all tokens in a sentence, demonstrates empirically that these correlate with sentence semantics through stability and similarity properties, and uses these correlations to predict core neurons once during pre-filling and fix them throughout decoding — eliminating per-token MLP predictors and their overhead. Evaluations on OPT and LLaMA models across Information Extraction, QA, and Translation tasks show negligible task degradation while achieving up to 10.33× speedup over the Huggingface baseline and 2.72× over PowerInfer on a TITAN XP GPU.

## Strengths

- **Novel sentence-level core neuron formulation with empirical validation.** The paper defines sentence-wise core neurons (Definition 2) and demonstrates on C4 that using only α=0.4/β=0.25 (roughly 10% of neurons) incurs only 2–3% perplexity increase (Fig. 1a,b). The observation that tokens in the same sentence activate similar neurons (Fig. 1c) provides a principled explanation for why a fixed sentence-level subset suffices.

- **Discovery and exploitation of stability/similarity between core neurons and semantics.** Two insights are empirically established: (1) core neurons remain stable when sentence semantics are stable (Fig. 3a,c — adding 64-token continuations to 256-token sentences changes core neurons by only 6%), and (2) core neurons of semantically similar sentences cluster together (Fig. 4a–c, ag_news topics showing layer-wise topic clustering). These insights directly enable the two prediction strategies without requiring per-token MLP predictors.

- **MLP-free architecture delivering substantial measured speedups.** CoreInfer achieves a 10.33× speedup over the Huggingface Transformer and 2.72× over PowerInfer on an NVIDIA TITAN XP (Table 2), with only 7.28GB GPU memory vs. 12GB for the full model. On an A100, it achieves up to 5.5× speedup over the Transformer baseline (Fig. 3, Upper). The elimination of per-token predictors and the sentence-level fixed activation map are clearly identified sources of improvement.

- **Model and task generality across architectures.** The method is evaluated on OPT-6.7b/13b/30b, LLaMA2-7b, and LLaMA3.1-8b across six datasets in three task categories. Performance degradation is typically below 10% relative, and some zero-shot tasks even show slight improvements (e.g., TruthfulQA BLEU max for OPT-13b: 9.35→9.86). The approach works beyond ReLU-based models (covering SiLU-based LLaMA as well).

## Weaknesses

### Fatal
None.

### Major
- **Similarity-guided prediction pipeline is critically underspecified.** The paper states (Sec. 4.1) that "we cluster the training dataset based on this similarity" to form semantic groups, and then select the top-γ most frequent neurons within the assigned group. However, it does not specify: (1) what dataset is used for clustering, (2) what embedding model measures sentence similarity, (3) what clustering algorithm is used, (4) the number of clusters per layer, or (5) the procedure for assigning an input sentence to a cluster during inference. This branch of the method is used for zero-shot tasks (Table 2) where output sentences may be out-of-distribution relative to any fixed cluster set. Without these details, the similarity-guided branch is not reproducible, and its reported results cannot be independently verified or extended.

- **Stability analysis has a limited scope that does not cover key use cases.** The stability experiments (Insight-1, Fig. 3) only test *fluent continuous extensions* of already-long sentences (starting from 256 tokens). The paper then applies stability-guided prediction to few-shot tasks (Information Extraction, few-shot QA and Translation) where the generated output may diverge semantically from the prompt (e.g., generating an answer that changes topic). The paper provides no evidence that core neurons remain stable in such settings. A direct measurement of core-neuron similarity between pre-filling and decoding stages for each few-shot task would be needed to validate the stability hypothesis.

### Minor
- **Spearman correlations are moderate but described as "strong".** The reported correlations between core-neuron similarity and semantic similarity (Table 1: 0.56–0.66 on STS-B, 0.41–0.51 on SICK) are in the moderate range, and similar to prior work ([sementic]: 0.66 on STS-B, 0.51 on SICK). The paper calls these "strong correlations" (Sec. 5.1). While the correlation is sufficient for the application, the characterization is somewhat inflated.

- **No statistical variance reported for task performance.** Table 1 (task performance) reports single numbers without confidence intervals or standard errors. Given the modest performance differences, these would help distinguish signal from noise.

- **Pre-filling overhead not quantified.** The paper claims "zero-cost sparse inference" (abstract, Sec. 1), but the pre-filling stage must compute *all* neuron activations for the prompt to determine core neurons. The end-to-end speedup figures should include this overhead. The pre-filling cost is not reported or broken out from decoding speed.

- **Sparse computation implementation not described.** The paper does not explain how non-core neurons are skipped during decoding — whether via binary masking, custom CUDA kernels, or another mechanism. Without this, the measured speedup cannot be cleanly attributed to sparsity versus implementation-level optimizations.

- **Overstated dichotomy with prior work.** The paper claims prior methods "believe that the activation pattern of neurons cannot be predicted before inference" (Sec. 2). However, PowerInfer explicitly identifies "hot neurons" (frequently activated) globally before inference, so the dichotomy is not as clean as stated. The real distinction is that CoreInfer predicts at the *sentence* level rather than per-token, which is a fairer and more accurate characterization.

### Trivial
None.

## Nice-to-Haves
- Testing on longer input contexts (beyond ~64 tokens) to see whether core neurons shift within a single input.
- An ablation study explaining the occasional zero-shot performance improvements over the original model (e.g., whether they stem from the core-neuron selection or randomness).
- Time breakdown showing pre-filling vs. decoding contributions to end-to-end speed.

## Removed Points

- **"Memory numbers impossible under activation sparsity" (Critic Point 1):** Removed. The critic claims that 7.28GB for OPT-6.7b is "impossible" under activation sparsity because "all model weights remain stored." The paper never makes this claim. In practice, activation-sparse methods (including PowerInfer) selectively load only the weights of active neurons onto the GPU — a standard implementation choice. The paper's language ("deploying the necessary neurons to the GPU," line 442) is consistent with this. The memory numbers are entirely plausible given the method's selective weight loading.

- **"Comparison conflates weight pruning with activation sparsity" (part of Critic Point 4):** Removed. PowerInfer, the key baseline, uses the same selective-weight-loading approach ("hot neurons"), making the comparison valid. The Transformer baseline comparison shows the total system-level speedup of the approach, which is standard practice.

- **"Missing related works":** Removed per instruction — not verifiable without external sources.

- **Various formatting/grammar nitpicks:** Removed per instruction (parser artifacts, not author errors).

## Novel Insights

None beyond the paper's own contributions. The two independent reviews largely converge on the paper's strengths and weaknesses; neither surfaces an angle the paper itself does not discuss.

## Suggestions

1. **Fully specify the similarity-guided pipeline** in the camera-ready version: provide the clustering dataset, embedding model, algorithm, number of clusters per layer, and the assignment procedure for unseen inputs. Without this, the method is not reproducible.

2. **Add a per-task stability validation** for few-shot tasks: measure the actual Jaccard similarity between pre-filling core neurons and decoding core neurons for each few-shot task to confirm the stability hypothesis holds when the generated output can diverge semantically.

3. **Report pre-filling overhead** separately and include it in the end-to-end speedup calculation, or clarify whether the reported decoding speeds already include end-to-end (pre-fill + decode) timing.

4. **Add variance/confidence intervals** to the task performance table and report statistical significance for the comparison against baselines.

5. **Describe the implementation of sparse computation** — how non-core neurons are skipped at the kernel level — to allow readers to assess whether the reported speedup could be reproduced.
