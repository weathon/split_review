Now I have a thorough understanding of the paper. Let me compose my final consolidated review after verifying all claims against the actual paper text.

---

## Summary

This paper proposes PASLE (Progressive Adaptation with Selective Label Enhancement), a test-time adaptation framework that replaces definite one-hot pseudo-labels with candidate pseudo-label sets for uncertain samples. The framework partitions test data into confident and uncertain subsets using a dynamic threshold, assigns one-hot labels to confident samples and candidate label sets to uncertain ones, and progressively refines these assignments as the model adapts. Experiments on domain generalization benchmarks (PACS, VLCS, OfficeHome, DomainNet) and corruption benchmarks (CIFAR-10-C, CIFAR-100-C) show improvements over several baselines.

## Strengths

- **Novel use of candidate pseudo-label sets for uncertain TTA samples.** Instead of the standard one-hot pseudo-labels that cannot be revised, PASLE assigns candidate label sets to uncertain samples, allowing the model to retain uncertainty information and refine decisions as adaptation progresses (Section 3.3, Proposition 1, Eq. 4–7). This directly addresses a real limitation of existing pseudo-labeling TTA methods.
- **Progressive threshold decay mechanism.** The threshold τ(r) decreases linearly over adaptation steps (Eq. 9), naturally reflecting the model's growing confidence as it aligns with the target domain. This is a simple, well-motivated design that connects the algorithm's behavior to the model's evolving state.
- **Strong empirical performance against 10 baselines.** PASLE outperforms all compared methods across four domain generalization datasets with both ResNet-18 and ResNet-50, and on CIFAR-10-C and CIFAR-100-C corruption benchmarks (Tables 1, 2). The reported improvements (5.63% on domain generalization with ResNet-18) are substantial.
- **Robustness analysis.** Parameter sensitivity analysis (Figure 2a) shows stable performance across a range of τ_start and τ_end values, and PASLE consistently outperforms baselines under varying batch sizes (Figure 2b), supporting practical applicability.

## Weaknesses

### Fatal
None.

### Major

1. **Eq. (6) defines the uncertain subset in a way that mathematically overlaps with the confident subset.**  
   The confident set is defined as D_H^r = {x | d^p - d^q > τ(r)} (Eq. 4). The uncertain set is defined as D_M^r = {x' | ∃ j ∈ Y, d'^p - d'^j > τ(r)} (Eq. 6). Since a confident sample satisfies d^p - d^q > τ(r), it also satisfies "there exists j (namely j=q) such that d^p - d^j > τ(r)," placing it in both sets. The paper presents these as a partition ("split" — line 74), but the written definitions are not disjoint. The intended semantics is clear from context (D_M^r should contain samples where some labels are eliminated but the correct label is not uniquely determined), but the formal definition needs correction. The algorithm description cannot be reproduced as written without ambiguity about how the two subsets are constructed.

2. **Missing strong baselines for a 2026 submission.** The paper compares against 10 methods (TENT, SHOT-IM, T3A, TAST, TSD, etc.) but omits several standard online TTA methods including EATA (Niu et al., 2023), SAR (Zhao et al., 2023), and CoTTA (Zhang et al., 2022). These methods are cited in the related work (lines 22–23) but not included as experimental baselines. Given that these have been standard baselines for several years, the headline claim "PASLE achieves the best performance across all benchmark datasets" cannot be properly evaluated without comparing against them.

3. **Ablation of the core contribution is limited to a single dataset.** The ablation study (PASLE vs. PASLE-NC, which removes candidate pseudo-labels) is only reported on OfficeHome with ResNet-18 (Table 3, lines 301–306). The paper's central claim — that candidate pseudo-label sets drive the improvement — would require consistent evidence across multiple benchmarks (all domain generalization datasets and corruption datasets). The sample-utilization plot (Figure 1) is also from a single domain of one dataset. This narrow evaluation makes it difficult to assess whether the candidate-set mechanism generalizes.

### Minor

4. **Theoretical analysis is weakly connected to the method.** Theorem 1 is a standard Ben-David et al. (2010) domain adaptation bound restated with a β parameter for target sample proportion. It does not involve pseudo-labels, candidate sets, thresholds, or any PASLE-specific mechanism. Theorem 2 bounds the empirical risk gap by E[||q-p||_2] but does not prove that PASLE's candidate-set assignment reduces this distance relative to one-hot pseudo-labels. The theory provides high-level motivation but does not derive or validate any algorithmic design choice in PASLE.

5. **Sensitivity analysis only on one corruption type.** Parameter sensitivity (Figure 2a) is evaluated exclusively on shot noise corruption of CIFAR-10-C. Results on other corruption types or domain generalization datasets would strengthen confidence in the reported robustness.

6. **No discussion of limitations or failure cases.** The conclusion (Section 5) summarizes results without acknowledging any limitations of the approach, such as computational overhead of maintaining a buffer, sensitivity to the linear decay schedule choice, or scenarios where the method might underperform.

### Trivial

- None.

## Nice-to-Haves

- Expand ablation of candidate pseudo-labels to all datasets (domain generalization and corruption benchmarks) to quantify the contribution of the core mechanism more thoroughly.
- Include a figure showing how candidate-set cardinality evolves over adaptation steps, to visually demonstrate progressive refinement.
- Add qualitative examples where confident pseudo-labels would be incorrect but the candidate set contains the correct label, illustrating the method's benefit.

## Removed Points

- **"Tables 1 and 2 are not viewable" and "Eq. (7) is cut off."** These are PDF parsing artifacts — the original submission contains these elements. Removed per hard rules on parser artifacts.
- **"No mention of EATA, SAR, or CoTTA in related work."** This is factually incorrect; all three are cited (lines 22–23). The weakness is that they are not included as *experimental baselines*, which is already captured in Major weakness #2 above. Removed the inaccurate phrasing.
- **"Theorem 1 assumption is unrealistic for online TTA because source data is inaccessible."** This is a modeling assumption for theoretical analysis, common in domain adaptation bounds. It does not reflect the algorithm's actual operation. Weakened and moved to Minor weakness #4 (theory is weakly connected), but the specific criticism about source accessibility is removed as it misunderstands the role of theoretical assumptions.
- **"Hyperparameter selection uses source validation which is unusual for TTA."** Using source-domain validation splits for hyperparameter selection is standard practice in the TTA literature (Gulrajani & Lopez-Paz, 2021; cited in the paper line 288). Removed.
- **Strength from Strength Finder: "Theoretical generalization bound for TTA" presented as a core strength.** The theory is indeed present, but it is weakly connected to the algorithm. Downgraded from a core strength to a minor supporting point (see Minor weakness #4).
- **Strength from Strength Finder: "Ablation and analysis confirm key design choices" presented as a core strength.** The ablation is limited to one dataset, which the Strength Finder overstates. The evidence is present but thin; captured in Major weakness #3.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a genuine tension: the paper's central idea (candidate pseudo-label sets for uncertain TTA samples) is creative and well-motivated, yet the evidence for it rests on surprisingly narrow footing given the novelty claim. The missing baselines further weaken what would otherwise be a solid empirical story. This is a paper with a good high-level idea that would benefit from a substantially expanded evaluation.

## Suggestions

1. **Fix the definition of D_M^r in Eq. (6).** Add the condition d'^p - d'^q ≤ τ(r) to ensure the uncertain and confident subsets are disjoint, or define D_M^r as the complement of D_H^r (excluding samples that fall into neither category).
2. **Add EATA, SAR, and CoTTA as baselines** to all reported benchmarks, or qualify the SOTA claim to reflect the compared methods.
3. **Run PASLE-NC (no candidate sets) on all datasets** to demonstrate that the benefit of candidate pseudo-labels generalizes beyond OfficeHome.
4. **Discuss limitations** — e.g., computational overhead of the buffer, sensitivity to the τ_des schedule, and scenarios where candidate sets might not help.

## Score and Decision

**Score:** 5.0  
**Decision:** Reject

The paper identifies a genuine limitation of existing TTA methods and proposes a novel solution. However, the evaluation has significant gaps: key baselines (EATA, SAR, CoTTA) are missing, the ablation of the core mechanism is limited to a single dataset, and the method description contains a formal definition error in Eq. (6) that must be resolved. While the idea has merit, the paper in its current form does not provide sufficient evidence to support its claims. Substantial revision — particularly adding baselines and expanding the ablation — is needed before the contribution can be properly assessed.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>