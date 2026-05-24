Round 1 bracket: paper plausibly between ~4.5 and 6. Let me narrow.## Summary

The paper adapts highly-compressed image tokenizer ideas (TiTok-style) to trajectory representation in autonomous driving. It proposes a conditional autoencoder with (i) adaptive soft (noise-injection) quantization and (ii) causally-ordered, variable-length tokens via nested dropout, producing a tiny discrete latent space (e.g. N=3, D=3, N_levels=2 → 512 codes) over which greedy tree search can optimize arbitrary user-specified objectives without retraining. Experiments on the Waymo Open Motion Dataset cover reconstruction, motion prediction, two planning objectives, behavior transfer, and a preliminary multi-agent / LLM-coupled extension.

## Strengths

- **Greedy token search matches or beats the learned encoder on reconstruction (Table 1).** Greedy search with N=3, N_levels=3 reaches ADE 0.301, essentially identical to the unquantized autoencoder (0.298), and clearly beats the encoder under the same quantization (e.g. 0.386 vs 0.403 at N_levels=2). This is a clean demonstration that the causal+quantized latent structure makes discrete latent search a viable substitute for a learned generator.
- **Concrete, reproducible evidence of training-free planning behaviour (Table 3).** Greedy search lifts left-turn success rate from 0% to 75.5% and speed-reduction success from 0% to 63.2%, with near-zero road-edge contact (0% / 0.13%), showing that the framework can synthesize specified maneuvers without retraining.
- **Frozen-tokenizer LLM coupling matches a fine-tuned multimodal baseline (Table 4).** With a small adapter into Qwen3-4B-Instruct, the latent tokens approach Motion-LLaVA on ROUGE-L (0.788 vs 0.792), BLEU (0.611 vs 0.616), and METEOR (0.450 vs 0.449), despite Motion-LLaVA being fine-tuned end-to-end on a 7B base. This is real evidence that the tokens carry high-level semantic content.
- **Adaptive soft-quantization schedule is empirically motivated.** Figure 2 shows the adaptive σ schedule converging to substantially lower training and validation ADE than a fixed-noise baseline, and the connection to amplitude-limited noisy channels (Smith 1971) is a tidy theoretical hook.
- **Honest framing of prediction.** The paper itself states the prediction results are "not competitive with highly tuned state-of-the-art" and shows variance-objective vs random-objective ablation (last row of Table 2) to argue the predicted variance is informative.

## Weaknesses

### Fatal
None — the core mechanism is internally coherent and the central reconstruction/search claim is supported.

### Major

- **The headline "flexible test-time objectives" claim rests on only two objectives and no test-time-flexible baseline (Section 3.4 / Table 3).** The framework's selling point versus guided diffusion, classifier guidance, conditional VAEs, etc., is supported only by a left-turn objective and a speed-reduction objective — both low-dimensional and well-aligned with dataset modes. Section 4 contrasts the approach with loss-guided diffusion in principle ("guided diffusion using arbitrary objective functions can be challenging to implement, as there is no access to the final 'clean' sample…") but never compares against one on the same scenarios. For a paper whose central contribution is *flexibility at test time*, the absence of even a single head-to-head competitor on these tasks is the most consequential gap.

- **The "greedy search significantly outperforms the learned encoder" framing (Section 3.2) needs qualification.** The greedy search uses an ADE objective computed against the ground-truth trajectory; the encoder has no such oracle. As written ("Table 1 shows that greedy search significantly outperforms the learned encoder, demonstrating that greedy token selection is a valid approach"), this invites readers to attribute the gap to the search procedure when it is partly driven by the search's oracle access. The claim is fine if reframed as: greedy search over the tiny latent space *suffices* to recover or exceed encoder-quality reconstructions — but the current sentence is misleading.

- **Multi-agent results (Section 3.5) are too thin to support the section's three sub-claims.** Section 3.5 advances claims about (a) joint multi-agent reconstruction, (b) interaction generation, and (c) interaction understanding. The supporting evidence is one figure (Figure 6) with a single qualitative example, one downstream LLM table (Table 4), and a reference to Table 5 (reconstruction). There is no quantitative measure of how often the joint decoder produces consistent multi-agent behavior under a single-agent objective. Given the headline "joint trajectory tokenization for multi-agent tasks," this section is closer to a teaser than a substantive contribution and should be scoped that way.

### Minor

- **Behavior transfer (Section 3.1, Figure 5b) is reported only qualitatively.** "A class of maneuvers may be characterized by a single latent token sequence … transferred to new environments" is supported by an aggregate visualization over ~250 scenarios with no transfer-success rate, off-distribution failure rate, or comparison against a trivial baseline (e.g., heading-policy library). A numerical summary would convert "interesting examples" into a claim.

- **The "exponentially less than 512" framing of search cost (Section 3.4) is correct but overstates the saving.** 24 vs 512 is real, but the absolute search space is tiny (512 total codes for the planning model, 8 for the prediction model with N=1); the wall-clock figure (115 trajectories/sec) is useful but lacks a comparator (e.g., guided-diffusion planning latency on the same scenes).

- **Adaptive-schedule hyperparameters (Eq. 2: ADE_target, γ, Δσ) lack an isolated ablation.** Figure 2 contrasts adaptive vs. fixed σ; it does not separate the contributions of the three hyperparameters or their sensitivity. Given the paper relies on the schedule as a key design choice, a small sweep would strengthen this section.

- **The abstract's "robotics" framing overgeneralizes from a single dataset.** All empirical work is on WOMD (driving). Section 5 admits manipulation is left to future work, which is fine, but the abstract phrasing ("robotics applications such as manipulation or navigation") oversells scope relative to evidence.

- **Prediction (Table 2) is reasonably positioned as a sanity check by the text, but its inclusion in the main results invites it to be read as a contribution.** minADE₆=0.6793 trails MTR (0.605, the architecture this work builds on) and DriveGPT (0.524). The paper does flag this honestly; the issue is structural placement, not dishonesty.

### Trivial
- None

## Nice-to-Haves
- Add at least one head-to-head with a loss-guided diffusion or classifier-guided generation baseline on the left-turn / speed-reduction tasks (same scenarios, same metrics, plus latency). This directly substantiates the paper's main implicit argument.
- Expand the planning evaluation to combined/conflicting/off-prior objectives (e.g., goal + lane preference + speed cap; goal off the road) so the boundaries of "flexibility" are visible.
- Report a quantitative behavior-transfer success rate with a naive baseline (Section 3.1).
- Report a quantitative joint-consistency measure for Section 3.5 (e.g., interaction-feasibility rate over many scenes when only one agent's goal is specified).
- Empirically verify that the soft-quantization encoder distribution approaches the channel-optimal discrete one alluded to via Smith (1971).
- Reframe Table 2 explicitly as a sanity check rather than a benchmark contribution.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Latent space is extraordinarily small, structurally limits expressible objectives."** The harsh critic's claim that a 512-element space restricts the method to "a maneuver vocabulary of low cardinality per scene" is partly speculative — the same property is what enables exhaustive enumeration and the paper itself motivates this trade-off. Removed as a structural-fatal-style sweep; the limited-objective concern is retained, but anchored to the actual evaluation rather than to capacity arithmetic.
- **"Missing engagement with MPC over learned dynamics / conditional behavior cloning / Diffuser-style planners."** Per rules, do not assert missing related work without external verification.
- **Generic "this paper addressed an important problem" framing** from the strength finder if any — kept only the specific evidence-backed strengths.
- **"Motion-LLaVA comparison uses a different base LM and is therefore unfair."** This is asymmetric in the paper's *disfavor* (Motion-LLaVA is end-to-end fine-tuned 7B, this method uses a frozen tokenizer + adapter on a smaller LM). Per the hard rule on unfair-against-self comparisons, this is intentional and not a weakness.

## Novel Insights

None beyond the paper's own contributions. The central observation — that highly compressed, causally-ordered, lightly-quantized latents make training-free search a credible substitute for a learned conditional generator — is the paper's own thesis, and the reviews surface no insight beyond it.

## Suggestions

- Replace the "greedy search significantly outperforms the learned encoder" sentence in §3.2 with one that explicitly notes the oracle nature of the search objective.
- Move Table 2 to "sanity check" framing in the text and surface Table 3 (and an expanded version of it) as the main planning result.
- Add a single guided-diffusion baseline (e.g., loss-guided trajectory diffusion) on the same ~300 left-turn and ~800 speed-reduction scenarios; report success, edge-contact, and latency.
- Provide a small Eq.-2 hyperparameter sweep (ADE_target, γ, Δσ).
- Quantify behavior transfer in §3.1 with at least one numerical success/failure metric.
- Either expand §3.5 with quantitative joint-consistency metrics and a richer interaction-generation evaluation, or reposition it explicitly as a preliminary demonstration.

## Axis-level evaluation

- **Originality:** Above average. Porting the "highly compressed tokenizer + minimal generator" pattern from image work into driving trajectories, and exploiting the resulting tiny discrete latent for training-free search, is a clean and novel framing.
- **Importance:** Real but not large. Training-free, flexible-objective planning is a legitimate niche, but the paper does not yet demonstrate that its instantiation is the right tool for it.
- **Claim support:** Mixed. Reconstruction and basic planning claims are well supported; flexibility, behavior transfer, and multi-agent claims are under-supported.
- **Soundness:** Sound design, no methodological red flags. Some framing choices (Table 1 oracle comparison; abstract scope) need tightening.
- **Clarity:** Generally clear; figures and tables align with the text.
- **Value to community:** Modest. The reconstruction and search-vs-encoder result is interesting; the test-time-objective story needs the missing baseline to be impactful.

## Score and Decision

**Anchors retrieved:**

Round 1 (bracketing):
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/pzZjyYee6L.md — avg 2.50 — Reject — trajectory forecasting paper; this paper is clearly stronger (better motivation, cleaner thesis).
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/k1qVBh5fnb.md — avg 3.40 — Reject — Latent Diffusion Planning; this paper is more original and better motivated.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/OZ3NXrF3gQ.md — avg 2.50 — Reject — Reward-free Policy Optimization; not topically close, but this paper is clearly more polished.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/DCg9r2DKKe.md — avg 2.50 — Reject — STL-Drive; this paper is clearly above.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/r125wFo0L3.md — avg 5.00 — Reject — Large Trajectory Models on WOMD; very comparable: below-SOTA prediction, complex setup, modest empirical case. (Read in full.)
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/72MSbSZtHv.md — avg 5.33 — Reject — RedMotion; close in vibe; this paper has cleaner concept but thinner planning evidence. (Read in full.)
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/UapxTvxB3N.md — avg 5.75 — Accept — Traj-LLM; this paper is more methodologically novel but its empirical case is narrower. (Read in full.)
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/Vv76fCYffN.md — avg 6.40 — Accept — Navigation-Guided Sparse Scene Representation; this paper has thinner downstream evaluation.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/DzGe40glxs.md — avg 8.00 — Accept — emergent planning in model-free RL; this paper is below.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/uKZdlihDDn.md — avg 7.60 — Accept — diffusion graph networks for fluids; not comparable but clearly higher tier.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/agPpmEgf8C.md — avg 8.00 — Accept — predictive auxiliary objectives in RL; clearly higher tier.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/bH6T0Jjw5y.md — avg 8.00 — Accept — Time-lagged Information Bottleneck; clearly higher tier.

Initial bracket from Round 1: **[4.5, 6.0]**.

Round 2 (narrowing):
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/sAOtKKHh1i.md — avg 5.00 — Reject — Subwords as Skills (tokenization for sparse-reward RL); this paper is comparable in conceptual ambition but with broader scope.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/mb2ryuZ3wz.md — avg 5.75 — Accept — "How many tokens is an image worth?" — closest methodological analogue (variable-length tokens via recurrent encoding). That paper has more thorough ablations and downstream validation; this paper has a more novel application but thinner planning evaluation. (Read in full.)
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/sfTsvy05MX.md — avg 4.75 — Reject — LL-VQ-VAE; this paper is more ambitious in framing.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/8ROIRnKloJ.md — avg 5.67 — Reject — ε-VAE; comparable but with stronger experimental section.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/TOiageVNru.md — avg 6.00 — Accept — Physics-informed TD metric learning; not directly comparable but better-supported claims.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/hPWWXpCaJ7.md — avg 6.00 — Accept — GEVRM; broader empirical case than this paper.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/B2N0nCVC91.md — avg 6.50 — Accept — FLIP; broader and more thorough.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/c0chJTSbci.md — avg 6.25 — Accept — Zero-Shot Robotic Manipulation with image-editing diffusion; broader empirical case.

**Comparison and final placement.** The paper sits roughly between the "Large Trajectory Models" anchor (5.0, reject; below-SOTA WOMD prediction, complex framework not justified by results) and the "How many tokens is an image worth?" anchor (5.75, accept; same tokenization paradigm but with broader empirical validation). Like the former, this paper's prediction is below SOTA and its planning evaluation is narrow (two objectives, no test-time-flexible baseline). Unlike the former, it has a sharper conceptual contribution (training-free latent search), clean reconstruction-vs-encoder evidence (Table 1), a credible LLM-coupling result (Table 4), and honest scoping of the prediction result. It does not reach the empirical breadth of the 5.75–6.0 accept anchors. I place it just under the borderline.

MY FINAL SCORE: <score>5</score>
MY FINAL DECISION: <decision>Reject</decision>