## Summary

This paper formalizes the problem of *reliability scoring*: assessing how much a reported dataset deviates from an unobserved ground truth, given only auxiliary observations from an unknown statistical experiment. The authors propose the **Gram determinant score**, which measures the volume spanned by the empirical joint distribution of reports and observations. Theoretically, they show the score preserves three ground-truth-based reliability orderings (exact-match, Blackwell, approximate Hamming/dist) under certain conditions, prove a uniqueness result that it is the only experiment-agnostic score up to scaling, and establish impossibility results that delineate the fundamental limits of reliability scoring. Empirically, they test the score on synthetic label-manipulation data, CIFAR-10 embeddings, and CES employment data.

---

## Strengths

1. **Well-formalized new problem and solid theoretical framework.** The paper introduces a clean formalism (misreport matrices, reliability orderings, experiment-agnosticism) for a practically important but understudied problem — assessing dataset reliability without ground truth. The hierarchy of orderings (Exact Match → Blackwell → Hamming) and their refinement relationships (Proposition 2.1) provide a principled foundation for the paper.

2. **Genuine theoretical contributions in Theorem 4.2 and Proposition 4.3.** The Gram determinant score is shown to preserve exact-match and Blackwell orderings under exactly the conditions that impossibility results prove are necessary (linearly independent experiments). The uniqueness result (Proposition 4.3) — that any continuous, positive, homogeneous, experiment-agnostic score must be a power of det(QᵀQ) — is a clean and nontrivial characterization that goes beyond merely proposing a new metric. The multiplicative factorization Γ(PQ) = det(PᵀP)·det(Q)² is elegant and gives strong intuition.

3. **Impossibility results (Proposition 3.1) clearly delineate what is achievable.** The paper does not overclaim — it proves exactly when no score can work (exact-match on rich experiment sets, Hamming on diagonally dominant misreport matrices, Blackwell with any linearly dependent experiment). These results motivate the specific restrictions (𝒫_indep, 𝒬_Lδ) used in the positive theorems and give the reader a clear picture of the frontier.

4. **Kernel extension and two estimators broaden applicability.** The plug-in estimator (Definition 4.4) and the kernelized extension (Definition 4.6) show the authors thought about practical deployment. The asymptotic preservation guarantee for the plug-in estimator (Proposition 4.5) connects theory to practice, and the kernel variant handles continuous embeddings (used in the CIFAR-10 experiment).

5. **Experiments span three distinct settings** — synthetic categorical data, image embeddings, and real economic time series — providing initial evidence that the score behaves as expected across different observation processes and corruption types.

---

## Weaknesses

### Major

1. **No comparison against any alternative scoring method in the main paper.** The experimental section evaluates only the Gram determinant score in isolation. The paper discusses related scores (KL-divergence, f-divergence, determinant-based scores, Kong 2024's determinant mutual information) in §1.1 but never implements or compares against any of them. The reader cannot assess whether the Gram determinant offers meaningful advantages over simpler alternatives — e.g., trace of the Gram matrix, negative conditional entropy, or the determinant mutual information that directly inspired this work. The paper mentions Appendix G discusses other candidates, but the main empirical narrative lacks any comparative baselines, which is a significant omission for a paper that claims the score "effectively captures data quality."

2. **The "nearly tight" claim is overstated for the Hamming/dist ordering.** The abstract and introduction assert that the conditions for preserving orderings are "nearly tight." While this is true for exact-match (𝒬_nonperm is exactly the boundary) and Blackwell (𝒫_indep is necessary), it is **not** true for the Hamming/dist ordering. The impossibility (Proposition 3.1) covers 𝒬_dom (allowing ~50% misreport per class), but the positive result (Theorem 4.2 part 3) requires 𝒬_{L,1/64L²d²} — for d=5, L=1, this is δ ≈ 0.0625% of labels. The gap between "any score fails above roughly 50% corruption" and "the Gram determinant is guaranteed to work below 0.06% corruption" is enormous, and calling this gap "nearly tight" is misleading. The paper should either sharpen the bound, acknowledge the gap explicitly, or reframe the claim to apply only to parts 1 and 2 of Theorem 4.2.

### Minor

3. **Limited experimental scope undermines generalizability claims.** The synthetic experiments use a single random generation of (𝐱, 𝐏). The image experiments use a single trained SimCLR model. The employment experiment uses a single small dataset (N=209) with arbitrary 4-bucket discretization. While corruption trials are repeated (M=100), the underlying conditions are not varied, making it unclear whether the observed monotonicity is robust across different observation processes, label distributions, or embedding models.

4. **Theory–experiment gap not discussed.** Theorem 4.2 part 3 guarantees preservation only for δ ≤ 1/(64L²d²) (extremely clean data), yet experiments test corruption up to 50%. The paper does not address why the method succeeds far outside its guaranteed regime — this is either a robustness property worth highlighting or a potential artifact of specific experimental choices. The silence on this gap is a missed opportunity for deeper analysis.

5. **Employment experiment lacks uncertainty quantification.** Figure 3d reports a single score per vintage with no confidence intervals or error bars, despite the small sample size (N=209). The claim that "revisions substantially improve reliability" would be far more convincing with bootstrap intervals or sensitivity analysis over the discretization granularity.

6. **Computational complexity is not discussed.** The plug-in estimator requires computing pairwise agreement frequencies, which naïvely scales O(N²d²). For real-world datasets with large d (e.g., ImageNet-scale label spaces), this could be prohibitive. The paper also does not discuss whether the estimator is practical for the settings it targets.

### Trivial

- **Kendall-tau experimental description (Figure 2d)** is ambiguous: "generate 1000 datasets for each N" — it is unclear whether these are independent draws of (𝐱, 𝐲, 𝐏) or repeated corruption draws from a fixed base. The reviewer's confusion here is legitimate.

---

## Nice-to-Haves

- A minimal baseline comparison (e.g., trace of Gram matrix, negative entropy of reports given observations) would substantially strengthen the empirical section without requiring extensive new experiments.
- Varying the random seed for 𝐏 and 𝐱 in synthetic experiments would help demonstrate robustness of the observed monotonicity.
- Sensitivity analysis for the employment data discretization (e.g., 3 vs 5 buckets) and reporting confidence intervals would improve trust in the real-data result.
- A discussion of why the Gram determinant works at corruption levels far beyond the theoretical guarantee (Theorem 4.2 part 3) — even a heuristic argument — would close an important gap.

---

## Removed Points

The following points from the inputs were removed with justification:

- **"Invertibility of Blackwell ordering fails in practice" (Harsh Critic §2.3).** The paper explicitly acknowledges this — §2.3 states the ordering is defined on 𝒬_reg (invertible, diagonally maximal matrices) and that this restriction is *necessary* for the ordering to be a strict partial order. The critic's concern is already addressed in the paper.
- **"Section 2.3 condition that invertibility fails when some label is never reported."** Again, the paper deliberately restricts to invertible matrices for the Blackwell ordering and does not claim it applies universally. This is a definitional choice, not a flaw.
- **"No discussion of how linearly independent experiments can be verified in practice."** This is outside the paper's scope — the theory assumes the experiment is in 𝒫_indep and provides preservation guarantees; verification in practice is a separate empirical question.
- **"Plug-in estimator O(N²d²) complexity should be discussed" — kept as minor weakness 6 (it is a real omission)**, but the presentation here is about scalabiltiy, which is important to note.
- **"Missing sensitivity analysis for employment" — merged into minor weakness 5.**
- **Various formatting/style nitpicks from the harsh critic** — removed per instructions (parser artifacts, not author errors).
- **Strength Finder's generic "addressed an important problem"** — removed as too generic. Kept only concrete, paper-specific strengths.

---

## Novel Insights

None beyond the paper's own contributions. The synthesis of the two reviews mainly clarifies the gap between the paper's self-assessment ("nearly tight") and the actual numerical bounds, and highlights the absence of baselines as the single most impactful improvement area.

---

## Suggestions

1. **Add at least one baseline comparison** — e.g., compare the Gram determinant against the trace of the Gram matrix or the determinant-based mutual information of Kong (2024) on the synthetic data. This would immediately contextualize the contribution.
2. **Rephrase the "nearly tight" claim** throughout the paper to qualify that it applies to the exact-match and Blackwell orderings, and acknowledge the gap for the Hamming/dist ordering. Add a brief discussion quantifying the gap.
3. **Repeat the synthetic experiments** over multiple random seeds for 𝐏 and 𝐱 (e.g., 10 seeds) to show the monotonicity is robust.
4. **Report confidence intervals** for the employment data scores (e.g., via bootstrap), and provide a brief sensitivity analysis over the number of quantile buckets.
5. **Add an explicit discussion** reconciling the theory (Theorem 4.2 part 3 bound) with the experimental regime (up to 50% corruption), even if only as a conjecture or heuristic observation.
6. **Clarify the Kendall-tau experiment description** — specify whether the 1000 datasets per N are independent draws of (𝐱, 𝐲, 𝐏) or repeated corruptions from a fixed base.

---

## Score and Decision

### Calibration anchors

**Round 1 — Bracketing:** Initial search placed the paper between weak anchors (avg 2.0–3.0, e.g., OdoS6cH8MP on data valuation, cHy00K3Och on coresets) and strong anchors (avg 7.6–8.0, e.g., EUSkm2sVJ6 on data usage inference, E78OaH2s3f on condition alignment). Middle anchors included LVFoynuAQn (4.33, dataset similarity metric), RW37MMrNAi (5.60, autoencoder-based label mistake detection), SpTzsQjgxF (5.75, DPP rule-based data rating). The paper's combination of novel theory with limited empirical evaluation situates it in the upper-middle band.

**Round 2 — Narrowing:** Compared against four anchors in the 5.5–7.25 range:
- **jOVfFAxBf6 (5.75, SE(2)-invariants):** Strong pure-math theory, limited experiments on one dataset. Our paper has weaker experiments but similarly strong theory. Comparable quality, slightly below.
- **OwNoTs2r8e (6.00, No Free Hallucination):** Purely theoretical impossibility results, no experiments, accepted. Our paper has both theory and experiments, but the "nearly tight" overclaim is a presentational flaw this anchor doesn't have. Roughly comparable.
- **icTZCUbtD6 (6.20, H-CAT hardness):** Comprehensive empirical benchmark, accepted. Stronger experiments but weaker theory than our paper.
- **34STseLBrQ (7.25, Polynomial Width):** Strong theoretical result with clean proofs, accepted. Better executed than our paper.

**Final bracket:** The paper is weaker than the 7+ anchors (cleaner theory, stronger experiments) and stronger than the 4.33 anchor (limited theory). It is comparable to the 5.75–6.20 anchors but with a notable presentational flaw (overclaimed "nearly tight") that the comparables do not share. Score set at **5.5**.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>