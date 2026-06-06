## Summary

This paper formally studies KV cache critical entry identification from an output perturbation perspective. Starting from the observation that prior methods rely solely on attention weights, the authors derive a perturbation upper bound (Theorem 3.3) showing that projected value norms (through W^O) also matter. They then propose a two-stage greedy algorithm that selects entries by a combined score A · ‖VW^O‖₁ and validate it as a plug-and-play add-on to SnapKV, AdaKV, and HeadKV across Llama-3.1-8B, Mistral-7B, and Qwen2.5-32B on 29 datasets, consistently cutting compression loss by more than half at 40% cache size.

---

## Strengths

- **Formal perturbation-grounded motivation (Theorem 3.3):** The paper is the first to formally bound attention output perturbation and show it depends jointly on attention weights and projected value states — directly motivating the inadequacy of attention-only heuristics. The bound in Eq. (5) is concise and interpretable.

- **Large, consistent empirical gains across 3 models, 3 methods, 29 datasets:** Figure 1 and Tables 1–2 show gains uniformly: e.g., AdaKV on Qwen2.5-32B at 40% cache improves from 24.3% Ruler loss to 0.69%; LongBench improvements hold in 88/90 tested cases. Figure 2 confirms gains persist across cache sizes from 20%–60% on both Llama and Mistral.

- **Negligible computational overhead:** The extra cost is O(n) (projecting V through W^O) and adds 0.06 s TTFT at 32K context (batch=1), with identical decoding speed, while achieving 2.49× speedup over full cache.

- **Perturbation analysis directly validates the mechanism:** Figures 4–6 confirm the method reduces actual output perturbation in 92% of Llama attention heads, that reductions accumulate across layers, and that this holds across cache budgets from 2.5% to 40% — directly connecting the theory to practice.

- **Robustness to hyperparameter α:** Table 4 shows that α=0.5 is safe across all models (especially critical for Mistral where α=0 causes a catastrophic 10-point collapse below baseline, while α=0.5 consistently beats the base method).

---

## Weaknesses

### Fatal
None.

### Major

- **Theory-algorithm mismatch in the two-stage construction.** Assumption 3.4 requires Stage 1 to select entries with the *highest attention weights* (so that σ = Σ Top_k(A, b') > 0.5), which makes the coefficient (2 − 1/σ) in Theorem 3.5 positive and meaningful. However, Algorithm 1 line 3 replaces A with the combined score `𝒜 = (A + ε) ⊙ ‖𝒱‖₁`, and both Stage 1 (line 5) and Stage 2 (line 8) then select from this combined score. Stage 1 therefore does not select by pure attention weight but by the product of attention weight and value norm. Assumption 3.4 is not guaranteed by the algorithm's design — the paper defers to Appendix A for empirical verification. As a consequence, Theorem 3.5's formal guarantee does not directly apply to Algorithm 1 as coded; it holds only approximately in practice. The empirical results are strong regardless, but the paper overstates the tightness of the theory-algorithm connection by presenting Theorem 3.5 as a formal guarantee of Algorithm 1. A corrected presentation would either (a) state a modified theorem that applies when Stage 1 uses the combined score, or (b) implement a version where Stage 1 strictly selects by pure attention weight and test whether performance differs.

- **Two-stage framing obscures algorithmic simplicity.** Because Stage 1 and Stage 2 both operate on the same combined-score pool (Stage 2 just continues from where Stage 1 left off on the remaining entries after removing Stage 1 selections), the two-stage procedure is equivalent to selecting Top-b entries by the combined score `𝒜 = (A + ε) ⊙ ‖VW^O‖₁`. The two-stage scaffolding exists to connect the simple heuristic to the formal bound, not because it produces a different selection than a single Top-b pass. This framing creates unnecessary complexity and could mislead readers into thinking the two stages are algorithmically distinct. The paper would be more transparent if it acknowledged this equivalence directly.

### Minor

- **Algorithm 1 header states α = 0.25 but the entire paper uses α = 0.5.** Section 3.5 and Section 4.1 both set α = 0.5 for all experiments; Table 4 ablates over {0.0, 0.3, 0.5, 0.7}. The inconsistency in the algorithm pseudoheader is confusing and should be corrected.

- **α = 0.5 is presented as universally safe, but α = 0.0 outperforms it on Llama.** Table 4 shows: Llama α=0.0 achieves 44.35 average vs. 43.77 for α=0.5. The paper's claim that α=0.5 is "both robust and easy to apply" is accurate only as a *safe default* (it avoids the catastrophic Mistral failure at α=0), not because it is uniformly optimal. The characterization should be more precise: α=0.5 is a conservative safe choice that avoids worst-case failures at a small cost to peak performance.

- **Independent compression is labeled "more practical" without full justification.** Section 4.1 states: "This setting better simulates practical scenarios (e.g., multi-turn QA or prefixed contexts) where multiple questions often pertain to the same context, or the question is unavailable during context compression." While this justification is reasonable, joint compression (context + query together) is the dominant setting in single-turn applications. The paper relegates the joint setting to Appendix F; given that the proposed criterion includes query-independent value norms, whether gains persist in the query-aware setting is relevant to assessing the contribution's scope.

### Trivial
- None beyond the α=0.25 header issue noted above (already listed as Minor due to paper-wide inconsistency).

---

## Nice-to-Haves

- **Ablation isolating the W^O projection from the raw value norm.** The method uses ‖VW^O‖₁ (projected value norm), but ‖V‖₁ (unprojected) is cheaper to compute and may yield similar or comparable gains. One additional ablation table would directly test whether the W^O projection is necessary, potentially simplifying deployment.

- **Extended layer-wise perturbation analysis.** Figure 5 shows that perturbation reductions accumulate across layers and nearly vanish at the final layer — a substantive observation suggesting compound benefits. Connecting this to models with large vs. small empirical gains (e.g., Llama vs. Mistral) would deepen the explanation of *why* the method works, not just *that* it works.

- **Cache-size sweep for Qwen2.5-32B on Ruler.** The paper acknowledges the prohibitive cost and omits this curve from Figure 2. Even two data points (20% and 60%) would help assess whether the dramatic AdaKV improvement (24.3% → 0.69% loss) at 40% is specific to that cache size or general.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"More than half" framing is benchmark-sensitive (Harsh Critic).** The critic argues the headline claim is specific to 40% cache / Ruler. However, Figure 1 explicitly shows both Ruler and LongBench averages at 40% cache, and the caption states "(shown at 40% cache size; see experiments for other sizes)." The paper is transparent about this. The LongBench losses (e.g., 7.48% → 3.88% for Llama SnapKV) are real reductions. The claim is accurate as stated; no verification gap. Removed as it misreads the paper's honest framing.

- **Qwen2.5-32B cache-size sweep missing (Harsh Critic).** The paper explicitly acknowledges this omission due to compute cost. The Ruler 40% results and LongBench results for Qwen are still reported. This is a compute-driven limitation, not a methodology flaw.

- **SCBench limited to one method/model (Harsh Critic).** Section 4.4 presents this as supplementary evidence ("further evaluate"), not as the primary validation. Limiting scope for supplementary experiments is standard. Removed as nitpick.

- **Strength Finder: "Important problem" and generic significance claims.** Per filtering rules, generic statements about importance are removed. Only concrete, paper-specific strengths are retained above.

---

## Novel Insights

The most genuinely novel observation in this paper — and the one most deserving of further development — is the layer-wise perturbation accumulation (Figure 5): per-head perturbation reductions at early layers compound through residual connections to produce substantially smaller hidden-state perturbations at the final layer, with the reduction approaching zero by layer 30. This suggests that even small per-head selection improvements have outsized end-to-end impact, explaining why what appears to be a minor criterion change (multiply attention weight by value norm) produces large generation quality gains. This layer-compounding insight is novel in the KV eviction literature and opens a path for theoretically grounded budget-allocation policies that prioritize selection quality in high-leverage early layers.

---

## Suggestions

1. **Fix the theory-algorithm gap explicitly.** Either (a) add a theorem that applies when Stage 1 uses the combined score, or (b) clarify that the two-stage construction is a theoretical device while the actual algorithm is Top-b(A · ‖VW^O‖₁). The Appendix A verification is necessary but not sufficient as a formal fix.
2. **Correct the α = 0.25 default in Algorithm 1's header** to match the α = 0.5 used throughout the paper.
3. **Acknowledge the two-stage → Top-b equivalence** in the algorithm description. This does not weaken the paper; it makes the method more accessible and reproducible.
4. **Reword the α = 0.5 justification** to reflect that it is a safety-first default (avoiding worst-case failure) rather than an optimal value.
5. **Add one ablation row**: ‖V‖₁ (unprojected) vs. ‖VW^O‖₁, to validate whether the output projection is necessary.

---

## Score and Decision

**Originality:** The core algorithmic change is simple (multiply by value norm), but the formal perturbation-bound framing and the theoretical insight connecting W^O to selection quality are original contributions to the eviction literature.
**Importance:** KV cache efficiency is a high-impact practical problem; a plug-and-play enhancement with this magnitude of gain is directly useful.
**Claims supported:** Empirical claims are very well supported. Theoretical claims are slightly overstated due to the theory-algorithm gap.
**Soundness:** Experiments are thorough and fair. The theoretical framework has a real but non-fatal gap.
**Clarity:** Generally clear; the α inconsistency and two-stage framing create some confusion.
**Community value:** High — directly usable by practitioners deploying cache eviction, compatible with multiple SOTA methods.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>3</clarity>
<community_value>4</community_value>
</subscores>