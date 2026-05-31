Now let me do calibration retrieval.Round 1 bracket: 4.0 - 6.5. Let me narrow.Now I have enough calibration. Let me write the final review.

## Summary
TrojanTO proposes the first post-training, action-level backdoor attack against trajectory optimization (TO) models such as DT, GDT, and DC. The method combines MI-FGSM trigger optimization, length-based trajectory filtering, partial batch poisoning, and IMC-style bi-level alternating training, and is evaluated on six D4RL tasks with a 0.3% poisoning rate. Empirically, TrojanTO outperforms Baffle and IMC baselines (CP 0.701 vs. 0.342 and 0.551).

## Strengths
- **Underexplored threat model with practical motivation** (Section 3.3): the paper carefully distinguishes pre-/during-/post-training attacks and positions itself in the post-training, no-training-data regime — a regime not addressed by Baffle or earlier offline-RL backdoor work.
- **Strong empirical investigation of factors** (Sections 4.1–4.3, Tables 1–3, Fig. 1): the systematic study of target-action sensitivity (boundary vs. interior actions in Table 1), trigger-dimension sensitivity (Table 2), and the irrelevance of reward manipulation (Fig. 1) is a genuinely useful contribution independent of the attack itself.
- **Component ablations support the methodological claims** (Table 5): removing TF, BP, or AT each measurably degrades ASR/BTP/CP, providing direct evidence that all three modules contribute.
- **Headline empirical superiority with a low poisoning budget** (Table 4): TrojanTO reaches average CP 0.701 across 3 architectures × 6 tasks with only 0.3% poisoning, vs. Baffle's 0.342 at 10% — a 30× reduction in poisoning rate.
- **Realistic robustness and persistence checks** (Tables 6, 7): the attack degrades gracefully under multiplicative trigger noise and maintains effect over multiple consecutive steps within the context window.

## Weaknesses

### Fatal
None.

### Major
- **Trigger dimensions (1,2,3) are selected from a per-task search on Half/Walk and then applied universally** (Section 4.2, Table 2). ASR varies from 0.915 down to 0.000 across dimension triplets, and the paper "fix[es] the trigger dimensions to (1, 2, 3)" for all subsequent tasks (Hopp, Ant, Kit, Pen) on which the selection was not validated. Under the stated threat model (no training-data access, Section 3.3), the adversary cannot in general locate such dimensions. The main-table benchmark numbers are therefore conditioned on a search the threat model does not naturally afford. The paper notes that "Additional attempts at dimension selection methods are detailed in Appendix F," which partially addresses the concern, but in the main text this remains the most consequential evaluation choice and is not justified.
- **Including the boundary target action '1' in the averaged "diverse target action" results** (Section 4.1 vs. Table 4). Section 4.1's analysis (Table 1) shows that '1' yields ≈1.0 ASR almost regardless of method — this is *the* inflation pattern the paper criticizes prior work for. Averaging '1', 'fixed random', and 'arithmetic' in Table 4 therefore partly benefits from the same evaluation choice the paper argues against. Reporting boundary vs. non-boundary target types separately would let the strong claims rest on the harder cases.

### Minor
- **ASR threshold ε is defined symbolically in Eq. 2 but no specific value is given in the main text.** Because ε directly governs whether a per-episode trial counts as successful, a single ε value should appear with the main results, ideally with sensitivity to multiple ε. The single-step success criterion (one triggered step per episode) also makes the metric closer to "the trigger sometimes pushes the action close once" than to "the trigger reliably forces the target action."
- **Loss notation drifts between Eq. 1, the unnumbered "L = L_p + λ L_c" at the end of Section 5.2, and Eq. 7's "λ L_p + (1−λ) L_c."** In Eq. 1 λ scales the clean-imitation term; in Section 5.2 λ still scales L_c; in Eq. 7 λ scales L_p instead and (1−λ) scales L_c. This is plausibly notation drift rather than a conceptual contradiction, but it impedes reproducibility and clarity of the formal objective.
- **Baseline scope mismatch** (Section 6.1, Table 4). Baffle is a policy-level attack (acknowledged in Section 2), so beating it on action-level metrics is mechanical rather than informative. IMC's adaptation from image inputs to the sequence-modeling setting is not documented in detail, which is consistent with some very low IMC numbers (e.g., CP 0.013 on Hopp-DT). Leading with "absolute capability under the stated threat model" rather than ratios over these baselines would better match what the experiments actually demonstrate.
- **Section 4.3 wording overstates the negative result.** Fig. 1 shows that all reward-manipulation variants converge to similar curves, including the no-RM case. The accurate claim is "reward manipulation is *unnecessary* given the rest of the method," not "reward manipulation is *ineffective*." The latter framing is slightly stronger than the evidence.
- **Trajectory-filtering assumption "longer = better"** (Section 5.1) is plausible for locomotion tasks with early-termination dynamics but less obvious for fixed-length tasks like Kitchen/Pen. No per-task check on this assumption appears in the main text.
- **Persistence interpretation** (Section 6.3, Table 6). Since the perturbed state remains inside the model's context window for k subsequent steps, some of the "persistence" effect can be attributed to the sliding window rather than to a robust trigger-action coupling. A control where the trigger is shown once and removed from the subsequent context window would isolate the model contribution; the current section reads slightly stronger than what the design measures.

### Trivial
None retained.

## Nice-to-Haves
- Separate boundary vs. non-boundary target-action results everywhere (Table 4 in particular), and lead with the non-boundary case as the headline.
- Either justify the (1,2,3) trigger-dimension choice with a defensible adversary procedure (e.g., a small-budget search executable under the stated threat model) or analyze why low-index MuJoCo state dimensions are inherently easier to backdoor (attention/gradient analysis on the pretrained TO model).
- Report ASR at multiple ε in the main text and clarify the value used in Table 4.
- Briefly try input-space anomaly detectors targeted at low-dimensional state anomalies (a natural defense given that the trigger lives on three coordinates), in addition to the defenses summarized in Section 6.5.
- Reconcile the λ formulation across Eq. 1, Section 5.2, and Eq. 7 with a single canonical statement.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **"All experiments are on D4RL with comparatively small TO models, while the introduction over-promises scale"** — this is a framing critique, not a verifiable methodological flaw, and demoted.
- **"Baffle is not the right baseline / IMC adaptation is not tuned"** as a fatal-tier objection — kept in *Minor* in a softer form. The paper itself acknowledges Baffle's policy-level nature (Section 2); the asymmetry mostly favors arguing more carefully about scope, not invalidating numbers.
- **"Cited references / models / benchmarks must be independently verifiable"** — by hard rule, removed.
- **Generic strength: "addresses an important problem"** — removed for being non-specific.
- **Strength about defense evaluation being conclusive** — the defenses are summarized in one paragraph (Section 6.5) with full results in the appendix; the strength is real but cannot be tier-1 evidence based on what is in the main text.
- **Speculative-fatal framing of trigger-dimension cherry-picking** ("conditioned on a trigger location the threat model does not naturally provide… the rest of the argument depends on what is in Appendix F") — kept as Major, but not promoted to Fatal because Appendix F is referenced and the issue may be addressed there.

## Novel Insights
None beyond the paper's own contributions. The genuine insights — that boundary target actions inflate ASR almost regardless of method, that reward manipulation is unnecessary for backdooring TO models, and that trigger dimension placement dominates trigger-value design in continuous state spaces — are all the paper's own findings in Section 4.

## Suggestions
- Make the (1,2,3) decision either auditable (with a search procedure executable under the stated threat model) or principled (with a per-task gradient/attention analysis); without one of these, headline ASR conditioned on this choice will continue to read as cherry-picked.
- Drop '1' from the headline averages in Table 4 and report it as a separate column. Doing so would sharpen — not weaken — the core empirical message, because TrojanTO already wins on non-boundary targets.
- Add a single sentence in Section 3.4 giving the ε value used to compute ASR throughout the main results, and a short table at a few ε values.
- Add a "context-removed" control to Section 6.3 to isolate true model persistence from sliding-window persistence.
- Rewrite Section 4.3's conclusion as "reward manipulation is unnecessary" rather than "ineffective" to match Fig. 1.
- Unify λ notation across Eqs. 1, the inline expression before §5.3, and Eq. 7.

## Evaluation summary
- **Originality**: Moderate-positional. Each method component is borrowed (MI-FGSM, IMC, length-filtering, partial poisoning), but the assembly addresses a real gap — post-training, action-level backdoor on continuous-action sequence models.
- **Importance**: Real but not central. The threat surface is genuine; the paper is the first systematic empirical look at it.
- **Claim support**: Mixed. The qualitative claim "TO models are vulnerable to action-level backdoors under low budgets" is well-supported. The quantitative headline numbers in Table 4 are inflated by including boundary targets and by trigger-dimension search on a subset of tasks.
- **Soundness of experiments**: Reasonable scale (3 architectures × 6 tasks × 3 target types × 3 seeds), comprehensive ablations, robustness and persistence analyses. Main concerns are the dimension-selection methodology and ASR threshold transparency.
- **Clarity**: Mostly clear; loss notation drifts and ε remains unspecified in the main text.
- **Value**: Useful as a feasibility demonstration and a careful empirical mapping of which factors matter for TO-model backdoors. Less useful as a calibrated vulnerability quantification, given the evaluation choices above.

## Score and Decision

**Calibration anchors retrieved:**

Round 1:
- `S5JCqTJyKj.md` — Deferred Backdoor Functionality Attacks (avg 3.0, reject). Weak anchor; broader and less rigorous than this paper. TrojanTO is clearly stronger.
- `INzc851YaM.md` — Multi-objective offline RL (avg 3.0, reject). Off-topic but a weak-band anchor; TrojanTO is clearly above this.
- `324fOKW1wO.md` — Sample-efficient Imitative Decision Transformer (avg 3.33, reject). Weak; TrojanTO is above this.
- `RfYD6v829Y.md` — TrojanRAG (avg 3.40, reject). Comparable topical scope (backdoor + downstream behaviors); the reviewers found it incremental. TrojanTO has more comprehensive empirical evaluation.
- `em0gAL8fbK.md` — Temporal-Logic Backdoor on offline RL/AD (avg 4.0, reject). Closest topical anchor I read in full. TrojanTO is more comprehensive in tasks, models, and ablations; clearly above this.
- `ZtOnddFVT3.md` — Self-Alignment for Offline Safe RL (avg 4.67, reject). Less topically related but middle-band.
- `phAlw3JPms.md` — Robust offline RL via sequence modeling (avg 6.5, accept). Sequence-modeling robustness; cleaner contribution than TrojanTO and clearly above.
- `UhW2wA1pRV.md` — Robust DRL against behavior manipulation (avg 5.5, reject). Comparable in empirical strength but adds theoretical analysis; TrojanTO lacks theory but covers more architectures.
- `6Mxhg9PtDE.md`, `9pW2J49flQ.md`, `4KqkizXgXU.md`, `Bo62NeU6VF.md` — strong anchors (8.0–9.5). All off-topic LLM safety / LTL papers; TrojanTO is clearly below this band.

Round-1 bracket: **between 4.0 and 6.0**, with 5.5 anchors being the most informative comparable.

Round 2 (within bracket):
- `ZyPRwskBli.md` — Backdoor in Seconds via Model Editing (avg 4.75, reject). Read in full. Similar threat model (post-training, data-free) but applied to pre-trained vision/diffusion models. Reviewers found it useful but incremental; concerns about baseline choice and generality. TrojanTO is comparable in scope but on a more underexplored target (TO models in RL), with broader empirical sweep.
- `Gf4KZIqLHD.md` — DIFF2 backdoor on diffusion (avg 5.5, reject). Different domain.
- `UhW2wA1pRV.md` (re-encountered) — 5.5, reject.
- `vRyp2dhEQp.md` — Efficient Backdoor Attacks under data-constrained scenarios (avg 5.75, accept). Empirical with realistic threat model; the closest topical accept anchor.
- `HZnnHDrBXD.md` — Tree-based Action-Manipulation on continuous RL (avg 5.75, reject). Read in full. Theoretical attack with bounded cost on continuous-action RL — comparable scope, more theory but less empirical breadth than TrojanTO.
- `YLJs4mKJCF.md` — Poisoning Fair Representations (avg 6.0, accept). Off-topic.
- `MsRdq0ePTR.md`, `V7PYbRzD0h.md`, `kMT8ujhYbA.md`, `V4y0CpX4hK.md` — LLM/agent security benchmarks, not directly comparable.

**Comparative placement**: TrojanTO sits in the same band as `UhW2wA1pRV` (5.5, reject), `ZyPRwskBli` (4.75, reject), and `HZnnHDrBXD` (5.75, reject). It is stronger than `em0gAL8fbK` (4.0). It is weaker than `vRyp2dhEQp` (5.75, accept) and `phAlw3JPms` (6.5, accept), both of which have either a cleaner methodological story or a more cleanly bounded contribution. The two Major weaknesses (trigger-dimension cherry-picking from main-text perspective, '1' inclusion in averages) pull it slightly below the cluster of 5.5-rated rejects in terms of headline-number credibility, but the empirical investigation in Section 4 and the breadth of architectures/tasks pull it back up to about that band.

**Final score**: 5.0 — solidly in the middle band, comparable to the rejected anchors at 5.5 (`UhW2wA1pRV`, `HZnnHDrBXD`) but pulled down slightly by the two Major evaluation-design concerns that affect the headline numbers. Not at the accept-band level of `vRyp2dhEQp` (5.75 accept) or `phAlw3JPms` (6.5 accept) because the central empirical claim is not as cleanly supported.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>