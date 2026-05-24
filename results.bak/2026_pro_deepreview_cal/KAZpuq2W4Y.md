Now I have a thorough understanding of the paper and calibration anchors. Let me produce the consolidated review.

---

## Summary

This paper proposes HOMIL (Higher-Order Multi-Instance Learning), which augments standard attention-based MIL for whole-slide image classification by adding a second-order representation (covariance of cluster features) alongside the conventional first-order attention-pooled mean. It also introduces DBSCAN-based adaptive clustering to reduce computational cost by grouping similar patches before aggregation. Results on CAMELYON16 and TCGA-NSCLC show modest but consistent gains over several baselines, with substantially reduced runtime compared to dynamic-aggregation methods.

## Strengths

- **Clear conceptual motivation grounded in established limitations of MIL.** The paper identifies a concrete gap — standard MIL aggregates only the first-order moment, discarding feature correlations — and proposes a natural extension. The analogy to statistical moments (Section 3.2) provides a clean framing that is easy to follow and makes the contribution legible to a broad audience.

- **Ablation study cleanly isolates the contribution of each component.** Table 3 shows that removing the second-order module (w/o SOM) drops ACC from 96.98% to 95.98% and F1 from 96.54% to 94.94%, while removing clustering (w/o CM) increases runtime by 71% and degrades both ACC and AUC. These ablations convincingly demonstrate that both the covariance representation and the clustering module matter independently.

- **Practical efficiency gains from adaptive clustering are demonstrated.** The DBSCAN-based clustering compresses the number of instances by factors >5 (compression ratios 0.18 and 0.16), yielding total 5-fold runtimes of 310s on CAMELYON16 and 3685s on TCGA-NSCLC — 1.5–35× faster than dynamic-aggregation baselines (TransMIL, MambaMIL, HMIL) while achieving the best or near-best accuracy.

- **Consistent cross-dataset and cross-metric performance.** HOMIL achieves top ACC, AUC, and F1 on both CAMELYON16 (metastasis detection) and TCGA-NSCLC (lung cancer subtyping), two tasks with different diagnostic challenges. The fusion weight analysis (Figure 2b) further shows that the second-order representation is meaningfully integrated (α^(2) ≈ 0.45), not ignored by the model.

## Weaknesses

### Fatal

None.

### Major

- **Narrative claims "attention-weighted covariance" but the computation is an unweighted sum of outer products.** Section 4.1 and 4.3.3 describe the second-order representation as an "attention-weighted covariance matrix," yet the formula (Eq. in §4.3.3, line 156) is **C = Σ_k g̃_k g̃_k^⊤** — a uniform sum with no attention weights on the outer products. The centering uses the attention-weighted mean **v^(1)** (which is correct), but the second-order moment under the attention distribution would be **Σ_k a_k (g_k − v^(1))(g_k − v^(1))^⊤**. The actual statistic is a uniform covariance around the attention-weighted mean. This mismatch between what the paper says it computes and what it actually computes undermines the statistical narrative of §§3.2–4.3.3. The method still captures second-order information, so the issue is not fatal, but the framing must be corrected — either the computation should be revised to include attention weights, or the description should drop the "attention-weighted" qualifier and motivate the covariance differently.

- **No statistical significance testing for the SOTA claim.** Performance gaps over the strongest baselines are small relative to reported standard errors: on CAMELYON16, HOMIL ACC is 96.98 ± 2.43 vs. MambaMIL 96.48 ± 1.37 (gap 0.50pp, within one SE); on TCGA-NSCLC, HOMIL F1 is 92.93 ± 2.62 vs. HMIL 92.83 ± 1.47 (gap 0.10pp). Without paired significance tests across the 5 folds (or confidence intervals for the differences), the paper's central claim of "consistent improvements over strong MIL baselines" is not rigorously supported. The consistent pattern across metrics and datasets is suggestive but does not substitute for a formal test.

### Minor

- **Covariance compression via 1D convolution + double max-pooling lacks justification.** The row-wise 1D convolution with 4 kernels of size 64 followed by two nested max-poolings (§4.3.3) is an ad-hoc compression of a d×d covariance matrix into a d-dimensional vector. The paper provides no reasoning for why this particular operation is chosen over alternatives (e.g., bilinear pooling, flattening + linear projection, or matrix normalization approaches from the GCP literature). It is also unclear what structural information from the full covariance is preserved or discarded. A brief justification or sanity-check comparison would substantially strengthen this design choice.

- **HMIL baseline is not described, obscuring the novelty claim.** HMIL (Jin et al., 2025) is listed as a baseline and its name suggests it already involves higher-order statistics. The paper provides no description of what HMIL does or how HOMIL differs from it. A one-paragraph summary of HMIL's mechanism and the key differences would let readers assess the novelty of HOMIL relative to existing higher-order MIL work.

- **The claim that DBSCAN forms small clusters for pathological regions is not empirically verified.** Section 4.2 asserts that "pathological patches … form small clusters or remain as outliers, enabling fine-grained processing of critical regions." This is a central motivation for choosing DBSCAN, but no evidence is provided — e.g., cluster sizes stratified by tissue type, or correspondence between small clusters and high-attention regions. The claim is plausible given DBSCAN's density-adaptive property, but without verification it remains an assumption.

### Trivial

- The abstract describes computing "the covariance matrix of the patch representation vectors across the entire slide" (unweighted), while §§4.1–4.3.3 use the "attention-weighted" language — an inconsistency that should be resolved alongside the major fix above.
- The ablation table (Table 3) reports standard errors for the full model but not for the ablation variants, making it harder to assess whether ablation differences are statistically meaningful.

## Nice-to-Haves

- A linear-probe experiment comparing classification from the full covariance matrix vs. the compressed v^(2) vector would directly test whether the compression preserves discriminative second-order information.
- Discussion of why the uniform (unweighted) covariance might actually be preferable to the attention-weighted version — e.g., attention weights could suppress informative but low-attention feature correlations — would turn the narrative mismatch into an interesting design choice.
- Reporting standard errors for all ablation variants in Table 3.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"Figure 1 labeling of v^(2) (n × d) is incorrect" (Harsh Critic)** — This appears to be a parser artifact from the figure caption extraction, not an actual error in the original paper. The figure description in the parsed text is garbled. REMOVED.

2. **"Sensitivity analysis (Appendix) is not discussed in the main text" (Harsh Critic)** — The paper explicitly discusses the sensitivity analysis on lines 291–292: "we conduct a sensitivity analysis on the key hyperparameters of the clustering module (Appendix: Sensitivity Analysis). Results show our method maintains stable, high performance across a broad range of settings." REMOVED — the claim is factually incorrect.

3. **"The use of PCA + DBSCAN … discards within-cluster variation" followed by "the paper does not discuss how this affects the ability to capture patch-level feature correlations" (Harsh Critic)** — The paper does discuss cluster feature aggregation via mean pooling (§4.1, Step 2). The concern about within-cluster variation loss is a reasonable observation but is factored into the broader clustering design trade-off (efficiency vs. fidelity). The paper openly trades some within-cluster detail for computational efficiency. This is not a hidden or unexamined issue. REMOVED as a standalone weakness — the efficiency-accuracy trade-off is explicit.

4. **"The method lacks any analysis of whether the compressed covariance vector actually preserves discriminative second-order information" (Harsh Critic)** — This is a real concern but is better categorized under the Minor weakness about the compression method lacking justification, which is already included. The harsh critic's phrasing implies a fatal gap, but the ablation study (Table 3, w/o SOM) already shows that including the second-order module improves performance, providing indirect evidence that useful information is preserved. REMOVED as a standalone weakness; the concern is folded into the existing Minor point about compression justification.

5. **Strength Finder: "This paper addressed an important problem" / "This paper targeted an interesting question"** — Generic, content-free statements. REMOVED.

6. **"The paper rests on … a fundamental mismatch between the statistical motivation and the actual computation [that] weakens the contribution" claimed as fatal (Harsh Critic)** — While the mismatch is real (retained as Major above), it is not fatal. The method computes a genuine covariance around an attention-weighted mean and the ablation shows the second-order component helps. The paper can fix this by adjusting the narrative or computation. The harsh critic overstates the severity. DEMOTED from Fatal to Major.

## Novel Insights

None beyond the paper's own contributions. The reviewers' observations largely confirm or qualify claims already present in the paper rather than surfacing genuinely new interpretations.

## Suggestions

- **Align the computation with the narrative.** Either (a) revise the covariance formula to **C = Σ_k a_k (g_k − v^(1))(g_k − v^(1))^⊤** and claim the genuine attention-weighted second moment, or (b) drop the "attention-weighted" language and motivate the unweighted covariance as a complementary global descriptor of feature spread. Option (a) is cleaner and preserves the elegant statistical framing.

- **Add paired significance tests.** A simple paired t-test (or Wilcoxon) across the 5 folds comparing HOMIL against the best competitor on each dataset's primary metric would address the major weakness. Even if the differences are not statistically significant at p < 0.05, reporting the p-values would strengthen the paper by honestly characterizing the strength of evidence.

- **Briefly describe HMIL** (2–3 sentences) in the baselines section to clarify what it does and how HOMIL differs.

- **Add a sentence justifying the covariance compression design.** Even a brief note — e.g., "We use 1D convolution with max-pooling because it is parameter-efficient (O(d·m·T) parameters) and preserves local row-wise covariance structure while being invariant to the ordering of feature dimensions" — would help.

---

**Originality:** The idea of extending MIL with second-order moments is conceptually appealing and not widely explored in the WSI literature. The execution borrows standard components (ABMIL, DBSCAN, 1D convolution) but combines them into a coherent framework.

**Importance:** WSI classification is a high-impact application, and more expressive slide-level representations are genuinely needed. The efficiency gains from clustering are practically valuable for deployment.

**Claims supported:** The core claim that second-order statistics help is supported by the ablation (Table 3). The SOTA claim is suggestive but not statistically rigorous. The efficiency claim is well-supported.

**Soundness:** The methodology is largely sound, with the exception of the narrative–computation mismatch in the covariance formulation and the lack of significance testing.

**Clarity:** The paper is generally well-written and easy to follow. The statistical moment framing is intuitive. The main clarity issue is the inconsistent use of "attention-weighted" for the covariance.

**Value to community:** Moderate. The second-order moment extension to MIL is a useful conceptual contribution that could inspire follow-up work, and the empirical results on standard benchmarks are a reasonable baseline for future comparisons.

## Score and Decision

### Calibration anchors

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| Mamba-HMIL (0yVP49SDg0) | 3.25 | R1 | HOMIL is clearly stronger — better motivation, cleaner ablation, clearer writing |
| Pg-GAT (MOCEoNsjEx) | 3.00 | R1 | HOMIL is stronger — more focused contribution, better empirical validation |
| Covariance+Hessian (anek0q7QPL) | 5.00 | R2 | HOMIL is comparable or slightly stronger — more applied but with a clearer use case and ablation |
| PointMIL (T7ZVzuObcj) | 5.50 | R2 | Similar tier — both apply MIL to a domain with a clear methodological twist; HOMIL has better efficiency results |
| Set-level labels (AZW3qlCGTe) | 5.67 | R2 | Similar quality — both have a good idea with moderate empirical validation; HOMIL's ablation is cleaner |
| Covariance pooling theory (q1t0Lmvhty) | 6.00 | R1 | HOMIL is weaker — less theoretical depth, fewer datasets, weaker statistical evidence |

Round 1 bracket: **~4.5–7.0**. Round 2 narrowed to: **~5.0–6.0**. HOMIL sits closest to PointMIL (5.50) and the set-level labels paper (5.67) — a solid empirical contribution with a clear idea but lacking the theoretical rigor or statistical thoroughness that would push it higher.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>