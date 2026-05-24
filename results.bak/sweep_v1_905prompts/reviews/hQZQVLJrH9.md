Now I have solid calibration. Let me synthesize the final review.

**Round 1 bracket**: I initially estimated this paper sits between 5.0 and 7.0 based on the bracketing pass. The weak anchors (~3.0) are incremental empirical papers with no theoretical depth; the middle anchors (5.0-7.0) have theoretical contributions but incomplete validation; the strong anchors (~8.0) are about fundamentally different topics.

**Round 2 narrowing**: I focused on the 4.5-7.5 range. The most comparable paper is the conceptor-based steering paper (avg 5.0), which proposes a theoretical framework for steering but has unclear presentation and limited experiments. A steering paper with a theoretical framework (avg 5.5) also provides a useful comparison. The current paper is stronger than these in theoretical rigor and novelty of the core idea (steering↔influence duality), but shares similar weaknesses in empirical completeness.

Let me now write the final review.

Some notes on filtering the reviewers' points:

**Harsh Critic - Critical Issue 1 (generalization bound mismatch)**: This is legitimate. Theorem 6.1 describes $\tilde{f} = f_\theta + \alpha UV^\top$ - a rank-k weight perturbation - while the rest of the paper is about activation-vector steering. The proof sketch says "IAS changes only a rank-k submatrix of the layer weight" without justification. This is a genuine disconnect. **Keep as Major.**

**Harsh Critic - Critical Issue 2 (slope 1.5)**: The paper reports cosine 0.978 and slope 1.50 without discussing the slope. This is a valid concern but the harsh critic overstates it. A slope of 1.5 doesn't "undermine the credibility" - it shows a strong linear relationship, just a scaled one. The paper should discuss this, but it's not fatal. **Keep as Minor** (the paper should explain this, but the high cosine still supports the claim).

**Harsh Critic - Critical Issue 3 (no provenance experiment)**: Valid. The paper advertises data provenance as a key contribution but never demonstrates it. **Keep as Major.**

**Harsh Critic - Critical Issue 4 (generalization bound)**: Same as Issue 1. Already covered.

**Harsh Critic - Eq. (2) inconsistency**: The harsh critic says the equation is wrong. Looking at it carefully: the paper writes $\Delta h^* = \mathbf{J}_{h \rightarrow y}^\top \mathbf{J}_{\theta \rightarrow y} \Delta \theta$, but the correct expression should involve the pseudoinverse. This is a genuine error in the equation as written (though Theorem 5.2 later gives the correct form). **Keep as Minor.**

**Harsh Critic - Theorem 4.2 construction**: The harsh critic says the construction of $\rho_s$ is not explicit. The paper says "the measure $\rho_s$ constructed in Eq. 4" but Eq. 4 is just the theorem statement, not a construction. This is a valid point. **Keep as Minor.**

**Harsh Critic - Detoxification comparison**: The paper shows IAS slightly worse than CAA without comment. **Keep as Minor.**

**Harsh Critic - Fig 3 interpretation**: The connection between $\Sigma$ and the plotted quantity is unclear. Looking at the figure description: "Spectral radius of Xc^T diag(y) Xc" - this is not the same as the eigenvector of Σ. Valid concern. **Keep as Minor.**

**Strength Finder points to filter**:
1. "Closed-form duality" - This is genuine and specific. **Keep.**
2. "Empirical validation of first-order equivalence" - Cosine 0.978 is real but the slope issue tempers it. **Keep but note the caveat.**
3. "Necessary and sufficient condition for perfect steering" - The γ diagnostic is genuinely useful. **Keep.**
4. "Spectral recipe for optimal steering" - This is a real contribution. **Keep.**
5. "Generalization guarantees" - Tainted by the disconnect issue. **Remove** (this strength conflicts with the verified weakness).
6. "No-free-lunch lower bound" - This is a valid theoretical result. **Keep but with note about Section 6 context.**
7. "Practical workflow with low computational overhead" - This is specific and grounded. **Keep.**

Let me check: "Generalization guarantees" conflicts with verified weakness that Section 6 is disconnected. So I remove it per the rules.

Actually, hold on. The strength finder says about the generalization bound: "The Rademacher bound shows that a rank‑k IAS correction adds at most αL√(2k/(dn)) to the empirical complexity." But the harsh critic correctly points out that this bound is about weight editing, not activation steering. So this strength is based on a premise that's questionable. I'll **remove** it.

Let me also consider the "No-free-lunch lower bound" - Theorem 6.2. This is different from Theorem 6.1 - it's about the activation steering regime directly (it bounds the ratio of activation-space effects to parameter-space effects). This is cleanly about activation steering and doesn't have the weight-editing issue. So I'll keep this strength.

Now, about the "practical workflow" strength: the paper claims low computational cost, but the harsh critic points out that computing Σ requires inverse-Hessian-vector products. Let me check: the paper says "two backward passes per input" for the basic IAS computation, but the spectral recipe (Theorem 5.3) requires power iteration with inverse-Hessian-vector products. So the "low computational overhead" claim needs qualification. I'll keep the strength but with caveat.

Let me also apply the "strength finder vs weakness" rule: "If a strength conflicts with a verified weakness, the weakness wins." The "practical workflow" strength claims low overhead, which is partially true for basic IAS but not for the spectral recipe. I'll keep this as a qualified strength.

OK, let me write the review now.Now I have all the information needed. Let me write the final consolidated review.

## Summary
The paper establishes a first-order equivalence between activation steering (adding vectors to hidden states) and influence functions (re-weighting training data). It introduces Influence-Aligned Steering (IAS), a closed-form construction connecting these two previously separate techniques, along with an alignment diagnostic γ that quantifies when steering can faithfully reproduce influence effects, and a spectral recipe for optimal steering directions. The core theoretical contribution — the steering↔influence duality — is novel and fills a genuine gap in the interpretability literature.

## Strengths
- **Closed-form duality between steering and influence (Theorem 4.2)**. The paper constructs a signed measure ρₛ over training examples such that any steering vector of magnitude α induces the same first-order logit shift as re-weighting examples by ρₛ, with ‖ρₛ‖₁ = |α|. This is the first constructive map connecting these two lines of work. The converse direction (any influence weighting admits a steering vector) is also proved.

- **Alignment diagnostic γ (Theorem 5.1)**. The paper derives a scalar γ(x) — the smallest principal angle between the activation and parameter Jacobian subspaces — and proves that the relative logit error of the optimal steering vector is bounded by √(1−γ(x)²). This gives practitioners a quantitative feasibility test for when steering can work, which prior work lacks entirely. The empirical validation (Figure 2) shows γ increasing from 0.64 (layer 0) to 0.94 (layer 11) in GPT-2 Medium, confirming the diagnostic behaves as expected.

- **Spectral optimality under a norm budget (Theorem 5.3)**. The paper shows that the top eigenvector of a Fisher-influence matrix Σ maximizes expected first-order logit change, with a power-iteration algorithm that uses mini-batches. This replaces ad-hoc direction searches with a principled optimization. The ImageNet experiment (Figure 3) provides initial validation.

- **Empirical support for the linear approximation (Figure 1)**. Across 5000 prompt–token pairs, predicted vs. actual logit shifts have cosine 0.978 — strong evidence that the first-order linear approximation holds in practice and that IAS vectors faithfully capture the direction of influence updates.

## Weaknesses

### Fatal
None.

### Major
- **No demonstration of the provenance-tracing workflow**. The paper repeatedly advertises that ρₛ enables mapping steering vectors back to causal training examples — "steer first, trace provenance to training examples" is a headline contribution. Yet no experiment actually demonstrates this. The detoxification experiment builds steering vectors from Jigsaw prompts but never computes ρₛ or shows that top-weighted examples correspond to toxic documents. The data-provenance claim is therefore unvalidated. This is the single most significant gap between the paper's promises and its evidence.

- **Generalization bound (Section 6) uses a weight-space interpretation not connected to the paper's core method**. Theorem 6.1 describes a model "obtained by adding a rank‑k IAS correction" written as f̃ = f_θ + αUV^T, which is a weight-matrix perturbation, not a vector added to activations. The proof sketch states "IAS changes only a rank‑k submatrix of the layer weight," but the rest of the paper defines IAS as an activation-space operation — and never justifies that adding a vector to activations at layer ℓ is equivalent to a low-rank weight perturbation. This section is insufficiently motivated; the bound may be correct in isolation but its relevance to activation steering is unclear. The no-free-lunch bound (Theorem 6.2) does not share this problem, as it directly addresses activation-space perturbations.

### Minor
- **Figure 1 slope of 1.5 is not discussed**. The paper reports slope 1.50 (predicted vs. actual logit shift) without comment. If the first-order theory were exact, the slope would be 1.0. A slope of 1.5 means the actual effect is systematically 50% larger than predicted — a discrepancy the paper should acknowledge and explain (e.g., second-order effects from nonlinearities above the layer, or an artifact of how "predicted" is computed). The high cosine (0.978) still supports a strong linear relationship, but the unaddressed scaling gap weakens the quantitative validation.

- **Detoxification results show IAS slightly worse than CAA without discussion**. In Table 1, IAS has higher toxicity (0.0164 vs. 0.0150) and higher perplexity (13701 vs. 13291) than CAA. The paper does not mention this, nor does it provide confidence intervals or statistical tests. Since IAS is presented as a principled alternative, the fact that it does not match the simpler CAA should be addressed.

- **Equation (2) has an algebraic error**. The dual program derivation gives Δh* = J_{h→y}^⊤ J_{θ→y} Δθ, but the correct expression involves the pseudoinverse: Δh* = J_{h→y}^† J_{θ→y} Δθ. Theorem 5.2 later gives the correct form (J_{h→y}^†), so this is a typo in a critical equation rather than a conceptual error, but it should be fixed.

- **Construction of ρₛ in Theorem 4.2 is not explicit**. The paper says "the measure ρₛ constructed in Eq. 4," but Eq. 4 is the theorem statement itself, not a construction. The reader cannot determine how ρₛ is computed from the main text. This belongs in the main paper or a clear appendix reference.

- **Figure 3 interpretation is unclear**. The histogram plots "Spectral radius of Xc^T diag(y) Xc" but Theorem 5.3 defines Σ as a different matrix involving inverse-Hessian-vector products. The connection between the plotted quantity and the spectral optimality claim is not explained.

### Trivial
- None.

## Nice-to-Haves
- Add confidence intervals or error bars to the detoxification comparison (Table 1).
- Clarify the computational cost of the spectral recipe (power iteration with inverse-Hessian-vector products) vs. the basic IAS vector (two JVPs).
- Define hyperparameters (α, layer choice) for the detoxification experiment to aid reproducibility.

## Removed Points
These points from the reviewers are removed with brief justification:
- Harsh critic's claim that the slope of 1.5 "undermines the credibility of the entire first-order equivalence claim": Overstated. The slope is a discrepancy that should be discussed, but cosine 0.978 still provides strong evidence for a linear relationship. Moved from "fatal" to "minor."
- Harsh critic's claim that Theorem 6.1 "is not just weak—it is incoherent with the rest of the paper": The theorem is insufficiently motivated and disconnected, but "incoherent" overstates the case; it's a major weakness, not fatal.
- Strength finder's "generalization guarantees" claim: Conflicts with the verified weakness that Section 6 is disconnected from the main method. Removed.
- Harsh critic's points about missing appendix content or computational cost details: These are covered by the paper's own cost model and would be in the appendix. Removed per hard rules.
- Harsh critic's section-by-section notes about notation in Theorem 5.3's power iteration: This is a minor presentation issue.

## Novel Insights
None beyond the paper's own contributions. The core observation — that activation steering and influence functions are first-order projections of the same sensitivity tensor, with a closed-form duality and a scalar diagnostic γ governing perfect equivalence — is the paper's own contribution, not something synthesized from the reviews.

## Suggestions
1. Add one concrete provenance-tracing experiment: pick a steering vector (e.g., the detoxification CAA vector), compute ρₛ over a small training subset, and show that top-weighted examples are indeed toxic. This would validate the paper's most distinctive promised workflow.
2. Discuss the slope of 1.5 in Figure 1, ideally by decomposing the residual per logit index to isolate whether the mismatch is uniform or dimension-specific. If possible, provide an explanation (e.g., second-order amplification, normalization choices).
3. Either remove Section 6.1 (Theorem 6.1) entirely or add a clear justification for why a rank-k weight perturbation model captures the effect of activation steering. The rest of the paper (Sections 3–5) does not depend on this section.
4. Fix the algebraic error in Equation (2) to include the pseudoinverse consistently.

## Score and Decision

**Calibration protocol summary:**

**Round 1 — Bracketing:**
| Anchor | Score | Topic | Comparison |
|--------|-------|-------|------------|
| z1yI8uoVU3 | 3.00 | Activation steering evaluation framework | Much weaker: purely empirical, no theory, narrow scope. Current paper significantly stronger. |
| wYVP4g8Low | 3.00 | MLP activation functions | Unrelated topic. |
| WT2bL7sCM1 | 3.00 | Hessian-free influence functions | Narrow incremental contribution vs. novel cross-area unification. Current paper stronger. |
| qJkCEcd50n | 3.00 | Influence function manipulation | Different problem. |
| KjBG4JNOc2 | 6.20 | Influence measure for training robustness | Stronger empirical validation but less theoretical novelty. Somewhat comparable quality. |
| 9wjGUN65tY | 5.00 | Steering vectors + conceptors | Most directly comparable: theoretical steering framework with incomplete validation. Current paper has stronger theory and cleaner presentation but similar empirical gaps. |
| p85TNN62KD | 5.50 | Influence functions for non-decomposable loss | Comparable score range but different topic. Both have strong theory with empirical gaps. |
| wozhdRCtw | 7.00 | Activation steering for instruction-following | Better empirical completeness but less theoretical depth. |
| 4xWQS2z77v | 8.00 | Convex duality for neural nets | Unrelated topic. |

**Round 2 — Narrowing:**
| Anchor | Score | Topic | Comparison |
|--------|-------|-------|------------|
| 9wjGUN65tY | 5.00 | Steering vectors + conceptors | Current paper is stronger theoretically (duality + bounds vs. conceptor derivation) but shares similar empirical incompleteness. Slightly above this anchor. |
| 2XBPdPIcFK | 5.00 | ActAdd activation engineering | Highly divergent reviews (8,3,6,3). Primarily empirical paper with limited theory. Current paper stronger in theoretical rigor. |
| ZPkNrs6aNO | 5.50 | Confident direction steering | Has theoretical framework but with weak empirical validation and missing baselines. Current paper is comparable in quality — strong theory, incomplete validation. |
| YCu7H0kFS3 | 4.75 | Entropic activation steering | Narrower contribution. Current paper stronger. |
| KjBG4JNOc2 | 6.20 | Influence measure | Better empirical completeness. Current paper has more novel theoretical contribution. |
| dTQmayPKMs | 6.33 | Influence functions for RLHF | Well-executed but narrower scope. Current paper has broader significance. |
| EsjoMaNeVo | 6.00 | Steering no-regret learners | Different topic (game theory). |
| wpXGPCBOTX | 6.75 | Inverse optimal transport | Unrelated topic. |

**Final placement:** The paper is strongest in its core theoretical contribution (Sections 3–5), which is genuinely novel and well-executed. However, it significantly overclaims by advertising a data-provenance workflow it never validates, and Section 6 contains a poorly-justified result. The empirical evaluation supports the theory (cosine 0.978) but has an unexplained quantitative discrepancy (slope 1.5). Compared to the 5.0 anchors (conceptor paper, ActAdd), this paper has stronger theory and cleaner presentation. Compared to the 5.5–6.2 anchors, it has comparable or greater theoretical novelty but larger empirical gaps. The missing provenance experiment is the decisive gap that prevents a higher score.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>