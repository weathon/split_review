Now I have a thorough understanding of the paper and the reviewer claims. Let me produce the final consolidated review.

---

## Summary

This paper studies learning from imperfect human feedback by modeling it as a continuous-action dueling bandit with agnostic corruption on utilities. The paper claims: (1) a lower bound of Ω(d max{√T, T^ρ}) for learning from a ρ-imperfect user, (2) that this bound is tight, (3) an efficiency-robustness tradeoff for DBGD (regret O(√d T^{1-α} + √d T^α C) under arbitrary corruption), and (4) the first tight lower bound for standard DBGD (Ω(T^{3/4})). The key technical tool is a regret decomposition lemma for dueling feedback.

## Strengths

1. **First corruption-robust dueling bandit result for continuous action spaces.** Prior work (di2024nearly, saha22a, komiyama2015regret) is restricted to finite action sets; the paper explicitly identifies this gap and addresses it. (Section 1, paragraph 3: "ours is the first to investigate a robust dueling bandit algorithm under corruption for continuous action space.")

2. **Novel regret decomposition lemma for dueling feedback under corruption.** Lemma 3 (line 155–159) decomposes dueling regret into "regret of decision" and "observation error" (bias from corruption). The paper correctly notes that prior decompositions (foster2023statistical) relied on an online estimation oracle that cannot be constructed under agnostic corruption with dueling feedback. This lemma is used to control the impact of corruption on gradient estimates and is likely to be of independent interest.

3. **Explicit tradeoff result for DBGD.** Theorem 2 (line 140–142) shows that by tuning the exploration radius δ ∝ T^{-α}, DBGD achieves regret O(√d T^{1-α} + √d T^α C) for any α ∈ (0, 1/4], smoothly interpolating between efficient-but-fragile (α=1/4) and robust-but-inefficient (α→0). While the tradeoff conceptually resembles bias-variance tradeoffs, its instantiation for gradient-based dueling bandits under corruption is novel.

4. **First tight lower bound specifically for DBGD.** Corollary 1 (line 174–176) identifies that standard DBGD (α=1/4) suffers Ω(T^{3/4}) regret. This had remained open despite extensive study, and the parallel-world argument is conceptually interesting.

## Weaknesses

### Fatal

1. **Lemma B1 (bandit-to-dueling regret conversion) is invalid, undermining all lower bound claims.** The proof of Lemma B1 (lines 282–312) constructs algorithms L₀ and L₁ that receive dueling/comparison feedback and claims that the bandit reward lower bound applies to them. The bandit reward lower bound (Shamir 2013, Lattimore–Szepesvári 2020) is proven for algorithms that observe scalar reward feedback μ(a_t) + noise. The constructed Lᵢ only observes a binary comparison outcome between a_{0,t} and a_{1,t} — a fundamentally different and less informative feedback signal. The proof asserts "we know all algorithm with bandit feedback with utility function μ has to occur regret at least \overline{Reg}" but Lᵢ is never shown to be an algorithm that *receives bandit reward feedback*. There is no argument connecting comparison outcomes to reward observations. Since Theorem 1 and Proposition 1 both rely on Lemma B1 to convert their bandit reward lower bounds into dueling lower bounds, these core lower bound results are unsubstantiated. This is not a matter of insufficient detail — it is a logical gap that would require an entirely different argument to fix.

### Major

2. **The DBGD lower bound proof (Corollary 1) is not rigorously established.** The proof (lines 590–598) is a short, informal argument that relies on a parallel-world construction with several unverified steps: (a) the claim that a₂ is proposed at most 8c₀ T^{3/4−ε} times follows from a constant-per-pull regret lower bound that is not formally justified for this setting; (b) the indistinguishability argument between the two problem instances under stochastic feedback is asserted without a formal coupling or a proper information-theoretic argument; (c) the budget calculation for the adversary (C = 2c₀ T^{3/4−ε}) and the claim that this enables corrupting exactly 8c₀ T^{3/4−ε} pulls is not fully derived. For the first claimed tight lower bound for a well-studied algorithm, the standard of proof must be higher. The proof sketch as presented does not constitute a complete argument.

3. **The paper's upper bounds (Theorems 2, NC-SMD proposition) address arbitrary corruption while the matching lower bounds (Theorem 1) address the strictly weaker ρ-imperfect setting with known ρ.** This asymmetry means the claim that the upper bounds are "tight" or "near-optimal" for the arbitrary corruption setting is unsupported. The paper acknowledges this distinction (lines 64–66: "our lower bound... will hold even in the weaker ρ-imperfect user feedback") but the overall significance is weakened by the fact that no lower bound is provided for the setting in which the general upper bounds operate.

### Minor

4. **The regret decomposition lemma (Lemma 3), while novel for dueling feedback, follows the structural template of Foster et al. 2023.** The paper acknowledges this inspiration (line 144), but the framing slightly overstates the novelty. The key challenge is adapting it to the sparser dueling feedback, which is non-trivial but more incremental than a completely new conceptual framework.

5. **Experiments are limited in scope and baselines.** The synthetic experiments use d=5 with 5 seeds per setting; the Spotify experiment uses a discrete subsample with only 100 iterations for the Versatile-DB comparison. The baselines Doubler and Sparring are not designed for corruption robustness, making the comparison less informative. These experiments support the theory but do not constitute extensive empirical validation.

### Trivial

6. The paper contains two different abstracts (lines 3–6 and lines 1053–1055) where the second mentions an algorithm name "RoSMID" that does not appear in the body. This appears to be an editing artifact from an earlier draft that was not cleaned up.

## Nice-to-Haves

- A formal information-theoretic lower bound proof for dueling feedback directly (without going through bandit reward feedback) would validate the paper's main claims and is likely the correct way to fix the fatal issue.
- Stronger baselines designed for corruption (beyond Doubler and Sparring) and larger-scale experiments would strengthen the empirical evaluation.

## Removed Points

- **"Efficiency-robustness tradeoff is a routine exercise / standard bias-variance tradeoff"** (Harsh Critic). The paper is transparent that the algorithmic techniques are not new (line 121: "The key novelty in our results is not about the development of fundamentally new algorithmic techniques") and the tradeoff instantiation for dueling bandits is genuinely novel. REMOVED — overstates the case and ignores the paper's own framing.
- **"Two different abstracts signal lack of care in presentation"** (Harsh Critic). The parser extracts text from PDFs and can introduce artifacts; this is a known issue with PDF extraction. The substantive content concern is noted but the character judgment is removed. DEMOTED to Trivial.
- **"Experiments compare against inappropriate baselines"** (Harsh Critic). Doubler and Sparring are standard dueling bandit baselines used in the literature. The claim that they are "not designed for corruption" is true, but the paper is transparent about this (line 191, 201). The comparison with Versatile-DB (a corruption-robust baseline) is provided in the appendix. REMOVED — the paper reasonably acknowledges the baseline limitations.
- **"The paper's main theoretical results are undermined"** (Harsh Critic's conclusion). Only partially true — the upper bounds and tradeoff results are not undermined by the Lemma B1 issue. RETAINED as separate items (Weaknesses 1, 2, 3) with proper calibration.
- **Several strengths from the Strength Finder** were too generic or sycophantic ("superior empirical performance over Versatile-DB" — only for T=100 iterations with very limited compute; "experimental validation on real-world data" — the Spotify experiment is quite small). These are dropped or demoted.

## Novel Insights

The key novel analytic insight that emerges from the reviews (beyond the paper's own statements) is that the paper's Lemma B1 attempted a reduction that is not justified: converting bandit reward lower bounds to dueling lower bounds by treating a dueling algorithm's output actions as a bandit algorithm's decisions. This overlooks the fundamental difference in feedback structure — comparisons versus scalar rewards — which is exactly the modeling choice the paper itself argues is important. The tradeoff analysis for DBGD (Theorem 2) and the decomposition lemma (Lemma 3) are genuinely useful contributions that do not depend on this reduction, and they could form the core of a stronger paper if restructured around direct dueling lower bounds.

## Suggestions

1. Remove or replace Lemma B1 with a proper information-theoretic lower bound that directly operates on dueling/comparison feedback without requiring a bandit reward intermediate step.
2. Formalize the DBGD lower bound proof (Corollary 1) with a complete coupling argument and explicit budget accounting.
3. Restructure the paper's narrative to clearly separate the validated contributions (upper bounds, tradeoffs, DBGD lower bound) from the unsubstantiated ones (general lower bound via Lemma B1).
4. Add confidence intervals or more runs to the experiments, and include additional corruption-robust baselines where feasible.

## Score and Decision

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>