Now I'm ready to write the final review.

---

## Summary

This paper introduces LLEGO, a genetic programming (GP) method for decision tree induction that uses LLMs as semantically-aware variation operators. The key technical contributions are a fitness-guided crossover operator (conditioned on a target fitness to exploit promising regions) and a diversity-guided mutation operator (sampling low-likelihood offspring to explore under-visited areas), both realized through structured natural-language prompts. LLEGO is evaluated on 7 classification and 5 regression datasets against greedy (CART, C4.5), exact (GOSDT, DL8.5), and GP (GATree) baselines, showing competitive-to-superior average performance, particularly at depth 4.

## Strengths

1. **Novel integration of LLMs as guided variation operators for tree induction.** The central idea — using LLMs not as unguided generators but as crossover and mutation operators with explicit fitness and diversity signals — is genuinely novel. The fitness-guided crossover (Section 3.2) conditions offspring generation on a target fitness $f^*$ derived from parent fitness, while the diversity-guided mutation (Section 3.3) actively samples offspring with low likelihood under the parent distribution. This is a clear advance over prior work using LLMs as unguided variation operators (Meyerson et al., 2023; Fernando et al., 2024).

2. **Controllable exploration–exploitation trade-off through principled hyperparameters.** The paper provides a systematic analysis (Section 5.2, Figures 5–6) of how $\alpha$ (crossover target fitness) and $\tau$ (mutation diversity temperature) affect offspring quality and diversity. This demonstrates that LLEGO offers interpretable control, enabling practitioners to adjust the balance based on problem characteristics.

3. **Broad applicability to both classification and regression.** Unlike exact optimization methods (GOSDT, DL8.5) that are limited to classification, LLEGO is evaluated on both settings (Tables 1 and 2). This is a practical advantage that broadens the impact of the work.

4. **Systematic ablation study.** Figure 7 ablates the semantic prior, the two operators, and the higher arity ($\nu=4$ vs. $\nu=2$). The full LLEGO achieves the best search efficiency, with each component contributing positively. The paper is transparent about the results, even when they complicate the narrative.

## Weaknesses

### Fatal
None.

### Major

1. **The semantic priors contribution is weaker than the title and narrative suggest.** The ablation `LLEGO_no_prior` removes task context and semantic reasoning yet "performs very competitively" (Section 5.3). The paper acknowledges this in the limitations ("while LLEGO can operate effectively without semantic priors"), but this directly undercuts the headline contribution of "semantically-aware evolution" in the title and abstract. If the method works almost as well without semantic priors, it is unclear how much of the gain is attributable to the claimed conceptual innovation vs. the LLM's general few-shot pattern-matching ability. The paper would benefit from reframing the contribution around the guided operators rather than the semantic priors.

2. **Overclaiming of empirical results.** The paper states LLEGO "outperforms baselines comprehensively" (Section 5.1). Yet it also notes that at depth 3 "sparse optimal induction methods such as DL85 and GOSDT demonstrate increased competitiveness." The paper reports average ranks, which likely show LLEGO leading on average, but "comprehensively" implies a level of dominance the data do not support. The claim that the advantage "becomes more pronounced" at depth 4 is also not obviously consistent across all individual datasets. More precise language — e.g., "LLEGO achieves the best average rank" — would be more accurate.

### Minor

3. **No statistical significance testing.** Only 5 runs are reported per dataset. Many comparisons involve overlapping standard deviations, and no confidence intervals, t-tests, or rank-based tests are provided. The paper makes strong comparative claims ("consistently outperforms," "significantly more efficient") without any statistical support.

4. **The "fewer evaluations" claim lacks empirical support.** The paper asserts LLEGO "achieves this superior performance while requiring fewer evaluations" (Section 5.1) but never reports the actual number of evaluations for either LLEGO or GATree. Since both use $G=25$ and $N=25$, and LLEGO generates $N$ crossover + $N$ mutation offspring per generation (Section 3.4), the claim is not obviously justified. The efficiency comparison in Figure 4 uses generations on the x-axis (standard in GP), but the "fewer evaluations" claim needs explicit support.

5. **Limited GP baseline coverage.** Only one GP baseline (GATree) is compared. While GATree is a reasonable representative, the broader GP-for-decision-trees literature includes other methods. Including at least one additional GP-based tree induction method would strengthen the comparison.

6. **Single closed-source LLM.** The paper relies on GPT-3.5-turbo and does not test an open-source alternative (e.g., Llama 3), which limits reproducibility and leaves the method vulnerable to API changes.

### Trivial
None.

## Nice-to-Haves

- Report wall-clock time and number of evaluations alongside generations for the efficiency comparison, to contextualize the LLM inference overhead.
- Include a comparison with a small, randomly initialized transformer (no pretraining) to better isolate the effect of pre-trained semantic knowledge vs. general LLM architecture.
- Add statistical significance tests (paired t-tests or Wilcoxon signed-rank tests) for the main comparative claims.

## Removed Points

- **"Unfair time-based comparison invalidates efficiency claims"**: Removed. The paper's efficiency comparison (Figure 4) uses generations, which is the standard metric in GP literature for comparing search dynamics. The 10-minute wall-clock limit in the experimental setup is simply an overall cutoff, not the basis for the efficiency analysis. The paper also acknowledges computational cost as a limitation in Section 6. The reviewer misread generations-based comparison as a wall-clock comparison.
- **"Missing ensemble baselines (Random Forest, XGBoost)"**: Removed as scope creep. The paper is about single decision tree induction, not ensemble methods. Comparing against ensembles would answer a different research question about interpretable vs. black-box models.
- **Pure formatting, typo, and style nitpicks**: Removed per instructions (parser artifacts, not author errors).
- **"Cherry-picks favorable comparisons" with insufficient evidence**: Removed. The paper reports average ranks across all datasets and discusses cases where baselines are competitive. The criticism is not supported by the paper's actual reporting practices.

## Novel Insights

The most interesting finding is the tension between the paper's framing and its own ablation results. The paper claims that "semantic priors" from LLMs drive the improved search, but `LLEGO_no_prior` — which strips away semantic reasoning and only uses the LLM for few-shot in-context learning — is "very competitive." This suggests that the practical benefit of using LLMs in this GP pipeline may come less from their pre-trained domain knowledge about decision trees and more from their ability to perform structured few-shot generation conditioned on exemplars. If so, this is itself a valuable insight (and the paper deserves credit for running the ablation), but it reorients the claimed contribution: the value lies in using LLMs as flexible conditional generative models with tunable stochasticity (via $\alpha$ and $\tau$), rather than as repositories of semantic knowledge. The paper would be stronger if it leaned into this interpretation rather than framing the semantic prior as the core innovation.

## Suggestions

1. **Reframe the contribution** to reflect what the ablation shows. The operators (fitness-guided crossover, diversity-guided mutation) are genuinely novel and well-designed; the semantic prior narrative is secondary and should be presented as such. Consider a more precise title such as "LLM-Guided Genetic Programming for Decision Tree Induction."
2. **Add statistical testing** (even simple paired t-tests) for the main comparisons in Tables 1 and 2.
3. **Report wall-clock time and evaluation counts** so readers can assess practical trade-offs.
4. **Tone down overclaims** — replace "outperforms baselines comprehensively" with more precise language about average ranks and discuss specific datasets where baselines are competitive.
5. **Include an open-source LLM baseline** (e.g., Llama 3) to address reproducibility and isolate API-specific effects.

## Score and Decision

**Originality**: High — LLM-guided variation operators with explicit fitness/diversity control for tree induction is genuinely novel.  
**Importance of question**: Moderate — decision tree induction is well-studied; the practical relevance depends on cost-benefit trade-offs not fully characterized.  
**Claims support**: Moderate — claims of superiority are somewhat overbroad; no statistical testing; ablation tensions weaken the semantic-prior narrative.  
**Soundness of experiments**: Moderate — methodology is sound, baselines are reasonable, but missing evaluation counts and wall-clock data.  
**Clarity of writing**: Good — operators are clearly described; the paper's narrative is coherent despite the framing-ablation tension.  
**Value to community**: Moderate — the idea is promising and could inspire further work on LLM-guided combinatorial optimization, but needs stronger evidence and more honest framing.

The paper makes a novel contribution — the guided LLM-based operators are well-conceived and the results are generally positive. However, the paper overstates its claims (both about comprehensive empirical dominance and about the centrality of semantic priors), and the experimental evaluation lacks statistical rigor and some important supporting data. These issues are addressable with revisions. I recommend **weak accept** conditional on the authors addressing the overclaiming, the framing-revision around semantic priors, and adding at minimum statistical testing and evaluation counts.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>