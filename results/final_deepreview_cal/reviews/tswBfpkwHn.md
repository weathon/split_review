Now I have all the evidence I need. Let me compose the final review.

Round 1 bracket: I see clear separation. Weak anchors (avg 3.0-3.4) are papers with fundamental flaws or very tangential content — our paper is much stronger. Middle anchors (5.0-6.5) include closely matched theoretical ICL papers. Strong anchors (7.5+) are mostly applied papers on different topics. The plausible bracket is **5.0–6.5**.

Round 2 narrowing: The most relevant anchors are "Trained Transformer Classifiers" (6.0, pure theory, no experiments, but clean framing) and "Toward Understanding In-context vs. In-weight Learning" (6.5, theory + experiments, some framing concerns). Our paper has experiments (unlike the 6.0 anchor whose reviewers flagged missing experiments as a weakness) and a novel first-of-its-kind analysis, but has more noticeable framing issues than both. This places it near the 6.0 anchor rather than above it.

---

## Summary

This paper provides the **first theoretical analysis** of the training dynamics and in-context learning (ICL) generalization of a one-layer Mamba model on binary classification tasks with additive outliers. The paper derives a closed-form expression separating Mamba's linear attention from its nonlinear gating (Eq. 3), proves convergence and sample complexity bounds (Theorem 1), and shows that under certain conditions Mamba can tolerate outlier fractions approaching 1 at test time while a comparable linear Transformer fails beyond 1/2 (Theorems 2 and 4). Experiments on synthetic data validate the theoretical predictions.

## Strengths

- **First theoretical training dynamics analysis for Mamba ICL.** While prior work (Li et al. 2024b, 2025b) analyzed Mamba-like models at global minima, Theorem 1 provides explicit convergence guarantees under SGD — a genuine step forward. The analysis handles a controllable fraction \(p_a\) of outlier-containing examples during training, which is more general than existing Transformer-only analyses (Huang et al., Li et al. 2024a).

- **Closed-form decomposition separating linear attention from nonlinear gating.** Equation (3) rewrites one-layer Mamba as a linear attention term (parameterized by \(\mathbf{W}_B, \mathbf{W}_C\)) followed by a sigmoid-based gating product \(G_{i,l+1}(\mathbf{w})\). This decomposition is the foundation for all subsequent results and enables a direct architectural comparison with linear Transformers (which correspond to \(G_{i,l+1}=1\)).

- **Mechanistic characterization via Corollaries 1 and 2.** Corollary 1 shows the learned linear attention concentrates on examples sharing the same relevant pattern as the query. Corollary 2 proves the gating suppresses outlier examples (gating value \(\le \text{poly}(M_1)^{-1}\)) and induces exponential decay with index distance from the query. Together they provide a testable account of Mamba's internal operation, and Figures 3-4 empirically validate these predictions.

- **Empirical validation of the theoretical comparison.** Figure 2 confirms that under three different outlier-labeling functions (flipped, targeted, random), Mamba maintains near-zero error for \(\alpha\) up to 0.8 while the linear Transformer fails sharply at \(\alpha > 0.5\), consistent with the theoretical bounds.

## Weaknesses

### Major

1. **The robustness claim in the abstract and introduction omits a critical condition on test outliers.**  
   Theorem 2 requires test outliers to lie in the set  
   \(\mathcal{V}' = \{ v \mid v = \sum_{i=1}^V \lambda_i v_i^*, \sum_{i=1}^V \lambda_i \ge L > 0, \ldots \}\)  
   —i.e., positive linear combinations of training outlier patterns. The abstract states the model "maintains accurate predictions even when the proportion of outliers exceeds the threshold that a linear Transformer can tolerate" without flagging this condition. The introduction's contribution list is somewhat better (Section 1.1, point 1: "unseen outliers that are linear combinations of the training-time outliers") and P1 in Section 3.1 states it clearly. However, the headline-level framing repeatedly emphasizes "fraction approaches 1" without the cone restriction, creating a mismatch between the paper's strongest claims and what is actually proven. This is not a mathematical error — the restriction is correctly stated in the theorems — but it is a significant *framing* issue because a reader scanning the abstract and intro walks away with a broader belief than the theory supports. The paper should state this restriction explicitly in the abstract and the very first claim in the introduction.

2. **The comparison with linear Transformers is presented as a definitive limitation, but only sufficient conditions are established.**  
   The paper repeatedly states that "linear Transformers can only generalize well when \(\alpha < 1/2\)" (Section 1.1, P2) and "can tolerate at most a 1/2 fraction of outliers" (Section 4.1). Theorem 4 gives *sufficient* conditions for the Transformer to achieve low error, not a proof that \(\alpha \ge 1/2\) is impossible. The paper does acknowledge in Section 3.4 (line 191) that "the comparison is made between sufficient conditions," but this nuance is lost in every summary statement. Since the same is true of Mamba's own bound (Theorem 2 is also sufficient), the contrast should be framed symmetrically: "under our sufficient conditions, the Transformer bound yields \(\alpha < 1/2\) while the Mamba bound permits \(\alpha\) up to 1." Claiming Mamba *outperforms* Transformers in the absolute sense overstates what the theory proves.

### Minor

3. **The experiments test only test outliers inside the cone \(\mathcal{V}'\).**  
   The test patterns used (Section 4: \(v'_1=0.7v_1^*+0.6v_2^*-0.4v_3^*\), etc.) all satisfy the positive-coefficient-sum condition from Theorem 2(a). The paper does not test outliers *outside* this cone (e.g., a pattern orthogonal to all training outliers, or one with purely negative coefficients). Such an experiment would either validate that the cone condition is necessary or reveal it is looser than required. Either outcome would strengthen the paper.

4. **Several theoretical conditions are dense and hard to compare across theorems.**  
   Theorems 1-4 each list a dozen or more interlocking conditions on batch size \(B\), outlier magnitude \(\kappa_a\), prompt lengths \(l_{tr}, l_{ts}\), outlier fractions \(p_a, \alpha\), etc. The paper notes that Mamba requires larger batch sizes and more iterations, but the reader must cross-reference multiple theorem statements to extract the comparison. A single table contrasting the sufficient conditions for Mamba vs. Transformer would substantially improve readability.

### Trivial

5. Minor labellings in Section 3.1 (P1) — the clause "but should contain a positive linear combinations" has a singular/plural mismatch ("a ... combinations").

## Nice-to-Haves

- The paper could briefly discuss what the cone condition means in practical terms (e.g., the attacker cannot inject a completely novel corruption direction).
- The derivation of Eq. (3) is deferred to Appendix E.1. Adding one sentence of intuition for why the gating product takes its particular form would help the reader in the main text.

## Removed Points

- *Criticism about the derivation being relegated to the appendix*: The derivation is standard for theoretical papers; the main text states the result and cites the appendix.
- *Criticism about computational complexity comparison not being discussed*: This is outside the paper's stated scope (theoretical convergence analysis).
- *Criticism about no ablation on initialization scheme*: The initialization is clearly stated; sensitivity analysis is not standard for this type of theoretical paper.
- *Criticism about missing related works*: Not permitted per review guidelines; the paper cites relevant prior work (Li et al. 2024a,b, 2025b; Huang et al. 2023; Zhang et al. 2023).
- *Strength Finder's generic praise about "addressing an important problem"*: Removed as superficial; kept only evidence-grounded strengths.

## Novel Insights

The most interesting insight comes from comparing the two models' learning dynamics: Mamba's nonlinear gating forces it to require larger batch sizes and more iterations to converge (Theorem 1 vs. Theorem 3), but this same gating structure pays off at inference by enabling outlier suppression that scales with index distance (Corollary 2). This inverse relationship — harder to train, more robust at test time — is a genuine architectural tradeoff that the paper surfaces clearly. The exponential-index-decay property of the gating (\(G_{h(j)} \ge \Theta(1/2^{j-1})\)) is also notable because it links Mamba's sequential structure directly to a "local bias" that Transformers with position-agnostic linear attention lack.

## Suggestions

1. **Revise the abstract and introduction** to include the cone condition explicitly. For example: "Mamba maintains accurate predictions even when the fraction of outlier-containing context examples approaches 1, *provided the test outliers are positive linear combinations of outlier patterns seen during training*."
2. **Reframe the Transformer comparison** throughout to use symmetric language: "under our sufficient conditions, the bound for Transformers requires \(\alpha < 1/2\) while the bound for Mamba permits \(\alpha\) up to 1."
3. **Add an experiment with test outliers that are orthogonal to the training outlier subspace** (i.e., violate the cone condition) to probe whether the condition is tight.
4. **Add a comparison table** for the main text summarizing the sufficient conditions for Mamba vs. Transformer (batch size, iterations, \(\kappa_a\) range, \(l_{tr}\), \(\alpha\) tolerance).

## Score and Decision

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| 4y3GDTFv70 | 3.25 | 1 | Weaker: emergent abilities theory with limited rigor |
| fzZfju8y0g | 3.40 | 1 | Weaker: different topic (PDE solving via ICL) |
| uOnElfFuey | 3.00 | 1 | Weaker: automata extraction, not training dynamics |
| NSBP7HzA5Z | 3.00 | 1 | Weaker: conceptual inductive bias, no formal results |
| Jwtpbhheoy | 5.00 | 1 | Comparable: ICL uncertainty quantification, similar theory+exp setup but less novel |
| **jwsPS8yRe4** | **6.00** | **1/2** | **Comparable: transformer ICL theory, same model simplification, but lacks experiments (a flagged weakness there)** |
| aKJr5NnN8U | 6.50 | 1/2 | Stronger: cleaner framing, well-connected experiments |
| ikwEDva1JZ | 6.50 | 1/2 | Stronger: broader ICL analysis, well-executed probing |
| i9RTCC6whL | 4.67 | 2 | Weaker: Mamba stability analysis, applied not theoretical |
| AL1fq05o7H | 6.25 | 2 | Not directly comparable: original Mamba paper, different genre |
| 1TXDtnDIsV | 4.67 | 2 | Weaker: MambaCL application, no training dynamics theory |
| 97rOQDPmk2 | 7.33 | 2 | Stronger: more complex model (2-layer, softmax), cleaner claims |

**Round 1 bracket:** 5.0–6.5. **Round 2 narrowing:** The paper is stronger than the 4.67–5.0 anchors (which lack training dynamics theory or are purely applied) and slightly weaker than the 6.5 anchors (which have cleaner framing). It is most comparable to the 6.0 anchor (Trained Transformer Classifiers) — both use simplified one-layer architectures and rigorous theory — but our paper has the advantage of empirical validation, offset by more noticeable framing issues.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>