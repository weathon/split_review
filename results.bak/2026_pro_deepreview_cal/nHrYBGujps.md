Now I have a thorough understanding of both the paper and the calibration landscape. Let me synthesize the final review.

---

## Summary

BIRD-INTERACT introduces a benchmark for interactive text-to-SQL that replaces static dialogue transcripts with a dynamic, function-driven user simulator and two evaluation modes: a protocol-guided conversational setting (*c*-Interact) and an autonomous agentic setting (*a*-Interact). The benchmark comprises 900 tasks (600 FULL, 300 LITE) constructed by systematically injecting ambiguities and state-dependent follow-up sub-tasks into single-turn SQL tasks, spanning the full CRUD spectrum. Evaluation of seven frontier LLMs reveals very low success rates (GPT‑5 achieves only 8.67% end-to-end on FULL in *c*-Interact and 17.00% in *a*-Interact), and targeted experiments — memory grafting and interaction test-time scaling — isolate communication strategy as a key bottleneck beyond SQL generation ability.

## Strengths

- **Function-driven user simulator is a genuine methodological contribution with strong validation.** The two-stage design (LLM semantic parser → constrained symbolic action → controlled response) demonstrably prevents ground-truth leakage: on the USERSIM‑GUARD dataset, failure rates for unanswerable questions drop from 67.4% (baseline) to 2.7% (Figure 6). Human-alignment is corroborated by a Pearson correlation of 0.84 (p=0.02, Table 3) between simulator-driven and human-driven success rates. This directly addresses a known weakness in LLM‑simulated interactive evaluation.

- **The task suite introduces principled, verifiable interactive difficulty.** The ambiguity injection taxonomy (superficial query ambiguity, knowledge chain breaking, environmental noise) and the state‑dependent follow‑up sub‑task design (Section 3.2) create tasks that are provably unsolvable without interaction yet reconstructable once clarifications are given. The resulting difficulty is genuine: even the strongest model reaches only 8.67% overall success rate on BIRD‑INTERACT‑FULL in *c*-Interact (Table 2).

- **Memory grafting experiment cleanly isolates communication as a bottleneck.** By transplanting clarification histories from stronger models (Qwen‑3‑Coder, O3‑Mini) into GPT‑5 (Section 5.2, Figure 5), success rate rises from 13.8% to 20.5% without changing the SQL generator. This directly supports the paper's central claim that strategic interaction skill — not just SQL generation — drives multi‑turn text‑to‑SQL performance.

- **Dual evaluation settings reveal complementary model behaviors.** The contrast between *c*-Interact (protocol‑guided) and *a*-Interact (agentic) surfaces meaningful differences: GPT‑5 ranks worst in *c*-Interact (14.50% SR) but best in *a*-Interact (29.17% SR, Table 2), providing actionable insight into how interaction paradigms interact with model architectures.

- **Broad task coverage across CRUD operations and domain types.** The benchmark includes 190 DM tasks alongside 410 BI tasks (Table 1), evaluates both analytical and operational SQL, and reports separate metrics for each category (Table 2), offering a more complete assessment than SELECT‑only benchmarks.

## Weaknesses

### Fatal

None.

### Major

None. The core claims are well-supported by the evidence presented.

### Minor

- **The "ITS Law" language overstates the evidence (Section 5.2).** The paper states that a model "satisfies this law if, given enough interactive turns, its performance can match or even surpass that of the idealized single‑turn task." Figure 4 shows suggestive scaling trends for a few models on the LITE set, but no model demonstrably reaches or surpasses idealized performance within the tested patience range (0–7). The claim is better framed as an observed scaling behavior rather than a "law." Moderating the language to "ITS scaling trend" or similar would align the claim with the evidence without diminishing the genuine finding.

- **No explicit limitations section.** The paper acknowledges some limitations in the Future Work section (Section 8), such as the absence of a free‑mode complement to the budget‑constrained *a*-Interact setting. However, a dedicated limitations section would strengthen transparency — for instance, noting that the benchmark inherits biases from the underlying LIVESQLBENCH tasks, that the two‑subtask structure may not capture arbitrarily long conversational threads, and that the user simulator still relies on an LLM parser (even if validated as high‑accuracy).

### Trivial

- **User simulator backbone for main experiments is not explicitly stated.** The cost footnote in Section 5 says $0.03/task but does not name the model. From Section 6 one can infer it is GPT‑4o or Gemini‑2.0‑Flash, but stating this explicitly in Section 4 or 5 would improve reproducibility.

- **Budget parameter justification is absent.** The formulas for $\tau_{\text{clar}}$ and $B$ are given (Section 4), but the choices of $\lambda_{\text{pat}}=3$, $B_{\text{base}}=6$, and the factor‑of‑2 in the agentic budget are not explained. A brief note on how these were set (pilot experiments, resource reasoning) would help readers interpret the evaluation design.

- **Model set inconsistency between LITE and FULL experiments.** Figure 4 (LITE ITS experiment) uses Claude‑3.7‑Sonnet, O3‑Mini, GPT‑4o, and Qwen‑3, whereas Table 2 (FULL) uses GPT‑5, Claude‑Sonnet‑4, and others. A brief acknowledgment of this difference would prevent reader confusion.

## Nice-to-Haves

- **Downstream impact of simulator quality on model rankings.** The paper convincingly shows the function‑driven simulator is more reliable (Section 6), but does not demonstrate whether a lower‑fidelity simulator would change the relative ranking or absolute scores of tested models. A small‑scale ablation comparing results with a baseline simulator vs. the proposed one on the LITE set would sharpen the claim that difficulty stems from task design rather than simulator strictness.

- **Deeper categorization of failure modes.** The paper gives aggregate SR and reward. A coarse breakdown of why tasks fail (insufficient clarification, incorrect SQL despite clarification, failure to track state in follow‑ups) — even on a subset — would help the community focus research efforts.

- **Action distribution context for *a*-Interact.** The paper reports that *submit* and *ask* dominate action distributions (60.87% combined). A brief discussion of whether prompt design or explicit action‑cost structure might bias models toward these actions would prevent over‑interpretation.

## Removed Points

These points were flagged in the input reviews but are removed from the final review. Treat them with caution.

- **"All experiments are single runs with temperature 0 — even temperature 0 can exhibit small runtime variations for closed‑source models."** REMOVED. This is a negligible limitation; deterministic evaluation with temperature 0 is standard practice for benchmark evaluation, and any runtime variation would be trivially small and not affect conclusions.

- **"The p‑values in the human‑alignment study (0.02, 0.03) are borderline."** REMOVED. A p‑value of 0.02 is statistically significant at the standard α=0.05 threshold; calling this "borderline" is incorrect. The correlations themselves (0.84, 0.79) are strong.

- **Any concern about model/tool/benchmark existence or availability.** REMOVED per hard rules — all cited resources exist.

## Novel Insights

The memory grafting experiment (Figure 5) is the paper's most striking finding and one that generalizes beyond text‑to‑SQL: it demonstrates that a model's interactive communication skill can be decoupled from its core task competence, and that transplanting interaction histories from a more communicatively adept model can substantially improve outcomes. This suggests that interaction strategy may be a distinct capability dimension that is undertrained in current LLMs, with implications for agent design beyond the database domain.

## Suggestions

- Add a short Limitations section before Future Work, acknowledging the inherited biases from LIVESQLBENCH, the two‑subtask structure, and the LLM‑parser dependency of the simulator.
- Replace "ITS Law" with "ITS scaling behavior" and rephrase the claim to match Figure 4's evidence: "some models show monotonic performance gains with additional interaction turns, narrowing the gap toward idealized single‑turn performance."
- Explicitly state the simulator backbone model used in Section 5 experiments.
- Add a one‑sentence justification for the budget parameter choices ($\lambda_{\text{pat}}=3$, $B_{\text{base}}=6$, factor‑of‑2).
- Note the model‑set difference between LITE ITS experiments and FULL main experiments.

## Score and Decision

**Anchor comparison:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| DB‑GPT‑Hub (NmILZXKcOi) | 3.75 | R1 | BIRD‑INTERACT is substantially stronger — it is a genuine benchmark contribution with novel task design and simulator, not just a framework integration. |
| CHASE‑SQL (CvGqMD5OtX) | 6.25 | R1 | Different genre (method vs. benchmark). BIRD‑INTERACT's contribution as a benchmark is more cohesive and its experimental analysis is comparably thorough. |
| MINT (jp3gWrMuIZ) | 6.75 | R2 | Closest topical match (multi‑turn interactive benchmark). BIRD‑INTERACT's user simulator design is more carefully validated (USERSIM‑GUARD, human alignment), its task construction is more principled (ambiguity taxonomy, state dependency), and its domain‑specific focus enables deeper analysis (memory grafting). BIRD‑INTERACT is clearly stronger. |
| DiscoveryBench (vyflgpwfJW) | 7.00 | R2 | Both are well‑constructed domain benchmarks. BIRD‑INTERACT's simulator innovation and dual‑mode evaluation give it an edge. Comparable or slightly stronger. |
| LiveBench (sKYHBTAxVa) | 7.33 | R2 | Both are challenging, well‑validated benchmarks. LiveBench's core "contamination‑free" claim faced significant reviewer pushback; BIRD‑INTERACT's core claims are better supported. BIRD‑INTERACT is comparable, slightly stronger. |
| WildBench (MKEHCx25xp) | 7.33 | R2 | WildBench curates real user queries with LLM judging; BIRD‑INTERACT builds a principled interactive task suite with executable ground truth. Different strengths, comparable quality. |
| Spider 2.0 (XmProj9cPs) | 8.00 | R1/R2 | Most similar benchmark paper. Spider 2.0's enterprise scope (multi‑dialect, real‑world data, codebase integration) is more ambitious. BIRD‑INTERACT's contribution in the interactive dimension and user simulator design is novel but more narrowly scoped. BIRD‑INTERACT is slightly below Spider 2.0. |

**Round‑1 bracket:** 6.5–8.0 (between CHASE‑SQL at 6.25 and Spider 2.0 at 8.00).

**Round‑2 narrowing:** The paper is clearly stronger than MINT (6.75) and comparable to LiveBench/WildBench (~7.33). It falls slightly short of Spider 2.0 (8.00) due to narrower scope and minor presentation issues (ITS Law language, missing limitations section). 

**Final Score: 7.5**

This reflects a strong benchmark paper with a well‑validated methodological contribution (the function‑driven simulator), principled task construction, and insightful experiments, held back from the 8.0+ range only by minor overclaiming of one finding and the absence of an explicit limitations section — both trivially fixable.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>