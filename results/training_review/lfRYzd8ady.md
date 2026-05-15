Now I have all the evidence I need. Let me compose the final review.

## Summary

This paper introduces DCWM (Discrete Codebook World Model), a model-based RL method that represents latent states as discrete codes from a fixed codebook (via Finite Scalar Quantization) and trains transition dynamics using a cross-entropy classification loss, avoiding observation reconstruction. The method is evaluated on continuous control benchmarks (DMControl, Meta-World) and achieves strong results, particularly on high-dimensional locomotion tasks (Dog, Humanoid) where it outperforms both TD-MPC2 and DreamerV3.

## Strengths

- **Strong empirical results on challenging high-dimensional control tasks**: DCWM significantly outperforms TD-MPC2 and DreamerV3 on the Dog and Humanoid tasks in DMControl (Fig. 4), where observation spaces are large (ℝ²²³ for Dog) and action spaces are wide (ℝ³⁸). The aggregate results in Fig. 3 confirm that DCWM outperforms both baselines on DMControl across all reported metrics.

- **Clean causal isolation of key design choices**: Figure 5 provides a principled decomposition comparing continuous vs. discrete latent spaces, MSE vs. cross-entropy loss, and deterministic vs. stochastic dynamics. The comparison convincingly shows that the combination of discrete latent space + stochastic dynamics + cross-entropy training drives the improvement, with the "Discrete+CE+det" variant confirming that stochasticity (not just CE loss) is essential. This is the paper's strongest evidence.

- **Novel application of FSQ to world models without reconstruction**: Using Finite Scalar Quantization to obtain a fixed codebook for latent representations, trained via a self-supervised consistency loss, is a technically clean contribution that avoids both the codebook collapse issues of VQ-VAE and the unreliability of reconstruction-based objectives.

- **Robustness to hyperparameters**: Section 5.4/Fig. 10 shows DCWM is not particularly sensitive to codebook size or latent dimension, which is practically useful.

## Weaknesses

### Fatal
None.

### Major

- **Incomplete evidence for the superiority of codebook encodings (Claim C2)**: The experiment in Section 5.3 (Fig. 6) only varies the encoding used by the reward, critic, and policy networks, while the dynamics model always uses the codebook encoding. The paper states that using one-hot or label encodings for the dynamics "led to the agent being unable to learn" (line 231–232) but presents no data or analysis to support this claim. Since the dynamics model is arguably the most important component of a world model, and claim C2 is a stated contribution, the absence of this ablation is a significant gap. The evidence for C2 is therefore limited to non-dynamics components, where codebook encoding shows benefits in sample efficiency (over labels) and computational efficiency (over one-hot).

### Minor

- **Planning uses expected (continuous) codes without ablation**: During decision-time planning (Eq. 12), the paper replaces stochastic discrete samples with the expected code, yielding a continuous vector that "does not necessarily take a valid discrete value" (line 132). The authors note they "find it effective" but provide no comparison to sampling-based planning. This is a gap because the reward and value functions are trained exclusively on discrete codes but evaluated on continuous interpolations during planning. An ablation comparing expectation vs. sampling would clarify whether the discrete structure is actually being leveraged at decision time.

- **"State-of-the-art" claim is overstated for Meta-World**: The abstract claims DCWM "surpasses" TD-MPC2 and DreamerV3 on continuous control benchmarks. However, on Meta-World, the paper reports DCWM "generally matching TD-MPC2" (line 89, Fig. 3 right panel), not outperforming it. The strong outperformance is specific to DMControl (particularly Dog/Humanoid tasks). The claim should be qualified to reflect this task-dependent result.

- **Only evaluated on deterministic environments**: The paper acknowledges this limitation, but it restricts the generality of the contribution. The benefits of modeling multimodal categorical distributions over latent transitions are primarily motivated for stochastic settings, so the deterministic-only evaluation leaves an important question open. This is a scope limitation rather than a flaw in what was done.

### Trivial

- The "Discrete+CE+det" variant description is present but somewhat dense (line 151); a clearer standalone summary in the main text (beyond the figure caption) would improve readability.

## Nice-to-Haves

- An ablation comparing planning with stochastic sampling vs. expected codes (as noted above).
- Reporting what fraction of codes are actively used, with t-SNE visualization of encoder outputs colored by code assignment, to illustrate the learned representation structure.
- A brief note on whether the Gumbel-softmax temperature is annealed or fixed during training.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Criticism about Discrete+CE+det not being fully explained**: The paper explicitly states (line 151) that "logits were obtained as the MSE between the dynamics prediction and each code in the codebook." This is a clear explanation, so the criticism is removed as factually incorrect.
- **Criticism about missing confidence intervals**: The paper reports "95% stratified bootstrap confidence intervals" (line 89) for aggregate results. This criticism is removed as factually incorrect.
- **Criticism about stop-gradient not being discussed**: The paper explains that target codes use stop-gradient to prevent gradients from flowing through the target path (line 91). This is standard practice and adequately described.
- **Criticism about label encodings not being tested for dynamics**: The paper acknowledges trying this and reports it failed (line 231). The criticism that this should have been included is valid (see Major weaknesses above), but the framing in the Harsh Critic that the paper "does not test" it is imprecise — the paper states they tried it. The missing element is data, not absence of trying.

## Novel Insights

Beyond the paper's own contributions, the reviews collectively highlight an interesting tension: the paper's strongest ablation (Fig. 5) isolates the benefit of discrete+stochastic+CE as a package deal, but the weakest link is the claim that the *codebook structure specifically* (rather than any discrete encoding) is responsible. The deterministic environments limitation is also noteworthy — it suggests the stochastic dynamics may be helping via a training regularization effect (Gumbel-softmax sampling during multi-step rollouts) rather than through genuine aleatoric uncertainty modeling, which would be required in stochastic environments. This distinction is important for future work aiming to extend the method to partially observable or stochastic domains.

## Suggestions

1. **Provide the missing dynamics-encoding ablation**: Run a comparison where the dynamics model uses one-hot or label encodings (while keeping the rest of the architecture fixed) and report results — even if they fail, the data is essential evidence for Claim C2.
2. **Ablate planning with vs. without sampling**: Compare the current expected-code planning against sampling-based planning (with and without temperature) to validate that the continuous interpolation doesn't harm performance and to justify the design choice.
3. **Qualify the "state-of-the-art" claim** to distinguish DMControl (clear outperformance) from Meta-World (competitive/matching).
4. **Consider adding a stochastic environment** (e.g., DMControl with sensor noise) to at least partially address the acknowledged limitation.

## Score and Decision

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>