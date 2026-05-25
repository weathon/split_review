Now I have all the information needed. Let me synthesize the final review.

## Summary
This paper proposes VQ-Transplant, a two-stage framework that enables plug-and-play replacement of Vector Quantization (VQ) modules in pre-trained visual tokenizers (specifically VAR) without costly end-to-end retraining. Stage I substitutes the native VQ module with a new one while freezing the encoder-decoder. Stage II performs lightweight decoder adaptation (5 epochs on ImageNet-1k) to realign the decoder with the new quantized latent space. The paper also introduces MMD-VQ, a non-parametric distribution-alignment VQ method using Maximum Mean Discrepancy. Experiments show the framework works with 5 different VQ algorithms across multi-scale and fixed-scale configurations, achieving competitive reconstruction fidelity (MMD VAR rFID 0.81 vs. VAR's 0.92) while requiring only 44 GPU-hours compared to 960 for full VAR training.

## Strengths

1. **Practical and well-motivated framework.** Decoupling VQ module development from full tokenizer retraining addresses a real bottleneck in VQ research. The two-stage approach (substitution + lightweight adaptation) is simple, intuitive, and clearly explained (Section 4.1). The computational savings are substantial (Table 1: 44 vs. 960 GPU-hours), and the comparison to from-scratch training in Table 6 directly validates the efficiency claim.

2. **Broad empirical validation across VQ algorithms and configurations.** The paper tests 5 distinct VQ methods (Vanilla, EMA, Online, Wasserstein, MMD) in both multi-scale (Table 3) and fixed-scale (Table 7) configurations, and at multiple codebook sizes (K=4096, 8192 for multi-scale; K=16384, 32768, 65536 for fixed-scale). This systematically demonstrates that distribution-alignment methods (Wasserstein, MMD) consistently achieve the lowest quantization error and best reconstruction after adaptation, while non-alignment methods (Vanilla, EMA) struggle. The consistency of patterns across configurations strengthens confidence in the framework's generality.

3. **Clear demonstration of the adaptation effect.** Tables 3 and 7 cleanly separate the "substitution" (VQ-only) and "adaptation" (decoder fine-tuning) phases. The substitution phase alone yields degraded reconstruction (e.g., MMD VAR K=4096 rFID 1.52 vs. VAR's 0.92), confirming the decoder-quantization mismatch. After only 5 epochs of adaptation, all distribution-alignment methods recover and surpass the original VAR (MMD VAR reaches 0.91 at K=4096, 0.81 at K=8192). The epoch-by-epoch tracking in Table 4 and the 20-epoch extension in Table 5 further validate that adaptation is both necessary and effective.

4. **Cross-dataset generalization.** The framework achieves strong results on FFHQ (rFID 1.21), CelebA-HQ (rFID 2.60), and LSUN-Churches (rFID 1.79) without architectural changes (Tables 8-10), outperforming prior full-training baselines including VQGAN-LC. This demonstrates that the VQ replacement + lightweight adaptation transfers beyond ImageNet-1k.

## Weaknesses

### Major

1. **Missing control experiment for isolating the effect of VQ replacement from in-distribution fine-tuning.** The paper's headline comparison (MMD VAR rFID 0.81 vs. VAR rFID 0.92) compares the proposed method — which includes decoder adaptation on ImageNet-1k — against the original VAR tokenizer that was pre-trained on OpenImages and evaluated zero-shot on ImageNet-1k without any fine-tuning (Tables 2, 3). The critical missing baseline is: fine-tune the **original** VAR decoder on ImageNet-1k for the same 5 (or 20) epochs **without changing the VQ module**. Without this control, it is impossible to attribute how much of the improvement comes from the VQ replacement itself versus simply from adapting the decoder to the ImageNet-1k distribution. The paper's claim of "superior reconstruction fidelity" is weakened by this confound. Note that the substitution-only results (before adaptation) are worse than the original VAR, so some of the post-adaptation gain is clearly due to fine-tuning; the missing control would quantify how much.

### Minor

2. **Headline improvement relies on a larger codebook.** The paper's central fidelity result (MMD VAR rFID 0.81 vs. VAR's 0.92, Table 2) uses a codebook of size K=8,192, double VAR's K=4,096. At equal codebook size (K=4,096, same 680 tokens), the margin is marginal: 0.91 vs. 0.92. While the paper does report this iso-codebook comparison and does not hide it, the presentation emphasizes the K=8,192 result without sufficiently caveating that the improvement comes partly from a larger codebook. The modest improvement at equal codebook size is worth acknowledging more explicitly.

3. **Speedup claim compares across different datasets and hardware.** The 21.8× speedup (Table 1) compares VQ-Transplant on ImageNet-1k (2×A100, 22 hrs) against VAR training on OpenImages (16×A100, 60 hrs). These differ in dataset size (~7×), hardware count (8×), and training scope (full model vs. VQ+decoder only). The speedup is informative as a practical comparison of total cost, but the paper should acknowledge these confounds and include a per-image or per-epoch cost comparison for transparency. The from-scratch comparison in Table 6 is a cleaner and more defensible efficiency argument.

4. **Unclear whether cross-dataset adaptation was performed per-dataset or transferred.** Section 5.3 evaluates on FFHQ, CelebA-HQ, and LSUN-Churches, showing both "Substitution" and "Adaptation" results (Tables 8-10). However, the paper does not clearly state whether the decoder adaptation was performed separately on each target dataset or whether a single ImageNet-1k-adapted model was evaluated across datasets. If adaptation was done per dataset, the "generalization" claim is partially about adaptation to each target distribution; if transferred, the results are more impressive. This should be clarified.

5. **Fixed-scale partition strategy is not justified or ablated.** The fixed-scale VQ implementation (Section 5, Experiment Setup) partitions 32-d features into two 16-d sub-vectors. This design choice is not motivated, and alternative partition strategies (e.g., 8×4, 4×8, or no partitioning with larger codebooks) are not explored. The impact of this choice on quantization quality is unclear.

### Trivial

6. **No limitations section.** The paper lacks a discussion of limitations (e.g., dependence on a suitable pre-trained tokenizer, instability of adversarial training during adaptation, cases where the framework underperforms as shown by the LDM results in the appendix).

## Nice-to-Haves

- An ablation of the fixed-scale partition strategy (e.g., varying sub-vector dimensionality) to justify the 16+16 design.
- A per-image or per-epoch cost comparison alongside the total GPU-hour speedup to improve transparency.
- A brief discussion of when VQ-Transplant is unlikely to work well (e.g., tokenizers with tight encoder-VQ-decoder coupling), partially covered by the LDM experiment (Appendix D).

## Removed Points

- *"Invalid comparison — confounding VQ replacement with in-distribution fine-tuning"* (Critic's Point 1): **Kept as Major Weakness #1** (after verification, the missing control is real and consequential).
- *"Confounding variables in reconstruction comparisons"* (Critic's Point 2, about unequal token counts/codebooks): **Partially kept as Minor Weakness #2.** The critic's stronger framing (that no iso-parameter comparisons exist) is factually wrong — Table 3 provides iso-codebook comparisons. The valid sub-point about larger codebooks is retained as Minor.
- *"Misleading speedup claim"* (Critic's Point 3): **Removed.** The speedup is a practical comparison of total cost. The paper provides from-scratch training comparisons (Table 6) as a cleaner efficiency baseline. The critic's objection about pre-training cost misunderstands the contribution: VQ-Transplant is designed for researchers who already have access to pre-trained tokenizers. A softened version is retained as Minor Weakness #3.
- *"No isolation of the framework's contribution"* (Critic's Point 4): **Removed as standalone.** The paper does ablate VQ methods within the framework (Tables 3, 7). The specific missing baseline ("fine-tune decoder without VQ change") is already captured in Major Weakness #1.
- *"MMD-VQ's marginal benefit over Wasserstein VQ"*: **Removed.** The data honestly shows MMD and Wasserstein are close; the paper does not overclaim here.
- *"Comparison to from-scratch training missing the right baseline"*: **Removed.** Table 6 directly addresses from-scratch training comparisons.
- *"Code and models are referenced with a placeholder"*: **Removed per hard rule** — the paper cites the repository; questioning its existence is not permitted.
- *Strength: Generic praise of the problem importance*: **Removed.** Replaced with concrete strengths only.
- *Strength: "Dramatic training efficiency"*: **Retained as Strength #1** (supported by Tables 1, 6).

## Novel Insights

The reviews surface one genuinely novel observation beyond the paper's own contributions: the finding that distribution-alignment VQ methods (Wasserstein, MMD) substantially outperform non-alignment methods (Vanilla, EMA, Online) when used with frozen encoder-decoder architectures (Tables 3, 7) — and that this gap is larger after substitution than after adaptation. This suggests that the codebook-feature distribution match is especially critical when the decoder cannot jointly adapt to the VQ's idiosyncrasies. This insight could inform future VQ algorithm design for plug-and-play scenarios.

## Suggestions

1. **Add the critical control experiment:** Fine-tune the original VAR decoder on ImageNet-1k for 5 and 20 epochs without changing the VQ module. Report the same reconstruction metrics and compare directly against VQ-Transplant variants at equal codebook size and token count. This single experiment would substantially strengthen the paper's attribution of improvements to VQ replacement.

2. **More transparent framing of the speedup:** Either (a) present the from-scratch comparison in Table 6 as the primary efficiency argument, or (b) break down the speedup into components (dataset size, hardware, training scope) so readers can assess each factor.

3. **Clarify cross-dataset evaluation protocol:** State explicitly whether decoder adaptation was performed separately on each target dataset or whether a single ImageNet-1k-adapted model was evaluated across all datasets. If the latter, the generalization claim is stronger and should be highlighted.

4. **Add a limitations paragraph.** Acknowledge dependencies (requires pre-trained tokenizer, adversarial training in Stage II may be unstable), and discuss cases where the framework underperforms (as with LDM tokenizer).

## Score and Decision

The paper introduces a practical and well-motivated framework for decoupling VQ development from full tokenizer training. The experiments are broad in scope (5 VQ algorithms, 2 configurations, 4 datasets) and provide useful insights about distribution-alignment methods. However, the missing control experiment (fine-tuning the original VAR decoder on ImageNet-1k without VQ replacement) is a significant gap that weakens the central claim of superior reconstruction fidelity — it conflates VQ improvement with in-distribution adaptation. This is a remediable flaw, and the paper's core contribution (the framework itself) remains valid and useful. On balance, the paper is acceptable with revisions.

**Originality:** Moderate — the VQ-Transplant idea is simple but practically useful. MMD-VQ is incremental over Wasserstein VQ.

**Quality:** Solid empirical methodology overall, but the missing control is a notable gap.

**Clarity:** Well-written and clearly structured.

**Significance:** Potentially high for the VQ research community, as it lowers the barrier to experimenting with new quantization methods.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>