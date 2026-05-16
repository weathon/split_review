Now I have all the information I need. Let me compose the final consolidated review.

## Summary

This paper introduces **Zero-Shot Noisy TTA (ZS-NTTA)**, a practical setting where vision-language models (VLMs) must adapt to test data streams containing out-of-distribution (noisy) samples in a zero-shot manner. Through careful analysis (gradient analysis, score distribution visualization, three-pipeline comparison), the paper shows that existing TTA methods fail because unfiltered noisy samples dominate gradients during adaptation, and because coupling the classifier and detector degrades both sub-tasks. The proposed **AdaND** decouples these roles — keeping the VLM frozen while training a lightweight linear noise detector using ZS-CLIP's outputs as pseudo-labels, with Gaussian noise injection to handle clean data streams. Experiments across 11 ID datasets and multiple OOD datasets show consistent improvements over baselines, with computational costs comparable to frozen CLIP.

## Strengths

- **Mechanistic analysis of TTA failure under noisy streams**: The paper does not merely observe that TTA methods underperform — it explains *why*. The three-pipeline comparison (GT > ZS-CLIP > Normal > All-update, Table 1), score-distribution visualization (Figure 3), and gradient analysis (Figure 4, showing noisy-sample gradients an order of magnitude larger than clean-sample gradients) collectively demonstrate that unfiltered noisy data overwhelms adaptation. The gradient-stage analysis (three stages of degradation in Tent) is particularly insightful and directly motivates the decoupling design.

- **Consistent and efficient performance across diverse settings**: AdaND achieves strong and consistent gains over baselines across 44 ID-OOD dataset pairs (Tables 2–3) — e.g., +8.32% Acc_H on ImageNet ZS-NTTA — while maintaining runtime and memory comparable to frozen ZS-CLIP and far below TPT or Tent (Table 4). The extensive evaluation (11 ID datasets, varied noise ratios 0%–75%, multiple backbones in Table 23) demonstrates that the method generalizes well beyond any single benchmark.

- **Practical handling of unknown noise prevalence via Gaussian injection**: The ablation in Table 6 cleanly demonstrates the necessity of both components: without Gaussian injection, the detector fails on clean streams; without the detector, performance degrades on noisy streams. Additional ablations (Tables 15–16) confirm robustness to noise type and injection frequency, showing the method works without prior knowledge of the stream's noise ratio.

- **Clean problem formulation and benchmark construction**: The ZS-NTTA setting is well-motivated by real-world open-world deployment, clearly distinguished from both standard TTA and ZS-OOD detection, and comes with a well-designed evaluation protocol (Acc_S, Acc_N, Acc_H).

## Weaknesses

### Fatal
None.

### Major

- **Overclaimed ZS-OOD detection results due to unfair comparison set**. The paper repeatedly claims state-of-the-art performance on ZS-OOD detection (abstract, Section 1 contributions, Section 6 conclusion), but Table 5 compares AdaND against *static* methods (Energy, MaxLogit, MCM, CLIPN, NegLabel) that do not see test data, while AdaND is a test-time adaptation method that processes the full test stream and updates online. This gives AdaND access to the test distribution — a fundamentally different setting. The paper references Fan et al. (2024) as a test-time OOD detection method but does not include it (or any test-time-adaptive OOD method) in the comparison. The 9.40% FPR95 improvement over static methods is not an apples-to-apples comparison. The core ZS-NTTA contribution is unaffected, but this overclaim on a secondary result weakens credibility. The authors should either add test-time OOD detection baselines or explicitly reframe the OOD results as "AdaND also produces competitive scores despite operating under the harder ZS-NTTA setting" rather than claiming SOTA on the standard ZS-OOD benchmark.

### Minor

- **Main results (Tables 2–3) lack statistical significance measures for the largest datasets.** The paper reports single numbers for ImageNet and its variants without confidence intervals or standard deviations across multiple runs. Multi-seed experiments (seeds 0–4) are provided only for CIFAR-10/100 (Tables 18–19, as referenced) with a note about "computational constraints." Some gains are modest (e.g., 0.3 Acc_H on Food-101; 49.36 vs. 48.12 on ImageNet-A). While the consistent pattern across many datasets partially mitigates this concern, the paper would be stronger with at least 3 seeds on the main ImageNet results or a clearer argument that the pipeline is deterministic for the reported setting.

- **Adaptive threshold not directly ablated for AdaND itself.** The paper validates adaptive vs. fixed thresholds for the baseline ZS-CLIP pipeline (Section 2), but does not ablate this choice within the AdaND framework. Since the adaptive threshold is a component shared with OWTTT (Li et al., 2023), a dedicated ablation would clarify how much of the gain comes from the threshold versus the learned detector.

- **The Gaussian injection, while clever, is a somewhat ad hoc solution.** The paper does not provide a formal justification for why Gaussian noise is the optimal choice (beyond empirical robustness in Table 15), nor does it analyze sensitivity to the Gaussian variance parameter. The ablation covers noise *type* and *frequency*, but not the *scale* of the injected noise relative to the feature distribution.

### Trivial

- The term "noisy samples" is used to mean OOD samples (outside the ID label space), which could be confused with label noise common in TTA literature. The paper defines this clearly in Section 2, but the terminology choice is slightly unconventional.

## Nice-to-Haves

- **Add a variant with a static (non-adaptive) detector** to isolate whether the gain comes from the linear architecture itself or from online adaptation. Currently, AdaND is compared against ZS-CLIP (static), but it is unclear how much of the improvement is due to the linear layer versus the adaptation loop.
- **Include harder, fine-grained OOD scenarios** where noisy samples are visually similar to ID (e.g., different bird species not in the ID set) to test the limits of the method. The paper uses standard OOD benchmarks where ID/OOD separability is relatively easy (e.g., ImageNet vs. SVHN).
- **Discuss the assumption that ID class names are known.** This is standard for zero-shot classification, but in truly open-world TTA, the ID task may not be specified in advance. Acknowledging this boundary would strengthen the framing.

## Removed Points

These points were raised by reviewers but are removed or downgraded after verification against the paper:

- **"Gaussian noise may inadvertently affect the adaptive threshold in noisy streams"** — Removed. The paper explicitly states (Section 4.2) that injected noise is *intentionally* included in the threshold calculation, and the ablation (Tables 15–16) confirms robustness. The reviewer misread the design.
- **"Missing appendix/proofs/references"** — Removed per policy. The parser strips these; they exist in the original submission.
- **"Style/formatting nitpicks"** — Removed per policy. Garbled characters and formatting artifacts are parser errors, not author errors.
- **"Terminology confusion about 'noisy samples'"** — Removed. The paper defines the term clearly in Section 2. This is a presentation preference, not a technical flaw.
- **"Should also cover Y/domain Z/additional tasks"** beyond the paper's stated scope — Moved to Nice-to-Haves.

## Novel Insights

The reviews surface one genuinely novel observation beyond the paper's own contributions: the gradient-stage analysis of Tent (three stages of degradation) is a particularly sharp diagnostic tool that could be reused by future work studying TTA failure modes. The reviewers also correctly note that the paper's core thesis — that decoupling the classifier and detector is the right strategy for ZS-NTTA — is well-supported, but that the OOD detection overclaim is an unnecessary vulnerability that distracts from the otherwise solid contribution.

## Suggestions

1. **Reframe the ZS-OOD detection results.** Either (a) compare against test-time-adaptive OOD methods (e.g., Fan et al. 2024, or a simple TTA-baseline applied to OOD), or (b) explicitly acknowledge that the comparison is adaptive vs. static and downgrade the claim from "state-of-the-art" to "competitive despite operating under the harder ZS-NTTA setting."
2. **Add at least 3 seeds for the main ImageNet results** (or report that the pipeline is deterministic and justify why). Report standard deviations in Tables 2–3.
3. **Add an ablation of the adaptive threshold within AdaND** (fixed vs. adaptive) to isolate its contribution.
4. **Remove or soften "state-of-the-art" language for ZS-OOD** throughout the paper (abstract, contributions list, conclusion) unless the comparison is made fair.
5. **Analyze the scale of injected Gaussian noise** (variance sensitivity) to complement the existing ablation on type and frequency.

## Score and Decision

The paper introduces a well-motivated new problem (ZS-NTTA), provides a clear mechanistic analysis of why existing methods fail, and proposes a simple, efficient, and empirically effective solution (AdaND). The core ZS-NTTA contribution is sound and well-supported by extensive experiments. The main weakness is an overclaimed secondary result (ZS-OOD detection) that relies on an unfair comparison protocol. This is fixable and does not undermine the primary contribution. The lack of variance reporting on ImageNet is a secondary concern.

**Score**: 7.0

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>