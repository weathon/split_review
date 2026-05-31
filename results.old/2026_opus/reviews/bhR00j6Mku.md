## Summary
The paper presents the first systematic study of benchmark contamination detection for Large Reasoning Models (LRMs) across two threat scenarios: (Stage I) SFT contamination on a base model followed by RL — where the authors show that brief GRPO training conceals contamination from a battery of 10 detection methods; and (Stage II) extensive SFT contamination with CoT applied directly to advanced LRMs — where detection drops to near-random. The paper accompanies the Stage I empirical finding with a theoretical decomposition of the NLL drift and a clipping-removal ablation that empirically isolates PPO-style importance sampling/clipping as the mechanism behind detection concealment.

## Strengths
- **Comprehensive controlled empirical study (Table 2, Table 5):** 10 detection methods × 6 reasoning benchmarks × 2 base models, with consistent AUROC drops after GRPO (e.g., Loss 75.48% → 61.26%; LiRA 89.13% → 74.89%) and near-random AUROC across all 10 detectors in Stage II. The breadth of detectors and benchmarks gives the headline claim solid coverage.
- **Clean causal isolation of the RL effect (Table 1, Table 2 rows comparing RL w/ Clean vs RL w/ Clean&Mem):** The paper rules out the most obvious alternative explanations — that RL is simply "forgetting" or that the concealment requires re-exposure to members during RL. Tab. 1 shows the contaminated model retains ~7.14% pass@1 inflation after GRPO, and Tab. 2 shows RL-on-clean degrades detection nearly as much as RL-on-member+clean.
- **Clipping ablation (Table 3) is the strongest piece of evidence:** Removing the clipping term in GRPO restores Loss-detector AUROC from 61.26% → 73.28%, and in RAFT++ from 57.58% → 74.39%, while plain RAFT (no clipping) already preserves separability (77.51%). This is a direct, mechanistic experiment that backs the theoretical attribution.
- **Theoretical decomposition (Theorem 3.1, Eq. 5) provides a structural account:** The covariance/mean decomposition gives a vocabulary for why three closely related algorithms (RAFT / RAFT++ / GRPO) behave differently, even where some of the within-decomposition sign arguments are empirically rather than rigorously established.
- **Log-prob density visualizations (Fig. 3 and Fig. 4):** Show the member/non-member separation collapsing visually (AUROC 0.698 → 0.605 on GPQA after GRPO; near-identical distributions after Stage II contamination), making the mechanism interpretable.

## Weaknesses

### Fatal
None.

### Major
- **Theorem 3.1 is a decomposition, not a prediction; the concealment claim relies on intuitive sign/variance assertions that are inserted into the derivation without proof.** For RAFT: "non-members correct trajectories can exhibit much higher variance in loss and probabilities, thus the β_N term is typically larger than β_M" (§3.2). For RAFT++: "the new term Cov(ℓ_k, Σ ρ_t m_t) is negative as correct path with higher loss are anomaly and typically got clipped more. Moreover, this is much more prominent in non-members". For RAFT specifically, the paper itself says "Empirically, the covariance gap offsets the mean gap, yielding Δ_N − Δ_M ≥ 0" — meaning RAFT's non-concealment is *empirical*, not a theoretical prediction. As framed in §3.2 ("theoretical analysis to demonstrate that PPO-style clipping and importance sampling are the root cause"), the math is doing less work than the prose claims; it accommodates the ablation rather than predicting it. The paper should either lift these variance/sign claims into named assumptions with empirical verification, or honestly reframe the section as a decomposition that interprets the ablation.

### Minor
- **No variance/uncertainty quantification on AUROC.** Several benchmarks are small (AIME24=30, AIME25=30, AMC23≈40), so with a 50/50 member/non-member split each cell in Tables 2, 3, 5 is computed on ~15–20 vs ~15–20. The standard error on AUROC at these sizes is comparable to many of the reported Δ values, especially per-benchmark cells. The aggregate (averaged) trends are likely robust (LiRA −14 averaged over six benchmarks is hard to attribute to noise), but the per-cell numbers are presented with more authority than the sample sizes support. Bootstrap CIs would distinguish the truly significant drops from those that are not.
- **The clipping ablation (Table 3) is run only on the Loss detector.** The theoretical claim is supposed to be general across detectors that rely on NLL separability, but the ablation only shows clipping-removal restoring AUROC for Loss. Reproducing the pattern for at least one reference-free (Min-K%, Max-K%) and one reference-based (LiRA) detector would substantially tighten the theory→experiment bridge.
- **The Stage II generalization-vs-memorization interpretation is asserted rather than tested.** §4 shows two things clearly — extensive CoT contamination inflates pass@1 and existing detectors fall to ~50% AUROC. The interpretation offered ("LRMs internalize the underlying knowledge and reasoning process … enabling generalization to distributionally similar questions") is supported only by Fig. 4 showing both member and non-member log-probs rising together. This is consistent with generalization but also with a simpler domain-shift explanation. No experiment is offered that would distinguish the two (e.g., training on benchmark A and measuring log-prob gain on an unrelated text distribution).
- **The "RL conceals contamination" framing partially blurs the threat model.** The paper's central control — RL on clean data degrades detection nearly as much as RL on member+clean (Tab. 2) — is the right experiment, but it changes what the finding actually means. Normal LRM post-training is now an unavoidable confound for any SFT-stage contamination detection, regardless of intent. Fig. 1 and the introduction frame RL as a deliberate concealment step; the real, broader implication is that pre-LRM detectors are essentially broken against any standard LRM pipeline. This is more a framing issue than a content gap, but it under-sells the scope of the problem.
- **"Extensive GRPO training would render all existing detection methods to near-random performance eventually" (after Fig. 2) is an extrapolation.** At 156 steps, LiRA in Tab. 2 still sits at 74.89% — degraded but well above random. The rhetoric overshoots what 156 steps of GRPO actually demonstrate; either the claim should be tightened or longer-trained runs should be shown.

### Trivial
None worth flagging.

## Nice-to-Haves
- Convert the asserted variance/sign claims in §3.2 into named assumptions or lemmas, and add a small empirical verification (e.g., directly measure Var(ℓ_k | r=1) for members vs non-members and confirm the assumed ordering).
- Extend the clipping-removal ablation in Table 3 to LiRA and Min-K%, not just Loss.
- For Stage II, run at least one experiment that pries apart generalization from generic domain shift — e.g., contaminate on benchmark A and measure log-prob gain on a held-out unrelated math benchmark, or vary the distributional similarity between training corpus and held-out set and look for a monotonic effect on log-prob gain.
- Add bootstrap confidence intervals on AUROC, particularly for AIME24/25 and AMC23, where per-cell sample sizes are smallest.
- Broaden the algorithm coverage beyond GRPO/RAFT/RAFT++ — including DPO or REINFORCE++ would strengthen the "broad class of RL methods" generalization claim.
- §3.1's choice to compute detection scores on 8 generated rollouts rather than the canonical benchmark response (deferred to Appendix E.2) interacts with the headline result; this protocol choice deserves explicit defense in the main text.

## Removed Points
These points are flagged to be removed, treat them with caution:

- *Harsh critic's note on §5 conclusion brevity*: This is presentation polishing rather than a substantive flaw; the paper does propose two concrete directions, and brevity here doesn't damage the contribution.
- *Strength Finder's general "addresses an important problem" framings*: removed under the strength-filtering rule — these are not specific to this paper's evidence.
- *Generic "more models / more benchmarks" requests beyond what was already kept under nice-to-haves*: the model and benchmark coverage in the paper (2 base models for Stage I, 4 LRMs for Stage II, 6 benchmarks, 10 detectors) is already adequate.

## Novel Insights
The paper's most insightful and field-relevant observation is that PPO-style importance-sampling-with-clipping mechanically degrades the NLL separability that essentially every existing log-prob-based contamination detector relies on — and that this effect happens *even when RL is performed on entirely clean data*. This reframes a class of attacks ("hide contamination by post-training") as something closer to an inadvertent property of modern LRM pipelines: the standard recipe for turning a base LLM into a reasoning model already destroys the statistical signal these detectors were designed to find. The Stage II observation — that an LRM contaminated with CoT data shifts log-probs upward uniformly across members and non-members — is a useful, if under-tested, complement, suggesting that the memorization-only assumption underlying most current detectors is the deeper problem.

## Suggestions
- Reframe §3.2: distinguish the algebraic decomposition (Theorem 3.1) from the substantive claim that clipping causes concealment, and either prove the variance/sign claims or label them as empirically-verified assumptions.
- Add bootstrap CIs to Tables 2, 3, 5 to disambiguate per-cell drops from noise.
- Reproduce Table 3's clipping ablation for at least 2 additional detectors covering reference-free and reference-based families.
- Add one Stage II experiment that distinguishes generalization from domain shift (cross-benchmark log-prob measurement).
- Soften the extrapolation about all detectors falling to random with more GRPO training, or run a longer-horizon experiment to substantiate it.
- In Fig. 1 and the introduction, lead with the broader implication: any standard LRM training pipeline (not just deliberate concealment) breaks SFT-stage contamination detectors.

## Axis Evaluation
- **Originality:** High — the systematic study of contamination detection in the LRM training regime (specifically the RL-stage concealment effect, with mechanistic attribution to clipping) is genuinely new.
- **Importance of research question:** High — leaderboard integrity for LRMs is a present, practically relevant problem, and the paper documents a previously-unanalyzed vulnerability.
- **Whether claims are well supported:** Mixed — the empirical core (Tab. 2, Tab. 3, Tab. 5) is well-supported; the theoretical framing slightly overshoots what the math delivers, and the Stage II interpretation rests on lighter evidence than its prominence in the discussion suggests.
- **Soundness of experiments:** Largely sound — clean controls (RL on clean vs RL on clean+member, further-SFT control), large detector zoo, multiple base models, clipping ablation. Missing: confidence intervals on small benchmarks; clipping ablation across more detectors.
- **Clarity:** Good. The two-stage threat structure is easy to follow, and Fig. 1 effectively frames the contribution.
- **Value to community:** Substantial — both as a wake-up call to detector developers (memorization-only methods are inadequate for LRMs) and as a concrete mechanistic finding (PPO-style clipping is a measurable driver of concealment).

## Calibration Trace

**Anchors retrieved:**
- Round 1:
  - `OdoS6cH8MP.md` — avg 2.00 — generic LM textual data valuation paper; not topically similar
  - `wwO8qS9tQl.md` — avg 3.00 — LM explainability benchmark; weakly related
  - `ly10tMV6cD.md` — avg 3.25 — structure-rich text benchmark; not similar
  - `RuY1r1PDdQ.md` — avg 3.00 — instruction following eval; weakly related
  - `Nk1MegaPuG.md` — avg 4.25 — *Evading Data Contamination Detection (read in full)* — closest weak anchor; shallower attack paper without theoretical mechanism; this paper is clearly stronger
  - `zWqr3MQuNs.md` — avg 6.25 — *Detecting Pretraining Data with Min-K% (read in full)* — directly relevant baseline method paper; this paper is in dialogue with it
  - `Nsms7NeU2x.md` — avg 6.75 — *How much can we Forget about Data Contamination (read in full)* — theory + empirical paper on contamination forgetting; comparable depth, this paper is more timely (LRM era) and has cleaner causal ablation
  - `rAylWUIKtu.md` — avg 4.25 — retro-holdout benchmark inflation; loosely related
  - `syThiTmWWm.md` — avg 7.75 — null-models cheating LLM benchmarks; conceptually similar (gaming benchmarks) but different domain
  - `jOmk0uS1hl.md` — avg 8.00 — *Training on the Test Task (read in full)* — strong anchor; cleaner conceptual paper with broader implications and stronger writing
  - `EUSkm2sVJ6.md` — avg 7.60 — dataset usage cardinality inference; related to membership inference theory
  - `SnDmPkOJ0T.md` — avg 8.00 — REEF model fingerprinting; tangential
- Round 2:
  - `SQnitDuow6.md` — avg 5.50 — VPO RLHF; not directly relevant
  - `86zAUE80pP.md` — avg 6.25 — CPPO continual RLHF; tangential
  - `vl8VpW2niQ.md` — avg 5.40 — memorization in ICL; tangential
  - `DpFeMH4l8Q.md` — avg 5.67 — group preference optimization; not relevant
  - `m2NVG4Htxs.md` — avg 6.75 — *To the Cutoff and Beyond (read in full)* — longitudinal contamination analysis; comparable depth, this paper's mechanism is more novel
  - `sKYHBTAxVa.md` — avg 7.33 — *LiveBench (read in full)* — benchmark construction paper, less directly comparable
  - `pljYMCYDWJ.md` — avg 6.20 — Logicbreaks rule-following theory; tangential
  - `8Rov0fjpOL.md` — avg 5.80 — unsafe information leakage; tangential
  - `dRel8fuUK4.md` — avg 6.00 — RMIA membership inference; technically relevant
  - `kmn0BhQk7p.md` — avg 7.20 — Beyond Memorization (privacy inference); tangential

**Round-1 bracket:** 5.5–7.5. Clearly stronger than Nk1MegaPuG (4.25, similar attack-on-detection setup but without the LRM-specific scope, mechanism, or clipping ablation), comparable in depth to Nsms7NeU2x (6.75) and m2NVG4Htxs (6.75), and below the conceptual clarity and broader impact of jOmk0uS1hl (8.00).

**Round 2 narrowing:** The two closest anchors are Nsms7NeU2x (6.75, Reject) and m2NVG4Htxs (6.75, Accept). The current paper has:
- A timely, previously-unstudied scope (LRMs specifically) that neither anchor covers.
- A clean, well-targeted ablation (clipping removal in Tab. 3) that gives mechanistic causal evidence comparable in cleanness to the natural-experiment design of m2NVG4Htxs.
- A partial theoretical decomposition that, while not as tightly proved as Nsms7NeU2x's forgetting bound, lines up neatly with the ablation.
- Real but not-fatal weaknesses (Stage II interpretation under-tested, ablation limited to one detector, no AUROC CIs).

Against the LiveBench / Training-on-Test-Task (~7.3–8.0) anchors, this paper is narrower in scope, has a more contested theoretical framing, and the Stage II contribution is shallower — so it should sit below them. Against the 4.25 anchor it is clearly stronger. Against the two 6.75 anchors it is comparable in depth and arguably more timely/mechanistic, but its theory falls short of its rhetoric in a way reviewers will reasonably ding.

**Final placement:** 6.5 — slightly above the 6.75 cluster anchors on novelty and mechanistic clarity, but pulled back from 7+ by the over-claimed theory, missing CIs, and under-tested Stage II story.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>