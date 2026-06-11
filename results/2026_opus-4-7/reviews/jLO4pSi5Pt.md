## Summary
The paper proposes L-TTA, the first test-time adaptation method targeting long-tailed test streams for Vision-Language Models. It introduces three co-designed mechanisms — Synergistic Prototypes (Deterministic + Exclusionary), Rebalancing Shortcuts trained with a Class Re-Allocation loss, and Balanced Entropy Minimization — and evaluates across 15 datasets, three imbalance ratios, and four additional VLM backbones.

## Strengths
- Well-motivated problem framing with concrete VLM-specific failure modes diagnosed in Figure 1 (Text-induced Tail Erosion; Modality-bias Amplification), distinguishing the setting from generic LT+TTA mixtures.
- The EP update rule (Eq. 5) weighting every class by φ_c is a sensible answer to the "tail prototypes are starved" problem; Table 6 confirms DPs and EPs are non-redundant (removing either costs ~3–4% Macro-F1).
- Broad empirical evidence: L-TTA beats all 11 VLM-TTA baselines on OOD-Avg, CDB, and CB across imb ∈ {10, 20, 50}; Macro-F1 gains often exceed Acc gains (+2.20 vs +1.02 on CDB; +2.64 vs +2.87 on CB), directly supporting the rebalancing claim.
- Practical efficiency (1.45h / 1.89G on A100), substantially cheaper than RLCF/WATT/SCAP while topping the HM metric on LT-CDB and LT-CB.
- Robustness across ε in Table 7 and consistent gains across four additional backbones (ViT-L/14, ViT-H/14, SigLIP-L/16, MetaCLIP-BigG) in Table 5.

## Weaknesses

### Fatal
None.

### Major
- **Missing LT/non-i.i.d. TTA baselines in main tables.** Section 2.1 discusses DELTA, LAME, and SAR explicitly, but none appear as competitors in Tables 1–3. SAR appears only as a strawman in Figure 1(b.2). Without these methods evaluated on the same CLIP backbone, the claim that gains stem from the *long-tailed* design (rather than the prototype/cache architecture L-TTA shares with TDA/DPE) is not isolated.
- **Circular class-prior estimation in BEM.** Eq. 9 needs π, which the paper says is "continually updated based on the current predicted pseudo-labels." Under a head-biased streaming model the estimate is contaminated by the very bias BEM aims to correct. The paper offers no oracle-prior comparison, no warm-up procedure, and no analysis of estimation error; Proposition 2 implicitly assumes π is correct.

### Minor
- **Propositions are weaker than their framing suggests.** Proposition 1 restates the well-known head-class bias of EM. Proposition 2 only states that the signed head-tail gradient gap shrinks; it does not bound the reduction, characterize fixed points, or guarantee correct gradient direction. The phrasing "both intuitively and theoretically interpretable" overstates Eq. 10.
- **BEM's empirical contribution is small relative to its theoretical emphasis.** Table 6: SyP+RS → +BEM adds only +0.36 Acc / +0.66 Macro on ViT-B/16, despite being the most theoretically advertised piece. Worth acknowledging in the writing.
- **Ambiguous hyperparameter K.** §4 states "K = 0.3"; the ablation reports "K = 0.2 yields the best performance" over the range 0.1–1; Eq. 6 treats K as an integer count of hyper-class vectors. K appears to actually be a ratio, but this is never stated.
- **The η=0 ablation does not isolate RS.** In Figure 4(b), η=0 disables L_CRA but the RS attention module is still present with random hyper-class vectors — measuring "RS without CRA" vs. "RS with CRA," not "no RS" vs. "RS."
- **Stream length under varying imbalance is unspecified.** Exponential subsampling at imb = 50 may yield a shorter stream than imb = 10; performance differences could partly be a sample-size effect rather than imbalance per se.

### Trivial
- HM (harmonic mean of Acc and Macro) is the headline column in Table 4 but is defined only in the caption.
- "5 runs" are reported but standard deviations are not shown in the main tables; given ~1.5% gains on OOD-Avg, error bars would help.

## Nice-to-Haves
- Re-run main tables with DELTA / SAR / LAME (and a logit-adjustment-on-running-prior baseline) on identical CLIP backbones.
- Oracle-prior upper bound for BEM; sensitivity analysis to prior-estimation error.
- Tighten Proposition 2 into a bound dependent on the prior-estimation error.
- Surface head/tail accuracy in the main tables rather than the appendix.
- Provide a clean "no RS" ablation distinct from the "RS with η=0" condition.

## Removed Points
These points are flagged as removed; treat them with caution.
- **CRA loss "has trivial zero-activation minima"** (harsh critic). The MoE Load Balancing Loss it is modeled on shares the same dot-product structure; softmax-normalized attention precludes the trivial-zero solution. The critic himself flagged this as a possible parser artifact; not a verified flaw.
- **Generic novelty claim "first to study long-tailed TTA for VLMs"** as a standalone strength — kept only because it is tied to specific failure-mode evidence in Figure 1; otherwise generic.

## Novel Insights
None beyond the paper's own contributions. The EP-via-weighted-update-of-all-classes and the (1−P̃)^β-weighted log-prior in BEM are the paper's design ideas; no additional insight emerges from the reviews.

## Suggestions
- Include DELTA / SAR / LAME on the same CLIP backbone in the main tables.
- Add an oracle-prior comparison and prior-estimation-error sensitivity for BEM.
- Clarify K's units; rerun with a single, consistent setting between Implementation Details and ablations.
- Add a true "no RS" ablation row.
- Report std devs in main tables; clarify whether stream length is held constant across imb.

## Calibration Anchors

Round 1 (bracketing):
- pdzHpQbGrn (avg 2.5, Reject) — TTA active prompt learning for VLMs; much narrower contribution than L-TTA.
- ZaudLwn0Hm (avg 2.5, Reject) — few-shot VLM adaptation; weaker than L-TTA.
- HfJxXbXlYJ (avg 3.0, Reject) — LLM2CLIP; off-topic.
- JIlIYIHMuv (avg 2.5, Reject) — LVLM continual learning; off-topic.
- b20VK2GnSs (avg 7.0, Accept) — MLLM concept drift under long-tail + OOD; closely related and stronger.
- BUDxvMRkc4 (avg 4.67, Reject) — Balanced language guidance for long-tail CLIP (training-time, not TTA).
- kIP0duasBb (avg 6.67, Accept) — CLIP-Reward TTA; comparable scope, accepted.
- yD2JMeKumt (avg 6.0, Reject) — DOTA distributional TTA for VLMs; very close in scope and contribution scale.
- WyEdX2R4er, TPZRq4FALB, uAFHCZRmXk, 3i13Gev2hV (all avg 8.0) — broader-impact or analysis papers, stronger.

Round-1 bracket: between 5.5 and 7.

Round 2 (narrowing):
- eXrUdcxfCw (avg 4.8, Reject) — Continual TTA with source + EMA target prototypes; similar prototype mechanism but narrower setting and weaker writeup than L-TTA.
- 75PhjtbBdr (avg 6.25, Accept) — Multi-label TTA with Bound Entropy Minimization; comparable in technical depth and similar in spirit (variant of EM).
- fRpAUgKJhT (avg 5.75, Reject) — Class-aware prompt reweighting for VLMs; narrower scope.
- jzzEHTBFOT (avg 6.0, Accept) — C-TPT calibrated TTA prompt tuning; comparable maturity.

Comparison: L-TTA is broader empirically than DOTA (yD2JMeKumt, 6.0) and 75PhjtbBdr (6.25, accepted), has stronger problem framing than BUDxvMRkc4 (4.67), but shares DOTA's borderline-acceptance issues (missing critical baselines, theory weaker than framing). I place L-TTA slightly above DOTA but below b20VK2GnSs (7.0). Final score: 6.0.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>