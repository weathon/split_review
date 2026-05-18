## Summary

This paper investigates whether feed-forward (FFN) and recurrent neural networks (RNN) with fixed random weights and learned biases can serve as universal function approximators. It presents Theorem 1 (FFN) and Theorem 2 (RNN), claiming that bias-only training achieves universal approximation with high probability given sufficiently wide hidden layers, and supports these claims with experiments on multi-task image classification and dynamical system trajectory generation. The work is motivated by biological plausibility (non-synaptic learning mechanisms like threshold adaptation) and connections to the Strong Lottery Ticket Hypothesis (SLTH).

---

## Strengths

**1. Novel theoretical direction.** The paper initiates the study of expressivity for bias-only training in both FFNs and RNNs, a setting that (as the paper correctly notes) is largely unexplored compared to output-weight training or masking. Connecting this to the SLTH over units adds theoretical interest to the contribution.

**2. Multi-task learning experiments are convincing and well-executed.** Figure 1B shows bias-only FFNs (32K trainable parameters) achieving test accuracy comparable to fully-trained networks (25M parameters) across 7 diverse image classification tasks. The gap is small (only KMNIST shows a significant difference), demonstrating that bias learning is a genuinely viable learning paradigm.

**3. Task specialization analysis (Figure 1C) provides mechanistic insight.** The Task Variance clustering reveals that bias learning leads to task-selective hidden units, closely paralleling observations in fully-trained networks (Yang et al. 2019). The positive correlation between bias values and task variance supports the "masking via bias" intuition central to the paper's theory.

**4. RNN dynamical systems experiments are empirically informative.** Figures 3 and 4 demonstrate that bias-only RNNs can generate both simple (cosine) and complex (van der Pol, Lorenz) dynamics, and the Jacobian eigenvalue analysis in Figure 3B provides an elegant mechanistic explanation for how bias tuning shapes effective connectivity without changing synaptic weights.

**5. Honest about limitations and scope.** The paper explicitly acknowledges that the RNN result is weaker (pointwise convergence only, finite-time), that "exceedingly massive" widths are required, and that the mask-learning comparison has a confound in the soft-mask steepening schedule. This candor strengthens credibility.

---

## Weaknesses

### Fatal
None.

### Major

**1. The γ-parameter bounding property for ReLU is asserted without proof or reference, yet it is essential to Theorem 1.**

Definition 2 calls an activation *γ-parameter bounding* if it allows universal approximation even when every individual parameter (weight or bias) is bounded by ±γ. Proposition 1 asserts that ReLU (and Heaviside) satisfy this for *any* γ > 0. This is a strong claim: it requires that for any continuous function on a compact set and any prespecified bound γ > 0, there exists a one-hidden-layer ReLU network with *all* parameters within [−γ, γ] that approximates the function to within any tolerance. Standard universal approximation theorems do not guarantee this — they allow parameters to grow arbitrarily. The paper provides no construction, proof, or external reference for this claim. The proof sketch for Theorem 1 (lines 92–96) depends on this property to bound the parameters of CN₁, so without it the FFN theorem is unsupported. The paper's remark that "We leave it to future work to determine which other activations are parameter bounding" (line 76) suggests awareness that the property is nontrivial, yet ReLU itself is not justified.

**2. The RNN universal approximation theorem (Theorem 2) is not adequately justified; the proof sketch does not confront the recurrent coupling issue.**

The proof sketch (line 124) says the RNN argument proceeds "analogous to Theorem 1": approximate the target dynamical system with an RNN CR₁, then find a subnetwork within a wider random RNN CR₂ that approximates CR₁. For FFNs, the subnetwork construction works because input and output weights are independent across units. For RNNs, selecting a subset of hidden units inherits a *submatrix* of the large random recurrent weight matrix, and this submatrix must approximate CR₁'s full recurrent matrix block by block. The paper does not discuss the probability that a random m×m matrix contains a k×k submatrix close to a target matrix, nor does it address how the temporal dynamics couple all selected units simultaneously. The sketch states "we can find" without quantifying the required width or the probability of success for the recurrent case. A proper proof would need to handle this combinatorial probability, which differs structurally from the FFN parameter-wise argument. The paper itself acknowledges the result is only pointwise and finite-time (line 122), but the deeper issue is whether the subnetwork construction works for recurrent architectures at all. Without a more detailed argument, the claim of "a first proof of the SLTH over units for RNNs" is unsubstantiated.

### Minor

**3. The RNN universal approximation theorem used as a building block may not cover ReLU activations.**

The paper cites Schafer (2006) for the existence of CR₁ (an RNN approximating the target dynamical system). Schafer's result treats sigmoidal activations; extending it to unbounded activations like ReLU is not trivial and is not discussed. Even if such results exist elsewhere, the paper should either cite them explicitly or state the activation assumptions required for CR₁'s existence. This does not invalidate the paper's approach but is a missing detail that a reader would need to verify the proof chain.

**4. The mask vs. bias learning comparison uses a soft-masking procedure with a steepening schedule, creating a confound in the optimization landscape.**

The paper acknowledges this confound (line 206) as a limitation. However, because the comparison is presented as evidence that "bias learning performs similarly to learning masks" and that the solutions are "correlated but distinct" (r ≈ 0.46), the confound matters: the difference in optimization dynamics between the two methods could drive them toward different basins regardless of the underlying parameterization. The paper's own caveat that "further research is needed to determine if this trend is reliable" is appropriate, but the strength of the empirical conclusion about similarity is somewhat softened as a result. This is a minor issue given the paper's primary focus is theory.

**5. The multi-task comparison does not control for number of trainable parameters.**

The bias-only network has 32K trainable parameters, while the fully-trained baseline has 25M. Showing that the bias-only network matches the fully-trained network's performance is a notable result. However, it is not clear whether the gap is attributable to the bias-learning *mechanism* or simply to having fewer parameters. A fully-trained network with the same 32K trainable parameters (e.g., training only the output layer) is not tested. This does not invalidate the paper's main claim (that bias learning *works*) but makes it harder to interpret the "comparable performance" result mechanistically.

---

## Nice-to-Haves

- A same-parameter-count control for the multi-task experiment (e.g., training only output weights), to isolate whether bias learning offers an advantage over other parameter-efficient schemes.
- A systematic study of how performance scales with hidden-layer width for a fixed target function, more tightly connecting experiments to the theory's "exceedingly massive hidden layer widths" requirement.
- Explicit discussion of how the initial condition in Theorem 2 is set (the paper states a hidden-state initial condition exists but does not clarify whether it is freely chosen or learned).

---

## Removed Points

- The harsh critic's framing of the multi-task experiment design criticism as a major flaw: moved to Minor/Nice-to-Have. The paper's claim is about viability of bias learning, not parameter efficiency per se. The absence of a same-parameter-count baseline does not threaten the paper's core claim.
- The critic's observation that the "choice of activation for the RNN approximation theorem" requires a specific citation: kept as Minor (point 3) rather than Major. This is a detail the authors could address in a rebuttal, not a structural flaw.
- The critic's comment that "correlation analysis does not convincingly show that bias learning performs similarly to learning masks": downgraded. The paper already acknowledges this confound explicitly. The correlation analysis is presented as suggestive, not definitive.
- The critic's suggestion that the eigenvalue analysis "could be expanded" about the connection to theory: removed as a non-specific presentational suggestion that does not affect the paper's validity.

---

## Novel Insights

The most interesting observation not fully stated by the paper itself arises from comparing its two theoretical gaps. The FFN theorem's dependence on the γ-parameter bounding property, and the RNN theorem's dependence on the recurrent submatrix selection problem, both reduce to the same fundamental question: *how many random parameters are needed before one can find a subnetwork that matches a target configuration?* In the FFN case, the subnetwork is constructed unit-wise with independent input/output weights, so the required width scales roughly like the number of parameters in the target network. In the RNN case, the recurrent submatrix introduces quadratic coupling — every pair of selected units must simultaneously match target entries — so the required width likely scales exponentially in the target hidden size (by birthday-paradox / coupon-collector arguments). This exponential gap suggests that the RNN result, even if true, may be qualitatively harder to realize in practice than the FFN result. The paper's empirical success with modest RNN widths (200–1024 units) thus tells us something the theory does not: that practical bias learning in RNNs may succeed through mechanisms beyond the masking argument used in the proof sketch.

---

## Suggestions

1. Provide a proof or constructive argument for Proposition 1 (γ-parameter bounding for ReLU). A plausible approach: scale the target function to a small range, use many ReLU units with tiny input weights to construct bump-like basis functions, and show that the output weights can also be bounded by γ by using enough units.
2. For the RNN theorem, either (a) provide a rigorous treatment of the submatrix selection probability (quantifying how width must scale with target hidden size to make the probability arbitrarily close to 1), or (b) reframe Theorem 2 as a conjecture supported by empirical evidence, acknowledging that the FFN theorem is proven while the RNN result is a plausibility argument.
3. Cite an RNN universal approximation theorem that applies to ReLU activations, or state the activation assumptions explicitly.
4. Address the "many unstated assumptions" concern by adding a paragraph that walks through the logical chain: (i) universal approximation theorem ⇒ ∃ CR₁ with some width; (ii) γ-parameter bounding property (proved) ⇒ CR₁'s parameters bounded by γ; (iii) random sampling ⇒ ∃ subnetwork in CR₂ approximating CR₁ with high probability for large enough width; (iv) bias learning ⇒ subnetwork can be selected via biases.

---

## Score and Decision

This paper tackles an interesting and under-explored question, and its empirical results provide genuine evidence that bias learning is a viable paradigm. The biological motivation and connections to SLTH are well-argued. However, the paper presents itself primarily as a theoretical contribution (both theorems are stated upfront as the main results), and in this respect it falls short. The γ-parameter bounding property — on which the FFN theorem depends entirely — is asserted without proof or reference. The RNN theorem is only sketched with a proof-by-analogy that bypasses the key technical difficulty of recurrent coupling. These are not presentation nitpicks; they are gaps in the core theoretical claims that the paper sets out to make. Until these gaps are resolved (or the paper is reframed as an empirical study with a more modest theoretical component), the contribution as stated is not convincing. The experiments are solid but do not compensate for unsubstantiated theorems.

**Originality**: High — the setting (bias-only training) is genuinely novel.
**Quality of claims**: Low — the central theoretical claims are not adequately supported.
**Experimental soundness**: Good — experiments are well-designed and reproducible.
**Clarity**: Good — the paper is well-written and clearly structured.
**Value**: Potentially high, if the theoretical gaps can be resolved.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>