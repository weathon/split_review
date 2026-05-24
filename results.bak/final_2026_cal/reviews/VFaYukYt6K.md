Now I have all the information I need. Let me write the final consolidated review.

## Calibration Summary

**Round 1 (Bracketing):** Initial search positioned the paper in the 3.5–7.5 band; papers below 3.5 were clearly weaker (scores 2.67–3.33, different topics), papers above 7.5 were on unrelated topics (image generation, protein design). The closest topical match was in the 3.5–7.5 band.

**Round 2 (Narrowing):** The most relevant anchors within the bracket are:
- **LAP** (avg 4.67, Reject): latent diffusion planner. Has closed-loop SOTA results on nuPlan but limited novelty. The paper under review has more novel framework but weaker planning evaluation. Comparable or slightly below.
- **TrajTok** (avg 5.00, Accept Poster): trajectory tokenizer with strong empirical results but incremental contribution. The paper under review has broader scope and more novel idea but weaker validation. Slightly below.
- **FlowDrive** (avg 4.50, Reject): flow-matching planner with SOTA results but limited novelty. The paper under review has more novelty but weaker results. Comparable.
- **ReflectDrive** (avg 4.67, Accept Poster): discrete diffusion + reflection for planning. Mixed reviews on novelty and evaluation. Comparable.
- **VADv2** (avg 5.50, Accept Poster): tokenized action space, SOTA on multiple benchmarks. Stronger empirical validation than the paper under review.

**Final Score:** The paper has genuine novelty (compressed latent tokens + greedy search for planning) and solid prediction results, but its core claim about planning with arbitrary objectives is inadequately validated — no planning baselines, no composable-objective experiments, narrow metrics. This places it below TrajTok (5.00) and VADv2 (5.50), around the level of LAP (4.67) and FlowDrive (4.50), but with a different weakness profile (more novelty, less evidence). The evidence gap rates a 4.0 — the idea is promising but not yet ready for acceptance.

**Anchors retrieved (all rounds):**

| Anchor ID | Avg Score | Round | Comparison |
|-----------|-----------|-------|------------|
| 8viZQgKVWT | 2.67 | 1 | Much weaker paper, withdrawn |
| IyTA7a9ppZ | 3.00 | 1 | Weaker paper, different framing |
| MKM8iEaowV | 3.00 | 1 | Weaker, diffusion+RL planning |
| upMaonekAE | 3.33 | 1 | Weaker, different scope |
| uHEaVkj8I3 (LAP) | 4.67 | 1,2 | Latent planner, SOTA results but less novel; comparable to slightly above |
| w12WVeZN0z (FlowDrive) | 4.50 | 1,2 | Flow matching planner, SOTA but limited novelty; comparable |
| 0a4dA6eUHN (VADv2) | 5.50 | 1,2 | Stronger empirical validation, somewhat different framing |
| iB9qx28gv4 | 4.00 | 1 | 4D latent world model, different domain |
| Zvy2agYouY (TrajTok) | 5.00 | 2 | Trajectory tokenizer, strong empirical results; slightly above |
| XJxXSMLDoZ (ReflectDrive) | 4.67 | 2 | Discrete diffusion planning, mixed reviews; comparable |
| abJCjkIwi5 (OccDriver) | 5.33 | 2 | Occupancy-based planning, stronger evaluation |

---

## Summary

This paper proposes a framework for trajectory prediction and planning in autonomous driving based on a highly compressed conditional trajectory autoencoder with causally ordered, discrete latent tokens. The key idea is to learn a compact token representation where a simple greedy search over discretized token values can optimize arbitrary test-time objectives (e.g., "turn left," "slow down") by relying on the decoder's generative prior. The autoencoder uses adaptive soft quantization (noise injection) rather than hard VQ, nested dropout for variable-length encoding, and an MTR-style environment encoder. The method is evaluated on the Waymo Open Motion Dataset for reconstruction (Table 1, greedy search matches the encoder), motion prediction (Table 2, competitive results from reconstruction-only training), guided maneuver generation (Table 3), multi-agent interaction modeling, and LLM-based scene understanding (Table 4).

## Strengths

- **Greedy token search outperforms the learned encoder on reconstruction (Table 1).** With just one token at 3 quantization levels, greedy search achieves ADE 0.524 vs. the autoencoder's 0.617, and this advantage holds across token counts. This directly validates that the causal, noise-resilient latent structure makes heuristic search effective — a key enabler of the framework.

- **Competitive motion prediction from reconstruction-only training (Table 2).** The decoder with variance-minimizing search achieves minADE₆ = 0.6793 on WOMD, exceeding the Waymo LSTM baseline (1.0065) and approaching MTR (0.6050) despite being trained purely on reconstruction, not prediction. The random-objective row (0.7311) confirms the objective function matters, not just the decoder.

- **Clean, principled framework for combining deep priors with model-based objectives.** The idea of compressing trajectories into a few causally ordered discrete tokens and then searching over them is conceptually elegant. The adaptive soft quantization is well-motivated (avoids codebook collapse, achieves better training stability than fixed noise in Figure 2), and the nested dropout + causal masking structure (Figure 3) cleanly enables variable-length decoding.

- **Multi-agent interaction generation with only a single-agent objective (Figure 6).** Optimizing only the pedestrian's final position yields consistent joint behavior (the vehicle yields or crosses appropriately), demonstrating that the compressed latent representation captures interaction semantics without explicit multi-objective engineering.

- **LLM transfer matches a dedicated motion understanding model (Table 4).** With a small adapter MLP + LoRA on Qwen3-4B, the token representation matches Motion-LLaVA (a larger, end-to-end fine-tuned model) on WOMD-Reasoning metrics, supporting the claim that tokens carry high-level semantic information.

## Weaknesses

### Major

- **No baselines for the planning experiments (structural gap in evaluation).** Table 3 reports 75.5% success for left-turn and 63.2% for speed-reduction objectives, compared only to "none (original scenario)" at 0%. Without any comparison to a classical trajectory optimizer (e.g., optimizing a piecewise-polynomial trajectory with a kinematic model), a diffusion planner with classifier guidance, or even a simple heuristic, the reader cannot assess whether these success rates reflect a genuine advance or merely the ease of the selected scenarios. This is the paper's central claim ("arbitrary user-specified objectives") and the evidence is incomplete.

- **No composable-objective experiments despite the title claiming "Composable Costs."** The paper tests two objectives individually (turn left, slow down) but never composes them. The title and framing promise compositionality, yet no experiment tests, e.g., "turn left *and* slow down" or any multi-term objective. Given that the framework's main selling point is flexibility, the absence of even a single composable-objective demonstration is a notable gap between the claimed contribution and the evidence.

- **Planning evaluation metrics are too narrow.** The only quantitative safety metric is "edge contact" (collision with road geometry). Collisions with other dynamic agents, kinematic feasibility (jerk, acceleration limits), and ride comfort are not reported. For a planning system, this is an incomplete safety evaluation.

### Minor

- **No ablation against standard vector quantization or finite-scalar quantization.** The paper motivates adaptive soft quantization as a way to avoid VQ training challenges (codebook collapse), but never compares reconstruction quality or planning success against a standard VQ-VAE or FSQ at comparable compression levels. The only comparison in Figure 2 is fixed noise vs. adaptive noise, leaving the reader unsure whether simpler quantization would work as well.

- **Greedy search comparison asymmetry (Table 1).** The greedy search has access to ground-truth trajectories for its reconstruction objective, while the learned encoder does not. The result that search outperforms the encoder is therefore expected and not surprising — the interesting finding is that greedy search is feasible, which is established.

- **Token semantics experiments are qualitative only.** The "library of behaviors" experiment (Figure 5b) uses ~250–200 environments but provides no quantitative success rate or failure analysis. This limits the strength of the claim about "meaningful semantics."

## Nice-to-Haves

- Adding a constant-velocity baseline to Table 2 (prediction) would help calibrate the difficulty, though the existing baselines (Waymo LSTM, MotionCNN, etc.) already provide reasonable context.
- An ablation varying compression level (number of tokens, noise level) and measuring downstream planning success would strengthen the connection between representation quality and planning performance.
- A limitations paragraph (e.g., greedy search may get stuck in local optima, dependence on decoder generalization to out-of-distribution scenarios) would improve the paper's completeness.
- Runtime comparison against alternative planning approaches would contextualize the efficiency claim (115 trajectories/second).

## Removed Points

Criticisms that were removed per the filtering rules:

- **"Missing appendix references / Table 5 not visible"** — The appendix exists in the original submission but is stripped by the PDF parser. Removed per Hard Rules.
- **"Missing hyperparameters in main text"** — The paper gives architecture details (MTR-style, PointNet, transformer dimensions) at a level appropriate for the main text; full details would be in the appendix. Removed per Hard Rules.
- **"The gap between 0.6793 and 0.7311 (random objective) is small"** — A 7% relative improvement in minADE on WOMD is non-trivial. This is an inaccurate assessment of the magnitude. Removed per Hard Rules.
- **"Prediction without constant velocity baseline"** — The paper already provides strong learned baselines (Waymo LSTM at 1.0065 is a standard simple baseline). The critic's estimate of "1.5–2.0" is for a different evaluation setup. Removed as factually questionable and already adequately addressed.
- **"Related work comparison missing"** — Removed per Hard Rules: I cannot verify missing related works without external sources.
- **"Section 2.2 is 'expected, does not provide new insight'"** — This is an opinion about presentation, not a verifiable weakness. Removed.
- **"Multi-agent section feels included for breadth rather than depth"** — Subjective opinion about paper structure, not a specific weakness. Removed.
- **"Formatting/typo nitpicks"** — Removed per Hard Rules.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add planning baselines.** Compare against at least one trajectory optimizer (e.g., optimize a spline in Frenet frame with a learned dynamics model, or use diffusion with classifier guidance on the same WOMD scenarios). Without this comparison, the planning experiments are standalone demonstrations rather than evidence of superiority.

2. **Add at least one composable-objective experiment.** The title promises "composable costs" — a simple composition like "turn left *and* reduce speed to 5 m/s" would make the central claim concrete. This is a low-cost, high-impact addition.

3. **Broaden planning safety metrics.** Report collision rate with other dynamic agents (using available WOMD agent histories), off-road rate, and kinematic feasibility (max acceleration/jerk). This would substantially strengthen the claim that generated behaviors are "feasible and realistic."

4. **Ablate quantization strategy.** Compare adaptive noise injection against a standard VQ-VAE baseline at comparable bitrate to quantify the benefit of the proposed soft quantization.

5. **Discuss limitations explicitly.** The paper should acknowledge that greedy search may converge to local optima, that the decoder's generative prior limits the range of achievable behaviors (it cannot produce maneuvers far from the training distribution), and that WOMD is a log-replay dataset, not an interactive simulator.

## Score and Decision

The paper proposes a genuinely novel and well-motivated framework for combining deep generative priors with flexible test-time optimization via latent token search. The prediction results are solid and the token semantics demonstrations are compelling. However, the central claim about planning with arbitrary objectives is inadequately validated: no baselines for the planning experiments, no composable-objective demonstrations despite the title, and narrow safety metrics. These gaps prevent the paper from making a convincing case for its core contribution. The paper needs substantial strengthening of the planning evaluation before it is ready for acceptance.

<score>4.0</score>
<decision>Reject</decision>