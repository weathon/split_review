## Summary

This paper presents a formal study on KV cache eviction for efficient LLM inference. The authors recast critical KV cache entry selection as an output perturbation minimization problem, derive a tractable upper bound on attention output perturbation (Theorem 3.3) that depends on both attention weights *and* projected value state norms, and propose a two-stage greedy algorithm (Algorithm 1) that minimizes this bound. The resulting drop-in selection criterion replaces the attention-weight-only heuristic in three SOTA eviction methods (SnapKV, AdaKV, HeadKV), yielding average compression-loss reductions of more than 50% across 29 datasets on three LLMs with negligible added latency.

---

## Strengths

- **Formal grounding for a previously heuristic field.** Prior cache eviction methods (H2O, SnapKV, AdaKV, HeadKV) rely purely on attention weights without theoretical justification for why this criterion is sufficient. The paper is the first to formally define a criticality criterion (Definition 3.1) and bound the resulting attention-output perturbation. Theorems 3.2, 3.3, and 3.5 are rigorous and complete, culminating in a selection objective that is provably tighter than any attention-only scheme.

- **Strong, broad empirical validation.** Results span three model families (Llama-3.1-8B, Mistral-7B, Qwen2.5-32B), 29 datasets from two well-established benchmarks (RULER and LongBench), multiple cache sizes (20%–80%), and an additional multi-turn setting (SCBench). The improvement is consistent: 97.8% of the 90 long-dependency test cases show improvement, and average compression loss is reduced by more than half. The head-wise, layer-wise, and budget-wise perturbation analyses in Section 4.7 close the loop between theory and practice.

- **Plug-and-play with negligible overhead.** Algorithm 1 requires only one additional matrix multiplication per head (projecting V through W^O), which is linear in sequence length. The measured TTFT overhead of 0.06 s at 32K context (batch 1) confirms practical deployability.

- **Rigorous robustness analysis.** Section 4.5 shows that the hyperparameter α is non-trivial (setting α=0 on Mistral collapses performance by >10 points) while α=0.5 is both theoretically justified (Assumption 3.4 is satisfied in >99% of heads) and empirically robust across all tested models.

---

## Weaknesses

### Fatal
None.

### Major

- **The combined scoring metric A_i · ‖VW^O_i‖₁ closely mirrors Wanda-style pruning scores.** The Wanda weight-pruning criterion (Sun et al., 2024b, cited in the paper) is exactly (activation norm) × (weight norm). The paper's metric is (attention weight) × (projected value norm), which is structurally identical. This analogy is mentioned only briefly in the related work and is never developed into an explicit comparison. Because this structural similarity is central to assessing the novelty of the insight, the lack of explicit discussion is a gap—readers may wonder whether the contribution amounts to "apply Wanda to KV cache," and the paper does not adequately disambiguate.

- **The two-stage design is empirically motivated but theoretically weakly justified.** Theorem 3.5 proves that stage 2 minimizes a perturbation bound *given* Assumption 3.4 (stage 1 accumulates >50% of cumulative attention weight). But stage 1 in Algorithm 1 (line 3) uses the *combined* score A (already multiplied by value norms), not pure attention weights, so Assumption 3.4's guarantee is not formally verified from the algorithm as written—only empirically (Appendix A, not included). A single-stage greedy selection by A_i · ‖VW^O_i‖₁ without the two-stage split should serve as a controlled ablation; the only relevant comparison (α=0 in Table 4) conflates the effect of the two-stage structure with the effect of the combined metric.

### Minor

- **Tightness of the bound is not analyzed.** If the gap between L (actual perturbation) and θ (bound) is large, constraining θ may not reliably constrain L. The empirical analysis in Section 4.7 partially compensates, but no tightness characterization is provided, leaving uncertainty about whether the theoretical bound is the operative mechanism or whether the empirical gains arise simply from using a better heuristic score.

- **Mistral-7B gains on RULER are noticeably weaker than for the other models.** At 40% cache, AdaKV + ours reduces loss from 55.4% to 11.6% for Mistral on Ruler, but HeadKV + ours still leaves a 26.4% loss—larger than most results for the other models. The paper does not analyze why the gains are smaller or whether the power-law attention assumption is less satisfied on Mistral.

### Trivial

- Algorithm 1 describes stage 1 as prioritizing "high attention weights" (text, line 126), but line 3 already overwrites A with the combined score before stage 1 selection; the explanation could be clarified.

---

## Nice-to-Haves

- An explicit ablation comparing (1) pure attention-weight selection, (2) single-stage combined-score selection (no two-stage split), and (3) the full two-stage Algorithm 1 would cleanly separate the contributions of the scoring metric and the two-stage design.
- A discussion connecting the bound to Wanda and explaining the conceptual difference (e.g., the softmax re-normalization effect absent in Wanda) would strengthen the novelty framing.
- Reporting actual absolute scores alongside loss percentages in Figure 1 would improve reproducibility.

---

## Novel Insights

The central insight—that the perturbation from KV cache eviction depends on the product of attention weights and the L₁ norm of projected value states (through W^O)—is genuinely useful. While analogous ideas appear in weight pruning (Wanda), their application to token-level KV cache selection under softmax normalization involves a distinct derivation (Theorems 3.2–3.3) with non-trivial interaction effects from softmax re-normalization. The layer-wise accumulation analysis (Figure 5), showing that per-head perturbation reductions compound across 30 transformer layers to produce large final-hidden-state improvements, is a practically important and underexplored finding for the cache eviction community.

---

## Suggestions

- Add a controlled single-stage ablation (select top-b entries by A_i · ‖VW^O_i‖₁ without stage splitting) to isolate whether the two-stage design, the combined metric, or both drive the gains.
- Explicitly connect Algorithm 1 to Wanda and discuss why the softmax normalization structure changes (or does not change) the optimal criterion relative to unstructured weight pruning.
- Verify Assumption 3.4 analytically or provide a tighter formal statement given that stage 1 uses the combined score rather than raw attention weights.

---

## Score and Decision

The paper formalizes an important empirical problem with sound theory, proposes a simple and effective plug-and-play algorithm, and validates it comprehensively. The main limitation is that the core novelty partially overlaps with existing pruning literature (Wanda), and the two-stage design lacks a clean ablation. Nevertheless, the gains are substantial and reproducible, the theoretical framework is new to the cache-eviction community, and the work will likely influence future research in this active area.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>