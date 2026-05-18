Now I have all the information I need. Let me compose the consolidated review.

---

## Summary

This paper proposes CDGIL (Curriculum Dynamic Graph Invariant Learning), a framework that combines disentangled representation learning with curriculum-style scheduling to handle distribution shifts in dynamic graphs. The method has three components: (1) a dual disentangled dynamic attention network that separately captures invariant and variant patterns, (2) a self-paced intervention mechanism that adjusts adversarial reassembly intensity based on training loss, and (3) a gradient-based sample importance reweighting strategy. Experiments on real-world (COLLAB, Yelp) and synthetic dynamic graph datasets show consistent ROC-AUC improvements over eight baselines, including the prior state-of-the-art DIDA.

## Strengths

- **Novel problem formulation**: The paper identifies a genuine gap in prior work (DIDA) — that existing dynamic graph OOD methods ignore training status and sample importance when learning invariant patterns. Integrating training-aware scheduling with invariant learning in dynamic graphs is a reasonable and underexplored direction (Abstract; Section 1).

- **Self-paced intervention with a stage-aware design**: The method dynamically controls intervention intensity $\lambda_r$ via the current training loss, applying weaker intervention early and stronger intervention later. This is a sensible, principled design that grounds the training schedule in the model's own learning progress (Section 4.2, Eq. 7).

- **Consistent empirical gains across datasets**: CDGIL outperforms all baselines (including DIDA) on both real-world and synthetic datasets under distribution shift, often by substantial margins (Tables 1, 2). The pattern holds across multiple shift levels on synthetic data, suggesting the approach is not dataset-specific.

- **Time-aware weighting is a practical addition**: The time-series reweighting (Section 4.3.1) accounts for the intuition that temporally closer graph data are more similar — a simple but sensible adaptation for dynamic graphs that most prior OOD methods lack.

## Weaknesses

### Major

- **The gradient-based sample reweighting (Section 4.3.2) is critically underspecified and non-reproducible.** The paper states: "we first calculate their loss … and perform gradient backward, thus we have the gradient of all of the prediction results." It never specifies: (a) which loss function is used (binary cross-entropy? MSE? — the loss $\ell(\mathbf{y}_{pred}, \mathbf{y}_{true})$ is given as a generic placeholder), (b) with respect to which model parameters the gradient is taken, or (c) how per-sample gradients are extracted from a batched dynamic graph where nodes share neighborhoods and temporal dependencies. The mapping function $f$ is an elaborate expression $f(x)=-\exp(\mathrm{sigmoid}(\log(x)\bar{A}+B)*C+D)$ for positive gradients and $f(x)=1$ for negative gradients, introducing four hyperparameters ($A,B,C,D$) with zero theoretical or empirical justification. No ablation, sensitivity analysis, or convergence study is provided for this component. Since this is one of the two core "curriculum" contributions, the paper's technical contribution is unverifiable as written.

- **Core training loss functions are never defined.** The losses $\ell_{trainI}$ and $\ell_{trainV}$ for the invariant and variant encoders are referenced repeatedly (Section 4.2, Algorithm 1) but never formally defined. The preliminary (Section 3.1) says the paper studies "node-level tasks" and $\mathbf{Y}_{t+1}$ typically represents "node property or edge status," while the experiments evaluate on link prediction. The actual loss formulation used for optimization is absent. Without this, Algorithm 1 and the entire optimization procedure are ambiguous.

- **Experimental results lack statistical rigor.** Tables 1 and 2 report only point estimates of ROC-AUC without standard deviations, confidence intervals, or any indication of multiple runs/ seeds. It is impossible to assess whether the reported improvements over DIDA (or any baseline) are statistically significant. Given that the margins over DIDA are sometimes modest (e.g., synthetic datasets), this is a critical gap. The ablation study (Figure 2) is presented only as an image with no numerical values, making the magnitude of component contributions unverifiable.

### Minor

- **The intervention intensity formula has a mathematical subtlety:** $\lambda_r = \lambda_0 * \min(\ell, \ell_{\min})^{-1}$. As $\ell \to 0$, $\lambda_r \to \infty$ with no clipping or normalization described. The term $\ell_{\min}$ is described as "a threshold for the minimum loss" — unclear whether this is a floor (below which intensity saturates) or a ceiling, and the inverse formulation inverts the typical intuition (smaller loss → larger intervention). In practice this may be harmless if loss never approaches zero, but the paper should address this.

- **The "curriculum learning" framing is thin.** The paper claims to be "the first to study curriculum learning for dynamic graph distribution shift," but the curriculum mechanism consists solely of a loss-based scheduling rule for intervention intensity plus a gradient-based sample reweighting function. There is no difficulty measurer that orders examples by complexity in the standard curriculum learning sense, and there is no evaluation of whether the proposed ordering improves convergence or final performance compared to a random order baseline. The connection to the curriculum learning literature is asserted rather than demonstrated.

- **The dual disentangled architecture vs. DIDA is insufficiently differentiated.** The paper says it uses "dual DDGAT" with separate invariant and variant encoders, but does not clarify whether the two encoders share weights, operate on different feature subspaces, or how the learnable mask $\mathbf{m}_f$ is applied independently to each. Given that the equations shown are structurally identical to DIDA's, the architectural difference needs to be stated explicitly.

- **No hyperparameter sensitivity analysis.** The method introduces at least six key hyperparameters ($\lambda_0, \lambda_{\text{assemble}}, \lambda_{\text{diff}}, A, B, C, D$, plus the time weight $\lambda$) without any sensitivity study or guidance for setting them. This raises concerns about cherry-picking, particularly for the gradient reweighting hyperparameters $A$-$D$.

- **Complexity analysis (Section 5.4) is incomplete.** The paper claims $O(|E| d + |V| d^2)$ complexity for CDGIL, less than DIDA's $O(|E| d + |V| d^2 + |E_t| |S| d)$, but omits the gradient computation cost for the sample reweighting step, which requires per-sample backward passes and is at least $O(|E_t| d)$ per epoch.

### Trivial

- None beyond the minor points above.

## Nice-to-Haves

- Report standard deviations and results from multiple random seeds (at least 3–5) for all experimental tables.
- Provide numerical values for the ablation study (Figure 2) rather than only a visual comparison.
- Include a comparison against training with random ordering of samples to validate the curriculum component's specific benefit.
- Provide guidance or a sensitivity analysis for the gradient-reweighting hyperparameters $A,B,C,D$.

## Removed Points

- *"Section 2.2 appears to be missing; the numbering jumps from 2.1 to 2.3."* — This is a parser artifact; the original submission's section numbering cannot be verified from the parsed text. Remove per formatting-artifact rule.
- *"The paper does not include more recent dynamic graph OOD methods (e.g., any from 2024–2025)."* — Cannot verify the existence of such methods; the hard rule prohibits speculating about missing related works. Remove.
- *"The self-paced intervention mechanism is nearly identical to DIDA's intervention"* — The paper explicitly states (Section 4.2) "Following (Zhang et al., 2022), we adopt the approximate intervention method." The novelty is in the scheduling rule, not the intervention itself. The paper is transparent about this. Remove as it misidentifies the claimed contribution.
- *"The curriculum label is applied post-hoc"* — The paper does use training status (loss) to adjust intervention and gradient signals to reweight samples, which are genuine forms of automatic curriculum learning. This criticism mischaracterizes the method. Remove, though the thinness of the connection is kept as a minor weakness.
- *Strength Finder claims about ablation "confirming" contributions.* — The weakness about Figure 2 lacking numerical values conflicts with the strength's "confirmed" claim. Moved here per rule that weakness wins. The existence of an ablation study is a positive, but its conclusiveness is limited by the lack of numbers.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any insight that the paper itself does not already articulate.

## Suggestions

1. **Clarify the gradient-based reweighting.** Specify which loss function, which parameters' gradients are computed, and how per-sample gradients are extracted from a batched dynamic graph. If this mechanism cannot be cleanly specified, consider replacing it with a simpler, principled alternative (e.g., importance sampling from a learned difficulty predictor).
2. **Define ℓ_trainI and ℓ_trainV explicitly.** State the exact loss formulation (e.g., binary cross-entropy for link prediction) so that the optimization procedure in Algorithm 1 is unambiguous.
3. **Add standard deviations and multi-seed results** to all experimental tables, and provide numerical values for the ablation study.
4. **Add a discussion of the λ_r formula's behavior** near zero loss, and consider adding a clipping mechanism or reformulating the scheduling rule to avoid unbounded growth.
5. **Provide hyperparameter sensitivity analysis** for at least the most critical hyperparameters (λ_0, λ_assemble, λ_diff) to demonstrate robustness.

## Score and Decision

**Originality:** The idea of combining curriculum-style training scheduling with dynamic graph invariant learning is novel, but the execution is standard building on DIDA.

**Importance:** The problem (distribution shift in dynamic graphs) is practically important and timely.

**Claims support:** Partially supported — the empirical results consistently favor CDGIL, but the lack of statistical rigor and underspecified method weaken confidence.

**Soundness:** The methodological description has significant gaps that affect reproducibility. The experimental protocol lacks basic statistical reporting.

**Clarity:** The writing is understandable at a high level but critically underspecified in key technical details (loss functions, gradient computation, hyperparameter choices).

**Value:** The problem framing and consistent empirical trends suggest potential value, but the paper is not ready for publication without major revisions addressing the specification gaps and experimental rigor.

**Overall assessment:** The paper tackles an important and timely problem, and the empirical trend is promising. However, a core technical component (gradient-based reweighting) is described so vaguely that it cannot be reproduced, the training loss functions are never defined, and the experimental results lack any statistical validation. These are structural problems that go beyond presentation polish. The paper needs major revisions before it can be accepted.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>