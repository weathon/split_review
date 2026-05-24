Round-1 bracket: this paper has decent empirical results but the harsh critic's concerns (training-free baseline at 47.6% vs trained 52.8%; UI-Vision worse than UI-Venus 7B; OSWorld-G barely better than base) are largely valid against the strong headline framing. Topically closest anchors live in the 5–6 range. I'll narrow.## Summary
GUI-Spotlight is a tool-augmented, multi-turn inference framework for GUI visual grounding paired with a modified GSPO reinforcement-learning objective that adds a behavior-cloning auxiliary term on result-and-format-correct trajectories. With 18.5K training samples and a UI-TARS-1.5-7B initialization the model reaches 52.8% on ScreenSpot-Pro, while a controlled ablation (Figure 5) shows a training-free repeated-single-turn inference baseline using the same base already attains 47.6%, and cross-benchmark results on UI-Vision and OSWorld-G are mixed.

## Strengths
- **Auxiliary cross-entropy term stabilizes RL.** Figure 3 (right) shows that vanilla GRPO/GSPO oscillates and the reward collapses around step 300, whereas the proposed J'(θ) keeps the curve monotonic near 0.9 — a clean empirical demonstration of a useful stabilization trick for multi-turn tool-use RL.
- **Strong absolute result on ScreenSpot-Pro under tight data budget.** 52.8% with 18.5K samples on a UI-TARS-1.5-7B base (Table 3), compared with V2P-7B (50.6% at 9.6M) and GTA-1-7B (50.1% at 1.56M). Even after discounting the inference-time tool-use compute, this is a real improvement over the same base (38.7% → 52.8%).
- **Documentation of negative results.** Section 4.1 reports seven RL variants under matched conditions, including discarded ideas (top-p uncertainty sampling, continuous reference-policy updates), providing concrete numbers (35.8–39.5% for discarded variants vs. 47.6% for the chosen design) that are useful to practitioners.
- **Concrete reward-design ablation.** Figure 4 (right) shows a 10.5-point ScreenSpot-Pro gap between Crop/Extract weight ratios 0.25/0.05 and 0.15/0.15, providing actionable guidance for reward tuning rather than a hand-waved choice.

## Weaknesses

### Fatal
None.

### Major
- **The headline data-efficiency comparison is not apples-to-apples and the controlled comparison shows a much smaller gain.** The abstract and Section 5.1 frame the contribution as "18.5K samples beating 9.6M-sample baselines." But Section 5.4 / Figure 5 reveals that strategy ② (repeated single-turn inference at test time, no GUI-Spotlight training) already reaches 47.6% from the same UI-TARS-1.5-7B base, so the marginal contribution of the entire 18.5K-sample training pipeline and the spotlight tools is only +5.2 points. The paper does not foreground this gap. The trained model also issues multiple model calls per query while V2P-7B/GTA-1-7B run single-pass, so the "trained on 100× less data" framing trades training compute for inference compute that is never quantified (no latency, no token cost, no average number of tool calls per query reported). This makes the headline contribution materially less impressive than the introduction implies.
- **Cross-benchmark picture contradicts the across-the-board win the introduction claims.** On UI-Vision (Table 4) GUI-Spotlight (UI-TARS) reaches 23.4%, *below* UI-Venus-Ground-7B at 26.5% — yet the introduction lists 23.4% as "substantially outperforming comparable 7B baselines." On OSWorld-G (Table 5) GUI-Spotlight reaches 62.7%, only +0.8 over its own UI-TARS-1.5-7B base (61.9%) and 5 points behind GTA1-7B (67.7%). Section 5.3's "competitive with 72B-scale models" framing obscures that the method barely moves from initialization on this benchmark. The win is concentrated on ScreenSpot-Pro, and the paper does not analyze why.
- **The "modified GSPO" framing misattributes credit.** J'(θ) (Eq. on p.4) is defined by filtering to format-and-result-correct trajectories and adding token-level cross-entropy; this is SFT-on-positives mixed into the RL objective. Figure 3 (right) confirms this is the term doing the stabilization, not the GSPO importance-sampling change — vanilla GSPO collapses identically to GRPO. Naming the contribution after GSPO rather than after the filtered behavior-cloning term obscures what is actually doing the work and disconnects the framing from the empirical evidence the paper itself provides.
- **Stage-1 SFT actively hurts (39.3% → 17.8%, Fig. 2) yet is never ablated as removable.** This is an interesting and important finding — SFT on tool-use trajectories degrades grounding accuracy by 21.5 points, which the paper attributes to the model learning to emit tool calls instead of direct answers. But the paper retains Stage 1 in the pipeline without testing whether RL from the raw base (skipping Stage 1) converges to a similar or better point. This is the single most important ablation that is missing, given that Figure 2 already shows the warm-up is harmful in isolation.

### Minor
- **Backbone-contingent generality claim.** The Qwen2.5-VL-7B variant lands at 38.7% on ScreenSpot-Pro and 8.3% on UI-Vision — below OS-Atlas-7B (9.0%) and far below UI-Venus-7B (26.5%). The paper presents the Qwen +11.9 delta as evidence of transfer "beyond UI-specialized backbones," but the absolute numbers suggest the spotlight pipeline depends on a GUI-grounded backbone. The claim should be softened to "complements a GUI-grounded backbone."
- **Reward-weight sensitivity is partially explored.** Only Crop vs. Extract ratio is ablated (Figure 4 right). The Answer/FindColor/Format weights (0.30/0.20/0.20) get no sensitivity analysis. Given that the controlled gain over the training-free baseline is ~5 points, transparency about whether weights were tuned on a held-out split rather than on ScreenSpot-Pro itself would strengthen the claim.
- **Figure 2 stage labeling appears inconsistent with the text.** Section 3.2.2 says Stage 1 uses 2561 SFT samples and Stage 2 uses 12K; the figure/table pair 2561 with "Stage 0" and 12K with "Stage 1." The labeling should be reconciled.
- **Section 4.1 ambiguity over additive vs. independent.** The bar chart compares modifications ①–⑦ "added to" GRPO at 37.3%, but it is not clear from the prose whether modifications stack or are each evaluated against GRPO independently; given that ⑦ jumps by +10.3 while the rest are within ±2.2, this matters for interpretation.

### Trivial
- The Section 5.4 narrative ("a substantive post-training gain") would read more honestly if the 47.6 → 52.8 numbers were stated explicitly in the prose rather than only on the chart.

## Nice-to-Haves
- Report inference-time compute (tokens or wall-clock per query, average tool-call depth) so the trade-off "Nx inference compute for ~500× less training data" is explicit rather than implicit.
- Provide a fair iterative-inference baseline using a stronger backbone (UI-Venus-7B or GTA-1-7B) with GUI-Spotlight's multi-turn prompts but no further training, to isolate whether the gains come from the protocol or from the specific RL recipe.
- Investigate why the spotlight pipeline helps disproportionately on ScreenSpot-Pro (very high-resolution, sparse targets) versus UI-Vision / OSWorld-G; converting this differential into a positioning claim ("we help on 4K, sparse-target benchmarks") would be more defensible than the current across-the-board framing.
- Ablate J'(θ): vary the filter (correct+format vs. correct-only vs. format-only) and vary λ. Given that J'(θ) is the technical novelty, this is the ablation most needed.
- Add a tool-call depth-vs-accuracy curve so readers can reason about the compute/accuracy frontier.

## Removed Points
These points are flagged to be removed; treat them with caution.

- *Harsh critic's request to "lead with the Section 5.4 comparison rather than the Table 3 headline."* This is presentation advice rather than a verifiable defect; the underlying issue (overstated framing) is already captured in the Major weakness.
- *Generic Strength-Finder claim that "documentation of negative results is comprehensive."* Kept (concrete, evidenced) — not removed.
- *"Generality across backbones is a strength" (Strength Finder).* Removed because the absolute numbers on the Qwen variant (8.3% on UI-Vision) contradict the strength; the delta-based framing is the same one criticized in Minor. The deeper observation — that the method depends on a GUI-grounded backbone — is captured under Minor.

## Novel Insights
The single observation across the reviews that is genuinely novel beyond the paper's own framing is the recognition that the paper's "modified GSPO" is, mechanistically, RL plus filtered behavior cloning on successful rollouts, and that the behavior-cloning term — not the GSPO importance-sampling change — is what stabilizes multi-turn tool-use training. Restated: when reward signals are sparse and tool-call format is fragile, a token-level SFT loss restricted to format-and-result-correct trajectories acts as an anchor that prevents the policy from drifting into unparseable outputs. This is a useful, transferable recipe for any multi-turn tool-use RL setup. Separately, Figure 2's 21.5-point drop from SFT warm-up is a counter-intuitive signal that SFT on tool-use trajectories can degrade grounding skill, and may argue for skipping SFT warm-up entirely in similar pipelines.

## Suggestions
- Rewrite the abstract and Section 5.1 framing to lead with the Figure 5 comparison: "iterative spotlight + RL beats both single-pass SOTA and training-free iterative inference," with the 47.6 → 52.8 numbers stated explicitly and the inference-compute trade-off acknowledged.
- Add the Stage-1-ablation experiment (RL from raw base, no SFT warm-up) and report whether 49.6%+ is reachable without the warm-up; this is the single most informative experiment the paper does not run.
- Rename or reframe the objective: rather than "modified GSPO," describe the contribution as "GSPO + behavior cloning on tool-filtered positives," and structure Section 3.2.2 around the J'(θ) ablation.
- Soften the UI-Vision and OSWorld-G claims to reflect the actual rankings (below UI-Venus-7B on UI-Vision; below GTA1-7B on OSWorld-G).
- Report tool-call depth statistics and an inference-compute number per query.

## Evaluation by Axis
- **Originality:** Moderate. Combining iterative tool-use with RL and filtered behavior cloning is incremental over GRPO/GSPO + tool-use work, but the J'(θ) stabilization observation is concrete and useful.
- **Importance of question:** Solid. High-resolution GUI grounding is a real bottleneck for GUI agents.
- **Are claims well supported:** Partially. ScreenSpot-Pro claim holds in absolute terms; the data-efficiency framing is misleading once the Figure 5 baseline is considered; UI-Vision and OSWorld-G claims are overstated relative to leaderboards in Tables 4 and 5.
- **Soundness of experiments:** Mixed. The negative-results catalogue and Figure 3 dynamics are well-executed; the missing Stage-1 ablation and absent inference-compute accounting weaken the case.
- **Clarity of writing:** Reasonable; the stage-labeling inconsistency in Figure 2 and the additive-vs-independent ambiguity in Section 4.1 hurt.
- **Value to research community:** Modest. The J'(θ) stabilization trick and the negative-results catalogue are the most reusable artifacts.

## Calibration

**Round 1 anchors retrieved:**
- `nE3flbe88p` (3.25, reject) — Minecraft multi-agent benchmark, not topically aligned.
- `gNoqEdT2wO` (2.33, reject) — multimodal continual learning, not aligned.
- `BVACdtrPsh` (3.00, reject) — text-rich visual benchmark, not aligned.
- `E2CR6hmV1I` (3.00, reject) — LLM multi-agent process rewards, partially related.
- `M9iky9Ruhx` (6.00, accept) — Grounding MLLM in GUI World; closest topical anchor; cleaner contribution than this paper's, no overclaiming.
- `nNyjIMKGCH` (5.75, reject) — Reinforced UI grounding with RL; topically very close, rejected despite mostly 6's.
- `QarKTT5brZ` (6.25, accept) — GUI-World dataset paper.
- `jY2ow7jRdZ` (5.25, reject) — SpiritSight GUI agent; close analog (cleaner system, rejected for backbone fairness).
- `kxnoqaisCT` (7.75, accept) — UGround; this is the universal grounding paper the submitted work cites and uses data from.
- `Q6a9W6kzv5` (8.00, accept), `7gUrYE50Rb` (8.00, accept), `HnhNRrLPwm` (8.00, accept) — not topically aligned.

**Round-1 bracket:** between ~4 and ~6. The paper sits in the "mixed-results GUI grounding" zone occupied by the rejected anchors (UI-Pro 4.25, SpiritSight 5.25, Reinforced UI Grounding 5.75, AutoGUI 5.0).

**Round 2 anchors retrieved:**
- `5wmAfwDBoi` (4.25, reject) — UI-Pro recipe paper; weakness: limited innovation, scope concerns. This paper has stronger methodological novelty but more overclaiming.
- `wl4c9jvcyY` (5.00, reject) — AutoGUI dataset; received polarized scores 6/8/3/3. Comparable polarization risk.
- `hHF5AayC7O` (4.75, reject) — web-agent demonstrations; only loosely related.
- `MPJ4SMnScw` (5.50, accept) — agentic re-alignment workflow, somewhat related conceptually.
- `gXyWbl71n1` (6.25, accept) — multi-turn composed image retrieval; tangential.
- `vbr1OKK19i` (4.75, reject), `lCqNxBGPp5` (5.00, reject), `zVagbJLgkP` (5.33, reject), `4FRUNLuY54` (5.33, reject) — VLM-perception/tool-use papers, multiple rejected.

**Narrowing:** The submitted paper sits clearly above UI-Pro (4.25) — it has more methodological novelty (J'(θ), tool-coordinated RL) — but below M9iky9Ruhx (6.00, accept), whose contribution is cleaner and not undermined by mixed cross-benchmark results. It is comparable to SpiritSight (5.25) and Reinforced UI Grounding (5.75): all three papers have a real contribution accompanied by overclaiming or fairness questions, and all three were rejected. The cross-benchmark inconsistency (loss on UI-Vision vs. UI-Venus, near-zero gain on OSWorld-G), the +5.2-only marginal gain over a training-free baseline that the paper doesn't foreground, and the misnamed "modified GSPO" contribution push this paper toward the SpiritSight/Reinforced-UI cluster rather than the M9iky9Ruhx accept anchor.

Final placement: 4.5 — between UI-Pro (4.25) and SpiritSight (5.25), reflecting genuine but overstated contribution and material concerns about how the headline is supported.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>