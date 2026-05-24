Now I have all the evidence I need. Let me synthesize the final review.

## Summary

The paper proposes SigMap, a multimodal foundation model for wireless localization combining two main ideas: (1) cycle-adaptive masking for self-supervised pretraining that dynamically adjusts to periodic CSI patterns, and (2) a map-as-prompt framework that encodes 3D geographic information via GNNs and integrates it as a soft prompt during fine-tuning. The model is evaluated on DeepMIMO and WAIR-D benchmarks, showing strong accuracy improvements over baselines and parameter-efficient cross-scenario adaptation.

## Strengths

- **Cycle-adaptive masking improves over fixed strategies.** Table 3 shows adaptive masking achieves 0.673 m MAE and 84.5 % CDF@1 m on multi-BS localization, outperforming grid-only (0.770 m, 80.3 %) and strip-only (0.753 m, 75.3 %) variants. This directly validates the core motivation—disrupting periodic shortcuts forces the model to learn more meaningful representations.

- **Map-conditioned prompt tuning delivers substantial accuracy gains.** In single-BS localization (Table 1), adding the 3‑D map prompt reduces MAE from 2.275 m to 1.564 m (31 % improvement) and more than doubles CDF@1 m. The multi-BS setting (Table 2) sees MAE drop from 0.789 m to 0.673 m. Table 4 further shows that even a 2‑D bird’s‑eye map retains most of the benefit (MAE 1.692 m vs. no‑map 2.275 m), confirming that the prompt mechanism captures topological constraints effectively.

- **Parameter-efficient cross-scenario generalization.** On the unseen DeepMIMO O2 scenario, fine-tuning only 0.085 M parameters (0.7 % of total) yields 1.026 m MAE, outperforming LWLM by 53.2 % (Table 4.5). On the challenging WAIR‑D dataset (100 cities), the same approach gives 1.880 m MAE vs. LWLM’s 3.375 m. Fine‑tuning completes in 30 minutes (Table 5), demonstrating practical deployability.

- **Ablation on map quality provides actionable insights.** Table 4 quantifies the contribution of 3‑D vs. 2‑D vs. no map, showing most gain comes from topological information rather than fine height details—suggesting a low‑cost deployment path using 2‑D footprints.

## Weaknesses

### Fatal
None.

### Major

1. **Zero-shot terminology is unsupported; the evaluation is few-shot.** The abstract and contribution list claim the model exhibits "strong zero-shot generalization in unseen environments" (lines 20, 55). However, Section 4.5 explicitly describes a *few-shot* setup: "only the downstream task heads are fine-tuned using limited target samples (approximately 100 instances per scenario)" and calls it a "few-shot learning setup" (line 329). Zero-shot inference without any target-domain labels is never conducted or reported. This misrepresentation inflates the claimed capability. The fix is straightforward—replace "zero-shot" with "few-shot" throughout—but as written, the paper claims more than it demonstrates.

2. **The "NLoS-aware attention mechanism" is introduced only in the experiments, not described in the methodology.** Section 4.2 (line 259) states "The key advantage stems from our NLoS-aware attention mechanism that explicitly models multi-path propagation" and gives Equation 11. Yet the Methodology section (Section 3) contains no description of this mechanism, no explanation of where it fits in the architecture, and no training details. The multi-BS attention fusion described in Section 3.5 (Eq. 9–10) uses different notation and is not clearly connected to Eq. 11. A component claimed as a "key advantage" must be fully specified in the method description, not only in the experimental section. This omission makes the architecture incomplete as presented.

### Minor

3. **Cycle-adaptive masking algorithm is underspecified.** Section 3.3 states that "shift patterns are computed using cross-correlation analysis" and gives Eq. 6, but does not describe what form the cross-correlation takes, how the periodicity shift \(d_{\text{final}}\) is derived from data, or how the mask width \(w\) is set. While some details may reside in the (now-stripped) appendix, the main text should provide a clear enough description for readers to understand what was actually done.

4. **Baseline comparisons lack sufficient context.** The paper does not state how baselines (OMP, CNN, SWiT, LWLM) were configured, whether hyperparameters were tuned, or whether they received the same fine-tuning samples in the generalization experiments. The very high RMSE of LWLM (11.837 m on DeepMIMO O2) relative to its MAE (2.213 m) is unusual and suggests it may not have been optimally adapted, raising questions about the fairness of the reported margins.

5. **Map-as-prompt is not compared against simpler map-integration baselines.** The ablation (w/ map vs. w/o map) shows the benefit of map information, but the paper does not compare against more straightforward ways of incorporating map data (e.g., concatenating map features as additional input channels). Without such a comparison, it is difficult to attribute the gains specifically to the *prompt mechanism* rather than to the mere presence of map information.

6. **Text/table discrepancy.** The text (line 352) reports WAIR‑D MAE as 1.580 m, but the table (line 348) shows 1.880 m. The stated improvement (44.3 %) matches the table value, confirming the text contains an error.

7. **Inconsistent parameter efficiency numbers.** Section 4.5 says "updating only 0.4 % of parameters," while Section 4.6 says "0.7 %." The actual ratio (0.085 M / 11.73 M ≈ 0.72 %) supports the latter, so the 0.4 % is incorrect.

8. **Unanalyzed RMSE increase with adaptive masking.** Table 3 shows adaptive masking yields lower MAE (0.673) than strip masking (0.753) but *higher* RMSE (1.099 vs. 0.972). The paper claims superiority based on MAE and CDF@1 m but does not discuss why RMSE degrades or what this implies about error distribution.

### Trivial

None beyond those listed above.

## Nice-to-Haves

- A limitations subsection discussing sensitivity to map quality, computational cost of Delaunay triangulation at scale, and the domain gap between simulated and real-world CSI would strengthen the paper.
- Statistical significance measures (standard deviations, confidence intervals) for the main results, since only 5-run averages are reported.
- Real-world validation on a measurement campaign would substantially increase the paper's impact.
- Comparison with a simple map-concatenation baseline to isolate the benefit of the prompt mechanism itself.

## Removed Points

These points were flagged by the reviewers but are removed or demoted per the filtering rules:

- **"Method components undisclosed" (excessive framing):** The harsh critic's characterization of the missing NLoS attention as making the method "incomplete" and "unverifiable" is too severe. The component is described (Eq. 11) and the main architecture is otherwise well-specified. The criticism is kept as Major #2 but in a more measured form.
- **"Missing related works on map-integrated localization":** Removed per instructions — I cannot verify the existence or absence of specific related works without external sources.
- **"No proof in appendix / missing proofs":** Removed per instructions — the appendix exists in the original submission; the parser strips it.
- **"No zero-shot results at all":** This conflates "zero-shot not done" with "zero-shot claimed but not done." The paper claims zero-shot but does few-shot; the criticism is kept as Major #1 but re-framed as a terminology mismatch, not a missing experiment.
- **Generic/unsupported strengths from the Strength Finder:** The Strength Finder's generic praise ("addressed an important problem," etc.) is dropped. Only concrete, evidence-backed strengths are retained.
- **"Map-as-prompt not benchmarked against other map-using methods"** — kept as Minor #5 but weakened: the paper does have an ablation (w/ vs w/o map), just not against alternative integration methods.
- **"CDF curves not provided"** — the paper references Appendix B.5, which is stripped. Removed per the appendix rule.

## Novel Insights

The reviews surface a disconnect between the paper's self-presentation and its actual evaluation design: the central claim of "zero-shot generalization" is contradicted by the few-shot setup (Major #1), while the "key advantage" of the NLoS-aware attention is relegated to the experiments section (Major #2). Together, these suggest the paper front-loads ambitious framing that the described method and experiments do not fully deliver. This pattern—overclaiming at the abstract/contribution level while deferring critical details to experimental sections or appendices—is more informative than any single technical weakness.

## Suggestions

1. Replace every instance of "zero-shot" with "few-shot" or "cross-scenario" to match the actual evaluation protocol.
2. Move the NLoS-aware attention description (Eq. 11 and its role in the architecture) into the Methodology section (Section 3), with a clear explanation of where it operates relative to the multi-BS fusion attention (Eq. 9–10).
3. Provide the cross-correlation algorithm for \(d_{\text{final}}\) derivation and explain how \(w\) is set, either in the main text or with a clear pointer to the appendix.
4. Correct the text/table discrepancy (1.580 → 1.880) and the parameter efficiency inconsistency (0.4 % → 0.7 %).
5. Add a brief discussion of the Table 3 RMSE reversal—why adaptive masking increases RMSE relative to strip masking despite improving MAE.
6. Include a simple baseline that concatenates map features as additional input channels to isolate the contribution of the prompt mechanism itself.

## Score and Decision

### Calibration Report

**Round 1 (Bracketing):** Three queries on "wireless localization deep learning transformer" across score bands. Weak anchors (avg < 3.5): scores 2.0–3.25 (rejected papers on unrelated topics). Middle anchors (3.5–7.5): scores 4.0–7.0, including Wi‑GATr (avg 7.00, Accept) and NaviFormer (6.00, Reject). Strong anchors (>7.5): scores 7.6–8.0 (theoretical/architecture papers, not topically relevant). This bracketing suggested the paper sits in the 4–7 range, since it is clearly stronger than the weak anchors but does not reach the strong anchors.

**Round 2 (Narrowing):** Two queries targeting specific aspects (map+prompt+transformer, masking+few-shot). Retrieved MeshMask (avg 6.33, Accept), FOLK (avg 6.50, Accept), and additional anchors in the 5.0–6.5 range. After reading Wi‑GATr (7.00), MeshMask (6.33), and FOLK (6.50) in full, the paper under review is weaker than all three due to the methodological omissions (Major #2), the unsubstantiated zero-shot claim (Major #1), and editorial errors. It is comparable to NaviFormer (6.00, Reject), which was rejected for related completeness issues.

**Anchors consulted:**
- `9TClCDZXeh` (Wi‑GATr, avg 7.00, Round 2): cleaner presentation, real-world validation, accepted. SigMap is weaker.
- `bFHR8hNk4I` (MeshMask, avg 6.33, Round 2): masked pretraining for physics, accepted. SigMap comparable on novelty but weaker on completeness.
- `VmJdqhuTCh` (FOLK, avg 6.50, Round 2): frequency-guided masking for SSL, accepted. SigMap less polished.
- `Pj3ErOxlLo` (NaviFormer, avg 6.00, Round 1): transformer for navigation, rejected. SigMap comparable.
- `NHhjczmJjo` (avg 7.00, Round 1): in-context sparse recovery, accepted. Not topically similar.
- `PVGS8UZ6GX` (avg 4.00, Round 1): maze navigation transformer, rejected.
- `Pxik3T6Mn9` (avg 4.50, Round 1): mobility modeling, rejected.
- `5dDYhvt6dY` (avg 3.00, Round 1): position embeddings, rejected.
- Weak anchors (avg 2.0–3.25, Round 1): clearly weaker than SigMap.

**Final score:** 5.5

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>