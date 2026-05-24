Now I have all the evidence I need. Let me synthesize the final review.

---

## Summary

LoLoRA proposes a modification to LoRA that freezes the A adapter matrix (eliminating its activation storage) and instead updates it via local, gradient-free Hebbian PCA rules during the forward pass, while B is trained normally with backpropagation. The authors provide a theoretical analysis showing that under a random regression assumption, the optimal A initialization spans the top principal components of the input covariance, motivating the PCA-based local updates. The method is evaluated on NLU (GLUE), math reasoning (MetaMathQA→GSM8K), and multimodal instruction tuning (LLaVA).

## Strengths

- **Principled theoretical motivation**: Theorem 4.4 provides an explicit characterization of the optimal A under a random regression model, showing it should span the top-r eigenvectors of the input covariance. This offers a clean theoretical justification for why PCA-based initialization and updates make sense, complementing the empirical findings of prior work (EVA). The paper acknowledges the limitations of the assumption (conclusion, line 392).

- **Validated local-rule ablation**: Table 6 compares five local update variants. Rules that converge to the principal subspace (HPCA, AE) consistently outperform SoftHebb and approach full LoRA performance, confirming that the theoretical insight translates to effective practical update rules.

- **Multi-domain evaluation**: The method is tested across three distinct settings (NLU, math reasoning, multimodal), which is reasonable coverage for a method paper. The math reasoning experiment (Table 3) shows LoLoRA HPCA matching the best baseline accuracy (0.829) with reduced memory vs. standard LoRA.

## Weaknesses

### Major

- **The local updates add memory and complexity without clear benefit over simply freezing A with good initialization.** This is the central problem. LoRA-FA with EVA initialization (a one-shot PCA pass) already freezes A and achieves the same or better memory savings. LoLoRA's novelty — the online local updates — adds an optimizer for A that *increases* memory relative to LoRA-FA (Table 4: 24.1 GB vs. 23.9 GB) and does not consistently improve performance. On GLUE (Tables 1–2), LoLoRA HPCA actually underperforms LoRA-FA with uniform initialization on CoLA (66.3 vs. 67.9) and RTE (84.6 vs. 86.4). On multimodal (Table 4), LoLoRA HPCA (2.93 perplexity) trails LoRA-FA EVA (2.92). The paper's framing of memory savings relative to standard LoRA is misleading — all savings come from freezing A (LoRA-FA's contribution), while LoLoRA's local updates add memory overhead with negligible performance gains.

- **The claim of "maintains performance comparable to standard LoRA" is contradicted on GLUE.** Standard LoRA (uniform) outperforms LoLoRA HPCA on 6 of 8 GLUE tasks, sometimes substantially (CoLA: 69.6 vs. 66.3; QQP: 91.7 vs. 90.6; MNLI: 90.8 vs. 90.3). The math task (Table 3) is the only setting where LoLoRA matches standard LoRA, and there LoRA-FA EVA achieves the same result without online updates.

- **The theoretical analysis uses an assumption disconnected from real fine-tuning.** Theorem 4.4 assumes the optimal weight change ΔW₀ is an i.i.d. Gaussian matrix (Assumption 4.1). This is never motivated and is almost certainly false for real downstream tasks. The paper acknowledges this limitation (line 392: "we considered each submodule isolated with stationary targets, which is not strictly the case in multilayer architecture"), but the theory is presented as the paper's primary intellectual contribution and the results do not carry over to the actual optimization objective. The theory provides intuition, not a rigorous guarantee.

### Minor

- **Memory analysis is incomplete.** The paper reports only "extra memory" (peak GPU memory minus frozen model memory) without breaking down activation vs. optimizer vs. parameter memory. The "up to 20%" claim for GLUE is referenced but left to an unavailable appendix. Total training memory is never reported, making it difficult to assess practical significance. No comparison with gradient checkpointing, a standard technique for reducing activation memory that would be a natural baseline.

- **The conclusion overstates results.** The claim that "HPCA consistently outperforms standard LoRA-FA in two out of three experimental setups" (line 390) is misleading: on GLUE, LoLoRA HPCA is worse than LoRA-FA (uniform) on 2 of 8 tasks and the gains over LoRA-FA (EVA) are within 1-2 points; on multimodal, it does not outperform LoRA-FA (EVA).

### Trivial

- None that carry weight.

## Nice-to-Haves

- A comparison with gradient checkpointing applied to standard LoRA would contextualize whether the memory savings from LoLoRA exceed what simple activation recomputation can achieve.
- Demonstrating a scenario with significant input distribution shift during training (e.g., curriculum learning) would better motivate online subspace tracking over static EVA initialization.

## Removed Points

These points were flagged for removal, as they are either parser artifacts, lack concrete paper anchoring, or are unreasonable:

- **Insufficient hyperparameter details (Harsh Critic #4)**: The paper references Appendix C for hyperparameters. The appendix was stripped by the parser; this is not an author error.
- **No statistical significance tests**: Standard deviations are reported; formal hypothesis testing is not standard practice for LoRA benchmark evaluations in this community.
- **Missing comparison with Q-LoRA**: Q-LoRA targets weight quantization, an orthogonal memory bottleneck. Demanding this comparison is scope creep.
- **"The local updates introduce extra hyperparameters that are not discussed"**: The hyperparameters exist in the stripped appendix. The paper does mention the smoothing factor (0.98) and optimizer choice in the main text.
- **"The paper does not engage with the fact that EVA already provides a one-shot PCA initialization"**: The paper explicitly discusses EVA in related work (Section 2), in the method rationale (Section 4: "This theoretical insight complements the results of EVA paper"), and in experiments. The engagement exists.

## Novel Insights

The paper's most interesting observation is the theoretical asymmetry between adapters A and B (Theorems 4.4 and 4.5): under the random regression model, there exists a well-defined optimal subspace for A (the top eigenvectors of the input covariance), while any full-rank B is equally good. This formalizes the intuition from prior empirical work (Zhu et al., 2024; Paischer et al., 2024) that A and B play fundamentally different roles, with A serving as a feature extractor and B as a task-specific projector. This insight is genuinely novel even if the assumption it relies on limits its direct applicability.

## Suggestions

- Reframe the paper around the comparison with LoRA-FA, not LoRA. The real baseline is LoRA-FA with various initializations, since freezing A is what saves memory. Currently, the paper's claimed advantage over LoRA-FA is not supported.
- If there exists a setting where online PCA tracking of the input distribution meaningfully outperforms static EVA initialization (e.g., long training runs with distribution shift), that would be the strongest possible demonstration of LoLoRA's value. The current experiments don't provide this.
- Provide a full memory breakdown (parameters, optimizer states, activations) for at least one setting, and compare against gradient checkpointing.

## Score and Decision

**Bracket analysis (Round 1)**: The paper sits between weak LoRA-variant anchors (~3.0–3.3) and strong accepted papers (ReLoRA at 5.75, VeRA at 7.25). The most directly comparable anchor is LoRA-FA (5.33, Reject), which freezes A entirely. LoLoRA adds theoretical motivation and local updates to LoRA-FA's core idea.

**Narrowing (Round 2)**: Additional anchors confirm the bracket. "Activations Aren't Cheap" (4.25, Reject) had limited novelty and narrow impact. "Expressive Power of LoRA" (6.50, Accept) is a theory paper with rigorous results that connect to practice. LoLoRA sits below LoRA-FA (5.33) because its added complexity (local updates) yields no clear empirical or memory benefit over the simpler baseline.

**Final comparison**: LoLoRA is more novel than LoRA-FA in conception (theory + local updates vs. simple freezing) but weaker in execution: the local updates don't improve performance, they increase memory relative to LoRA-FA, and the theory's assumptions limit its practical relevance. Compared to ReLoRA (5.75, Accept), LoLoRA's empirical gains are far less convincing. The paper falls between "Activations Aren't Cheap" (4.25) and LoRA-FA (5.33), closer to the lower end.

**Anchors referenced**:
- RbKThNNFxr (LoRA-FA, avg 5.33, Round 1): Most direct baseline; simpler method with clearer memory claim. LoLoRA is less convincing empirically.
- 3ylNuZXtMg (Activations Aren't Cheap, avg 4.25, Round 2): Memory-efficiency LoRA paper with limited novelty. LoLoRA has more ambition but similarly underwhelming gains.
- DLJznSp6X3 (ReLoRA, avg 5.75, Round 1): Accepted LoRA variant with clearer empirical benefits. LoLoRA falls short of this standard.
- likXVjmh3E (Expressive Power of LoRA, avg 6.50, Round 2): Theory paper with stronger results. LoLoRA's theory is weaker and less connected to practice.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>