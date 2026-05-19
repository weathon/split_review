- Decision: Accept
- Avg Score: 6.20
- Scores: 5, 8, 6, 6, 6
Now I have all the information I need. Let me construct the final consolidated review.

---

## Summary

This paper introduces Learning from Randomness (LFR), a self-supervised representation learning method that replaces domain-specific augmentations with the task of predicting random neural-network projections of the input. The method encodes data into representations that support simple predictors to match outputs of multiple randomly initialized projector networks, using a batch-wise Barlow Twins (BBT) loss and a DPP-based diversity selection mechanism. LFR is evaluated across time series, tabular, and medical image domains, and shows competitive or state-of-the-art results among self-supervised methods on most datasets.

## Strengths

- **Novel augmentation-free pretext task.** The core idea — learning representations by predicting random data projections rather than enforcing invariance under hand-crafted augmentations — is a genuinely different mechanism from invariance-based, masking-based, and reconstruction-based SSRL. Section 3 formalizes the approach as an MLE lower bound (Eqs. 2–3), and the method applies to any data modality without modification.
- **Consistently strong empirical results across diverse modalities.** In Table 1, LFR achieves the best self-supervised result on 5 of 7 datasets spanning time series (HAR: 93.1, Epilepsy: 97.9), tabular data (Income: 85.2, Theorem: 51.6), and medical images (Kvasir: 74.9). It outperforms domain-specific methods like TS-TCC on time series and SCARF/STab on tabular data, demonstrating the practical value of the approach.
- **Clear and well-motivated problem framing.** Section 1 and Figure 1 vividly illustrate concrete failure modes of standard augmentations (e.g., color-jittered histopathology producing unsafe images, physical constraints violated by tabular augmentations). This makes the case for an augmentation-free method compelling.
- **Thoughtful design for projector diversity.** The DPP-based projector selection (Section 3.3) is a principled way to avoid redundant projectors without gradient computation. The ablation in Figure 3 confirms that diversity encouragement at both initialization and selection improves downstream accuracy.

## Weaknesses

### Fatal

None.

### Major

- **Missing ablation of the divergence measure (loss function).** The paper introduces three novel components simultaneously: (a) random projection targets, (b) the batch-wise Barlow Twins (BBT) loss, and (c) DPP-based diversity selection. Yet the ablation study (Section 4.5) only examines the number of projectors, batch size, predictor training steps, and embedding dimension — it never varies the loss function. Section 3.2 briefly argues that MSE, CE, and contrastive losses have deficiencies, but no experiment supports this claim. A reader cannot tell whether LFR's success comes from the random-projection concept itself, the specific BBT loss, or an interaction between them. This is the most significant evidential gap, as it directly affects attribution of the paper's central contribution.

- **The advantage over a simple autoencoder is modest on several datasets, and this is not adequately analyzed.** The autoencoder is the most natural domain-agnostic reconstruction-based baseline. On HEPMASS, LFR (90.1) is worse than the autoencoder (90.7). On Income, LFR (85.2) is within 0.2 of the autoencoder (85.0). On MIMIC-III, the gap is 46.6 vs. 44.9 — modest. The paper discusses autoencoder limitations in Section 2 (low-level reconstruction), but does not connect this critique to the experimental results to explain why the margins are small on some datasets and large on others. Without this analysis, it is unclear in which settings LFR should be preferred over a simpler, faster autoencoder.

### Minor

- **Ablation studies and diversity analysis are performed on a single dataset (Kvasir).** The paper acknowledges this limitation (Section 4.5: "While we have observed similar trends in other datasets, the significance may vary"), but hyperparameter choices and conclusions about DPP selection drawn from one dataset may not transfer. A second dataset would substantially strengthen generality claims.

- **No statistical significance or confidence intervals for small performance gaps.** Several comparisons involve margins under 1–2% (e.g., LFR vs. autoencoder on Income, LFR vs. TS-TCC on Epilepsy). Without significance testing or effect-size discussion, it is unclear whether these differences are meaningful beyond random variation.

- **The instability motivating the EM-style alternating training is asserted but not demonstrated.** Section 3 states that joint training "showed fluctuating progress which prevented the model from converging to satisfactory solutions" (line 88), but no convergence plots, loss curves, or qualitative examples are provided. This makes the EM design choice appear unmotivated.

- **The rationale for using batch-wise (rather than feature-wise) decorrelation in the BBT loss is not explained.** The paper adapts the Barlow Twins loss from the feature dimension (as originally proposed) to the batch dimension (Eq. 4), but does not provide intuition for why decorrelating across instances' predictions is beneficial when matching random projector outputs. The original Barlow Twins reduces feature redundancy; it is not obvious that the same principle transfers to the batch setting.

- **No runtime or computational cost comparison.** The method requires K random projectors, K predictor networks, DPP pre-processing, and alternating training. The paper provides no wall-clock time, FLOPs, or parameter-count comparison to baselines (especially the autoencoder). If LFR is substantially slower for marginal gains, this is practically relevant.

- **The MLE lower-bound derivation (Eqs. 2–3) motivates optimizing the objective but does not specifically justify random projections over other targets (e.g., input reconstruction, fixed random noise).** The argument that "downstream tasks could include arbitrary data projections" is reasonable but the formal connection between the MLE bound and the preference for random projections over input reconstruction is not made concrete.

### Trivial

None.

## Nice-to-Haves

- Compare against a baseline using a randomly initialized, frozen target network (similar to BYOL/SimSiam with a fixed random target) to isolate the effect of learning to predict random projections vs. the full BBT + DPP setup.
- Validate DPP-based projector diversity on a held-out batch to confirm that the selected projectors remain diverse across the dataset.
- Show probing-task or representation-visualization analyses to illustrate whether LFR learns more abstract features than the autoencoder, as the paper's motivation suggests.

## Removed Points

*The following points were evaluated and found to not be valid weaknesses of the paper or to be unsupported by the text. They are included for transparency.*

- "The paper does not discuss the known failure mode of autoencoders — prioritizing low-level reconstruction." **Removed: factually incorrect.** The paper explicitly states this at line 50: "these methods tend to prioritize low-level reconstruction over capturing high-level abstractions required for downstream tasks."
- "The paper fails to discuss prior work that uses random projections for representation learning (e.g., 'Representation Learning with Random Background'/'RandomViT')." **Removed: cannot verify existence of cited works, and the instructions prohibit criticizing missing related works without external verification.**
- "SimCLR and SimSiam baselines using image augmentations are unfair comparisons / serve as weak baselines." **Removed: the paper transparently acknowledges this limitation (Section 4.1, Table 1 caption) and includes these methods for completeness. The asymmetry favors the baseline, not the proposed method.**
- "The conclusion undercuts the earlier 'outperforms state-of-the-art' framing." **Removed: the conclusion's qualification ("for general applications... contrastive-learning-based SSRL is still likely to outperform") is appropriately honest about scope and does not contradict the evidence showing LFR outperforms SSRL baselines on most tested datasets.**
- "The paper should compare to the autoencoder more rigorously with reconstruction visualizations." **Moved to Nice-to-Haves: this would strengthen the paper but is not a core weakness.**

## Novel Insights

The harsh critic's framing that the crucial question is "why random projections rather than input reconstruction?" points to an analysis that the paper itself does not fully provide. The strongest insight from synthesizing the reviews is that the paper's contribution may be more precisely stated as: *random projection targets, when combined with the BBT loss and diversity selection, produce an effective domain-agnostic pretext task* — but the individual contribution of each component remains unclear. The strength finder correctly identifies that the paper's key empirical claim is supported on its own terms (best SSRL method on 5/7 datasets), but the harsh critic rightly notes that the paper would be significantly stronger by isolating the role of random projections from the BBT loss. The tension between the two reviews reveals that the paper's weakest link is not the overall results but the attribution of those results to the specific novelty claimed.

## Suggestions

1. **Run a loss-function ablation on at least two datasets** — replace the BBT loss with MSE and with a standard contrastive loss, keeping all other components fixed. This is the single most important experiment to add, as it determines whether the core idea (random projections) or the specific loss drives performance.
2. **Add a dedicated discussion of the autoencoder comparison.** Explain the pattern: on which datasets does LFR clearly outperform the autoencoder, and on which does it not? Connect this to the paper's hypothesis about random projections avoiding low-level feature capture.
3. **Provide significance tests** (e.g., bootstrap or paired t-test) for the key comparisons where margins are <2%, or at minimum discuss effect sizes and variability.
4. **Add one convergence plot** comparing joint training vs. alternating training to justify the EM approach.
5. **Add a brief intuitive explanation** for why batch-dimension decorrelation is sensible for this setup.
