Now I have sufficient information to construct the final consolidated review. Let me write it.

## Summary

This paper introduces FROND, a framework that replaces the integer-order derivatives in continuous GNNs (GRAND, CDE, GREAD, GraphCON, etc.) with Caputo fractional derivatives of order β ∈ (0,1]. The core idea is that fractional-order dynamics incorporate memory of the full feature evolution history, enabling non-Markovian dynamics that can mitigate oversmoothing. The paper provides a random walk interpretation connecting F-GRAND-l (the linear variant) to a non-Markovian random walk, proves an algebraic convergence rate Θ(t^{-β}) for this linear case (contrasting with exponential convergence of integer-order models), and validates the framework experimentally on multiple backbone architectures across node and graph classification tasks.

## Strengths

- **Novel and well-motivated application of fractional calculus to continuous GNNs.**  The idea of generalizing integer-order derivatives in neural ODE-style GNNs to fractional Caputo derivatives is original and grounded in a genuine physical motivation: many real-world graphs exhibit fractal/hierarchical structure, and fractional diffusion equations are the correct mathematical model for such media.  This is a direction that existing continuous GNN literature has not explored.

- **Clean theoretical analysis for the linear diffusion case.**  Theorem 1 (non-Markovian random walk interpretation) and Theorem 2 (algebraic convergence rate Θ(t^{-β})) are genuinely insightful.  They establish a formal connection between fractional order and memory-dependent dynamics, and the proof that convergence slows algebraically (vs. exponentially for integer-order)—together with the oversmoothing experiment in Figure 3 showing F-GRAND maintaining performance up to 128 layers—provides a concrete mechanism for why fractional order helps.

- **Modular framework that extends multiple backbone models.**  FROND is not a single architecture but a general framework: the paper demonstrates fractional variants of GRAND, GRAND++, CDE, GREAD, and GraphCON, all without adding trainable parameters.  This demonstrates generality and suggests the approach could be ported to future continuous GNN designs.

- **Ablation study on β reveals meaningful structure.**  Table 3 shows that tree-structured datasets (Airport) benefit from smaller β (more memory), while citation networks prefer β close to 1.  This pattern is consistent with the fractal hypothesis and gives the framework practical flexibility rather than being ornamental.

## Weaknesses

### Fatal
None.

### Major

1. **Confounded experimental comparison between F-GRAND and GRAND baselines.**  The paper states "Where available, results from the paper [Chamberlain2021] are used" (line 309) for GRAND baselines, and separately states that F-GRAND uses the basic predictor solver (line 298).  The original GRAND paper used adaptive ODE solvers (Dormand–Prince from torchdiffeq), while the basic predictor at β=1 reduces to the Euler method.  This means F-GRAND results and GRAND baselines were obtained with *different numerical solvers*, introducing a confound: any observed improvement could partially reflect solver accuracy rather than the fractional derivative itself.  The paper's claim at line 288 that the basic predictor "simplifies to the Euler solver in…[chamberlain2021grand]" is misleading—GRAND did not use Euler.  This confound undermines the clean attribution of performance gains to fractional order.  The authors should re-run all integer-order baselines using the basic predictor (which at β=1 becomes Euler) to isolate the effect of β.

2. **Suspiciously large gains on Airport and Disease with undertuned GRAND-l baseline.**  On Airport, GRAND-l scores 80.5±9.6 (standard deviation of 9.6 is unusually large), GRAND-nl scores 90.9±1.6, and F-GRAND-l scores 98.1±0.2.  The large std dev and 10-point gap between GRAND-l and GRAND-nl strongly suggest GRAND-l was not properly tuned for these datasets.  The paper does not provide evidence that hyperparameters for GRAND-l were optimized comparably to F-GRAND-l.  While F-GRAND-l also outperforms the better-tuned GRAND-nl (90.9→98.1) and GIL (91.5→98.1), the specific comparison to GRAND-l on these datasets is unreliable.  A controlled hyperparameter search for all baselines under a unified protocol is needed.

3. **Theoretical analysis covers only the linear diffusion case, while experimental claims extend to nonlinear variants.**  The random walk interpretation (Theorem 1) and the algebraic convergence proof (Theorem 2) are explicitly for F-GRAND-l (the linear fractional diffusion equation).  Yet the paper also presents F-GRAND-nl, F-GREAD, F-CDE, and F-GraphCON—all involving nonlinear attention, reaction, or convection terms—without any theoretical justification that fractional order helps in these settings.  The paper does not overclaim the theory's scope (it clearly states it applies to the linear case), but the result is a gap between what is proven and what is tested.  This limits the mechanistic understanding of why fractional order benefits the nonlinear variants.

### Minor

- **Unclear which baseline results were re-run vs. taken from prior papers.**  Line 309 says "Where available, results from the paper [Chamberlain2021] are used" for GRAND, and line 396 says the same for CDE.  But the paper does not specify which datasets these apply to (e.g., the GRAND paper did not report results on Airport or Disease), nor what solver was used when baselines were re-run.  This ambiguity makes it difficult to assess the severity of the solver confound.

- **The ablation study on β (Table 3) is limited to only 2 datasets with fixed T=8.**  A broader sweep across more datasets and varied integration times would strengthen the empirical validation of how β controls the memory-dynamics trade-off.

- **Computational cost of the full-memory solver is O(n²) in time steps, but practical implications are not discussed.**  The short-memory principle is mentioned in passing (Figure 1, right panel) but deferred to the appendix.  The paper would benefit from a brief discussion of whether the observed gains persist under short-memory truncation, which is essential for practical applicability.

### Trivial
None (the paper is generally well-written; minor presentation issues cannot be reliably distinguished from PDF-parsing artifacts).

## Nice-to-Haves

- The solver confound could be resolved by a controlled experiment: run GRAND-l with the basic predictor (Euler) at β=1 and compare against F-GRAND-l at β<1 with the same solver. This would cleanly isolate the effect of β.
- Reporting computational cost (runtime/memory) across different β values and solver variants would help practitioners assess the practical overhead of the memory-dependent dynamics.

## Removed Points

**"The proof of Theorem 1 lacks a derivation; the connection to Gorenflo 2002 is claimed without proof."** — Removed. The paper cites Gorenflo (2002) for the technique and states the proof follows from established results. This is standard practice; a full reproduction of prior work's proofs is not expected.

**"β=0.1 on Airport (Table 3) likely produces a numerical artifact — the solver is unstable at such extreme values."** — Removed. This is speculative and unsupported. The paper's main result for Airport uses β=0.5 (Table 1), not 0.1. The ablation in Table 3 varies β with fixed T=8, which is a different experimental setting.

**"The paper does not provide confidence intervals for the results."** — Removed. Standard deviations are reported for all experiments, which is standard practice for this class of benchmarks.

## Novel Insights

None beyond the paper's own contributions. The observation that the optimal β correlates with graph topology (tree-structured → smaller β, citation networks → larger β) is already discussed by the authors.

## Suggestions

1. **Rerun all integer-order baselines (GRAND-l, GRAND-nl, CDE, etc.) using the exact same numerical solver (basic predictor) with the same hyperparameter tuning pipeline.**  At β=1, the basic predictor reduces to Euler, giving a controlled ablation.  This is the single most important change to support the paper's central claim.

2. **Document explicitly for each dataset whether baseline results are from prior papers or re-run, and specify the solver used in each case.**  Include this in a reproducibility statement.

3. **Add a brief discussion of whether and how the theoretical insights for F-GRAND-l (algebraic convergence, memory-dependent random walk) might extend heuristically to the nonlinear variants.**  Even a conjectural paragraph would help bridge the theory–experiment gap.

4. **Include a small experiment testing whether the short-memory principle preserves the observed gains, to address practical scalability concerns.**

## Score and Decision

**Anchor comparisons:**

| Anchor Path | Avg Score | Comparison |
|---|---|---|
| `i8vPRlsrYu.md` (Residual Connections/Oversmoothing) | 7.00 | Stronger theory (nonlinear analysis) and cleaner experiments. This paper has a more novel core idea but weaker experimental methodology. |
| `duGygkA3QR.md` (GNN Meets DMD) | 6.60 | Accepted paper with extensive experiments. This paper has more original theory but a less rigorous experimental setup. |
| `7b2JrzdLhA.md` (Graph Neural Ricci Flow) | 6.00 | Similar-level theory; both have scope limitations in experiments. This paper has a comparable contribution but a solver confound this one lacks. |
| `mxkm1Pr2PM.md` (GNN Mean Field Game) | 5.33 | Rejected paper with presentation issues. This paper is clearer and has more solid theoretical grounding, but both have experimental methodology concerns. |
| `za9tj3izLn.md` (Opinion Dynamics) | 4.33 | Weak contribution, rejected. This paper is substantially more novel and substantive. |
| `jrKPOQBq9i.md` (PoincareNorm) | 3.75 | Weak contribution, unclear benefits, rejected. This paper has clearer contributions and stronger theory. |
| `0e26yMOCbd.md` (Charge Dirichlet Energy) | 3.40 | Rejected; weak claims. This paper is substantially stronger. |

The paper introduces a genuinely novel idea (fractional-order continuous GNNs) with clean theoretical analysis for the linear case and modular applicability to multiple architectures. However, the experimental validation is compromised by a solver confound between F-GRAND and its baselines, and the most striking improvements (Airport/Disease) coincide with indicators of undertuned baselines. The paper needs major revisions to the experimental design before the core claim can be reliably assessed. Relative to the calibration anchors, the paper's originality and theory place it above the clearly weak papers (3.4–4.3) but the experimental confound prevents it from reaching the level of a clean accept (6.0+). It falls between the 5.33 and 6.0 anchors.

**MY FINAL SCORE:** <score>5.0</score>  
**MY FINAL DECISION:** <decision>Reject</decision>