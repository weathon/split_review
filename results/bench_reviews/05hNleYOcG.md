Now I have all the information I need. Let me write the consolidated review.

---

## Summary

PLAGUE introduces a modular, three-phase framework (Planner → Primer → Finisher) for automated multi-turn LLM jailbreaking that incorporates lifelong learning via goal-embedding-based strategy memory retrieval. The framework achieves state-of-the-art attack success rates across five modern LLMs, including 81.4% SRE on OpenAI o3 and 67.3% on Claude Opus 4.1, with controlled turn budgets. A key contribution is the systematic decomposition of multi-turn attacks into composable phases, supported by thorough ablations showing additive gains from backtracking, reflection, planning, and memory retrieval.

## Strengths

- **Strong empirical results with large margins over baselines**: PLAGUE achieves SRE of 81.4% on OpenAI o3 (32.1% relative improvement over GOAT at 58.7%), 93.1% on o1, 97.8% on DeepSeek-R1, 95.8% on Llama 3.3 70B, and 67.3% on Claude Opus 4.1 (40.2% over Crescendo). These are substantial margins on a diverse set of contemporary models, evaluated on the full 200-sample HarmBench dataset.

- **Thorough and informative component ablations**: Table 3 adds backtracking, reflection, planning, and strategy retrieval incrementally atop GOAT, revealing clear additive contributions for each component. Notably, the ablation reveals model-specific vulnerability patterns — reflection provides the largest gain for o3, while backtracking is most critical for Claude Opus 4.1. This level of component analysis is rare in jailbreak papers and provides genuine insight.

- **Genuinely modular, plug-and-play framework**: The three-phase design is not just a conceptual framing — it is demonstrably composable. GOAT and Crescendo are substituted as Finisher modules with measurable effects (Tables 3, 4), and ActorBreaker's planner is plugged in to improve diversity by 15% (Figure 3) without meaningful ASR degradation. This practical modularity is a stronger contribution than a monolithic new attack.

- **Lifelong learning via goal-aware memory retrieval**: PLAGUE is the first multi-turn attack with a memory component (Table 1). The strategy retrieval mechanism (cosine similarity on goal embeddings, threshold 0.6, max 2 examples) provides measurable ASR gains (e.g., +4.1% SRE on o3, +3.4% on Claude Opus 4.1 in Table 3). The paper also provides qualitative examples of semantically related goal pairs.

- **Controlled efficiency analysis**: Table 5 demonstrates that PLAGUE's performance gains come with only modest overhead — 3–4 target LLM calls on average, comparable to Crescendo and within one call of GOAT, while requiring only a single planner-phase call versus ActorBreaker's four.

## Weaknesses

### Fatal

None. The core claims are supported by the evidence presented.

### Major

- **Sloppy reporting of the Claude Opus 4.1 headline result**: The abstract claims 67.3% SRE on Claude Opus 4.1. This number appears in Table 6 (Appendix C.4) as “PLAGUE (Best; equal budget)” with SRE 0.673, but the main results Table 2 reports only 0.465 (46.5%) with a footnote pointing to Table 4, which itself reports 0.601 (60.1%). The body text at line 646 states "Table 4 shows that our attack outperforms Crescendo, achieving an ASR of 67.3% on Opus 4.1, a 40.2% improvement" — but Table 4 shows 0.601, not 0.673. The data exists across the paper and is internally consistent once cross-referenced, but the presentation is confusing: readers cannot determine from the main text which configuration produced the abstract's headline number. This is a presentation error that undermines clarity, not the validity of the result, but it must be fixed.

### Minor

- **Unequal ASR@K protocol across baselines**: PLAGUE uses ASR@2 (two independent attempts per goal, selecting the higher rubric-scored attempt). GOAT and Crescendo are run once each. ActorBreaker is fairly allocated K=2. While the performance gaps are large enough that the conclusions likely survive single-attempt evaluation (e.g., 0.814 vs. 0.587 on o3), this makes the precise relative improvements over GOAT and Crescendo somewhat overstated. The paper should either grant all methods the same K or report K=1 for PLAGUE as well.

- **Sequential learning confound in memory evaluation**: PLAGUE processes the 200 HarmBench goals sequentially, updating the strategy memory after each success. The paper does not control for goal ordering, randomize it, or include a memory-reset baseline. Since the retrieval ablation in Table 3 compares configurations processed in a fixed order, the ASR gain attributed to RSS may partially reflect easier goals encountered earlier seeding the memory for harder later goals. This does not invalidate the core claim (baselines have no memory at all, so the comparison direction is conservative), but it means the exact contribution of the retrieval mechanism is confounded with order effects.

### Trivial

- The abstract lists phases as "Primer, Planner and Finisher" (line 26), but the framework actually executes Planner → Primer → Finisher. This is a minor ordering error in the abstract's text.

- The Rubric Scorer model is specified only as "Qwen Models" (line 438) without the exact model identifier, while the Evaluator model is precisely specified (Qwen3-235B-A22B-fp8).

## Nice-to-Haves

- Validating the internal rubric scorer against the final StrongREJECT metric would confirm that the attack's internal optimization proxy aligns with the actual harmfulness evaluation. This is a reasonable request but not standard in the jailbreak literature, where most attacks lack any internal scoring.

- An analysis of how the strategy memory evolves over the 200-goal run (how many strategies are added, retrieval hit rate, category-wise benefits) would strengthen the lifelong-learning narrative.

- Ablating the rubric scoring thresholds (7/10 for Primer, 3/10 for Finisher) would characterize sensitivity to these hyperparameters.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh critic's claim that "the 67.3% figure appears solely in a supplementary comparison (Table 6) without specifying which PLAGUE configuration produced it"**: The configuration IS specified — it's labeled "PLAGUE (Best; equal budget)" in Table 6. The real problem is the sloppy cross-referencing (text cites Table 4 when the number is from Table 6), not that the configuration is unspecified.

- **Harsh critic's claim that "the claimed 40.2% improvement... is not reproducible from the numbers in Table 4"**: While the text incorrectly cites Table 4, the improvement is reproducible: 0.673 (Table 6) / 0.48 (base Crescendo) = 1.402 = 40.2% improvement. The data exists; the cross-reference is wrong, not the math.

- **Strength Finder's claim about "near-perfect ASR on categories like misinformation"**: This is supported by Figure 4 and is a valid strength, retained above.

- **Harsh critic's concern about the evaluator model (Qwen3-235B-A22B-fp8) being "very recent and large" and lacking justification**: The evaluator model choice is standard practice in jailbreak evaluation (using a strong model as judge). This is a scope-creep criticism.

- **Harsh critic's concern about LLM-as-a-judge classification accuracy for category-wise analysis**: This applies equally to all prior work using HarmBench with LLM judges. The paper follows community-standard practice.

- **Harsh critic's complaint about "no validation that the internal rubric correlates with StrongREJECT"**: Moved to Nice-to-Haves — this is a reasonable request but not standard practice, and the rubric-based internal scoring is a design choice, not a flaw.

- **Strength Finder's generic strength about "tools and insights to understand the importance of plan initialization, context optimization and lifelong learning"**: This is a restatement of the paper's own claims, not a verifiable strength. Dropped.

## Novel Insights

The component-wise ablation across two different victim models (Table 3, o3 vs. Claude Opus 4.1) reveals that different safety-trained models have fundamentally different vulnerability profiles: o3 is most susceptible to reflection-based feedback, while Claude Opus 4.1 is most susceptible to backtracking (removing failed turns from the target's history). This model-dependent decomposition of attack effectiveness is a genuinely informative finding that goes beyond the headline ASR numbers — it suggests that model-specific attack tailoring (enabled by the plug-and-play framework) is valuable, and that safety training may produce qualitatively different defense surfaces rather than simply "stronger" ones.

## Suggestions

- Fix the Claude Opus 4.1 result presentation: either make Table 4 (or a new unified table) the canonical source for the 67.3% number, or explicitly state in the main text which table and configuration yields the abstract's headline result. The current cross-referencing is confusing and detracts from otherwise strong results.

- Add a brief discussion of the ASR@2 protocol's implications for baseline comparisons, and ideally report K=1 results for PLAGUE alongside K=2 to clarify the contribution of repeated sampling.

- Randomize goal order across runs or include a note acknowledging the sequential ordering limitation in the memory evaluation.

## Score and Decision

**Anchor comparison:**

| Anchor | Avg Score | Decision | Comparison |
|--------|-----------|----------|------------|
| JCB (OkjB6PWJEA) | 3.00 | Reject | PLAGUE has far more comprehensive evaluation, stronger novelty (modular framework + lifelong learning vs. synonym substitution), and much better results. Substantially stronger. |
| CoaxChain (6yCZEruFu9) | 3.50 | Reject | PLAGUE is purely black-box (no surrogate model needed), evaluates on more and harder models, and has clearer methodology. Clearly stronger. |
| GRAF (f9BuANYtJf) | 4.40 | Reject | GRAF fabricates target model responses; PLAGUE interacts with real model outputs. PLAGUE's framework is more principled and its evaluation more trustworthy. |
| SEMA (6eSNG1VNkl) | 5.00 | Accept (Poster) | SEMA has limited frontier model evaluation; PLAGUE evaluates on o3, Opus 4.1, o1. PLAGUE's ablations are more informative and its modular design is more actionable. Stronger. |
| Morpheus (11z2ZV85eV) | 5.00 | Reject | Morpheus evaluated on only 50 behaviors; PLAGUE uses full 200-sample HarmBench. PLAGUE's three-phase decomposition is more clearly articulated. Stronger. |
| ADJ (ilnKzaQSCh) | 5.50 | Accept (Poster) | ADJ has theoretical novelty but severe computational overhead and a theory-practice gap. PLAGUE is more practical, more efficient, and has equally strong or better empirical results. Comparable overall, PLAGUE slightly stronger empirically. |

PLAGUE is clearly above the 3.0–4.4 range and surpasses the 5.0 papers (SEMA, Morpheus) in comprehensiveness of evaluation, strength of empirical results, and clarity of ablations. The presentation issues around the Claude Opus 4.1 number are real but fixable and do not undermine the core results. The paper makes a genuine contribution to multi-turn jailbreak methodology through its modular, lifelong-learning framework with strong supporting evidence.

**Originality**: Good. The three-phase decomposition with lifelong memory retrieval is genuinely novel for multi-turn attacks, and the plug-and-play composability is a practical advance over monolithic prior approaches.

**Importance**: High. Multi-turn jailbreaking is the realistic threat model and understanding what drives attack success is important for developing defenses.

**Claims supported**: Mostly well-supported. The empirical results are strong and ablations are thorough. The Claude Opus 4.1 presentation needs fixing.

**Soundness**: Good, with minor methodological caveats (ASR@2 protocol, sequential ordering).

**Clarity**: Generally clear, with one notable presentation problem (the Claude Opus 4.1 cross-referencing).

**Value to community**: High. The modular framework enables systematic exploration of attack components, and the model-specific vulnerability findings are actionable.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>