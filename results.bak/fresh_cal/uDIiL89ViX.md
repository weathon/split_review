Now I have a thorough understanding of the paper and can verify every claim. Let me write the final consolidated review.

## Summary

The paper investigates whether dictionary learning can extract biologically-meaningful concepts from unsupervised microscopy foundation models (MAEs trained on Cell Painting data). It proposes Iterative Codebook Feature Learning (ICFL), a new dictionary learning algorithm that avoids dead features without explicit regularization, and combines it with PCA whitening on a control dataset as a form of weak supervision. The paper demonstrates that extracted features are selective for cell types, genetic perturbations, and functional gene groups; that ICFL matches or exceeds TopK SAEs in selectivity while having zero dead features; and that the features correlate strongly with handcrafted CellProfiler features. Qualitative analysis links specific features to known biological mechanisms (adherens junctions, ALG-3 co-localization with ER, TSC-2 and membrane markers).

## Strengths

1. **Quantitative evidence of biologically-meaningful features from unsupervised microscopy models.** Table 3 (referenced in text) reports hundreds of ICFL features with average selectivity above 0.1 across diverse biological labels (cell types, batch effects, siRNA/CRISPR perturbations, functional gene groups), providing direct evidence that dictionary learning can extract features correlated with known biological concepts from a completely unsupervised vision model.

2. **ICFL eliminates dead features without auxiliary regularization.** Table 1 (referenced) shows ICFL has 0 dead features out of 8192 across all conditions, while TopK SAEs have thousands of dead features. This is a concrete algorithmic advantage validated by the paper's own experimental protocol.

3. **PCA whitening on a control dataset substantially improves feature quality.** Figure 2a shows that without PCA whitening, linear probing accuracy drops considerably (e.g., from ~0.45 to ~0.30 for Task 3), and this effect dominates over sparsity choices. The paper provides a clear biological motivation: unperturbed HUVEC cells serve as a control, and whitening downweights directions that capture nuisance variation rather than perturbation signal.

4. **Unsupervised features match handcrafted CellProfiler features in selectivity.** Figure 3e shows ICFL features achieve nearly identical maximum average selectivity scores as CP features across genetic perturbations, and the Pearson correlation of 0.71 between CP and ICFL feature selectivities per label (Figure 3g) provides a strong validation that the method recovers patterns similar to domain-expert-designed features.

5. **Qualitative analysis grounds features in known biology.** Section 7.1's case study of the adherens-junctions-correlated feature ties token-level heatmaps to disrupted cell morphology and unperturbed cells that retain connections. Section 7.2's channel-specific correlation analysis (ALG-3: 0.63 with ER vs. 0.16 with actin; TSC-2: -0.71 with membrane/Golgi) provides concrete evidence that features localize to subcellular compartments consistent with known gene function.

## Weaknesses

### Fatal
None.

### Major

- **Ambiguity in the ICFL vs. TopK selectivity comparison (Figures 2d–2f).** Section 6 opens with "If not further specified, we always use features extracted from ICFL in combination with PCA whitening" — this only sets the default for ICFL. When the paper reports "We plot in Figure 2d-2f the selectivity scores for both ICFL features and TopK SAEs" and claims "ICFL features consistently achieve higher selectivity scores than TopK SAE features," it does not explicitly state whether TopK also received PCA whitening. Since Figure 2a demonstrates that PCA whitening itself causes large improvements, the reader cannot determine whether the claimed advantage is due to ICFL's algorithmic design or to differential preprocessing. This is the paper's headline quantitative result, and the ambiguity undermines its interpretability.

- **Missing PCA whitening implementation details.** The paper describes learning "a PCA-and-centerscale transform on this control dataset" (Section 5) but does not specify how many principal components are retained, whether the output dimension is reduced, or what the "centerscale" operation entails exactly. These details are necessary for reproducibility.

### Minor

- **Unspecified subset of Task 3 labels in the CellProfiler comparison.** The paper states the comparison uses "a subset of Task 3" (Section 6.2) without specifying which labels were selected or the selection criterion. This limits the reader's ability to assess whether the match between CP and ICFL features is robust across all 1138 siRNA perturbations.

- **No error bars or uncertainty quantification on selectivity and linear probing curves.** Figures 2a–2f and 3e–3g report single curves without variance estimates, making it impossible to assess the reliability of the observed differences — particularly for the ICFL vs. TopK selectivity comparison that is central to the paper's claims.

- **ICFL algorithm description could benefit from a fuller specification.** While the paper correctly cites OMP (Mallat & Zhang 1993) and describes the iterative residual-subtraction procedure clearly, the optimization used to "learn the features z^(1) that best reconstruct x≈W_dec z^(1)" (least-squares solve vs. gradient-based approach) is not explicitly stated. The full pseudo-code (Algorithm 1) was present in the original submission but is missing from the extracted text; it should be included in the main paper or appendix for completeness.

### Trivial
- The figures are not directly readable in the extracted text (parser artifact), but the captions and in-text descriptions are adequate to follow the results.

## Nice-to-Haves

- A comparison to additional dictionary learning variants (e.g., standard L1-sparse autoencoders, Gated SAEs, or JumpReLU SAEs) would strengthen the claim that ICFL is broadly advantageous, though the comparison to TopK and CellProfiler is reasonable given the paper's focus.
- A hyperparameter sensitivity analysis for the sparsity parameters (K=100 for TopK, J=20/k=5 for ICFL) and the random-reset threshold (cosine > 0.9) would be useful but is not required for the validity of the current results.
- Statistical significance tests for the selectivity difference between ICFL and TopK would strengthen the quantitative claims, though the consistent advantage across tasks is already suggestive.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Paper does not cite classic dictionary-learning literature (OMP, K-SVD, etc.)"** — Removed because it is factually incorrect. The paper explicitly cites "the orthogonal matching pursuit algorithm of Mallat & Zhang (1993)" and describes ICFL as a variant thereof. This criticism reflects a misreading of the paper.
- **"ICFL is essentially OMP and novelty is unacknowledged"** — Removed. The paper acknowledges the OMP relationship and the novelty lies in the training procedure (alternating between OMP-based sparse coding and gradient-based decoder updates with random resets), which is distinct from standard OMP-based dictionary learning.
- **"Lack of comparison to Gated/JumpReLU SAEs"** — Weakened to a nice-to-have. The paper compares against TopK SAE (the most standard baseline in this literature) and CellProfiler (the domain gold standard). This is sufficient for a first demonstration in a new application domain.
- **"Algorithm 1 missing / reproducibility concern about missing pseudo-code"** — Removed because Algorithm 1 was present in the original submission as an image and was stripped by the PDF parser. The textual description in Section 4 is already substantive for a reader familiar with OMP.
- **"Table 1 and Table 3 content not visible"** — Removed; these are parser artifacts.
- **"Missing related work"** — Removed per instruction (cannot verify external sources).

## Novel Insights

The most interesting observation that emerges from merging the reviews is the tension between two features of the paper: the ICFL algorithm is described as using "a variant of OMP" with iterative residual subtraction, while simultaneously claiming novelty. The paper's actual novelty appears to lie not in the sparse-coding step (which is standard OMP) but in the alternating optimization loop (OMP-based sparse coding → gradient-based decoder update → random resets for decorrelation) that prevents dead features without auxiliary regularization. This hybrid approach — combining the matching-pursuit family's deterministic sparse coding with gradient-based decoder learning — is under-explored in the mechanistic interpretability literature and could be worth highlighting more explicitly. Additionally, the paper's use of PCA whitening on a control dataset as a form of "weak supervision" for dictionary learning — downweighting variance directions that correspond to nuisance variables rather than signal — is a practical insight that may transfer to other scientific domains where control data is available.

## Suggestions

1. **Explicitly state the PCA whitening configuration for both methods in the selectivity comparison.** In a revision or rebuttal, clarify whether Figures 2d–2f compare ICFL+PCA vs. TopK+PCA, ICFL+PCA vs. TopK alone, or both with/without PCA. If TopK does not receive PCA whitening by default, add the missing condition and report all four combinations.
2. **Report the number of PCA components retained** and details of the centerscale transform used for whitening. This is a one-sentence addition that significantly improves reproducibility.
3. **Add error bars or confidence intervals** to the selectivity and linear probing plots, or at minimum explain why single-run results are sufficient in this setting (e.g., deterministic training, large token counts).
4. **Specify which subset of Task 3 labels was used** for the CellProfiler comparison and why.
5. **Explicitly state** whether the optimization for learning z^(1) in ICFL is a least-squares solve (as in standard OMP) or a differentiable alternative, and include the full Algorithm 1 in the main body.

## Score and Decision

This paper makes a genuine contribution: it provides the first systematic evidence that dictionary learning extracts biologically-meaningful features from unsupervised microscopy foundation models, proposes a practical algorithm (ICFL) that avoids dead features, and validates the features against a human-expert-designed baseline (CellProfiler) with strong correlation. The qualitative analysis is particularly compelling and grounds the approach in real biology.

The main weakness is the ambiguity in the experimental reporting — specifically whether the ICFL vs. TopK selectivity comparison controls for PCA whitening — which is significant because it affects the paper's central quantitative claim. However, this is an addressable clarity issue rather than a fatal flaw: Figure 2a already demonstrates that the authors can and do run both methods with and without PCA, suggesting the missing transparency is a reporting oversight rather than a confounded experimental design. The paper's other contributions (qualitative validation, CellProfiler comparison, dead-feature analysis) stand independently.

With the PCA condition clarified, this paper would be a solid contribution to both the mechanistic interpretability and computational biology communities.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>