Now I have all the information needed. Let me compile the final review.

## Summary

This paper introduces Agent Workflow Memory (AWM), a method that induces abstract, reusable sub-routine workflows from agent trajectories and integrates them into the agent's memory to guide future task-solving. AWM operates in both an offline setting (inducing workflows from training examples) and an online setting (inducing workflows from self-generated successful trajectories during streaming test-time inference). The method is evaluated on WebArena and Mind2Web, showing improvements over prior methods.

## Strengths

- **Well-motivated and clearly explained framework for reusable workflow induction** — The idea of extracting abstract sub-routines (e.g., "search for a product" rather than "buy dry cat food") from agent trajectories and abstracting away example-specific values is a useful conceptual contribution. The paper clearly distinguishes between concrete experiences and abstract workflows (§3.2–3.3), and the separation of concerns into an induction module and a memory integration step is clean.

- **Flexible dual-mode operation** — AWM is designed to work both offline from annotated training examples and online in a supervision-free streaming setting where workflows are induced only from self-generated successes (§3.3). This is a practical design choice since many real-world settings lack curated training data.

- **Thorough ablation studies** — The paper systematically investigates design choices: LM-based vs. rule-based induction (§6.1, Tables 3–4), code vs. text workflow format (§6.2, Table 5), NL descriptions vs. filtered HTML as environment representations (§6.3, Table 6), and action space expansion (§7, Table 7). These help isolate which design decisions matter.

## Weaknesses

### Fatal
None.

### Major

- **WebArena online evaluation confounds test-time adaptation with workflow induction** — On WebArena, AWM operates in the online streaming setting, learning from test queries as they arrive. The baselines (BrowserGym, SteP) are static and do not adapt. As the paper acknowledges (§4.1), WebArena has no training data, so only the online setting is feasible. However, this means the 51.1% relative improvement over BrowserGym conflates two factors: (1) the benefit of any test-time adaptation/memory accumulation, and (2) the specific benefit of inducing *abstract workflows* rather than, say, just storing full successful trajectories. An ablation that stores full successful trajectories (without abstraction into sub-routines) would isolate whether the abstraction step is responsible for the gains. Without it, the WebArena results demonstrate that an adapting system outperforms non-adapting systems, which is useful but weaker than the paper's implied claim about workflow induction *per se*. The Mind2Web offline results provide cleaner evidence on this front.

- **Ambiguity about which setting produces cross-domain generalization claims** — The abstract states "online AWM robustly generalizes in cross-task, website, and domain evaluations" (lines 10–11), but the Mind2Web cross-domain and cross-website results (which produce the 8.9–14.0 absolute point gains mentioned) are not explicitly labeled as offline or online in the paper's main text. The paper's description (§4.2) says both settings are explored for the cross-task split, but the source of the cross-domain/website numbers is unclear. If these are offline results, the "online" qualifier in the abstract is misleading; if they are online results, the same test-set adaptation confound applies.

### Minor

- **No analysis of the LM evaluator's accuracy in this setting** — The online loop depends entirely on the LM-based evaluation module from Pan et al. (2024) to gate which trajectories become workflows (line 109). The paper does not report precision, recall, or bias of this evaluator on WebArena or Mind2Web tasks. While the evaluator is from prior work, its reliability in the specific task distribution matters and is unexamined. (The paper references an appendix "examination of quality" for the induction module, but this is about induction quality, not the evaluator.)

- **No order-sensitivity analysis for the online streaming setting** — Online AWM processes test queries in a fixed streaming order (line 100). The order in which tasks are encountered affects which workflows are induced early and what experience is available for later tasks. The paper does not discuss whether results are robust to different orderings, and no randomization or variance estimates are reported.

- **Low absolute success rates on Mind2Web** — Task-level success rates on Mind2Web are 2–5% for all methods including AWM (Tables showing GPT-4 results). While this reflects benchmark difficulty and AWM does improve relative to baselines, readers should calibrate expectations accordingly.

### Trivial
None.

## Nice-to-Haves

- Adding a baseline that adapts via storing full successful trajectories (without sub-routine abstraction) would cleanly isolate the benefit of the abstraction step.
- Analyzing evaluator accuracy (precision/recall) and measuring sensitivity to evaluator errors would strengthen the online results.
- Reporting order-sensitivity or running multiple random orderings would address a natural concern about the streaming evaluation protocol.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh critic's claim that the evaluator issue is "evidential of the first order"**: While the evaluator's accuracy is unexamined, this is a missing analysis rather than a fundamental flaw. The evaluator is from established prior work (Pan et al., 2024), and the paper's appendix (stripped by the parser) may contain further quality analysis. Moved from "fatal" to "minor."
- **Harsh critic's claim that the paper "does not currently establish that workflow induction per se is responsible for the reported gains" on WebArena**: This conflates two issues. The WebArena results show that an adapting AWM system outperforms non-adapting baselines — this is a valid result, just not one that isolates the abstraction step's contribution. The paper has enough other evidence (offline Mind2Web, ablations) to establish that workflows contribute to the gains. The criticism is valid but overstated.
- **Strength Finder's "large and consistent performance gains" claim about WebArena's 51.1%**: Rephrased to clarify the confound rather than presenting it as unqualified evidence.
- **"Order sensitivity" from the harsh critic's "Missing Experiments"**: Moved to Minor weaknesses.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **For the WebArena experiment**: Add an ablation that stores full successful trajectories (without abstraction into sub-routines) in memory during online streaming, to isolate whether the abstraction into reusable sub-routines is what drives the gains versus generic test-time adaptation.
2. **Clarify the Mind2Web cross-domain/website experimental setting**: Explicitly state in §4.2 whether these generalization results use the offline setting (inducing from training domains and applying to unseen domains) or the online setting, and adjust the abstract's phrasing accordingly.
3. **Provide evaluator accuracy statistics**: Report the precision and recall of the LM evaluator (Pan et al., 2024) on a held-out subset of tasks from each benchmark.

## Score and Decision

**Originality**: The idea of inducing abstract, reusable sub-routines and abstracting away example-specific values is a useful contribution, though related to prior work on skill discovery (Voyager, Trove). The dual offline/online framing is clean.

**Importance of research question**: Web agents that can learn from experience and generalize across tasks/domains is an important and timely problem.

**Claims support**: Partially supported. The Mind2Web offline results provide cleaner evidence than the WebArena online results, which conflate test-time adaptation with workflow abstraction.

**Soundness of experiments**: The ablation studies are thorough and honestly evaluated. The main experimental confound (online adaptation vs. static baselines on WebArena) is a structural issue that limits what can be concluded from the headline results.

**Clarity of writing**: The paper is clearly written and well-structured. The method description is easy to follow.

**Value to the community**: The concept of abstract workflow induction and the experimental framework are valuable, but the confounded comparison reduces the strength of the evidence.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>