Now I have all the information needed to write the final consolidated review.

## Summary

This paper investigates weak-to-strong boosting for vision models, where a weaker (lower-accuracy) model supervises a stronger (higher-capacity or higher-potential) model. The authors propose AdaptConf, an adaptive confidence distillation loss that dynamically weights between the weak teacher's soft labels and the strong student's self-generated hard labels on a per-sample basis using a confidence signal. Experiments across image classification (CIFAR-100, ImageNet), few-shot learning, transfer learning, and noisy-label learning show consistent improvements over prior KD methods and the AugConf baseline (Burns et al., 2023).

## Strengths

- **Consistent empirical advantage across diverse settings.** AdaptConf outperforms both traditional KD methods and the AugConf baseline on nearly every evaluated teacher-student pair, including same-architecture (Table 2), different-architecture (Table 4), and ImageNet (Table 3) settings. Improvements of 0.5–2% absolute accuracy are reported, and these hold across 3-trial averages.

- **Substantial gains when ground-truth labels are absent.** In the "only weak teacher soft labels" scenario (Table 4b), AugConf and AdaptConf achieve much larger improvements than other KD methods. This directly supports the paper's core thesis — that weak supervision alone can effectively boost a stronger model, even without true labels.

- **Robustness to hyperparameter variation.** The ablation study (Figure 2) shows that AdaptConf's accuracy fluctuates less across temperature settings than AugConf's accuracy fluctuates across α values, indicating the adaptive formulation is more stable and easier to use in practice.

- **Strong performance under noisy labels.** On CIFAR-100 with asymmetric label noise (Table 8), AdaptConf improves top-1 accuracy by +0.81% over the scratch baseline, while other KD methods often degrade performance. This demonstrates resilience to imperfect supervision.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **The design of β(x) uses hard labels for confidence estimation while the loss uses soft labels, a choice that is not justified or analyzed.** In Eq. (2), β(x) = exp(CE(f(x), ˆf(x))) / (exp(CE(f(x), ˆf(x))) + exp(CE(f(x), ˆf_w(x)))) uses cross-entropy with *hard* labels from both models, while the first loss term uses the weak model's *soft* labels. The paper states this measures "confidence" but does not explain why hard-label CE is preferred over soft-label divergence for this purpose, nor what the behavioral implications of this choice are. An ablation comparing the current β formulation to one using soft-label KL divergence would clarify the design rationale. This does not invalidate the empirical results but limits the paper's methodological clarity.

- **Some experiments use same-architecture teacher-student pairs, which departs from the paper's framing of leveraging "smaller, weaker models."** Table 2 pairs e.g., ResNet56→ResNet56 and WRN-40-2→WRN-40-2, where the teacher is weaker only in accuracy, not capacity. While this is a valid weak-to-strong setup in the "born-again" sense (Furlanello et al., 2018) and the paper does include genuinely weak-to-strong different-architecture pairs (Table 4), the paper would benefit from explicitly separating these two settings and clarifying which claims apply to each.

- **No statistical significance or confidence intervals reported.** The reported gains (e.g., +0.33% on ImageNet with an 83.5% baseline) are modest in absolute terms. While improvements at high accuracy levels are meaningful, the lack of variance estimates makes it difficult to assess whether the improvements are robust across runs beyond the reported 3-trial averages.

- **The comparison in Figure 2 compares α (AugConf) to temperature T (AdaptConf), which are not directly analogous controls.** AugConf's α directly weights the two loss terms, while temperature affects softmax sharpness rather than the weighting per se. While the result still demonstrates that AdaptConf is more robust, a cleaner ablation would vary β's formulation directly.

### Trivial
None.

## Nice-to-Haves
- A controlled ablation comparing AdaptConf to AdaptConf with β fixed to the average learned value (per setting) would more directly isolate the benefit of per-sample adaptivity.
- A dedicated table of genuinely weak-to-strong pairs (e.g., ResNet-18 → ResNet-101) with a clear accuracy gap is suggested to strengthen the paper's core claim.

## Removed Points
These points are flagged to be removed; treat them with caution.

1. *"No ablation isolates the contribution of adaptivity"* — The reviewer claimed no comparison to a fixed-weight version of the same two-term loss exists. However, AugConf IS exactly that: L = (1-α)CE(f, f_w) + αCE(f, ˆf) with a fixed global α. The comparison to AugConf across all tables directly tests the benefit of per-sample adaptivity. The reviewer overlooked this.

2. *"If only soft labels are available, the hard label version is not"* — The reviewer claimed an inconsistency between the "only soft labels" scenario and the method's need for ˆf_w(x). However, hard labels are trivially derived from soft labels via argmax. This is not a real issue.

3. *"On CIFAR-10, AdaptConf does not improve either"* — The paper states "all methods except ours negatively impact the model." Avoiding degradation when all other methods hurt performance IS a positive robustness result, not a failure to improve.

4. *Pure formatting/style nitpicks* about table placeholders, parser artifacts, and similar presentation issues that stem from PDF extraction, not the original submission.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. Provide a clear justification for the hard-label CE formulation of β(x) in Eq. (2), or ablate against a soft-label version.
2. Add significance measures (confidence intervals or std deviations across trials) for main results, especially the +0.33% ImageNet gain.
3. Explicitly delineate same-architecture vs. different-architecture results and discuss how each setting supports or qualifies the weak-to-strong claim.
4. Include at least one experiment with a clearly weaker teacher (e.g., >10% accuracy gap) to more directly demonstrate the method's value in the strict weak-to-strong regime.

## Score and Decision

**Anchor comparisons (all from calibration corpus):**

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| `/home/.../FwkYeLovHk.md` | 3.33 | Weak-to-strong CLIP paper — much weaker; tested only on DomainNet, simpler method. Current paper is significantly stronger. |
| `/home/.../pHe4P1IVnb.md` | 5.50 | Bayesian WeakS-to-Strong for NLP — similar quality; comparable methodological depth, broader task scope. Current paper has broader vision experiments. |
| `/home/.../OZitfSXpdT.md` | 6.50 | TGeo-KD for adaptive fusion ratios — stronger theoretical motivation and cleaner ablations. Current paper is less theoretically grounded. |
| `/home/.../m50eKHCttz.md` | 7.25 | Knowledge transfer across 400+ models — far more comprehensive. Current paper is substantially weaker in scale. |
| `/home/.../yV6wwEbtkR.md` | 6.67 | Bayes CMI for KD — strong theory-motivated method. Current paper is less rigorous theoretically. |
| `/home/.../QKqWnNkwPL.md` | 3.00 | Self-distillation for diffusion — weak experimental results. Current paper is stronger. |
| `/home/.../8TbqoP3Rjg.md` | 2.00 | KD to mitigate model collapse — poor presentation, weak experiments. Current paper is much stronger. |

Relative to these anchors, the paper sits slightly below the 5.50 WeakS-to-Strong paper (which has cleaner ablations and methodological justification) and well below the 6.50+ papers (which have more theoretical depth or experimental scale). It is clearly above the 3.33 and below papers, which have fundamental issues with their core claims or experimental support.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept</decision>