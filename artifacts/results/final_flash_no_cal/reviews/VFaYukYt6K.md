Now I have sufficient information to write the consolidated review.

## Summary

This paper proposes a conditional trajectory autoencoder that learns a highly compressed (N=3, D=3), causally-ordered, discrete-valued latent space for trajectories, and demonstrates that a simple greedy search over these latent tokens enables motion planning with arbitrary user-specified objectives at test time without retraining. The method is evaluated on the Waymo Open Motion Dataset for reconstruction, prediction, planning (left-turn and speed-reduction maneuvers), and multi-agent interaction modeling.

## Strengths

- **Greedy latent search matches or outperforms the learned encoder for reconstruction (Table 1).** This validates the core representation design: with 3 tokens at N_levels=3, greedy search achieves 0.301 ADE versus the unquantized autoencoder's 0.298. The result shows the causal, discrete structure is exploited by greedy search to compress at least as effectively as the trained encoder.

- **Planning with arbitrary objectives succeeds without retraining (Table 3).** Token search achieves 75.5% success for left-turn maneuvers and 63.2% for speed reduction over automatically selected WOMD scenarios, while maintaining zero or near-zero road-edge contact. This directly demonstrates the framework's key promise of flexible test-time optimization of user-specified objectives.

- **Adaptive soft quantization demonstrably improves over fixed noise injection (Figure 2).** The adaptive schedule (Eq. 2) produces lower and more stable validation ADE than a fixed noise level, justifying the design choice and showing rigorous empirical support for this technical component.

- **Causal ordering and nested dropout produce variable-length coarse-to-fine reconstructions (Figure 3).** The qualitative demonstration that using more tokens improves reconstruction fidelity and reduces predicted uncertainty directly supports the greedy search strategy, where tokens can be selected one at a time.

- **Computational efficiency makes the approach practical (Section 3.4).** Greedy search with N=3, D=3, N_levels=2 requires only 24 decoder evaluations per scenario and generates approximately 115 trajectories/second on an RTX 6000 Ada GPU.

## Weaknesses

### Major

- **Planning evaluation lacks baselines that would contextualize the results.** The paper demonstrates that greedy token search can achieve 75.5%/63.2% success for left-turn/speed-reduction objectives, but provides no comparison to alternative methods — not even a simple trajectory optimizer in the original space, gradient-based optimization in a continuous latent version of the same autoencoder, or a learned policy. Without such baselines, it is impossible to determine whether the proposed approach offers advantages in solution quality, feasibility, or computational efficiency over standard alternatives, which weakens the central claim that this framework is useful for robotics planning.

- **Insufficient ablation studies support the design choices.** The method incorporates several non-trivial components (adaptive soft quantization, causal masking, nested dropout, hard quantization at test time, greedy search), yet only one is ablated (adaptive vs. fixed noise, Figure 2). The importance of causal ordering, nested dropout, and the discrete token space for the success of greedy search is not isolated. Controlled experiments removing causal masking, replacing discrete quantization with continuous latents, or testing gradient-based optimization in the same latent space would be needed to establish which design choices are essential versus incidental.

### Minor

- **The prediction evaluation does not explain how 6 trajectory modes are generated.** The paper reports minADE6/minFDE6 metrics requiring six trajectory predictions, yet uses a single-token model (N=1, D=3) that normally produces a single trajectory output. How multiple modes are obtained (beam search with different initializations, top-K from the search, or another mechanism) is not specified, making the metric incompletely defined. Additionally, standard prediction metrics such as miss rate and overlap are omitted.

- **Multi-agent interaction generation is almost entirely qualitative.** The joint trajectory generation results (Figure 6) show only two qualitative examples. No quantitative metrics measure interaction quality (collision rate, off-road rate, goal success rate, interaction plausibility). The paper cites Table 5 for reconstruction metrics, but that table is in the appendix (stripped from the reviewed text); the main paper should include key reconstruction metrics to support the multi-agent claims.

- **The LLM reasoning experiment (Table 4) has confounded comparisons.** The comparison uses Qwen3-4B-Instruct-2507 with LoRA adapters against LLaVA-v1.5-7b and Motion-LLaVA (also 7B), varying both model architecture and scale simultaneously. This makes it difficult to attribute the competitive performance specifically to the autoencoder tokens rather than to the smaller model's efficiency or the LoRA fine-tuning approach. The experiment is presented as evidence of token semantics but would be more informative with a controlled comparison holding the base LLM fixed.

- **Token semantics analysis (Section 3.1) lacks quantitative support.** The behavior-transfer experiment selects the "most common token encoding" for maneuver buckets, but does not report how frequently that encoding occurs within each bucket, how many scenarios each bucket contains, or the variance of reconstruction error when applying the transferred encoding across environments.

- **The two-stage multi-agent architecture (Section 3.5) is introduced without justification.** Why a separate second-stage encoder/decoder over agent features is needed rather than jointly tokenizing all agent trajectories from the start is not discussed.

### Trivial

- The edge contact rate of 0.76% for "original scenarios" in the speed-reduction experiment is not explained, and seems high for ground-truth driving data.
- The left-turn success metric (cumulative heading change >45°) does not distinguish genuine intersection left turns from U-turns or trajectories that go off-road without edge contact.

## Nice-to-Haves

- Sensitivity analysis for the adaptive noise hyperparameters (γ, Δσ, ADE_target).
- Quantitative evaluation of the coarse-to-fine representation (reconstruction error as a function of number of tokens held out), to substantiate the qualitative Figure 3.
- Failure case analysis for planning (examples where greedy search fails and why).
- Ablation isolating whether a simpler continuous latent space with gradient-based optimization could achieve similar planning results — this would clarify the necessity of the discrete design.
- Testing more diverse planning objectives beyond left-turn and speed-reduction.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism that Table 1 comparison is "misleading" because greedy search uses ground-truth information the encoder never has access to.** This is factually incorrect: both the encoder and greedy search operate in a reconstruction setting where the ground-truth trajectory is available. The encoder receives the trajectory as input (that is the point of an autoencoder), and the greedy search evaluates reconstruction ADE against the same trajectory. The comparison is between two methods for compressing a given trajectory, and the encoder does have access to the trajectory at test time. Removed as a misunderstanding of the paper.

- **Criticisms about missing appendix content, missing proofs, or absent references.** The parser strips appendix sections from all papers; these exist in the original submission. Removed per rules.

- **Formatting and style nitpicks.** Removed per rules.

- **Criticism about missing related works (PlaNet, Dreamer, guided diffusion).** The rule prohibits me from introducing missing-related-work criticisms as I lack external sources to confirm existence or framing. Removed per rules.

- **Criticism that the paper should commit to single-mode metrics or explain multiple modes.** Kept the explanation gap as a Minor weakness but removed the framing that the paper's comparison in Table 2 is "misleading" — the paper's own language is measured ("While not competitive with highly tuned state-of-the-art trajectory prediction methods, performance exceeds or approaches that of many common prediction baselines"), and this is an accurate characterization of the results.

- **Claim that adaptive noise schedule hyperparameters lack sensitivity analysis.** This is a standard "could be more thorough" criticism that applies to nearly every hyperparameter in every paper. It is a nice-to-have, not a weakness.

- **Strength from the Strength Finder about multi-agent tokenization enabling "consistent interaction generation"** with evidence from Figure 6 and Table 4. The interaction generation part (Figure 6) is qualitative only, weakening the "consistent" claim. Moved the LLM result to its own Minor weakness.

## Novel Insights

None beyond the paper's own contributions. The reviews surface expected concerns about missing baselines, insufficient ablations, and incomplete evaluation — these are standard rigor gaps rather than observations that reveal something new about the approach or its implications.

## Suggestions

1. Add planning baselines — at minimum, compare greedy search over discrete tokens to gradient-based optimization in a continuous-latent version of the same autoencoder and to a simple trajectory optimizer (e.g., MPC) in the original space.
2. Run controlled ablations removing causal masking, nested dropout, and discrete quantization to isolate essential components.
3. Clarify how 6 modes are obtained for the prediction metrics (minADE6/minFDE6).
4. Add quantitative multi-agent interaction metrics (collision rate, off-road rate) for the joint generation scenarios.
5. Control the LLM experiment by comparing the same base LLM with and without the autoencoder tokens, rather than comparing different model families.
6. Provide quantitative support for the token semantics analysis (frequency of selected encodings, variance of transfer fidelity).

## Score and Decision

**MY FINAL SCORE:** <score>6.0</score>
**MY FINAL DECISION:** <decision>Accept</decision>