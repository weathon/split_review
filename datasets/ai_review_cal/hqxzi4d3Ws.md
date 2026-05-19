- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3, 3
Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper adapts classical randomized smoothing to certify robustness against parameter-level noise in parameterized quantum circuit (PQC) classifiers. It introduces Theorem 3.1, which guarantees that any parameter perturbation δ within an L₂-norm bound scaled by per-parameter σ will not change the smoothed classifier's prediction. The paper shows that optimizing for this bound maps naturally onto Evolutionary Strategies (sNES), requiring only a change of objective function. Experiments on two condensed-matter classification tasks (cluster phase classification and SPT state preparation) demonstrate achievable robustness-accuracy trade-offs and robustness-variance correlations.

## Strengths

- **Theorem 3.1 provides a formally stated certified robustness guarantee for parameter noise in PQC classifiers.** The theorem (Eq. 1) adapts the classical randomized smoothing framework (Cohen et al., 2019; Tecot & Hsieh, 2021) to PQC parameter perturbations, giving an explicit bound ‖δ ⊘ σ‖₂ < ½(Φ⁻¹(p_A) − Φ⁻¹(p_B)) that guarantees the smoothed classifier's prediction is unchanged. The paper is clear about the provenance of the bound, and the adaptation is technically sound. (Evidence: Section 3.1, Definition 3.3, Theorem 3.1, Equation 1.)

- **The connection between optimizing the certified bound and Evolutionary Strategies is clean and practical.** The paper shows (Section 3.2) that training to maximize the certified margin ½(Φ⁻¹(p_A)−Φ⁻¹(p_B)) is equivalent to running sNES with a modified objective, requiring no new optimization infrastructure. This is a genuine insight that makes the method immediately deployable for practitioners already using ES for VQA optimization. (Evidence: Section 3.2, Equations re-formulating the optimization goal.)

- **Per-parameter σ enables flexible, non-uniform certified radii.** Rather than assuming uniform robustness across all parameters, the diagonal covariance matrix allows each parameter to have its own noise tolerance. The experiments in Sections 5.2–5.3 illustrate that this can leverage differing parameter sensitivities to improve overall robustness, as evidenced by the robustness-variance correlation analysis. (Evidence: Section 3.1 discussion, Section 5.2 results discussion, Figures 1–2.)

- **Empirical validation on two distinct condensed-matter classification tasks.** The method is demonstrated on cluster phase classification (12-qubit Hamiltonian) and SPT state preparation classification (8-qubit Hamiltonian), both important benchmarks. The results present robustness-accuracy frontiers and robustness-variance correlations, showing the method can be applied to different types of PQC tasks. (Evidence: Sections 5.2–5.3, Figures 1–2.)

## Weaknesses

### Fatal
None. The theoretical framework (Theorem 3.1 → ES connection) is sound and constitutes a valid contribution. No weakness in the review invalidates the paper's core theoretical claims.

### Major

- **No baselines: the experiments do not establish that the method improves robustness over alternative approaches.** The paper presents trade-off curves for the proposed method but never compares against (a) standard (non-robust) training of the same PQC evaluated under parameter noise, or (b) a simple test-time-only smoothed classifier derived from a standard-trained model. Without such comparisons, the reader cannot determine whether the proposed training procedure provides any robustness benefit beyond what one would obtain from a normally trained circuit or from naively applying randomized smoothing at test time. This is the single most significant weakness — the experiments characterize the method but do not validate it against alternatives. (Verified: Sections 5.2–5.3 contain no baseline comparisons.)

- **No empirical certified accuracy at a concrete noise level is reported.** The paper defines metrics derived from the certified radius (certified area geometric mean, semi-axis average) and reports their averages over the test set. However, it never picks a specific parameter noise level σ_noise and reports the fraction of test points for which the certificate radius exceeds that noise level (i.e., certified accuracy). The metrics presented are useful, but the paper's central claim of "noise resilience" would be substantially strengthened by a concrete demonstration that for a specific noise level, X% of test points are provably robust. (Verified: Sections 4–5 report only radius-derived metrics, not certified accuracy at a chosen σ_noise.)

### Minor

- **Training and test sets of only 50 samples each raise generalization concerns.** Both tasks use 50 training samples and 50 test samples. The paper does not report the number of PQC parameters, discuss whether 50 samples is sufficient, report variance over multiple data splits, or provide confidence intervals for the reported metrics. The paper acknowledges on line 210 (Figure 2 caption) that "results may vary due to randomness and instability in optimization," yet does not quantify this variability. (Verified: Line 175, Section 5.)

- **The QCNN architecture details (parameter count, depth, ansatz specifics) are not provided beyond references to Cong et al. (2019) and Vatan & Williams (2004).** This affects reproducibility and makes it impossible to assess whether the 50-sample dataset is plausibly sufficient. (Verified: Section 5.1.)

### Trivial
None.

## Nice-to-Haves

- Adding a standard-trained baseline and a test-time-only smoothed baseline would significantly strengthen the experimental validation.
- Reporting certified accuracy at one or more specific σ_noise values (e.g., the fraction of test points certified at noise levels corresponding to known device characteristics) would make the practical implications clearer.
- Reporting confidence intervals or standard deviations over multiple runs or data splits would improve reproducibility.
- A brief resource analysis (e.g., number of circuit evaluations per gradient step, wall-clock time for hyperparameter sweeps) would help practitioners assess feasibility, though the paper's reference to Appendix B.3 (stripped in extraction) likely addresses this.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **"No details on sample complexity or computational cost for estimating p_A/p_B via Monte Carlo"** — The paper states (line 85) that concentration inequalities are used to estimate bounds on p_A and p_B and references Appendix B.3 for details. The appendix was stripped by the PDF parser; it exists in the original submission. Per instructions, missing appendix content should not be penalized. Additionally, the paper explains that the smoothed classifier's computational cost is similar to standard PQC evaluation.

2. **"No comparison with other quantum certified robustness methods"** — While a nice addition, the paper's scope (parameter noise certification for PQCs) is distinct from input-noise or mid-circuit-noise certification methods. The paper cites these prior works (Weber et al., Du et al.) and contextualizes the difference. Demanding comparisons against methods targeting different noise models would be scope creep.

3. **"The robustness-variance correlation analysis is speculative"** — The paper explicitly describes this as an analysis of observed correlations and offers two possible explanations (Section 5.3, lines 225–228). Speculative interpretation of experimental observations is standard practice and not a weakness.

4. **Any formatting, style, or grammar criticisms** — These are parser artifacts, not present in the original submission.

## Novel Insights

The reviews do not produce a genuinely novel insight beyond the paper's own contributions. The key observation — that randomized smoothing for PQC parameter noise can be optimized via standard Evolutionary Strategies with a margin-based objective — is the paper's own core insight and is correctly identified by both reviews.

## Suggestions

1. **Add at least two baselines**: (a) standard (non-robust) PQC training, evaluated under the same Gaussian parameter noise but without retraining, and (b) a test-time-only smoothed classifier derived from a standard-trained model. This will directly demonstrate the method's robustness benefit.
2. **Report certified accuracy**: pick a specific noise level (e.g., σ_noise = 0.01) and report the fraction of test points where the certified radius exceeds ‖δ ⊘ σ‖₂. This makes the practical impact concrete.
3. **Increase dataset size or report multi-run statistics**: if generating more ground states is feasible, use larger training sets. Otherwise, report results over multiple train/test splits with means and standard deviations.
4. **Report the PQC parameter count and architecture details** for the QCNN used, to allow readers to assess whether the 50-sample dataset is adequate.
5. **Temper the language** in the abstract and introduction regarding "provably noise-resilient" claims. The method provides a theoretical guarantee for the smoothed classifier, but the experimental demonstration would benefit from more modest framing or explicit acknowledgment of the evaluation limitations.
