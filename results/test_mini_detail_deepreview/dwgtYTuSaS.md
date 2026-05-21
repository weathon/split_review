Now I'll write the final review and determine the score.

## Summary

The paper introduces Continuous Online Action Detection (COAD), a new task formulation where OAD models learn from streaming video in a single causal pass without data storage. It also curates Ego-OAD, a large-scale egocentric OAD benchmark from Ego4D (87 classes, 22,991 instances, 263h), and proposes training strategies (state continuity, orthogonal gradient projection, non-uniform loss) that enable online adaptation while maintaining generalization.

## Strengths

- **Novel and well-motivated task formulation.** The paper identifies a genuine gap: existing OAD models are trained offline and cannot adapt to the dynamic, personalized contexts of wearable devices. COAD formalizes a setting that directly addresses the constraints of on-device training (single-pass, causal, no data storage). Figure 2 clearly contrasts standard offline OAD training with the proposed COAD pipeline.

- **Large-scale egocentric OAD benchmark (Ego-OAD).** Curated from Ego4D MQ, this provides 87 classes, 22,991 instances, and 263 hours of video, significantly expanding the diversity of available egocentric OAD datasets beyond EPIC-KITCHENS' kitchen-only scope. The 36% instance overlap is acknowledged and semantically similar descriptions are grouped to mitigate ambiguity.

- **Component-level ablation isolating each contribution.** Table 3 systematically removes each proposed strategy: removing non-uniform loss drops out-stream mAP by 4.2% (26.0→21.8), removing orthogonal gradient reduces recall by 4.5% (76.0→71.5), and state continuity provides a smaller but consistent gain. This provides clear evidence that each component contributes to generalization.

- **Continuous improvement over the stream is demonstrated.** Figure 4 shows that COAD's out-of-stream performance steadily improves as more in-stream data is processed, while ablated variants plateau, supporting the core claim that the full method enables effective continuous learning.

## Weaknesses

### Major

- **Label ambiguity in Ego-OAD is not adequately addressed.** The paper states that 36% of instances overlap and that different annotators may describe the same action with different fine-grained labels (e.g., `clean_/wipe_kitchen_appliance` vs. `clean_/wipe_other_surface_or_object`). The solution — merging via union and grouping into 87 classes — is described but not evaluated. Standard mAP and Top-5 Recall become ill-posed under this ambiguity: a model predicting both semantically similar labels is rewarded for what amounts to guessing the union. The paper provides no inter-annotator agreement analysis, no analysis of how the grouping resolves conflicts, and no alternative evaluation (e.g., soft overlap measures that treat grouped labels as equally correct, or the original Ego4D MQ retrieval protocol). This makes the magnitude of the headline numbers uncertain.

- **EPIC-KITCHENS results undermine the universal benefit claim.** Table 2 shows that on EPIC-KITCHENS, both COAD and the w/o COAD baseline *frequently underperform* the Pretrained Only model — particularly on in-stream metrics (e.g., Verb mAP in: 29.0 Pretrained Only vs. 16.6 w/o COAD and 29.0 COAD; Action mAP in: 9.6 vs. 4.9 vs. 7.9; Action Top-5 in: 22.9 vs. 14.4 vs. 20.5). The paper attributes this to "fine-grained actions," but this explanation is post-hoc and not validated. If the proposed method can hurt performance on a standard benchmark, the paper should clearly characterize when COAD is and is not beneficial, rather than claiming "COAD consistently achieves the best generalization."

### Minor

- **No error bars or statistical significance.** All results are single numbers from presumably single runs. Given the stochastic nature of online training and the small deltas between COAD and w/o COAD on some metrics (e.g., out-stream ego mAP: 26.0 vs. 25.5), it is impossible to assess whether the observed improvements are meaningful.

- **No direct comparison to existing OAD models.** The baselines are ablations of the proposed method rather than existing OAD models (e.g., LSTR, TeSTra). The paper uses MiniROD's architecture, so the "w/o COAD" baseline is a reasonable ablation of COAD's strategies. However, including a comparison where an existing OAD model is trained on the pretraining set and evaluated on out-of-stream data would help the reader calibrate the absolute performance level. This is not a fatal omission — the paper's claim is about the COAD formulation, not SOTA on a standard benchmark — but it would substantially strengthen the evaluation.

### Trivial

- None.

## Nice-to-Haves

- The IID Training upper bound in Figure 4 uses multiple epochs and full supervision. A tighter comparison would be an IID model trained for the same number of gradient steps as COAD's single pass, to isolate the effect of the single-pass constraint.
- The qualitative results in Figure 5 are illustrative but add little beyond what the tables show.

## Removed Points

The following points from the inputs were removed with justification:

- **"Misleading headline claims" (Harsh Critic #4):** The abstract claims "up to 20% in top-5 accuracy." In Table 1, the largest in-stream Top-5 improvement is 22.5 absolute points (exo pretrain: 57.5→80.0). This is *above* 20% — the claim is slightly conservative, not overstated. The comparison to Pretrained Only is a standard baseline comparison, and the paper also reports Δ over w/o COAD. **[REMOVED — factually incorrect]**
- **"Unfair split sizes" (Harsh Critic #5):** The paper explicitly states the split (186 pretrain, 1,177 in-stream) is intentional: "We allocate the majority of training data to the in-stream split to better assess the impact of continuous learning on this data under the COAD scheme." This is a deliberate design choice to test the core thesis. **[REMOVED — misunderstanding of experimental design]**
- **Generic strengths from Strength Finder (e.g., "important problem"):** These lacked specific evidence anchors and were redundant with the more concrete strengths retained above.
- **"No comparison to MiniROD":** The paper's architecture IS MiniROD (An et al., 2023). This criticism is factually wrong at the architectural level. The w/o COAD baseline is the appropriate ablation. **[REMOVED — factually incorrect]**

## Novel Insights

None beyond the paper's own contributions. The combination of existing techniques (orthogonal gradient projection from Han et al., non-uniform loss from MiniROD) under single-pass, state-continuous training is a sensible synthesis, but the reviews do not surface any unexpected insight about why this combination works beyond what the paper already states.

## Suggestions

1. **Address label ambiguity directly.** Report inter-annotator agreement on Ego-OAD, show how the 87-class grouping resolves the described conflicts, and evaluate with a metric that treats semantically grouped labels as equally correct (e.g., soft mAP).
2. **Add error bars.** Run at least 5 seeds for all main results and report mean ± std.
3. **Characterize when COAD helps vs. hurts.** The EPIC-KITCHENS results show COAD can underperform the Pretrained Only baseline. Add analysis of what properties of the data determine whether COAD is beneficial.
4. **Include at least one existing OAD model as a reference point.** Training LSTR or TeSTra on the pretraining set and evaluating without adaptation would provide a useful anchor.

## Calibration Anchors

### Round 1 — Bracketing (4.5–6.0)
- **MSxCBXD5C8 (Anomalous Action Recognition, 3.00):** Much weaker paper — lacks clear motivation and the method is a straightforward application of attention without ablation. The current paper is substantially stronger.
- **5f0n5yi8qK (Video-prompt RL, 3.40):** Weak evaluation, limited generalization. The current paper is clearly better motivated and validated.
- **2HdZPEQUig (Object-Centric Video Learning, 3.00):** Weak results, poor clarity. Current paper is significantly stronger in presentation and evidence.
- **3ZdGSTxKuy (Harry Potter atypical videos, 2.00):** Lacks focus and rigorous evaluation. Current paper is far more rigorous.

### Round 2 — Narrowing
- **Y7jJN0VQ4y (CL-WSVAD, 5.71, Reject):** Closely related (continual learning for video understanding + new task). That paper also had missing baselines and limited evaluation, but its baselines were more extensive than the current paper's ablations-only setup. The current paper's dataset contribution is stronger, but its label ambiguity issue is more serious. **Current paper is slightly weaker (~5.0).**
- **7L2bpe7lfm (Large Scale Video CL, 4.50, Reject):** Had significant novelty concerns (similar approaches existed) and missing baselines. The current paper has a clearly novel task formulation and a stronger dataset contribution. **Current paper is stronger (~5.0 vs. 4.50).**
- **jawV7vhGHw (PrAViC, 4.25, Reject):** Online video classification with early exiting. Questionable theoretical contribution, missing baselines. The current paper is more solid overall. **Current paper is stronger (~5.0 vs. 4.25).**
- **G9Ea7mlqGO (CLIP Online Continual Learner, 3.80, Reject):** Weak method, limited novelty. The current paper is substantially stronger in both problem framing and evaluation.

**Final bracket determination:** The paper is clearly above the 3.8–4.5 range but below the 5.71 anchor (CL-WSVAD). The label ambiguity issue and the EPIC-KITCHENS counter-evidence are more serious than that paper's problems. Score positioned at 5.0 — a solid submission with real contributions but evaluation gaps that prevent acceptance at this venue.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>