Now I have a thorough understanding of the paper and can verify the key claims. Let me compose the consolidated review.

---

## Summary

This paper proposes a method to rank 3D image blocks by combining 2D patch rankings from axial, coronal, and sagittal views. The approach uses feature selection (FS) with Grad-CAM to generate heatmaps with fewer highlighted regions, then defines feature/heatmap matrices from which patches are ranked. A block ranking algorithm fuses the three 2D rankings (requiring all views to be positive) to produce a Block Ranking Map (BRM). A hybrid variant uses multiple feature-set sizes to improve robustness. Evaluation on ADNI (AD) and autism datasets verifies top-ranked blocks against ChatGPT and literature. The paper also releases three FS pipelines that combine Chi2, mutual information, f_regression, f_classif, and RFE in different orders.

## Strengths

- **FS-Grad-CAM produces more interpretable heatmaps than standard Grad-CAM.** By selecting only top-ranked features before computing gradients (Equations 2–4), the method generates heatmaps where highlighted patches are concentrated in brain regions (Figure 2(b)), unlike standard Grad-CAM which highlights many areas including those outside the brain (Figure 2(d)). This is a concrete advantage and is clearly demonstrated within the paper.

- **The 3D block ranking algorithm requires all three anatomical views to agree.** Algorithm 2's Step 1 selects a block only when θ_{jk}>0, θ_{ik}>0, and θ_{ij}>0 — meaning the corresponding axial, coronal, and sagittal patches are all positively ranked. This tri-view requirement reduces false positives compared to methods that treat each view independently. The hybrid version (combining multiple feature-set rankings) further reduces bias from a single FS method.

- **Top-ranked blocks map to brain areas independently associated with the target diseases.** For AD (Table 1), the top-10 blocks include the CA1 hippocampus, entorhinal cortex, and temporal lobe — all well-established AD-relevant regions supported by cited literature (Braak & Braak 1991; Gómez-Isla et al. 1996; Jack Jr. et al. 1997). For autism (Table 2), blocks include the right inferior frontal gyrus and fusiform gyrus, also supported by literature (Dapretto et al. 2006; Hadjikhani et al. 2004). This provides face validity that the ranking identifies clinically meaningful regions.

- **Evaluation on two independent 3D datasets (AD and autism)** demonstrates that the framework is not dataset-specific and generalizes across disease domains and classification tasks (3-class and binary).

## Weaknesses

### Major

1. **Data leakage from slice-level train/test split.** The paper extracts 20 consecutive 2D slices from each 3D brain (yielding 19,640 slices from 982 volumes) and splits them into 13,748 training / 2,636 testing at the *slice level* — not the subject level (Section 4, paragraph 1). This means slices from the same 3D brain (same patient) can appear in both training and test sets. For the 2D CNNs that generate the feature maps on which the entire ranking pipeline depends, this constitutes data leakage. The reported testing accuracies (0.9309–0.9897) are likely inflated and unreliable. The paper does not discuss this issue.

2. **Key algorithms are underspecified, preventing reproduction.** Algorithm 1 (the 2D patch ranking algorithm) lists its five input matrices but provides no body or procedure (Section 2.5, lines 127–131). Algorithm 3 (the hybrid 3D block ranking algorithm) is referenced as "shown in Algorithm 3" (Section 3, line 143) but does not appear in the paper. Algorithm 2's Step 1 defines a block ranking score φ_{ijk} = f(θ_{jk}, θ_{ik}, θ_{ij}) where f is a "monotonically non-decreasing function," but f is never defined (Section 3, line 147). Without these algorithmic specifications, the method cannot be independently implemented or evaluated.

3. **No comparative evaluation against any existing explainability method.** The paper contains no comparison to 3D Grad-CAM (which the authors cite), 2D Grad-CAM, occlusion maps, or any other saliency/explainability baseline. The only contrast shown is between using top-250 features vs. all 16,384 features within the authors' own framework (Figure 2). This is an ablation of the FS choice, not a comparison to an alternative method. Without baselines, the reader has no basis to judge whether the proposed method advances the state of the art or is simply a more complicated way to produce similar results.

4. **Critical mapping from block indices to brain coordinates is acknowledged as imprecise.** The paper states in Section 7 (future work) that "it is critical to find a precise function mapping indices (i,j,k) of a 3D image block to corresponding world coordinates (I,J,K) of a 3D image block of the standard 3D brain of the 'ebrains' software tool." However, the evaluation in Tables 1 and 2 *depends* on exactly this mapping to associate top-ranked blocks with brain areas. The paper does not describe how the mapping was performed for the current results. This means the claimed associations between blocks and brain regions rest on an unspecified and acknowledged-as-imprecise mapping.

### Minor

1. **Validation relies on ChatGPT for ground truth.** While the paper also cites scientific literature, ChatGPT is used as a primary verification tool (e.g., "ChatGPT states that CA1 (Hippocampus) left is indeed associated with AD diagnosis"). ChatGPT is a language model that can produce plausible but incorrect statements; it is not a reliable scientific ground truth. The literature citations do provide partial support, but no systematic statistical test (permutation test, comparison to random block rankings, or quantitative overlap with known atrophy maps) is performed.

2. **Hyperparameter choices are not justified.** The paper uses 20 slices (indices 22–41) from the middle of each 3D brain, and top-250 / top-100 feature sets. No sensitivity analysis or ablation is provided for these choices, so it is unclear how robust the results are to these parameters.

3. **Numerical inconsistency in the AD dataset split.** The paper reports 13,748 training images (70% of 19,640) and 2,636 testing images (claiming 30% of 19,640). However, 30% of 19,640 is 5,892, not 2,636; 13,748 + 2,636 = 16,384, not 19,640. This error needs correction.

### Trivial

- None beyond the numerical inconsistency noted above.

## Nice-to-Haves

- A user study (even a small pilot with 2–3 physicians) comparing diagnostic understanding with vs. without the BRM would substantially strengthen the claimed clinical utility.
- Comparing the proposed method's top-ranked blocks to those produced by 3D Grad-CAM or occlusion-based methods would help establish whether the tri-view ranking is actually beneficial.
- Releasing code with the algorithmic specifications would address the reproducibility concerns.

## Removed Points

*These points are flagged for removal; treat them with caution.*

- The harsh critic's claim that ebrains is a "specific (proprietary?) software tool" is removed — the paper cites ebrains; questioning its availability is not permitted per the review guidelines.
- The harsh critic's concern that "the order in each pipeline seems arbitrary" and "no justification is given" for the three FS combinations is removed as a scope-creep/formatting nitpick — the paper does describe the three pipelines and their orders, and FS ordering is standard practice; the method's contribution does not depend on justifying one ordering over another.
- The strength finder's claim that "external validation with ChatGPT and published literature confirms clinical relevance" is retained but tempered by the minor weakness about ChatGPT's reliability.
- The harsh critic's note about "code and trained models not mentioned" is removed per guidelines — reproducibility nitpicks about large artifacts impractical to include are excluded.
- The strength finder's strength about evaluation on two datasets is retained but noted as supporting rather than core, since testing on two datasets is standard practice.

## Novel Insights

None beyond the paper's own contributions. The reviews surface no observation about the paper's approach or results that the authors themselves did not identify or imply.

## Suggestions

1. **Fix the data split.** Perform a subject-level split (e.g., 70/30 at the 3D-volume level), then extract slices from each split subject. Re-run the entire pipeline (CNN training, FS, heatmap generation, patch/block ranking) and re-report all results. This is the single most important correction.

2. **Provide complete pseudocode for Algorithms 1 and 3**, and define the function f in Algorithm 2 explicitly (even a simple additive or multiplicative combination of the three view scores).

3. **Add at least one baseline comparison.** For example, train a 3D CNN on the same data, generate 3D Grad-CAM saliency maps, and compare the top-ranked blocks (or overlap with known diseased regions) to those from the proposed method.

4. **Describe how the (i,j,k)-to-coordinate mapping was performed** for the current results, even if imprecise. Currently this is a black box.

5. **Replace or supplement ChatGPT verification** with a quantitative metric: e.g., compute spatial overlap with known atrophy templates from the literature, or perform a permutation test comparing the ranking against random block selection.

6. **Correct the numerical error** (2,636 vs. 5,892 for the test set size) and clarify whether the counts are per-view or total.

## Score and Decision

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>