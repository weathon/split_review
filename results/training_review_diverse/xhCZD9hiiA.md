Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper proves that an MLP with batch normalization and orthogonal random weight matrices (drawn from the Haar distribution) avoids gradient explosion at initialization while maintaining orthogonalization of representations. The key contributions are non-asymptotic, finite-width theoretical guarantees: (1) exponential decay of the isometry gap with depth (Theorem 1), and (2) a depth-independent bound on expected log-gradient norms (Theorem 2), directly contradicting prior mean-field results that suggested gradient explosion is unavoidable in BN networks. The paper also presents empirical results on training stability and a heuristic activation shaping scheme for non-linear activations.

## Strengths

- **First non-asymptotic proof that gradient explosion is avoidable in BN networks.** Theorem 2 proves that the expected log-norm of per-layer gradients is bounded by a constant depending only on width and input isometry gap — with no dependence on depth — directly refuting the previously believed inevitability of exponential gradient explosion in BN networks [Yang 2019, Theorem 3.9]. This is a genuine theoretical contribution, supported by clean experimental validation (Figure 4 shows log-gradient norms staying flat for orthogonal weights while exploding for Gaussian weights).

- **Non-asymptotic, finite-width analysis with explicit rates.** Unlike prior mean-field analyses that are asymptotic in width or rely on hard-to-verify assumptions [Yang 2019, Daneshmand 2021], Theorem 1 gives an explicit exponential decay rate for the isometry gap ($\E[\IG(X_{\ell+1})] \le \IG(X_0)e^{-\ell/k}$ with $k = C d^2(1+d\,\IG(X_0))$) that holds for any finite width $d$ without taking limits. This finite-width regime is precisely the setting of practical neural networks, making the analysis more directly applicable than prior work.

- **Careful experimental validation of theoretical predictions.** Figures 1–4 systematically confirm the theoretical claims: isometry gap decay matches the predicted exponential rate, gradient norms remain flat across depth for orthogonal weights (vs. exponential growth for Gaussian weights), and degenerate inputs trigger gradient explosion while non-degenerate inputs do not. All experiments use 10 independent runs with confidence intervals.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **The $n=d$ (batch size equals width) requirement is a significant practical limitation that is not empirically tested for robustness.** The entire theory requires the input matrix to be square ($d \times d$), which means batch size must equal network width. In modern deep learning, widths are often much larger than typical batch sizes. The paper states this requirement (line 71) but does not explore whether gradient properties degrade gracefully when $n \neq d$, nor does it provide any theoretical or experimental evidence about how the bounds change when this condition is violated. For a paper with "Training Without Depth Limits" in its title, this constraint is a substantial gap between theory and practice that deserves more explicit discussion and experimental probing.

- **The activation shaping section (Section 5) is heuristic and lacks a reproducible prescription in the main text.** While the paper defines the "rate of explosion" $R(\ell, \alpha_\ell)$ and states that gains should decay "faster than a harmonic series," the main text does not provide a concrete algorithm or formula for selecting the gain $\alpha_\ell$ as a function of depth and width. The paper references Appendix~\ref{sec:shaping} for details, but a self-contained main-text prescription is missing. Since activation shaping is presented as a contribution ("we also design an activation shaping scheme"), the lack of a concrete, reproducible scheme weakens this component of the paper. The empirical evidence (Figure 5) is suggestive but does not constitute a fully specified method.

- **The theoretical guarantees hold at initialization, while the training claims are empirically supported but not theoretically justified.** Theorems 1 and 2 analyze expectations over random weight matrices drawn at initialization, yet the paper's title ("Towards Training Without Depth Limits") and Section 4 ("Implications on training") focus on training behavior. The paper acknowledges this gap ("While the SGD trajectory strongly diverges from the initial conditions that we analyze theoretically," line 214), and the training experiments are legitimate empirical contributions. However, the framing could more clearly separate what is proven (initialization properties) from what is observed (training stability) to avoid overclaiming the scope of the theory.

### Trivial
None.

## Nice-to-Haves

- Experiments systematically varying batch size and width independently ($n \neq d$) to probe how gradient behavior degrades — or whether the phenomenon is more robust than the theory requires.
- A brief comparison with alternative approaches to managing gradients in BN networks (e.g., gradient clipping, controlling BN scale parameters) to contextualize the contribution.
- Discussion of the computational cost of generating Haar-distributed orthogonal matrices for large widths, since this is more expensive than sampling Gaussian weights.
- Training experiments on higher-dimensional datasets (e.g., CIFAR100) where the width must match the batch size.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"The activation shaping lacks a formal definition of 'rate of explosion.'"** — Removed because the paper explicitly defines it as "the slope of the log norm of the gradients $R(\ell, \alpha_\ell)$" (line 243). This criticism is factually wrong.

- **"The reference to Appendix B does not help a reader who only has the main text."** — Removed because the parser strips appendices; they exist in the original submission. The substance about the main text being vague is retained in Minor Weakness #2 above.

- **"The linear network's lower accuracy undermines the practical relevance."** — Removed because the paper explicitly addresses this (line 214: "confirming that the sin and tanh networks are not operating in the linear regime"). The linear construction is a theoretical tool, not a practical recommendation.

- **"Missing comparison to gradient clipping and other competing approaches."** — Removed as scope creep. The paper's contribution is a theoretical construction and analysis, not an empirical comparison of training techniques.

- **"Only CIFAR10 experiments."** — Downgraded to Nice-to-Have. The theoretical experiments (Figures 1–4) use random data, and the training experiments on CIFAR10 are sufficient to validate the theory's implications.

## Novel Insights

Beyond the paper's own contributions, the reviews surface a useful observation about the tension between theoretical elegance and practical applicability. The paper's core finding — that orthogonal weights + BN + square batch size avoids gradient explosion — is clean and mathematically rigorous. But the $n=d$ constraint and the reliance on initialization-only guarantees create a gap between what the theory proves and what the title/presentation suggests about training. This is not a fatal flaw (every theoretical paper has assumptions), but it is a pattern worth noting: reviewers will rigorously probe whether simplifying assumptions are acknowledged and tested for robustness. The activation shaping section additionally reveals that when a paper presents a heuristic as a contribution, reviewers expect it to be concrete and reproducible, not merely suggestive.

## Suggestions

- Explicitly test and report how gradient behavior changes when $n \neq d$ (e.g., width 100, batch sizes 50 and 200) to either show robustness or honestly document degradation. This single experiment would substantially strengthen the paper.
- Provide a concrete formula for activation gains (e.g., $\alpha_\ell = 1/\sqrt{\ell}$ or similar) in the main text, not just the appendix, so the activation shaping scheme is self-contained and reproducible.
- Clarify the scope in the title and abstract: e.g., change "Towards Training Without Depth Limits" to "Gradient Stability at Initialization in Deep Batch-Normalized Networks with Orthogonal Weights" — or at minimum add a sentence in the abstract explicitly stating that the theoretical guarantees are at initialization while training results are empirical.

## Score and Decision

This is a solid theoretical paper with a genuine contribution: the first non-asymptotic proof that gradient explosion can be avoided in BN networks, with explicit finite-width bounds. The experimental validation is clean and supports the theory. The main weaknesses are the practical $n=d$ constraint (an honestly stated but underexplored limitation) and the heuristic nature of the activation shaping section. Neither is fatal — the core theoretical contribution stands on its own. The paper is well-written, clearly motivated, and addresses an important open question in the theory of deep learning.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>