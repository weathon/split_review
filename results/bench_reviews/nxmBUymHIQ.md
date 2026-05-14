Now I have sufficient information to write the final review. Let me compile it.

## Summary
This paper proposes LoLoRA, a memory-efficient fine-tuning method that combines local unsupervised updates (Hebbian PCA) for the LoRA A matrix with gradient-based updates for the B matrix. Theoretically, Theorem 4.4 proves that under a random regression model, optimal frozen A should span the top eigenspace of the input covariance, motivating online subspace tracking via HPCA. Empirically, the method is evaluated on GLUE (RoBERTa-large), MetaMathQA (LLaMA-3.1-8B), LLaVA-v1.5-7B, and ablations on TinyLlama.

## Strengths
- **Theoretical characterization of optimal A initialization**: Theorem 4.4 provides a clean result: under a random regression target model, the minimizer set for frozen A consists of arbitrary nonsingular linear transformations of the top-r eigenvectors of the input covariance. This formalizes and generalizes the empirical EVA initialization (Paischer et al., 2024) and provides a principled justification for using PCA-converging local rules. The proof is mathematically rigorous and goes beyond prior empirical observations in this space.

- **Novel hybrid local–gradient update architecture**: Algorithm 1 frees the input z immediately after the forward pass for the A adapter, eliminating activation storage for backpropagation through A while still allowing A to adapt via local Hebbian updates. This design is technically novel over both standard LoRA (which stores activations for both adapters) and LoRA-FA (which freezes A entirely). The empirical results in Tables 4 and 6 confirm that this hybrid strategy can recover some of the performance lost by freezing A.

- **Breadth of evaluation across modalities and scales**: The method is tested on natural language understanding (RoBERTa-large, 355M), mathematical reasoning (LLaMA-3.1-8B), multimodal understanding (LLaVA-1.5-7B), and ablations on TinyLlama-1.1B. This multi-domain, multi-scale validation demonstrates the approach is not narrowly tailored to a single task type.

- **Comprehensive ablation of local update rules**: Table 6 compares five local learning rules (HPCA with/without centering, HPCA with SVD-first initialization, autoencoder loss, SoftHebb) across three ranks. The results provide practical guidance: PCA-converging rules all perform similarly, while SoftHebb underperforms. This supports the theoretical insight that spanning the correct eigenspace is what matters, not the specific update rule.

## Weaknesses

### Fatal
None.

### Major
- **Overclaimed performance advantage over LoRA-FA.** The paper states in the conclusion that "HPCA consistently outperforms standard LoRA-FA in two out of three experimental setups." This claim is not well supported by the data. On GLUE (Tables 1–2), LoLoRA HPCA underperforms LoRA-FA (uniform) on 5 of 8 tasks and matches or beats it on only 3. On MetaMathQA (Table 3), LoLoRA (82.9%) ties LoRA-FA (EVA) and the difference from LoRA-FA (uniform, 82.6%) is within one standard deviation. On LLaVA (Table 4), LoLoRA outperforms LoRA-FA (uniform) but not LoRA-FA (EVA). Meanwhile, the memory savings over standard LoRA are already achieved by the simpler LoRA-FA baseline—LoLoRA actually uses *more* memory than LoRA-FA (24.1 GB vs 23.9 GB on LLaVA, Table 4). The paper's central narrative—that local updates to A recover the performance lost by freezing A while preserving memory savings—is not convincingly demonstrated: the performance recovery is inconsistent across tasks, and the memory advantage over LoRA-FA is absent. This is the most significant weakness and undermines the paper's core empirical claim.

- **Theoretical motivation rests on an assumption disconnected from practice.** Theorem 4.4 assumes ΔW₀ has i.i.d. Gaussian entries (Assumption 4.1). In real LLM fine-tuning, ΔW₀ is highly structured, effectively low-rank, and task-dependent. The random-matrix model makes the problem equivalent to finding the top eigenvectors of the input covariance—a result that is essentially independent of the downstream task. The paper acknowledges this limitation only briefly ("we considered each submodule isolated with stationary targets") and does not argue why the Gaussian assumption should hold or what insights from the simplified model transfer to the realistic setting. While simplified theoretical models are common in ML, the gap here is large enough to weaken the theory's role as a justification for the method.

### Minor
- **Selective framing in comparisons.** The paper's GLUE summary says "LoLoRA achieves slightly better results than LoRA-FA (EVA)" but does not highlight that LoLoRA underperforms LoRA-FA (uniform) on most GLUE tasks. The conclusion uses the ambiguous phrase "standard LoRA-FA" without clarifying whether it means uniform or EVA initialization, and the claim "consistently outperforms standard LoRA-FA in two out of three experimental setups" obfuscates the mixed nature of the results. Greater precision in reporting would strengthen the paper's honesty.

- **Small but non-negligible memory overhead versus LoRA-FA.** The paper rightfully compares memory to standard LoRA for its headline savings, but Table 4 shows LoLoRA uses 24.1 GB vs LoRA-FA's 23.9 GB. The extra optimizer state for the local rule offsets the memory benefit. This is acknowledged in the conclusion but the memory claims in the abstract and introduction could mislead readers into thinking LoLoRA improves on LoRA-FA's memory efficiency.

- **On GLUE and MathQA, the performance differences between methods are often within one standard deviation.** For example, on MathQA (Table 3), all fine-tuned methods cluster within 0.821–0.829 with error bars of ~0.005, and on most GLUE tasks the standard deviations overlap between methods. This limits the statistical significance of any claimed advantage.

### Trivial
None.

## Nice-to-Haves
- A direct memory breakdown for one experiment, reporting peak allocated memory broken down by component (base weights, adapters, optimizer states, activations), would clarify exactly where the memory trade-offs occur.
- A study of HPCA subspace convergence during training—does the row space of A actually track the top eigenvectors of the evolving input covariance? The theory assumes stationary input distribution, but in practice the distribution shifts during fine-tuning.
- A plot of validation loss over training steps for one task (e.g., CoLA or GSM8K) comparing LoRA, LoRA-FA, and LoLoRA would reveal convergence speed differences.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **Criticism about missing experimental details (rank, hyperparameters) for GLUE experiments**: The paper states "see Appendix C" for hyperparameter details. Since the appendix was stripped by the PDF parser, these details exist in the original submission but are not visible here. Per the review guidelines, criticisms about missing appendix content are removed.
- **Criticism that memory comparison should be against LoRA-FA, not standard LoRA**: The paper explicitly compares memory to standard LoRA in its main claims (abstract: "further reducing the memory required for fine-tuning" refers to standard LoRA). The memory advantage over LoRA-FA is not claimed—the paper acknowledges the extra optimizer state. This is a misreading by the reviewer.
- **Criticism that LoLoRA "further reduces memory" is misleading**: As noted above, the paper compares memory to standard LoRA throughout. The full statement in the abstract is explicit: "maintains performance comparable to standard LoRA while further reducing the memory required for fine-tuning." This is accurate.

## Novel Insights
The reviews surface an important tension in the paper: the theoretical framework (Theorem 4.4) is elegant and formally correct under its assumptions, but the Gaussian random target assumption strips away precisely what makes fine-tuning interesting—namely, that ΔW is structured, task-specific, and low-rank. This creates a disconnect: the theory says "initialize A to match the input covariance eigenvectors," but it cannot explain why a local update that tracks a *moving* input covariance would outperform a static initialization (EVA), since the theory assumes stationarity. The empirical results corroborate this gap: HPCA-based online updates do not consistently outperform EVA initialization. This suggests that for practitioners, the simpler EVA initialization (a one-shot PCA before training) may be preferable to the more complex online HPCA scheme, unless non-stationarity is severe enough to warrant continuous adaptation—a condition the paper does not demonstrate exists in the settings tested.

## Suggestions
1. **Tone down the central empirical claim.** Replace "consistently outperforms standard LoRA-FA" with an honest summary: LoLoRA matches or slightly beats LoRA-FA (EVA) on some tasks, underperforms LoRA-FA (uniform) on others, and does not achieve a consistent advantage. Frame the contribution as a *method* for adapting A without activation storage, not as a method that empirically dominates LoRA-FA.
2. **Articulate why the Gaussian random target assumption is useful despite being unrealistic.** Add a paragraph discussing what insights survive when the assumption is relaxed (e.g., the analysis might still capture the *average* behavior over random targets, or the PCA alignment might be beneficial even for structured targets).
3. **Include a memory breakdown table** showing the contribution of each component (activations, optimizer states, weights) to total memory for LoRA, LoRA-FA, and LoLoRA. This would clarify the small but real memory overhead of LoLoRA vs LoRA-FA.
4. **Be precise about which variant of LoRA-FA is being compared.** Use "LoRA-FA (uniform)" or "LoRA-FA (EVA)" consistently throughout, including in summary statements and the conclusion.

## Score and Decision
**Calibration anchors** (all from ICLR 2026 human-review corpus):

| Paper | Avg Score | Comparison |
|-------|-----------|------------|
| LoRA-FA (OXmRvlihi3.md) | 3.50 (Reject) | Similar setting (freezing A); that paper also had overclaimed empirical advantages. Current paper has stronger theoretical contribution but similar empirical gap. Slightly stronger. |
| LoFT (86P3sb1dpr.md) | 6.00 (Accept Poster) | Much stronger empirical validation with consistent improvements over LoRA across tasks. Current paper weaker empirically. |
| α-LoRA (4AnuvEx3an.md) | 3.00 (Reject) | Similar pattern of clean theory under strong assumptions + limited empirical validation. Current paper has broader evaluation. Slightly stronger. |
| PSOFT (FSHrinMArK.md) | 5.00 (Accept Poster) | Stronger empirical results across 35 tasks. Current paper weaker. |
| ScaLoRA (zL9wxlDExi.md) | 4.80 (Reject) | Stronger theory with analytical optimal scaling; rejected despite this. Comparable quality. |
| BAFT (edgZd6BVzx.md) | 4.00 (Reject) | Similar quality—has a principled idea but empirical gains are modest. |
| PrefixMemory-Tuning (LvUMpZE44r.md) | 5.00 (Accept Poster) | Clearer empirical improvements over baseline. Current paper weaker. |

The paper has genuine intellectual contributions (Theorem 4.4, the hybrid local–gradient architecture, the comprehensive ablation of local rules) but the central empirical claim is not supported by the data—LoLoRA does not reliably outperform the simpler LoRA-FA baseline, and its memory savings over LoRA-FA are marginal. The theoretical framework provides intuition but rests on assumptions that are far from the realistic fine-tuning setting. Placed among the calibration anchors, the paper is comparable to mid-range rejected papers (3.5–4.5) and weaker than accepted papers in this space.

MY FINAL SCORE: <pineapple>4.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>