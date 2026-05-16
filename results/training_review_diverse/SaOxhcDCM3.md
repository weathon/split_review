Now I have a thorough understanding of the paper and all reviewer claims. Let me produce the final consolidated review.

---

## Summary

This paper presents an empirical study of self-consuming training loops for LLMs trained from scratch. The authors introduce a logic-expression dataset that enables unambiguous evaluation of correctness and diversity, and systematically investigate four data cycles (full synthetic, balanced, incremental, expanding) over 50 generations with varying proportions of generated vs. fresh data. The central finding is that self-consuming training improves output correctness but degrades diversity, with fresh data only slowing—not stopping—the decline.

## Strengths

1. **First systematic study of self-consuming training loops for LLMs trained from scratch.** Prior work (Shumailov et al., 2023; Guo et al., 2023) studied iterative *fine-tuning* of LLMs, but the paper correctly distinguishes this from the *from-scratch* setting (lines 85–87), which is how new-generation LLMs like GPT-4 are actually trained. The paper fills this gap.

2. **Novel logic-expression verification method enabling unambiguous quality and diversity measurement.** By using Boolean expressions that can be syntactically and semantically evaluated (True/False/error), the paper avoids proxy-based metrics (BLEU, ROUGE) that are inherently ambiguous for evaluating generative quality. The method is clearly described in Section 3.1–3.2 and enables the quantitative bar plots in Figure 3 and diversity curves in Figures 4–6.

3. **Systematic quantitative analysis across multiple data cycles and fresh-data proportions.** The paper goes beyond a single condition: it compares four distinct data cycles (full synthetic, balanced, incremental, expanding) and varies λ (the proportion of generated data) within the incremental and expanding cycles. This provides a richer picture than prior work. Key quantitative results include: with 25% fresh data diversity drops only ≈11% over 50 generations, versus ≈36% with 0% fresh data (Section 4.2).

4. **Transparent limitation discussion.** The paper acknowledges single-run experiments, limited model size, the artificial nature of the logic-expression dataset, and the from-scratch vs. fine-tuning distinction in Section 6. This candor strengthens the credibility of the reported trends.

## Weaknesses

### Fatal

None.

### Major

1. **Single run per experimental configuration, limiting the reliability of quantitative claims.** The paper acknowledges this (lines 272–273): "the main results of this work consist of only one run per experimental configuration." While the qualitative direction of the diversity decline is consistent across four data cycles and multiple λ values—making it unlikely to be a stochastic artifact—the specific numerical claims (e.g., "decreases by approximately 36%," "68% decrease in diversity," the precise generation at which collapse occurs) lack error bars and cannot be taken as precise or replicable. The paper uses the word "inevitably" (line 24), which is too strong for a phenomenon demonstrated on a single seed per configuration. Multiple runs (even for a subset of conditions) would substantially strengthen the evidence.

2. **Overclaimed scope: the experiments do not study "Large Language Models" in any practical sense.** The paper's title and introductory framing refer to "Large Language Models" throughout, yet the experiments use a 10.6M-parameter GPT-style model trained on 10k logic-expression strings with a 7-token vocabulary. The gap between this setup and a true LLM (e.g., GPT-4 with >100B parameters, natural language with >50k vocabulary, complex syntactic/semantic structure) is enormous and unbridged. The limitations section (lines 277–278) acknowledges that "real text has a way larger vocabulary and more complex structures" but dismisses this as a secondary concern. The paper would be more scientifically precise if it positioned itself as studying self-consuming loops in *small transformer language models on a symbolic language*, with cautious speculation about implications for LLMs. As written, the scope claim misrepresents what was actually demonstrated.

### Minor

3. **The claim to be "the first study" of self-consuming training loops for LLMs requires sharper qualification.** The abstract and introduction state this as "the first study investigating the self-consuming training loop for LLMs" (line 4). The paper correctly notes (lines 85–87) that prior work studied *fine-tuning* rather than *from-scratch* training, but the initial framing could mislead readers who do not read the related work section carefully. A more precise early qualifier ("the first study of the self-consuming training loop for LLMs *trained from scratch*") would avoid this.

4. **The Levenshtein diversity metric, while reasonable, conflates token-level variation with semantic diversity.** The metric is calculated on token sequences (line 125) and may overestimate diversity when token edits do not change the underlying Boolean structure (e.g., `True or False` vs. `True or True` differ by one token but both evaluate to True with different semantics). A complementary metric such as the number of distinct expression trees or unique evaluation-True outputs would strengthen the diversity analysis. The paper does not discuss this limitation of the metric.

5. **The relationship between improving correctness and declining diversity is presented as two separate results rather than analyzed as two sides of a single process.** The training data consists entirely of True expressions (line 180). As the model converges to generating only True expressions, the space of possible valid outputs shrinks, naturally reducing diversity. The paper currently presents correctness improvement and diversity decline as separate findings (Sections 4.1 and 4.2) without discussing how the former mechanistically drives the latter. An explicit tie between these measures would deepen the analysis.

### Trivial

None substantively impactful beyond what is captured above.

## Nice-to-Haves

- A non-self-consuming control (training multiple independent models on D0 without iteration) would isolate the effect of the loop from the effect of repeated training, though generation 1 already serves as a partial baseline.
- Analyzing hidden representations (attention patterns, hidden-state variance) could provide mechanistic insight into collapse.
- Releasing code would support reproducibility (not flagged as missing by the paper; the paper does not make an availability statement).

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"No comparison with a baseline that does not use self-consuming training"** — Removed because generation 1 *is* trained only on real data D0 and serves as the baseline. The paper inherently compares all subsequent generations against this first generation.
- **"The sentence about paying for human-generated content is a non-sequitur"** — Removed because the sentence (line 16) connects logically: if even paid workers use LLMs, fresh human data may become unreliable, motivating the concern about self-consuming loops.
- **"The first study claim is imprecise because Shumailov et al. studied LLMs"** — Removed/weakened to Minor #3 because the paper carefully distinguishes from-scratch from fine-tuning (lines 85–87). The claim is properly qualified in the paper itself.
- **Exaggerated severity of single-run issue in the harsh critic (calling it "structural" and that quantitative results "should not be taken at face value")** — Kept as a Major weakness but downgraded from Fatal because the trend is replicated across 4 data cycles and multiple λ values, providing internal consistency beyond a single run.
- **Strength Finder strengths that are generic** — No generic strengths were present; all three core strengths were specific and evidence-backed.

## Novel Insights

None beyond the paper's own contributions. The cross-configuration consistency is the most compelling aspect: across four different data cycles and multiple fresh-data proportions, diversity declines monotonically in every condition, providing convergent evidence that the effect is robust even within the single-run constraint.

## Suggestions

1. **Add multiple random seeds (at least 3–5) for a core subset of conditions** — e.g., the full synthetic cycle, incremental (λ=0.25), and expanding (λ=0.9 and λ=0.75). Plot diversity curves with error bands. This is the single highest-leverage improvement.

2. **Adjust the title and scope claims** to reflect what was actually studied: a small transformer model on a symbolic language, not "Large Language Models." For example: "Transformer Language Models Suffer From Their Own Output: An Analysis of Self-Consuming Training on a Symbolic Language." This would make the paper more scientifically precise without diminishing its contribution.

3. **Add a complementary diversity metric** such as the number of distinct expression trees or unique semantically correct outputs per generation, to validate that the Levenshtein-based diversity decline reflects genuine semantic collapse rather than token-level surface variation.

4. **Explicitly connect correctness and diversity** by showing that as the proportion of True expressions increases, the number of distinct expression structures decreases, making the trade-off transparent.

## Score and Decision

The paper addresses an important and timely question with a clever experimental design. However, the single-run limitation and the significant gap between the claimed scope ("Large Language Models") and the actual experiment (10.6M-parameter model on logic-expression strings) weaken the contribution. The core qualitative finding is plausible and consistent across configurations, but the paper does not yet provide the quantitative rigor its strongest claims demand. With multiple runs and more careful scope framing, this could be a solid empirical contribution.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>