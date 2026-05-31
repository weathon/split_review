Now I have a good picture of the paper. Let me do calibration search before writing the final review.Initial bracket: **6.0 – 7.5** based on MINDE (6.5, direct continuous analog), SEDD (6.6), and score-based discrete convergence (7.0). Now I'll narrow.Round 1 bracket: **6.0 – 7.5**. Round 2 anchors cluster around 6.0–6.5 (MINDE=6.5, Flow-MI=6.0, InfoNet=5.75). INFO-SEDD is a targeted discrete extension of MINDE with stronger real-world demonstrations and a novel absorbing-noise insight — placing it above MINDE at ~6.5–7.0.

---

## Summary

INFO-SEDD proposes a mutual information and entropy estimator for high-dimensional discrete data by combining Dynkin's formula with Continuous Time Markov Chain (CTMC) score functions. The central technical contribution is that using an absorbing noise process allows a single model trained on the joint distribution to also evaluate marginal scores (Equation 6), eliminating the need for a second separately-trained model. Two variants are introduced—INFO-SEDD-J (joint KL formulation) and INFO-SEDD-C (conditional formulation)—and the method is demonstrated on synthetic benchmarks, text summarization model selection, genomics motif discovery, and Ising model entropy estimation.

---

## Strengths

- **Rigorous CTMC-based formulation with error bounds.** Section 2.2 derives the KL estimator via Dynkin's formula, and Equation (7) provides a concrete error decomposition separating score approximation error from truncation bias (the latter decaying exponentially in T). This gives the estimator clear consistency guarantees not available to variational estimators.

- **Non-obvious absorbing-process design enabling single-model inference.** Equation (6) shows that under the absorbing CTMC, the marginal score ratio $\vec{p}_t^X(x)/\vec{p}_t^X(x')$ can be computed by querying the joint model with Y masked to the absorbing state ∅. This is a concrete, non-trivial insight that reduces compute overhead and enables MI estimation across arbitrary variable subsets without retraining.

- **Strong empirical accuracy in high-MI, high-dimensional synthetic settings.** Table 1 shows INFO-SEDD-J achieving 9.92 ± 0.12 at MI=10, 20.02 ± 0.21 at MI=20, through 47.77 ± 1.18 at MI=50, while all seven competitors either plateau or diverge. The margin is decisive, not incremental.

- **Consistent estimates on real-world text summarization.** Figure 1 shows both INFO-SEDD variants growing approximately linearly with ρ and landing within the entropy-rate range [256ρ, 303ρ] nats derived from independent prior estimates, while variational competitors severely underestimate or behave non-monotonically.

- **Practically validated downstream application (model selection).** Table 2 shows INFO-SEDD-C achieving Pearson r = 0.740 with human consistency judgments on the SUMMEVAL dataset—the highest among all tested methods—demonstrating that the estimated MI is not a mere mathematical exercise but a useful signal for NLP practitioners.

- **Genomics consistency test with competitor comparison.** Figure 4 shows INFO-SEDD-C closely tracking the classifier-based reference MI curve across all ρ values on the HUMAN vs. WORM dataset, with competitors visibly degrading at higher ρ, providing an independently grounded reference for validation.

---

## Weaknesses

### Fatal
None.

### Major

- **INFO-SEDD-J exhibits large positive bias at ρ = 0 in the text consistency test, with no diagnosis offered.** Figure 1's description makes clear that "Infosed-J (green) shows MI values starting around 10²" even when ρ = 0 (all text–summary pairs are random, so true MI ≈ 0). The paper acknowledges only in passing that "INFO-SEDD-C obtains MI estimates closer to zero than the joint variant, when ρ = 0.0," but provides no explanation or diagnosis. The most likely cause—that randomly paired English texts still share vocabulary, syntax, and topical structure making the joint score model see apparent correlation—is a structural limitation of INFO-SEDD-J for text data. This directly affects the interpretation of Table 2: INFO-SEDD-J's correlation of 0.550 with human consistency may partly reflect a distributional-similarity artifact rather than genuine MI. The paper presents both variants as valid estimators without warning practitioners against using INFO-SEDD-J on domains where X and Y come from the same distribution family.

- **Synthetic benchmark is constructed so that MI = D throughout, creating a favorable factorized regime.** All rows in Table 1 satisfy MI = D (10 nats at D=10, 20 nats at D=20, etc.), meaning each position pair (xᵢ, yᵢ) contributes exactly one nat independently. The CTMC's sparse rate matrices, which modify one token at a time, are well-suited to this factorized structure. The paper never tests a case where information is concentrated in a small number of cross-dimensional correlations (e.g., MI=40 with D=10 and non-factorized dependencies). While the real-world results (text, DNA) do involve complex dependencies and INFO-SEDD still performs well, Table 1 cannot be read as evidence of robustness to concentrated cross-dimensional MI—that scenario remains untested.

### Minor

- **Motif discovery result (Figure 5) is presented purely descriptively with no competitor.** The TATA-box localization in *Arabidopsis thaliana* is the paper's most visually compelling result, but no competing method's profile is shown. The justification—"other MI estimators would need different training runs for each window"—is a valid practical argument, but it does not establish that competitors would fail to localize the motif even with per-window training. A brief discussion of what a window-retrained competitor would look like (or why it would fail) is needed to strengthen this claim.

- **The D|χ| scaling of the error bound in Equation (7) is never empirically validated.** The bound's first term scales as $\bar{\sigma}(T) D |\chi|$, meaning at D=50 and |χ|=4 the prefactor is 200× the score approximation error. The sample-complexity ablation shows accurate estimates at 10³ samples (Appendix C.1.5), but this does not tell practitioners when D|χ| scaling becomes the binding constraint relative to sample size. The bound is stated but not shown to be tight or informative in practice.

### Trivial
None that warrant mention after filtering parser artifacts.

---

## Nice-to-Haves

- An experiment with MI concentrated in a few cross-dimensional correlations (e.g., MI=40, D=10, non-factorized) would test whether the CTMC approximation degrades gracefully in that regime and significantly strengthen the synthetic evaluation.
- Explicit practitioner guidance on when to prefer INFO-SEDD-C over INFO-SEDD-J. The paper presents both as valid, but the ρ=0 text behavior strongly suggests INFO-SEDD-C as the default for domains where X and Y come from the same distribution family.
- Moving the Ising model entropy results (Appendix D) into the main paper, even as a summary—exact ground truth is rare in this area and would provide a third independently verified data point.
- Clarifying the training protocol for consistency tests: is a single model trained once (at ρ=1 or on mixed data) and evaluated at all ρ values, or is a separate model trained per ρ? This distinction matters for interpreting the ρ=0 behavior, particularly for INFO-SEDD-J.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

1. **"INFO-SEDD-J bias is due to distributional overlap and constitutes a structural limitation invalidating Table 2"** (Harsh critic framing the bias issue as near-fatal): The paper does show INFO-SEDD-C achieving r=0.740, the highest correlation in Table 2, and the overall claim that INFO-SEDD outperforms competitors in model selection is supported by the -C variant. The -J bias is a real issue (retained as Major) but does not invalidate the core contribution since INFO-SEDD-C remains well-behaved. Demoted from near-fatal to Major.

2. **"The comparison in Figure 4 may partly reflect how poorly embedding-based methods interact with CADUCEUS rather than a general CTMC advantage"** (Harsh critic): This is a speculative confound. All methods use the same CADUCEUS backbone under the same experimental conditions, which is a fair comparison. The paper does not overclaim beyond this setup. Removed.

3. **"Extension to mixed continuous/discrete data via Generator Matching understates non-trivial challenges"** (Harsh critic): This concern is about a stated future direction, not a result in the paper. Scope-creep criticism. Removed.

4. **MINDE's failed curve should be shown in Figure 1** (Harsh critic): A formatting/presentation preference, not a substantive concern. Removed.

5. **Strength: "Important problem targeted"** (Strength Finder): Generic importance claim without specific grounding. Removed.

---

## Novel Insights

The Harsh Critic's observation about the synthetic benchmark design is genuinely insightful: by construction, all Table 1 experiments have MI = D with factorized per-position dependence, which aligns optimally with the CTMC's sparse unit-Hamming-distance transitions. While the real-world results partially compensate, this means the synthetic benchmark is not an independent stress test for the cross-dimensional dependence regime. The paper would benefit from explicitly acknowledging this scope limitation while pointing to the real-world experiments as complementary evidence.

The absorbing-process insight enabling single-model marginal scores (Equation 6) is the paper's cleanest novel finding—it is a direct consequence of absorbing dynamics and has practical downstream value for subset MI estimation without retraining, as demonstrated in the TATA-box sliding-window experiment.

---

## Suggestions

1. **Add a diagnostic for the INFO-SEDD-J ρ=0 bias.** A simple experiment: evaluate INFO-SEDD-J on synthetic data where X and Y are drawn from *different* distribution families (not English text) at ρ=0 to determine whether the bias is general or domain-specific. If it is text-specific, explicitly recommend INFO-SEDD-C for domains with overlapping marginals.

2. **Include one non-factorized synthetic experiment.** Fix D=10 and vary MI from 5 to 40 nats using a non-factorized coupling (e.g., XOR-type joint distribution). This would provide independent evidence of robustness beyond the D=MI regime.

3. **Provide at least a qualitative competitor comparison for Figure 5.** Even if training per-window is impractical, a single trained baseline evaluated with per-window masking (similar to INFO-SEDD-J's approach) would situate the motif discovery result.

4. **State the consistency test training protocol explicitly** (single pre-trained model vs. per-ρ model) to rule out the confound that shuffling test pairs at ρ=0 does not reflect in-distribution behavior.

---

## Score and Decision

**Anchor comparison summary:**

| Path | Avg score | Round | Comparison to INFO-SEDD |
|---|---|---|---|
| 0kWd8SJq8d.md (MINDE) | 6.50 | 1 & 2 | Direct continuous-domain analog; INFO-SEDD adds genuine discrete contribution, absorbing-noise insight, and stronger real-world applications |
| 71mqtQdKB9.md (SEDD) | 6.60 | 1 | Discrete diffusion language modeling; foundational to INFO-SEDD but doesn't target MI estimation |
| pq1WUegkza.md (convergence of score-based discrete diffusion) | 7.00 | 1 | Theoretical focus without applications; INFO-SEDD is more applied but has real-world validation |
| peNgxpbdxB.md (discrete diffusion samplers) | 6.00 | 1 | More focused on combinatorial optimization than MI; comparable scope |
| PyHRUMxKbT.md (InfoNet) | 5.75 | 2 | Rejected; less principled approach, continuous data only |
| KC2MViQASx.md (f-divergence MI) | 5.60 | 2 | Rejected; incremental variational work |
| spDUv05cEq.md (flow-based variational MI) | 6.00 | 2 | Accepted; comparable scope but less novel design |

**Round 1 bracket**: 6.0 – 7.5.

**Round 2 narrowing**: MINDE (6.5) is the closest analog — it introduced diffusion-based MI estimation for continuous data and scored 6.5. INFO-SEDD extends this to discrete data with:
- A technically non-trivial adaptation (Dynkin's formula vs. Girsanov's theorem for discrete CTMCs)
- A novel absorbing-process trick that avoids dual-model training (not present in MINDE)
- Two practical real-world application domains (text, genomics) with competitor comparisons
- A stronger set of downstream tasks (model selection, motif discovery)

Against these advantages, INFO-SEDD-J has a clear and undiagnosed bias issue in text, and the synthetic benchmark is favorably designed. INFO-SEDD-C is robustly validated. The paper is strictly stronger than MINDE in application breadth and the absorbing-process insight is novel, placing it above 6.5. The ρ=0 bias issue and benchmark design keep it from reaching 7.5. Final score: **7.0**.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>