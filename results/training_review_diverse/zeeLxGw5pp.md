Now I have all the information needed to produce the final consolidated review.

## Summary

This paper proposes a VAE-based framework for detecting both out-of-distribution (OoD) inputs and adversarial examples targeting a downstream classifier. The main contributions are: (1) showing that classical VAE with importance sampling achieves OoD detection comparable to a Bayesian VAE with weight uncertainty, (2) dissecting the importance-sampling variance to identify the decoder as the primary source of variation, (3) demonstrating that a single VAE hole-indicator score can detect both OoD and adversarial inputs (both discriminative and generative), and (4) an active-defense algorithm that uses HMC-based latent-code restoration to separate generative adversarial examples from OoD inputs.

## Strengths

- **Classical VAE + importance sampling matches Bayesian VAE for OoD detection**: Tables 1 and 2 show that the standard deviation of importance-sampled log-likelihoods from a single classical VAE yields detection performance nearly identical to that of a full Bayesian VAE (e.g., MNIST vs. FashionMNIST: ROC AUC 0.967 vs. 0.968; AUPRC 0.971 vs. 0.970). This directly supports the claim that Bayesian weight uncertainty is unnecessary for sensitivity-based OoD detection — a clean negative result with practical implications.

- **Adversarial examples from discriminative classifiers are reliably detected by the VAE hole indicator**: Results across FGSM, CW, and JSMA attacks on MNIST, FashionMNIST, and SVHN (Tables 3–5) show consistent detection, with the paper reporting high AUPRC values. This demonstrates that a VAE trained on the same data can serve as a plug-and-play filter without requiring access to the classifier's weights or architecture.

- **The VAE filter also detects attacks on its own encoder**: Table 6 reports successful detection of generative adversarial examples (attacks on the VAE's encoder), validating that a single score (the hole indicator) works for both discriminative and generative threats.

- **Mechanistic insight into the source of detection signal**: Figure 1 and the associated analysis show that the decoder term $\log p(x|z)$ dominates the importance-sampling variance, while the encoder and prior contribute little. This identifies why Bayesian weight uncertainty is unnecessary and directly motivates the hole-indicator score.

- **Honest reporting of the distinction algorithm's limitations**: The paper explicitly states (§4, line 321) that "there is no possibility to delimit outlier and discriminative adversarial attacks relying only on the MSSSIM gain," only generative attacks can be separated. When the conclusion and results are read together, the actual scope is clearer than the abstract suggests.

## Weaknesses

### Fatal

None.

### Major

- **The abstract overclaims the scope of the distinction algorithm**: The abstract states the paper develops methods to "automatically distinguish between them [adversarial examples and OoD inputs]." However, the results (§4) and the conclusion (§6) clarify that the distinction algorithm only separates **generative** adversarial examples from OoD and discriminative attacks. The paper itself acknowledges (line 321) that discriminative adversarial attacks cannot be delimited from OoD using MSSSIM gain. This claim-evidence gap in the abstract inflates the contribution; if read alone, the abstract promises a general adversarial-vs-OoD discriminator that the method does not deliver. This is fixable through careful reframing.

- **No baselines for adversarial detection performance**: The paper compares its OoD detection results to Daxberger & Hernández-Lobato (2019), but provides no experimental comparison with existing adversarial detection methods (e.g., ODIN, Mahalanobis-distance-based detection, or the unified defenses of Lee et al. 2018 and Ahuja et al. 2019 that are cited in the introduction). Without baselines, the reader cannot judge whether the reported detection rates (Tables 3–6) are competitive or weak. For instance, CW attack consistently yields the lowest detection scores — is this a known limitation shared by other methods, or a specific weakness of the proposed filter? The absence of comparative context is the single largest evidential gap in the paper.

### Minor

- **No uncertainty quantification on detection results**: The paper states that doubly stochastic experiments were run 10 times and averaged, but no standard deviations, confidence intervals, or error bars are reported for any metric. Given the stochasticity from both weight sampling and importance sampling, this omission makes it difficult to assess the reliability of the reported numbers.

- **The Lipschitz continuity constraint (§3.2.4) is not ablated**: The paper enforces a predefined Lipschitz constant on the encoder map and claims it improves robustness, but never compares detection performance with and without this constraint. Whether it is essential or incidental remains unclear.

- **"Transferability" is used in a non-standard sense**: The paper defines transferability in §2.2 in the standard adversarial-examples sense (the same perturbation fools different classifiers), but then uses it to describe the phenomenon that adversarial examples from a classifier are **detected** (not misclassified) by a VAE. While the underlying observation is real — adversarial perturbations move inputs off the data manifold in ways detectable by the VAE — calling this "transferability" conflates detection with misclassification and could mislead readers. The paper would benefit from a more precise term (e.g., "cross-model sensitivity").

- **The metrics used for adversarial detection are not explicitly restated**: The paper states metrics (ROC AUC, AUPRC, FPR80) for OoD detection (line 267), but does not clearly confirm that the same metrics apply to the adversarial detection tables (Tables 3–6). The table captions (images) likely clarify this, but the main text should be explicit.

- **HMC-based active defense is described only at a high level**: Algorithm 1 is referenced but appears only in an image (line 172 shows `![](images/...)`) and is not described in algorithmic detail in the text. For a component central to the distinction claim, a pseudocode outline in the main text would improve clarity.

### Trivial

- The conclusion could be more precisely worded to avoid giving the impression that the distinction algorithm works for all adversarial types; it currently reads as accurate on close reading ("distinguishes generative adversarial examples from both outliers and discriminative adversarial attacks") but could be made even clearer.

## Nice-to-Haves

- A comparison of ROC curves for classical vs. Bayesian VAE on the same OoD benchmarks, with confidence bands, would strengthen the paper's core negative result.
- A diagnostic showing how the importance-sampling variance estimates stabilize with increasing sample size (currently 100 samples) would improve trust in the estimator.
- A larger-scale benchmark (e.g., CIFAR-100 or an ImageNet subset) would test generalization beyond the four datasets used, though this is secondary given the paper's scope.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The paper does not include the actual values in the text"** — The table images are present in the original submission; their absence in the parsed text is a parser artifact, not an author omission.
- **"Softmax as k-means clustering" criticism** — This is a cited framing from Hess et al. (2020) used to motivate the work, not a paper claim. Not a weakness.
- **"No adversarial detection metric specified" overstated** — The metrics (ROC AUC, AUPRC, FPR80) are stated for OoD evaluation; the adversarial tables (images) likely contain these headers. The main text could be clearer but this is not an omission as the harsh critic implied.
- **Criticisms about formatting/style** — Parser artifacts, not author errors.
- **Strength Finder's claim about MSSSIM gains "e.g., generative adversarial examples on MNIST produce a mean MSSSIM gain of 0.1656"** — This is specific content from the tables that cannot be verified through the parsed text, but is consistent with the paper's description that generative adversarial examples produce substantially higher MSSSIM gains.

## Novel Insights

The reviews surface a key tension that the paper does not fully resolve: the very mechanism that makes the VAE a good universal detector (adversarial inputs land in latent holes) also prevents it from distinguishing between different types of problematic inputs (discriminative adversarial vs. OoD). The paper's honest reporting of this limitation is a strength, but it also means the claimed "distinction" contribution is narrower than the framing suggests. The observation that the decoder dominates the importance-sampling variance (not the encoder or prior) is the genuinely novel mechanistic insight — it explains *why* Bayesian weight uncertainty is unnecessary and directly connects the hole-indicator literature to the sensitivity-analysis literature. None of the other insights from the reviews go beyond the paper's own contributions.

## Suggestions

1. **Reframe the abstract and conclusion** to match what the experiments actually support: the paper presents a VAE-based *detector* for both OoD and adversarial inputs, plus a limited distinction algorithm that works only for generative adversarial examples. Drop the implication of a general adversarial-vs-OoD discriminator.

2. **Add adversarial detection baselines** — at least one or two competitors (e.g., ODIN, Mahalanobis distance) on the same attack/dataset combinations. Even if the proposed method does not outperform them, the reader needs context to interpret the numbers.

3. **Report standard deviations or confidence intervals** on all main results (OoD detection and adversarial detection) given the stochastic nature of the method.

4. **Ablate the Lipschitz constraint** — show detection rates with and without it to determine whether it is essential.

5. **Replace "transferability"** with a more precise term (e.g., "cross-model sensitivity" or "shared latent vulnerability") when describing the detection of classifier adversarial examples by the VAE.

## Score and Decision

**Originality**: Moderate. The finding that classical VAE matches Bayesian VAE is a useful negative result. The decoder-variance dissection is the most original component.

**Importance of research question**: High. Unified detection of OoD and adversarial inputs is a practically relevant problem.

**Support for claims**: Moderate. The detection results are credible but lack baselines; the distinction claim is overbroad in the abstract.

**Soundness of experiments**: Adequate but incomplete. Missing baselines and uncertainty quantification weaken the evaluation.

**Clarity of writing**: Fair. The paper is readable but has imprecise framing (abstract overclaim, "transferability") and the algorithm description is partially deferred to an image.

**Value to community**: Moderate. The key observation about Bayesian weight uncertainty being unnecessary and the source-of-variation analysis are useful for practitioners building lightweight detection filters.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>