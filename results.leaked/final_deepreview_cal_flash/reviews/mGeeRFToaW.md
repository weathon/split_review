Now I have a good calibration. Let me finalize my assessment.

The most comparable anchor is SensZOQ (5.80, accepted) — same problem of ZO + quantization for LLM fine-tuning. QZO has a more novel core idea (perturbing scales rather than masking weights) but suffers from a more significant evaluation gap (no variance reporting across multiple runs, which is necessary for stochastic ZO methods). The other anchors — Sparse MeZO (5.50, rejected), SubZero (4.25, rejected), QR-Adaptor (5.40, rejected) — are all in the 4-6 range with similar concerns about novelty, evaluation scope, or missing baselines. LOZO (7.00, accepted) is a stronger paper with rigorous theory and more comprehensive evaluation that QZO doesn't match.

I'll place QZO at 5.0 — solid core idea, promising results, but the evaluation gaps (especially no variance reporting) are significant enough to warrant a major revision.

Now let me produce the final review.

## Summary

The paper proposes QZO, which enables zeroth-order optimization on quantized LLMs by pertubing continuous quantization scales rather than discrete quantized weights. This yields dramatic memory savings (3× over MeZO, 18× over full-precision AdamW) while maintaining competitive performance on five NLP tasks across multiple model families (OPT, Llama-2, Llama-3) and quantization schemes (GPTQ 4-bit, AQLM 2-bit).

## Strengths

1. **Clever and original core idea** — Perturbing the quantization scale (continuous) rather than the discrete weights elegantly sidesteps the fundamental incompatibility between ZO's continuous perturbations and quantized discrete weights. This is conceptually clean and practically effective (Sec 3.2.1, Definition 3.3).

2. **Dramatic and well-documented memory reduction** — Figure 1/Table 1 consistently shows QZO using 3× less memory than MeZO and 18× less than full-precision fine-tuning across three 7B-level models (e.g., Llama-2-7B: 5.0 GB vs MeZO's 14.8 GB). The memory profiling methodology (first 100 steps, batch size 1) follows the convention set by MeZO.

3. **Compatibility with multiple PTQ methods** — Works with both scalar-based GPTQ (4-bit, Table 1) and codebook-based AQLM (2-bit, Table 3), demonstrating generality beyond a single quantization approach. This is a real strength given the paper's claimed orthogonality to PTQ methods.

4. **DDC ablation convincingly demonstrates necessity** — Figure 2 shows clear training collapse (NaN loss within 22 steps) without DDC, while DDC keeps directional derivatives and loss stable. The threshold sensitivity analysis (Figure 3) shows robustness for C ≥ 75.

5. **FLOPs and parameter count analysis** — Table 2 shows QZO uses ~1% of the trainable parameters and ~0.1–10% of the FLOPs of MeZO, quantifying the computational efficiency gains.

6. **Publicly released code and reproducibility statement** (Sec 7).

## Weaknesses

### Major

1. **No variance reporting across multiple runs** — All results in Tables 1 and 3 are single numbers without standard deviations or indication of multiple random seeds. Zeroth-order optimization is inherently stochastic — the perturbation seeds, data sampling, and SGD noise all introduce variation. Without confidence intervals, mixed results (e.g., Llama-3.1-8B on CB: QZO 69.6 vs MeZO 91.1; Llama-2-7B on SQuAD: QZO 85.5 vs MeZO 80.7) cannot be interpreted as reliable differences. The MeZO paper (Malladi et al., 2023) reported results over three seeds, setting a precedent this paper does not follow. This gap undermines the central claim that QZO "performs on par with MeZO."

### Minor

2. **DDC unbiasedness claim (Theorem 1) is questionable without stronger assumptions** — Clipping the directional derivative d to [-C, C] generally introduces bias unless the distribution of d satisfies strong symmetry/zero-mean-tail conditions. The proof is deferred to the appendix (stripped by the parser), so we cannot verify it from what is on the page. The empirical evidence for DDC's effectiveness (Figure 2) is clear and valuable regardless, so the paper should either provide a rigorous unbiasedness proof or reframe the theoretical contribution as a variance-reduction heuristic with bounded bias (which the ablation already supports).

3. **Missing comparison with QLoRA as a memory-efficient fine-tuning baseline** — The paper aims at "pushing the limits of memory-efficient training" but does not compare with or discuss QLoRA (Dettmers et al., 2023) in the experiments, despite citing it. QLoRA fine-tunes low-rank adapters on a 4-bit base model with backprop, achieving a comparable ~5–6 GB memory footprint for 7B models. A direct comparison would clarify QZO's practical advantages (no adapter tuning, simpler pipeline) or disadvantages (accuracy gap, convergence speed).

4. **Memory comparison partly confounded by different parallelism strategies** — Figure 1's caption states "Fine-tuning w/ AdamW is done with fully-sharded data parallel" while other methods presumably are not. This means the 18× reduction headline partly reflects different distribution strategies, not just the algorithmic differences. The SGD baseline (no FSDP) at 26.8 GB vs QZO's 4.8 GB = 5.6× gives a more direct comparison. The paper should report all methods under consistent parallelism settings or provide a clear breakdown of what contributes to each memory number.

5. **Imprecise notation in variance derivation (Eq. 8)** — The derivation writes Var[∇̂′] = 𝔼[‖∇̂′‖²] − 𝔼[‖∇̂′‖]² where it should use ‖𝔼[∇̂′]‖² (norm of expectation, not expectation of norm). This confuses the definition of variance for vector-valued random variables. The intuitive conclusion (variance reduction from d'² ≤ d²) likely still holds under the unbiasedness assumption, but the derivation as written is technically incorrect.

### Trivial

6. Minor presentational issues: "Var[∇̂′] ≤ Var[∇̂] holds almost surely" is an odd phrasing since variance is a deterministic number, not a random variable.

## Nice-to-Haves

- An ablation that separates the effect of quantization from the reduction in parameter count: e.g., MeZO applied to only the scales of a full-precision model vs QZO applied to the same scales of the quantized model. This would isolate how much of QZO's performance is due to the quantization-aware perturbation vs simply solving a lower-dimensional problem.
- Training curves showing convergence behavior over 20k steps, and whether QZO saturates or could benefit from longer training.
- A memory breakdown table specifying exactly what is stored in GPU (weights, perturbation vectors, activations, quantization metadata) for each method.
- Ablation on alternative 4-bit PTQ methods (e.g., AWQ, QuIP) to strengthen the orthogonality claim.
- Multiple runs for the DDC threshold sensitivity plot (Figure 3).

## Removed Points

These points were flagged by the harsh critic or strength finder but are removed with justification:

- **"Unfair comparison with MeZO due to parameter count asymmetry"** — Removed. The fact that QZO updates fewer parameters (scales only) is a feature of the design, not a confound. The system-level comparison (QZO on 4-bit scales vs MeZO on 16-bit weights) is exactly the relevant comparison for evaluating memory-efficient fine-tuning methods.
- **"The Fine-tuning upper bound underperforms relative to typical published numbers"** — Removed. This is speculative without evidence; the fine-tuning numbers use SGD (not AdamW) due to budget constraints, and the paper clearly states this.
- **"The big gap on CB for Llama-3.1 (MeZO 91.1 vs Fine-tune 62.5) is suspiciously high"** — Removed. Without variance reporting, this is speculation. The concern about missing variance is already captured in Weakness #1.
- **Generic concerns about "degrees of freedom are very limited" for scale-only fine-tuning** — Removed. This is speculation about what kind of adaptation is possible; the empirical results demonstrate that scale-only fine-tuning works across tasks.
- **"Missing hyperparameters for MeZO"** — Removed. The paper states MeZO uses the official code and defaults, which is standard practice.
- **Strength Finder strengths that conflict with verified weaknesses** — The strength about "theoretical variance reduction via DDC" is partially undermined by Weakness #2 (the unbiasedness claim is questionable). The empirical component of this strength is retained; the theoretical claim is weakened.

## Novel Insights

None beyond the paper's own contributions. The key insight — perturbing quantization scales rather than discrete weights to enable ZO on quantized models — is the paper's own contribution and is novel.

## Suggestions

1. **Run all experiments over at least 3 random seeds and report means with standard deviations.** This is the single most impactful improvement and is essential for a stochastic ZO method.
2. **Add QLoRA as a baseline** for memory and performance comparison, even if only for the 4-bit 7B models.
3. **Reframe Theorem 1** as a heuristic variance-reduction technique with bounded bias, or provide a rigorous unbiasedness proof with explicit assumptions.
4. **Clarify the memory measurement setup**: specify the parallelism strategy used for each method, provide a component-wise memory breakdown, and report the 5.6× savings vs SGD (no FSDP) alongside the 18× headline number.
5. **Fix the notation in Eq. 8**: use ‖𝔼[∇̂]‖² rather than 𝔼[‖∇̂‖]² for the variance definition.

## Score and Decision

Round-1 bracket: Between 4.0 and 6.0 based on calibration search.

Round-2 anchors used for narrowing within this bracket:
- SensZOQ (myYzr50xBh) — avg 5.80, accepted. Most directly comparable (ZO + quantization for LLMs). QZO has a more novel core idea but weaker evaluation standards (no variance reporting, which SensZOQ's reviewers did not flag as a major issue). QZO is weaker than this anchor.
- Sparse MeZO (4Kw4KAoVnx) — avg 5.50, rejected. Similar topic (ZO fine-tuning with sparsity). QZO has a more novel core idea (perturbing scales vs masking weights) and broader experiments. QZO is slightly stronger than this anchor.
- QR-Adaptor (zcx6rIMbbR) — avg 5.40, rejected. Quantized fine-tuning with a different approach. Similar evaluation breadth. QZO is approximately comparable to this anchor.
- SubZero (FK6T0U4Mg1) — avg 4.25, rejected. Random subspace ZO. Limited novelty and narrow experiments. QZO is clearly stronger than this anchor.
- LOZO (9BiVepgmWW) — avg 7.00, accepted. Low-rank ZO with strong theory and comprehensive evaluation. QZO is weaker than this anchor.

Final positioning: The paper has a genuinely clever core idea and clear memory savings, but the evaluation gaps (especially the complete absence of variance reporting) keep it from being a strong accept. It is between Sparse MeZO (5.50) and SensZOQ (5.80), closer to the lower end. Score: 5.0.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>