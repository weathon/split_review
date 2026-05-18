Now I have a thorough understanding of the paper. Let me construct the final consolidated review.

## Summary

This paper proposes the Polyak Parameter Ensemble (PPE), a method that constructs a weighted average of model parameters saved at each epoch interval during training. PPE requires no additional test-time memory, no extended training, and no trainable parameters. The method is evaluated extensively on knowledge graph embedding (KGE) tasks — link prediction with DistMult, ComplEx, and QMult across 7 datasets plus multi-hop reasoning — and on CIFAR-10 image classification. Results show consistent improvements over the single-model baseline across nearly all settings, with benefits growing as embedding dimension increases.

## Strengths

- **Consistent generalization improvement across a diverse experimental landscape.** PPE improves MRR and Hits@N for three KGE models on FB15K-237, YAGO3-10, NELL-995 splits, UMLS, KINSHIP, Mutagenesis, and Carcinogenesis (Tables 4–6), improves multi-hop query answering (Table 7), and shows smoother accuracy trajectories on CIFAR-10 (Figure 1). This breadth of evidence across 11 datasets, 3 model architectures, and 2 task types supports the paper's central claim.

- **Virtually zero additional computational cost.** As claimed, PPE requires no extra training time, no test-time latency increase, and the same memory footprint as a single model. The paper notes "we did not detect any runtime overhead of using PPE" (Section 5), and this zero-overhead property is a genuine practical advantage over prediction ensembles.

- **Empirical scaling analysis with embedding dimension.** Table 8 systematically varies embedding size d from 4 to 256 on UMLS and KINSHIP, showing that PPE's benefits become more tangible as model capacity grows (for d ≥ 32, DistMult+PPE achieves higher scores in 81/96 cases). This gives practical guidance about when the method is most useful.

- **Theoretical motivation linking parameter averaging to gradient noise reduction.** Section 3 derives how equal-weight averaging divides later-epoch gradient contributions by the epoch index i, thereby reducing the influence of noisy mini-batch gradients from later epochs. This provides a principled rationale beyond the empirical gains.

## Weaknesses

### Fatal
None.

### Major

- **No experimental comparison against Stochastic Weight Averaging (SWA, Izmailov et al., 2018).** The paper cites Izmailov et al. (2018) in its related work (line 36) but never discusses or experimentally compares against SWA, which is the most directly relevant prior work. SWA also averages model parameters over a training trajectory, requires no additional memory at test time, and improves generalization. With equal weights and a cutoff epoch (j=200), PPE with λ=1.0 is essentially SWA restricted to the tail of training. The paper's claimed contribution — the exponential weighting scheme — cannot be assessed without comparing against the equal-weight variant (which is SWA). This is the single most important missing experiment.

- **No comparison against prediction ensembles or other lightweight ensemble techniques.** The paper frames PPE as a remedy to the three disadvantages of prediction averaging (training cost, latency, memory), yet never compares PPE's generalization against the prediction-ensemble approaches it critiques. Comparisons against, e.g., a 2-model prediction ensemble, MC Dropout, or snapshot ensembles (Huang et al., 2017) are needed to calibrate the practical significance of the "virtually no additional cost" claim. Without them, the reader cannot judge whether the trade-off (modest parameter averaging gains vs. potentially larger prediction-ensemble gains) favors PPE.

- **No error bars, confidence intervals, or multi-seed results.** Every result table reports single numbers with no variance. For a method whose improvements are often modest (fractions of a percent in MRR), the reader cannot determine whether the gains are reliable or due to random seed variation. Given that KGE training can be sensitive to initialization and optimizer stochasticity, single-run reporting is insufficient to support the paper's claims.

### Minor

- **The CIFAR-10 experiment is presented only as a qualitative visualization (Figure 1) with no quantitative test accuracy numbers.** Reporting final test accuracy and comparing PPE to the base model (and ideally to SWA) would straightforwardly strengthen the claim that the method generalizes beyond KGE.

- **The mathematical derivation mixes notation (Θ and w for parameters) and has clarity gaps.** The derivation in Section 3 uses Θ for parameter vectors in SGD update equations but switches to w at several unmarked transitions. The derivation also assumes simple SGD, while experiments use Adam — the paper does not discuss whether the theoretical argument (which relies on gradient noise being the primary source of circling) holds under adaptive optimizers.

- **The claim about alleviating "circling behavior" around a minimum is plausible but unsubstantiated.** The paper provides no empirical evidence (e.g., tracking of gradient norms, parameter displacement, or loss-surface visualization) for this mechanism.

- **The exponential weighting scheme and the cutoff epoch j=200 are underexplored.** j=200 is fixed for all datasets, including those trained for only 200 epochs (where j=N means only the final epoch gets weight). λ ∈ {1.0, 1.1} is tested, but no sensitivity analysis is provided for either hyperparameter.

### Trivial
None that survive the hard-rule filter.

## Nice-to-Haves

- Include multi-seed runs with standard deviations for all main results. This would significantly improve credibility.
- Compare against SWA with the same schedule (equal weights on the tail). If PPE (with λ=1.1) outperforms SWA on KGE tasks, the exponential weighting becomes a genuine contribution. If not, the paper should be reframed as an application of SWA to KGE models — still useful, but requiring adjusted claims.
- Compare against at least one lightweight prediction ensemble baseline (e.g., 2-run prediction averaging) to calibrate the quality-compute trade-off.
- Report concrete training-time measurements (seconds/epoch with and without PPE) on a specified GPU.
- Include a clear pseudocode description of the PPE update procedure.

## Removed Points

- **"The paper never cites SWA."** Removed as factually incorrect. The paper cites Izmailov et al. (2018) — the SWA paper — at line 36. The valid concern (no experimental comparison against SWA) is preserved in the Major weaknesses.

- **"ααα0:j = 0 and αααj+1:N = N1−j is garbled."** Removed as a parser artifact. The original submission's mathematical notation was likely typeset correctly.

- **Criticism about typos/grammar** ("beneftis," "zigzaging," "the same memory the memory requirement"). Removed per hard rules: parser-stripped formatting artifacts are not author errors.

- **Criticism that "more heavily influenced by the parameter vectors obtained at the early stage" is wrong.** Removed as a misunderstanding of the derivation. Equation (6) correctly shows that later-epoch gradients are divided by their epoch index i, making the ensemble more influenced by earlier parameter vectors. The paper's claim is mathematically sound.

## Novel Insights

None beyond the paper's own contributions. The reviewer analyses largely recapitulate the paper's stated claims (PPE improves generalization at zero cost, benefits scale with d) while identifying methodological gaps (missing SWA comparison, missing prediction-ensemble baselines, no error bars). No reviewer offers a novel synthesis that recontextualizes the work in an unexpected way.

## Suggestions

1. **Add an SWA baseline.** Run SWA (uniform averaging over the tail of training) with the same epoch cutoff and compare against PPE with λ=1.0 and λ=1.1. This single experiment would determine whether the exponential weighting adds value over standard parameter averaging, and would directly address the most important gap.

2. **Add error bars.** At minimum, report results over 3–5 random seeds with mean and standard deviation for the main results (Tables 4–6). This is especially important for the smaller datasets where improvements are marginal.

3. **Add at least one prediction ensemble baseline.** A 2-model prediction ensemble (two independently trained models, predictions averaged at test time) would calibrate the benefit of PPE against the simplest alternative ensemble method.

4. **Quantify the CIFAR-10 results.** Report final test accuracy numbers, and ideally compare against SWA and the base model.

5. **Clarify the weighting procedure with pseudocode.** A step-by-step description of when and how α coefficients are applied, how the running average is maintained, and when the ensemble is finalized would aid reproducibility.

## Score and Decision

The paper has genuine empirical breadth — 11 datasets, 3 model architectures, 2 task types — and the consistent improvement across this landscape is a real finding. However, the contribution is limited by two major methodological gaps: (1) the most directly relevant prior work (SWA) is cited but never experimentally compared against, making it impossible to assess what PPE adds beyond applying SWA to KGE models; (2) the paper critiques prediction ensembles but never compares against them, leaving the "remedy" framing unsupported. Combined with the absence of error bars, these gaps weaken the paper below the acceptance threshold. The empirical results are suggestive and useful, but the experimental design as presented does not substantiate the claimed novelty or practical significance.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>