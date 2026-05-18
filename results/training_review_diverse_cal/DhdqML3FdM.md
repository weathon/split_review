Now I have thoroughly verified every claim against the paper. Let me write the consolidated review.

## Summary

This paper presents a theoretical and empirical analysis of the limitations of Structured State Space Models (SSMs) using computational complexity theory. It claims three main theoretical results: (1) one-layer SSMs cannot efficiently solve function composition over large domains without impractically large state sizes (Theorem 1); (2) even with Chain-of-Thought prompting, SSMs require a number of CoT steps that scales as Ω(√(n log n)/(dp)) for iterated composition (Theorem thm-CoT); and (3) multi-layer SSMs are constrained by log-space computational capacity (Theorems ssm_log_space and LogSpace), placing them in the complexity class L and limiting their reasoning abilities on NL-complete and P-complete problems.

## Strengths

1. **Solid lower bound for one-layer SSMs on function composition (Theorem 1).** The paper provides a clean communication-complexity reduction from a three-party problem to SSM computation, deriving a probability-of-error bound of at least R/(3n log n) when model capacity (d²+d)p is insufficient. The reduction is clearly explained: Grace computes the initial hidden state, Faye sends matrix/vector aggregates, and Xavier reconstructs the final hidden state. This is a well-structured adaptation of prior Transformer results (Peng et al.) to SSMs.

2. **Extension of the complexity-theoretic analysis framework from Transformers to SSMs.** Prior work focused on Transformers (Merrill et al., Peng et al.). This paper systematically adapts communication-complexity and logspace arguments to SSMs, bridging a clear gap in the literature. The framing of SSM limitations through computational complexity classes provides a coherent organizing principle.

## Weaknesses

### Fatal

None. While the paper has significant issues, they are repairable in principle with major revisions.

### Major

1. **Theorem ssm_log_space (log-space bound) has a mathematically incorrect proof.** The theorem states that an L-layer SSM can be computed with O(L log N) bits when precision p and embedding dimension d satisfy p,d ≤ poly(N). The proof claims that "each element of these matrices can be represented using O(log N) bits" because p and d are polynomially bounded (line 217), and later asserts "numbers are represented with p = O(log N) bits of precision" (line 232). This is unjustified: p ≤ poly(N) does **not** imply p = O(log N). If p = N^c for any constant c>0, each matrix element requires N^c bits, not O(log N) bits, and a single hidden state vector would already require d·p bits that can be polynomial in N. The theorem's conclusion (that SSMs are in L) is nevertheless consistent with prior work (Merrill et al. 2024 placed SSMs in TC^0 ⊆ L), but the proof as presented is incorrect and needs a proper justification — for instance, by assuming constant d and p, or at most O(log N) precision, which are standard in practice but different from the stated condition.

2. **Theorem thm-CoT (CoT lower bound) proof contains a significant gap in the communication protocol construction.** The proof states (line 179) that "Alice computes φ_{r, n+k}(x₁,…,x₂ₙ) from φ_{r-1}(x₁,…,x₂ₙ) and x₁,…,xₙ" — i.e., she computes the (n+k)-th hidden state of the SSM using only the first n input tokens. However, the SSM's recurrent hidden state at position n+k necessarily depends on **all** tokens processed up to that point, including x_{n+1},…,x_{n+k}, which belong to Bob's portion of the input. Since Alice does not know Bob's tokens, she cannot compute this hidden state unless the SSM's architecture has some special property that allows this factorization — no such property is argued or even mentioned in the proof. The proof appeals to similarity with "the proof of Theorem 2 in [peng2024limitations]" (line 165), but the Transformer setting differs crucially (attention can selectively ignore positions), and no explanation is given for why the SSM's recurrent computation permits the same partitioning. Without a working reduction, the claimed CoT lower bound does not follow.

### Minor

3. **Experimental results are absent from the main text.** Section 7 (Experiments) describes the setup — models used (GPT-4, Jamba), hardware, and evaluation methodology — but contains no results whatsoever (no tables, figures, or accuracy numbers). The introduction mentions two isolated accuracy figures (GPT-4 27%, Jamba 17% on 4×3-digit multiplication) as motivation, but these are not systematic experimental results. Even accounting for possible appendix stripping, a conference paper's main text should present at least summary empirical findings to support claims of "empirical validation." As it stands, the experimental section is a methods paragraph without outcomes.

### Trivial

4. **The bound in Theorem thm-CoT has negligible practical significance for realistic parameters.** Even if the proof were repaired, the bound R ≥ (3/100)·√(n log n)/(dp) yields values well below 1 for typical settings (e.g., dp≈500, n≈1000 gives ~0.6 CoT steps), meaning it does not provide a meaningful constraint in practice. This does not invalidate the mathematics, but the paper oversells the practical implications.

## Nice-to-Haves

- If the log-space proof is repaired, explicitly state the assumption that d and p are constants or at most O(log N), which matches practical SSM configurations.
- Provide experimental summary results in the main paper (e.g., a table with accuracy across tasks/models), even if detailed breakdowns remain in an appendix.
- Clarify whether the CoT proof intends to assume linear SSMs (input-independent A,B,C,D matrices), which might permit the claimed factorization — and if so, state this assumption explicitly.

## Removed Points

These points were raised by reviewers but do not hold up under verification against the paper:

- **"The paper claims multi-layer SSMs cannot overcome limitations of one-layer SSMs as a proven statement"**: The paper explicitly marks this as a conjecture ("We conjecture that any SSM with a constant number of layers would still be unable..." — line 120). The reviewer's criticism is factually incorrect. **Removed.**
- **"Missing discussion of empirical observations in literature"**: The related work section (lines 268-273) discusses Dziri et al. on compositional tasks, Merrill et al. on complexity, and others. The connection is present. **Removed.**
- **"Definition of SSM with CoT is unclear"**: The definition (lines 131-138) provides a recursive construction with clear notation. While unusual in form, it is functionally precise. **Removed.**
- **Strength Finder's "Empirical alignment with theory"**: The claimed strength rests on two numbers in the introduction (GPT-4 27%, Jamba 17%), not on systematic results. The main experiments section has no results. This strength is unsupported and conflicts with verified Weakness #3. **Removed.**
- **Reproducibility nitpicks** and **formatting complaints**: Trivial parser artifacts. **Removed.**

## Novel Insights

None beyond the paper's own contributions, as the two main novel theorems (CoT lower bound and log-space proof) have unresolved issues. The adaptation of Theorem 1 from Transformers to SSMs is competent but incremental.

## Suggestions

1. **Fix the log-space proof.** The key issue is making the precision/dimension assumptions precise. Either assume d = O(1), p = O(log N) (consistent with practical SSMs) and state this explicitly, or provide a correct argument that poly(N) precision implies the correct space bound. Cite Merrill et al. 2024 for the already-established result.
2. **Rework the CoT lower bound.** The current reduction from pointer chasing is not justified for SSMs. Either provide a rigorous argument showing how Alice can compute the relevant hidden state without Bob's tokens, acknowledge the need for linear (input-independent) SSMs, or restructure the proof entirely. The appeal to "similarity with Peng et al." is not sufficient — the Transformer and SSM architectures work differently.
3. **Include experimental results in the main text.** Even a single summary table with accuracy, standard deviations, and model comparisons across tasks would substantially strengthen the paper and support the theory-empirics link claimed in the abstract.
4. **Temper the claims about Theorem thm-CoT's practical implications** unless the bound can be strengthened to give nontrivial values for realistic parameters.

## Score and Decision

The paper has one solid theoretical contribution (Theorem 1, adapting existing Transformer results to SSMs) but the two other main theoretical results have significant issues: the log-space proof contains a mathematical error, and the CoT lower bound rests on an unjustified protocol construction. The experiments section lacks results in the main text. These problems are repairable but require substantial revisions. In its current form, the paper cannot be accepted.

MY FINAL SCORE: <pineapple>3.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>