Here is my consolidated review after carefully cross-referencing reviewer claims against the paper.

---

## Summary

PLAGUE introduces a modular three-phase framework (Planner, Primer, Finisher) for generating multi-turn jailbreak attacks on LLMs. The framework disentangles plan initialization, context building, and final-prompt generation, and augments attacks with a memory-based strategy retrieval mechanism. Evaluated on HarmBench against frontier models (o3, o1, Claude Opus 4.1, Deepseek-R1, Llama 3.3-70B), PLAGUE achieves StrongREJECT ASR of 81.4% on o3 and 67.3% on Claude Opus 4.1—substantial absolute improvements over prior multi-turn attacks—with comparable or lower query budgets. The paper's core technical contribution is the clean decomposition of multi-turn attacks into interchangeable phases, validated through systematic component ablation and a finisher-substitution experiment.

## Strengths

- **Well-designed modular framework with systematic validation.** The three-phase decomposition (Planner → Primer → Finisher) is a clean architectural abstraction that disentangles plan generation, context escalation, and final execution. The paper validates this design empirically: Table 3 traces the incremental contribution of each component (backtracking, reflection, planner, strategy retrieval) from a GOAT baseline, showing, for example, that reflection provides the largest single gain on o3 (+0.149 SRE) while backtracking is most impactful on Claude Opus 4.1 (+0.174 SRE). Table 4 further validates modularity by swapping the GOAT finisher for Crescendo on Claude Opus 4.1, raising SRE from 0.222 to 0.673. This is concrete, comparative evidence for the plug-and-play claim.

- **Strong empirical results on resistant frontier models.** PLAGUE achieves 81.4% SRE on OpenAI o3 (vs. next-best multi-turn baseline 61.6%) and 67.3% SRE on Claude Opus 4.1 (vs. 48.0% for base Crescendo). These are meaningful absolute gains on models widely considered among the most safety-aligned. The results on Deepseek-R1 (97.8% SRE), o1 (93.1%), and Llama 3.3-70B (95.8%) demonstrate broad effectiveness.

- **Efficiency analysis with concrete query counts.** Table 5 provides per-method breakdowns of target, evaluator, and planner-phase LLM calls. Despite the additional Planner component, PLAGUE's total call count is comparable to Crescendo and within one call of GOAT (e.g., on o3: PLAGUE 6.53 total calls vs. Crescendo 5.28 vs. GOAT 3.08). The Planner phase requires only 1 Attacker call vs. ActorBreaker's 4. This demonstrates that the performance gains are not simply due to higher query volume.

- **Model-differentiated analysis of component contributions.** The paper observes that reflection dominates gains on o3 while backtracking dominates on Claude Opus 4.1 (Table 3). This provides actionable insight for practitioners: different models have different vulnerabilities, and the framework's modularity enables targeted customization.

## Weaknesses

### Fatal
None. The paper's core claims are supported by the evidence presented; no error invalidates the overall contribution.

### Major

- **Asymmetric baseline constraints weaken comparative claims.** The paper modifies several baselines in ways that are not applied symmetrically to PLAGUE, which undercuts the headline comparative claims ("improving by more than 30%"). Specifically:
  - **Crescendo's backtracking is removed** (Section 4: "We remove any explicit backtracking counts from their attack"), while PLAGUE retains its own backtracking mechanism. Backtracking is an integral part of Crescendo's ability to recover from dead ends; disabling it while keeping PLAGUE's equivalent is not an apples-to-apples comparison. The budget standardization (6 turns) could have been applied to Crescendo *with* backtracking by letting backtracking consume turns from the budget, as is done for PLAGUE.
  - **ActorBreaker is limited to 2 actors**, whereas its design relies on diverse actor exploration. The paper's rationale (matching ASR@K to K=2) is reasonable, but the paper does not quantify how much performance ActorBreaker loses under this constraint versus its standard configuration.
  
  These issues do **not** invalidate the paper's results—the gaps are large enough (e.g., 81.4% vs. 61.6% on o3) that even restored baselines would likely not overturn the main findings—but they do mean the precise "32.14%" and "40.2%" improvement figures rest on comparisons that are not strictly fair. The paper should present comparisons against fully-capable baselines (with matching budget constraints applied neutrally) alongside the constrained ones, or should apply identical constraints to PLAGUE's own components.

- **"Lifelong learning" framing exceeds the evidence.** The paper repeatedly frames lifelong learning as a central contribution (title, abstract, Section 3.3.1, Section 3.5). However, the mechanism is a vector-store that (a) is initialized with only two strategies from Crescendo, (b) adds strategies when attacks succeed, and (c) retrieves by cosine similarity. The paper demonstrates that adding RSS (retrieving successful strategies) improves ASR (Table 3: +0.041 SRE on o3, +0.034 on Claude Opus 4.1), but it provides **no sequential multi-goal evaluation** that would substantiate "lifelong" learning—i.e., there is no experiment showing that performance improves over a sequence of attack goals as the memory bank grows, that the library does not saturate, or that retrieval is meaningfully better than a random static set of seed strategies. The improvement attributed to "lifelong learning" could equally come from a well-chosen initial seed or a single round of in-context learning. The "lifelong" framing should either be supported with a proper sequential evaluation or scaled back to "memory-augmented planning."

### Minor

- **No variance or confidence intervals reported.** Key ASR results (Table 2, Table 3, Table 4) are reported as point estimates "averaged over three runs" with no standard deviations or confidence intervals. Given the high stochasticity of multi-turn attacks (plan sampling, LLM output variance, backtracking decisions), a gap of 0.01–0.04 between configurations could easily fall within noise. The paper uses ASR@K=2 to mitigate variance, which is noted, but standard deviations would substantially increase confidence in the headline comparisons. This is standard practice in empirical ML papers and would be inexpensive to provide.

- **Attacker model sensitivity unexplored.** All experiments use Deepseek-R1 as the sole Attacker model (Section 4). The paper claims PLAGUE is a "plug-and-play framework," but the extent to which its strong results depend on the reasoning ability of Deepseek-R1 is not tested. Evaluating with a cheaper or weaker attacker (e.g., GPT-4o-mini, Llama 3-70B) would demonstrate generality and would clarify whether the framework's benefits are separable from the attacker model's capability.

- **Rubric scorer design choices are heuristic and unanalyzed.** The Rubric Scorer assigns 4 points for relevance and 2 points each for three other dimensions, with a threshold of 8/10 for success and 7/10 for the Primer phase. The paper provides no sensitivity analysis for these thresholds. The scoring heuristic is central to the backtracking/reflection logic, and its influence on the reported ASR is unknown.

- **GOAT modifications' effect is asserted without evidence.** The paper modifies GOAT's evaluation environment (per-round rubric scoring instead of consolidated evaluation) and disables attack history, claiming the impact is "negligible" based on "extensive ablation" (Section 4). The ablation is not presented; this claim is unsupported in the main text. While the per-round scoring change likely *helps* GOAT (more feedback), the net effect of both changes is unclear.

### Trivial
None.

## Nice-to-Haves

- **Qualitative failure analysis.** The paper notes that performance plateaus around 6 turns and that long context causes semantic drift (Section 5.2). A breakdown of *how* plans fail (drift vs. refusal vs. weak final query) would deepen the contribution and help guide further improvements.
- **Memory bank saturation study.** Does retrieval quality degrade or plateau as the library grows? Is there a risk of catastrophic interference or diminishing returns as more strategies are added?
- **Comparison of RSS against a random static strategy set.** To strengthen the claim that retrieval *from a growing bank* is the source of improvement, the paper could compare RSS against an equally sized random static set of unrelated strategies.
- **Test with alternative budget limits.** All experiments use a fixed 6-turn / K=2 budget. Testing with different budgets (e.g., 4 turns, 8 turns) would characterize the framework's robustness to budget constraints.

## Removed Points

The following points from the original reviews are removed per the filtering guidelines:

- **GOAT evaluation environment "alteration" as a weakening**: The critic claimed GOAT's evaluation environment was "altered" in a way that handicaps it. In fact, the change (invoking Rubric Scorer after each round instead of only at the end) gives GOAT more per-round feedback, which likely *improves* GOAT's performance. This criticism is factually inverted and does not support the claim of asymmetric weakening.
- **ActorBreaker target calls cited as "standard" values**: The critic claimed "the paper reports standard ActorBreaker uses 4–5.8 target calls in Table 5." Table 5 reports ActorBreaker's *constrained* (2-actor) configuration, not its standard one. The specific numerical claim is incorrect, though the general concern about the actor constraint remains valid.
- **Missing appendix content (Table 6, Appendix C.4)**: The critic faulted the paper for not presenting X-Teaming/FITD data and for insufficient appendix content. The appendix is stripped by the PDF parser and is present in the original submission.
- **AutoDAN-Turbo as "conceptually confused" baseline**: The critic argued that comparing a single-turn method over 6 rounds is confused. Many prior papers compare single-turn and multi-turn methods under equal turn budgets; this is a standard practice, not a confusion.
- **Related works omissions**: Removed per rule.
- **Formatting/style/typo nitpicks**: Removed per rule.
- **Speculative claims about what the appendix might contain**: Removed per rule.

## Novel Insights

The most interesting observation emerging from the reviews is the **model-dependent component sensitivity**: reflection dominates gains on o3 while backtracking dominates on Claude Opus 4.1 (Table 3). This is not just a minor ablation result—it suggests that different frontier models have qualitatively different failure modes under multi-turn attacks, and that a one-size-fits-all attack design is suboptimal. The paper's modular framework (enabling practitioners to swap in/out backtracking, reflection, or planning for specific target models) is more valuable in light of this result than the "lifelong learning" framing, which is less well-supported. The review process also highlights a tension in red-teaming evaluation: standardized budgets are necessary for fair comparison, but they interact destructively with methods whose core mechanisms (e.g., Crescendo's backtracking) intrinsically consume turns.

## Suggestions

1. **Restore Crescendo's backtracking within the 6-turn budget** for the main comparison, or apply the same constraint to PLAGUE's equivalent mechanism. Report both the budget-constrained and fully-capable baseline results so readers can assess the impact of standardization choices.

2. **Add a sequential lifelong learning experiment**: run PLAGUE over a sequence of 50–100 attack goals, tracking ASR as a function of the number of past successes absorbed into memory. If performance improves measurably over the sequence, the "lifelong" framing is supported; if not, reframe the contribution as "memory-augmented planning" or "experience retrieval."

3. **Report standard deviations or 95% confidence intervals** for all ASR tables, computed over the three runs.

4. **Add an ablation with a cheaper attacker model** (e.g., GPT-4o-mini or Llama 3-70B) to separate the framework's contribution from the attacker model's capability.

5. **Analyze rubric scorer threshold sensitivity** by varying the success threshold (±1 point) and reporting the resulting ASR range.

## Score and Decision

**MY FINAL SCORE: <score>7.0</score>**
**MY FINAL DECISION: <decision>Accept</decision>**