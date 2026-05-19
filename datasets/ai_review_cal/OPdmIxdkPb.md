- Decision: Reject
- Avg Score: 4.75
- Scores: 3, 3, 8, 5
Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

---

## Summary

This paper compares two paradigms for leveraging LLMs in query-efficient planning: using the LLM as a *heuristic* within a search-based planner (ToT-I, instantiated as ToT-DFS and ToT-BFS) versus using the LLM as a *generative planner* that proposes entire action sequences and adapts them based on world-model feedback (Boomerang). The main empirical finding is that the generative planner achieves higher success rates under a fixed query budget across Blocksworld (78%), Logistics (82%), Grippers (89%), and Robotouille (57%), outperforming both LLM-based baselines (ReAct, ToT-DFS/BFS) and classical planners (FastDownward). The paper argues that generative planners are more adaptive to feedback because they can revise entire plans, whereas heuristic methods remain constrained by the search tree.

---

## Strengths

1. **Clear paradigm-level comparison with consistent advantages.** The paper defines two competing frameworks cleanly and demonstrates that Boomerang outperforms all baselines across all four domains (Blocksworld: 78% vs FD 63% vs ReAct 52%; Logistics: 82% vs ToT-DFS 4%; Grippers: 89% vs ToT-DFS 31%; Robotouille: 57% vs ToT-DFS 17%). The consistency of the advantage across diverse domains (PDDL benchmarks and a realistic simulator) supports the robustness of the finding.

2. **Principled formalization of query-efficient planning.** Section 2 formulates the problem as a policy $\pi(q_k | \phi, H_k)$ over state-action queries, which cleanly unifies both paradigms and highlights why ReActSelect (the "gold standard" policy over *all* state-action pairs) is intractable. This framing provides a solid conceptual foundation for the algorithmic design choices.

3. **Mechanistic explanation for why generative planners succeed.** The paper identifies a concrete failure mode: heuristic planners get trapped in *cul-de-sacs* because they can only select among nodes the search tree offers, while Boomerang can incorporate cul-de-sac feedback to re-route the entire plan in the next iteration. This is a specific, falsifiable, and domain-independent explanation that goes beyond reporting aggregate numbers.

4. **Connection to lazy-search theory.** Drawing a link between Boomerang (full-plan generation with feedback) and posterior sampling in lazy search (Section 3.2) grounds the approach in established planning theory rather than treating it as an ad-hoc prompt scheme. This gives the work theoretical anchoring beyond pure empiricism.

5. **Large-scale evaluation across multiple domains.** The paper tests on 900 problems (600 Blocksworld + 100 each for Logistics, Grippers, Robotouille), covering both classic PDDL environments and a realistic robotics simulator. This breadth reduces the risk that results are an artifact of a single benchmark.

---

## Weaknesses

### Fatal
None.

### Major

1. **Missing a directly comparable generative baseline (Reflexion).** The paper evaluates Boomerang against ReAct and ToT-DFS/BFS, but Reflexion (Shinn et al., 2023) — which is cited in related work and also generates trajectories with iterative refinement based on environment feedback — is not included as a baseline. Reflexion builds multiple ReAct trajectories with a reflection step between them, making it a natural point of comparison within the generative paradigm. Without this comparison, it is difficult to assess whether Boomerang's advantages stem from its specific design (full-plan generation in one shot) or simply from the general generate-and-refine loop. The paper's central claim would be substantially strengthened by including Reflexion and discussing where the two approaches diverge.

2. **Unsubstantiated theoretical claim about a Bayesian regret bound.** The main text (Section 3.2) states: *"We derive a Bayesian regret bound that is sub-linear with the planning iterations needed by Boomerang before it returns a feasible solution."* No bound, theorem statement, or even the form of the bound (e.g., $O(\sqrt{T})$, $O(\log T)$) is presented — only a conceptual connection to posterior sampling. If the bound exists in the appendix, the main text should at minimum state the result and its assumptions. As it stands, this is a substantive claim that cannot be evaluated. The authors should either state the bound explicitly or temper the claim.

### Minor

3. **LLM model and hyperparameters not specified in the main text.** The paper never states which LLM was used (e.g., GPT-4, GPT-3.5, Claude), what temperature was used, or the specific beam sizes / $k$ values for ToT-BFS and ToT-DFS. These details are critical for reproducibility and for assessing whether the heuristic methods were reasonably tuned. (If these appear in the ablation sections or appendix of the original submission, they should be summarized in the main text.)

4. **Success-under-budget is the primary reported metric but raw query counts are not presented in text.** The paper states it measures average query counts (Section 4.1), but the text reports only success rates. Success-under-budget is a reasonable proxy — if a method uses fewer queries per plan, it will succeed more often under a fixed budget — but the headline claim about query *efficiency* would be more directly supported by reporting average queries and their variance. (If query counts appear in figures that were not available in the extracted text, they should also be reported numerically.)

5. **The performance gap for heuristic methods on some domains is very large, raising questions about tuning.** ToT-DFS achieves only 4% on Logistics, 31% on Grippers, and 17% on Robotouille. While the paper's narrative (heuristics can't escape cul-de-sacs) provides a post-hoc explanation, these extremely low success rates suggest the implementation may not represent the best possible instantiation of the heuristic paradigm. Some ablation showing whether different beam sizes, $k$ values, or prompt designs significantly change heuristic performance would strengthen the comparison.

### Trivial
None.

---

## Nice-to-Haves

- Direct query count distributions (with variance) alongside success rates.
- An analysis of how Boomerang's performance changes with the number of allowed iterations/plans.
- Inclusion of RAP (Hao et al., 2023) or LLM-MCTS as additional heuristic-paradigm baselines, to show that the generative advantage holds against more sophisticated search strategies.

---

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Unfair comparison: heuristic methods use a coarse state evaluator."** The critic argued that ToT's three-category heuristic (Impossible/Maybe/Certain) is too coarse to be fair. This is not a weakness of the comparison — it is a *structural feature* of the heuristic paradigm. Heuristics evaluate individual states; giving them full-plan-level feedback would blur the paradigm distinction the paper is studying. The paper's core argument is precisely that this structural limitation makes heuristics less adaptive. Removed.

- **"Missing RAP and LLM-MCTS baselines."** These fall under the heuristic paradigm (LLM-guided search), for which the paper already includes ToT-BFS and ToT-DFS as representative instantiations. Including every possible heuristic variant is not required. Removed.

- **"Query efficiency claim unsubstantiated without raw query counts."** As noted above, success-under-budget is a valid, commonly used proxy for query efficiency. The paper also reports measuring query counts, which presumably appear in figures. This is retained as a Minor weakness (point 4 above) rather than removed entirely, but the stronger version of this criticism is rejected. Demoted from "structural flaw" to Minor.

- **Speculative complaints about confidence intervals / multiple runs.** The paper runs on 600+100+100+100 problems per condition, which gives substantial statistical power. Demanding confidence intervals for every point estimate when the problem count is this large is a generic nitpick. Removed.

- **"Theoretical bound not in main text — unverifiable."** This is retained as Major weakness 2 above, but I note that the parser strips appendices; if the full derivation appears in the appendix of the original submission, the main text should still state the bound's form. The criticism is kept but downgraded from "methodological gap" to Major rather than Fatal.

---

## Novel Insights

None beyond the paper's own contributions. Both reviewers' comments surface genuine concerns about missing baselines and unsubstantiated theoretical claims, but do not identify novel weaknesses or interpretations that the paper itself does not already touch upon.

---

## Suggestions

1. **Add Reflexion as a baseline.** This is the single most impactful addition: it directly addresses whether Boomerang's design (full-plan generation in one shot with feedback on the whole plan) adds value beyond the generate-and-refine loop already present in Reflexion.

2. **State the regret bound explicitly in the main text** (even if the full proof is deferred to the appendix). A simple theorem statement — e.g., "Boomerang achieves Bayesian regret $R(T) = O(\sqrt{T})$ under assumptions X, Y, Z" — would transform the vague theoretical claim into a verifiable contribution.

3. **Report query counts directly** in a table (mean and variance per method per domain) to complement the success-rate figures. This directly addresses the "query efficiency" claim.

4. **Specify the LLM model, temperature, and key hyperparameters** (beam size $b$, action set size $k$, query budget per domain) in the main experimental setup section.

5. **Diagnose why ToT-DFS performs so poorly on Logistics (4%).** A brief ablation showing whether this is due to the state evaluator, the action proposer, or a poor beam configuration would clarify whether the comparison is fair to the heuristic paradigm.

---
