I have all the information needed. Let me now compose the final consolidated review.

## Summary

The paper proposes a unified VAE-based framework for detecting both Out-of-Distribution (OoD) inputs and adversarial examples using a single pre-trained generative model that can serve as a modular filter for any DNN classifier. The core contributions are: (1) demonstrating that a classical VAE with importance sampling achieves OoD detection comparable to a Bayesian VAE, showing that Bayesian weight uncertainty is unnecessary; (2) dissecting the marginal likelihood to identify the decoder term as the primary source of the variance that distinguishes inliers from outliers, establishing a link to the hole-indicator score; and (3) showing that adversarial examples transfer from discriminative classifiers to the generative VAE model (landing in latent holes), enabling their detection via the same hole-indicator score. The paper also proposes an active-defense algorithm (HMC + MSSSIM) that can distinguish generative adversarial attacks from OoD inputs, though this distinction does not extend to discriminative adversarial examples.

## Strengths

1. **Classical VAE matches Bayesian VAE for OoD detection**: The paper empirically demonstrates that importance-sampling-based variance scores from a single classical VAE achieve OoD detection performance comparable to a full Bayesian VAE (Tables 1 vs 2). This directly challenges the prevailing assumption that Bayesian weight uncertainty is required for sensitivity-based OoD detection, and it is a practically useful finding since classical VAEs are simpler to train and deploy.

2. **Decoder sensitivity identified as the primary source of variation**: The component-wise analysis in Section 3.3.1 (Figure 1) convincingly shows that the decoder log-likelihood term log p(x|z) dominates the variance that separates inliers from outliers, while the encoder and prior terms contribute negligibly. This dissection explains why latent-code sampling (the hole indicator) works as well as weight sampling, and it is the paper's most technically interesting and well-supported finding.

3. **Adversarial examples transfer from discriminative to generative models and are detectable**: The hole indicator detects discriminative adversarial examples (FGSM, CW, JSMA) across MNIST, FashionMNIST, and SVHN with ROC AUC values above 0.84, reaching 0.999 for FGSM on MNIST (Tables 3–5). This confirms a non-trivial transferability property and enables a practical detection mechanism that requires no access to the classifier's weights or architecture.

4. **Plug-and-play modularity**: The VAE filter is trained independently on the input data distribution and can be inserted before any DNN classifier of arbitrary architecture without retraining or accessing the classifier's internals. This is a practical advantage over methods that are class-conditional or require modification of the classifier itself.

5. **Comprehensive evaluation across multiple datasets and attack types**: Experiments span four datasets (MNIST, FashionMNIST, SVHN, CIFAR10) as in-distribution/OoD pairs, three discriminative attack types (FGSM, CW, JSMA), and generative encoder attacks, with positive results throughout.

## Weaknesses

### Fatal

None.

### Major

1. **Abstract overclaims the ability to distinguish adversarial from OoD inputs; the distinction algorithm only partially works.** The abstract states that the paper develops "separate methods to automatically distinguish between them" (adversarial vs. OoD). In practice, the algorithm using HMC + MSSSIM gain can only separate *generative* adversarial attacks (attacks on the VAE encoder) from OoD inputs. The paper itself acknowledges on line 321 that "there is no possibility to delimit outlier and discriminative adversarial attacks relying only on the MSSSIM gain." Since discriminative attacks (FGSM, CW, JSMA) are the practically relevant threat model, the distinction claim in the abstract is misleading. The conclusion (line 340) rephrases this more honestly as "distinguishes generative adversarial examples from both outliers and discriminative adversarial attacks," but the overall narrative still over-emphasizes the distinction capability. This does not invalidate the paper's core detection results, but the framing needs honest rescoping. *(Note: if read as "distinguish [which type of attack is occurring]" the claim is only partially supported for generative attacks; if read as "detect both types" the detection claim is supported, but the abstract and introduction clearly foreground the distinction goal.)*

2. **No baseline comparisons for adversarial detection.** The paper reports ROC AUC, AUPRC, and FPR80 for detecting adversarial examples (Tables 3–5), but does not compare against any existing adversarial detection methods such as MagNet, PixelDefend, feature squeezing, or other VAE-based defenses. Without baselines, it is unclear whether the proposed approach is competitive, or whether detection is trivially easy for these datasets/attacks. For OoD detection, the paper does reference Daxberger & Hernández-Lobato (2019) as a state-of-the-art comparison, but the adversarial detection results lack this context entirely.

### Minor

1. **No ablation of the Lipschitz constraint on the encoder.** Section 3.2.4 introduces a Lipschitz constraint (via GroupSort activation) on the encoder map, described as needed "to further increase robustness." The Lipschitz constraint is used in experiments with the hole indicator (line 258), but there is no controlled experiment comparing detection performance with and without it. Given that the paper's headline finding is that importance-sampling variance suffices for detection, it is unclear whether the Lipschitz constraint is necessary, helpful, or neutral. An ablation would clarify this.

2. **The active-defense algorithm is an incremental contribution over Kuzina et al. (2024).** The paper adopts the HMC-based latent code reevaluation approach from Kuzina et al. (2024) and adds MSSSIM gain for distinguishing attack types. However, this addition only works for generative attacks, and the paper never makes a compelling case for *why* distinguishing attack type from OoD matters in practice — if the VAE is a gatekeeper, the natural response to both is to block the input. The practical motivation for the distinction algorithm is underdeveloped.

3. **Transferability is asserted but not analyzed.** The paper reports that discriminative adversarial examples land in VAE latent holes (Tables 3–5) and calls this "especially remarkable," but offers only a brief speculation ("similarity of internal representation within DNNs," line 303). A deeper analysis — e.g., does this hold across deeper architectures, varying attack strengths, or different victim classifier families? — would substantially strengthen the paper's main detection claim.

4. **No specification of the thresholding procedure.** The paper does not describe how the decision boundary for the hole indicator or variance score is set. Is it dataset-dependent? Fixed? Determined by a validation set? This is needed for reproducibility.

5. **No discussion of computational cost.** The active-defense algorithm requires running HMC for every input flagged by the hole indicator. If the VAE is intended as a real-time filter, the overhead of HMC sampling per input could be prohibitive. The paper should at least acknowledge this limitation.

6. **The paper's organization interleaves methodology and analysis.** Section 3 mixes multiple ideas (weight uncertainty, importance sampling, hole indicator, disentangling variation, Lipschitz constraints, latent representation analysis) in a way that makes it hard to track which method is used in which experiment. For example, the important "disentangling variation" analysis (Section 3.3) appears between the Lipschitz discussion and the latent representation analysis, rather than being consolidated with the experimental evaluation.

### Trivial

None.

## Nice-to-Haves

- A deeper investigation into *why* adversarial examples from discriminative models transfer to the VAE's latent space. The paper could test this across different victim classifier architectures, attack strengths, and datasets.
- Release of code and model checkpoints would strengthen the empirical contribution and enable reproduction.
- An ablation study comparing detection with and without Lipschitz constraints would clarify whether this design choice is necessary.
- A discussion of failure cases: for which types of inputs does the hole indicator fail, and why?

## Removed Points

- **"Core OoD detection result requires trusting absent quantitative data"**: The tables (1–8) are present as embedded images in the PDF but stripped by the parser. The text references specific comparisons (e.g., "comparable with the state-of-the-art," line 273). Per the hard rules, parser artifacts are not paper errors; this criticism is removed.
- **"No error bars or confidence intervals"**: The paper states experiments were run 10 times and averaged (line 260). Whether error bars appear in the tables cannot be determined from the parser-stripped text. This concern is removed as it may stem from the parser artifact.
- **"Code and models not mentioned as available"**: The paper does not mention code release, but this is a common practice in academic papers and not a weakness per se. Moved to Nice-to-Haves.
- **Strength Finder's strength #4 ("Active defense distinguishes generative adversarial examples from OoD inputs")**: This is retained — it correctly describes what the paper achieves and does not conflict with Weakness #1, which notes the algorithm *fails* for discriminative attacks. No conflict.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Reframe the paper's contributions honestly.** The abstract and introduction should state that the distinction algorithm works for generative (encoder) attacks, while discriminative adversarial examples and OoD inputs cannot be distinguished from each other using this method. The paper's strongest contribution — that a single classical VAE detects both OoD and adversarial inputs using the same hole indicator — should be the narrative centerpiece.

2. **Add baseline comparisons for adversarial detection.** Compare against at least one established method (e.g., MagNet, PixelDefend, or a simple feature-squeezing baseline) to contextualize the reported ROC AUC values.

3. **Add an ablation removing the Lipschitz constraint** to show whether it is necessary for the reported detection performance. If it is unnecessary, simplify the method; if it helps, quantify by how much.

4. **Specify the threshold selection procedure** for the hole indicator and variance scores. Even a brief description (e.g., "the threshold is set on a held-out validation set to maximize the F1 score") would significantly improve reproducibility.

5. **Restructure the paper** to consolidate the methodology (Bayesian VAE → classical VAE → hole indicator → Lipschitz) in a clear flow before the experimental evaluation, and move the "disentangling variation" analysis into the experimental results section where it belongs.

## Score and Decision

Originality: The finding that Bayesian weight uncertainty is unnecessary for sensitivity-based detection, and the decoder dissection, are genuinely novel contributions that clarify an open question in the literature. However, the active-defense component is largely adopted from prior work with an incremental addition.

Importance: The problem — a unified defense against both OoD and adversarial inputs — is important and practically relevant. A modular, plug-and-play VAE filter has clear practical value.

Claims support: The core detection claims are supported by the presented results (assuming the embedded tables contain the described numbers). However, the distinction claim is overstated relative to what is actually demonstrated.

Soundness: The experimental methodology (10 runs, multiple datasets, multiple attacks) is reasonable. The missing adversarial detection baselines and the absent Lipschitz ablation weaken the evaluation.

Clarity: The paper is generally readable but could benefit from a clearer structure separating methodology from analysis.

Value: The paper provides a practically useful empirical finding (classical VAE suffices, decoder drives the variance) and a working detection pipeline. With honest reframing and additional baselines/ablations, it would be a solid contribution.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>