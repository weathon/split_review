Now I have all the evidence needed. Let me write the final consolidated review.

## Summary

This paper extends the KKT-based data reconstruction method of Haim et al. (2022) to a transfer-learning setting: small MLPs are trained on embeddings extracted from large pre-trained vision transformers (ViT, DINO, DINOv2, CLIP), and the reconstruction pipeline operates on those embeddings before inverting them back to images. The paper further introduces a clustering-based approach to identify promising reconstructed candidates without needing access to the original training data. Results are shown on Food-101 and iNaturalist images at 224×224 resolution, representing a genuine resolution advance over prior work limited to CIFAR/MNIST.

## Strengths

- **High-resolution image reconstruction from transfer-learned models (a clear advance)**: Prior KKT-based reconstruction was limited to small images (32×32). The paper successfully demonstrates reconstruction at 224×224 from MLPs built on top of modern vision transformers (ViT, DINO, DINOv2, CLIP), with models achieving >95% test accuracy (Section 4). This is a non-trivial extension because the reconstruction pipeline must operate in embedding space and invert those embeddings back to images.

- **Clustering-based selection without training data access**: Section 5 introduces agglomerative clustering on reconstructed candidates to select representatives for inversion, reducing inversion cost from thousands to tens. This directly addresses a key limitation of prior work (Haim et al., Buzaglo et al.) that relied on knowing the original training images to pick good candidates. The CIFAR-10 quantitative validation (Figure 7) provides reasonable evidence that the clustering approach can recover meaningful reconstructions.

- **Evaluation across multiple backbones and datasets**: Results span four vision transformer backbones and two diverse datasets (Food-101, iNaturalist) in both binary and multiclass settings (Figures 3-5), demonstrating generality beyond a single backbone or domain.

- **Transparent discussion of limitations**: The paper candidly documents settings where the method fails (CNN backbones, linear models, no weight decay) and explicitly shows the inversion quality ceiling (Figure 6, comparing original images → inverted originals → inverted reconstructions). This honesty helps calibrate the reader's expectations.

- **Figure 5 (cossim_preds) links to theory**: Shows correlation between reconstruction cosine similarity and model output margin, aligning with the KKT-equation framing from Haim et al. and providing evidence that reconstructed candidates are recovering support-vector-like training points.

## Weaknesses

### Fatal
None.

### Major

1. **The headline results (Figures 3-4) rely on ground-truth embeddings for candidate selection, which is not a realistic attack scenario.** Section 3.3 pairs each training embedding with its nearest reconstructed candidate and shows only the top 40. The paper is transparent about this (Section 3.3: "In practice, the original training embeddings are not available"), but the primary visual evidence for the paper's central claim — that training data can be reconstructed from transfer-learned models — uses information unavailable to an attacker. The clustering method (Section 5) is meant to address this, but its high-resolution evaluation is purely qualitative (8 visual pairs, Figure 6). This means the paper's two key claims are mismatched with the evidence: the realistic-attack claim relies on the clustering method, which lacks quantitative high-resolution validation, while the ground-truth-selected results are impressive but unrealistic. **This mismatch undercuts the paper's narrative that it addresses "realistic settings."**

2. **The clustering method — the paper's most practically relevant contribution — lacks quantitative evaluation on high-resolution data.** The clustering approach is validated with SSIM-based quantitative metrics only on CIFAR-10 (32×32, Figure 7). For the claimed high-resolution setting (Food-101, 224×224), the evidence is limited to 8 shown pairs with no metrics (precision, recall, SSIM, or fraction of clusters that genuinely match training images). An attacker needs to know what fraction of cluster representatives actually correspond to training data, and this number is not reported for the high-resolution case.

3. **No comparison to or discussion of baselines from prior reconstruction work on comparable settings.** The paper does not compare against applying Haim et al. or Buzaglo et al. directly to the same data (e.g., training an MLP on raw pixels at 224×224 and running reconstruction). While this comparison is difficult (the input dimension would be ~150K), a principled baseline — even a negative result showing that pixel-space reconstruction fails — would substantiate the claimed advantage of the embedding-space approach. Without it, the "significant advancement" over prior work is asserted rather than demonstrated.

### Minor

1. **"Non-visual data" contribution is overstated.** The paper claims "reconstruction of non-visual data (feature vectors of intermediate layers)" (Contributions list) and "showcasing its applicability beyond visual data" (Abstract). In practice, the paper reconstructs image embeddings derived from images and inverts them back to images. True non-visual data (text embeddings, tabular data) is never reconstructed. The method would work on any embedding vector, but this is never demonstrated — the paper only shows image-to-image reconstruction through an embedding bottleneck.

2. **All experiments use n=100 training images.** The abstract criticizes prior work for "limited training set sizes," but the paper itself uses the same small-scale regime. While n=100 is realistic for transfer learning, the paper does not show results at larger n (e.g., n=500, 1000) to substantiate the claim of overcoming training-set-size limitations. The CIFAR-10 clustering experiment uses n=500 but at 32×32 resolution.

3. **The KKT theory foundations do not strictly apply to the models used.** The reconstruction method assumes homogeneous networks trained with gradient flow, but the paper trains MLPs with weight decay using SGD. The paper inherits this gap from prior work (Buzaglo et al. 2023 note it works empirically), but does not discuss which training configurations cause the method to succeed or fail, beyond the empirical observations about weight decay. This limits the generalizability claims.

4. **Numerical metrics (SSIM, LPIPS, mean cosine similarity) are absent for the core reconstruction results.** The paper relies entirely on visual inspection of reconstructed images and per-sample cosine similarity plots. While visual inspection is standard in this sub-area, aggregate metrics would strengthen the evaluation and make comparisons with future work possible.

### Trivial

None.

## Nice-to-Haves

- **Disentangle reconstruction error from inversion error**: The paper already provides the ingredients (Figure 6 compares inverted original embeddings vs. inverted reconstructed embeddings), but a direct quantitative breakdown — "reconstruction error accounts for X% of the total image difference" — would strengthen the analysis. Currently, the reader cannot tell whether poor reconstructions are due to the KKT method failing or the inversion method struggling.

- **False-positive analysis for clustering**: Showing examples where clustering-based representatives do NOT match any training image would help calibrate the practical utility of the method.

- **Sensitivity to reconstruction hyperparameters (learning rate, σ, number of candidates m)**: The method runs 50-100 reconstruction sweeps with m=500, but the sensitivity of results to these choices is not analyzed.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism that the evaluation is "cherry-picking with access to ground truth" (in the harsh framing)**: The paper explicitly acknowledges this limitation in Section 3.3 and introduces the clustering method to address it. The ground-truth-based selection is a standard demonstration approach (also used by Haim et al. and Buzaglo et al.) and is not presented deceptively. However, the underlying concern — that headline results overstate what an attacker can achieve — is retained in Major Weakness #1 above.

- **Criticism about missing appendix / proofs**: The parser strips appendix content; these exist in the original submission.

- **Criticism about missing related work**: Removed per instructions — I cannot independently confirm existence of missing references.

- **Strength Finder's generic strength about "addressing an important problem"**: Dropped as too generic and lacking specific evidence.

## Novel Insights

None beyond the paper's own contributions. The key insight — that reconstruction can be moved from pixel space to embedding space, enabling higher-resolution image recovery and opening clustering-based selection — is the paper's own contribution, not a novel synthesis from the reviews.

## Suggestions

1. **Add a quantitative evaluation of the clustering method on high-resolution data**: For Food-101, report the fraction of the top-10 or top-45 cluster representatives whose nearest training image has cosine similarity > some threshold (or SSIM > 0.3 after inversion). This is the single most important missing experiment.

2. **Clearly separate the two evaluation regimes in the paper**: Label "Demonstration (uses ground truth for selection)" vs. "Realistic attack (uses clustering)" more prominently so readers can distinguish what the method achieves in each setting.

3. **Add a baseline**: Run Haim et al.'s method directly on low-resolution versions of the same datasets (e.g., 32×32 downsampled Food-101) to show that the embedding approach is genuinely superior, or at least discuss why pixel-space reconstruction is infeasible at 224×224.

4. **Tone down or clarify the "non-visual data" claim**: The paper reconstructs image embeddings that are inverted back to images. Describing this as "non-visual data reconstruction" is misleading.

5. **Explore larger training set sizes (n=500, 1000)**: Even a single experiment would substantiate the claim of overcoming "limited training set sizes."

## Score and Decision

**Calibration anchors (from retrieval):**

| Path | Avg Score | Comparison |
|:---|:---:|:---|
| VoLDkQ6yR3 (Understanding Reconstruction Attacks with NTK) | 6.67 | Stronger theoretical grounding and more thorough experiments; accepted. This paper is weaker on both dimensions. |
| ZJftXKy12x (SimuDy — Simulating Training Dynamics) | 6.25 | Comparable scope of contribution but with more thorough evaluation on practical models; accepted. This paper has a novel idea but weaker empirical validation. |
| GlPVnuL66V (Provable Privacy Attacks on Shallow NNs) | 6.00 | Rejected despite decent score due to limited scope and presentation issues. This paper has broader practical relevance but suffers evaluation gaps. |
| GbEmJmnQCz (Is Memorization Necessary for Generalization?) | 4.40 | Thorough analytical paper with clear experimental design. This paper is comparable in quality of contributions but less rigorous in evaluation. |
| LJULZNlW5d (Vanishing Privacy: Fast Gradient Leakage) | 3.00 | Weaker novelty and evaluation. This paper's contributions are more solid. |
| 0rS9o1uKqu (Training-Like Data Reconstruction) | 2.50 | No quantitative metrics, no baselines. This paper is substantially stronger. |

**Reasoning:** The paper has a genuine contribution — extending KKT-based reconstruction to embedding space with a clustering-based selection method — and demonstrates impressive high-resolution visual results. However, the evaluation has a significant mismatch between claims and evidence: the headline results use ground-truth supervision unavailable to an attacker, while the realistic clustering method lacks quantitative high-resolution validation. The lack of baselines and aggregate metrics further weakens the empirical case. The contributions are real but the evidence does not fully support them in the current form.

Relative to the anchors, this paper is stronger than the score-2–4 papers (clear contribution, reasonable method) but weaker than the accepted papers at score-6+ (insufficient evaluation rigor for the claims made). It is most comparable to GlPVnuL66V (avg 6.00, Reject): a paper with genuine insights whose evaluation gaps prevented acceptance.

**Score:** 5.0

**Decision:** Reject

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>