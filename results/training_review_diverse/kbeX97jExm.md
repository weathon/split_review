Now I have all the information needed for a thorough, well-supported final review.

## Final Consolidated Review

## Summary

This paper proposes the neural wave equation—a non-homogeneous wave equation with a learnable neural network source function—for sequence labeling on irregularly sampled data. The key idea is to evolve hidden states continuously across both observation time and architectural depth, using the wave equation's propagative dynamics to avoid the smoothing-out of information that the authors attribute to heat‑equation–based alternatives (CDR‑NDE). The paper derives d'Alembert's analytical solution to argue for "denser connections" across hidden states, develops several source-function architectures (Single GRU, Single MLP, Double Gating, MLP+GRU), and reports empirical improvements over 14 baselines on four irregularly sampled benchmarks.

---

## Strengths

1. **Novel application of the wave equation as a sequence architecture.** While prior work (CDR-NDE) used the heat equation for continuous depth, this paper is the first to propose the wave equation, which has qualitatively different dynamics (propagative vs. diffusive). The analytical solution (d'Alembert's formula, Equation 9) provides a principled argument that each hidden state depends on source terms integrated over all previous depths and a cone of neighboring time points—a genuinely denser connectivity pattern than standard RNNs or heat‑equation models. This is a novel architectural contribution.

2. **Strong empirical results across multiple irregularly sampled benchmarks.** The Neural Wave–Double Gating variant achieves the highest accuracy on Person Activity, Neural Wave–Single MLP achieves the best MSE on Walker2D, Double Gating achieves the best AUC on PhysioNet Sepsis, and the method remains competitive on Stance classification—all against 14 baselines including ODE-RNN, Neural CDE, and CDR-NDE. The paper benchmarks against a comprehensive set of baselines using standard evaluation protocols from Lechner & Hasani (2020).

3. **Ablation confirms the critical role of the learned source.** The homogeneous wave equation (no source) performs substantially worse on all datasets (e.g., 51.73% vs. ~82% on Person Activity), validating that the non-homogeneous neural source is essential. This cleanly separates the effect of the PDE structure from the effect of the learned source function.

4. **Implicit depth eliminates manual depth tuning.** Figure 2 demonstrates that ODE-RNN and LSTM require exhaustive model selection over depth, whereas the neural wave equation achieves comparable or better performance with no depth tuning—a practical advantage for practitioners.

5. **Honest discussion of the memory–speed trade-off.** The paper acknowledges that neural wave equations consume 1807–2137 MB versus 244 MB for Neural CDE, while being an order of magnitude faster. This transparency helps contextualize deployment decisions.

---

## Weaknesses

### Fatal
None. The paper's core contributions are novel and the experimental evidence, while imperfect, supports the claims.

### Major

1. **Unclear how the finite-difference discretization handles irregularly sampled observation times.** This is the paper's most significant methodological gap. The core update (Equations in Section 4) uses the central difference term (h_{t+Δt,d} − 2h_{t,d} + h_{t−Δt,d}) with a fixed Δt, implicitly assuming a uniform grid in the observation-time dimension. For irregularly sampled sequences, the spacing between consecutive observations varies, and a fixed Δt is not consistent with the actual timestamps. The paper mentions using a "continuous, per-channel intensity as explained in Kidger et al. (2020)" for constructing input paths, but this addresses only the *input* embedding—not the hidden-state dynamics. The relationship between the irregular observation timestamps and the Δt in the finite-difference scheme is left entirely unspecified. While the model clearly *works* on irregular data empirically (the results speak for themselves), the paper must explain how the discretization accommodates non-uniform time gaps (e.g., using non-uniform finite differences, treating t as a sequential index with actual times embedded elsewhere, or some other mechanism). This is not a fatal flaw—the empirical evidence is still interpretable—but it is a significant clarity gap that weakens the methodological exposition.

2. **Missing key state-of-the-art baselines in the experimental comparison.** The paper cites both Contiformer (Chen et al., 2023) and structured state-space models (S4; Gu et al., 2022) in the Related Work but evaluates against neither. Given that these are prominent recent methods for irregular time series (Contiformer) and long-sequence modeling (S4), their absence from the experiments makes it difficult to gauge the proposed method's position relative to the current state of the art. The paper also could not run Neural CDE on two of four datasets (Walker2D, Stance) due to computational constraints, leaving the strongest established baseline absent from half the benchmarks.

3. **The "denser connections" advantage over the heat equation is asserted but not rigorously validated.** The paper contrasts the analytical solutions of the wave and heat equations (Equations 9 and 11) to argue that the latter suffers from exponential decay of lower-depth information. However:
   - The heat‑equation model (CDR-NDE) uses a learned source function that could learn to compensate for the homogeneous decay—the analytical comparison ignores this.
   - No controlled experiment isolates the PDE type while keeping everything else (source function architecture, training setup) identical. The paper compares Neural Wave variants against CDR-NDE, but the source functions differ, so the performance gap cannot be cleanly attributed to the PDE choice.
   - The wave equation's integral term in d'Alembert's solution does not decay, but boundary effects and numerical damping are not discussed as potential mitigations.

   The claimed advantage is plausible but remains a motivational hypothesis rather than an established fact.

### Minor

1. **No error bars reported in the prose for the proposed method's main results.** The ablation study reports standard deviations (±0.16, ±0.003, ±0.001) but the main test-set numbers for the Neural Wave variants are given without uncertainty intervals in the text. (The table content was stripped by the PDF parser; if error bars appear in the original Table 1, this point is moot.) At minimum, multi-seed results should be reported.

2. **No parameter count comparison.** Given that the neural wave model consumes substantially more memory (1807–2137 MB vs. 244 MB for Neural CDE), it would be informative to know the number of trainable parameters—whether the memory increase reflects greater model capacity or simply the cost of solving a second-order PDE. This would help readers assess whether the performance gains are due to the wave equation dynamics or just additional parameters.

3. **The source-function variant selection is not justified.** The paper proposes four neural network parameterizations of the source term (Single GRU, Single MLP, Double Gating, MLP+GRU) but tests only the homogeneous ablation (no source) and does not explain why these particular architectures were chosen over alternatives. The performance differences among variants are attributed post-hoc to the number of neighboring hidden states used, but the design space is explored without systematic reasoning.

4. **The Contiformer citation in Related Work acknowledges its relevance but the paper does not explain why it was excluded from the experiments.** A brief justification (e.g., "Contiformer requires a different training setup incompatible with our evaluation protocol") would be helpful.

### Trivial

- The heat-equation analytical solution (Equation 11) uses `\exp^{(-k\lambda_n d)}` where `\exp(...)` is standard, and the variable mixing in the integral (t vs. d) is unclear due to the swapped roles of time and depth. The notational sloppiness makes the derivation harder to follow but does not affect the validity of the qualitative argument.
- Figure 2's horizontal red line for the neural wave model is functionally informative (demonstrates no depth tuning needed) but would benefit from a brief caption note explaining that the model's performance does not depend on an explicit depth hyperparameter.

---

## Nice-to-Haves

- A controlled experiment that keeps the source function architecture identical and swaps only the PDE (wave vs. heat) would cleanly isolate the effect of the PDE choice.
- Including Contiformer and S4 as baselines would strengthen the paper's positioning against current SOTA.
- A visual or quantitative measure of gradient propagation through depth (e.g., gradient flow norms, effective receptive field) would substantiate the "denser connections" claim empirically.
- The Walker2D dataset uses only 10% random dropouts—a relatively mild form of irregularity. Testing on more severely or irregularly sampled data (e.g., random observation times) would strengthen the evaluation.

---

## Removed Points
*These points are flagged to be removed per the review guidelines; treat them with caution.*

1. **"The method cannot be applied to irregularly sampled data" (fatal framing).** The paper states this as a structural flaw that invalidates the contribution. While the handling of irregular timestamps is indeed unclearly explained, the experimental results on irregular data demonstrate that the method *does* work—the missing piece is the *explanation*, not the functionality. Downgraded from Fatal to Major.
2. **"The extracted text does not include the content of Table 1" (parser artifact).** The table exists in the original submission; the PDF-to-text extraction process stripped it. This is not an author error.
3. **"No error bars for the proposed method"** accusation. The ablation study (Section 5.5) does report ± values. The main results may include error bars in the stripped Table 1. Downgraded from Major to Minor.
4. **"Boundary conditions not discussed"** — the paper explicitly references Appendix A.12 for boundary conditions, which was stripped by the parser.
5. **"Figure 2's horizontal line is meaningless"** — the paper's point is that the wave model's performance does not depend on a tunable depth hyperparameter, which is exactly what a flat line demonstrates. This is informative, not meaningless.
6. **General formatting/style nitpicks** (e.g., "the assumption g(z)=0 is not discussed in the context of sequence modeling") — the assumption is standard and clearly stated.
7. **"The paper should also cover Y / additional tasks"** demands beyond scope (e.g., testing on more irregular datasets). Moved to Nice-to-Haves.
8. **Complaint about "no empirical comparison between wave and heat equation models using the same source function"** framed as fatal omission. Downgraded to Minor as it is a reasonable suggestion but not a fatal flaw—the paper does compare against CDR-NDE (heat equation) directly.

---

## Novel Insights

Beyond the paper's own contributions, the reviews surface one genuinely useful observation: the paper's core architectural innovation (wave equation PDE with learned source) is cleanly separable into (a) the PDE dynamics and (b) the learned source function. The ablation study (Section 5.5) shows that (b) is far more important than (a)—the homogeneous wave equation performs poorly, while all source-equipped variants perform well regardless of the specific PDE dynamics. This suggests that the primary benefit of the framework may not be the wave equation *per se* but rather the richer connectivity pattern enabled by the non-homogeneous formulation, which could potentially be achieved with other second-order PDEs as well. The paper would benefit from explicitly discussing this nuance rather than framing the wave equation alone as the source of improvement.

---

## Suggestions

1. **Clarify the irregular-sampling mechanism.** Specifically, state whether the finite-difference ∆t refers to actual time gaps (requiring non-uniform finite differences) or to sequential index spacing (with actual times used only in input/output projections). Provide the precise formula used in the implementation.
2. **Add a controlled PDE-ablation experiment.** Compare wave vs. heat equation using identical source function architectures (e.g., the same Double Gating source for both PDEs) to isolate the effect of the PDE type.
3. **Report multi-seed error bars for the main results** and include parameter counts for all models.
4. **Add Contiformer and S4 baselines** or provide a clear justification for their exclusion.
5. **Clean up the notational issues in Equation 11** and ensure consistency between the wave and heat equation derivations.

---

## Score and Decision

The paper proposes a genuinely novel and interesting idea—using the non-homogeneous wave equation as a continuous-depth architecture for sequence modeling. The empirical results are strong across multiple benchmarks, and the ablation study cleanly demonstrates the necessity of the learned source function. The main weaknesses—the unclear handling of irregular timestamps in the discretization, missing SOTA baselines, and the lack of a controlled PDE-type ablation—are significant but addressable in revision. The core contribution is novel and well-motivated, and the experimental evidence on four datasets provides reasonable support for the claims.

**Score:** 6.0 / 10

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>