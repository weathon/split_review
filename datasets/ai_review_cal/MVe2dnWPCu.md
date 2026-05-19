- Decision: Accept
- Avg Score: 7.50
- Scores: 6, 8, 8, 8
Now I have all the information needed. Let me produce the consolidated review.

## Summary

This paper proposes PICLE, a probabilistic framework for modular continual learning that uses cheap fitness models (a generative model for perceptual/few-shot transfer and a Gaussian process for latent transfer) to avoid expensive training of every candidate module composition. The method is evaluated on the established CTrL benchmark and a new compositional extension (BELL), and compared against several modular and non-modular baselines. The key claim is that PICLE is the first modular CL algorithm to simultaneously achieve perceptual, few-shot, and latent transfer while scaling to long problem sequences, and the experimental evidence supports this claim.

## Strengths

- **First modular CL method to combine all three forward-transfer types with scalability.** Table 1 (wraptable) shows PICLE achieves perceptual, few-shot, and latent transfer while MNTDP-D lacks few-shot/latent transfer and LMC lacks scalability. This is quantitatively supported: on BELL's S^few, PICLE achieves +34.65 higher transfer than MNTDP-D; on latent-transfer sequences S^in and S^sp, it achieves +14.67 and +23.65 higher transfer than the PT-only ablation (Section 6).

- **Scalable search via constant path evaluations per problem.** The PT search (Section 4) evaluates at most L paths per problem, and the NT search (Section 5) evaluates at most c+L-ℓ_min-1 paths — both independent of library size. Figure 2's resource plots on CTrL's S^long confirm that PICLE's FLOPs and memory grow far slower than HOUDINI and LMC, backing the scalability claim.

- **Principled probabilistic fitness approximation.** The generative model for PT paths (Eq. 3-4) and the GP model for NT paths (Eq. 6) avoid the need to train each candidate composition, combining prior knowledge with problem-specific data. This is a structural improvement over MNTDP-D's k-NN heuristic and LMC's linear combination approach.

- **Outperforms state-of-the-art modular CL on long sequences.** On CTrL's S^long (100 problems), PICLE achieves 69.65% average accuracy vs. MNTDP-D (65.64%) and LMC (64.49%). On BELL's long sequence (60 problems), PICLE attains +12.25 higher accuracy than standalone, vs. +8.83 for MNTDP-D.

- **Introduces the BELL benchmark** — a compositional extension of CTrL with a larger and more varied problem space (O(6^8) paths), providing a stronger testbed for evaluating different transfer types than existing benchmarks.

## Weaknesses

### Fatal
None.

### Major

- **The NT model's distance function d(λ, λ') is underspecified (Section 5).** The paper defines a squared exponential kernel κ(λ, λ') = σ² exp{ -d(λ, λ')²/(2γ²) } where d is "the distance between two functions" (line 205). It then states that hidden activations are stored and "combined" into function inputs (line 207), but never specifies (a) what distance metric is used (Euclidean, cosine, L1, or something else), (b) how many hidden activations are stored, (c) how they are "combined" across modules, or (d) the exact procedure for computing the distance from these inputs. This is not a superficial omission — the kernel is the core of the GP model, and without knowing how d is computed, the method cannot be reproduced from the paper alone. The concept (distance in function space) is clear, but the implementation details required for reproducibility are missing.

### Minor

- **Scalability claim about "constant training requirements" needs qualification (Sections 5-6).** The paper's claim (line 43) refers to evaluating a constant number of compositions and training networks of fixed size — this holds for neural network training. However, the GP within the NT search fits hyperparameters on the evaluated NT paths (lines 205, 223). It is clear from context that this is per-problem (c data points, O(c³) cost), so the constant-training claim technically holds. But the paper does not explicitly clarify whether the GP is refit on the full history of all problems or only on the current problem's evaluated paths, and does not measure or report the GP's wall-clock cost. A brief clarification and timing breakdown would strengthen the paper.

- **No error bars or variance reported.** Results are reported as point estimates averaged over 3 runs (BELL) and 1-3 runs (CTrL), with no standard deviations or confidence intervals (lines 257-258). Given the modest performance differences in some comparisons (e.g., CTrL S^long: 69.65 vs. 65.64), variance information is important to assess significance.

- **Key hyperparameters (c, ℓ_min, k) are not reported.** The paper defines c (number of NT paths evaluated via BO), ℓ_min (minimum suffix length), and k (projected dimensionality) as hyperparameters (lines 160, 222-223) but does not state their values or provide a sensitivity analysis. This limits reproducibility.

- **The memory measurement in Figure 2 is unspecified.** The caption says "maximum memory required by each algorithm" but does not clarify whether this measures runtime peak memory (active parameters + activations) or total model storage (library size). PICLE's nearly flat memory curve is plausible under one interpretation but not the other.

- **Derivation of Eq. 4 from Eq. 3 is sketched but not fully shown.** The paper states that marginalizing activations yields Eq. 4 (line 145) but omits the intermediate steps. The result is plausible, but providing the derivation would improve clarity.

### Trivial
None — no typos or formatting issues are present in the extracted content.

## Nice-to-Haves

- **Ablation of PT vs. NT components.** The paper evaluates the PT-only ablation on latent-transfer sequences (Section 6), which is helpful. A full ablation showing the contribution of each model across all sequence types would further strengthen the analysis.
- **State the backward transfer limitation earlier** (e.g., Section 1). The paper correctly notes this in Section 6 (line 274); flagging it in the introduction would prevent any perception of overclaiming.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **LMC omission on BELL as a "red flag."** The harsh critic casts doubt on BELL's fairness because LMC is not reported. The paper explicitly explains (line 264) that LMC "performed worse than standalone on these sequences despite our efforts to adjust it to this setting, so we do not report it." This is an honest disclosure, not a flaw. **Removed** — the paper already addresses this.

- **GP scalability concern (that cost grows across problems).** The harsh critic speculates that GP training data might include "the full history of evaluated NT paths across all problems." Reading the paper (lines 219-224), the GP operates within a single problem's Bayesian optimization loop, accumulating at most c data points per problem — constant per problem. The claim holds. **Removed** — this is a reading error; demoted to the Minor point above about needing clarification.

- **"Strengthening the Paper on Its Own Terms" items about GP cost analysis and NT model specification.** These duplicate the Major/Minor weaknesses already listed. **Merged** into the existing weaknesses above.

- **Various generic strengths from the Strength Finder** that are generic/unsupported (e.g., general praise of importance). The strengths listed in the Strengths section above are concrete and grounded.

## Novel Insights

None beyond the paper's own contributions. The two reviews converge on the same assessment: the paper's contribution is solid and well-supported, with the main concern being the underspecified NT model distance function. The harsh critic's strongest point (reproducibility gap in the NT kernel) is real but fixable; the reviewer's other criticisms range from already-addressed (LMC omission) to clarifications (GP cost). Neither review identifies a weakness that threatens the core claims.

## Suggestions

1. **Specify the NT distance function completely.** State the exact distance metric (e.g., Euclidean distance between the outputs of the two suffixes when fed the combined set of stored hidden activations), how many activations are stored per suffix, how they are combined, and how the function output comparison is performed.
2. **Clarify the GP fitting procedure.** State explicitly that the GP is fit only on the c NT paths evaluated for the current problem, and report the wall-clock time per problem for GP inference and hyperparameter fitting (separately from neural network training).
3. **Report hyperparameter values** for c, ℓ_min, and the projection dimension k, and add a brief sensitivity study for at least c.
4. **Add error bars** (std. deviation over the 3 runs) to the main result tables, or explain why they are omitted.
