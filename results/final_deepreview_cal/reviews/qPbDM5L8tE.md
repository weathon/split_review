Now I have enough anchors to calibrate. Let me synthesize my analysis and write the final review.

---

## Summary

CoRAL proposes a modular neuro-symbolic framework for zero-shot, contact-rich robotic manipulation that separates visual perception (VLM + FoundationPose) from LLM-based reasoning. The LLM generates cost functions and symbolic contact strategies that guide an MPPI reactive controller, with closed-loop online adaptation and a memory unit for experience reuse. The framework is evaluated on six contact-rich tasks against VLA baselines and human-designed cost functions.

## Strengths

- **Role separation is convincingly validated by ablation.** The "Unified VLM" variant—which collapses perception and planning into a single multimodal model—fails nearly completely on all challenging tasks (0/10 on T1, T3, T5, T6), while the full CoRAL framework achieves substantial success rates (e.g., 4/10 on T1, 9/10 on T5). This stark contrast in Table 1 directly supports the paper's central architectural claim that decoupling vision and LLM reasoning is essential for contact-rich manipulation.

- **The online refinement loop demonstrably improves success rates.** Removing the outer refinement loop causes dramatic performance drops: T1 falls from 4/10 to 0/10, T3 from 10/10 to 3/10, T5 from 9/10 to 4/10 (Table 1). This provides clear evidence that LLM-driven adaptation mid-execution is functional and impactful, independent of the parameter-correction visualization.

- **Memory unit provides measurable benefits.** The experience retrieval module improves success rates on T1 (2/10 → 4/10) and T3 (9/10 → 10/10) while reducing completion times (e.g., 212s → 162s on T1). This demonstrates that the memory mechanism meaningfully contributes beyond the base architecture.

- **Well-chosen task suite stresses contact-rich manipulation.** The six tasks span multi-stage reasoning (T1), force control (T4), dynamic maneuvers (T5), and multi-contact environmental reasoning (T6), providing a meaningful testbed that exposes clear weaknesses in end-to-end VLA baselines.

## Weaknesses

### Major

- **Figure 4 contradicts the text's description of the online parameter adaptation experiment.** Section 4.1.4 states that the evaluation world was initialized with a "severely overestimated mass (2.0 kg vs. a ground truth of 0.1 kg)" and that the LLM's adaptation caused the agent's belief to converge "remarkably close" to the true value. However, Figure 4 shows an "Initial Mass" constant at 1.00 kg and a "Corrected Mass" that drops to approximately 0.85 kg, with a y-axis spanning only 0.75–1.00 kg. The figure is completely at odds with the described experimental setup: the initial mass shown (1.0 kg) does not match the text (2.0 kg), the corrected value (≈0.85 kg) is nowhere near the claimed ground truth (0.1 kg), and neither the initial nor the corrected values correspond to the text's narrative. This directly undermines the specific claim that the LLM can drive parameter estimates toward true physical values—one of the paper's four stated contributions. The adaptation loop's *existence* is still supported by the refinement ablation in Table 1, but the precise mechanism of parameter convergence is not credibly demonstrated.

- **The LLM's cost-function generation capability is insufficiently specified to evaluate the method's core novelty.** The paper states that "the LLM is free to introduce any cost terms constructible from the available state, pose, and action variables, and is not restricted to a fixed finite set of cost terms." Yet no detail is given on how the LLM's output is translated into executable cost functions (e.g., a domain-specific language, code generation with parsing, or selection from a template library). Equation 2 is explicitly labeled as "only an illustrative example." Without this specification, the reader cannot judge whether the LLM is truly formulating novel cost structures or merely selecting weights for a hand-engineered library of pre-defined terms. This is the paper's most distinctive claim relative to prior work (IMPACT, VLMPC), and the evidence for it is missing.

### Minor

- **Text-table contradiction in the pose-tracking ablation narrative.** Section 4.1.3 claims the *w/o Pose Tracking* variant resulted in "catastrophic failure across all tasks (0/10 success)." However, Table 1 reports 9/10 success on T2 (Pick+Place Box) for this variant. The narrative overstatement damages precision but does not invalidate the underlying finding—pose tracking is indeed critical for all contact-rich tasks, and the 9/10 on the simpler T2 is a nuance worth noting rather than a data problem.

- **Contact-strategy ablation is based on a single illustrative run.** The 83.9% step reduction and 63.9% path-length reduction reported in Section 4.1.4 for the guided vs. unguided contact strategy comparison appear to come from one trajectory each (Appendix Figure 5). No mean, variance, or trial count is reported. The paper treats this as quantitative evidence for the strategy's importance, but single-run results do not support quantitative conclusions.

- **Memory retrieval and online adaptation mechanisms are under-specified.** The description of the RAG-based memory retrieval (Section 3.2) mentions that "the LLM embeds the current task into a latent semantic space" but does not specify the similarity metric, the embedding method, or how the retrieved cost function is merged with the current state. Similarly, the mechanism by which the LLM produces updated physical parameter estimates from episode logs (Section 3.4) is not explained. These gaps hinder reproducibility.

- **Limited evaluation of the explainability claim.** The abstract states that the modular approach "demonstrably enhances both manipulation performance and system explainability." The explainability evidence consists of a single textual example of failure diagnosis. The robustness of this feature across tasks is not evaluated.

- **No statistical dispersion reported.** Table 1 reports only success rates and mean completion times. Given 10 trials per task, reporting standard deviations for completion times and confidence intervals for success rates would strengthen the comparative claims.

- **Randomization ranges are not specified.** The paper states that initial object poses, masses, friction coefficients, and box dimensions were randomized, but the ranges are not reported, limiting the reader's ability to assess task difficulty and reproduce the setup.

### Trivial

- The feedback gain matrix K_f in Equation 7 is not specified (values, tuning method, or sensor sources).
- Prompts used for the VLM/LLM modules are not provided, which limits reproducibility.

## Nice-to-Haves

- Reporting aggregated results over multiple trials for the contact-strategy ablation (Section 4.1.4) would transform an anecdotal illustration into genuine quantitative evidence.
- Providing a concrete, non-trivial example of a cost term generated by the LLM that goes beyond pre-defined primitives would substantially strengthen the method's presentation.
- Including a comparison against a non-LLM task-and-motion-planning baseline would help contextualize the LLM's specific contribution beyond the VLA comparisons.

## Removed Points

These points from the input reviews were considered but removed:

- *"Missing appendix references" / "Appendix ??" —* The parser strips appendix sections from all papers; this is not an author error. Any criticism rooted in missing appendix content is removed.
- *"Missing related works" —* Per instructions, I do not have external sources to confirm the existence of missing related works.
- *Strength Finder claim that w/o Pose Tracking yields "0/10 success on every task" —* This is factually incorrect per Table 1 (T2 shows 9/10). The general point about pose tracking being critical holds, but the absolute framing is wrong.
- *Formatting/style nitpicks and grammar issues —* Removed per instructions; these are parser artifacts or trivial presentation issues.
- *Harsh Critic's speculation about "the appendix may specify X but…" —* Removed; evaluation is based on the paper as presented, not on speculation about stripped content.

## Novel Insights

The paper's most genuinely novel observation is the demonstration that an LLM can formulate the *structure* of an MPPI cost function—not merely generate subgoals or cost maps—and that this formulation can be refined online through a closed-loop adaptation mechanism triggered by physical execution failures. While the evidence for the parameter-convergence aspect of this claim is compromised (see Major weakness 1), the success-rate improvement from the refinement loop (Table 1) provides independent support that this LLM-as-cost-designer paradigm is functional and worth further investigation.

## Suggestions

- **Resolve the Figure 4 discrepancy as the highest priority.** Either re-run the experiment with the described parameters (2.0 kg initial, 0.1 kg ground truth) and replot, or correct the text to match the actual experiment. Additionally, include the friction correction plot that the text mentions but the figure does not show. This is essential for the paper's credibility on its online adaptation contribution.
- **Describe the cost-function interface concretely.** Show the prompt structure, output format, and a real (non-illustrative) example of a cost term the LLM generated. Even a single paragraph with a prompt excerpt and the LLM's output would address the largest methodological gap.
- **Correct the pose-tracking narrative.** Change "catastrophic failure across all tasks (0/10 success)" to something like "catastrophic failure on all contact-rich tasks (0/10), while occasionally succeeding on the simple T2 pick-and-place where VLM pose estimates happen to be adequate (9/10)."
- **Report multi-trial statistics for the contact-strategy ablation.** Even 5 trials with mean ± std would transform this from anecdotal to meaningful.

## Score and Decision

**Round 1 bracket:** The paper sits between the weak anchors (GRAIL at 3.0, Diff-Transfer at 3.4) and the strong anchors (GenSim, Geometry-aware RL at 8.0), with the most relevant middle anchors being RePLan (4.25), Make a Donut (5.25), and SuSIE (6.25). Initial bracket: 4.0–6.0.

**Round 2 narrowing:** Compared to RePLan (4.25, rejected for too-few trials and unclear VLM specification), CoRAL has broader evaluation (6 tasks, 10 trials each) and more thorough ablation, but adds the Figure 4 integrity issue. CoRAL is somewhat stronger than RePLan. Compared to Make a Donut (5.25, rejected for open-loop LLM planning and limited technical insights), CoRAL's closed-loop adaptation is more sophisticated, but the Figure 4 contradiction and cost-function under-specification are significant detractors. CoRAL lands slightly below Make a Donut. SuSIE (6.25, accepted) has stronger evaluation with real-world experiments and more compelling evidence for its core claims; CoRAL is clearly weaker.

**Final score: 5.0.** The paper contributes a genuinely interesting architecture and provides solid ablation evidence for role separation and refinement benefits. However, the Figure 4 contradiction directly undermines one of four stated contributions, and the under-specification of the cost-function generation mechanism leaves the paper's most distinctive claim unverified. These are fixable issues, but in the current submission they prevent full confidence in the reported results.

**Anchor comparison summary:**
| Anchor | Avg Score | Round | Comparison |
|---|---|---|---|
| GRAIL (oyXoGJQlUf) | 3.00 | R1 | CoRAL substantially stronger: more tasks, quantitative results, ablations |
| Diff-Transfer (EODzbQ2Gy4) | 3.40 | R1 | CoRAL stronger: better evaluation, clearer architecture |
| Robot Policy Code (WtHKqtHVXo) | 4.00 | R1 | CoRAL somewhat stronger: broader evaluation, more thorough ablation |
| RePLan (gisAooH2TG) | 4.25 | R2 | CoRAL slightly stronger: more tasks, more trials, clearer ablation, but has Figure 4 issue |
| Make a Donut (iTsHStJKcm) | 5.25 | R2 | CoRAL slightly weaker: comparable architecture novelty but Figure 4 contradiction and cost-function under-specification are more damaging |
| Instruct2Act (JWrl5pJCnl) | 5.00 | R1 | Comparable quality; CoRAL addresses harder tasks but has data integrity concern |
| SuSIE (c0chJTSbci) | 6.25 | R2 | CoRAL clearly weaker: less rigorous evaluation, no real-robot experiments, Figure 4 issue |
| GenSim (OI3RoHoWAN) | 8.00 | R1 | CoRAL clearly weaker: less compelling evidence, data issues |

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>