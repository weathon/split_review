## Summary

LoLoRA is a LoRA variant that updates the A matrix using local unsupervised learning rules (Hebbian PCA or autoencoder) during the forward pass rather than via backpropagation, while B is trained normally with gradients. This avoids storing input activations for A's backward pass, reducing memory relative to standard LoRA. The paper provides a theoretical proof (Theorem 4.4) that PCA-based initialization of A is optimal under a random regression model, and evaluates across GLUE (RoBERTa-large), GSM8K (LLaMA-3.1-8B), LLaVA-v1.5-7B, and ablations on TinyLlama.

## Strengths

- **Theorem 4.4 provides a formal optimality proof for PCA-based A initialization that is strictly stronger than anything in prior work.** EVA (Paischer et al., 2024) showed empirically that initializing A with principal components of activations helps, but did not prove optimality. Theorem 4.4 derives that the optimal A is any nonsingular linear transformation of the top-r eigenvectors of the input covariance matrix, giving theoretical grounding to the EVA heuristic that prior work lacked.

- **The ablation study (Table 6) systematically benchmarks five local update rules across three ranks on TinyLlama.** Methods converging to the top-r PCA subspace (HPCA variants and AE) consistently outperform SoftHebb (which does not converge to that subspace), directly confirming Theorem 4.4's prediction and providing practitioners an evidence-based ranking of candidate local rules.

- **The paper evaluates across three distinct domains (NLU, math reasoning, multimodal) with consistent methodology and standard deviations over three seeds,** reducing the risk that results are specific to one architecture or task type.

- **Algorithm 1 gives a concrete, implementable recipe** showing exactly how to free the input activation memory for A (FREE_MEMORY(z)) while keeping the optimizer state for local updates, distinguishing the approach from both standard LoRA and LoRA-FA.

## Weaknesses

### Major

- **The paper's performance claims against LoRA-FA are overstated relative to the evidence.** The paper frames LoRA-FA as a "naive implementation" (line 15) and concludes that "HPCA consistently outperforms standard LoRA-FA in two out of three experimental setups" (line 332). However, the strongest LoRA-FA variant uses EVA initialization, not uniform initialization. Against LoRA-FA (EVA), LoLoRA's results are essentially tied: identical on GSM8K (0.829), slightly worse on LLaVA (1.075 loss vs 1.070), and within noise on GLUE. The ablations (Tables 5-6) show LoLoRA HPCA (2.535 at r=8) matching LoRA-FA (EVA) (2.536). The memory profile is also identical to LoRA-FA (26 GB on LLaMA-3.1-8B, Table 3) or slightly worse (24.1 GB vs 23.9 GB on LLaVA, Table 4). The abstract's claim of "further reducing the memory required for fine-tuning" is accurate only relative to standard LoRA — not relative to LoRA-FA, which is the directly relevant baseline. The paper's framing consistently implies an advantage over LoRA-FA that the data does not support.

- **The theoretical analysis (Theorem 4.4) adopts assumptions far from the practical setting, and does not specifically support the online update mechanism over static EVA initialization.** Theorem 4.4 assumes (i) each submodule is an isolated linear layer, (ii) the optimal weight change ΔW₀ is i.i.d. Gaussian, and (iii) the input distribution is stationary. In a deep transformer undergoing fine-tuning, none of these hold: layers interact, weight changes are structured, and input distributions shift as earlier layers update. The authors acknowledge this gap (line 334), but the theory justifies PCA-based A (validating EVA) without specifically supporting the claim that online local updates during fine-tuning provide additional benefit. The key unanswered question is whether online adaptation matters at all — and the evidence (LoLoRA ≈ LoRA-FA (EVA)) suggests it may not in these settings.

- **The paper does not empirically verify the core premise that A's subspace actually changes during fine-tuning or that local updates track this change.** The central argument for preferring online updates over frozen EVA initialization is that the input distribution shifts over time and A should adapt. Yet no experiment measures whether A's subspace drifts, compares the subspace learned by LoLoRA to the true top principal components over time, or tests settings where input distribution shifts are known to accumulate (e.g., multi-epoch training, domain adaptation). Without this, the motivation for the online mechanism remains unsubstantiated, and the simpler approach (LoRA-FA with EVA initialization) appears equally effective.

### Minor

- **The main experiments (GLUE, GSM8K, LLaVA) do not state the rank r used in the main text.** The ablation section uses r=2,4,8 for TinyLlama, but the main experiments defer to Appendix C (stripped by the parser). The rank is a critical experimental detail that should be in the main text.

- **The GSM8K evaluation uses best-checkpoint reporting (testing every 0.2 epochs and reporting the best).** This can differentially favor methods with different convergence patterns; reporting final accuracy or a principled early-stopping rule would be cleaner.

- **The paper does not ablate the FREE_MEMORY(z) effect.** Without running LoLoRA with activations retained, it is unclear whether any performance gap relative to full LoRA is due to the local update rule versus the absence of stored activations for A's backward pass.

### Trivial

None.

## Nice-to-Haves

- Directly test whether online adaptation matters by tracking A's subspace overlap with the true principal components during training, or by evaluating in settings with known distribution shift (multi-epoch, continual fine-tuning).
- Provide a full accounting of LoLoRA's costs: the optimizer state for A and forward-pass local update computation should be factored into memory/runtime comparisons against LoRA-FA.

## Removed Points

These points were considered during review but were removed or demoted. Treat them with caution.

**Removed from Harsh Critic:**
1. "Comparison against full LoRA is not favorable / not the right comparison" — REMOVED. The paper claims "comparable" performance to standard LoRA, which is an appropriate comparison. LoLoRA approaching full LoRA is a reasonable result, not a weakness.
2. "Theory provides little predictive value" (critic framed as fatal) — DEMOTED to Major and merged. The authors acknowledge the gap (line 334). The theory still provides value by justifying PCA-based A even if it doesn't prove the online mechanism.
3. "Missing related works" — REMOVED. Cannot confirm missing related works exist per instructions.
4. "Reproducibility concerns about hyperparameters in appendix" — REMOVED. Appendix C is stripped by the parser; these details exist in the original submission.
5. Section-by-section framing complaints — merged into the Major weakness about overclaiming.
6. "Rank values not stated" — kept as Minor, noting the appendix likely contains them.

**Removed from Strength Finder:**
1. "Table 3 demonstrates non-trivial memory-accuracy Pareto improvement" — Partially kept. The improvement over standard LoRA is real but also achieved by LoRA-FA (EVA).
2. "Evaluation across three domains" — Kept.
3. "Algorithm 1 shows how to free memory" — Kept.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Reposition the paper's narrative: the theoretical proof that PCA-based A is optimal (Theorem 4.4) is the strongest contribution and should be the central claim. The current framing overemphasizes the online mechanism, which the evidence does not show to outperform static EVA initialization.
2. State the rank for all main experiments in the main text.
3. Report final accuracy (not best checkpoint) for GSM8K, or justify why best-checkpoint reporting is unbiased.
4. Include experiments that directly verify whether A's subspace drifts during fine-tuning and whether LoLoRA's HPCA updates track this drift better than static EVA initialization.

## Score and Decision

**Calibration anchors (all rounds):**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| ALLoRA (7X65yoKl3Y) | 3.33 | R1 | Fatal flaws; LoLoRA is much stronger |
| HoLoRA (igGeaxOiFM) | 3.00 | R1 | Incremental variant; LoLoRA is stronger |
| UnoLoRA (49ti6LOUw5) | 3.00 | R1 | Multitask LoRA; LoLoRA is stronger |
| Conditional LoRA Gen (AjunxrcKa2) | 3.40 | R1 | Different approach; not directly comparable |
| **ReLoRA** (DLJznSp6X3) | **5.75** | R1 | Accepted. Stronger empirical improvement over baselines; LoLoRA is slightly weaker |
| **LoRAM** (s7DkcgpRxL) | **6.20** | R1 | More dramatic memory savings; LoLoRA is weaker |
| **LoRA-FA** (RbKThNNFxr) | **5.33** | R1 | Direct baseline, rejected for incremental novelty; LoLoRA has stronger theory but similar overclaiming — comparable |
| FLoRA (OALIb8oNfl) | 5.75 | R1 | Accepted tensor PEFT; LoLoRA is slightly weaker |
| MoRA (SxOrhLuuVz) | 4.75 | R1 | Rejected for limited improvement; comparable |
| **EVA** (DM6Q45HWSk) | **4.75** | R2 | Closest prior work (PCA-based A initialization). Criticized for lacking theory — LoLoRA addresses this but still shows marginal improvements; LoLoRA is slightly stronger |
| EigenLoRA (KxGGZag9gW) | 5.00 | R2 | Comparable quality |
| **Expressive Power of LoRA** (likXVjmh3E) | **6.50** | R2 | Pure theory, much stronger theoretical contribution; LoLoRA is weaker |
| RandLoRA (Hn5eoTunHN) | 6.00 | R2 | Stronger analysis; LoLoRA is weaker |
| dEBORA (5M0ic2RxQZ) | 6.67 | R2 | Stronger optimization contribution; LoLoRA is weaker |
| GeoLoRA (bsFWJ0Kget) | 6.25 | R2 | Stronger theory+empirics; LoLoRA is weaker |

**Round 1 bracket:** 4.5–6.0  
**Round 2 narrowing:** The paper sits between EVA (4.75, which it improves upon via theory) and ReLoRA (5.75, which has clearer empirical advantages). Taking the strongest anchor comparisons — slightly above EVA (4.75) due to the theoretical proof, slightly below ReLoRA (5.75) because the claimed performance advantage over the strongest baseline does not materialize — the appropriate score is **5.0**.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>