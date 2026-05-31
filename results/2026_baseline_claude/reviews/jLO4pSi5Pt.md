Now I have read the complete paper. Let me write a comprehensive review.

---

## Summary

This paper proposes L-TTA (Long-tailed Test-Time Adaptation), the first method specifically designed for test-time adaptation of Vision-Language Models (VLMs) under long-tailed test distributions. The method introduces three co-designed components: Synergistic Prototypes (SyPs, comprising Deterministic and Exclusionary Prototypes), Rebalancing Shortcuts (RSs using cross-attention with hyper-class vectors regularized by a Class Re-Allocation loss), and Balanced Entropy Minimization (BEM, a theoretically grounded variant of entropy minimization that penalizes over-optimization of confident/head classes). The method is evaluated on 15 datasets across three benchmarks and multiple backbone architectures, consistently outperforming twelve baselines in both accuracy and macro-F1.

---

## Strengths

- **Novel, well-motivated problem setting.** The paper identifies two specific failure modes for LT-TTA with VLMs—Text-induced Tail Erosion and Modality-bias Amplification—and motivates each component of L-TTA as a direct remedy. The distinction from prior unimodal LT-TTA methods (e.g., SAR, DELTA) is articulated with empirical evidence (Figure 1b.2 showing SAR performance collapse on VLM backbones).

- **Comprehensive experimental validation.** L-TTA is tested across three benchmark types (OOD, Cross-Domain, Corruption), three imbalance ratios (10, 20, 50), five backbone architectures (ViT-B/16, ViT-L/14, ViT-H/14, SigLIP-L/16, MetaCLIP-BigG), and twelve baselines covering training-free, prompt-based, visual-adaptation, and prototype-based methods. Gains are consistent: +1.47%/+1.70% OOD Acc./Mac-F1 (imb=10), +2.87%/+2.64% on the Corruption Benchmark (imb=10), and an average of +1.5%/+1.8% across all stronger backbones.

- **Theoretical grounding for BEM.** Propositions 1 and 2 formally show that standard EM widens the gradient gap between head and tail classes, and that BEM explicitly narrows this gap. This analytical justification elevates BEM above a simple heuristic, distinguishing it from prior logit-adjustment methods by handling the nonlinear interactions of EM gradients.

- **Efficiency.** L-TTA (1.45 h on full ImageNet, 1.89 GB GPU memory) outperforms substantially slower training-based methods (WATT: 27.7 h, RLCF: 18.3 h) in both accuracy and macro-F1, with shortcuts trained without gradient propagation through the backbone.

- **Ablations are thorough and transparent.** Each component's marginal contribution is quantified separately on two backbones (Table 6), and sensitivity to four hyperparameters is studied with appropriate ranges (Figure 4). The robustness to dynamic head/tail-class ordering in the stream (Table 7) validates real-world applicability.

---

## Weaknesses

### Fatal
None.

### Major

- **Hyperparameter inconsistency between implementation details and ablation.** Section 4 (Implementation Details) states K = 0.3 as the default for the number of hyper-class vectors in RSs. Section 4.2 (Ablation Studies) tests K ∈ {0.2, 0.4, 0.6, 0.8, 1.0} and concludes K = 0.2 yields best performance. The value K = 0.3 does not even appear in the ablation sweep. If K = 0.2 is optimal, the main-table experiments should use it; if K = 0.3 was used for main results, the claim that K = 0.2 is best is internally contradictory. This casts doubt on the reliability of the reported numbers relative to the stated hyperparameter choices.

- **EP initialization and early-stream behavior are under-analyzed.** The paper's justification for EPs—that they "can always be updated along the datastream" because any sample contributes to all classes—implicitly assumes the prediction distribution P(y|x̃) is well-calibrated from the start. Under severe long-tailed sampling, head-class predictions will dominate early in the stream, causing EPs of tail classes to be primarily updated with features that are only weakly excluded (small φ_c), closely resembling DPs. The paper does not provide an analysis of EP quality as a function of stream position or imbalance ratio, nor does it demonstrate that EPs remain meaningfully distinct from DPs throughout adaptation.

- **Pseudo-label-based class prior estimation may compound head-class bias.** BEM's penalty term relies on continuously updated class priors estimated from pseudo-labels (line 138: "the class prior is continually updated based on the current predicted pseudo-labels"). Under long-tailed conditions, pseudo-labels are themselves biased toward head classes. The paper provides no analysis of how the quality of these prior estimates evolves, or how estimation error propagates into BEM's rebalancing efficacy.

### Minor

- **Artificial LT construction from balanced datasets.** All benchmarks are constructed by subsampling originally (nearly) balanced datasets to impose a specific imbalance ratio. The resulting tail classes may retain high-quality prototypes simply because they already appear in CLIP's pretraining at comparable frequencies to head classes. An evaluation on naturally long-tailed datasets (e.g., iNaturalist, Places-LT) would more faithfully represent real-world conditions.

- **No direct comparison with unimodal LT-TTA baselines in tables.** SAR and DELTA are discussed in the introduction as representative unimodal LT-TTA methods applied naively to VLMs, and Figure 1(b.2) shows their instability. However, neither appears in Tables 1–3 to let readers see their numbers directly alongside L-TTA.

### Trivial

None worth listing separately beyond the K inconsistency noted above.

---

## Nice-to-Haves

- An analysis of the EP-DP feature similarity over the datastream would clarify whether EPs provide genuinely complementary representations or converge toward DPs.
- A unified ablation that fixes K consistently at either 0.2 or 0.3 across all experiments, with explicit acknowledgment of the optimal value.
- Reporting the head-class vs. tail-class breakdown in the main text (currently deferred to appendix) would directly validate the rebalancing claim.

---

## Novel Insights

The paper makes the genuinely insightful observation that applying entropy minimization in a long-tailed online streaming context creates a feedback loop that preferentially sharpens head-class predictions. Proposition 1 formalizes this: because head classes dominate the argmax, their logits receive the most negative gradient from the entropy objective, widening the gap with tail classes beyond the initial distributional imbalance. Connecting this to VLM-specific failure modes—where textual embeddings themselves carry pre-training biases independent of visual input (Text-induced Tail Erosion)—is a meaningful contribution: it shows that LT problems in VLMs are qualitatively different from unimodal LT-TTA because two coupled, independently biased modalities must be jointly rebalanced.

---

## Suggestions

- Align the K hyperparameter between implementation details and ablation, and clarify whether K is an absolute count or a fraction of C.
- Provide a simple time-series analysis (accuracy by stream position) showing that EPs provide well-distributed updates even for tail classes early in training.
- Include at least one naturally long-tailed dataset (iNaturalist or Places-LT) to validate beyond artificially subsampled benchmarks.
- Explicitly report the pseudo-label prior estimation quality (e.g., correlation between estimated and true class frequencies at different stream stages) to validate the BEM mechanism.

---

## Score and Decision

The paper identifies a genuinely novel problem—long-tailed TTA for VLMs—and proposes a well-motivated, efficient solution with consistent empirical gains across an unusually large set of benchmarks and architectures. The theoretical analysis of BEM is a meaningful contribution beyond simple empirical demonstration. The main concern is the internal inconsistency in hyperparameter reporting (K = 0.3 vs. K = 0.2) and the lack of analysis of EP quality under early-stream conditions, which leaves some doubt about whether the design works as claimed or whether performance gains arise from the combination of known components in a favorable experimental regime. These are significant but do not invalidate the core contribution.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>