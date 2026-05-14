Now I have all the information I need. Let me synthesize the final review.

---

## Summary

PLAGUE proposes a plug-and-play, three-phase framework (Planner, Primer, Finisher) for multi-turn LLM jailbreaks that incorporates lifelong learning via a strategy memory bank. The framework decomposes the attack pipeline into modular components, allowing existing attacks (GOAT, Crescendo, ActorBreaker) to be swapped in as sub-modules. Evaluated on HarmBench across five frontier models (o3, o1, Deepseek-R1, Claude Opus 4.1, Llama 3.3 70B), PLAGUE reports state-of-the-art attack success rates, including 81.4% SRE on o3, supported by systematic component-wise ablations.

## Strengths

- **Modular three-phase decomposition with demonstrated benefits**: The Planner–Primer–Finisher separation is a clean design abstraction. Table 3 shows that adding backtracking, reflection, planning, and strategy retrieval progressively raises SRE on o3 from 0.587 (GOAT alone) to 0.814, with each component contributing measurably. Table 4 further demonstrates modularity by showing how swapping the Finisher from GOAT to Crescendo raises Claude Opus 4.1 performance to 67.3% SRE.

- **Lifelong strategy learning is novel for multi-turn attacks**: PLAGUE is the first multi-turn attack with a memory bank that stores successful strategies indexed by goal embeddings and retrieves them via cosine similarity (Section 3.3.1, confirmed by Table 1's component comparison). The RSS ablation in Table 3 shows this retrieval adds meaningful gains (+4.1 SRE on o3, +3.4 on Claude Opus 4.1).

- **Model-specific insights from systematic ablation**: Table 3 reveals that different components matter for different models — reflection drives gains on o3 while backtracking matters most for Claude Opus 4.1. This is a useful contribution for tailored red-teaming.

- **Efficiency on par with lean baselines**: Table 5 demonstrates that PLAGUE's total LLM calls are within ~1 call of GOAT and comparable to Crescendo, while delivering substantially higher ASR, confirming that gains do not come from increased query budget.

## Weaknesses

### Fatal

None.

### Major

- **Unvalidated baseline modifications for GOAT**: The paper modifies GOAT by removing attacker history and adding rubric-scorer-based early stopping, claiming "through extensive ablation, we observe negligible impact" of these changes (Section 4, Baselines). These ablations are not reported anywhere in the paper, and without them the reader cannot assess whether the modified GOAT baseline is faithful to the original method's strength. Since GOAT is the strongest baseline on o3 (Table 2), the headline "32.14% improvement" depends critically on this being a fair comparison. This needs to be addressed with reported ablations or a clear justification.

- **Cross-sample information leakage via the strategy memory bank**: The lifelong-learning memory R⁺ accumulates successful attack strategies across the full 200-goal HarmBench dataset during evaluation, and retrieval is based on cosine similarity between goal embeddings (Section 3.3.1). The paper never states that memory is reset per sample or per run. Consequently, an early jailbreak on one goal can inform later attacks on semantically similar goals, meaning the per-sample ASR is not computed under independent conditions. The RSS ablation in Table 3 (+4% SRE on o3, +3.4% on Claude Opus 4.1) indicates this effect is modest and not the sole driver of gains — PLAGUE without RSS still substantially outperforms baselines. Nevertheless, the paper should either (a) reset memory per goal and report those numbers, (b) report results using a strategy set collected from a held-out subset, or (c) explicitly discuss this as a feature rather than treating it as standard evaluation.

### Minor

- **No budget-scaling comparison for baselines**: Figure 2 shows PLAGUE's ASR scaling from 2 to 8 turns (plateauing at 6), which partially motivates the 6-turn budget. The paper does not provide equivalent scaling curves for any baseline, so the reader cannot assess whether the 6-turn cap differentially penalizes methods that might benefit from more turns (e.g., Crescendo's gradual escalation). A single-point comparison at 6 turns, without showing robustness across budget choices, weakens the strength of the comparison.

- **Ambiguous "improvement factor" phrasing**: The introduction states "improve by a factor of 32.14% for OpenAI's o3" and "by a factor of 40.2% on Claude's Opus 4.1." This phrasing is ambiguous — these are relative improvements (0.587 → 0.814 SRE is ~38.6% relative gain, and 0.48 → 0.673 SRE is ~40.2% relative gain), not multiplicative factors. Clarifying this as relative percentage-point improvement would avoid misinterpretation.

### Trivial

- The rubric scorer R's prompts for Planner vs. Finisher phases are described as "slightly modified" (Section 3.2) but deferred to Appendix B.1. Since the appendix is stripped from the submission copy, the reader cannot verify these differences. This is not a substantive flaw but worth noting for completeness.

## Nice-to-Haves

- A quantitative diversity metric (e.g., self-BLEU or embedding dispersion) across generated attack plans would substantiate the paper's claims about "diverse" attacks, which are currently supported only by a brief note about ActorBreaker's planner diversity (Section 5).
- Running PLAGUE with memory populated from a disjoint goal subset and evaluating on a held-out set would cleanly isolate the lifelong learning benefit from contamination effects.
- Reporting standard deviations or confidence intervals across the three runs would add statistical rigor, especially for the smaller-margin improvements in Table 3.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh Critic Claim: "Cross-sample contamination makes the empirical results untrustworthy / invalidates the paper"**: While the memory contamination concern is real (addressed as a Major weakness above), the harsh critic framed it as fatal and untrustworthy. This is overstated. Table 3 shows that PLAGUE without RSS (GOAT+BT+R+P) achieves 0.773 SRE on o3, already substantially above the GOAT baseline (0.587). The contamination primarily affects the RSS component, which contributes only ~4 additional SRE points. The core architectural gains are not dependent on cross-sample memory.

- **Harsh Critic Claim: "Metric-selection protocol gives PLAGUE an asymmetric advantage"**: The rubric scorer R uses generic criteria (compliance, practicality, detail, relevance — Section 3.2) and is applied uniformly for ASR@K selection across methods. GOAT is explicitly modified to use the same R (Section 4, Baselines). While PLAGUE also uses R internally for reflection/backtracking (which baselines do not), this is part of the method's design, not an evaluation asymmetry. The final judge J is external and independent. This criticism does not hold.

- **Strength Finder: "State-of-the-art results on diverse, resistant models" (as an unqualified strength)**: Kept above but qualified. The numbers are strong but the baseline fidelity concerns temper this claim somewhat.

- **Strength Finder: "Fine-grained rubric-based feedback" as a standalone strength**: Rubric-based scoring is common in LLM red-teaming; this is not a distinctive contribution. Removed as a standalone strength.

- **Harsh Critic: "Introduction's conclusion that PLAGUE breaks through with ease is premature"**: This is a tone complaint about confident language ("with ease"), not a substantive weakness. Removed.

- **Harsh Critic: "The abstract presents dramatic claims that the experimental section cannot sustain"**: Generic skepticism. The experimental section does report 81.4% SRE on o3 with systematic ablation support. The claims are ambitious but tied to evidence. Removed.

- **Harsh Critic: "The Crescendo backtracking-count removal and ActorBreaker K=2 limitation are unjustified modifications"**: For Crescendo, the paper follows the official implementation and only removes backtracking counts (a bookkeeping mechanism, not algorithmic). For ActorBreaker, K=2 is a natural budget constraint matching PLAGUE's own K=2. These are reasonable experimental controls. Removed.

- **Strength Finder: "Efficiency comparable to baselines" kept but generic phrasing trimmed.**

- **Strength Finder: "Well-written / clear"**: Removed as generic.

## Novel Insights

Beyond the paper's own contributions, the ablation results in Table 3 contain an interesting and underexplored finding: the relative importance of different attack components varies substantially across target models. Reflection drives most of the gain on o3 (SRE jumps from 0.612 to 0.761), while backtracking drives it on Claude Opus 4.1 (0.222 → 0.396). This suggests that model-specific safety alignment strategies create qualitatively different vulnerability profiles — o3 may be more susceptible to iterative refinement, while Claude may be more susceptible to context management. This observation has implications beyond PLAGUE, suggesting that red-teaming evaluations should account for model-specific vulnerability taxonomies rather than treating all models as interchangeable targets.

## Suggestions

- Report the missing GOAT ablation (with vs. without attacker history, with vs. without rubric-scorer early stopping) to validate baseline fidelity, or cite prior work that establishes these modifications are safe.
- Add a brief discussion of the memory accumulation design choice: why it is reasonable for a lifelong-learning system, and under what conditions it should vs. should not be reset.
- Add baseline scaling curves (ASR vs. turn budget for 1-2 representative baselines) to complement Figure 2 and justify the 6-turn choice beyond PLAGUE's own plateau.
- Clarify the "improvement by a factor of X%" language throughout the paper to avoid ambiguity between relative and absolute gains.

---

**Anchor comparison:**

| Anchor | Path | Avg Human Score | Comparison to PLAGUE |
|---|---|---|---|
| MAPA | h0lOaeDwF2.md | 2.50 | Much weaker: limited novelty, small-scale evaluation, no frontier models, weaker writing |
| CoaxChain | 6yCZEruFu9.md | 3.50 | Weaker: engineering contribution with limited novelty, baseline concerns similar but evaluation less comprehensive |
| GRAF | f9BuANYtJf.md | 4.40 | Closer but weaker: interesting methodology but flawed by response fabrication attacking "illusional" models; PLAGUE's methodology is cleaner and its ablation is more systematic |
| MultiBreak | uJgfj5EJ2W.md | 4.50 | Different genre (benchmark paper); comparable scores but PLAGUE is an attack method with stronger technical contribution |
| SEMA | 6eSNG1VNkl.md | 5.00 | Most comparable: SEMA has a clean RL-training methodology, strong transfer results, but evaluates on fewer/smaller models; PLAGUE evaluates on more diverse frontier models (o3, o1, Claude Opus 4.1) with stronger absolute numbers but has baseline fidelity concerns. Roughly comparable quality. |

PLAGUE sits near SEMA (5.00) in contribution and evaluation quality. It has a stronger model suite and better ablation insights, but carries the baseline-modification concern that SEMA avoids. The memory contamination issue is real but modest in impact. Overall, the paper makes a clear contribution with systematic evidence, placing it in the Accept (Poster) range.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>