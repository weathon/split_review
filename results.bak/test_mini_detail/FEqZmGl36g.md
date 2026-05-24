Now I have all the information I need. Let me synthesize the final review.

## Calibration Summary

**Round 1 (Bracketing):**
- Weak band (score < 3.5): Papers like "Flow Matching for One-Step Sampling" (3.25), "TCIG" (1.5) — rejected papers with fundamental flaws
- Middle band (3.5–7.5): "Discrete Guidance" (6.5, accepted poster), "Controlled Denoising" (4.6, rejected), "Correcting Flows" (5.25, rejected), "Motion Guidance" (7.0, accepted poster)
- Strong band (7.5+): "Simplifying CMs" (9.2, oral), "Learning Energy Decompositions" (8.0, oral) — top-tier papers

**Round 2 (Narrowing):**
- "Injective flows for star-like manifolds" (6.0, accepted poster) — similar level of contribution, solid but narrow
- "Improving GGNS" (6.33, rejected) — despite similar score, rejected due to novelty concerns; ESS-Flow has clearer novelty
- "Deep MMD Gradient Flow" (5.75, accepted poster) — solid integration of ideas but uncompetitive performance

**Initial bracket:** The paper sits between 5.0 and 7.0.
**Narrowing:** Compared to "Discrete Guidance" (6.5, accepted), ESS-Flow has a comparably clear contribution but a less clean protein experiment. Compared to "Injective flows" (6.0, accepted), ESS-Flow has broader applicability but more experimental ambiguity.

**Final score: 6.0** — comparable to accepted poster papers like "Injective flows" and slightly below "Discrete Guidance" due to the protein experiment clarity issue. The method contribution is clear, well-grounded, and practically relevant.

Here is the consolidated review:

---

## Summary

This paper introduces ESS-Flow, a training-free method for controlled generation with pretrained flow-based generative models. The key insight is to formulate conditional generation as Bayesian inference in the Gaussian source space of flow models and apply elliptical slice sampling (ESS), which requires only forward passes through the transport map and potential function — no gradients or Jacobians. The method is demonstrated on materials generation (targeting properties like bulk modulus, band gap, and space-group symmetry) and protein backbone structure prediction from sparse distance measurements.

## Strengths

- **Gradient-free controlled generation with non-differentiable potentials.** The space-group experiment (Section 5.1) targets a specific crystallographic symmetry using a binary indicator computed by a non-differentiable external program. ESS-Flow achieves 92.3% of samples with the target space group vs. 2.5% from the unconditional prior (Table 3). This directly demonstrates the paper's core claim — applicability when gradients are unavailable — which gradient-based methods (D-Flow, PnP-Flow) cannot even attempt on this task.

- **Geometric convergence guarantee.** Proposition 1 (Section 4.1) establishes that the ESS-Flow Markov chain converges geometrically fast in total variation under mild regularity conditions on the pullback potential. This provides a theoretical grounding absent from optimization-based methods like D-Flow and PnP-Flow, which offer only point estimates with no asymptotic sampling guarantees.

- **Avoids trapping in disconnected manifolds.** The toy experiment (Figure 2) shows D-Flow samples becoming trapped in a disconnected manifold component, while ESS-Flow samples are well-distributed along the target. This concretely illustrates a failure mode of gradient-based source-space methods that ESS-Flow overcomes by being gradient-free.

- **Minimal hyperparameter tuning.** Algorithm 1 and the surrounding text note that ESS-Flow has only two free parameters: the number of MCMC steps and the ODE discretization (the latter addressed by the multi-fidelity extension). This is a practical advantage over DAPS, PnP-Flow, and D-Flow, which require tuning learning rates, noise schedules, or regularization strengths.

## Weaknesses

### Fatal
None.

### Major

- **Unclear experimental setup in the protein backbone experiment may undermine the comparison.** Section 5.2 states: "Since we require a deterministic mapping between source and data samples, we modify Chroma's random protein graph construction to use k-nearest neighbors and generate samples with the probability flow ODE." This modification is necessary for ESS-Flow and D-Flow (which operate in source space). It is not explicitly stated whether ADP-3D and DAPS also use this modified Chroma, or whether they were run on the original (stochastic, random-graph) version they were designed for. ADP-3D and DAPS rely on the noising process of the original diffusion model, and switching to a probability-flow ODE changes the generative model in a way that may handicap these methods. The resulting comparison — where ADP-3D and DAPS show very low ELBO (-5.68, -8.07) and very high clash counts (731.3, 483.3) while ESS-Flow and D-Flow (both source-space methods) show ELBO near the unconditional — is consistent with a prior mismatch rather than an inherent advantage of ESS-Flow. The authors must clarify whether all methods used the same Chroma model. If the comparison is not prior-controlled, the protein results cannot be interpreted as supporting ESS-Flow's superiority. **This is a clarity issue in experimental reporting that needs full resolution; it does not invalidate the method itself or the materials experiments.**

### Minor

- **The convergence guarantee (Proposition 1) does not formally cover the binary-indicator potential used in the space-group experiment.** Proposition 1 requires the pullback potential to be "bounded away from 0 and ∞ on compact sets." The space-group task uses g(c) = 𝟙[P_c = y], which is zero almost everywhere in the source space, violating this condition. The paper does not discuss this. While the method works well empirically (92.3% success), the geometric convergence guarantee does not formally apply to this experiment. A brief clarifying remark would be appropriate.

- **The multi-fidelity extension has limited practical utility.** The importance-weighting scheme yields effective sample sizes of 65.3% and 33.9% for bulk modulus and shear modulus, but only 0.1% and 1.0% for band gap and stability (Section 5.1.1). The poor results occur on the sharpest target distributions, exactly where computational savings would be most valuable. While the paper honestly presents this as a "proof of concept" and acknowledges the limitation, the current scheme adds little value as presented.

### Trivial
None.

## Nice-to-Haves

- The runtime cost comparison across methods could be more explicit (e.g., ODE solves per valid sample).
- The claim that ESS-Flow is "asymptotically exact" could be qualified: exact for the discretized transport map, not the continuous-time ODE.
- The notation for T_δ^Δ in Equation (4) is somewhat overloaded and could be clarified.

## Removed Points

- **Criticism that the protein experiment "invalidates the comparison" and is "structurally compromised"** — This is too strong given the ambiguity in the text. The paper describes a modification to Chroma in the experimental setup section, which suggests all methods use the same modified model. The issue is a lack of explicit clarification, not a proven structural flaw. Moved from "Fatal" to "Major" with softened language.
- **Criticism about D-Flow being unfairly compared with continuous atomic-number approximation** — The paper acknowledges this and explains it as necessary to enable comparison; this is a reasonable design choice for the experiment.
- **Strength finder's claim about multi-fidelity as a core strength** — The multi-fidelity results are mixed and the paper itself acknowledges their limitation. Calling this a "strength" overstates the evidence.
- **Strength finder's claim about "produces more realistic samples in protein structure prediction"** — This claim depends on the unresolved prior-clarity issue and cannot be asserted as a strength without qualification.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a new perspective that the paper itself does not already articulate.

## Suggestions

1. **Clarify the protein experiment setup explicitly.** State whether ADP-3D and DAPS were run on the same modified Chroma (k-NN graph, probability flow ODE) or the original Chroma. If the latter, the comparison is not valid and should be removed or reframed. If the former, explain how these methods were adapted to the probability flow ODE setting and add a note about any implementation challenges.
2. **Add a brief remark about the binary-indicator potential and Proposition 1.** A sentence noting that the space-group experiment operates outside the formal convergence guarantee (since the potential is not bounded away from zero) but works well in practice would be sufficient.
3. **Reframe or remove the multi-fidelity contribution.** Either strengthen it with a practical scheme (e.g., coarse-to-fine burn-in) or remove it from the contributions list and instead present it as a negative result with lessons for future work.

## Score and Decision

Based on the comparison with calibrated anchors: this paper is stronger than "Correcting Flows with Marginal Matching" (5.25, rejected) and "Controlled Denoising" (4.6, rejected), comparable to "Injective flows for star-like manifolds" (6.0, accepted poster) and "Deep MMD Gradient Flow" (5.75, accepted poster), and slightly below "Unlocking Guidance for Discrete State-Space" (6.5, accepted poster) due to the experimental clarity issue. The core method contribution — gradient-free source-space MCMC for flow-based models with a convergence guarantee — is novel, well-motivated, and convincingly demonstrated on the space-group task. The protein experiment needs clarification but does not undermine the overall contribution.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>