Now I have a thorough understanding of the paper and have verified the key claims. Let me produce the consolidated review.

---

## Summary

This paper tackles the Lookback Window Limitation (LWL) in time series forecasting, where Transformer-based models degrade with longer lookback windows. It proposes two model-agnostic modules: an Information Bottleneck Filter (IBF) for reducing input redundancy via learned masking with noise injection, and a Hybrid-Transformer-Mamba (HTM) that partitions long sequences into blocks processed by Transformer while Mamba handles the full sequence. Combined with PatchTST to form PIH, the approach achieves SOTA results with a lookback window of 1024—longer than typical prior settings. Fig. 3a provides the clearest evidence: PIH's error decreases monotonically from L=96 to L=1024, whereas PatchTST degrades after L=512.

## Strengths

- **Demonstrated performance gains at previously infeasible window lengths**: PIH achieves SOTA results with L=1024 across seven datasets. Fig. 3a directly shows that PIH's error decreases monotonically from L=96 to L=1024, while PatchTST degrades at L=1024. This provides the most direct evidence that the proposed modules help models benefit from longer windows. Tab. 1 further confirms PIH outperforms several baselines, including those (PatchTST, DLinear, NLinear) evaluated at the same L=1024 window.

- **Practical complexity reduction**: HTM achieves 2–3× reduction in both computation time and memory compared to PatchTST (Fig. 3b), and ablation (Fig. 6) shows the hybrid design outperforms a pure-Mamba variant (HMM), confirming the complementary value of combining Transformer (efficient for short subsequences) with Mamba (linear-complexity long-range processing).

- **Thorough ablation isolating module contributions**: Component ablation (Fig. 6) separates the effects of IBF, HTM, and their combination across four forecast horizons and seven datasets. Both modules individually improve upon the PatchTST baseline, with the combination yielding further gains—especially at the longest prediction horizon (T=720).

- **Interpretability through subsequence selection**: The IBF module provides a natural mechanism for temporal attribution by identifying important patches. The visualization (Fig. 3c) showing selected patches aligning with peak positions adds value beyond raw forecasting accuracy.

## Weaknesses

### Fatal
None. The empirical results are not invalidated by any single issue; the core finding that the proposed architecture achieves stronger long-window performance is supported by the data.

### Major

- **Incomplete derivation of the IBF compression loss (Eq. 9)**. The compression term of the IBF loss is given as:  
  `-I(z^noise, z) ≤ E_z(-½ log A + 1/(2N) A + 1/(2N) B²) := L_comp(z^noise, z)`  
  but the symbols A and B are never defined in the paper. The surrounding text says "we can derive its variational upper bound" and then jumps to the final expression with no intermediate steps. A reader cannot verify whether this bound is correct, what assumptions it relies on, or how it relates to the claimed IB objective. This is a structural gap: the paper's theoretical framing is IB, but the actual loss function being optimized is underspecified. Without this derivation, the IBF module is effectively a learned masking scheme with noise injection and a heuristic loss—the IB motivation is decorative rather than functional.

- **The "model-agnostic" claim is unsupported by architectural details**. The paper asserts model-agnosticity and shows results for integrating IBF+HTM into Transformer, Informer, and Autoformer (Section 4.2, Fig. 4–5), but provides zero technical description of *how* these integrations work. It does not specify whether patching is applied to all architectures (Informer and Autoformer operate on raw time points), how architecture-specific components (ProbSparse attention, decomposition) compose with the new modules, or where IBF/HTM are inserted. Without these details, the claim cannot be evaluated and the experiments are not reproducible. This undermines a core contribution.

- **Core hyperparameters are not reported**. The paper mentions patch length P, stride S, number of blocks K, temperature τ, and IB trade-off parameter β by name, but provides no numerical values for any of them. While full experimental details may belong in an appendix, the absence of any values from the paper means the method is underspecified to the point that a reader cannot assess the sensitivity or reproduce the results.

### Minor

- **The empirical evidence for "overcoming LWL" in integrated models is weaker than claimed**. For the integration experiments (Section 4.2), the paper selects the best results across windows for both originals and integrated models, rather than showing direct comparisons at the same long window (e.g., L=720 or 1024). Fig. 5 provides performance curves that partially address this, but the text emphasizes "window limitations shift from 48→192, 48→96, 120→228"—comparing different optimal windows rather than verifying that the integrated model is strictly better at the same long window. The evidence is suggestive and consistent with the claim, but does not isolate *at the same window* that the modules overcome degradation.

- **Interpretability evidence is anecdotal**. The paper shows one example (Fig. 3c) with selected patches at peak positions but provides no quantitative evaluation of whether the identified patches are semantically meaningful, how stable the selection is across samples, or whether it improves over random selection.

- **Complexity analysis is imprecise**. The stated complexity O(L/P) + O((L/PK)²) uses L/P as a stand-in for the patch count N, but N depends on both P and stride S. The quadratic term presumably applies only when full self-attention is used on blocks; this should be clarified.

- **No error bars or standard deviations** are reported. Time series forecasting results can be sensitive to randomness, and single-run reporting weakens confidence in the comparisons.

### Trivial
None.

## Nice-to-Haves

- If the A and B terms in Eq. 9 do have a principled derivation from a known closed-form expression for the variational IB bound under Gaussian assumptions, the authors could state what those assumptions are and provide a citation or brief derivation. Alternatively, a simpler, clearly justified compression regularizer (e.g., an explicit KL divergence between the masked and original representations) would make the method verifiable without the IB framing.

- Reporting results with standard deviations over multiple seeds would strengthen the empirical comparisons.

- Comparison against or discussion of recent large time series models (e.g., Liu et al. 2024a) is acknowledged as future/orthogonal work, but a brief explanation of why direct comparison was not feasible would improve completeness.

## Removed Points

- **Criticism that the empirical comparison is fundamentally insufficient to show LWL overcoming**: Fig. 5 *does* show performance curves across windows for integrated models, partially addressing this. The comparison in Tab. 1 between PIH at L=1024 and baselines at their best windows is a standard way to establish SOTA; the asymmetry favors the baselines (they get their optimal window, PIH uses a fixed one). The concern is valid but overstated—downgraded from Major to Minor.

- **Criticism about the "overfitting temporal noise" claim citing Zeng et al. 2022**: This is a claim attributed to an existing published paper. Whether the characterization is perfectly accurate is a citation-level concern, not a paper-level weakness. Removed.

- **Strength about "model-agnostic modules that systematically overcome LWL"**: This strength directly conflicts with the verified weakness that the model-agnostic claim is unsubstantiated (no integration details provided). Removed per the rule that weaknesses defeat conflicting strengths.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an observation that the paper itself does not already contain or imply.

## Suggestions

1. **Complete the IBF derivation**: Define A and B in Eq. 9, or provide the full variational bound derivation. Without this, the IB framing cannot be evaluated. If the derivation is too complex for the main paper, a clear statement like "following [citation], under Gaussian assumptions the bound simplifies to ..." with a full derivation in supplementary material would suffice.

2. **Provide concrete integration recipes**: For each base architecture (Transformer, Informer, Autoformer), specify in pseudocode or algorithmic steps: (a) whether patching is applied, (b) where IBF and HTM are inserted, (c) how architectural components (ProbSparse attention, decomposition) are composed with the new modules.

3. **Report all hyperparameter values**: P, S, K, τ, β, and any training details (learning rate, epochs, batch size) in the main paper or a clearly referenced appendix.

4. **Strengthen the LWL-overcoming evidence for integrated models**: Present a table version of Fig. 5 showing, for each model and at each common window (e.g., 336, 720, 1024), the MSE of both the original and the integrated version. This directly tests whether the modules close the degradation gap.

## Score and Decision

The paper addresses a real and well-recognized problem, and the high-level ideas are sensible. The empirical results—especially Fig. 3a showing PIH's monotonic improvement from L=96 to L=1024 while PatchTST degrades—provide genuine evidence that the proposed architecture overcomes the lookback window limitation. The computational benefits of HTM are also convincingly demonstrated.

However, the paper has three significant weaknesses that prevent acceptance in its current form: (1) the IBF compression loss (Eq. 9) contains undefined variables A and B, making the core theoretical framing unverifiable; (2) the claimed model-agnosticity is unsupported by any architectural integration details; and (3) core hyperparameters are unreported, making the method underspecified. These are not fatal—they are addressable with concrete additions—but they are structural gaps that require substantial revision, not minor clarification.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>