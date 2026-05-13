Now let me run the calibration search to anchor my scoring.Now I have enough information to write the final review. Let me synthesize everything.

---

## Summary

RT-Trajectory proposes conditioning robot manipulation policies on coarse 2D trajectory sketches, extracted automatically via hindsight labeling from the existing RT-1 demonstration dataset. The sketches encode temporal progression (via color grading), height (via a green channel for the 2.5D variant), and gripper interactions (via colored circle markers). The method is evaluated on 7 unseen manipulation skills with multiple trajectory input modalities (human drawings, human videos, LLM-generated waypoints, and image-generation models), showing substantially higher success rates (67%) than language-conditioned (16.7%) and goal-conditioned (26%) baselines across 64 total evaluation trials.

---

## Strengths

- **Scalable hindsight labeling:** The method automatically derives 2D trajectory conditioning signals from existing proprioceptive and calibrated-camera data in the RT-1 dataset, requiring no manual annotation and enabling straightforward scaling to new demonstration corpora. This is a genuine practical advantage over both goal-image and manual annotation pipelines.

- **Well-motivated design space framing:** The paper clearly positions trajectory sketches between over-specification (goal images, full video) and under-specification (language). The 2D projection design is well-reasoned: it is human-interpretable, strips task-irrelevant scene content, and allows humans or automated tools to draw on top of the initial camera image. The 2D vs. 2.5D comparison concretely demonstrates that height encoding reduces ambiguity for tasks like *Pick from Chair* where vertical positioning is critical.

- **Versatile inference modality taxonomy:** The paper goes beyond a single input pathway and demonstrates four distinct trajectory-specification methods (human drawings, human videos, LLM Code-as-Policies, image generation models), with quantitative results for two of them. Human-video-derived sketches achieve 94–100% on *Pick* vs. 42% for an IK planner, and 75% on *Fold Towel* vs. 25%. This range of modalities substantially strengthens the paper's practical contribution.

- **Large training scale:** Conditioning is trained on ~73K real robot demonstrations across 542 seen tasks (the full RT-1 dataset), making the results much more credible than typical few-shot simulation papers.

---

## Weaknesses

### Fatal
None.

### Major

- **Critically small per-task evaluation budget for the headline claims.** The main quantitative comparison (Section 4.1/Fig. 4) uses 64 total trials across 7 unseen skills — approximately 9 binary-outcome trials per task per method. With ~9 trials, the 95% confidence interval for a 50% success rate is approximately ±33 percentage points. The paper asserts "outperform our baselines by a large margin" and in the Conclusion writes "significantly outperforming the best prior state-of-the-art methods, which achieved 26%." While the overall aggregate (64 trials) gives somewhat more power, the per-task claims (and the headline presentation) are directionally suggestive at best. The gap between 67% and 26% is large enough to be meaningful at the aggregate level, but individual task comparisons and the use of the word "significant" are not supported at this evaluation scale. This is a known limitation of physical robot evaluation, but the strength of the language used in the abstract and conclusion is not justified by the evidence.

- **Manuscript submitted with numerous unresolved \todo{} markers in core sections.** The submitted text contains at least 15 `\todo{...}` markers embedded in the main body, including in the evaluation protocol (Section 4, lines 161–162), the human-drawing GUI description (Section 3.4, lines 105–106), the human-video inference modality (Section 3.4, lines 109–110), and the Fréchet distance analysis (Section 4.4, lines 272–276). These are LaTeX authorial notation indicating unfinished writing, not parser artifacts — they appear verbatim in the extracted text because the LaTeX definition renders them inline. Several mark out entire procedural paragraphs describing key experimental details (how evaluation scenes are set up, how trajectory sketches are generated for the RT-1-Goal baseline). This signals an incomplete submission in core methodological and experimental sections, reducing reproducibility and making certain methodological choices unverifiable.

### Minor

- **RT-Trajectory (2D/2.5D) underperforms the IK planner on Open Drawer with LLM-generated trajectories (60% vs. 71%; Table 2b)**, yet the paper frames this experiment as evidence of RT-Trajectory's superiority, citing only the pick task results. The text states "RT-Trajectory outperforms the IK planner in diverse pick tasks due to its ability to adapt motion to scene nuances" — this is accurate but selectively reported. The Open Drawer result, where a non-learning baseline beats the proposed method, receives no analysis or explanation. Understanding when the method fails to follow structured, precise LLM-generated paths would meaningfully characterize the method's limitations.

- **No ablation of individual representation components.** Color grading (temporal encoding) and interaction markers are each presented as design contributions (Section 3.2), but only the 2D vs. 2.5D comparison (which isolates the height/green channel) appears in the main results. The marginal contribution of temporal color grading and of interaction markers individually is never isolated. Given that the representation design is one of the two core contributions of the paper, this gap makes it impossible to know which design choices actually matter.

- **Seen-task performance not evaluated.** The method replaces language conditioning with trajectory conditioning across the full training dataset, but the paper never reports whether task performance on the 542 *seen* tasks is preserved, degraded, or improved relative to the original RT-1 baseline. If trajectory conditioning hurts seen-task performance, the trade-off must be characterized.

### Trivial

- The Fréchet distance analysis (Section 4.4) demonstrates that evaluation trajectories are dissimilar from training trajectories but does not connect trajectory similarity metrics to task success rates. A scatter plot of Fréchet distance vs. success rate per task would make this analysis genuinely explanatory rather than descriptive confirmation of a design-time fact (unseen tasks are, by construction, dissimilar).

---

## Nice-to-Haves

- **Joint trajectory + language conditioning baseline:** The paper replaces language with trajectory sketches; evaluating a combination would reveal whether the two modalities are complementary (trajectory resolves ambiguity in motion; language resolves semantic ambiguity) or redundant.

- **Human sketch quality sensitivity analysis:** Since the train-test gap between hindsight trajectories and hand-drawn sketches is structural, systematically varying sketch precision (coarse vs. detailed for the same task) would quantify how much drawing quality matters and inform practitioners.

- **Failure mode analysis:** Qualitative characterization of when trajectory conditioning fails (wrong height estimation, ambiguous sketch, poor grasp-point localization) would substantially strengthen the paper's understanding of method limits.

---

## Removed Points

*These points were flagged for removal — treat them with caution.*

1. **Harsh Critic: Goal-conditioned baseline implementation is opaque and potentially unfair** — The implementation details for RT-1-Goal are explicitly stated to be in the appendix ("implementation details and goal conditioning generation are presented in App. \ref{app:rt1-goal}", line 176). Per the hard rules, the appendix exists in the original submission and is merely stripped by the parser. This criticism depends on information the meta-reviewer cannot see, and is removed as it conflates a parser limitation with an author omission. It is weakened to a note that these details are in the appendix.

2. **Strength Finder: "Significant empirical gains" as a standalone strength** — While the 67% vs. 26% result is real, calling it "significant" in a statistical sense is contradicted by the small evaluation budget. The strength is partially absorbed by the verified weakness on evaluation scale.

3. **Strength Finder: Fréchet distance analysis as a "strong methodological tool"** — The Fréchet analysis is useful but does not connect similarity to success rates, making it incomplete as presented. Kept only as a Trivial note in main weaknesses.

---

## Novel Insights

The most genuinely novel observation across the reviews is the structural tension between hindsight labeling (which produces smooth, precise trajectories from proprioceptive data) and the coarser, noisier sketches that humans or automated tools provide at inference time. The paper's success despite this train-test sketch gap suggests that the policy learns a robust "sketch-following" capability that tolerates significant input variation — which is a more interesting finding than the aggregate success rate comparison. Connecting the degree of sketch coarseness to task success rate (e.g., through systematic sketch degradation experiments) would make this insight concrete and constitutes the most valuable direction for future work. The Fréchet distance machinery is already in place to support such an analysis.

---

## Suggestions

1. **Run more trials:** Increase to 20–25 trials per task per method for the unseen-skill evaluation. This would allow the headline claims of "significant outperformance" to be defensibly stated with at least informal confidence intervals.

2. **Remove or resolve all \todo{} markers before submission.** The evaluation protocol and inference modality sections in particular need to be complete for reviewers to assess methodology fairly.

3. **Add seen-task performance table:** Report success rates on a sample of seen tasks to characterize the trade-off (if any) introduced by replacing language with trajectory conditioning.

4. **Isolate representation components:** Add a 2-row ablation table: (a) 2D trajectory only (no color grading, no interaction markers), (b) + color grading only, (c) + interaction markers only, (d) full 2D, (e) full 2.5D. This would validate each stated design choice.

5. **Analyze the Open Drawer LLM failure:** Explain specifically why the IK planner outperforms the learned policy on this task with LLM-generated trajectories but not on pick tasks. Is the drawer opening geometry less tolerant of policy smoothing? This is a useful negative result that deserves analysis.

---

## Score and Decision

**Anchor comparison (all retrieved anchors):**

| Path | Avg Human Score | Comparison |
|---|---|---|
| `pISLZG7ktL` (Data Scaling Laws in Imitation Learning) | 8.0 | Much stronger: 40K demos, 15K robot rollouts, rigorous ablations, no quality issues. RT-Trajectory cannot match this rigor. |
| `OI3RoHoWAN` (GenSim) | 8.0 | Much stronger: creative LLM-based task generation, extensive simulation evaluation. Not directly comparable but anchors the top. |
| `7BLXhmWvwF` (Geometry-aware RL) | 8.0 | Stronger: well-constructed benchmarks, clean experimental design. |
| `c0chJTSbci` (Zero-Shot Robotic Manipulation via Image-Editing Diffusion) | 6.25 | Comparable: real robot experiments, similar scale, clear contributions; RT-Trajectory has stronger task generalization numbers but more submission quality issues. |
| `p01BR4njlY` (Solving New Tasks via Internet Video) | 5.75 | Comparable: addresses task generalization, solid paper with some weaknesses (simulation-only, limited tasks). RT-Trajectory has real robot evaluation and broader modality coverage. |
| `VEdeDd13gx` (ManiBox) | 5.25 | Comparable: sim-to-real generalization, somewhat limited. RT-Trajectory is roughly at the same level given its quality issues. |
| `Aqfwhna1D7` (CrayonRobo) | 5.20 | Most topically similar (2D visual prompts for robot manipulation); RT-Trajectory is clearly stronger — larger training scale, more modalities, hindsight labeling innovation — but also has more quality issues. |
| `s3sJenvY5H` (On Evaluation of Generative Robotic Simulations) | 4.75 | Weaker: evaluation framework with high score variance. RT-Trajectory is stronger on contribution. |
| `VaoeAi5CW8` (Diffusion Trajectory-guided Policy) | 4.25 | Similar trajectory-guidance idea; RT-Trajectory is significantly stronger on experimental scope (real robots, 73K demos, multiple modalities). |
| `PH7ja3T0vN` (State Combinatorial Generalization) | 4.50 | Weaker: largely theoretical with limited experiments. RT-Trajectory is stronger. |
| `InUpEfpXQS` (Tra-MoE) | 3.50 | Weaker: scaling study without real robot results. RT-Trajectory is stronger. |
| `fvTaoyH96Z` (Non-Parameterized Randomization) | 2.33 | Much weaker: limited contribution, theoretical framing without robot applicability. |
| `9GKMCecZ7c` (Building Generalist Robot Policy from Pre-trained Representations) | 3.40 | Weaker: limited contribution to generalization. |
| `OvrmA3GMiX` (Learning Transferable Sub-goals) | 3.75 | Weaker: RL-focused, simulation-only. |

**Calibration conclusion:** RT-Trajectory is clearly stronger than anchors in the 3.5–4.5 range. It competes with anchors in the 5.2–6.0 range. The \todo{} markers, small evaluation budget, and missing ablations are real but not fatal. The idea is novel in the robot policy conditioning space, the real-robot scale is respectable, and the 67% vs. 26% gap is directionally convincing even if not statistically rigorous by traditional standards. The submission quality issues (15+ todo markers in core methodological sections) are real and non-trivial but not idea-killing.

**Final score: 5.0** — The paper has a genuine, practically motivated contribution and real-robot experiments demonstrating strong task generalization. However, the submitted manuscript is incomplete (unresolved todo markers in core sections), the headline quantitative claims are stated more strongly than the evaluation budget supports, and key ablations are missing. This places it solidly in borderline territory, closer to the reject side of borderline given the submission completeness issue.

**MY FINAL SCORE: <pineapple>5.0</pineapple>**
**MY FINAL DECISION: <orange>Reject</orange>**