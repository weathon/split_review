Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper revisits the multi-play multi-armed bandit with shareable arm capacities (MP-MAB-SAC) problem under a new reward model where reward variance does not scale with the number of plays. It makes three contributions: (1) a tight sample-complexity lower bound Ω(σ²/μₖ² log δ⁻¹) for learning arm capacities, matched by algorithm ActInfCap — closing a gap from prior work; (2) the first instance-independent regret lower bound Ω(σ√(TK)) and a strengthened instance-dependent lower bound Ω(∑ cσ²/μₖ² log T); (3) an algorithm PC-CapUL with both instance-dependent and instance-independent regret upper bounds. The paper is primarily theoretical with a brief experimental section.

## Strengths

- **Sample complexity gap genuinely closed.** Theorem 1 proves a minmax lower bound Ω(σ²/μₖ² log δ⁻¹) for learning a single arm's capacity, and Theorem 2 shows ActInfCap matches this bound exactly. This eliminates the gap in Wang et al. (2022a), whose lower bound was the trivial Ω(log δ⁻¹) and upper bound was O(mₖ²σ²/μₖ² log δ⁻¹). This is a clean, self-contained result.

- **First instance-independent regret lower bound.** Theorem 3 establishes Ω(σ√(TK)) for any learning algorithm. This result was absent from prior work and provides meaningful scaling guidance for algorithm design in this setting.

- **Strengthened instance-dependent regret lower bound.** Theorem 4 gives Ω(∑ cσ²/μₖ² log T), replacing Wang et al.'s trivial Ω(∑ log T) lower bound. The dependence on μₖ⁻² is non-trivial and intuitively correct.

- **Novel algorithmic principles with provable guarantees.** Algorithm 2 (PC-CapUL) introduces four heuristics (preventing excessive UE, balancing UE/IE, favoring larger-mean arms, stopping on convergence) that together achieve the first instance-independent regret upper bound for this setting. The comparison against the prior Orch baseline in Figure 1 shows substantial empirical improvement.

## Weaknesses

### Fatal
None.

### Major

- **The claim that the regret upper bounds "match" the lower bounds is significantly overstated.** The instance-dependent lower bound (Theorem 4) is Ω(∑ cσ²/μₖ² log T) — with **no dependence on capacities mₖ**. The instance-dependent upper bound (Theorem 5) contains terms like Σₖ ((Σᵢ 2304σ²mᵢ²/μᵢ² log T)(μₖ−c)mₖ) where mₖ appears quadratically. Similarly, the instance-independent lower bound (Theorem 3) is Ω(σ√(TK)) while the upper bound (Theorem 6) scales as σ√((9216M³+128KM+1152M²N)M T log T) where M = Σ mₖ — dramatically larger when capacities are non-uniform. These are not constant-factor gaps; they are structural differences in parameter dependence. The repeated claim of "matching up to acceptable model-dependent factors" is misleading and would need to be replaced by an honest characterization of the gap and its sources. This is the paper's most consequential flaw because it undermines the central narrative. *(Verified: compare Theorem 3/4 vs Theorem 5/6 in the paper.)*

- **The motivation regarding "closing the gap of Wang et al." is misleading because the reward model is changed.** The paper changes from Wang et al.'s reward model (1) (where variance scales with min{aₖ, mₖ}²) to (5) (where variance is independent of the number of plays). The sample complexity and regret results are derived under model (5). While the paper does state the model change explicitly, it then claims to "close the gap" of Wang et al. as if the comparison were apples-to-apples. The gap closed is under a different, arguably harder model. The paper never compares results under the same model, weakening the claimed significance. *(Verified: paper states both models (1) and (5) in Section 1, and acknowledges the model is "harder," but the narrative framing still implies a direct improvement.)*

### Minor

- **Experimental evaluation is too narrow for a paper claiming practical relevance.** Only one baseline from prior work (Orch) is compared against; the third baseline "MP-SE-SA" is introduced without any citation or description of what it is. No error bars or multiple-seed runs are reported — the single regret curves in Figure 1 cannot be assessed for variance. No ablation study isolates the effect of the four claimed design principles. The movement cost c is mentioned as varied (0.2, 0.1, 0.01) but no results for different c values are shown. The paper is primarily theoretical, so these are not fatal, but they limit the confidence readers can place in the algorithm's practical efficiency. *(Verified: Section 6 — only one figure shown, no error bars, MP-SE-SA undefined.)*

- **The role of the movement cost c is underdeveloped.** The constant movement cost c is introduced in the model (Section 3) and appears in the instance-dependent lower bound (Theorem 4), but its effect on the optimal allocation, the algorithm's decisions, and the upper bounds is not systematically analyzed. The experiments mention varying c but do not present results. *(Verified: c appears in model definition and Theorem 4, but the paper does not analyze how it affects the algorithm or optimal strategy.)*

- **Lemma 5 is referenced multiple times but its statement does not appear in the main text.** The algorithm's design principles are repeatedly justified by "the insight from Lemma 5" (in the description of PC-CapUL), but Lemma 5 is not stated in the main body. This makes the algorithmic rationale hard to follow for a reader limited to the main text. *(Verified: Lemma 5 referenced on lines 43 and 238 but not stated in the visible text. Per policy this would be in the appendix, but the algorithm description relies on it.)*

### Trivial

- The baseline "MP-SE-SA" is mentioned without any citation or description, leaving the reader to guess what it is.
- The paper says "match the lower bounds" in both the abstract and introduction without acknowledging the structural gap — this should be corrected in any revision.

## Nice-to-Haves

- An ablation study isolating the four design principles of PC-CapUL (removing the prioritization rule, removing the stop-learning condition, etc.) would substantially strengthen the empirical validation.
- Error bars or multiple runs for Figure 1 would allow readers to assess the variability of the regret curves.
- A systematic experimental study varying the movement cost c would help validate its role in the lower bounds.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Missing initialization of mₖ,₀ˡ, mₖ,₀ᵘ in Algorithm 1"** — REMOVED because it is factually wrong. Algorithm 1 line 1 clearly states: "Initialize: t←0, mₖ,₀ˡ←1, mₖ,₀ᵘ←N." *(Verified on line 191.)*
- **"No appendix with proofs / missing proofs"** — REMOVED per policy. The parser strips appendix content from all papers; the original submission contains these proofs (Lemma 5 and full theorem proofs are referenced in-text).
- **"Figures not embedded in the text"** — REMOVED as a parser/formatting artifact.
- **"Typos, grammar, formatting issues"** — REMOVED per policy as parser artifacts, not author errors.
- **"Missing comparison to uniform allocation, epsilon-greedy, etc."** — REMOVED. The paper already compares against three baselines including one from prior work (Orch) and a variant (PC-CapUL-old). For a primarily theoretical paper, this is adequate. Adding more naive baselines would not change the evaluation.
- **Strength Finder's claim that "upper bounds match the lower bounds"** — REMOVED per conflict rule: this strength conflicts with the verified weakness that the bounds do not actually match (structural gap in capacity dependence). The strength is inaccurate.

## Novel Insights

The most interesting observation emerging from the reviews — beyond what the paper itself states — is that the sample complexity result (Theorem 1/2) is the paper's cleanest contribution and stands on its own, while the regret upper bounds are a separate (and much looser) story. The structural gap between the lower bounds (which are capacity-independent) and the upper bounds (which carry mₖ² terms) suggests either that the lower bounds can be strengthened substantially, or that the algorithm is far from optimal. A reader should treat the regret analysis as providing an upper bound on the algorithm's performance, not as a fundamental limit that is tight. The paper would benefit from contrasting the tightness of the sample complexity result with the acknowledged looseness of the regret bounds, and from discussing which direction (tightening the lower bound or improving the algorithm) is more plausible.

## Suggestions

1. **Honestly characterize the gap between upper and lower regret bounds.** Remove or qualify all claims of "matching." Explicitly state the residual gap (mₖ dependence in the upper bound vs. no mₖ in the lower bound) and discuss whether the lower bound or the algorithm is likely to be the source of looseness. This is the single most important change.

2. **Clarify the relationship to Wang et al.'s model.** Make explicit that the sample complexity gap is closed under a different (harder) reward model, and describe what this implies about the comparison. Consider adding a short discussion of how results would change under the original model (1).

3. **Expand the experimental section.** Add at least error bars or multiple runs. If possible, add an ablation showing the impact of one design principle (e.g., the "favorable arms win UE first" priority rule). Show results for at least one non-default value of c.

4. **Define or cite MP-SE-SA.** The reader needs to know what this baseline is.

5. **Move a key lemma to the main text.** Since Lemma 5 is used to justify the algorithm's design principles, its statement (if not its full proof) should appear in the main body.

## Score and Decision

This paper has genuine technical contributions — most notably the tight sample complexity result and the first instance-independent regret lower bound. However, the central narrative of "matching regret bounds" is not supported, and this overclaiming pervades the abstract and introduction. The paper can be repaired with a candid revision, but in its current form, the main claim does not hold. I cannot recommend acceptance.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>