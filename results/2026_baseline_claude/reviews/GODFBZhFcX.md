## Summary
PCE (Planner-Composer-Evaluator) is a modular framework for embodied multi-agent planning under partial observability. It observes that LLM reasoning traces already contain implicit assumptions about the environment, but these are used locally and inconsistently. PCE extracts these assumptions, structures them into a decision tree (internal nodes = Boolean environment assumptions, leaves = actions), and evaluates each root-to-leaf path by a weighted combination of scenario likelihood, conditional gain, and execution cost. Experiments on C-WAH and TDW-MAT across three LLM backbones consistently show PCE outperforming four communication-centric baselines in task success and efficiency, with a user study further validating that selective communication is perceived as more trustworthy.

---

## Strengths

- **Well-motivated core observation.** The empirical insight that LLM CoT traces encode assumptions "locally and implicitly, without being globally aggregated" is concrete and directly motivates the Composer–Evaluator design. The worked example in Figure 2 makes the gap vivid and is convincing.
- **Comprehensive LLM backbone sweep.** Testing on GPT-4o mini (commercial, small), GPT-OSS:20B (open-source reasoning model), and Gemma3:4B (open-source small) across both benchmarks substantially strengthens generalizability claims. PCE is the best or tied-best across all nine benchmark–backbone combinations for the primary metric.
- **Informative scaling ablation.** Figure 3 directly addresses whether PCE's gains could be "explained away" by simply using a bigger or deeper model. The consistent gap between PCE and Planner-only at every capacity/depth level is the paper's most scientifically valuable empirical result.
- **Component ablation is principled.** Table 3 isolates each of the three modules and shows that removing any one hurts performance. The *w/o Planner* variant in particular shows a large regression (42.76→56.46 steps), quantifying the importance of having a strong initial reasoning seed before tree construction.
- **User study adds a real-world perspective.** The 7-point Likert evaluation across Appropriateness, Usefulness, Efficiency, and Trust is a meaningful addition that few algorithmic papers include. The finding that *Com always* is penalized for disruption while *w/o Com* is penalized for opacity directly supports the selective-communication design philosophy.

---

## Weaknesses

### Fatal
None.

### Major

1. **Token usage claim is overstated for TDW-MAT.** The abstract and conclusion state "comparable token usage," but in TDW-MAT with GPT-4o mini, PCE consumes 197,807 tokens versus CoELA's 113,059—a ~75% increase. With GPT-OSS:20B, PCE uses 337,225 versus CoELA's 237,499. The "comparable" framing holds mainly for C-WAH, where reduced episode length compensates for higher per-step cost. The claim needs to be qualified or the tradeoff discussed honestly: PCE trades more total inference tokens for better task success in TDW-MAT.

2. **Statistical robustness is unverifiable with current episode counts.** C-WAH uses only 10 episodes. With such small samples, performance differences like PCE vs. REVECA (42.76 vs. 46.80 steps in C-WAH/GPT-4o mini) cannot be distinguished from random variation without confidence intervals or significance tests. TDW-MAT has 24 episodes, which is better but still marginal. The lack of variance reporting (standard deviation, bootstrap confidence intervals, or p-values) prevents confident interpretation of whether the observed orderings are stable.

3. **LLM-estimated likelihood and gain scores are unvalidated in the main paper.** The Evaluator's utility function relies entirely on LLM-estimated L and G scores. When these estimates are wrong, PCE could select the same (or worse) action than naive planning. The paper references human-expert correlation studies in Appendix A.10–11 but presents no characterization of estimation error in the main text—not even a qualitative failure-case analysis. Because the validity of the entire decision-tree scoring rests on these estimates, this is an important gap for the main body.

### Minor

1. **Hyperparameter sensitivity relegated to appendix without summary.** The cost function has three free parameters (α, β, λ), all set to 1. The main text does not report even a high-level sensitivity summary, making it hard to assess how robust the results are to this choice. If performance is sensitive to λ in particular, the comparison to baselines (which have no such parameter) is partially confounded.

2. **DEC-POMDP formulation vs. actual method.** Section 3 formally frames the problem as a DEC-POMDP, but the Composer explicitly disclaims solving it ("rather than computing true probabilities, which would amount to solving an intractable POMDP, we approximate these criteria using LLMs"). This is a reasonable engineering choice, but the formal framing creates an expectation of a principled approximation guarantee that is never provided. The section could be shortened or reframed as motivation rather than formal grounding.

3. **User study sample size.** 12 participants is small for a Likert-scale study; the paper should acknowledge this limitation explicitly.

4. **Communication counts for PCE are conspicuously low.** PCE generates 1.70 communication actions on average in C-WAH/GPT-4o mini versus 9.88 for CoELA. The paper frames lower Comm as efficient, but never examines whether there are systematic scenarios where PCE communicates too little and misses useful information. A precision/recall analysis of communication decisions would strengthen this aspect.

### Trivial
- The Figure 4 caption incorrectly lists "PCE (blue)" twice instead of once per condition.

---

## Nice-to-Haves

- Reporting mean ± std (or 95% CI) for all main table entries would immediately address the statistical robustness concern without requiring additional experiments.
- A token-budget-controlled comparison (fix total tokens, vary allocation) would sharpen the efficiency story in TDW-MAT where PCE uses significantly more tokens.
- A brief quantitative summary of Appendix A.10–11 (e.g., Spearman correlation between LLM-estimated scores and ground-truth) would make the reliability claim self-contained in the main paper.
- A failure-mode analysis (e.g., when does the Evaluator's ranking mismatch the optimal choice?) would complement the qualitative case studies and provide insight for future work.

---

## Novel Insights

The paper's most genuinely novel insight is the structural diagnosis of *why* scaling LLMs fails to resolve planning uncertainty in partially observable settings: it is not a capacity problem but an aggregation problem. Larger models still produce fragmented, locally-grounded assumptions; what is missing is an explicit mechanism to reconcile those assumptions globally before committing to an action. The scaling ablation (Figure 3) empirically demonstrates that PCE's structured uncertainty handling and raw model capacity are orthogonal dimensions of improvement, with their combination being additive rather than redundant. This suggests that future work on embodied planning should treat "explicit assumption management" as a first-class design axis, separate from model scale or chain-of-thought depth.

---

## Suggestions

- Add confidence intervals or standard deviations to all table entries; with 10 episodes in C-WAH this is critical for credibility.
- Revise the abstract/conclusion's "comparable token usage" framing to acknowledge the TDW-MAT tradeoff explicitly (e.g., "comparable or moderately higher token usage in exchange for substantial performance gains").
- Include a 2–3 sentence summary of Appendix A.10–11 findings (LLM score reliability) in the main paper's ablation section.
- Report at least one sensitivity result for λ in the main text (e.g., λ ∈ {0.5, 1, 2}) to give readers a sense of robustness.
- Consider adding a discussion of failure modes: specific scenarios where the Evaluator's ranking is incorrect and how often they occur.

---

## Score and Decision

PCE addresses a well-identified gap, presents a coherent and implementable solution, and supports its claims with multi-benchmark, multi-backbone experiments and an ablation study that goes beyond most contemporaries. The scaling ablation is particularly compelling. The primary concerns—statistical robustness with small episode counts, overstated token efficiency claims in TDW-MAT, and absence of LLM-score reliability characterization in the main body—are significant but fixable without new experiments. None constitute a fatal flaw.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>