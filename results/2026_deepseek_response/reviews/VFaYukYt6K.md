Now I have enough calibration data to finalize. Let me write the consolidated review.

## Summary

This paper proposes a framework for motion planning by searching over the latent tokens of a highly compressed, causally-ordered conditional autoencoder trained on the Waymo Open Motion Dataset. The key idea is that with extreme compression (N=3 tokens, D=3 dimensions), a simple greedy best-first search over discretized token values can optimize arbitrary user-specified objectives at test time without retraining any models. The paper demonstrates token semantics (behavior transfer), motion prediction via variance-minimizing search, guided maneuver generation (left turn, speed reduction), and multi-agent interaction modeling.

## Strengths

1. **Novel adaptive soft quantization scheme.** The paper introduces a noise-injection mechanism (Equations 1-2) that avoids codebook collapse issues common in VQ-VAEs while still producing the quantized latent structure needed for discrete search. The adaptive schedule that gradually increases noise until a target reconstruction accuracy is reached is clever, well-motivated, and empirically validated (Figure 2 shows it outperforms fixed noise levels).

2. **Greedy search matches or exceeds the learned encoder on reconstruction.** Table 1 is the paper's strongest empirical result: greedy search with 3 tokens at N_levels=3 achieves ADE of 0.301 vs. the autoencoder without quantization at 0.298, proving that search can effectively navigate the latent space. This directly validates the core claim that the causally ordered, structured latent space enables efficient exploration.

3. **Token semantics and behavior transfer are compelling demonstrations (Section 3.1).** The token swapping experiments (Figure 5a) show genuinely semantic transfer — decoding a trajectory encoding in a different environment produces coherent, semantically appropriate behavior. The automatic identification of token sequences encoding specific maneuver classes (e.g., left turn, deceleration) and their transfer across hundreds of environments (Figure 5b) is a strong qualitative demonstration that the latent space captures meaningful behavior structure.

4. **Planning with arbitrary objectives achieves meaningful success rates with practical efficiency.** Table 3 shows 63-76% success rates on left-turn and speed-reduction objectives across hundreds of scenarios, with near-zero road edge contact. The method runs at 115 trajectories/sec on an RTX 6000 Ada GPU, making it practical for real-time planning. The efficiency claim (24 decoder evaluations vs. 512 exhaustive) is well-supported.

## Weaknesses

### Fatal
None.

### Major

1. **No comparison against trajectory optimization baselines for planning tasks.** The paper's central claim is that latent search "combines deep priors with model-based objectives." However, the planning experiments (Section 3.4) only compare against the original scenario behavior and token search at different depths. There is no comparison against classical trajectory optimization (e.g., optimizing the same objective with dynamics constraints directly in trajectory space), against diffusion-based planning, or against any other planning method. Without such baselines, it is unclear whether the latent search actually produces *better* or *more realistic* trajectories than simpler alternatives, or whether the decoder's