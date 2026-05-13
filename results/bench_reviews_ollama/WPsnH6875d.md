Now I have enough information to write the consolidated review. Let me carefully assess each claim.

## Summary

The paper identifies a methodological flaw in prior "safe SSL" evaluations: when fixing total unlabeled data size and varying unseen-class proportions, seen-class data decreases simultaneously, confounding the measured impact of unseen classes. To address this, the authors propose the RE-SSL framework that fixes seen-class data (r_s) while independently varying unseen-class data (r_u) across five factors (sample number, category number, category index, nearness, label distribution). They evaluate 15 SSL methods on CIFAR-10/100 using five metrics and two robustness definitions, finding that unseen classes do not necessarily harm—and can sometimes improve—performance, and that simpler SSL methods (PseudoLabel, PiModel) appear more "robust" than sophisticated ones (FixMatch).

## Strengths

- **Identification of a genuine methodological flaw in prior work.** The paper correctly identifies that previous safe SSL evaluations confounded the loss of seen-class data with the addition of unseen-class data. The structural causal model (Fig. 1) and the comparison of evaluation setups (Fig. 2a vs. 2b) provide a clear and valid critique. This is the paper's strongest contribution.

- **Comprehensive empirical evaluation.** The paper evaluates 15 SSL algorithms (10 classical, 5 robust) across 5 factors and multiple metrics on CIFAR-10 and CIFAR-100, generating a large body of comparative data. The GM analysis in Table 6, which ranks the relative impact of each factor (sample number being most impactful at 0.170, label distribution least at 0.040), provides useful empirical insights.

- **Multi-dimensional evaluation design.** Moving beyond the single-factor evaluations of prior work to systematically study sample number (r), category number (C_n), category index (C_i), nearness, and label distribution (C_ib) is a genuine organizational contribution that reveals previously unexamined aspects of how unseen classes interact with SSL models.

## Weaknesses

### Fatal
None.

### Major

- **The proposed framework introduces a confound comparable to the one it identifies.** The paper's central critique of prior work is that they confounded the decrease in seen-class data with the increase in unseen-class data. However, by fixing r_s and adding unseen-class data as r_u increases, the total dataset size grows monotonically with r_u. Any observed performance maintenance or improvement could be attributed to more total training data (providing more gradient updates, regularization, etc.) rather than unseen-class data being benign or beneficial. The paper's claim that "unseen classes may even enhance [SSL performance]" (abstract) is unsupported without a control that adds seen-class data (or random noise data) at the same rate. The paper does not acknowledge this limitation in Section 7, instead only noting the lack of theoretical analysis. This mirrors the very confounding the paper criticizes in prior work.

- **"Robust" methods are simply methods that barely use unlabeled data.** The paper finds that PseudoLabel and PiModel are the most "robust" but then explains: "The unsupervised loss derived from their inconsistencies is minimal, hence the algorithms exhibit strong robustness" (Section 5.4). This means these methods are insensitive to unseen-class data precisely because they are insensitive to all unlabeled data. Calling this "robustness" conflates ineffectiveness with robustness and misrepresents the practical takeaway. A truly robust method should effectively leverage seen-class unlabeled data while being resistant to unseen-class data—not be robust by ignoring all unlabeled data.

### Minor

- **The nearness experiment confounds semantic and input-space differences.** Section 5.4 compares "near OOD" (CIFAR-10 classes, 32×32 RGB) vs. "far OOD" (MNIST, 28×28 grayscale) to study the effect of semantic nearness. These datasets differ dramatically in input space, color channels, and distributional properties, making it impossible to attribute observed differences solely to semantic nearness. The conclusion that "the smaller the semantic shift... the less damage to the SSL models" is not well-supported by this comparison. This is partially mitigated by the fact that cross-dataset OOD comparisons are common practice, but the specific semantic-shift claim should be qualified.

- **The δ_g = −0.020 threshold is chosen without justification.** Section 5.3 states "assume that σ_g equals -0.020" but provides no reasoning for this particular value. Different thresholds would change which methods are classified as "robust," making the robustness categorization somewhat arbitrary. Since Definition 1 uses an existential quantifier ("if there exists δ_g such that R_slope ≥ δ_g"), every algorithm technically satisfies it, and the practical classification depends entirely on this unstated threshold choice.

- **R_slope linear regression may misrepresent nonlinear accuracy trends.** The metric fits a linear slope across 7–8 r values, but the accuracy data in Tables 1–2 often shows nonlinear patterns (sharp initial drops, plateaus, or recoveries). While R_slope serves as a useful summary statistic, it can assign similar slopes to qualitatively different trajectories. The paper does not discuss this limitation or consider alternatives (e.g., AUC, monotonic regression).

### Trivial
None.

## Nice-to-Haves

- A control experiment adding equal-volume seen-class data (or random noise data) alongside the unseen-class data would cleanly separate the "more data" effect from the "unseen class data" effect, substantially strengthening the paper's core claim.
- Reporting the supervised-only baseline accuracy at each r_u value would help distinguish "robust because ignoring unlabeled data" from "robust because handling unseen classes well."
- Testing on at least one additional domain beyond CIFAR-10/100 (e.g., SVHN, DomainNet) would strengthen generality claims.

## Removed Points

- *Claim that unseen classes "demonstrate" performance enhancement (Strength Finder #4)*: This claimed strength is contested by the total-dataset-size confound. Without a same-volume control, it is impossible to attribute performance gains to unseen-class data specifically rather than to increased training data volume. **Move to removed.**

- *Insightful analysis of near vs. far OOD (Strength Finder #5)*: The near/far comparison is confounded by input-space differences (CIFAR vs. MNIST), undermining the semantic-shift conclusion. This is noted as a minor weakness. **Move to removed as a strength.**

- *Harsh critic's claim about 3 seeds and no standard deviations*: While 3 seeds is on the low side, this is common practice in deep learning evaluations and the paper reports average accuracy. Requesting more seeds or confidence intervals is a nice-to-have, not a substantive weakness. **Move to removed.**

- *Harsh critic's claim about limited datasets (only CIFAR)*: The paper evaluates on both CIFAR-10 and CIFAR-100. While more datasets would strengthen generality, two standard benchmarks is adequate for an evaluation-focused paper. This is a nice-to-have, not a major weakness. **Move to removed.**

- *Harsh critic's notational criticism about stray `\1}` in label space definition*: This is a parser artifact, not an author error. **Move to removed.**

- *Harsh critic's claim that GM conflates increasing and decreasing trends*: GM measures deviation from mean, which is by design a measure of sensitivity regardless of direction. This is a feature, not a bug—GM captures overall variability. **Move to removed.**

- *Harsh critic's claim that C_n results are just a "more data" effect*: This is a reasonable concern but is subsumed by the overall total-dataset-size confound already listed as a major weakness. **Move to removed as redundant.**

## Novel Insights

The paper's most important insight is that the "conventional wisdom" that unseen-class unlabeled data is always harmful may be an artifact of a flawed evaluation protocol. However, this insight is partially undermined by the fact that the proposed evaluation protocol has its own confound (total data volume), and that methods classified as most "robust" are simply those that barely utilize unlabeled data. The most defensible takeaway is that the impact of unseen-class data is highly method-dependent: methods with strong unsupervised losses (FixMatch, FreeMatch) are genuinely sensitive to unseen classes, while methods with weak unsupervised losses are trivially robust. The five-factor decomposition (r, C_n, C_i, nearness, C_ib) with GM rankings reveals that sample quantity (r) dominates the impact while label distribution (C_ib) matters least—this ordering is a useful empirical finding.

## Suggestions

- Add a control experiment where seen-class data is added at the same rate as unseen-class data to distinguish the volume effect from the unseen-class effect. This is the single most important improvement.
- When discussing "robust" methods, differentiate between methods that effectively use seen-class unlabeled data while resisting unseen classes (valuable robustness) and methods that are insensitive to all unlabeled data (trivial robustness). Including a supervised-only baseline at each r_u level would make this distinction clear.
- Justify or systematically test the δ_g = −0.020 threshold, or replace the binary robust/not-robust classification with a continuous ranking.
- Qualify the nearness finding to acknowledge that CIFAR-10 vs. MNIST comparisons conflate semantic distance with input-space differences.

## Score and Decision

The paper makes a genuine and important contribution by identifying the confounding variable in prior safe SSL evaluations. The comprehensive evaluation of 15 methods across 5 factors also provides useful empirical data. However, the proposed RE-SSL framework introduces a confound (total dataset size increasing with r_u) that is comparable in severity to the one it identifies, and the paper does not acknowledge this limitation. The claim that unseen classes "may even enhance" performance lacks the necessary controls. Additionally, the most "robust" methods are simply those that least effectively use unlabeled data, making the robustness label misleading in practical terms. These issues significantly weaken the paper's positive claims, though the diagnostic contribution remains. With revisions—particularly adding a same-volume control and reframing the "robustness" finding—the paper could be significantly strengthened.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>