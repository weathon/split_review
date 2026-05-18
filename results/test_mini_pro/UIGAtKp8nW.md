Now I have a thorough understanding of the paper and the calibration anchors. Let me compose the final consolidated review.

---

## Summary

MUBen is a benchmark that systematically evaluates 8 uncertainty quantification (UQ) methods across 4 primary backbone molecular representation models (ChemBERTa, GROVER, Uni-Mol, DNN) on 14 MoleculeNet classification and regression tasks under scaffold splitting. The paper identifies actionable trends: Deep Ensembles consistently improve both prediction and calibration, Temperature Scaling reliably reduces classification overconfidence, Bayesian methods (BBP, SGLD) excel at regression uncertainty estimation despite sometimes degrading accuracy, and larger models like Uni-Mol are most prone to overconfidence. A Tanimoto-similarity binned analysis of distribution shift on QM9 provides a concrete look at how calibration degrades under increasing train-test mismatch.

## Strengths

- **Broad, well-organized benchmark design**: The paper evaluates 4 primary backbone architectures spanning SMILES, 2D graph, 3D conformation, and hand-crafted feature descriptors, paired with 8 UQ methods from four distinct methodological categories (deterministic, Bayesian, post-hoc, ensembles). This breadth, maintained under a consistent scaffold-split evaluation protocol, makes MUBen one of the most comprehensive UQ evaluations in the molecular domain (Sections 4.1–4.3).

- **Actionable, evidence-backed insights**: The paper identifies concrete regularities — Deep Ensembles consistently help both prediction and calibration (Tables 5.1–5.2), Temperature Scaling is a low-cost calibration fix for classification (Figure 5.2), BBP/SGLD deliver strong regression uncertainty at the cost of mean prediction accuracy (Figure 5.3, Table 5.2), and Uni-Mol's superior expressiveness comes with the worst calibration (Figure 5.3, Section 5). These findings are well-supported by the reported rankings and MRRs.

- **Distribution-shift stability analysis**: The experiment binning QM9 test points by Tanimoto similarity to training scaffolds (Figure 5.5, Section 5) shows that while predictive error degrades smoothly under increasing distribution shift, calibration error remains relatively stable. This goes beyond aggregate metrics and offers a template for more granular UQ evaluation.

- **Transparent handling of model scope**: The paper includes TorchMD-NET and GIN as supplementary backbones and explains clearly why they are treated separately (limited pre-training scope for TorchMD-NET, no pre-training for GIN), along with frozen-backbone and random-split ablation experiments (Table 5.3). This adds credibility rather than hiding unfavorable results.

## Weaknesses

### Fatal

None.

### Major

- **Lack of metric variance reporting undermines the benchmark's prescriptive claims**: The paper reports averages over 3 seeds but provides no standard deviations, confidence intervals, or statistical comparisons anywhere in the main text. For a benchmark that claims to guide method selection — e.g., "BBP and SGLD deliver commendable performance in predicting regression uncertainty, capturing 7 out of 8 top ranks" — readers cannot assess whether differences between methods are distinguishable from noise. While 3-seed averaging is standard practice in this subfield, omitting any measure of dispersion weakens the core claim that these rankings can inform practitioner decisions. The paper should at minimum report per-dataset standard deviations for the metrics that underpin the ranking tables.

- **Analysis remains largely descriptive rather than diagnostic**: Many observations are restated as trends (e.g., "SGLD's tendency to 'play safe' by predicting larger variances," "larger models are more confident") without deeper investigation into mechanism. The explanation for SGLD's behavior — "the noisy training trajectory prevents SGLD and BBP from sufficiently minimizing the gap between the predicted mean and true labels" — is a post-hoc hypothesis (explicitly marked as "we assume") rather than verified through, e.g., examining how predicted variance varies with data density or tracking the evolution of variance during training. A benchmark aiming to inform UQ selection would benefit from at least one or two case studies dissecting *why* a specific backbone–UQ pair succeeds or fails.

### Minor

- **No OOD detection evaluation**: The paper motivates UQ through uncertainty-critical applications (e.g., high-throughput screening, wet-lab design) where detecting out-of-distribution inputs matters at least as much as in-distribution calibration. The scaffold-split setup creates a mild OOD scenario, but the paper only probes this through calibration error and one distribution-shift experiment on QM9. Including a held-out scaffold detection task with AUROC would substantially strengthen alignment between the paper's motivation and its evaluation.

- **Gaussian assumption for regression calibration not discussed**: The CE metric (Section 3) assumes a Gaussian predictive distribution parameterized by predicted mean and variance. The paper does not discuss whether this assumption holds across the diverse MoleculeNet regression tasks (e.g., QM7/QM9 may be approximately Gaussian; solubility may not be). If violated, CE values may not accurately reflect calibration quality.

- **Distribution-shift analysis limited to one dataset**: The Tanimoto-similarity binning experiment on QM9 (Figure 5.5) is the paper's strongest analytical contribution but is performed only on a single dataset with limited backbones. Extending it to at least one classification dataset would strengthen the generality of the conclusions.

- **Training split variance not captured**: The paper uses three random seeds {0, 1, 2} but does not clarify whether these seeds also control the scaffold split itself. If the split is fixed and only initialization/training randomness varies, the reported variance underestimates the true variance from dataset partitioning, which matters for a benchmark.

### Trivial

- The paper does not discuss the known sensitivity of ECE to binning strategies and sample sizes, which is a standard methodological caveat in the UQ literature.

- The interaction between validation-based early stopping and UQ methods with multi-phase training schedules (e.g., SWAG) is not explained, which could affect reproducibility for those specific methods.

## Nice-to-Haves

- A hyperparameter sensitivity study showing how UQ metric rankings shift under different learning rates, prior scales, or ensemble sizes would strengthen confidence in the reported trends. The paper already acknowledges the coarse hyperparameter grid as a limitation.

- Reliability diagrams for all UQ methods on a few representative classification datasets (not just the Focal Loss and Temperature Scaling examples in Figure 5.2) would make over/under-confidence patterns more immediately visible.

- Scatter plots of predicted standard deviation vs. absolute error for key backbone–UQ combinations would reveal whether calibration improvement comes from genuine uncertainty-error correlation or uniform variance inflation.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Criticism about ensemble size not being stated in the main text**: The harsh reviewer flagged that the Deep Ensemble size is not in the main text. The paper references the appendix (`\cref{appsec:uncertainty}`), and per the hard rules, appendix-deferred content is not a valid weakness (the parser strips appendix sections).

- **Criticism about backbone selection bias (TorchMD-NET/GIN demotion)**: The paper transparently explains why TorchMD-NET (pre-trained only on quantum mechanical data) and GIN (no pre-training) are treated as secondary backbones and still reports their results. This is a reasonable design choice, not a flaw.

- **Criticism about missing appendix / supplementary tables**: The harsh reviewer noted that "supplementary material (not available) may contain full tables." The parser strips appendix sections; per hard rules, this concern is invalid.

- **Criticism about introduction overstating novelty**: The reviewer claimed the paper overlooks existing UQ work on pre-trained molecular models. Per hard rules, missing related work critiques are not included since we cannot verify their existence.

- **Criticism about lack of epistemic/aleatoric uncertainty decomposition**: This is outside the paper's stated scope (evaluating UQ methods for calibration and prediction, not decomposing uncertainty types). Removed as scope creep.

- **Criticism about DNN feature specification**: The reviewer asked which 200 RDKit features are used. The appendix presumably contains these details; this is a trivial implementation detail that does not affect the paper's core claims.

- **Strength Finder claim about "rigorous evaluation under distribution shift" (unqualified)**: While scaffold splitting is a good protocol, the lack of statistical rigor (no standard deviations) and the limited number of seeds temper the "rigorous" label. Kept in Strengths but qualified.

## Novel Insights

The most distinctive finding from this benchmark is the persistent observation that backbone expressiveness and calibration quality are inversely related — Uni-Mol, the strongest predictor, is also the most overconfident — and that this relationship holds across multiple UQ method categories. The Tanimoto-similarity binned analysis further reveals that this calibration gap is relatively stable under increasing distribution shift (error degrades but calibration holds), suggesting that the overconfidence problem in large molecular models is structural rather than merely a consequence of particular train-test splits. This insight has practical implications: the paper demonstrates that UQ method selection matters *more* for larger backbone models, as shown by the larger calibration-error gaps between Deterministic and best-UQ for Uni-Mol vs. DNN.

## Suggestions

1. Add standard deviations (at minimum) across the 3 seeds to the ranking tables. Even a compact report of per-dataset variance would substantially strengthen the benchmark's prescriptive value.
2. Pick one well-performing and one poorly-performing backbone–UQ pair and provide a deeper diagnostic analysis (e.g., predicted variance histograms, error-variance correlation, or training dynamics) to move beyond descriptive reporting.
3. Extend the Tanimoto-similarity distribution-shift analysis to at least one classification dataset and one additional UQ method to test the generality of the calibration-stability finding.
4. Add a brief discussion of the Gaussian assumption underlying the regression CE metric and its potential limitations for non-Gaussian molecular property distributions.

---

**Originality**: The paper is the first to systematically benchmark UQ methods on pre-trained molecular representation models at this breadth. While the individual components (UQ methods, backbones, datasets) are not novel, the combination and systematic evaluation fill a genuine gap.

**Importance**: Uncertainty-aware molecular property prediction is important for drug discovery and materials science. The paper's findings provide practical guidance for practitioners selecting UQ strategies.

**Claim support**: The claims are generally supported by the evidence, though the lack of variance reporting weakens the prescriptive authority of the rankings.

**Soundness**: The experimental design (scaffold splits, 3 seeds, consistent metrics, multiple backbones and UQ categories) is sound. The main soundness gap is the omission of variance estimates.

**Clarity**: The paper is well-organized and clearly written, with effective use of tables, MRR visualizations, and calibration curves.

**Value**: The benchmark provides a useful reference for the molecular ML community and a template for more rigorous UQ evaluation. The Tanimoto-similarity analysis in particular offers a replicable methodology for probing distribution-shift effects on calibration.

## Score and Decision

**Anchor comparison:**

| Anchor | Path | Avg Score | Comparison |
|--------|------|-----------|------------|
| MARCEL (molecular conformer ensembles benchmark) | NSDszJ2uIV | 6.33 | MARCEL curates novel datasets and defines a new problem framing; MUBen uses existing datasets (MoleculeNet) and existing methods, giving MARCEL a novelty edge. MUBen has broader UQ method coverage and comparably strong insights. |
| BEV UQ benchmark | k3y0oyK7sn | 5.40 | Both are UQ benchmarks in specific domains. BEV UQ introduces a new loss function alongside the benchmark; MUBen is benchmark-only but covers more methods and datasets. Similar level of contribution. |
| BenchMol (multi-modality molecular benchmark) | 1JgWwOW3EN | 4.80 | BenchMol has broader modality coverage but suffers from fundamental concerns about label quality and practical value. MUBen has a tighter, more defensible scope and more actionable findings. |
| Risk-to-Uncertainty (UQ theoretical framework) | cWfpt2t37q | 7.00 | This paper has a strong theoretical contribution that MUBen lacks; MUBen is purely empirical. MUBen clearly scores below this anchor. |
| MoleculeCLA (computational molecular benchmark) | P5jreWnIjV | 4.00 | MoleculeCLA has fundamental label accuracy concerns and limited task diversity. MUBen uses established wet-lab datasets and has a clearer value proposition. MUBen is clearly stronger. |
| LST-Bench (time-series benchmark) | 2wwPG1wpsu | 2.50 | LST-Bench has marginal novelty and limited insights. MUBen is substantially stronger in both breadth and insight quality. |

MUBen sits between BEV UQ (5.40) and BenchMol (4.80). It is a solid benchmark paper with genuine breadth and actionable insights, held back primarily by the lack of variance reporting and predominantly descriptive analysis. It does not reach the level of benchmarks that combine breadth with novel dataset curation or theoretical contributions (6.0+), but it is clearly above fundamentally flawed or narrow benchmarks (≤4.0).

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>