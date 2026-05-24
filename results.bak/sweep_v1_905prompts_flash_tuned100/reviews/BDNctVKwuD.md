Now I have sufficient calibration data. Let me write the consolidated review.

Here is my full assessment:

**Key verification of the harsh critic's central claim about IoU inconsistency:**

Looking at Table 2 carefully: The **GradCAM IoU column is reported for ALL models** — including CFCE (18.88) and CFCE+KL (51.52). The **ContrastiveCAM IoU column** is a supplementary metric that is also available for the CE w/ Arch baseline (30.27). So the critic's claim that "baselines use GradCAM while CFCE-trained models use ContrastiveCAM" is factually inaccurate for the GradCAM IoU column. The paper does provide a consistent comparison (GradCAM IoU for all models). The ContrastiveCAM IoU column is an additional metric. This significantly deflates the critic's central "fatal" criticism.

However, the paper's own narrative does emphasize the ContrastiveCAM IoU numbers (89.22%, 93.39%) as headline results, and these are more dramatic than the GradCAM IoU numbers. This is a valid presentational concern but not a fatal flaw.

Let me compile the final review.

---

Now let me compile my final calibrated score decision.

**Round 1 bracket**: Between ~4 and ~7 (clearly stronger than the 2.5-3.4 anchors, clearly weaker than 8+ anchors).

**Round 2 anchors within bracket**: 
- "How to Probe" (6.25, Accept) - The paper under review has stronger theory but messier evaluation. Slightly weaker → ~5.5.
- "INTR" (6.00, Accept) - Similar level of evaluation concern. The paper under review has more quantitative evaluation → ~5.5-6.0.
- "Feature map smoothing" (5.25, Reject) - The paper under review is clearly stronger → at least 5.5.
- "Causal Alignment" (6.00, Accept) - Cleaner evaluation → the paper under review is slightly weaker → ~5.5.
- "SPADE" (5.00, Reject) - The paper under review is stronger → at least 5.5.

**Final score**: 5.5. The paper has genuine theoretical contributions and moderately strong empirical evidence. The main weaknesses preventing a 6+ are: (1) the narrative emphasis on the ContrastiveCAM IoU numbers which lack comparison to vanilla baselines, (2) unclear bias-zeroing implementation, (3) no direct ContrastiveCAM vs HiResCAM faithfulness comparison, (4) no hyperparameter sensitivity analysis. These are bounded weaknesses—they don't invalidate the core claims but prevent the paper from being a clear, strong accept.## Summary

This paper makes two contributions: (1) **ContrastiveCAMs**, a new explanation method derived from HiResCAM that is invariant to an additive constant shift \(M\) (Theorem 3.2 → 3.5), and (2) **Core-Focused Cross-Entropy (CFCE)**, a training loss that penalizes non-core region contributions during classification by leveraging ContrastiveCAMs and user-supplied core masks. The paper provides theoretical consistency proofs (Theorem 4.6) and evaluates on Hard-ImageNet, Oxford-IIIT Pets, and PASCAL VOC, reporting improvements in feature alignment metrics and downstream segmentation.

## Strengths

1. **Novel theoretical identification of HiResCAM's non-uniqueness (Theorem 3.2).** The paper proves that HiResCAMs can be shifted by an arbitrary matrix \(M\) without changing softmax probabilities. This is a genuine theoretical insight about a widely used explanation method, supported by a clean proof and a concrete illustration (Figure 1). The derivation is technically sound.

2. **ContrastiveCAMs provide a principled fix with invariance to the spurious shift (Theorem 3.5).** The contrastive formulation (Definitions 3.3, 3.4) is a natural and theoretically grounded response to the identified redundancy. Proposition 4.1 further shows that ContrastiveCAMs directly relate to the actual probability predictions (under bias-free assumption), giving them a clear semantic interpretation.

3. **The CFCE loss is well-motivated and theoretically grounded (Theorem 4.6).** Proposition 4.2 and Remark 4.3 convincingly show that standard cross-entropy does not inherently favor core over non-core regions. The proposed CFCE loss directly addresses this and is proved to be classification-calibrated with respect to the core-constrained risk—a non-trivial theoretical guarantee.

4. **Empirical evidence across multiple datasets and metrics, with standard deviations reported.** The paper evaluates on Hard-ImageNet (Table 2), Oxford-IIIT Pets (Table 3), and PASCAL VOC (Table 4), with results reported across multiple ablation conditions. The core-region ablation metrics (Gray Mask, Gray BBOX, Tile) and RFS are consistent across all methods and show meaningful differences: CFCE models suffer much larger drops when core is removed (e.g., Gray Mask: 41.78% vs 76.53%), directly indicating stronger reliance on core regions.

5. **Robustness to approximate masks is demonstrated.** Table 3 shows CFCE with SAM-generated masks (83.54% IoU) and bounding boxes (79.13% IoU) performs close to the ground-truth mask (92.72% IoU), demonstrating practical utility beyond the oracle-mask setting.

## Weaknesses

### Fatal

None.

### Major

1. **The narrative over-indexes on ContrastiveCAM IoU while de-emphasizing the GradCAM IoU comparison.** The paper's headline "5× improvement" narrative (18% → 89% IoU) draws from the ContrastiveCAM IoU column, but this metric is only reported for Arch-modified models. The GradCAM IoU column *is* consistent across all models—it shows a modest improvement for CFCE (18.88 vs CE w/ Arch's 16.25) and a genuine gain for CFCE+KL (51.52 vs 16.25). However, the paper's framing in the abstract and the strength summaries leans heavily on the more dramatic ContrastiveCAM numbers without sufficiently foregrounding the consistent-but-more-modest GradCAM IoU comparison. This is not an invalidation of the results, but it is a presentational weakness that could mislead readers about the magnitude of improvement under a consistent evaluation protocol. The paper should restructure the narrative to lead with the consistent metrics (GradCAM IoU, ablation drops, RFS) and present ContrastiveCAM IoU transparently as a supplementary metric.

2. **No direct faithfulness comparison between ContrastiveCAM and HiResCAM.** The paper claims ContrastiveCAM provides "more faithful attention maps" (abstract) but never empirically tests this claim. A direct comparison (e.g., via insertion/deletion scores, AOPC, or pixel perturbation metrics) between ContrastiveCAM and HiResCAM on held-out models is absent. The theoretical invariance to \(M\) is principled, but whether this translates to empirically superior explanations for real, fixed networks is unvalidated. This weakens the paper's framing of ContrastiveCAM as an independently valuable explanation method (as opposed to a convenient differentiable component for the CFCE loss).

3. **Unclear whether the bias-free assumption is enforced in practice.** Section 4 states "By zero-ing the final bias vector (i.e., \(\mathbf{b} := \mathbf{0}_C\) for \(h\) only)" for the theoretical derivation that motivates CFCE. The paper does not clearly state whether all trained models (including baselines) use bias-free classifiers or only the CFCE models. If the bias is zeroed only for CFCE models, the comparison is not fully controlled; if it is zeroed for all models, this is a non-trivial architectural constraint that should be discussed as a limitation, especially since classifier bias is a standard component. This ambiguity undermines reproducibility.

4. **Limited hyperparameter analysis.** The KL regularization (Eq. 18) introduces three hyperparameters \(\lambda_1, \lambda_2, \lambda_3\) with no sensitivity analysis. Given that the KL term drives the largest GradCAM IoU improvement (51.52 vs 18.88), understanding how performance varies with \(\lambda_1\) is critical for practical use.

### Minor

1. **Overstated critique of HiResCAM (mirroring the critic but with proper weight).** Theorem 3.2 is technically correct: the *mapping from CAMs to probabilities* is non-unique. However, for a *fixed trained network* and *fixed input*, Eq. (2) computes a unique HiResCAM deterministically. The paper's framing that HiResCAMs "fail to guarantee a faithful interpretation" (Section 3) and "can, in principle, completely corrupt HiResCAM explanations" overstates a theoretical redundancy that may never manifest in practice. The paper would benefit from acknowledging that ContrastiveCAM explains a different target (probability differences rather than logits) rather than "fixing" a flawed method.

2. **The "CE w/ Arch" baseline is not adequately described in the main paper.** The paper states that architectural modifications are "detailed in Appendix C" (stripped from this version). Without even a brief summary of what changes are made (e.g., bias zeroing? GAP adjustment? feature map dimensionality changes?), the reader cannot assess the fairness of the comparison between CE w/ Arch and CFCE. This is critical because CE w/ Arch is the primary fair baseline for ContrastiveCAM IoU comparisons.

3. **No discussion of computational overhead.** Computing ContrastiveCAMs during training requires multiple forward-backward passes per image (contrastive pairs for each non-target class). The paper should report training time relative to standard CE.

### Trivial

None.

## Nice-to-Haves

- An ablation study isolating the contribution of the KL regularization term vs. the base CFCE loss.
- A direct faithfulness benchmark (insertion/deletion scores) comparing ContrastiveCAM vs. HiResCAM.
- A controlled degradation experiment (dilating/eroding core masks) to assess robustness to mask quality more systematically.
- Reporting training time overhead.

## Removed Points

- **"Unfair IoU comparison is fatal" (harsh critic, Critical Issue #1):** The critic claimed IoU is computed with different methods for different models. This is **factually incorrect for the GradCAM IoU column** in Table 2, which reports GradCAM IoU for *all* models including CFCE (18.88%) and CFCE+KL (51.52%). The ContrastiveCAM IoU column is supplementary and IS available for the CE w/Arch baseline (30.27%). The paper also acknowledges the limitation in the caption. Demoted from fatal to a presentational concern listed as Major weakness #1.
- **"HiResCAM limitation is entirely overstated" (harsh critic, Critical Issue #2):** Partially valid but overstated by the critic. The theorem is correct and relevant; the paper's framing is somewhat aggressive but not dishonest. Moved to Minor weakness #1.
- **"Missing appendix details" (harsh critic, Critical Issue #3):** Per policy, the parser strips appendix content from all papers; these details exist in the original submission. However, some description of the architectural modifications should be in the main paper body. Moved to Minor weakness #2.
- **Strength Finder's claim about "Table 2: CFCE achieves ContrastiveCAM IoU of 89.22% compared to 30.27% for the cross-entropy baseline":** This is factually correct — CE w/Arch (the fair baseline) achieves 30.27% ContrastiveCAM IoU. Retained as a valid strength but with the caveat noted in Major weakness #1.

## Novel Insights

None beyond the paper's own contributions. The key insight—that HiResCAMs are non-unique under additive shifts because softmax is shift-invariant—is the paper's own novel theoretical contribution. The reviewers did not surface additional novel observations beyond what the paper itself claims.

## Suggestions

1. **Restructure the results narrative** to lead with metrics that are consistently computed across all models: GradCAM IoU, core-region ablation accuracy drops (Gray Mask, Gray BBOX, Tile), and RFS. Present ContrastiveCAM IoU as a supplementary metric with a clear statement that it is only available for Arch-modified models.
2. **Clearly state whether bias is zeroed in practice** for all models or only CFCE models. If it is zeroed, discuss this as a design choice and limitation.
3. **Add a direct faithfulness experiment** (e.g., deletion/insertion curves) comparing ContrastiveCAM and HiResCAM on a standard pre-trained model. This would substantially strengthen the claim that ContrastiveCAMs are "more faithful."
4. **Include a hyperparameter sensitivity study** for \(\lambda_1\) (or a note on how they were selected) to make the KL regularization practically usable.
5. **Provide a brief summary of the architectural modifications** in the main paper body, even if full details remain in the appendix.

## Score and Decision

**Calibration Summary:**

| Anchor ID | Avg Human Score | Round | Comparison to This Paper |
|-----------|---------------|-------|------------------------|
| BwQUo5RVun | 3.00 | 1 (bracket, < 3.5) | Much weaker — poorly motivated, unclear contributions |
| FTSUDBM6lu | 2.50 | 1 | Much weaker — unclear methodology |
| ilGdLPy3mA | 3.40 | 1 | Much weaker — limited scope |
| wZiH43e5Ah | 3.00 | 1 | Much weaker — limited empirical validation |
| 57NfyYxh5f | 6.25 | 1 (bracket, 3.5–7.5) | Slightly stronger — cleaner evaluation with consistent metrics, similar ResNet50-only limitation |
| GjfIZan5jN | 7.33 | 1 | Stronger — cleaner framing, broader experiments |
| bkdWThqE6q | 6.00 | 1 | Similar — both have evaluation concerns but solid ideas. Paper under review has more quantitative experiments |
| T7q5LBGISH | 5.25 | 1 | Weaker — less novel, more serious evaluation concerns |
| ozZG5FXuTV | 6.00 | 2 (narrow) | Slightly stronger — cleaner causal alignment evaluation |
| ffcHGwb4KF | 5.00 | 2 (narrow) | Weaker — computational cost concerns, less novel |
| lHbLpwbEyt | 6.00 | 2 | Similar — both use interpretability-guided training |

**Round 1 bracket:** 4.0 – 7.0 (clearly stronger than the 2.5–3.4 anchors, clearly weaker than the 8+ anchors).

**Round 2 narrowing:** Compared to anchors at 6.00–6.25, the paper under review has stronger theoretical grounding but weaker evaluation presentation. Compared to anchors at 5.00–5.25, it is clearly stronger (more theory, broader experiments, better motivation). The paper sits between these two bands.

**Final score rationale:** The paper has genuine theoretical contributions and substantial empirical evidence. The main weaknesses are bounded rather than fatal: the GradCAM IoU column *is* consistent across all methods, the core-region ablation metrics are clear, and the CFCE loss is well-motivated. However, the narrative emphasis on the less-comparable ContrastiveCAM IoU numbers, the lack of a direct ContrastiveCAM vs HiResCAM faithfulness comparison, and gaps in reproducibility documentation (bias status, architectural summary, hyperparameter analysis) prevent the paper from being a clear 6.0+. A score of 5.5 reflects a borderline-acceptable paper with real contributions that would benefit from targeted revisions to strengthen the evaluation presentation.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>