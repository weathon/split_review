Now let me read the calibration papers to calibrate scoring.Round-1 bracket: **5.0 – 6.5**. Now narrowing within the bracket.I've gathered sufficient calibration data. Now let me compose the final review.

---

## Summary

MUBen is a benchmark paper that systematically evaluates 7 uncertainty quantification (UQ) methods—spanning deterministic, Bayesian, post-hoc calibration, and ensemble categories—across 6 molecular backbone models (ChemBERTa, GROVER, Uni-Mol, DNN, TorchMD-NET, GIN) and 14 MoleculeNet property prediction datasets. The central contribution is empirical: establishing which UQ methods pair well with which backbone architectures and characterizing how the expressiveness–calibration trade-off plays out across diverse molecular tasks. Key findings include the consistent benefit of Deep Ensembles, the lightweight effectiveness of Temperature Scaling for classification, the advantage of BBP/SGLD for regression uncertainty, and Uni-Mol's tendency toward overconfidence despite best predictive accuracy.

---

## Strengths

- **Comprehensive scope that fills a genuine gap**: No prior work had jointly evaluated modern pre-trained molecular backbones with a diverse UQ method suite at this scale. The combination of 7 UQ methods × 6 backbones × 14 datasets spanning quantum mechanics, physical chemistry, physiology, and biophysics is broader than prior molecular UQ benchmarks, which typically covered a single architecture class or narrow task domain (Section 4).

- **Actionable practitioner guidance grounded in systematic evidence**: The recommendation to use Deep Ensembles for consistent gains across both prediction and calibration (Tables 1 and 2), Temperature Scaling as a lightweight always-useful classifier calibrator (with a concrete caveat on ToxCast scaffold-calibration misalignment), and BBP/SGLD for regression uncertainty despite accuracy costs (Section 5, Table 2, "7 out of 8 top ranks") are concrete, not vague.

- **Insightful SGLD "play safe" mechanistic observation**: Figure fg5.3 and the accompanying analysis show that SGLD consistently predicts large variances without better error–variance correlation, with a plausible causal explanation (noisy training preventing mean convergence). This is specific enough to guide practitioners away from SGLD when precise regression accuracy matters.

- **Tanimoto-binned OOD distribution shift analysis (Section 5, Figure fg5.5)**: The binning of QM9 test data by Tanimoto similarity to training scaffolds and the resulting observation that calibration error stays stable while RMSE/MAE grows nearly linearly with OOD-ness is a genuinely novel analytical contribution within a benchmark paper.

- **Frozen backbone and random split ablations (Table 5.3)**: These controls isolate the effect of backbone expressiveness on calibration (frozen backbones improve regression CE; random splits produce overconfident variance estimates), directly supporting the paper's broader expressiveness–calibration thesis.

---

## Weaknesses

### Fatal
None.

### Major

- **Rankings reported without statistical uncertainty estimates** (Section 4.3, all tables): Each metric is the mean of exactly 3 seeds, and no standard deviations or confidence intervals appear in the tables. For the fine-grained ranking claims—particularly "BBP and SGLD capture 7 out of 8 top ranks for 4 backbones on two metrics" (Section 5)—it is impossible to determine whether these advantages are robust or small-sample artifacts. Scaffold splits are deterministic, so the split itself is not a source of variability, but seed-to-seed variance on small datasets like FreeSolv and BACE is well-documented to be high. A benchmark paper whose utility is guiding method selection is particularly vulnerable to this gap: practitioners relying on rankings need to know how stable the rankings are. This is not a structural flaw—the data already exists—but presenting it without error bars understates how much noise is in the headline claims.

### Minor

- **The primary/supplementary backbone split is only partially justified before results** (Section 4.1 vs. Section 5): The paper does state the split up front in Section 4.1, attributing it to pre-training constraints (TorchMD-NET limited to QM data; GIN randomly initialized). However, the in-text justification in Section 5 ("excluded from the primary benchmark due to their limited capabilities") frames performance as the deciding criterion, which is circular for a benchmark. The principled architectural/pre-training rationale in Section 4.1 is the right frame; the paper should consistently use that framing rather than shifting to capability-based language in Section 5.

- **Coarse hyperparameter grids may disadvantage noise-sensitive methods** (acknowledged in Section 6): The paper itself acknowledges "coarse-grained hyperparameter grids" in the Conclusion. SGLD and BBP are more sensitive to their learning-rate schedules and noise temperatures than Temperature Scaling (one parameter) or Deep Ensembles (trivially tuned). The comparison therefore slightly tilts against Bayesian methods. The paper is transparent about this, but it is worth flagging that the relative ranking of BBP/SGLD vs. simpler methods may overstate the accuracy penalty of the former.

- **The expressiveness–calibration relationship claim is supported informally** (Section 5, last paragraph): The conclusion that "models with lower expressiveness tend to exhibit better calibration" is a potentially important finding, but the paper supports it with qualitative comparison of Uni-Mol vs. DNN via figures rather than systematic correlation analysis. A table correlating each backbone's mean prediction accuracy with its mean calibration error across datasets would sharpen this from an impression into a result.

### Trivial

None beyond the methodological points above.

---

## Nice-to-Haves

- The Tanimoto-binned OOD analysis on QM9 is compelling, but QM9's DFT-computed (essentially noiseless) labels are a special case. Extending the analysis to at least one noisy biological dataset (e.g., Tox21 or BACE) would test whether calibration stability under distribution shift holds when labels themselves have stochastic measurement error.

- A practical decision table mapping task type (classification/regression) × backbone choice × data availability to recommended UQ method would operationalize the benchmark's purpose without requiring new experiments.

- Multi-task aggregation across ToxCast (617 tasks) vs. Tox21 (12 tasks) uses macro-averaging. A brief check of whether conclusions change under task-count weighting would strengthen robustness of headline classification findings.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

**Harsh Critic: Focal Loss description is "slightly off"** — The paper cites both Lin et al. and Mukhoti et al., and its framing ("minimizes a regularised KL divergence") explicitly follows Mukhoti et al.'s Dirichlet/maximum-entropy regularization interpretation rather than the raw re-weighting framing. This is a valid theoretical lens, not an error. Removed.

**Strength Finder: "This paper addressed an important problem"** — Generic strength with no specific grounding. Removed from strengths.

**Strength Finder: "Use of proper scoring rules"** — While accurate, this is standard practice and not specific to this paper's contribution. Removed as a standalone strength; the quality of metric selection is absorbed into the general experimental rigor.

**Harsh Critic: Uni-Mol's factors are "confounded" and the conclusion about 3D conformations is "not isolated"** — The paper explicitly lists multiple factors explaining Uni-Mol's performance ("large network size, various pre-training data and tasks, and the integration of results from different conformations") without claiming to isolate 3D conformations specifically. The claim attributed to the harsh critic is a strawman. Removed.

---

## Novel Insights

The most genuinely novel insight is the tension between expressiveness and calibration made concrete in a real benchmark. The paper demonstrates that Uni-Mol, the most predictively accurate backbone, consistently has the *worst* calibration, while DNN with hand-crafted RDKit features calibrates better than all pre-trained models on several tasks. This directly challenges the implicit assumption that better models need UQ methods less. The SGLD "play safe" behavior (large predictive variances without better error–variance correlation) is a specific mechanistic observation that complements the general finding: Bayesian training methods regulate variance at the cost of mean accuracy, yielding an indirect, not principled, uncertainty signal. Together, these findings suggest that the standard accuracy–calibration trade-off may be *amplified* rather than resolved by model scale in molecular property prediction, which has direct practical consequences for active learning and high-throughput screening pipelines where both accuracy and calibrated confidence are needed simultaneously.

---

## Suggestions

1. **Add seed-level standard deviations to all main tables** (or at minimum to the headline ranking summary rows). The experiments are already run; this requires only reporting what is computed.

2. **Consolidate the backbone inclusion rationale into a single consistent framing**: use the architectural/pre-training argument from Section 4.1 in Section 5 as well, rather than reverting to capability language.

3. **Run the Tanimoto OOD analysis on Tox21 or BACE** to test whether calibration stability under distribution shift generalizes beyond noiseless quantum datasets.

4. **Add a scatter plot of backbone mean RMSE vs. mean CE across datasets** to support the expressiveness–calibration claim quantitatively.

---

## Score and Decision

### Calibration Summary

| Anchor | Path | Avg Score | Round | Comparison to MUBen |
|---|---|---|---|---|
| Drug Response Benchmark | u8L1zzGXRq | 3.0 | R1 (low) | Much weaker: inconsistent benchmarks, narrow scope |
| MoleculeCLA | P5jreWnIjV | 4.0 | R1 (mid) | Weaker: new dataset but single-task evaluation |
| MARCEL Conformer Benchmark | NSDszJ2uIV | 6.33 | R1 (mid) | Comparable: introduces new datasets; MUBen has broader UQ coverage |
| EGraFFBench | NvJxTjTQtq | 6.0 | R1 (mid) | Comparable: new datasets+metrics, but correctness concerns; MUBen more reliable |
| BenchMol | 1JgWwOW3EN | 4.8 | R1 (mid) | Somewhat weaker: broader modalities but shallower UQ analysis |
| RoFt-Mol (mol FT benchmark) | IbCvnpJ4py | 5.25 | R2 | Weaker: single backbone type, limited pre-training coverage; MUBen clearly stronger |
| BEV UQ Benchmark | k3y0oyK7sn | 5.40 | R2 | Comparable but MUBen broader (7 UQ × 6 backbones × 14 datasets vs. 5 × 2 × 3), though BEV paper adds novel loss |
| FairlyUncertain | C1Wp4ubvXZ | 5.60 | R2 | Comparable: systematic UQ benchmark in different domain; similar scope trade-offs |
| GeoBFN | NSVtmmzeRB | 8.0 | R1 (high) | Much stronger: novel algorithmic contribution with strong experimental support |

**Round-1 bracket**: 5.0–6.5  
**Round-2 narrowing**: MUBen is clearly better than RoFt-Mol (5.25) due to broader backbone coverage and SOTA models. It is comparable to BEV UQ Benchmark (5.4, Accept) in depth but is broader. It falls short of MARCEL (6.33) because it introduces no new datasets. The acknowledged coarse hyperparameter search and absence of error bars keep it from the upper end of the bracket.

**Final score: 5.5** — MUBen is a solid, well-scoped benchmark that fills a genuine gap and delivers useful practitioner insights. The absence of statistical uncertainty on rankings (3 seeds, no error bars) is a real methodological gap for a paper whose primary product is method rankings. The work is publishable and community-useful but sits at the borderline, weaker than anchor MARCEL (6.33) and comparable to BEV UQ benchmark (5.4).

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>