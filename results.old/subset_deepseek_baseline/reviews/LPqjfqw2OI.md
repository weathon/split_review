## Summary

The paper introduces Factorization Memory, a recurrent neural network architecture that maintains multiple memory states and updates them selectively using learned affinity scores. A sparse variant updates only the top-\(k\) most relevant states at each step, keeping inference cost proportional to \(k\) rather than the full memory size. The model is designed to be parallelizable during training (via prefix scan) and efficient at inference, aiming to match Transformer performance on short contexts while exceeding it on long contexts. Experiments on models up to 1.7B parameters report competitive test loss on 1024-token windows, better extrapolation to 2048 and 128K tokens, and inference speedups over Mamba-2.

## Strengths

- **Novel architecture with a clean mechanism.** The idea of using the same learned affinity distribution for both memory write (update) and memory read (merge) is elegant and directly enables the sparse formulation. This differs from prior sparse RNN proposals by tying the two operations, which naturally keeps only the active memory states in the computation graph.
- **Thorough scaling-law analysis.** The paper systematically varies model size (62M-1.7B) and training FLOPs, presenting loss frontiers for all three architectures on both the training context length and a doubled context length. This goes beyond a single-model comparison and gives insight into how performance changes with scale.
- **Empirical evidence of sparse-update effectiveness.** Figure 5 demonstrates that updating only 25% of the memory states achieves the same test loss as the dense version when the total number of memory states is large enough, and that increasing memory width continues to help even with sparse activation. This is a non-trivial result that validates the design.
- **Multilingual evaluation.** The downstream evaluation includes both English and Japanese benchmarks, showing consistent improvements over Mamba-2 and Transformer in both languages. This broadens the validity of the findings beyond a single language.

## Weaknesses

### Major

- **Long-context evaluation methodology for baselines is not described.** The paper claims “superior extrapolation” to 2048 tokens and 128K tokens, but it never explains how the Transformer baseline – which was trained on 1024-token sequences – is evaluated on longer contexts. If the Transformer simply attended to the last 1024 tokens (or used no positional adaptation), the resulting loss increase is expected and the comparison becomes unfair. Similarly, the Mamba-2 baseline may or may not have been adapted; the paper should at least state the evaluation procedure. Without this clarification, the central claim of long-context superiority is not properly supported. This weakness affects the key takeaway of the paper.
- **No downstream long-context benchmarks.** The paper evaluates long-context performance only through test loss on long documents. While loss is informative, it is not a direct measure of task-level ability. The downstream tasks in Table 1 are all relatively short (MMLU, HellaSwag, etc.) and do not require the model to leverage tokens beyond a few hundred. To convincingly demonstrate better long-context capabilities, the authors should include at least one long-context benchmark (e.g., LongBench, Scrolls, or a dedicated long-document QA task). The long-context loss advantage may not translate to better task performance.

### Minor

- **Downstream results show only point estimates.** No confidence intervals, standard deviations, or significance tests are reported for the 1B-model evaluations in Table 1. Given the small absolute differences (e.g., 30.98 vs 29.53), it is unclear whether the improvements are reliable or simply noise.
- **Inference speed comparison lacks kernel details.** The paper reports a 35-40% speedup over Mamba-2 using “optimized CUDA/Triton kernels,” but does not describe the kernel design or explain why the sparse update yields this advantage. Part of the gain may come from a less optimized Mamba-2 baseline rather than intrinsic architectural superiority. The code is not released during review, making the speed claim hard to verify.
- **Memory scaling experiments are limited to a single model size.** Figure 5 uses models of only 60-70M parameters. Whether the sparse-update advantage holds at larger scales is not tested.

### Trivial

- The temperature \(\tau\) is mentioned as a hyperparameter for controlling the sharpness of \(\alpha_t\), but it is only introduced in the memory scaling experiments (Section 4.1.3) and not in the main model description. It should be defined in Section 3.

## Nice-to-Haves

- Include long-context downstream evaluations (e.g., summarization, multi-document QA) to strengthen the claim of practical superiority.
- Provide detailed pseudo-code or complexity analysis (FLOPs per step) for the sparse memory update, compared against Mamba-2’s update.
- Release the custom CUDA/Triton kernels to allow reproduction of the speed results.
- Add a comparison against a hybrid model (e.g., Hymba or Griffin) to see how much of the long-context gain is due to removing attention vs. the memory mechanism itself.

## Novel Insights

None beyond the paper’s own contributions.

## Suggestions

- Clarify exactly how the Transformer and Mamba-2 baselines are evaluated on sequences longer than their training context. If position interpolation, sliding windows, or truncation are used, state it explicitly. If none were used, the long-context comparison is invalid and must be corrected.
- Add at least one established long-context benchmark (e.g., LongBench’s NarrativeQA or QMSum) to the downstream evaluation table.
- Report standard deviations or confidence intervals for the downstream task scores to assess significance.
- Provide a complexity table comparing the theoretical FLOPs and memory requirements of Factorization Memory (dense and sparse) against Mamba-2 and Transformer at the same scale.

## Score and Decision

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>