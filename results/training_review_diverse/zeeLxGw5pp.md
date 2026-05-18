Now I have all the information needed to cross-verify the reviewer's claims against the paper. Let me write the consolidated review.

## Summary

This paper proposes a VAE-based unified filter for detecting both Out-of-Distribution (OoD) inputs and adversarial examples targeting an image classifier, without requiring access to the classifier's internals. Its main claims are: (1) Bayesian weight uncertainty is not necessary — a classical VAE with importance sampling achieves comparable OoD detection; (2) the decoder's log-likelihood term is the dominant source of detection signal, linking to the "hole indicator"; (3) adversarial examples fall into the same latent holes as OoD inputs; (4) a subset of adversarial examples (encoder/generative attacks) can be distinguished from OoD via HMC-based active defense; (5) the VAE can serve as a plug-and-play filter for any classifier trained on the same data.

## Strengths

- **Disentangling OoD detection from Bayesian weight uncertainty (Tables 1–2).** The paper empirically demonstrates that importance sampling in a classical (non-Bayesian) VAE achieves OoD detection AUC comparable to a Bayesian VAE with weight sampling. This is a useful finding that challenges the prior assumption (Daxberger & Hernández-Lobato, 2019) that Bayesian inference over DNN weights is essential for variance-based OoD detection.

- **Unified detection of OoD and adversarial inputs via a single score (Tables 3–6).** The paper shows that the "hole indicator" (variance of log-likelihood across latent code samples) detects both OoD inputs and adversarial examples (FGSM, CW, JSMA, and encoder attacks) across multiple datasets. The demonstration that discriminative-model adversarial examples are detectable by a generative model trained on the same data (transferability from discriminative to generative representations) is a non-trivial empirical finding.

- **Mechanistic dissection of the importance-sampling variance (Figure 1).** By measuring the standard deviations of the decoder, encoder, and prior terms separately, the paper identifies that the decoder log-likelihood term dominates the variance signal. This provides a concrete explanation for why the hole indicator works and connects an empirical observation (VAE-based OoD detection) to a specific architectural component.

## Weaknesses

### Fatal

None.

### Major

1. **Distinction algorithm is oversold relative to its actual capability.** The abstract states the paper develops methods to "automatically distinguish between" adversarial examples and OoD inputs. However, the paper itself acknowledges (line 321) that "there is no possibility to delimit outlier and discriminative adversarial attacks relying only on the MSSSIM gain." The distinction only works for *generative* (encoder-directed) adversarial attacks. Discriminative adversarial examples (FGSM, CW, JSMA) — the most common and practically relevant type — cannot be distinguished from OoD inputs by the proposed algorithm. The framing in the abstract and introduction suggests a more general solution than what is actually delivered. This gap between promise and delivery is significant.

2. **No baseline comparisons for adversarial detection.** While the paper cites Daxberger & Hernández-Lobato (2019) for OoD detection context, there is no comparison against *any* existing adversarial detection method (e.g., ODIN, Mahalanobis detection, feature squeezing, MagNet, Defense-GAN, or even simple softmax-entropy thresholding). Without baselines, the reported AUC values (Tables 3–6) cannot be evaluated as competitive or not. This is critical because adversarial detection constitutes roughly half of the paper's claimed contribution. The omission makes it impossible to know whether the proposed method improves upon or underperforms existing alternatives.

3. **Plug-and-play claim is unsupported.** The paper asserts the VAE filter can be "plugged into any DNN image classifier of arbitrary architecture trained on the same data inputs without the need for its retraining or accessing the layers and weights" (abstract and Section 6). However, the experiments use a *single* victim classifier architecture (the default from Cleverhans). No experiment varies the classifier architecture, trains independent classifiers on the same data, or tests whether the VAE filter generalizes across them. This claim is therefore an untested assertion, not an empirical result.

### Minor

1. **FGSM with ε=3 on [0,1] inputs is an extreme perturbation.** On pixel values in [0,1], ε=3 saturates all pixels to 0 or 1, effectively destroying the image. While such inputs are still "adversarial" in the sense that they cause misclassification, detection performance under this regime is not informative about realistic attacks. Results under smaller, more standard ε values (e.g., 0.1–0.3) are needed to judge practical utility. The current CW and JSMA results (which use optimized small perturbations) are more meaningful but the paper's strongest results come from FGSM.

2. **Bayesian vs. classical VAE comparison is not fully controlled.** The Bayesian VAE (Table 1) includes BBB layers (variational parameters over weights), while the classical VAE (Table 2) uses the same architecture "without the BBB" (line 258). This conflates two differences: weight sampling vs. fixed weights, and a different model parameterization. A cleaner ablation would use the same BBB-enabled architecture for both conditions and simply switch between sampling weights vs. using their means. That said, the core finding — that the classical VAE works well — is still valid and useful; the comparison issue weakens but does not invalidate the claim.

3. **Limited OoD evaluation scope.** The paper tests only two OoD pairs: MNIST↔FashionMNIST and CIFAR10↔SVHN. Both are relatively easy pairs with visually distinct distributions. No near-OoD benchmarks (e.g., CIFAR10 vs. CIFAR100) or more challenging scenarios are evaluated, which limits confidence in the method's generalizability.

4. **No ablation of Lipschitz continuity enforcement.** The paper claims that Lipschitz control (via GroupSort activations) "further increase[s] robustness" (line 220) but provides no experiment comparing the method with and without this constraint. The reader cannot assess whether this design choice contributes to the reported results or is incidental.

5. **Missing variability estimates.** The paper states experiments were repeated 10 times and averaged (line 260), but no confidence intervals, standard deviations, or standard errors are reported in the main tables. This makes it impossible to assess the statistical significance of differences between methods (e.g., Bayesian vs. classical VAE in Tables 1–2).

### Trivial

- The algorithm description is referenced ("see Algorithm 1," line 216) but the algorithm block was stripped by the parser. If present in the original submission, this is a non-issue.

## Nice-to-Haves

- Including HMC-based distinction results for smaller FGSM perturbations would make the FGSM detection results more practically meaningful.
- Testing the VAE filter with 2–3 different independently-trained classifier architectures would validate (or refute) the plug-and-play claim.
- A dedicated pseudocode block for the distinction algorithm would improve clarity (assuming one does not already exist in the original submission).

## Removed Points

These points from the reviewers are removed per the meta-review guidelines; they are listed here for reference but should not be considered valid criticisms:

- **"Transferability terminology is unconventional/misleading"** — The paper explicitly defines its use of "transferability" (lines 73–76) in the context of discriminative-to-generative transfer. This is a clear, well-scoped use of the term and not misleading.
- **"The higher variance of the decoder term is a natural consequence of dimensionality"** — This criticism misunderstands the measurement. The paper measures variance of log p(x|z) *across different importance-samples z*, not across pixel dimensions. The finding that the decoder term dominates the variance across z-samples is a genuine mechanistic insight, not a dimensionality artifact. However, the related point that the hole indicator is definitionally the same quantity is valid and is addressed above in the analysis.
- **"No comparison with Song et al. 2017"** — This is subsumed by the broader (and valid) criticism about missing adversarial detection baselines; singling out a specific paper is unnecessary.
- **"Algorithm description is scattered in text"** — The paper references "Algorithm 1" (line 216); the algorithm block was likely present in the original submission and stripped by the parser. If it exists, this criticism is moot.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any perspective that the paper itself does not already articulate.

## Suggestions

1. **Adjust the framing of the distinction algorithm.** Clearly state in the abstract and introduction that the HMC-based distinction works only for generative/encoder-directed adversarial attacks, while discriminative adversarial examples and OoD inputs remain conflated under the unified detection score. This would match what the paper actually demonstrates and avoid overclaiming.

2. **Add at least one adversarial detection baseline.** Even a simple comparison (e.g., softmax entropy thresholding, ODIN, or Mahalanobis) would dramatically strengthen the empirical section by contextualizing the reported AUC values.

3. **Validate the plug-and-play claim.** Test the same pre-trained VAE filter with at least one additional independently-trained classifier architecture (different depth, different activation function) on the same dataset.

4. **Add variability measures.** Report standard deviations or error bars for the main results (Tables 1–6) to allow readers to assess whether observed differences are meaningful.

5. **Include results for smaller, realistic FGSM perturbations** (e.g., ε ∈ {0.1, 0.2, 0.3}) and consider near-OoD benchmarks (e.g., CIFAR10 vs. CIFAR100).

## Score and Decision

The paper has several genuine strengths — most notably the demonstration that Bayesian weight uncertainty is not required for VAE-based OoD detection and the finding that adversarial examples occupy similar latent "holes." However, the core contribution is weakened by three major gaps: (1) the distinction algorithm is oversold — it works only for generative adversarial attacks, not the more common discriminative ones; (2) no baselines are provided for the adversarial detection half of the claimed contribution, making it impossible to assess whether the method is competitive; and (3) the central plug-and-play claim is an untested assertion. These gaps collectively make the empirical support too thin to justify the scope of the claims. While the paper presents useful observations, it does not deliver a validated, deployable solution as framed. A major revision with additional experiments and more honest framing could make this a solid contribution.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>