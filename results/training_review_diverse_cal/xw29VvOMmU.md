Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper proposes LQ-LoRA, a method that decomposes each pretrained weight matrix into a quantized component (Q) and a low-rank component (L₁L₂) using an iterative algorithm inspired by robust PCA. The low-rank component is initialized to compensate for quantization error and is the only part updated during finetuning. The method further incorporates (1) an integer linear program (ILP) to assign mixed quantization configurations per layer under a target bit budget, and (2) a data-aware variant that weights the decomposition objective by an approximate Fisher information matrix. Experiments on LLaMA-2 (7B, 70B) and RoBERTa-Large show consistent improvements over QLoRA and GPTQ-LoRA baselines across language modeling, instruction tuning, and GLUE benchmarks, and the approach also shows promise as a post-training compression technique.

## Strengths

- **Core idea is well-motivated and empirically effective.** The paper identifies a genuine limitation of existing quantized LoRA methods (zero initialization of LoRA components ignores quantization error) and proposes a principled fix: initializing the low-rank components to capture the residual from quantization. Figure 1 empirically confirms that the LQ decomposition reduces reconstruction error across all layer types compared to vanilla NF-3 quantization.

- **Consistent improvements across model sizes (355M–70B) and tasks.** LQ-LoRA outperforms QLoRA and GPTQ-LoRA at comparable or lower bit budgets on C4 perplexity, WikiText perplexity, MMLU, GLUE, and instruction-following evaluations. For example, 3.5-bit LQ-LoRA (Fisher) is generally comparable to 4.127-bit QLoRA; 2.75-bit LQ-LoRA is competitive with 3.127-bit QLoRA. These cross-bit improvements are meaningful and consistent.

- **Mixed-precision via ILP enables flexible bit budgets.** The ILP formulation allows users to specify arbitrary target bit rates and assigns different quantization configurations to different matrices. The paper demonstrates this works effectively across 2.5–3.5 bit regimes, and the allocation patterns differ meaningfully between Fisher-weighted and unweighted variants (Figure 3).

- **Fisher-weighted variant provides large gains at extreme quantization (2.5 bits).** On GLUE with RoBERTa-Large at 2.5 bits, LQ-LoRA (Fisher) achieves 87.3 vs. unweighted LQ-LoRA (85.7) vs. QLoRA (75.4), demonstrating the data-aware weighting is especially valuable in aggressive compression regimes.

- **Better use of higher LoRA ranks than QLoRA.** Table IV shows LQ-LoRA's performance improves with increasing rank (perplexity drops ~0.5 from rank 64 to 256), while QLoRA is insensitive to rank. This validates the intuition that the decomposition leverages the low-rank component to meaningfully capture variance.

## Weaknesses

### Fatal
None.

### Major

- **Missing component-level ablation.** The paper bundles three distinct innovations — low-rank residual initialization, ILP-based mixed-precision assignment, and Fisher-weighted decomposition — but never isolates their individual contributions. Without comparing (a) LQ-LoRA uniform vs. QLoRA (to measure the low-rank init's benefit alone), (b) LQ-LoRA (ILP, no Fisher) vs. LQ-LoRA uniform (to measure the ILP's isolated benefit), and (c) LQ-LoRA (Fisher, uniform) vs. LQ-LoRA uniform (to measure data awareness's isolated benefit), it is impossible to attribute the reported gains to any specific component. Given the authors' own observation (footnote, §3.1) that initializing Q⁽⁰⁾ to quantize(W) yields similar performance, the iterative algorithm may not be the driver either. This is the single most important missing analysis.

- **Fisher-weighted approximation is central but unvalidated.** The data-aware variant provides the largest gains at the 7B scale (Figure 2) and is presented as a core contribution, yet the row/column-constant approximation is justified only by the statement that it "clearly does not hold" and "we found this approach to work well in practice" (§3.3). No evidence is provided that the approximation preserves directions of high Fisher importance; no comparison is made to a more principled (if slower) iterative weighted low-rank approximation on small matrices where it is tractable. The footnote that an activation-matching objective underperformed Fisher does not validate the approximation itself — it only shows Fisher is less bad than another flawed approach. Given the centrality of this component, the lack of validation is a significant gap.

- **ILP objective minimizes reconstruction error, not downstream performance.** The ILP assigns configurations to minimize $\|\mathbf{W}^{(i)} - (\mathbf{Q} + \mathbf{L}_1\mathbf{L}_2)\|_F^2$, but there is no guarantee this aligns with final task performance. The authors acknowledge this in §5, but the experiments do not include a comparison to a simpler heuristic (e.g., allocating more bits to layers with higher reconstruction error after uniform quantization, or a uniform configuration at the same average bit rate). Without this, it is unclear whether the ILP's complexity is justified or whether any mixed-precision assignment derived from the same error metric would perform similarly.

### Minor

- **PTQ comparison is not apples-to-apples.** In Table III (PTQ results), LQ-LoRA is compared to GPTQ and other methods that perform weight-only quantization *without gradient-based finetuning*. Even the base LQ-LoRA PTQ variant uses Fisher backpropagation through the model for the decomposition, and the "effective bits" includes the low-rank components. The additional finetuning experiment (§4.2, second paragraph) goes even further. While the paper is transparent about these choices, the comparison risks misleading readers about the source of LQ-LoRA's advantage in the pure compression setting. A version of LQ-LoRA that does not finetune the low-rank components and uses them purely as a better initialization for quantized weights would clarify this.

- **Instruction tuning evaluation lacks variance estimates.** The Vicuna-style evaluation (80 questions, GPT-4 pairwise judging) reports single numbers without error bars or significance tests. At the 7B scale, the gap between LQ-LoRA (Fisher, 3.5 bit) at 67 and QLoRA (4-bit) at 52 is large, but without variance estimates it is difficult to assess robustness given the small sample size and known LLM-as-judge variability.

- **Iterative algorithm is overframed given the evidence.** The paper presents an iterative RPCA-style algorithm with a stopping criterion, but the footnote in §3.1 states that initializing $\mathbf{Q}^{(0)} = \text{quantize}(\mathbf{W})$ (a single-step residual SVD) did not yield significant performance differences. This suggests the iteration beyond one step is decorative. The paper's narrative should be adjusted to align with what the evidence actually supports.

### Trivial

- **Rank sensitivity analysis (Table IV) is only shown on C4 perplexity.** Showing the same trend on a downstream task (e.g., MMLU) would increase confidence that the improved initialization translates to better task performance, not just better reconstruction.

## Nice-to-Haves

- A component ablation as described in the first Major weakness above. This would substantially strengthen the paper.
- A small-scale validation of the Fisher approximation (e.g., on a single transformer layer where exact weighted SVD is tractable).
- A simpler heuristic baseline (e.g., allocate bits proportional to each layer's reconstruction error under uniform quantization) to compare against the ILP.
- Error bars or confidence intervals for the instruction tuning results.

## Removed Points

- **Criticism that the iterative algorithm being "not clearly needed" fatally undermines the paper's claims** — downgraded from the harsh critic's framing to Minor. The paper's central contribution is low-rank compensation of quantization error, not iteration count. The iterative framing is a heuristic optimization procedure; the fact that it converges in one step from a good initialization does not invalidate the approach. However, the paper's narrative over-emphasizes iteration, which is a presentation issue.
- **Strength Finder's generic claim that the paper "is a sensible and practical method"** — this is a generic assessment, not a specific strength with evidence. Moved here.
- **Strength Finder's claim that the Fisher approximation is "justified with a practical workaround"** — the paper acknowledges the practical concern (Fisher requires backprop) but does not *justify* the row/column-constant approximation itself; it merely notes it works empirically. This conflates practical feasibility with approximation validity.
- **The harsh critic's suggestion to "drop the iterative framing" entirely** — this is a suggestion for revision, not a weakness. Moved to Nice-to-Haves.
- **Criticism about comparing LQ-LoRA (with finetuning) to GPTQ (without finetuning) in the PTQ setting** — partially kept in Minor. The paper does describe two separate conditions (base PTQ + additional finetuning experiment), so the criticism somewhat overstates the conflation. However, even the base PTQ variant uses Fisher backprop, which pure PTQ methods do not.

## Novel Insights

None beyond the paper's own contributions. The reviews identify important missing analyses (ablations, approximation validation) but do not surface novel interpretations of the results that the paper itself missed. The key observation from the harsh critic — that the iterative algorithm may not be the source of improvement given the footnote about one-step initialization — is a valid point about framing but follows directly from the paper's own disclosure.

## Suggestions

1. **Add a component ablation** — This is the single most impactful improvement. Compare (a) LQ-LoRA with uniform quantization (no ILP, no Fisher) vs. QLoRA at the same bit rate to isolate the low-rank init's benefit; (b) LQ-LoRA with ILP vs. uniform LQ-LoRA to measure the ILP's benefit; (c) LQ-LoRA (Fisher, uniform) vs. LQ-LoRA (uniform) to measure data awareness's benefit. This would resolve the largest ambiguity in the paper.
2. **Validate the Fisher approximation** — On small matrices where exact weighted SVD is tractable, compare the row/column-mean approximation to the ground-truth solution. At minimum, show that the scaling matrices $\mathbf{D}_{\text{row}}, \mathbf{D}_{\text{col}}$ are not degenerate or that the approximation captures meaningful variance in Fisher importance.
3. **Include a simple mixed-precision heuristic baseline** — Even allocating bits proportional to each layer's uniform quantization reconstruction error would test whether the ILP's optimization adds value beyond any non-uniform assignment.
4. **Clarify the PTQ comparison** — Either report PTQ results from a version of LQ-LoRA that does not use gradient-based finetuning, or add a baseline where GPTQ quantized weights also receive LoRA finetuning (GPTQ-LoRA is already used in the finetuning experiments — report it in the PTQ table).
5. **Add variance estimates** for the instruction tuning evaluation (e.g., bootstrapped confidence intervals or results across multiple seeds).

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>