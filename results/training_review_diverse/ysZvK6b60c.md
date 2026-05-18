Now I have a thorough understanding of the paper. Let me write the consolidated review.

---

## Summary

This paper proposes CALoR, a defense against model inversion attacks (MIAs) that combines three components: (1) a confidence adaptation loss that slightly reduces the model's prediction confidence on private samples, biasing the attacker's optimization objective; (2) low-rank compression of the classification head to reduce leaked information; and (3) a Tanh activation function between the compressed layers to induce gradient vanishing. The method is evaluated on FaceScrub and CelebA across multiple architectures (CNNs and Transformers), resolutions (64×64 and 224×224), and seven attack methods (GMI, KED, PPA, LOMMA, PLG, IF, Mirror). Empirical results show substantial reductions in attack accuracy compared to prior defenses (MID, BiDO, LS, TL), especially in high-resolution settings where target models maintain >96% test accuracy.

## Strengths

1. **Joint exploitation of three defense mechanisms with demonstrated synergy.** The paper clearly identifies three weaknesses in the MIA pipeline (attack objective misalignment, MI overfitting, optimization difficulties) and designs explicit components to address each. Ablation studies (Table 4, Table 5, Figure 5) isolate each component's contribution, showing that confidence adaptation alone reduces IF accuracy by 3–4%, low-rank compression at rank 30 limits attack accuracy to 13.0% (vs. 69.2% at rank 512), and Tanh yields the steepest gradient decay. The combined method substantially outperforms any single component.

2. **Strong empirical results in the most challenging scenario — high-utility models.** When target models achieve >96% test accuracy (MS-Celeb-1M pre-training), prior defenses struggle (PLG attack accuracy: 14.0–15.0% for LS/BiDO vs. 16.8% undefended), while CALoR drops PLG accuracy to 4.3% and IF accuracy from 22.1% to 13.6%, with feature distances 1.5–2× larger (Table 3). This addresses a real gap where existing defenses degrade under high model utility.

3. **Comprehensive evaluation across diverse settings.** Experiments span two datasets (FaceScrub, CelebA), multiple resolutions (64×64, 224×224), CNN and Transformer backbones (IR-152, ResNet-152, Swin-v2, ViT-B/16, FaceNet-112, MaxViT), seven attack methods (GMI, KED, Mirror, PPA, LOMMA, PLG, IF), and both unconditional/conditional GAN paradigms. This breadth supports generalization claims.

4. **Low-rank compression is shown to be a particularly simple and effective defense mechanism.** The ablation on rank dimension (Table 5) convincingly shows that low dimensionality of the classifier head maintains model utility while sharply reducing attack success — a finding with practical value independent of the other components.

## Weaknesses

### Fatal
None.

### Major

1. **Undisclosed attack hyperparameter tuning (or lack thereof).** The paper reports dramatic drops in attack accuracy (e.g., IF dropping from 75.5% to 35.3% on low-resolution FaceScrub, Table 1) while stating only that they "carefully adjust the hyperparameters governing the defense strength" (line 177) — i.e., defense hyperparameters, not *attack* hyperparameters. It is never stated whether the attack methods (learning rates, number of optimization steps, GAN prior loss weights, classification loss variants) were tuned per defended model or used a single configuration across all defenses. MIAs have multiple tuning knobs, and a defense that changes the output landscape can make default attack settings suboptimal without genuinely increasing hardness. This is the most consequential omission because the paper's central claim depends on these numbers being a fair comparison. The authors should explicitly state, for each attack method, which hyperparameters were used and whether they were adapted per defense.

2. **Absence of adaptive attacker evaluation.** The paper frames its defense as targeting three "inherent weaknesses" of MIAs and claims to be "comprehensive." However, it evaluates only standard, non-adapted attack methods. An attacker who knows the defense strategy could adapt in several plausible ways: (a) against confidence adaptation — use a soft target derived from model predictions on auxiliary data rather than the one-hot vector, or increase the prior loss weight; (b) against Tanh gradient vanishing — use higher-order optimizers or a surrogate loss (e.g., softmax-free cosine loss) that is less affected by vanishing gradients; (c) against low-rank compression — train a separate proxy model that approximates the original high-rank behavior, or use multiple random initializations to search the inversion space more broadly. Without adaptive attack experiments (even a limited set), the claim of "comprehensive" defense remains unsubstantiated against a knowledgeable adversary. This gap is especially acute given the paper's explicit claim to target weaknesses that an adaptive attacker could try to circumvent.

### Minor

1. **Overclaimed novelty of the "first comprehensive analysis."** The paper states it is "the first to conduct comprehensive analyses of weaknesses inherent in MIAs" (line 29). However, the three identified weaknesses have been individually discussed in prior work: the attack objective / prediction-confidence properties are central to label smoothing defenses (LS, 2024); MI overfitting is discussed at length in LOMMA (2024), which the paper itself cites; and optimization difficulties (non-convexity, gradient vanishing) are well-documented in PPA (2022) and PLG (2023). What is genuinely novel is the *combination* of the three weaknesses as an organizational lens and the corresponding three-pronged defense — but the paper would benefit from moderating the "first comprehensive analysis" claim and instead emphasizing the engineering insight that combining these specific techniques works well.

2. **Motivational evidence in Figure 2 is correlational, not causal.** The paper shows that models with lower average confidence on private images yield lower attack accuracy and uses this as evidence that confidence reduction strengthens defenses (lines 126–127). However, this correlation could be driven by a third factor (e.g., models that produce low confidence may simply have less useful internal representations). The paper uses this as motivation rather than proof, which is reasonable, but the phrasing "demonstrate that lower confidence brings more challenging to MIAs" (line 127) slightly overstates the strength of the evidence. A causal demonstration (e.g., intervening on confidence via label smoothing at varying strengths while controlling for model quality) would strengthen the motivation.

3. **Missing explicit hyperparameter values and sensitivity analysis in the main text.** The confidence adaptation loss has two hyperparameters *a* and *b* (line 134) that control the strength of confidence reduction. The main text defines their role and notes the equilibrium confidence value (exp(-1/b)), but does not state the specific values used in the main experiments or discuss their sensitivity. The ablation study (Table 4, mentioned in the appendix) apparently covers some of this, but the main paper should at minimum report the chosen values and give a sense of stability — especially important since the method requires a two-stage training procedure.

### Trivial

1. **Terminology imprecision.** The paper refers to compressing the classifier head's feature dimension as "low-rank compression" and calls the bottleneck dimension "the rank of the classifier head" (line 208). While mathematically defensible (a d×30 linear layer has rank at most 30), this terminology may confuse readers who expect a matrix-rank regularization method (e.g., nuclear norm minimization). Clarifying that this is a bottleneck architecture would help.

## Nice-to-Haves

- **Compare to a simple capacity-reduction baseline.** The low-rank compression component is essentially a bottleneck that limits model capacity. A controlled comparison against simply reducing the width of a standard fully-connected layer (same dimensionality, no bottleneck structure) would clarify whether the bottleneck structure itself matters or just the reduced dimensionality.
- **Attack accuracy vs. optimization steps.** Showing attack accuracy as a function of the number of optimization steps (or learning rate) would reveal whether CALoR genuinely prevents convergence or merely slows it down — an important distinction for practical security.
- **Visualization of the optimization landscape.** For the confidence adaptation component, visualizing the attacker's loss landscape with and without defense (e.g., via 1D/2D slices of the loss surface) would strengthen the claim that the defense biases the attacker's objective.
- **Explicit statement of computational cost.** The two-stage fine-tuning procedure (CE pre-training + CA fine-tuning) is not expensive, but a brief note on training time overhead would be helpful for practitioners.

## Removed Points

These points were raised by reviewers but are removed or downgraded per the review guidelines:

- **"Missing parentheses in confidence adaptation loss derivation"** — This is a PDF parsing artifact, not an author error. Removed.
- **"Low-rank compression term is misleading"** — The term "low-rank" is standard in deep learning for bottleneck architectures (the linear layer matrix literally has low rank). Kept as a Trivial terminology clarification rather than a genuine weakness.
- **Several generic strength entries from Strength Finder** — Removed generic/superficial strengths (e.g., "addresses an important problem") that lack specific content or conflict with verified weaknesses.
- **"Correlation is not causation" as a Major weakness** — Downgraded to Minor because the paper uses it only as motivation (lines 126–128), not as a rigorous proof. The phrasing is slightly overconfident but not a structural flaw.

## Novel Insights

The review reveals that the paper's most underappreciated insight is the observation that **low-rank compression of the classifier head provides a near-free privacy benefit**: it maintains test accuracy while drastically reducing the information available for inversion attacks. The ablation (Table 5) suggests that at rank ~30, the model retains sufficient discriminative power while the attacker's search space is effectively collapsed — a finding that is both practically useful and theoretically interesting. The synergy with Tanh (which adds a second, orthogonal barrier via gradient decay) and confidence adaptation (which shifts the optimization target) makes the combination greater than the sum of its parts. However, the core weakness revealed by cross-referencing the reviews is that the paper's empirical claims are only as strong as the transparency of its attack evaluation protocol — and on this dimension the paper is currently opaque.

## Suggestions

1. **Mandatory: Disclose attack hyperparameters for each defense.** For each MIA method (GMI, KED, PPA, LOMMA, PLG, IF), provide a table showing the learning rate, number of optimization steps, loss weights, and any GAN prior settings used. State explicitly whether these were tuned per defense, and if so, on what validation criterion (e.g., attack accuracy on a held-out subset).
2. **High priority: Add at least one adaptive attack experiment.** The most informative adaptive attack would be: an attacker who replaces the classification loss with a softmax-free alternative (e.g., cosine-based loss) to mitigate Tanh gradient vanishing, or uses a proxy model trained without low-rank compression to bypass the bottleneck. Even a limited set of adaptive attacks would substantially strengthen the "comprehensive" claim.
3. **Moderate the novelty claims.** Replace "first comprehensive analysis" with language emphasizing the novel *combination* of weaknesses exploited and the specific design of the three-pronged defense.
4. **Report hyperparameter values *a* and *b* used in the main experiments**, and provide a brief sensitivity note (e.g., "varying *b* from 2 to 10 changed attack accuracy by at most 3%").
5. **Clarify the bottleneck terminology** by explicitly noting that the low-rank header is a linear layer with small output dimension, rather than a regularization enforcing matrix rank.

## Score and Decision

This paper presents a solid engineering contribution to MIA defense with strong empirical results across diverse settings. The combination of three techniques is novel and the ablation studies convincingly show that each component contributes. However, two major issues — undisclosed attack tuning and the absence of adaptive attack evaluation — prevent full acceptance of the paper's central claims in their current form. The overclaimed novelty of the "comprehensive analysis" is a secondary concern. The paper is on the right track and could be accepted with major revisions that address the attack transparency issue.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>