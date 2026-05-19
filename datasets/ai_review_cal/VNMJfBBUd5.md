- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6
Good, I have all the verification I need. Here is the consolidated review.

---

## Summary

This paper introduces Activation Gradient based Poisoned sample Detection (AGPD), a three-stage method that uses the angular distribution of activation gradients (gradient circular distribution, or GCD) to detect poisoned samples in backdoor attacks. The core insight is that in a backdoored model, poisoned and clean samples within the target class exhibit more dispersed activation-gradient directions and are separable in this space, while clean classes remain compact. AGPD first computes GCDs for all classes, identifies target class(es) via an anomaly-detection Z-score on a dispersion metric (CVBT), then iteratively filters poisoned samples using a sample-level closeness metric. Extensive experiments across 10 backdoor attacks, 2 datasets, 2 architectures, and 8 prior detection methods consistently show large-margin improvements.

## Strengths

1. **Novel gradient-based metric outperforms activation-based separation.**  
   Table 3 reports Silhouette scores in activation vs. activation-gradient space across eight attacks. The gradient space achieves consistently higher scores (e.g., 0.664 vs. 0.529 for BadNets, 0.696 vs. 0.485 for Blended, 0.515 vs. 0.379 for TaCT), directly supporting the core claim that GCD provides better separability than activations used by prior methods.

2. **State-of-the-art detection results across diverse attack settings.**  
   Over 12 backdoor attack variants (all-to-one, all-to-all, multi-target), AGPD achieves an averaged TPR of 96.66% on CIFAR-10 and 99.92% on Tiny ImageNet, exceeding the runner-up by 18.23% and 11.8%, respectively (Tables 1–2). These gains hold across sample-agnostic and sample-specific triggers, clean-label and non-clean-label variants.

3. **Robust detection at very low poisoning ratios where competing methods fail.**  
   At 0.5% poisoning ratio (Figure 3), AGPD maintains TPR around 90%, while AC and SCAn approach near-zero TPR. This demonstrates that the gradient-based metrics remain discriminative even when poisoned samples are extremely scarce.

4. **Target class identification is accurate even at 1% poisoning ratio.**  
   Over 120 backdoored models (Figure 5 left), SCAn's target-identification accuracy drops below 20% at 1% poisoning, while AGPD retains much higher accuracy. This shows the CVBT-based Z-score metric is more reliable for target class identification.

5. **Works with minimal clean reference data (1 sample per class) and out-of-distribution references.**  
   Figure 5 (middle) shows that even with one clean sample per class, or with OOD samples from CIFAR-5m, AGPD maintains high TPR on most attacks. This addresses a practical limitation of prior work that assumes larger or in-distribution clean datasets.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Stage 3 stopping criterion (JS divergence trace-back) is underspecified.**  
   The paper describes a trace-back strategy that selects the iteration where JS divergence "locates at the stable and low region" (line 184), but provides no concrete algorithm for detecting this region—no threshold, knee-finding rule, or automated procedure. Since the main detection results rely on the fixed threshold τₛ = 0.05 (and the sensitivity analysis shows stable performance across τₛ values), this step appears to be an unvalidated engineering detail. The paper would be stronger by either specifying the procedure precisely and showing it improves results, or removing it in favor of the simpler fixed-threshold rule that already works.

2. **CVBT dispersion metric is not justified over simpler alternatives.**  
   The CVBT metric (Eq. 4) computes RMSE of cosine similarity values under two basis vectors. The paper does not explain why simpler directional dispersion measures (e.g., circular variance, angular standard deviation) would not suffice. An ablation or brief justification would strengthen the method section.

3. **No standard deviations or confidence intervals reported.**  
   Results tables report point estimates (TPR, FPR, F1) without variance across multiple runs. Given that the performance margins are large, this is not a fatal concern, but reporting variability (e.g., over 3–5 seeds) would strengthen the evidence, especially for attacks where margins are narrower.

4. **Basis selection in CVBT is not analyzed for sensitivity to outliers.**  
   The CVBT metric picks the vector with the maximal angle as the second basis (Eq. 4). The paper does not analyze what happens if this farthest point is an unrepresentative outlier rather than a poisoned sample far from the clean reference. The strong empirical results suggest the effect is limited in practice, but a brief discussion or synthetic test would improve methodological soundness.

### Trivial

1. **Threshold τ_z = e² is not included in the sensitivity analysis.**  
   While τ_s is sweeped from 0.01 to 0.1 (Figure 5 right), τ_z is fixed at e² without equivalent analysis. The Z-score distribution (Figure 4b) shows a clear margin between target and clean classes, so the choice is likely robust, but a brief note or figure would close the gap.

2. **Notation density.**  
   The paper introduces many symbols (ρ, z, s, τ_z, τ_s) with multi-level superscripts and subscripts (layer, class). While the flow is readable, a notation table in an appendix would help readers track definitions.

## Nice-to-Haves

- **Ablation: GCD on activations vs. gradients with the same pipeline.** Running the AGPD pipeline using activations (rather than activation gradients) would directly isolate whether the improvement comes from the gradient input or from the GCD methodology itself. This would rule out the alternative hypothesis that the GCD machinery, not the gradient perspective, drives the gains.
- **Robustness to dirty reference samples.** The method assumes reference samples are clean, but a defender cannot guarantee this. Injecting a small fraction of poisoned samples into the reference set and measuring performance degradation would be informative for practical deployment.
- **Wall-clock time comparison.** The method trains a model and computes gradients through all layers for all samples. A rough runtime comparison to other methods (or an estimate) would help practitioners assess feasibility.

## Removed Points

*These points were flagged for removal; treat them with caution.*

- **Criticism that Observations 1–2 need a quantitative sanity check across all 10 attacks.** The paper already provides this via the Silhouette Score analysis (Tab. 3) and the Statistics section (Fig. 4a showing ρ values). This concern is adequately addressed.
- **Criticism about Adap-Blend not specifically challenging gradient-based detection.** The critic acknowledges this is moot since AGPD performs well against it. The point adds no substantive weakness.
- **"Robustness to OOD data" framing as a missing piece.** The paper already tests OOD reference samples (CIFAR-5m) and shows good performance. Presenting this as a missing analysis would be incorrect.
- **"More models would strengthen" type arguments.** The evaluation already covers 2 architectures and 2 datasets. Generic requests for more are not actionable weaknesses.
- **Any comment about missing appendix content, missing proofs, or absent references.** The parser strips these; they exist in the original submission.

## Novel Insights

The most striking finding that emerges from the review is that gradient-direction dispersion (measured via a relatively complex two-basis CVBT metric) achieves a clean separation that activation-space methods consistently miss, even against adaptive attacks (Adap-Blend) and at poisoning ratios as low as 0.5%. The fact that AGPD works with a single clean reference sample per class and with OOD references is a second-order insight that speaks to the fundamental robustness of the gradient-direction signal—it is not an artifact of careful hyperparameter tuning or large reference sets. Beyond the paper's own contributions, the comparison exposes a pattern: activation-based methods (AC, Beatrix, SCAn) degrade gracefully on some attacks but collapse on low-ratio or multi-trigger settings, whereas gradient-based methods maintain performance, suggesting the gradient space genuinely captures different (and more attack-invariant) information than the activation space.

## Suggestions

1. **Specify the JS-divergence stopping rule.** Replace the vague "stable and low region" with a concrete rule (e.g., select the first iteration after which JS divergence stays below a threshold for T consecutive iterations). Alternatively, drop the trace-back entirely and show that the fixed τₛ iteration works equally well.
2. **Add standard deviations** to the main results tables over 3–5 random seeds.
3. **Include a brief justification** for why CVBT is used instead of simpler directional dispersion measures (or show empirically that CVBT outperforms them).
4. **Note the τ_z threshold choice** and why it is robust (the Z-score distribution in Fig. 4b makes this clear), even if a full sensitivity sweep is not conducted.
