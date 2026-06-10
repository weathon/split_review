## Summary

This paper proposes Natural GaLore, a memory-efficient optimizer that extends GaLore by incorporating second-order information via the inverse empirical Fisher Information Matrix (FIM). The key technical contribution is an efficient, matrix-free application of the inverse FIM to low-rank gradients using Woodbury's Identity, Cholesky decomposition, and matrix-vector products, costing O(s²) time where s is the gradient history length. The method is designed as a drop-in replacement for AdamW within the GaLore framework. Experiments cover LLaMA pre-training on C4 (60M–1.1B parameters, comparing against GaLore), RoBERTa fine-tuning on GLUE (comparing against full fine-tuning and LoRA), and TinyLlama fine-tuning on the TinyAgent function-calling benchmark (comparing against LoRA and GPT-4-Turbo).

## Strengths

- **Efficient matrix-free application of the inverse empirical FIM to low-rank gradients (Section 3.3, Eqs. 190–204).** The Woodbury Identity derivation is correct and the computational approach (Cholesky decomposition on an s×s matrix, avoiding explicit construction of the high-dimensional FIM) is technically sound. This is a non-trivial algorithmic contribution: prior work like K-Fac requires per-layer information and is computationally heavy, whereas this approach operates entirely in GaLore's low-rank subspace.

- **Consistent perplexity improvements over GaLore in pre-training (Section 4.1, Table~lora_compare_llama).** The paper reports that Natural GaLore achieves lower validation perplexity than GaLore across LLaMA models at multiple scales (60M–1.1B) on C4 data. This directly demonstrates that the second-order correction yields optimization gains where GaLore alone is the baseline.

- **Concrete fine-tuning improvements over LoRA.** On GLUE (Section 4.2), Natural GaLore with rank 4 achieves 86.05% average vs. 86.28% for full fine-tuning and 85.61% for LoRA — closing much of the gap typical of PEFT methods. On the TinyAgent benchmark (Section 4.3), Natural GaLore achieves 83.09% accuracy vs. 80.06% for 16-bit LoRA.

- **Theoretical motivation with acknowledged caveats (Section 3.2).** The paper links the method to Fisher efficiency and the Cramér-Rao lower bound (Eq. 164) while honestly noting that the guarantee requires convexity, realizability, and access to the exact FIM — conditions that do not strictly hold. The discussion is appropriately cautious.

- **Drop-in design.** The natural gradient estimate (Eq. 202–203) is fed directly into the standard Adam update, requiring no changes to the rest of the GaLore pipeline. This is a concrete practical advantage over methods like K-Fac.

## Weaknesses

### Major

- **The "no additional memory overhead" claim relative to GaLore (abstract, Sections 1 and 3.3, conclusion) is unsupported and likely false for any s > 0.** The method stores the stacked gradient matrix G = [vec(g_k), …, vec(g_{k-s})] (Eq. 190), which occupies (s+1) × (r × m) values — additional memory that GaLore does not require. The paper never specifies s for any experiment, making the claim impossible to verify. If s = 0 the method collapses to standard GaLore; if s > 0 there is additional memory cost. This is a central claim that the paper must either substantiate with a memory accounting or retract.

- **Key hyperparameters s (gradient history length) and λ (Tikhonov regularization) are never disclosed for any experiment, and no ablation studies are provided.** The method's behavior critically depends on both: s controls the quality of the empirical FIM estimate and the memory footprint; λ controls the regularization strength. Without knowing their values, the experiments are not reproducible. Without ablations, the reader cannot tell whether improvements come from the natural gradient transform, favorable choices of these hyperparameters, or interaction with learning rate tuning (which itself is tuned per method but the chosen values are not reported).

- **GaLore baseline is missing from two of three experiment suites.** The paper is titled "Natural GaLore" — an improvement on GaLore. Yet:
  - **GLUE fine-tuning (Section 4.2):** Only full fine-tuning and LoRA are compared. GaLore itself is absent.
  - **TinyAgent function-calling (Section 4.3):** Only LoRA (16-bit) and GPT-4-Turbo are compared. GaLore is absent.
  
  Without these comparisons, the paper cannot substantiate its core claim that Natural GaLore improves upon GaLore in these settings. The pre-training experiments (Section 4.1) do include GaLore, which partly mitigates this, but the omission in two-thirds of the empirical evaluation is a significant gap.

### Minor

- **The GPT-4-Turbo comparison (abstract, Section 4.3) is framed as "surpassing GPT-4-Turbo by 4%" but compares a fine-tuned TinyLlama 1.1B against an off-the-shelf model evaluated zero-shot.** Any fine-tuned specialized model is expected to outperform a non-fine-tuned general model on a narrow benchmark. This framing inflates the perception of the method's contribution. The relevant comparison is the improvement over LoRA (83.09% vs. 80.06%), which is a legitimate result. The GPT-4 comparison should be dropped or clearly contextualized.

- **Model sizes are reported inconsistently.** The abstract (line 4) lists "60M, 130M, 350M, and 1.1B" while the introduction (line 69) lists "60M, 300M, and 1.1B" — three sizes instead of four, and "300M" instead of "350M." This discrepancy undermines confidence in the experimental reporting.

- **Best validation perplexity is reported rather than final perplexity at a fixed iteration count (Section 4.1, line 217).** Reporting the best value masks convergence dynamics. If Natural GaLore converges faster, reporting final perplexity at a fixed budget would be more informative and is standard practice.

- **The "up to 65.5% reduction in optimizer states" claim (conclusion, line 270) appears without any derivation or reference to a calculation in the main text.** This number is unsupported by the paper as presented.

- **The projection matrix P_k is updated periodically (~200 steps), but the paper does not discuss whether the gradient history G remains coherent when P_k changes.** If P_k is updated, the gradient vectors in G come from different subspaces, making the empirical FIM estimate inconsistent. This is a technical subtlety that should be addressed.

### Trivial

- None that are not covered above or moved to Removed Points.

## Nice-to-Haves

- Reporting wall-clock time for the natural gradient transform versus standard GaLore would help readers assess the computational overhead of the Cholesky decomposition and matrix-vector products.
- Learning curves (validation perplexity vs. iterations) rather than just best perplexity would directly demonstrate the claimed faster convergence.
- An ablation over s (e.g., s ∈ {1, 5, 10, 20}) and λ would substantially strengthen the paper.

## Removed Points

- **Notation imprecision (n as parameter count, m as batch size in GaLore description):** The reviewer notes that the description conflates per-layer and global quantities. This is a minor expositional imprecision that does not affect the paper's contribution or correctness. Removed as a formatting/style-level point that doesn't warrant inclusion.
- **Missing tables via \input{} commands:** The paper uses external \input{} files for result tables. This is a standard LaTeX practice. The extracted text's inability to render them is a parser limitation, not an author error. Removed per instructions.
- **Strength about TinyAgent "surpassing GPT-4-Turbo":** This framing is misleading (see Weaknesses) and the strength claim as stated (from the Strength Finder) conflicts with a verified weakness. Removed per instructions about strength/weakness conflict.
- **General concerns about missing computational cost analysis of GaLore's SVD recomputation:** This is a generic "could be better" comment that doesn't identify a specific flaw. Removed as area-of-concern sweep.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Specify s and λ for every experiment** and provide an ablation study varying s across a range (e.g., 1, 5, 10, 20) with corresponding memory measurements. This is essential for reproducibility and for grounding the memory-overhead claim.
2. **Include GaLore as a baseline in the GLUE and TinyAgent experiments.** Without this, the paper cannot support its central thesis that Natural GaLore improves on GaLore outside of pre-training.
3. **Either retract the "no additional memory overhead" claim or provide a precise memory accounting** that explains how G is stored without extra memory. If the claim is true, show the calculation; if false, restate honestly as "negligible additional overhead" with quantification.
4. **Remove or recontextualize the GPT-4-Turbo comparison.** Present it only as context (small fine-tuned model vs. large proprietary zero-shot model) and avoid framing it as "beating GPT-4."
5. **Report final perplexity at fixed iteration counts** in addition to (or instead of) best perplexity.
6. **Resolve the model size inconsistency** between abstract (60M, 130M, 350M, 1.1B) and introduction (60M, 300M, 1.1B).
7. **Provide a derivation or citation for the "65.5% reduction in optimizer states" claim** referenced in the conclusion.

## Score and Decision

The core algorithmic idea — applying the inverse empirical FIM to GaLore's low-rank gradients via Woodbury's Identity — is novel and technically sound. The pre-training results with GaLore as a baseline are promising. However, the paper has significant evaluation gaps that prevent acceptance at a top venue: key hyperparameters are undisclosed, the "no additional memory overhead" claim is unsupported and likely contradicted by the method's own design, GaLore is absent from two of three experiment suites, and a headline result (GPT-4-Turbo comparison) is misleadingly framed. These issues can be addressed in revision, but the paper in its current form does not present a complete and verifiable evaluation.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>