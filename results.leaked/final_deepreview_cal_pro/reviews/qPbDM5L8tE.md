Now I have a comprehensive picture. Let me compose the final consolidated review, filtering the harsh critic's points carefully against the paper.

---

## Summary

CoRAL presents a modular neuro-symbolic framework for zero-shot, contact-rich robotic manipulation. It decouples perception (FoundationPose + VLM for pose tracking and physical parameter estimation) from reasoning (an LLM that formulates MPPI cost functions and contact strategies) and execution (an MPPI controller with reactive feedback). The system features nested feedback loops: an inner MPPI loop for reactive control and an outer LLM-driven loop for online adaptation from failures. A memory unit retrieves past successful experiences. The framework is evaluated on six simulated manipulation tasks against SOTA VLAs (OpenVLA-OFT, π₀.₅), human-designed cost baselines, and four ablations.

## Strengths

- **Strong ablation design validates the modular architecture.** The four ablations (w/o Pose Tracking, Unified VLM, w/o Refinement, w/o Memory) cleanly isolate each component's contribution. The Unified VLM ablation (collapsing perception and planning into a single prompt) yields 0/10 on complex tasks, directly validating the core hypothesis that role separation is essential. Removing FoundationPose also yields 0/10, confirming that a dedicated pose estimator is non-negotiable for the precision this pipeline requires (Table 1).

- **LLM-generated costs approach expert-designed performance on hard tasks.** On T5 (Flip Box), CoRAL achieves 9/10 vs. the expert FSM's 10/10; on T6 (Flip with Wall), 7/10 vs. 9/10 (Table 1). This shows the LLM can automatically recover much of the structure of carefully engineered, task-specific cost functions.

- **Online adaptation demonstrably recovers from initial physical mischaracterizations.** The w/o Refinement ablation drops T1 from 4/10 to 0/10, and Figure 4 shows the LLM iteratively correcting an overestimated mass parameter from 1.0 kg toward the true 0.85 kg, providing concrete evidence for the outer loop's corrective capability.

- **Contact strategy quantitatively prunes the search space.** The LLM-guided contact strategy on T6 reduced end-effector travel by 63.9% and completion time by 83.9% compared to uninformed sampling — a well-quantified demonstration that high-level reasoning meaningfully guides low-level planning.

- **Maintains competence on standard benchmarks.** CoRAL matches both VLAs on standard pick-and-place tasks (T2: 10/10; T3: 10/10), showing the modular design does not sacrifice baseline capability.

## Weaknesses

### Fatal

None.

### Major

- **Explainability claims are not substantiated.** The paper lists "explainability" as a core contribution and states the modular design "demonstrably enhances … system explainability." The only evidence provided is a single qualitative vignette (the "Flip with Wall" failure recovery) whose details are deferred to the stripped appendix. No quantitative metric, systematic qualitative analysis, or user study is offered. The ablation studies measure task success, not explainability. The claim should either be toned down substantially or supported with concrete evidence.

- **Reliance on an accurate simulator is acknowledged but its implications for the zero-shot claim are under-discussed.** The MPPI inner loop requires forward rollouts in a "Planning World" that, in these experiments, is essentially the same MuJoCo instance as the evaluation environment. The paper's brief limitation statement ("performance is currently contingent on the fidelity of the vision-based world model") acknowledges the issue but does not explore what happens under simulator mismatch. Since the zero-shot framing is a central selling point, this gap between simulation conditions and the real-world deployment scenario the paper gestures toward warrants more explicit discussion.

### Minor

- **Baseline comparison asymmetry should be more candidly discussed.** CoRAL's MPPI controller has access to force/torque feedback and an internal simulator (planning world) for forward rollouts. The VLA baselines (OpenVLA-OFT, π₀.₅) operate purely on visual and language inputs with no equivalent model access. While comparing model-based and model-free paradigms is legitimate, the paper's headline claim that CoRAL "significantly outperforms" SOTA VLAs would benefit from explicitly noting what each approach has access to, so readers can properly contextualize the performance gap.

- **Limited statistical power.** All results use 10 trials per condition with no confidence intervals. While this is common in simulation robotics work, differences like 2/10 vs. 4/10 (T1, memory ablation) are fragile at this sample size, and the robustness analyses (contact strategy, parameter correction) are based on single illustrative runs rather than repeated trials.

- **Memory unit details are underspecified.** The paper does not report how many past episodes were stored in memory for the experiments, how many were retrieved, or what retrieval threshold was used. This makes the memory benefit (e.g., T1 improving from 2/10 to 4/10) harder to interpret — was this from one stored episode or many?

### Trivial

- The LLM prompts used for cost-function generation and online adaptation are not visible (appendix-stripped), limiting reproducibility assessment.

## Nice-to-Haves

- Scaling up trials to 50–100 per condition with binomial confidence intervals would substantially strengthen the statistical case.
- Testing with an intentionally degraded planning world (e.g., perturbed mass, different friction models) would directly probe the system's robustness to simulator mismatch and significantly strengthen the paper's practical relevance claims.
- A systematic taxonomy of failure modes with associated LLM diagnoses would turn the explainability claim from an anecdote into evidence.

## Removed Points

These points were flagged from the harsh critic but are removed for the stated reasons:

- **"Unfair baseline comparison" characterized as fatal**: The critic framed the simulator access asymmetry as undermining the entire comparison. But model-based vs. model-free comparisons are standard — the paper is transparent about its architecture. The asymmetry merits acknowledgment (retained above as Minor) but does not invalidate the comparison.

- **"The Unified VLM ablation is a straw-man"**: The critic claimed collapsing perception and planning into a single model is "almost guaranteed to fail." This is hindsight bias. The ablation directly tests the paper's core hypothesis that role separation matters. If the result were obvious, it would not be worth reporting — but it is the central empirical claim the paper makes.

- **"Even fine-tuning an end-to-end policy is insufficient — this misrepresents the situation, because the baselines were not fine-tuned on these tasks"**: The paper is explicit that the baselines use off-the-shelf LIBERO checkpoints and states this is a zero-shot test. It does not claim the baselines were fine-tuned on CoRAL's tasks.

- **"The planning-world assumption is never acknowledged as a limitation in the main text"**: Factually incorrect. Section 5 (Limitations & Conclusion) states: "While promising, the framework's performance is currently contingent on the fidelity of the vision-based world model."

- **Criticism about missing appendix/proofs/prompts**: The parser strips appendix sections from all papers; the original submission includes them. Removed per hard rule.

- **Demand for user study to validate explainability**: While a user study would strengthen the claim, the core problem is that the paper provides essentially no evidence at all — not that it lacks a particular form of evidence. The retained criticism focuses on the absence of evidence rather than prescribing a specific methodology.

## Novel Insights

The paper's architecture embodies a genuinely interesting insight: using an LLM not merely as a perceptual guide or subgoal proposer (as in prior work) but as the formulator of the MPPI cost function's mathematical structure itself. This lets commonsense reasoning about physical interactions (e.g., "maintain contact during pushing") be directly compiled into the optimization objective that drives low-level control, creating a tighter and more explainable link between high-level intent and execution than prior LLM+planning integrations achieve.

## Suggestions

- Tone down the explainability contribution or add a table of failure-recovery episodes with LLM diagnoses and ground-truth causes.
- Add a dedicated paragraph discussing the planning-world assumption and its implications for real-world deployment, ideally with a conceptual roadmap for how structural model mismatch could be addressed.
- Report the number of episodes in the memory unit for each condition and clarify the retrieval mechanism's sensitivity to threshold settings.
- Move the LLM prompts from the appendix into the main paper or at minimum reference them explicitly so readers can assess prompt-dependence.

## Score and Decision

**Round 1 bracketing**: Queries returned anchors at 3.0–3.4 (weak), 4.0–6.25 (middle), and 8.0 (strong). CoRAL is clearly above the weak band (well-structured system with meaningful ablations) and clearly below the strong band (simulation-only, unsubstantiated explainability claim, limited statistical power). Initial bracket: **5.0–6.5**.

**Round 2 narrowing**: Retrieved anchors within the bracket included Instruct2Act (5.00, Reject), Make a Donut (5.25, Reject), GenBot (5.50, Reject), HAMSTER (6.00, Accept), and Online Self-Improvement (6.25, Reject). CoRAL is stronger than Instruct2Act (more principled integration, harder tasks, better ablations) and comparable to or slightly stronger than Make a Donut (both simulation-primary, but CoRAL has more complete ablation design). It is comparable to HAMSTER (both propose modular/hierarchical architectures; HAMSTER has real-world experiments but simpler tasks and weaker ablations). It is slightly weaker than Online Self-Improvement (which has real-world experiments and a more general training methodology).

**Anchor comparison summary**:
| Anchor | Score | Round | Comparison |
|---|---|---|---|
| wl1Kup6oES (Appearance to Motion) | 3.00 | R1 | CoRAL is substantially stronger |
| oyXoGJQlUf (GRAIL) | 3.00 | R1 | CoRAL is substantially stronger |
| WtHKqtHVXo (Robot Policy Code) | 4.00 | R1 | CoRAL has more complete evaluation |
| qGL6fE1lqd (LLMPhy) | 4.40 | R1 | CoRAL has better integration and ablations |
| JWrl5pJCnl (Instruct2Act) | 5.00 | R2 | CoRAL has harder tasks and better ablations |
| iTsHStJKcm (Make a Donut) | 5.25 | R1 | Comparable; CoRAL has better ablation design |
| fZZ4ubttru (GenBot) | 5.50 | R2 | Comparable; different style of contribution |
| 3UWuFoksGb (Planning Abstractions) | 5.50 | R2 | Different problem domain |
| h7aQxzKbq6 (HAMSTER) | 6.00 | R2 | Comparable quality; HAMSTER has real-world |
| I0To0G5J7g (Online Self-Improvement) | 6.25 | R2 | CoRAL slightly weaker; S-I has real-world |
| c0chJTSbci (Zero-Shot Diffusion) | 6.25 | R1 | Different approach; CoRAL slightly weaker |
| OI3RoHoWAN (GenSim) | 8.00 | R1 | CoRAL is clearly below this tier |

CoRAL lands between Make a Donut (5.25) and HAMSTER (6.00). Given the real but addressable weaknesses (explainability overclaimed, simulation-only scope, limited trials), I place it at **5.5** — a solid contribution with a well-executed core idea and good ablation evidence, but not yet at the threshold where weaknesses are trivial. The explainability claim in particular needs to be either substantiated or significantly toned down.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>