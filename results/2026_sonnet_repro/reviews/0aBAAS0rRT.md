Now let me run calibration searches to properly score this paper.Round 1 bracket: **3.5 to 5.5**. The paper's contributions are real but have several verifiable issues. Let me narrow.Now I have sufficient calibration data. Let me write the final consolidated review.

---

## Summary

SigMap proposes a two-stage wireless localization foundation model combining: (1) a cycle-adaptive masked autoencoding pretraining strategy that disrupts CSI periodicity to prevent shortcut learning, and (2) a GNN-based "map-as-prompt" mechanism that encodes 3D building geometry into soft prompt tokens prepended to a frozen transformer backbone during fine-tuning. Experiments on ray-traced DeepMIMO and WAIR-D datasets show improvements over supervised and self-supervised baselines, particularly when geographic prompts are used.

---

## Strengths

- **Map-as-prompt yields large, consistent gains with ablation support.** Table 4 isolates the geographic prompt's contribution: 3D mesh gives MAE 1.564 m, 2D bird's-eye gives 1.692 m, no map gives 2.275 m. The finding that 2D polygon captures most topological benefit is informative and well-controlled.
- **Genuine parameter efficiency.** Table 5 reports 0.085 M trainable parameters during fine-tuning (~0.4% of total), 30-minute fine-tuning time versus 36-hour pretraining. This is a concrete practical advantage, not a generic claim.
- **Cross-scenario transfer results are competitive.** Table 4.5 shows SIGMAP outperforms LWLM by ~53% on DeepMIMO O2 and ~44% on WAIR-D Scenario-2 with only task-head updates, demonstrating the backbone's transferability.
- **Multi-BS collaborative localization shows a clean story.** Table 2 gives a natural hierarchy: SIGMAP w/ map (0.673 m) > SIGMAP w/o map (0.789 m) > LWLM (0.828 m) > SWiT (1.102 m), with increasing gaps toward simpler baselines.

---

## Weaknesses

### Fatal
None — no weakness fully invalidates the core results.

### Major

- **Zero-shot claim in abstract directly contradicts the experimental protocol.** The abstract asserts "strong zero-shot generalization in unseen environments," and Section 1.2 repeats "zero-shot generalization." But Section 4.5 explicitly says: *"only the downstream task heads are fine-tuned using limited target samples (approximately 100 instances per scenario)"* and calls it *"This few-shot learning setup."* Fine-tuning the task head on 100 target samples is *few-shot*, not zero-shot — these terms have distinct meanings in transfer learning. The mismatch between the abstract's "zero-shot" framing and the actual experimental protocol is not a minor qualification; it overclaims the generalization capability. The abstract and Section 1.2 must be corrected to describe the actual protocol.

- **Equation (11) is introduced without definition and not grounded in the methodology.** Section 4.2 states: *"The key advantage stems from our NLoS-aware attention mechanism that explicitly models multi-path propagation"* and presents Eq. (11) with notation `W_NLoS` and `o_s^(i)`. Neither term appears anywhere in Section 3 (methodology). This equation is absent from the architecture description, is not ablated, and its relationship to Equations 9–10 (multi-BS fusion attention) is unexplained. If this is a real architectural component that contributes to Table 1 performance, it must be defined in Section 3 and ablated. If it is post-hoc interpretation, it should be removed. As written, it creates an undocumented ghost component that undermines methodological integrity.

- **Figure 5 radar chart contains unexplained metrics and an unidentified baseline.** The radar chart lists dimensions "AoA," "ToA," and "oss_scenario" that are not reported in any table or discussed in the text. The chart also includes a method labeled "CMP" that is never named anywhere in the paper. These elements suggest the figure may be a carry-over from a different version of the experiments, raising questions about result completeness and accuracy.

- **No map-capable baseline isolates the prompt encoding contribution from simply having map data.** All baselines (OMP, CNN, SWiT, LWLM) are map-blind, so the gap between SIGMAP (w/ map) and SIGMAP (w/o map) demonstrates that map data helps localization — a well-established fact. The paper provides no map-aware baseline (e.g., concatenating map features to LWLM or a map-conditioned MLP) to demonstrate that the GNN-prompt encoding mechanism itself is the correct way to incorporate geographic information, beyond the simpler alternative of just feeding map features into the baseline architectures.

### Minor

- **Table 3 RMSE inconsistency is not addressed.** Strip-masking achieves RMSE of 0.972 m while adaptive masking achieves 1.099 m (the same as full 4-BS SIGMAP w/ map). The paper presents adaptive masking as superior but does not explain why a metric (RMSE) that penalizes outliers more heavily favors strip-masking. This could reflect a distribution shift in errors, but the paper is silent.

- **Numerical inconsistency between Section 4.5 text and Table 4.5.** The text states *"SIGMAP reaches 1.026 m MAE on DeepMIMO O2 and 1.580 m on WAIR-D Scenario-2"* but the table reports 1.880 m for WAIR-D Scenario-2. The text figure (1.580) and table figure (1.880) cannot both be correct.

- **Simulation-only evaluation limits the scope of practical claims.** All experiments use ray-traced data (DeepMIMO, WAIR-D). The abstract and introduction motivate the work via "autonomous driving, extended reality, and smart manufacturing." No measured channel data is included. The sim-to-real gap in NLoS environments (hardware impairments, unmodeled clutter, calibration errors) is known, and not being tested on any real measurements is a meaningful limitation that the paper should acknowledge more clearly.

### Trivial

- Section 3.3 provides Equation (6) but does not specify how `d_final` is derived from the cross-correlation output (which rows are correlated, what happens with multiple periodicities).

---

## Nice-to-Haves

- A map-aware baseline using a simpler map-encoding strategy (e.g., MLP on concatenated map statistics fed to LWLM) would significantly strengthen the case that GNN-based prompt encoding is the right mechanism, not just that map information helps.
- Visualizing what the backbone attends to differently under adaptive vs. strip masking (e.g., attention maps, nearest-neighbor retrieval in representation space) would make the masking contribution more mechanistically credible.
- Stratifying generalization errors by scene complexity in WAIR-D (100-city evaluation) would provide insight into when the model transfers well vs. poorly.

---

## Removed Points

*These points are flagged for removal; treat them with caution.*

- **Harsh critic's "unfair comparison invalidates the headline claim"** — DEMOTED to Major (map-capable baseline gap). The map-as-prompt IS the paper's stated contribution; comparing map-aware SIGMAP against map-blind baselines is the intended demonstration. The genuine concern is narrower: whether a simple map-conditioned baseline would match the GNN-prompt design. This doesn't invalidate the headline, it narrows the interpretable contribution.

- **Simulation-only evaluation as a "decisive problem"** — DEMOTED to Minor. Simulation-only evaluation is widespread in the wireless localization literature, and WAIR-D uses geometry derived from real OpenStreetMap cities. This limits the strength of practical claims but does not invalidate them.

- **Strength: "Realistic data and evaluation scenarios"** — REMOVED. The claim of "conditions close to physical wireless environments" is too strong given all experiments are ray-traced and there is no real-measurement validation.

- **Strength: "Comprehensive evaluation against diverse baselines"** — REMOVED for being generic/superficial. The baselines are limited to 4 methods and all are map-blind, making "comprehensive" a stretch.

---

## Novel Insights

SigMap's radar chart inconsistency (Figure 5 containing unreported metrics and an unnamed baseline "CMP") and the WAIR-D numerical discrepancy (1.580 m in text vs. 1.880 m in table) together suggest the paper may have been assembled from an earlier experimental version without full reconciliation. The undefined Eq. (11) fits the same pattern: an explanation from a prior model version inserted into the results without updating the methodology. Authors should audit all cross-references between figures, tables, text claims, and the methodology before resubmission.

---

## Suggestions

1. Rename "zero-shot generalization" throughout to "few-shot fine-tuning with frozen backbone" to accurately describe the protocol.
2. Either introduce Eq. (11) properly in Section 3 with an ablation, or remove it from Section 4.2.
3. Reconcile Figure 5 — remove or explain "AoA," "ToA," "oss_scenario," and "CMP," or add the corresponding experiments to the paper.
4. Fix the Section 4.5 text to match the table value for WAIR-D Scenario-2 (1.880 m, not 1.580 m).
5. Add a map-capable baseline (even a simple concatenation-based one) to isolate the GNN-prompt contribution from the value of having map data.
6. In the ablation (Table 3), acknowledge and discuss the RMSE regression under adaptive masking.

---

## Score and Decision

**Calibration anchors:**

| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| 9TClCDZXeh (Differentiable Wireless Simulation w/ Geometric Transformers) | 7.00 | R1 | Accept; stronger — real-world validation, cleaner methodology, no undefined equations |
| 7ipjMIHVJt (DASFormer, self-supervised signal pretraining) | 5.25 | R1 | Reject; comparable issues — evaluation coverage gaps, comparison fairness concerns |
| NeVbEYW4tp (Self-TPT, prompt tuning for VLMs) | 5.00 | R2 | Reject; similar tier — useful contribution but evaluation issues |
| XTwwtlEfTF (Robust Multimodal with Parameter-Efficient Adaptation) | 4.50 | R2 | Reject; slightly weaker contribution |
| ryIHtXE9uG (In-context Fine-tuning for Time-Series Foundation Models) | 5.60 | R2 | Reject; cleaner methodology than SigMap, fewer definitional inconsistencies |

**Round 1 bracket:** 3.5–5.5  
**Round 2 narrowing:** The paper's real contributions (map-as-prompt ablation, parameter efficiency, transfer results) align it with the 5.0–5.25 range. However, the combination of: a zero-shot/few-shot abstract mismatch that is directly contradicted in the body text, an unexplained equation in the results section with notation absent from the methodology, a radar chart with unreported dimensions and an unnamed baseline, and a numerical inconsistency between text and table push it slightly below DASFormer (5.25). These are not speculative gaps — each is directly verifiable from what is on the page, and together they suggest the paper was not carefully reconciled before submission.

**Final score: 4.5 — Reject**

**Axes summary:**
- *Originality*: Moderate — cycle-adaptive masking is novel; GNN-prompt tuning for wireless channel adaptation is novel in this domain.
- *Importance of research question*: High — cross-scenario wireless localization is practically critical.
- *Support for claims*: Weak-to-moderate — the zero-shot claim contradicts the text, and a key stated advantage (NLoS-aware attention, Eq. 11) is ungrounded in the methodology.
- *Soundness of experiments*: Fair — ablations are reasonable but marred by RMSE inconsistency, unexplained figure content, and no map-aware baseline.
- *Clarity of writing*: Below average — numerical inconsistency, undefined notation in results section, figure with phantom elements.
- *Value to community*: Moderate — the map-as-prompt idea with concrete parameter efficiency is useful, but the paper's credibility is weakened by the presentation issues.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>