## Summary

This paper addresses **post-treatment selection** in interventional causal discovery — a setting where samples are selectively included after interventions (e.g., gene-perturbed cells that pass quality-control filters). The authors show that existing invariance-based frameworks cannot distinguish genuine causal effects from selection artifacts, because both produce identical patterns of variant marginal and invariant conditional distributions. They propose a new causal formulation that explicitly models post-treatment selection within an augmented DAG framework, define a *FI*-Markov equivalence class and its graphical representation (*F*-PAG) with novel edge types, and develop a provably sound and complete algorithm *F*-FCI. Experiments on synthetic data and a real-world gene perturbation dataset demonstrate improved precision in recovering causal relations over baselines.

---

## Strengths

- **Novel, well-motivated problem**: The identification that post-treatment selection produces the same invariant-conditional/variant-marginal pattern as direct causation — making it invisible to standard invariance-based frameworks — is a clean and important observation. The gene quality-control motivation is compelling and well-grounded in practice (Norman et al., per-protocol clinical trials).

- **Complete theoretical package**: The paper delivers a full theoretical stack: explicit Markov property characterization (Theorem 1), graphical criteria for the equivalence class (Theorem 2), a novel graphical notation (*F*-PAG with square marks and two new inducing-path arrows), and provable soundness and completeness of *F*-FCI (Theorems 3 & 4). This completeness-of-contribution is rare and valuable.

- **Elegant discriminatory mechanism**: The insight that hard interventions on *Type I inducing nodes* (intermediate nodes on inducing paths between intervened variables) can block selection paths and expose whether a genuine causal link or selection path exists is technically elegant. It generalizes the d-separation blocking idea in a non-trivial way.

- **Thorough empirical evaluation**: Comparisons across six strong baselines (GIES, IGSP, UT-IGSP, JCI-GSP, FCI-interven, CDIS), multiple graph sizes (10–25 variables), sample sizes (500–2000), hard and soft interventions, and both precision/SHD metrics demonstrate consistent improvements. The real-world application to Norman gene perturbation data adds practical credibility.

---

## Weaknesses

### Fatal
None identified.

### Major

1. **Completeness claim lacks precision**: Theorem 4 states that "each type of substructure … can be identified by different types of CI patterns," but this is not as crisp as standard completeness theorems in causal discovery (e.g., Meek's completeness for CPDAGs, Zhang's completeness for FCI), which require that the output is the *unique most informative* PAG consistent with all entailed CIs. The theorem does not explicitly assert that no additional edges can be oriented without additional assumptions, nor that the *F*-PAG is the unique maximally informative representation for the *FI*-Markov equivalence class. This leaves the completeness result ambiguous.

2. **Faithfulness under selection is under-examined**: The algorithm assumes standard faithfulness (Section 4), but selection bias operating via conditioning on S=1 can create complex collider-induced dependencies that are not standard independence model artifacts. The interaction between selection-induced conditioning and the faithfulness assumption is not analyzed, and known failures of faithfulness under selection (e.g., selection creates algebraic dependencies) are not discussed.

3. **Practical scope of Type I inducing nodes**: The discriminatory power of *F*-FCI for resolving genuine causal links from selection paths depends critically on hard interventions on Type I inducing nodes. The paper acknowledges this limitation ("future direction"), but provides no quantification of coverage in practice — e.g., what fraction of causal relations in the Norman dataset remain unresolved (represented as ○→) due to absence of Type II inducing node interventions.

### Minor

1. **Baseline comparison is structurally favorable**: All baselines explicitly ignore post-treatment selection. The observed precision improvements may in large part reflect that F-FCI avoids confirming false positives from selection paths, rather than genuine structural learning gains. An ablation or adapted baseline (e.g., FCI applied to pre-debiased data) would strengthen the conclusions.

2. **Real-world evaluation via Enrichr is indirect**: Using prior regulatory knowledge from Enrichr as ground truth for the Norman dataset is standard in the genomics causal discovery literature but noisy. The paper does not report how many identified *selection* paths (as opposed to causal links) match known biology, which would be the most distinctive validation of the selection-identification capability.

### Trivial
- The algorithm pseudocode (Algorithm 1, Step 2.2) was heavily damaged by the parser, with all six orientation conditions rendered identically as `(⊥, ⊥, ⊥, ⊥)`. The accompanying Figure 4 and body text compensate, but the full condition table would aid reproducibility.

---

## Nice-to-Haves

- A worked example end-to-end (from observational+interventional data to *F*-PAG output) on a small 5-variable graph with selection would significantly improve accessibility of the algorithm.
- Discussion of computational complexity of *F*-FCI relative to standard FCI, particularly the overhead from Step 2.3 (detecting Type I inducing nodes and conducting additional CI tests).
- Sensitivity analysis: what happens when the faithfulness assumption partially fails due to selection?

---

## Novel Insights

The central novel insight is that post-treatment selection creates a structural "camouflage" under standard invariance-based causal discovery: because conditioning on S=1 induces a Y-structure collider path that propagates intervention effects identically to direct causation, existing frameworks cannot distinguish the two cases. The resolution via hard interventions on intermediate Type I inducing nodes — which *block* the selection path while leaving genuine causal paths active — is technically elegant and suggests a broader principle: in causal discovery with structured missing data mechanisms, additional targeted interventions on intermediate nodes (not just on the endpoints of interest) can resolve otherwise unidentifiable equivalence classes. This extends the reach of interventional causal discovery beyond what can be inferred from endpoint-only interventions.

---

## Suggestions

- Prove or disprove that the *F*-PAG is the unique maximally informative graphical object for the *FI*-Markov equivalence class, analogous to Zhang (2008b)'s maximally informative PAG for observational ECs.
- Provide a formal statement of the faithfulness condition adapted to the conditional distribution P(X|S=1) and discuss implications for the algorithm's guarantees.
- Quantify in experiments the fraction of edge pairs left with uncertain marks (○→) vs. resolved marks (→, ↔, □—□), and how this varies with the availability of interventions on inducing nodes.

---

## Score and Decision

The paper makes a genuine, complete contribution: it identifies a real overlooked problem, provides a full theoretical treatment with an equivalence characterization and a sound/complete algorithm, and validates the approach empirically. The major weaknesses (imprecise completeness statement, unexamined faithfulness interaction with selection, and unquantified practical coverage) are real but do not invalidate the core claims or results. The work meaningfully advances the scope of interventional causal discovery.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>