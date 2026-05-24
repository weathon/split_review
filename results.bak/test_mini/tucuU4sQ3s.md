Now I have all the information I need. Let me synthesize the final review.

---

## Summary

This paper proposes NuSA-CL, a memory-free continual learning method for vision-language models (specifically CLIP) that constrains task-specific low-rank updates to lie within an approximate null space of the model's current weights. The null space is identified via SVD by retaining only low-energy singular directions (the complement of the top-k principal components capturing ρ fraction of spectral energy). The update ΔW = U_n M V_n^T ensures orthogonal updates in parameter space, and after each task the update is merged into the backbone, keeping model size fixed. On the MTIL benchmark, NuSA-CL achieves 68.6% Transfer, 75.1% Avg, and 82.8% Last — the best among all storage-free methods — using only 1.5M trainable parameters with zero persistent storage and minimal training cost.

## Strengths

1. **Elegant, principled method for memory-free CL.** The persistent null-space constraint (ΔW = U_n M V_n^T with frozen U_n, V_n) is a clean and theoretically motivated design. Unlike prior subspace-initialization approaches (e.g., MiLoRA) that allow updates to deviate, the persistent constraint is mathematically guaranteed to produce updates orthogonal to the principal subspace. The ablation in Table 4a confirms this is critical: unfreezing U_n, V_n drops Transfer from 68.58% to 62.60%.

2. **Impressive efficiency–accuracy tradeoff versus storage-based methods.** NuSA-CL uses 40× fewer parameters than MoE-Adapters (1.5M vs. 59.8M), less than half the peak GPU memory (6.6 GB vs. 15.5 GB), and 2.8× less training time (1.21 vs. 3.42 GPU-hours), yet achieves nearly matching performance (Transfer 68.6 vs. 68.9, Last 82.8 vs. 85.0). This concretely demonstrates that a memory-free approach can rival expensive storage-based methods.

3. **Strong empirical evaluation across settings.** The paper evaluates on three regimes: the full-shot MTIL benchmark (11 datasets), the challenging 5-shot MTIL benchmark, and the class-incremental CIFAR-100 benchmark with up to 50 steps. The 5-shot results are particularly convincing — NuSA-CL decisively outperforms InflLoRA (Avg 70.3% vs. 68.9%) despite InflLoRA using additional gradient projection memory. The long-sequence CIFAR-100 results show the advantage grows with task count (71.85% Last vs. 67.36% for ZSCL at 50 steps).

4. **Well-designed ablations validate core design choices.** The subspace selection ablation (Tail vs. Top vs. Random) cleanly shows that low-energy directions yield consistently lower forgetting at every tested rank (e.g., 2.57% vs. 4.44% vs. 4.57% forgetting at r=128). The update rank ablation reveals a clear stability-plasticity trade-off maximized at r=128. The core mechanism ablations (Table 4a) cleanly isolate the contributions of the persistent constraint and multimodal adaptation.

## Weaknesses

### Major

1. **No variance reporting across multiple runs.** All main results (Tables 1, 2, 3) are reported as single numbers without error bars or standard deviations. With 11 datasets and multiple method comparisons, run-to-run variance is non-negligible. This is the most significant empirical gap: it is impossible to determine whether reported differences between NuSA-CL and close competitors (e.g., InflLoRA on several metrics, or the 0.3% gap to MoE-Adapters on Transfer) are statistically meaningful. The paper should report at minimum 3 seeds with mean ± std for the main tables.

### Minor

2. **The "knowledge accumulation" spectral analysis is oversold relative to the evidence.** Figure 2 shows effective rank changes of ~0.9% (text encoder: 57.9%→58.8%) and ~0.6% (vision encoder: 51.8%→52.4%) across 10 tasks. The paper frames this as "active accumulation" and "consistently increasing" utilization of underused spectral directions. The claimed trend is directionally consistent, but the magnitude is extremely small — for a d=768 layer, 0.6% corresponds to ~4.6 dimensions out of 768. The paper provides no error bars, confidence intervals, or statistical tests, and this level of change is within the range that could arise from random fluctuation. The authors should either (a) provide multi-seed evidence with CIs, (b) show that singular values within the null space themselves grow across tasks, or (c) temper the claims. This analysis is a nice-to-have insight that the paper over-relies on; the core contribution does not depend on it.

3. **The theoretical motivation (Section 4) is accurately scoped but largely intuitive.** Lemma 1 bounds |⟨W, ΔW⟩_F| ≤ σ_{k+1}·‖M‖_F, and Theorem 2 sums this across tasks. The paper explicitly acknowledges these are "parameter space" bounds and "a local stability condition rather than a full function-level guarantee." This is appropriately modest, but the section ends up providing limited formal insight beyond what can be inferred directly from the construction: if updates are confined to low-energy directions, their overlap with prior weights is small. The theory is clean but does not tighten the connection to actual forgetting in function space.

4. **"Memory-free" and "zero additional storage" framing could be more precise.** The paper uses "memory-free" and "zero additional storage" to contrast against methods that require persistent task-specific modules or replay buffers. This is a fair distinction — NuSA-CL merges all updates and requires no persistent storage beyond the backbone weights. However, the SVD computation produces U_n and V_n bases that occupy GPU memory during training (e.g., 768×128 each per layer for r=128). While these are temporary and comparable to what any SVD-based method would need, the absolute claim "zero additional storage" conflates temporary computation buffers with persistent additional storage. This is a minor presentation issue; the substantive advantage (no persistent storage growth) should be the focus.

### Trivial

- The term "null space" is technically imprecise — the subspace spanned by (U_n, V_n) is a low-energy subspace, not the mathematical null space of W. The paper acknowledges "approximate null space" occasionally but mostly uses "null space" alone.
- The "-" entries for the Aircraft column in Table 2's Transfer row are never explained. Since Transfer is defined as "zero-shot accuracy on unseen tasks," it is understandable that the first task has no meaningful Transfer value, but this should be stated explicitly.

## Nice-to-Haves

- Quantifying the actual singular value spectrum decay (σ_{k+1} values) for CLIP's attention projections would strengthen the theoretical motivation by making concrete how small σ_{\max}^{null} actually is at ρ=0.95.
- A brief discussion of per-task breakdowns (e.g., each task's forgetting curve across the sequence) would be informative.
- Analysis of sensitivity to task order would strengthen claims about robustness.

## Removed Points

- **Weakness about InflLoRA re-implementation (from harsh critic):** The paper states it was re-implemented "on the CLIP architecture for fair comparison" — the critic's request for more detail is reasonable but is a reproducibility concern standard for conference papers, not a substantive weakness. The main results of the paper don't depend on the precise InflLoRA implementation (the comparison is directional).
- **Weakness about theoretical bound's cumulative nature (from harsh critic):** The critic claimed "the cumulative bound does not control interference with the earliest tasks — only with the weights as they existed right before each update." This is factually incorrect: W_{t-1} encodes all past knowledge (since all previous updates have been merged), so interference with W_{t-1} captures interference with the complete accumulated knowledge. The bound does control cumulative interference.
- **Several generic "could be" speculations (from harsh critic):** Claims about "run-to-run variance could be significant" without evidence, concerns about potential saturation under "extreme lifelong settings" without showing evidence of the problem. These are speculation, not verified problems.
- **Strengths about "addressing an important problem" and "well-written" (from strength finder):** Generic statements that any paper could claim. Removed per filtering rules.
- **Criticisms about missing appendix content:** The appendix was stripped by the PDF parser. Per instructions, assume it exists in the original submission.
- **Criticism about "null space" terminology being technically incorrect:** While factually correct, this is a trivial terminology choice acknowledged by the paper, not a substantive issue.

## Novel Insights

None beyond the paper's own contributions. Both the harsh critic and strength finder converged on the paper's stated contributions without adding a genuinely novel perspective that the paper itself missed.

## Suggestions

- Report all main results (Tables 1, 2, 3) with at least 3 random seeds and standard deviations.
- Either strengthen the spectral accumulation evidence (multi-seed CIs, showing singular value changes directly) or reframe the "accumulation" narrative as speculative.
- Clarify that "zero additional storage" refers to persistent/post-training storage, acknowledging that temporary SVD bases exist during training (as they do for other PEFT methods).
- Add a brief footnote explaining the "-" entries in Table 2's Transfer row.

## Score and Decision

**Calibration details:**

Round 1 bracketing (score ≤3.5; 3.5–7.5; ≥7.5) placed the paper in the middle band. Relevant anchors:
- KeepLoRA (T3Vc5fkTzV.md, avg 5.50, Accept Poster) — Closest comparable paper: same CLIP+MTIL setting, similar subspace-constraint framing. NuSA-CL has a cleaner method (direct reparameterization vs. gradient projection), better efficiency, and stronger ablation analysis, but shares the limitation of no variance reporting. **NuSA-CL is slightly stronger overall.**
- NUFILT (HDIf3fYqPP.md, avg 5.50, Accept Poster) — Null-space filtering for model merging (related technique, different setting). Comparable quality but different problem.
- OSFT (vQcyqsGJDw.md, avg 5.00, Accept Poster) — SVD + orthogonal updates for LLM continual learning. More complex, some fairness concerns. **NuSA-CL is cleaner and better evaluated.**
- HippoTune (MtDiLnnYgm.md, avg 6.50, Accept Poster) — Bio-inspired iterative retrieval, strong results but more complex and narrower evaluation. **NuSA-CL is comparable in quality but less novel architecturally.**
- CNSP (NXduufyPtY.md, avg 4.80, Reject) — Null-space projection for prompt-based CL. Marginal improvements over prior work. **NuSA-CL is clearly stronger.**
- Adaptive Rank LoRA (uqoKr4m8hl.md, avg 5.00, Reject) — CLIP + LoRA rank analysis. Similar evaluation but rejected. **NuSA-CL is substantially stronger.**

Round 1 bracket: [5.0, 6.5]. Round 2 narrowing placed NuSA-CL above KeepLoRA (5.50) and OSFT (5.00) but below HippoTune (6.50), settling at 6.0.

The paper presents a clean, well-motivated method with strong empirical results and compelling efficiency advantages. The main empirical gap (missing variance) and the oversold spectral analysis are real issues but do not invalidate the core contribution, which is independently supported by multiple ablation studies and consistent performance across benchmarks.

**MY FINAL SCORE: <score>6.0</score>**
**MY FINAL DECISION: <decision>Accept</decision>**