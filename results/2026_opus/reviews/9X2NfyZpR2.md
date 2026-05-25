Now I have enough calibration. Let me write the final review.

## Summary
The paper introduces TbLTA, the first weakly-supervised framework for dense Long-Term Action Anticipation (LTA), trained using only video transcripts (ordered action lists without timing/duration). The architecture combines a transcript-conditioned temporal alignment module (ATBA), a cross-modal attention layer with transcript-derived local masks, CTC and CRF losses, and a duration head supervised by momentum-based class-wise priors. On Breakfast the deterministic model is competitive with fully supervised baselines (29.03 vs ActFusion 28.45 avg); on 50Salads and EGTEA there are still substantial gaps under deterministic comparison.

## Strengths
- **Novel and well-motivated problem setting.** TbLTA is the first dense-LTA model trained from transcripts alone, eliminating frame-level boundary annotations. Prior weakly-supervised work for LTA (Zhang et al., 2021) still relies on temporally localized labels, so this is a genuine extension of the supervision spectrum.
- **Competitive deterministic Breakfast result.** Under a like-for-like deterministic protocol the model matches ActFusion on Breakfast (29.03 vs 28.45 avg in Table 1) and beats all supervised baselines at Obs 30% across all prediction horizons (e.g., 40.28 vs 35.79 at β=10%). This is the strongest piece of evidence in the paper.
- **Component-level ablations isolate contributions.** Table 4 shows each module — cross-modal attention (≈5.7 pts on Breakfast), CRF (≈4.1 pts at long horizons), duration loss (≈3.3 pts on Breakfast), CTC (≈0.6–0.8 pts) — yields measurable gain. The cross-modal design is further contrasted with a "simplex" variant, isolating the value of the transcript-derived local mask and gated residual fusion.
- **Rare-class result on EGTEA is informative.** TbLTA reaches 60.11 mAP on Rare verbs vs Anticipatr 55.10 (Table 2), suggesting that transcript supervision can transfer useful priors to under-represented classes, although this comes with a substantially lower All score.

## Weaknesses

### Fatal
None. The contribution is real and at least one comparable deterministic result supports the headline claim.

### Major
- **Headline framing leans on an oracle-style metric.** In Table 1 the most visually salient numbers are "Ours* — Top1" (Breakfast 37.15 avg, 50Salads 28.51 avg), and the §4.2 narrative ("TbLTA achieves substantially higher accuracy by capturing multiple plausible futures") invites direct comparison to deterministic supervised baselines like ActFusion. Top-1 over K sampled futures is best-of-K, which is not comparable to single-shot deterministic predictions. The deterministic-only comparison is more honest and more mixed: competitive on Breakfast, a ~7-point gap on 50Salads (20.92 vs 28.39), and an ~11-point All gap on EGTEA (65.37 vs 76.80). The text should foreground the deterministic story.
- **Cross-modal attention's inference-time behavior is not specified.** Eqs. (1)–(2) and the surrounding text build the local mask M from pseudo-labels Ŷ that are themselves produced by aligning to the transcript Y; §3 states only [E ∥ X_obs] is available at inference. The paper never explains what M is at test time (is the cross-attention module dropped? populated from the TAS head's predicted labels? from class tokens only?). Since this module is the single largest ablation gain on Breakfast (≈5.7 pts), the gap between training-time and inference-time mechanics directly affects how to interpret the headline number. This is the clearest missing piece in §3.1 and §4.
- **Anticipation decoder description is internally inconsistent.** §3.1 describes the decoder as a "transformer-based parallel decoder … fixed set of queries Q ∈ ℝ^{C_LTA × d_LTA} attends to F̃" and simultaneously as "terminating when an ⟨EOS⟩ token is generated, treating anticipation as structured prediction." Parallel query-based decoding with fixed cardinality and autoregressive EOS termination are different generation regimes; the paper conflates them, which also affects how Eq. (5)–(6) (linear-chain CRF over T_pred positions) is interpreted.

### Minor
- **"Mitigates data imbalance" on EGTEA is overstated.** Rare 60.11 vs 55.10 is real, but Freq 73.46 vs 83.30 and All 65.37 vs 76.80 are large drops. The broader claim ("high-level semantic supervision … can mitigate data imbalance") is supported only by the Rare cell, with no variance reported.
- **Self-supervised duration head risks self-reinforcement.** The momentum buffer d̂ stores per-class frequencies of the segmentation head's *own* predictions, and is then used to supervise the duration regression head (Eq. 7). The asymmetric ablation impact (0.2 pts on 50Salads vs 3.3 pts on Breakfast) is not explained, and the risk of collapse on noisier datasets is not discussed.
- **Encoder description cites "pyramid hierarchical local attention" with only a Vaswani reference.** Vanilla Transformer does not have this construction. Either a specific borrowed module should be cited or the description should be tightened — this affects reproducibility for the encoder.
- **Ablations only report Top-1 MoC.** Since Top-1 is the oracle-friendly stochastic metric, ablations are run on the most favorable scoring; whether each component also lifts the deterministic prediction (the protocol that matters for fair comparison) is not shown.
- **No analysis of why TbLTA beats supervised baselines specifically at Obs 30% but not Obs 20% on Breakfast.** This is the paper's most striking deterministic result; without seed variance or analysis the reader cannot tell whether it is a property of transcript supervision or a noisy split-level fluctuation.

### Trivial
- Eq. (6) writes the CRF partition function as a brute-force sum over C^{T_pred}, while in practice forward-backward is used. Standard but worth noting.
- The discussion in §4.1 narrows EGTEA evaluation to verbs (19 classes) rather than 106 verb-noun classes; this is consistent with comparators but should be flagged when the EGTEA result is introduced rather than only in the metrics paragraph.

## Nice-to-Haves
- A two-stage baseline: feed pseudo-labels from a strong off-the-shelf weakly-supervised TAS model into FUTR/ActFusion, and compare against TbLTA. This is the most informative missing experiment: it would localize whether TbLTA's gain comes from joint design or simply from transcripts containing strong symbolic signal.
- Seed variance / per-split numbers on the four Breakfast splits, especially around the Obs 30% column.
- A rough quantification of the annotation-cost difference between transcript-only and frame-level supervision, to substantiate the cost-savings motivation in the abstract.
- Restructure the central claim around the deterministic Breakfast comparison and treat Top-1 stochastic numbers as a separate evaluation regime.

## Removed Points
These points are flagged to be removed; treat them with caution.

- *Harsh critic: "Transcripts leak the future action symbol sequence, so 'weak supervision' overstates the framing."* — Within the TAS/LTA literature, transcript-only supervision is the standard "weak" regime; the paper is consistent with this convention and explicitly defines what is and isn't given. The framing is conventional, not misleading. Demoted from a "methodological gap" to a remark.
- *Harsh critic: "Two identical blocks both labeled Table 4 in the parsed output."* — This is a parser artifact; one of the blocks is the intended Table 3.
- *Strength Finder: "Stochastic variant achieves high accuracy demonstrates flexibility in modeling multiple plausible futures."* — Conflicts with the verified weakness about Top-1 being an oracle metric; weakness wins.
- *Strength Finder: "Cross-modal attention design with local masking and gated residual fusion yields substantial gains" (full claim).* — Kept in spirit, but tempered: the gain is real in ablations, however the inference-time mechanism for this module is not specified, so the magnitude is partially confounded.

## Novel Insights
None beyond the paper's own contributions. The work is novel as a setting (first transcript-only dense LTA) but does not surface broader insights that go beyond reporting that transcripts alone can drive competitive dense anticipation on at least one benchmark.

## Suggestions
- In §3.1 and Fig. 2, explicitly describe the inference-time behavior of the cross-modal attention module: what populates the mask M when no transcript is available, and whether the cross-attention path is active at test time.
- Resolve the parallel-decoder vs autoregressive-EOS contradiction in the decoder description; if generation is fully parallel, drop the EOS language; if autoregressive, rewrite Eq. (5)–(6) accordingly.
- Reposition Table 1 so the deterministic row is the headline comparison; clearly mark Top-1 stochastic numbers as best-of-K and avoid juxtaposing them with deterministic supervised baselines in the narrative.
- Add a two-stage pseudo-label baseline (WS-TAS → supervised LTA on those pseudo-labels) to localize where TbLTA's gains come from.
- Report seed variance on Breakfast splits, especially for the Obs 30% column where the deterministic claim is strongest.
- Run at least the cross-attention and CRF ablations on the deterministic prediction in addition to Top-1 MoC.

## Evaluation along required axes
- **Originality.** Genuinely novel supervision regime for dense LTA; the strongest aspect of the paper.
- **Importance of research question.** Reducing annotation cost for LTA is a meaningful objective and transcripts are a natural compromise; well-motivated.
- **Whether the claims are well-supported.** Mixed. The deterministic Breakfast claim is supported. The stronger comparative claims rely on a Top-1 metric that is not directly comparable to supervised baselines. The 50Salads and EGTEA gaps are acknowledged but not engaged with.
- **Soundness of experiments.** Standard benchmarks, standard protocols, ablations isolate components — but the cross-modal attention inference path is unspecified and ablations are reported only on the favorable metric.
- **Clarity of writing.** Reasonable overall, with two specific issues: the decoder description is internally inconsistent, and the cross-modal attention's training/inference asymmetry is not made explicit.
- **Value to the community.** Establishes a new weakly-supervised baseline; useful if framing and clarifications are improved.

## Score and Decision

### Anchor retrieval
**Round 1 (bracketing):**
- `2HdZPEQUig.md` — Efficient Object-Centric Learning for Videos — avg 3.00, Round 1 low band — unrelated topic but anchors the rejection range; clearly weaker than the paper under review.
- `YGWxpOI6Y0.md` — VideoGPT+ — avg 3.40, Round 1 low band — video understanding, weaker than this paper which has a clearer novel contribution.
- `MSxCBXD5C8.md` — Anomalous Action Recognition — avg 3.00, Round 1 low band — unrelated; weaker.
- `ujNe7sybJu.md` — Video Summarization via LLMs — avg 2.50, Round 1 low band — unrelated; weaker.
- `Bb21JPnhhr.md` — AntGPT (LTA with LLMs) — avg 6.25, Round 1 mid band — *read in full*; very close topic (LTA), achieves SOTA on three datasets; stronger empirical claim than this paper.
- `dl34rOnbqJ.md` — Actions-to-Action — avg 4.40, Round 1 mid band — egocentric action anticipation, weaker empirical work than this paper.
- `f3CdjpPkSq.md` — Action Sequence Augmentation — avg 6.50, Round 1 mid band — action anticipation, strong evaluation.
- `HEXtydywnE.md` — LASER (neuro-symbolic weak supervision) — avg 6.00, Round 1 mid band — weakly-supervised video; comparable cleanliness.
- `9Cu8MRmhq2.md`, `LbEWwJOufy.md`, `weM4YBicIP.md`, `QQBPWtvtcn.md` — Round 1 high band — all are on different topics (long-term video alignment, gesture video, audio-driven portrait, view synthesis) but all are markedly more polished and complete than the paper under review.

Round-1 bracket: between ~4.5 and ~6.5.

**Round 2 (narrowing):**
- `dl34rOnbqJ.md` — Actions-to-Action — avg 4.40 (reject) — narrower; less novelty than the paper under review.
- `Bb21JPnhhr.md` — AntGPT — avg 6.25 (accept) — *read in full*; cleaner story and SOTA results; stronger than this paper.
- `GQgPj1H4pO.md` — Weakly Supervised VidSGG via Natural Language — avg 6.00 (accept) — *read in full*; very direct parallel ("first weakly-supervised X via natural language"), well executed; this paper has comparable novelty but more presentation issues (Top-1 framing, cross-attention inference ambiguity, decoder description inconsistency).
- `HEXtydywnE.md` — LASER — avg 6.00 (accept) — weakly-supervised video with language; cleaner than this paper.
- `sEARCNzhrP.md` — Interaction-based TAS — avg 5.00 (reject) — TAS-side, comparable depth.
- `IryGDUHxDE.md` — Unsupervised open-vocabulary action — avg 5.25 (reject).
- `HCoSsULNxG.md` — Weakly Supervised Skilled Activity — avg 4.75 (reject).

**Comparison.** The paper sits below the 6.0 accept cluster (VSNLS, LASER, AntGPT) because (a) the cross-modal attention inference path is unspecified for the module that carries the largest ablation gain; (b) the central comparative narrative relies on an oracle Top-1 protocol; (c) deterministic gaps on 50Salads and EGTEA-All are acknowledged but not engaged. It sits above the ~4.4–5.0 reject cluster (Actions-to-Action, Interaction-TAS) because the problem setting is genuinely novel and at least one benchmark (Breakfast) yields a clean, comparable, competitive deterministic result. Settling around 5.0 — borderline reject; the contribution is real but the presentation and unspecified inference path stand in the way of a publishable result in the current form.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>