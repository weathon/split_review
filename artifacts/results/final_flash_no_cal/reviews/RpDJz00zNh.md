Now I have a thorough understanding of the paper and can verify the reviewer claims against the actual paper content. Let me write the consolidated review.

## Summary

The paper introduces ConciseHint, a framework for improving reasoning efficiency in large reasoning models (LRMs) by continuously injecting conciseness hints (manually designed text or learned embeddings) *during* token-by-token generation — an in-reasoning intervention paradigm distinct from the typical "before-reasoning" approaches (prompting or fine-tuning). The method adaptively controls injection intensity based on query complexity (Equation 1) and dynamically selects injection position (Equation 3) to balance accuracy, efficiency, and computational overhead. Experiments on Qwen3-1.7B/4B/8B and DeepSeek-R1-14B across GSM8K, AIME24, and GPQA-Diamond show consistent token reduction (27–49%) with minimal accuracy loss, and the method can be combined with existing efficiency techniques (BeConcise, Prompt, Deer, NoWait) for further gains.

## Strengths

- **Consistent token reduction with minimal accuracy loss across models and benchmarks.** Table 1 shows ConciseHint reduces token usage by 27–49% on GSM8K, 4–17% on AIME24, and 26–44% on GPQA‑Diamond across Qwen3‑4B, Qwen3‑8B, and DeepSeek‑R1‑14B while maintaining accuracy within 1–2 points of the original. For example, on Qwen3‑4B GSM8K, tokens drop from 2,381 to 1,213 (49% reduction) with only a 0.07% accuracy change (94.81% → 94.74%).

- **Adaptive injection intensity is shown to be necessary for complex queries.** Table 3 ablates fixed vs. adaptive intervals: a fixed small interval (64) causes catastrophic accuracy drops on AIME24 (Qwen3‑4B: 67.00% → 45.33%), whereas the proposed complexity-adaptive strategy maintains 67.00%. On easy GSM8K, fixed and adaptive are comparable. This cleanly validates the design choice.

- **Seamless integration with existing methods further pushes efficiency.** Table 1’s "Ours (baseline)" rows show ConciseHint consistently reduces tokens when applied on top of BeConcise, Prompt, Deer, and NoWait (e.g., Ours(Prompt) on Qwen3‑4B GSM8K reduces tokens from 1,263 to 839 — an additional 33.5% reduction). This demonstrates the method's flexibility as a plugin.

- **Learned hint embeddings (ConciseHint‑T) provide additional token reduction and controllability.** Table 2 shows training hint embeddings on MixChain‑Z‑GSM8K (on Qwen3‑1.7B) further reduces tokens over the manual hint (e.g., GSM8K: 1,237 → 996 at γ=0.7). Figure 3 demonstrates smooth accuracy–efficiency trade-offs via interpolation in embedding space.

- **Evaluation across multiple state‑of‑the‑art LRMs** (Qwen3‑1.7B/4B/8B, DeepSeek‑R1‑14B) and three benchmarks of varying difficulty supports generality.

## Weaknesses

### Fatal
None.

### Major

- **No control experiment for the causal mechanism.** The paper claims the hint "encourages" conciseness but does not compare against injecting irrelevant or opposite text (e.g., random tokens, "be verbose") to verify that the effect is specific to the conciseness instruction rather than a generic disruption of the generation process. While the ablations (position, interval, adaptive control) are consistent with the claimed mechanism, the lack of a simple control leaves the causal interpretation underdetermined. The core empirical result (token reduction + accuracy preservation) is not threatened, but the paper's explanatory claim is weaker than it could be.

### Minor

- **Baseline configurations are underspecified.** Deer (early exit) is described only as "terminates the reasoning when the model is confident enough" and NoWait as "prohibits transition tokens like 'wait' and 'alternatively'" — neither the confidence threshold for Deer nor the exact token suppression mechanism for NoWait is stated. This makes it difficult to assess whether these baselines are used optimally or whether the reported improvements over them (often substantial) could be artifacts of suboptimal default settings.

- **ConciseHint‑T evaluation is limited in scope.** Trained-hint experiments are conducted only on the smallest model (Qwen3‑1.7B) and trained exclusively on a GSM8K‑derived dataset. Results on larger models (Qwen3‑4B/8B, DeepSeek‑R1‑14B) are absent, so the practical utility of trained hints on stronger models is unclear. Additionally, accuracy on GPQA‑Diamond drops from 39.39% to 35.05% at γ=1.0 — a non-trivial degradation that is acknowledged but not analyzed.

- **Efficiency evaluation in the main paper relies solely on token count.** Token count is a reasonable proxy, but the main text provides no wall-clock time or FLOPs measurements; it defers cost analysis to the appendix (Section A.2) and simply states extra costs are "negligible." Since the appendix is not visible in the submission, a brief runtime comparison or prefill-cost estimate in the main paper would strengthen confidence that token reductions translate into real speedups.

- **The constant 1024 in the position formula (Eq. 3) appears without explanation.** The formula \(p = \tau_k \cdot \min((\tau_k - \alpha)/1024, 0.8)\) uses 1024 as a normalizing denominator with no stated motivation. While the paper claims insensitivity (with appendix support), the choice is unexplained in the main text.

### Trivial

- **Minor overclaim in novelty framing.** The paper states existing methods "do not directly intervene during the reasoning stage when the model generates tokens one by one." This is imprecise — Deer (early exit) and NoWait (token suppression) do intervene during generation, though via different mechanisms. The contribution is more accurately described as *continuous hint injection*, a distinct and underexplored intervention type, not a completely untouched paradigm.

- **Interesting accuracy improvements are not discussed.** ConciseHint sometimes improves accuracy (e.g., Qwen3‑4B AIME24: 64.33% → 67.00% with Ours(Ori); Qwen3‑8B AIME24: 64.67% → 69.67% with Ours(Prompt)). These increases, though modest, are worth a brief comment — they hint at possible regularization or focus benefits that could be relevant to understanding the method.

## Nice-to-Haves

- A comparison with an irrelevant/opposite-text injection (e.g., "be verbose") to isolate the causal effect of the specific conciseness instruction.
- A sensitivity plot or table in the main paper for the key formula constants (α, β, the 1024 denominator, the 0.8 cap) to confirm the claimed insensitivity.
- Wall-clock time measurements for a representative setting (e.g., Qwen3‑8B on AIME24) to validate that token reductions translate to real speedups.
- ConciseHint‑T results on at least one larger model (e.g., Qwen3‑4B) to demonstrate scalability.

## Removed Points

These points were flagged in the reviews but are treated with caution for the reasons stated:

1. **"No explanation for why injection should work" (Harsh Critic #1).** The paper explicitly provides an explanation: injecting a conciseness instruction into the autoregressive context steers the model toward shorter continuations. The paper also provides supporting evidence via ablations (position, interval) and transition-word statistics. The mechanism is intuitively clear even without a formal causal analysis. The valid residual concern (lack of random-text control) is retained as a Major weakness above.

2. **"No sensitivity analysis" for formulas (Harsh Critic #2).** The paper states that "empirical results show the performance is not sensitive to β" and explicitly references "Section A.1" for a detailed ablation of α and β. Since the parser strips appendix content, this criticism may be addressing content that exists in the original submission.

3. **"No cost analysis" (Harsh Critic #5).** The paper states that "the detailed theoretical and empirical analysis for injection costs can be found at Section A.2," which is stripped by the parser. The retained weakness above is reframed as a request for main-paper evidence rather than a claim that the analysis is missing entirely.

4. **"The dynamic position may cause near-tail degradation in later cycles" (Section-by-section notes on Table 4).** The dynamic strategy caps position at \(0.8 \cdot \tau_k\), which is materially different from the "at the tail" condition (position ≈ \(\tau_k\)) that caused catastrophic drops. The paper's position ablation does not isolate this specific concern, but the cap provides a plausible safety margin. This is a reasonable question but not a confirmed weakness.

5. **Various generic or speculative concerns** about Deer/NoWait being "training-free" methods when the paper already classifies them as such, and about the method potentially being "brittle" — these are speculation not anchored to specific evidence in the paper.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a genuinely novel observation about the method or results that was not already present in the paper.

## Suggestions

1. Add a simple control experiment: replace the concise hint with an irrelevant phrase (e.g., "the sky is blue") or an opposite instruction (e.g., "be verbose") and report token counts and accuracy. This would substantially strengthen the causal claim.
2. Provide brief wall-clock timing data for a representative configuration (e.g., Qwen3‑8B on AIME24 or GPQA‑Diamond) to validate that token reductions translate to real speedups.
3. Expand ConciseHint‑T to at least one larger model (e.g., Qwen3‑4B) to demonstrate that learned hints provide value beyond the manual hint on stronger backbones.
4. Include a short sensitivity table in the main text for the key constants (α, β, the 1024 denominator, the 0.8 cap) rather than deferring entirely to the appendix.
5. Specify the Deer confidence threshold and NoWait token-suppression details used in experiments to improve reproducibility.

## Score and Decision

**Score:** 7.0  
**Decision:** Accept

**Rationale:** The paper presents a simple, well-motivated, and empirically effective method for improving reasoning efficiency. The core idea — continuous in-reasoning hint injection — is clearly novel relative to the dominant before-reasoning paradigms. The experiments are thorough in terms of model variety (4 LRMs), benchmark coverage (3 datasets of varying difficulty), and ablations (interval, position, integration with existing methods). The main weaknesses (lack of causal control experiment, underspecified baselines, limited training-variant evaluation, no wall-clock measurement) are real but addressable and do not undermine the core empirical contribution. The method's simplicity and demonstrated compatibility with existing techniques make it practically useful. A score of 7.0 reflects a solid conference contribution with clear strengths and identifiable but non-fatal gaps.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>