- Decision: Reject
- Avg Score: 3.80
- Scores: 3, 3, 5, 3, 5
Now I have all the verification I need. Let me produce the consolidated final review.

## Summary

This paper proposes a new problem setting — Realistic Open-world Long-tailed Semi-supervised Learning (ROLSSL) — that removes the assumption that known and novel class distributions are similar (unlike prior OLSSL), and assumes labeled known-class data is far scarcer than unlabeled data. The authors also propose Dual-stage Post-hoc Logit Adjustment (DPLA), which adjusts logits using sample frequency, class count, and dataset size (first stage) and estimated unlabeled data frequencies (second stage). Experiments on six datasets under three distribution types show DPLA outperforming OpenLDN (the only adapted baseline) with large margins.

## Strengths

1. **The ROLSSL setting fills a genuine gap.** Table 1 explicitly contrasts ROLSSL against 10 related settings, showing it uniquely removes the S/N distribution-consistency assumption and relaxes the unrealistic data balance of prior OLSSL. This formalization is well-motivated and practically relevant.

2. **DPLA yields large, consistent gains over the adapted baseline (OpenLDN) across all datasets and distribution types.** For example, under CIFAR-10 Uniform, DPLA achieves 50.5% All accuracy vs. OpenLDN's 24.2%; under CIFAR-10 Reversed, novel-class accuracy jumps from 1.2% to 38.3% (Table 1). The pattern holds across all six datasets and all three distribution forms.

3. **The ablation study cleanly isolates each DPLA stage.** The SVHN ablation (Table 3) shows the first-stage logit adjustment raises novel-class accuracy from 0.5% (baseline) to 32.5%, the second stage adds further gains to 35.3%, and the pseudo-label refinement yields 35.4%. This directly confirms the dual-stage design is responsible for the improvement.

4. **The scaling-factor analysis (Figures for CIFAR-100 and ImageNet-100) validates the necessity of the first-stage redesign.** Unmodified PLA performs worse than the OpenLDN baseline on many-class datasets, while the proposed scaling factor restores and surpasses baseline performance, confirming the paper's diagnosis that vanilla PLA fails on larger class counts.

5. **Section 4.3 (daomrs) provides a concrete diagnosis of OpenLDN's failure in ROLSSL.** The paper shows OpenLDN progressively loses novel-class recognition during training on SVHN, while DPLA maintains stable recognition. This behavioral analysis strengthens the argument that DPLA addresses a real deficiency in existing methods.

## Weaknesses

### Fatal
None. The core contribution (ROLSSL setting + DPLA method) is not invalidated by any single unrecoverable error.

### Major
- **Only one baseline compared under the ROLSSL setting.** Tables 1 and 2 compare DPLA exclusively against OpenLDN for the long-tailed conditions. OpenLDN was designed for a different setting (balanced S/N distributions, more labeled data) and clearly struggles on ROLSSL (novel-class accuracies as low as 0.5–4.2%). While the "Semi-supervised & Open-world" rows provide 8 additional OSSL baselines under non-long-tailed conditions, no OLSSL method (e.g., BACON, NCDLR) or LTSSL method (e.g., DASO, ACR) mentioned in Related Work is adapted to ROLSSL. Without this, it is unclear whether DPLA is genuinely effective or merely less broken than the one baseline that was adapted.

- **Missing hyperparameter values for key components.** The method introduces \(\mathcal{C}_{base}\), \(\mathcal{S}_{base}\) in Eq. (3) and \(\alpha, \beta\) in Eq. (4). None of these values are reported for any dataset or distribution condition. The ablation for the scaling factor shows that different magnitudes affect performance (Figures for CIFAR-100, ImageNet-100), but the specific settings used in the main tables are never stated. The second-stage parameters \(\alpha, \beta\) are never reported or ablated at all. This undermines reproducibility.

- **No error bars or multi-run statistics.** All results in Tables 1 and 2 are reported as single numbers. The paper acknowledges that OpenLDN is unstable (line 265: it "rarely" regains novel-class recognition, requiring cherry-picking the best run), yet DPLA's own variance is never quantified. Given the acknowledged instability, readers cannot assess whether DPLA's advantage is robust across seeds.

- **Sign inconsistency between the prediction rule and the loss function.** The prediction rule in Eq. (2) uses \(f_y(x) - \tau_1 \cdot \log \Omega_y\) (subtracting the adjustment from logits). However, the balanced cross-entropy loss in Eq. (7) uses \(e^{f_y + \tau \log \Omega_y}\) in the numerator (adding the adjustment). If \(\Omega_y\) is larger for more frequent classes (since it includes \(\mathcal{F}_{y_i^l}\) as a factor), then Eq. (2) correctly reduces the bias toward frequent classes while Eq. (7) would amplify it. This sign conflict is never discussed or resolved.

### Minor
- **Temperature scaling notation is confusing.** The paper introduces \(\tau_1\) in Eq. (2), \(\tau_2\) in Eq. (6), and \(\tau\) (without subscript) in Eq. (7) and the text discussion. The relationship among these values is never specified, and it is unclear whether they are the same parameter or independently tunable.

- **Ablation of DPLA components is limited to SVHN (10 classes).** The component-level ablation (Table: Baseline → +First Stage → +Second Stage → +PLR) is conducted only on SVHN, a digit-recognition dataset with 10 classes. While the scaling-factor analysis covers CIFAR-100 and ImageNet-100, the stage-by-stage decomposition is not validated on larger-class datasets where the problem is hardest.

- **Notation error in Section 3.1.** The imbalance ratio formula \(\gamma_n^u = \max_c M_1 / \min_c M_{c_k}\) uses inconsistent indices (\(M_1\) is a constant, not a function of \(c\); \(M_{c_k}\) is a single class, not an extremum). This appears to be a copy-paste error.

- **S/N Consistency column in Table 1 is not defined.** The column values ("Reject", "Yes", "No") are not explained in the caption or text, making the table harder to interpret.

- **The claim of "up to 50.1% performance improvements" is ambiguous.** It conflates absolute percentage-point gains (novel-class accuracy on CIFAR-10 Uniform: 3.8% → 53.9%, a 50.1 percentage-point increase) with relative improvement. While the numbers are correct, the phrasing could mislead readers into thinking this is a relative improvement.

### Trivial
- The t-SNE visualizations (Figure 4) are qualitative and lack quantitative clustering metrics (e.g., silhouette score) to substantiate the visual claim of "better recognition performance."
- The phrase "no premise on the distribution relationships" (abstract) slightly overstates the setting; the paper tests three specific distribution forms (consistent, uniform, reversed), which are representative but finite.

## Nice-to-Haves
- Adapting at least 2–3 additional methods (e.g., BACON, DASO, or a simple LTSSL + open-world combination) to ROLSSL would substantially strengthen the evaluation.
- Reporting the values of \(\mathcal{C}_{base}, \mathcal{S}_{base}, \alpha, \beta\) used in all main experiments is essential for reproducibility.
- Including multi-run statistics (mean ± std over 3–5 seeds) would address the stability concern the paper itself raises about OpenLDN.
- A limitations section acknowledging the method's reliance on estimated class frequencies, sensitivity to hyperparameters, and the scope of distribution types tested would improve the paper's completeness.

## Removed Points
These points are flagged for removal — they are inaccurate, overblown, or based on misunderstandings of the paper:

- **"Contradiction between 'no premise on distribution' and three specific forms"** — The paper means the setting does not *assume* a specific distribution relationship (unlike prior work assuming consistency), and then evaluates three *representative* forms. This is not a contradiction; it is a reasonable experimental design. The abstract's phrasing could be clearer, but the critic's framing as a contradiction is too strong. → Moved here from weaknesses.

- **"Cherry-picking OpenLDN's best run is a fundamental failure of comparison fairness"** — The paper openly admits selecting OpenLDN's best run, which makes the comparison *harder* for DPLA, not easier. This is non-standard methodology (no error bars) and is absorbed into the "no error bars" weakness above, but it does not unfairly inflate DPLA's results. → Merged into the error-bars weakness; the "cherry-picking" framing in isolation is misleading.

- **"Section 3.2 is copied verbatim from standard OSSL descriptions"** — The paper describes the OSSL framework as background. This is standard practice for self-contained exposition. The critic provides no evidence of verbatim copying, and the description is appropriate for the paper's scope.

- **"The baseline table is irrelevant"** — The "Semi-supervised & Open-world" rows in Tables 1 and 2 provide context on how standard OSSL methods perform on the same datasets without the long-tail component. This is useful for understanding the difficulty added by the long-tailed conditions, not irrelevant.

- **"Missing related works"** — Removed per instructions (cannot verify with external sources).

- **"Missing appendix content, proofs, or references"** — Removed per instructions (parser strips these from all papers).

- **All pure formatting/style/typo nitpicks** — Removed per instructions (parser artifacts, not author errors).

## Novel Insights
None beyond the paper's own contributions. The two reviewers' perspectives are largely consistent: both recognize the value of the ROLSSL setting and the plausibility of DPLA, while flagging the insufficient evaluation breadth and missing details as the main barriers to acceptance.

## Suggestions

1. **Expand baselines**: Adapt at least 2–3 additional methods (e.g., BACON, DASO, or a simple re-weighting + OpenLDN combination) to the ROLSSL setting and report their performance under all three distribution types.

2. **Report all hyperparameters**: State the values of \(\mathcal{C}_{base}, \mathcal{S}_{base}, \alpha, \beta\) used for every dataset and distribution condition. Provide ablation of these parameters on CIFAR-100 or ImageNet-100, not just SVHN.

3. **Add error bars**: Report means and standard deviations over multiple random seeds (3–5) for all methods and conditions.

4. **Fix the sign inconsistency**: Clarify whether Eq. (7) should use \(-\tau \log \Omega\) (consistent with Eq. 2) or \(+\tau \log \Omega\). If the latter, explain the reasoning. Also unify the temperature notation (\(\tau, \tau_1, \tau_2\)).

5. **Extend component ablation to larger datasets**: The stage-by-stage ablation (Table 3) should be replicated on at least one dataset with more classes (e.g., CIFAR-100) to demonstrate that the component benefits generalize beyond 10-class problems.

6. **Fix the notation error**: Correct the indices in the formula for \(\gamma_n^u\) in Section 3.1.
