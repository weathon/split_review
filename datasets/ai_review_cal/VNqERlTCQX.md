- Decision: Reject
- Avg Score: 3.00
- Scores: 1, 3, 5, 3
Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

This paper proposes Molecular Similarity-Aware Consistency Regularization (MSCR), a plug-and-play technique for molecular generative models with latent spaces. MSCR uses Matched Molecule Pairs (MMPs) to generate chemically valid similar molecule pairs, then applies two regularization terms — a KL-divergence distribution term and a ratio-based metric consistency term — to align similarity in chemical space with similarity in the latent space. Experiments on TransVAE and GEOLDM across ZINC, ChEMBL, and QM9 show improvements on similarity consistency, reconstruction, validity, uniqueness, and lead optimization tasks (GSK3β, JNK3).

## Strengths

- **Chemically principled data augmentation via MMPs**: Section 3.1 and Figure 2(a) motivate the use of MMPs by contrasting them with generic augmentations (random deletion, node dropping, flipping) that can produce invalid molecules. MMPs provide chemically valid, subtle structural variations grounded in medicinal chemistry, giving the method a domain-specific advantage. The paper explicitly argues that MMPs capture fine- and coarse-grained similarity structure.

- **Two-component regularization design with ablation support**: MSCR decomposes alignment into a coarse-grained distribution term (KL divergence between latent posteriors of MMP pairs, Eq. 3) and a fine-grained metric term (ratio of latent to chemical similarity, Eq. 4). The ablation (Table 5) confirms both components contribute, with the distribution term playing a stronger role — supporting the stated coarse-to-fine design rationale.

- **Empirical improvement on consistency and generation metrics**: Table 1 shows TransVAE+MSCR achieves SC=0.895 vs. TransVAE=0.719 on ZINC, and GEOLDM+MSCR achieves SC=0.758 vs. GEOLDM=0.701 on QM9. The method also shows consistent (though variable-magnitude) improvements in reconstruction accuracy, validity, and uniqueness across datasets, suggesting the regularization does not harm — and sometimes helps — core generative quality.

- **Generality across model families and molecular representations**: MSCR is applied to both TransVAE (sequence-based 2D) and GEOLDM (point-cloud 3D), and tested on three datasets (ZINC, ChEMBL, QM9), demonstrating it is not tied to a single architecture or molecular representation.

## Weaknesses

### Fatal
None.

### Major

- **The Consistency of Similarity (SC) metric is poorly designed and its interpretation is unclear**: SC is defined as TanimotoSimilarity / CosineSimilarity, with values closer to 1 claimed to indicate better alignment. This ratio conflates two very different situations: (a) both spaces agree a pair is *similar* (both similarities high → ratio ≈1) and (b) both spaces agree a pair is *dissimilar* (both similarities low → ratio ≈1). The paper randomly samples "500 pairs of molecules" (line 146) without specifying whether these are MMP pairs or random molecules — if mostly dissimilar, the ratio is mechanically near 1 regardless of alignment quality. The reported SC gains (~0.72→0.90 for TransVAE on ZINC) are not straightforwardly interpretable as evidence that chemically *similar* molecules are mapped closely in latent space. Since this metric is the paper's primary quantitative evidence for its central claim of "clearly reflect[ing] similarity relationships in latent space" (abstract), this is a significant weakness.

- **The claimed advantage of MMPs over alternative augmentations is asserted but never tested**: The paper states MMPs "introduce more robust similarity information than other conventional augmentation methods" (abstract) and argues that generic augmentations "could easily result in invalid or meaningless molecular structures" (Section 3.1). However, no experiment compares MSCR with MMPs to MSCR with any other augmentation strategy (e.g., random SMILES perturbation, functional group replacement, or graph noise). The ablation (Table 5) only compares the two loss terms within the MMP framework. The unique contribution of MMPs to the method's success is therefore unsubstantiated.

- **Optimization results are presented without statistical significance and show inconsistent gains**: Tables 2–4 report improvements of typically 1–3 percentage points on GSK3β and JNK3 under BO, GD, and RS, but no variance, confidence intervals, or multiple-trial statistics are provided. On JNK3/ChEMBL, MSCR *underperforms* the baseline on novelty under GD and RS (acknowledged in line 166). The offered explanation ("lack of good initial molecules for JNK3") is post-hoc and unsupported — the baseline faces the same data limitation. These results are too weak and noisy to convincingly demonstrate that MSCR materially improves downstream optimization.

- **No ablation of the loss components on the optimization tasks**: Table 5 ablates the distribution and metric terms only on consistency, reconstruction, validity, and uniqueness metrics. Whether the distribution term alone, the metric term alone, or both produce the reported optimization gains is unknown. Since the optimization results are the main downstream evidence for MSCR's value, this gap weakens the chain from regularization to practical benefit.

### Minor

- **Two-stage training confound is not controlled**: The training procedure (Algorithm 1) first trains with the original loss alone, then fixes the decoder and adds the consistency losses. The ablation never compares "no regularization with two-stage training + MMP data" against the full MSCR. Part of the reported gains could stem from the extended training schedule or from training on MMP-augmented data alone, without the consistency losses themselves.

- **Reproducibility gaps**: (a) MMP generation is described only as "based on established MMP rules" (line 48) — no algorithm, threshold, or implementation is given. (b) The normalization of cosine similarity from [-1,1] to [0,1] (line 93) is mentioned but the method (e.g., clipping at 0, linear rescaling, or other) is not specified, making the metric term in Eq. 4 non-reproducible. (c) The description of the λ hyperparameter as having "positive or negative value depends on whether the data is a positive sample or a negative sample" (line 80) is confusing since all training data are positive MMP pairs, and the negative case is never defined or used.

- **The SC evaluation setup is underspecified**: The paper states it "randomly sampled 500 pairs of molecules" (line 146) but does not clarify whether these are MMP pairs (which would be biased toward higher similarity) or random unrelated molecules (which would be biased toward dissimilarity). The interpretation of the SC values depends on this choice, and altering it could reverse conclusions.

### Trivial
None.

## Nice-to-Haves
- Replace the SC ratio with a proper alignment measure, such as Spearman correlation between chemical and latent similarities over a held-out pair set, or mean absolute error after quantile normalization.
- Add a control experiment: train the baseline model for the same number of total epochs split into two stages (without consistency losses) to isolate the effect of the regularization from the extended training schedule.
- Compare MSCR with MMPs to MSCR with at least one alternative chemistry-aware augmentation (e.g., functional group replacement, scaffold hopping) to test the claimed superiority of MMPs.

## Removed Points
- **"The paper does not compare MSCR's distribution term to CR-VAE's KL regularizer / whether CR-VAE applied to molecules would solve the same problem"** — The paper already discusses CR-VAE (lines 34–35) and distinguishes MSCR from it (molecules vs. images, sensitivity vs. latent quality). Requesting a direct experimental comparison with CR-VAE applied to molecules asks for work outside the paper's stated scope and is speculative.
- **"Both base models are from 2021/2023, weakening generality"** — Rule prohibits mentioning missing related works or newer baselines.
- **"Section 5 limitation about two perspectives not being adequate is not discussed in experiments"** — The paper acknowledges this as a limitation in the future work section; criticizing it as an omission misreads the intent of self-acknowledged limitations.
- **"The paper incorrectly implies that only MMPs produce valid molecules"** — The paper says generic augmentations "could easily result in invalid or meaningless molecular structures" (line 48–49), which is factually correct for random deletion/flipping/node-dropping. It does not claim that no chemistry-aware alternative exists.
- **Various formatting/style nitpicks and speculative concerns** removed per filtering rules.

## Novel Insights
None beyond the paper's own contributions. The reviews did not surface a perspective on the work that the authors themselves had not already articulated.

## Suggestions
1. **Fix the SC metric**: Replace Tanimoto/Cosine ratio with a well-understood correlation measure (Spearman's ρ or Kendall's τ) between the full similarity lists in chemical and latent space, or report mean squared error after scaling. This would make the central quantitative claim interpretable and comparable across papers.
2. **Add error bars**: Report all optimization results (Tables 2–4) with at least 3 random seeds and standard deviations. This is standard practice and would help readers assess whether the 1–3% improvements are meaningful.
3. **Test the MMP claim**: Add one simple comparison — e.g., MSCR with MMPs vs. MSCR with random SMILES perturbation or functional group replacement — to directly test whether MMPs provide the claimed advantage over alternatives.
4. **Specify the cosine normalization**: Clearly state how cosine similarity is normalized to [0,1] (e.g., `(cos + 1) / 2` or `max(0, cos)`). Without this, the metric loss (Eq. 4) and the SC metric are not reproducible.
5. **Clarify the SC sampling procedure**: Specify whether the 500 random pairs for SC evaluation are drawn from the set of MMP pairs or from the full dataset, and justify this choice.
