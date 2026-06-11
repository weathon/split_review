Now I have a clear picture. Let me compile the final review.

**Bracket (Round 1):** The paper sits between G5KbDVAlI6 (4.00, rejected GISL paper on selection bias in gene networks — similar topic but weaker) and xByvdb3DCm (8.00, accepted CDIS paper on selection bias in interventional studies — similar topic but much stronger). Initial bracket: 4.0–6.5.

**Narrowing (Round 2):** Compared to Lxst78Rrwj (5.00, rejected — fundamental theoretical gap with no guarantee for downsampling proxy) and BZYIEw4mcY (6.00, accepted — strong theory with polynomial-time guarantee but limited experiments and presentation issues). Our paper has stronger theory than the 5.00 anchor (sound framework, no fundamental gap), but the garbled algorithm and missing direct validation of the central claim pull it below the 6.00 accepted anchor. Final score: **5.0**.

---

## Summary
This paper addresses post-treatment selection bias in interventional causal discovery — the problem that samples are selectively retained after interventions, creating spurious dependencies that mimic causal effects. The authors propose an augmented DAG framework that explicitly models selection alongside interventions, define a refined FI-Markov equivalence class and its F-PAG graphical representation, and develop the F-FCI algorithm with claimed soundness and completeness. Synthetic experiments show improved precision and SHD over six baselines; a real-world case study on gene perturbation data is included.

## Strengths
- **Genuinely underexplored problem with clear motivation**: The paper demonstrates via Figure 1 that post-treatment selection and direct causation produce identical CI patterns (variant marginal, invariant conditional) under existing interventional frameworks — a non-obvious gap well-motivated by gene perturbation quality control and clinical trial examples.
- **Substantial theoretical framework**: The paper constructs a coherent apparatus: augmented DAG with selection variable S (Definition 1), FI-Markov equivalence (Definition 2), graphical criteria (Theorem 2, Lemmas 2–4), and the F-PAG representation (Definition 5) with novel edge marks (▲, △) that capture distinctions invisible to standard PAGs. The core insight — using hard-hard intervention comparisons on Type I inducing nodes (Definition 6) to break the symmetry between causation and selection (Figure 4) — is clever and well-illustrated.
- **Consistent empirical gains on synthetic data**: Figure 6 shows F-FCI outperforming six baselines (GIES, JCI-GSP, IGSP, UT-IGSP, FCI-interven, CDIS) on DAG Precision and SHD across varying graph sizes (10–25 variables) and sample sizes (n=500–2000), under both hard and soft interventions, with nonlinear SEMs (sin, tanh, square, linear).

## Weaknesses

### Fatal
None.

### Major
- **Algorithm specification is not reproducible as presented**: (a) In Algorithm 1 Step 2.2, all six orientation branches test the identical CI pattern `(⟂, ⟂, ⟂, ⟂)` — clearly a parsing artifact rather than the intended distinct patterns. (b) The `AllPaths` function in Step 2.1 is never defined; it is unclear what paths are considered and how they are computed from the observational skeleton. (c) The refinement in Step 2.3 references F-PAG edge marks (`X_I → X_n ◦→ X_j`) that are themselves the structures being learned, creating a circular specification. These gaps make the algorithm unreproducible from the main text alone, which is a serious issue for a paper whose primary contribution includes a "provably sound and complete algorithm."
- **Evaluation does not directly validate the paper's central claim**: The paper's core contribution is distinguishing post-treatment selection from genuine causation. But the main results (Figure 6) report aggregate DAG Precision and SHD, which conflate multiple error sources. The paper references Table 1 as evaluating "ability to distinguish post-treatment selection" specifically, but this table is not shown in the main text. Without it, readers cannot assess whether F-FCI actually succeeds at its stated purpose versus simply being a better general-purpose causal discovery method.

### Minor
- **No ablation isolating the mechanism**: The evaluation does not include an ablation (e.g., F-FCI without Step 2.3's Type I inducing node refinement) to demonstrate that the claimed theoretical innovation specifically drives the improvement rather than other components of the method.
- **"Without imposing graphical or parametric assumptions" is overstated** (Section 1, line 33): The framework assumes causal Markov, faithfulness (stated in Section 4), and the augmented DAG formulation; these are standard but are assumptions nonetheless. The phrasing should be qualified.
- **Real-world evaluation is thin**: Section 5.2 describes an application to the Norman et al. gene perturbation dataset but provides no quantitative results or comparisons in the main text, referring readers to Appendix D.3. Enrichr-based validation provides only associative prior knowledge, not ground-truth causal validation.

### Trivial
- Abstract uses "F-FCL" while the body consistently uses "F-FCI" — minor inconsistency.

## Nice-to-Haves
- Include the selection-vs-causation discrimination results (Table 1) in the main text.
- Add an ablation study removing Step 2.3's Type I inducing node refinement.
- Discuss algorithmic complexity, even informally (Step 2.1's exhaustive conditioning-set search may be exponential).
- Strengthen the real-world evaluation with quantitative comparisons against baselines.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **Harsh Critic: "Post-treatment" framing is motivational, not formal**: The paper explicitly states it specializes in post-treatment selection (Section 2.1) and provides concrete motivating examples. The mathematical framework is general to selection bias, but the paper is transparent about its scope, and the CI patterns exploited (variant marginal, invariant conditional after intervention) are precisely those that arise under post-treatment selection. The framing is appropriate and the criticism is removed.
- **Harsh Critic: Baseline comparison is uninformative**: The argument that baselines not designed for selection bias make the comparison uninformative is partially valid, but comparing against existing interventional causal discovery methods is standard practice and demonstrates that handling selection bias matters. The demand for ablation is kept as a minor weakness; the framing that the comparison is "uninformative" is removed.
- **Harsh Critic: Algorithm issues are "fatal"**: The six identical CI patterns are clearly a PDF parsing artifact. The prose description (Section 4) conveys the algorithm's logic. The real issues are underspecification, not fundamental incorrectness — kept as Major but demoted from the harsh critic's fatal framing.
- **Strength Finder: "Strong empirical evidence across synthetic and real-world settings"** (real-world component): The real-world evaluation is too thin in the main text to qualify as strong evidence. Removed the real-world claim from strengths; kept the synthetic evidence strength.
- **Strength Finder: "Provably sound and complete algorithm"**: The proofs are in the stripped appendix and cannot be verified. The algorithm specification issues weaken confidence. The strength is kept but grounded in the theoretical framework rather than the algorithm guarantees.

## Novel Insights
The observation that hard-hard intervention comparisons on a third variable (Type I inducing node) can break the symmetry between causation and selection-induced dependence is genuinely novel. Figure 4's exhaustive characterization of CI patterns across eight structural configurations provides a clean taxonomy that could inform future work on selection bias in causal discovery. The F-PAG representation with its novel edge marks (▲, △) offers a more expressive language for describing equivalence classes in this setting.

## Suggestions
- Fix the pseudocode: provide distinct CI patterns for each orientation case in Step 2.2, define `AllPaths` precisely, and resolve the circularity in Step 2.3 by specifying the refinement in terms of CI test outcomes rather than F-PAG marks.
- Bring the selection-vs-causation discrimination metric (Table 1) into the main text as a primary result.
- Add an ablation experiment removing Step 2.3 or replacing it with a simpler heuristic to isolate the Type I inducing node strategy's contribution.

## Anchor Comparisons
- **G5KbDVAlI6 (4.00, Round 1):** GISL paper on selection bias in gene networks — similar topic but smaller experiments (5–9 nodes), weaker theory, rejected. Our paper is clearly stronger.
- **xByvdb3DCm (8.00, Round 1):** CDIS paper on selection bias in interventional studies — similar topic, accepted with all 8s. Has cleaner framework (twin graph), clearer algorithm, comprehensive real-world evaluation across two domains. Our paper does not reach this level.
- **Lxst78Rrwj (5.00, Round 2):** Invariance-based causal discovery — rejected. Has a fundamental theoretical gap (no guarantee that downsampled data corresponds to interventions). Our paper's theory is more sound but shares presentation/evaluation gaps. Our paper is comparable or slightly stronger.
- **BZYIEw4mcY (6.00, Round 2):** Causal discovery with latent variables, accepted with all 6s. Has strong theory, polynomial-time guarantee, trustworthiness guarantees, but limited experiments and presentation issues. Our paper has better experiments but a more severely garbled algorithm specification. Slightly below this anchor.
- **cbFqqtJGtA (4.25, Round 2):** Perturbation target prediction — related domain, rejected. Our paper is stronger in scope and execution.
- **fGhr39bqZa (6.00, Round 2):** Causal graph recovery via homologous surrogates, accepted with all 6s. Strong theory on latent variables. Our paper addresses a different problem but has comparable theoretical depth with weaker algorithmic presentation.
- **nHkMm0ywWm (6.50, Round 2):** Partially observed linear non-Gaussian models, accepted. Strong identifiability results, solid execution. Our paper is clearly below this level.
- **Bp0HBaMNRl (6.75, Round 2):** Differentiable causal discovery for latent hierarchical models, accepted. Novel methodology, strong presentation. Our paper is below this level.

**Round 1 bracket:** 4.0–6.5. **Round 2 narrowing:** The paper lands between the 5.00 and 6.00 anchors — stronger theory and experiments than the 5.00 anchor, but with algorithm specification gaps that pull it below the 6.00 accepted anchor.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>