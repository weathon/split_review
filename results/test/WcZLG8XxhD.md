## Summary

This paper extends learning-augmented streaming to the matrix setting, with two main contributions: (1) a learning-augmented Misra-Gries algorithm for frequency estimation that matches the state-of-the-art bound of Aamand et al. (2023) using a simpler, deterministic single-sketch approach, and (2) the first learning-augmented variant of the Frequent Directions algorithm for matrix streaming, with theoretical error bounds under Zipfian singular values and experimental results showing 1–2 orders of magnitude improvement over standard FD on real video/hyperspectral datasets.

## Strengths

- **Simpler, deterministic algorithm matching state-of-the-art for learned frequency estimation.** The learning-augmented Misra-Gries algorithm (Theorem 3.2) achieves Θ(1/m · n/(ln d)²) expected error under a perfect oracle, matching Aamand et al. (2023) but using a single deterministic Misra-Gries sketch instead of multiple CountSketch tables with O(log log n) overhead. The proof sketch is provided (lines 117–123) and experiments on CAIDA and AOL show it is competitive with or outperforms learned CS++ without requiring tunable hyperparameters (Figure 2, Section 4.2).

- **First learning-augmented algorithm for the matrix streaming (Frequent Directions) problem.** The paper generalizes the learning-augmented framework from 1D frequency estimation to high-dimensional vector streams, defining a weighted error (Equation 2) that reduces to the standard frequency estimation error as a special case (lines 33–45). Algorithm 2 projects input vectors onto predicted and orthogonal subspaces, each handled by a separate FD sketch. Experiments on four real video/hyperspectral datasets (Hyper, Logo, Friends, Eagle) demonstrate 1–2 orders of magnitude improvement over standard FD (Figure 1).

- **Clean theoretical unification.** The paper shows explicitly (lines 35–45) that frequency estimation is a special case of matrix streaming: when input vectors are standard basis vectors, the weighted error (Equation 2) reduces to Equation (1), and Algorithm 2 reduces to learned Misra-Gries. This provides a principled generalization rather than an ad-hoc extension.

- **Robustness for the Misra-Gries case is well handled.** Section 3.1 (line 127) shows that the learned MG algorithm retains the worst-case guarantees of classic MG regardless of predictor quality, because half the space is used for exact counts of predicted heavy hitters and the other half for a standard MG sketch. The analysis also covers imperfect oracles (line 127).

## Weaknesses

### Major

None.

### Minor

- **The FD experiments use the first matrix's exact SVD as the "predictor," which is a favorable setup and differs from the usual learning-augmented pipeline.** Section 4.1 (line 146) states: "we use the top singular vectors of the first matrix in the sequence to form the prediction." While this is transparently described and works well due to temporal similarity, it is not "predictions trained on past data" in the usual sense — it is an exact SVD computed on the first time step, which the streaming algorithm is designed to avoid. The abstract's phrasing ("predictions trained on past data") slightly overstates this. A natural follow-up would be to test predictors learned from past matrices in a leave-one-out setup or from a training set.

- **No experimental evaluation of the robust variant for Frequent Directions.** The paper acknowledges (line 133) that Algorithm 2 "does not come with a robustness guarantee" and describes a modification using residual error estimation (Li et al., 2024), with theoretical results in the appendix (Theorem E.1–E.2). However, Section 4.1 tests only the non-robust version. While the paper is transparent about this limitation, evaluating the robust variant (or at least discussing whether the non-robust algorithm happens to be robust on the tested datasets) would strengthen the empirical case.

- **Frequency estimation experiments do not include a non-learned MG baseline.** The comparisons are against learned CountSketch and learned CS++ only (Section 4.2). Including the non-learned MG baseline would allow readers to directly see the improvement attributable to learning. (The contribution does not hinge on this, but it is an omission worth noting.)

- **Figure 2 interpretation could be clearer.** The paper mentions that CS++ has a tunable hyperparameter C and that "sometimes our algorithm outperforms the best hyperparameter choice CS++," but it is not explicitly stated which C values were tried or how the single CS++ curve shown corresponds to these choices. The caption says "Randomized algorithms are averaged across 10 trials and one standard deviation is shaded," but does not specify which C value or values the curve represents.

### Trivial

- Theorem 3.4's bound as stated in the main text does not show explicit dependence on $m_L$ (the number of predicted directions). In the perfect-oracle case the bound is Θ((1/(ln d)²) · ‖A‖_F² / m), and the dependence on $m_L$ is implicit in the space allocation. Clarifying this in the theorem statement would help readability.

- The choice of τ = 0.5·m_L and τ = 0.5·(m−2m_L) in Algorithm 2 (lines 89–90) is not discussed. A brief justification would be helpful.

- The bound of Theorem 3.3 is garbled in the extracted text (a parser artifact); in the original submission this would have been readable.

## Nice-to-Haves

- Include the non-learned MG and non-learned FD as baselines in all experimental plots to quantify the lift from learning.
- Test the robust variant of learned FD (from Appendix E) on the same datasets, or include a discussion of why the non-robust algorithm appears empirically robust in these settings.
- Consider a more realistic predictor for the FD experiments, e.g., trained on past matrices via a learned low-rank mapping, to match the "learning-augmented" framing more closely.
- State the bound of Aamand et al. (2023) explicitly when claiming the match.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Theoretical analysis of FD is absent / proofs entirely omitted."** The paper states (line 107) that proofs for Theorems 3.3 and 3.4 follow similar techniques to the MG case, and the appendix (stripped by the parser) contained the full analyses including Theorems E.1–E.2 on robustness. Per hard rules, missing appendix content stripped by the parser is not a valid criticism.

- **"Theorem 3.1 bound has a suspicious form that can be negative/undefined."** The bound Θ(ln(m/ln(d/m)) · ln(d/m)/(ln d)² · n/m) is well-defined and positive in the standard asymptotic regime (d > m, m sufficiently large relative to d). The edge case where m/ln(d/m) < 1 occurs only for extreme parameter choices outside the meaningful streaming regime. This is not an error; it is standard asymptotic notation.

- **"The claim of matching Aamand et al. is not substantiated."** The paper cites Aamand et al. (2023) and states the match. Explicitly quoting the prior bound would be nice but is not required; the reader can verify the cited work.

- **"Missing related works."** Per hard rules, I cannot confirm the existence of missing references.

## Novel Insights

The reviews reveal that the paper occupies an interesting position: the learned Misra-Gries contribution is clean, self-contained, and fully validated (theory + experiments + robustness), while the learned FD contribution is more ambitious but also less fully developed — the prediction methodology is a special case, the robustness fix is theoretical only (deferred to the appendix), and the experiments evaluate only the non-robust variant. This asymmetry is not a flaw per se (the FD extension is genuinely novel), but it means the paper's two halves should be judged somewhat differently. The MG half is polished and complete; the FD half is a promising but more preliminary extension that would benefit from tighter integration between the theory and the experimental design. The paper's core value lies in demonstrating that the learning-augmented framework can meaningfully generalize to matrix streaming, not just frequency estimation.

## Suggestions

- Clarify the FD prediction methodology in the abstract and introduction — frame it as "warm-start using the SVD of the first matrix in the sequence" rather than "predictions trained on past data," or implement a genuinely learned predictor.
- Add a brief paragraph discussing why the non-robust FD algorithm performs well on the tested video datasets despite the known adversarial failure mode — this would address a natural reader concern.
- Include the non-learned MG baseline in Figure 2 and the non-learned FD baseline already shown (it is shown in Figure 1, so this is only a concern for the frequency estimation experiments).
- Tighten the presentation of Theorem 3.4 to show the bound's dependence on space allocation more explicitly.

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>