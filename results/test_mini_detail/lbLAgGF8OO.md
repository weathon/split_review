Now I have everything I need. Let me compile the final consolidated review.

## Summary

This paper introduces Dig-DEC (Dual Information Gain Decision-Estimation Coefficient), a model-free DEC framework that replaces the optimism principle of prior work with information-gain-driven exploration. The framework yields three main contributions: (1) a proof that Dig-DEC ≤ optimistic DEC + η, with a concrete bandit instance where the improvement is arbitrarily large (Theorems 13–14); (2) the first model-free regret bounds for hybrid MDPs (stochastic transitions, adversarial rewards) with bandit feedback, resolving an open problem from [LWZ25]; and (3) refined online estimation procedures that improve regret exponents in both the average-error and squared-error regimes.

## Strengths

1. **Dig-DEC is provably no larger than optimistic DEC and can be much smaller.** Theorem 13 shows \(\text{dig-dec} \le \text{o-dec} + \eta\), and Theorem 14 gives a 3-armed bandit instance where optimistic DEC forces \(\Omega(\sqrt{T})\) regret while Dig-DEC achieves \(O(1)\). This directly demonstrates the advantage of removing optimism and adding information-gain terms.

2. **First model-free regret bounds for hybrid MDPs with bandit feedback.** The paper obtains bounds for hybrid bilinear classes and coverable MDPs under linear reward with bandit feedback (Table 2), explicitly resolving the open problem left by [LWZ25]. The removal of optimism is critical here because it avoids the need for explicit reward estimators.

3. **First DEC-based method to achieve \(\sqrt{T}\) regret in Bellman-complete MDPs.** Table 1 reports \(H\sqrt{dT}\log|\Phi|\) regret for Bellman-complete on-policy bilinear classes and coverable MDPs. This matches the performance of optimism-based approaches [JLM21, XFB⁺23] within the DEC framework for the first time, improving over the \(T^{5/6}\) bound of [FGQ⁺23].

4. **Sharper concentration via an unbiased estimator for average estimation error.** Section 4.2.1 constructs an unbiased product-of-half-sample estimator, improving the regret exponents over the biased estimator of [FGQ⁺23]. The constant-order Est bound (\(\log^2|\Phi|\)) for the squared-error case (Theorem 11) is a crisp improvement over prior \(T^{1/2}\) dependence.

5. **Flexible divergence framework.** Section 4 generalizes the AIR framework with a general divergence \(D\), enabling a clean mirror-descent-style analysis that recovers prior results of [XZ23] and [LWZ25] more simply. This flexibility is demonstrated by the fact that the hybrid model-based case achieves Est independent of \(\log|\Phi|\), while [LWZ25] required a more complex two-level algorithm.

## Weaknesses

### Fatal

None. The harsh critic's central claim — that the regret bounds in Tables 1–2 are inconsistent with the stated theorems — is based on calculations using exponents that the PDF parser has demonstrably garbled. The text itself reveals the garbling: e.g., line 219 states the estimator "improves their rate of Est from \(\sqrt{T}\) to \(T^{1/2}\)" (identical numbers), and the introduction contains superlinear \(T^{3/2}\) exponents that cannot be correct. The Bellman-complete rows of Table 1 check out perfectly when computed from the stated dig-dec and Est bounds. The remaining apparent inconsistencies are parser artifacts, not mathematical errors.

### Major

- **Strong assumptions limit the generality of the hybrid-setting results.** The hybrid setting requires known linear reward features (Assumption 4) and a partition structure (Assumptions 2–3) that does not cover cases like hybrid low-rank MDPs with unknown reward features. The paper acknowledges this limitation (lines 121–123) and the authors leave it as future work, but it narrows the scope of the claimed "first model-free regret bounds for hybrid MDPs with bandit feedback."

- **The computational complexity of Algorithm 1 is not addressed.** The algorithm requires solving a minimax saddle-point problem (Eq. 3) over \(\Delta(\Pi)\) and \(\Delta(\Psi)\) at each round. Prior AIR-based algorithms face similar challenges, but for a paper claiming a general framework, the absence of any discussion of computational tractability is a noticeable gap. The paper's own definition of "model-free" (line 43) explicitly excludes computational constraints, so this omission is self-consistent but limits practical relevance.

### Minor

- **The presentation of exponents is confusing due to what appear to be parser artifacts.** The abstract claims \(T^{3/5}\) (on-policy) / \(T^{7/8}\) (off-policy) for the average-error case, while Table 1 shows \(T^{2/3}\) for both. The hybrid table (Table 2) contains entries with superlinear \(T^{3/2}\) dependence. Without consulting the appendix (which contains the detailed derivations), a reader cannot verify which exponents are correct from the main text alone. While these are likely extraction artifacts, they undermine the main text's self-containedness.

- **The discussion of high-probability bounds is brief.** The paper mentions (line 278) that high-probability bounds are possible with a variant of \(D\) in the stochastic setting, but notes this variant "cannot handle the hybrid setting." Given that the hybrid setting is adversarial, high-probability guarantees would be more meaningful, and the limitation warrants more discussion.

- **The intuition for when Dig-DEC improves over optimistic DEC in MDP settings is underdeveloped.** Theorem 14 gives a bandit example, but for the MDP settings that motivate the paper (bilinear classes, Bellman-eluder dimension, coverability), the paper does not sketch *why* the extra KL information-gain term yields strict improvement. The decomposition in Section 6 (lines 311) mentions that the second KL term captures distributional differences ignored by mean-based divergences, but this insight is not explicitly connected to the MDP applications.

### Trivial

None.

## Nice-to-Haves

- A brief worked example in the main text showing the regret derivation (from dig-dec and Est to final bound) for one representative setting would substantially improve verifiability.
- A discussion of whether the minimax problem (Eq. 3) can be solved efficiently for any of the concrete MDP classes considered.
- Expanding the high-probability discussion — even just noting why the hybrid setting precludes the simple KL variant and whether alternative approaches exist — would strengthen the presentation.

## Removed Points

The following points from the reviewer inputs were removed, with justification:

1. **"Regret bounds in Tables 1–2 are inconsistent with stated theoretical results"** (Harsh Critic, Critical Issues): Removed. The harsh critic's calculation assumes \(\mathbf{Est} \lesssim T^{1/2}\) from Theorem 7, but line 219 shows the parser garbled this exponent ("improves from \(\sqrt{T}\) to \(T^{1/2}\)" — identical numbers). The Bellman-complete cases verify correctly. The exponent discrepancies are parser artifacts per the hard formatting-artifact rule.

2. **"Abstract claims \(T^{3/5}\) but tables show \(T^{2/3}\)"** (Harsh Critic): Removed as a formatting artifact. The parser has extensively garbled exponents throughout the document (e.g., superlinear \(T^{3/2}\) in the introduction, identical "improvement" from \(\sqrt{T}\) to \(T^{1/2}\)). Without the original PDF, these cannot be attributed to the authors.

3. **"Paper relies heavily on appendices not included in review copy"** (Harsh Critic): Removed per hard rule. The parser strips appendices from all papers; they exist in the original submission.

4. **"No Algorithm 1 implementation guidance"** (Harsh Critic): Downgraded from a weakness to a nice-to-have. The minimax problem is standard in the AIR framework, and the paper's contribution is the analysis framework, not an implementation recipe.

5. **"Strengths about the paper addressing an important problem / targeting an interesting question"** (Strength Finder): Removed as generic/superficial per the filtering instructions.

## Novel Insights

None beyond the paper's own contributions. The two reviewer inputs did not produce a genuinely novel observation that the paper's own analysis does not already contain.

## Suggestions

1. **Clarify the exponents.** Whether through a corrigendum or an updated version, the authors should ensure the abstract, introduction, and tables agree on the regret exponents. A single worked derivation for one representative setting (e.g., on-policy bilinear with \(\overline{D}_{\text{av}}\)) in the main text would allow readers to verify the logic.
2. **Discuss computational considerations.** Even briefly noting that the minimax problem reduces to a tractable form in each specific MDP class would address the computational complexity gap.
3. **Expand the discussion of Assumptions 3–4.** A paragraph explaining which well-studied MDP classes satisfy these assumptions (and which do not) would help readers assess the scope of the results.

## Score and Decision

### Calibration

**Round 1 — Bracketing:**
- Weak anchors (score < 3.5): avg 2.5–3.0 — papers with fundamental flaws or lack of novelty. This paper is clearly above these.
- Middle anchors (3.5–7.5): the most relevant band.
  - `/home/wg25r/review_agent/human_reviews/4WM0OogPTx.md` (avg 6.75, Accept poster) — good empirical contribution with sound theory. The Dig-DEC paper has stronger theoretical novelty but less empirical grounding.
  - `/home/wg25r/review_agent/human_reviews/1zuJZ1jGvT.md` (avg 5.0, Reject) — offline RL with diffusion, had presentation issues and missing baselines. The Dig-DEC paper is stronger in clarity and contribution.
- Strong anchors (score > 7.5): avg 8.0 — oral/spotlight papers. The Dig-DEC paper's parser-induced presentation issues and strong assumptions keep it below this tier.

Initial bracket: [5.5, 7.0]

**Round 2 — Narrowing:**
- `/home/wg25r/review_agent/human_reviews/3K3s9qxSn7.md` (avg 6.33, Accept poster) — theory paper on representation complexity. Solid theoretical contribution, limited experimental validation. The Dig-DEC paper has comparable theoretical depth with more concrete results (explicit regret bounds, resolved open problem).
- `/home/wg25r/review_agent/human_reviews/nIEjY4a2Lf.md` (avg 6.0, Accept poster) — theory paper on misspecified Q-learning. Matching upper/lower bounds, narrow setting. The Dig-DEC paper has broader applicability but less crisp optimality guarantees.
- `/home/wg25r/review_agent/human_reviews/lF2aip4Scn.md` (avg 6.5, Accept poster) — theory paper on demonstration-regularized RL. Strong theoretical results, well-written. The Dig-DEC paper has comparable theoretical contributions.
- `/home/wg25r/review_agent/human_reviews/Pe2lo3QOvo.md` (avg 6.25, Accept poster) — RLHF theory paper. Near-optimal tradeoffs. Similar tier.

The Dig-DEC paper's novel DEC framework, Theorems 13–14, and resolution of an open problem place it comparably to these accepted theory papers. The parser-induced presentation issues are a genuine weakness but not a mathematical one. The paper sits comfortably within the accepted-poster range.

**Final score: 6.0** — a solid theory paper with clear contributions, held back from a higher score by the parser-garbled presentation and the strength of its assumptions.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>