Now I have a thorough understanding of the paper and can produce the consolidated review.

## Summary

This paper revisits the multi-play multi-armed bandit with shareable arm capacities (MP-MAB-SAC) problem, but with a modified reward model that removes capacity information from the reward variance (constant-variance noise instead of Wang et al.'s variance-scaling noise). The paper makes three contributions: (1) a sample complexity lower bound Ω(σ²/μ²_k log δ⁻¹) for learning arm capacities and an algorithm (ActInfCap) that matches it, closing the gap left by Wang et al. (2022a) — albeit under a different reward model; (2) new instance-independent (Ω(σ√(TK))) and instance-dependent (Ω(∑ cσ²/μ²_k log T)) regret lower bounds; (3) an algorithm (PC-CapUL) with regret upper bounds claimed to match these lower bounds "up to acceptable model-dependent factors."

## Strengths

1. **Clean sample complexity matching under the new model.** Theorem 1 proves a minmax lower bound Ω(σ²/μ²_k log δ⁻¹) for learning arm capacity, and Algorithm 1 (ActInfCap) provably matches it (Theorem 2) up to a universal constant factor. The lower bound is independent of m_k, which is a genuine improvement over the prior art's trivial lower bound of Ω(log δ⁻¹). *(Abstract lines 6–7, Section 4)*

2. **First instance-independent regret lower bound for this problem family.** Theorem 3 provides a minmax lower bound Ω(σ√(TK)), which was absent in prior work (Wang et al. 2022a had no such result). Theorem 4 strengthens the instance-dependent regret lower bound from Ω(∑ log T) to Ω(∑ cσ²/μ²_k log T), providing meaningful dependence on μ_k. *(Section 5.1, Theorems 3–4)*

3. **Novel confidence intervals and principled algorithm design.** Lemma 1–2 derive tighter confidence intervals for the new constant-variance reward model by moving the UE estimation error term above the denominator (rather than in it, as in Wang et al.). The PC-CapUL algorithm's four design principles (preventing excessive UE, balancing UE/IE, favoring high-μ arms, stopping on convergence) are each grounded in formal analysis. *(Section 4.2, Section 5.2; Lemmas 1–2)*

## Weaknesses

### Fatal
None.

### Major

1. **The paper claims to "close the sample complexity gap of Wang et al. (2022a)" but this is achieved under a different reward model.** Wang et al.'s reward function was R_k(a_k) = min{a_k, m_k}(μ_k + ε_k) where variance scales with (min{a_k, m_k})². This paper replaces it with R_k(a_k) = min{a_k, m_k}μ_k + ε_k, which has constant variance σ². All lower bounds and algorithms are derived for this new model, and no results are provided for Wang et al.'s original model. The abstract, introduction, and conclusion repeatedly claim to "close the sample complexity gap" and "strengthen the regret lower bound" of Wang et al., but these are apples-to-oranges comparisons. While the paper is transparent about proposing a new reward function (lines 25–28), it never delineates which claimed contributions hold for the original model versus the new one. The framing is misleading: the paper should say "Under our new (more fundamental) reward model, we prove bounds that are tighter than those Wang et al. obtained under their (easier in some respects) model," not "we close the gap of Wang et al." *(Abstract lines 6–7, Section 1 lines 25–31, Section 1.1 line 39, Section 7 line 375)*

2. **The regret upper bounds do not match the lower bounds in important parameter dependencies, undercutting the "matching" claim.** The instance-dependent upper bound (Theorem 5) scales with m²_k, while the instance-dependent lower bound (Theorem 4) has no m_k dependence at all. The instance-independent upper bound (Theorem 6) scales like √(M⁵ T log T) where M = ∑ m_k, while the instance-independent lower bound (Theorem 3) is σ√(TK) — independent of M. The paper dismisses these gaps as "acceptable model-dependent factors," but m²_k and M^{5/2} can be arbitrarily large relative to the lower bound expressions. The claim that the bounds "match" is not supported; the upper bounds are substantially looser. *(Theorems 3–6 and their remarks)*

3. **The experimental evaluation is insufficient to support the algorithmic claims.** Only one experiment (varying K) is described in detail. No error bars, confidence intervals, or multiple-seed results are reported. The actual regret values are given only as vague qualitative descriptions ("converges to around 4×10⁵"). Three baselines are listed (MP-SE-SA, Orch, PC-CapUL-old) but only two are discussed in the results. No ablation studies test the individual contributions of the four design principles of PC-CapUL. The experiments do not systematically vary N, c, or μ_k despite listing these in the setup. *(Section 6, especially lines 362–365)*

### Minor

1. **The sample complexity metric in Section 4 (number of actions on a single arm) is not clearly connected to the regret objective.** The lower bound is stated in terms of the number of inference rounds t, but ActInfCap can use many plays per round (e.g., a_{k,t} = m^u_{k,t-1} which could be as large as N). The sample complexity analysis does not account for the cost (in plays/regret) of each action. The paper never explains how sample complexity in actions translates to the regret bounds in Section 5. *(Section 4, Theorem 1–2)*

2. **The instance-dependent regret upper bound (Theorem 5) contains very large numerical constants (2304, 1152, 9216), suggesting a loose analysis.** Combined with the m²_k and M^{5/2} dependencies, this makes the bound far from tight and gives little practical guidance. *(Theorem 5, Theorem 6)*

3. **Several algorithmic design choices lack rigorous justification.** The alternating UCB/LCB schedule in ActInfCap (Algorithm 1) is presented without argument for why it is optimal or necessary. The "favorable arms win UE first" heuristic in PC-CapUL is motivated by intuition but the proof that it is optimal is not provided. *(Algorithm 1, Section 5.2 design principles)*

4. **Theorem 2's sample complexity guarantee depends on an unspecified universal constant ξ**, making the result non-quantitative. While common in theory papers, this undermines the "exact matching" claim somewhat. *(Theorem 2, line 212)*

### Trivial

1. The phrase "four folds" (lines 43, 238) appears to be a non-standard usage; "four aspects" or "four components" would be clearer.

## Nice-to-Haves

- Compare PC-CapUL against a natural UCB-based adaptation (e.g., treating each arm as having an unknown effective capacity and applying UCB on per-play reward).
- Report regret curves with error bars over multiple random seeds.
- Provide an ablation study separating the four design principles of PC-CapUL.
- Include a small-scale case study (e.g., K=3) where the evolution of UCB/LCB and the per-arm exploration counts can be visualized.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **Claim that Theorem 1's Le Cam proof is "not provided"** — The paper states the proof uses "Le Cam's method with a careful tracking of the number of UEs" (line 114). The full proof is deferred to the appendix, which is standard. The parser strips appendices; this is not a paper flaw.

2. **Claim about Line 11 condition being "the opposite" of the stated goal** — The reviewer says "Line 11 condition τ̂ ≤ ι̂ is about preventing excessive UEs, but the condition is the opposite." The condition τ̂ ≤ ι̂ correctly sets w_k=1 (do IE) when IE count ≤ UE count, which implements the stated goal of preventing excessive UEs. The condition is not wrong; the reviewer misunderstood the algorithm.

3. **Claim that "no standard bandit algorithms (UCB1, Thompson sampling)" are included** — The paper addresses a specialized bandit setting (MP-MAB-SAC with scarce capacities, constant-variance rewards, and movement cost). Standard UCB1/TS are not directly applicable without non-trivial adaptation, and three baselines (MP-SE-SA, Orch, PC-CapUL-old) are included. This is scope creep.

4. **Claim about "missing appendix" content** — The paper's proofs are in the Appendix which was stripped by the parser. Criticizing their absence is invalid.

5. **Claim that the paper does not discuss why variance is constant** — The paper explicitly motivates this choice at lines 25–31: "reduce the capacity information in the reward to the minimum such that only the reward mean contains the capacity information... finds its root in the reward model of conventional linear bandits."

## Novel Insights

Beyond the paper's own contributions, the reviews surface a key structural tension: the paper's claimed "matching" has two different senses that are conflated. The sample complexity results genuinely match (Section 4 is clean). The regret bounds do not — the upper bounds carry m²_k and M^{5/2} dependencies entirely absent from the lower bounds. This suggests either (a) the lower bounds are not tight for this problem, or (b) the upper bound analysis is loose in ways that could be tightened. The paper's rhetoric treats both as "matching up to model-dependent factors," but a factor that can be arbitrarily large (like m²_k relative to a lower bound with no m_k dependence) is not a cosmetic gap — it reflects an incomplete understanding of the problem's fundamental difficulty. Separately, the model-change issue reveals that the paper's strongest claim (closing the prior gap) rests on a cross-model comparison that is not apples-to-apples: the paper proves a better sample complexity rate in a harder model (constant-variance) than Wang et al. proved in an easier model (variance reveals capacity), which is interesting but not equivalent to "closing the gap" in the original problem.

## Suggestions

1. **Reframe the paper honestly.** Distinguish clearly between contributions that close gaps in the *original* Wang et al. model (none — the paper provides no results for that model) and contributions for the *new* constant-variance model. State: "Under a new reward model that isolates capacity information in the mean, we prove tighter bounds than prior work achieved under the original model."

2. **Tighten the regret upper bounds or prove matching lower bounds.** The m²_k and M^{5/2} factors in the upper bounds need to be reconciled with the m_k-free lower bounds. Either remove the "matching" claim, prove that these dependencies are unavoidable (new lower bounds), or tighten the analysis.

3. **Strengthen the experimental section.** Add error bars, multiple seeds, and systematic variation of N, c, and μ_k. Include at least one ablation study testing the design principles. Provide a table of numerical regret values for concrete comparison.

## Score and Decision

The paper contains genuine technical contributions: tighter confidence intervals, a novel sample complexity lower bound that is matched by ActInfCap, and new regret lower bounds. However, the framing is misleading (claiming to close gaps from prior work while changing the problem definition), the regret upper bounds do not match the lower bounds in meaningful ways, and the experimental validation is thin. The paper's value is in its analysis of the constant-variance model, not in "closing" previously open problems. With honest reframing and tightened bounds, this could be a solid paper.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>