Now I have verified everything. Here is my final consolidated review.

---

## Summary

This paper proposes F-Fidelity (FFid), a framework for faithfulness evaluation of XAI explanations that combines (i) explanation-agnostic fine-tuning of the classifier using random stochastic masks to prevent information leakage and mitigate OOD issues, and (ii) bounded removal that caps the number of removed elements to a constant fraction of the input rather than a fraction of the explanation. The paper evaluates FFid on image (CIFAR, Tiny ImageNet) and time-series (PAM, Boiler) domains against Fid, ROAR, and RFid baselines, and provides a theoretical result (Theorem 1) connecting the FFid\(^+\) metric to ground-truth explanation size under an idealized influence-tier assumption.

## Strengths

- **Core idea addresses a real, well-identified problem**: The paper correctly identifies two limitations of prior removal-based faithfulness metrics — OOD issues in direct perturbation, and information leakage in ROAR's explanation-specific retraining — and proposes a clean solution: explanation-agnostic fine-tuning with random stochastic masks. The loss in Eq. (4) formalizes this in a simple, reusable way that avoids retraining per explainer.

- **Bounded removal is a principled fix to a previously overlooked confound**: Prior RFid work removed a fraction of the *explanation size itself*, making evaluation results depend on the arbitrary sparsity choice. FFid caps removals at \(\beta td\) (a fraction of the *total input*), making comparisons across sparsity levels meaningful. This is a simple but genuinely useful insight.

- **Strong empirical signal in the controlled-degradation experiments**: On Tiny ImageNet, FFid achieves perfect macro correlations (-1.00) across all three comparison settings (MoRF vs GT, LeRF vs GT, MoRF vs LeRF) for both SG-SQ and GradCAM, while baselines (Fid, ROAR, RFid) show substantially weaker or even reversed correlations. The pattern holds across CIFAR, PAM, and Boiler datasets. The use of both macro (AUC-based) and micro (per-sparsity-level) correlations provides a more nuanced evaluation than single-number summaries.

- **Ambitious theoretical connection between the metric and explanation sparsity**: The attempt to prove that FFid\(^+\) can recover the size of the most influential tier (Theorem 1) is a novel and interesting direction that goes beyond what existing faithfulness metrics attempt.

## Weaknesses

### Major

1. **Claimed NLP experiments are entirely absent from the paper.** The abstract states "We conducted experiments on multiple data structures, such as images, time series, and natural language" and the introduction lists "comprehensive evaluations across multiple data modalities (images, time series, and natural language)" as a main contribution. However, Section 4 contains only two subsections: 4.1 (Image Classification) and 4.2 (Time Series Classification). No NLP experiments appear anywhere in the paper. This is not a parser artifact — the paper's structure simply does not include an NLP section. This overclaim directly undermines the stated contribution of broad multi-modal applicability and would mislead readers.

2. **Theorem 1 is presented without proof or proof sketch, yet is listed as a core contribution.** The theorem (lines 171-176) asserts monotonic behavior of the expected FFid\(^+\) function under influence-tier assumptions. No derivation, proof, or even a proof outline is provided. The paper claims "We theoretically and empirically analyze the relationship between the explanation size and the FFid metrics" as a main contribution, but the theoretical component is incomplete. The gap between the idealized theorem and the actual finite-sample computation of FFid\(^+\) in Section 6 is also not bridged.

3. **No ablation studies isolate the contributions of the two main components.** The paper compares FFid (fine-tuning + bounded removal) against Fid (neither), ROAR (retraining, no bounded removal), and RFid (bounded removal, no fine-tuning). But there is no experiment testing, e.g., FFid without fine-tuning, or RFid on the fine-tuned model, to determine whether the improvements come primarily from the fine-tuning, the bounded removal, or their combination. Without this, it is impossible to attribute the reported gains to specific design choices. Similarly, the \(\beta\) parameter is critical but only tested at \(\beta=0.5\) in most experiments with no sensitivity analysis.

4. **No statistical significance or uncertainty reported for any correlation metric.** All Spearman correlations are presented as point estimates without confidence intervals, p-values, or standard errors. With only 6 explainers per experiment (the degraded variants), these correlations are highly sensitive to individual data points. The reader cannot assess whether FFid's apparent superiority over baselines is reliable or within the noise of the measurement. This is a basic expectation for an empirical paper drawing comparative conclusions.

### Minor

1. **The synthetic ground-truth construction inherits the limitations of the base explainer.** The evaluation creates ground-truth rankings by adding controlled noise to explanations from SG-SQ or GradCAM, assuming that more noise = less faithful. While this is a common approach in the literature (used in ROAD and elsewhere), the paper overstates the strength of this validation by calling it a "ground-truth ranking...in terms of faithfulness" (line 49-50). What the experiments actually validate is that FFid can recover a synthetic noise-level ordering. The approach is reasonable for benchmarking metrics, but the paper should acknowledge the gap between synthetic and true faithfulness more explicitly.

2. **Notational inconsistency in the RFid definition (Eq. 2).** The equation uses \(P(y_i=f(\chi^+(\cdot)))\) inside a sample average, where \(P\) appears to denote a probability over the random removal process. However, the notation then averages over \(n\) samples as if \(P\) returns an indicator. This should be clarified: is \(P\) a probability that is then averaged, or should it be an indicator? This is confusing and should be fixed.

3. **The negative correlation sign is not explained.** The paper reports negative correlations (e.g., -0.60 to -0.71 for GradCAM on CIFAR) without discussing the expected direction of the metric. For a metric where higher values indicate better faithfulness, a good correlation with ground truth (where lower noise = better) should be negative. The paper should make this explicit to avoid reader confusion.

4. **The strong influence-tier assumptions in Section 5 are not discussed in terms of practical limitations.** The theory assumes that elements within a tier have identical influence and the function \(g\) depends only on counts per tier. This is essentially a linear additive structure. The paper acknowledges these are "idealized assumptions" but does not discuss how far real classifiers deviate from them, or what this means for the theory's practical applicability.

### Trivial

- The paper uses "Emprical" (line 183) instead of "Empirical" in a section heading.
- Line 108: "takes a the input dimensions" — typo.
- The paper references Algorithm 1 but the algorithm text appears to be in an \input file that was not expanded in the extracted text.

## Nice-to-Haves

- A comparison to ROAD (Rong et al. 2022), which addresses similar OOD/information-leakage issues with a different strategy, would strengthen the positioning of FFid. ROAD is mentioned in related work but not compared experimentally.
- A principled way to select \(\beta\) (rather than fixing it at 0.5) would make the framework more practically useful. For example, could \(\beta\) be set based on the model's robustness characteristics or the dataset's known sparsity?
- Scatter plots showing FFid values vs. noise level at individual sparsity levels would help the reader visualize the ranking behavior, beyond the aggregated correlation tables.
- A brief discussion of how many random mask samples are used during fine-tuning and evaluation (the stochasticity in \(\chi^+\) means individual evaluations may vary) would improve reproducibility.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **"The ground-truth ranking is based on noise level relative to a single base explainer (IG)":** The reviewer states IG is the base explainer, but the paper says "such as IG" — the actual experiments use SG-SQ and GradCAM. Moreover, the controlled-degradation methodology is standard practice in XAI evaluation (used by ROAD and others). The paper is transparent about this approach. This is not a fatal flaw; it is a reasonable benchmarking strategy.

2. **"Fine-tuning with random masking is just standard data augmentation (CutMix, random erasing)":** While conceptually related, the paper's specific contribution is using this fine-tuning for *evaluation* (making the classifier in-distribution for the removal-based metric), not for general robustness. The motivation and application are distinct. This criticism conflates the technique with its purpose.

3. **"The paper should include larger datasets / more models":** The current set (ResNet on CIFAR/Tiny ImageNet, LSTM on two time-series datasets) is adequate for a first presentation of the method. The criticism is generic and does not identify a specific gap.

4. **"Missing \(\beta\) sensitivity analysis":** Moved from "major" to "nice-to-have" — the paper does test multiple \(\beta\) values in Section 6 (Figure 1 on colored-MNIST), showing the behavior across \(\beta\in\{0.2,0.5,1.0\}\). This partially addresses the concern, though not in the main image/time-series experiments.

5. **"The degradation process is vague":** The paper states noise proportions and the base explainers (SG-SQ, GradCAM). For a conference paper, this level of detail is adequate; the missing precision is minor and can be resolved during revision.

## Novel Insights

The most interesting observation that emerges from these reviews is the tension between the paper's ambitions and its execution. The core technical insight — that you can fine-tune a classifier once with random masks to serve as a robust evaluation platform for any explainer — is genuinely clever and practically valuable. It cleanly sidesteps both the OOD problem and the information leakage problem in one shot. However, the paper undermines itself by overclaiming: the NLP experiments do not exist, the theorem is unproven, and the synthetic ground truth, while standard practice, is presented in language that implies stronger validation than it actually provides. The "true explanation size recovery" angle (Theorem 1 + Section 6) is the most novel part of the paper conceptually, but it is also the least substantiated — resting on unproven theory and validated only on a simple two-tier colored-MNIST setup. If the authors focused on delivering what they promise (prove the theorem, add NLP experiments, add ablations), the paper would be significantly stronger.

## Suggestions

1. **Add the missing NLP experiments or remove the claim.** This is the most actionable fix: either conduct experiments on a sentiment classification dataset (e.g., IMDB with LIME or Integrated Gradients) and report results, or explicitly remove "natural language" from the abstract and introduction. Given that the fine-tuning framework is described as modality-agnostic (mask tokens in language), demonstrating this claim is important for the paper's credibility.

2. **Include a proof of Theorem 1 (even if deferred to an appendix).** Without a proof or at minimum a detailed sketch, the theorem is not a contribution — it is a conjecture. Since the empirical validation in Section 6 is limited to a two-tier synthetic setting, the theory needs to carry more weight.

3. **Add ablation experiments isolating components.** At minimum, compare: (a) Fid (no modifications), (b) RFid (bounded removal only), (c) FFid without fine-tuning (bounded removal on original model), (d) FFid (full method). Also test at least two additional \(\beta\) values (e.g., \(\beta=0.3, 0.7\)) in the image experiments.

4. **Report uncertainty for correlation estimates.** Use bootstrap resampling to provide 95% confidence intervals for the Spearman correlations, or at minimum flag which correlations are not statistically distinguishable from zero. With 6 data points per correlation, this matters.

5. **Clarify the notational inconsistency in Eq. (2)** (the \(P(\cdot)\) inside the sample average) and explicitly state the expected direction of the metric (higher is better / lower is better) to explain the sign of the reported correlations.

## Score and Decision

This paper has a genuinely useful core idea and presents reasonably strong empirical evidence on images and time series. However, it is held back by three significant problems: (1) claimed NLP experiments that simply do not exist, (2) a central theorem presented without proof, and (3) a lack of experimental rigor (no ablations, no significance testing). These are not minor nitpicks — they directly affect the paper's ability to support its stated contributions. A major revision could make this a strong paper, but in its current form the evidence does not match the claims.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>