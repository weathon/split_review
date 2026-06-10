Now let me write the final consolidated review.

## Summary

This paper proposes an algorithm for learning stochastic PPDDL-style action models from demonstrations, relaxing a key independence assumption from prior work (Juba & Stern, 2022) that the effects on individual fluents are independent random variables. The core idea is to use higher-order tensor moments and Kruskal's theorem to achieve identifiability of boolean effect vectors, enabling recovery of the joint distribution of an action's effects across fluents. The paper presents a polynomial-time algorithm with formal safety and approximate-completeness guarantees.

## Strengths

- **Relaxes a restrictive independence assumption from prior work**: The paper explicitly identifies that Juba & Stern (2022) assumed effects on individual fluents are independent random variables, and proposes a method for general stochastic effects where actions can jointly set arbitrary subsets of fluents (line 14: "Previous work that tackles safe learning… assumed that the effects of actions on each fluent are independent random variables. In this work, we relax that assumption."). This is a genuine and well-motivated generalization of the problem class.

- **Formal identifiability argument via Kruskal's theorem for boolean vectors**: Section 2.3 provides a principled argument that when the moment degree is d = O(log r), the tensor decomposition of boolean component powers is unique. Lemma 1 is stated (though unproven) to establish that the effect vectors can be uniquely recovered from the moments. This addresses a genuine technical challenge — generic identifiability guarantees do not apply to discrete (binary) vectors.

- **Principled handling of missing tensor entries**: The paper identifies that not all moment tensor entries can be estimated (states where a literal is already true do not reveal whether it was an effect), and proposes adding d-CNF disjunctive preconditions to restrict action usage to states where the relevant minors are fully observed (lines 154–158). This is a theoretically grounded approach to handling data sparsity that respects the safety guarantees.

- **Formal safety and approximate-completeness guarantees**: Theorems 1 and 2 provide explicit guarantees that the learned model's trajectory distribution is close to the true distribution, and that if training policies succeed with probability p, the learned model contains a policy succeeding with probability at least p − O(ε). The sample complexity is bounded by poly(|A|, |F|^{O(log r)}, L, 1/ε, 1/δ).

## Weaknesses

### Major

1. **Core algorithm is critically underspecified — Eq. (7) and Eq. (8) are never defined**: The algorithm references "the SDP in Eq. 7" (lines 181, 250) and an inconsistency criterion "Eq. 8" (line 184), but neither equation appears anywhere in the paper. The SDP is described in prose (lines 232–234) but not written as a formal optimization problem with variables, constraints, and objective; the inconsistency criterion is never defined at all. Since the algorithm is the paper's central technical contribution, a reader cannot implement it or fully evaluate its correctness from the paper as written. This is not a minor presentation issue — the paper repeatedly invokes these missing equations as key steps in the algorithm.

2. **Lemma 1 — the foundation of the identifiability argument — is stated without proof**: The claim that for S ⊆ {0,1}^n, if |S| ≤ 2^{k+1} − 2 then S^{⊗k} is linearly independent (line 79) is non-trivial (the bound is exponential in k). No proof or citation is provided. Without this lemma, the entire identifiability argument (and thus the motivation for using Kruskal's theorem over boolean vectors) rests on an unsubstantiated claim.

3. **Correctness proof for the main fragment-composition algorithm is too brief**: The proof (lines 248–250) is approximately 10 lines of informal reasoning for the paper's central technical algorithm. Key steps are asserted without adequate justification: that the SDP solution yields a rank-1 matrix under the given (underspecified) constraints, that the spectral structure is preserved across blocks with different observed subsets, and that the whitening ensures consistency in the missing-entry setting. Lemma 3 (termination) and Lemma 4 (probability consistency) each have one-paragraph proofs that lack the rigor expected for a theoretical paper at a top venue.

4. **No experimental validation**: The paper contains no experiments — not on synthetic data, not on IPC benchmark domains, not even a toy demonstration. For a paper proposing a new algorithm with claimed polynomial-time guarantees, the complete absence of empirical evidence is a significant shortcoming. Even small-scale experiments would substantially strengthen the work.

### Minor

1. **Safety and completeness theorems are delegated to prior work without justification**: Line 273 states: "The only difference between the proofs of these theorems and Juba & Stern (2022) is that we change the dependence on the number of fluents |F| to the dependence on the number of effects |F|^{O(log r)}." Given that the model class has changed (from independent fluents to general joint distributions), it is not obvious that the existing proofs carry over with only a dimension parameter change. Some justification or sketch of the proof adaptation is needed.

2. **No conclusion, discussion of limitations, or outlook**: The paper ends abruptly after Theorem 2 (line 271). There is no discussion of the scope of assumptions (no conditional effects, grounded representation, small constant r, competent demonstrations), potential failure modes, directions for relaxation, or even a summary of contributions. This makes the paper feel unfinished.

### Trivial

- The tensor reshaping description (lines 75–77) could be slightly more explicit about how the (2k+1)-mode tensor is mapped to a 3-mode tensor.

## Nice-to-Haves

- Discussion of the r ≤ n requirement from Jennrich's algorithm and its implications for domains with few fluents.
- A conclusion/discussion section synthesizing contributions and acknowledging limitations.

## Removed Points

These points from the source reviews were identified as invalid, speculative, or nonsensical during verification and are removed from the main assessment:

- **"Missing sections 2.1 and 2.2"**: This is a formatting/parser artifact from PDF extraction. The paper's section numbering is internally consistent for the content that exists. Removed per the rule that formatting artifacts are not author errors.
- **"Whitening matrix computation not addressed for rank deficiency"**: The paper mentions PCA-based computation (line 221) and Lemma 1 establishes linear independence of effects when the moment degree is sufficient. This concern is at best a minor elaboration, not a real weakness. Removed.
- **"Tensor reshaping argument unclear"**: The description (lines 75–77) is one sentence but conceptually clear for the target audience. Removed.
- **Generic "important problem" / "timely topic" strengths from Strength Finder**: These lacked specific evidence anchored in the paper content. Removed per filtering rules.
- **Criticism about definition of consistent/inconsistent local vectors**: This is subsumed by the missing Eq. 8 issue (Major weakness #1 above). Merged, not duplicated.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the incomplete nature of the technical exposition but do not identify any novel angle the paper itself missed — they primarily document what is missing rather than what is wrong with what is present.

## Suggestions

1. Fully specify the SDP (Eq. 7) as an explicit optimization problem with variables, constraints, and objective. Define the inconsistency criterion (Eq. 8) precisely.
2. Provide a proof (or a citable reference) for Lemma 1 — this is the linchpin of the identifiability argument and cannot be left as an exercise.
3. Expand the correctness proof for the fragment-composition algorithm (Section 4.2) with rigorous reasoning about the missing-entry setting, the spectral properties of contracted blocks, and the consistency of the SDP-based alignment.
4. Include experiments on at least one small IPC probabilistic planning benchmark (e.g., Tireworld or Blocksworld with a few fluents) or synthetic data with known ground-truth effect distributions.
5. Add a conclusion/discussion section that addresses limitations, assumptions, and directions for future work.
6. Provide a brief justification for why the safety/completeness proofs from Juba & Stern (2022) carry over to the new setting where effects are not independent.

## Score and Decision

**Score**: 4.0/10 — The paper has a creative and well-motivated core idea (using higher-order tensor moments + Kruskal's theorem for identifiability of boolean vectors in stochastic action model learning) and correctly identifies an important limitation of prior work. However, the paper as submitted does not deliver a complete, rigorous, or reproducible contribution. The algorithm is critically underspecified (key equations referenced but never defined), a foundational lemma is unproven, the main correctness proof is too brief to be convincing, and there is no experimental validation. These are structural gaps, not matters of polish.

**Decision**: Reject

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>