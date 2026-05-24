Now I have enough context to write the review. Let me finalize my analysis.

## Summary

The paper introduces WASI (Weight-Activation Subspace Iteration), a method for resource-constrained fine-tuning of transformer models. WASI jointly compresses both model weights and activations into low-rank subspaces, leveraging the observation that these subspaces remain stable across fine-tuning iterations. By using subspace iteration instead of recomputing full SVD at each step, WASI achieves up to 62× memory reduction and up to 2× FLOPs reduction while maintaining accuracy comparable to vanilla training. Real-hardware validation on a Raspberry Pi 5 shows a 1.4× speedup. The method is evaluated on ViT, SwinT, and TinyLlama across multiple vision datasets and BoolQ.

## Strengths

1. **Joint weight-activation compression with real hardware validation.** The paper demonstrates up to 62× memory reduction and 1.4× real speedup on a Raspberry Pi 5 (Section 4.4, Figure 8) while maintaining accuracy, providing concrete evidence that the method translates theoretical savings to measurable on-device gains — a rarity in this literature.

2. **Subspace stability hypothesis is empirically verified.** Section 4.2 (Figure 3a) explicitly measures rank stability across 40 fine-tuning epochs, and Figure 3b confirms that WSI (subspace iteration) requires 1.36× fewer FLOPs than recomputing full SVD for the same accuracy. This grounds the core technical claim in direct experiment, not just citation of prior theory.

3. **Generality across architectures and datasets.** WASI is evaluated on ViT, SwinT, and TinyLlama across five image datasets (CIFAR-10/100, CUB, Flowers, Pets) and BoolQ (Section 4.3, Figures 5–7), showing consistent accuracy-efficiency trade-offs. This breadth strengthens the claim that the method is not tied to a single architecture.

4. **Dynamic programming for rank selection.** The paper improves ASI's brute-force rank search with a dynamic-programming strategy that reduces search cost from exponential to linear (Section 3.3, Appendix A.2), a concrete algorithmic improvement with practical value.

5. **Better memory efficiency than SVD-LLM.** WASI achieves up to 100× higher memory efficiency than SVD-LLM at similar accuracy (Section 4.3, Figure 5), a direct head-to-head comparison that supports the claim of outperforming prior state-of-the-art weight-compression methods.

## Weaknesses

### Major

1. **TinyLlama evaluation is too weak to support claimed generality to LLMs.** The TinyLlama experiment (Section 4.3, Figure 7) uses ε=0.1 (far more aggressive compression than the ε=0.9 used in vision experiments), fine-tunes only the last 5 layers, and achieves 64–66% accuracy on BoolQ — near the random-guess baseline for binary yes/no questions. The paper reports massive compression ratios (953× activation memory, 30× weight memory) at this extreme setting, but without a meaningful accuracy baseline it is impossible to assess whether the compressed model is actually learning the task. This experiment does little to substantiate the claim that WASI generalizes to language models.

2. **On-device validation is limited to a single configuration.** The Raspberry Pi 5 evaluation (Section 4.4) tests only one model (ViT), one dataset (CIFAR-10), and one hardware platform. Given that the paper's title and framing emphasize on-device learning, the absence of experiments on more constrained devices (e.g., ARM Cortex-M class microcontrollers, or devices with ≤256 KB SRAM as in prior on-device learning work) or across different models/datasets on the same hardware leaves the broad on-device learning claim undersupported. The paper cites Lin et al. (2022) working under a 256KB budget; WASI is not tested under comparable constraints.

3. **The simplifying assumption that the "same optimal rank" applies to both weights and activations (Section 3.4) is unexamined.** The paper states this assumption explicitly in the complexity analysis, but provides no ablation or justification that it is reasonable in practice. Weights and activations have very different dimensionalities and spectral properties; coupling their ranks without empirical validation weakens the theoretical analysis and could mislead practitioners about when WASI is beneficial.

### Minor

4. **No error bars or multiple-run statistics.** All reported results (Figures 5–8) appear to come from single runs. While single-run evaluation is common in this area, given that the accuracy differences between WASI and vanilla at high ε are small (sometimes within ~1%), the absence of variance reporting makes it hard to assess whether the differences are meaningful or noise.

5. **No comparison with LoRA-style parameter-efficient fine-tuning.** The paper acknowledges LoRA in the related work and explains why it is not a direct competitor (it does not reduce inference cost and adds memory overhead during training). However, LoRA is the most widely used approach for efficient transformer fine-tuning, and even a brief comparison (e.g., WASI vs. LoRA for the same memory budget on one dataset) would help readers situate the method's practical value.

### Trivial

6. The abstract claims FLOPs reduction "up to 2×" while Section 4.3 reports "1.5×" at ε=0.9. The abstract's "up to" language is technically not false, but the specific experimental anchor for the 2× claim is not clearly pointed to in the experiments.

## Nice-to-Haves
- An ablation study decoupling weight compression from activation compression (i.e., WASI vs. WSI-only vs. ASI-only) would isolate the marginal benefit of weight compression given that activation compression is the primary driver of memory savings in backpropagation.
- The paper could benefit from wall-clock energy measurements (not just latency) on the Raspberry Pi 5, since energy efficiency is a stated motivation.

## Removed Points
No points to remove — no Harsh Critic input was provided with weaknesses to filter. All weaknesses above are from direct paper reading.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
- Strengthen the LLM evaluation by using a larger ε value that yields non-trivial accuracy, or report accuracy degradation at the ε=0.1 setting relative to a fair baseline.
- Add on-device experiments on a more constrained platform (e.g., a microcontroller or phone-class device) to support the on-device learning framing.
- Report error bars (at minimum across 3 seeds) for the main accuracy-efficiency trade-off curves.
- Include an ablation that separates the contribution of weight compression from activation compression.

## Score and Decision

**Calibration rounds:**

**Round 1 (Bracketing):** Searched across three bands. Weak anchors (score < 3.5) retrieved papers like "Dynamic Rank Adjustment" (2.67) and "FOSL" (3.00) — these are methodologically weaker papers with limited validation. Middle anchors (3.5–7.5) retrieved Trion (5.60, Accept Poster), PLUMAGE (4.67, Reject), and "Attention Layers Add Into Low-Dimensional Residual Subspaces" (4.00, Reject). Strong anchors (>7.5) retrieved papers on unrelated topics (transduction, matrix sign, RL, embodied navigation). **Initial bracket: 4.5–6.5.**

**Round 2 (Narrowing):** Searched within (4.5, 6.5) for on-device ViT compression, retrieving Vulcan (6.00, Accept Poster) and TEMPEST (5.00, Reject). Also searched within (3.5, 7.5) for subspace/low-rank training, confirming Trion (5.60) as the most topically relevant comparison. **Narrowed bracket: 5.0–6.0.**

**Comparison to anchors:**
- **Trion (5.60, Accept Poster):** Similar contribution level — both propose practical low-rank training methods with solid empirical validation. WASI has real hardware results (Raspberry Pi 5) which Trion lacks, but Trion has stronger theoretical grounding and more extensive LLM evaluation. **WASI is comparable to Trion.**
- **Vulcan (6.00, Accept Poster):** Post-training ViT compression for edge with comprehensive experiments. WASI's training-time approach is novel in comparison and its hardware validation is genuine, but Vulcan's experiments are more thorough (multiple hardware platforms, detection/segmentation tasks). **WASI is slightly weaker than Vulcan.**
- **PLUMAGE (4.67, Reject):** Low-rank gradient estimator with unclear practical advantage over baselines and limited real-world validation. **WASI is clearly stronger than PLUMAGE.**

**Final score:** Placing WASI between PLUMAGE (4.67) and Vulcan (6.00), and comparable to Trion (5.60), I assess WASI at **5.5**. The method makes a solid practical contribution with real hardware validation that many comparable papers lack, but the weak LLM evaluation and somewhat incremental nature (combining adapted WSI with improved ASI) prevent a higher score.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>