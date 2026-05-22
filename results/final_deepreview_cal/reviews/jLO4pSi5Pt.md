Now I have everything I need. Let me compile the final review.

## Summary

This paper introduces L-TTA, the first test-time adaptation method specifically designed for vision-language models (VLMs) operating on long-tailed test streams. The method addresses two identified failure modes — text-induced tail erosion and modality-bias amplification — through three co-designed components: Synergistic Prototypes (SyPs) comprising deterministic and exclusionary prototypes to enrich tail-class representations, learnable Rebalancing Shortcuts (RSs) for dynamic inter-class rebalancing, and Balanced Entropy Minimization (BEM) with theoretical guarantees to reduce head-class bias in entropy minimization. Experiments across 15 datasets, three imbalance ratios (10, 20, 50), three benchmarks (OOD, cross-domain, corruption), and multiple backbones show consistent improvements in both accuracy and macro-F1 over 12 existing VLM TTA methods.

## Strengths

- **First systematic solution for LT-TTA on VLMs with concrete failure-mode analysis**: The paper identifies two failure modes specific to long-tailed TTA in VLMs (text-induced tail erosion and modality-bias amplification, Section 1, Figure 1b) and designs three co-dependent components to address them. The strongest evidence is the comprehensive results: on the OOD Benchmark at imb=10 (Table 1), L-TTA outperforms all 12 baselines, achieving 65.97%/61.18% (Acc/Mac) vs. the next best DPE at 64.50%/57.57%, a margin of 1.47%/1.70%.

- **Broad and consistent gains across diverse benchmarks, imbalance ratios, and backbones**: Tables 1–3 cover three benchmarks at three imbalance ratios over 15 datasets. L-TTA ranks first on nearly all entries. For example, on the Cross-Domain Benchmark (Table 2), L-TTA averages 68.77% Acc and 63.44% Mac, exceeding all prior methods, and the macro-F1 improvement (2.20%) significantly exceeds the accuracy improvement (1.02%), confirming the method meaningfully rebalances predictions. Gains hold across ViT-L/14, ViT-H/14, SigLIP-L/16, and MetaCLIP-BigG backbones (Table 5).

- **Theoretical grounding for Balanced Entropy Minimization**: Proposition 1 proves that standard EM creates a positive expected gradient for head classes and negative for tail classes, exacerbating bias. Proposition 2 proves BEM reduces the gradient gap between head and tail classes. These propositions (with proofs in Appx. A) provide formal justification rare in the TTA literature.

- **Efficiency-accuracy trade-off**: Table 4 shows L-TTA achieves the highest harmonic mean of Accuracy and Macro-F1 (67.20 on LT-CDB, 46.08 on LT-CB) while requiring only 1.45h runtime and 1.89G memory — competitive with lightweight methods and far cheaper than RLCF (18.30h) or WATT (27.70h).

- **Ablation studies validate each component**: Table 6 shows dropping DPs or EPs degrades macro-F1 by 3.22–3.95%, removing RSs reduces macro-F1 by 1.71%, and removing BEM reduces macro-F1 by 0.66%. The full model (SyP+RS+BEM) yields the best results, confirming all three components contribute positively and synergistically.

## Weaknesses

### Major

- **Missing variance estimates for all main results**: Tables 1–3 report only means over "5 runs for each experiment" with no standard deviations, confidence intervals, or other uncertainty quantification. Many comparisons are close (<1% difference, e.g., ImageNet-A at imb=50: DPE 60.21 vs. L-TTA 60.07 where L-TTA is *worse*; Caltech101 at imb=10-50 average: DPE 94.85 vs. L-TTA 95.26). Without variance, the reader cannot assess whether the claimed superiority is reliable or reflects noise from random subsampling, augmentation, and ordering. This is the most important missing piece given that many differences are small.

- **BEM pseudo-label-based prior estimation is not validated against the true prior**: Equation (9) uses a class prior π that is "continually updated based on the current predicted pseudo-labels." In a long-tailed stream, pseudo-labels will be biased toward head classes, potentially producing a skewed prior that offsets the intended rebalancing effect. The paper does not compare BEM using the *true* test-set priors (which are known from the controlled construction) against BEM using the estimated priors. A control experiment showing whether the pseudo-label estimation introduces bias or matches the oracle case would substantially strengthen the claim that BEM works as intended rather than relying on a specific prior estimation scheme.

- **Test-stream ordering protocol is not specified**: The paper states only that random sampling constructs the long-tailed distribution; it does not specify the order in which samples are presented to the model during sequential TTA. If the stream is randomly shuffled (i.i.d. within the long-tailed set), tail classes appear at a steady rate and prototype methods receive regular updates from the start — a much easier scenario than the realistic head-first or imbalanced-stream case the paper's motivation describes. The robustness experiment in Table 7 (varying ε for tail-class appearance probability) partially addresses this and shows encouraging stability, but this experiment is buried in the ablation section and should either be the main evaluation setup or be described upfront to definitively rule out ordering as a confound.

### Minor

- **Initial entropy threshold θ for DPs is unspecified**: Equation (4) uses a threshold θ to select confident views for DP updates and states "if 𝒯 ≠ ∅, we update θ with the minimal entropy in 𝒯 following the above EMA manner." However, no initial value for θ is given, making the first-step behavior unreproducible. A too-high initial θ could include noisy views, a too-low one could exclude nearly all tail-class views early on.

- **Hyperparameter discrepancy: default K vs. best K from ablation**: The Implementation Details state K=0.3, but the ablation text (Section 4.2) says "setting K=0.2 yields the best performance." The figure caption uses "b" rather than K for the same quantity. The paper should either adopt K=0.2 as default or explain why 0.3 is used despite 0.2 being better, and resolve the naming inconsistency (K vs. b).

- **BEM formulation notation**: The variable $\tilde{\mathbb{P}}$ in Equation (9) is used before it is defined; it appears to be the softmax of the modified logits z' but this is not stated explicitly. Clarifying would improve reproducibility.

### Trivial

- The term "Asp. I, II" and "Asp. II" in the introduction (Section 1, around Figure 1c) uses undefined abbreviations. While the context (the two failure modes listed just above) makes the meaning inferable, defining "Asp." explicitly would improve clarity.

## Nice-to-Haves

- Including at least one unimodal long-tailed TTA baseline (e.g., SAR or DELTA applied naively to the VLM) would further validate the claim that unimodal solutions fail for VLMs, which is currently supported only by illustrative analysis in Figure 1(b.2) rather than controlled comparison.

- The corruption benchmark uses only Gaussian noise at three severity levels. While Appendix J covers other corruption types, summarizing cross-corruption robustness in the main text would strengthen the claim of general robustness.

- Brief analysis of cases where L-TTA performs worse than baselines (e.g., ImageNet-A at imb=50) would provide useful context about the method's limitations.

## Removed Points

The following points from the inputs were removed with justification:

- **Criticism that EPs don't "store the most improbable features"**: The harsh critic claimed the mechanism does not match the name. However, Eq. (5) shows that features are weighted by φ_c = (max P - P(y_c|x))/max P — high weight when the model assigns low probability to class c. The name accurately describes what the mechanism does (features improbable *for class c*). Retaining this criticism would reflect a misunderstanding of the method.

- **Criticism about "Asp." never being defined**: While technically true, the context makes it clear these refer to the two failure modes. This is a trivial clarity issue, already captured in the Trivial section.

- **Complaints about notation heaviness and inconsistency (Ẽ_v vs V, Ẽ_t vs T)**: The notation is standard for CLIP papers and the mappings between different variable names are clearly defined. This is a style preference, not a substantive weakness.

- **Claim about comparison fairness being asymmetric in favor of baselines**: The evaluation compares against 12 existing methods reproduced with their provided hyperparameters, which is standard practice for TTA papers.

- **Mention of missing appendix content as a weakness**: Appendix pages are stripped by the parser; they exist in the original submission. Do not penalize for missing appendix content.

- **Concern about "if the calculated cardinality is less than the class cardinality itself" breaking the imbalance ratio**: The paper acknowledges this edge case. For standard benchmarks like ImageNet derivatives, each class has far more samples than needed for any imbalance ratio up to 50 (1000-class ImageNet has ~1300 images/class). This concern is hypothetical and unsupported by evidence that it actually affects the reported ratios.

## Novel Insights

The most interesting observation to emerge from the reviews is the tension between the paper's core motivation (long-tailed stream where head classes dominate early) and the evaluation design (which doesn't control for ordering). The fact that L-TTA shows robustness to ordering in Table 7 suggests either (a) the method is genuinely robust to stream ordering (a strength) or (b) the ordering manipulation in Table 7 (varying ε for tail-class probability) does not fully capture the sequential stress the motivation describes. The paper would benefit from explicitly resolving this ambiguity: if L-TTA is robust to ordering, that should be a highlighted strength; if ordering matters, the evaluation should control it. Either way, the current gap between the motivating scenario and the evaluation protocol is worth careful attention.

## Suggestions

1. **Add standard deviations** (or confidence intervals) to all main results tables (1–3). Run each experiment with different random seeds that control both the subsampling and the stream ordering, and report the resulting variance.

2. **Ablate BEM prior estimation**: Compare BEM with true test-set priors (known from the construction) vs. BEM with the default pseudo-label-estimated priors. If they are equivalent, this addresses the feedback-loop concern; if not, discuss the gap.

3. **Specify the stream ordering** explicitly in the main experimental setup. Either adopt a head-first ordering that stresses tail prototypes, or randomize across multiple seeds (and report variance, per suggestion 1). Move the robustness experiment (Table 7) into the main evaluation to establish that ordering is not a confound.

4. **Resolve the K=0.3 vs. K=0.2 discrepancy** and the naming inconsistency (K vs. b) in Figure 4c and the main text.

5. **Specify the initial value** of the entropy threshold θ for DPs in Equation (4).

## Score and Decision

### Calibration Report

**Round 1 (Bracketing):** Three queries on "test-time adaptation long-tailed vision-language models" returned anchors in three bands: weak (<3.5, scores 2.33–2.50), mid (3.5–7.5, scores 4.40–7.00), and strong (>7.5, scores 8.00). Initial bracket: this paper falls between 4.5 and 7.0.

**Round 2 (Narrowing):** Two queries on "test-time adaptation CLIP long-tailed vision language models prototypes" and "test-time adaptation prototypes entropy minimization CLIP" returned anchors within the bracket: scores 5.50 (BAT-CLIP, Reject — fatal flaw with ground-truth label usage), 5.67 (Proof, Reject), 6.00 (DOTA, Reject — all 6s), 6.25 (ML-BEM, Accept), 6.67 (RLCF, Accept). Compared to these, the paper under review is:
- **Better than** BAT-CLIP (5.50) — which had a fatal flaw this paper does not have
- **Better than** ROSITA (4.67) and BLG (4.67) — which were criticized for incremental contribution vs. this paper's novel problem formulation
- **Comparable to** DOTA (6.00) — both have solid methodology and extensive experiments but similar validation gaps
- **Slightly weaker than** RLCF (6.67) — RLCF's multi-task scope and cleaner evaluation offset its more incremental contribution

**Final score:** 6.0, positioned between DOTA (6.00) and RLCF (6.67), reflecting the paper's genuine novelty and broad evaluation but discounted for the missing variance reporting and the unvalidated BEM prior estimation.

**Anchors retrieved (all rounds):**
- pdzHpQbGrn (2.50, R1) — weaker paper on active TTA for VLMs
- JIlIYIHMuv (2.50, R1) — weaker paper on continual learning for LVLMs
- ZaudLwn0Hm (2.50, R1) — weaker paper on few-shot prompt learning
- gNoqEdT2wO (2.33, R1) — weaker paper on multimodal class-incremental learning
- b20VK2GnSs (7.00, R1) — accepted concept drift paper, stronger evaluation
- BUDxvMRkc4 (4.67, R1) — rejected BLG paper, incremental contribution
- lF9QXpfNHm (4.67, R1) — rejected ROSITA paper, incremental contribution
- 9RnTw9YiXV (4.40, R1) — rejected LVLM long-tail paper
- TPZRq4FALB (8.00, R1) — accepted paper on multi-modal reliability bias
- WyEdX2R4er (8.00, R1) — accepted paper on visual data-type understanding
- uAFHCZRmXk (8.00, R1) — accepted analysis paper on modality gap
- 1aF2D2CPHi (8.00, R1) — accepted paper on data-free distillation
- k9NYnsC4Mq (5.67, R2) — rejected Proof paper on continual learning
- z7PhIgVmZU (5.50, R2) — rejected BAT-CLIP paper, fatal flaw with GT labels
- kIP0duasBb (6.67, R2) — accepted RLCF paper, multi-task TTA
- yD2JMeKumt (6.00, R2) — rejected DOTA paper, distributional TTA
- 75PhjtbBdr (6.25, R2) — accepted ML-BEM paper, multi-label TTA
- KNtcoAM5Gy (5.50, R2) — rejected BaFTA paper, backprop-free TTA

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>