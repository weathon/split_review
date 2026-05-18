Now I have all the information needed. Let me compose the final consolidated review.

## Summary

This paper identifies a fundamental mismatch in standard Concept Activation Vector (CAV) computation: linear classifiers (SVMs, ridge, etc.) optimize class *separability*, so their weight vectors (filters) incorporate distractor directions unrelated to the concept signal. The authors propose **pattern-based CAVs**, computed via a simple covariance-based regression (Eq. 4) that isolates only the signal component. The paper evaluates alignment with true concept directions in controlled settings, and demonstrates downstream benefits for TCAV sensitivity testing and CAV-based model correction (ClArC) across VGG16, ResNet18, and EfficientNet-B0 on three datasets (ISIC2019, Pediatric Bone Age, FunnyBirds).

## Strengths

1. **Principled theoretical grounding.** Section 3.1 clearly explains, citing Haufe et al. (2014), why linear classifier weights (filters) capture both signal and distractor components — they optimize separability, not signal recovery. The contrast between filter optimization (Eq. 1) and pattern optimization (Eq. 2) is precise and the 2D toy experiments (Fig. 1) visually demonstrate the failure mode.

2. **Extensive quantitative alignment evidence.** Figure 2 reports cosine similarity between CAVs and ground-truth concept directions for all 13 Conv layers of VGG16 across three controlled datasets, *with standard errors*. Pattern-CAVs consistently achieve higher alignment (e.g., ~0.9 vs. ~0.4 for ISIC2019) while filter-CAVs achieve higher AUC (as expected from a separability objective). This directly supports the paper's core claim.

3. **Invariance to feature preprocessing demonstrated.** Figure 4 shows that pattern-CAV alignment with ground truth is unaffected by centering, max-scaling, or their combination, while filter-CAV alignment varies substantially. This is a practical advantage since preprocessing is often neglected in CAV workflows.

4. **Two downstream applications evaluated.** TCAV experiments (Sec. 4.3.1) on FunnyBirds show pattern-CAVs match ground-truth sensitivity scores while filter-CAVs produce lower scores for VGG16 and EfficientNet-B0. ClArC model correction (Sec. 4.3.2) shows pattern-CAVs yield higher biased-test accuracy and lower artifact sensitivity across architectures, with qualitative heatmaps confirming reduced artifact reliance.

5. **Honest limitation discussion.** Section 4.3.3 explicitly notes that for applications requiring class separability (e.g., post-hoc concept bottleneck models), filter-CAVs may be preferable. This nuanced conclusion strengthens credibility.

6. **Method is hyperparameter-free and closed-form.** Pattern-CAVs (Eq. 4) require no regularization tuning, unlike SVM/ridge which need at least one hyperparameter. This is a practical advantage correctly identified.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

1. **ResNet18 TCAV result noted but unexplained.** Line 292 states "Interestingly, all CAV variants achieve a perfect score for ResNet18" on FunnyBirds. This means the directional divergence problem does not manifest for this architecture in this setting. The paper offers no analysis or hypothesis — e.g., whether residual connections decorrelate features, or whether the last Conv layer's dimensionality differs meaningfully from VGG16/EfficientNet. While this doesn't contradict the core claim (the paper says filter-CAVs *may* diverge, not that they *always* do), analyzing when divergence is and is not severe would deepen the contribution from "pattern-CAVs are better" to "pattern-CAVs are better when representation geometry introduces distractor correlations."

2. **Missing error bars / confidence intervals for TCAV results.** The paper reports standard errors for the cosine-similarity and AUC results (Fig. 2) and uses proper statistical tests (Wilcoxon-Mann-Whitney for AUC). However, the TCAV bar plots (Fig. 5) and the ClArC results (Table 1) present single values per condition without variance estimates. Given that the TCAV experiment averages over 10 classes, reporting variability across classes or across random seeds would strengthen confidence that observed differences are not within noise. This is a presentation gap, not a fatal flaw — the qualitative pattern holds across architectures — but it should be addressed.

3. **Ground truth computation for FunnyBirds TCAV could be more explicit.** The paper describes how ground truth concept directions are computed for controlled datasets (Sec. 4.2: paired samples with/without concept, activation difference) and uses "sample-wise" terminology for the FunnyBirds TCAV experiment (line 288). Given that FunnyBirds samples randomize all non-class-defining parts per sample (line 174-175), one can infer how counterfactuals are generated. However, the paper never explicitly states "For FunnyBirds, the ground truth direction for a sample is the activation difference between that sample and a counterfactual sample without its class-defining part." A brief clarifying sentence would remove all ambiguity.

### Trivial

None.

## Nice-to-Haves

- **Filter-CAV hyperparameter sensitivity.** The paper notes that filter-CAVs are sensitive to regularization strength. An explicit ablation (varying λ for ridge/SVM, showing cosine similarity fluctuation) would strengthen the practical advantage claim.
- **Computation time comparison.** Pattern-CAVs are closed-form (no training loop), which is a practical benefit worth quantifying.
- **Error bars for all main figures.** Bringing variance estimates to the TCAV and ClArC results would align with the rigor shown in Fig. 2.

## Removed Points

These points are flagged to be removed; treat them with caution. They were excluded under the filtering rules specified in the merger instructions.

1. **"Potential double-dipping"** (harsh critic's minor issues): The critic speculates that using ground truth direction for post-correction ΔTCAV evaluation might be problematic, but this is speculative and no concrete evidence of bias is provided.
2. **"Table 1 is not visible due to parser stripping"**: This is a PDF-parser artifact; the original submission has the table.
3. **"Bone age unlocalizable artifact"**: The paper already acknowledges this ("We consider the brightness artifact in Bone Age *unlocalizable* and therefore do not report artifact relevance in input space," line 334).
4. **"URL for animated visualizations is truncated"**: Formatting artifact from PDF extraction.
5. **ResNet18 as "counterexample" to "always diverge" claim**: The paper says filter-CAVs *may* diverge (line 5-6: "such a separability-oriented computation leads to solutions, which *may* diverge"), not *always*. The observation that ResNet18 achieves perfect TCAV scores in one setting is not a counterexample to this qualified claim; it is retained above as a minor point about missing analysis, not as a challenge to the paper's validity.

## Novel Insights

None beyond the paper's own contributions. The reviews surface standard methodological concerns (error bars, explicit definitions, unexplained data points) but do not uncover contradictions, alternative explanations, or missed connections that the paper itself does not address.

## Suggestions

1. **Add a brief analysis of the ResNet18 anomaly.** Even a short paragraph speculating why the directional divergence problem is less pronounced for residual architectures on FunnyBirds (e.g., examining eigenvalue spectra of activations, cosine similarity between filter- and pattern-CAVs for ResNet18) would strengthen the paper's scientific depth.
2. **Add standard errors or bootstrapped intervals for the TCAV bar plot (Fig. 5) and the ClArC table.** This is the single highest-leverage improvement to the quantitative evidence.
3. **Explicitly state the ground truth generation procedure for FunnyBirds** in the TCAV section, following the same format used in Sec. 4.2 for the other controlled datasets.

## Score and Decision

**Originality**: The paper identifies a genuine, underappreciated problem in a widely-used interpretability tool and introduces a principled, simple fix grounded in neuroimaging literature. This is a moderate originality contribution — not paradigm-shifting, but non-obvious and useful.

**Importance**: CAVs are used across many XAI pipelines; improving their precision has downstream value for concept testing, model debugging, and shortcut removal. The importance is solid.

**Claims supported**: The paper's central claim — pattern-CAVs align better with true concept directions than filter-CAVs — is well-supported by controlled experiments across three datasets and three architectures. The downstream benefits for TCAV and ClArC are demonstrated but would benefit from variance estimates.

**Soundness**: Methodology is theoretically grounded. Experiments are appropriately designed with controlled datasets providing ground truth. The limitations are honestly acknowledged.

**Clarity**: Writing is clear and well-structured. Figures effectively communicate the main ideas.

**Value**: The method is practical (closed-form, no hyperparameters), extensively validated, and ready to use in existing CAV pipelines. The paper will likely influence how CAVs are computed in practice.

No fatal flaws are present. The three minor weaknesses are addressable and do not undermine the core contribution.

MY FINAL SCORE: <score>8.0</score>
MY FINAL DECISION: <decision>Accept</decision>