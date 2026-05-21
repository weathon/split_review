Now I have a solid calibration. Let me synthesize the final review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths

**[Core] 1. First formalization of critical KV cache identification as output perturbation minimization.**  
Prior work (H2O, Scissorhands, SnapKV, AdaKV, HeadKV) relied on attention-weight heuristics without a formal objective. The paper defines the problem in Definition 3.1 as minimizing the L₁ distance between full-cache and evicted-cache attention outputs and derives an upper bound (Theorem 3.3) that reveals the importance of projected value states VW^O — a factor ignored by all prior methods. This provides a principled answer to the two questions posed in the introduction.

**[Core] 2. Universal plug-and-play enhancement with large, consistent gains.**  
The perturbation-constrained selection algorithm (Algorithm 1) integrates into three distinct SOTA eviction methods (SnapKV, AdaKV, HeadKV) by replacing only their selection step (Section 3.6, Algorithm 2). Gains are consistent across all three methods on 29 datasets spanning Ruler and LongBench (Figure 1, Tables 1–2). For example, on Qwen2.5-32B with Ruler, adding the algorithm reduces HeadKV's loss from 13.7% to 3.4% (Table 1). The improvement holds across 88 out of 90 long-dependency test cases on LongBench (Table 2).

**[Core] 3. Unusually thorough empirical evaluation.**  
The evaluation covers 13 Ruler tasks (Table 1) and 16 LongBench tasks (Table 2) with three LLMs (Llama-3.1-8B, Mistral-7B-v0.3, Qwen2.5-32B) at cache sizes from 20% to 60%, plus multi-turn QA on SCBench with contexts up to 100K tokens (Table 3). The sensitivity analysis on α (Table 4), efficiency benchmarks (Figure 3), and head/layer/budget-level perturbation analysis (Figures 4–6) provide strong supporting evidence that the mechanism works as intended.

**[Core] 4. Negligible computational overhead.**  
Efficiency evaluation (Section 4.6) shows TTFT increase of only 0.06s for batch size 1 (3.54→3.60s) and 0.04s per request for batch size 4. Decoding latency remains identical to the base cache eviction methods (0.0332s, 2.49× speedup over full cache). This makes the method practical for real deployment.

**[Supporting] 5. Direct validation of the perturbation-reduction mechanism.**  
Section 4.7 demonstrates that the algorithm reduces practical output perturbation in over 92% of Llama-3.1-8B attention heads, that reduction accumulates across layers (Figure 5), and that it holds across cache sizes from 2.5% to 40% (Figure 6). This bridges the theoretical bound to measurable empirical improvement.

## Weaknesses

### Fatal
None.

### Major

1. **Missing ablation that isolates the contribution of the value-state norm term.** The algorithm's key novelty is incorporating ‖V_i‖₁ into stage 2 selection. However, the paper does not include an ablation comparing (a) full algorithm (α=0.5), (b) two-stage with α=0.5 but stage 2 uses attention weights only (no ‖V_i‖₁), and (c) single-stage attention-weight-only baseline. Such an ablation would directly test whether the value-norm term adds value beyond the two-stage design itself. The α sensitivity analysis (Table 4) partially mitigates this — α=0.0 (all budget to stage 2 with value norms) outperforms the baseline for Llama but catastrophically fails for Mistral, suggesting the two-stage structure is critical for some models. But this does not isolate the value-norm term specifically: it conflates "two-stage" with "use value norms in stage 2." Without variant (b), the reader cannot tell whether the gains in stage 2 come from the second-pass reallocation or from the value-norm signal. Given that the paper's central claim is that value states matter beyond attention weights, this is a notable evidential gap.

### Minor

2. **Theoretical grounding is a motivating principle, not a provably optimal algorithm, and this could be stated more clearly.** Theorem 3.3 derives an upper bound θ on output perturbation. Minimizing θ directly is non-trivial (acknowledged in Section 3.4), so the paper proposes a two-stage greedy algorithm. Theorem 3.5 shows that under Assumption 3.4 (σ > 0.5), stage 2 minimizes a *different* upper bound θ̂ that factorizes over entries — but there is no analysis of how much suboptimality this two-stage factorization introduces versus the original bound, nor a comparison against a one-stage variant that jointly considers both terms. The paper is not hiding this (it says "directly minimizing the upper bound θ remains non-trivial"), but the framing of Theorem 3.5 ("directly minimizes an upper bound") could give a misleading impression of provable optimality. This does not undermine the empirical results, which are strong, but it means the theory should be presented as principled motivation rather than an exact algorithm guarantee.

3. **Statistical significance is not reported.** The Ruler experiments use 100 instances per task, and the improvements are generally large, so this is unlikely to change the qualitative conclusions. However, some task-level differences are small (e.g., Llama SnapKV on "niah_multik2y2" from 93.00 to 92.67, or some Code domain results in Table 2), and confidence intervals or standard errors would strengthen confidence in the reported gains. This is a minor evidential weakness.

### Trivial
None.

## Nice-to-Haves
- A summary figure or table of the σ > 0.5 verification (currently in Appendix A) in the main text would strengthen the justification of α=0.5.
- Discussion of limitations: whether the method extends to dynamic eviction during decoding, and whether W^O is always accessible (e.g., tied-embedding variants).

## Removed Points
- **Harsh Critic's point about Assumption 3.4 verification being in Appendix A (making it "impossible to verify")**: The appendix exists in the original submission but was stripped by the PDF parser. The paper clearly states the verification exists. This is not a methodological weakness.
- **Harsh Critic's point about using L₁ vs L₂ norm for V_i,; in the bound**: Footnote 1 already notes that L₂ distance yields similar gains (Appendix J). The bound uses L₁ for ‖V_i,:‖₁; the alternative metric choice for the overall distance is already discussed. This is a minor design choice, not a weakness.
- **Harsh Critic's suggestion to compare against FastGen or TOVA**: Not necessary given the paper already integrates with three SOTA methods (SnapKV, AdaKV, HeadKV) that cover the main design axes.
- **Strength Finder's generic strengths** (e.g., "addresses an important problem," "is well-written"): Removed because they lack specific, concrete anchors and are already implied by the core strengths retained.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. Add the ablation comparing two-stage (α=0.5) with stage 2 using attention weights only vs. attention×value-norm to directly isolate the contribution of the value-state term.
2. Report standard errors or confidence intervals for the main aggregate results.
3. Clarify in the main text that the theoretical analysis is a principled motivation for the selection criteria rather than a proof that the two-stage algorithm optimally minimizes the original bound.

## Score and Decision

Let me summarize the calibration anchors:

**Round 1 — Bracketing:**
| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| c6dwCJM0CK (Coverage-Driven KV) | 3.00 | R1 | Weaker: narrower evaluation, no theoretical foundation |
| T0ii3nAxk4 (SentKVCompress) | 2.50 | R1 | Weaker: sentence-level compression, less principled |
| 542c8KxeQt (SyncKV) | 3.33 | R1 | Weaker: addresses a different sub-problem (attention drift) |
| wnhwQp8Umq (EpiCache) | 3.33 | R1 | Weaker: episodic management, no perturbation theory |
| PhEHuo7oMm (ReST-KV) | 4.80 | R1 | Weaker: also uses output reconstruction but has O(L) prefill overhead, less comprehensive evaluation |
| k3IAjIsfyw (OracleKV) | 4.00 | R1 | Weaker: hand-crafted oracle guidance, less general |
| kMLfUshPwo (TAKE) | 4.00 | R1 | Weaker: chunked prefill eviction, narrower scope |
| t7lJ2OEGbJ (KVP - RL) | 4.00 | R1 | Weaker: RL-based, limited to one model, no latency measurements |
| VKGTGGcwl6 (Multi-turn conversation) | 8.00 | R1 | Different topic (conversation analysis), not comparable |
| kkBOIsrCXh (NavFoM) | 8.00 | R1 | Different topic (navigation), not comparable |

**Round 2 — Narrowing (4.5–7.5):**
| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| kXhPkDaFbJ (ProtoKV) | 5.00 | R2 | Weaker: expensive preprocessing (30+ min), smaller gains (+2.11%), less comprehensive evaluation |
| aNVKROYpLB (KVTC) | 5.50 | R2 | Comparable: different approach (transform coding), similar thoroughness, but has calibration dependency and latency concerns |
| B2iqbCQviR (MixKV) | 5.50 | R2 | Comparable: VLM-focused, similar plug-and-play approach, but less theoretical grounding |
| R7fv5NWfMm (Randomization Boosts) | 6.50 | R2 | Stronger on theory side but addresses a different problem (serving/routing, not single-sequence eviction) |

**Round 1 bracket:** The paper sits between ~5.0 and ~7.0, well above the weak KV cache eviction anchors (2.5–4.0) and comparable to or stronger than the middle anchors (5.0–5.5).

**Round 2 narrowing:** The paper is stronger than ProtoKV (5.00) — more thorough evaluation, cleaner approach, negligible overhead. It is comparable to KVTC (5.50) and MixKV (5.50) in thoroughness but has a stronger theoretical foundation. It does not match the theoretical depth of the Randomization Boosts paper (6.50), but that paper addresses a fundamentally different problem (multi-LLM serving).

**Final score: 6.0.** The paper has a novel theoretical framing, unusually thorough and convincing empirical evaluation, and practical plug-and-play utility with negligible overhead. The weaknesses — a missing ablation for the value-norm term and the theory-algorithm gap — are real but do not threaten the core claims. This is a solid Accept.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>