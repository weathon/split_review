Now I have all the information needed to cross-reference the reviewer claims against the paper. Let me construct the authoritative final review.

---

## Summary

This paper introduces Reverse Forward Curriculum Learning (RFCL), a two-stage model-free RL algorithm that first trains a policy via a per-demonstration reverse curriculum (initializing near success states in demonstrations and gradually moving further back), then generalizes to the full initial state distribution via a forward curriculum (adaptively prioritizing solvable-but-challenging initial states). The method is evaluated across 21 manipulation tasks from MetaWorld, Adroit, and ManiSkill2 with sparse rewards and very few demonstrations (often 5 or fewer). The central empirical result is that RFCL solves tasks (e.g., PegInsertionSide, PlugCharger) that prior methods fail entirely, achieving nonzero success where baselines achieve zero.

## Strengths

1. **Strong empirical performance on previously unsolvable tasks.** Figure 4 shows RFCL achieving ~60–70% success on PegInsertionSide and PlugCharger from ManiSkill2 with only 5 demonstrations, while all baselines (RLPD, JSRL, DAPG, Cal-QL) achieve 0%. This is the paper's most compelling result and a genuine advance.

2. **Per-demonstration reverse curriculum is a practical differentiator.** Prior work either uses one demonstration (Resnick et al., 2018) or a uniform curriculum over multiple demonstrations (Nair et al., 2018). The per-demonstration construction, where each demonstration has its own curriculum stage counter, is a reasonable and well-motivated design that handles multi-modality in demonstration data. The paper provides an ablation (Table 1, in the original submission) supporting this design choice.

3. **Extensive and rigorous benchmarking.** The method is evaluated across 21 tasks spanning three distinct environment suites, with multiple seeds (5 per run, with 30-seed follow-ups for high-variance tasks), 95% confidence intervals, and fair comparisons where baselines receive the same demonstrations. Figure 5 also systematically varies the number of demonstrations to show demonstration efficiency.

4. **Practical algorithmic innovations.** The dynamic episode timelimit (tied to the curriculum stage) and the off-policy adaptation of PLR for the forward curriculum are non-trivial engineering contributions that demonstrably accelerate training, as indicated by the ablations.

## Weaknesses

### Fatal
None.

### Major
None. The paper's central empirical claims are well-supported by the evidence presented.

### Minor

1. **Incomplete direct comparison to the most closely related prior methods.** The paper discusses Resnick et al. (2018) and Nair et al. (2018) in related work and explains why they differ (one-demo vs. multi-demo; per-demo vs. uniform), but does not include a direct experimental comparison. A reimplementation or adaptation of these methods on the same tasks would more crisply isolate the value of the per-demonstration reverse curriculum. The comparison to JSRL (another reverse-curriculum method) is also limited because the paper only has access to JSRL's published Adroit numbers and cannot run it on other benchmarks — though this limitation is transparently acknowledged.

2. **Insufficient sensitivity analysis for key hyperparameters.** Several design choices are acknowledged as impactful but their sensitivity is not examined: the reverse step size δ, the forward-curriculum threshold ω, the dynamic timelimit ratio φ (values are said to be fixed per suite but not listed), and the number of episodes k used to compute the forward-curriculum score q. The paper would be strengthened by demonstrating robustness (or documenting brittleness) of these parameters, ideally via a sweep or at least a reported table of chosen values. The absence is not fatal — the method works with fixed default values across all tasks — but it makes reproduction harder than necessary.

3. **Incomplete hyperparameter disclosure.** The paper does not report specific values for δ, ω, β (temperature), φ, m (successes required for curriculum advance), or the staleness scaling factor in a consolidated table. While the values are said to be fixed per suite, the reader cannot determine what they are from the main text. This is a reproducibility concern that should be addressed in a final version.

4. **Statistical rigor on high-variance tasks.** The paper acknowledges high variance on PegInsertionSide and PlugCharger (one seed failing) and references a 30-seed version in Figure 9 (appendix). The main results use 5 seeds, which is reasonable for large-scale RL experiments, but on tasks where one seed flips the mean from ~60% to 0%, more explicit discussion of the failure mode and whether it is systematic would be helpful.

### Trivial

- The claim of novelty is modestly overstated in the abstract ("novel reverse forward curriculum learning"). The individual components — reverse curriculum from demonstration states, curriculum progression based on success — each have clear precedent. The paper's actual novelty lies in the per-demonstration variant and the specific combination of reverse+forward curricula, which is a solid but incremental contribution. The paper itself is reasonably transparent about this; toning down the "novel" language slightly would better match the content.

## Nice-to-Haves

- A sensitivity sweep or robustness figure for the two most important hyperparameters (δ and ω).
- Direct experimental comparison against a reimplementation of Nair et al.'s uniform-reset approach on the ManiSkill2 tasks, using the same number of demonstrations.
- A table of all hyperparameter values used for each environment suite.

## Removed Points

These points were flagged during review but removed after verification against the paper:

1. **"The paper uses 'state' and 'observation' interchangeably without acknowledging partial observability"** — The paper explicitly states at line 54: "for simplicity in this paper state also refers to observation." This is a deliberate modeling choice, not an oversight.

2. **"The paper does not compare against a uniform forward curriculum"** — Figure 5's "reverse curriculum only" ablation is defined as "RFCL but instead of a forward curriculum in stage 2 we sample uniformly from the initial state distribution." This is exactly the comparison the reviewer requested.

3. **"The definition of nonzero return is vague"** — The paper uses a sparse +1/0 reward throughout. "Nonzero return" means any episode that achieves success. This is unambiguous.

4. **"Parser artifacts about Figure 1 text, reproducibility statement, and Table 1"** — These are parser artifacts that strip content present in the original submission. Not author errors.

5. **"The forward curriculum's impact is under-validated because no comparison to uniform forward"** — As noted above, Figure 5 provides this comparison. The remaining question about sensitivity analysis is retained as a minor weakness above.

## Novel Insights

The reviews highlight an important tension not fully articulated in the paper: the reverse curriculum stage creates a policy that is *specialized* to a narrow set of initial states (demonstration start points), while the forward curriculum must *generalize* from these to the full initial state distribution. The critical insight — which the paper could emphasize more — is that the forward curriculum works *because* the reverse curriculum has already solved the exploration problem; without stage 1, the forward curriculum's adaptive scoring (which relies on detecting "nonzero return") has nothing to latch onto. This explains why "forward curriculum only" fails while the combination succeeds. The paper's ablations hint at this but do not draw out the dependency structure explicitly.

## Suggestions

1. Add a direct experimental comparison against a reimplementation of Nair et al.'s uniform-reset curriculum (or Resnick et al.'s single-demo reverse curriculum extended to multiple demos) on the ManiSkill2 tasks, even if only on a subset (e.g., the hardest tasks). This would be the strongest evidence that the per-demonstration variant matters.

2. Report all hyperparameter values (δ, ω, β, φ, m, k, staleness factor) in a consolidated table, ideally per environment suite, in the main paper or appendix.

3. Include a brief sensitivity analysis for δ and ω, even if only on one or two representative tasks (e.g., one easy and one hard ManiSkill2 task). This would demonstrate robustness and help practitioners apply the method.

4. Tone down the novelty language in the abstract and introduction slightly to avoid overclaiming. The paper's contributions are clear and well-supported by results; modest language ("effective combination" rather than "novel algorithm") would better align framing with content.

## Score and Decision

This is a solid paper with a clear empirical contribution. The method achieves impressive results on tasks that prior work cannot solve at all, under a setting (very few demonstrations, sparse rewards) that is practically important. The weaknesses are all addressable and none undermine the core claim. The paper is well-written, the experiments are extensive, and the accompanying website provides code and visualizations.

**Overall assessment:** Accept. The paper would be strengthened by addressing the hyperparameter disclosure and sensitivity analysis, but these are incremental improvements to an already sound submission.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>