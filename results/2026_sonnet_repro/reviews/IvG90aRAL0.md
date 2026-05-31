Now let me run the calibration search.**Round 1 bracket: 5.0 – 6.5**

Now narrowing with round 2 search inside this bracket.Now I have enough information to write the complete review. Let me finalize my analysis of the paper.

---

## Summary

This paper proposes quantum Frank-Wolfe (QFW) algorithms for projection-free sparse convex optimization, covering both the vector domain (under ℓ₁-ball, simplex, and latent group norm constraints) and the matrix domain (under nuclear norm constraints). For the vector case, the algorithms achieve Õ(√d/ε) query complexity by combining quantum superposition over finite-difference gradients with Durr-Hoyer maximum finding, and O(1/ε) queries using Jordan's algorithm for Lipschitz objectives. For the matrix case, two algorithms are proposed: a Quantum Top Singular Vector Extraction (QTSVE) method achieving Õ(rσ₁³d/(σ₁−σ₂)ε²) update cost, and a Quantum Power Method (QPM) achieving Õ(√rd/ε³), both claimed to offer at least O(√d) speedup over classical baselines.

---

## Strengths

- **Clean O(√d) per-iteration query speedup in the vector domain:** Theorem 1 reduces per-round calls to the function value oracle from O(d) classically to Õ(√d), directly via quantum maximum finding over forward-difference gradient approximations. The analysis cleanly couples Lemma 2 (finite-difference error bound), Lemma 3 (gradient circuit), and Lemma 4 (quantum max finding) into an end-to-end convergence proof satisfying the FW approximate subproblem criterion (Lemma 1/Jaggi 2013). This is technically sound and clearly presented.

- **Systematic coverage of structured constraint sets:** The paper extends results uniformly across ℓ₁-ball, simplex (Theorem 2), and latent group norms (Theorem 6), achieving O(√|𝒢|) speedup in the last case. The framework also accommodates two distinct gradient oracle models (function-value and Lipschitz/Jordan), showing the authors understand the tradeoffs between oracle assumptions.

- **Novel observation on sparse state preparation:** The paper correctly identifies that FW iterates initialized at 0 and updated with standard basis vectors have at most t nonzero components after t steps, making state preparation for |x^(t)⟩ efficient (O(t) gates) and completely decoupled from d. This is a genuinely useful structural insight specific to the Frank-Wolfe setting.

- **Two complementary matrix algorithms with rigorous convergence:** QTSVE (Section 4.1) and QPM (Section 4.2) are well-motivated as complementary approaches (different rank/precision tradeoffs), each with full parameter settings and convergence proofs. The QTSVE's extension of quantum maximum finding to non-uniform states (Lemma 4 final clause) is a non-trivial technical contribution.

- **Function-value oracle model:** Unlike Chen & de Wolf (2023) who require precomputed matrix factors and a closed-form gradient, this paper works with only a function value oracle, making it applicable to a broader class of objectives. This is clearly stated and appropriately differentiated.

---

## Weaknesses

### Fatal
None.

### Major

- **Table 2 vs. Theorem 3 inconsistency — the main comparison table is internally inconsistent with the stated theorem.** Theorem 3 (page 7) gives complexity Õ(r·σ₁³(M_t)·d / (σ₁(M_t)−σ₂(M_t))·ε²). Table 2 (page 3) lists the QTSVE complexity as Õ(σ₁²(M)d / ((σ₁(M)−σ₂(M))·ε²)), which drops the rank factor r entirely and reduces σ₁'s exponent from 3 to 2. Since r determines when the quantum algorithm actually dominates classically (the factor reduction stated in Section 4.1 is O(dε/(rσ₁²(M))), which exceeds 1 only when ε > rσ₁²/d), omitting r from Table 2 makes the table's comparison with classical methods unverifiable at face value. This is in the main paper and directly undermines the central matrix-case claim.

- **ε-dependence degradation is not transparently characterized.** The quantum speedup in d is real, but it is purchased at the cost of worsened ε exponents: the classical power method costs O(d²/ε) while QTSVE costs Õ(rd/ε²) and QPM costs Õ(√rd/ε³). The paper acknowledges this implicitly: "Algorithm 3 reduces a O(dε/rσ₁²(M)) factor to the power method" — but this factor is less than 1 precisely when ε < rσ₁²/d, i.e., the regime where algorithms are typically run. The paper never states the joint condition on (d, ε, r, σ₁) under which quantum dominates end-to-end, making it impossible to assess when the headline "at least O(√d) speedup" claim holds in practice. A short remark or corollary that maps the dominance regime would substantially strengthen the paper.

- **No discussion of dequantization for the matrix case.** The QTSVE and QPM algorithms both rely on Assumption 4 (the Kerenidis-Prakash quantum access model), which is precisely the setting where Tang-type dequantization results have shown that classical algorithms under sample-query access can achieve similar complexity. For a paper claiming quantum advantage in the matrix case using this access model, the absence of any discussion of whether these results are susceptible to dequantization is a real gap. The paper should at minimum acknowledge why or whether this line of work applies (or doesn't apply) to the FW setting.

### Minor

- **Theorem 4 does not transparently show ε dependence.** The theorem body states complexity Õ(√r·σ₁⁴(M_t)·d / (1−σ₁(M_t))³·γ'_min^{2.5}) with no explicit ε, while ε enters implicitly through k_t = O(σ₁(M_t)ln(d)/ε) and δ_t = εγ'_min/(16σ₁). The ε³ dependence visible in Table 2 and the abstract requires substituting these parameter choices into Lemma 9's complexity, which is not done in the theorem statement. A reader should not need to reconstruct this algebraically; the theorem should show the full substituted complexity.

- **QRAM preprocessing cost is not addressed.** Assumption 4 posits Õ(1) quantum access to M via a prebuilt QRAM data structure. The paper correctly follows the convention of excluding gradient evaluation time (Remark 3), but does not discuss whether QRAM construction (which costs at least Ω(d²) to insert all entries) is subsumed in T∇ or is an additional overhead. The paper should clarify this, even in a remark; in many applications this cost is amortized but it is field-specific and should be addressed explicitly.

### Trivial
None after filtering formatting artifacts.

---

## Nice-to-Haves

- A "regime table" mapping joint conditions on (d, ε, r, σ₁) for which each quantum algorithm is provably faster than each classical baseline end-to-end would turn Table 2 into an honest and practically useful characterization of quantum advantage, and would also clarify whether QTSVE and QPM are genuinely complementary (e.g., QTSVE better at small ε when d > rσ₁²/ε, QPM better at higher rank or lower precision).
- Lower bounds on quantum query complexity for the FW linear subproblem would significantly strengthen the contribution; without them it is unclear whether the algorithms are optimal.
- For the latent group norm extension (Theorem 6), a brief worked example (e.g., group Lasso) connecting the abstract setting to a concrete application would improve readability.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Applications list is overreaching"** (harsh critic): The applications paragraph (sparse regression, matrix completion, AdaBoost, SVMs) is standard framing for FW papers and is not a misrepresentation. Removed as scope criticism.
- **"Theorem 5 speedup is in queries only, not computational time"**: The paper explicitly states in Table 1 that Theorem 5 costs O(d log d) gates per round and O(d log(d/ε)) qubits. The abstract also says "at the cost of more qubits and additional gates." The paper does not claim a computational time speedup for Theorem 5. Claim is based on a partial misread; removed.
- **"The sparse state preparation is a known observation"**: The strength finder's claim about this being "novel" is somewhat overstated — sparse state preparation is a known technique — but the specific application to FW iterates and its implication for d-independence of state prep is a genuinely useful observation. Retained as a supporting strength but weakened.
- **Strength: "End-to-end convergence analysis"** — retained as a specific, grounded claim.
- **Strength: "Clear benchmarking against classical baselines"** — partially removed due to the Table 2 inconsistency; the benchmarking is present but flawed in the matrix case.

---

## Novel Insights

The combination of quantum gradient circuits (via finite differences in superposition) with the FW iteration's sparsity structure is the paper's genuinely novel contribution: because FW iterates over sparse domains accumulate at most t nonzero components after t steps, state preparation is O(t)-gate and dimension-independent, making the overall quantum oracle complexity scale as Õ(√d/ε) rather than d × (state prep cost). This coupling of the FW sparsity geometry with quantum superposition is not merely "applying Grover to FW" but requires careful error propagation through the approximate subproblem machinery of Jaggi (2013). The QTSVE simplification — using quantum maximum finding to bypass the repeated sampling and threshold search used in prior quantum SVD methods (Bellante et al. 2022) — is also a concrete technical improvement, though one that carries over naturally from the vector-case machinery.

---

## Suggestions

1. **Fix Table 2** to include the rank factor r in the QTSVE complexity row and correct the σ₁ exponent to match Theorem 3 (σ₁³, not σ₁²).
2. **Add a remark or corollary** specifying the regime (d, ε, r, σ₁) under which each quantum algorithm dominates its classical counterpart end-to-end.
3. **Add a brief discussion** (1–2 paragraphs) on whether dequantization results apply to the matrix-case algorithms, clarifying whether the KP access model is genuinely stronger than sample-query access in this FW setting.
4. **Restate Theorem 4** to show the explicit ε dependence after substituting the parameter choices k_t and δ_t.
5. **Add a remark** on QRAM construction cost and whether it is subsumed in T∇.

---

## Score and Decision

**Calibration anchors retrieved:**

| Path | Avg Score | Round | Comparison to paper under review |
|------|-----------|-------|----------------------------------|
| CrMyHiUttz.md | 3.00 | 1 | Rejected zero-sum game paper; far weaker contribution than ours |
| hqxzi4d3Ws.md | 3.00 | 1 | Rejected quantum noise resilience; different topic |
| pB1FeRSQxh.md | 6.00 | 1, 2 | Accepted quantum min-max optimization; has upper AND lower bounds, more complete than ours |
| XaARrKTNh3.md | 5.25 | 1, 2 | Rejected quantum PPA meta-algorithm; methodological gaps; comparable scope |
| XABvLUXQ45.md | 4.80 | 1, 2 | Rejected quantum sparse online learning; narrower scope, weaker results |
| tDIL7UXmSS.md | 6.50 | 1, 2 | Accepted quantum D²-sampling; dequantization + experiments; stronger paper |
| rUx0zQFwD1.md | 5.33 | 2 | Rejected quantum LP speedup; incremental improvement, similarly positioned |
| TUiEgloner.md | 4.75 | 2 | Rejected quantum Hamiltonians; different topic |
| dLrhRIMVmB.md | 8.00 | 1 | Accepted quantum TDA, implemented end-to-end; far stronger |
| fMTPkDEhLQ.md | 8.00 | 1 | Tight lower bounds paper; different standard |
| RsJwmWvE6Q.md | 6.75 | 2 | Accepted matrix norm sketching; tight bounds, cleaner |

**Round 1 bracket:** 5.0 – 6.5

**Round 2 narrowing:** Within the bracket, the strongest comparators are:
- *pB1FeRSQxh* (6.0, accepted): That paper provides matching upper and lower bounds for quantum min-max optimization, making it more complete. Our paper is weaker because of the Table 2 inconsistency and absence of lower bounds, and the ε-tradeoff for the matrix case is not characterized.
- *rUx0zQFwD1* (5.33, rejected): Comparable scope (incremental quantum speedup on optimization), rejected for methodological gaps. Our paper has stronger vector results but comparable matrix issues.
- *XaARrKTNh3* (5.25, rejected): Slightly weaker contribution than ours but similar judgment territory.
- *tDIL7UXmSS* (6.5, accepted): That paper also uses the KP/QRAM model but explicitly provides dequantization analysis — precisely what our paper lacks for the matrix case.

**Assessment:** The paper's vector-domain contributions are clearly solid (clean, well-supported O(√d) speedup). The matrix-domain contributions are real but marred by the concrete Table 2/Theorem 3 inconsistency (r factor missing) and the absent regime analysis. Compared to *pB1FeRSQxh* (6.0), this paper is weaker; compared to *rUx0zQFwD1* (5.33) and *XaARrKTNh3* (5.25), it is stronger in the vector case but has comparable matrix-domain issues. The paper sits closer to the lower end of the bracket.

**Final score: 5.0** — The paper makes genuine contributions, particularly in the vector domain, but the Table 2/Theorem 3 inconsistency in the main text, the undiscussed ε-degradation in the matrix case, and the missing dequantization analysis bring it to a weak reject position. The vector results alone would support a borderline accept, but the matrix results — which are the more novel claimed contribution — have concrete presentation and analysis gaps that require revision before acceptance.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>