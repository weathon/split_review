Now I have all the information I need. Let me synthesize the final review.

## Summary
This paper proposes NuSA-CL, a memory-free continual learning framework for CLIP vision-language models. The method dynamically identifies an approximate null space of the model's current weights via SVD before each task, constrains all low-rank updates strictly within that subspace via a persistent constraint, and merges the update back into the backbone to maintain a fixed parameter budget. Experiments on the MTIL benchmark (11 diverse datasets) and CIFAR-100 class-incremental splits show that NuSA-CL outperforms all other storage-free methods (LoRA, MiLoRA) and achieves performance competitive with storage-based methods (MoE-Adapters, DIKI, ZSCL) while using 40× fewer parameters and 3× less training time.

## Strengths
- **Clean, memory-free design with strong empirical results.** NuSA-CL achieves Transfer 68.6%, Avg. 75.1%, and Last 82.8% on the MTIL benchmark with only 1.5M trainable parameters and zero additional storage — outperforming all storage-free baselines and rivaling storage-based methods at a fraction of the cost (Table 1). This directly validates the paper's claim of a superior efficiency-performance tradeoff.
- **The persistent constraint is demonstrably critical.** The ablation in Table 4a shows that unfreezing the null-space bases (training Uₙ, Vₙ) causes Transfer to drop from 68.58% to 62.60%, confirming that the strict, throughout-training constraint — not just initialization — is essential. Figure 3a further shows that the Tail (null-like) subspace consistently yields lower forgetting than Top or Random subspaces across all tested ranks.
- **Strong long-sequence scalability.** On the 50-step CIFAR-100 class-incremental benchmark, NuSA-CL achieves Last accuracy 71.85%, outperforming ZSCL (67.36%) by 4.49 percentage points, with the advantage growing as the sequence lengthens (Table 3). This provides convincing empirical evidence that the dynamic per-task SVD recomputation prevents spectral saturation.
- **Comprehensive efficiency and robustness analysis.** Table 1 provides clear comparisons of parameter counts, GPU memory, and training hours. Table 4b shows performance is stable across a wide range of energy cutoff thresholds (ρ = 0.80–0.999), and SVD initialization is under 1 minute per task — contrasting favorably with InLoRA's ~81 minutes of data-dependent computation.
- **Principled theoretical motivation with honest scope acknowledgement.** Lemma 1 and Theorem 2 bound parameter-space interference, and the paper explicitly acknowledges (Section 4) that these are local stability conditions rather than function-level guarantees, and defers tighter bounds to future work.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **Transfer metric protocol could be clearer.** The Transfer metric is defined as "zero-shot accuracy on unseen tasks" (Section 5.1). The paper would benefit from explicitly stating which specific task(s) are held out for Transfer evaluation, the evaluation timing (e.g., evaluated after each task and averaged), and an explanation for why Transfer can exceed the zero-shot CLIP baseline (Table 2 shows NuSA-CL Transfer 68.1% vs. zero-shot CLIP 65.3%). This improvement is a positive result — positive forward transfer from learning related tasks — but the paper does not comment on it. Clarifying the protocol and discussing the improvement would strengthen the paper without requiring additional experiments.
- **Evidence for the claimed "knowledge accumulation in null space" mechanism is suggestive but not definitive.** Figure 2 shows ~1% increases in effective rank and null ratio over 11 tasks (e.g., text encoder: 57.9% → 58.8%). While the trend is consistent, the changes are small and no error bars or statistical tests are provided. The paper's claim that NuSA-CL "actively accumulates knowledge by progressively filling this underutilized space" is plausible and consistent with the empirical results, but the spectral evidence alone does not conclusively rule out other explanations for the method's success (e.g., that orthogonal updates to principal directions suppress forgetting regardless of null-space filling). This does not undermine the paper's contribution — the method clearly works — but the exact mechanism is less tightly validated than the performance claims.
- **Task-order sensitivity is acknowledged as a limitation but not empirically characterized.** The limitations section (Section 7) mentions task-order sensitivity as future work, but the MTIL benchmark results are reported for a single task order. Given that the dynamic null-space recomputation could interact with task order, reporting results under at least one alternative ordering would strengthen the paper's robustness claims.

### Trivial
- Table 1's "Additional Storage" column could be more clearly defined. NuSA-CL does not list its training-time null-space bases (Uₙ, Vₙ), though these are discarded after merging. LoRA similarly stores low-rank matrices during training. A footnote clarifying that this column refers to permanent/ongoing storage would avoid confusion.

## Nice-to-Haves
- **Static null-space baseline.** An ablation where the null space is computed once from the initial pre-trained weights and never updated (no dynamic recomputation) would directly test whether the dynamic SVD recomputation is essential or whether a fixed projection suffices. This would further strengthen the paper's claims about the importance of task-wise recomputation.
- **Per-task forgetting breakdown.** Showing forgetting for each individual task (e.g., a per-dataset forgetting matrix) would reveal whether NuSA-CL's memory efficiency trades off against stable retention on particular datasets.
- **Larger backbone verification.** The paper focuses on ViT-B/16. Demonstrating the same trends on ViT-L would strengthen the scalability claims, though the authors note that attention projection dimensionalities remain moderate (768–1024) in larger variants.

## Removed Points
These points are flagged to be removed; treat them with caution:
- **"Zero storage overhead claim is misleading because training-time bases must be stored."** Removed because the bases are explicitly stated to be discarded after merging (Section 3.3). This is standard practice — LoRA and other PEFT methods similarly have training-time intermediates that are merged at inference. The paper's claim refers to permanent/ongoing storage.
- **"Missing comparisons with OGD, HAT, and other early orthogonal-projection methods."** Removed because OGD requires storing past gradients (not memory-free) and HAT uses per-task attention masks. The paper's baseline selection (LoRA, MiLoRA, InflLoRA, ZSCL, MoE-Adapters, DIKI) is comprehensive and appropriate for the PEFT+CLIP setting. The reviewer's suggestion of a static principal-subspace baseline is a nice-to-have, not a missing critical baseline.
- **"Small performance gap behind storage-based methods is understated."** Removed because the paper accurately describes the performance as "highly competitive" and "rivaling" — which is fair given the 40× parameter reduction, 3× speedup, and zero storage. The 2.2% gap behind MoE-Adapters is transparently reported.
- **"Calling it 'null space' is an approximation."** Removed because the paper consistently uses "approximate null space" throughout (e.g., lines 34, 82, 90, 98, 128) and the distinction is explicitly discussed. The reviewer's own note acknowledges "This is acknowledged."
- **"The bound is only in parameter space."** Removed because the paper explicitly states at line 128: "We emphasize that the above results are stated in parameter space and should be viewed as a local stability condition rather than a full function-level guarantee."
- **Strength Finder claimed strengths that conflict with verified weaknesses.** Removed one conflict: the Strength Finder claimed "Empirical evidence of knowledge accumulation via spectral dynamics" as a core strength. The effective rank changes are indeed visible, but the weakness about their small magnitude (1%) and lack of error bars is verified. The spectral evidence is retained as a supporting observation but downgraded from a "core strength."

## Novel Insights
A genuinely interesting observation from this review process is the convergence of multiple recent CL papers on SVD-based subspace analysis — KeepLoRA, OSFT, and NuSA-CL all use spectral properties of weights to guide orthogonal updates, yet each draws a different boundary: principal vs. residual (KeepLoRA), high-rank vs. low-rank (OSFT), and energy-dominant vs. null space (NuSA-CL). NuSA-CL distinguishes itself by applying the spectral constraint persistently throughout training (not just at initialization) and by dynamically recomputing the null space on the accumulating weights. The fact that persistent constraint beats initialization-only approaches (Table 4a: 68.58% vs. 62.60% when Uₙ,Vₙ are unfrozen) is a useful finding for the community — it suggests that the regime of constraint (static vs. persistent) matters as much as the direction of constraint.

## Suggestions
- Clarify the Transfer metric protocol in Section 5.1: state which datasets are held out, the exact evaluation timing, and how the average is computed. Briefly discuss why Transfer can exceed zero-shot CLIP.
- Add a static (one-time) null-space ablation to Section 6.3 to demonstrate the value of dynamic recomputation.
- Report results under at least one alternative task order for the MTIL benchmark, or provide a sensitivity analysis.
- Add error bars or confidence intervals to Figure 2's spectral measurements.

## Score and Decision

**Calibration anchors (all from ICLR 2026):**

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| KeepLoRA (T3Vc5fkTzV) | 5.50 (Poster) | Similar method (subspace-constrained LoRA for CLIP CL). NuSA-CL is slightly stronger on efficiency (1.5M vs 15.7M params) and long-sequence performance. |
| Null-Space Filtering / NUFILT (HDIf3fYqPP) | 5.50 (Poster) | Similar null-space + LoRA approach for model merging. Comparable rigor and results. |
| CNSP (NXduufyPtY) | 4.80 (Reject) | Null-space projection for prompt-based CL. Rejected for marginal improvement over prior work. NuSA-CL is clearly more novel and impactful. |
| Sculpting Subspaces / OSFT (vQcyqsGJDw) | 5.00 (Poster) | SVD-based orthogonal subspace for LLM CL. Similar methodology but different domain. Comparable quality. |
| Cross-Modal CLIP CL (mDuton6Tg7) | 3.00 (Withdrawn) | Flawed theoretical claims and weak baselines. NuSA-CL is substantially stronger across all dimensions. |
| MoRA (IyUq9NwOTS) | 4.50 (Reject) | Mixture-of-rank for CL. Rejected for unclear methodology and memory inefficiency. NuSA-CL is cleaner and more practical. |

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>