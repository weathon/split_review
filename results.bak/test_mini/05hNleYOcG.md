Now I have all the calibration data I need. Let me write the final consolidated review.

**Round 1 bracket analysis:** The paper is clearly above the weak band (<3.5, simple multi-turn papers with limited evaluation). It's comparable to the 4-6 band (GRAF 4.40, SEMA 5.00, Morpheus 5.00, ADJ 5.50) in terms of the multi-turn jailbreak domain. The paper targets harder models than most of these but has baseline-modification concerns that keep it from the 6.5+ range.

**Round 2 narrowing:** Comparing against SEMA (5.00, Accept Poster - weaker models, RL novelty), Morpheus (5.00, Reject - similar frontier model testing, "prompt engineering" concern), and ADJ (5.50, Accept Poster - theory-practice gap), PLAGUE scores comparably or slightly above due to its clean modular framework, thorough ablation, and testing on genuinely frontier models (o3, Claude Opus 4.1). However, the baseline modification concern tempers this.

**Final determination:** Score 5.5, Accept (Poster).

---

## Summary

This paper proposes PLAGUE, a modular three-phase framework (Planner, Primer, Finisher) for automated multi-turn jailbreak attacks on LLMs. It incorporates lifelong learning via a memory bank of successful strategies retrieved by goal embedding similarity. Evaluated on HarmBench across five frontier models (o3, o1, DeepSeek-R1, Claude Opus 4.1, Llama 3.3-70B), PLAGUE achieves SOTA attack success rates including 81.4% SRE on o3 and 67.3% on Claude Opus 4.1. The paper presents a systematic ablation study isolating each component's contribution and a budget analysis showing comparable LLM call counts to baselines.

## Strengths

1. **State-of-the-art results on genuinely frontier models.** PLAGUE achieves 81.4% SRE on OpenAI o3 and 67.3% on Claude Opus 4.1 (Table 2), improving over prior best by 32% and 40% respectively. These are among the hardest safety-aligned models available, making these results practically significant for the red-teaming community.

2. **Clean modular decomposition with systematic ablation.** The three-phase framework (Planner → Primer → Finisher) is well-motivated and the ablation study (Table 3) progressively adds Backtracking, Reflection, Planner, and Retrieval to show monotonic improvement on both o3 (0.587→0.814) and Claude Opus 4.1 (0.222→0.465). This controlled decomposition validates the design and is more rigorous than ablation provided by prior multi-turn works.

3. **Plug-and-play design that subsumes existing attacks.** The paper demonstrates that GOAT, Crescendo, and ActorBreaker can be dropped into PLAGUE's slots (Table 4), showing that using Crescendo as a Finisher with PLAGUE's Planner yields a 40.2% improvement on Claude Opus 4.1 over Crescendo alone. This modularity is a concrete practical contribution for red-teaming practitioners.

4. **Efficiency analysis with LLM call budgets.** Table 5 reports Target, Evaluator, and Planner LLM calls for each method, showing PLAGUE stays within one extra Target call of GOAT while achieving substantially higher ASR. This counters the concern that a more complex framework would be prohibitively expensive.

5. **Dual metric evaluation (SRE + Bin-ASR).** The paper reports both StrongREJECT (graded harmfulness) and binary-ASR (compatibility with prior work), providing more comprehensive assessment than most baselines.

## Weaknesses

### Major

- **Baseline modifications create uncertainty about comparative claims.** Each baseline is modified in ways that could reduce its performance: GOAT runs without attacker history ("impact is negligible" claimed but not evidenced); Crescendo has its own backtracking mechanism removed; ActorBreaker is limited to 2 actors. While the paper acknowledges these changes and provides rationales, it does not measure their impact. The reader cannot fully determine whether PLAGUE outperforms standard implementations of these baselines, or only modified versions. This is the most significant concern with the paper's central empirical claims.

- **"Lifelong learning" is overstated relative to the evidence presented.** The strategy library is initialized with two hand-curated seeds (line 120), operates within a single 200-sample HarmBench run (not across sessions), and relies on a cosine similarity threshold of 0.6 where fewer than 2 matches fall back to random retrieval. The paper does not report retrieval hit rates, analyze when retrieval actually helps versus hurts, or test whether performance improves over longer sequences. The framing as "lifelong" implies a scope of learning not demonstrated by the experiments.

- **Novelty is primarily architectural integration rather than fundamentally new algorithms.** Table 1 candidly shows that each individual component (planning from ActorBreaker, reflection from Crescendo, strategy libraries from GOAT, lifelong memory from AutoDAN-Turbo) exists in prior work. PLAGUE's contribution is identifying the right combination and providing a modular interface — a legitimate empirical contribution, but the paper frames it more ambitiously than the evidence supports.

- **Rubric scorer thresholds are presented without justification or ablation.** The scoring thresholds for backtracking (7/10 for Primer, 3/10 for Finisher, line 140) and the retrieval similarity threshold (0.6, line 128) are central design choices that directly affect behavior. No ablation or sensitivity analysis is provided to show these are not overfit to HarmBench.

### Minor

- **"Scales linearly" (Figure 2 caption) is imprecise.** The data (2→36.7, 4→68.7, 6→81.4, 8→80.8) shows a concave trend that plateaus at 6 turns, not a linear one. The paper immediately clarifies the plateau, making this a wording issue rather than a technical error, but it is inaccurate as written.

- **No statistical significance or variance reported.** Results are averaged over three runs but no error bars or confidence intervals are given. Several comparisons are close (e.g., DeepSeek-R1 SRE: PLAGUE 0.978 vs GOAT 0.978), making variance information important for interpretation.

- **Diversity analysis lacks a defined metric in the main text.** The paper claims "diversity improves by 15% (Figure 3)" and that "ActorBreaker has a higher overall diversity" without defining the diversity metric used. The figure presumably exists in the original paper, but the metric should be specified in the main text.

- **No Attacker LLM ablation.** All experiments use Deepseek-R1 as the Attacker. The contribution claims generality of the framework, which would be strengthened by showing results with at least one alternative Attacker model.

### Trivial

- Figure 2 caption: "PLAGUE scales linearly" (line 235) — as noted above, the trend is concave.
- The abstract claims "lesser or comparable query budget" but PLAGUE uses 6.53 total calls on o3 vs Crescendo's 5.28; the claim is still reasonable as "comparable" but slightly loose.

## Nice-to-Haves

- Validation of the Rubric Scorer against human judgments (standard for safety evaluation papers)
- Ablation of the backtracking thresholds (7/10, 3/10) and retrieval similarity threshold (0.6)
- Retrieval hit rate statistics for the lifelong learning component
- A variant with the strategy library initially empty to test whether the memory module truly learns

## Removed Points

These points were flagged by reviewers but are removed after verification:

- **"Fatal criticism about GOAT history removal with no evidence"** — The paper explicitly states "Through extensive ablation, we also observe that the impact on GOAT's performance with and without an attack history is negligible" (line 166). The claim is asserted without showing the ablation, which is a weakness but not fatal. This concern is retained in the Major section above.
- **"Table 2 is inconsistent for Claude"** — The paper clearly notes with an asterisk that Claude's best results are in Table 4 (line 190). This is transparent, not an inconsistency.
- **"Lack of discussion of data contamination"** — Speculative and not specific to this paper.
- **"Missing related works"** — Cannot verify without external sources; rule prohibits mentioning.
- **"Figure 3 is not properly described"** — Figure 3 was part of the original paper (stripped by parser). The text references it; the original submission would contain the figure with its caption and description.
- **Grammar/typo complaints** — These are parser artifacts, not author errors.

## Novel Insights

The most interesting insight from the harsh critic's analysis is a formalization that the paper hints at but does not state explicitly: the three-phase decomposition reveals that different components matter for different models. Table 3 shows that for o3, the largest single gain comes from Reflection (0.612→0.761), while for Claude Opus 4.1, the largest gain comes from Backtracking (0.222→0.396). This heterogeneity in which attack mechanisms are most effective against different safety-aligned models is potentially a deeper finding than the aggregate ASR numbers alone — it suggests that safety alignment methods create different failure mode distributions, and a modular framework like PLAGUE can exploit this.

## Suggestions

1. **Re-run the most critical baselines (GOAT with history, Crescendo with backtracking) under matched budgets** to demonstrate that PLAGUE's advantage is not an artifact of modifications. This single experiment would substantially strengthen the paper's core claims.

2. **Report retrieval hit rates for the lifelong learning module** — what fraction of queries retrieve at least one strategy with similarity >0.6, and does the hit rate increase over the course of the 200-sample run?

3. **Tone down the "lifelong learning" framing** to "within-benchmark memory augmentation" unless cross-session learning or cold-start (empty library) experiments are added.

4. **Define the diversity metric explicitly** in the main text, even if the figure details are deferred.

5. **Add error bars or confidence intervals** to the main results (Table 2), especially for close comparisons.

## Score and Decision

**Calibration anchors used:**

| Path | Avg Score | Round | Comparison to this paper |
|------|-----------|-------|-------------------------|
| `/home/wg25r/review_agent/human_reviews_2026/f9BuANYtJf.md` (GRAF) | 4.40 | R1 | Weaker — had fatal methodology flaw (response fabrication); PLAGUE is cleaner |
| `/home/wg25r/review_agent/human_reviews_2026/6eSNG1VNkl.md` (SEMA) | 5.00 | R1, R2 | Weaker on evaluation scope (smaller/older models), stronger on methodological novelty (RL training) |
| `/home/wg25r/review_agent/human_reviews_2026/11z2ZV85eV.md` (Morpheus) | 5.00 | R1, R2 | Similar frontier model testing, similar architectural-integration concerns; Morpheus rejected |
| `/home/wg25r/review_agent/human_reviews_2026/ilnKzaQSCh.md` (ADJ) | 5.50 | R2 | Similar novelty concerns but heavier mathematical framework; PLAGUE is cleaner |
| `/home/wg25r/review_agent/human_reviews_2026/7B9mTg7z25.md` (Attacker Moves Second) | 6.00 | R2 | Different contribution type (defense methodology critique); not directly comparable |
| `/home/wg25r/review_agent/human_reviews_2026/10gpXxro8z.md` | 2.67 | R1 | Much weaker — simple off-the-shelf LLM evaluation |
| `/home/wg25r/review_agent/human_reviews_2026/bQQkWXYjuy.md` | 2.50 | R1 | Much weaker — limited multi-turn approach |
| `/home/wg25r/review_agent/human_reviews_2026/h0lOaeDwF2.md` | 2.50 | R1 | Much weaker — LVLM-specific, narrower scope |
| `/home/wg25r/review_agent/human_reviews_2026/d1fVTnq3c8.md` | 2.50 | R1 | Much weaker — prompt guard bypass, different problem |

**Round 1 bracket:** Narrowed to 4.5–6.5 based on comparison to the weak (<3.5) and middle (3.5–7.5) bands.

**Round 2 narrowing:** Compared against SEMA (5.00), Morpheus (5.00), and ADJ (5.50). PLAGUE's stronger empirical evaluation on harder models and cleaner modular design place it above the 5.00 papers, while its baseline modification concerns and integration-dominant novelty cap it below 6.0.

**Final Score:** 5.5

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>