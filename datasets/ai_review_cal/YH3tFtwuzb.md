- Decision: Reject
- Avg Score: 5.40
- Scores: 8, 3, 5, 6, 5
Now I have all the information needed. Let me write the consolidated review.

## Summary

This paper proposes DP-BiTFiT, a differentially private fine-tuning method that trains only the bias terms of pre-trained models while keeping all other parameters frozen. The key insight is that bias gradients avoid the expensive activation storage and tensor multiplication required by weight gradients in DP-SGD. The paper provides a systematic complexity analysis of DP-PEFT methods (novel in itself), demonstrates a memory-efficient implementation that removes forward hooks, and benchmarks accuracy on text (GLUE, E2E) and vision (CIFAR, CelebA) tasks, showing that DP-BiTFiT matches state-of-the-art DP accuracy while being 2–30× faster and using 2–8× less memory than DP full fine-tuning.

## Strengths

1. **Parameter efficiency across diverse architectures**: Table 1 shows DP-BiTFiT trains only ≈0.1% of parameters across all tested models (0.077% for RoBERTa-large, 0.066% for GPT2-large, 0.090% for ViT-large), making it model-agnostic and substantially more parameter-efficient than linear probing (which can be 8% on ResNet50).

2. **Computational overhead independent of the feature dimension T**: Table 2 (complexity analysis) shows DP-BiTFiT's per-layer time overhead is +3Bp and space overhead +Bp with no dependence on T, whereas all weight-based DP methods (Opacus, GhostClip, LoRA, Adapter) incur overheads linear or quadratic in T. This analysis is a genuine contribution — it formalizes why bias-only DP training avoids the dominant DP overhead and is the first systematic complexity comparison of DP-PEFT methods.

3. **Activation-free forward pass realized with measured gains**: Section 3 concretely demonstrates that removing forward hooks yields a 30% training time reduction beyond simply disabling weight gradients (80 min → 63 min on RoBERTa-large/QQP), and the flowcharts in Figure 2 confirm that only DP-BiTFiT avoids caching activations. The complexity analysis in Table 2 formalizes why this is possible for bias-only training but not for weight-based methods.

4. **Strong empirical results with scalability demonstrations**: Figure 4 shows that DP-BiTFiT's memory stays constant as sequence length grows (SST2, RoBERTa-base, T=64→1024) while DP full and DP LoRA memory grows linearly, and similar flat scaling holds for image resolution with ResNet50. Accuracy results show DP-BiTFiT is competitive with SOTA (e.g., 99.0% on CIFAR10 at ε=2, BLEU 65.21 on GPT2-large vs. DP full 64.64 at ε=8).

## Weaknesses

### Fatal
None.

### Major

None. The core claims — that bias-only DP fine-tuning is far more efficient than weight-based DP fine-tuning while achieving competitive accuracy — are well-supported by the complexity analysis and the experimental results.

### Minor

1. **Accuracy comparisons rely on cited numbers from prior papers without full controlled re-implementation.** The accuracy tables (Tables 2, 3, 4) compare DP-BiTFiT against baselines whose numbers are taken directly from prior work (Li et al. 2021, Yu et al. 2021, etc.). The paper states "We use the same setup as [Li et al. 2021]" and "only increasing the learning rate for DP-BiTFiT," but the baseline values themselves are not re-computed under identical conditions. DP fine-tuning results are sensitive to hyperparameters (batch size, clipping threshold, number of epochs, noise multiplier). While this practice is common in the field, it reduces confidence in the claim that DP-BiTFiT "matches state-of-the-art accuracy" — especially when differences between methods are fractions of a percent.

2. **No variance or uncertainty measures are reported.** No standard deviations, error bars, or multiple-seed results are provided for any accuracy or efficiency measurement. DP training involves Poisson subsampling and Gaussian noise, which induce non-negligible run-to-run variation. A difference of <0.5% between methods (e.g., SST2: 92.4 vs 92.2 in Table 2) cannot be assessed as meaningful without some measure of uncertainty. This is a standard expectation in empirical ML papers and weakens the reliability of fine-grained accuracy comparisons.

3. **Training epochs are not stated for text experiments.** The CIFAR experiments specify 3 epochs in the table caption (line 360), but for GLUE (RoBERTa) and E2E (GPT2) experiments, the number of training epochs is only implied by the reference to "same setup as [Li et al. 2021]" and "[Bu et al. 2022]." This should be stated explicitly for reproducibility.

4. **Inconsistent multi-metric behavior on GPT2-large is not discussed.** Table 4 shows that DP-BiTFiT on GPT2-large achieves higher BLEU (65.21 vs. 64.64) but worse perplexity (2.59 vs. 2.26) compared to DP full fine-tuning. The paper highlights only the BLEU improvement without acknowledging or explaining this discrepancy. While different metrics capture different aspects of generation quality, leaving this unaddressed raises questions about whether the improvement is robust across evaluation dimensions.

### Trivial

- The efficiency benchmark figures (Figures 3, 4) do not specify the exact codebase versions or implementation details used for the LoRA and Adapter baselines. The paper specifies GhostClip/MixGhostClip for DP full fine-tuning baselines, but the implementation quality of the other PEFT baselines could affect the relative speed/memory comparisons.

## Nice-to-Haves

- Running a fully controlled head-to-head comparison where all baselines (DP full, LoRA, Adapter, Compacter) are re-implemented in the same codebase with the same hyperparameter search budget, and reporting results over multiple seeds with confidence intervals, would significantly strengthen the accuracy claims.
- Demonstrating DP-BiTFiT on a long-sequence task (e.g., document classification with T > 1024) where weight-based DP methods cannot fit in memory would make the scalability argument more compelling.
- Explicitly stating the RDP-to-(ε,δ) conversion, subsampling probability, and exact noise multiplier used would improve reproducibility.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Baseline implementations for efficiency comparisons are underspecified" (critic's Critical Issue 3)**: The paper does specify the DP algorithm used for full fine-tuning baselines (GhostClip for text, MixGhostClip for images) and presents an explicit complexity analysis. The critic's demand for exact codebase commits is a level of granularity that is not standard for conference publications and is better categorized as a trivial concern. Moved to Trivial tier above.

- **"Privacy accounting details should include subsampling probability and exact RDP conversion"**: These details are typically placed in the appendix, which is stripped by the parser. Per the removal rules, points about missing appendix content that exists in the original submission should be removed.

- **"The paper could strengthen the claim of scalability by showing a concrete example with long-sequence text"**: This is a nice-to-have suggestion, not a weakness. The paper already demonstrates scaling across T=64→1024 and image resolutions. Moved to Nice-to-Haves.

- **Strength: "State-of-the-art accuracy" (Strength Finder #4)**: The accuracy results are competitive and impressive, but the caveat about comparison methodology (weakness #1 above) tempers this claim. Rephrased in the strengths section above as "strong empirical results with scalability demonstrations" which is more accurate given the evidence base.

- **Critic's claim about DP-BiTFiT outperforming DP full on GPT2-large "outperforming" without caveat**: The paper does acknowledge "even outperforming DP full fine-tuning on GPT2-large" which is technically correct for BLEU. The critic's concern about PPL being worse is valid and is retained as a Minor weakness (#4). The claim of "outperforming" more broadly is retained but contextualized.

## Novel Insights

None beyond the paper's own contributions. The two reviews largely converge on the same set of observations: the method is well-motivated and the complexity analysis is a genuine contribution, but the experimental rigor has room for improvement, particularly around controlled comparisons and reporting of variance.

## Suggestions

1. Provide a dedicated table or appendix section reporting all experimental hyperparameters (batch size, learning rate, number of epochs, clipping threshold, noise multiplier, subsampling probability) for every experiment, rather than relying on cross-references to prior work.
2. Run all baselines (DP full, LoRA, Adapter) under the same codebase and report mean ± std over at least 3 seeds. This would address the single largest concern about the validity of the accuracy comparisons.
3. Explicitly discuss the multi-metric behavior on GPT2-large (PPL vs. BLEU trade-off) — a brief explanation would suffice.
4. Add a citation-style link or URL to the codebase in the paper for reproducibility.
