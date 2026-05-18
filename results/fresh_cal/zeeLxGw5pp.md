Now I have a thorough understanding of the paper. Let me produce the consolidated review.

## Summary

The paper proposes a unified VAE-based framework for detecting both out-of-distribution (OoD) inputs and adversarial examples. Its core contributions are: (1) showing that a classical VAE using importance sampling achieves OoD detection performance comparable to a Bayesian VAE (contradicting prior claims that Bayesian weight inference was necessary); (2) decomposing the marginal likelihood to show the decoder term accounts for nearly all the variation distinguishing inliers from outliers; (3) demonstrating that adversarial examples transfer from discriminative classifiers to the VAE and are detectable by the same hole-indicator score; and (4) proposing an active-defense algorithm (HMC + MSSSIM) to distinguish generative adversarial attacks from OoD inputs.

---

## Strengths

1. **Classical VAE equals Bayesian VAE for OoD detection via sensitivity.** Tables 1 and 2 show nearly identical AUPRC and ROC-AUC scores between the Bayesian VAE (weight uncertainty) and classical VAE (importance sampling only). This directly contradicts the claim in Daxberger & Hernández-Lobato (2019) that Bayesian weight inference is required, and is the paper's central empirical finding (lines 273–278).

2. **Decomposition pinpoints the decoder as the source of variation.** Section 3.3.1 and Figure 1 break the importance-sampled log-likelihood into decoder, encoder, and prior terms, and show that the decoder term \(\log p(\mathbf{x}|\mathbf{z})\) drives nearly all the variance distinguishing inliers from outliers. This provides a principled explanation for why the hole-indicator score works and connects the method to latent-hole detection in a well-founded way.

3. **Transferability of adversarial examples from discriminative to generative models.** Tables 3–5 report that adversarial examples crafted against a classifier (FGSM, CW, JSMA) are detected by the unsupervised VAE with high AUPRC (often approaching 1.00) across MNIST, FashionMNIST, and SVHN. This supports the claim that the VAE can serve as a model-agnostic filter without accessing the classifier's internals.

4. **VAE robustness to direct encoder attacks.** Table 6 shows that the hole indicator detects generative adversarial examples (targeting the VAE encoder itself) with AUPRC of 1.00 on MNIST and FashionMNIST and 0.89 on SVHN, demonstrating the VAE's own defense under Lipschitz-constrained training.

5. **Latent-space visualization of attack strength.** Figure 2 shows that as FGSM perturbation magnitude increases, the adversarial latent code drifts farther from the nearest cluster centroid, with weak attacks resembling near-OoD and strong attacks resembling far-OoD. This provides interpretable geometric evidence for the paper's claims about the relationship between attack strength and latent-space position.

---

## Weaknesses

### Fatal
None.

### Major

- **Gap between "defense" framing and detection-only evaluation.** The abstract and conclusion state that the VAE serves to "defend[] the DNN classifier against potential attacks" and "protect[] the DNN classifier." Yet all experiments report only detection metrics (ROC-AUC, AUPRC, FPR80) and MSSSIM values — there is no end-to-end experiment where the VAE filter is actually placed in front of a classifier and the classifier's accuracy on clean data, adversarial examples, and OoD inputs is measured with and without the filter. The detection metrics are a reasonable prerequisite for defense, but the paper overstates its conclusions by claiming "defense" without demonstrating the effect on classifier accuracy or quantifying the clean-data false rejection trade-off (abstract line 4, conclusion lines 340–341). Toned-down framing ("detection framework" rather than "defense") would better match the evidence.

### Minor

- **Distinction between OoD and discriminative adversarial examples is not achieved.** The paper's active-defense algorithm (Section 3.2.3, Tables 7–8) can distinguish generative adversarial examples from OoD inputs, but the paper explicitly acknowledges at line 321 that "there is no possibility to delimit outlier and discriminative adversarial attacks relying only on the MSSSIM gain." This is a clearly stated limitation, but the abstract's phrasing ("develop separate methods to automatically distinguish between them") is overly broad and could mislead readers into thinking the distinction algorithm applies to all attack types. The conclusion (line 340) is properly specific about *generative* adversarial examples, so the gap is limited to the abstract's framing.

- **No ablation study of Lipschitz continuity enforcement.** Section 3.2.4 introduces Lipschitz continuity constraints on the encoder to improve robustness, and the experiments state (line 258) that these constraints are applied where the hole indicator is used. However, there is no comparison of detection performance with and without this enforcement. The claim that it "further increase[s] robustness" (line 220) is therefore not directly supported by any presented data, reducing confidence in the design rationale.

- **Statistical uncertainty not reported despite multiple runs.** The paper states at line 260 that experiments were run "10 times each and averaged," but no standard deviations, confidence intervals, or error bars are reported in any table or figure. This makes it impossible to assess the stability of the reported AUPRC/ROC-AUC values, especially since they are the main evidence for the paper's core claims.

- **Limited comparison baselines.** For OoD detection, the paper compares only to Daxberger & Hernández-Lobato (2019), which is appropriate for the specific claim about Bayesian vs. classical VAE. However, the paper also motivates itself relative to prior unified OoD+adversarial approaches (Lee et al., 2018; Ahuja et al., 2019; cited at line 14) but does not experimentally compare against them. For adversarial detection, no baselines are provided at all. Additional comparisons would ground the claims of effectiveness more firmly.

### Trivial

- The MSSSIM gain values in Tables 7–8 are reported without clear indication of whether the differences between discriminative adversarial examples and OoD inputs are statistically meaningful (the paper states they are not distinguishable, but the raw numbers could be presented more clearly).

---

## Nice-to-Haves

- An end-to-end experiment plugging the VAE filter into a classifier and reporting clean accuracy, robust accuracy under attack, and the clean-data false-positive rate would directly validate the "defense" framing the paper currently claims.
- An ablation study isolating the effect of Lipschitz continuity on detection performance would justify its inclusion.
- Reporting standard deviations for all tables (since 10 runs were conducted) would strengthen reproducibility.

---

## Removed Points

These points from the reviewers are flagged for removal, treated with caution:

- **"No end-to-end defense experiment is fatal"** — downgraded to Major (see above). The paper demonstrates detection capability convincingly; a defense evaluation would strengthen but does not invalidate the core contribution.
- **"Algorithm 1 is missing from the main text"** — removed per instruction: the appendix (containing Algorithm 1) was stripped by the parser; it exists in the original submission.
- **"Not tested on more challenging datasets (CIFAR-100, Tiny ImageNet, near-OoD)"** — generic request for expanded scope; the paper already evaluates on MNIST, FashionMNIST, SVHN, and CIFAR-10, which is standard coverage.
- **"Comparison to ODIN, Mahalanobis, Energy-based methods"** — these are discriminative OoD detection methods outside the paper's VAE-focused scope; the paper's comparison to Daxberger (a VAE-based method) is the relevant baseline for its central claim.
- **Section-by-section presentation notes** (softmax/k-means framing not used, novelty relative to prior work unclear) — subjective observations without concrete errors.
- **"Metric 'Accuracy' is ambiguously labeled in Tables 3–5"** — the tables are embedded images; the text at line 285 states detection is based on the hole indicator, so the metric is detection accuracy.

---

## Novel Insights

None beyond the paper's own contributions.

---

## Suggestions

1. Tone down the "defense" framing to "detection" throughout the abstract and conclusion, or add an end-to-end experiment that measures classifier accuracy with the VAE filter in place.
2. Add an ablation table showing detection performance with and without Lipschitz continuity enforcement.
3. Report standard deviations alongside the averaged metrics in all tables.
4. Add a simple experimental comparison to at least one of the prior unified methods cited (Lee et al., 2018; Ahuja et al., 2019) to ground the claim of modularity advantage.
5. Clarify in the abstract that the OoD-vs.-adversarial distinction algorithm applies only to generative adversarial examples.

---

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>