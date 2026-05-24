Now let me write the consolidated review.

## Summary

This paper studies KV cache eviction in LLM inference. The authors observe that existing methods rely solely on attention weights for selecting critical cache entries. Through an output perturbation analysis, they derive an upper bound (Theorem 3.3) showing that **both** attention weights **and** projected value states matter. They propose a plug-and-play selection criterion—the product of attention weight and L1 norm of the projected value state—and integrate it into three existing eviction methods (SnapKV, AdaKV, HeadKV). Experiments on 29 datasets from Ruler and LongBench across three LLMs show consistent improvements, often halving the compression loss relative to the full cache, with negligible computational overhead (~0.06s additional prefill time).

---

## Strengths

1. **Formal perturbation bound reveals the insufficiency of attention-only heuristics (Theorem 3.3).** The derivation shows that output perturbation depends on both attention weights *and* projected value states \(\|\mathbf{V}_{i,:}\|_1\), providing a principled explanation for why attention-weight-only selection is suboptimal. This is a genuinely useful conceptual contribution to the cache eviction literature.

2. **Consistently strong empirical gains across a broad evaluation.** Across 3 LLMs (Llama-3.1-8B, Mistral-7B-v0.3, Qwen2.5-32B), 3 base eviction methods (SnapKV, AdaKV, HeadKV), and 29 datasets, the proposed selection criterion reduces compression loss by more than half on average (e.g., on Llama-3.1-8B with HeadKV at 40% cache, loss drops from 12.16% to 1.93% on Ruler). Improvements are seen in 88 out of 90 long-dependency test cases (97.8% success rate).

3. **Negligible computational overhead.** At 32K context and batch size 1, TTFT increases by only 0.06s (3.54→3.60s). Decoding latency is identical to the base eviction method. This confirms that the additional \(VW^O\) computation is effectively free.

4. **Perturbation analysis confirms practical behavior aligns with theory.** Figures 4–6 show that the algorithm reduces output perturbation in 92% of Llama-3.1-8B attention heads, with progressive benefits across layers and across cache budgets from 2.5% to 40%. This provides empirical support that the proposed selection criterion indeed lowers output perturbation, not just task scores.

---

## Weaknesses

### Major

1. **Mismatch between the textual description of the algorithm, the pseudocode, and the theoretical assumptions — the paper's central theoretical framing does not apply to the algorithm as implemented.**

   The text in Section 3.4 states: *"In the first stage, a fraction of the budget… is allocated to prioritize KV cache entries with high attention weights."* Assumption 3.4 then builds on this, requiring that stage 1 selects entries with the **highest attention weights** so that their cumulative weight \(\sigma > 0.5\). Theorem 3.5 then claims that stage 2 minimizes an upper bound of the perturbation, conditional on this assumption.

   **However, Algorithm 1 computes a composite score \(\mathcal{A} = (A + \epsilon) \cdot \|\mathbf{V}_{i,:}\|_1\) on line 3 and both stages select from this same composite score (lines 5 and 8).** The algorithm never selects entries by attention weights alone. Therefore:
   - Assumption 3.4 is **not guaranteed** by the algorithm — selecting by the product does not ensure the selected entries have the highest attention weights.
   - Theorem 3.5, which depends on this assumption, does **not** apply to the algorithm that was actually run.
   - The two-stage framing is also misleading: because both stages use the same score, the result is equivalent to single-stage Top-K selection by \(\mathcal{A}\).

   This is not a minor presentational glitch — it undermines the paper's central narrative of providing a "formally grounded" perturbation-constrained selection algorithm. The empirical results remain valid and interesting (the product score works well in practice), but the claimed theoretical grounding is disconnected from the actual implementation. The authors should either (a) revise Algorithm 1 so stage 1 uses attention weights alone, matching the text and theory, or (b) revise the text and theory to match the algorithm.

2. **Inconsistent \(\alpha\) value between pseudocode and experiments.** Algorithm 1 lists \(\alpha = 0.25\) as the default hyperparameter, but the text and all experiments use \(\alpha = 0.5\). This makes the pseudocode unreproducible as written.

### Minor

3. **Perturbation analysis measures only the first decoding token.** Section 4.7 reports perturbation on the *first decoding token's* attention output. The connection to cumulative perturbation over a full generation (and to downstream task accuracy) is plausible but not directly demonstrated. While reasonable as a proxy, the paper should acknowledge this limitation more explicitly.

4. **The \(\alpha\) ablation does not cleanly separate the contributions of attention weights vs. value norms.** Table 4 varies \(\alpha\) but, given the current pseudocode, both stages use the same composite score regardless of \(\alpha\), so varying \(\alpha\) would not change the set of selected entries. This suggests the *actual implementation* may differ from the pseudocode (using attention weights in stage 1 and the product in stage 2, as the text describes). The paper would benefit from an explicit comparison of three selection criteria head-to-head: attention alone, value-norm alone, and the product.

### Trivial

5. **Algorithm 1 uses variable name \(\mathbf{V}\) for the projected values \(VW^O\), while \(V\) is the original value states.** This is clear from context but could be confusing on first reading as the notation conflicts with standard usage.

---

## Nice-to-Haves

- The paper could explicitly state the selection criterion in one clear formula in the main text: *"We select entries with the largest \(A_i \cdot \| (VW^O)_i \|_1\)."*
- The efficiency results (TTFT increase of 0.06s) could be reported in a small table for precision, in addition to the figure.
- A comparison with the value-norm-alone baseline would cleanly demonstrate the contribution of each term in the product.

---

## Removed Points

- **"The α=0 experiment does not test the claimed separation of stages"** — This point is noted but folded into Major weakness #1 (the two-stage framing is inconsistent with the pseudocode anyway).
- **"Missing related works"** — Removed per instructions (cannot verify external sources).
- **"Formatting/style nitpicks" and "typos"** — Removed per instructions.
- Several generic strengths from the Strength Finder (e.g., "addressed an important problem") were removed per instructions as they lack specific citation or concrete content.

---

## Novel Insights

Beyond the paper's own contributions: the finding that the product \(A_i \cdot \|(VW^O)_i\|_1\) consistently outperforms attention-weight-only selection across 3 models and 3 base methods is a clean, reproducible empirical result that deserves attention regardless of the theoretical framing issues. The fact that 92% of Llama-3.1-8B heads show lower perturbation with this criterion suggests the value-norm signal is broadly, not selectively, useful.

---

## Suggestions

1. **Resolve the algorithm-theory inconsistency.** This is the single most important fix. Either:
   - **(Preferred option)** Revise Algorithm 1 so that stage 1 selects by attention weights alone (using \(A\) not \(\mathcal{A}\)) and stage 2 selects by the product \(\mathcal{A}\). This would make the algorithm match the text and satisfy Assumption 3.4, restoring the theoretical guarantee of Theorem 3.5.
   - Alternatively, revise the text and theory to describe a single-stage selection by the product \(\mathcal{A}\), dropping the two-stage framing and deriving an appropriate theoretical bound for this criterion.

2. **Fix the \(\alpha\) inconsistency.** Set \(\alpha = 0.5\) in Algorithm 1 to match all experiments, or clearly explain what \(\alpha = 0.25\) corresponds to.

3. **Add an explicit comparison of selection criteria.** Report results for: (a) attention weight alone, (b) value-norm alone, and (c) the product. This would cleanly demonstrate the contribution of each term.

---

## Calibration Report

**Round 1 (Bracketing):** Queried for "KV cache eviction in LLM inference" with three bands: (<3.5), (3.5–7.5), (>7.5). Low band returned papers avg 2.5–3.33 (rejected/withdrawn). Middle band returned ReST-KV (4.80, Accept Poster), DefensiveKV (5.60, Accept Poster), Learning to Evict (4.00, Reject), among others. High band returned papers on unrelated topics (oral/poster on multi-turn conversation, transduction, etc.) — none topically relevant to KV cache eviction.

**Round 2 (Narrowing):** Queried within (3.5–5.5) and (5.0–7.0). Retrieved TRIM-KV (5.50, Accept Poster), DefensiveKV (5.60, Accept Poster), ReST-KV (4.80, Accept Poster), and others.

**Anchors read in full:**
- **ReST-KV** (4.80, Accept Poster) — Similar topic; strong empirical results but some reviewers noted limited novelty and computational overhead. This paper has broader evaluation but worse internal consistency (theory-algorithm mismatch).
- **DefensiveKV** (5.60, Accept Poster) — Cleaner presentation and theory-practice alignment. This paper has a similar contribution level but the algorithm-theory mismatch is a liability that DefensiveKV does not share.
- **TRIM-KV** (5.50, Accept Poster) — Training-based approach; some reviewers questioned missing baselines and benchmarks. This paper is training-free with broader benchmark coverage but has the internal inconsistency issue.
- **Learning to Evict** (4.00, Reject) — RL-based approach with limited scope (one model, shorter contexts). This paper is clearly stronger empirically.

**Final score:** 5.0. The paper offers a genuinely useful empirical finding (product of attention weight and value norm as a selection criterion) with strong and broad evaluation, but the algorithm-theory mismatch is a real flaw that weakens the claimed formal grounding. The paper sits between ReST-KV (4.80) and DefensiveKV (5.60) — better evaluated than ReST-KV but with a more significant presentational/theoretical flaw.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept</decision>