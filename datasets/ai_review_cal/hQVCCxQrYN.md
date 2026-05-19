- Decision: Accept
- Avg Score: 6.67
- Scores: 6, 8, 6
Here is my final consolidated review, produced after carefully verifying every claim against the paper text.

---

## Summary

Plan-Seq-Learn proposes a modular framework that combines LLM high-level planning (GPT-4), vision-based motion planning (SAM + AIT*), and online RL (DRQ-v2) to solve long-horizon robotics tasks without requiring a pre-defined skill library. The method decomposes tasks into contact-free reaching phases (handled by motion planning) and contact-rich interaction phases (handled by RL). Experiments across 25+ tasks on four benchmarks (Robosuite, Meta-World, Kitchen, ObstructedSuite) with up to 10 stages show strong results, achieving 85–100% success rates where baselines often fail entirely.

## Strengths

- **Comprehensive empirical superiority on long-horizon tasks.** Tables 2 and 3 (two-stage and multi-stage results) show \our achieving 97–100% on two-stage Robosuite tasks and 85–100% on multi-stage tasks with up to 10 stages, while all baselines (E2E, RAPS, TAMP, SayCan) drop to 0% on the longest-horizon Kitchen tasks (K-MS-5, K-MS-7, K-MS-10). This directly supports the paper's central claim.

- **Handles contact-rich manipulation that defeats planning-only baselines.** On NutAssembly (Table 3), \our achieves 96% success vs. SayCan's 23% and TAMP's 20%. This large gap validates the paper's decomposition into contact-free motion planning and contact-rich RL — precisely the regime where pre-defined skill libraries fail.

- **Robustness to noisy pose estimation demonstrated quantitatively.** Table 4 shows \our maintains 100% success at pose noise σ=0.025 and 75% at σ=0.1, while SayCan drops to 27% and 0% at the same levels. This provides concrete evidence that \our's online RL adaptation recovers from pose errors that break open-loop planning methods.

- **Ablation validates stage termination conditions as critical.** Section 5.2 reports a 31% performance improvement (100% vs. 69%) when using stage termination checks over a fixed timeout on RS-Can, confirming that the curriculum-learning aspect of the plan is measurably important.

- **Shared policy across stages simplifies training without per-stage reward engineering.** Section 4.4 describes training a single RL policy across all stages. The empirical success on 4-stage NutAssembly and 10-stage Kitchen tasks validates this design choice.

- **Explicitly differentiates from most relevant concurrent work (BOSS).** The Related Work (paragraph on "Language Models for RL and Robotics") contrasts \our with BOSS, noting that BOSS requires a pre-defined skill library while \our learns low-level control directly — clarifying the paper's unique contribution.

## Weaknesses

### Fatal

None.

### Major

- **Hallucination filtering procedure is ambiguous — manual or automatic?** Section 3.2 (line 125) states: "We also delete components of the plan that contain LLM hallucinations (if present)." The paper does not specify whether this filtering is performed automatically by the system or manually by the authors before running experiments. If manual, the method as described is not fully autonomous, and the comparisons to baselines (which do not receive such correction) could be unfair. The paper also does not report how often hallucinations occur. This is the most significant reproducibility gap. The authors should clarify the procedure and, if manual, report the frequency of intervention.

### Minor

- **Stage termination conditions are described at a high level without precise definitions.** The paper states (line 143) that for most conditions, "$f_{stage}$ is evaluated by computing the pose estimate of the relevant object and thresholding." Specific thresholds, perceptual checks, and how conditions like "grasp" are determined (e.g., whether gripper state or force is used) are not provided. The ablation shows these conditions are critical (31% performance drop without them). While some detail may reside in the appendix, the main-text description is too vague for reproducibility.

- **GPT-4 dependency acknowledged but not discussed as a practical limitation.** Line 125 notes that "only GPT-4 was capable of producing correct plans across all the tasks we consider." This is an important practical constraint — the method requires a specific (potentially expensive, API-dependent) LLM. The paper does not discuss the implications of this dependency (e.g., cost, API availability, reproducibility if GPT-4 changes).

- **No quantitative analysis of LLM plan accuracy.** The paper does not report how often GPT-4 produces correct (vs. incorrect or hallucinated) plans across the 25+ tasks. Since the planning module is a core component, understanding its reliability would strengthen the claim that the planner is dependable enough to guide learning.

- **No failure mode analysis for the cases where \our does fail.** On RS-CerealMilk (85%) and RS-CanBread (90%), \our is not perfect, and \our has a 4% failure rate on NutAssembly, but the paper does not analyze what causes these failures (e.g., segmentation error, RL policy never learning a grasp, motion planning collision). Understanding failure modes would help the community assess robustness.

- **MoPA-RL not evaluated on multi-stage tasks.** MoPA-RL is the most directly relevant baseline that also integrates motion planning and RL, but it is only compared on single-stage tasks (Fig. 2). The paper argues (line 54) that \our's explicit decomposition is more suitable for long horizons, but this claim is not tested. A comparison on at least one multi-stage task would strengthen the argument.

- **Contact-free/contact-rich decomposition assumption not critically examined.** The paper assumes tasks decompose into alternating phases of contact-free reaching and contact-rich interaction (line 111). Tasks involving sustained contact (e.g., sliding, wiping) may not fit this decomposition. This limitation is not acknowledged.

### Trivial

None.

## Nice-to-Haves

- A learning curve for a long-horizon task (e.g., K-MS-5 or NutAssembly) would help illustrate that \our learns over time rather than being perfect from the start.
- Reporting the low-level horizon \(H_l\) parameter value and how it was chosen would aid reproducibility.
- The noise-robustness experiment (Table 4) shows the system works; an additional ablation isolating RL adaptation from Sequencing Module robustness would be insightful but is not required.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"0.0 with 0.0 std on long-horizon tasks appears too clean."** Removed. The paper explains this via cascading failures (line 247: "cascading failure problem becomes all the more problematic"). With 7 seeds and 10 evaluations each (70 evaluations), zero successes is a plausible outcome for methods that systematically fail in multi-stage settings.
- **"SAM segmentation accuracy not reported."** Removed. The paper uses SAM off-the-shelf without claiming contributions in segmentation; this is scope creep.
- **"Camera setup for baselines (single global view) is questionable."** Removed. The paper justifies this with an ablation referenced as Fig. "baseline camera abl" (line 202).
- **"The noise experiment does not isolate RL adaptation vs. Sequencing Module robustness."** Removed. The experiment successfully shows the overall system's robustness; the requested isolation is a deeper analysis beyond what is required.
- **"Variance across seeds should be shown with learning curves for long-horizon tasks."** Removed. Mean ± std across 7 seeds in tables is standard reporting; requesting learning curves for every task is excessive.
- **"\(H_l\) not specified."** Removed. This is a standard implementation detail likely in the appendix (stripped by parser).
- **"Missing discussion of the broken section reference."** Removed. The broken "Sec." reference (line 117) is a PDF parser artifact from LaTeX cross-referencing — the original submission is intact.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the hallucination-filtering ambiguity and the underspecified termination conditions as concrete gaps, but these are clarity issues rather than insights that change the paper's contribution. The strength finder's key observation — that the paper's contact-free/contact-rich decomposition is validated by the large gap between \our and planning baselines on NutAssembly — is already stated in the paper itself.

## Suggestions

1. **Clarify the hallucination filtering procedure.** State explicitly whether it is automatic or manual. If automatic, describe the detection mechanism. If manual, acknowledge it as a limitation and report the frequency of intervention across tasks.
2. **Provide table of stage termination conditions.** For each condition type (grasp, place, turn, open, push), specify the perceptual test, distance/pose thresholds, and whether gripper state or force is used. This is critical for reproducibility.
3. **Add a brief failure analysis.** Even a short paragraph analyzing the 4% failure on NutAssembly or 15% on RS-CerealMilk would improve the paper's rigor.
4. **Report LLM plan accuracy.** A simple table showing how often GPT-4 produces a correct (executable) plan per task would strengthen confidence in the planning module.
5. **Acknowledge the GPT-4 dependency as a limitation** in the conclusion or a limitations paragraph.
6. **Test MoPA-RL on at least one multi-stage task** if feasible; otherwise, discuss more explicitly why the comparison is missing and what it would likely show.
