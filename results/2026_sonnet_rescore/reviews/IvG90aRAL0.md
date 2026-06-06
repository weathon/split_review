## Summary
The paper proposes quantum-accelerated Frank-Wolfe (FW) algorithms for projection-free sparse convex optimization across vector domains (ℓ₁ ball, simplex, latent group norm) and matrix domains (nuclear norm). Using quantum superposition over gradient finite differences, Durr-Hoyer minimum/maximum finding, quantum singular value estimation, and ℓ₂ tomography, the authors achieve per-round query/time improvements of O(√d) or better over classical FW. For the vector domain, Theorem 1 achieves Õ(√d/ε) query complexity versus classical O(d); for the matrix domain, two algorithms (QTSVE and QPM) achieve Õ(rd/ε²) and Õ(√rd/ε³) update-step time, respectively.

---

## Strengths

1. **Rigorous, concrete quantum speedups in the vector domain**: Theorem 1 and Theorem 2 achieve Õ(√d log(C_f/ε)) queries per round for ℓ₁ and simplex constraints (Table 1), versus O(d) classically — a clean O(√d) reduction with explicit convergence guarantees. The key insight that FW iterates are sparse after t steps (at most t nonzero coordinates), enabling efficient incremental quantum state preparation O(t) per round, is a genuinely elegant observation that decouples state-preparation cost from dimension d.

2. **Novel unified quantum subroutine pipeline for the linear subproblem**: The paper designs a coherent pipeline — forward-difference gradient oracle (Lemma 3) → quantum maximum finding over non-uniform states (Lemma 4) — for the FW linear oracle. The error propagation from approximate gradients into FW convergence via Lemma 1 and Lemma 2 is carefully worked out and gives fully specified algorithms (Algorithm 2, Algorithm 3, Algorithm 4) rather than asymptotic sketches.

3. **Breadth across constraint types**: Theorem 6 extends the approach to latent group norm constraints with an O(√|𝒢|) speedup by coherently computing dual norms across groups in superposition — a non-trivial generalization that shows the technique is not ad-hoc.

4. **Quantified Lipschitz-continuous case (Theorem 5)**: Using Jordan's bounded-error algorithm reduces per-iteration query complexity to O(1) at the cost of more qubits and O(d log d) gates per round, and the abstract appropriately qualifies this tradeoff.

5. **Novel matrix-domain algorithms**: The QTSVE approach (Section 4.1) simplifies the Bellante et al. top-k singular vector extraction by replacing repeated sampling via quantum maximum finding; the QPM approach (Section 4.2) directly accelerates power iteration with quantum matrix-vector multiplication. Both are properly attributed and independently motivated.

---

## Weaknesses

### Fatal
None.

### Major

- **Table 2 is inconsistent with Theorem 3 and Theorem 4.** This is the most concrete problem in the paper, verifiable directly:

  - *QTSVE row in Table 2 (line 88)*: `Õ(σ₁²(M)d / ((σ₁-σ₂)ε²) + T∇)`
  - *Theorem 3 body (line 241)*: `Õ(r·σ₁³(M_t)·d / ((σ₁(M_t)-σ₂(M_t))·ε²))`
  
  The Table 2 entry drops the rank factor r entirely and reduces σ₁ from exponent 3 to 2 — a factor of rσ₁ — with no explanation. Since the condition for quantum advantage depends on r (as stated in the text following Theorem 3: "Algorithm 3 reduces a O(dε/rσ₁²(M)) factor to the power method"), the missing r in Table 2 makes the central comparison table untrustworthy.

  - *QPM row in Table 2 (line 89)*: `Õ(σ₁(M)√d / (1-σ₁(M)γ'_min)·ε³ + T∇)` — has explicit ε³ dependence.
  - *Theorem 4 body (line 294)*: `Õ(√r·σ₁⁴(M_t)·d / (1-σ₁(M_t))³·γ_min^{2.5})` — has no explicit ε in the expression, different dependence on σ₁ and the spectral gap, and an explicit r absent from Table 2.
  
  These discrepancies cannot be reconciled at a glance and require revision. The theorem bodies and Table 2 must agree (up to simplified notation that should be explained).

- **Quantum advantage condition for the matrix case is not clearly stated.** The headline "at least O(√d) speedup" for the matrix algorithms is stated unconditionally in the abstract but only holds in a specific regime. From the text following Theorem 3 (line 243), Algorithm 3 reduces a factor O(dε/rσ₁²(M)) relative to the power method — which is >1 (i.e., quantum wins) only when ε > rσ₁²(M)/d. For precision targets smaller than this threshold, the quantum algorithm's ε² denominator means it is slower than the classical power method's ε denominator. The abstract and Section 4 discuss only the "at least O(√d) speedup" without stating the regime. The paper should give an explicit corollary or remark identifying the joint conditions on d, r, σ₁, and ε under which each quantum algorithm dominates.

### Minor

- **Theorem 4 ε-transparency.** The complexity expression in the Theorem 4 statement has no explicit ε, while Table 2 shows ε³ and the parameter setting defines k_t = O(σ₁ ln d / ε) with explicit ε. The ε dependence is absorbed implicitly through k_t and δ_t, but the final expression in the theorem body should display the ε scaling after parameter substitution — as Table 2 and the abstract do. Readers cannot verify the ε³ claim from Theorem 4 alone without rederiving the substitution.

- **Dequantization not discussed.** The matrix-domain algorithms rely on the Kerenidis-Prakash QRAM quantum access model (Assumption 4), which is precisely the access model targeted by Tang-style dequantization results. The paper makes no mention of whether classical sample-access algorithms could achieve similar bounds. For a claim of quantum advantage in the matrix domain, at least a brief acknowledgment of this line of work and why or whether it does not apply here is warranted.

### Trivial

- The text following Theorem 3 says "Algorithm 3 reduces a O(dε/rσ₁²(M)) factor to the power method" — grammatically awkward ("reduces… a factor… to" should be "reduces the runtime by a factor of…"). Minor presentation fix.

---

## Nice-to-Haves

- A brief regime diagram or table for the matrix case, mapping out which algorithm (QTSVE vs QPM vs classical power method vs Lanczos) is optimal for which joint conditions on (d, ε, r, σ₁) — this would substantially clarify the practical value of the two complementary quantum algorithms.
- A remark on whether QRAM construction time O(d²) is subsumed within T∇ or is additional overhead. The paper follows "the classical convention of excluding gradient evaluation time" (Remark 3), but the cost of populating the QRAM tree with freshly-computed gradient entries each iteration is distinct from the gradient computation itself. Clarifying whether this is O(d²) amortized or free would strengthen the matrix-case claims.
- A brief mention of dequantization/sample-complexity classical lower bounds to help readers assess the robustness of the claimed quantum advantage in the matrix case.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"QRAM cost is not accounted for and may eliminate the quantum advantage."** (Harsh critic, structural claim) — The paper explicitly invokes the standard QRAM access model (Assumption 4) with Remark 3 noting it follows "the classical convention of excluding gradient evaluation time Jaggi (2013)." This is standard practice in QRAM-based quantum ML papers. Demoted to a nice-to-have clarification rather than a structural flaw; the assumption is widely used in the community.

- **"The O(1) query claim for Theorem 5 is misleading because gate cost is O(d log d)."** (Harsh critic) — The abstract already says "at the cost of more qubits and additional gates," and Table 1 explicitly lists O(d log d) gates. The tradeoff is disclosed in the paper. Not a real weakness.

- **"Jordan's algorithm speedup exists only in oracle query complexity, not computational time."** (Harsh critic) — The paper is clear on this distinction. The Theorem 5 claim is about query complexity and the gate overhead is correctly tabulated. Not a weakness.

- **Strengths about applications (sparse regression, AdaBoost, SVMs)** — The applications section lists many potential beneficiaries, but quantum hardware assumptions behind practical advantage are not addressed. This is standard for theoretical quantum algorithms papers, and the claim is about asymptotic complexity rather than practical deployment. This is not a weakness, but the strength claim "wide range of critical applications can benefit" is aspirational rather than concretely demonstrated.

- **Generic strength: "clear benchmarking against classical baselines"** — Weakened because Table 2 has the verified inconsistencies described above. The statement that Tables 1 and 2 "help the reader immediately assess the magnitude of the quantum advantage" is inaccurate for Table 2 given the r/σ₁ discrepancies.

---

## Novel Insights

The key conceptually novel observation is the exploitation of FW iterate sparsity for efficient quantum state preparation: because FW from a zero initialization produces solutions with at most t nonzero coordinates after t steps, the quantum state |x^(t)⟩ admits incremental construction in O(t) gates per round, keeping state-preparation overhead entirely decoupled from the ambient dimension d. This is not a quantum trick imported from the literature but a structural property of FW that the paper leverages cleanly. The QTSVE simplification — replacing the threshold-search and repeated sampling of Bellante et al. with a single application of quantum maximum finding — is a concrete improvement with independent interest for quantum SVD-based methods.

---

## Suggestions

1. Fix Table 2 to match the theorem statements exactly — either correct the theorem bodies or update Table 2 entries, and document any simplifications (e.g., fixing σ₁ = O(1)) as explicit remarks.
2. Add an explicit remark or corollary after Theorem 3 stating the condition ε > rσ₁²(M)/d under which Algorithm 3 beats the classical power method, and the analogous condition for QPM vs Lanczos.
3. Update Theorem 4 to show explicit ε dependence in the complexity expression after substituting k_t and δ_t, consistent with the abstract's Õ(√rd/ε³) statement.
4. Add a brief remark acknowledging the dequantization question for the QRAM-based matrix algorithms.

---

**Evaluation summary:**

| Axis | Assessment |
|---|---|
| Originality | Good: first quantum treatment of matrix FW; new QTSVE simplification and QFW-latent-group-norm are genuine |
| Importance | Moderate-high: FW algorithms are widely used; quantum speedups in d are meaningful if hardware matures |
| Claims supported | Mixed: vector domain claims are fully supported; matrix domain headline speedup is conditionally correct but the supporting table (Table 2) is internally inconsistent with theorems |
| Soundness of experiments | N/A (theory paper); proof structure for vector domain appears sound; matrix domain has presentation inconsistencies |
| Clarity of writing | Adequate in vector domain; matrix domain has transparency issues in Theorems 3–4 and Table 2 |
| Value to community | Moderate-high: provides a systematic quantum FW framework; the Table 2 issues must be resolved for the comparison to be trusted |

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>3</originality>
<importance>3</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>3</clarity>
<community_value>3</community_value>
</subscores>