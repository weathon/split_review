Now I have my calibration. Let me write the final review.

Round 1 bracket: I placed this paper between 5.5 and 7.5 based on comparing it against weak anchors (1.4–3.0 from papers like NEMESIS, BlackDAN, Quack), middle anchors (3.5–7.5 from MHJ at 5.75, ActorAttack at 5.33, PAIR at 4.75), and strong anchors (7.5+ from curiosity-driven red-teaming at 8.0, safety alignment papers at 9.5).

Round 2 narrowing: Compared against Simple Adaptive Attacks (6.14), FlipAttack (5.75), ArrAttack (7.00), and Jailbreak via GCG improvements (6.25), the paper sits at the upper end of this range but below ArrAttack's 7.0 due to missing statistical rigor.

## Summary

PLAGUE proposes a plug-and-play three-phase framework (Planner → Primer → Finisher) for automated multi-turn jailbreak generation, augmented with a lifelong learning memory bank that retrieves and reuses successful attack strategies. The framework achieves state-of-the-art StrongREJECT ASR of 81.4% on OpenAI o3 and 67.3% on Claude Opus 4.1, improving over prior best baselines by >30%, while maintaining comparable or lower total LLM call budgets. The framework is modular, allowing existing attacks (GOAT, Crescendo, ActorBreaker) to be plugged in as Planner or Finisher modules.

## Strengths

- **State-of-the-art results on the hardest models**: PLAGUE achieves 81.4% SRE on OpenAI o3 and 67.3% on Claude Opus 4.1 (Tables 2, 4), models widely considered highly resistant to jailbreaking. The improvements are large (32–40% relative gains over previous best) and systematic across all five models tested.

- **Well-designed ablation that isolates individual component contributions**: Table 3 adds backtracking, reflection, planner, and strategy retrieval one-at-a-time to a GOAT baseline, showing clear monotonic ASR improvements (e.g., o3: 0.587 → 0.612 → 0.761 → 0.773 → 0.814). This enables principled attribution of gains and reveals model-specific sensitivities (reflection critical for o3, backtracking for Claude Opus 4.1).

- **Modular plug-and-play design validated by experiment**: The claim that existing attacks can serve as interchangeable components is directly tested — swapping Crescendo for GOAT as the Finisher on Claude Opus 4.1 raises ASR from 0.465 to 0.673 (Table 4), demonstrating the framework's composability rather than just asserting it.

- **Efficiency analysis with concrete call budgets**: Table 5 breaks down Target, Evaluator, and Planner LLM calls per model, showing PLAGUE matches or beats Crescendo's total call budget while achieving substantially higher ASR (e.g., o1: 5.61 vs. 5.88 total calls, 93.1% vs. 69.2% ASR). This addresses the practical concern that multi-turn attacks are expensive.

- **Novel lifelong learning mechanism with clear evidence**: The memory bank retrieval (RSS) improves ASR by 4–5 points on o3 and Claude when added last (Table 3), and the design choice of goal-embedding cosine similarity (threshold 0.6, max 2 examples) is clearly motivated and described.

## Weaknesses

### Fatal
None.

### Major

1. **No measures of variance or statistical significance reported**: The paper states "scores are averaged over three runs for robustness" but does not report standard deviations, error bars, confidence intervals, or any statistical test for any result in Tables 2–5 or Figure 2. Given that (a) multi-turn attacks have high path variance, (b) the paper itself notes "increased variance observed due to a multitude of possible paths in multi-turn conversations" (Section 4), and (c) all comparisons are against baselines, the absence of any uncertainty quantification weakens the strength of every comparative claim. A difference of a few percentage points could easily fall within run-to-run noise.

2. **No evaluation against any defense mechanism**: The paper evaluates PLAGUE's attack success on undefended models but does not test against any known defense (e.g., SmoothLLM, Self-Reminder, safety prefixes, perplexity filtering, or input paraphrasing). Since the paper claims to "advance the frontiers of building robust LLM systems," showing at least some basic defense evasion would substantiate this framing. Without it, the reader cannot assess whether PLAGUE's gains are robust or easily nullified by standard defenses.

### Minor

1. **ASR@2 metric inflates scores relative to standard reporting conventions**: The paper uses ASR@2, selecting the best of two attempts per goal, and states "We use SRE and ASR interchangeably." This is non-standard — most prior work reports ASR without a Pass@K-style selection over multiple runs. While the paper attempts to apply the same convention to baselines (e.g., K=2 for ActorBreaker), this is not consistently possible (e.g., Crescendo and GOAT results likely come from their standard configurations). This makes direct comparison with prior reported numbers in Table 2 imprecise.

2. **Diversity claims are not substantiated in the visible text**: The paper claims PLAGUE's planning module "largely drives improvements in diversity" and references Figure 3 for a 15% diversity improvement when using ActorBreaker's module. However, no diversity metric is formally defined, and the diversity analysis figure (Figure 3) and the diversity evaluation against X-Teaming/FITD (Table 6) are both in the appendix that was stripped. Without seeing these, the diversity contribution is asserted but not verifiable from the main text.

3. **The bridge between SRE and Bin-ASR scores could be clearer**: The paper reports both SRE (graded, 0–1) and Bin-ASR (binary) and says "We use SRE and ASR interchangeably in our work" — but then the text predominantly quotes SRE values (e.g., "81.4% ASR on o3"), which is a graded score, not a traditional binary attack success rate. A reader comparing against prior binary-only work may overestimate the improvement. The paper should consistently label which metric is being quoted.

### Trivial
- The sentence "We observe that even the best attacks suffer from limited tactical diversity and a failure to learn during the course of a multi-goal attack run" is redundant with surrounding text.
- The paper could benefit from a single algorithm pseudocode overview instead of three separate algorithms in the appendix.

## Nice-to-Haves
- Testing against common defenses (SmoothLLM, paraphrasing, prompt-based safety filters) would substantially strengthen the paper's practical relevance.
- Reporting standard deviations or showing per-run scatter plots for the main results would address the most significant methodological concern.
- A clearer separation of ASR@K from standard ASR terminology would avoid reader confusion.

## Removed Points
- **Reproducibility concerns about code release**: Hypothetical concern — the paper is a conference submission and code release at publication is standard practice. Removed per hard rules.
- **Missing related works on specific attacks**: Removed per hard rules (cannot verify existence of suggested citations).
- **Formatting/style nitpicks**: Removed per hard rules (parser artifacts).
- **Complaints about appendix content being deferred**: The appendix was stripped by the parser; these references exist in the original submission per hard rules.

## Novel Insights
The most interesting finding is the asymmetric model-specific sensitivity to different attack components: reflection drives the largest gain for o3, while backtracking is most important for Claude Opus 4.1 (Table 3). This suggests that safety alignment engenders different failure modes across architectures/training procedures, and a one-size-fits-all attack is suboptimal — which directly motivates PLAGUE's plug-and-play modularity. The second insight is that goal-embedding-based retrieval (rather than response-embedding-based retrieval used in AutoDAN-Turbo) yields better lifelong learning signal, likely because semantically similar goals have more transferable attack strategies than semantically similar responses.

## Suggestions
1. Add standard deviations or confidence intervals for all main results (Tables 2–5), or at minimum report the per-run range to establish that the reported gains exceed run-to-run noise.
2. Evaluate against at least one standard defense (e.g., SmoothLLM, perplexity filtering) to test whether PLAGUE's gains are robust to basic countermeasures.
3. Clarify the ASR reporting convention: distinguish ASR@K from standard ASR, and specify which metric is being quoted when saying "81.4% ASR on o3."
4. If the appendix content (diversity analysis, Table 6, algorithms) is essential for reproducibility, consider moving key pieces (at least the diversity metric and Table 6) to the main paper.

## Score and Decision

**Calibration Anchors Used:**

| Anchor ID | Avg Score | Round | Comparison |
|-----------|-----------|-------|------------|
| 5kMwiMnUip | 1.40 | 1 (weak) | Much weaker — simple CoT prompting, no multi-turn framework |
| KyKTjRtyNG | 3.00 | 1 (weak) | Much weaker — single method on fewer models |
| BeOEmnmyFu | 2.50 | 1 (weak) | Much weaker — language-game approach, limited evaluation |
| kT6oc5CpEi | 3.00 | 1 (weak) | Much weaker — single-turn focus |
| fFtmpqLFvw | 5.75 | 1 (middle) | Weaker — human-only, single model (Llama), no automated framework |
| 1zt8GWZ9sc | 3.67 | 1 (middle) | Weaker — single-turn role-playing, older models |
| kvvvUPDAPt | 5.33 | 1 (middle) | Weaker — limited baselines, only 50 instances |
| w0b7fCX2nN | 3.75 | 1 (middle) | Weaker — simpler multi-turn, limited evaluation |
| 6Mxhg9PtDE | 9.50 | 1 (strong) | Much stronger — different topic (safety alignment depth), higher impact |
| syThiTmWWm | 7.75 | 1 (strong) | Stronger — different topic (benchmark gaming), higher community impact |
| 4KqkizXgXU | 8.00 | 1 (strong) | Stronger — curiosity-driven red teaming with RL, broader methodology |
| tc90LV0yRL | 8.67 | 1 (strong) | Stronger — different topic (cybersecurity benchmarks), higher scope |
| hXA8wqRdyV | 6.14 | 2 (narrow) | Comparable — strong ASR but simpler method, fewer models evaluated |
| hkjcdmz8Ro | 4.75 | 2 (narrow) | Weaker — PAIR is simpler, fewer models, lower ASR |
| aSy2nYwiZ2 | 6.67 | 2 (narrow) | Comparable — different focus (backdoor injection), similar empirical quality |
| e9yfCY7Q3U | 6.25 | 2 (narrow) | Comparable — improved GCG techniques, solid but narrower scope |
| sULAwlAWc1 | 7.00 | 2 (narrow) | Slightly stronger — ArrAttack includes defense evaluation and trained robustness model |
| H6UMc5VS70 | 5.75 | 2 (narrow) | Weaker — single-turn flipping attack, less comprehensive |
| iKgQOAtvsD | 5.75 | 2 (narrow) | Weaker — single-turn adversarial translation, narrower evaluation |

**Round 1 bracket:** 5.5–7.5 (clearly above the 3-range papers, comparable to the upper-middle band)

**Round 2 narrowing:** Anchors at 6.14, 6.25, 6.67, 7.00. The paper is stronger than the 5.75-range papers (FlipAttack, translation-based attack) but below ArrAttack (7.00) because ArrAttack includes defense evaluation and a trained component. The paper is comparable to the Simple Adaptive Attacks paper (6.14) and GCG improvements paper (6.25) but has a more novel framework contribution, though it lacks the statistical rigor those papers had.

**Final score:** 6.5. The paper's strengths — SOTA results on the hardest models, well-designed ablation, modular framework validated by experiment, and efficiency analysis — place it clearly in the top half of the bracket. The absence of variance reporting and defense evaluation prevents it from reaching the 7+ tier occupied by papers that address those concerns.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>