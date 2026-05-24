Now I have all the evidence I need. Let me produce the consolidated review.

## Summary

This paper studies the self-consuming training loop—where an LLM is repeatedly trained on data that includes its own previous outputs—using a 10.6M-parameter GPT-style transformer trained on a logic-expression dataset (where correctness can be verified unambiguously). Across four data cycle configurations (full synthetic, balanced, incremental, expanding), the authors find that correctness initially improves while diversity steadily declines, eventually collapsing to a single point. Fresh real data can slow but not stop this diversity collapse. The paper introduces a clean evaluation methodology based on formal logic expressions that sidesteps the proxy-metric problem of natural language evaluation.

## Strengths

- **Novel, unambiguous evaluation methodology using logic expressions.** The paper's core methodological contribution is a formal-language dataset where syntactic and semantic correctness can be verified analytically (via parse success and Boolean evaluation), avoiding reliance on proxy metrics like BLEU/ROUGE. This is a genuine and well-executed design choice that enables precise measurement of quality and diversity. (Sections 3.1–3.2, lines 106–125)

- **Systematic exploration of four data cycles and parameter variations.** The paper goes beyond a single self-consuming configuration, testing full synthetic, balanced, incremental, and expanding data cycles (Section 3.3, Figure 2), and further varies the proportion of generated vs. fresh data (λ parameter) for the incremental and expanding cycles (Figures 5–6). This provides a richer picture of how different dataset construction strategies affect the rate of diversity decline. (Sections 3.3, 4.2)

- **Clear empirical demonstration of a quality-diversity trade-off in the self-consuming loop.** The results show that correctness improves over generations (Figure 3) while diversity collapses (Figures 4–6), with quantitative measurements reported (e.g., 68% diversity decline for the incremental cycle, 30% for balanced, 22% for expanding). The finding that fresh data slows but does not stop the decline is illustrated across multiple λ values. (Lines 223–234)

## Weaknesses

### Fatal
None.

### Major

- **Title/abstract/scope consistently overclaim relative to the actual experiments.** The paper's title, abstract, introduction, and conclusions repeatedly refer to "Large Language Models" and "LLMs." However, the experiments are conducted on a 10.6M-parameter GPT-style transformer trained on a toy dataset of logic expressions—neither the scale nor the domain corresponds to anything practitioners would recognize as an LLM (e.g., GPT-3/4). The limitations section acknowledges this (line 270), but the mismatch is pervasive in the paper's framing: the abstract claims "the first study investigating the self-consuming training loop for LLMs," the introduction frames the societal urgency of LLM-generated content on the internet, and the conclusion speaks about "LLMs trained in a self-consuming training loop." If the paper were reframed as a study of self-consuming loops for *small transformers on a formal language*, the claims would be internally consistent, but the significance would be substantially reduced relative to the current headline. This is not a trivial rewording issue—the mismatch between claimed scope and experimental evidence is structural and would need to be resolved before the paper can be taken at face value.

- **No multiple runs or variance estimation.** The paper admits that "the main results of this work consist of only one run per experimental configuration" (line 272) and attempts to dismiss this concern ("we do not believe that this limitation is crucial"). For an empirical paper drawing conclusions about trends over generations and comparing rates of decline across conditions, a single run provides no way to assess whether the observed patterns are systematic or influenced by random variation in training or sampling. Even 2–3 seeds per configuration would provide basic variance estimates and substantially increase confidence. The authors' argument that "all experiments point toward the same direction" (line 272) does not substitute for statistical evidence. This is the single highest-impact improvement the paper needs.

### Minor

- **The claim that "all data cycles eventually reach zero diversity" is extrapolated.** Line 225 states: "ultimately, we expect all of them to eventually reach zero diversity if the self-consuming training loop is run for enough generations." Only the full synthetic cycle actually collapses to zero within the observed 50 generations. The balanced and expanding cycles decline slowly (30% and 22% respectively) and do not appear close to zero. While the trend is suggestive, presenting this as a conclusion rather than speculation overstates what the data shows. This should be softened to a hypothesis or qualified with the observed endpoint values.

- **No analysis of the mechanism driving diversity loss.** The paper documents *that* diversity declines but does not investigate *why*—e.g., whether the model converges to a narrow subset of the data manifold, whether sampling temperature or strategy matters, whether the correctness improvement is actually beneficial or a sign of mode collapse. A few ablations (e.g., testing different sampling strategies, analyzing the set of unique correct expressions over time) would have deepened the analysis considerably without changing the paper's direction.

- **The correctness improvements reported for the full synthetic cycle (100% True by generation 6) could reflect mode collapse rather than genuine learning.** The paper notes the quality improvement but does not analyze whether the model is learning diverse correct expressions or simply memorizing a narrow set of common patterns. This is directly relevant to the paper's own quality-diversity trade-off narrative.

### Trivial

- The paper uses "LLMs" throughout to refer to a 10.6M-parameter model. If the scope is adjusted, the terminology needs consistent updating.
- The quantitative presentation is uneven: diversity results are well-quantified (68%, 30%, 22%, etc.), but the correctness results (Figure 3) are described only qualitatively ("increases," "fastest increase," "nearly reaches this point"). Exact percentages at key generations would be helpful.
- Sampling temperature (0.8) is fixed without discussion of its effect on diversity results.

## Nice-to-Haves

- Running experiments with 2–3 seeds would address the most critical evidential weakness without requiring a full 5+ replication.
- Adding a small-scale natural-language experiment (e.g., a constrained vocabulary corpus) to test whether the same diversity trends hold would strengthen generalizability claims.
- Ablating the sampling temperature or testing nucleus/top-k sampling would clarify whether the diversity collapse is an artifact of the decoding strategy.
- Analyzing the *set* of unique correct expressions over time (not just their proportion) would directly connect the correctness and diversity results.

## Removed Points

- "Related work is mixed into Section 2, making it less prominent": This is a structural/organizational preference, not a substantive weakness. The related work is adequately covered.
- "No discussion of whether code/data will be released": Per guidelines, questioning release status of cited artifacts is not permitted. The paper does not promise code release, which is standard for this venue.
- "The model is small and the results may not transfer to large models": The paper's limitations section already acknowledges this (line 270). The critic's version of this point is retained and repackaged under the scope-overclaim weakness above, but the pure "results may not transfer" concern is addressed by the authors.
- "Could the paper test on a small natural-language corpus?": This is a nice-to-have, moved above. Not a weakness—the paper explicitly scopes itself to logic expressions as a design choice to avoid proxy-metric problems.
- "No hyperparameter sensitivity analysis (temperature, learning rate)": While these ablations would strengthen the paper, the fixed hyperparameters are clearly stated and reasonable. The critic's framing treats this as a missing requirement when it is more naturally a nice-to-have extension.

## Novel Insights

None beyond the paper's own contributions. The two reviewers' perspectives are largely complementary rather than generating new synthesis. The harsh critic's core observation—that the paper's scope claims are mismatched with its experimental instantiation—is not a novel insight from reviewing but a straightforward reading of the paper. The strength finder correctly identifies the logic-expression methodology as the paper's most distinctive contribution. The fact that these two perspectives converge (both acknowledge the controlled setting is the paper's strength and the scale mismatch is its weakness) confirms the paper's main tension rather than revealing something new.

## Suggestions

1. **Reframe the paper's scope accurately.** Change the title to something like "Self-Consuming Training Loops for Language Models: An Analysis on Logic Expressions" or "An Empirical Study of Self-Consuming Training Loops for Small Transformers." Consistently replace "LLM" with "language model" or "transformer" throughout, and adjust the abstract and introduction so that the claims match what is actually demonstrated. The societal-urgency framing about web-scale LLMs can be preserved as motivation in the introduction but must be clearly separated from what the experiments directly show.

2. **Run at least 3 seeds per experimental configuration.** This is the most impactful single improvement and directly addresses the weakest evidential link. Even a minimal replication would allow reporting mean trajectories with ranges, making the results far more credible.

3. **Add quantitative summaries for the correctness results.** Report the exact percentage of True expressions at key generations (e.g., generation 1, 5, 10, 25, 50) for each data cycle, rather than relying solely on qualitative descriptions.

4. **Soften the extrapolation claim.** Replace "we expect all of them to eventually reach zero diversity" (line 225) with a more measured statement: "the observed monotonic decline suggests that given sufficient generations, all data cycles may eventually reach zero diversity, but this outcome is only directly observed for the full synthetic cycle within 50 generations."

5. **Add a brief analysis of whether the correctness improvement corresponds to genuine learning or pattern memorization.** For example, report the number of *unique* correct expressions over generations alongside their proportion, to check whether the model is converging to a small set of repeated patterns.

## Score and Decision

The paper addresses an important and timely question with a clean experimental design and a genuinely novel evaluation methodology. The core empirical findings—correctness improves while diversity collapses, with fresh data slowing but not stopping the decline—are clearly demonstrated in the controlled setting. However, two issues prevent acceptance in current form: (1) the pervasive scope overclaim (title/abstract/framing refer to "LLMs" while experiments use a 10.6M-parameter small transformer on logic expressions), and (2) the complete absence of multiple runs or any form of variance estimation. Both are addressable, and the underlying contribution (the logic-expression methodology, the systematic data-cycle comparison) is solid. With the recommended revisions, the paper would provide a valuable empirical demonstration.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>