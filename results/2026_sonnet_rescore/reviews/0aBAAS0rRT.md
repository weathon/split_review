Now I have read the paper in full. Let me write the final meta-review, verifying each claim against the text.

---

## Summary

SigMap is a two-stage wireless localization foundation model that combines (1) a cycle-adaptive masked auto-encoding pre-training strategy designed to prevent shortcut learning in periodic CSI signals, and (2) a GNN-based "map-as-prompt" fine-tuning mechanism that encodes 3D building geometry via Delaunay-triangulated graph convolutions into soft prompt tokens prepended to a frozen transformer backbone. The method is evaluated on simulated DeepMIMO and WAIR-D datasets across single-BS NLoS, multi-BS collaborative, and cross-scenario generalization settings.

---

## Strengths

- **Map-as-prompt mechanism produces large, cleanly ablated gains.** Table 4 shows a controlled 3-tier ablation (3D mesh → 2D bird's-eye polygon → no map) on single-BS NLoS: MAE moves from 1.564 m to 1.692 m (+8% relative) to 2.275 m (+45% relative). The finding that most benefit comes from topological/LoS cues rather than 3D height detail is a specific and informative result, and the suggestion of visual prompts as a future direction is well-grounded in this finding.

- **Parameter efficiency of the fine-tuning stage is concretely demonstrated.** Table 5 reports 0.085 M trainable parameters during fine-tuning (<1% of total), with complete adaptation in 30 minutes over 1000 epochs. This is a practical advantage clearly substantiated by numbers.

- **Cross-scenario generalization results are substantial.** Table 4.5 shows SIGMAP (w/ map) at 1.026 m MAE on the entirely unseen DeepMIMO O2 and 1.880 m on WAIR-D Scenario-2 (100 real-world cities from OpenStreetMap), compared to LWLM at 2.213 m and 3.375 m respectively — reductions of ~54% and ~44%, with only task heads and the GNN prompt network updated (~100 labeled samples).

- **Multi-BS masking ablation confirms the cycle-adaptive strategy improves MAE and CDF@1m.** Table 3 shows adaptive masking at 0.673 m MAE and 84.5% CDF@1m vs. grid (0.770 m / 80.3%) and strip (0.753 m / 75.3%). The intuition — that disrupting periodic structure forces the backbone to learn global signal semantics — is coherent and supported by the MAE and CDF improvements.

---

## Weaknesses

### Fatal
None.

### Major

- **No map-capable baseline isolates the prompt mechanism contribution.** All baselines (OMP, CNN, SWiT, LWLM) operate on CSI alone with no access to the 3D map M, while the headline system "SIGMAP (w/ map)" receives 3D building geometry through the GNN prompt. Section 4.2 claims a 34.4% MAE improvement and more-than-doubled CDF@1m over LWLM, framing this as evidence of a superior foundation model. However, the performance gap cannot be attributed to model design alone when one system has a strictly richer input modality. The SIGMAP (w/o map) ablation shows the backbone alone is only marginally better than LWLM (2.275 m vs. 2.382 m MAE in Table 1; 0.789 m vs. 0.828 m in Table 2), meaning the headline claim rests almost entirely on map access rather than architectural superiority. Without at least one map-capable baseline — even a simple CNN or LWLM variant that also receives map features — readers cannot tell whether the gain stems from the *GNN prompt encoding* specifically or simply from *having a map at all*. The paper's core claim should be demonstrating that its specific map encoding mechanism is the right way to use geographic information, not merely that maps help.

- **"Zero-shot" claim in the abstract directly contradicts the experimental protocol.** The abstract states "exhibiting strong zero-shot generalization in unseen environments," and Section 1.2 repeats "strong zero-shot generalization." However, Section 4.5 explicitly states: *"only the downstream task heads are fine-tuned using limited target samples (approximately 100 instances per scenario), while the self-supervised backbone remains frozen."* This is few-shot fine-tuning of the task head and GNN prompt network (0.085 M parameters), not zero-shot inference. Zero-shot has a specific meaning in the transfer learning literature: no target samples, no updated parameters. The mismatch between the abstract claim and the experimental protocol is not a framing preference — it is an overclaim that propagates through the paper.

- **Equation (11) is a ghost architectural component.** In Section 4.2, the paper introduces an "NLoS-aware attention mechanism" in Eq. (11) with a weight matrix W_NLoS and claims it "allows the model to differentiate between direct and reflected paths, significantly reducing positioning ambiguity." This equation does not appear anywhere in Section 3 (the methodology), is not defined in the GNN pipeline (Algorithm 1) or the prompt-integration equations (Eqs. 9–10), and is never ablated. It is unclear whether W_NLoS is a real trained parameter, a post-hoc reinterpretation of attention weights, or an error. If it is a real architectural component contributing to the results in Table 1, it must be specified in Section 3 and ablated. As written, it creates an unverifiable component inserted in the results section.

### Minor

- **Table 3 presents an unaddressed RMSE inconsistency.** Strip-masking achieves RMSE of 0.972 m, while the paper's proposed adaptive masking achieves 1.099 m — adaptive masking has *worse* RMSE by 13%. The paper presents adaptive masking as the superior strategy ("best trade-off") but does not acknowledge or explain this regression. If the adaptive approach shifts the error distribution differently (e.g., reducing median error while increasing tail error), that is a meaningful finding worth discussing rather than silently overlooking.

- **Numerical inconsistency between Section 4.5 text and Table 4.5.** The text in Section 4.5 states "SIGMAP reaches 1.026 m MAE on DeepMIMO O2 and 1.580 m on WAIR-D Scenario-2," but Table 4.5 reports 1.880 m for SIGMAP (w/ map) on WAIR-D Scenario-2. The 300 mm discrepancy is not a rounding artifact and requires correction.

- **Figure 5 radar chart references undefined metrics and an undefined baseline.** The chart includes dimensions "AoA," "ToA," and "oss_scenario" that appear nowhere in the tables or text, and compares against a method "CMP" that is never defined or cited in the paper. This suggests the figure may carry over from an earlier version of the experiments. It raises uncertainty about whether the paper's results are fully self-consistent.

### Trivial

- **Simulation-only evaluation.** All experiments use ray-traced channels (DeepMIMO O1/O2, WAIR-D). The sim-to-real gap for wireless channels in NLoS environments is acknowledged broadly in the field. For an ML conference paper this is not unusual, but noting it as a limitation would strengthen the paper's self-awareness of scope.

---

## Nice-to-Haves

- Include at least one map-capable baseline (e.g., a map-feature-concatenated LWLM or MLP) to separate the contribution of *having* a map from the contribution of the *GNN prompt encoding mechanism*. This would make the paper's core architectural claim substantially more credible.
- A mechanistic visualization of what the backbone learns under adaptive vs. strip masking — such as attention maps, nearest-neighbor retrieval quality in representation space, or per-frequency reconstruction error — would strengthen the cycle-adaptive masking contribution beyond the partially inconsistent numbers in Table 3.
- Genuine zero-shot evaluation (frozen backbone, frozen task head, direct inference on unseen environments) as a supplementary experiment would let the paper earn its "zero-shot" framing.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic: "Underspecified cross-correlation procedure in Section 3.3."** Section 3.3 describes the adaptive masking conceptually but defers implementation details to Appendix B.3. Since the appendix is stripped from the reviewed version, this is not attributable to the authors. Removed per the rule against criticizing missing appendix content.

- **Strength Finder: "Strong zero-shot generalization" (Strength 3 framing).** The generalization results are real, but the framing as "zero-shot" is factually wrong per Section 4.5. Retained the underlying performance result as a strength but removed the zero-shot characterization.

- **Strength Finder: "Comprehensive evaluation against diverse baselines / radar chart (Figure 5)."** The radar chart (Figure 5) references undefined metrics and an unknown baseline "CMP," undermining its evidential value. The tabular comparisons (Tables 1–2) do cover four baseline types. Removed the radar chart as supporting evidence; the tabular breadth is noted but weakened by the absence of any map-capable baseline.

- **Strength Finder: "Realistic data and evaluation scenarios."** The data is ray-traced simulation, not real measured CSI. WAIR-D uses OpenStreetMap geometries but still generates channels via ray tracing. Describing ray-traced data as "realistic" or "close to physical wireless environments" is an overstatement. Removed as a standalone strength; the generalization to 100 diverse WAIR-D city scenes is a real practical signal retained elsewhere.

---

## Novel Insights

The most genuinely novel and practically important finding in this paper is the map-quality ablation (Table 4): a 2D bird's-eye polygon preserves ~85% of the localization benefit of a full 3D mesh (MAE 1.692 m vs. 1.564 m), while removing the map entirely costs 45% relative degradation. This suggests that for wireless localization, LoS/NLoS topology and floor-plan boundaries are the dominant geometric cues — not facade height or 3D structure — which has direct implications for how future map-conditioned localization systems should be designed. The suggestion to replace 2D maps with street-level photographs (visual prompts) as a low-cost substitute is well-motivated by this finding. The observation that the backbone alone barely beats LWLM (2.275 m vs. 2.382 m) while the combined system halves the error (1.564 m) is also informative: it reveals that map availability, not representational superiority, is the main driver of performance, which the paper should acknowledge more directly.

---

## Suggestions

1. **Restructure the main comparison claim.** Reframe Tables 1 and 2 to compare SIGMAP (w/ map) against a map-capable baseline variant, and present the w/o-map comparison as the measure of architectural transfer quality. This is the honest structure for the paper's contribution.

2. **Correct the abstract and Section 1.2.** Replace "zero-shot generalization" with "few-shot generalization" throughout. The few-shot protocol (100 labeled samples, 0.085 M updated parameters, 30 min) is itself a compelling practical result — it does not need to be oversold as zero-shot.

3. **Move Eq. (11) into the methodology and ablate it**, or remove it from Section 4.2. It cannot remain an undefined, unablated component appearing only in the results discussion.

4. **Address or acknowledge the RMSE regression in Table 3.** If adaptive masking trades tail error for median error, say so and quantify the trade-off.

5. **Fix the 1.580 m / 1.880 m discrepancy** in Section 4.5 / Table 4.5.

6. **Audit Figure 5.** Remove or define the AoA, ToA, oss_scenario dimensions and the "CMP" baseline, or replace the figure entirely with a cleaner visualization of the tabular results.

---

## Assessment

**Originality:** The map-as-prompt mechanism is a novel combination of GNN-based scene encoding and soft prompt injection into a frozen transformer. The cycle-adaptive masking idea is also original, though less compellingly demonstrated. The overall framework borrows heavily from NLP prompt tuning and MAE pretraining applied to wireless channels. Moderate-to-good originality.

**Importance of research question:** Cross-environment wireless localization generalization is a practically significant problem for 5G/6G deployment. The question of how to incorporate geographic map data efficiently is well-posed and relevant.

**Claims supported by evidence:** Partially. The map-ablation claim (Table 4) and the parameter-efficiency claim (Table 5) are well-supported. The headline performance advantage (Tables 1–2) conflates modality advantage with architectural advantage. The "zero-shot" claim is not supported by the experiments. The masking claim (Table 3) is mixed due to the RMSE regression.

**Soundness of experiments:** Adequate for the multi-BS and map-ablation sections. The missing map-capable baseline is a meaningful gap. The simulation-only setting is field-standard but limiting. Figure 5 introduces unexplained inconsistencies.

**Clarity of writing:** The methodology sections (3.3, 3.4) are reasonably well-written. The introduction of Eq. (11) in the results section is a structural error. The zero-shot/few-shot mislabeling is a repeated clarity failure. The 1.580/1.880 discrepancy is a careless error.

**Value to research community:** The map-as-prompt framework is a useful contribution to the wireless-AI intersection. The parameter-efficient adaptation result is practically valuable. The paper's current presentation dilutes these contributions with overclaims and inconsistencies.

---

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>

<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>2</claims_supported>
<soundness>2</soundness>
<clarity>3</clarity>
<community_value>3</community_value>
</subscores>