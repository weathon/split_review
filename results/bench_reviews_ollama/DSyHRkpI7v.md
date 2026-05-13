## Summary
The paper introduces Sub-optimal Data Pre-training (SDP), a method for human-in-the-loop RL that pseudo-labels reward-free sub-optimal transitions with reward 0, uses them to pre-train the reward model, and seeds the agent's replay buffer with the same data. SDP is evaluated as a plug-in to R-PEBBLE, PEBBLE, RUNE, and SURF across 9 DMControl/Meta-world tasks under low feedback budgets, and is reported to never hurt performance and to significantly improve learning in many conditions.

## Strengths
- **Breadth of evaluation for an HitL RL paper**: SDP is combined with one scalar method (R-PEBBLE) and three preference methods (PEBBLE, RUNE, SURF) across 9 tasks from DMControl and Meta-world (Sec. 5.2, Fig. 2), which is above-average coverage for this subfield.
- **Simple, plug-in design**: Algorithm 1 is short and architecturally agnostic — it adds two phases (reward-model pre-train and replay-buffer seeding) on top of any reward-learning HitL pipeline. This makes the method easy to adopt and to ablate cleanly.
- **Well-chosen ablation suite**: The component ablations (pre-train only vs. agent-update only vs. full SDP), the zero-weight-init control (Fig. 4 rightmost), and the "fake Gaussian transitions" control (Sec. 5.3) are the right kinds of probes for the mechanism, even if some of their results are uncomfortable for the stated narrative.
- **Transfer experiment is a genuine generalization test**: Using Walker-stand data for Walker-walk, etc. (Sec. 5.2, Fig. 4a) shows the method can use data whose state-action distribution differs from the target task, in 2/3 settings.

## Weaknesses

### Fatal
None.

### Major
- **Random-policy data in dense-reward tasks makes the pseudo-label nearly correct, so the headline experiments do not stress the claimed mechanism.** Sec. 4.2 states "we used state, action transitions from a random policy" for all main experiments (50k transitions). In DMControl locomotion and most Meta-world tasks, random policies genuinely receive near-zero reward on the vast majority of transitions, so labeling them 0 is approximately ground-truth labeling, not pseudo-labeling. The paper's framing ("pessimistic prior from incorrect-but-low-bias labels", Sec. 4.1) is therefore not really tested in the main results — only the transfer experiment (partially trained policies, Fig. 4a) probes the harder regime, and there SDP wins only 2/3.
- **Missing matched-data baseline.** The natural control — PEBBLE/R-PEBBLE with the same 50k transitions placed in the replay buffer (and optionally pre-trained as a feature extractor *without* the zero pseudo-label) — is absent. Without this, the lift over PEBBLE conflates (i) a richer initial replay buffer, (ii) reward-model pre-training as feature learning, and (iii) the zero-pseudo-label "pessimistic prior." The component ablation (Fig. 4b) compares phases of SDP against each other but does not separate the *zero-label* contribution from data-volume / feature-pretraining effects.
- **The "fake transitions" ablation is in tension with the stated mechanism.** Sec. 5.3 reports that pre-training on Gaussian-noise inputs targeting the same constant-zero output yields significantly worse results than pre-training on real sub-optimal transitions. Since both schemes share the "pessimistic output" target, this implies the benefit derives from the reward model fitting features of the real state-action distribution, not from the pessimistic-prior story in Sec. 4.1. The paper does not reconcile this and continues to claim the "free reward labels / head start in identifying low-quality transitions" framing.

### Minor
- **Significance reporting is incomplete and partially broken in narration.** Sec. 5.2 says "SDP significantly (p<0.05) improved learning" but the sentence is truncated and the text never enumerates the per-environment / per-algorithm count of significant wins. Fig. 2 uses asterisks, but at N=5 seeds the rate of significant wins materially qualifies the "never hurt; often helps" framing.
- **Conclusions about scaling of sub-optimal data are drawn from a single environment (Walker-walk).** Sec. 5.3 varies the data budget ∈ {5k, 15k, 50k} only on one task; the "more data → better" claim should be evaluated on at least one Meta-world task too.
- **The transfer experiment's one failure is unanalyzed.** Since the transfer setting is the *only* one where the pseudo-label is genuinely incorrect on a non-trivial fraction of transitions, the failure case is precisely the most informative datapoint and should be discussed.
- **"Readily-available sub-optimal data" framing is in tension with the experimental setup.** Random-policy rollouts presume simulator access; the implicit comparison to offline-RL-style pre-existing datasets is overstated for the setting tested.

### Trivial
- The justification "the bias is low ... does not greatly influence learning" (Sec. 4.1) is asserted, not measured; even a small empirical check of the learned reward on random vs. on-policy transitions would substantiate it.

## Nice-to-Haves
- A predicted-reward landscape visualization (random vs. on-policy transitions before/after pre-training) to directly test the "pessimistic prior" claim.
- A sparse-reward Meta-world task, where "0 is approximately correct" no longer trivially holds, to probe whether the bias becomes harmful.
- Re-running the main results table with partially-trained-policy data (as in the transfer experiment) as the default source of D_sub.

## Removed Points
*These points are flagged to be removed; treat them with caution.*
- *Harsh critic implied that not deeply differentiating from Yu et al. 2022 is a weakness.* This is a "missing related work / novelty" framing that the paper actually addresses (Sec. 2.2 cites it and the contribution statement explicitly positions SDP as porting the idea to HitL RL); removed under the rule against missing-related-works critiques.
- *Strength "feedback efficiency approaches the SAC oracle with 60 queries."* Kept implicitly within the breadth strength but not promoted as a standalone strength, because it depends on the random-policy / dense-reward setup that the Major weakness questions.
- *Strength "clean reproducible setup with simulated teacher / Welch t-tests."* Generic methodological hygiene rather than a paper-specific strength.

## Novel Insights
None beyond the paper's own contributions. The most interesting incidental finding is that the "fake transitions" ablation, taken at face value, points toward feature pre-training rather than a pessimistic-prior mechanism — but this is the paper's own ablation, not a meta-review insight.

## Suggestions
- Reframe (or at least extensively caveat) the contribution: based on the fake-transitions ablation, the mechanism is likely "reward-model feature pre-training that happens to bias outputs low," not a clean pessimistic-output prior. Either change the framing or add experiments that separate the two.
- Add the matched-buffer baseline (50k transitions in the replay buffer, no reward-model pre-training) for at least 3 representative tasks.
- Rerun the headline experiments using partially-trained-policy data (as in the transfer setup) as the default D_sub, and report per-condition significance counts rather than a single aggregate claim.
- Add a sparse-reward task to probe whether labeling rare positive-reward transitions as 0 introduces meaningful bias.
- Analyze the transfer-experiment failure case.

---

**Axis evaluation.** *Originality:* moderate — direct port of Yu et al. 2022's offline-RL trick to HitL RL, with a replay-buffer-seeding twist. *Importance:* feedback efficiency in HitL RL is a real bottleneck. *Are claims well supported:* partially — the "never hurts, often helps" empirical claim is broadly supported, but the mechanistic claim ("pessimistic prior from pseudo-labels") is not cleanly identified by the experiments as designed. *Soundness of experiments:* reasonable breadth, but missing the matched-data baseline and using a near-trivial data source for main results. *Clarity:* generally clear; algorithm and figures are easy to follow. *Value to community:* the technique is cheap to try and the breadth of base algorithms makes it a useful empirical reference, but the paper would have more lasting value if it correctly identified its mechanism.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>