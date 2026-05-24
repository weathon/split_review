Now I have all the information I need. Let me compile the final review.

## Summary

This paper addresses post-treatment selection bias in interventional causal discovery with latent confounders — a setting where samples are selectively included after interventions (e.g., quality control in gene perturbation studies). The authors introduce a formal augmented DAG formulation that explicitly models post-treatment selection, define a novel Fine-grained Interventional (FI) Markov equivalence class represented by a new F-PAG graphical notation, and develop a provably sound and complete algorithm (F-FCI) to recover causal structures up to this equivalence class. Experimental results on synthetic and real-world gene perturbation data demonstrate F-FCI's effectiveness against six baseline methods.

## Strengths

- **Well-motivated non-identifiability problem with concrete illustrations**: Figure 1 clearly demonstrates that existing interventional causal discovery frameworks cannot distinguish direct causation from post-treatment selection, as both produce identical distributional invariance patterns (variant p(effect) and invariant p(effect|cause)). This is substantiated through specific DAG comparisons showing identical CI patterns, establishing the need for the new formulation.

- **Rigorous theoretical development with soundness and completeness proofs**: The paper provides a complete chain of theoretical results — Theorem 1 (CI/invariance implementation), Lemmas 2–4 (characterizing when variables are dependent and when intervention alters marginal/conditional distributions), and Theorem 2 (graphical criteria for FI-Markov equivalence). Theorem 3 proves soundness and Theorem 4 proves completeness of the F-FCI algorithm, which is a stronger guarantee than the predecessor CDIS paper (Dai et al., 2025) which only proved soundness.

- **Novel graphical representation (F-PAG) extending PAG with new edge types**: Definition 5 introduces four mark types and eight edge types, extending PAG to encode finer distinctions. The square mark and inducing-path indicators (Definitions 5-6) provide concrete visual distinction between direct causation and inducing-path-mediated dependence (Figure 5), which standard PAGs collapse.

- **Key algorithmic insight — intervention-based disambiguation via Type I inducing nodes (Step 2.3)**: When two intervened variables share identical CI patterns regardless of direct causation (e.g., Figure 4(a) vs 4(b)), the algorithm exploits hard interventions on a third variable (Type I inducing node) to determine whether a true causal link exists. This is a concrete mechanism that distinguishes F-FCI from existing approaches.

- **Comprehensive empirical evaluation against multiple baselines across varying conditions**: Figure 6 compares F-FCI against six baselines (GIES, JCI-GSP, IGSP, UT-IGSP, FCI-interven, CDIS) across varying sample sizes (500–2000), numbers of variables (10–25), and hard/soft interventions, showing sustained advantage in precision and SHD.

- **Real-world validation on gene perturbation data**: Section 5.2 applies F-FCI to the Norman et al. (2019) single-cell gene perturbation dataset, reporting both regulatory links and spurious dependencies induced by post-treatment selection, validated against Enrichr prior knowledge.

## Weaknesses

### Fatal

None.

### Major

- **No ablation experiment without post-treatment selection**: All synthetic experiments include post-treatment selection by construction, and all baselines are methods that do not model it. This demonstrates that F-FCI handles selection better than methods blind to it (sufficiency), but the more informative test would be: when there is no post-treatment selection, does F-FCI degrade gracefully to FCI-interven, or does its additional modeling introduce unnecessary complexity? Without this control, the experiments do not establish that the F-PAG machinery is *needed* over simpler alternatives. The theoretical proofs (Theorems 3-4) partially compensate, but an empirical ablation would substantially strengthen the paper.

### Minor

- **Compressed algorithm presentation**: The mapping from the theoretical framework to Algorithm 1, particularly Step 2.3 (refine orientation), is dense. A worked example walking through one complete scenario (e.g., Figure 4(b) vs. (a)) showing the algorithm's CI tests and orientation decisions step by step would significantly aid comprehension and verifiability. The theory is well-developed but the bridge from theory to algorithm is the paper's weakest presentation link.

- **Intervention target selection not discussed in practice**: The theoretical framework depends critically on interventions being available on specific variables, including Type I inducing nodes. In practical settings like gene perturbation studies, intervention targets are predetermined by experimental design. The paper does not discuss what happens when required inducing-node interventions are unavailable (beyond the acknowledged Type II limitation in §6) or how to select targets when the structure is unknown.

- **Limited experimental repetitions**: Results are "averaged over 10 graphs" with 95% confidence intervals (Figure 6 caption). While this is not unusual in the field, more independent graph structures would strengthen the statistical reliability of the claims.

### Trivial

- **Real-world analysis largely deferred to appendix**: The Norman et al. application in §5.2 is very brief (essentially one paragraph referencing Figure 13 and Appendix D.3). Given that this is a key motivating application, including more detailed analysis in the main text would improve persuasive force.

## Nice-to-Haves

- A table mapping each F-PAG edge type to its causal interpretation would help readers navigate the eight edge types introduced in Definition 5.
- Discussion of computational complexity and scaling of CI tests in the new framework.
- Brief survey of how selection bias has been handled in the broader causal inference literature (e.g., Heckman selection models, inverse probability weighting) to sharpen the claim that the graphical/structural treatment is novel.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **Algorithm pseudocode is broken (Step 2.2 all rules share identical condition)** — This is a PDF parser artifact. The parser cannot distinguish the independence symbol (⊥, `\perp\!\!\!\perp`) from the dependence symbol (⊥, `\not\perp\!\!\!\perp`). The original paper uses distinct symbols for each of the six orientation rules, corresponding to the six CI pattern cases in Figure 4(i)'s table. The harsh critic's concern is based on mangled text, not an actual error in the paper. Removed per hard rules about parser formatting artifacts.

2. **"Missing related works" on Heckman selection models, IPW** — Per hard rules, I cannot verify external references not cited in the paper. The paper already cites Heckman (1978) and discusses the broader context.

3. **F-PAG edge count discrepancy in Definition 5** — The definition lists "eight types of edges" but the parser shows more than eight symbols. This appears to be another parser artifact where some edge types got split or merged.

## Novel Insights

The paper's genuinely novel insight is that post-treatment selection creates a distinct class of non-identifiability in interventional causal discovery — one that cannot be resolved by simply adding a selection variable to the augmented DAG (which is what existing methods do for pre-treatment selection). The key mechanism for disambiguation is that hard interventions on Type I inducing nodes (intermediate variables on inducing paths) break the symmetry between causal and selection-mediated dependencies by blocking selection effects on latent confounders. This insight, combined with the FI-Markov equivalence class that is provably finer than standard interventional equivalence classes, represents a meaningful advance beyond the predecessor CDIS work.

## Suggestions

- Add an ablation experiment running the same simulation *without* post-treatment selection to show F-FCI matches FCI-interven when selection is absent, directly demonstrating the additional modeling is necessary.
- Include a worked example of Algorithm 1 on one of the Figure 4 scenarios in the main text.
- Add a brief paragraph in §5 or §6 discussing what happens when inducing-node interventions are unavailable (practical constraint matching the biological motivation).

## Score and Decision

**Evaluation axis assessment:**
- **Originality**: High — post-treatment selection is a genuinely distinct problem from pre-treatment selection, and the F-PAG/FI-Markov equivalence contributions are novel extensions to the PAG framework.
- **Importance of research question**: High — the motivating biological examples (gene perturbation with quality control) are realistic and common.
- **Claims well-supported**: Yes, with strong theoretical proofs (soundness + completeness) and experimental validation. Minor gap: no no-selection ablation.
- **Soundness of experiments**: Adequate but could be strengthened with more repetitions and the missing ablation.
- **Clarity of writing**: Good but dense — the theory is well-organized, but the algorithm presentation is compressed.
- **Value to the community**: High — provides a principled framework for a common but overlooked problem, with open-source implementation.

**Calibration report:**

Round 1 anchors (bracketing):
- AvXrppAS2o (score 3.0, sim 0.71): Predictive method using causal structure, no real structural contribution — much weaker than F-FCI
- G5KbDVAlI6 (score 4.0, sim 0.76): GRNI with selection bias, no theoretical framework — weaker
- qe1CsfnN1W (score 6.25, sim 0.72): Causal effect estimation, different setting — moderately comparable
- xByvdb3DCm (score 8.0, sim 0.76): CDIS, the direct predecessor paper — highly comparable, same topic
- FhQSGhBlqv (score 7.5, sim 0.75): RLCD for latent causal discovery — comparable theoretical contribution level
- u63OVngeSp (score 7.0, sim 0.72): Causal order from single-variable interventions — comparable

Round 1 bracket: 6.5–8.0

Round 2 anchors (narrowing):
- SKulT2VX9p (score 6.67, sim 0.73): Interventional fairness with partial graphs — less novel theoretical contribution, F-FCI is stronger
- qe1CsfnN1W (score 6.25, sim 0.72): Causal effect estimation with post-treatment variables — different setting, less structural novelty
- xByvdb3DCm (score 8.0, sim 0.74): CDIS — same research group, predecessor topic; F-FCI extends with completeness proofs + F-PAG
- FhQSGhBlqv (score 7.5, sim 0.75): RLCD — similar theoretical rigor, well-written; comparable contribution

Positioning: F-FCI extends CDIS (score 8.0) with meaningful additions (completeness, F-PAG), making it at least comparable. However, CDIS received uniformly high scores partly due to excitement about the new problem formulation, while F-FCI tackles a more specific sub-problem (post-treatment vs. pre-treatment selection). F-FCI is stronger than the 6.25-6.67 anchors and comparable to the 7.5 anchor (RLCD). Given the missing no-selection ablation as a concrete weakness, I score slightly below CDIS's perfect 8.0.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>