Here is the final consolidated review.

---

## Summary

LS-Merge proposes shifting model merging from weight space to a learned latent space. The framework uses a transformer-based VAE to encode LLM weights into a continuous latent manifold, performs merging operations (interpolation, model soup) in that space, then decodes back to parameters. The key claimed innovations are (1) enabling cross-architecture merging (different widths, depths, model families) via dimensionality-matching projection and Gaussian optimal transport alignment, and (2) achieving more robust performance than weight-space averaging through the smoother latent manifold. The paper includes experiments on self-merging, LoRA expert fusion, cross-architecture merging, and ablations on compression and linear vs. non-linear encoding.

## Strengths

1. **Novel formulation of latent-space merging for cross-architecture transfer.** The core idea — encoding LLM weights into a VAE latent space, performing merging operations there, then decoding — is genuinely novel and addresses a real limitation of prior work. Unlike weight-space methods (which require architectural homogeneity) or activation-informed methods (which require forward passes on data), LS-Merge operates purely on static weight snapshots. This opens a new direction for the model merging field.

2. **Strong empirical results on expert merging (Table 3).** LS-Merge(soup) achieves 56.0 MMLU, 60.1 HellaSwag, and 56.1 NLQGraph, outperforming every weight-space baseline across 6 of 8 benchmarks. The best weight-space competitor (Greedy Soup) achieves 50.8 MMLU, 54.6 HellaSwag, and 52.9 NLQGraph — clear, non-marginal improvements. This provides the strongest evidence that latent-space merging can outperform weight-space methods.

3. **Self-merging demonstrates clear improvements (Table 2).** On Gemma-3-1B-it, LS-Merge raises MMLU from 32.20 (base) to 35.13 and MMLU-pro from 7.10 to 10.30, outperforming both the original checkpoint and single-sample VAE reconstruction. This supports the claim that sampling and averaging in latent space captures functionally useful variation.

4. **Weight statistics analysis (Table 1) motivates encoder design.** The paper documents high excess kurtosis (up to ~15) in early self-attention layers across three LLMs. This is useful empirical evidence that LLM weights are heavy-tailed, motivating the two-stage curriculum and transformer-based VAE design.

5. **VAE vs. PCA ablation (Table 8) convincingly justifies non-linear encoding.** PCA collapses to near-random accuracy (25.5 MMLU) even at 1.6× compression, while the VAE retains 96% of base accuracy (39.89 vs. 41.44) and remains stable up to 4×. This clearly validates the need for non-linear manifold learning.

6. **Competitive with activation-based methods without requiring activations (Table 4).** LS-Merge achieves 55.07 MMLU and 36.41 IFEval on Llama-2-13B merges, matching AIM (which requires per-sample activations) and substantially outperforming Task Arithmetic. This shows that a weight-space-only latent approach can rival methods with higher data requirements.

## Weaknesses

### Fatal

None.

### Major

1. **Insufficient evidence for the paper's most distinctive claim: cross-architecture merging.** The only cross-family experiment (LLaMA-3.2-1B → Gemma-3-1B, Table 5) is evaluated on just 3 tasks (WinoGrande, ARC-C, HellaSwag) with no confidence intervals. The reported gains over the base target model are small (+0.92 WinoGrande, +0.56 ARC-C, +1.03 HellaSwag). The paper does not compare against any plausible alternative for cross-architecture knowledge transfer (e.g., using the larger model's outputs to fine-tune the smaller one, distillation, or a simple weight-projection baseline). For the paper's headline claim — "first cross-family merging" — the empirical support is too thin.

2. **Claimed superiority over weight-space averaging lacks head-to-head test on full-size homogeneous models.** The abstract states that "latent-space interpolation is consistently more robust than direct weight-space averaging." However, the paper never directly compares latent interpolation vs. weight interpolation on full-size, non-LoRA homogeneous checkpoints (e.g., two independent fine-tunes of Llama-2-7B on the same base). The comparison on LoRA experts (Table 3) demonstrates the principle on small adapters, but the claim is made generically about all settings. A single experiment on full-size models would either strongly validate or reveal the limits of this central claim.

### Minor

3. **OT alignment ablation is narrow.** The OT alignment is only compared against "no-OPT" (naive latent interpolation without alignment). The paper does not compare against simpler alternatives (mean-only shift, whitening + re-coloring, CCA, or Sinkhorn-based OT), making it unclear whether the full Gaussian covariance matching is necessary. The finding that "OT only" (alignment without interpolation) degrades performance relative to the base model (WinoGrande drops from 56.83 to 51.13) is concerning and not investigated.

4. **Inconsistent evaluation protocols.** Two different evaluation pipelines are used (custom setup for Tables 2/3/6, `lm-eval` for Tables 4/5/7/8). While the switch is acknowledged and justified, it prevents direct comparability across experiments and introduces potential confounds in prompting, few-shot settings, and metric handling.

5. **Missing baseline details hurt reproducibility.** In Table 3, "Data Merge" appears with a dagger (†) but no explanation in the text; "Dare-Ties" appears without a citation. The "Best expert" baseline is ambiguous — it is defined as "best expert per task" but it is unclear whether this is an oracle per-task selection (which would not be a fair baseline) or a single expert for all tasks. These omissions make the comparisons harder to interpret.

6. **Variance reporting is inconsistent.** Tables 2 and 8 report ± values, but Tables 3, 4, and 5 do not. Since several reported gains are small (e.g., LS-Merge vs. AIM in Table 4: 36.02 vs. 36.00 on MBPP, 28.14 vs. 29.27 on HumanEval), the absence of error bars makes it impossible to assess statistical significance.

7. **Layer pairing in Algorithm 1 is heuristic and unvalidated.** When depths differ, layers are paired by index via `min(|L_src|, |L_tgt|)`. This assumes 1-to-1 functional correspondence between layers at the same position — an assumption unlikely to hold across different architectures (e.g., Gemma vs. LLaMA). Alternative pairing strategies (activation-based similarity, layer-type matching) are not explored.

### Trivial

8. **DARE-TIES and Data Merge baselines lack proper citations in the text.** Both appear only as row labels in Table 3 without textual explanation.

## Nice-to-Haves

- Compare OT alignment to simpler alternatives (mean-only shift, whitening + re-coloring, CCA).
- Add a head-to-head comparison of latent vs. weight-space interpolation on full-size homogeneous models (e.g., two fine-tuned Llama-2-7B checkpoints).
- Expand the cross-family evaluation to more tasks (MMLU, GSM8K) with confidence intervals.
- Include a computational cost breakdown (VAE training time, encoding/decoding overhead per model).
- Ablate the two-stage curriculum (deterministic AE → VAE) to measure its impact on downstream merging.

## Removed Points

These points were flagged during review but are removed from the main assessment for the reasons noted:

- *"The method for heterogeneous merging rests on unvalidated assumptions about latent correspondence" (originally framed as structural/fatal)* — This is incorporated into Minor weakness #7 but the original framing as a fundamental flaw was too strong since the paper demonstrates empirical success despite the heuristic pairing.
- *"Two-stage curriculum is never ablated"* — The paper notes details are in the appendix (which was stripped by the parser); this is a parser artifact issue.
- *"PCA comparison should include a linear autoencoder"* — PCA vs. VAE is a standard comparison for linear vs. non-linear embedding. The gap is so large (25.5 vs. 39.89 MMLU) that a linear autoencoder would not change the conclusion.
- *"Code release is essential"* — Standard reproducibility request but not a weakness of the paper's scientific content per se.
- *"Self-merging overstates the contribution (it's just latent-space SWA)"* — Self-merging is a natural extension of the latent-space framework, and the paper clearly frames it as such rather than claiming it is fundamentally new.
- *"Criticism about the PCA experiment being unfair"* — The explicit purpose of the experiment is to test whether the manifold is linear; PCA is the canonical linear method for this test.
- *"Missing related works"* — I do not have external sources to confirm their existence.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Directly test the central claim**: Add an experiment comparing latent interpolation vs. weight interpolation on full-size homogeneous models (e.g., two fine-tuned Llama-2-7B checkpoints) across a diverse set of benchmarks with error bars. This is the single most important experiment the paper is missing.

2. **Strengthen the cross-architecture evidence**: Expand the cross-family evaluation to more tasks (MMLU, GSM8K, HellaSwag is not enough), report confidence intervals, and compare against a simple baseline (e.g., using the larger model's weights to initialize the smaller architecture via projection, then brief fine-tuning).

3. **Broaden the OT ablation**: Compare OT alignment against mean-only alignment and whitening + re-coloring to isolate whether full covariance matching is necessary.

4. **Clarify baselines**: Explain what "Data Merge" is, cite DARE-TIES, and clarify the "Best Expert" definition. Add variance estimates to Tables 3, 4, and 5.

## Score and Decision

**Calibration anchors used:**

| Anchor | Path | Avg Score | Round | Comparison to this paper |
|---|---|---|---|---|
| WIDEN | 2pvMZKGYDR | 5.67 | R1/R2 | Similar scope (extending merging to harder setting); LS-Merge has stronger novelty but weaker evidence for core claim |
| What Matters for Model Merging at Scale? | fvUVe2gJh0 | 5.33 | R1/R2 | Comprehensive empirical study; LS-Merge has more novel methodology |
| UQ-Merge | SO0manOwUF | 5.50 | R2 | MLLM merging with uncertainty; similar quality and scope |
| SeedLoRA | jkCvAAcSDa | 5.50 | R2 | LoRA fusion; LS-Merge is more novel |
| SUPERMERGE | lIdc5DUplq | 4.33 | R1 | Gradient-based merging; LS-Merge is more novel and has stronger experiments |
| Style-conditioned Latent Interpolation | kVcEiWtld9 | 4.25 | R1 | Also uses VAE on LLM weights for interpolation; LS-Merge is more ambitious and thorough |
| ATM: Alternating Tuning and Merging | lNtio1tdbL | 3.00 | R1 | Weaker paper with significant issues; LS-Merge is clearly stronger |

**Round 1 bracket:** 4.5 – 6.5 (middle band).  
**Round 2 narrowing:** Compared to WIDEN (5.67) and UQ-Merge (5.50), LS-Merge has stronger novelty but weaker support for its most distinctive claim. It is comparable to the 5.50-range anchors in overall quality.  
**Final score: 5.5.** The paper presents a genuinely novel framework with solid evidence in some settings (expert merging, self-merging, ablations), but its core differentiating contribution (cross-architecture merging) has insufficient support, and a central claim (superiority over weight-space averaging on full models) lacks direct testing. The methodology is worthwhile but the empirical case is not yet convincing enough for acceptance.

**Decision: Reject.**

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>