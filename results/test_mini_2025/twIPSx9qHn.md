Now I have all the information I need. Let me compile the final review.

**Round 1 bracket**: Based on the first calibration pass, the paper sits between the weak anchors (~2.5-3.0, all rejects) and the strong anchors (~8.0, all oral/spotlight). The most relevant middle-band anchor is ResDex (7.0, poster) — a universal dexterous grasping paper. CrossDex addresses a harder problem (cross-embodiment) but has weaker evaluation (no SOTA baselines, limited zero-shot analysis, no real-world quantification). So the initial bracket is (4.5, 7.0).

**Round 2 narrowing**: Papers in (4.5, 6.0): VTDexManip (5.5, poster), AdaManip (5.5, poster), CrayonRobo (5.2, withdrawn), Make a Donut (5.25, reject). Papers in (6.0, 7.5): ResDex (7.0, poster), DexTrack (6.75, poster), AutoCGP (7.25, spotlight), RDT-1B (7.0, poster).

CrossDex is **above** VTDexManip (5.5) — its contribution is clearer and the method is more novel. CrossDex is **below** ResDex (7.0) — ResDex has SOTA comparisons on 3200 objects and stronger quantitative results, while CrossDex's evaluation lacks competitive baselines and has significant analysis gaps. I settle on **6.0**.

**Anchor summary** (all rounds):

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| xcHIiZr3DT.md | 2.50 | 1 | Much weaker — rejected paper on tactile extraction |
| sXF5P4N7e8.md | 3.00 | 1 | Much weaker — rejected goal-conditioned grasping paper |
| BUj9VSCoET.md | 7.00 | 1,2 | Stronger — SOTA baselines on 3200 objects, but same-hand setting |
| ajSmXqgS24.md | 6.75 | 1,2 | Slightly stronger — more thorough evaluation and real-world experiments |
| jf7C7EGw21.md | 5.50 | 1,2 | Weaker — contribution questioned, real-world results qualitative |
| RInisw1yin.md | 7.33 | 1 | Stronger — assembly tasks, thorough evaluation |
| KsUh8MMFKQ.md | 8.00 | 1 | Much stronger — oral paper, differentiable physics |
| 7BLXhmWvwF.md | 8.00 | 1 | Much stronger — oral paper, geometry-aware RL |
| 9ehJCZz4aM.md | 7.25 | 2 | Stronger — spotlight paper with thorough imitation learning |
| yAzN4tz7oI.md | 7.00 | 2 | Stronger — bimanual manipulation foundation model |
| Luss2sa0vc.md | 5.50 | 2 | Weaker — very mixed reviews, one extreme low score |
| Aqfwhna1D7.md | 5.20 | 2 | Weaker — withdrawn, visual prompting paper |
| iTsHStJKcm.md | 5.25 | 2 | Weaker — rejected deformable object paper |

Now I'll write the review.

Let me finalize the weaknesses after careful checking against the paper:

**Major weaknesses:**

1. **No comparison to SOTA single-hand methods adapted per hand** - The harsh critic is right that Table 1's baselines are all ablations of CrossDex's components. Figure 3 does compare to individual per-hand training, but only for state-based policies, not for the vision-based setting that constitutes the paper's main claim. A comparison showing what a SOTA single-hand method achieves (trained per hand, averaged) would contextualize whether cross-embodiment training is beneficial or costly.

2. **No per-hand breakdown of success rates** - The harsh critic flags this, and the paper indeed only reports averages across training hands and unseen hands. Without per-hand breakdown, it's impossible to know if performance is uniform or dominated by a single embodiment. This is a straightforward experiment (the data exists in the logs) and its omission weakens the main cross-embodiment claim.

**Minor weaknesses:**

3. **Zero-shot performance on unseen hands (35.2% vision) is not analyzed for failure modes** - The paper reports the number without any breakdown by hand, object category, or failure reason. This limits understanding of what drives the gap between training hands (80%) and unseen hands (35.2%). No per-object or per-hand analysis is provided.

4. **Table 1 lacks standard deviations or confidence intervals** - Table 2 includes error bars but Table 1, which contains the main results, does not. Given RL training variance, this is a notable omission.

5. **Real-world experiments are purely qualitative** - A single sentence and a video link with no quantitative metrics, no controlled evaluation, and no comparison even to the simulation-trained policy's performance under real-world conditions.

**Trivial:**
6. Abstract phrasing ("80% success rate across four distinct embodiments") could be read as 80% per hand rather than an average.

**Removed from harsh critic:**
- "Code and model not released" — Rule: cannot criticize release status of cited entities.
- "No comparison to GET-Zero" — Paper explicitly explains why GET-Zero doesn't apply to cross-embodiment scenarios.
- "No discussion of reward design" — Reward is defined in Equation 3 and described in text.
- "GRAB dataset sensitivity not analyzed" — Not a core claim; would be nice-to-have.

Let me write the review now.## Summary

CrossDex proposes a method for learning a single vision-based RL grasping policy that controls multiple dexterous hands with different morphologies (varying DoFs, number of fingers, sizes). The key technical ideas are: (1) a unified action space using human-hand eigengrasps (PCA-compressed MANO hand poses) mapped to each robot hand via learned neural retargeting networks, and (2) a unified observation space using only fingertip and palm 3D positions (discarding embodiment-specific joint angles). The policy is trained via a teacher-student framework on 45 YCB objects across four dexterous hands in IsaacGym and evaluated on two unseen hands. This is the first work to demonstrate a single dexterous grasping policy that transfers across structurally distinct hand types.

## Strengths

- **Unified action space via human eigengrasps is a principled solution to cross-embodiment control (Section 4.1).** Using PCA on the MANO hand pose space (trained on the GRAB dataset) produces a compact, low-dimensional action space that maps meaningfully to different robot hands through retargeting. Figure 4 shows that eigengrasps (especially 9-E) outperform raw MANO axis angles on zero-shot unseen-hand performance (~0.50 vs ~0.40), and the learned neural retargeting networks (Section 4.3) accelerate training from 300 fps to simulation-speed batch computation — a necessary engineering contribution for scalable cross-embodiment RL.

- **Unified observation space (discarding embodiment-specific joint positions) is convincingly validated (Table 4).** The ablation removing both embodiment randomization and embodiment-specific observations (Rand. ✓, Obs. ✗) achieves 0.885/0.800 (state/vision) on training hands and 0.391/0.352 on unseen hands. Adding embodiment-specific observations drops unseen-hand state performance from 0.391 to 0.044–0.259. This cleanly supports the paper's central claim that embodiment-unaware observations are critical for generalization.

- **Cross-embodiment training is comparable to or better than individual per-hand training (Figure 3).** The multi-task co-training across four hands reaches ~0.7 success rate by 10k iterations, exceeding the average of individually-trained per-hand policies (~0.6). This justifies the paper's design choice to not divide the embodiment space during teacher training.

- **Efficient finetuning to new embodiments and objects (Table 2).** CrossDex-initialized finetuning reaches 0.872 (state, LEAP Hand, 5 objects) vs. 0.798 for the best baseline (MT-Raw-A) and 0.758 for No-Pretrain. For multi-task vision finetuning on 55 unseen GRAB objects, CrossDex achieves 0.740 vs. 0.655 for the next best. These results confirm the pre-trained policy serves as a strong universal grasping prior.

- **Robustness to retargeting algorithm choice (Table 3).** All three retargeting variants (Position, Vector, DexPilot) yield similar training (~0.84–0.89) and zero-shot unseen (~0.44–0.50) performance, indicating the method does not depend on a specific retargeting objective.

## Weaknesses

### Fatal
None.

### Major

1. **No comparison to existing SOTA single-hand methods, adapted per hand.** The baselines in Table 1 (MT-Raw-OA, MT-Raw-A, MT-Raw-O) are ablations that remove components of CrossDex. They are useful for isolating the contribution of each component, but they do not answer the natural question: *how does CrossDex compare to training a state-of-the-art per-hand policy for each embodiment and averaging the results?* Figure 3 provides this comparison for the state-based setting (CrossDex ≈ individual), but Table 1 — where the paper's headline results are reported — has no such entry. Without this, the reader cannot assess whether the cross-embodiment approach provides a meaningful advantage over the simpler alternative of training separate policies. Including a per-hand trained vision-based policy baseline in Table 1 would directly substantiate the claim that CrossDex is "a step towards a universal grasping policy" that is better than training per-hand.

2. **No per-hand breakdown of success rates.** Table 1 aggregates results across four training hands and two unseen hands into single numbers. The reader cannot tell whether performance is uniform (e.g., 80% on all four hands) or dominated by one embodiment (e.g., 95% on one hand and 65% on others). A per-hand breakdown is a straightforward experiment (the data exists in the training logs) and its omission weakens the core cross-embodiment claim. Per-object breakdown is also missing — the paper only notes that "42 of 45 objects exceed 60%" on training hands, with no analogous analysis for unseen hands.

### Minor

3. **Zero-shot performance on unseen hands (35.2% vision) is reported without any failure analysis.** While CrossDex substantially outperforms the best baseline (21.0%), the gap between training (80.0%) and unseen (35.2%) performance is large and unexamined. The paper does not provide a breakdown by unseen hand (LEAP vs. Inspire), by object category, or by failure mode (e.g., poor retargeting mapping vs. insufficient observation space vs. object-specific challenges). This analysis would help the community understand the method's limitations and guide future work.

4. **Table 1 lacks standard deviations or confidence intervals.** Table 2 reports standard deviations, but Table 1 — which contains the paper's primary results — reports only point estimates. Given that RL training can exhibit nontrivial variance across seeds, this is a notable omission. The very small error bars in Table 2 (e.g., ±0.002) also warrant clarification of whether they are standard deviations or standard errors, and over how many seeds.

5. **Real-world experiments are purely qualitative.** Section 5.5 describes a single real-world setup (RM65 arm + LEAP Hand + RealSense camera) and directs readers to a project-page video. No quantitative metrics (success rate over a fixed number of trials), controlled lighting/object-placement conditions, or comparisons to baselines are reported. While the paper's primary contribution is in simulation, the real-world section is presented as supporting evidence without any measurable validation.

### Trivial

6. The abstract ("80% success rate in grasping objects from the YCB dataset across four distinct embodiments") could be misread as 80% on each hand individually rather than the reported average across hands. A per-hand listing or a more precise phrasing would avoid ambiguity.

## Nice-to-Haves

- An analysis of how sensitive the eigengrasp results are to the choice of dataset (GRAB) used for PCA. Would a different human-pose dataset yield different eigengrasps and different performance?
- A justification for dropping the little finger from the observation space (Section 4.2). The paper states this is "practical" because the little finger is "typically less critical," but a small ablation verifying that including it does not harm (or helps) performance on five-fingered hands would strengthen the claim.
- A comparison to GET-Zero or other cross-embodiment methods, even a qualitative discussion of why they cannot be adapted to this setting, would contextualize the contribution better.

## Removed Points

These points are flagged to be removed; treat them with caution if raised:

- **Code/model not released as criticism**: Rules prohibit questioning the availability of cited resources. The paper has a project page; release status cannot be verified from the submission alone.
- **Missing comparison to GET-Zero as a baseline**: The paper explicitly explains in Section 2 that GET-Zero "cannot generalize across different types of dexterous hands" because it uses GNNs for morphological variants of the same hand. This is addressed.
- **No discussion of reward design**: The reward is defined in Equation 3 and described in the text. Different objects use the same reward function, which is standard practice in multi-task grasping RL.
- **GRAB dataset sensitivity not analyzed**: A potentially interesting analysis, but the paper makes no claim about optimal dataset choice for PCA eigengrasps. This is a speculative extension, not a missing experiment.
- **Generic "evaluation lacks rigor" / "claims insufficiently supported" framing**: These are category-driven noise without a specific concrete anchor in the paper. The concrete evaluation gaps are listed above as specific weaknesses.

## Novel Insights

The harsh critic and strength finder converge on the same picture from opposite directions: the core methodological insight — using MANO eigengrasps as a universal action interface and fingertip positions as an embodiment-agnostic observation — is sound, novel, and convincingly ablated. Every ablation in the paper (Table 4, Figure 4, Table 3) cleanly confirms that both components contribute meaningfully to cross-embodiment transfer. However, the paper's evaluation strategy is too narrowly focused on within-method ablations. The absence of a comparison to SOTA single-hand methods (adapted per hand) means the strongest claim — "cross-embodiment learning is beneficial" — rests on Figure 3 alone, which covers only the state-based setting. The reviewer asymmetry is informative: the method is stronger than the evaluation that supports it. A paper with this level of methodological novelty would benefit from evaluation that matches its ambition.

## Suggestions

1. **Add per-hand individually-trained vision-based baselines to Table 1.** Train separate vision policies for each training hand using a standard dexterous grasping architecture (e.g., the teacher-student framework from Xu et al. 2023 or Wan et al. 2023) and report the average. This directly answers whether cross-embodiment training is beneficial or costly compared to the simpler alternative.

2. **Add a per-hand breakdown of success rates** for both training and unseen hands, in a supplemental table or a new figure. This is a one-line logging change and would substantially strengthen the cross-embodiment claim.

3. **Analyze the zero-shot failures on unseen hands.** Report per-unseen-hand success rates, per-object-category breakdown, and a categorization of failure modes (retargeting failure vs. observation insufficiency vs. task policy failure). This would help the community understand the method's current limitations.

4. **Report standard deviations or confidence intervals for Table 1**, consistent with Table 2.

5. **Add quantitative real-world evaluation** — even 20–50 trials on a small set of objects with a success/failure count would turn the real-world section from a qualitative demo into a meaningful validation.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>