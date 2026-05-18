Now I have all the information needed. Let me produce the final consolidated review.

---

## Summary

This paper proposes a standardized framework for measuring "bias shifts" — changes in attribute prevalence between training data and generated images — in unconditional image generative models. Applying this framework to diffusion models and BigGAN on CelebA and DeepFashion, the key finding is that attributes fall into two categories based on classifier decision boundary density: *subjective* (high boundary density) attributes exhibit large bias shifts, while *non-subjective* (low boundary density) attributes show small shifts. The paper further demonstrates that conventional image quality metrics (FID, KID, FLD) do not correlate with bias shifts, and that large diffusion models show smaller bias shifts than BigGAN or small diffusion models.

## Strengths

- **Reference-free bias shift metric.** By defining bias shift as |P_cls^gen(C=1) − P_cls^val(C=1)|, the metric cancels out any ideal reference distribution. This makes the analysis applicable regardless of which fairness standard one might choose, cleanly isolating changes induced by the generative model (Section 3.2, Eq. 3).

- **Standardized framework isolating inductive bias.** The pipeline trains a classifier on the same dataset as the generative model, then uses it to label training/validation and generated images consistently. This avoids introducing external biases from pre-trained models and enables a principled study of inductive bias effects (Section 3.2, Figure 2).

- **Discovery of subjective/non-subjective attribute taxonomy with mechanistic explanation.** The paper identifies that attributes with high bias shifts are precisely those where the classifier's decision boundary lies in a high-density region, while low-bias-shift attributes have boundaries in low-density regions (Figures 5–6, Table 1). The explanation — that density mass is harder to transport across a low-density boundary — connects the empirical pattern to a concrete mechanism, which is the paper's most interesting contribution.

- **Demonstration that quality metrics and bias shifts are independent.** The paper shows that FID, KID, and FLD continue to improve during training while bias shifts plateau or increase (comparison of Figures 3 and 4). This is a clear, practically important finding: bias cannot be inferred from generation quality and must be evaluated separately.

- **Systematic comparison across model types.** The comparison of large/small diffusion models with BigGAN (Figure 7) shows that architecture and capacity affect bias shifts beyond what traditional metrics capture, with large diffusion models exhibiting substantially lower bias shifts. This provides actionable guidance for model selection.

## Weaknesses

### Fatal

None.

### Major

- **The central finding is potentially confounded with classifier behavior, and the paper does not validate that the pipeline measures generative model shifts rather than classifier sensitivity.** The bias shift metric and the attribute taxonomy (subjective vs. non-subjective) both depend on the same classifier's pre-sigmoid logits. The observed pattern — larger bias shifts for attributes with dense-boundary classifiers — could partly or entirely reflect that the classifier is differentially sensitive to distribution shifts across attributes, rather than the generative model differentially shifting attribute prevalence. Specifically, for a given distribution shift (e.g., blurrier generated images), samples near a dense boundary are more likely to cross it, inflating the measured shift for subjective attributes regardless of the generative model's actual attribute-level behavior. The paper acknowledges classifier errors (lines 71–72) and uses consistent labeling, but it does not perform a synthetic shift experiment (e.g., artificially subsampling an attribute in the training set and checking whether the pipeline recovers the known shift) or validate classifier predictions on generated images via human evaluation. Without such validation, the paper's core empirical claim — that generative models shift attribute prevalence more for subjective attributes — rests on an untested assumption. This is the most significant weakness in the paper and limits the strength of the conclusions.

### Minor

- **Single-run comparisons for BigGAN with no uncertainty quantification.** The comparison between BigGAN and diffusion models (Figure 7) is based on a single training run for BigGAN. The paper acknowledges run-to-run variability for diffusion models (Figure 8 shows 3 seeds), but no such quantification is provided for BigGAN, making it unclear whether the observed difference is statistically robust. Given that GAN training is known to be seed-sensitive, this weakens the comparative claim.

- **Framing oversells relevance to deployed text-to-image systems.** The introduction motivates the work with biases in DALL-E, Stable Diffusion, and Midjourney (line 10), but the experiments are restricted to unconditional pixel-level models trained from scratch on CelebA and DeepFashion. The paper acknowledges this limitation (lines 19–20), but the framing throughout — particularly the use of "bias" language and fairness-motivated examples — implies broader relevance than the evidence supports. The work is better positioned as a study of distribution shift in unconditional generative models rather than a "bias analysis" with direct implications for practical fairness.

- **Conditional bias experiments (Section 4.6, Figure 10) receive minimal analysis.** The finding that conditioning on a subjective attribute (Old) increases bias shifts even for non-subjective attributes is intriguing but is only briefly discussed. The paper itself flags that this may be due to classifier error, which again underscores the main confound concern. A deeper analysis would strengthen the paper.

- **No quantitative correlation between bias shifts and image quality metrics.** The paper claims these are independent based on visual comparison of trends over training (Figures 3 vs. 4), but does not compute correlation coefficients or rank correlations. A simple quantitative check would make the claim more precise.

- **The explanation for why small diffusion models show increasing bias shifts at later training steps is vague.** The paper attributes this to "more washed out" images (line 218) without analysis or evidence. Given that this is one of the paper's four main observations, a more concrete explanation would be valuable.

### Trivial

- The code and model checkpoints are not released, which hinders reproducibility. (This is standard to note for a full paper; the contribution remains understandable without them.)

## Nice-to-Haves

- **Synthetic shift validation:** Artificially subsample an attribute in the training set to create a known prevalence shift, re-run the classifier, and verify that the bias shift metric recovers the induced shift. This would directly address the main confound concern.
- **Per-attribute classifier accuracy on the validation set** (likely in the appendix, which was stripped by the parser) should be prominently discussed to help readers assess the confound.
- **Multiple seeds for BigGAN** and confidence intervals for the model comparison in Figure 7.
- **Human evaluation on a sample of generated images** to verify that classifier predictions are equally reliable across attribute types.

## Removed Points

- *Criticism about using P_cls^val vs. P_cls^train without verifying representativeness* — The paper explicitly addresses this choice (line 71: "as the classifier may overfit to the training set"). The concern is already dealt with.
- *Complaint that per-attribute classifier accuracy is missing* — The paper references an appendix ("2 show in detail the classifier performance for each attribute") that was stripped by the parser. It exists in the original submission.
- *Criticism that the confound is "almost tautological"* — This overstates the issue. The paper's finding (dense-boundary attributes show larger measured shifts) is an empirical observation about the interaction between distribution shifts and classifier boundaries, not a logical necessity. The weakness stands, but the dismissal as tautological is inaccurate.
- *Demand for confidence intervals from probabilistic classifiers or bootstrap sampling* — This is a nice-to-have but not standard practice for this type of large-scale generative model evaluation, where a single run with 10K generated samples is the norm.

## Novel Insights

The reviewer's confound argument, while valid, actually highlights something useful: the paper's framework and the confound are two sides of the same coin. If the observed effect were entirely a classifier artifact, the finding would still be valuable — it would mean that any bias evaluation pipeline using classifiers is systematically more reliable for non-subjective attributes and inherently noisier for subjective ones. This is itself a methodological insight that practitioners need to know. The paper's value does not collapse if the confound is real; it merely needs to be reframed as a finding about the measurement system (classifier + generative model) rather than about the generative model in isolation.

## Suggestions

1. **Add a synthetic shift validation experiment** (subsample an attribute, re-label with the classifier, check if the metric recovers the induced shift). This is the single most impactful addition and directly addresses the main weakness.
2. **Run BigGAN with at least 3 seeds** and report mean ± std in Figure 7.
3. **Compute rank correlations** between bias shifts and FID/KID/FLD across checkpoints to quantify the claimed independence.
4. **Reframe the paper's scope** in the introduction and conclusion to more precisely describe what it studies: the measurement of attribute prevalence shifts in unconditional generative models, not "bias" in the social fairness sense. The technical content supports the former; the latter framing invites expectations the paper does not meet.

## Score and Decision

The paper proposes a thoughtful framework and contributes genuinely interesting empirical observations — particularly the boundary-density taxonomy and the dissociation from traditional quality metrics. However, the central finding is undermined by an unresolved confound between the measurement tool (classifier) and the measured quantity (bias shift), and the paper's most consequential comparative claim (BigGAN vs. diffusion models) lacks statistical support. With targeted validation this could be a strong paper, but in its current form the conclusions outrun the evidence.

**Score:** 5.5

**Decision:** Reject

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>