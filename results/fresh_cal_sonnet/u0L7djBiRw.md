Now let me run the calibration search in parallel with reading more of the paper.Let me read one of the middle-range calibration papers and then do the narrowing search.Initial bracket: **4.5 – 6.5**. The paper's algorithmic novelty with theoretical guarantees puts it in the middle tier, but the missing P-SRHT baseline and absent proof sketch weaken it. Let me narrow with round 2.Let me read the FastLSH paper (4.5) and the HyperAttention paper (6.33) for precise calibration.Now I have enough to write the final review. Let me compare the paper against the calibration anchors:

- **FastLSH (4.5, Rejected)**: Very similar spirit — fast version of a randomized technique with theoretical guarantees. FastLSH was rejected partly because its guarantees were only asymptotic; the paper under review has finite-sample non-asymptotic guarantees (Theorem 6 matches Rademacher exactly). The RLE paper is stronger than FastLSH.
- **Matrix Product Sketching (5.75, Accepted)**: Revisits a well-studied sketching problem, clean theory + experiments, accepted. The paper under review is somewhat comparable but has the missing P-SRHT baseline and no ablation.
- **HyperAttention (6.33, Accepted)**: Addresses a more prominent problem (LLM attention) with stronger experiments. The RLE paper is weaker on experimental completeness.

**Round-1 bracket:** 4.5 – 6.5  
**Round-2 narrowing:** The paper lands between FastLSH (4.5) and Matrix Product Sketching (5.75), closer to the latter. Score: **5.0**

---

## Summary

The paper proposes a Rademacher-Like Embedding (RLE) that embeds an *n*-dimensional vector into *k*-dimensional space in O(n + k²) time and space using a compact Rademacher matrix and auxiliary random arrays, instead of an explicit *k×n* matrix. Theorems 1–6 establish that the implicitly generated matrix inherits the key statistical properties of Rademacher embedding and achieves the same oblivious ℓ₂→ℓ₂ subspace embedding guarantee (Theorem 6, matching Balabanov & Nouy 2019). Numerical results on single-pass RSVD and randomized GMRES show 1.5–1.7× and 1.3× average speedups respectively while preserving or improving accuracy.

---

## Strengths

- **Linear complexity with non-asymptotic guarantees (Theorems 1–6):** Theorem 1 gives O(n + k²) time/space; Theorem 3 establishes that RLE's rows are mutually independent and entries within each row are mutually independent (each ±1/√k with equal probability); Theorem 6 then establishes that RLE achieves the *same* (ε, δ, d) oblivious ℓ₂→ℓ₂ subspace embedding dimension bound as full Rademacher embedding (k ≥ 7.87ε⁻²(6.9d + log(1/δ))). This is a finite-sample, non-asymptotic guarantee, not merely a limiting result.

- **Cache-friendly dense arithmetic:** The method avoids the sparse data structures of sparse sign embedding, which suffer from irregular memory access. This architectural advantage is confirmed empirically—the speedups are real and consistent across both application domains.

- **GMRES validation is convincing:** Figure 2 shows that RLE tracks the standard Arnoldi convergence curve closely across three large sparse test cases (up to 5.6M × 5.6M), while running 1.3× faster than P-SRHT and sparse sign. This is the strongest evidence in the paper.

- **E[Θ^TΘ] = I always (not just in expectation):** As shown in Theorem 4, the diagonal of Θ^TΘ is *always* 1 (not just in expectation), because each entry of Θ is always ±1/√k. This is a stronger property than it appears.

---

## Weaknesses

### Fatal
None.

### Major

- **P-SRHT is absent from the RSVD comparison (Table 1).** Section 4.2 includes P-SRHT as a competitor in the GMRES experiments, and Section 2.1 introduces P-SRHT as the primary O(n log n) accelerated alternative to dense embeddings. Its absence from Table 1 (the primary RSVD evaluation) is unexplained and asymmetric. Since P-SRHT is faster than Gaussian embedding in many regimes and is the most natural competing baseline for this experiment, omitting it leaves the most important competitor out of the paper's headline table. The abstract's claim of "1.7× speed-up on average" is stated without clarifying that this is relative to sparse sign embedding, not P-SRHT; the Gaussian comparison yields only 1.5×.

### Minor

- **No hyperparameter ablation for ξ, ζ, ω.** The paper uses ξ=2, ζ=1, ω=2 throughout all experiments without justification or sensitivity analysis. The choice ζ=1 (P is a single Rademacher row) is the most aggressive possible setting, and the claim that it is "safe in practice" is asserted but not demonstrated. A small ablation varying ζ ∈ {1, 2, 3} would let readers understand the speed-accuracy tradeoff and give guidance for deployment.

- **Theorem 6 is stated in the main text without any proof sketch bridging it to the prior theorems.** Theorem 3 establishes that RLE's rows are mutually independent and within-row entries are mutually independent—this directly matches the statistical structure needed to apply existing Rademacher subspace-embedding proofs (e.g., matrix Chernoff bounds). A single sentence explaining "Theorem 6 follows by applying the standard Rademacher argument from Balabanov & Nouy (2019) to the independent row structure established in Theorem 3" would make the headline result verifiable in the main text. Without this bridge, a reader cannot judge whether the proof is routine or non-trivial.

- **"Remarkably smaller" 2-norm error claim is not supported by variance estimates.** Section 4.1 states the RLE's relative 2-norm error is "remarkably smaller than Gaussian embedding and sparse sign embedding." Since all three methods converge to the same optimal rank-k approximation in expectation, a single run showing one method appearing better could reflect random variation rather than a systematic advantage. The paper should either report averages over multiple runs or temper this language.

### Trivial

- The abstract reports "1.7× speed-up on average" without specifying this is the comparison to sparse sign embedding. The comparison to Gaussian embedding gives 1.5×. Selective reporting of the larger number without context is mildly misleading.

---

## Nice-to-Haves

- A brief confirmation that all tested (n, k) pairs satisfy k ≤ O(n^{1/2})—e.g., for the 5.6M × 5.6M matrix with k=200, k² = 40,000 ≪ 5.6M—would close an unnecessary gap for readers checking the linear complexity claim.
- The paper could show how the (ε, δ, d) guarantee from Theorem 6 translates into the convergence bound for the sketched OLS in Algorithm 2, tightening the connection between the theory and the GMRES experiments rather than presenting them as parallel sections.
- The parallel version mentioned in the conclusion (§5) would be a natural follow-up, and a brief analysis of expected speedup from parallelization would strengthen the paper's forward-looking claims.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

**From the Harsh Critic:**

- *"The proof of Theorem 5 is absent from the main text."* — This is a PDF parser artifact. The proof exists in the appendix of the original submission, which is stripped from all evaluated papers. **Removed.**

- *"The proof of Theorem 3 is incomplete regarding shared signs S for columns mapping to the same bucket."* — The proof as written says entries in the same row "depend on different entries of P." While terse, the argument is correct in spirit: entries y_i = Σ_j sum_{a,b,j} * c where a = R_i, b = E_{a,i,j}, c = S_{a,i,j}—each output element i uses a different slice of S indexed by j, so even when two columns hash to the same bucket (same partial sum), the sign applied per output element is distinct. The criticism identifies a valid terseness issue, but it does not identify a logical gap. **Demoted to Trivial presentation issue but already captured in the Theorem 6 proof sketch point.**

- *"Figure 1 uses ζ=2 while all experiments use ζ=1."* — This is intentional; the figure is an illustrative diagram, not an experiment. Using ζ=2 makes the diagram more informative. **Removed as a formatting nitpick.**

**From the Strength Finder:**

- *"Clear, explicit algorithmic description: Algorithm 3 and Figure 1 give a step-by-step account."* — The harsh critic correctly notes that the figure (ζ=2) and algorithm (ζ=1 in experiments) are not always reconciled, and the description is somewhat difficult to follow. Generic presentation praise dropped. **Removed.**

- *"Small constant parameters: ζ=1, ξ=2, ω=2 show tiny overhead."* — The claim that these constants are "indeed tiny" is partially undermined by the lack of ablation; we don't know whether ζ=2 would give substantially better accuracy at modest cost. Strength is weakened to background context. **Removed as standalone strength.**

---

## Novel Insights

The method's core innovation—using a compact ζ-row Rademacher matrix as a "basis" and reassembling output elements via shared partial sums weighted by random signs—effectively decouples the statistical independence requirement (needed for embedding guarantees) from the cost of explicitly enumerating the full k×n matrix. The key observation is that Theorem 3's mutual independence of rows, combined with mutual independence of entries within each row, is *sufficient* to inherit the Rademacher subspace embedding bound from Balabanov & Nouy (2019), even though full mutual independence across all n×k entries does not hold. This shows that many classic random-matrix guarantees rely on row-level independence rather than full entry independence—a structural insight with potential applicability to designing other linear-complexity random matrices.

---

## Suggestions

1. **Add P-SRHT to Table 1.** It is already implemented for Section 4.2; reporting its RSVD speed and error would cost minimal effort and would make Table 1 complete.
2. **Add a ζ ablation.** Report timing and accuracy for ζ ∈ {1, 2, 3} on one representative test case. This directly addresses the question of whether ζ=1 is genuinely sufficient.
3. **Add a one-sentence proof sketch for Theorem 6** in the main body: identify which property of the prior theorems makes the Balabanov & Nouy proof apply.
4. **Report variance.** Run each experiment 5–10 times (with different random seeds) and report mean ± std for timing and error. This would validate the "remarkably smaller error" claim and confirm that speedups are repeatable.

---

## Score and Decision

**Calibration anchors:**

| Path | Avg Score | Round | Comparison to paper under review |
|------|-----------|-------|----------------------------------|
| `BvQkjCnXXr.md` (FastLSH) | 4.50 | R2 | Similar spirit (fast randomized algorithm with theoretical guarantee); weaker because its guarantees are asymptotic only and it misses a key ingredient vs. prior work. RLE paper is clearly stronger. |
| `5dpuLgwQ0d.md` (Finding Clusters) | 4.75 | R2 | Nearly-linear clustering algorithm; different problem. Less relevant. |
| `tra8ktyk0E.md` (Dynamic KDE) | 5.50 | R2 | Dynamic sketching with theory + empirics; comparable scope but different problem. |
| `eHfq8Q3LeD.md` (Matrix Product Sketching) | 5.75 | R1+R2 | Closest in structure: new sketching algorithm, theory + two applications. Slightly stronger: cleaner evaluation, no missing baselines. |
| `Frok9AItud.md` (Node Similarities) | 5.80 | R1+R2 | Random projections + applications; different focus. Comparable tier. |
| `Eh0Od2BJIM.md` (HyperAttention) | 6.33 | R2 | Linear-time approximate algorithm for prominent problem; stronger applications and more complete experiments. RLE paper is weaker. |
| `tDIL7UXmSS.md` (Quantum D²-sampling) | 6.50 | R2 | Quantum-inspired k-means++ with theoretical guarantees. Higher novelty and impact. |
| `RsJwmWvE6Q.md` (Optimal Sketching) | 6.75 | R1 | Tight sketching bounds with matching lower bounds—stronger theoretical contribution. |

**Round-1 bracket:** 4.5 – 6.5  
**Round-2 narrowing:** The paper is clearly above FastLSH (4.5) due to non-asymptotic guarantees, better experimental coverage, and explicit acknowledgment of the mutual-independence limitation. It falls below Matrix Product Sketching (5.75) due to the missing P-SRHT baseline in Table 1 and the absent hyperparameter ablation. These are real, fixable gaps rather than fatal flaws, but they do reduce credibility at the paper's current stage. The paper lands at **5.0**.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>