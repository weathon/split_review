## Summary

This paper proposes GLoRA (GeLoRA), a method that uses the estimated intrinsic dimensionality of hidden-state representations to adaptively select LoRA ranks per transformer layer. The core idea is that the difference in intrinsic dimension between a block's input and output manifolds provides a lower bound on the number of parameters needed to optimize that block, which is then used to set the rank of each LoRA matrix. The method is evaluated on GLUE and SQuAD using DeBERTaV3-base, showing modest improvements over standard LoRA (~1 point on GLUE average) while using a comparable parameter budget.

## Strengths

1. **Novel and well-motivated rank-selection strategy.** Using the intrinsic dimensionality of hidden representations to inform layer-specific LoRA ranks is a genuinely interesting idea that differs from prior heuristic approaches (importance-score pruning, binary gating, etc.). The connection to manifold geometry is a fresh perspective in the LoRA literature.

2. **Competitive empirical results on GLUE and SQuAD.** The paper reports an average GLUE score of 87.92 across six tasks (vs. LoRA at 86.95) and SQuADv1.1 EM/F1 of 86.72/92.84, outperforming LoRA variants by 0.45–2.27 EM points. The results are consistently positive across tasks and are averaged over five random seeds with standard deviations reported.

3. **Lower training runtime than several adaptive baselines.** Table 4 (training clock time) shows GeLoRA has lower wall-clock training time than SoRA and BitFit when ranks are matched. This is a concrete efficiency benefit.

4. **Interesting secondary analysis of intermediate task tuning.** The paper uses its intrinsic-dimension framework to offer a plausible explanation for why intermediate task tuning helps (Figure 3 shows compression of intrinsic dimensions after warm-up), going beyond the typical intuition-based justification.

## Weaknesses

### Fatal
None.

### Major

1. **The theoretical framework does not establish the claimed connection to LoRA rank selection.** The paper presents Theorem 3.2 and Corollary 3.2.1 as the theoretical foundation, but there are critical gaps:

   - Theorem 3.2 bounds the *Jacobian rank of the pretrained transformer block* (max rank of J(T_i, x, θ) over inputs). It says nothing about the rank needed for the *LoRA update* ΔW, which is a low-rank perturbation added to the frozen weights. No formal link is established between these quantities.
   
   - Corollary 3.2.1 bounds N_{i-1}, defined as "the number of parameters required to optimize at transformer block i" — a quantity the paper never formally defines. It is then treated as if it were the LoRA rank, but a bound on "required parameters" is not the same as a bound on the rank of a low-rank matrix factorization.
   
   - The rank-selection rule r_i = max(d_{i+1} - d_i, 0) + 1 is presented as following from these results, but this is not logically derivable. A lower bound on "required parameters" does not prescribe a precise rank value — it only says that using *fewer* will fail. Setting the rank to the lower bound (plus a fixed offset of 1) is a heuristic choice, not a theoretical prescription.
   
   The paper would be stronger if it honestly reframed this as theoretically-motivated heuristic rather than claiming a derivation.

2. **A major promised evaluation is entirely absent.** Section 3.4 states that the paper will "investigate instruction-following tasks by fine-tuning the model on the Airoboros dataset and evaluating on MT-Bench" using Phi-2. The results section (3.6) contains only GLUE (3.6.1) and SQuAD (3.6.2) — no instruction-following results appear anywhere in the paper. For a paper that claims "empirical validation on multiple tasks," having one of three announced evaluations completely missing is a significant deficiency.

3. **Preprocessing cost of intrinsic dimension estimation is not quantified, making efficiency claims incomplete.** The paper acknowledges (Section 4) that "our technique shifts some computational overhead to the preprocessing step" but provides no measurement of this cost: how many data points are used for the 2-NN estimation? What is the wall-clock time? How does it scale with model depth? The efficiency comparison (Table 4) measures only training time and excludes this cost. Without this information, the claim that GeLoRA "incurs less computational overhead" is unsupported.

### Minor

1. **Small performance margin and uncontrolled accuracy comparison.** The GLUE improvement over standard LoRA is ~1 point (87.92 vs. 86.95). The paper does not include an accuracy comparison where parameter counts are explicitly matched for standard LoRA vs. GeLoRA, so it is unclear whether the gain comes from adaptive rank allocation or simply from using a different (possibly higher) parameter budget on some tasks.

2. **"State-of-the-art" claim on SQuAD is unverifiable.** The paper states "GeLoRA achieves state-of-the-art performance" (Section 3.6.2) but does not specify what the prior SOTA was, making this claim impossible to verify from the paper itself.

3. **Adaptive scaling factor α_i is not ablated.** The method uses α_i/r_i = const (ratio = 32), which means α_i varies per layer. For standard LoRA, α is typically fixed across layers. The effect of this adaptive scaling vs. standard fixed-α is never evaluated. An ablation would clarify whether the rank allocation or the scaling scheme drives the results.

4. **Single model scale for main experiments.** All GLUE and SQuAD experiments use DeBERTaV3-base. While the paper mentions Phi-2 for instruction-following (which has no results), the core NLU/QA claims rest on a single model family and size, limiting the support for claims about "large language models" more broadly.

### Trivial

1. **Naming inconsistency.** The title uses "GLoRA" while the body consistently uses "GeLoRA." These should be unified.
2. **Theorem 3.2 and Corollary 3.2.1 are stated without proof or citation.** Even as heuristic motivation, providing a sketch or reference would help.

## Nice-to-Haves

- A parameter-controlled accuracy comparison matching GeLoRA's total parameter budget against standard LoRA at the same budget would cleanly isolate whether the adaptive allocation (rather than the specific parameter count) drives the improvement.
- Ablation of the +1 offset: how sensitive are results to this choice?
- Reporting statistical significance given the modest margins would strengthen the claims.

## Removed Points

These points from the reviewers were removed with justification:

- *Misleading rhetorical move re: full fine-tuning comparison* — The paper's comparison of PEFT methods to full FT on parameter count is used as context for efficiency, not as a central claim. This is a minor rhetorical flourish, not a substantive weakness.
- *FIM being "almost surely full rank" undermines motivation* — The paper correctly handles this transition (line 73), explaining that near-zero eigenvalues justify the shift to intrinsic dimension. This is standard in the intrinsic-dimension literature.
- *Notation complaints about "N\bar{\aleph_{\phi}}"* — This is a parser artifact from the PDF-to-text extraction, not a paper error.
- *Missing statistical significance tests* — Five seeds with standard deviations are reported, which meets the standard practice in this area.
- *Missing per-matrix rank allocation for K/Q/V/O* — The paper explicitly acknowledges this as a limitation ("Since we cannot localize the specific important parameters within each matrix"), not a claimed contribution.
- *Generic requests for larger datasets, more models, sensitivity analysis* — These are reasonable extensions but not weaknesses; the scope of the evaluation is appropriate for the paper's claims.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Reframe the theoretical contribution.** Present the intrinsic-dimension framework as motivated heuristic inspiration rather than a derivation of the rank formula. Theorem 3.2 and Corollary 3.2.1 provide intuitive justification, but the actual rank-selection rule is a pragmatic design choice built on this intuition. The paper's value does not hinge on a strict derivation.

2. **Complete the missing instruction-following experiment.** This is non-negotiable for the paper as scoped. Either include the results or remove the claim from the evaluation protocol.

3. **Quantify the preprocessing cost.** Report the wall-clock time and data requirements of the 2-NN estimation step, and present a total-cost comparison (preprocessing + training) alongside the current training-only comparison.

4. **Run a parameter-matched accuracy comparison.** Compare GeLoRA against standard LoRA at the same total parameter budget to demonstrate that the adaptive allocation (not the parameter count) drives the improvement.

5. **Ablate the adaptive α_i scaling.** Show results with and without the per-layer scaling to clarify its contribution.

## Score and Decision

The paper has a genuinely interesting core idea and delivers positive empirical results. However, the theoretical claims substantially overstate what is actually established, a major experiment promised in the evaluation protocol is entirely missing, and the efficiency claims are unsubstantiated because the preprocessing overhead is unmeasured. These gaps are individually addressable but collectively significant for a top-venue submission. The paper would need honest reframing of its theoretical contribution, completion of the missing experiment, and quantification of the preprocessing cost before it meets the standard for acceptance.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>