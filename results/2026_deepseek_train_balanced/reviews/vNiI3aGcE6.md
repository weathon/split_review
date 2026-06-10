## Summary

This paper proposes ME-Nash-QL, a self-play algorithm for two-player zero-sum Markov games (TZMG) that aims to simultaneously optimize space, sample, and computational complexity while outputting a Markov Nash policy. The paper claims O(SABH) space complexity (the information-theoretic minimum for storing Q-values), Õ(H⁴SAB/ε²) sample complexity, O(T·poly(AB)) computational complexity, and a burn-in cost of Õ(SAB·H¹⁰). The contributions are positioned against prior work — particularly Nash-VI (model-based, O(S²ABH) space, O(T·poly(SAB)) compute) and V-learning (model-free, non-Markov policy, O(H⁶) sample dependence) — as achieving the best space and computational complexity while matching the best sample complexity rate and improving burn-in under S > H³.

---

## Strengths

- **Information-theoretically minimal space complexity O(SABH).** The paper shows ME-Nash-QL requires only the storage of Q-values themselves, achieving O(SABH) space — the minimum possible in tabular cases. This improves on Nash-VI (O(S²ABH)), V-learning (O(S(A+B)T)), OMNI-VI (O(S²A²B²T)), and PReBO (O(SABHT)). This is a clear and verifiable theoretical advance.

- **Computational complexity O(T·poly(AB)), eliminating the S factor from per-episode computation.** The paper demonstrates that each episode's policy improvement reduces to a CCE computation solvable by linear programming in O(poly(AB)) time, yielding total O(T·poly(AB)) computation. This improves on Nash-VI (O(T·poly(SAB))) by removing dependence on S.

- **Outputs a single Markov and Nash policy, unlike prior model-free algorithms.** The paper explicitly contrasts with V-learning (non-Markov output) and Nash V/Q-Learning (nested mixture of Markov policies). ME-Nash-QL is identified as the first model-free TZMG algorithm that simultaneously outputs a Markov policy and a Nash policy, achieved through a single output policy extracted via the smallest optimism-pessimism gap (Theorem 2).

- **Better burn-in cost than Nash-VI under the S > H³ regime.** The paper proves burn-in cost Õ(SAB·H¹⁰) versus Nash-VI's Õ(S³ABH⁴), a factor of S² improvement. For large state spaces where S ≫ H³ — such as Go (S = 2³⁶¹, H between 150–722) — this is a meaningful improvement over the only prior algorithm with matching asymptotic sample complexity.

---

## Weaknesses

### Major

- **The simplified Õ(H⁴SAB/ε²) sample complexity hides an unacknowledged parameter regime.** Theorem 1 gives T ≥ C₀(H⁴SAB/ε² · log⁴(...) + H⁷SAB/ε · log³(...)). The paper presents Õ(H⁴SAB/ε²) as the unqualified sample complexity (abstract, introduction, conclusion). However, the first (1/ε²) term dominates the second (1/ε) term only when ε ≪ 1/H³. For H = 10 this is ε ≪ 0.001; for H = 100 it is ε ≪ 10⁻⁶. The paper does not acknowledge this condition, let alone discuss its restrictiveness. The burn-in cost of Õ(SAB·H¹⁰) is similarly astronomical — H¹⁰ = 10¹⁰ for H = 10 — yet is presented as an unqualified improvement. These numbers are not contextualized against the regimes in which they would actually govern the bound. This is not fatal (the bound is technically correct) but it is a significant omission that affects how the headline claim should be interpreted.

- **Key algorithmic innovations are named but not explained in the main text.** The paper claims two technical innovations: "reference-advantage decomposition technique" (borrowed from single-agent RL and applied to TZMG) and an "innovative early-settlement approach." Neither is actually described:
  - "Early-settlement method" appears only twice (lines 29, 123) plus one reference to "perform updates of reference values under the early settlement" (line 126). What it does, how it works, and why it is innovative are not stated.
  - The combination step referenced as "lines 11–12 in Algorithm 1" (line 136) — which describes how Q̅ and Q̲ are formed from Q̅^R, Q̲^R, Q^UCB, Q^LCB — is unintelligible without the algorithm listing. While the detailed pseudocode was in the appendix (stripped by the parser), the main text should nevertheless give enough conceptual description for a reader to understand what the algorithm is doing. Currently it does not.

### Minor

- **The multi-player general-sum extension (Theorem 3) is a placeholder, not a contribution.** The extension is described in a single sentence (line 33) plus a theorem statement (line 173). No algorithm modifications, no explanation of how the two-player techniques generalize, and the resulting bound (Õ(H⁴S∏Aᵢ/ε²)) has explicit exponential dependence on the number of players — this is the curse of multi-agent, not a solution to it. This section adds no technical content and reads as an attempt to claim generality without doing the work.

- **The connection between CCE computation and the algorithm is not explained.** The paper states that computational complexity is O(T·poly(AB)) "due to the CCE computation by linear programming" (line 175). CCE is mentioned in the related work (Feng et al., 2023) and cited as the source of the computational bound, but the algorithm description in Section 3.1 never mentions CCE or explains how CCE computation enters the policy improvement step. A reader cannot tell how the algorithmic structure connects to the complexity claim.

- **Burn-in cost comparison is framed as a clear win without acknowledging regime dependence.** The paper states its burn-in cost Õ(SAB·H¹⁰) beats Nash-VI's Õ(S³ABH⁴) and gives the Go example (S > H³) to illustrate. This is correct in that regime. But the paper does not explicitly state "ME-Nash-QL has lower burn-in cost than Nash-VI when S > H³; otherwise Nash-VI's burn-in may be smaller." The comparison is presented as unconditional superiority (abstract: "best burn-in cost"), which is imprecise. The regime S > H³ is reasonable but the paper should own the condition transparently.

### Trivial

None beyond normal parser artifacts.

---

## Nice-to-Haves

- Clarify whether the estimated transition probabilities in Eq. (11) are stored as a full tensor or computed from individual samples. The paper says "stochastic estimate" (line 134), suggesting the latter, but also calls P̂ "the estimate of P" — the ambiguity could be resolved with one sentence.
- The comparison with Nash-VI on burn-in cost could include a simple numerical example in the regime S > H³ to illustrate when ME-Nash-QL wins, alongside a caveat about when it does not.

---

## Removed Points

These points were raised by reviewers but removed after verification against the paper.

- **"Model-free claim contradicted by P̂ in Eq. (11)"**: The paper explicitly states that P̂(V̅ − V̅^R) is the "stochastic estimate" (line 134) — i.e., a single-sample estimate, consistent with model-free operation. The critic's interpretation that a stored transition tensor is required is not supported by the paper's own description. Removed as factually incorrect.

- **"Analysis section is empty"**: Section 4 is short (four lines of notation definitions) because the full proof is deferred to the appendix, which is standard for theory papers at this venue. The appendix was stripped by the parser. Removed as a parser artifact issue.

- **"Reward r_h(s,a) in Eq. (11) missing action b"**: Likely a parser formatting artifact from PDF extraction; the paper defines r_h(s,a,b) in Section 2. Removed per formatting-artifact rule.

- **"Sample complexity used ambiguously"**: The paper defines regret (Def. 2) and sample complexity (line 101) explicitly and states their relationship. The critic's claim is not supported. Removed as incorrect.

- **"Algorithm description makes paper unreadable as standalone document"** (framed as fatal): While the main text description is thin, the full pseudocode was in the appendix (stripped by parser). The retained weakness above ("key innovations not explained in main text") captures the real issue without overstating it. The fatal framing is removed; the substantive concern is preserved under Major.

- **Several strengths from the Strength Finder were removed as generic or unsupported**: "Sample complexity superior to V-learning for long horizons" — this is a real comparison but is a direct restatement of the paper's own claim without additional insight. The core strengths (space, compute, policy quality, burn-in) are retained.

---

## Novel Insights

None beyond the paper's own contributions. The reviewer inputs do not surface an insight about the paper that the paper itself does not articulate.

---

## Suggestions

1. **Add a prose explanation of the early-settlement method and reference-advantage decomposition in the main text** — at minimum, describe the conceptual purpose of each, even if the update equations remain in the appendix. Currently these are named but not explained.

2. **State the regime condition for the simplified sample complexity explicitly.** Add a remark such as: "When ε ≤ c/H³ for a universal constant c, the first term dominates and the bound simplifies to Õ(H⁴SAB/ε²)." This would be honest and informative without weakening the result.

3. **Clarify the model-free status of the algorithm with respect to the P̂ notation.** A single sentence stating "P̂_{h,s,a,b} denotes the empirical estimate from a single observed transition, not a stored transition tensor" would resolve the ambiguity.

4. **Either develop the multi-player extension substantively or remove it.** The current one-sentence treatment adds no value and invites criticism. If the authors have a genuine generalization, they should sketch the modifications; otherwise, deferring it to future work would be more honest.

5. **Explain the role of CCE computation in the algorithm.** The computational complexity claim hinges on this — the algorithm section should briefly describe when and how CCE is computed and how it connects to policy improvement.

---

## Score and Decision

This paper makes genuine theoretical contributions: O(SABH) space complexity (information-theoretically minimal), O(T·poly(AB)) computational complexity, and the first model-free TZMG algorithm to simultaneously output a Markov and Nash policy. The sample complexity rate Õ(H⁴SAB/ε²) matches the best existing model-based method (Nash-VI) with better burn-in under S > H³.

However, the paper has significant presentation gaps. The two claimed innovations (early-settlement method, reference-advantage decomposition in TZMG) are not described in the main text — they are named but not explained. The headline sample complexity is presented without acknowledging the ε ≪ 1/H³ regime required for the simplified bound, which is restrictive. The multi-player extension is a placeholder, and the CCE computation underlying the computational claim is disconnected from the algorithm description.

These are fixable issues, but they are substantive enough that the paper in its current form does not meet the clarity and completeness standard expected at a top venue. The core ideas are promising; the presentation needs substantial revision.

**MY FINAL SCORE:** <score>5.0</score>
**MY FINAL DECISION:** <decision>Reject</decision>