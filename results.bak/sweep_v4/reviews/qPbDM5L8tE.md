Now I have all the information needed. Let me compose the final consolidated review.

---

## Summary

The paper proposes CoRAL, a modular neuro-symbolic framework for zero-shot contact-rich robotic manipulation. It separates the roles of a VLM (perception: pose tracking via FoundationPose, physical parameter estimation) from an LLM (reasoning: generating MPPI cost functions, contact strategies, and online adaptation plans), with a memory unit for experience reuse and a reactive controller for execution. Experiments across six simulated contact-rich tasks compare CoRAL against OpenVLA-OFT, π₀.₅, human-expert-designed cost baselines, and multiple ablations.

## Strengths

1. **Well-motivated modular architecture.** The core design — explicitly separating perception (VLM + dedicated pose estimator) from reasoning (LLM for cost functions and contact strategies) — is clearly articulated and addresses a genuine limitation of monolithic VLA models. The LLM-generated cost function (Eq. 2) and contact strategy (Eq. 3) concretely ground symbolic reasoning into the MPPI optimization.

2. **Zero-shot capability on contact-rich tasks where end-to-end VLAs completely fail.** On the four hardest tasks (T1: Push+Pick Board, T4: Push with Constant Force, T5: Flip Box, T6: Flip with Wall), CoRAL achieves 4/10, 9/10, 9/10, and 7/10, while OpenVLA-OFT and π₀.₅ score 0/10 or at most 1/10 (Table 1). This demonstrates that the neuro-symbolic approach can succeed in scenarios where imitation-learned policies have no coverage.

3. **Evidence that role separation matters beyond just pose tracking.** The comparison between *w/o Pose Tracking* (9/10 on T2) and *Unified VLM* (2/10 on T2) provides reasonable evidence that separating perception and planning roles is beneficial even when both use VLM-graded pose estimates. On simpler tasks where pose tracking alone still works (T2), the Unified VLM collapse shows that role separation contributes independently.

4. **Quantified pruning from the LLM contact strategy.** In the Flip with Wall task, the guided strategy reduces MPPI planning steps from 199 to 32 (83.9% fewer) and end-effector path length from 3.69 m to 1.33 m (Section 4.1.4). This cleanly measures how the symbolic strategy constrains the action search space.

## Weaknesses

### Fatal
None.

### Major

1. **Figure 4/text inconsistency in the mass correction experiment (Section 4.1.4).** The text states that the evaluation world was initialized with mass = 2.0 kg against a ground truth of 0.1 kg. However, Figure 4 shows an initial planning-world mass of ~1.0 kg (not 2.0 kg) and the corrected estimate converging to ~0.85 kg (not 0.1 kg). The y-axis range (0.75–1.00 kg) cannot even display the claimed ground truth of 0.1 kg. This is a concrete, verifiable inconsistency in one of the paper's signature results on "online parameter adaptation." The authors must reconcile the text, figure, and experimental parameters before this result can be trusted. (*This is the single most concerning issue — it directly undermines the robustness claim.*)

2. **Thin statistical evidence for the main quantitative comparisons.** All success rates are based on 10 trials per condition with no confidence intervals, standard errors, or significance tests. Key comparisons (CoRAL with memory 4/10 vs. w/o memory 2/10 on T1; CoRAL 7/10 vs. Expert FSM 9/10 on T6) are within the noise for this sample size. While 10 trials is not uncommon in simulation-based robotics papers, the complete absence of any variance reporting means the reader cannot assess whether the reported differences are meaningful. This affects all headline claims about relative performance.

3. **Memory unit details are underspecified.** Section 3.2 states that memory uses RAG with the LLM embedding tasks into a "latent semantic space," but no specifics are given about: (a) the embedding model or dimensionality, (b) the retrieval mechanism or similarity threshold, (c) whether memory accumulates across all tasks or is per-task, or (d) the maximum number of stored episodes. The improvement from 2/10 to 4/10 on T1 (10 sequential trials of the same task) could reflect a single successful trial being replayed rather than any form of generalization. The paper presents this as "learning from experience" but the mechanism is too vaguely described to be reproducible or to distinguish genuine generalization from memorization.

### Minor

1. **Success criteria for T4 are not explicitly stated.** The task description (Table 1 notes) says "Push with Constant Force, testing the reactive controller's ability to manage force feedback," but the paper does not define what constitutes success. Without this, the 9/10 result is difficult to interpret.

2. **The online adaptation claim is broader than the evidence.** Beyond the Figure 4 inconsistency, the paper asserts that CoRAL can "correct physical parameters online" but the evidence is limited to a single demonstration with one parameter (mass) under one condition. The ablation shows that the *w/o Refinement* variant performs worse, but this doesn't isolate parameter correction from strategy refinement — the outer loop changes both simultaneously.

3. **Honesty of the "narrowing the gap" framing.** CoRAL achieves 4/10 vs. Expert FSM 8/10 on T1 and 7/10 vs. 9/10 on T6. The paper describes this as "narrowing the gap," which is technically accurate (the single-stage expert gets 0/10 and 3/10 respectively) but is a positive spin on what is still a substantial gap to the best human-designed controller.

### Trivial

- The completion time comparison (CoRAL 45s vs. OpenVLA 5s on T2) is noted but not discussed as a limitation. While this is expected given that MPPI is a planning-based method, a brief acknowledgment in the limitations section would improve transparency.

## Nice-to-Haves

- Analysis of how often the LLM generates degenerate/unsensible cost functions versus useful ones, compared to random cost weights.
- Ablation of the $N_{retry}$ hyperparameter (currently fixed at 15).
- Cross-task memory transfer experiments (e.g., transferring a strategy from T1 to help T4).
- Real-world validation on a physical robot, which is the obvious next step for a robotics paper claiming practical applicability.
- A corrected Figure 4 with consistent axes, ground-truth markers, and experimental parameters matching the text.

## Removed Points

- *83.9% faster uses step counts not wall-clock time:* The paper explicitly says "steps" (32 vs. 199), which is a valid metric in simulation where each step has fixed compute cost. Removed as not a weakness.
- *OpenVLA speed comparison (9× slower):* Apples-to-oranges comparison between a planning-based and an end-to-end method. Mentioned as a nice-to-have acknowledgment, not a weakness.
- *Missing related work:* Cannot verify from available information.
- *Reproducibility nitpicks about undisclosed hyperparameters beyond what is reasonable to expect:* The paper reports $K=200$, $H=50$, $\lambda=0.1$, $N_{retry}=15$, and the hardware setup — this is adequate for a systems paper.
- *Speculative fatal claims* (e.g., "no amount of rewriting can fix it"): Overly strong language that is not warranted by the actual severity of the issue in context of community norms.
- *Strength Finder's generic strengths* (e.g., "addresses an important problem"): Removed as superficial.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any observation that goes substantially beyond what the paper itself articulates.

## Suggestions

1. **Fix Figure 4 immediately.** Ensure the numerical values in the text (initial mass, ground truth, corrected estimate) match the figure axes and plotted data exactly. If the figure is from a different run than described, state this explicitly. The current inconsistency is the single biggest barrier to trusting the online adaptation result.
2. **Add confidence intervals or bootstrapped error bars** to the main results table. Even with 10 trials, reporting the exact binomial confidence interval would give readers a realistic sense of the uncertainty.
3. **Provide concrete details on the memory mechanism:** embedding model, similarity function, indexing structure, and whether memory spans tasks or is per-task. Without this, the memory contribution cannot be properly evaluated.
4. **Acknowledge the simulation-only limitation** more prominently in the main paper (it is deferred to Appendix A.3.2, which was stripped during parsing — but the main text should note this).
5. **Define success criteria for all tasks**, especially T4 where it is not self-evident.

## Score and Decision

**Calibration anchors** (from `calibration_search`):

| Path | Avg Score | Comparison to CoRAL |
|------|-----------|---------------------|
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/9pKtcJcMP3.md` (VLP) | 7.00 | Stronger: real-robot validation, cleaner evaluation, broader scope. CoRAL has figure inconsistency. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/lFYj0oibGR.md` (RoboFlamingo) | 6.50 | Stronger: thorough ablations, SOTA on CALVIN, cleaner presentation. CoRAL more novel architecturally but weaker evidence. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/gVnJFY8nCM.md` (Residual-MPPI) | 6.25 | Stronger: sound evaluation, real control domain. CoRAL more interesting approach but less rigorous. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/h7aQxzKbq6.md` (HAMSTER) | 6.00 | Stronger: sim + real experiments. CoRAL comparable in architecture novelty but sim-only. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/KTtEICH4TO.md` (CORN) | 4.75 | Similar: both address contact-rich manipulation with modular designs, both have sim-to-real claims, similar score range. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/VEdeDd13gx.md` (ManiBox) | 5.25 | Comparable but cleaner: has real-world experiments. CoRAL has more novel architecture but figure issue. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/oyXoGJQlUf.md` (GRAIL) | 3.00 | Weaker: very simple evaluation, narrow contribution. CoRAL addresses harder tasks with better baselines. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/koza5fePTs.md` (LLM Planning Bench.) | 2.00 | Weaker: largely reproduces known results. CoRAL has genuine novelty. |

The paper proposes a genuinely interesting architecture and shows it can handle contact-rich tasks that end-to-end VLAs completely fail on. However, the Figure 4/text inconsistency undermines one of its marquee results, and the thin statistical evidence (10 trials, no CIs) weakens the quantitative claims. The paper falls between the stronger accepted papers (6.0–7.0) and the clearly weak papers (2.0–3.0), closer to papers in the 4.5–5.25 range that have promising ideas but significant execution issues.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>