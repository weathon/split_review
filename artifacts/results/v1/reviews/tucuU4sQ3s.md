Now I have all the information I need. Let me synthesize the review, carefully cross-checking each claim.

## Summary

This paper proposes NuSA-CL, a memory-free continual learning method for vision-language models that constrains low-rank weight updates to the low-energy (tail) subspace of current weight matrices, identified via SVD. The method is cyclically applied: SVD to identify the null space, constrained adaptation within that space, and weight merging. The core idea is clean, well-motivated, and addresses a genuine scalability bottleneck in continual learning for foundation models. Experiments on the MTIL benchmark (11 tasks) show strong performance against storage-free PEFT baselines, and results on CIFAR-100 (up to 50 steps) demonstrate scalability to longer sequences.

## Strengths

- **Superior efficiency–performance tradeoff (Table 1).** NuSA-CL achieves 68.6% Transfer, 75.1% Avg, and 82.8% Last accuracy on the MTIL benchmark using only 1.5M trainable parameters, zero additional storage, 6.6 GB peak GPU memory, and 1.21 GPU-hours — a 40× parameter reduction and ~3× speedup over comparable storage-based methods. The advantage over LoRA (63.9% Transfer) and MiLoRA (62.8%) is substantial and directly validates that the null-space constraint provides a real benefit beyond mere parameter efficiency.

- **Subspace selection ablation confirms design choice (Figure 3a).** Across all tested ranks, constraining updates to the tail (null-like) subspace yields consistently lower forgetting (e.g., 2.57% vs. 4.44% for Top at r=128). This directly validates the core hypothesis that low-energy directions provide lower interference for continual updates.

- **Persistent constraint is critical to performance (Table 4a).** Unfreezing the null-space bases (Uₙ, Vₙ) causes Transfer to drop from 68.58% to 62.60%, confirming that the strict orthogonality constraint — not merely subspace initialization — is essential. This cleanly distinguishes NuSA-CL from prior SVD-based adaptation methods (e.g., MiLoRA) that use low-energy subspaces only for initialization.

- **Strong 5-shot results (Table 2).** Under data-limited 5-shot evaluation, NuSA-CL achieves 68.1% Transfer vs. 66.8% for InflLoRA (which uses gradient projection memory) and 60.4% for LoRA, demonstrating that the null-space constraint is particularly beneficial when data is scarce.

- **Effective on long task sequences (Table 3).** On the 50-step CIFAR-100 split, NuSA-CL achieves 71.85% Last accuracy, outperforming ZSCL (67.36%) by 4.4%. This provides evidence that the dynamic null-space recomputation strategy does not saturate over long sequences.

## Weaknesses

### Fatal
None.

### Major
- **Missing PEFT baselines on the CIFAR-100 class-incremental benchmark (Table 3).** Table 3 compares NuSA-CL against full fine-tuning methods (Continual-FT, LwF, ICaRL, LwF-VR) and ZSCL, but does *not* include LoRA, MiLoRA, or InflLoRA — the same PEFT methods compared on the MTIL benchmark. Since the paper specifically frames the CIFAR-100 experiments as testing "long-sequence scalability" and the advantage of the null-space constraint, the absence of these baselines weakens the claim that NuSA-CL's benefit over naive PEFT persists as task count grows. Without these numbers, the possibility that standard LoRA (or MiLoRA) would also perform well on CIFAR-100 at 50 steps cannot be ruled out. This is a concrete omission affecting the completeness of the evaluation; it does not invalidate the MTIL results but limits the support for the long-sequence claim.

### Minor
- **Ambiguous definition and reporting of the Transfer metric (Table 2 and Section 5.1).** Transfer is defined as "the zero-shot accuracy on unseen tasks" without specifying the aggregation protocol. In Table 2, the Transfer row excludes Aircraft (the first task) for all methods, while the zero-shot CLIP baseline row includes it — yet the paper does not explain this discrepancy or state the exact evaluation procedure (e.g., for each task, evaluate on all future tasks, then average). A reader cannot reproduce the reported Transfer numbers without inferring the protocol from prior work. The relative ordering of methods is unlikely to change, but the lack of clarity undermines reproducibility.

- **Over-interpretation of spectral dynamics (Section 6.1).** The paper claims a "clear and consistent increase" in effective rank for NuSA-CL, implying active and meaningful expansion into null-space dimensions. However, the actual changes shown in Figure 2 are small (effective rank from ~57.9% to ~58.8% for the text encoder; ~51.8% to ~52.4% for the vision encoder — absolute increases of 0.6–0.9% over 11 tasks). While the trend is indeed consistent and contrasts with the flat behavior of LoRA/Full-FT, the magnitude is modest enough that describing it as "progressive utilization" and a "fundamental divergence" overstates the evidence. The more defensible and still interesting finding is that the null ratio does *not* collapse, meaning the null space remains usable after many tasks. The text should be revised to avoid over-claiming.

- **Writing quality / clarity issues.** The paper uses "InflORA" in tables but "InflLoRA" in text (the correct name per the cited paper is "InflLoRA"). The SVD efficiency comparison reports "InLoRA ~81 min" in Table 4b without specifying hardware, number of layers decomposed, or what the 81 minutes covers (total across all tasks? per task?). The parameter counts in Table 1 show NuSA-CL at 1.5M vs. LoRA at 15.7M with "consistent rank" — the difference is mechanically because NuSA-CL's M matrix has r² parameters per layer vs. LoRA's r·(m+n), which should be explained for clarity rather than left implicit.

### Trivial
- Figure 2 axis labels are small and the 0.6–0.9% changes are barely visible without close inspection.
- The paper uses both "InflLoRA" and "InflORA" inconsistently.

## Nice-to-Haves
- The paper would benefit from adding LoRA, MiLoRA, and InflLoRA baselines to the CIFAR-100 experiments (Table 3) to complete the evaluation.
- No standard deviations or multiple seeds are reported; while single-run evaluation is standard practice in this benchmark suite, adding a note about stability (or running 2–3 seeds for a representative subset) would strengthen the evidence.
- A brief decomposition of the SVD initialization cost (per-layer time, number of layers decomposed) would help readers assess scalability to larger backbones.

## Removed Points
- **"SVD initialization 81 minutes seems implausible"** — This is the reviewer's incredulity about a reported number, not a paper weakness. InLoRA's data-dependent gradient projection computation on 11 tasks' worth of data is plausibly expensive, and the paper provides the comparison in good faith. REMOVED.
- **"The paper frames 'minimizing interference' suggesting a stronger guarantee than the parameter-space bound provides"** — The paper explicitly states: "We emphasize that the above results are stated in parameter space and should be viewed as a local stability condition rather than a full function-level guarantee." The concern is preemptively addressed. REMOVED.
- **"Rank used for baselines should be reported; fairness of comparison uncertain since parameter counts differ"** — The paper states "consistent rank" was used. The parameter count difference (NuSA-CL 1.5M vs. LoRA 15.7M) is an *inherent consequence* of the different parameterization (r² vs. r·(m+n)), not evidence of different ranks. The comparison is structurally fair. REMOVED.
- **"Energy threshold ρ=0.95 may not be optimal across layers/tasks"** — Table 4b demonstrates robustness across ρ ∈ [0.80, 0.999]; Transfer varies by <1%. The concern is empirically addressed. REMOVED.
- **"No standard deviations"** — Downgraded to Nice-to-Have; single-run evaluation is standard for deterministic CL benchmarks on these datasets.

## Novel Insights

The reviews surface few observations beyond the paper's own contributions. The most notable is the fine-grained point about metric definition: the paper's framing of Transfer as "zero-shot accuracy on unseen tasks" without specifying the aggregation protocol or explaining why Aircraft is excluded from the Transfer row (Table 2) is a genuine clarity gap that could mislead readers. The spectral dynamics discussion also benefits from the scrutiny that the reported changes are very small in absolute terms, a nuance that the paper's prose smooths over. However, these are refinement-level observations rather than transformative insights.

## Suggestions
1. **Complete the CIFAR-100 evaluation by adding LoRA and MiLoRA baselines** to Table 3. This directly addresses the most significant gap and would solidify the long-sequence scalability claim.
2. **Clarify the Transfer metric definition** in Section 5.1: state the exact protocol (e.g., "for each task t, evaluate on all tasks > t; then average across all t"), and note why Aircraft is excluded from the Transfer row in Table 2 while included in the zero-shot CLIP baseline.
3. **Tone down the spectral dynamics language** in Section 6.1. Replace "clear and consistent increase" with a more measured description that notes the small magnitude while highlighting the key finding — the null space does not saturate even after many tasks.
4. **Fix the InflLoRA/InflORA inconsistency** and provide hardware details for the SVD timing comparison.

## Score and Decision

### Calibration Anchors

| Anchor | Avg Score | Query Bucket | Comparison |
|--------|-----------|--------------|------------|
| JIlIYIHMuv (LVLM-CL) | 2.50 | Topic-low | Much weaker paper — unclear method, missing baselines, poor writing. Current paper is substantially stronger. |
| bqv7M0wc4x (ICL-TSVD) | 5.50 | Topic-mid | Comparable quality — both have clear methods, theoretical motivation, and empirical support. ICL-TSVD had stronger theory but was criticized as incremental. Current paper has a more novel approach. Accepted. |
| k9NYnsC4Mq (PROOF) | 5.67 | Topic-mid | Comparable quality — both address VLM continual learning. PROOF had more concerns about inference mismatch and missing standard deviations. Current paper has fewer substantive methodological concerns. Rejected despite scores. |
| sb7qHFYwBc (C-CLIP) | 6.50 | Topic-high | Stronger paper — introduced a new benchmark and more comprehensive evaluation. Current paper has a more novel method but less thorough benchmarking. Accepted. |
| NmiFwEP8K5 (GE-PEFT) | 4.50 | Weakness: missing baselines | Lower quality — evaluation gaps noted as major weakness. Current paper shares a similar weakness on CIFAR-100 but has stronger overall evidence on MTIL. Rejected. |
| PJjHILiQHC (Spectral Dynamics) | 6.25 | Weakness: overclaiming | Off-topic but relevant to the spectral over-interpretation concern. This paper was rejected despite high scores when claims were found overstated. |

The low-band anchor (2.50) failed due to unclear methodology, absent baselines, and poor writing — the current paper does not share these failures. However, the missing-baseline anchor (GE-PEFT at 4.50) was penalized for incomplete evaluation, a weakness the current paper partially shares on CIFAR-100. The mid-band anchors (5.50–5.67) represent papers with clear contributions but documented gaps, which is where this paper sits. The high-band anchors (6.50+) had more comprehensive evaluation and fewer gaps.

**Score: 5.0** — This paper has a novel, principled method and strong evidence on the primary benchmark (MTIL), but the incomplete CIFAR-100 evaluation and ambiguities in metric documentation keep it below the median. The contribution is real and the method is well-designed, but the evaluation is not fully thorough.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>