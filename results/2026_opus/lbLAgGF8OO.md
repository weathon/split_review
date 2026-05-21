Now I have a clear picture of the paper. Let me verify the key parser-error claims, then proceed with calibration.My round-1 bracket is **(5.5, 7.5)** — the paper is comparable to other theoretical adversarial-RL papers like aPNwsJgnZJ (avg 6.0). Let me narrow further.Based on round 2 narrowing, the paper compares as follows:
- vs. aPNwsJgnZJ (6.0, horizon-free adversarial linear mixture): Dig-DEC is **stronger** — multiple distinct contributions, resolves stated open problem, broader generality (hybrid bilinear/coverable, not just linear mixture, bandit not just full-info).
- vs. txD9llAYn9 (7.0, model-based RL minimalist): Dig-DEC is **comparable** — similar level of technical depth, both achieve multiple bound improvements; Dig-DEC has presentation problems the model-based paper does not.

This places the paper between 6.0 and 7.0, closer to 6.5 given that the headline hybrid-bandit result is deferred to appendix in §5.2.

Now I'll write the final review.

---

## Summary

The paper introduces **Dig-DEC**, a model-free decision-estimation coefficient that replaces the optimism principle of [FGQ+23]'s optimistic DEC with a pure information-gain objective combining a KL regularization term and an estimation-error divergence. The authors prove Dig-DEC is never larger than optimistic DEC (Theorem 13) and exhibit a constructed bandit where it is strictly smaller (Theorem 14); they also redesign the online estimation procedures (sample-splitting unbiased estimator in §4.2.1; refined two-timescale procedure in §4.2.2) to obtain improved T-rates and establish the first model-free regret bounds for hybrid MDPs (bilinear/coverable) with adversarial rewards and bandit feedback, resolving an open problem from [LWZ25].

## Strengths

- **Formal dominance over optimistic DEC.** Theorem 13 establishes `dig-dec_η^{Φ,D̄} ≤ o-dec_η^{Φ,D̄} + η` for any D̄, so every prior optimism-based bound is recoverable in the new framework — the new complexity measure is a strict generalization, not a sideways move.
- **First model-free, bandit-feedback regret for hybrid MDPs.** The paper resolves [LWZ25]'s explicitly stated open problem by handling adversarial rewards with bandit feedback in hybrid bilinear classes and coverable MDPs (Section 5.2 / Table 2). Removing optimism is the key technical mechanism — without an explicit reward estimator, bandit-feedback hybrid analysis becomes tractable.
- **First DEC-based √T regret for Bellman-complete MDPs.** §4.2.2 / Theorem 11 redesigns the two-timescale procedure so `Est ≲ log²|Φ|`, yielding √T regret with only `log|Φ|` dependence (Table 1, last block). This matches optimism-based approaches [JLM21, XFB+23] and improves [FGQ+23]'s `T^{5/6}` — the first time a DEC-based method matches optimism-based rates in this regime.
- **Sharper average-error estimator via sample splitting.** §4.2.1 constructs an unbiased estimator `L_h(φ) = Σ_h (2/τ Σ_{i≤τ/2} ℓ_h)(2/τ Σ_{i>τ/2} ℓ_h)` instead of [FGQ+23]'s biased squared-mean. Theorem 7 gets `Est ≲ N log|Φ| T^{1/2}`, leading to the headline T-exponent improvements in the abstract.
- **Mirror-descent-style analysis generalizes AIR.** The first-order optimality / Bregman argument around Eq. (5)–(6) replaces [XZ23]'s "constructive minimax theorem" with a cleaner, more flexible analysis that accommodates arbitrary convex divergences D and recovers [XZ23]/[LWZ25] results (Appendix C). This is plausibly a contribution future work will build on.
- **Concrete separation example.** Theorem 14 exhibits a 3-armed bandit where the optimistic-DEC algorithm of [FGQ+23] suffers `Ω(√T)` regret while Dig-DEC achieves O(1) — proving the new KL information-gain term can yield arbitrarily large improvements via distributional differences that mean-based D̄ cannot see.

## Weaknesses

### Fatal
None.

### Major

- **The hybrid-bandit result — the paper's headline contribution — is essentially invisible in the body.** §5.2 ("Hybrid Settings") is two sentences pointing at Table 2; the actual hybrid bilinear class, the lemma bounding `dig-dec` in the hybrid case, and the technical mechanism by which the absence of explicit reward estimation pays off are all deferred to Appendix I. Given that this is the resolution of [LWZ25]'s open problem and the most-touted contribution, the body should at minimum state the hybrid bilinear class concretely, give the key Dig-DEC bound, and walk through (at least informally) why removing optimism unlocks the bandit case. As written, a reviewer who restricts themselves to the body cannot verify the central claim of the paper.

- **The "strict improvement" over optimistic DEC is shown only on a constructed bandit; canonical settings yield the same dimensional rates.** Theorem 13 only guarantees `dig-dec ≤ o-dec + η`, and the paper itself concedes at the end of §6: "by regularization only, we can recover the bounds achieved by optimistic DEC in the stochastic setting (this can be seen from the proof of Theorem 13), though it is unclear whether it can give strict improvement." The `dig-dec` entries in Table 1 (`H²dη`, `√(H³d|A|η)`, etc.) match the dimensional rates one would write for optimistic DEC; only the Est-side rates differ. Theorem 14's 3-armed bandit is the sole strict-improvement witness. The abstract's "can be much smaller in special cases" is technically supported, but an MDP-class example would much better justify the new complexity measure as a contribution in its own right.

### Minor

- **Assumption 5 conflates a regularity condition with an adversary restriction.** Line 205 imposes `E^{π,M_t}[ℓ_h(φ; o_h)] = E^{π,M_{t'}}[ℓ_h(φ; o_h)]` across all `t, t'` inside an assumption labelled "Average estimation error." This effectively pins down the relevant part of the environment across rounds and is what makes hybrid learning tractable. Which adversarial moves does it forbid? The paper would benefit from explicit discussion separating the realizability-type content of Assumption 5 from its adversary-restriction content, especially given that the same conflation appears in Assumption 6 (line 241).

- **Assumption 3 (linear reward, known features) is restrictive and acknowledged so.** The authors are upfront that hybrid low-rank MDPs with unknown reward features (where [LMWZ24] obtains log dependence) are not covered, and that [LWZ25] had the same limitation. This is fine as a scope statement but does limit the generality of the headline hybrid result.

- **Comparison to prior rates in Tables 1–2 lacks a "prior-best" column.** A reader cannot tell at a glance which entries match prior bounds (showing the framework subsumes them) and which are strict improvements. Given that the headline rate improvements (`T^{5/6} → √T`, `T^{3/4} → T^{3/5}`) are scattered between the abstract and §1, a single column in Table 1 would resolve this.

- **The additive `η` slack in Theorem 13.** The relation is `dig-dec ≤ o-dec + η`, not pointwise ≤. The abstract's "is always no larger than optimistic DEC" should be qualified. It is unlikely to bite at the rates discussed (η is typically tuned to a small power of T), but the qualification belongs in the statement.

### Trivial

None retained — see Removed Points for what was filtered out.

## Nice-to-Haves

- A worked, MDP-scale example (not the 3-armed bandit) where Dig-DEC strictly improves over optimistic DEC — ideally an MDP class where reward distributions differ but means coincide, since that is precisely the regime the new KL information-gain term is designed to exploit.
- Promote the mirror-descent-style analysis (the Bregman argument around Eq. (5)–(6)) and the framework's recovery of [XZ23] / [LWZ25] from "see Appendix C" to a stand-alone subsection. This is plausibly the most reusable contribution of the paper.
- A stand-alone, body-level statement of the unbiased sample-splitting estimator (§4.2.1) and the refined two-timescale procedure (§4.2.2) as independent technical lemmas — the paper claims independent interest for both, and that claim is more credible if the lemmas are visible in the body.

## Removed Points

*These points are flagged to be removed — treat them with caution.*

- **Parser-corruption complaints about the abstract / §1 / Tables 1–2 exponents (e.g., `T^{3/4} → T^{3/5}`, `T^{5/6} → T^{7/8}`, `T^{13/8}`, `T^{3/2}`, "ALR" vs. "AIR" in Theorem 3, "from √T to T^{1/2}" in §4.2.1).** These are PDF-extraction artifacts (sub/superscript scrambling), not author errors. The harsh critic already flagged them as such; per the global rule, formatting artifacts are out of scope.
- **"The exponents in Table 2 may be super-linear in T."** This is conditioned on the parser corruption above. The Strength Finder correctly notes the intended on-policy bilinear hybrid rate is `Õ(d(H^5 log|Φ|)^{1/2} T^{2/3})`, which is sublinear. Demoted from a structural concern (since the harsh critic's own framing makes it conditional).
- **"Hybrid bounds rest on the restrictive Assumption 3 (linear reward, known features)."** The paper explicitly scopes this out as future work in §3 (line 121) and acknowledges [LWZ25] has the same limitation. Kept in Minor with weaker wording; not promoted to Major.
- **"Reproducibility / experiments missing."** Not raised, but worth being explicit: this is a theoretical paper and should not be faulted for the absence of experiments, per the harsh critic's own framing.
- **Generic strength: "addresses an important problem / interesting question."** Strength Finder did not include this, but typical noise of this type is preemptively removed.

## Novel Insights

The conceptual move that earns this paper its place is the decomposition of Dig-DEC's KL information-gain term into two parts: a *regularization* component `KL(ν_φ, ρ)` that keeps the marginal close to the prior (and recovers optimistic-DEC-equivalent bounds without invoking the optimism principle), and a *distributional information gain* component `KL(ν_φ(·|π,o), ν_φ)` that captures discrepancies invisible to mean-based estimation divergences (and powers the strict improvement in Theorem 14). The observation that optimism in [FGQ+23] is *not* fundamental — that it can be replaced by a regularizer that does the same work in stochastic settings while remaining viable under bandit feedback in adversarial settings — is the novel insight that goes beyond the paper's own headline claims. The cleaner mirror-descent-style analysis is the methodological side of the same insight: by abandoning the "constructive minimax theorem" framing, the framework opens to arbitrary convex divergences.

## Suggestions

- **Move the hybrid-bilinear-bandit walk-through into the body.** A page in §5.2 covering (i) the concrete hybrid bilinear class, (ii) the key lemma bounding `dig-dec`, and (iii) where the absence of explicit reward estimation enters the analysis would convert the open-problem resolution from "asserted" to "demonstrated."
- **State all polynomial-in-T rates in prose, not only in Tables 1–2.** Given that the headline improvements (`T^{5/6} → √T`, `T^{3/4} → T^{3/5}`, `T^{2/3}` for hybrid bilinear) are exactly what a DEC-literate reader is looking for, restating them outside the tables in the abstract and §1 prevents any ambiguity from rendering issues.
- **Add a "prior-best" column to Tables 1–2.** Even informal pointers (`[FGQ+23]: T^{5/6}`, `[LWZ25]: full-info only`) would let a reader see at a glance which rows are subsumption and which are strict improvement.
- **Sharpen Theorem 13's qualifier.** Replace "Dig-DEC is always no larger than optimistic DEC" in the abstract with "Dig-DEC is at most o-DEC + η for the same η" to match the actual statement.
- **Separate Assumption 5's adversary-restriction component from its realizability component.** Discuss explicitly which adversarial moves are forbidden by `E^{π,M_t}[ℓ_h] = E^{π,M_{t'}}[ℓ_h]` and what changes if one tries to relax it.

---

**Axis-by-axis assessment.**
*Originality:* High — Dig-DEC is a genuinely new complexity measure, and the regularization-vs-optimism reframing is a real conceptual move.
*Importance of research question:* High — the DEC/E2D line is a central thread in modern theoretical RL, and the hybrid-bandit-feedback open problem from [LWZ25] is a specific, well-motivated target.
*Are claims well supported:* Mostly. The body presentation of the headline hybrid result is too thin; the strict-improvement claim is supported only via toy bandit. The other claims (Theorem 13, the estimator improvements, the √T result for Bellman-complete) are well supported.
*Soundness of analysis:* The framework analysis (mirror-descent / Bregman argument around Eq. (5)–(6)), Theorem 13, and the estimator constructions look careful and correct insofar as the body permits verification.
*Clarity of writing:* Mixed. The framework section (§4) is clean. §5.2 is essentially a placeholder pointing to an appendix, which is the major presentation flaw.
*Value to the research community:* Substantial — the mirror-descent-style generalization of AIR and the Dig-DEC complexity measure are likely to be picked up by follow-up work.

## Anchor papers retrieved

| Path | Avg | Round | Relation to paper |
|---|---|---|---|
| `lFzUHGebeb.md` | 2.00 | 1 (weak) | Online linear regression, not relevant — used only as low-band marker. |
| `5s1qpjrNvZ.md` | 3.00 | 1 (weak) | Empirical RL, not theoretical — low-band marker. |
| `L143pPpIHv.md` | 3.00 | 1 (weak) | PAC-MDP, weak paper — low-band marker. |
| `EWKPEtwjTy.md` | 2.50 | 1 (weak) | Discrete actor/critic, irrelevant. |
| `aPNwsJgnZJ.md` | 6.00 | 1+2 (mid) | **Read in full.** Horizon-free adversarial linear mixture MDPs; first algorithm for the setting; closest topical match. Dig-DEC is broader (multiple settings, bandit feedback, resolves open problem) and at least as deep. |
| `eUEMjwh5wK.md` | 6.00 | 1 (mid) | Adversarial RL but applied/empirical — less relevant. |
| `5e0yWSNGIc.md` | 5.33 | 1 (mid) | Certified training in RL — empirical, not relevant. |
| `sQYQ9i1g86.md` | 5.00 | 1 (mid) | Offline RL game-theoretic; weaker theory than Dig-DEC. |
| `5t57omGVMw.md` | 8.00 | 1 (strong) | Online learning for solver parameters — different area but mathematically tight. Dig-DEC is below this in clarity/exposition. |
| `stUKwWBuBm.md` | 8.00 | 1 (strong) | Multi-agent RL via behavioral economics — different area. |
| `9pW2J49flQ.md` | 8.00 | 1 (strong) | DeepLTL — empirical, irrelevant. |
| `8BAkNCqpGW.md` | 8.00 | 1 (strong) | **Read in full.** Policy gradient for confounded POMDPs, first-of-its-kind theory paper. Dig-DEC has comparable conceptual depth but worse body-level presentation. |
| `S24zdyiWDT.md` | 6.00 | 2 (mid-low) | IRL hardness — theoretical RL, slightly lighter framework contribution than Dig-DEC. |
| `Yx7TnC6AAp.md` | 5.75 | 2 (mid-low) | Imperfect-info games with linear FA — similar style, slightly narrower than Dig-DEC. |
| `OmFlDvsvc3.md` | 6.00 | 2 (mid-low) | Reward learning regret mismatch — different setting. |
| `RMgqvQGTwH.md` | 7.00 | 2 (mid-high) | Offline-enhanced on-policy PG — hybrid RL theory with best-of-both-worlds; comparable depth and broader empirical bridge than Dig-DEC. |
| `txD9llAYn9.md` | 7.00 | 2 (mid-high) | **Read in full.** Minimalist model-based RL with horizon-free / second-order bounds; comparable depth to Dig-DEC and cleaner body presentation. Dig-DEC narrowly below due to §5.2 thinness. |
| `eJ0dzPJq1F.md` | 7.25 | 2 (mid-high) | Imitation+RL blending; less topically aligned. |
| `DFTHW0MyiW.md` | 7.00 | 2 (mid-high) | Robust RL with adaptive defense; less aligned. |

**Round 1 bracket:** (5.5, 7.5) — clearly above the weak anchors (all empirical/weak-theory, ≤ 3.0) and below the 8.0 anchors (more polished theoretical contributions); comparable to the 6.0–7.0 cluster of theoretical RL papers.

**Round 2 narrowing:** Dig-DEC clearly **exceeds** aPNwsJgnZJ (6.0) in scope (multiple settings, bandit feedback, multiple rate improvements, framework generalization) and resolves a named open problem. It is **comparable to** txD9llAYn9 (7.0) in technical depth but with worse body-level presentation of the headline hybrid-bandit result. That places it slightly below 7.0 and clearly above 6.0 — **6.5**.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>