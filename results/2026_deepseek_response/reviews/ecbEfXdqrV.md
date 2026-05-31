Now let me write the final review with calibration.

## Calibration Analysis

**Round 1 — Bracketing:**
- Weak band (<3.5): Papers at 2.50–3.40 (rejected for limited novelty, insufficient experiments).
- Middle band (3.5–7.5): Papers at 4.25–6.75 (mixed accept/reject decisions).
- Strong band (>7.5): Papers at 8.00 (accepted, near-unanimous strong scores).

The paper clearly exceeds the weak band (it has real contributions — full ADBench benchmark, formal definition, theoretical analysis) and is below the strong band (which requires near-unanimous endorsement and more polished execution). Initial bracket: between 4.5 and 7.0.

**Round 2 — Narrowing (inside bracket):**

Anchors consulted in full:
- "Explaining OOD Paradox through Likelihood Peaks" (5.67, Reject, scores 6,5,6) — similar ambition to explain a phenomenon, had theoretical and experimental limitations; this paper has stronger empirical scope but similar structural issues.
- "Anomaly Detection by Estimating Gradients of Tabular Data" (5.75, Reject, 6,5,6,6) — comparable ADBench-level benchmark; this paper is slightly stronger in contribution framing.
- "AnoLLM" (6.75, Accept, 6,8,8,5) — strong empirical results, accepted despite concerns (computational cost, baseline tuning).
- "MCM" (6.67, Accept, 6,8,6) — novel method with strong experiments, accepted.
- "DRL" (5.75, Accept, 6,5,6,6) — accepted after rebuttal.

The paper is stronger than the 5.67/5.75 cluster (more comprehensive benchmark, cleaner analysis narrative) but weaker than the 6.67/6.75 cluster (less novel methodology, unoperationalized definition, idealized theory). Final score: **6.0**.

---

## Summary

This paper proposes a domain-agnostic formal definition of the "counterintuitive phenomenon" where deep generative models assign higher likelihoods to anomalous data, and investigates whether this phenomenon occurs in tabular anomaly detection. Through experiments on all 47 ADBench tabular datasets (plus 10 CV/NLP embedding datasets) benchmarked against 12 baselines, the paper shows that NF-SLT (Normalizing Flow with Simple Likelihood Test) consistently outperforms other methods, indicating the phenomenon is rare in tabular data. Theoretical and empirical analysis links this success to lower dimensionality and weaker feature correlations in tabular data.

## Strengths

1. **Comprehensive benchmark without selection bias**: Uses all 47 ADBench tabular datasets and 10 CV/NLP embedding datasets without exclusion (Section 4), explicitly motivated to avoid cherry-picking. Table 1 shows NF-SLT achieves the highest average AUROC (0.8575), lowest average rank (3.43), and an extremely low Fail Ratio (0.02) among 12 baselines.

2. **Domain-agnostic formal definition** (Definition 3.3): Addresses vague definitions in prior work by requiring both (i) a high proportion (β) of comparison models outperforming the generative model, and (ii) a minimum significant performance gap (γ), enabling consistent detection across domains. The definition is applied to the CIFAR-10/SVHN case as a concrete example.

3. **Theoretical analysis linking dimensionality to likelihood gap**: Theorem 5.4 shows that under principled conditions the lower bound of the likelihood gap between normal and anomalous data decreases linearly with dimension d; Corollary 5.6 links this to an inverse relationship between the AUROC upper bound and dimensionality, providing formal grounding for why lower-dimensional tabular data is less susceptible to the phenomenon.

4. **Feature correlation analysis via intrinsic dimension ratio**: Section 5.2 quantifies overall feature correlation through the d Ratio (intrinsic/ambient dimension). Using synthetic Gaussian data (Figure 1, left/center) and real datasets (Figure 1, right; Table 4), the paper demonstrates that tabular data have a d Ratio much closer to 1 than image data, supporting the claim that heterogeneous tabular features prevent the phenomenon.

5. **Dimensionality-reduction experiments validate predictions**: Table 2 uses ICA to vary retained dimensions on image OOD pairs, showing AUROC increases as dimension decreases when ℍ(P) > ℍ(Q), consistent with Theorem 5.4. Table 3 (bilinear resize) shows that even simple image downscaling can raise AUROC above 0.5 in formerly inverted cases.

## Weaknesses

### Fatal

None.

### Major

- **Hyperparameter selection procedure may systematically disadvantage baselines**: A single hyperparameter configuration was selected based on the average AUROC across all 47 datasets. This is non-standard for tabular AD benchmarks where per-dataset tuning (via validation splits) is common practice. If some baselines require per-dataset tuning to be competitive while NF-SLT is more robust to fixed hyperparameters, the relative performance ranking could favor NF-SLT. The paper does not show that the chosen configurations are near-optimal for each model on each dataset. (Ref: Section 4, Evaluation paragraph)

### Minor

- **Definition 3.3 thresholds β and γ are not concretized**: The definition introduces parameters β and γ but never assigns concrete values. The paper applies the definition qualitatively (e.g., calling a 0.02 AUROC gap on 'yeast' "small" or the imdb gap "very small"), making the central claim — that the phenomenon "rarely occurs" — imprecise and difficult to verify independently. Some concretization (e.g., β=0.5, γ=0.05, or derived from baseline variance) would make the empirical claim crisp and reproducible. (Ref: Definition 3.3, Section 4 discussion)

- **Theorem 5.4 relies on the product-distribution (independence) assumption**: The theorem assumes P and Q are product distributions, which is violated by virtually all real data. The paper later argues that feature correlation is central to explaining the phenomenon (Section 5.2), creating tension with the theoretical model that assumes none. The experimental evidence in Table 2 (ICA-reduced images) is consistent with the theorem but does not validate it for correlated data, because ICA enforces independence. The paper acknowledges this for raw images (Table 3 discussion) but does not bridge the gap between the idealized theory and real tabular datasets. The theoretical explanation is therefore a proof of concept under restrictive conditions rather than a directly applicable result. (Ref: Theorem 5.4, Section 5.1)

- **No uncertainty quantification or statistical tests**: Table 1 reports average AUROC/AUPRC from 10 repeated experiments but includes no standard deviations, confidence intervals, or statistical tests (e.g., Wilcoxon signed-rank) comparing NF-SLT to baselines. This makes it difficult to assess whether the reported performance differences are statistically reliable. (Ref: Table 1)

- **Bilinear resize explanation lacks direct evidence**: The paper explains the anomalous behavior in Table 3 (e.g., CelebA/SVHN) by post-hoc reasoning that resizing "strengthens correlation" and reduces entropy, but provides no direct measurement of entropy or correlation changes in the resized images. (Ref: Section 5.1, Table 3 discussion)

### Trivial

None.

## Nice-to-Haves

- Verify the entropy condition (ℍ(P) > ℍ(Q)) directly for the image datasets used in Table 2 to strengthen the link between theory and experiments.
- Ablate sensitivity of results to hyperparameter selection for baselines.
- Analyze the impact of the 50% normal training split on the phenomenon.

## Removed Points

These points were flagged by reviewers but removed after cross-checking against the paper:

- "Definition depends on the choice of comparison models" — This is inherent to any relative evaluation; the paper is transparent about its design choice.
- "Prior work already notes limited overlap in tabular data" — The paper explicitly extends prior work (Kirichenko et al., limited to 2 datasets with no baselines) and acknowledges this.
- "No ablation on flow architectures" — Appendix G is mentioned in the paper; the appendix was stripped by the parser.
- "No analysis of anomaly contamination in training set" — The ADBench protocol (50% normal data for training) is a standard one-class setting; this is scope creep.
- "Limited computational cost discussion" — Not a core weakness for an analytical/empirical paper.
- Missing related works — Cannot be verified without external sources.
- Typographical/formatting nitpicks — Parser artifacts, not author errors.
- Claims about "unreleased" or "unavailable" models/datasets — All cited entities are assumed to exist per the review protocol.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Set concrete default values for β and γ** in Definition 3.3 (e.g., β = 0.5, γ = 0.05, or derived from empirical variance across baselines) and apply the definition systematically to compute the fraction of ADBench datasets where the phenomenon occurs. This would turn the qualitative heuristics into a crisp, reproducible result.

2. **Report standard deviations or confidence intervals** for all main results in Table 1, and add a paired statistical test (e.g., Wilcoxon signed-rank across datasets) to support the "outperforms" claim.

3. **Add per-dataset hyperparameter tuning or sensitivity analysis** to address the fairness of comparisons. At minimum, show that the single-configuration results are stable under reasonable hyperparameter variations for baselines.

4. **Acknowledge the independence assumption more explicitly** and either relax it or strengthen the empirical correlation analysis (Section 5.2), which is already the paper's strongest contribution and does not depend on the idealized theory.

5. **Directly verify the entropy condition** for the image datasets used in Table 2 to connect theory and experiments.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>