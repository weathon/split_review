Now I have a clear picture from round 2. Let me finalize the review.

**Anchor comparison summary:**

| Anchor | Score | Comparison to NuSA-CL |
|--------|-------|----------------------|
| ICL-TSVD (Round 2) | 5.50 | Our paper is clearly stronger — more novel method, better ablations, cleaner empirical story |
| PROOF (Round 1) | 5.67 | Our paper is stronger — cleaner approach, better efficiency, no expansion-based issues |
| Spectral Regularization (Round 2) | 6.25 | Comparable quality; our method is more targeted with better ablations, spectral reg. has marginal improvements |
| TiC-CLIP (Rounds 1+2) | 6.25 | Comparable; different contribution type (benchmark vs. method), both solid |
| C-CLIP (Rounds 1+2) | 6.50 | Comparable; C-CLIP has benchmark + method, our paper has more novel mechanism + better ablations |

Our paper sits slightly below C-CLIP due to the verifiable proof error in Lemma 1, but above ICL-TSVD and PROOF. **Final score: 6.0**.

---

## Summary
NuSA-CL proposes a memory-free continual learning method for CLIP-style vision-language models. Before each task, it computes the SVD of current weights, identifies the low-energy singular subspace, and constrains a low-rank weight update to lie strictly within that subspace by learning only a small r×r matrix M while freezing the basis vectors U_n, V_n. The update is merged back into the backbone after each task, maintaining a fixed parameter budget with zero external storage. Experiments on MTIL and CIFAR-100 CIL benchmarks show NuSA-CL outperforms other storage-free methods and rivals storage-based approaches at a fraction of the cost.

## Strengths
- **Clean, well-motivated method with compelling empirical validation of the core mechanism.** The subspace ablation (Figure 3a) shows that adapting in the Tail (low-energy) subspace consistently yields lower forgetting than Top or Random across all tested ranks — a direct, well-controlled validation of the central design choice. The persistent constraint ablation (Table 4a) shows that unfreezing U_n and V_n drops Transfer from 68.58 to 62.60, confirming the persistent constraint is necessary, not merely an initialization detail.
- **Superior efficiency-performance tradeoff with transparent, comparable metrics.** Table 1 provides a four-dimensional efficiency comparison alongside three performance metrics. NuSA-CL achieves 68.6 Transfer / 75.1 Avg / 82.8 Last with 1.5M params, zero additional storage, and 1.21 GPU-hours — approximately 40× fewer parameters than MoE-Adapters (59.8M) while approaching its performance, and decisively better than all other storage-free methods. LoRA-family baselines were re-implemented on the same CLIP ViT-B/16 backbone for fair comparison.
- **Null-space dynamics analysis provides direct quantitative evidence for the accumulation-over-overwriting narrative.** Figure 2 shows that while LoRA and Full-FT maintain nearly static effective rank across tasks, NuSA-CL shows a consistent progressive increase — directly evidencing that the method integrates knowledge by expanding into previously underutilized spectral directions. The spectral persistence data (313.58 null directions remain in the most saturated layer after 10 tasks, more than double r_max=128) addresses the natural concern about null-space exhaustion.
- **Long-sequence scalability validated.** On the 50-step CIFAR-100 benchmark (Table 3), NuSA-CL achieves 71.85% Last accuracy, outperforming ZSCL — a strong storage-based method — by 4.4 percentage points, with the margin growing as task sequence length increases.

## Weaknesses

### Fatal
None.

### Major
- **Mathematical error in Lemma 1's proof (Section 4.1).** The proof claims `Tr(Σ_n M) ≤ ‖Σ_n‖_2 · ‖M‖_F = σ_max^null · ‖M‖_F`. This step is not generally valid. By Cauchy-Schwarz on the diagonal entries, the correct bound is `|Tr(Σ_n M)| ≤ ‖Σ_n‖_F · ‖M‖_F`. A concrete counterexample: Σ_n = diag(10, 10), M = diag(1, 1) yields |Tr(Σ_n M)| = 20 while the claimed bound gives 10√2 ≈ 14.14. The qualitative interpretation survives under the corrected bound since ‖Σ_n‖_F is still small for low-energy singular values, and the empirical results do not depend on this bound's tightness. The proof must be corrected (or the bound restated using ‖Σ_n‖_F).
- **Parameter-count disparity confounds the LoRA comparison.** NuSA-CL trains only r² parameters per weight matrix (an r×r matrix M), while standard LoRA trains r(m+n) parameters (two projection matrices). At r=128 on ViT-B/16, this yields ~1.5M vs ~15.7M total parameters — a factor-of-10 difference. Fewer parameters naturally regularize and may reduce forgetting, making it unclear whether NuSA-CL's advantage over LoRA stems from the null-space constraint or simply from lower capacity. The MiLoRA comparison (same ~15.7M parameters as LoRA, yet NuSA-CL beats it decisively) partially mitigates this confound but does not fully isolate the effect. A parameter-matched LoRA baseline (e.g., LoRA at lower rank matching NuSA-CL's budget) would cleanly separate the constraint effect from the capacity effect.

### Minor
- **Theory section is parameter-space only and acknowledged as such.** Lemma 1 and Theorem 2 bound parameter-space inner products, not changes in predictions on previous tasks. The paper honestly acknowledges this limitation (line 122: "should be viewed as a local stability condition rather than a full function-level guarantee"). However, the section occupies space for results that are then explicitly scoped as not providing function-level guarantees, making its contribution to the paper's argument modest.
- **"Null space" terminology is imprecise.** The paper uses "null space" to describe the span of low-energy singular vectors. In linear algebra, the null space (kernel) of W is {x : Wx = 0}, not the span of low-energy singular vectors. The paper qualifies this as "approximate null space" in places, but the conflation could mislead readers. "Low-energy subspace" would be more accurate.
- **Vision-only vs. text-only modality asymmetry is unexplained.** Table 4a shows that vision-only adaptation (Transfer: 65.14) is substantially worse than text-only (68.47), which nearly matches both-modality (68.58). This interesting asymmetry is noted but left unexplained.

### Trivial
- "Ultimate form of scalability" (line 28) is rhetorical excess. The method achieves zero *additional* storage and zero *auxiliary* model load, which is genuinely strong — the language could be more precise.
- The energy cutoff ρ defaults to 0.95 (as inferred from Table 4b) but is never stated explicitly in the main text as the default value.

## Nice-to-Haves
- A parameter-matched LoRA baseline (e.g., LoRA at a rank that matches NuSA-CL's ~1.5M parameter budget) would cleanly isolate the null-space constraint effect from parameter count.
- An additional benchmark beyond MTIL and CIFAR-100 (e.g., DomainNet for domain-incremental learning) would broaden the evidence base.
- Brief discussion of what happens at extreme ρ values (ρ → 1), where the "null space" collapses and the method should degrade toward very-low-rank LoRA.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **Harsh critic: Missing discussion of EWC/SI in related work.** Removed — instructions forbid flagging missing related works, as the reviewer cannot confirm relevance from external sources. The paper's related work already covers CL+PEFT, orthogonal projection methods, and SVD-guided adaptation.
- **Harsh critic: Training details (learning rate, optimizer, batch size, epochs) absent from main text.** Removed — these are implementation details from the stripped appendix. The paper states backbone (CLIP ViT-B/16) and r_max=128, which is sufficient for understanding the method.
- **Harsh critic: Mixing re-implemented and reported numbers (ZSCL in Table 3).** Removed — ZSCL is a full fine-tuning method requiring 4 GPUs and 47 GPU-hours; re-implementing it is a large separate effort. The paper clearly marks re-implemented baselines with † and reports ZSCL from the original paper transparently. This is standard practice.
- **Harsh critic: Theory section "reads as decorative" and consumes space.** Removed as overly harsh framing. The theory provides principled parameter-space motivation; the paper correctly scopes it. The section is brief (26 lines) and does not overclaim.
- **Strength Finder: "Theoretical motivation provides a principled, though appropriately scoped, interference bound."** The strength is valid in spirit (the paper correctly scopes its theory) but is downgraded given the proof error in Lemma 1.
- **Harsh critic: Claim that the SVD step stores "the full decomposition and the basis matrices during training" as a contradiction to "zero storage overhead."** Removed — the paper clearly claims zero *additional* storage (line 28: "zero storage overhead, zero auxiliary model load, and zero parameter growth"), and the SVD basis matrices are intermediate computations, not persistent storage. This is a misreading.

## Novel Insights
The null-space dynamics analysis (Figure 2, Section 6.1) provides a genuinely novel lens on continual learning: tracking effective rank evolution across tasks as a diagnostic for whether a method accumulates knowledge in dormant spectral directions versus overwriting principal components. This is a concrete, quantifiable mechanistic explanation that goes beyond typical CL evaluations and could generalize as an analytical tool for other merge-based continual learning methods.

## Suggestions
- Correct Lemma 1's proof by replacing `‖Σ_n‖_2` with `‖Σ_n‖_F`, or provide a different derivation. The qualitative claim (null-space updates have bounded parameter-space interference) still holds.
- Add a parameter-matched LoRA baseline or explicitly discuss why the MiLoRA comparison already addresses the parameter-count confound (same capacity, worse performance).
- Either rename the "null space" to "low-energy subspace" or add a clarifying sentence distinguishing the approximate null space (low-energy singular subspace) from the algebraic null space (kernel).

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>