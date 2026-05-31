## Summary
SigMap is a wireless localization foundation model for 5G/6G applications that combines two innovations: (1) cycle-adaptive masked autoencoding that detects CSI periodicity via cross-correlation and generates masks that disrupt periodic shortcuts during self-supervised pre-training; and (2) a "map-as-prompt" framework that encodes 3D building geometry and base-station positions via a GCN on a Delaunay triangulation graph, injecting the result as soft prompt tokens into a frozen transformer backbone during fine-tuning. The method is evaluated on DeepMIMO and WAIR-D datasets and claims state-of-the-art localization accuracy with strong cross-environment generalization.

---

## Strengths

- **Cycle-adaptive masking is a well-motivated and novel design**: The insight that periodic CSI patterns can be exploited as reconstruction shortcuts in standard MAE training is technically sound. Computing row-wise cross-correlation to detect dominant periodicity and generating shift-aware masks (Eq. 6) is a concrete, principled fix, and the ablation in Table 3 confirms non-trivial gains (0.673 m vs. 0.770 m vs. 0.753 m for adaptive, grid-only, and strip-only, respectively).

- **The map-as-prompt framework is practical and efficient**: Converting 3D map geometry into GCN-derived soft prompt tokens that are prepended to the frozen transformer input is elegant and parameter-efficient (only 0.7% of parameters updated during fine-tuning; 30 min fine-tuning vs. 36 h pre-training). The ablation in Table 4 shows that even a 2D bird's-eye view retains most of the benefit, suggesting robustness to map quality.

- **Cross-dataset generalization experiments add credibility**: The evaluation on two held-out environments — DeepMIMO O2 and WAIR-D Scenario-2 (100 OpenStreetMap cities) — is broader than typical wireless localization papers. The performance gaps over LWLM (~53% on O2, ~44% on WAIR-D in MAE) are substantial and not trivially attributable to model size alone.

- **Multi-BS attention fusion is well-designed**: The learned weighted fusion of per-BS [CLS] tokens (Eqs. 9–10) enables dynamic prioritization of base stations with favorable geometry, and the multi-BS results (0.673 m MAE, 84.5% CDF@1m) substantiate this claim.

---

## Weaknesses

### Fatal
None identified.

### Major

1. **The "zero-shot" claim in the abstract is factually incorrect.** Section 4.5 explicitly states that "approximately 100 instances per scenario" are used to fine-tune task heads for generalization experiments. This is *few-shot* learning, not zero-shot. Claiming zero-shot generalization is a material misrepresentation of the experimental protocol that will mislead readers.

2. **Baseline fairness is never established.** SIGMAP w/ map receives 3D building mesh and base-station positions that competing baselines (LWLM, SWiT, CNN, OMP) do not appear to receive. It is never stated whether these baselines are given any map information. If they are not, the comparison is a measurement of "our model with extra inputs" vs. "baselines without those inputs" rather than a head-to-head evaluation of the representation learning strategies, which is the core claim.

3. **The foundation model framing is overstated.** Pre-training is conducted exclusively on a single simulated scenario (DeepMIMO O1_3p5). A model pre-trained on one simulated urban layout and fine-tuned on two others does not constitute a foundation model in the sense established in NLP or vision. The cross-scenario gains are plausibly attributable to the map prompt at fine-tuning time rather than large-scale pre-training diversity.

4. **Numerical inconsistency in the generalization results.** Section 4.5 text states "1.580 m on WAIR-D Scenario-2," but the corresponding table reports **1.880 m** MAE for the same configuration. This 18% discrepancy in a headline result is unresolved in the paper.

### Minor

1. **Equation 11 (NLoS-aware attention) appears in Section 4.2 without prior description in the methodology.** This attention mechanism over NLoS paths is invoked to explain single-BS improvements but never described in Section 3. It is unclear whether this is distinct from the multi-BS fusion in Eq. 9 or an additional architectural component.

2. **The radar chart metrics "AoA" and "ToA" (Figure 5) are never formally defined or reported in any table.** Their inclusion in a comprehensive comparison figure without corresponding quantitative results is unverifiable.

3. **The ablation on masking (Table 3) is only on multi-BS 4-BS setting.** Given that cycle-adaptive masking is a pre-training strategy, its benefit should be most visible in representations, but showing its effect only in the easier multi-BS setting leaves open how much it helps in the harder single-BS scenario.

### Trivial
- Minor tension between Algorithm 1 (simple neighborhood sum GCN) and the matrix formula for the GCN update (symmetric normalized Laplacian form); these are equivalent but presented as if distinct.

---

## Nice-to-Haves

- A proper zero-shot experiment where **no** target samples are used and only the geographic prompt is adapted would validate the zero-shot claim.
- Including at least one baseline (e.g., LWLM) augmented with the same 3D map input to isolate the contribution of the representation learning from the contribution of additional geographic inputs.
- A sensitivity analysis on GCN depth and the number of prompt tokens.

---

## Novel Insights

The cycle-adaptive masking strategy offers a transferable insight beyond wireless localization: in any domain where signals exhibit strong periodicity (e.g., audio, biomedical time series, financial data), generic random masking may be insufficient because local periodic interpolation substitutes for genuine representation learning. Explicitly measuring and blocking dominant periodicities before masking is a principled defense against this failure mode. The map-as-prompt framework demonstrates that heterogeneous spatial graphs encoding physical-world geometry can serve as lightweight, environment-specific conditioning signals for frozen transformers — a pattern potentially applicable to other sensing modalities (LiDAR, radar) where scene topology constrains signal physics.

---

## Suggestions

- Correct the abstract and Section 4.5 to use the accurate term "few-shot" (100 samples) rather than "zero-shot."
- Provide a fair baseline comparison by either giving LWLM/SWiT access to the same map information or explicitly evaluating SIGMAP without map against other map-free baselines.
- Resolve the 1.580 m vs. 1.880 m discrepancy in the WAIR-D result.
- Describe Equation 11 in the methodology section if it is part of the architecture, or remove it if it is redundant with Eq. 9.
- Provide quantitative AoA/ToA metrics if they appear in Figure 5.

---

## Score and Decision

The cycle-adaptive masking idea is technically sound and novel within the wireless sensing literature, and the map-as-prompt framework is practical with genuine empirical gains. However, the zero-shot claim is factually contradicted by the paper's own experimental setup (100-sample fine-tuning), the baseline comparison is potentially unfair due to asymmetric map access, and there is an unresolved numerical inconsistency in the headline generalization result. These are not cosmetic issues — they directly undermine the strength and verifiability of the paper's key contributions as stated. The work is worth developing but requires substantive revision before publication.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>