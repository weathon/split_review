## Summary
EconAgentBench introduces three multi-turn benchmark environments for LLM agents in economic settings—procurement (constrained integer optimization with unknown effectiveness scores), scheduling (stable matching with unknown preferences), and pricing (non-stationary demand with unknown parameters). The paper evaluates seven frontier LLMs using synthetic, difficulty-scalable environments and demonstrates that behavioral metrics beyond aggregate scores can surface economically meaningful insights about agent behavior.

---

## Strengths

- **Genuine exploration requirement is well-designed**: The hidden-parameter setup is principled. Procurement withholds effectiveness scores $e_1,\ldots,e_n$ (Section 3.3.1), scheduling withholds all worker/task preferences (Section 3.3.2), and pricing withholds all demand parameters including how $\alpha_i$ evolves (Section 3.3.3). No agent can trivially solve any task on period 1, making multi-turn reasoning under uncertainty a genuine prerequisite.

- **Difficulty scaling is empirically validated**: For all tested LLM agents and all three environments, HARD scores are significantly lower than BASIC scores ($p < 0.05$, one-sided Welch's $t$-test; Section 4.1, Table 2). The mechanism is transparent and scalable beyond the three instantiated levels.

- **Substantively novel finding regarding reasoning vs. non-reasoning models**: GPT-5 and Gemini 2.5 Pro lead on stationary tasks (procurement and scheduling), but GPT-4.1 achieves the highest pricing score (66.8 vs. GPT-5's 58.9, Table 2). This reversal—reasoning models underperforming on the non-stationary task—is an empirically grounded and non-obvious observation that speaks to a genuine capability dimension.

- **Behavioral metrics exhibit interpretable alignment with scores**: Budget utilization (Table 3) is highest for GPT-5 (97.0%) and o4-mini (95.9%), the two top-performing procurement agents, and the correspondence between best-so-far rate and scheduling score is monotone across the top three models (Table 3). These metrics add diagnostic signal beyond aggregate scores.

- **Lightweight, future-proof tool-use protocol**: Any LLM supporting function calling can participate, requiring only the tools listed in Table 1. This design avoids proprietary interfaces and keeps the benchmark forward-compatible.

---

## Weaknesses

### Fatal
None.

### Major

- **Absence of algorithmic baselines**: The paper evaluates LLMs only against each other, leaving absolute performance levels unanchored. For procurement, the task is a constrained nonlinear integer program for which greedy or bandit methods are natural comparisons. For scheduling, footnote 8 of the paper itself notes that a stable matching can be computed in polynomial time from even a single adversarially chosen blocking pair (citing Bei et al., 2013; Emamjomeh-Zadeh et al., 2020), making the absence of a Gale-Shapley-style adapted algorithm especially notable. For pricing, the dynamic pricing literature offers straightforward gradient-based or contextual bandit baselines. Without these reference points, GPT-5's procurement score of 75.0 cannot be interpreted as impressive, adequate, or poor. The paper claims the benchmarks yield "economically meaningful insights" (Contribution 3), but this claim is weakened when there is no reference to the economic problem's intrinsic difficulty.

- **No uncertainty estimates for inter-model comparisons**: The only reported significance test is for difficulty scaling (BASIC vs. HARD, pooled across models). For the inter-model comparisons that form the paper's empirical narrative in Sections 4.2 and 4.3, no confidence intervals or standard errors are provided. With 12 instances per difficulty level at temperature 1, the variance of estimates for individual models could be substantial. For example, procurement HARD shows o4-mini at 60.9, Claude 3.5 Sonnet at 54.6, and GPT-4.1 at 33.6—but without error bars, it is unclear which of these gaps are statistically meaningful. The wide spread of scheduling HARD scores (from 3.2 for GPT-4o to 90.5 for GPT-5) suggests high instance-level variance.

### Minor

- **Adaptability metric is confounded with initial performance quality**: The paper defines adaptability as the difference between the score in the last 50 periods and the average score in the first 10 periods. The paper itself acknowledges (Section 4.3) that Gemini 1.5 Pro's high adaptability (7.4%, Table 3) "is driven by poor-quality actions in the first 10 periods" rather than genuine adaptation. A model that starts poorly and improves to mediocre scores identically to a model that starts mediocre and improves to good scores, which conflates recovery from bad initialization with genuine adaptive capability.

- **Scheduling normalization denominator underspecified in main text**: The success metric uses $\mathbb{E}_{\text{uniform random matching}}[\# \text{blocking pairs}]$ as denominator (Section 3.3.2, equation for success metric), but the main text does not state whether this expectation is computed analytically or via Monte Carlo simulation. Since negative scores are possible and meaningful, this affects interpretability of results for weak models. (This may be specified in the stripped appendix, but is absent from the main text.)

- **Linear vs. periodic non-stationarity patterns analyzed in aggregate**: Two distinct pricing dynamics (linear shifts and periodic shifts in $\alpha_i$, Section 3.3.3) are described, but Table 2 reports a single pooled pricing score. If they produce qualitatively different difficulty profiles or elicit different agent strategies, this distinction is invisible in the results.

### Trivial
None.

---

## Nice-to-Haves

- The observation that reasoning models underperform non-reasoning models on non-stationary pricing (Section 4.2) deserves deeper analysis. The paper notes this "perhaps surprisingly" in two sentences without investigating why. A characterization of the pricing strategies models actually deploy—e.g., by categorizing logged notes and actions—would make this finding mechanistic rather than anecdotal and substantially strengthen Section 4.3.

- The discussion in Section 5 gestures at deployment thresholds ("over 90% or 95% EconAgentBench scores") but does not ground these in the actual distribution of current model scores. A rough gap analysis (e.g., no model exceeds 76% in procurement or 70% in pricing) would sharpen the practical framing.

- Adding one lightweight algorithmic baseline per task (e.g., a greedy heuristic for procurement, a Gale-Shapley-adapted algorithm for scheduling) would be the single highest-leverage addition to the paper.

---

## Removed Points
*These points are flagged to be removed — treat them with caution.*

- **"Best-so-far rate is not causal, only a proxy for model quality"** (Harsh Critic, Section 4.3): Removed as a standalone weakness. The paper presents the metric as descriptive and diagnostic, not as a causal mechanism. That high-quality models may score better throughout—including on first submissions—does not invalidate the metric's use as a behavioral correlate of performance. The paper does not overclaim causality.

- **"BASIC pricing is qualitatively different from MEDIUM/HARD due to $n=1$ simplifying the nested logit"** (Harsh Critic, Section 3.3.3): Removed. The nested logit at $n=1$ is well-defined; whether it simplifies structurally depends on parameter values and is speculative without performing the calculation. Not a verifiable paper error.

- **"Pricing results (linear vs. periodic) should be collapsed if they do not differ"** (Harsh Critic): Partially removed. Kept as a nice-to-have (separate analysis would strengthen the paper) but the current aggregate presentation is not a methodological error.

- **Generic strength: "this paper addresses an important problem"** (Strength Finder summary): Removed as generic. Replaced by specific strength evidence from the paper.

- **"Reasoning under uncertainty tests general capability, not just economic capability"** implied as a strength: Removed as vague and not substantiated by comparative evidence.

---

## Novel Insights
The most genuinely novel finding in the paper is the reversal in model rankings between stationary and non-stationary environments: reasoning models (GPT-5, Gemini 2.5 Pro) dominate on procurement and scheduling, but the non-reasoning GPT-4.1 leads on non-stationary pricing. This suggests that the exploration-exploitation structure of non-stationary optimization penalizes the structured, deliberate search strategies of reasoning models, which may over-plan in domains that require fast, heuristic adaptation. This is not only a diagnostic result for the specific models tested but raises a broader question about when reasoning-model computation is productive vs. counterproductive in partially observable economic environments.

---

## Suggestions
1. Add at least one lightweight algorithmic baseline per task—a greedy budget-saturating heuristic for procurement and a Gale-Shapley-adapted algorithm with blocking-pair feedback for scheduling—and report how far LLMs fall below these in absolute terms.
2. Report 95% confidence intervals over the 12 runs for all scores in Table 2, even simple bootstrap intervals, to allow readers to assess which inter-model comparisons are statistically robust.
3. Replace or supplement the adaptability metric with one that controls for initial performance quality—e.g., normalized improvement relative to starting score—to distinguish genuine adaptation from recovery from bad initialization.
4. Analyze linear-shift and periodic-shift pricing instances separately in Table 2 (or an additional table), since the two patterns test different aspects of non-stationary adaptation.
5. Expand Section 4.2's pricing discussion to include at least a qualitative categorization of the pricing strategies adopted by GPT-4.1 vs. reasoning models, grounding the "simple heuristics" observation in actual agent behavior.

---

**Originality:** The benchmark combines economic theory (nested logit, stable matching, constrained optimization) with LLM agent evaluation in a principled way; the task designs are not recycled from prior benchmarks. However, as a benchmark paper, the originality ceiling is inherently limited.

**Importance:** Economically-grounded, multi-turn agent benchmarks are genuinely underrepresented in the literature, and the authors identify a real gap. The practical framing (AI adoption decisions) is plausible.

**Claims supported:** The difficulty scaling claim is well-supported. The "economically meaningful insights" claim is partially supported (budget utilization and best-so-far rate are informative), but the adaptability claim is self-undermined. Absolute performance claims are unanchored without algorithmic baselines.

**Soundness:** Experimental design is principled but statistically underpowered for inter-model comparisons. The economic models (nested logit, stable matching) are drawn from rigorous literature.

**Clarity:** Writing is clear; mathematical formulations are precise and correct as presented.

**Community value:** Fills a genuine gap in LLM evaluation for multi-turn economic reasoning. Publicly released code and synthetic generation make it immediately usable and extensible.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>