Now I have a thorough understanding of the paper. Let me write the final consolidated review.

---

## Summary

This paper presents a theoretical framework that explains dynamical simplicity bias — the tendency of gradient descent to learn solutions of increasing complexity — across multiple neural network architectures. The framework comprises: (i) a rigorous static analysis showing that fixed points and invariant manifolds are embedded hierarchically across widths for a general class of networks (Theorems 1–3, covering fully-connected, convolutional, and self-attention layers); (ii) a heuristic dynamic analysis disentangling two distinct mechanisms for timescale separation — data-induced (producing low-rank weights) vs. initialization-induced (producing sparse weights); and (iii) empirical validation of the framework's predictions about how width, data distribution, and initialization affect saddle-to-saddle dynamics.

## Strengths

- **Unified static framework across architectures (Theorems 1–3, Corollary 2):** The paper proves that embedded fixed points and invariant manifolds exist for a general class of networks defined by Equation (1), encompassing fully-connected, convolutional, and attention-based layers. Theorem 1 extends Fukumizu & Amari (2000) by adding cases (iii) and (iv) for homogeneous and linear activations — which the paper argues are precisely the saddles visited during learning. Theorem 3 provides the invariant manifold construction, and Corollary 2 extends the hierarchy to deep networks.

- **Novel disentanglement of two timescale separation mechanisms:** The distinction between *data-induced* timescale separation (Section 5.1, Theorem 4 — distinct singular values of the input-output correlation matrix drive rank-ordered weight growth across all units) and *initialization-induced* timescale separation (Section 5.2, Proposition 5 — distinct random initial values drive sequential unit recruitment) is a genuinely insightful conceptual contribution. This cleanly explains why linear networks develop low-rank weights while quadratic/self-attention networks develop sparse weights, and makes differential predictions about the effects of width and data distribution.

- **Predictive implications confirmed empirically:** The theory makes non-obvious, testable predictions: (a) increasing width shortens plateaus for quadratic/self-attention networks but not linear networks (Figure 2A); (b) equalizing data singular values eliminates plateaus in linear networks but only shortens them in self-attention (Figure 2B); (c) initializing near invariant manifolds but away from saddles still yields saddle-to-saddle dynamics (Figure 2C); (d) the ordering of singular values predicts plateau durations on MNIST (Table 1, Figure 3). These differential predictions across architectures are a strong demonstration of the framework's explanatory power.

- **Constructive extension of prior theory:** Cases (iii) and (iv) in Theorem 1 are new and turn out to be the ones relevant for learning dynamics, unlike the previously known cases (i) and (ii). This closes an important gap in the Fukumizu & Amari line of work.

- **Clarity of exposition:** The conceptual diagram (Figure 1A) and the architecture-spanning experiments (Figure 1B–G) effectively communicate the intended mechanism. The paper is well-structured, with the static analysis (Sections 3–4) cleanly separated from the dynamic analysis (Section 5) and implications (Section 6).

## Weaknesses

### Fatal

None.

### Major

- **Gap between rigorous static analysis and heuristic dynamic analysis:** The static analysis (Theorems 1–3, Corollary 2) is rigorous and applies to the full class of architectures defined by Equation (1). However, the dynamic analysis (Section 5) that connects these static structures to actual gradient flow trajectories is heuristic and restricted to two-layer networks with linear or quadratic activations. The paper is transparent about this (explicitly calling the arguments "heuristic" on line 375, and acknowledging "the analysis of dynamics in Section 5 only applies to two-layer networks" on line 715–716), but the title ("Saddle-to-Saddle Dynamics Explains a Simplicity Bias Across Neural Network Architectures") and abstract overstate what has been rigorously demonstrated. The framework provides a *plausible mechanism* rather than a *proven explanation* for the full architectural range. This does not invalidate the contribution but means the paper's claims should be understood as a framework with proven static components and heuristic dynamic components, not a complete rigorous theory.

### Minor

- **Dynamic analysis is limited to two-layer networks with linear/quadratic activations:** While the fixed-point and invariant-manifold results (Sections 3–4) are general, the actual dynamics are analyzed only for the two-layer linear case (Theorem 4) and two-layer quadratic case (Proposition 5). Deep network dynamics are conjectured (Section 7) and simulated (Figure 5) but not analyzed. The paper acknowledges this limitation clearly, so this is a scope limitation rather than a flaw.

- **Self-attention analysis covers linear self-attention only:** The dynamics in Section 5.2 apply to linear self-attention (no softmax). Softmax self-attention appears only in a single appendix simulation (Figure 4A) with no theoretical underpinning. The body text is largely accurate about this (using "linear self-attention" consistently), but the abstract's reference to "attention-based architectures" without qualification slightly over-promises relative to what is analyzed. This is a scope limitation.

- **Empirical validation is primarily illustrative:** The experiments in Figures 1–4 use synthetic data with hand-chosen singular value spectra. The MNIST experiments (Figure 3, Table 1) provide a step toward realism and do include quantitative evidence (singular value growth coinciding with loss drops), but the validation remains at the level of qualitative demonstration. Systematic measurement of predicted plateau durations across multiple data conditions, or experiments on more challenging tasks (e.g., CIFAR-10), would strengthen the empirical case. That said, for a primarily theoretical paper, the level of empirical validation is reasonable.

### Trivial

None beyond parser artifacts (spacing, equation rendering), which are not author errors.

## Nice-to-Haves

- Quantitative metric for plateau durations compared against theoretical predictions (e.g., based on singular value gaps or initialization gaps) would strengthen the empirical case.
- Extension of the dynamic analysis to deep networks or to softmax attention, even partially, would substantially close the gap between the framework's scope and what is rigorously established.
- Analysis of architectures with residual connections and layer normalization, which are standard in modern transformers, would enhance practical relevance.
- A phase diagram showing where saddle-to-saddle vs. lazy vs. mixed behavior occurs as a function of initialization scale and data spectrum.

## Removed Points

*These points were flagged for removal — treat them with caution:*

- **"The paper's central claim is not supported by its analysis"** — This overstates the problem. The paper has two components: (1) a rigorous static analysis (Theorems 1–3) that IS proven for the general class of architectures, and (2) a heuristic dynamic analysis (Section 5) for specific cases. The paper is honest about which parts are proven vs. heuristic. The contribution is a framework combining both, not a fully rigorous dynamical theory. The title and abstract over-claim somewhat, but the core static contributions are genuine and well-supported.

- **"The definition of simplicity for ReLU networks is underdeveloped"** — The paper defines simplicity as "expressible with few hidden units" consistently across all architectures. For ReLU networks, the invariant manifolds of Theorem 3(iii) (proportional weights) provide the formal link: when ReLU weights satisfy θ_i = γ θ_j, the network is expressible with one fewer unit. The "kinks" language in the abstract is informal but backed by this formal mechanism.

- **"No quantitative metric ties the observed plateaus to the effective-width transitions predicted by the theory"** — Table 1 and Figure 3 do provide this for the MNIST experiments: singular value growth coincides with loss drops, and the singular values approximately match plateau durations. The paper also explicitly ties predicted effects of width (Figure 2A), data distribution (Figure 2B), and initialization (Figure 2C–D) to the theory.

- **"The empirical support is only illustrative; it does not validate the framework"** — While the experiments are indeed illustrative, this characterization understates their role. The experiments test specific differential predictions of the theory (e.g., width affects linear and quadratic networks differently) and confirm them. For a primarily theoretical paper, this level of validation is appropriate. The paper does not claim large-scale empirical validation.

- **"The simulations in Figures 1–4 use artificially constructed toy datasets"** — True but expected for a theory paper. The MNIST experiments (Figure 3) partially address this.

- **Various formatting/typographical issues** — These are PDF parser artifacts, not present in the original submission.

- **Missing related works** — Not evaluated as per instructions.

- **"No statistical evidence or systematic study across multiple data conditions is provided"** — The paper is primarily theoretical; the experiments serve as demonstrations of the theory's predictions. Demanding systematic empirical studies from a theory paper is scope creep.

- **"Extension to residual connections and layer normalization"** — This is scope creep. The paper explicitly scopes its analysis to feed-forward layers defined by Equation (1). The Discussion mentions skip connections as a future direction.

## Novel Insights

Beyond the paper's own contributions, the reviews highlight a structural tension common in deep learning theory: the difficulty of bridging rigorous static analyses (fixed points, invariant manifolds) with dynamic analyses of gradient flow. The paper's approach — proving static structure for a broad class and then analyzing dynamics heuristically for tractable sub-cases — represents a pragmatic strategy. The disentanglement of data-induced vs. initialization-induced timescale separation is the most conceptually novel insight, as it provides a unifying lens for understanding why different architectures exhibit qualitatively different forms of simplicity bias (low-rank vs. sparse) while sharing the same underlying saddle-to-saddle mechanism.

## Suggestions

- **Tone down the title and abstract claims** to more accurately reflect what is proven vs. what is argued heuristically. For example: "A Unified Framework for Saddle-to-Saddle Dynamics and Simplicity Bias Across Architectures" or similar, with the abstract clarifying that the static analysis is rigorous and the dynamic analysis is developed for tractable cases with heuristic extensions.
- **Add a limitations subsection** early in the paper (e.g., at the end of the introduction) explicitly itemizing what is proven (Theorems 1–3, Corollary 2), what is analyzed heuristically (Section 5 dynamics), and what is conjectured (deep networks, higher-order activations). The Discussion already does some of this, but front-loading it would manage reader expectations.
- **Include a quantitative metric in the main experiments** (e.g., ratio of predicted vs. actual plateau duration for the MNIST experiments in Figure 3) to strengthen the empirical case without requiring large-scale experiments.

Now, calibration against anchors to determine the score.

## Score Calibration

**Anchor papers retrieved:**

| Path | Avg Score | Comparison to Paper Under Review |
|------|-----------|----------------------------------|
| `/home/wg25r/review_agent/human_reviews_2026/B4zcoLvjw0.md` | 6.00 | Saddle-to-saddle in deep ReLU networks. Has a rigorous theorem about the first saddle escape but is narrower in scope (one architecture, one phase of dynamics). The current paper has broader scope (multiple architectures, full saddle sequence) but less rigorous dynamics. Comparable quality. |
| `/home/wg25r/review_agent/human_reviews_2026/oqP3qkHAsA.md` | 3.50 | Bias-mediated linearization in ReLU nets. Rejected for weak theoretical support and limited novelty. The current paper is clearly stronger — it has rigorous theorems and a unified framework. |
| `/home/wg25r/review_agent/human_reviews_2026/YgudIlQ9nC.md` | 3.50 | Steepest mirror flows for saddle escape. Narrower scope, focused on optimization algorithm choice. The current paper is more ambitious and has broader architectural coverage. |
| `/home/wg25r/review_agent/human_reviews_2026/qBAV2DEvAC.md` | 5.50 | Implicit bias and neural scaling laws. Empirically richer but theoretically less unified. The current paper is comparably strong but trades empirical breadth for theoretical unification. |
| `/home/wg25r/review_agent/human_reviews_2026/b36drMoKir.md` | 0.50 | Gradient flow convergence — fundamentally flawed proof. The current paper is vastly superior; its static proofs are correct and well-structured. |
| `/home/wg25r/review_agent/human_reviews_2026/IlyesljaNb.md` | 6.00 | Intrinsic training dynamics. Rigorous theory about gradient flow reparameterization, applied to ReLU and linear networks. Comparable in quality and scope — both provide theoretical frameworks for understanding neural network training dynamics. |
| `/home/wg25r/review_agent/human_reviews_2026/xa3oLRQG55.md` | 4.00 | Diagram expansions for gradient flow. Novel approach but limited applicability. The current paper is more directly relevant and has clearer practical implications. |
| `/home/wg25r/review_agent/human_reviews_2026/SaJ9fn3PdL.md` | 3.50 | Unifying low-dimensional observations. Rejected for overclaiming and limited novelty. The current paper is stronger — more novel, better executed. |
| `/home/wg25r/review_agent/human_reviews_2026/cmuHsIGlqC.md` | 3.00 | Sharpness of minima in deep matrix factorization. Narrow theoretical result. The current paper has broader scope and more implications. |

**Positioning:** The paper under review is most comparable to B4zcoLvjw0 (6.00) and IlyesljaNb (6.00). Like B4zcoLvjw0, it studies saddle-to-saddle dynamics with a mix of rigorous and heuristic analysis. It is broader in scope (covering multiple architectures rather than just ReLU) but less rigorous in its dynamic analysis. Like IlyesljaNb, it provides a theoretical framework for understanding training dynamics across architectures. The current paper's static analysis is rigorous and valuable; the dynamic analysis is heuristic but well-motivated and empirically supported. The paper is clearly stronger than the 3.0–4.0 range papers and clearly not in the 0.5 range. Compared to the 6.0 anchors, the paper's ambition and scope are similar or greater, but the heuristic nature of the dynamics analysis tempers the contribution. **Score: 6.0**.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>