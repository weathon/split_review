Now I have all the information needed. Let me construct the final consolidated review.

---

## Summary

This paper introduces NARCISSUS, an unsupervised anomaly detection method built on the insight that models trained on a mix of normal and sparse anomalous data converge on normal data first. The method uses a tailored "Very Early Stopping" (VES) scheme with a robust ensemble variant (RVES) to halt training precisely when normal data has been fit but anomalous data has not, turning any semi-supervised model into an unsupervised one. Evaluations are conducted primarily on multivariate time series (6 datasets, 7 base models), with additional experiments on images (MVTec2D, MNIST) and graphs (UCI Message, Digg).

---

## Strengths

- **Novel and practically useful insight.** The observation that models converge on normal data before anomalous data when trained on mixed unlabeled data is clearly motivated, empirically supported (Figure 1), and leveraged in a principled way. This is the paper's most original contribution.

- **Extensive time-series evaluation.** Across 6 multivariate time-series datasets and 7 base semi-supervised models (TranAD, GDN, NPSR, LSTM-NDT, OmniAnomaly, USAD, MTAD-GAT), NARCISSUS consistently matches or approaches the F1 scores of the same models trained on clean normal data (differences within 0.02 in most cases). On SMAP with GDN, it even outperforms the semi-supervised version (F1 0.93 vs. 0.86). The breadth of this evaluation (42 data points) is the paper's strongest evidence.

- **VES + RVES design is well-motivated and ablated.** The ablation (Figure 3, Tables 6–7, Appendix) convincingly shows that (a) pure bootstrapping (randomly sampling training data) is highly unstable (F1 ranging 0.43–0.97 on MBA), (b) VES alone substantially improves stability, and (c) RVES (the ensemble variant) further reduces worst-case degradation. This step-by-step validation supports the design choices.

- **Model-agnostic framework demonstrated across 10 architectures.** NARCISSUS is applied to fundamentally different model types — reconstruction-based (TranAD, PatchCore), prediction-based (GDN, NPSR), generation-based (AnoGAN), and graph-based (AddGraph) — supporting the claim that the early-convergence phenomenon is not model-specific.

---

## Weaknesses

### Fatal
None.

### Major

**1. Theorem 4.2 does not provide a rigorous theoretical foundation for the method, despite being presented as a core contribution.**  
The theorem states that if $N_n \cdot \delta_n \gg N_a \cdot \delta_a$ (cumulative gradient magnitude from normal data dominates anomalous data), then SGD converges toward fitting normal data with a bounded difference from anomaly-free training. The "proof" merely observes that under this condition, parameter updates are dominated by normal data. The claimed bound on the difference from anomaly-free training is asserted without derivation — the proof simply invokes "convergence properties of SGD with bounded noise" without making the argument concrete.  

More critically, the paper does not empirically verify that the condition $N_n \cdot \delta_n \gg N_a \cdot \delta_a$ actually holds in practice for the tested anomaly detection problems. The paper argues it follows from sparsity ($N_n/N_a$ large) and well-bounded data ($\delta_a$ not exceeding $\delta_n$ by orders of magnitude). But in reconstruction/prediction-based AD, anomalous points can produce very large losses (and therefore large gradients) early in training, potentially violating the condition. The paper provides no gradient measurements to confirm the condition.  

The theorem is presented as a theoretical centerpiece (in a section titled "Stochastic Gradient Descent Learns to Fit Normal Data First"), but it functions as a restatement of the method's intuition rather than a testable or verifiable theoretical guarantee. This is a structural issue: the paper claims a theoretical foundation that does not bear scrutiny.

**2. Main empirical results lack variance estimates, which is critical for a method whose central selling point is robustness.**  
Tables 1 and 2 report only point estimates (precision, AUC, F1) without standard deviations, confidence intervals, or any measure of variability across independent runs. This is a significant evidential gap because:

- NARCISSUS involves multiple sources of randomness (random validation subset selection in each VES run, multiple training runs in the RVES ensemble, random initialization).
- The ablation (Figure 3) shows that the alternative approach (bootstrapping) produces F1 scores ranging from 0.43 to 0.97 — a massive spread. The paper argues NARCISSUS is more robust, but without reporting NARCISSUS's own variance across independent runs, the reader cannot assess whether the claimed superiority over bootstrapping is statistically meaningful.
- The phrase "differences in F1 score are within 0.02" is based on point estimates with no associated uncertainty. A difference of 0.02 could be within the noise of the method.

This is the most consequential weakness because it directly undermines the paper's central claim about achieving semi-supervised-level accuracy reliably.

### Minor

**3. VES convergence criterion is under-specified for reproducibility.**  
Algorithm 1 states that "conventional early stopping is applied" on the intersection of filtered validation subsets, but does not specify the exact metric being monitored, the patience threshold, the delta for improvement, or any early-stopping hyperparameters. The statement "empirically we can choose a large $\eta$" provides no practical guidance. Since VES is the core algorithmic contribution, the early-stopping criterion needs to be fully specified.

**4. Generalization beyond time series is not convincingly demonstrated.**  
For images, only one dataset per method is used (MVTec2D for PatchCore, MNIST for AnoGAN). For graphs, two small datasets (UCI Message, Digg) are tested. No comparison to unsupervised methods designed specifically for images/graphs (e.g., DeepSVDD, f-AnoGAN, OC-GNN) is provided. The paper acknowledges this limitation in the Discussion, but the claim of "domain-agnostic applicability" is not well-supported by the evidence presented.

**5. Self-supervised methods are excluded from comparison with a reasonable but limiting rationale.**  
The paper states that self-supervised methods "would need a method like NARCISSUS as a module" and are thus excluded. This is a defensible design choice, but it means the comparison is against a restricted set of baselines. The paper would benefit from at least one self-supervised baseline (e.g., the cited Zhang et al., 2023) to calibrate NARCISSUS's relative performance against the full landscape of unsupervised AD approaches.

### Trivial

- Equation (2) notation: "$p(x \in \mathbb{U} | \mathcal{L}(x) > \sigma) < \epsilon$" mixes a set membership with a conditional probability in a way that lacks a well-defined probability space. This does not affect the method but is mathematically imprecise.

---

## Nice-to-Haves

- **Gradient norm measurements.** Rather than a non-rigorous theorem, the paper would be strengthened by empirically measuring cumulative gradient contributions from normal vs. anomalous data across training epochs for several datasets, showing that the condition $N_n \cdot g_n \gg N_a \cdot g_a$ (with actual gradient magnitudes) holds.
- **Additional unsupervised baselines for time series** (e.g., Isolation Forest, LOF, DeepSVDD adapted for time series) would broaden the comparison scope.
- **Computational cost analysis.** The paper claims "comparable computational overhead" but provides no runtime or epoch-count comparisons. A brief table showing training wall-clock time for NARCISSUS vs. standard semi-supervised training vs. bootstrapping would be informative.
- **Sensitivity to RVES ensemble size.** The ablation does not characterize how performance varies with the number of VES repeats.
- **Discussion of limitations with long-term dependencies.** The paper assumes data is "well-bounded." For time series with trends or seasonality, normal points far from the current model's predictions may also produce large gradients, potentially causing misclassification.

---

## Removed Points

These points were flagged by reviewers but are removed for the following reasons (treat with caution if referenced elsewhere):

1. **Strength: "Theorem 4.2 derives a precise condition and provides a theoretical foundation."** — Conflicts with the verified weakness that the theorem is not rigorous and does not provide meaningful theoretical support. Moved here per the conflict rule (weakness wins).

2. **Strength: "Demonstrated generalization to image and graph anomaly detection."** — Conflicts with the verified weakness that generalization is not convincingly demonstrated due to limited scope. Moved here per the conflict rule.

3. **Criticism: "Not applicable to anomaly detection" claim (after Theorem 4.2) is unsubstantiated.** — The paper references Theorem A.2 in the appendix for this claim. Since the appendix was stripped by the parser, this criticism cannot be verified and is removed per the rule on missing appendix content.

4. **Notation error: "$\sum_{y\in\mathbb{N}}$" should be "$\sum_{y\in\mathbb{Y}}$".** — Minor typographical/notation issue. Removed per the rule on typos and formatting nits.

5. **Missing related works (InterFusion, DeepSVDD for time series, etc.)** — Removed per the rule that missing related works should not be mentioned, as external sources cannot confirm their existence in the context.

---

## Novel Insights

None beyond the paper's own contributions.

---

## Suggestions

1. **Report variance across multiple independent runs of the full NARCISSUS pipeline** (different random seeds, validation splits, retraining). Provide confidence intervals or error bars for F1, AUC, and precision in Tables 1 and 2. This single addition would address the most significant weakness.

2. **Clarify the VES convergence criterion.** Specify the exact metric monitored on the intersection of filtered subsets, the patience value, the improvement delta, and how $\eta$ is set in practice. This is necessary for reproducibility.

3. **Either strengthen Theorem 4.2 or reposition it as intuition.** The theorem as presented is not a rigorous result and gives a false sense of theoretical grounding. Either provide a proper bound on the difference from anomaly-free training (non-trivial), or move the current content to the Discussion/Intuition section and replace it with empirical gradient measurements.

4. **Expand image/graph experiments** to at least one additional dataset per modality to strengthen the generalization claim, or explicitly scope the contribution to time series.

---

## Score and Decision

**Originality:** High — the early-training-dynamics insight for unsupervised AD is novel.  
**Importance of research question:** High — achieving semi-supervised-level accuracy without labels is practically important.  
**Claims supported:** Moderate — time-series results are extensive but missing variance estimates; cross-modal generalization claims are weakly supported.  
**Soundness of experiments:** Moderate — good range of baselines and datasets, but the lack of variance estimates is a significant gap for a robustness-oriented method.  
**Clarity of writing:** Good — the paper is well-structured and the core idea is clearly communicated.  
**Value to community:** Moderate — the method is practical and model-agnostic, but the current evidential standard is below what is needed to trust the claimed robustness.

The paper identifies a genuinely interesting phenomenon and proposes a pragmatic framework to exploit it. The time-series experiments, though lacking variance estimates, suggest the method has real potential. However, the gap between the claimed robustness and the evidence provided (no variance estimates, non-rigorous theory, weakly supported modality generalization) is too large for acceptance at this stage.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>