## Summary

This paper derives exact closed-form solutions for the learning dynamics of two-layer deep linear networks under λ-balanced initializations ($\mathbf{W}_2^T\mathbf{W}_2 - \mathbf{W}_1\mathbf{W}_1^T = \lambda\mathbf{I}$), generalizing prior work (Fukumizu 1998, Braun et al. 2023) from the zero-balanced case ($\lambda=0$) to arbitrary λ. The authors use these solutions to characterize the rich-to-lazy learning regime transition, showing that λ controls whether learning follows sigmoidal dynamics (rich, feature-learning regime) or exponential dynamics (lazy, kernel regime), and identify a novel "semi-structured lazy" regime where one layer preserves task structure while the other is task-agnostic.

## Strengths

- **Exact closed-form solutions under the relaxed λ-balanced assumption (Theorem 1)**. The paper provides explicit analytical expressions for all four quadrants of the $\mathbf{Q}\mathbf{Q}^T$ dynamics matrix (lines 190–206), covering the network function, representational similarity matrices, and finite-width NTK. Prior work was restricted to $\lambda=0$; this is a genuine generalization with non-trivial eigendecomposition of the $\mathbf{F}$ matrix (Lemma 2).

- **Analytical characterization of the rich-to-lazy transition limits (Theorem 2)**. The paper gives precise limiting transition functions: as $\lambda \to 0$, singular value dynamics converge to a sigmoidal curve (rich regime); as $\lambda \to \pm\infty$, they converge to $1-e^{-|\lambda|t/\tau}$ (exponential/lazy regime). These limits provide a clean, quantitative handle on how relative scale interpolates between regimes.

- **Identification of a "semi-structured lazy" regime (Section 4, lines 257–278)**. The paper shows analytically that for large $|\lambda|$, one layer's RSM converges to identity (task-agnostic) while the other retains structured task-specific content scaled by $1/\lambda$. This is genuinely novel and goes beyond prior characterizations (Chizat et al., Jacot et al.) where lazy-regime representations are entirely static and unstructured.

- **Architecture-dependent lazy/rich asymmetry and delayed-rich phase (Section 4, lines 301–310)**. The analysis shows that funnel networks ($N_i > N_o$) enter the lazy regime as $\lambda \to \infty$ while inverted-funnel networks do so as $\lambda \to -\infty$, with a delayed-rich phase where the NTK initially remains static before evolving. This extends rank arguments from prior work to the multi-output setting.

- **Exact numerical validation across the λ spectrum (Figure 2)**. Analytical predictions (dotted lines) overlay numerical simulations for loss, network function, weight correlation matrices, and NTK at $\lambda=-5, 0.001, 5$ and show exact agreement.

## Weaknesses

### Major

- **The closed-form expression for the singular-value transition function $\gamma_\alpha(t;\lambda)$ at general λ is not provided.** Theorem 2 (lines 228–241) gives $s_\alpha(t) = s_\alpha(0) + \gamma_\alpha(t;\lambda)(\tilde{s}_\alpha - s_\alpha(0))$ and then states only the $\lambda \to 0$ and $\lambda \to \pm\infty$ limits. The paper's central claim is that λ controls the *continuum* from rich to lazy, but the most interpretable quantity that would show how the interpolation works for intermediate λ is absent in closed form. While the general dynamics *can* be computed from Theorem 1, the paper stops short of delivering the clean, explicit singular-value solution that would make the transition fully transparent. This is the single biggest gap between what the abstract promises and what the main text delivers.

- **The "applications" section (Section 5) is purely qualitative and adds no empirical weight to the paper's claims.** The continual learning discussion is a placeholder paragraph. The reversal learning claim (that $\lambda \neq 0$ avoids the saddle point) is stated without any quantitative demonstration—no learning curves, no timescales, no comparison to the $\lambda=0$ baseline. The transfer learning example (goldfish, "eats worms") is described in prose without supporting figures or metrics. For a paper submitted to a top venue, these sections read as speculation rather than application. They should either be moved to a "Discussion/Future Work" section or be substantiated with quantitative results.

### Minor

- **The "deep" framing is inflated for a two-layer analysis.** The title and abstract refer to "deep linear networks," but the analysis is for a two-layer network. While any network with $\ge 2$ layers is technically deep, the contribution would be more accurately scoped as "two-layer linear networks." This matters because the extension to depth $>2$ is left as future work (Discussion), and the title over-reaches relative to what is proven.

- **The relationship between λ (relative scale) and absolute-scale initialization is not fully disentangled.** The paper acknowledges (line 247) that "similar effects have been observed previously in the context of large absolute scales independently of the relative scale," but does not show a controlled comparison where λ is varied while absolute scale is held fixed vs. varying absolute scale alone. The semi-structured lazy regime is the most compelling candidate for a genuinely distinct phenomenon, but the paper could sharpen the evidence by directly comparing λ-based predictions to uniform-scaling predictions in a side-by-side experiment.

- **No error metrics are reported for the numerical validation (Figure 2).** The figure shows "exact matches" between analytical and numerical solutions via overlay, but no quantitative deviation measure (MSE, relative error, etc.) is provided. Given the acknowledged numerical instability (line 215), some validation metric would strengthen confidence.

### Trivial

- The theorem label at line 260 (`\label{theorem:singular_values_lambda}`) uses a different naming convention than the other theorem labels (`thm:singular-values`, `thm:lamdba-ballanced-dynamics`). Minor internal inconsistency.
- The abstract mentions "deep linear neural networks" while the rest of the paper uses "deep linear networks." Consistent terminology would be cleaner.

## Nice-to-Haves

- Deriving and presenting the explicit closed-form $\gamma_\alpha(t;\lambda)$ at general λ would substantially strengthen the paper's core contribution and turn the rich-to-lazy characterization from endpoint knowledge into full-spectrum knowledge.
- A direct controlled comparison (vary λ at fixed absolute scale vs. vary absolute scale at fixed λ) would cleanly demonstrate that λ is an independent control parameter beyond what prior absolute-scale theory predicts.
- Quantitative results (learning curves, timescales, comparison metrics) for the reversal learning and transfer learning claims would make the applications section substantive rather than speculative.

## Removed Points

These points were removed per filtering rules (with brief justification):

- *"Several key theorems are referenced but absent from the main text"* — The parser strips appendix content from all papers. The cross-references to `thm:internal_representations_lambda`, `thm:ntk_lambda`, and `thm:rate-delayed-rich` refer to content that exists in the original submission's appendix; per instructions, criticisms about missing appendix content must be removed.
- *"The assumptions are restrictive to the point that the 'deep' and 'wide' claims are heavily qualified" (regarding N_h = min(N_i, N_o) ruling out wide networks)* — The assumption N_h = min(N_i, N_o) does not rule out wide networks; it sets the hidden dimension to match the smaller of input/output dimensions, which is the standard minimal width for full-rank analysis. The paper honestly states this assumption.
- *"The λ-balanced initialization captures the same phenomenon as absolute-scale variation... not adequately disentangled" (as a fatal/structural issue)* — The paper provides mathematical derivations and simulations showing that λ produces asymmetric effects (which layer is lazy/rich) that absolute scale alone cannot produce. The semi-structured lazy regime is a clearly novel prediction. The critic's assertion that this is "asserted rather than demonstrated" ignores the explicit mathematical results in the paper.
- *Strength: "Reversal learning succeeds for λ ≠ 0 where λ = 0 fails"* — The paper states this claim but provides no quantitative evidence (no learning curves, no timescales, no comparison). The claim is speculative in the submitted text, not a demonstrated strength.
- *"No ablation of assumptions"* — Generic weakness request. Theoretical ablation is done through mathematical analysis of the assumptions' role, which the paper provides.
- *"Simulation details not in main text"* — Refers to appendix content stripped by parser.

## Novel Insights

The combination of the harsh critic's and strength finder's perspectives reveals a coherent picture: the paper genuinely delivers on extending the Riccati framework from zero-balanced to λ-balanced initializations (Theorem 1 is the core technical contribution), but it undersells itself by over-claiming on two fronts. First, it presents the singular-value limits as if they fully characterize the transition when the general-λ closed form would be the natural capstone. Second, it includes speculative application paragraphs that add no weight and only invite scrutiny. The paper would be stronger by either removing the applications entirely (focusing on the theoretical contribution) or substantiating them. The "semi-structured lazy" regime is genuinely novel and does not follow trivially from prior absolute-scale work—this is the paper's most interesting conceptual finding and deserves more emphasis.

## Suggestions

1. **Provide the general-λ expression for $\gamma_\alpha(t;\lambda)$** in Theorem 2, or explicitly state that the singular-value dynamics at general λ can be derived from Theorem 1 and give the derivation in the main text (not just the appendix).
2. **Remove or substantially expand the applications section.** If the paper is a theory paper, state it as such. If the applications are intended as contributions, provide quantitative simulations with baselines.
3. **Tone down the "deep" framing** in the title and abstract to "two-layer linear networks" to match what is actually proven, or add a clear statement that deeper extensions are future work.
4. **Add a direct comparison experiment** that varies λ while fixing absolute scale, and vice versa, to explicitly demonstrate λ's independent role.
5. **Report quantitative error metrics** for the numerical validation in Figure 2 (e.g., relative MSE between analytical and numerical trajectories).

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>