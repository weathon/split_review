Now I have a thorough understanding of the paper and all the reviewer claims. Let me produce the final consolidated review.

---

## Summary

This paper proposes PASLE (Progressive Adaptation with Selective Label Enhancement), a test-time adaptation framework that partitions test samples into confident and uncertain subsets, assigning one-hot pseudo-labels to confident samples and candidate pseudo-label sets to uncertain ones. A dynamic threshold is progressively reduced as adaptation improves, refining the candidate sets over time. Experiments on six benchmark datasets (PACS, VLCS, OfficeHome, DomainNet, CIFAR-10/100-C) show consistent improvements over several existing TTA methods.

## Strengths

- **Novel methodological contribution**: Unlike prior TTA methods that assign definite pseudo-labels to all test samples, PASLE explicitly models uncertainty at the label level via candidate pseudo-label sets. The ablation study (Table 3) confirms that removing candidate labels (PASLE-NC) degrades performance across all OfficeHome target domains, directly supporting the value of this design choice.

- **Consistent empirical gains across diverse benchmarks**: PASLE achieves the highest accuracy on all six benchmark datasets under both ResNet-18 and ResNet-50 backbones, with average improvements of 5.63% (ResNet-18) and 4.19% (ResNet-50) over the next-best method on domain generalization tasks. The strong performance on DomainNet (345 classes, 6 domains) demonstrates scalability.

- **Progressive threshold reduction is validated**: Figure 1 shows that PASLE uses progressively more pseudo-labeled samples over time compared to the variant without candidate labels, providing direct evidence that the dynamic threshold successfully refines uncertain pseudo-labels as adaptation progresses.

- **Robustness to hyperparameters and batch sizes**: Figure 2 shows stable performance across a broad range of τ_start/τ_end values and consistent outperformance of baselines under varying batch sizes, which is practically important for online deployment.

## Weaknesses

### Fatal
None.

### Major
- **Missing standard recent TTA baselines**: The experimental comparison omits several widely-cited online TTA methods from 2022–2023: CoTTA (Wang et al., 2022), EATA (Niu et al., 2022), and SAR (Niu et al., 2023). These are standard reference points in the current TTA literature. Without them, the claim of "state-of-the-art" performance is not fully supported. The paper mentions Niu et al. (2023) in related work but does not include it as a baseline.

- **No variance estimates for main results**: Tables 1 and 2 report only point estimates without standard deviations. Only the ablation study (Table 3) reports mean ± std. Given that performance differences on corruption benchmarks are often modest (~1–2 percentage points), it is impossible to assess statistical significance. This is standard practice in the TTA literature and should be included.

### Minor
- **Overlap between confident and uncertain subset definitions**: The paper's text says PASLE "partitions" data into confident and uncertain subsets (implying disjoint sets). However, Eq. (4) and Eq. (6) are defined independently on the same pool (D_T^r ∪ B^{r-1}) without excluding D_H^r samples from D_M^r. Since d^p - d^q > τ(r) implies ∃ j, d^p - d^j > τ(r) (for j = q), we have D_H^r ⊆ D_M^r. This means confident samples would be double-counted in the loss (Eq. 2). The paper should clarify that D_M^r is defined on the complement of D_H^r, or adjust the formulation. (Note: this is a clarity/presentation issue, NOT the "fatal structural flaw" claimed by one reviewer — see Removed Points.)

- **Ablation study is limited**: Only one ablation is performed (removing candidate labels entirely). Missing ablations include: (i) replacing the candidate loss with standard cross-entropy on the argmax for uncertain samples, (ii) no threshold decay (fixed τ), and (iii) no buffer mechanism. Additional ablations would more precisely attribute the gains to specific components.

- **Parameter sensitivity analysis is narrow**: Figure 2 tests only one corruption type (shot noise) from CIFAR-10-C. Results may not generalize to other corruption types or datasets.

- **Theoretical analysis is generic**: Theorem 1 is a standard domain adaptation bound (Ben-David et al., 2010; Zhang et al., 2019) with no modification specific to label enhancement or candidate sets. Theorem 2 provides a generic bound connecting label distribution quality to risk but does not directly justify the threshold schedule, subset selection strategy, or loss forms. The theory is not tightly connected to the method's specific design choices.

- **Figure 1 y-axis label is ambiguous**: "Number of samples used for training" could mean cumulative gradient updates, unique samples, or cumulative selections. The figure legend is missing.

- **Proposition 1's assumption is strong**: The assumption that |f_j(·;Θ^r) − f_j(·;Θ^∗)| ≤ ½τ(r) for all classes is not justified for the fixed τ(r) schedule (Eq. 9). Early in adaptation, this bound may be violated, causing false elimination of the correct label. This failure mode is not discussed.

### Trivial
- None that survived filtering (parser artifacts and formatting nitpicks removed).

## Nice-to-Haves
- Per-corruption breakdown for CIFAR-10/100-C would reveal whether PASLE is robust to all corruption types or biased toward some.
- A limitations paragraph discussing when PASLE might fail (e.g., severe distribution shifts, poor calibration, many classes) would strengthen credibility.
- Runtime/throughput comparison would be useful since online TTA cares about computational cost.
- Justification for the buffer size K = batch_size/4 (currently described as arbitrary).

## Removed Points
These points are flagged to be removed, treat them with caution:
- **"Structural flaw: confident and uncertain conditions are identical"** (Critic #1, main claim): The critic claimed Eq. (4) and Eq. (6) have "identical conditions" both requiring d^p − d^q > τ(r). This is factually incorrect. Eq. (4) requires d^p − d^q > τ(r) (margin against the second-highest class). Eq. (6) requires ∃ j ∈ Y, d^p − d^j > τ(r) (there exists some class with a large margin). These are different conditions — the critic confused ∃ (there exists) with ∀ (for all). The conditions are not identical, and the candidate sets produced by Eq. (7) for samples in D_M^r \ D_H^r are genuinely meaningful (they eliminate low-scoring labels while keeping p and close competitors). A corrected version of this point (overlapping sets, see Minor weaknesses above) is retained.
- **"The paper should cover Y / additional domain Z"** and similar scope-creep demands.
- **Various formatting/style nitpicks** and criticism about missing appendix content (parser artifacts).
- **Strength about theoretical analysis**: Conflicts with the verified weakness that the theory is generic; per rules, weakness wins.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. Add CoTTA, EATA, and SAR as experimental baselines, or provide a clear justification for their omission.
2. Report mean ± std over at least 3 runs for all main experiments (Tables 1 and 2).
3. Clarify the relationship between D_H^r and D_M^r — explicitly state they are disjoint and define D_M^r on the complement of D_H^r to avoid double-counting.
4. Deepen the ablation: test no threshold decay (fixed τ), replace candidate loss with cross-entropy on the argmax, and test no buffer.
5. Add a limitations paragraph discussing failure modes (e.g., severe shifts, poor calibration, many classes).

## Score and Decision

This paper presents a genuinely novel and well-motivated idea for test-time adaptation. The core contribution — selective label enhancement with candidate pseudo-label sets — is clearly articulated, theoretically grounded at a high level, and empirically validated across diverse benchmarks with consistent gains. The main weaknesses (missing baselines, no variance estimates) are addressable and do not undermine the core contribution. The paper should be accepted with requests for revision.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>