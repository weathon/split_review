## Summary

VT-WM is the first multi-task visuo-tactile world model that integrates fingertip tactile sensing (Digit 360 via Sparsh-X embeddings) with exocentric vision (Cosmos tokenizer) into a factorized spatiotemporal transformer predictor for contact-rich robot manipulation. The paper claims tactile grounding reduces object-permanence failures by 33% and improves causal compliance by 29% in autoregressive imagination rollouts, and that these gains translate to up to 35% relative improvement in zero-shot CEM planning on a real Allegro + Franka platform. A multi-task fine-tuning experiment further shows 77% vs. 22% success on a new plate-insertion task compared to task-specific behavioral cloning.

---

## Strengths

- **Quantified improvement in imagination quality:** VT-WM achieves a 33% average reduction in normalized Fréchet distance for object motion across five tasks (Fig. 4) and a 29% overall reduction in spurious motion of static objects (Fig. 6), with statistical significance on key tasks (e.g., push fruits: t=6.06, p<10⁻⁶; place fruits: t=4.38, p<0.001). The metric design — CoTracker keypoints, normalized Fréchet distance, paired t-tests — is well-matched to the physical claims.

- **Diverse real-robot evaluation on a genuinely hard platform:** Testing on an Allegro Hand + Franka Panda with Digit 360 fingertips across five distinct contact-rich tasks (place fruits, push fruits, wipe cloth, stack cubes, scribble with marker) is more demanding than typical tabletop setups. The consistent directional improvement of VT-WM over V-WM across all tasks is notable.

- **Transparent failure-mode analysis:** The paper acknowledges the one case where VT-WM is worse — causal compliance for "scribble with marker" (t = −1.22, p = 0.23 vs. V-WM) — rather than suppressing it, and the rollout visualizations (Figures 5, 7) make failures interpretable.

- **Data efficiency result is clean and compelling:** The 77% (7/9) vs. 22% (2/9) comparison over nine balanced trials for the plate-insertion task is a crisp, integer-verifiable result that directly supports the transfer learning story (Section 4.3).

- **Architecture is clearly described:** Section 3.2.1 explicitly states that vision and tactile tokens are "concatenated along the spatial dimension to form a unified input sequence," and that factorized spatio-temporal attention (spatial then temporal) is used to handle the multi-modal token sequence efficiently.

---

## Weaknesses

### Fatal
None.

### Major

- **Planning success rates are arithmetically inconsistent with the stated five-trial protocol.** Section 4.2 states results are "averaged over five trials per task from distinct initial conditions," but the reported values — 83%, 92%, 69%, 93%, 70%, 75%, 83% — are not multiples of 20%, which is the minimum resolution for five binary outcomes. The only value consistent with five binary trials is 100%. The data-efficiency experiment (9 trials, 77% ≈ 7/9, 22% ≈ 2/9) confirms the authors can and do use integer-consistent metrics when the denominator is nine; the inconsistency in Fig. 8 left is therefore unexplained. The most plausible explanation — that multi-step tasks (Reach&Push, Wipe Cloth, Stack Cubes) are scored per subgoal — is never stated, but even subgoal scoring does not produce clean integers under any obvious subgoal count. Without knowing whether the metric is binary task completion, subgoal-level success, or something else, the headline claim of "35% higher success rates" and its comparisons cannot be independently verified. This is an evidential gap in the paper's primary planning claim, not a speculation about the method's capability.

### Minor

- **The decoder used for visualization and CoTracker evaluation is unacknowledged.** VT-WM operates entirely in latent space (Cosmos latents for vision, Sparsh-X latents for touch). Figures 5 and 7 display decoded RGB frames, and CoTracker requires decoded images for pixel-level keypoint tracking. The Cosmos tokenizer includes a built-in decoder, which is almost certainly what is used, but this is never stated. Since decode quality affects what CoTracker can track during heavy occlusion — precisely the condition the object-permanence metric targets — a brief statement (one sentence) confirming that the Cosmos decoder is used and that no separate trained component is involved would eliminate this ambiguity and strengthen reproducibility.

- **The "data efficiency" framing somewhat overstates the comparison.** The experiment compares VT-WM (multi-task pre-trained on an unspecified large dataset, fine-tuned on 20 new demonstrations) against ACT trained from scratch on only 20 demonstrations. Section 4.3 acknowledges the pre-training advantage ("it already encodes contact dynamics from prior tasks"), so the paper is not misleading in its narrative, but the framing as a "data efficiency" result implies sample efficiency for the new task in isolation. The advantage may stem from pre-training scale, world-model architecture, or the CEM planner; the current experiment does not separate these factors.

- **Scribble-with-marker causal compliance degradation is noted but unexplained.** For "scribble with marker," VT-WM has a higher normalized Fréchet distance than V-WM for static objects (Fig. 6; t = −1.22, not significant). The paper flags this without analysis. Understanding whether the model is over-interpreting marker contact as causing ambient object motion would strengthen the paper's physics-grounding argument and show the authors understand the mechanism, not just the averages.

### Trivial

- Training horizon H = 3–5 is stated as a range without specifying how it was chosen; a single sentence on sensitivity would be informative.

---

## Nice-to-Haves

- **Increase planning trial counts to 20–30 per task and report binary task-completion rates with confidence intervals.** This is feasible within a week of robot time and would bring the planning evidence to the same standard as the rollout quality evidence. If subgoal-level scoring is used for multi-step tasks, reporting both task-level and subgoal-level rates would be more informative.

- **Ablation isolating test-time tactile context from tactile training signal.** The paper hypothesizes (Section 3.2.3) two separate tactile benefits: (1) training signal that teaches contact dynamics, and (2) test-time context that disambiguates initial state. An ablation comparing VT-WM-full vs. VT-WM-no-tactile-context-at-test-time would separate these mechanistically.

- **Disentangle pre-training scale from world-model architecture in the data-efficiency experiment.** Training ACT on the full multi-task dataset plus 20 new task demonstrations would clarify whether the 3.5× advantage over task-specific ACT comes from the pre-training breadth, the world-model architecture, or the CEM planner.

- **Brief analysis of the scribble-with-marker causal compliance degradation** — even a hypothesis about over-attribution of contact to object motion would strengthen the physics-grounding narrative.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Temporal mismatch between 30Hz actions and 6Hz tactile (Harsh Critic):** The paper states actions are "chunked from 30Hz into groups of 5," yielding 30/5 = 6Hz action chunks. Tactile input is also at 6Hz. No temporal mismatch exists; the concern is factually incorrect.

- **Four Digit 360 sensor embeddings combination is unexplained (Harsh Critic):** Section 3.2.1 states "Vision and tactile tokens are concatenated along the spatial dimension to form a unified input sequence." The paper explicitly describes concatenation along the spatial dimension. The concern is a misread.

- **V-WM baseline receives less test-time information (Harsh Critic):** The asymmetry in test-time tactile context (VT-WM has it, V-WM by definition does not) favors VT-WM, which is the system being proposed. Per the hard rules, unfair comparisons that favor the proposed method are the paper's intended design, not an error. The paper is transparent about this in Section 4.2.

- **"First multi-task visuo-tactile world model" claim is too strong (Harsh Critic):** Zhang & Demiris (2023) is acknowledged in the related work, and the paper clearly distinguishes VT-WM as multi-task, planning-capable, and real-robot-validated. The novelty claim is appropriately scoped.

- **Strength Finder — generic strengths about "important problem" and "scalable combination":** Removed as insufficiently specific. The retained strengths are anchored to specific figures and results.

---

## Novel Insights

The most genuinely novel insight surfaced by the reviewers — not merely echoing the paper's own claims — is the mechanistic specificity of the object-permanence improvement: tactile feedback disambiguates *in-hand* states that are visually opaque (Figure 5, cube-transport phases), and this disambiguation propagates through CEM rollouts to produce quantifiably better plans. The fact that the gains are *largest* for multi-step tasks requiring sustained contact (Reach&Push +35% relative, Wipe Cloth +31% relative) while free-space reaching shows no gap (100%/100%) is a clean empirical separation that validates the paper's central causal claim. The one anomaly — degraded causal compliance on scribble with marker — hints that tactile-informed models may systematically over-attribute static object motion to marker contact, an interesting failure mode that points toward a limitation of contact-centric supervision for tasks with ambiguous causal structure.

---

## Suggestions

1. **Clarify the planning success metric unambiguously** — state explicitly whether it is binary task completion, subgoal-level, or per-step success, and reconcile with the five-trial denominator or correct the trial count.
2. **Confirm decoder usage** — one sentence stating that the Cosmos tokenizer's built-in decoder is used for image reconstruction in all visualizations and CoTracker evaluations.
3. **Reframe Section 4.3** as "multi-task transfer" or "pre-training + fine-tuning efficiency" rather than plain "data efficiency" to more accurately convey what is being compared.
4. **Run more planning trials** (20–30) per task to support the headline quantitative claims with appropriate confidence intervals.
5. **Add a qualitative or quantitative hypothesis** for the scribble degradation in causal compliance, even if brief.

---

## Evaluation on Key Axes

**Originality:** High — the first multi-task, planning-capable, real-robot VT-WM is a clear step beyond prior task-specific visuo-tactile dynamics models.

**Importance of research question:** High — contact physics are a genuine bottleneck for world-model-based manipulation; grounding via touch is a well-motivated and practically relevant direction.

**Claims well-supported:** Moderate — the imagination-quality claims (33%, 29%) are statistically rigorous; the planning claims rest on thin, metrically ambiguous evidence.

**Soundness of experiments:** Moderate-to-good — architecture is principled, evaluation metrics are appropriate, real-robot results are directionally consistent, but the planning evaluation has a verifiable arithmetic inconsistency with the stated protocol.

**Clarity of writing:** Good — motivation is clear, contributions are crisp, and the evaluation pipeline is mostly transparent, with the decoder and planning-metric gaps being the main ambiguities.

**Value to the research community:** High — the Cosmos + Sparsh-X + factorized transformer design is reusable, the evaluation framework (CoTracker + Fréchet distance for imagination quality) is a useful benchmark contribution, and the negative result (scribble degradation) adds nuance.

---

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>