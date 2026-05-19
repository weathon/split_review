- Decision: Reject
- Avg Score: 3.80
- Scores: 3, 5, 3, 5, 3
Now I have all the information needed. Let me produce the consolidated review.

## Summary

SUMMER proposes a framework for Multimodal Emotion Recognition in Conversations (MERC) combining three core modules: (1) Sparse Dynamic Mixture of Experts (SDMoE) for token-wise dynamic expert selection with differentiable sparse routing, (2) Hierarchical Cross-Modal Fusion (HCMF) with teacher-guided attention masking and residual connections, and (3) Interactive Knowledge Distillation (IKD) where a frozen unimodal (text) teacher guides a multimodal student in both latent and logit spaces. The method is evaluated on IEMOCAP and MELD, reporting improvements over prior SOTA, particularly on minority and semantically similar emotion classes.

## Strengths

- **Novel retrograde distillation from unimodal teacher to multimodal student**: The paper introduces Interactive Knowledge Distillation (IKD, §3.6) where a pre-trained text-only teacher supervises a multimodal student via intermediate feature masking (DynAttn), KL-divergence in logit space, inner feature MSE, and label smoothing. Ablation (Table 4) confirms IKD is the single most impactful component — removing it causes the largest performance drop across emotion categories. This retrograde setup (smaller-teacher-guides-larger-student) is a genuine departure from the typical large-teacher-distills-small-student paradigm in MERC.

- **Sparse Dynamic MoE with differentiable routing**: SDMoE (§3.4) replaces fixed Top-K expert selection with a dynamic gating mechanism that statistically deactivates experts outside (μ−2σ, μ+2σ) and uses Gumbel-Softmax for differentiability. Ablations (Table 4, "Replace SDMoE with MoE") show consistent degradation across all emotion categories, confirming the dynamic routing is beneficial beyond what a static MoE provides.

- **Systematic component-level ablation**: The ablation study (Tables 3–4) separately removes/replaces SDMoE, HCMF, IKD, and sub-losses within IKD, and compares different teacher modalities (Table 3). This allows readers to attribute gains to individual modules. The fact that IKD removal causes the largest drop and that text teachers outperform multimodal teachers supports the core architectural claims.

- **Demonstrated gains on minority and confusable emotion classes**: The paper reports specific per-class improvements — e.g., +15.5% F1 in "Fear" over CORECT on MELD, +9.76% w-ACC in "Happy" on IEMOCAP, +3.32% in "Frustration" — which go beyond just top-line metrics and support the claim that the method helps with underrepresented and semantically similar categories.

## Weaknesses

### Major

- **No statistical significance or variance reported across runs**. All results in Tables 1–4 appear to be from single runs. Given the framework's complexity (multiple interacting modules: SDMoE routing with Gumbel noise, HCMF masking, IKD with four loss terms), the reported improvements — especially the 2.61% w-ACC gain on IEMOCAP — could fall within run-to-run variance. Without error bars or multi-seed reporting, the reliability of the claimed improvements is unverifiable. This is the most significant methodological gap.

- **Gradient conflict claim is motivation-level only, never empirically validated**. The paper repeatedly invokes "gradient conflicts from modal heterogeneity" (abstract, §1, §3.6) as the central motivation for IKD, but provides no measurement or visualization of gradient behavior (e.g., gradient cosine similarity between modalities with and without IKD). The claim that IKD "reduces gradient conflicts" remains an untested hypothesis in the paper as written.

- **Key hyperparameters and design choices are underspecified or unablated**. 
  - The dynamic routing threshold (μ−2σ, μ+2σ) in Eq. 2 is given without any sensitivity analysis. Why 2σ? 
  - The masking threshold of 0.5 in Eq. 4 is similarly unexamined.
  - The dynamic adjustment factor φ in Eq. 6 is introduced but never given a value or range.
  - The number of experts (n), hidden sizes of BiGRU experts, and temperature parameter T are mentioned but not specified.
  
  These are not formatting nits — they are architectural knobs that could affect performance, and their values are absent from the paper. (Some may reside in the stripped appendix, but the main text should at minimum state them.)

### Minor

- **The retrograde distillation hypothesis is only partially isolated**. The ablation removes IKD entirely (no distillation). Table 3 does compare unimodal vs. multimodal *teachers*, showing text-only works best. However, the paper does not test whether the benefit comes specifically from the teacher's *unimodality* vs. from having any distillation signal. A comparison replacing the unimodal teacher with a self-distillation setup (as used in the SDT baseline) while keeping other SUMMER components fixed would isolate this. This limits the strength of the claim that "retrograde" (unimodal-to-multimodal) distillation is the operative mechanism, vs. distillation itself.

- **Baseline comparison protocol is unclear**. The paper does not specify whether baseline numbers in Tables 1–2 are taken from published papers or re-implemented under controlled conditions. While citing published results is standard practice in MERC, this makes it impossible to rule out differences in feature extractors, data splits, or tuning protocols as confounds. At minimum, the paper should state the source of each baseline number.

### Trivial

- None that survive filtering (parser artifacts removed).

## Nice-to-Haves

- A sensitivity sweep for the μ±kσ range (k ∈ {1, 1.5, 2, 2.5}) and the HCMF mask threshold (0.3–0.7) would strengthen claims about robustness.
- Reporting training/inference time or parameter counts would contextualize the complexity added by SDMoE and IKD.
- Quantitative separability metrics (silhouette score, NMI) for the t-SNE visualization would strengthen the qualitative clustering claim.

## Removed Points

- **"The evaluation does not provide a fair or controlled comparison with baselines"** — demoted from the critic's framing. Citing published results under standard splits is the convention in MERC. While the paper should state the source of each baseline number, this is a minor clarity issue, not a structural flaw. The concern is moved to Minor.
- **"Does not test whether a unimodal teacher is better than a multimodal teacher"** — REMOVED. Table 3 explicitly compares different teacher modality combinations. The paper states "the text modality consistently outperforms others" and that combining text with other modalities yields only "marginal performance gains." The critic's assertion is factually incorrect; the paper does test this.
- **"Missing related works"** — REMOVED per instructions (cannot verify existence of missing citations).
- **"Formatting nitpicks / reproducibility complaints about missing appendix"** — REMOVED. The appendix was stripped by the parser. The paper references §A.1 and §A.2 for details; these exist in the original submission.

## Novel Insights

None beyond the paper's own contributions. The two reviews surface a legitimate tension: the paper proposes a well-articulated architecture with clean ablations, but the evaluation lacks the statistical rigor (no error bars, no sensitivity analysis on thresholds, unvalidated gradient-conflict narrative) needed to fully support its strongest claims. The most useful observation from the reviews is that the paper's central motivation — gradient conflicts — is entirely unmeasured, which is a missed opportunity to make the contribution more convincing.

## Suggestions

1. **Report mean and std over at least 3–5 random seeds** for all main results and ablations. This single change would address the most glaring evaluation gap.
2. **Add a comparison replacing IKD with self-distillation** (while keeping SDMoE and HCMF) to isolate whether the teacher's unimodality matters vs. distillation being applied at all.
3. **Specify all missing hyperparameters** (number of experts, hidden sizes, T, φ value/range) and add a brief sensitivity analysis for the two thresholds (k in μ±kσ and the 0.5 mask cutoff).
4. **Add a gradient analysis** (e.g., cosine similarity between modality gradients with/without IKD) to empirically support the gradient-conflict motivation.
5. **State the source of each baseline number** (original paper citation vs. re-implementation) to clarify the comparison protocol.
