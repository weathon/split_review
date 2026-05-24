I have enough information. Let me now compile the final consolidated review.

---

## Summary

This paper formalizes critical KV cache entry identification as minimizing output perturbation in LLM inference. The authors derive an upper bound on the L₁ perturbation of attention output (Theorem 3.3), revealing that attention weights alone are insufficient — the projected value states (VW^O) also matter. Based on this analysis, they propose a two-stage perturbation-constrained selection algorithm that first prioritizes high-attention entries then jointly considers attention weights and value norms. Integrated as a plug-in into SnapKV, AdaKV, and HeadKV, it reduces compression loss by more than half on average across 29 datasets from Ruler and LongBench on Llama-3.1-8B, Mistral-7B, and Qwen2.5-32B. Additional head- and layer-level perturbation analyses confirm the mechanism.

## Strengths

- **Formal grounding of critical cache identification.** The paper defines the problem from an output-perturbation perspective (Definition 3.1) and derives an upper bound (Theorem 3.3) showing that attention weights alone are insufficient — the value states projected through the parameter matrix are also essential. This provides a theoretical justification that prior empirical methods (H2O, Scissorhands, SnapKV) lacked. The theoretical framing is genuinely novel for the cache eviction literature.
- **Universal and substantial empirical improvement.** When integrated with three SOTA eviction methods (SnapKV, AdaKV, HeadKV) across three LLMs, the algorithm reduces compression loss by more than half on average. For example, on Qwen2.5-32B with AdaKV at 40% cache on Ruler, loss drops from 24.30% to 0.69%; on Llama-3.1-8B with AdaKV at 40%, loss drops from 13.92% to 5.24%. Gains are consistent across 97.8% of 90 long-dependency test cases on LongBench and across varying cache budgets (Figure 2). These results are well-supported by Tables 1–2 and Figures 1–2.
- **Empirical validation of the theoretical mechanism at multiple granularities.** The paper shows that the algorithm reduces actual output perturbation in over 92% of attention heads for Llama-3.1-8B (Figure 4), that this reduction accumulates across layers to lower final-layer perturbation (Figure 5), and that it holds across cache budgets from 2.5% to 40% (Figure 6). This multi-level analysis directly connects the theoretical bound-minimization to practical behavior.
- **Negligible computational overhead.** The additional computation (L₁ norm of projected value states) adds only 0.06s to TTFT at 32K context for batch size 1 (3.54→3.60s), and decoding latency is identical to the base eviction methods (Figure 3). This makes the improvement practical for deployment.
- **Hyperparameter analysis confirms the two-stage design is necessary.** Sensitivity analysis (Table 4) shows that α=0 causes severe degradation on Mistral-7B (31.94 vs. 42.85 average), demonstrating that the two-stage split is functionally important and not a free parameter.

## Weaknesses

### Fatal
None.

### Major

1. **Algorithm pseudocode is inconsistent with the textual description and theoretical framing.**  
   The text (Section 3.4, paragraph 2) states that Stage 1 should select entries based on attention weights *alone* and Stage 2 should consider both attention weights and value norms. Assumption 3.4 formalizes Stage 1 as `Top_k(A, b')` — selecting the highest raw attention weights. However, Algorithm 1 computes a composite score 𝒜 = (A+ε) ⊙ ‖VW^O‖₁ *before either stage* and uses it for both Stage 1 and Stage 2 selection. Under this pseudocode, both stages use the same criterion, collapsing the two-stage design into a single-stage top-k on the composite score.  

   The empirical evidence (Table 4) proves that this is **not** what was actually implemented: α has a large effect on Mistral-7B (score 31.94 at α=0 vs. 42.85 at α=0.5), which would be impossible if both stages used identical criteria. The paper must present a corrected Algorithm 1 that matches the implementation and the theoretical justification. Specifically, the computation of 𝒜 = (A+ε) ⊙ ‖VW^O‖₁ should appear only before Stage 2, and Stage 1 should select on raw attention weights A.  

   **Why it matters:** This is not a minor typo — the central claim of a "formally grounded two-stage selection" depends on the stages implementing different criteria. As printed, the algorithm does not match the theory, preventing reproducibility. The results themselves appear valid (the empirical evidence is consistent across many settings), so this is a presentation/fixability issue rather than a fatal methodological flaw, but it is the most significant barrier to acceptance.

### Minor

2. **The bound analysis does not discuss tightness.**  
   Theorem 3.3 derives an upper bound θ on the output perturbation, and the algorithm is designed to minimize θ. However, the paper does not discuss how tight this bound is or whether minimizing θ reliably reduces the actual perturbation. This gap is partially addressed by the empirical perturbation analysis in Section 4.7 (Figures 4–6 show actual perturbation reduction), but a brief discussion of bound looseness would strengthen the theoretical framing.

3. **The theory is derived for a single query state, but the integration uses aggregated attention weights.**  
   The theoretical analysis (Theorems 3.3, 3.5) is developed for a single query vector q attending to the KV cache. However, the integration into SnapKV/AdaKV/HeadKV (Algorithm 2) uses mean-pooled or max-pooled attention weights over an observation window of several queries. The paper should discuss how the single-query bound translates to this aggregated setting, or at minimum acknowledge this gap. (This is noted briefly in the harsh critic's "Strengthening" section and is a reasonable point.)

### Trivial

4. **Ambiguous notation in Algorithm 1.** Line 5 reads "for all K_i, V_i ∈ K, V that A_i ∈ Top_k(𝒜, b')". Since A_i is the raw attention weight and Top_k(𝒜, b') returns composite-score values, this condition is unclear. It should be rewritten, e.g., "for all (K_i, V_i) such that the index i is among the top-b' positions by 𝒜", or more clearly as separate score-sorting steps for each stage.

## Nice-to-Haves

- Discussion of failure modes for the two-stage selection: e.g., when Stage 1 consumes too much of the budget on high-attention but low-value-norm entries, leaving insufficient budget for Stage 2 to be effective.
- A brief discussion of how the bound in Theorem 3.3 could be tightened, or conditions under which it is loose.
- Analysis of whether the selected entries differ systematically between code vs. non-code tasks (to explain the code-domain anomaly noted in Table 2), which would strengthen the already-reasonable explanation about code tasks' low dependency on long-range context.

## Removed Points

- **"Missing appendix / missing proofs / reproducibility concerns from missing code"** — Removed per hard rules. The parser strips appendix content; proof references in the text (Appendix K.1–K.3) are assumed to exist in the original submission. Code release is standard practice but not required for evaluation.
- **"Algorithm–theory misalignment invalidates the core claim"** — Demoted from "fatal" to "major". The empirical evidence (Table 4, Figures 1–2, 4–6) is too strong and too consistent across 29 datasets, 3 models, and 3 methods to conclude the method itself is invalid. The issue is that the *presented* algorithm is wrong, not that the method is wrong. The authors must fix the pseudocode, but the contribution survives.
- **"The paper does not present the correct algorithm"** — Merged into weakness #1. Handled there.
- **"Section 3.3 constant C depends on the full cache"** — This is inherent to the bound formulation and not a weakness; it is correctly stated. Removed.
- **Strength: "This paper addressed an important problem"** — Generic. Moved here.
- **Strength: "Timely motivation"** — Generic. Moved here.

## Novel Insights

The harsh critic's detection of the pseudocode inconsistency is the most valuable signal in these reviews. It is a concrete, verifiable flaw that the paper's own Table 4 exposes: if Algorithm 1 were implemented as written, α would be a dummy parameter, but Table 4 shows α matters dramatically on Mistral. This means the text description, the pseudocode, and the implementation are triply misaligned, and fixing this is the single most important revision. Beyond this, the intersection of the harsh critic's general-sounding criticisms (bound tightness, single-query-to-window gap) with the actual paper content confirms these are genuine but minor gaps that do not threaten the contribution. The strength finder's observations about the multi-level perturbation analysis (Figures 4–6) and the computational overhead (Figure 3) are well-supported and correctly identify the paper's concrete assets.

## Suggestions

1. **Rewrite Algorithm 1** to align with the textual description and the theory: compute attention weights A; Stage 1 selects top-b' by A; then compute the composite score 𝒜 = (A+ε) ⊙ ‖VW^O‖₁; Stage 2 selects top-b'' by 𝒜 from the remaining entries. Verify that the corrected pseudocode matches the actual implementation.
2. Add a brief paragraph discussing bound tightness (even a qualitative statement) and one addressing how the single-query derivation relates to the observation-window aggregation used in practice.
3. Clarify the notation in Algorithm 1 (especially the selection condition) to make the selection criterion unambiguous for each stage.

## Score and Decision

### Calibration

**Round 1 — Bracketing.** Searched for papers on KV cache eviction/pruning in the bands (0–3.5), (3.5–7.5), and (7.5–10).  
- Weak band: IntelLLM (3.0, Reject), FTP (3.0, Reject), MixAttention (2.0, Reject), PrefixQuant (3.0, Reject). These papers have unclear contributions or weak empirics. **This paper is clearly stronger** — it has a novel theory, strong empirics, and thorough analysis.  
- Mid band: KVMerger (4.33, Reject), HeadKV (6.5, Accept Poster), DynamicKV (4.4, Reject), KV Prediction (4.5, Withdrawn).  
- Strong band: FastGen (8.0, Accept Oral), Retrieval Head (8.0, Accept Oral). These are clean, well-executed papers. **This paper is weaker** because of the algorithm presentation issue.

**Initial bracket:** 4.5 – 7.5.

**Round 2 — Narrowing.** Searched more precisely within (4.5–6.5) and (5.5–7.5).  
- OmniKV (6.0, Accept Poster): Dynamic KV selection. Similar-level contribution but my paper has stronger theoretical grounding.  
- Palu (5.75, Accept Poster): Low-rank projection. My paper has stronger novelty and broader evaluation, but Palu is cleaner.  
- ShadowKV (6.75, Reject): Strong throughput gains but rejected for missing ablation and complexity concerns. My paper has a different (cleaner) evaluation story.  
- FreqKV (5.8, Reject): Frequency domain compression.  
- HeadKV (6.5, Accept Poster): Already discussed.

**Narrowed comparison:** My paper is stronger than Palu (5.75) and comparable to HeadKV (6.5) and OmniKV (6.0) in overall contribution, but the algorithm pseudocode issue prevents it from reaching HeadKV's cleanliness. It is weaker than FastGen (8.0).

**Final score: 6.0** — an Accept-level contribution (poster quality) that provides novel theoretical grounding and strong empirical evidence, with one significant but fixable presentation issue.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>