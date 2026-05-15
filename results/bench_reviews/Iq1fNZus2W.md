Now I have all the information I need. Let me synthesize the final review.

## Summary

This paper addresses the computational bottleneck of multi-condition control in Diffusion Transformers (DiTs), where the "concatenate-and-attend" strategy leads to O(c²n²) complexity. The authors propose PKA (Patch-wise and Keyword-Aware Attention), decomposing full attention into two specialized modules: Position-Aligned Attention (PAA) for spatial conditions (O(N) complexity) and Keyword-Scoped Attention (KSA) for subject-driven conditions (mask-based pruning), complemented by a Condition Cache that reuses KV projections after the first denoising step and an early-timestep sampling strategy for faster fine-tuning. Experiments on FLUX.1 show up to 10× inference speedup and 5.12× VRAM reduction for the attention module.

## Strengths

- **Clean, well-motivated architectural decomposition.** The paper identifies two distinct sparsity patterns in multi-condition DiT attention — diagonal localization for spatial conditions and keyword-confined activation for subject conditions (Figures 2–3) — and designs PAA and KSA as direct structural consequences of these observations. The O(N) PAA formulation (Eq. 2) and the KSA two-step masking (Eqs. 3–4) follow naturally from the evidence.

- **Substantial and convincingly documented efficiency gains.** Figures 7–8 show that PKA achieves 3.90×–10.0× inference speedup and 2.46×–5.12× attention-module VRAM reduction across 1–16 conditions, consistently outperforming both OminiControl2 and UniCombine. The gains grow with condition count, which is precisely the regime where multi-condition control becomes prohibitive.

- **The Condition Cache design is practical and complementary.** By structuring condition tokens to only self-attend (Figure 4b), the KV cache (Figure 4a) incurs zero overhead on the attention pattern itself. This is a simple, orthogonal mechanism that compounds savings across all denoising steps.

- **Early-timestep sampling insight is well-supported.** The perturbation experiment (Figure 5) provides clean evidence that early denoising steps carry most of the conditioning information. The shifted logit-normal distribution (μ=0.5, δ=1.5) shows faster convergence and better final control fidelity in Figure 11.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Quality comparisons are confounded by uncontrolled training recipes, though the asymmetry favors the baselines.** The paper fine-tunes FLUX.1 with LoRA (20k steps, Prodigy optimizer) on a curated subset of Subject200K, while OminiControl2 and UniCombine are compared as-released (full fine-tuning, full Subject200K, AdamW optimizer). The quality improvements in Table 1 (e.g., FID 52.99 vs. 61.03) could reflect differences in optimizer, LoRA regularization effects, or data selection rather than the PKA mechanism alone. That said, *the direction of the asymmetry favors the baselines* (more data, full FT with more parameters), making this a conservative comparison — the method achieves better quality with a weaker training recipe. A controlled experiment retraining all methods with identical data, optimizer, and schedule would cleanly separate architectural gains from training artifacts.

2. **No statistical significance or variance reported.** All metrics in Table 1 are point estimates with no error bars, confidence intervals, or indication of the number of generation seeds. FID is known to have high variance across seeds. Without this, the reported improvements (e.g., FID 52.99 vs. 61.03) cannot be assessed for reliability. This is standard practice in many generative modeling papers but is still a weakness.

3. **Efficiency reported only at the attention-module level, not end-to-end.** Figures 7–8 measure attention-module latency and VRAM. Reporting total generation time and total VRAM (including VAE, text encoder, and sampling loop) would confirm that the attention savings translate to practical wall-clock benefits.

4. **Spatial alignment assumption for PAA is not fully analyzed.** Section 3.2.1 assumes one-to-one spatial correspondence between condition tokens (SP) and noisy image tokens (X). The paper does not discuss how alignment is enforced when condition encoders produce tokens at different resolutions or aspect ratios, nor does it analyze failure cases from misalignment. Since the experiments use only Canny and Depth (same-resolution conditions), the robustness of PAA to resolution mismatch is untested.

5. **KSA mask stability across timesteps is unquantified.** The mask reuse strategy (Eqs. 3–4) relies on temporal consistency cited from prior work, but the paper provides no Jaccard similarity or overlap statistics comparing masks at successive timesteps. If the mask changes significantly between t and t+1, the reuse strategy could degrade subject fidelity.

6. **Early-timestep sampling lacks quantitative ablation.** Figure 11 shows only qualitative results for the early-timestep sampling strategy. No FID, CLIP-I, or controllability metrics are reported for models trained with vs. without the shifted distribution, so the claim of accelerated convergence and "enhanced control fidelity" is supported only by visual inspection.

7. **KSA sparsity statistics are not reported.** The paper uses ε=0.2 as the default threshold but never reports what fraction of image tokens are retained (or the average sparsity ratio). Reporting this across diverse prompts/subjects would help practitioners understand the efficiency-quality trade-off.

8. **The "swa condition" column in Figure 9 is unexplained.** The ablation table includes a column labeled "swa condition" with very low latency and VRAM (13.58s, 198MB) but no description in the text or caption. This appears to be SWA applied to condition tokens, but readers cannot verify.

### Trivial
None.

## Nice-to-Haves
- Controlled retraining of OminiControl2/UniCombine with the same LoRA setup, data subset, and optimizer would cleanly isolate PKA's contribution to quality.
- End-to-end latency and VRAM numbers would confirm practical benefits.
- Reporting variance over 3–5 seeds for all metrics in Table 1.
- Visualization of KSA masks across timesteps to validate the temporal consistency assumption.
- Sparsity statistics (fraction of tokens retained) for KSA at different ε thresholds.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **"Unfair comparison with baselines (Structural)"** — Removed per hard rule on asymmetry favoring baselines. The baselines used full fine-tuning on the full dataset (more training), while the proposed method used LoRA on a curated subset (less training). This makes the comparison *conservative* for the proposed method, not structurally invalid. (Kept as a minor weakness above since a controlled experiment would still be valuable.)

2. **"The paper does not release the subset, making reproduction difficult"** — Removed per hard rule: dataset release concerns are not valid criticisms.

3. **"Missing related works"** — Removed per hard rule: I cannot confirm whether works exist outside my knowledge.

4. **"Missing appendix, missing proofs in appendix"** — Removed per hard rule: parser strips appendix sections; they exist in the original submission.

5. **Strength Finder claim about "competitive quantitative generation quality despite drastic efficiency gains"** — Dropped because it conflicts with the verified weakness about uncontrolled training recipes confounding quality comparisons.

6. **Strength Finder claim about "Generalizable framework"** — Dropped as it's generic and not supported by experiments on diverse condition types beyond Canny, Depth, and Subject.

## Novel Insights

None beyond the paper's own contributions. The reviews converge on the same basic assessment: the efficiency ideas are clean and well-motivated, but the quality evaluation is not as clean as the efficiency evaluation. The tension between the two reviews — the Harsh Critic emphasizing the training-recipe confound and the Strength Finder accepting the quality comparisons at face value — is the central axis of evaluation.

## Suggestions

1. **Retrain baselines under identical conditions.** This is the single most impactful change. Use the same LoRA hyperparameters, same data subset, same optimizer (Prodigy with 20k steps) for OminiControl2 and UniCombine, then re-run Table 1. If PKA still outperforms under controlled conditions, the quality claim is ironclad.

2. **Add error bars or variance to Table 1.** Run each method with at least 3 different seeds and report mean ± std for all metrics. This is a quick fix that substantially improves rigor.

3. **Report end-to-end efficiency.** Add a row to Table 1 or a supplementary table showing total generation time and total VRAM (not just attention module). This would bridge the gap between module-level and practical gains.

4. **Add a brief discussion of PAA alignment.** Clarify how spatial correspondence is maintained when condition encoders output at different resolutions, and note any limitations.

5. **Report KSA mask stability and sparsity.** Include a plot of Jaccard similarity between masks at consecutive timesteps, and a table showing average token retention ratio vs. ε.

6. **Quantify the early-timestep sampling benefit.** Add a row to the ablation showing FID/CLIP-I for μ=0 vs. μ=0.5 with the same total iterations.

## Score and Decision

**Calibration anchors** (all from the human review corpus):

| Anchor | Path | Score | Comparison |
|--------|------|-------|------------|
| SLA (Sparse-Linear Attention) | eD8IPvNoZB.md | 5.00 | Both address DiT attention efficiency through sparsity. SLA has cleaner quality evaluation (fine-tunes and compares to same-baseline). This paper's efficiency gains are more specific to multi-condition but larger in that niche. **This paper is slightly weaker due to uncontrolled quality comparison.** |
| DiffSparse | V3eUas3VCL.md | 4.50 | Both propose efficient DiT mechanisms with similar validation depth. DiffSparse has wider architecture coverage; this paper has larger specific speedups. **Comparable.** |
| SPRINT | aTVollXaaI.md | 5.50 | Stronger validation, cleaner controlled experiments, wider architecture generality. **This paper is weaker.** |
| Scale-DiT | nk33zCmbH7.md | 5.33 | Rejected despite higher score due to novelty concerns. This paper has clearer novelty in its attention decomposition. **This paper is comparable.** |
| SparseD | dwbrZtYP04.md | 5.00 | Cleaner experimental design (lossless acceleration claim well-supported). **This paper is slightly weaker.** |
| DraftAttention | jUNmW3s45i.md | 2.50 | Novelty concerns, missing citations, weak evaluation. **This paper is substantially stronger.** |
| MixDiffusion | t9Wx3W2B0x.md | 3.00 | Training-free multi-condition but high computational overhead. **This paper is substantially stronger.** |
| VIST3A | kI27Niy4xY.md | 8.00 | Oral-level paper with much stronger validation. **This paper does not compare at this level.** |

The paper makes a clean efficiency contribution with well-motivated modules (PAA, KSA, Condition Cache) and documents substantial speedups (up to 10×) and memory savings (up to 5.12×). The quality comparison is the main weakness: different training recipes confound the attribution of quality improvements to PKA alone, though the asymmetry favors the baselines (more data, full fine-tuning), making the comparison conservative. The most comparable anchor, SLA (5.00), has a cleaner quality evaluation but similar contribution type. DiffSparse (4.50) has a similar profile of substantial efficiency gains with some experimental gaps. This paper sits between these two.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>