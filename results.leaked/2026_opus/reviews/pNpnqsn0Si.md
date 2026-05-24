Now I have enough calibration. Let me synthesize the final review.

Round-1 bracket: Based on initial searches, the paper sits between the weak-anchor rejects (~2-3) and strong-anchor accepts (~8). Round-1 narrowed to bracket [4.5, 6.5] based on similar adaptive-computation papers.

Round-2 narrowed within [5.0-6.0] using direct analogs:
- Hyper-UT (5.00, Reject): adaptive computation transformer with similar critique patterns (synthetic motivation vs evaluated tasks, missing baselines).
- Pause Tokens (5.50, Accept, split 8/3/3/8): directly closest analog — Goyal et al. is cited by Thoughtbubbles. Reviewers split on whether contribution is enough given missing comparisons.
- Efficient Stagewise Pretraining (5.75 Reject / 6.75 Accept): pretraining method with similar contribution scope.
- γ-MoD (6.67 Accept): more polished MoD-related work.

Thoughtbubbles compares: stronger architectural novelty than Hyper-UT, similar scope to Pause Tokens with better empirical breadth (3 scales × 2 datasets) and unsupervised allocation, but weaker than γ-MoD on baseline rigor (Thoughtbubbles' Copy-N is strawman and MoD itself is cited but not run).

---

## Summary

The paper introduces **Thoughtbubbles**, a decoder-only transformer that learns, via standard LM loss alone, to dynamically fork or prune residual streams between certain layers — creating "bubbles" of additional latent computation at tokens that need them. At 150M–772M parameters trained on 2.5B tokens of OpenWebText/peS2o, it reports lower validation perplexity than both a parameter-matched GPT-2 baseline and a computation-matched "Copy-N" baseline that duplicates input residuals, with consistent (if small) gains on LAMBADA and HellaSwag and an interpretability finding that allocated forks correlate with token entropy.

## Strengths

- **Genuinely novel mechanism.** §2.3–2.4 (Eqs. 1–10) define a cumulative-score, top-k forking step plus score-attenuated attention/residual update that lets the model learn dynamic *parallel* (not depth-skipping) compute allocation from LM loss only. Unlike pause-token methods (Goyal et al. 2024; Sun et al. 2025), placement is not manual.
- **Consistent perplexity improvement across scales and datasets.** Table 1 shows Ours (κ=4L) is the best on perplexity in all six (scale × dataset) cells, e.g., 19.74 vs. 21.22 at 772M OpenWebText, 13.77 vs. 14.64 at 772M peS2o, and the 319M Thoughtbubbles beats the 772M baseline on OpenWebText (Figure 3) — a striking compute-size trade-off.
- **Forks are functionally used, not vestigial.** Figure 4 shows the "og" rightmost token attends to its child forks with attention scores an order of magnitude higher than to other tokens, providing concrete evidence the forked streams influence the output computation.
- **Unsupervised interpretable allocation.** Figure 5 shows fork count correlates with token entropy measured by both the forking model and an independent baseline LM, suggesting the learned allocation is non-arbitrary.

## Weaknesses

### Fatal
None. The mechanism works at the tested scales, the perplexity gains are real, and no claim collapses given what is on the page.

### Major

- **No comparison against a real adaptive-compute method.** §6 cites Mixture-of-Depths (Raposo et al. 2024), Universal Transformers, MoEUT (Csordás et al. 2024), and MrT5 (Kallini et al. 2024) — all adaptive-compute methods trained with LM loss only — but none are run as baselines. The only computation-matched baseline (Copy-N, §3.3) is a non-adaptive duplicator that "[takes] the rightmost residual for decoding." The contribution as stated ("first unsupervised dynamic allocation of latent parallel computation") leans hard on the "parallel residual streams" qualifier to exclude MoD-style adaptive-compute work; without at least one MoD-class baseline, the empirical claim reduces to "beats naive duplication." This is the central evidential gap.

- **Output averaging is an uncontrolled confound on the headline perplexity numbers.** Eq. (11) decodes every residual stream and averages the resulting distributions weighted by cumulative scores — effectively a small output ensemble. The Copy-N baseline does *not* do this (§3.3 explicitly takes the rightmost residual for decoding). The paper does not report (a) a Thoughtbubbles variant that decodes only the rightmost residual, or (b) a Copy-N variant that averages over all copies' decode distributions. Without one of these ablations, an unknown share of the perplexity gain is attributable to score-weighted output ensembling rather than to the forking mechanism itself. This directly threatens the mechanistic interpretation.

- **Framing/evidence mismatch.** §1 motivates the method as "scaling inference-time compute" and "parallel thinking" / multi-step reasoning, but every reported evaluation is short-pretraining perplexity plus zero-shot LAMBADA/HellaSwag/BLiMP/PIQA. GSM8K is explicitly deferred to §8. The reasoning/test-time-compute narrative is grafted onto results that the evidence supports only as "an architecture variant that lowers perplexity at small scales." The underlying perplexity result is genuine; the surrounding claim is broader than the evidence.

### Minor

- **No variance/seed reporting on the headline table.** Several Table 1 cells differ by ~0.1–0.3 PPL or ≤1 accuracy point. At 2.5B-token pretraining and 150–319M parameters, this is plausibly within seed noise on HellaSwag/PIQA/BLiMP. The "319M Ours > 772M baseline" claim in particular deserves a multi-seed confirmation. The paper's *perplexity* gaps at 772M and 319M (~1+ PPL) probably exceed noise; the smaller-scale and downstream-accuracy cells less so.

- **peS2o 150M LAMBADA regression at κ=2L is uncommented.** Table 1 row: Ours (κ=2L) gets 5.0 LAMBADA vs. baseline 8.1, while Ours (κ=4L) recovers to 10.3. This non-monotonic behavior at small scale weakens the "robust gains" framing and warrants discussion.

- **Top-k gradient pathology acknowledged but not solved.** §8 states "too much forking results in no further performance improvement … due to certain tokens with high cumulative scores early on in the model being dropped by hard top-k decisions later in the model, thus resulting in no gradients to update the early large cumulative scores." Forking is inserted only before layers 3/7/11 (§3.1); whether the front-loaded placement is in part a workaround for this optimization issue is not openly examined. The randomization/noise mitigation is mentioned but not implemented or tested.

- **Test-time-compute scaling claim is not scanned.** Although the paper frames the method as test-time compute scaling, there is no κ_inference sweep — only the comparison of dynamic vs. fixed forking in Figure 6. A monotonic perplexity-vs-κ_inference curve would be the direct evidence for the framing.

- **Concave-parabolic entropy claim is not falsified against the alternative explanation.** §5's post-hoc explanation (highest-entropy tokens are clause edges where extra compute does not help) is consistent with the data but indistinguishable from the alternative that high-entropy tokens are exactly the tokens with poorly-trained scores due to the top-k gradient issue in §8.

### Trivial
- None substantive given the parser caveat.

## Nice-to-Haves

- A head-to-head against Mixture-of-Depths (Raposo et al. 2024) under matched FLOPs would be the single highest-leverage addition.
- An ablation that (a) decodes only the rightmost stream from Thoughtbubbles, and (b) averages across copies in Copy-N, isolating the forking mechanism from output-distribution mixing.
- A κ_inference sweep at fixed κ_train to directly support the "test-time compute scaling" framing.
- Probe forked residuals to show they specialize beyond what the parent residual computes — this would convert Figure 4's "forks are used" into "forks are doing something specific."
- A clean per-batch FLOPs accounting at κ=4L vs. Copy-5 (as currently presented, the FLOPs-matching is a worst-case bound).

## Removed Points

These points are flagged to be removed; treat them with caution.

- *Generic strength about importance of "parallel thinking" framing.* The strength finder leaned partly on the abstract's framing; since the Major weakness above (framing/evidence mismatch) is verified, the "addresses an important problem" angle is downgraded rather than counted as evidence.
- *Concerns about reproducibility from undisclosed seeds or training details.* Single-seed pretraining at this scale is standard practice in the subfield; treat as a minor methodological note, not a structural defect.
- *Implication that front-loaded forking (layers 3/7/11) is unfair/non-standard.* The paper discloses the placement and defers details to an appendix; without verified evidence of cherry-picking, this is speculative and is folded into the Minor "top-k pathology" note instead.

## Novel Insights

None beyond the paper's own contributions. The most genuinely novel observation from the reviews is the methodological point that score-weighted decoder averaging (Eq. 11) is itself an output ensemble — distinct from the forking mechanism — and that the paper conflates the two empirically. This is an observation about the experimental design rather than a new external insight.

## Suggestions

- Run Mixture-of-Depths (and at least one of MoEUT or UT) at the same scales/FLOPs and report against them in Table 1.
- Add two ablations: Thoughtbubbles-rightmost-decode and Copy-N-with-decode-averaging. If a meaningful fraction of the gain survives the first, the mechanistic claim is much stronger.
- Report multi-seed variance for at least the 150M and 319M rows of Table 1; one or two seeds may be enough to clarify which deltas are real.
- Tighten the framing in §1 and §7 to match the evidence: an architecture that lowers perplexity via adaptive parallel compute at small scale, with reasoning evals as future work, rather than a "test-time compute scaling" / "parallel thinking" architecture.
- Add a κ_inference sweep on a fixed checkpoint and report whether perplexity decreases monotonically as forking budget grows.

## Axis Evaluation

- **Originality**: High. The forking/pruning of residual streams with score-attenuated attention is a non-obvious mechanism distinct from MoD (depth skipping), pause tokens (fixed placement), and Universal Transformers (recurrence).
- **Importance of the research question**: Moderate-to-high. Unsupervised, latent, input-adaptive compute is a live area; the framing as test-time-compute scaling, however, overstates what is evaluated.
- **Whether claims are well supported**: Mixed. The perplexity claim is supported relative to in-paper baselines, but the central comparative claim against adaptive compute is undermined by the missing MoD-class baseline, and the mechanistic claim is undermined by the output-averaging confound.
- **Soundness of experiments**: Adequate within the design as scoped — three scales, two datasets — but missing the variance reporting and ablations that would isolate the contribution.
- **Clarity of writing**: Generally clear; equations 1–11 are precisely stated; figures convey the mechanism well. The motivation/evidence gap is a clarity issue at the framing level.
- **Value to the community**: Real but currently capped by the experimental gaps. A revision that includes a MoD comparison and the averaging ablation would substantially raise its value.

---

**Anchors retrieved**

Round 1 (bracketing):
- `MI0UiWeqOl.md` (2.33, Reject) — much weaker, off-topic interactions paper; bottom-of-bracket anchor.
- `7LZjuA4AB2.md` (3.00, Reject) — pretraining distribution-shift, weaker.
- `jqx5XI4Yr3.md` (3.40, Reject) — protein adapters, off-topic.
- `WM5G2NWSYC.md` (2.00, Reject) — sub-network adaptation, much weaker.
- `tI3eqOV6Yt.md` (5.00, Reject) — Hyper-UT, adaptive computation, read in full; very comparable scope, comparable critique pattern (synthetic motivation vs evaluated tasks).
- `1SO93f7sVf.md` (4.25, Reject) — LoRA pretraining, less topical.
- `ZyH5ijgx9C.md` (5.75, Reject) — stagewise pretraining, read in full; methodologically more careful than Thoughtbubbles.
- `Y5LjYI4N6P.md` (6.75, Accept) — same stagewise pretraining work, accepted version.
- `PdaPky8MUn.md` (8.00, Accept) — long-seq fair comparison, clearly stronger and broader.
- `vf5aUZT0Fz.md` (8.00, Accept) — DEPT, stronger.
- `wg1PCg3CUP.md` (8.00, Accept) — scaling laws, clearly stronger.
- `t7P5BUKcYv.md` (8.00, Accept) — MoE++, more polished and broader.

Round 2 (narrowing in [4.5, 7]):
- `1GTARJhxtq.md` (5.75, Accept) — perplexity-based data pruning, comparable rigor concerns but accepted; less ambitious claims.
- `i7oU4nfKEA.md` (6.25, Reject) — multilinguality, off-topic.
- `huuKoVQnB0.md` (6.00, Accept) — pretraining data improvement, more polished.
- `zpBamnxyPm.md` (5.75, Reject) — downstream scaling, off-topic.
- `mb2ryuZ3wz.md` (5.75, Accept) — variable image tokenization, conceptually adjacent (adaptive representational capacity), accepted with similar rigor profile.
- `q44uq3tc2D.md` (6.67, Accept) — γ-MoD, read in full; more comprehensive and well-baselined than Thoughtbubbles.
- `tFV5GrWOGm.md` (6.00, Accept) — ElasticTok, adaptive token allocation; accepted with cleaner story.
- `6qUUgw9bAZ.md` (6.50, Accept) — Learning How Hard to Think, input-adaptive LM compute; accepted, more directly evaluates adaptive allocation claim than Thoughtbubbles does.
- `ph04CRkPdC.md` (5.50, Accept split 8/3/3/8) — Pause Tokens, read in full; directly closest analog. The 3/3 reviewers' decisive concern was missing comparison to ACT/adaptive-compute alternatives — exactly the missing-MoD problem Thoughtbubbles has.
- `30oIfmrcFO.md` (6.25, Accept) — Seq-VCR pause-token reasoning, more focused reasoning eval.
- `UJkgGbLfWA.md` (5.00, Reject) — planning tokens, similar contribution-scope issue.

**Final placement.** Thoughtbubbles sits squarely between Pause Tokens (5.5 Accept) and Hyper-UT (5.0 Reject). Its architectural novelty and consistent perplexity improvements push it above Hyper-UT (which had less convincing empirical breadth). But its missing-MoD baseline and unaddressed output-averaging confound place it below γ-MoD (6.67) and below "Learning How Hard to Think" (6.50), both of which directly compare against the relevant adaptive-compute alternatives. It is closest in spirit to Pause Tokens, but with the same flaw that earned Pause Tokens its 3/3 reviews (no comparison to the adaptive-compute family it competes with). Net: ~5.0.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>