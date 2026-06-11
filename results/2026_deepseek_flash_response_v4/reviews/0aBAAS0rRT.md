Now I have enough information to finalize. Here is my complete review with calibration analysis:

---

## Summary

SigMap proposes a self-supervised foundation model for wireless localization with two innovations: (1) cycle-adaptive masked modeling that dynamically masks CSI based on detected periodicity to prevent shortcut learning, and (2) map-conditioned prompt tuning where 3D building geometry is encoded via a GNN and injected as soft prompts into a frozen Transformer backbone. The method achieves strong results on DeepMIMO and WAIR-D ray-traced datasets, outperforming baselines by substantial margins (e.g., 34.4% MAE improvement over LWLM in single-BS localization).

## Strengths

- **Cycle-adaptive masking is a principled solution to a genuine periodic-shortcut problem in wireless SSL.** Table 3 shows adaptive masking (0.673 m MAE) outperforms both fixed grid (0.770) and strip (0.753) masking, confirming the mechanism works as intended.

- **The map-as-prompt framework with GNN-encoded 3D geometry is a novel and parameter-efficient transfer mechanism.** Table 4 shows the 3-D map prompt contributes 31% MAE improvement (1.564 m vs. 2.275 m no-map), while Table 5 demonstrates only 0.085M parameters (0.7% of total) are tuned during fine-tuning. Algorithm 1 provides a clear specification of the generation pipeline.

- **Strong and consistent empirical gains across all settings.** SigMap beats LWLM by 34.4% in single-BS MAE, 18.7% in multi-BS, and 53.2% on unseen DeepMIMO O2 — margins large enough to not be explained by random variation.

- **Systematic ablation isolates each component's contribution.** Masking strategy (Table 3), map modality (Table 4), and map presence (Tables 1–2, generalization table) are separately ablated, making attribution of gains transparent.

- **Practical efficiency is demonstrated with concrete numbers.** Table 5 reports 0.83 ms/sample inference, 30 min total fine-tuning over 1000 epochs, and only 0.085M trainable parameters during fine-tuning.

## Weaknesses

### Fatal
None.

### Major

1. **"Zero-shot" claim contradicted by experimental setup.** The abstract (line 9) and contribution list (line 43) claim "strong zero-shot generalization in unseen environments," yet the generalization experiments (Section 4.5, line 317) explicitly state: "only the downstream task heads are fine-tuned using limited target samples (approximately 100 instances per scenario)." This is a few-shot fine-tuning setup, not zero-shot. This is a factual inaccuracy in the paper's central promise and misleads readers about what was actually evaluated. The paper itself even calls it a "few-shot learning setup" at line 317, contradicting its own abstract.

2. **The cycle-adaptive masking mechanism is underspecified for reproducibility.** The core algorithmic innovation (Section 3.3, Eq. 6) depends on $d_{\text{final}}$, the "detected periodicity shift," which is said to be computed via "cross-correlation analysis" (line 134). The paper never specifies: what signal is cross-correlated against what reference? Over which dimension of the CSI tensor (subcarrier, antenna, time)? What algorithm converts the cross-correlation output to scalar $d_{\text{final}}$? How is the mask width $w$ determined? Without these details, the central technical contribution cannot be reproduced or properly assessed. The paper also does not clarify whether "strip-masked" and "grid-masked" in Figure 3 are variants of the adaptive mask or standard random masks.

### Minor

1. **Standard deviations not reported despite claiming 5 independent runs.** Line 239 states results are averaged over 5 runs, but no standard deviations, error bars, or any variance information appear in any table (Tables 1–4, generalization table). Without this information, it is impossible to assess statistical significance. The large margins somewhat mitigate this concern, but it remains a basic reporting requirement.

2. **Evaluation is entirely on synthetic ray-traced data.** Both DeepMIMO and WAIR-D are ray-traced simulations. While this is standard practice in the CSI localization literature, the paper claims "practical deployability" (line 227) and applicability to real-world 5G/6G applications (abstract, conclusion) without any evaluation on measured data. These claims should be tempered to reflect the simulation-only scope, or explicitly acknowledged as a limitation.

3. **Missing important SSL baselines from the comparison.** The related work (lines 26–28) discusses CrowdBERT and WirelessGPT as directly relevant SSL-based localization methods, but they are not included in the experimental comparison (Section 4.2). While LWLM and SWiT are included as baselines, omitting these closely related methods weakens the comparative claims. The paper should either include these baselines or justify their exclusion.

4. **NLoS-aware attention mechanism (Eq. 11) appears without architectural context.** Equation (11) is introduced in Section 4.2 as explaining "the key advantage" — "our NLoS-aware attention mechanism that explicitly models multi-path propagation." Yet this mechanism was never described in the methodology (Section 3). The notation $\mathbf{o}_s^{(i)}$ is not defined, and it is unclear whether this is part of the backbone, the prompt mechanism, the task head, or something separate. Additionally, the paper claims "interpretable fusion" as a contribution (line 42) but provides no attention maps, visualizations, or analysis demonstrating interpretability.

5. **Only two baselines reported for generalization experiments (Section 4.5).** SWiT, CNN, and OMP are dropped in the cross-scenario evaluation, making the generalization claims less comprehensive.

### Trivial
None.

## Nice-to-Haves

- An ablation isolating the periodicity detection itself (e.g., applying the adaptive pattern using random shifts vs. detected periodicity) would clarify whether the benefit comes from detection or the adaptive structure.
- Discussion of why SigMap's RMSE/MAE ratio in single-BS (3.63) is much larger than LWLM's (2.44), suggesting a long error tail worth explaining.
- A comparison to LoRA or adapter-based fine-tuning to contextualize the parameter efficiency claims against standard alternatives.
- Attention-map visualizations showing how prompt tokens interact with CSI tokens in LoS vs. NLoS conditions to support the interpretability claim.

## Removed Points

These points are flagged to be removed, treat them with caution:
- **"No evidence that periodicity shortcuts degrade existing methods"** — Speculative demand that the paper prove a negative. The ablation in Table 3 indirectly addresses this.
- **"LLM hallucination claim uncited"** — Minor citation issue, not a core weakness of the paper.
- **"RMSE/MAE ratio discussion"** and **"Table 2 improvement modest"** — Nitpicky observations about result interpretation, not actual weaknesses.
- **"Table 3 ablation conflates two changes"** — A refinement request, moved to Nice-to-Haves.
- **"No LoRA/adapter comparison"** — Nice-to-have, not a core flaw.
- **"Missing related works"** — Rule prohibits mentioning missing related works.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Fix the zero-shot claim.** Either rename to "few-shot" or "cross-scenario generalization" in the abstract and contributions, or run an actual zero-shot evaluation (direct transfer with no fine-tuning). The former is faster and still valuable.
2. **Fully specify the cycle-adaptive masking algorithm.** Provide a pseudo-code algorithm showing exactly how $d_{\text{final}}$ is computed from cross-correlation, which dimensions are involved, and how $w$ is determined.
3. **Report standard deviations** for all main metrics. This is low-effort and would significantly improve credibility.
4. **Clarify the NLoS-aware attention (Eq. 11).** Either integrate it into the methodology section with proper notation, or remove it from the experiments if it is not actually part of SigMap.
5. **Add missing SSL baselines** (CrowdBERT, WirelessGPT) or explicitly justify their exclusion.

## Score and Decision

**Calibration analysis:**

*Round 1 bracket:* I determined this paper sits between 4.5 and 6.5 based on initial comparisons.

*Anchor papers retrieved across all rounds:*

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| `9TClCDZXeh.md` (Wireless Simulation with Geometric Transformers) | 7.00 | R1 | Stronger: has real-world validation, clearer architecture novelty |
| `29JDZxRgPZ.md` (EM-GANSim) | 6.00 | R1, R2 | Comparable: similar issues (missing details, synthetic eval) but SigMap has better ablations |
| `7KDuQPrAF3.md` (Foundation Model for Error Correction) | 6.25 | R1 | Slightly stronger: comparable evaluation scope but clearer method specification |
| `7ipjMIHVJt.md` (DASFormer) | 5.25 | R1, R2 | Weaker: less technical novelty, worse ablations |
| `q3WzT2mrhB.md` (WiFi Mesh Regression) | 4.00 | R1 | Much weaker: limited novelty, poorer evaluation |
| `4S2L519nIX.md` (All-Atom GNNs Pre-Training) | 6.50 | R2 | Slightly stronger: more comprehensive experiments despite similar "zero-shot" overclaim |
| `Pj3ErOxlLo.md` (NaviFormer) | 6.00 | R2 | Comparable but stronger evaluation (includes real-world data) |
| `72MSbSZtHv.md` (RedMotion) | 5.33 | R2 | Similar score range |
| `CiiLchbRe3.md` (Pretrained Transformer for Decision Making) | 5.25 | R2 | Similar score range |

*Round 2 narrowing:* After reading full reviews of anchors in the ~5–7 range, I narrowed to 5.0–6.0.

*Final positioning:* SigMap is clearly stronger than DASFormer (5.25) and WiMTR (4.0), comparable to EM-GANSim (6.0) but with significant issues (zero-shot claim error, underspecified core method) that the 6.0 papers do not have. It is weaker than the Geometric Transformers paper (7.0) and the Geom-GNN paper (6.5). The most appropriate position is **5.5**.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>