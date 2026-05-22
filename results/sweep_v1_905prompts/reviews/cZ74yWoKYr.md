Now I have all the information I need. Let me compile the final review.

**Round 1 bracket:** Based on calibration search, the paper sits between the weak anchor band (papers scoring ~2-3, mostly reject due to limited evaluation or flawed methodology) and the strong anchor band (papers scoring ~8-9, accepted at top venues). The most informative band is the middle band (3.5-7.5) where the previous version of this same paper sits at 5.75.

**Round 2 narrowing:** Compared to the previous version (5.75), the current version adds: Ruler benchmark (13 tasks including needle-in-a-haystack), Qwen2.5-32B evaluation, SCBench multi-turn QA, detailed perturbation analysis (Figures 4-6), and improved notation. These are substantial improvements. The paper is stronger than ChunkKV (5.25) and LazyLLM (5.00) which have similar scopes but less thorough evaluation. It's weaker than CAKE (7.00) which introduces a more novel layer-wise allocation algorithm and demonstrates 10× decoding speedup.

**Final score: 6.0** — The paper has solid theoretical motivation, thorough evaluation across diverse settings, and a practical plug-and-play contribution. The main weaknesses are a pseudocode inconsistency (Algorithm 1) and the incremental nature of the contribution (a better selection metric within existing frameworks).

Now writing the review.

---

Let me be precise about the Algorithm 1 issue. The harsh critic says:

"Algorithm 1 (lines 2–3) first computes attention weights `A = softmax(qK^T)`, then immediately overwrites `A` with `(A+ε) ⊙ (L1 norm of rows in V)`. Both stages then select from this overwritten `A`, meaning both stages actually use the same product—contradicting the textual description."

This is factually correct based on the pseudocode. The text says Stage 1 uses attention weights alone. The pseudocode has both stages using the product. This is a real inconsistency.

However, the harsh critic also says "If the implementation matched the pseudocode, the two-stage structure would be meaningless" — this is speculation. The implementation likely matches the text (since the α ablation shows α=0 meaning no Stage 1 causes degradation on Mistral, confirming Stage 1 serves a distinct purpose). So it's most likely a pseudocode bug where `A` was reused as a variable name.

Let me note this clearly.## Summary

This paper formalizes KV cache entry selection from an output perturbation perspective. It derives an upper bound on the L₁ output perturbation (Theorem 3.3) that depends on both attention weights *and* projected value-state norms, revealing that attention-weight-only heuristics are suboptimal. Based on this insight, the paper proposes a two-stage greedy algorithm (Algorithm 1) that first selects entries with high attention weights (to satisfy a coverage condition) and then selects to minimize the derived upper bound. The algorithm is a plug-and-play enhancement demonstrated across three LLMs (Llama-3.1-8B, Mistral-7B, Qwen2.5-32B), three SOTA eviction methods (SnapKV, AdaKV, HeadKV), and 29 datasets from Ruler and LongBench, reducing average compression loss by ~57.5% with negligible computational overhead.

## Strengths

- **First formal treatment of critical KV cache selection from an output perturbation perspective.** Theorem 3.3 derives an explicit upper bound involving both attention weights *A* and projected value states *VWᵒ*, providing a principled justification for going beyond attention-weight-only heuristics. This is a genuine conceptual contribution to a field dominated by empirical rules.

- **Consistent and large improvements across diverse settings.** Across 3 models × 3 eviction methods × 29 datasets, the algorithm reduces compression loss by an average of ~57.5%. Gains are particularly pronounced at small cache budgets (20-40%), and head-/layer-/budget-wise perturbation analysis (Figures 4-6) empirically validates that the theoretical bound translates to reduced practical perturbation.

- **Negligible overhead and clean integration.** The additional computation (one linear projection *VWᵒ* + elementwise product) adds only 0.04s per request at 32K context (Figure 3a) and does not affect decoding latency. Algorithm 2 shows how the method replaces a single selection step in existing observation-window-based frameworks, making it truly plug-and-play.

- **Thorough ablation and analysis.** The α sensitivity study (Table 4) confirms both the robustness of α=0.5 and the critical necessity of the two-stage design (α=0.0 degrades Mistral by >10 points). The perturbation analysis at head, layer, and budget levels provides direct evidence that the theory-motivated objective reduces actual output perturbation.

## Weaknesses

### Major

- **Algorithm 1 pseudocode is inconsistent with the textual description.** The text states Stage 1 selects KV entries by attention weights alone, while Stage 2 uses the product of attention weights and value-state norms. However, the pseudocode overwrites `A` (originally softmax attention weights) on line 3 with `(A+ε) ⊙ L1_norm(VWᵒ)`, and both Stage 1 (line 5) and Stage 2 (line 8) select from this overwritten product. This makes both stages use the same criterion in the pseudocode, contradicting the text, Assumption 3.4 (which references `∑ Top_k(A, b')` on raw attention weights), and Theorem 3.5. The implementation almost certainly matches the described two-stage design (the α=0.0 ablation confirms Stage 1 serves a distinct purpose), but the pseudocode as written is wrong and must be corrected. This is the most critical presentation issue in the paper.

- **The theoretical framing overstates the rigor.** The paper claims to "formalize" and "provide theoretical analysis," but the two-stage greedy algorithm is a heuristic motivated by, not derived from, the upper bound. Stage 1 uses a fixed α=0.5 with no per-head or per-budget adaptation beyond the single heuristic rule (allocate 50% of budget to high-attention entries). While Assumption 3.4 is verified empirically (Appendix A), the bound's tightness is never evaluated — no comparison of the bound value to actual perturbation for random vs. optimized selections. The theory provides valuable motivation and a selection criterion for Stage 2, but the overall algorithm design involves substantial heuristic engineering.

### Minor

- **No comparison with a direct single-stage product baseline.** The paper motivates the two-stage design via Assumption 3.4, but never compares against a single-stage baseline that simply selects the top-*b* entries by `A_i × ||VWᵒ_i||₁`. The α=0.0 ablation partially covers this, but it is only tested at 20% cache on LongBench, not across budgets or on Ruler. A dedicated single-stage product baseline would cleanly isolate the value of Stage 1.

- **The "more than half reduction" claim lacks precise reporting.** While the average across all 18 method-model pairs is ~57.5% (supporting the claim), individual pairs vary from 20.4% (SnapKV on Mistral, Ruler) to 97.2% (AdaKV on Qwen, Ruler). Reporting the average relative reduction with per-pair breakdown and standard deviation would make the claim precise and verifiable, rather than relying on visual inspection of Figure 1.

- **No statistical significance or variance reporting.** All tables report point estimates without error bars, confidence intervals, or significance tests. Given the large number of tasks and the consistent but sometimes modest improvements (e.g., few domains where gains are <1 point), standard errors or paired tests would strengthen confidence in the results.

### Trivial

- The α sensitivity analysis (Table 4) is only shown at 20% cache budget. The paper mentions 10% results in Appendix C (stripped), but evaluating at multiple budgets (e.g., 10%, 40%) would strengthen the robustness claim.

## Nice-to-Haves

- An analysis of failure cases — tasks, heads, or token positions where the method does not improve (or slightly degrades), with discussion of why.
- A brief sketch of the key inequality steps in the bound derivation (Theorem 3.3 → Theorem 3.5) in the main text, so readers can assess the assumptions without consulting the appendix.
- Results on larger models (e.g., 70B scale) to strengthen the claim of universality.

## Removed Points

*The following points were raised by reviewers but are removed as noise:*

- **"Theoretical bound is not directly optimized" (harsh critic):** Demoted. Stage 2 (Theorem 3.5) *does* directly minimize the upper bound θ̂ — selecting top-*k* by `A_i × ||VWᵒ_i||₁` maximizes Σ N''ᵢ Aᵢ ||Vᵢ,:||₁, which is precisely the term being optimized. The critic incorrectly conflates "Stage 1 is heuristic" with "the algorithm does not minimize the bound."
- **Missing baselines (StreamingLLM etc.):** Per hard rules, I cannot evaluate completeness of related-work coverage without external sources. Removed.
- **Formatting/typo/style nitpicks (appendix stripping, variable naming, etc.):** Removed per hard rules — these are parser artifacts or standard presentation issues.
- **"More than half claim is imprecise" as a strong weakness:** Weakened. The calculation confirms ~57.5% average reduction. The claim is factually correct; the weakness is only about precision of presentation, not accuracy.

## Novel Insights

Beyond the paper's own contributions, a synthesis of the reviewer signals reveals an important tension: the paper's theoretical machinery (the bound derivation) is largely orthogonal to its algorithmic success. The bound provides a *rationale* for why value states matter, but the actual algorithm is a simple two-stage Top-K that could have been discovered purely empirically. This disconnect — between the formal framing and the heuristic execution — is a recurring pattern in the efficient-inference literature. The paper would be strengthened by explicitly acknowledging this gap and positioning the theory as *motivation* for a search direction, rather than as a *derivation* of the algorithm.

## Suggestions

1. **Fix Algorithm 1** to match the description: keep raw attention weights `A` for Stage 1 selection, and use a separate variable (e.g., `S`) for the product `(A+ε) ⊙ ||VWᵒ||₁` used in Stage 2.
2. **Add a single-stage product baseline** (select top-*b* by `A_i × ||VWᵒ_i||₁` directly) across multiple cache budgets to empirically justify the two-stage design.
3. **Report the average relative loss reduction** with a per-pair breakdown and standard deviation, making the "more than half" claim precise.
4. **Include error bars or confidence intervals** for at least a representative subset of results (e.g., 3-4 LongBench tasks with multiple seeds).
5. **Evaluate α at additional cache budgets** (e.g., 10%, 40%) to strengthen the robustness analysis.

## Score and Decision

**Calibration anchors used (all rounds):**

| Path | Avg Score | Round | Comparison to this paper |
|------|-----------|-------|-------------------------|
| `lRTDMGYCpy` (same paper, prev. version) | 5.75 | 1 | Current version is stronger (added Ruler, 32B model, perturbation analysis). |
| `am5Z8dXoaV` (LazyLLM) | 5.00 | 1 | Weaker — less thorough evaluation, more hyperparameter tuning concerns. |
| `0ZcQhdyI3n` (LSH-E) | 3.83 | 1 | Weaker — limited baselines, no timing experiments, narrower scope. |
| `pG820nmDvy` (Top-k attention) | 4.67 | 1 | Weaker — lacks formal motivation, limited baselines. |
| `4QWPCTLq20` (IntelLLM) | 3.00 | 1 | Much weaker — poor evaluation, unclear contribution. |
| `CRQ8JuQDEd` (MiKV) | 5.00 | 2 | Comparable scope but this paper has stronger theoretical motivation. |
| `8sglLco8Ti` (ChunkKV) | 5.25 | 2 | Comparable but this paper has stronger empirical validation. |
| `EQgEMAD4kv` (CAKE) | 7.00 | 2 | Stronger — more novel layer-wise allocation, 10× decoding speedup. |

**Round 1 bracket:** 4.5–7.0. **Round 2 narrowing:** Compared to the previous version (5.75) which lacked Ruler, 32B evaluation, and perturbation analysis, the current version is clearly stronger. It is weaker than CAKE (7.00) which introduces a more novel algorithm with latency improvements. The final score of **6.0** reflects a solid contribution with thorough empirical validation, tempered by the incremental nature of the contribution (a better selection criterion within existing frameworks) and the Algorithm 1 presentation flaw.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>