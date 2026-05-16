Now I have a thorough understanding of the paper. Let me produce the consolidated review.

## Summary

This paper proposes LQ-LoRA, a method that decomposes each pretrained weight matrix into a quantized component (fixed during finetuning) and a low-rank component (trainable), using an iterative algorithm alternating between SVD and quantization. It further introduces an integer linear programming (ILP) formulation for assigning different quantization configurations to different matrices under a memory budget, and explores a data-aware variant using Fisher-weighted reconstruction. Experiments on RoBERTa and LLaMA-2 (7B and 70B) show that LQ-LoRA outperforms QLoRA and GPTQ-LoRA at comparable bit widths.

## Strengths

- **Iterative low-rank plus quantized decomposition improves upon static quantization for LoRA initialization.** The paper shows that the iterative algorithm reduces reconstruction error compared to first quantizing then applying standard LoRA (Figure 1), and this improved initialization translates to consistent downstream gains across model sizes and tasks (Figure 2, Tables 1 and 2). This is the paper's primary contribution and is well-supported.

- **Mixed-configuration quantization via ILP enables flexible, non-uniform bit allocation across layers.** The ILP framework assigns different quantization parameters (bit-width, block size) to each matrix subject to a target memory budget, achieving lower storage with less accuracy loss than uniform schemes. The 2.75-bit LQ-LoRA (ILP-allocated) matches or beats 3.127-bit QLoRA on multiple metrics (Figure 2), demonstrating a real practical advantage.

- **Ablation shows LQ-LoRA makes better use of increased LoRA rank than QLoRA.** Table 5 (rank analysis) shows that raising rank from 8 to 256 improves LQ-LoRA by 1.3 perplexity points, whereas QLoRA improves by only 0.3 points. This cleanly confirms that the decomposition utilizes additional rank for error reduction at initialization.

- **Memory-breakdown analysis quantifies practical deployment gains.** Figure 5 shows that sub-3-bit quantization dramatically reduces storage of the 70B model, enabling single-GPU deployment and finetuning on an 80GB GPU, which is a concrete demonstration of the method's memory efficiency.

## Weaknesses

### Fatal

None.

### Major

- **The model compression comparison against PTQ methods is confounded by additional finetuning.** In §5.2, LQ-LoRA is compared against sub-4-bit PTQ methods (GPTQ, OmniQuant, etc.), but the LQ-LoRA procedure involves additional finetuning on a larger calibration dataset (two C4 partitions + WikiText-2, sequence length 2048) and subsequent quantization of the LoRA components. Standard PTQ methods perform one-shot quantization without finetuning. This asymmetry favors LQ-LoRA, making the claim that it "generally outperforms other sub-4-bit PTQ methods" (line 250) misleading. The paper should either report LQ-LoRA performance *without* the additional finetuning as a fair PTQ baseline, or clearly frame these results as "model compression via continued finetuning" rather than PTQ. This does not undermine the core finetuning contributions, but it weakens a secondary claim presented in the abstract and §5.2.

### Minor

- **The Fisher-weighted variant delivers inconsistent benefits and rests on an unvalidated approximation.** In §3.3, the weighted SVD problem is solved by assuming homogeneous rows or columns of the Fisher information matrix — an assumption the authors acknowledge "clearly does not hold" (line 184). No analysis is provided to quantify how far F deviates from this structure or whether the approximation error is empirically small. The empirical results are inconsistent: on GLUE (Table 2), Fisher helps at 2.5 bits (87.3 vs. 85.7) but is *worse* at 2.75 bits (86.4 vs. 87.1), and essentially tied at 3.0 and 3.25 bits. On LLaMA-2-7B it helps consistently, but "this discrepancy shrinks at the 70B scale" (line 243). Given that Fisher computation requires backprop through the entire model (partly undermining the memory-efficiency motivation, as the paper notes), the marginal and inconsistent gains do not convincingly justify the added complexity. This is a weakness of the Fisher variant specifically, not of the core LQ-LoRA method (which works well without it).

- **No ablation isolating ILP allocation from the decomposition itself.** The paper compares LQ-LoRA to QLoRA and GPTQ-LoRA, both of which use uniform quantization. To quantify the contribution of the ILP mixed-configuration scheme specifically, the paper should include a control where LQ-LoRA uses the same (uniform) configuration for all matrices at a matched average bit rate. Without this, it is unclear how much of the gain comes from the decomposition versus the dynamic allocation.

- **The ILP pre-computation cost for larger models is not discussed.** The paper states the pre-computation takes "a few hours" for LLaMA-2-7B on 4 A100s (line 129). For LLaMA-2-70B, which has roughly 10× the matrices with larger dimensions, this cost likely scales substantially. Since the method's motivation is memory efficiency, the practical overhead of this one-time cost should be acknowledged.

- **The analysis of mixed-configuration allocations (Figure 4) remains shallow.** The discussion only notes that "ILP is able to allocate different configurations to different matrices" and that allocations differ between Fisher and non-Fisher variants. Systematic patterns (e.g., do deeper layers get more or fewer bits? are certain matrix types systematically assigned higher precision?) are not examined, leaving the ILP analysis as a descriptive rather than informative result.

### Trivial

- **Stopping criterion for the iterative algorithm is underspecified.** The paper states "terminate the algorithm if the error increases" (line 69), but does not clarify whether this is relative to the previous iteration, whether oscillations are handled, or whether the algorithm can restart. This is minor and easy to clarify.

## Nice-to-Haves

- A version of the model compression experiment using LQ-LoRA *without* additional finetuning, to serve as a fair comparison to one-shot PTQ methods.
- A simple control experiment isolating the effect of ILP allocation from the decomposition (LQ-LoRA with uniform config at matched bit rate).
- Quantification of the Fisher approximation error on a few representative matrices, to validate that the row/column-scaling solution correlates with the true weighted SVD objective.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **"The claim that the quantized component remains fixed and only the low-rank component is updated is standard in QLoRA as well."** — The critic treats this as a presentation issue, suggesting the novelty should be clearer. The paper's novelty is in the *decomposition/initialization*, which is explicitly stated in the same paragraph (lines 19-20) and the method section. The paper is clear about this distinction; the critic's reading does not reflect a substantive flaw.

2. **"No confidence intervals or significance tests for any metric; Vicuna evaluation has no tie rates reported."** — The experimental setup follows QLoRA's conventions exactly, where single-run evaluation is standard for LLM finetuning at this scale, and Vicuna-style GPT-4 pairwise comparisons (80 questions) are canonical. Demanding confidence intervals here would be applying a standard not typical for this class of paper.

## Novel Insights

None beyond the paper's own contributions. The reviewers converged on the core method being sound and the main results convincing, with disagreements confined to the Fisher variant (which is optional) and the PTQ framing (which is secondary). The most valuable insight from the meta-review is that the paper would be stronger if it removed the PTQ comparison claim or added a fair control, and if it presented the Fisher variant as an exploratory extension rather than a core contribution — neither of which changes the accept/reject judgment.

## Suggestions

1. **Reframe the model compression section.** Either report LQ-LoRA perplexity *without* the additional finetuning (so that the comparison to one-shot PTQ methods is fair), or explicitly frame the results as "post-training with continued language modeling" rather than "post-training quantization."
2. **Add an ILP vs. uniform ablation control.** Run LQ-LoRA with a single uniform configuration at the same average bit rate to isolate the benefit of mixed-configuration allocation from the benefit of the decomposition itself.
3. **Provide at least a basic validation of the Fisher approximation** on a few representative matrices (e.g., comparing the true weighted reconstruction error against the approximate solution), or de-emphasize the Fisher variant as an exploration rather than a core contribution.
4. **Clarify the stopping criterion.** Specify: "terminate if the error increases relative to the previous iteration" or similar.

## Score and Decision

This paper's primary contribution — the iterative low-rank plus quantized decomposition for initializing LoRA components, combined with ILP-based mixed-configuration quantization — is novel, well-motivated, and empirically validated across multiple model sizes (RoBERTa-Large, LLaMA-2-7B, LLaMA-2-70B) and tasks (language modeling, instruction tuning, GLUE). The method consistently outperforms strong baselines (QLoRA, GPTQ-LoRA) at comparable bit widths. The weaknesses identified (confounded PTQ comparison, inconsistent Fisher benefits, missing ablation) are real but do not threaten the core contributions and can be addressed without altering the paper's main findings. The paper is honest about limitations and includes useful negative results.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>