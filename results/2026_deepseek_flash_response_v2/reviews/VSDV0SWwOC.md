## Summary

LS-Merge proposes shifting LLM model merging from weight space to a learned latent space, using a Transformer-VAE with a two-stage training curriculum and optimal transport alignment to enable both homogeneous and cross-architecture merging. On expert fusion (Table 3), the method achieves sizeable gains over weight-space baselines (e.g., +5.2 MMLU over Greedy Soup), and the PCA vs. VAE ablation (Table 8) cleanly demonstrates that linear compression is structurally inadequate. However, the paper's most distinctive claim — heterogeneous (cross-architecture) merging — rests on thin evidence (3 benchmarks, marginal gains, an OT component that harms when used alone), and the VAE's usable compression range is very narrow (r ≤ 1.6), which limits practical advantage given the overhead of training and running the encoder-decoder.

## Strengths

- **Expert merging results are strong and consistent.** Table 3 shows LS-Merge(soup) achieving 56.0 MMLU, 60.1 HellaSwag, and 56.1 NLQGraph versus the best weight-space baseline (Greedy Soup) at 50.8, 54.6, and 52.9 — margins of 3–5+ absolute points across an 8-benchmark suite. This is a clear and non-trivial improvement over established methods in a setting where weight-space merging already applies.

- **PCA vs. VAE ablation (Table 8) cleanly motivates the non-linear design.** At identical compression ratios, PCA collapses MMLU to ~25.5% while the VAE retains ~39.9% (96% of base performance). Importantly, PCA is equally poor at r=1.6 and r=4.0, showing the failure is structural (linearity) rather than one of capacity. This evidence directly justifies the VAE design choice.

- **Self-merging (Table 2) shows non-trivial gains on single models.** Gemma-3-1B-it improves from 32.20 to 35.13 on MMLU (+2.93) and from 28.70 to 31.16 on HellaSwag (+2.46), verified with standard deviations across 3 runs. This addresses the limitation that most merging methods require multiple models.

- **Weight-distribution analysis (Table 1, Figure 2) is a useful empirical contribution.** The documentation of high kurtosis (up to ~15) and sharp PCA eigenvalue decay across Gemma and LLaMA families provides concrete motivation for encoder design choices, and the finding is informative for future weight-encoding work.

## Weaknesses

### Fatal
None.

### Major

1. **Heterogeneous merging — the paper's most distinctive claim — is weakly supported.** Cross-family results (Table 5) are reported on only 3 benchmarks (WinoGrande, ARC-C, HellaSwag) with marginal gains (e.g., WinoGrande: 56.83→57.75, +0.92). More concerning: OT alignment alone *harms* performance on every benchmark (e.g., WinoGrande 56.83→51.13, ARC-C 42.78→34.25), and the full method merely recovers from this damage. The paper does not address why OT degrades latents when used without interpolation. Intra-family results (Figure 4a) are presented as a bar chart without numeric labels. The optimal mixing coefficient λ=0.1 is very close to the target-only regime (90% target, 10% source), raising the question of how much cross-architecture knowledge is actually being transferred versus the gain being a small perturbation effect. For a claimed core contribution, the evidence is not commensurate with the scope of the claim.

2. **The VAE's usable compression range is very narrow.** Table 7 shows that at r=1.6, the VAE generalizes acceptably to unseen models (~2% drop). At r=2, HellaSwag drops from 49.07→38.88 for Gemma-3-1B-it and MMLU from 40.76→32.22. At r=4, models are near-random (e.g., 25.66 HellaSwag). The paper frames this as a "clear trade-off," but r=1.6 is very mild compression — it is unclear whether the overhead of training a VAE, encoding all weights, and decoding is practically justified over simpler weight-space methods that achieve stronger results on expert merging (as the paper's own Table 3 shows weight-space methods are weaker, but the point is about the overhead-vs-benefit for the latent representation itself). The paper acknowledges in Section 6 that the method does not "strictly require a tight bottleneck," but this somewhat undercuts the motivation for learning a compressed latent representation at all.

### Minor

3. **Missing computational cost details.** The paper never reports VAE training GPU-hours, VAE parameter count relative to the encoded models, number of training weight snapshots used, or the inference overhead of encoding and decoding weights. These are essential for any practical assessment of the method's feasibility.

4. **Compression ratio r is not defined.** Values r={1.6, 2.0, 4.0} are used throughout Tables 7–8 without specifying whether r = original parameter count / latent code size or another definition.

5. **Self-merging lacks a weight-space stochastic baseline.** Table 2 compares against the base model and single-sample VAE reconstruction, but does not control for whether the gains come from stochastic perturbation-and-averaging in general (e.g., adding noise to weights in weight space and averaging multiple samples). The improvement could reflect regularization from the VAE's inherent randomness rather than anything specific to the latent manifold.

6. **No variance reported for heterogeneous results.** Table 5 reports no standard deviations despite very small margins (0.5–1%), while other tables (2, 8) include σ values. Given the marginal gains, variance information matters for interpreting whether these improvements are meaningful.

7. **Tension between the heavy-tailed weight analysis and the Gaussian OT approximation.** Section 3.1 documents that raw LLM weights are heavily leptokurtic (kurtosis ~15), and the paper uses this to argue encoders must "preserve tail events." Yet the OT alignment (Equation 2) approximates each layer's latent distribution as Gaussian (fully characterized by its empirical mean and covariance). While this tension is partially mitigated because the VAE regularizes latents toward a Gaussian prior via the KL term, and because the raw weight analysis concerns a different distribution than the latent representations, the paper does not discuss this issue at all.

### Trivial

8. **Figure 4a lacks numeric labels on bars.** The intra-family heterogeneous merging figure shows accuracy visually but provides no concrete numbers, making independent interpretation difficult.

## Nice-to-Haves

- Evaluate cross-architecture merging on the full 8-benchmark suite used in Table 3 rather than only 3 benchmarks.
- Provide a weight-space stochastic baseline for self-merging (e.g., Gaussian noise perturbation and averaging).
- Directly address why OT alignment alone degrades performance.
- Report computational costs to enable practical feasibility assessment.

## Removed Points

These points were flagged for removal by the filtering process; they are reproduced here only in case they prove useful during discussion:

- **Criticism that OT Gaussian assumption is "fatal" internal inconsistency:** Removed because (a) the OT operates on *latent* representations, which the VAE explicitly regularizes toward a Gaussian prior via the KL term, not on raw weights; (b) the paper acknowledges the Gaussian approximation explicitly ("it can approximate..."); (c) the weight-distribution analysis concerns a different distribution (raw weights) than the one being aligned (latents). The point is kept as Minor (#7) but the framing as "fatal" or "structural" is removed.

- **Criticism that PCA vs VAE comparison is unfair:** Removed — the comparison is methodologically appropriate for testing whether linear methods suffice; the paper's claim is precisely that linear methods are structurally inadequate, and the ablation is correctly designed to test this.

- **Criticism that the paper "should not be accepted based on its strongest claimed contribution":** Removed as an editorial judgment rather than a specific weakness. The assessment is captured substantively in the weaknesses above.

- **Complaints about missing appendix content:** Removed per instructions (appendix is stripped by the parser).

- **Request for more models/datasets in general:** Generic criticism that would apply to most papers; the existing evaluation on 8 benchmarks (Table 3) is already reasonable.

- **Strength about cross-family heterogeneous merging:** This is a borderline case — the results are positive but marginal. It is kept implicitly through the paper's narrative but not listed as a standalone strength given the weak evidence.

## Novel Insights

None beyond the paper's own contributions. The most useful observations — the weight distribution characterization and the PCA vs. VAE comparison — are already presented by the authors.

## Suggestions

1. Strengthen the heterogeneous merging evaluation by (a) testing on the full 8-benchmark suite, (b) reporting variances for all results, (c) analyzing why OT alone degrades performance, and (d) exploring whether a non-Gaussian transport method resolves the tension with the paper's own weight statistics.

2. Report the computational cost (GPU-hours, VAE size, dataset size) so readers can assess practical feasibility.

3. Add a weight-space stochastic perturbation baseline for the self-merging experiment to disentangle the effect of stochastic averaging from latent-space exploration.

4. Define the compression ratio r explicitly, and discuss whether mild compression (r≈1.6) justifies the overhead of training and running a VAE.

5. Add numeric labels to the bars in Figure 4.

## Score and Decision

**Calibration Anchors (all rounds):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| lNtio1tdbL.md (ATM) | 3.00 | R1 | Fundamentally flawed (misaligned with merging goals). LS-Merge is much stronger. |
| XVHXVdoV11.md (Collective Model Intelligence) | 3.40 | R1 | Exploratory paper. LS-Merge has stronger empirical contributions. |
| kVcEiWtld9.md (Few-shot Style VAE) | 4.25 | R1 | Similar VAE-on-weights technique but weaker evaluation. LS-Merge is stronger. |
| kF3tNnhkvX.md (Iterative Preference Learning) | 4.60 | R2 | Merging for preference optimization. LS-Merge has more novel approach. |
| fvUVe2gJh0.md (What Matters for Model Merging at Scale) | 5.33 | R2 | Evaluation paper. LS-Merge has stronger novel contribution as a method paper. |
| Bq3fEAGXUL.md (Realistic Evaluation of Model Merging) | 5.33 | R2 | Evaluation paper. Different contribution type. |
| 2pvMZKGYDR.md (WIDEN) | 5.67 | R1/R2 | Extends merging to PT models. Comparable quality: LS-Merge has more novel approach but weaker evidence for headline claim. |
| utz99dx2RN.md (VAE-Var) | 6.50 | R2 | Unrelated domain (meteorology). |
| 9ca9eHNrdH.md (Sparse Autoencoders) | 7.00 | R2 | Unrelated topic (mechanistic interpretability). |
| 9Cu8MRmhq2.md (Norton OT) | 8.00 | R1 | Unrelated topic (video-language). |
| vf5aUZT0Fz.md (DEPT) | 8.00 | R1 | Unrelated topic (pretraining). |

**Round-1 bracket:** 5.0–7.0 (based on comparisons to weak anchors around 3.0, middle anchors around 4–5.67, and strong anchors around 8.0 on unrelated topics).

**Round-2 narrowing:** Compared against the most relevant anchors (WIDEN at 5.67, evaluation papers at 5.33, the VAE-style paper at 4.25). LS-Merge is clearly stronger than papers scoring ≤4.25, comparable to WIDEN (5.67) but with a more novel approach and weaker evidence for its headline claim. The paper's strong expert merging results and clean VAE ablation place it above evaluation papers at 5.33, but the thin heterogeneous evidence prevents it from reaching the 6+ range.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>