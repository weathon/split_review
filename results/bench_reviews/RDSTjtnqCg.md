## Summary
The paper analyzes ASH by separating its pruning and scaling components, argues that pruning can hurt while scaling improves OOD detection, and proposes SCALE as a post-hoc activation-scaling method. It further proposes ISH, a training-time fine-tuning method that uses the same activation-derived scale factor to emphasize samples with stronger “ID-ness.” The core idea is simple and empirically promising, but several central claims are overstated, especially the claimed mathematical guarantee of unchanged ID accuracy and the theoretical link from activation mass to energy-based OOD separation.

## Strengths
- **Simple and concrete decomposition of ASH into pruning vs. scaling.** Section 3.2 explicitly separates ASH’s pruning and scaling components, and Fig. 3(b) reports a useful diagnostic: stand-alone scaling improves AUROC up to about \(p=0.85\), while stand-alone pruning decreases AUROC. This is a meaningful empirical insight rather than just a new heuristic.
- **SCALE is operationally simple and attractive as a post-hoc method.** The method requires no retraining, no architecture modification, and only computes a sample-dependent statistic \(Q/Q_p\) from penultimate activations before scaling all features.
- **The empirical results are encouraging on standard OOD benchmarks.** Table 1 shows SCALE improving over ASH-S on ImageNet-1K/OpenOOD v1.5, especially near-OOD AUROC/FPR@95: 81.36/59.76 versus ASH-S 79.63/62.03. Table 2 also reports improvements over ASH-S on CIFAR-10 and CIFAR-100 with DenseNet-101.
- **The paper includes a useful ordinary fine-tuning baseline for ISH.** Table 4 includes both “TorchVision Model” and “TorchVision Model Extended” with SCALE, which partially contextualizes how much of ISH’s gain comes from simply fine-tuning longer.

## Weaknesses

### Fatal
None.

### Major
- **The claimed “no ID accuracy trade-off” / argmax-preservation guarantee for SCALE is mathematically false as stated.** The paper defines logits as \(\logit = W F + b\), and SCALE computes \(\logit' = W(cF)+b = cWF+b\). This is not a positive scalar multiple of the original logits \(WF+b\) unless the classifier bias is absent, shared across classes, or scaled consistently. Therefore, scaling all activations equally does **not** generally preserve logit ordering. This directly contradicts the paper’s statement that “the \(\arg\max\) is not affected and there is no trade-off for ID accuracy.” The empirical ImageNet result in Table 1 shows no ID accuracy drop in that setting, but the claimed guarantee is not valid.
- **The theoretical explanation does not rigorously justify the claimed OOD mechanism.** Proposition 1 concerns ratios of unweighted activation mass, \(Q_p/Q\), under rectified-Gaussian assumptions. The paper then asserts that pruning or scaling transfers to logits and energy scores, but the classifier weights are signed and class-dependent, biases are present, and the energy score is nonlinear in all logits. A larger unweighted activation sum or a larger scalar \(Q/Q_p\) does not by itself imply a larger ID-vs-OOD energy separation. The analysis is useful as intuition, but it should not be presented as establishing the mechanism.
- **The state-of-the-art claims are stronger than the evidence supports.** SCALE is competitive and improves over listed baselines, but the ImageNet evidence is on a single architecture, ResNet-50, and the far-OOD improvement over ASH-S is extremely small: AUROC 96.47 to 96.53 and FPR@95 16.86 to 16.53. The CIFAR results use a single DenseNet-101 setting and report aggregate metrics. Without per-dataset breakdowns or variance estimates, the paper supports “competitive and often better in these reported settings,” but not a broad or robust SOTA claim.
- **The ISH contribution is not cleanly isolated from fine-tuning and hyperparameter choices.** Table 4 includes a helpful extended-fine-tuning baseline, but ISH also uses selected training choices such as a smaller weight decay, and these are not ablated. Moreover, the strongest comparisons mix training methods and postprocessors: LogitNorm uses MSP, CIDER uses KNN, while ISH is evaluated with SCALE. Thus, the paper does not fully establish that the gains come from ISH’s backward activation shaping rather than SCALE plus ordinary fine-tuning and favorable training choices.

### Minor
- **The paper should report how often SCALE changes ID predictions.** Because the argmax guarantee fails with classifier biases, the relevant empirical question is not only final ID accuracy but also the rate of prediction changes and whether changed predictions are correct or incorrect.
- **The percentile-selection protocol is under-specified for CIFAR.** The ImageNet section states that OpenOOD v1.5 uses a dedicated OOD validation set and that \(p=0.85\) is validated, but the CIFAR hyperparameter-selection procedure is not clearly described. Since SCALE is sensitive to \(p\), this affects interpretability of the CIFAR results.
- **The paper reports mostly aggregate near/far or aggregate CIFAR results.** Per-dataset results would help determine whether SCALE consistently improves OOD detection or whether improvements are driven by a subset of OOD datasets.
- **The notation around the scaling factor is confusing.** The method defines \(r=Q/Q_p\) but applies \(\exp(r)\), while later text sometimes refers to \(r\) itself as the scale factor. Since \(Q/Q_p \ge 1\), the distinction between \(r\) and \(\exp(r)\) matters for numerical behavior and for interpreting the method.
- **The “ID-ness” interpretation for ISH is under-analyzed.** All training samples are ID by construction, so it is unclear whether high \(Q/Q_p\) samples are more prototypical, easier, more confident, less diverse, class-biased, or simply higher-norm. This matters because ISH effectively reweights training gradients.

### Trivial
None.

## Nice-to-Haves
- Compare SCALE against simple scalar-score baselines using \(Q/Q_p\), feature norm, activation sparsity, logit norm, or combinations of these with energy. This would clarify whether the benefit comes from feature scaling specifically or from injecting a sample-dependent magnitude statistic into the OOD score.
- Include histograms of energy scores before and after SCALE, not only scale-factor histograms, to show how ID/OOD separation changes.
- Add sensitivity analysis over classifier bias magnitude or evaluate bias-free final classifiers to directly test the theoretical limitation of the argmax claim.
- For ISH, compare against matched fine-tuning baselines with the same optimizer, learning-rate schedule, weight decay, epochs, and postprocessor.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **Bias vector dimension typo.** The harsh review noted that the bias is written as \(\mathbb{R}^D\) instead of \(\mathbb{R}^K\). This appears to be a notation/typing issue and should not be weighted as a substantive weakness. The substantive issue is the presence of a bias term in the classifier, not the dimension typo.
- **Generic related-work complaints.** Comments that the paper should discuss additional related works or that the related-work section is incomplete are removed, since missing related works cannot be verified here and should not be manufactured.
- **Formatting or parser artifacts.** Any comments about broken table formatting, stray braces, line breaks, or awkward extracted text are removed as PDF-extraction artifacts.
- **Overly broad criticism that post-hoc methods can sometimes preserve ID accuracy.** This is directionally true but too generic. The important, paper-specific issue is that SCALE’s claimed argmax guarantee is invalid with a biased classifier.
- **Strength Finder claim that the Gaussian assumption is well validated.** The paper does report chi-square p-values and activation statistics, but this support is weak for high-dimensional rectified, correlated activations and does not establish the later energy-score conclusions. I therefore do not count this as a strong, central strength.
- **Computational-cost nitpicks about “0.1x” or “one-third” training effort.** The paper’s epoch accounting is somewhat simplified, but the main table does make clear that ISH uses 10 additional epochs versus 30 for some methods and 180 total for AugMix. This is not a core flaw compared with the lack of controlled ISH ablations.

## Novel Insights
The most important synthesis is that the paper’s empirical idea is stronger than its mathematical framing. SCALE may work because the activation-derived scalar \(Q/Q_p\) is a useful sample-dependent statistic correlated with ID/OOD status, but the paper over-interprets this as an order-preserving feature transformation and as a theoretically justified energy-gap amplifier. Reframing SCALE as a simple empirical energy-score enhancer, rather than a guaranteed ID-preserving mechanism, would make the contribution much more defensible.

## Suggestions
- Replace the claimed ID-accuracy guarantee with an empirical statement, or modify the method so that the entire logit vector, including bias handling, is scaled in an actually order-preserving way.
- Add an explicit derivation or counterexample discussion for biased classifiers, and report the fraction of samples whose predicted class changes under SCALE.
- Downgrade the theoretical claims from “shows” or “reveals” to “motivates,” unless the analysis is extended to signed classifier weights, biases, and the energy score.
- Report per-dataset ImageNet and CIFAR results, plus variance or repeated-run statistics where feasible, especially because some gains over ASH-S are small.
- For ISH, add a matched ordinary fine-tuning baseline using the same weight decay, optimizer, LR schedule, epochs, and SCALE postprocessor, and ablate the backward scaling itself.
- Clarify whether the applied scale is \(r\) or \(\exp(r)\), and discuss the numerical range of this factor across datasets and percentiles.

## Score and Decision
I calibrated this paper against the following retrieved human-review anchors:

- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/YMgMGPjUPg.md`, avg 4.75, Reject — close topic: activation-statistic OOD detection with CIFAR/ImageNet experiments, but reviewers questioned novelty and gains over ASH/DICE/SCALE/ReAct; this paper is somewhat more focused but has a more serious false guarantee.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/Oo5spZRpH6.md`, avg 3.67, Reject — activation-histogram OOD detector with unusually strong claims and insufficient explanation; the present paper is more credible empirically, so it should score above this.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/1ebgtm7P10.md`, avg 4.25, Reject — post-hoc OOD method on OpenOOD/CIFAR/ImageNet with scope and baseline concerns; the present paper has a clearer simple method and stronger diagnostic experiment, so it is above this.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/6sfRRcynDy.md`, avg 4.75, Reject — OOD method with competitive results but overclaimed theory and incomplete comparisons; this is quite similar in weakness pattern.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/VTYg5ykEGS.md`, avg 6.50, Accept — stronger benchmark/analysis contribution with broader value; the present paper is narrower and has more serious claim-validity issues.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/xE5ZaZGqBW.md`, avg 5.00, Reject — OOD detection paper with near/far benchmark claims; comparable borderline quality.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/VAmVEghgoC.md`, avg 4.50, Reject — empirical OOD method with weak conceptual justification; similar but this paper’s empirical tables are somewhat stronger.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/eN0RyRVbSm.md`, avg 6.50, Reject — extensive empirical OOD results but weak heuristic theory; this suggests strong experiments can offset theory concerns, but the present paper’s experiments are less broad.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/LjygLD0AkT.md`, avg 5.00, Reject — claimed OOD guarantees with unrealistic assumptions and weak connection to decisions; very relevant to the current paper’s false/overstated guarantee.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/GrDne4055L.md`, avg 6.25, Accept — theory-plus-empirics OOD robustness paper; stronger theoretical grounding than the present work.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/xUO1HXz4an.md`, avg 7.50, Accept — post-hoc OOD method with broad experiments, substantial gains, and generally convincing analysis; this paper is clearly below that standard.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/dm8e7gsH0d.md`, avg 6.00, Accept — very close feature-shaping/OOD topic with broader formulation and multi-architecture support; the present paper is below it due to the invalid ID-preservation guarantee and narrower experiments.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/mUXdysoxEP.md`, avg 6.75, Accept — stronger OOD method paper with solid feature-separation claims; the present paper is less well supported.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/ljwoQ3cvQh.md`, avg 7.00, Accept — OOD behavior analysis with broader empirical scope; stronger than the present submission.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/9ROuKblmi7.md`, avg 5.75, Accept — post-hoc OOD method with extensive evaluation but some assumption/sensitivity concerns; the present paper is slightly below because one headline guarantee is mathematically wrong.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/xQit6JBDR5.md`, avg 5.50, Reject — post-hoc angle-based OOD score on CIFAR/ImageNet; similar borderline empirical-method category.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/6Z8rZlKpNT.md`, avg 3.40, Reject — weak post-hoc latent-density OOD method; the present paper is substantially stronger.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/uWUovmBRUq.md`, avg 4.00, Reject — lower-scoring post-hoc OOD analysis; the present paper has more actionable empirical contribution.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/yNZi38u52U.md`, avg 3.75, Reject — weaker OOD confidence method; the present paper is stronger.

Relative to these anchors, this paper is above the low-scoring OOD papers with unclear methods or implausible results, but below accepted feature-shaping/OOD papers that have broader empirical support and more defensible theoretical claims. The simple SCALE idea and diagnostic ASH decomposition are valuable, but the false ID-preservation guarantee and overclaimed theory are serious for a paper whose central pitch is “state-of-the-art without ID trade-off.”

**Score: 5.0 / 10**  
**Decision: Reject**

MY FINAL SCORE: <pineapple>5.0</pineapple>  
MY FINAL DECISION: <orange>Reject</orange>