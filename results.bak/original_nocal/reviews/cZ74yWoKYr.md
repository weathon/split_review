Now I have all the information needed. Let me produce the final consolidated review.

**Note on Algorithm 1's inconsistency**: I need to verify the exact notation. Line 2 sets `A = softmax(qK^T)`, then line 3 overwrites `A` as `(A + ε) ⊙ (L1 norm...)`. On line 5, `A_i ∈ Top_k(A, b')` — this `A` refers to the post-overwrite combined score. The text says stage 1 prioritizes "high attention weights." This is a genuine discrepancy.

---

## Summary

This paper formalizes critical KV cache entry selection as minimizing output perturbation. By deriving an upper bound on the L₁ output perturbation (Theorem 3.3), the authors show that attention weights alone are insufficient — the projected value states (VW^O) also matter. They propose a two-stage greedy selection algorithm that constrains this bound and integrate it as a plug-and-play enhancement into three existing cache eviction methods (SnapKV, AdaKV, HeadKV). Experiments across 29 datasets from Ruler and LongBench, three LLMs (7B–32B), and multiple cache sizes show consistent and often large improvements.

## Strengths

1. **Formal derivation showing attention weights alone are insufficient.** Theorem 3.3 derives an upper bound on output perturbation that includes both attention weights and the L₁ norm of value states projected through W^O. This provides a principled argument — grounded in the actual attention computation — for why prior attention-only heuristics are suboptimal. (Section 3.3, Equation 5)

2. **Consistent and substantial empirical gains.** Across three LLMs, three base eviction methods, 29 datasets, and multiple cache sizes, the proposed algorithm reduces compression loss by more than half on average (e.g., AdaKV on Llama-3.1-8B in Ruler: from 13.92% loss to 5.24%; Qwen2.5-32B: from 24.30% to 0.69%). On LongBench, 88 out of 90 test cases improve. These gains are verified at multiple cache budgets (20%–80%) and extend to multi-turn SCBench tasks. (Figure 1, Tables 1–3)

3. **Universal plug-and-play integration with negligible overhead.** The algorithm replaces only the selection step in existing eviction pipelines (Algorithm 2). Efficiency measurements (Figure 3) show a TTFT increase of only 0.06s at 32K context (batch size 1), with decoding latency identical to base methods — making the improved quality essentially cost-free.

4. **Empirical verification that the algorithm reduces actual output perturbation.** Head-wise analysis shows lower perturbation in 92% of Llama-3.1-8B attention heads (Figure 4), and layer-wise analysis shows the reduction accumulating to near-zero perturbation at the final layer (Figure 5). This directly links the theoretical perturbation bound to observable practical behavior.

5. **SCBench multi-turn QA results** demonstrate effectiveness in realistic long-horizon interactive settings (e.g., EN.QA at 40% budget: 15.71 → 22.14), showing the method works beyond single-turn benchmarks.

## Weaknesses

### Fatal

None.

### Major

1. **Algorithm 1 pseudocode is inconsistent with the textual description and theoretical framework.** The text (line 130–131) states that Stage 1 "prioritize[s] KV cache entries with high attention weights," and Assumption 3.4 explicitly defines Stage 1 as selecting by `Top_k(A, b')` where `A` denotes attention weights. However, Algorithm 1 (line 3) overwrites the variable `A` with the combined score `(A + ε) · ||VW^O||_1`, and then line 5 uses this combined score for Stage 1 selection. The theory (Assumption 3.4, Theorem 3.5) assumes Stage 1 selects by attention weights alone, but the pseudocode selects by the combined product. **The α ablation confirms this is not just a notation issue:** If both stages used the same combined score `𝒜`, then selecting the top `b` entries (α=0) would yield the same set as splitting into `b'` then `b''` (α=0.5) — the results would be identical. But Table 4 shows α=0 produces a catastrophic 31.94 vs α=0.5's 42.85 on Mistral-7B, proving the implementation uses different scoring for the two stages. This means the pseudocode is erroneous: the implementation almost certainly uses raw attention weights in Stage 1 (as described in text) and the combined score in Stage 2, but Algorithm 1 does not reflect this. The paper must be corrected with a consistent, verifiable pseudocode. *(Verifiable from: Algorithm 1 lines 2–5, line 130 text, Assumption 3.4, Table 4)*

2. **Theory–experiment gap: single-query bound vs. multi-query observation window.** The theoretical bound (Theorem 3.3) and the selection criterion (Theorem 3.5) are derived for a single query state `q` (the most recent token). However, the experimental protocol (Section 4.1) compresses the cache *before the question is introduced*, using an observation window of `n'` tokens whose attention weights are averaged (Algorithm 2). The paper provides no argument that the same bound holds when attention weights are averaged across multiple queries, nor does it discuss how the selection should be adapted. Algorithm 2 (line 8) simply calls Algorithm 1, but Algorithm 1 expects a single query `q` and recomputes attention on line 2 — it is unclear how the pre-computed averaged attention weights `Ā` are passed in. This gap weakens the claimed formal grounding of the method in the primary evaluation setting. *(Verifiable from: Theorem 3.3 derivation in Section 3.3, Algorithm 2 lines 2–3 and 8, Section 4.1 compression scenario description)*

### Minor

3. **Missing ablation isolating the value-state term.** The paper motivates its core insight by contrasting attention-weight-only selection with the proposed combined score. However, no experiment directly compares using `A` alone vs. `A · ||VW^O||₁` as the selection criterion within the proposed two-stage framework. Such an ablation would directly validate how much of the gain comes from the value-state term vs. the two-stage greedy procedure. The α ablation (Table 4) partly addresses this but does not isolate the value-state contribution cleanly.

4. **Default hyperparameter mismatch.** Algorithm 1's input list specifies α = 0.25 as default, but all experiments use α = 0.5. While minor, this inconsistency adds to the impression that the pseudocode is not carefully aligned with the actual implementation.

### Trivial

None.

## Nice-to-Haves

- A controlled experiment using only the last token as the query (rather than observation-window averaging) would help bridge the theory–experiment gap and clarify the role of multi-query averaging.
- Reporting the cost of the `VW^O` multiplication separately would help practitioners understand the overhead breakdown.
- Concrete selection examples showing which entries different scoring methods choose (e.g., a head's attention weight distribution alongside the combined score) would make the "why value norms matter" insight more tangible.

## Removed Points

- **Claim that the two-stage design is "incoherent" / "the method is not credible":** Overly strong characterization given that the text description, theoretical framework, and ablation results are all consistent with a method that uses attention-only in Stage 1 and combined scoring in Stage 2. The core issue is a **pseudocode error** (showing combined score in Stage 1) rather than an incoherent method. The method works and is described coherently in text; only the pseudocode needs correction. The claim has been demoted to a Major weakness (item 1 above) rather than treated as fatal.
- **"The paper should not be accepted in its current form":** Removed as a conclusion rather than a weakness. The assessment of acceptance is reflected in the final score.
- **Harsh critic's claim that Theorem 3.5 "does not apply" if Stage 1 uses combined score:** This is rendered moot once the pseudocode is corrected — the theory assumes attention-only Stage 1, which is what the text and implementation actually use.
- **Strength Finder's generic strengths about "addressing an important problem":** Removed as superficial. Only concrete, evidence-backed strengths are retained.
- **Criticism about missing related work:** Removed per instructions.
- **Formatting/style nitpicks and reproducibility concerns about undisclosed hyperparameters:** Removed per instructions.
- **Criticism about H2O simulation being unsupported by FlashAttention-2 / OOM:** The paper explains this clearly (Section 4.1), citing prior work's approach. Removed as a misunderstanding.

## Novel Insights

The most noteworthy finding from the review process is the empirical contradiction in Table 4: the sharp performance drop at α=0 on Mistral-7B (31.94 vs 42.85 at α=0.5) serves as *independent, unintentional evidence* that the two-stage design genuinely matters. If Stage 1 and Stage 2 used identical scoring (as the pseudocode suggests), α would be irrelevant. The fact that α has a dramatic effect confirms that the actual implementation uses a different scoring function in each stage (attention weights in Stage 1, the combined product in Stage 2), and that the safeguard of Stage 1 is critical for some models. This makes the need for a corrected pseudocode even more urgent — but it also strengthens the empirical case for the two-stage approach beyond what the paper itself argues.

## Suggestions

1. **Fix Algorithm 1** to correctly show Stage 1 selecting by raw attention weights `A` (before the element-wise product with value norms), and Stage 2 selecting by the combined score `(A + ε) · ||VW^O||₁`. Ensure the notation is unambiguous and matches the implementation.
2. **Clarify the integration path** between Algorithm 2 and Algorithm 1: how are the averaged observation-window attention weights `Ā` passed into Algorithm 1? Does Algorithm 1's line 2 get replaced with the pre-computed `Ā`?
3. **Add an ablation** comparing `A` alone vs. `A · ||VW^O||₁` within the two-stage framework to isolate the contribution of the value-state term.
4. **Add a brief discussion** (even a paragraph in Appendix) on why the single-query theoretical bound is expected to carry over to the multi-query averaged setting, or state this as a limitation.

## Score and Decision

**Overall assessment:** The paper makes a genuinely useful contribution — identifying that value states and the output projection matter for KV cache selection, formalizing this through a perturbation bound, and demonstrating large, consistent empirical gains across extensive benchmarks. However, the presentation of the core algorithm is compromised by a clear pseudocode error (showing the combined score for Stage 1 instead of raw attention weights) that contradicts both the textual description and the theoretical framework. This is a significant presentation flaw but not a fatal one: the text description, theory assumptions, and — crucially — the α ablation results are all mutually consistent and point to a well-defined method that works. The paper needs a corrected pseudocode and a clearer account of how the theoretical bound connects to the observation-window experimental setting. The empirical evidence is strong enough to warrant acceptance after these corrections.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>