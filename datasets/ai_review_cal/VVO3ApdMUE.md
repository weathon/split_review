- Decision: Accept
- Avg Score: 5.50
- Scores: 6, 3, 5, 8
Now I have all the information I need. Let me produce the final consolidated review.

---

## Summary

This paper analyzes the satisfiability problem (SAT) for transformer encoders (TE), establishing complexity and computability results. It proves that SAT is undecidable for TE classes commonly studied in the expressiveness literature (with hardmax and expressive scoring, including log-precision variants), and that under restrictions like quantized fixed-width arithmetic or bounded input length, SAT becomes decidable but NEXPTIME-complete. The results are framed in the context of formal reasoning tasks such as verification and interpretability.

## Strengths

1. **Undecidability of TE satisfiability with hardmax and expressive scoring (Theorem 1)**. The paper provides a clear reduction from the octant tiling-word problem to SAT for TE in the class \(\transCundec\), establishing a fundamental limit on formal reasoning for transformer encoders. The reduction strategy (decoding tile positions, linear attention for neighbor access, FNN-based condition checking) is well-motivated.

2. **Undecidability persists for log-precision TE (Theorem 2)**. The paper extends the undecidability result to the log-precision setting, which is a commonly studied restriction in the expressiveness literature (Merrill & Sabharwal, 2023). This shows that log-precision alone does not circumvent undecidability — a non-trivial strengthening.

3. **Clear framing connecting SAT to formal reasoning tasks (Section 3)**. The paper explicitly relates the abstract SAT problem to concrete verification (robustness properties) and interpretation (abductive explanations) tasks, giving the technical results immediate practical relevance.

4. **Honest discussion of limitations and open questions (Section 6)**. The paper acknowledges that results rely on hardmax (not softmax) and points to the interplay between embedding expressiveness and attention complexity as future work, preventing over-generalization.

## Weaknesses

### Fatal

None.

### Major

1. **Proof of Lemma 3 (the small-word property) is incomplete, undermining Theorem 4.** The proof (lines 498–512) presents a reasonable sketch — using periodicity and bounded representation size to argue that unnecessarily long words contain removable subwords — but then the text literally cuts off at "A formal proof relies" with nothing following. Lemma 3 is the linchpin of the NEXPTIME upper bound for quantized TE with periodic embeddings (Theorem 4). Without a complete argument (even a complete sketch), this result cannot be evaluated. This is not a parser artifact; the main-text proof is truncated.

2. **Hardness of the bounded octant word-tiling problem is assumed without proof or citation, undermining the lower bounds of Theorems 3 and 5.** The paper asserts that the bounded octant word-tiling problem is NP-hard (unary encoding) and NEXPTIME-hard (binary encoding) — see lines 466–471. No proof, reduction, or citation is provided. The classic bounded tiling problem is well-known to be NEXPTIME-complete for rectangular tilings, but the octant (triangular, word-encoded) variant is not a standard problem, and its hardness does not automatically follow. The lower bounds for the bounded satisfiability results (Theorem 3) and the NEXPTIME-hardness result (Theorem 5) rest on this unsubstantiated claim.

3. **The proof sketch for Theorem 2 (log-precision undecidability) is too brief to be convincing.** The sketch (lines 404–414) asserts that "the magnitude and precision of all values used and produced in the computation \(T_{\mathcal{S}}(w)\) depend polynomially on \(n\)" without any supporting analysis. A paper presenting a formal undecidability result should provide a more detailed argument about why the specific constructed transformer's internal values (including intermediate FNN computations) remain within the log-precision bound for all input lengths. (Note: the reviewer's specific concern about fixed FNN weights changing the asymptotic growth rate is incorrect — fixed constants multiplied by polynomially-growing values remain polynomial — but the sketch is still far too terse for the significance of the claim.)

### Minor

1. **FNN construction details and size bounds are not argued for complexity lower bounds.** The paper assumes that the FNNs used to check tiling conditions in the reductions can be built with polynomial size in the tiling system. For the undecidability result (Theorem 1), polynomial size is not required, but for the NEXPTIME-hardness and NP-hardness lower bounds (Theorems 3 and 5), the reductions must be polynomial-time. The paper says "specifically built feed-forward neural networks" (line 389) without arguing that these FNNs are of polynomial size or providing a concrete construction. This gap is partially mitigated by standard results (two-layer ReLU networks can implement logical conditions with polynomial size), but the paper should at least reference this.

2. **Proof sketch for Lemma 2 (linear attention) is described behaviorally without a construction.** The lemma states that an attention head can attend to positions based on a linear function of the input values. The paper describes the desired behavior but does not provide even a sketch of how the scoring function \(N(\langle Q\mathbf{x}, K\mathbf{y}\rangle)\) achieves this. For a theoretical paper, the plausibility is clear but the reader cannot verify the construction without filling in significant details.

### Trivial

None.

## Nice-to-Haves

- A brief discussion of how these worst-case complexity results relate to the feasibility of verification tools in practice (e.g., whether practical instances are likely to be easier than the worst case).
- Explicit treatment of how the FNNs in the reductions can be realized with a bounded number of layers/hidden units polynomial in the tiling system size.

## Removed Points

These points from the reviews are removed with justification:

1. **FNN weights producing super-polynomial values in log-precision proof (Harsh Critic's "Critical Issues" point 1).** The critic claimed that fixed FNN weights could amplify values beyond the log-precision bound. This is incorrect: fixed constants multiplied by polynomially-growing values produce polynomially-growing values. Asymptotic growth is unaffected by fixed multiplicative constants. The weakness is factually wrong and removed.

2. **Definition of attention head as tuple (score, pool) is non-standard.** This is a formatting/presentation nitpick that does not affect the validity of results.

3. **Fixed-width arithmetic definition is too vague.** The paper explicitly states it uses a high-level view and cites rigorous definitions from Baranowski et al. (2020) and Constantinides & D (2020). This is a deliberate scope choice, not a flaw.

4. **Criticism about overflow in Theorem 5 (NEXPTIME-hardness for fixed-width arithmetic).** The critic claims the embedding's quadratic sum term would overflow fixed-width arithmetic for the required word lengths. However, the constructed TE \(T_{\mathcal{S},n}\) is built for a specific \((\mathcal{S}, n)\). The bit-width \(b\) can be chosen as part of the construction to accommodate values up to \(O(n^2)\), and since \(n\) is binary-coded, \(b = O(\log n)\) is polynomial in the input size. The reduction is valid. This criticism misunderstands the standard practice of embedding parameters into the constructed instance.

5. **Strength Finder's generic strengths.** Claims like "clear problem definition" and "honest discussion of limitations" are retained as appropriate, but claims about importance of the research question and value to the community (when phrased generically) are removed as they lack specific evidence beyond the paper's own framing.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any genuinely novel perspective that the paper itself does not already present.

## Suggestions

1. **Complete the proof of Lemma 3.** The small-word property is central to Theorem 4 and must be fully argued, even if only as a detailed sketch, in the main text.

2. **Provide a citation or brief proof for the hardness of the bounded octant word-tiling problem.** Either reduce from the classic bounded tiling problem (which is NEXPTIME-complete) or cite a source where the octant variant is proven hard. Without this, the lower bounds are unsupported.

3. **Expand the proof sketch for Theorem 2 (log-precision undecidability)** to include a concrete bound showing that all intermediate values in the constructed transformer are polynomial in \(n\) and therefore representable with \(O(\log n)\) bits.

4. **Briefly address FNN size** in the reductions used for complexity lower bounds, either by providing a concrete construction or citing known results about the size of ReLU networks implementing boolean conditions.
