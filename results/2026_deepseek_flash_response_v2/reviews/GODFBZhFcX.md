## Summary

PCE proposes a Planner-Composer-Evaluator framework that extracts implicit environmental assumptions from LLM reasoning traces, structures them into a decision tree, and scores each path by likelihood, gain, and cost for uncertainty-aware action selection in multi-agent embodied planning. The key idea is to replace communication-heavy coordination with structured reasoning over the assumptions already latent in LLM outputs.

## Strengths

1. **Consistent task-performance improvement across three LLM backbones and two benchmarks**: Tables 1 and 2 show PCE achieves the best Total Steps on C-WAH and highest Total success rate on TDW-MAT against all four baselines in every backbone condition. This cross-backbone, cross-benchmark consistency is strong evidence that the benefit is not an artifact of a particular model or environment.

2. **PCE's gains are empirically shown to be additive to scaling, not reducible to it**: Figure 3 plots Total Steps against model size (4B→12B→27B) and reasoning depth (Low→Medium→High), comparing PCE against a Planner-only ablation. At every scale, PCE achieves substantially lower steps, and the Planner-only variant shows only modest improvement from scaling alone. This directly supports the core claim that structured uncertainty handling complements scaling.

3. **Component ablation confirms all three modules are indispensable**: Table 3 shows that removing any module (Planner, Composer, or Evaluator) degrades performance relative to full PCE, validating the three-module design.

4. **Dramatic communication reduction while improving task performance**: On C-WAH with GPT-4o mini, PCE uses 1.70 communication actions per episode vs. 9.88–10.24 for baselines — a 72–83% reduction — while achieving the fastest task completion. On TDW-MAT the gap is even wider (PCE: 3.58 vs. baselines up to 108.92).

5. **Principled scoring formulation grounded in DEC-POMDP theory**: The Evaluator's utility function (Eq. 1–3) decomposes action selection into scenario likelihood, conditional gain, and execution cost with explicit movement/communication cost terms, providing a cleaner formal treatment than the ad-hoc dialogue mechanisms in baselines.

## Weaknesses

### Major

1. **No variance or uncertainty reporting across all experiments**: Tables 1, 2, and 3 report only point estimates without standard deviations, confidence intervals, or any indication of the number of independent runs. Since every system uses stochastic LLMs whose outputs vary across calls, single-number comparisons are not statistically informative. We cannot tell whether observed differences (e.g., PCE 42.76 steps vs. REVECA 46.80 steps in C-WAH with GPT-4o mini, or PCE 87.50% vs. CaPo 73.33% in TDW-MAT) are meaningful or within noise. This limits the strength of the paper's comparative claims.

2. **C-WAH benchmark has only 10 evaluation episodes**: The paper states C-WAH "consists of 10 episodes." With only 10 episodes per condition (and combined with no multi-seed reruns), a single difficult or easy configuration can substantially shift aggregate results. TDW-MAT is somewhat better at 24 episodes but still modest. This limits confidence in the reported rankings, though it is a limitation shared with prior work on the same benchmark.

### Minor

3. **Token usage claims are overstated for TDW-MAT**: The paper claims "comparable token usage," but in TDW-MAT, CoELA consistently achieves substantially lower total token consumption than PCE across all three backbones (30%–47% less). While PCE's token usage is lower than most other baselines (CaPo, CoTS, REVECA) and the per-step overhead is acknowledged, the headline claim of "comparable" does not accurately characterize the CoELA comparison in TDW-MAT. In C-WAH the claim is reasonable (PCE is best or second-best across backbones).

4. **User study measures passive observation, not active collaboration**: The study (Section 5.3) has 12 participants who "received the same observations and action choices as the agent" — i.e., passively watched the agent's actions rather than actively collaborating. This tells us about perceived behavior, but does not directly support the paper's stated motivation about human-agent teamwork where "continuous questioning and reporting can disrupt established workflows." An interactive within-subjects design would be needed to test that claim. The small sample size (n=12) and absence of statistical testing further limit the strength of the conclusions.

5. **Cost function formulation imprecision (Eq. 1)**: The constraint 𝟙{move(a)} + 𝟙{comm(a)} = 1 implies every action must be classified as either movement or communication. However, the paper also describes actions like grasping, opening containers, and transporting targets (Section 4.5) — physical actions that are neither movement (traversal distance) nor communication. In practice they likely incur zero cost under the current formulation (d(a)=0), which is reasonable, but the hard constraint is imprecise and should be clarified.

### Trivial

6. **The user study lacks statistical testing**: Likert-scale results (Figure 4) are reported as average scores without significance tests or variance bars. With only 12 participants, it is unclear whether the observed differences are statistically reliable.

## Nice-to-Haves

- Run experiments with multiple seeds (at least 3–5) and report mean ± std or confidence intervals to enable statistical comparison.
- More precisely qualify the token usage claim: acknowledge CoELA's efficiency advantage in TDW-MAT and frame PCE's contribution as better task performance with moderate additional computational cost.
- Briefly summarize the findings from the human-expert correlation studies (Appendices A.10, A.11) in the main text to directly address concerns about Evaluator estimate quality.
- Expand the user study to an interactive setting with active human collaboration.

## Removed Points

- **"Evaluator's likelihood and gain estimates have no validation"**: REMOVED. The paper explicitly states (line 268) that "reliability assessments of the Composer and Evaluator based on human-expert correlation studies" are presented in Appendices A.10 and A.11. The authors do provide validation; it is deferred to the appendix due to space constraints, which is standard practice.
- **"w/o Composer ablation result (Comm=0.26) needs explanation"**: REMOVED. The result is coherent: without the Composer to structure assumptions and generate scenario trees, the system relies on the Planner's raw reasoning trace, which rarely selects communication. This is not a flaw; it is expected behavior that validates the Composer's role.
- **"Missing limitations section"**: REMOVED. This is a presentation preference, not a substantive flaw in the research.
- **"Cost formulation is a methodological gap"**: DEMOTED to Minor (point 5 above). The zero-cost for manipulation actions is reasonable given that the cost function measures traversal distance and message length; the imprecision is in the hard constraint, not in the concept.

## Novel Insights

The reviews surface a revealing tension: PCE dramatically reduces communication (72–83% on C-WAH, and even more on TDW-MAT), yet its total token usage is often higher than the most token-efficient baseline (CoELA) in TDW-MAT. This means the efficiency benefit of reduced communication is partly offset by the internal computation of the three-module pipeline (Planner + Composer + Evaluator all calling an LLM each step). The paper acknowledges this ("higher per-step inference cost") but could more sharply characterize the net token trade-off, helping readers understand when PCE's approach is worth the extra computation. The scaling analysis (Figure 3) showing that model scaling alone yields only modest gains, while PCE + scaling yields consistent improvement, is the paper's strongest empirical contribution and deserves highlighting as evidence that structured uncertainty handling is distinct from and complementary to scaling.

## Suggestions

1. Report all main results with variance (at least 3–5 seeds) and add a brief statistical analysis showing that the observed improvements over baselines are significant.
2. Since the appendix already contains human-expert correlation studies for the Evaluator, briefly summarize their findings (1–2 sentences) in the main text to address concerns about the core mechanism's validity.
3. Qualify the token usage claim: state explicitly that PCE's total tokens are comparable to or lower than most baselines, but acknowledge CoELA as a more token-efficient alternative in TDW-MAT, and frame the contribution as better task performance at moderate additional computational cost.
4. Run the LLM scaling ablation (Figure 3) on TDW-MAT as well, since C-WAH's 10 episodes weaken the generality of the claim.

### Calibration Anchors

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| CoELA (EnXJfQqy0K) | 6.50 | 1 & 2 | Direct baseline; PCE outperforms it and has a stronger conceptual contribution; both share evaluation limitations |
| CaPo (KRv9NubipP) | 6.00 | 1 | Another direct baseline; PCE is more novel (CaPo was seen as incremental over CoELA) |
| HAZARD (n6mLhaBahJ) | 6.75 | 1 & 2 | Benchmark paper, different contribution type |
| COMBO (YXRyYkb1im) | 6.67 | 2 | Trained generative world models for multi-agent; different approach but similar evaluation scale concerns |
| ReAd (y5tkxH7kxQ) | 5.00 | 2 | Rejected; PCE is clearly stronger in novelty and generalization |
| Gen. World Explorer (8NlUL0Cv1L) | 6.25 | 2 | Related area but different problem focus |
| Agent-Oriented Planning (EqcLAU6gyU) | 5.60 | 2 | Non-embodied task decomposition; PCE is more grounded |

**Round 1 bracket:** (5.5, 7.0) — paper is well above the 3.0–5.0 reject-level papers and below the 7.5+ benchmark/analysis papers.
**Final score determination:** PCE is closest to CoELA (6.50) in overall quality, with a stronger conceptual contribution but a minor token-claim overstatement that CoELA does not have. It is clearly above CaPo (6.00) in novelty. The evaluation weaknesses (no variance, small C-WAH) are shared with the baselines and appear to be community-normal limitations.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>