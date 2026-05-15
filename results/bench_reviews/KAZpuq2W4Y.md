Now I have all the information I need. Let me compose the final review.

---

## Summary

This paper proposes HOMIL, a framework for whole-slide image (WSI) classification that extends attention-based multiple instance learning (ABMIL) by incorporating second-order moments (covariance matrices) and adaptive DBSCAN clustering. The clustering groups patches at variable granularity—coarse for normal tissue, fine for pathological regions—reducing computational cost. First- and second-order representations from cluster features are fused via learned attention weights for slide-level classification. Experiments on CAMELYON16 and TCGA-NSCLC show improvements over baselines, with substantial runtime reduction from adaptive clustering.

## Strengths

- **Efficiency gains from adaptive clustering are real and well-motivated.** DBSCAN's density-based clustering naturally produces large clusters for abundant normal tissue and small/fine clusters for rare pathological regions. The resulting compression ratios (0.16–0.18, Section 5.3) yield a 5-fold runtime of 310s on CAMELYON16, far below MambaMIL (7200s) or HMIL (10800s), while maintaining top accuracy (Table 1). The ablation confirms removing clustering both increases runtime by 71% and drops accuracy by 1.26% (Table 3).

- **The second-order moment module provides a complementary signal beyond first-order pooling.** The ablation (Table 3) shows that removing the second-order moment ("w/o SOM") drops accuracy from 96.98% to 95.98% and AUC from 99.23% to 98.51% on CAMELYON16, confirming the covariance representation contributes information not captured by attention-weighted mean pooling alone.

- **The statistical reinterpretation of ABMIL as first-order moment estimation is clean and intuitive.** Framing attention pooling as 𝔼_{a_i}[h_i] (Section 3.1) provides a principled motivation for incorporating second-order moments and naturally positions the work relative to standard MIL.

- **Evaluation follows community-standard protocols.** Both datasets use 5-fold cross-validation with patient-level partitioning, consistent feature extractors (CONCH), and a unified codebase across all methods—enabling a fair relative comparison.

## Weaknesses

### Major

- **The "attention-weighted covariance matrix" description is overstated relative to the actual computation.** Section 4.3.3 is headed "attention-weighted covariance matrix" and the text claims it is derived from such, but Equation (7) defines C = Σ g̃_k g̃_k^T with no per-cluster attention weights a_k in the sum. Only the centering term v^(1) is attention-weighted (since g̃_k = g_k − v^(1) and v^(1) = Σ a_k·g_k). The individual cluster contributions to the outer product are unweighted, meaning a cluster with near-zero attention contributes identically to the covariance as a highly attended cluster (modulo centering effects). The ablation therefore cannot isolate the effect of attention-weighting within the second-order stream, and the paper's narrative that attention modulates the second-order representation is not fully realized.

- **The abstract and introduction overclaim by describing patch-level covariance while the computation is on cluster means.** The abstract states the method computes "the covariance matrix of the patch representation vectors across the entire slide" (line 13), and Section 3.2 motivates capturing "pairwise relationships... across the slide" at the patch level. However, the actual method (Section 4.1–4.3) first mean-pools patches within DBSCAN clusters, then computes covariance on these cluster summaries g_k. While the body acknowledges this (line 29: "Both moments are computed based on cluster representations"), the abstract does not, and the disconnect between the motivation (patch-level variability) and the computation (cluster-level) is never discussed or justified. Within-cluster covariance—a component of the variability the paper claims to capture—is discarded. The paper should explicitly discuss what is lost and why the design choice is reasonable (e.g., DBSCAN's fine clusters for pathological regions may make within-cluster variance negligible where it matters).

### Minor

- **Performance gains on TCGA-NSCLC are modest and within overlapping standard errors.** HOMIL achieves 93.24% ACC vs. HMIL's 92.89% (Table 2), a 0.35% gap with overlapping standard errors (±2.47 vs. ±1.45). The improvement over ABMIL (91.05%) is more substantial but the gap to the next-best method is not clearly significant. The paper should discuss statistical significance or acknowledge the modest margin.

- **The "w/o CM" ablation variant is underspecified.** The paper states that removing the Clustering Module drops accuracy (Table 3), but does not clarify what replaces it—is the second-order moment computed on all individual patches, or on some other aggregation? Without this detail, it is difficult to interpret what the ablation actually measures.

- **The fusion weight dynamics weaken the "second-order is essential" narrative.** Figure 2b shows α^(2) (second-order weight) decreasing from ~0.5 to ~0.45 while α^(1) rises to ~0.6. The paper acknowledges this (Section 5.5) but does not investigate whether the second-order module could be removed after convergence or whether its role is primarily as a training regularizer. The ablation does show a persistent 1% accuracy drop without SOM, confirming it contributes, but the declining reliance merits deeper analysis.

- **Missing comparison with DSMIL and other covariance-aware MIL methods.** DSMIL computes instance-level similarity that implicitly captures second-order structure. Including such baselines would better contextualize the novelty of the proposed covariance mechanism.

### Trivial

- The abstract says "covariance matrix of the patch representation vectors" but should say "cluster representation vectors" to match the method.
- DBSCAN hyperparameters (d′=32, ε at 65th percentile, minPts=4) are stated without sensitivity justification in the main text (though the appendix reportedly contains analysis).
- Conv1D kernel hyperparameters (m=64, T=4) for covariance vectorization are given without ablation or rationale.

## Nice-to-Haves

- An ablation computing covariance with explicit attention weights (C = Σ a_k·g̃_k g̃_k^T) would test whether attention-weighting in the second-order stream matters.
- A variant computing second-order moments directly on patch features (bypassing clustering) would quantify what within-cluster information is lost.
- Visualization of what the covariance matrix captures vs. first-order representations (e.g., cluster-level interpretability examples) would strengthen the conceptual contribution.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Runtime comparison is unfair—HOMIL's time includes clustering while baselines exclude it."** The reviewer claimed this biases in HOMIL's favor. This is factually incorrect. The paper states (line 244) that HOMIL's time *includes* clustering while baselines include only training+inference. Including more components in HOMIL's timing *penalizes* it, making the comparison conservative. HOMIL wins despite this disadvantage. Removed.

- **"TransMIL typically exceeds 92% on TCGA-NSCLC and the numbers suggest baselines were not tuned."** All methods use the same CONCH feature extractor, data splits, and unified codebase. Absolute numbers can differ from published results (which used different encoders/settings); what matters for fair comparison is that all methods share identical conditions. The relative comparison remains valid. Removed as a criticism of the paper, though the modest gains remain a legitimate observation (noted under Minor weaknesses).

- **"Architecture diagram (Figure 1) contradicts the written method."** The extracted figure caption describes Conv1D applied to instance features before clustering, but I cannot verify what the actual figure shows versus parser-extracted caption artifacts. Without access to the actual figure, I cannot confirm this discrepancy. Removed as unverifiable from the provided materials.

- **"The second-order representation is computed on cluster means, not on original patch features, contradicting the stated motivation—and this disconnect is not discussed or acknowledged."** The paper explicitly acknowledges this at line 29: "Both moments are computed based on cluster representations rather than individual patches." The acknowledgment exists; the abstract is the only place that is misleading. This was downgraded to a Minor weakness focused on the abstract-method mismatch.

- **Generic strength: "The problem is clinically and technically relevant."** Too generic without specific evidence; dropped.
- **Generic strength: "The paper attempts an end-to-end solution that jointly considers aggregation granularity and statistical richness."** Too vague; dropped.

## Novel Insights

None beyond the paper's own contributions. The framing of ABMIL as first-order moment estimation is a clean reinterpretation but not a genuinely novel insight about the problem domain.

## Suggestions

- Revise the abstract and Section 4.3.3 heading to accurately reflect that the covariance is computed on cluster representations (not patches) and that the outer-product sum is unweighted (only centering is attention-aware).
- Specify what the "w/o CM" variant actually computes—does it fall back to patch-level second-order aggregation or something else?
- Report statistical significance tests for the key comparisons, particularly the TCGA-NSCLC results where margins are small.
- Discuss the trade-off of discarding within-cluster covariance explicitly, and justify why cluster-mean covariance is sufficient given DBSCAN's adaptive granularity.

---

Now comparing against calibration anchors:

| Anchor Paper | Avg Score | Comparison to HOMIL |
|---|---|---|
| ASMIL (CYmjrbQRyM) | 6.00 | ASMIL identifies a clear, underexplored problem (attention instability), offers well-motivated and well-ablated solutions, and is clearly presented. HOMIL has a less crisp contribution, more internal inconsistencies, and weaker ablation design. HOMIL is clearly weaker. |
| MAMMOTH (S5Io33pc78) | 6.50 | MAMMOTH has exceptionally comprehensive experiments (8 methods × 19 tasks), clear contribution, and strong ablation. HOMIL's experimental scope and clarity of contribution are substantially weaker. |
| SpecMIL (MniooZbsKw) | 3.50 | SpecMIL had a novel idea but insufficient experimental validation and weak empirical gains. HOMIL has more solid experiments, clearer gains, and better efficiency results. HOMIL is stronger. |
| PackMIL (EAmn2k52T8) | 3.50 | PackMIL had unclear methodology and modest/unclear gains. HOMIL has a clearer method and more interpretable results. HOMIL is stronger. |
| CLS-Tuned (Sz2kL7UiEG) | 2.50 | CLS-Tuned had thin novelty, poor presentation, and overclaims. HOMIL has substantially more substance. HOMIL is much stronger. |
| Efficient Patch Search (rYbYbgeaEv) | 4.00 | Similar caliber to HOMIL—interesting idea with some execution issues. Comparable quality. |
| DMIL-Net (0yqWGNFEJA) | 3.00 | Different domain (image forgery). Not directly comparable but clearly weaker than HOMIL. |
| WSI-GT (Y7kJ4oUgwL) | 1.50 | Much weaker paper overall. HOMIL is clearly stronger. |

HOMIL falls between the rejected 3.5–4.0 papers and the accepted 6.0+ papers. It has real contributions (efficiency from clustering, complementary second-order signal) but also significant issues: the "attention-weighted covariance" claim is overstated, the abstract misrepresents the computation granularity, gains on TCGA-NSCLC are modest, and ablation details are incomplete. These issues prevent acceptance in current form but are addressable. The paper is a borderline case.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>