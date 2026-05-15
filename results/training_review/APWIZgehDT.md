Now I have all the information needed to produce the consolidated review.

---

## Summary

This paper presents a three-part paradigm for studying and modulating human perceptual variability using synthetic images generated along ANN decision boundaries. First, it generates ambiguous digit images via uncertainty and controversial guidance (regularized by a diffusion model and a human-judgment surrogate), collects ~117k behavioral trials from 246 participants, and releases the varMNIST dataset. Second, it fine-tunes classifiers with group-level and individual-level human data, showing that the Spearman correlation between model and human perceptual entropy jumps from ρ=0.08 to ρ=0.74 and that IndivNet outperforms GroupNet by ~5% on individual datasets. Third, it uses individually fine-tuned models to generate controversial stimuli for 18 participants (18 pairs), reporting a 3% improvement in success rate and 12% improvement in targeted ratio over varMNIST baselines.

## Strengths

- **Novel two-stage generative pipeline for probing perception**: The combination of ANN boundary sampling (uncertainty/controversial guidance) with a digit-judgment surrogate trained on human responses produces ambiguous stimuli that are both recognizable to humans and evoke high perceptual variability. The ~80% average success+bias rate (Figure 3b) across five classifiers, two strategies, and ten digit pairs provides strong evidence that the pipeline works as designed.

- **Large-scale behavioral dataset and validation**: The varMNIST dataset (19,943 images, 246 participants, 116,715 trials) is a substantial community resource. The individual-level fine-tuning (IndivNet) improves accuracy by ~20% over BaseNet on varMNIST and by an additional ~5% over GroupNet on individual datasets, with 241 of 246 participants showing improvement (Figure 4a). This provides statistically robust evidence that the approach captures meaningful individual differences.

- **Strong alignment between model and human perceptual uncertainty after fine-tuning**: The Spearman correlation between model entropy and human entropy rises from ρ=0.08 (essentially chance) to ρ=0.74 after group fine-tuning (Figure 4c). This is a large effect and demonstrates that fine-tuned models capture not just discrete choices but the *degree* of human perceptual variability — a depth not shown in prior counterfactual approaches.

- **Systematic comparison of architectures and strategies**: The paper evaluates five classifier architectures (VGG, CORNet, VIT, MLP, LRM) and two guidance strategies (uncertainty vs. controversial), showing that CORNet yields the highest success rate in uncertainty guidance and that controversial guidance outperforms uncertainty guidance overall. This provides a useful benchmark for future work.

- **Demonstration that individual fine-tuning primarily benefits high-entropy stimuli**: Figure 4d shows IndivNet's largest accuracy gains over GroupNet occur on high-entropy (most ambiguous) images, revealing that the method captures subtle, case-specific variability that distinguishes individuals — beyond what group-level alignment achieves.

## Weaknesses

### Fatal
None.

### Major

- **The manipulation experiment's "improvement" is measured against an inappropriate baseline.** The paper compares individually tailored stimuli (IndivNet) to the *entire varMNIST dataset* (Section 5.2, Figure 5). But varMNIST is a large generic set of ~20,000 images not designed for the specific participant pairs and digit pairs used in the manipulation experiment. A proper baseline would compare IndivNet-generated stimuli against (a) stimuli generated using the group-level model (GroupNet) for the same pairs and digit targets, or (b) a carefully matched subset of varMNIST controlling for digit pair. Without this controlled comparison, the claimed 3% success rate increase and 12% targeted ratio improvement cannot be attributed to individual fine-tuning specifically — they could reflect any number of confounds (e.g., the IndivNet images being optimized for different digit pairs, the smaller stimulus set reducing noise, or the second-round participants being more familiar with the task). The reported p-values are only meaningful relative to a fair baseline. The paper's argument that the sample size is much smaller (200 vs. 20,000) does not resolve this, because a smaller set can trivially appear better if the larger set includes many low-quality or irrelevant images for the specific pair.

### Minor

- **The generative method is under-specified for reproducibility.** The paper states "we employ a classifier-guided diffusion model for image generation" (Section 3.1) and provides loss functions, but does not specify: which diffusion model architecture (DDPM? score-based? latent?), how the guidance losses are incorporated into the reverse diffusion process (gradient-based sampling at each step? conditioning via classifier logits? a separate optimization loop?), what guidance scale is used, or the number of sampling steps. While classifier-guided diffusion is a standard technique (Dhariwal & Nichol, 2021), the specific combination with the digit-judgment surrogate loss (`L_total = L + max((1-f_surr(x))^2, 0.5)`) and the two guidance strategies requires more procedural detail. This is a practical barrier to reproduction and building on the method.

- **Individual fine-tuning on small per-participant data raises overfitting concerns that are not fully ruled out.** Each participant contributes ~500 trials; after the 80:20 split, ~320 individual-specific trials are used to fine-tune full-classifier architectures (VGG, VIT — millions of parameters). While the paper mixes group data (varMNIST, MNIST) in a 2:1:1 ratio, providing some regularization, the paper does not report early stopping, weight decay, cross-validation, or other safeguards against memorization. The claim that MNIST accuracy does not drop (Figure 4a) is reassuring but does not guarantee that the 5% improvement on varMNIST-i reflects genuine generalization to the individual's perceptual tendencies rather than memorization of ~320 training responses. Bootstrap confidence intervals for the Spearman correlation (ρ=0.08→0.74) would also strengthen the entropy alignment result by showing it is not driven by outliers.

- **Manipulation experiment sample size is modest.** The in-lab manipulation experiment involves 18 participants (18 pairs). While this is typical for human behavioral experiments of this kind, it limits the statistical power and generalizability of the findings. The paper reports p<0.001 but does not state which test was used (e.g., paired permutation test, Wilcoxon) or whether multiple comparisons were adjusted for.

### Trivial

- The loss function design `max((1-f_surr(x))^2, 0.5)` uses a squared penalty and a threshold of 0.5 without ablation or justification for these specific choices. The paper's explanation ("the max function is used so that when the score is above a certain threshold, the gradient of the digit judge will not affect generation") is intuitive but would benefit from a brief rationale for the threshold value.

- The exclusion of participants based on sentinel trials (124/400 in the digit-judgment experiment, 154/400 in the recognition experiment) is mentioned but the specific exclusion criteria are not described. While this is standard practice and the details likely belong in an appendix, a brief note on the exclusion rule would improve transparency.

## Nice-to-Haves

- Comparing ANN boundary sampling against a simpler ambiguity generation method (e.g., linearly interpolating between digit prototypes, adding random noise) would strengthen the case that the ANN boundary correspondence is meaningful rather than incidental. This is not a core flaw — the paper's claim is that this specific pipeline *works*, not that it is superior to all alternatives — but it would elevate the contribution.

- Per-image bootstrap confidence intervals for the Spearman correlation between model and human entropy would increase confidence that the ρ=0.08→0.74 improvement is robust and not driven by a small number of high-entropy outliers.

- Reporting accuracy of the digit-judgment surrogate on a held-out test set would ground its role in the generation pipeline.

## Removed Points

These points were flagged by reviewers but are removed (with brief justification) to avoid misleading evaluation:

1. **"No baseline comparison to show ANN boundary sampling is superior to simpler methods"** — The paper's central claim is that this pipeline *works* (evokes human variability), not that it is superior to all alternatives. The experimental evidence (high entropy, ~80% success+bias rate) sufficiently supports the claim. Demanding a comparison to linear morphs or random perturbations asks the paper to solve a question outside its stated scope.

2. **"Claims are overstated (e.g., 'illuminated key distinctions', 'selectively manipulate')"** — The claim about "key distinctions" is supported by the entropy correlation analysis (ρ=0.08 vs. 0.74). "Selectively manipulate" is supported by the manipulation experiment showing improved guidance directionality. The reviewer's demand for mechanistic explanation is a higher bar than what the paper claims.

3. **"80% threshold for p1+p2 is arbitrary and inflates effectiveness"** — The paper clearly distinguishes success from bias and reports both separately. A threshold requiring summed proportions ≥80% from two out of ten possible digits is reasonably strict for defining successful guidance, not "very loose."

4. **"124/400 participants excluded — this is a weakness"** — Sentinel-trial-based exclusion is standard practice in behavioral research. The exclusion rate (~30%) is not unusual for online experiments where participants may fail attention checks.

5. **"The paper fails to position its novelty precisely"** — The paper explicitly distinguishes itself from Golan et al., Gaziv et al., Veerabadran et al., and Feather et al. (Section 6), noting that its method can influence both models and human perception simultaneously and has broader applicability. Whether one finds this convincing is a matter of judgment, not a factual omission.

6. **Related works criticisms** — Per hard rules, I cannot evaluate missing related works claims.

7. **Formatting/style nitpicks, typos, reproduction complaints about missing appendix content** — Parser-stripped content or trivial presentation issues per hard rules.

## Novel Insights

One genuinely novel observation emerges from synthesis of the two sets of reviews that goes beyond the paper's own claims: the paper's most impressive quantitative result — the Spearman correlation jump from 0.08 to 0.74 — simultaneously serves as the strongest evidence for the approach and the most concerning red flag. A jump this large from a base model that is essentially at-chance (ρ=0.08) to near-ceiling could reflect either a genuine breakthrough in capturing perceptual uncertainty or a methodological artifact (e.g., the entropy computation collapsing on a few highly ambiguous stimuli, or the fine-tuning process overfitting to the specific entropy distribution of the training set). The paper's failure to provide bootstrap confidence intervals or show per-image residuals leaves this question unresolved. Conversely, if this result holds up under scrutiny, it would be a remarkable finding — suggesting that group-level fine-tuning alone accounts for nearly all explainable variance in human perceptual uncertainty, which would substantially reframe how the community thinks about ANN-human alignment.

## Suggestions

1. **For the manipulation experiment**: Add a controlled comparison where IndivNet-generated stimuli are evaluated against GroupNet-generated stimuli for the same participant pairs and same digit targets. This is the only way to separate the effect of individual fine-tuning from the effect of generating new images.

2. **For reproducibility**: Specify the diffusion model architecture, guidance scale, number of sampling steps, and how the loss functions are optimized relative to the reverse diffusion process (gradient-based classifier guidance at each step, or a separate optimization loop).

3. **For overfitting concerns**: Report 5-fold cross-validation results for individual fine-tuning, or at minimum report the held-out validation accuracy per participant alongside the training accuracy, to demonstrate that the improvement is not driven by memorization.

4. **For the entropy correlation**: Provide bootstrapped 95% confidence intervals for the Spearman correlation (ρ=0.08→0.74) to verify the result is not outlier-driven.

5. **Clarify the baseline for the 20% accuracy improvement**: State the absolute accuracy of BaseNet, GroupNet, and IndivNet on varMNIST explicitly (it appears in the figure but the values are not called out in the text).

## Score and Decision

**Overall assessment**: This paper tackles an important problem (inter-individual perceptual variability) with a well-designed three-stage pipeline, produces a substantial behavioral dataset, and shows strong evidence that fine-tuning aligns model and human perceptual uncertainty. The primary methodological contributions — the generative pipeline and the alignment/individual fine-tuning approach — are supported by the experiments. The main liability is the manipulation experiment's baseline comparison, which undermines the strongest claim about "selective manipulation." This is addressable but cannot be fixed in a rebuttal alone — it requires an additional controlled experiment. The paper's first two contributions (generation pipeline and alignment) are solid and would represent a meaningful advance even without the third.

However, because the manipulation experiment is presented as a core contribution (Contribution 3) and its main result relies on a confounded comparison, the paper in its current form overclaims what it demonstrates. A major revision adding the controlled baseline (IndivNet vs. GroupNet) would put the paper in strong shape.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>