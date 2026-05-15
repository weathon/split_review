Now I have all the information needed. Let me produce the consolidated review.

## Summary

CFGen is a flow-based conditional generative model for discrete multi-modal single-cell data (RNA counts and ATAC peak accessibility). It combines a latent Flow Matching prior with negative binomial and Bernoulli likelihood decoders to explicitly model the discrete, over-dispersed, and sparse nature of single-cell data. It further extends classifier-free guidance for Flow Matching to a compositional multi-attribute setting (Proposition 1), enabling controlled generation under multiple biological and technical covariates using a single trained model.

## Strengths

- **Explicitly models discrete counts and recovers sparsity/over-dispersion better than continuous alternatives.** By using a negative binomial likelihood with gene-specific inverse dispersion and a Bernoulli likelihood for accessibility, CFGen captures the per-gene mean-variance trend and the distribution of zero counts per cell almost perfectly, whereas scDiffusion (which assumes continuous data) produces a shifted, unrealistically low sparsity pattern (Figure 2, panels a and b). This directly supports the paper's core methodological motivation.

- **Achieves state-of-the-art or competitive distribution matching across four diverse scRNA-seq datasets.** In Table 1, c-CFGen obtains the lowest MMD on three of four datasets (PBMC3K, Dentate gyrus, HLCA) and the lowest Wasserstein-2 distance on three of four (PBMC3K, Dentate gyrus, HLCA), outperforming scDiffusion and scVI. On the large HLCA dataset (584k cells), CFGen is the only conditional model with competitive MMD and Wasserstein-2 while scDiffusion and scVI score substantially worse.

- **Multi-modal generation outperforms existing VAE-based models on both RNA and ATAC modalities.** On the PBMC10K multiome dataset, CFGen achieves the lowest MMD and Wasserstein-2 for both RNA and ATAC (Table 2), and yields higher Pearson correlations across all 15 cell types for marker gene expression and marker peak accessibility than MultiVI (Figure 3b), demonstrating biologically meaningful multi-modal generation beyond distribution matching.

- **Single model enables unconditional, single-attribute, and multi-attribute generation without retraining.** By learning both conditional and unconditional velocity fields via classifier-free guidance with one network (described in Algorithms 1 and 2), CFGen can generate samples with no conditioning, single-attribute conditioning, or composition of arbitrary attribute subsets by adjusting guidance weights at inference time. This is demonstrated in Figure 4 where the same model produces unconditional coverage, single-attribute generations, and attribute intersections.

- **Data augmentation for rare cell type classification shows practical downstream value.** Using CFGen to upsample rare cell types improves held-out F1 scores of a kNN classifier on scGPT embeddings, with improvement inversely correlated with cell type frequency (Pearson r = -0.31 on PBMC COVID, -0.29 on HLCA; Figure 5).

## Weaknesses

### Fatal
None.

### Major

- **Compositional guidance (a core contribution) is only evaluated qualitatively with no quantitative metrics.** Section 5.3 presents only UMAP visualizations (Figure 4) with no attribute classification accuracy, attribute consistency scores, or percentages of generated cells matching the target attribute combination. Guidance strengths ω_i are not selected systematically; the paper acknowledges that "different attribute pairs require varying guidance strengths" but does not study this sensitivity quantitatively. The conditional independence assumption in Proposition 1 is stated but never tested, and its violation in real datasets (where attributes such as cell type and donor may correlate) could render the composition invalid. Since compositional multi-attribute generation is presented as a primary ML contribution, the lack of quantitative validation is a significant gap.

- **Data augmentation experiment lacks baselines needed to attribute improvement to CFGen's specific approach.** The experiment compares a kNN classifier trained on the original training set vs. one trained on the original set augmented with CFGen-generated cells. There is no comparison with (a) simple random oversampling of real rare cells to the same class proportions, (b) augmenting with data from other generative models (scVI, scDiffusion), or (c) using CFGen to generate equal numbers per class (to isolate rebalancing from data quality). Without these controls, the observed improvement could reflect merely having more training data for rare classes rather than CFGen's specific synthetic data quality.

### Minor

- **Autoencoder reconstruction quality is not separately validated despite a two-stage training procedure.** The encoder and decoder are pre-trained before the flow is learned (Section 4.1), yet no reconstruction metrics (e.g., correlation between input and decoded counts, per-gene MSE) are reported. While the end-to-end metrics (MMD, WD) implicitly validate the full pipeline, separate reconstruction validation would strengthen confidence that the latent space is meaningful before flow training. The flow's advantage over a simple Gaussian prior (as in scVI) is demonstrated by the overall results, but ablation isolating the autoencoder quality would be informative.

- **kNN F1 scores for cell-type classification of generated cells are uniformly low across all methods (0.08–0.43).** This suggests that cell-type identity is not well preserved by any generative model on a per-cell basis, which tempers the claim that cells are "realistic" at the annotation level. However, this affects baselines equally (scVI's F1 is also low at 0.09–0.43) and does not undermine comparative claims about distribution matching or biological property recovery.

- **In the unconditional setting, scGAN outperforms u-CFGen on some metrics (e.g., Tabula Muris MMD: scGAN 17.05 vs. u-CFGen 38.05; HLCA MMD: scGAN 30.34 vs. u-CFGen 84.84).** The paper's discussion of unconditional results could more transparently acknowledge these cases. (u-CFGen still wins on 6 of 8 unconditional metrics, so this does not threaten the overall conclusions.)

### Trivial

- The generative factorization assumes independence of size factor \(l\) and attribute \(y\) (Eq. 1), which may not hold when cell type correlates with total counts. The paper acknowledges this and notes flexibility in the factorization (line 102), but does not test the impact of violations.

## Nice-to-Haves

- For multi-modal evaluation, a baseline concatenating separately trained scVI and PeakVI (or scVI+scVI) could further contextualize CFGen's joint modeling advantage.
- An ablation of size factor conditioning to understand its role in generation quality.
- Downstream evaluation beyond classification (e.g., differential expression, trajectory inference) would broaden the demonstrated utility.

## Removed Points

These points are flagged to be removed, treat them with caution:

- *"The proof is relegated to the appendix (unavailable)."* — **Removed by rule:** The parser strips appendix sections from all papers; they exist in the original submission.
- *"Discrete modeling is only in the decoder (same as scVI); the novelty is the flow prior, not the discrete likelihood."* — **Removed:** The paper's claim is about the *combination* of discrete likelihoods with a flow matching prior, which differs from scVI's Gaussian prior. The critic understates the methodological distinction.
- *"The compositional guidance is straightforward; Zheng et al. (2023) already established CFG for flow matching."* — **Removed:** This is a judgment of novelty. Proposition 1 extends single-attribute CFG for flow matching to multi-attribute composition, which is a nontrivial bridge connecting compositional diffusion scores to flow-matching vector fields.
- *"Improvement may reflect that scGPT's representation is better at capturing CFGen's patterns, not that CFGen data is inherently higher quality."* — **Removed:** The held-out evaluation is on *real* data; improved classification of real cells after training on CFGen-augmented data indicates genuine signal, not a representation artifact.
- *"Multi-modal comparison lacks scVI+PeakVI concatenated as a baseline."* — **Moved to Nice-to-Haves:** Not a standard baseline; the paper already compares with MultiVI, PeakVI, and scVI.
- *"The ATAC metric uses TF-IDF normalization — whether this is appropriate for binary data is not discussed."* — **Removed:** TF-IDF on binary accessibility data is standard practice in single-cell genomics (e.g., Signac, ArchR).

## Novel Insights

None beyond the paper's own contributions. The reviewers did not identify any pattern or insight about the paper that the authors themselves had not already stated.

## Suggestions

1. **Add quantitative evaluation for compositional guidance**: Compute attribute classification accuracy, attribute consistency scores, or fraction of generated cells matching target attribute combinations (e.g., what percentage of cells generated for "CD14+ monocytes + donor 1" actually cluster with real CD14+ monocytes from donor 1?). This is the single most important addition to validate a core contribution.

2. **Add simple oversampling baseline for data augmentation**: Compare CFGen augmentation against random oversampling of real rare cells to the same class proportions. This is a minimal control that would substantially strengthen the augmentation claims.

3. **Report autoencoder reconstruction metrics**: Include correlation between input counts and decoded means, or per-gene reconstruction MSE, to validate that the latent space is meaningful before flow training.

4. **Test compositional guidance when the conditional independence assumption is violated**: On a dataset where attributes are correlated (e.g., cell type and batch covary), assess whether compositional guidance degrades.

5. **Add an ablation isolating augmentation quality from rebalancing**: Generate equal numbers of cells per class (not upsampling rare types) and test whether classification improves. This would separate the benefit of CFGen's data quality from the benefit of having more examples of rare types.

## Score and Decision

The paper makes a solid contribution — combining discrete likelihoods with flow matching for single-cell data is well-motivated and leads to improved distribution matching and biologically faithful properties (sparsity, overdispersion). The compositional guidance framework is theoretically sound and practically relevant. However, two weaknesses substantially limit the strength of the presented evidence: (1) the compositional guidance (a core contribution) lacks any quantitative validation, and (2) the data augmentation experiment lacks the baselines needed to attribute improvement to CFGen specifically. These are addressable with additional experiments and do not invalidate the paper's primary claims about generative performance. The paper merits acceptance contingent on these gaps being addressed.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>