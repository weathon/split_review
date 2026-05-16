Now I have all the information needed. Let me synthesize the final review.

## Summary

This paper proves, for the first time, that feedforward and recurrent neural networks with fixed random weights can achieve universal function approximation (or finite-time trajectory approximation for RNNs) when only the bias parameters are trained, under the assumption of a "bias-learning" activation function (e.g., ReLU). The theoretical existence proofs are supported by experiments on multi-task image classification (7 tasks), dynamical system generation (cosine, van der Pol, Lorenz), and comparisons with mask learning. The paper is a theoretical contribution with illustrative experiments, relevant to neuroscience (non-synaptic plasticity) and AI (bias fine-tuning).

## Strengths

- **First theoretical proof of universal approximation for FFNs trained only on biases (Theorem 1):** The paper proves that a single-hidden-layer network with fixed random weights (sampled uniformly) can approximate any continuous function on a compact set with high probability, using only bias tuning. This extends prior work that required training output weights or other parameter subsets, and the proof sketch is coherent and explicitly acknowledges the "exceedingly massive" width requirement.

- **First proof of universal approximation for RNNs trained only on biases (Theorem 2):** Theorem 2 extends the result to discrete-time RNNs, showing finite-time trajectory approximation of smooth dynamical systems with high probability via bias-only learning. The paper honestly notes the limitations (pointwise convergence, finite-time) and discusses how these might be strengthened.

- **Empirical validation across multiple tasks and dynamical systems with strong performance:** Bias-only FFNs achieve accuracy comparable to fully-trained networks on 7 image classification tasks (Fig. 1B), and bias-only RNNs generate complex dynamics (cosine, van der Pol oscillator, Lorenz system) with R² > 0.99 (Figs. 3A, 4A), despite orders of magnitude fewer trainable parameters. This demonstrates practical viability beyond the theoretical guarantee.

- **Mechanistic analysis reveals task-specific functional organization (Fig. 1C):** K-means clustering of Task Variance reveals that bias learning produces task-specialized hidden units, similar to findings in fully-trained networks, providing insight into how bias-only networks solve multiple tasks.

- **Jacobian analysis reveals mechanism for oscillation generation in bias-trained RNNs (Fig. 3B):** By tracking eigenvalue spectra of the Jacobian, the paper shows that bias learning shapes the effective connectivity to produce oscillatory dynamics while the fixed recurrent weights remain unchanged, giving a clear dynamical-systems explanation for how bias-only training works in the recurrent case.

- **Systematic comparison with mask learning (Fig. 2):** The paper compares bias learning and unit-masking on matched weights, finding a correlation of 0.46 between hidden unit variances and a slight accuracy advantage for bias learning. This helps position bias learning within the lottery-ticket literature.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Gap between theory's width requirement and experimental regime:** The proof relies on constructing an extremely wide network whose hidden-layer width must be large enough that random units fall within ε-windows of target parameters — a requirement that implicitly scales exponentially with the input dimensionality + output dimensionality. For MNIST (784 inputs, 10 outputs), the theoretical width required would be astronomical. The paper acknowledges "exceedingly massive hidden layer widths" (line 96) but never quantifies this scaling or discusses why experiments succeed with moderate widths (e.g., 32,000 for MNIST). This creates a disconnect: the theory establishes possibility-in-principle, but the paper does not explain whether the experiments operate in a regime the theory covers, or whether a different mechanism (e.g., graded masking rather than hard on/off) accounts for the empirical success. Adding a brief discussion of this gap — even if informal — would significantly strengthen the paper.

- **Missing experimental details for the non-autonomous RNN experiment (Fig. 4):** The caption and text for the Lorenz system experiment specify that the hidden width is 1024 units, but do not state whether the fully-trained and bias-only networks had matched trainable parameter counts or what the fully-trained network's architecture was. This is provided for the autonomous RNN experiment (Fig. 3D caption: "fully-trained and bias-learning networks had the same number of learnable parameters") but omitted for Fig. 4, making the comparison impossible to assess.

### Trivial

- **Weight distribution mismatch between theory and RNN experiments:** The theory (Theorem 2) assumes weights sampled uniformly from $[-R, R]$ (distribution $p_R$). The RNN experiments (Fig. 3, 4) use Gaussian weights (recurrent: $(g/\sqrt{m})\mathcal{N}(0,1)$, output: $\mathcal{N}(0,1/m^2)$). The FFN experiments correctly use uniform weights matching the theory. The proof likely extends to any continuous distribution with density bounded away from zero on the required interval, but the paper should note this explicitly or use uniform weights in the RNN experiments for consistency.

## Nice-to-Haves

- **Comparison against a matched-parameter-count fully-trained network in the multi-task experiment:** The paper compares bias-only (32K parameters) against a much larger fully-trained network (25M parameters). The bias-only network's competitive performance is impressive, but comparing against a smaller fully-trained network with ~32K parameters would help isolate the effect of bias-only learning versus parameter count.

- **Quantitative scaling analysis:** A non-asymptotic bound relating hidden width to $\epsilon$, $\delta$, and input/output dimensions — even a loose one — would help readers understand the gap between the theory and experimental regime.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Proposition 1 justification missing from main text:** The Harsh Critic notes the proof is deferred to the appendix. Per guidelines, missing appendix content is a parser artifact — the appendix exists in the original submission. Removed.

- **"The paper should also cover Y / domain Z / additional tasks":** No such points were present; all criticisms were within scope.

- **Criticism about unfair comparison (multi-task):** The Harsh Critic suggests comparing against a fully-trained network with matched parameter count. The current asymmetry (25M params vs. 32K) actually favors the baseline, not the author's method, making the bias-only result *more* impressive. This is not a weakness. Moved to Nice-to-Haves.

## Novel Insights

The reviews converge on a key observation not fully articulated in the paper: the theoretical existence proof and the experimental demonstrations effectively make *different* claims about why bias learning works. The proof says "with astronomically many units you can do exact masking"; the experiments say "with moderate units you get good performance." The paper would benefit from treating these as complementary but distinct contributions — the theory showing that in-principle universal approximation is possible (ruling out fundamental impossibility), and the experiments showing empirical viability via mechanisms that may differ from the proof's hard-masking construction (e.g., graded activation adjustments). This reframing would resolve the apparent tension and make both contributions stronger.

## Suggestions

- Add a discussion section (or expand the existing Discussion) that explicitly addresses the width scaling gap. At minimum, state the rough scaling relationship implied by the proof, acknowledge that the experiments operate far from this regime, and offer a hypothesis for why (e.g., graded biases provide continuous adjustments, or the tasks do not require exact approximation). This honesty would strengthen rather than weaken the paper.

- In the non-autonomous RNN experiment (Fig. 4), specify the architecture and parameter counts for the fully-trained comparison network, matching the level of detail provided for Fig. 3.

- Add a sentence noting that the proof's reliance on uniform sampling can be relaxed to any continuous distribution with density bounded away from zero on the relevant interval, justifying the use of Gaussian weights in RNN experiments.

## Score and Decision

The paper delivers a novel theoretical contribution (first proofs of universal approximation via bias-only learning for both FFNs and RNNs) supported by well-designed experiments and mechanistic analysis. The primary weakness — the unaddressed gap between the theory's astronomical width requirement and the experiments' moderate widths — is a genuine limitation but does not invalidate either the theory (which is a valid existence proof) or the experiments (which demonstrate practical viability through an apparently different mechanism). The paper is honest about needing "exceedingly massive" widths and would be strengthened by discussing this gap explicitly. Overall, the paper makes a solid contribution to the expressivity literature with relevance to both neuroscience and AI.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>