Now I have a thorough understanding of the paper and all the critiques. Let me write the consolidated review.

## Summary

This paper initiates the study of Fair Submodular Cover (FSC), which combines a submodular cover objective (minimize cardinality to reach a function threshold) with proportion-based fairness constraints on protected groups. The paper makes three main contributions: (i) conversion theorems that turn bicriteria algorithms for Fair Submodular Maximization (FSM) into bicriteria algorithms for FSC, adapting the Iyer-Bilmes conversion framework to the fair setting; (ii) new bicriteria algorithms for FSM that achieve (1−O(ε), 1/ε) and (1−O(ε), ln(1/ε)+1) guarantees by using β-extensions of the fairness matroid; and (iii) empirical validation on a maximum coverage instance. The continuous algorithm's guarantee of (1−O(ε), ln(1/ε)+1) for FSM, paired with the conversion, aims to match the best-known bicriteria guarantee for submodular cover without fairness.

## Strengths

- **First formalization of Fair Submodular Cover.** The paper correctly identifies that fairness for submodular cover has not been previously studied, and provides a natural proportion-based formulation (p_c|S| ≤ |S∩U_c| ≤ q_c|S|). This opens a new direction at the intersection of algorithmic fairness and submodular optimization.

- **Novel conversion framework from FSM to FSC.** The paper adapts the Iyer-Bilmes conversion to the fair setting through two algorithms (\conv and \convc). The conversion is nontrivial because the fairness matroid constraint prevents direct application of the standard cardinality-constrained conversion. Theorem 1 shows that a (γ,β)-bicriteria FSM algorithm yields a ((1+α)β, γ)-bicriteria FSC algorithm, which is a clean structural result.

- **New bicriteria FSM algorithms with γ→1.** The paper proposes three algorithms (greedy-fairness-bi, threshold-fairness-bi, and the continuous contialg) that achieve approximation guarantees arbitrarily close to 1 on the function value by allowing larger solution budgets. The continuous algorithm's (1−O(ε), ln(1/ε)+1) guarantee improves on the discrete algorithms' O(1/ε) budget factor, which is a meaningful technical achievement.

- **Introduction of the β-extension of the fairness matroid.** Definition 1 formalizes the β-extension, and Lemma 3 (lem:feasible_OPT) states an exchange property between bases of the original matroid and bases of its β-extension. This is used as a building block for the FSM algorithms' analysis.

## Weaknesses

### Major

- **Missing feasibility argument in the discrete conversion (Algorithm 1 / Theorem 1).** The conversion algorithm guesses κ for |OPT| and runs an FSM subroutine with budget κ and lower bounds ⌊p_cκ⌋. The paper does not argue that when the guess κ overshoots |OPT| (which must happen due to the (1+α)-factor geometric search), there exists a feasible solution to this FSM instance with f-value ≥ τ. The optimal FSC solution S* satisfies p_c|S*| ≤ |S*∩U_c|, but when κ > |S*|, the lower bound ⌊p_cκ⌋ can exceed |S*∩U_c|, so S* itself may not be feasible for the FSM instance. The paper's assumption (∑_c min{q_c, |U_c|/(β(1+α)|OPT|)} ≥ 1) is stated but never connected to a constructive argument that a feasible FSM set with f ≥ τ exists. This gap affects the correctness of Theorem 1 and all downstream results that rely on it. Notably, the issue does not arise when κ = |OPT| exactly (S* is feasible then), but the geometric search may skip over that value.

- **The exchange lemma (Lemma 2 / lem:feasible_OPT) is stated without proof sketch and the claimed property is very strong.** The lemma claims that for *any* base S of M_β and *any* base T of M, and *any* permutation of S, there exists a sequence E where each element of T appears β times, such that adding elements of E one-by-one to prefixes of S always stays in M_β. This is a strong exchange property for a nontrivial matroid variant. The paper provides no proof sketch in the main text (the proof is relegated to a stripped appendix), and the property is far from obvious. Since this lemma is central to the analysis of all three FSM algorithms (Theorems 3–5), the paper's theoretical guarantees rest on an unverified claim. *Note: The specific objection that "β copies are impossible in a matroid" reflects a misunderstanding — the lemma's sequence E can contain repeated elements, and the set-union operation S_i ∪ {e_{i+1}} removes duplicates naturally. The concern is about the lemma's correctness and strength, not about duplicates.* The authors: the specific objection about "β copies" is based on a misunderstanding — E is a sequence (allowing repetitions), and the condition S_i ∪ {e_{i+1}} is evaluated as a set (duplicates are naturally removed). The lemma is technically well-formed; the concern is whether it is provably true.

### Minor

- **In-expectation guarantee mismatch for the continuous conversion (Theorem 2).** Theorem 2's guarantee on the function value holds "in expectation," but the paper's definition of an (α,β)-bicriteria approximation for FSC (Section 1) does not specify probabilistic guarantees. A reader expects a deterministic lower bound on f(X). The paper should either extend the definition to allow in-expectation or high-probability guarantees, or provide a concentration argument.

- **The continuous conversion ratio can be ill-defined for small γ.** The fraction ((1−ε/2)γ − ε/3) / (1 + ε/2 + ε/(3γ)) in Theorem 2 can become negative when γ is small (e.g., γ < ε/(3(1−ε/2))). While the intended FSM subroutines have γ ≈ 1, the theorem statement should explicitly state the domain of γ for which the ratio is meaningful.

- **Non-integer β in the discrete algorithms.** The discrete algorithms use M_{1/ε} as the constraint matroid, but Definition 1 defines the β-extension only for β ∈ ℕ₊. Since 1/ε is generally not an integer, the paper should clarify whether ⌈1/ε⌉ is used implicitly, and how this affects the approximation ratios.

- **Limited experimental evaluation.** Experiments are conducted on a single dataset (Twitch Gamers, 5000 nodes) with one submodular function (maximum coverage). The continuous algorithm is not evaluated. The baseline is only the vanilla greedy algorithm without fairness — no comparison to a simple fairness-enforcing baseline (e.g., greedy with post-processing or a different fair maximization algorithm). This limits the empirical support for the framework.

### Trivial

- The definition of the fairness matroid on line 76 contains a typographical inconsistency: "U^c" should read "U_c" in the sum term ∑_c max{|S∩U^c|, l_c}.

## Nice-to-Haves

- A proof sketch of how the assumption ∑_c min{q_c, |U_c|/(β(1+α)|OPT|)} ≥ 1 ensures that a feasible FSM solution with f ≥ τ exists when κ exceeds |OPT|.
- A comparison to a post-processing baseline for fairness in the experiments (e.g., running the standard greedy cover algorithm and then swapping elements to improve fairness).
- A brief discussion of how to handle non-integer β (e.g., using ⌈β⌉ and adjusting the approximation ratio accordingly).

## Removed Points

- *"The paper relies heavily on proofs relegated to an appendix that is not visible"* and *"Proofs or extended sketches for the two main lemmas...are missing from the main text"* — Removed. The paper parser strips appendix content from all submissions; these sections exist in the original. This is a known parsing artifact, not an author error.

- *"Lemma 2 is likely incorrect as stated because a matroid cannot contain the same element more than once"* — Removed. This is a misreading: E is a sequence (allowing repetitions), and the condition S_i ∪ {e_{i+1}} is a set operation that removes duplicates. The lemma as stated is well-formed; the concern should be about the strength of the claimed property, not about set/sequence confusion.

- *"The continuous algorithm is not evaluated"* — The paper states it evaluates only the discrete algorithms; this is not a weakness per se but a scope choice. Moved here for completeness.

## Novel Insights

None beyond the paper's own contributions. The reviewer comments do not surface a surprising new angle on the work that the paper itself does not already present.

## Suggestions

1. **Fix the feasibility gap:** Provide a rigorous argument that when κ exceeds |OPT|, there exists a set S of size κ satisfying both the fairness constraints (⌊p_cκ⌋ ≤ |S∩U_c| ≤ ⌈q_cκ⌉) and f(S) ≥ τ. This likely requires showing that the optimal FSC solution can be extended by adding elements from under-represented groups without harming the function value (by monotonicity). The existing assumption ∑_c min{q_c, |U_c|/(β(1+α)|OPT|)} ≥ 1 should be connected directly to this construction.

2. **Provide a proof sketch of the exchange lemma (Lemma 2):** Even a brief sketch in the main text would help reviewers assess its plausibility. The property is central to all three FSM algorithm analyses and should not be taken on faith.

3. **Clarify the probabilistic guarantee:** Extend the FSC bicriteria definition to accommodate in-expectation guarantees, or provide a high-probability guarantee via concentration for the continuous conversion.

4. **Address the integer β issue:** Explicitly state that β = ⌈1/ε⌉ is used for the discrete algorithms when 1/ε is not an integer, and adjust the approximation ratios accordingly (the effect is absorbed into O(ε) notation but should be acknowledged).

## Score and Decision

The paper tackles a well-motivated new problem and proposes a thoughtful framework. However, the main theoretical results are undermined by a missing feasibility argument in the core conversion theorem and an unverified exchange lemma that is central to the FSM algorithm analysis. These are not minor presentational issues — they affect the credibility of the claimed guarantees. The paper needs substantial revision to the theoretical analysis before it can be accepted.

MY FINAL SCORE: <pineapple>4.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>