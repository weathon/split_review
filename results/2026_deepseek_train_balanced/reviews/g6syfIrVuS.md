Now I have thoroughly verified the paper content against all reviewer claims. Let me write the consolidated review.

## Summary
This paper derives the maximal update parameterization (μP) for two families of local learning algorithms — Predictive Coding networks and Target Propagation — in the infinite-width limit. It provides closed-form fixed-point solutions for PC in linear networks, shows that PC's gradient interpolates between first-order GD and GNT-like updates depending on parameterization, and discovers that TP eliminates the kernel regime (b_L=1/2 induces feature learning rather than kernel behavior). Experiments on FashionMNIST verify μTransfer across widths.

## Strengths
- **Explicit μP for PC without the Fixed Prediction Assumption (Theorem prop:mup-pc).** Prior work required FPA to connect PC to BP; this paper derives μP without it, using a perturbation argument that treats both learning rate and inference step size as infinitesimal parameters (Eq. 269). The empirical verification (Figure 1, right) shows that μTransfer holds even without FPA, which is a nontrivial result.

- **Closed-form fixed-point solution for PC in deep linear networks (Theorem thm:linear-pc).** The explicit solutions for e_l^* and v_l^* (Eqs. 322–326) go substantially beyond the previously known approximate fixed-point equation (Eq. PCTP), providing exact characterization of when PC reduces to GD versus GNT. This enables the paper to show that C_γ = O(1/M) in the infinite-width limit, so PC's gradient converges to GD under standard scaling.

- **Discovery that TP eliminates the kernel regime.** Theorem prop:mup-tp yields b_L=1/2 for TP, which would normally induce a kernel regime in BP. The paper demonstrates rigorously (Section 5.2) that because TP's gradient depends on the feedback weights Q^*_L (a regression of the last layer on the downstream layer) rather than on W_L itself, the dependence between W_L and Δh_{L-1} vanishes, causing α=1/2 (CLT scaling) instead of α=1. This forces r ≤ 0, making the kernel regime impossible. Figure 8 (right) empirically confirms ω_L stays at 1/2 across widths. As the paper correctly notes (line 479), this appears to be the first example where b_L=1/2 induces feature learning rather than kernel behavior.

- **Systematic derivation framework extended to local learning.** The paper extends Yang et al.'s perturbation approach (previously used only for BP gradient methods) to jointly handle learning rate and inference step size as infinitesimal parameters. This framework is reusable for analyzing other local learning algorithms with inner-loop dynamics.

## Weaknesses

### Major
None.

### Minor
- **Experimental validation is limited to a single dataset.** All experiments use FashionMNIST (3-layer MLP or CNN with tanh). While the paper's primary contribution is theoretical and the experiments serve to verify μTransfer, the claim of providing a "solid foundation for the further development of local learning schemes in large-scale neural networks" (line 35) would be strengthened by at least one additional dataset (e.g., CIFAR-10) demonstrating that the μTransfer finding is not dataset-specific. This is not a fatal issue for a theory paper, but it limits the strength of the practical claims.

- **No statistical reporting in experiments.** The paper does not report multiple seeds, error bars, or variance estimates. All empirical claims (Figures 1, 2, 5, 6, 7, 8, 9) rest on single-curve plots. For claims about optimal hyperparameter transfer and trends across widths, basic variance information would substantially increase confidence that the observed patterns are reliable rather than artifacts of a single run. This is a standard expectation even for illustrative experiments in theory papers.

- **The PC→GD convergence tension could be discussed more explicitly.** The paper shows (Corollary following Theorem 3.3) that PC's gradient reduces to GD in the infinite-width limit under standard γ_L=Θ(1) scaling, and even for γ_L=Θ(M) the GNT direction is close to GD (Figure 3, cosine similarity plots). While the paper does acknowledge this (lines 339–340: "it is important to highlight that GNT behaves similar to GD in the infinite-width limit"), it does not discuss what this implies for the practical motivation of using PC in wide networks. If PC's extra inference machinery collapses to GD asymptotically, the biological-plausibility or architectural-flexibility arguments for PC would still stand, but the paper could clarify this point. This is a framing suggestion, not a flaw in the results.

- **The TP derivation assumes linear feedback networks trained to the pseudo-inverse solution** (line 423: "Consider a linear feedback network"; line 437: Q_l^* = h_{l-1}(h_l^⊤ h_l + μI)^{-1}h_l^⊤). The paper acknowledges this assumption. However, it would strengthen the paper to test whether the no-kernel-regime finding is robust to (a) violations of this assumption during training or (b) nonlinear feedback. This is noted as a limitation (Section 6) but not empirically examined.

### Trivial
- The figure captions do not explicitly state the range of widths tested (e.g., M = 64, 128, 256, 512, 1024). While filenames contain "1024," the full set of widths should be stated in the main text or captions for clarity.

## Nice-to-Haves
- Adding error bars / multiple seeds to the core μTransfer plots (Figures 1, 7) would significantly strengthen the empirical contribution with minimal effort.
- A small-scale test of whether the TP no-kernel-regime finding (b_L=1/2 induces feature learning) holds under nonlinear feedback would increase confidence in the result's practical relevance.
- The paper could briefly discuss the rate at which PC's gradient approaches GD as width increases, to clarify the finite-width regime where PC's additional machinery provides non-negligible benefit.

## Removed Points
The following points from the inputs were removed per the filtering rules:
1. **"No code release is mentioned"** — Removed per hard rule: nitpicks about reproducibility artifacts impractical to include in a submission (code release is not part of the reviewable content).
2. **"The relationship between the linear-network analysis and the nonlinear experiments is not fully bridged (quantitative match not verified)"** — Removed because the paper's linear-network analysis is used for theoretical insight (exact fixed-point solutions), not as a quantitative predictor of nonlinear dynamics. The paper does empirically compare PC's gradient to BP's gradient in nonlinear networks (Figure 3, right), bridging the qualitative connection.
3. **"Experimental evidence too thin" framed as a fatal/critical issue** — Removed the "fatal" framing. The paper's primary contribution is theoretical; the experiments verify theoretical predictions. The limited scope is a minor weakness, not a critical one.
4. **Several strength-finder strengths that were generic** — Removed generic/superficial strengths (e.g., "perturbation method extended to handle inference dynamics" — this is already covered by the core strengths and is a methodology detail rather than a separate contribution; "stability condition for inference phase" — this is a derived consequence of the theory, not an independent strength; "clarifies PC–GNT connection" — this is entailed by the linear-network solution and is not a separate contribution).
5. **Harsh critic's framing of PC→GD as "undercutting stated motivation"** — Weakened to a minor/framing issue because the paper does address this finding (lines 330–340) and presents it as a characterization rather than a failure. The paper's motivation is to derive stable parameterization, not to show PC outperforms BP.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
- Add at least one additional experiment on a harder dataset (e.g., CIFAR-10 with a small CNN) to demonstrate that the μTransfer property generalizes beyond FashionMNIST. Even a single figure would substantially increase the credibility of the practical claims.
- Report all μTransfer experiments with 3–5 random seeds and show mean ± std in the plots. This is standard practice even for verification experiments and would eliminate the concern about single-run artifacts.
- Explicitly discuss the PC→GD convergence result as a framing issue: clarify whether the biological-plausibility motivation for PC is independent of the gradient's limiting form, and what finite-width benefits persist.

## Score and Decision
MY FINAL SCORE: <score>7</score>
MY FINAL DECISION: <decision>Accept</decision>