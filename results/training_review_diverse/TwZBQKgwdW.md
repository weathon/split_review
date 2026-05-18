Here is my final synthesized review.

---

## Summary

This paper proposes NTK-DFL, the first method to combine Neural Tangent Kernel (NTK)-based weight evolution with decentralized federated learning (DFL). Clients exchange Jacobians (not just weights) with neighbors, compute a local NTK, evolve their weights via the linearized NTK dynamics, and perform per-round weight averaging. A final model-averaging step aggregates all client models after training. Experiments on Fashion-MNIST, FEMNIST, and MNIST with up to 300 clients show consistent accuracy improvements over DFL baselines and 4.6× fewer communication rounds to reach target accuracy under high heterogeneity.

## Strengths

1. **Novel and well-motivated combination of NTK and DFL.** This is the first work to apply NTK-based weight evolution in a fully decentralized setting. The idea of using Jacobian exchange (rather than just weight exchange) to obtain more expressive updates is a genuinely new architectural idea for DFL, and the paper correctly identifies heterogeneity as the key challenge this addresses.

2. **Consistent empirical advantage across diverse settings.** NTK-DFL outperforms all baselines (D-PSGD, DFedAvg, DFedAvgM, DisPFL) on Fashion-MNIST, FEMNIST, and MNIST, under varying heterogeneity levels (α=0.1 to IID), sparsity levels (κ=2 to κ=10), and topologies (static vs. dynamic). The 3–4% accuracy lead established within 5 rounds (Figure 1) and maintained throughout training provides compelling evidence that the method works.

3. **Insightful analysis of the model variance–accuracy relationship.** Figure 8 shows a positive correlation between inter-model variance and final test accuracy, with NTK-DFL achieving both higher variance and higher accuracy than baselines. This provides an explicit mechanistic explanation for why the final model averaging step works well — the NTK-based updates generate beneficial diversity among client models.

4. **Practical robustness to weight initialization.** Figure 9 demonstrates that NTK-DFL maintains convergence even with per-client random initialization, whereas DFedAvg degrades noticeably. This is practically important for decentralized settings where synchronized initialization may be infeasible.

5. **Ablation confirms the role of per-round averaging.** The ablation study (Figure 7) shows that removing per-round averaging produces a long tail of low-accuracy models, confirming its stabilizing role in preventing local model drift.

## Weaknesses

### Fatal
None.

### Major

1. **No statistical replication — all results appear to be from single runs.** Every figure and table reports a single trajectory with no error bars, confidence intervals, or mention of multiple random seeds. The paper makes strong quantitative claims ("4.6 times fewer communication rounds," "at least 10% higher accuracy than the mean local model accuracy") that are presented as exact numbers. DFL baselines involve random topologies, stochastic gradients, and client sampling — single runs can be misleading. Without variance estimates, the reader cannot assess whether the reported advantages are statistically reliable or whether they hold across different graph realizations, data partitions, and weight initializations. This is the most impactful flaw in the paper because it directly affects the believability of every quantitative claim.

2. **The NTK formulation for multi-output models is underspecified and needs justification.** Equation (4) defines a scalar kernel H^{(k)}_{i,mn} = (1/d_2)⟨𝒥_i^{(k)}(x_m), 𝒥_i^{(k)}(x_n)⟩_F, which is the trace of the standard multi-output NTK (d_2 × d_2) divided by d_2, rather than the full matrix kernel. For a 10-class model (d_2=10), this discards cross-output information. The paper presents this as "the definition of the NTK" without acknowledging that it is a scalar approximation, without justifying why the trace kernel is appropriate for this setting, and without discussing how it relates to the NTK formulation used in the prior centralized NTK-FL work (Yue et al., 2023). While the equations are internally self-consistent (the scalar kernel is used coherently in Eq. 5–6), the lack of justification for this design choice weakens the theoretical framing. The paper should explicitly state that this is a trace kernel approximation, explain why it is suitable, and ideally compare against the full matrix kernel or cite precedent for this choice.

### Minor

3. **No communication cost analysis.** The paper claims "4.6× fewer communication rounds" as its headline result, but NTK-DFL exchanges Jacobian tensors (size O(N_i × d_2 × d)) rather than just weight vectors (size O(d)) per round. The per-round communication cost is significantly higher than standard DFL methods. Without reporting total communication volume (bits transmitted over all rounds), the round-count comparison is potentially misleading. A method that needs 4.6× fewer rounds but sends 10× more data per round is not communication-efficient overall. The paper acknowledges memory complexity and proposes Jacobian batching, but never quantifies communication cost.

4. **Unsupported claim about omitted baselines in Figures 3a/3b.** The captions state "Other baselines are not drawn but perform similarly to DFedAvg." This assertion is not backed by any presented data. Either show the curves or remove the claim.

5. **The client selection algorithm for final averaging requires a global validation set, partially weakening the "decentralized" framing.** The paper states that "each client that opts in to model averaging contributes a portion of its data to a global validation set before training begins." This is a central coordination assumption that is inconsistent with a fully decentralized, no-server paradigm. The basic final averaging (averaging all models) can be done in a decentralized way as the paper notes, but the *selection algorithm* specifically requires shared validation data. The paper should more clearly separate what is fully decentralized (training) from what requires some central coordination (the selection optimization).

6. **Weight evolution timing differs from standard NTK gradient flow, without discussion.** The per-round averaging happens *before* Jacobian computation (the NTK is computed on the averaged weights w̄_i^{(k)}), and Jacobians are recomputed each round. Standard NTK training computes the kernel once at initialization and keeps it fixed. The paper does not discuss how recomputing Jacobians each round and using them for multiple inner timesteps t affects the quality of the linearized approximation, nor does it compare to alternatives. This is worth clarifying but does not invalidate the method.

### Trivial
None.

## Nice-to-Haves

- A derivation tracing how Equation (4) (scalar kernel) follows from or approximates the standard multi-output NTK definition.
- A brief intuitive explanation of why the trace kernel works for the 10-class MLP setting (e.g., the outputs are symmetric enough that cross-output information is not critical).
- At minimum, 3-run averages with error bars on the headline results (Figure 1 convergence curves and the communication round table).

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The NTK definition appears to be incorrect"** — The reviewer framed this as a structural error. The kernel defined in Eq. (4) is a valid (trace) NTK; it is not *incorrect*, but it is a specific design choice (scalar approximation of the full d_2×d_2 kernel) that the paper should justify. Moved to Major Weakness #2 with corrected severity.
- **"Missing convergence theory"** — The paper is an empirical methods paper; theoretical analysis is not standard for this class of contribution. Keeping it would impose expectations mismatched with the paper's scope.
- **"Comparison with more recent DFL methods"** — This demands breadth outside the paper's scope and amounts to "missing related works," which I cannot verify.
- **"Weaknesses framed as 'the authors should add X'"** — Several suggestions (e.g., "provide full derivation," "show alternative comparison") are wishlist items that do not affect the core contribution's validity.
- **Generic strength from Strength Finder about addressing an "important problem"** — Too generic to retain without specific grounding in the paper content.

## Novel Insights

Beyond the paper's own contributions, the most interesting observation from the review process is the tension between the paper's two key claims: (a) NTK provides more expressive update directions, and (b) per-round averaging stabilizes training. These are partially in tension — averaging reduces variance among clients, while the NTK's expressiveness claim would be most impactful when clients diverge. The paper's finding that NTK-DFL creates a *beneficial* level of variance (Figure 8) while per-round averaging eliminates harmful variance (Figure 7) suggests a nuanced trade-off that could be explored systematically: the NTK updates push weights in directions that create useful diversity, while averaging prevents catastrophic drift. This two-level dynamic is underexplored in the paper and could motivate future theoretical work on the interaction between kernel-based updates and consensus averaging.

## Suggestions

1. **Add error bars.** This is the single highest-impact improvement. Run experiments with at least 3–5 random seeds (different graph realizations, data partitions, and weight initializations) and report mean ± std on the convergence curves and the communication round table. Without this, the quantitative claims are not properly supported.
2. **Clarify the NTK definition.** Explicitly note that Eq. (4) computes the trace of the multi-output NTK (a scalar kernel). Justify this choice, cite precedent if it exists, or discuss when the approximation might break down.
3. **Report total communication volume.** Provide a table comparing the per-round bytes transmitted and total bytes over all rounds for NTK-DFL vs. baselines. This is essential for evaluating practical utility in bandwidth-constrained settings.
4. **Separate the selection algorithm from the core claim.** Clearly distinguish between the fully decentralized training protocol and the final selection algorithm (which requires shared validation data). Consider moving the selection algorithm to an ablation/appendix and presenting the main results with simple averaging of all models.

## Score and Decision

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>