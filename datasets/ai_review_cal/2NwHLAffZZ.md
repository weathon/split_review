- Decision: Reject
- Avg Score: 2.33
- Scores: 3, 3, 1
Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

---

## Summary

This paper proposes that "weak derivative correlations" — specifically, asymptotic decay of certain inner products between first and higher-order derivatives of the hypothesis function at initialization — are the fundamental cause of the linearization phenomenon observed in wide neural networks and other overparameterized gradient-based learning systems. The authors formalize this claim by (a) introducing a random-tensor asymptotic framework based on stochastic big-O notation and the subordinate norm, (b) proving two equivalence theorems (Theorems 3.3 and 3.4) linking weak correlations to linearized dynamics under gradient descent, (c) sketching an application to wide neural networks via the tensor programs formalism, and (d) deriving a bound on deviation from linearity over training steps for SGD.

---

## Strengths

- **Conceptually novel framing of linearization.** Prior work (e.g., Chizat et al. 2019, Liu et al. 2020) identified descriptive conditions for linearization — an intrinsic scale, or a Hessian-to-gradient norm ratio. This paper instead proposes an *equivalence*: weak derivative correlations are shown to be both necessary and sufficient for linearized dynamics. This shifts the understanding from "linearization occurs" to "linearization occurs *because of* weak derivative correlations," which is a genuinely new perspective.

- **Equivalence theorems are clearly stated and the core mechanism is intuitive.** Theorem 3.3 (fixed weak correlations ↔ fixed-step linearity) and Theorem 3.4 (exponential weak correlations ↔ rescaled-learning-rate linearity) lay out a clean mathematical relationship. The proof sketch (Taylor expansion + continuous variation of η to prevent term cancellation) gives the reader a clear picture of why the equivalence holds, even if the full rigorous induction is deferred.

- **Generalization to SGD (Corollary 4.1).** Extending the deviation-from-linearity bound from deterministic GD to stochastic single-batch GD is practically relevant, since SGD is the dominant training algorithm in modern deep learning. The corollary connects the weak-correlations framework to a training-time guarantee rather than just a per-step asymptotic statement.

- **Random tensor asymptotic formalism (Section 2).** The introduction of stochastic big-O notation with the subordinate norm, plus the definition of a "definite asymptotic bound" for random tensors, provides a clean technical language for the analysis. This framework is self-contained and could be useful beyond this paper for other problems involving random tensors.

---

## Weaknesses

### Fatal
None.

### Major

- **Theorem 2.1 (Definite Asymptotic Bounds) is stated but not even sketched.** The "Proof Explanation" (lines 158–164) consists of a single observation about non-total orders on \(\mathcal{N}\) and an example involving sine and cosine. It does not describe any proof technique, does not cite a standard result, and does not even gesture at how existence or uniqueness might be established. Since the paper's entire asymptotic framework rests on the claim that every random tensor has a unique tight asymptotic bound, this is a significant gap in the main text. The reader cannot assess whether this lemma is true or under what conditions it holds.

- **The "Proof Explanations" for Theorems 3.3 and 3.4 (the paper's central results) are extremely high-level sketches.** The sketch (lines 332–340) conveys the key intuition — Taylor expansion around each step, equation (25) relating derivative changes to correlation tensors, and the "different terms cannot cancel since η can be varied continuously" argument — but does not address the induction structure, the handling of the uniform asymptotic bounds across inputs and steps, or how the quantifier order in the equivalences is managed. For a paper whose core contribution is these equivalence results, the main text needs to give the reader more than a 10-line sketch to assess technical correctness.

- **The variance-inequality justification (Section 2.2) is technically sloppy.** The claim that \(\text{Var}(M_1 M_2) \geq \text{Var}(M_1) \text{Var}(M_2)\) "generally" holds is not true without further assumptions (e.g., independence or uncorrelatedness). The paper uses this to motivate why stochastic big-O is preferred over moment-based definitions. While the overall point — that moment-based methods have difficulties with products — is valid, the specific inequality is presented without qualification and could mislead readers. This is a minor technical sloppiness in a motivational passage, but worth correcting.

### Minor

- **The "correlations" terminology is imprecise.** Definition 3.1 defines an object that is an inner product of derivative tensors without centering; the paper describes it as "resembling" the Pearson correlation and calls it "unnormalized." However, the sustained use of the word "correlation" throughout the paper (including the title) creates an expectation of a proper statistical correlation (centered, normalized). There is no technical error here — the paper is careful to qualify the analogy — but the framing is somewhat misleading. A clarification or renaming (e.g., "derivative alignment" or "derivative inner products") would strengthen the exposition.

- **The wide neural network example (Section 4.2) is asserted rather than demonstrated in the main text.** The paper claims (Section 4.2, item 1) that FCNNs are "\(n\)-fixed weakly correlated and \(n^{3/2}\)-exponential weakly correlated" and that the proof generalizes to any architecture covered by tensor programs. However, no induction step, no derivation of the correlation decay rates, and no explicit verification of the conditions on activation functions (equation (4)) are given in the main body. The text repeatedly references the appendix, which is stripped. While this is structurally standard, the main text alone does not allow the reader to evaluate whether the claim is substantiated.

- **Corollary 4.1 assumes strong convergence properties of the linearized SGD dynamics.** The assumption \(\mathcal{C}'(F_{\text{lin}}(s),\hat{y}) = O(e^{-s/T})\) uniformly is stated rather than derived, and the paper acknowledges (footnote) that known bounds for SGD typically concern variance, not uniform exponential decay. This limits the corollary's force — it says "if the linear system converges exponentially, then the deviation is bounded," but does not establish when the premise holds. The authors are upfront about this, but it weakens the practical import of the result.

### Trivial

- The text contains a few minor formatting issues (e.g., missing closing brace on line 325–326, the unclosed `\textup{` on line 202). These are parser artifacts and do not affect the technical content.

---

## Nice-to-Haves

- Provide even a brief sketch of how the existence claim in Theorem 2.1 could be approached (e.g., via a supremum over equivalence classes of \(\mathcal{N}\) under \(\sim\)).
- Show the induction base case for the wide NN example (e.g., a single-hidden-layer FCNN) in the main text.
- Discuss the relationship between the derivative correlation decay rate \(m(n)\) and the NTK's spectral properties more explicitly.

---

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"Theorems 3.3 and 3.4 are not proven" (Harsh Critic, Critical Issue 1).** The paper provides proof *explanations* in the main text and the full proofs are presumably in the appendix. Per the review guidelines, weaknesses about missing appendix proofs are not to be counted against the paper. The weakness I retained above is about the *insufficiency of the main-text sketch*, not about the absence of a full proof.

2. **"The existence and uniqueness of a definite asymptotic bound is asserted without a proof" (Harsh Critic, Critical Issue 3).** Same structural issue — the proof may be in the appendix. I retained the criticism in Major above specifically about the *emptiness of the main-text "Proof Explanation"* rather than the absence of a proof.

3. **"The wide neural network example is sketched, not demonstrated" (Harsh Critic, Critical Issue 4).** The criticism explicitly references the stripped appendix. Per guidelines, removed.

4. **"Norm property iii of Lemma 2.1 is stated without proof and not generally true" (Harsh Critic, Section-by-Section Notes).** This is factually incorrect: the paper defines the product as concatenation of indices (tensor product), not contraction. For the subordinate norm with disjoint index sets, \(\|M\| = \|M^{(1)}\|\|M^{(2)}\|\) is correct. The harsh critic appears to have misread the definition as a matrix product.

5. **"The Chicken and Egg subsection is philosophical and does not advance the technical argument" (Harsh Critic).** Discussion sections are allowed to contain philosophical reflection. This is not a weakness.

6. **"No empirical validation" (implied in Harsh Critic's Missing Parts).** The paper is a theory paper; empirical validation is not required for its contribution.

7. **Several "Section-by-Section Notes" that are general impressions rather than specific, citable weaknesses** (e.g., "notation is heavy and not fully integrated," "no formal comparison or derivation is given — merely interpretive remarks"). These are either subjective impressions or scope-creep demands removed per the filtering guidelines.

---

## Novel Insights

The two reviews disagree fundamentally: the Harsh Critic treats the thin main-text proof sketches as fatal, while the Strength Finder focuses on the conceptual contribution. Neither reviewer identified a genuine technical error in the paper's definitions or theorem statements (beyond the variance-inequality sloppiness). The most useful diagnostic observation is that the paper's ambition — claiming an equivalence-based "fundamental cause" for linearization — places a heavy burden on the proofs, and the main-text presentation does not carry that weight. This is a framing-and-presentation gap rather than a mathematical flaw, assuming the appendix proofs are correct.

None beyond the paper's own contributions.

---

## Suggestions

1. **Expand the main-text proof sketches.** In particular, the "Proof Explanation" for Theorem 2.1 should be replaced with a meaningful argument or removed as a theorem. The equivalence theorem sketches should include at least an induction outline and show how the uniform bounds are maintained across steps.
2. **Either clarify the "correlation" terminology or rename it.** A short note explaining that the object is an inner product (the numerator of a Pearson-like quantity) and acknowledging the absence of centering would resolve any ambiguity.
3. **Correct the variance inequality claim** in Section 2.2 to state it holds for independent or uncorrelated variables, if that suffices for the argument, or remove the claim and instead directly motivate stochastic big-O via the failure of moment-based methods.
4. **Include at least one concrete induction step for the wide NN example** in the main text — e.g., showing that for a single-hidden-layer FCNN the correlation terms scale as \(1/\sqrt{n}\).

---
