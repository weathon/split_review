Now I have all the information needed. Let me write the final consolidated review.

## Summary

This paper introduces PICLE, a modular continual learning framework that uses probabilistic models to estimate the fitness of module compositions without requiring full training. It distinguishes between perceptual/few-shot transfer (PT paths, evaluated via a probabilistic model over module inputs) and latent transfer (NT paths, evaluated via a Gaussian process over pre-trained suffixes). Experiments on the CTrL benchmark and a new BELL compositional benchmark show that PICLE outperforms prior modular CL methods, achieving perceptual, few-shot, and latent transfer simultaneously while maintaining scalability.

## Strengths

- **Probabilistic fitness proxy avoids expensive training**: The core idea—replacing full training of each module composition with a cheap probabilistic fitness estimate—directly addresses the scalability bottleneck in modular CL. The PT search evaluates only *L* paths per problem (constant in library size), and the NT search evaluates at most *c* + *L* − ℓ_min − 1 paths. This is the key mechanism that avoids the exponential blowup that plagued prior methods (Section 4, §"Search Strategy and Scalability"; Section 5, §"Search Strategy and Scalability").

- **First modular CL algorithm to simultaneously demonstrate perceptual, few-shot, and latent transfer with scalability**: Table 1 and the BELL/CTrL experiments show PICLE is the only modular method that checks all three boxes. On BELL's *S*^few, PICLE achieves +34.65 transfer over MNTDP-D; on *S*^in and *S*^sp, it achieves +14.67 and +23.65 transfer over the PT-only ablation. On the 100-problem CTrL *S*^long, PICLE attains 69.65 average accuracy vs. 65.64 for MNTDP-D and 64.49 for LMC. Figure 2 confirms PICLE maintains low and stable FLOPs/memory throughout long sequences, unlike HOUDINI and LMC whose costs grow sharply.

- **Novel GP-based model for latent transfer**: The NT search introduces a Gaussian process prior with a kernel based on function-space distance between pre-trained suffixes. Using UCB-based Bayesian optimization to predict the performance of untrained NT paths is a new technique in modular CL (Section 5).

- **Efficient approximation of module input distributions**: The use of random projections to a low-dimensional space followed by a multivariate Gaussian fit reduces parameter count from *O*(*v* + *v*²) to *O*(*k* + *k*²) with *k* ≪ *v*, making the PT model computationally feasible (Section 4).

- **Performance-based prior improves transfer**: The PT model incorporates a prior proportional to validation accuracy on the original task. On the difficult *S*^out** sequence, PICLE achieves +10.33 higher transfer than MNTDP-D, attributed to this prior (Section 6).

## Weaknesses

### Fatal

None.

### Major

- **PT posterior approximation (Equation 4) lacks a clear derivation**. The paper starts from the joint distribution (Equation 3) and claims to marginalize out activations, but Equation 4 contains a normalization term of the form p(**h**^(i−1)|*m*^i) / Σ_{*m*∈L_i} p(**h**^(i−1)|*m*)p(*m*) whose appearance is not derived step-by-step. While the equation is explicitly labeled an "approximation" (the tag reads `approximation`), the paper does not explain why this particular form is justified or how it arises from a proper marginalization. Since the entire PT search strategy depends on this posterior, the lack of a sound derivation or clear heuristic justification weakens confidence in the method's theoretical grounding. This is fixable—the authors can either provide a rigorous derivation or explicitly state and empirically validate a heuristic—but in its current form it is a significant omission.

- **The NT kernel and distance function are underspecified, hurting reproducibility**. The kernel uses a distance *d*(λ, λ′) between two pre-trained suffixes "in function space," but the paper never specifies: (a) what distance metric is used (Euclidean? L1? cosine? something else?), (b) how functions are evaluated on the constructed set of inputs, and (c) how hidden activations from different problems are combined to form the function input set. The kernel hyperparameters σ and γ are said to be fit via marginal likelihood maximization (line 205), which is standard, but the core distance computation—essential to defining the GP model—remains unspecified. This must be clarified before the NT component can be correctly implemented or assessed.

### Minor

- **Limited statistical rigor in experimental evaluation**. BELL results are averaged over only 3 sequence versions (line 257–258) with no confidence intervals, error bars, or standard deviations reported. While the observed improvements are large (e.g., +34.65 transfer on *S*^few), the thin statistical basis weakens the persuasiveness of the central claims. Similarly, CTrL results do not report variance despite stochastic sequence construction. Additional runs or error bars would meaningfully strengthen the evidence.

- **Random Search (RS) baseline results are not systematically reported**. RS is listed as a baseline (line 236) and mentioned in passing for *S*^sp (line 272) and in Table 1, but no quantitative results for RS appear across sequences. Given that RS can in principle achieve all transfer types (just not efficiently), reporting its performance would clarify whether PICLE's advantage is substantive or an artifact of search space properties.

- **Scalability analysis focuses narrowly on training cost while the search itself has growing costs**. The paper correctly states that "training requirements are constant" (line 43), but the PT search computes posteriors over all modules in each layer (O(\|L^i\|) per layer), and the NT Bayesian optimization considers a growing set of previous solutions. While these costs are cheap relative to training, omitting any discussion of search cost growth makes the scalability claims feel incomplete.

- **No discussion of limitations**. The paper does not discuss when PICLE might fail: e.g., when the Gaussian input distribution assumption is violated, when the best NT suffix is not a substring of a previous solution (a restriction the paper acknowledges but does not analyze), or when training distributions shift drastically. A dedicated limitations paragraph would improve the paper's credibility.

- **Table 1 criteria are not operationally defined**. The checkmarks for "few-shot transfer" and "latent transfer" appear to reflect whether methods *demonstrated* these properties in the specific experimental setup, not whether they *can* in principle. This conflation could mislead readers about the generality of the comparison.

### Trivial

- The description of how the initial NT candidate is chosen for Bayesian optimization (the first evaluated path) is not specified. This is a small implementation detail that should be clarified.
- The BELL benchmark description in the main text is brief but acceptable given the appendix.

## Nice-to-Haves

- An ablation that removes the GP component from NT (e.g., using only the prior over suffixes) would help isolate the benefit of the GP model and strengthen the claim that the GP enables latent transfer.
- Sensitivity analysis for key hyperparameters (the rank *k* in the Gaussian approximation, the minimum suffix length ℓ_min, and the BO budget *c*) would help practitioners understand trade-offs.
- A discussion of how the random projection dimension *k* was chosen and evidence that the Gaussian approximation is faithful enough to be useful would strengthen the PT component.

## Removed Points

These points were identified in the reviewer inputs but are removed or downgraded per the rules. Treat them with caution.

1. **"The claim that PICLE is the first to achieve all three transfer types is an overclaim"** — Removed. The paper's claim is about *existing modular CL algorithms as evaluated*, not about hypothetical adaptations of other approaches. Table 1 and the experimental comparisons support the claim that among *existing* modular CL methods, PICLE is the first to demonstrate all three properties with scalability.

2. **"The paper should cover Y / domain Z / additional tasks"** — Removed as scope creep. The paper focuses on the task-aware, data-incremental supervised setting and benchmarks designed to test specific CL desiderata; demands for additional domains or settings would constitute a different paper.

3. **Pure formatting, style, or grammar nitpicks** — Removed per hard rules (parser artifacts, not author errors).

4. **"The paper does not prove no other approach could be adapted to achieve all three transfer types"** — Removed as a strawman. The paper compares against existing methods as they are, not hypothetical adaptations.

## Novel Insights

The reviews surface two key insights beyond the paper's own contributions. First, the PT posterior approximation occupies an uneasy space between "principled derivation" and "heuristic"—the paper calls it an approximation but does not clearly tag it as a heuristic design choice or provide a step-by-step derivation. Clarifying this would strengthen both the methodology and the reader's trust. Second, the NT kernel's distance function is the linchpin of the GP model's expressiveness, yet it is the least specified component in the paper. The contrast between the high-level innovation (GP for latent transfer in modular CL) and the underspecified implementation details suggests a pattern where the "what" is clear but the "exactly how" needs substantive expansion for reproducibility.

## Suggestions

1. **Derive or clearly justify the PT posterior (Eq. 4).** Show the marginalization steps explicitly, or state clearly that it is a heuristic approximation and provide empirical validation (e.g., compare posterior rankings to actual path performance on a held-out set).

2. **Fully specify the NT kernel distance function.** Provide the exact formula for *d*(λ, λ′), including the metric used, how function outputs are computed from stored activations, and how inputs from different problems are combined.

3. **Report confidence intervals or variance across runs** for at least the key BELL and CTrL sequences to demonstrate statistical significance.

4. **Include RS baseline results quantitatively** across all sequences to confirm that PICLE's advantage is not merely due to a favorable search space.

5. **Acknowledge and bound the search cost** (posterior evaluations for PT, GP inference for NT) in addition to the training cost, to give a complete picture of scalability.

## Score and Decision

The paper addresses an important problem and proposes a clever, novel solution with strong empirical results. However, two structural issues—the unclear derivation of the PT posterior and the underspecification of the NT kernel/distance—undermine confidence in the methodology and reproducibility. These are fixable but constitute real gaps in the current submission. The experimental evidence, while supportive, would also benefit from greater statistical rigor.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>