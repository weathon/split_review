Now I have enough understanding of the paper. Let me do calibration retrieval.I have sufficient anchors. Let me now write the final review.

**Round 1 bracket**: Topically closest anchors were NanoMoE (3.00, reject) and EfficientSkip (2.50, reject), both small-scale MoE/sparse architecture proposals with limited evaluation and weak baseline comparisons. Initial bracket: 2.5 – 4.5.

**Round 2 narrowing**: ME-LoRA (3.75, reject), LokiLM (3.60, reject), Quantifying Variance (4.17, reject), Experts on Demand (3.50, reject) cluster near 3.5. Papers in the 5.5 range (NanoLM, Studying SLMs, COrAL) all have more substantial evaluation and don't carry headline-overclaim + sign-error + single-seed flaws together. MoEP's combination of issues places it close to the 3.0 cluster.

---

## Summary
MoEP proposes a decoder-only architecture that combines top-k routing across **parallel transformer sub-blocks** with **MoE shrink/grow projections** that move tokens between a high hidden dimension (used at the first/last full layer) and a low hidden dimension (used inside a stack of parallel layers). The total parameter count is kept fixed against a dense GPT-2 baseline, and the system is evaluated on the BabyLM strict-small (10M words, ~28M parameters) track.

## Strengths
- **Fixed total-parameter sparse design is concretely instantiated and beats the matched dense GPT-2 baseline on the AoA-excluded macro average** (MoEP 49.00 vs. own GPT-2 48.10, HF GPT-2 46.60; Table 1). This is the cleanest piece of evidence for the central thesis that sparsity can be added without growing total parameters.
- **The architecture is fully specified end-to-end with public training/eval pipelines**: tokenizer training, shared epoch seed across models, 1M-word checkpointing, BabyLM's official evaluation pipeline, and released code/weights (Section 4, Tables 2–3) — enabling independent verification of the headline result.

## Weaknesses

### Fatal
None — the issues below are serious and accumulate, but none in isolation invalidates the paper outright.

### Major
- **The headline "outperformed all BabyLM strict-small baseline models" (§1, §5.1) is not what Table 1 shows.** On the macro average that excludes AoA, all three GPT-BERT baselines beat MoEP cleanly: causal 54.10, focus-causal 53.65, mixed-causal 52.40, versus MoEP 49.00 (3–5 point gaps, larger than any margin MoEP claims over GPT-2). The "win" only holds under the AoA-inclusive macro average, where the GPT-BERT models score −3.9, 3.8, 14.5 on AoA — a single task dragging them down. The paper does soften this in §5.1 ("Even when excluding AoA … MoEP still outperformed the BabyLM GPT-2 baseline, which we consider our primary comparison"), but the abstract and §1 do not — and the over-strong framing is what frames the contribution.
- **No ablations isolate the four contributions.** The architecture combines (a) top-k routing among $P$ parallel blocks, (b) reduced hidden dimension $d_P < d_L$, (c) the MoE shrink projection, (d) the MoE grow projection, plus the expert type (linear vs. SwiGLU). The paper varies none of $P$, $k$, $N$, $d_P/d_L$, $E$, or the shrink/grow MoE blocks individually. With a ~0.9 point gap over the authors' own GPT-2 on a single seed, there is no way to attribute that gain to the proposed mechanism rather than to extra routing parameters, capacity reallocation, or the load-balance regularizer.
- **Contribution 3 (routing analysis) is not delivered.** §1 promises "We analyze expert networks routing behavior and show that layer level parallelism enable fast and stable training." Appendix A.3 reports *evaluation-score* trajectories over training, not routing behavior — no expert utilization, no per-block selection histograms, no analysis of whether load-balancing actually prevents collapse. The conclusion may be correct, but the evidence for it is not in the paper.
- **The MoEP-SwiGLU comparison is not parameter-matched.** Table 2 reports MoEP at 28M (matched to GPT-2) but MoEP-SwiGLU at 38M (36% larger). §5.1 nonetheless concludes that "lightweight linear experts are more effective at the small scale" from this comparison. A 36% larger model performing slightly worse is at least as consistent with mis-tuning or under-training as it is with expert-type intrinsic difference — undermining Contribution 4.

### Minor
- **Sign inconsistency in the load-balance loss.** Eq. 2 writes $\mathcal{L}_{\text{balance}} = -\sum_i p_i \log p_i$ (entropy of the average routing distribution). Entropy is *maximized* by uniform routing, so to *prefer* uniform routing it should be subtracted from the loss; Eq. 3 adds it with a positive coefficient. As written, either Eq. 2 should drop the minus sign, or Eq. 3 should use negative $\lambda$. Either way, the formal description of the regularizer is inconsistent with its purpose. In a method paper this needs to be exact.
- **Single seed (Table 3: seed 42).** With a ~0.9-point macro-average gap to the authors' own GPT-2, the headline difference is well within typical seed-to-seed variance at this scale. The claim could still hold with multi-seed runs but is not currently supported.
- **Sample-efficiency claim is not clearly supported by the cited appendix.** §5.1 points to Appendix A.3 to support that "MoEP extracted useful patterns earlier during training," but §4 states both MoEP and GPT-2 peak at the 30M-word checkpoint. The appendix's qualitative claim about MoEP scores being more uniformly at-or-above task means at peak is suggestive, but no overlaid checkpoint curves with seed variance are provided.
- **Notation: §3.3 conflates $P$ and $K$.** "Each Parallel Layer contains $P$ Parallel blocks $\{B_1, \dots, B_K\}$." Earlier the index runs to $P$; here the same set is indexed to $K$ (also the routing top-$k$ symbol).
- **Output aggregation rule is under-specified.** §3.3 says routed inputs are "summed up together" but does not state whether outputs are gate-weighted, mean-pooled, or normalized — a non-trivial detail for top-k expert routing.

### Trivial
None substantive beyond presentation issues that should not influence acceptance.

## Nice-to-Haves
- A controlled comparison at fixed total parameter count between: (a) MoEP as proposed, (b) MoEP with routing disabled (all $P$ blocks always active), (c) a serial — not parallel — stack with the same shrink/grow projections, and (d) the authors' own GPT-2, all with multiple seeds.
- A direct routing-behavior analysis: per-block utilization histograms, effect of removing the load-balance term, top-1 vs. top-2 sensitivity. This would substantiate Contribution 3.
- A sample-efficiency curve (macro-avg vs. training tokens) with seed bands for MoEP vs. the matched GPT-2.
- Reporting active-vs-total parameters per token; a parameter-fixed sparsity story needs both.
- Re-framing of the GPT-BERT comparison honestly under the AoA-excluded metric.

## Removed Points
*These points are flagged as removed; treat with caution.*

- *Strength Finder claim 2 — "Layer-level parallelism + top-k routing enables faster early learning"*: Demoted to a minor strength, not removed. The paper states both MoEP and GPT-2 peak at 30M words (Section 4), so the "faster early learning" framing is not cleanly supported by the cited appendix.
- *Strength Finder claim 3 — Load-balancing loss formally defined*: Removed because the formulation has the sign inconsistency noted in the Minor section; we cannot list it as a clean strength.
- *Strength Finder claim 4 — "Code/weights released for reproducibility"*: Demoted into the main released-pipeline strength; do not list separately.
- *Harsh critic: "Layer-level MoE is overstated as relatively unexplored"*: This is a framing nitpick rather than a substantive flaw and does not affect the central claim. Worth mentioning to the authors but not weighting against acceptance.
- *Harsh critic: HF-GPT-2 baseline vs own GPT-2 reimplementation gap (1.5 pts) implies "matched conditions" not honored*: The two are in fact different training runs (HF baseline vs. their own); the paper does treat the authors' own GPT-2 as the primary comparison in §5.1. Not a major flaw, more a presentation/transparency concern.

## Novel Insights
None beyond the paper's own contributions. The architectural ingredients (top-k routing over parallel residual blocks, dimensional shrink/grow projections, parallel sub-paths) all exist in the cited literature (PaLM, Branchformer, PaPaformer, MoLE); the novelty is in their specific combination at fixed total parameter count.

## Suggestions
- Re-write the abstract and §1 to claim only what Table 1 supports: MoEP modestly beats the matched-parameter GPT-2 baseline on the AoA-excluded macro average; under that same metric GPT-BERT is stronger. Position MoEP as competitive-with-GPT-2 *and* sample-efficient (if multi-seed data supports it), not as state-of-the-art on the track.
- Fix Eqs. 2/3: clarify whether the regularizer is the entropy of mean-routing (with a *negative* $\lambda$) or the negative entropy (with a *positive* $\lambda$).
- Add at least 3-seed runs for MoEP vs. own GPT-2 on the macro average and report variance bands.
- Add ablations: $P \in \{2, 4, 8\}$, $k \in \{1, 2\}$, $N \in \{4, 10, 16\}$, removal of shrink/grow MoE, and an "always active" $P=k$ control. Even small slices of this would meaningfully strengthen the paper.
- Add the routing analysis Contribution 3 promises (utilization, entropy curves, ablating $\mathcal{L}_{\text{balance}}$).
- Either match MoEP-SwiGLU to 28M total parameters or remove the "lightweight linear experts are more effective at small scale" conclusion.

---

**Evaluation on the requested axes.**
*Originality:* Moderate — the combination of layer-level routing with dimensional shrink/grow is a reasonable design point, but each ingredient is established in prior work and the novelty framing is overstated.
*Importance of the question:* Fixed-parameter sparsity for small LMs is a legitimate and useful question.
*Claims-vs-support:* The strongest claims (beating all BabyLM baselines, faster sample efficiency, routing analysis demonstrating stability) are not well supported by the table or appendix actually presented.
*Soundness of experiments:* Single seed, no ablations, parameter-budget asymmetry for SwiGLU variant, and an equation-sign inconsistency in the regularizer reduce confidence.
*Clarity of writing:* Mostly intelligible; notation issues in §3.3, equation sign ambiguity in §3.4, and a small handful of under-specified procedures.
*Value to community:* The released code and a competitive small-model variant are real but modest; in current form the empirical evidence is too thin to justify drawing the conclusions the paper draws.

---

**Calibration anchors retrieved**
| Path | Avg score | Round | How it compares to MoEP |
|---|---|---|---|
| `04RLVxDvig.md` NanoMoE | 3.00 | R1 + R2 | Most topically similar; small-scale MoE-flavored building block with limited eval, no real baselines, modest claims — MoEP is similar in scope but with one acknowledged matched-parameter win and additional framing/sign issues. |
| `7DY2DFDT0T.md` EfficientSkip | 2.50 | R1 | Sparse LM transformation, single model, narrow eval; MoEP has somewhat tidier presentation and a clear matched-parameter result, putting it slightly above. |
| `762u1p9dgg.md` MOEfication by Experts as Masks | 3.40 | R1 | Sparse-from-dense MoE work, mixed reception; comparable territory to MoEP. |
| `XVHXVdoV11.md` Collective Model Intelligence | 3.40 | R1 | Less topically aligned. |
| `rWui9vLhOc.md` MoLEx | 6.33 | R1 | Stronger — substantial fine-tuning study, ablations; MoEP not at this bar. |
| `6mLjDwYte5.md` MoE + Instruction Tuning | 6.75 | R1 | Stronger empirical scope, multi-setup study; MoEP not at this bar. |
| `UUZuwDv8iw.md` Fantastic Experts | 4.33 | R1 | Borderline reject for narrow experiments; MoEP slightly weaker due to overclaim + sign issue. |
| `9XETcRsufZ.md` Mixture of Parrots | 7.00 | R1 | Has theoretical + empirical contributions far above MoEP. |
| `vf5aUZT0Fz.md` DEPT, `xXTkbTBmqq.md` OLMoE, `tcsZt9ZNKD.md` Sparse Autoencoders, `tyEyYT267x.md` SAR diffusion | 8.0–8.67 | R1 | Substantially stronger papers — not comparable. |
| `E2RyjrBMVZ.md` Quantifying Variance | 4.17 | R2 | Rejected but more methodological depth than MoEP. |
| `0qexTTfnmH.md` Me-LoRA | 3.75 | R2 | Comparable: rejected for limited eval and unclear gains. |
| `H03dW4TysQ.md` Experts on Demand | 3.50 | R2 | Similar tier — small-scale routing-focused proposal. |
| `bppG9srkpR.md` LokiLM | 3.60 | R2 | Small-LM technical-report style, comparable scope. |
| `mao3y822aM.md` NanoLM | 5.50 | R2 | More rigorous methodology than MoEP. |
| `4xBew7kuYB.md` Studying Effects of Training Data on SLMs | 5.50 | R2 | More careful empirical study; MoEP not at this bar. |
| `0JjsZC0w8x.md` COrAL | 5.75 | R2 | More substantial method paper than MoEP. |

**Round 1 bracket:** 2.5 – 4.5 (below the 5.5+ anchors which all have multi-seed, ablation-driven, or much-larger empirical scope; above the 2.5 floor because MoEP at least delivers a matched-parameter result and a working released pipeline).

**Round 2 narrowing:** MoEP sits very close to NanoMoE (3.00) — both are architectural proposals with narrow evaluations and weak baseline framing. MoEP has slightly more polish (a working benchmark result, releases) but also unique problems (headline overclaim, sign error, undelivered Contribution 3). Net comparison: similar to NanoMoE, marginally weaker than Me-LoRA (3.75), clearly weaker than NanoLM (5.50). Anchored at **3.0**.

MY FINAL SCORE: <score>3.0</score>
MY FINAL DECISION: <decision>Reject</decision>