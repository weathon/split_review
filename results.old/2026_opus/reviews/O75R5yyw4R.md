Now let me run calibration searches to compare this paper against anchor papers.Round 1 bracket: based on initial comparisons, the paper sits between the 3.0 weak anchors and the 7.25 strong anchor. The most topically similar anchors are Ombm8S40zN (6.25, masked discrete diffusion steering, Accept) and vi3DjUhFVm (7.25, training-free SMC alignment, Accept). The paper is similar in spirit but has more internal inconsistency concerns. Bracket: **4.5 to 6.5**.Based on my Round 2 search, the most topically similar mid-range anchors are:
- Ombm8S40zN (6.25, DDPP - masked diffusion steering, Accept)
- G328D1xt4W (6.00, DRAKES - discrete diffusion reward fine-tuning, Accept)
- peNgxpbdxB (6.00, Scalable Discrete Diffusion Samplers, Accept)
- vi3DjUhFVm (7.25, DAS - SMC training-free alignment, Accept)

The paper has comparable empirical breadth (text + image, multiple backbones, multiple rewards) but lacks the wet-lab validation of DDPP and the cleaner theoretical packaging of DAS, plus has internal inconsistency issues (algorithm vs prose vs ablation) that the anchors don't have. The paper sits somewhat below DDPP/DRAKES (6.0-6.25).

Now writing the final review.

---

## Summary

The paper proposes IterRef, a test-time scaling method for discrete (masked-absorbing) diffusion models that frames reward-guided sampling as Multiple-Try Metropolis (MTM) with a noising-denoising transition kernel. With a particular balancing function the importance weights collapse and the acceptance test reduces to a simple reward ratio, and the authors prove (Prop. 1) that under reversibility the chain converges to the optimal reward-aligned intermediate distribution. Experiments span MDLM, LLaDA-8B (text) and MaskGIT (image) against BoN, SoP, SVDD, and FK Steering, with consistent reward gains — most notably reaching FK-level performance at ~4×–8× less compute on detoxification.

## Strengths

- **Consistent empirical superiority across modalities and backbones (Figure 2, Table 1).** IterRef beats four established baselines (FK, SVDD, SoP, BoN) on Toxicity / Sentiment / CoLA / Perplexity with both MDLM and LLaDA-8B, and on MaskGIT under CLIPScore (35.8 at NFE=16 vs. next-best 34.8). The breadth of the comparison is unusual for this line of work.
- **Convergence claim is concretely tied to the design (§3.1, Eq. 2–3, Prop. 1).** The chosen balancing function makes the importance weights collapse to 1/N and turns the acceptance ratio into a closed-form reward difference, which is a clean instantiation of MTM rather than a hand-rolled MCMC scheme.
- **Novel finding about *where* refinement helps in discrete diffusion (Table 2, §4.4).** Later denoising stages (closer to t = 0.1T) benefit most from refinement, opposite to the early-step dominance reported for continuous diffusion. This is a non-trivial empirical observation about discrete-diffusion dynamics.
- **Practical implementation reduces cost without (claimed) loss of guarantees (§3.3).** The balancing-function choice eliminates the backward proposal pool, and pool reuse on rejection avoids redundant resampling.
- **Safety case study with concrete budget (§4.5, Fig. 5a).** Reducing toxicity below 10% on the LLaDA-8B detoxification setup starting at 4× the base budget is a useful concrete data point.

## Weaknesses

### Fatal
None.

### Major

- **Mismatch between the algorithm description, the practical implementation, and the empirical knob N.** §3.1 shows w_n = N⁻¹ — uniform candidate selection — and the acceptance test β does not depend on N. §3.2 line 7 nonetheless calls this "**reward-weighted sampling** using w_n," and Table 3 shows N has very large effects (Toxic 3.3 → 54.0 from N=32,k=1 to N=4,k=8). The most plausible reconciliation is the pool-reuse trick in §3.3: reusing the same N candidates on rejection breaks i.i.d. proposal generation and is the mechanism by which N matters empirically — but in that case the practical algorithm is no longer the one for which Prop. 1's detailed balance is derived. The paper needs to either (a) describe the implemented selection step in the math, or (b) explicitly characterize the bias introduced by pool reuse. As written the "principled MTM" framing in §3.1 is in tension with the algorithm that produces the experimental numbers.
- **Algorithm 2 still describes the full forward+backward MTM that §3.3 says is eliminated.** Line 8 generates "N−1 auxiliary samples … and set x_t''^(N) = x_t" — the backward pool that the practical implementation drops. The reader cannot tell which version was actually run without going through §3.3 line-by-line, and the algorithm box is the natural reference. This compounds the issue above.
- **Closest MCMC competitor is acknowledged but not compared.** §5 explicitly cites PG-DLM (Dang et al., 2025), which "applies Particle Gibbs sampling, repeatedly resampling the entire trajectory multiple times" — the same conceptual move (MCMC over diffusion trajectories) for the same problem. Yet PG-DLM appears nowhere in Figure 2, Table 1, or Figure 5. DSearch and DTS are similarly cited but not benchmarked. Without these, one cannot tell whether the gains come from "MCMC refinement" generally or from the specific noising-denoising kernel choice — i.e., whether the methodological novelty is doing the work.
- **NFE accounting is single-axis despite the paper itself flagging the issue.** §3.3 states "aggregating these into a single NFE value may obscure meaningful differences, and it is preferable to report generative-model calls and reward-model calls separately." Figure 2, Figure 5(a), Figure 1, and Table 1 all collapse the two onto one axis. Because IterRef's noising step is described as "nearly zero cost" and acceptance uses reward-model calls, the cost balance shifts with backbone size (the paper notes MDLM and LLaDA-8B sit on opposite sides), and the headline "8× faster" claim depends on which model dominates. The direction of the result likely survives disaggregation, but the magnitude is currently unverifiable.

### Minor

- **Prop. 1's reversibility assumption ("q and p_θ form a reversible Markov kernel") only holds exactly when p_θ is the optimal denoiser of q.** With trained models this is approximate; the chain's stationary distribution is then only approximately p*(x_t). The paper does state the assumption, but Contribution 3 ("not simply heuristic … leads to convergence to the target distribution") reads as a stronger guarantee than the assumption supports. A one-line acknowledgement of the idealized-vs-realized gap would suffice.
- **Same reward used for guidance and for scoring on language tasks.** Toxic/Sentiment/CoLA/Perplexity (§4.2, §4.5) all evaluate on the same signal that drives the chain, which mechanically rewards harder search. The paper does provide held-out ImageReward for MaskGIT (§4.3), but no analogous held-out evaluator on the text side. Combined with the Figure 5(b) qualitative samples — which clearly show topic-evasion ("first lyrics of a Jamaica," "He is an icon for youngsters") rather than actual non-toxic completion — the evidence does not cleanly distinguish reward optimization from quality improvement. The paper flags this tendency in passing but does not engage with the implication for whether "below 10% toxicity" is the right success criterion.
- **Table 2 "Evenly" column reports much larger numbers than any single-step variant (65.0 vs 37.6 Toxic; 97.0 vs 37.6 Sentiment) despite the claim of fixed total budget.** The caption says "applying IterRef evenly at every timestep under the same total cost," but the magnitudes suggest the per-step budget under "Evenly" is larger, or the gain comes from applying refinement at many steps. A clearer statement of how compute was split would resolve this.
- **Ad-hoc explanation for LLaDA CoLA result (§4.2).** "BoN achieves larger gains, which can be attributed to the fact that LLaDA already generates a linguistically well-formed text" weakens the headline scaling claim and the same logic is not applied to other axes where LLaDA is similarly capable.
- **Small sample size with no variance/CI reporting.** 15 prompts × 20 samples × 3 seeds = 300 generations per text setting. Several reported gaps (e.g., MaskGIT CLIPScore 34.4 vs 34.8 at NFE=4) are within plausible noise; even rough standard errors would clarify which differences are real.

### Trivial

- Algorithm 2 line 9 references `x_t'^cand`, which is not defined elsewhere — presumably should be `x_t'`.

## Nice-to-Haves

- A held-out language evaluator (analogous to ImageReward for MaskGIT) or human evaluation on a small detoxification sample, to separate reward optimization from quality.
- An ablation isolating the role of pool reuse: with vs. without reuse at matched compute would directly test whether the empirical effect of N is real diversity or simply the reuse trick.
- Even a small comparison to PG-DLM at matched compute would substantially strengthen the "MCMC framing is what helps" story.
- Disaggregated NFE plots (generative calls vs. reward calls) on the same x-axis as Figure 2.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"The convergence guarantee oversells what is a heuristic" framed as fundamental* — demoted to Minor. The paper explicitly states the assumption (Prop. 1: "Assume that q and p_θ form a reversible Markov kernel"), so this is a calibration/overclaiming concern, not a structural flaw.
- *"The math gives uniform selection but prose says reward-weighted, therefore the central claim is invalid"* — kept as Major but **not** fatal. The harsh critic frames this as definitionally contradictory across math/prose/ablation, but the most natural reading is (i) selection is uniform from K, (ii) reward enters via β, and (iii) N matters because of pool reuse / acceptance-test conditioning. That requires authors to clean up the description, not to retract the contribution.
- *"§4.5 examples are reward hacking, undermining the safety claim"* — kept only as part of the Minor "same reward for guidance and scoring" point. The paper itself acknowledges the quoted-speech evasion, so this is a candor concern rather than an unaddressed flaw.
- *Generic strengths about importance of the problem and breadth of evaluation* — not kept as standalone strengths; folded into the concrete strengths above.

## Novel Insights

The most genuinely useful empirical observation surfaced here — beyond the paper's stated contribution — is the inversion of the "guidance is most effective in early steps" rule from continuous diffusion (Table 2): for masked discrete diffusion, refinement at later denoising steps (closer to t = 0.1T) dominates. That this holds across Toxic / Sentiment / Perplexity and not just CoLA is a non-trivial domain-specific finding that other discrete-diffusion guidance work should be aware of.

## Suggestions

- Rewrite §3.1–§3.2 so that the math, Algorithm 2, and §3.3 describe the *same* algorithm. Either fold pool reuse into the formal definition (and re-derive what happens to detailed balance), or write the math for uniform i.i.d. selection without reuse and add a separate "practical variant" section.
- Add PG-DLM (and ideally DSearch / DTS) as baselines to Figure 2 and Table 1, even on a subset of tasks. This is the single highest-leverage change.
- Replace Figure 2's single NFE axis with a 2-panel view (generative calls vs. reward calls), as §3.3 itself recommends.
- Add a held-out language evaluator on at least one text task (e.g., a different toxicity classifier than the one used for guidance) and report human evaluation on the detoxification sample to address reward hacking concerns.
- Clarify Table 2's per-step budget for "Evenly" vs. single-step variants, or rescale so the comparison is at literally matched compute.
- Soften the framing of Prop. 1 in §1's Contributions to reflect the reversibility assumption.

## Axis-by-Axis Assessment

- **Originality:** Moderate. Casting reward-guided discrete diffusion sampling as MTM with a noising-denoising kernel is a sensible and not-yet-explored framing, but it is one of several MCMC-style proposals for this problem (PG-DLM, DSearch, DTS), and the experimental section does not establish that the MTM specifics matter against those alternatives.
- **Importance of the research question:** Reasonable. Test-time scaling for discrete diffusion is genuinely under-explored, and a method that works at low compute would be useful.
- **Are claims well supported:** Partially. The empirical claim of "best among the chosen baselines" is well supported. The theoretical claim of convergence is supported only under an idealized reversibility assumption. The "8× faster" claim is supported on the single-NFE axis the paper uses but is sensitive to disaggregation it does not provide.
- **Soundness of experiments:** Adequate breadth (3 backbones, 5 rewards) but with internal-consistency issues (algorithm vs implementation, Table 2 budget), no variance reporting, and the closest MCMC competitor absent.
- **Clarity of writing:** Mixed. The intuition is clear and the figures communicate the headline result well, but §3 mixes the formal MTM, the practical implementation, and the algorithmic pseudo-code in a way that does not type-check — the harsh critic's confusion is symptomatic.
- **Value to the research community:** Real but bounded. The empirical numbers and the late-stage-refinement finding are useful; the framing inconsistencies and missing comparisons limit how much of the methodological story should be taken as established.

## Score and Decision

**Anchors retrieved:**

Round 1 (bracketing):
- `QKqWnNkwPL.md` — 3.00, weak band — self-distillation for diffusion; not closely related but anchors the floor.
- `W4djmqKZC6.md` — 3.00, weak band — pixel-aware reverse diffusion; only loosely related.
- `JJH7m9v4tv.md` — 3.00, weak band — post-hoc discriminator guidance; loosely related but at reject quality.
- `MBkoYFftRa.md` — 3.00, weak band — inner-loop feedback; unrelated.
- `2fgzf8u5fP.md` — 3.80, mid band — SVDD; close baseline-comparison territory, reject.
- `Ombm8S40zN.md` — 6.25, mid band — DDPP (masked discrete diffusion steering); most directly comparable, accepted with mixed reviews; current paper is similar in scope, somewhat weaker in theory cleanliness.
- `vi3DjUhFVm.md` — 7.25, strong band — DAS (training-free SMC for alignment); cleaner theory than the current paper.
- `KqbCvIFBY7.md` — 6.00, mid band — particle guidance; related but on continuous diffusion.
- `fV0t65OBUu.md` — 8.00, strong band — optimal covariance matching; cleaner contribution than the current paper.
- `xDrFWUmCne.md` — 8.00, strong band — LD3; not directly comparable.
- `6EUtjXAvmj.md` — 8.00, strong band — variational diffusion posterior sampling; theoretically tighter than the current paper.
- `esYrEndGsr.md` — 8.00, strong band — influence functions for diffusion; tangential.

Round 2 (narrowing within 4.5–6.5):
- `peNgxpbdxB.md` — 6.00 — scalable discrete diffusion samplers; methodologically tighter than the current paper.
- `G328D1xt4W.md` — 6.00 — DRAKES; reward optimization in discrete diffusion, theory-grounded; current paper has broader empirics but weaker internal consistency.
- `0gDQgwjoX0.md` — 4.67 — discrete Langevin dynamics; weaker than the current paper.
- `Qn4HEhezKW.md` — 5.00 — diffusion LM scaling; less ambitious method, broader experiments.
- `sMyXP8Tanm.md` — 6.20 — RADD (absorbing discrete diffusion); cleaner theoretical contribution.
- `1pTlvxIfuV.md` — 5.50 — reparameterized discrete diffusion; comparable polish.
- `MJNywBdSDy.md` — 5.75 — planned denoising; comparable empirical scope.
- `vxBvr5ZpIu.md` — 5.50 — Diffusion-PINN sampler; comparable.
- `b3CzCCCILJ.md` — 6.00 — revamping CFG; cleaner.

**Bracketing → narrowing:** Round 1 placed the paper between 3.0 and 7.25 with the closest topical anchor at 6.25 (DDPP). Round 2 sharpened this to (4.67, 6.25): the paper has clearly stronger empirics than the 4.67 anchor (Stochastic Gradient Discrete Langevin) and the ~5.0–5.5 anchors (Qn4HEhezKW, 1pTlvxIfuV), but its internal inconsistency between algorithm description and ablated knob, and the missing PG-DLM comparison, place it below the 6.00–6.25 anchors (DDPP, DRAKES, scalable discrete samplers) which have cleaner theory-implementation alignment. Calibrated against this, the paper sits in the upper-half of (4.67, 6.00) — closer to the 6.0 cluster than to the 4.67 anchor, but not at it.

**Final positioning:** below the most-similar accepted cluster (6.0–6.25), above the 5.0 reject cluster, with the major weaknesses being addressable in revision rather than fatal.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>