- Decision: Accept
- Avg Score: 6.75
- Scores: 8, 8, 5, 6
Now I have a thorough understanding of the paper and both reviews. Let me produce the final consolidated review.

---

## Summary

CFGen is a conditional flow-based generative model for single-cell RNA-seq (and multi-modal RNA+ATAC) data that explicitly models discrete counts using negative binomial and Bernoulli likelihoods, rather than operating on pre-processed continuous values. The paper also extends classifier-free guidance for Flow Matching to support compositional generation conditioned on multiple categorical attributes (e.g., cell type + donor) from a single trained model. Experiments across five datasets show that CFGen recovers sparsity and overdispersion more faithfully than continuous-space baselines, achieves strong distribution-matching metrics, and demonstrates a downstream application of data augmentation for rare cell type classification.

## Strengths

1. **Explicitly models discrete counts via negative binomial and Bernoulli likelihoods.** CFGen is the only conditional generative model among compared baselines (scDiffusion, scGAN, scVI) that operates directly on raw counts. Evidence: Sections 3.1 and 4.1 define the generative process with negative binomial and Bernoulli likelihoods. Figure 2 shows that CFGen recovers the gene-wise mean-variance trend and zero-count-per-cell distribution nearly perfectly, while the continuous-space scDiffusion produces an unrealistic shift toward actively expressed genes — a clear and fundamental advantage over prior work.

2. **Compositional multi-attribute guidance with a single trained model.** CFGen extends classifier-free guidance to Flow Matching for multiple categorical attributes (Proposition 1, Section 4.3), enabling generation conditioned on arbitrary subsets of attributes without training separate models. Figure 4 qualitatively demonstrates controlled generation across attribute intersections (e.g., CD14+ monocytes + donor 1) — a capability absent from prior single-cell generative models.

3. **State-of-the-art multi-modal generation (RNA + ATAC).** CFGen outperforms the VAE-based MultiVI and unimodal baselines (PeakVI, scVI) on both expression and accessibility modalities on PBMC10K. Table 2 shows CFGen achieves the lowest MMD and Wasserstein-2 distance for both RNA and ATAC, and Figure 3b shows higher Pearson correlation for cell-type-specific marker peak accessibility and marker gene expression across all cell types.

4. **Downstream data augmentation improves rare-cell-type classification.** CFGen-generated cells augmenting training sets boost scGPT-based classifier generalization. Figure 5 shows the improvement is inversely correlated with cell-type frequency (Pearson r = −0.31 on PBMC COVID, −0.29 on HLCA), demonstrating concrete biological utility for rare cell types.

5. **Scales to large, challenging datasets.** CFGen achieves top or second-best performance on datasets with hundreds of thousands of cells (Tabula Muris 245k, HLCA 584k), where other conditional models degrade sharply. Table 1 shows c-CFGen achieves MMD 91.04 and WD 10.72 on HLCA vs. scDiffusion at 218.58 and 15.82.

## Weaknesses

### Fatal
None.

### Major

1. **Augmentation experiment lacks a control baseline for increased sample size.** The experiment in Section 5.4 compares classification performance on original vs. CFGen-augmented training sets and reports improvement, especially for rare cell types. However, the design does not control for the trivial effect of increased sample size. Augmenting rare classes with any method — including simple random oversampling, SMOTE, or scVI generation — can improve kNN classification. Without a baseline that substitutes CFGen with a simpler augmentation strategy, the evidence does not support the claim that CFGen's *realistic* generation specifically drives the improvement. The conclusion may be correct but is not yet supported by the presented experiment. *(Verified from Sections 5.4: the experiment compares original vs. CFGen-augmented sets without a non-CFGen augmentation control.)*

2. **Compositional guidance relies on a conditional independence assumption that is not empirically validated.** Proposition 1 (Section 4.3) derives the compositional vector field under the assumption that attributes $y_1,\ldots,y_K$ are conditionally independent given the latent variable $\mathbf{z}$. This is a strong assumption — in practice, donor and cell type, or tissue and mouse ID, may share residual dependencies not fully captured by $\mathbf{z}$. The paper does not provide any diagnostic: no comparison of generated attribute-combination distributions to the real joint distribution, no test of whether the composition recovers correct class proportions, and no quantitative evaluation of how violations of this assumption affect generation quality. The qualitative UMAP plots in Figure 4 are suggestive but insufficient to validate the theoretical foundation of the central ML contribution. The Discussion mentions "reliance on multiple assumptions, including independence assumptions" but does not specifically address or test this one. *(Verified from Sections 4.3 and 5.3: the assumption is stated in Proposition 1; Section 5.3 provides only qualitative UMAP evaluation; Discussion acknowledges limitations generically.)*

### Minor

3. **Comparison to baselines across different data spaces requires clearer transparency.** scDiffusion and scGAN generate normalized continuous values while CFGen generates discrete counts. The evaluation uses MMD and Wasserstein distance on PCA projections — but the paper does not explicitly state in the main text how baseline outputs were converted to the count space used for evaluation. The paper references an appendix (`\cref{sec: baseline_descr}`) for details, which is stripped by the parser, but the fairness of the comparison hinges on whether baselines are evaluated in their native space or a space they were not designed for. If scDiffusion's continuous outputs were naively rounded or normalized to match count space, the comparison could be biased. *(Verified from Section 5.1: "scDiffusion and scGAN operate on a continuous-space domain... Thus, we train them using normalized counts (more in \cref{sec: baseline_descr})" — the conversion detail is deferred to the appendix.)*

4. **Multi-attribute guidance evaluated only qualitatively.** Section 5.3 presents only UMAP overlap plots for the compositional guidance results. A quantitative metric — e.g., the accuracy of predicting the intended attribute(s) on generated cells, the fraction of cells falling in the correct attribute intersection, or a distribution-matching metric for attribute-conditional generation — would substantially strengthen this section and directly validate Proposition 1's practical behavior. *(Verified from Section 5.3: "Qualitative evaluation of guidance performance...")*

5. **Figure 2 does not specify which dataset was used.** The caption for Figure 2 states "(a) Comparison between the gene-wise mean-variance trend in real data and samples from generative models. (b) Number of zeroes per cell frequency in real data and samples from generative models." but does not identify the dataset, making the qualitative claim harder to interpret and reproduce. *(Verified from Figure 2 caption/labeling in the paper.)*

### Trivial

6. **The unconditional evaluation on Tabula Muris shows scGAN (MMD 17.05) outperforming u-CFGen (MMD 38.05) on one metric** — this is not discussed, though u-CFGen wins on Wasserstein distance (7.70 vs. 12.70). The paper's overall claims are measured ("overcomes scGAN in five out of eight metrics") and the numbers are presented transparently in the table, so this is a minor presentational omission rather than a substantive flaw. *(Verified from Table 1.)*

## Nice-to-Haves

- **Ablation of the flow architecture** (latent dimension, number of flow steps, choice of marginal paths) would help understand design choices.
- **Discussion of computational cost** (training time, sampling speed) would aid practitioners.
- **A second multi-modal dataset** (e.g., from 10x Multiome or sci-CAR) would strengthen the generalization of the multi-modal claims.
- As the paper itself notes (Section 5.3), varying guidance strengths are needed across different attribute pairs — a more systematic study of how to select guidance weights in practice would be valuable.

## Removed Points

- **Criticism that the augmentation experiment cannot distinguish realistic generation from more data** — This is kept as a Major weakness (not removed), as it is a genuine evidential gap in that specific experiment.
- **Criticism about missing appendix, proofs, or implementation details** — Removed per instructions (parser strips appendix sections from all papers; they exist in the original submission).
- **Criticism about missing related works** — Removed per instructions (lack of external sources to confirm existence).
- **Criticism about Figure 2 being "subjective" / "UMAP overlap"** — This was merged into weaknesses 4 and 5 above rather than kept as a separate item.
- **Strength Finder's generic strengths about importance of the problem** — Removed per instructions. Only concrete, evidence-backed strengths were retained.

## Novel Insights

The most noteworthy insight from the synthesis is the tension between the paper's strongest and weakest claims simultaneously: the method's most convincing advantage — recovering realistic discrete data properties (sparsity, overdispersion) via explicit count likelihoods — is orthogonal to the two main weaknesses. The augmentation weakness (no oversampling baseline) would affect any generative model claiming to produce realistic rare-cell data, not just CFGen. The compositional guidance weakness (unvalidated conditional independence) is technically interesting because Proposition 1 is mathematically correct under its stated assumption; the missing piece is an empirical check that real single-cell attribute combinations approximately satisfy this assumption or that the method is robust to mild violations. If the authors could show even modest robustness (e.g., RMSE between predicted and real joint attribute distributions), the theoretical contribution would be well-supported.

## Suggestions

1. **Add a simple augmentation baseline.** For Section 5.4, add a control where rare cell types are augmented via (a) random oversampling and (b) scVI generation. If CFGen still yields the largest classification improvement, the claim that realistic generation matters is strongly supported. If not, discuss what the improvement actually stems from.

2. **Add quantitative validation for compositional guidance.** For Section 5.3, train a classifier to predict attribute combinations on generated cells and report the accuracy or proportion of cells correctly falling into the intended intersection. Show that this proportion increases with guidance strength $\omega$.

3. **Clarify the baseline evaluation conversion.** State explicitly in the main text (not just the appendix) how scDiffusion's and scGAN's continuous outputs were mapped to the count space for MMD/WD computation, and whether the evaluation was also run on log-normalized data (the native space of scDiffusion) for a side-by-side comparison.

4. **Specify the dataset in Figure 2's caption** so readers can interpret the qualitative claims.
