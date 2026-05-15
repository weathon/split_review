Now I have all the information needed. Let me produce the final consolidated review.

---

## Summary

This paper investigates whether neural networks with fixed random weights and **only trainable biases** can serve as universal function approximators. It proves that single-hidden-layer feedforward networks (FFNs) and recurrent neural networks (RNNs) with randomly sampled frozen weights and learned biases can approximate arbitrary continuous functions (FFNs) and finite-time trajectories of continuous dynamical systems (RNNs) with high probability, provided the hidden layer is sufficiently wide. The theoretical framework connects to the Strong Lottery Ticket Hypothesis (SLTH), yielding an alternative proof of unit-masking SLTH for FFNs and the first proof of unit-masking SLTH for RNNs. Experiments on multi-task image classification, dynamical system generation, and Lorenz attractor forecasting support the theory and reveal interesting emergent properties such as task-specific functional clustering and Jacobian shaping via bias modulation.

---

## Strengths

1. **Novel theoretical framing connecting bias-only learning to universal approximation and SLTH.** The paper provides a clean reduction: bias-only training is shown to be equivalent to unit masking, which allows the authors to leverage and extend SLTH machinery. This reframes what could be a niche observation (biases can approximately mask units) into a substantive theoretical contribution about expressivity with non-synaptic parameters.

2. **First proof of unit-masking SLTH for RNNs.** The paper explicitly claims (and provides a proof sketch for) the first theoretical guarantee that a sub-network of hidden units in a randomly initialized RNN can approximate finite trajectories of a continuous dynamical system. Extending SLTH-style results from FFNs to the recurrent setting, where errors propagate through time, is a genuine advance.

3. **Empirical demonstration of multi-task bias-learning with task-specific unit specialization.** The multi-task experiment (Section 4.1) shows that a single random-weight network with 32K bias parameters can match a 25M-parameter fully-trained network across 7 image classification tasks. The Task Variance clustering analysis (Fig. 1C) revealing distinct functional clusters that are selectively recruited for different tasks is an interesting mechanistic finding, paralleling observations from fully-trained networks.

4. **Mechanistic insight into how bias learning shapes RNN dynamics.** The eigenvalue analysis in Fig. 4B shows that bias learning sculpts the Jacobian (via the activation function derivative) to produce task-relevant dynamics despite fixed random recurrent weights. The sensitivity analysis to recurrent weight gain (Fig. 4D) provides a clear empirical boundary condition for when bias learning succeeds or fails at finite width.

5. **Honest treatment of limitations.** The paper transparently acknowledges the exponential width requirements, the finite-time and point-wise nature of the RNN result, and the confound in the bias-vs-mask comparison. This candor strengthens rather than weakens the work.

---

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **The RNN proof sketch in the main text is too brief to evaluate the core technical claims.** The sketch comprises approximately two sentences (line 124) and simply asserts that the FFN argument carries over "analogously" to the recurrent setting. However, the recurrent setting introduces qualitatively nontrivial issues that the FFN proof does not directly address: errors propagate and compound through time, the sub-network selection (biases) must remain fixed over unrolled time steps, and the universal approximation theorem for RNNs invoked (Schafer 2006) operates under different assumptions than the FFN case. The paper does not explain in the main text how these challenges are resolved. While the full proof likely resides in the appendix (which was stripped during parsing), the main text provides insufficient reasoning for readers to assess the validity of the claim that the SLTH-over-units holds for RNNs.

2. **The theoretical results require hidden-layer widths that scale exponentially in input+output dimension, with no bound or analysis provided.** As the paper acknowledges, the proof requires "exceedingly massive hidden layer widths" — the probability that a random neuron's parameters all fall within an epsilon-window of a target neuron's parameters is exponentially small in the parameter count, implying a required width that is exponential in $d_{in} + d_{out}$. The paper does not bound this width, compare it to known SLTH scaling results (e.g., Malach et al. 2020), or discuss practical regimes where the theory might apply. This is an honest limitation, but its severity for the paper's utility is underexplored.

3. **The bias-learning vs. mask-learning comparison is partially confounded, as the paper acknowledges.** The mask training uses a soft sigmoid with a scheduled steepness parameter, which introduces different optimization dynamics from the bias learning it is compared against. The paper acknowledges this (line 206–207) and draws only cautious conclusions, but the experiment's evidential value for understanding the relationship between the two methods is weakened. The reported correlation of 0.46 between hidden unit variances could partially reflect the specific scheduling artifact rather than an intrinsic property.

4. **The multi-task experiment's claim of "similar performance" needs more careful qualification.** The bias-only network (32K parameters) matched a fully-trained network (25M parameters) on most tasks, which is indeed impressive. However, the fully-trained network — being the same width — was heavily overparameterized. A comparison could also match total parameter budgets (e.g., a narrower fully-trained network with ~32K total parameters) to isolate the effect of architectural constraints. The paper's conclusion is not wrong, but the framing slightly overstates what is demonstrated.

### Trivial
- The notation for the target networks uses $\CN_1$/\CN_2$ for FFNs and $\CR_1$/\CR_2$ for RNNs, but these macros appear only in the proof sketch paragraphs and are not formally introduced; definitions inline would improve clarity.
- Figure 4D's x-axis label "Gain recurrent init." is somewhat ambiguous — the gain $g$ as defined in the text is clearly explained, but the figure label could be more self-explanatory.

---

## Nice-to-Haves

- **Direct empirical test of the universal approximation claim:** The paper validates bias learning on specific benchmarks but does not test whether a wide-enough bias-only network can fit a non-parameterized target function (e.g., a highly oscillatory function, random labels) and compare the empirical width scaling to the theoretical prediction. Such an experiment would directly probe the theory.
- **Controlled comparison of bias and mask learning under identical optimization:** Using hard masks via straight-through estimators would decouple the confound of the sigmoid schedule and provide a cleaner test of whether bias and mask learning converge to similar solutions.
- **Comparison of the required width to known SLTH scaling results:** Positioning the exponential width requirement relative to Malach et al. (2020) or other SLTH work would help readers assess how severe this limitation is relative to the state of the art.

---

## Removed Points

These points were flagged by reviewers but removed after cross-checking against the paper:

1. *"Proposition 1 (ReLU and Heaviside are γ-parameter bounding) is stated without proof in the main text, which is a gap."* — The proposition is labeled as a restatable environment, meaning its proof is in the appendix. The parser strips appendix content. The paper's definition of γ-parameter bounding (Definition 2) is clear, and Proposition 1's claim is plausible and standard. REMOVED per hard rule about missing appendix proofs.

2. *"The comparison to full training is misleading because the fully-trained network was likely narrower."* — The paper explicitly states "the networks had matched size and architecture" (line 143). The bias network used 32,000 hidden units, and the fully-trained network used the same width. The difference is the number of trainable parameters, not the architecture. REMOVED as factually incorrect.

3. *"The paper should include missing related works."* — I cannot confirm which works are actually missing without external literature knowledge. REMOVED per hard rule.

4. *Various formatting/grammar nitpicks.* — These are parser artifacts, not author errors. REMOVED per hard rule.

---

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface a perspective that the paper itself does not already articulate.

---

## Suggestions

1. **Expand the RNN proof sketch in the main text** to at least outline how the static sub-network selection (biases) handles temporally unfolding dynamics, how error accumulation is bounded, and why the universal approximation theorem for RNNs (Schafer 2006) yields a target network $\mathcal{R}_1$ with bounded parameters. A more detailed conceptual roadmap would significantly strengthen reader confidence in the claimed "first proof of SLTH over units for RNNs."

2. **Add a brief scaling discussion** explicitly bounding the required width in terms of $d_{in}, d_{out}, R, \epsilon$ and $\delta$, even if the bound is exponential. Compare this to Malach et al. (2020) or other SLTH bounds so readers can assess the gap between theory and practice.

3. **Replicate the bias-vs-mask experiment** with a hard masking approach (e.g., straight-through Gumbel-sigmoid or binary concrete) alongside the soft-sigmoid scheduling approach, to verify that the observed correlation is not an artifact of the training schedule.

4. **Add a width-scaling experiment** on a synthetic target function (e.g., a 1D or 2D oscillatory function with known Fourier components) to directly probe the predicted exponential scaling, even if only in low dimensions where it is feasible.

---

## Score and Decision

The paper makes a genuinely novel theoretical contribution — extending universal approximation guarantees to bias-only training and providing the first SLTH-over-units proof for RNNs — with supporting experiments that validate the core claims and uncover interesting emergent phenomena. The main weaknesses are that the RNN proof is insufficiently detailed in the main text, the exponential width requirement is discussed but not bounded or compared to the literature, and the bias-vs-mask experiment has an acknowledged confound. None of these are fatal: the paper's central results are well-motivated, the theory is clearly scoped, and the limitations are honestly discussed. The paper represents a solid contribution to both the theory of neural network expressivity and the neuroscience-inspired study of non-synaptic learning.

**Overall assessment: Accept.**

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>