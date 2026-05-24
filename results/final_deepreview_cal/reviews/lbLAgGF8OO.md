Now let me write the consolidated final review.

---

## Summary

The paper introduces Dig-DEC, a new model-free decision-estimation coefficient that removes the optimism mechanism from prior DEC-based algorithms and instead drives exploration through information gain (KL-based regularization and posterior entropy). The authors apply this framework to obtain regret bounds for model-free RL in stochastic and hybrid MDPs with bandit feedback, and also improve online function estimation procedures (unbiased batch estimator for average error, constant-bounded estimator for squared error). A constructive separation result (Theorem 14) shows Dig-DEC can be arbitrarily better than optimistic DEC.

## Strengths

- **Novel complexity measure with genuine conceptual advance (Section 4.1, Eq. 8).** Dig-DEC replaces optimism with two information-gain terms (KL regularization + posterior entropy). This is a clean conceptual contribution that generalizes the AIR framework and removes a mechanism (optimism) that was blocking extension to the hybrid/bandit setting.

- **Improved estimation procedures (Section 4.2).** The unbiased batch estimator for average Bellman error (splitting the batch into halves and cross-multiplying) and the refined two-timescale procedure for constant Est are nontrivial technical improvements over [FGQ⁺23]. These could have independent value.

- **Strict separation from optimistic DEC (Theorem 14).** The 3-armed bandit construction where Dig-DEC achieves constant regret while optimistic E2D suffers Ω(√T) regret provides concrete evidence that the information-gain terms capture something optimism cannot. This is a clean theoretical result.

- **Generalized and simplified analytical framework (Eq. 5–6).** The first-order optimality + Bregman decomposition analysis is more flexible than prior "constructive minimax" approaches and recovers prior results as special cases.

## Weaknesses

### Fatal

None that are verifiable from the paper as written without speculation about the appendix.

### Major

- **Internally inconsistent regret exponents between abstract and Table 1, and within the text itself.** The abstract claims estimation-procedure improvements from $T^{3/4}$ to $T^{3/5}$ (on-policy) and from $T^{5/6}$ to $T^{7/8}$ (off-policy). However, (i) $T^{7/8} > T^{5/6}$, so the claimed "improvement" is in the wrong direction for the off-policy case, and (ii) Table 1 reports $T^{2/3}$ for all $\overline{D}_{\text{av}}$ rows — matching neither $T^{3/5}$ nor $T^{7/8}$. Separately, line 39 claims improvement from $T^{5/8}$ to $T^{5/6}$, but $5/6 > 5/8$. These inconsistencies make it impossible for a reader to determine what the paper's actual claimed rates are, undermining the central quantitative contribution.

- **Four of five rows in Table 2 report superlinear regret ($T^{3/2}$ or $T^{13/8}$), contradicting the paper's central claim of sublinear regret for hybrid MDPs.** The introduction (line 38) claims "first sublinear regret for model-free learning in hybrid bilinear classes and Bellman-complete coverable MDPs." Table 2 Row 5 (coverable) shows $T^{3/2}$, which is asymptotically worse than the trivial $T$ bound — not sublinear. Rows 1–3 are also superlinear. Only Row 4 (off-policy Bellman-complete bilinear) reports $T^{1/2}$. The paper provides no explanation for why these bounds are superlinear or how they should be interpreted. If these are the true regret guarantees from the framework, the central claim collapses. If the table entries contain computational errors (plausible, since applying the stated formula $T \cdot \text{dig-dec} + \text{Est}/\eta$ with the stated dig-dec forms yields sublinear exponents), then the results table as published is incorrect.

- **Textual error in estimation-rate description.** Line 219 states the unbiased estimator "improves their rate of Est from $\sqrt{T}$ to $T^{1/2}$" — these are identical. The intended comparison is unclear. While likely a typo, in a theory paper where the main contribution is improved rates, imprecise rate statements erode confidence.

### Minor

- **The "first model-free regret bounds for hybrid MDPs with bandit feedback" claim is only partially supported** — one row of Table 2 is sublinear ($T^{1/2}$), and that row requires Bellman completeness plus an additional restriction (the $\star$ condition of Lemma 36, deferred to the appendix). The abstract and introduction do not qualify this claim sufficiently.

- **Heavy reliance on stripped appendix for core derivations.** The dig-dec bounds for all concrete settings (bilinear, BE, coverable) are deferred to Appendices H and I. The POSTERIORITYUPDATE procedures (Algorithms 3 and 4) are not described in the main body. Theorem 14's proof is in Appendix J. The main paper asserts results without enabling even partial verification.

- **Assumption 3 (unique reward-to-value mapping) is restrictive and not motivated with a concrete MDP instance in the main text**, limiting the reader's ability to assess the scope of the results.

### Trivial

- The $\sqrt{T}$ vs. $T^{1/2}$ redundancy at line 219.
- The abstract could more clearly distinguish between improvements from the estimation procedure alone versus the full Dig-DEC + estimation combination.

## Nice-to-Haves

- A worked example illustrating how the KL information-gain term in Dig-DEC captures distributional differences that the mean-based $\overline{D}$ misses, beyond the 3-armed bandit (Theorem 14), would strengthen the conceptual narrative.
- More prominent discussion of the known-feature limitation (Assumption 4) and the failure to handle unknown feature mappings for low-rank MDPs, so the scope is clear to a casual reader.

## Removed Points

These points are flagged to be removed, treat them with caution.

- **Harsh Critic: "Insufficient specification of the algorithmic framework and potential violation of convexity."** The $\mathbb{E}_{M\sim\nu}[g(M)]$ term is linear (hence convex) in $\nu$, and the KL-of-posterior term is standardly convex in the prior. No evidence of a convexity problem exists in the paper.

- **Strength Finder: "First model-free regret bounds for hybrid MDPs with bandit feedback" as an unqualified strength.** This is reframed as a partially-supported claim under Weaknesses, since most of Table 2 is superlinear.

- **Harsh Critic: claiming ALL Table 2 bounds are superlinear.** Row 4 is $T^{1/2}$, genuinely sublinear. The criticism is partially correct but overstated.

- **Strength Finder: "Generalized algorithmic framework (Section 4, Algorithm 1)" as a core strength.** This is a real contribution but the description is too generic to carry independent weight without the specific instantiations.

## Novel Insights

The paper's most genuinely novel observation is the decomposition of the KL term in Dig-DEC into a *regularization* component ($\text{KL}(\nu_\phi, \rho)$) and an *information-gain* component ($\mathbb{E}[\text{KL}(\nu_\phi(\cdot|\pi,o), \nu_\phi)]$), with the insight that the former alone can replace optimism and recover prior bounds, while the latter enables strict improvement over optimistic DEC. This two-component view of information-gain-driven exploration — and the recognition that removing optimism is what unlocks the hybrid/bandit extension — is conceptually clean and goes beyond prior DEC variants.

## Suggestions

- Recompute and verify every entry in Table 1 and Table 2 against the stated formula $T \cdot \text{dig-dec} + \text{Est}/\eta$. If the current entries are correct, explain the derivation explicitly; if not, correct them. The abstract's numbers must be reconciled with the tables.
- For hybrid Table 2 entries that remain superlinear after correction, either qualify the "sublinear regret" claim or explain why the bound is still meaningful (e.g., due to small constant factors for practical $T$).
- Bring at least a sketch of the POSTERIORITYUPDATE and the dig-dec bound derivations into the main text, so the core algorithmic and analytical contributions are partially verifiable without the appendix.

## Score and Decision

**Round 1 bracket:** Weak anchors (2.0–3.0) are clearly below this paper's conceptual contribution; strong anchors (8.0) are clearly above due to this paper's internal inconsistencies. The paper plausibly sits in the 3.5–6.5 range.

**Round 2 narrowing:** Read anchors at 4.25 (VBMLE for linear MDPs — competent but incremental), 5.20 (Model-Free BPI in CMDPs — solid but limited by assumptions), 5.50 (Minimax Optimal RL with Trajectory Feedback — clean, consistent results), and 6.00 (Horizon-Free Adversarial Linear Mixture MDPs — polished, clear contribution). The paper under review has more conceptual novelty than the 4.25 and 5.20 anchors but substantially worse result-presentation quality than all of them: multiple internally inconsistent exponent claims in the abstract, introduction, and tables. The 5.50 anchor has clean, verifiable results despite some presentation quibbles; this paper's results cannot be trusted at face value. The paper is therefore below the 5.20–5.50 cluster. Placed at **4.0**.

**Anchor comparison summary:**
| Anchor ID | Avg Score | Round | Comparison |
|---|---|---|---|
| lFzUHGebeb | 2.00 | R1 | Far weaker — flawed methodology, no clear contribution |
| A1WwYw5u8m | 3.00 | R1 | Weaker — incremental convergence result |
| 2h3m61LFWL | 4.25 | R2 | Comparable novelty but cleaner results; our paper below due to inconsistencies |
| w8Zo7jACq7 | 5.20 | R2 | Cleaner results, clearer contribution; our paper below |
| en3NwykrHW | 5.50 | R2 | Internally consistent, verifiable results; our paper meaningfully below |
| aPNwsJgnZJ | 6.00 | R2 | Polished, consistent, clear contribution; our paper far below |
| txD9llAYn9 | 7.00 | R1 | Far stronger — horizon-free, second-order bounds, clean |
| 6PbvbLyqT6 | 8.00 | R1 | Far stronger — polished, complete |

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>