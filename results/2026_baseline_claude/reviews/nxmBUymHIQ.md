## Summary

LoLoRA proposes a memory-efficient LoRA variant in which the A matrix is updated via gradient-free local (Hebbian PCA / SNL) rules during the forward pass, while B is trained normally with backpropagation. This avoids storing A's input activations for the backward pass, matching the activation-memory footprint of LoRA-FA. The paper also provides a theoretical analysis (Theorem 4.4) proving that, under a random-regression assumption, the optimal A initialization is any nonsingular transformation of the top-r eigenvectors of the input covariance matrix — formally grounding the empirically motivated EVA method and motivating the proposed online PCA updates.

---

## Strengths

- **Solid theoretical contribution.** Theorem 4.4 provides the first formal proof that PCA-based initialization of A is optimal under identifiable assumptions (random iid Gaussian ΔW₀, spectral decomposition of Σ_zz). This retroactively explains why EVA works and generalizes the claim beyond empirical evidence. Theorem 4.5 (any full-rank B initialization is equivalent) is a clean complementary result that aligns with empirical findings from prior work.

- **Practical motivation is clear and well-placed.** The paper identifies a real gap: LoRA-FA (frozen A) is cheap but uses arbitrary random projections; EVA requires an offline preprocessing pass; LoLoRA can track the optimal PCA subspace online without extra data passes. The advantage is demonstrated in Table 4 (LLaVA): LoLoRA without EVA init matches LoRA-FA+EVA in perplexity while saving ~40 minutes of preprocessing wall-clock time.

- **Diverse experimental coverage.** Evaluation spans NLU (RoBERTa-large/GLUE), math reasoning (LLaMA-3.1-8B/MetaMathQA → GSM8K Platinum), and multimodal instruction tuning (LLaVA-v1.5-7B), with multiple seeds, error bars, and memory profiling. This breadth supports generalizability claims.

- **Honest, self-critical reporting.** The authors explicitly note where LoLoRA does not beat standard LoRA (GLUE, Table 1-2), where HPCA updates add no value over EVA init (Table 4), and where EVA initialization dominates. This transparency strengthens confidence in the results.

- **The ablation (Table 6) is informative.** Comparing HPCA, HPCA-no-mean, HPCA-SVD-first, AE, and SoftHebb cleanly shows that any method converging to the dominant eigensubspace performs similarly, while SoftHebb (which doesn't guarantee PCA convergence) fails. This strongly validates the theoretical claim.

---

## Weaknesses

### Fatal
None.

### Major

1. **Performance advantage over LoRA-FA+EVA is negligible across all settings.** LoLoRA's headline claim is that it combines the memory efficiency of LoRA-FA with better-than-random A projections. But LoRA-FA+EVA achieves the same memory budget and the same or better accuracy in every table: GLUE (comparable), GSM8K (tie at 82.9%), LLaVA (2.92 vs 2.93 perplexity). The only concrete advantage of LoLoRA over LoRA-FA+EVA is avoiding the offline PCA preprocessing step. This is a real benefit for streaming/continual settings but is not sufficiently emphasized or studied.

2. **The random regression assumption (Assumption 4.1) is very strong.** Assuming ΔW₀ has i.i.d. Gaussian entries with zero mean is a worst-case uninformative prior that ignores the actual fine-tuning signal. In practice, ΔW₀ is systematically low-rank and task-structured, which is precisely why LoRA works. The theorem's conclusion (PCA of input covariance is optimal) may therefore be over-reliant on this idealization. The authors acknowledge the stationarity issue but do not investigate how far the results hold under more realistic priors.

3. **LoLoRA's memory savings over LoRA-FA are zero, not a new improvement.** The paper consistently frames LoLoRA as achieving "further memory reduction" vs. LoRA (e.g., abstract, Section 5.2 summary), but Tables 3 and 4 show LoLoRA (24.1 GB) uses slightly *more* memory than LoRA-FA (23.9 GB) because of extra local optimizer state for A. The net gain vs. LoRA is the same as LoRA-FA, not larger. This framing should be corrected.

### Minor

1. The ablation benchmarks (TinyLlama/Alpaca, Table 5-6) use perplexity differences in the third decimal place (e.g., 2.535 vs 2.536). At these scales, the reported differences could be within noise despite the error bars, making it difficult to draw firm conclusions about which local rule is strictly superior.

2. The paper only applies LoLoRA to attention weight matrices (W_q, W_k, W_v, W_o). MLP projections are excluded, limiting the generality and potentially underreporting the method's memory savings in memory-dominated scenarios.

### Trivial

- The proof of Theorem 4.6 is deferred but Theorem 4.4's proof is also deferred; both are referenced as being in Appendix A which is not included. This is a parser issue per the review guidelines.

---

## Nice-to-Haves

- A streaming or continual fine-tuning experiment would be the ideal demonstration of LoLoRA's unique advantage over LoRA-FA+EVA (no offline PCA pass needed).
- Scaling to larger rank values (r=16, 32, 64) would clarify whether performance gaps widen or narrow, given the theory predicts larger gains when the eigenspectrum is imbalanced.

---

## Novel Insights

The paper's most genuinely novel insight is Theorem 4.4's formal characterization of the set of optimal A matrices as arbitrary nonsingular transformations of the top-r eigenvectors of the input covariance matrix. This is a clean analytical result that simultaneously: (a) explains why EVA outperforms random initialization in LoRA-FA, (b) explains the empirically observed A/B asymmetry, and (c) clarifies that the exact rotation within the dominant eigensubspace does not matter — only the subspace itself. The complementary Theorem 4.5 (all full-rank B initializations are equivalent) is a nice by-product. Together, these provide a more principled view of LoRA adapter design than was previously available.

---

## Suggestions

- Quantify the EVA preprocessing overhead more precisely (currently only run-time in Table 4 for one setting) and compare it explicitly with LoLoRA's per-step overhead across model sizes.
- Include an experiment where the task distribution shifts mid-training (or fine-tuning is done in multiple stages), to show whether LoLoRA's online adaptation of A actually helps vs. EVA's fixed initialization.
- Explicitly add MLP layers (W_up, W_down) to the analysis and report whether memory and performance trends hold there too.

---

## Score and Decision

The paper presents a theoretically grounded, well-executed incremental contribution to memory-efficient fine-tuning. The theoretical results (Theorems 4.4, 4.5, 4.6) are clean and genuinely useful for understanding LoRA adapter design. The experiments are comprehensive and honest. The principal weakness is that LoLoRA's practical advantage over the combination of LoRA-FA+EVA is narrow — essentially: no offline preprocessing pass needed — and this advantage is not fully exploited or highlighted experimentally. The memory savings are identical to LoRA-FA (not larger), and performance differences are within error bars in most settings. The theoretical assumptions, while standard for tractability, are fairly idealized. Overall, the paper is a solid but incremental contribution that sits at the borderline.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>