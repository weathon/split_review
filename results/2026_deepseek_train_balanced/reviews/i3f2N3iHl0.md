## Summary

This paper claims to develop a unified quantum/symplectic geometric theory for Drug-Target Interaction (DTI) prediction with Domain Adaptation (DA). Section 2 (~275 lines) defines symplectic structures, quantum Wasserstein distances, DTI-preserving quantum channels, and quantum Fisher-Rao metrics, with theorems stated and accompanied by prose "proof" sketches. Section 3 (~30 lines of experimental text) evaluates a model combining Graph Attention Networks, a module called "KAN" (citing Kipf & Welling 2016), and an unspecified domain adaptation technique on two datasets (BindingDB, BioSNAP) against four baselines. The central problem is that the elaborate theoretical apparatus has no connection to the method actually tested — the paper is two disjoint documents stapled together.

## Strengths

- **Ablation study (Section 3.4, Figure 3).** The paper systematically removes the GCN, KAN, and DA modules on both datasets, showing which components contribute to performance. This provides more granular evidence than reporting a single final number.
- **Principled domain split via hierarchical clustering (Section 3.1).** Using clustering rather than random splits to construct source/target domains is a reasonable design choice that better simulates natural distribution shifts.

## Weaknesses

### Fatal

1. **Complete disconnect between the advertised theoretical framework and the evaluated method.** Section 2 develops an elaborate formalism involving DTI symplectic structures, quantum optimal transport, DTI-preserving quantum channels, quantum Fisher-Rao metrics, quantum Cramér-Rao bounds, and a unified variational principle with geometric stochastic gradient Langevin dynamics. Section 3 evaluates a model composed of a Graph Attention Network (GAT), a module it calls "KAN" (citing Kipf & Welling 2016 — i.e., a GCN), and an unspecified Domain Adaptation technique. **None of the theoretical constructs from Section 2 — not the symplectic Wasserstein distance, not the quantum Fisher-Rao metric, not the quantum channels, not the Cramér-Rao bound — are operationalized, computed, or even mentioned in the experimental section.** The paper does not describe how any part of the theory maps onto the neural architecture, what loss function is actually optimized, or how any theorem informs the training procedure. The title, abstract, and introduction promise a quantum-mechanical, symplectic-geometric theory; the body delivers a generic GNN+DA pipeline. This is not a missing ablation or an incomplete comparison — it is a structural failure of the paper's central claim.

### Major

2. **Mathematical "proofs" are prose outlines, not derivations.** Throughout Section 2, theorems are followed by "Proof" sections that consist entirely of step-lists (e.g., "1. Show that the space... forms an infinite-dimensional Lie group. 2. Equip... with a weak Riemannian structure. 3. Prove that... is lower semicontinuous...") with no actual calculations, inequality derivations, or verification of the invoked theorems' conditions. Theorem 2.1 says "under suitable regularity conditions" without specifying them. The Banach-Alaoglu theorem, Rellich-Kondrachov theorem, and direct method of calculus of variations are invoked but their applicability is never established. The mathematical content reads as a research proposal, not as a completed derivation.

3. **Abstract promises contributions not delivered in the body.** The abstract states: "deriving a Quantum Rao-Blackwell theorem and a Quantum Bayesian Cramér-Rao bound specifically for DTI-DA." Neither of these results appears anywhere in the paper body (Sections 1–4). The paper ends without introducing, stating, or proving these items. The gap between what is advertised and what is delivered is substantive.

4. **The actual method is not described.** The experimental section does not specify:
   - What loss function is optimized (the word "loss" never appears in the paper).
   - How drugs and targets are featurized (molecular fingerprints, sequences, graphs?).
   - What domain adaptation technique is used (adversarial? CORAL? MMD?).
   - The complete model architecture (no diagram beyond Figure 1, which is a generic illustration).
   
   The paper says it uses "GAT," "KAN," and "DA" without defining any of these components concretely. This makes the work neither reproducible nor clearly attributable.

5. **Weak experimental evaluation.** Only two datasets are used with no error bars, confidence intervals, or statistical significance tests. Baselines (SVM from 1995, RF from 1995, GraphDTA from 2021, MolTrans from 2021) do not include more recent DTI methods. The paper claims "five baselines" (line 315) but lists only four. Performance on BindingDB is near chance (ACC 0.502). AUC values are modest across the board (0.654–0.744), and improvements over the best baseline MolTrans are small (2.66% on AUC, 3.42% on AUPR on BioSNAP).

### Minor

6. **Unclear module naming and citation.** "KAN" is called "Knowledge-Aware Network" and cites Kipf & Welling (2016), which is the GCN paper. If this module is a GCN, the name "Knowledge-Aware Network" is non-standard and unexplained. If it refers to Kolmogorov-Arnold Networks, the citation is wrong. Either way, attribution and nomenclature are confusing.

7. **Ablation reveals limited DA contribution.** On BioSNAP, the KAN-only model achieves AUC 0.736 while the full model (KAN+DA) achieves 0.745 — a marginal 0.009 improvement that is not discussed or statistically assessed. On BindingDB, the full model's AUC (0.654) improves more substantially over KAN alone (0.621), but the overall near-chance accuracy raises questions about the task setup.

## Nice-to-Haves

- Reporting error bars across multiple runs and conducting statistical significance tests would substantially strengthen the experimental claims.
- Including post-2021 DTI prediction methods as baselines would provide a more realistic assessment of the method's competitiveness.

## Removed Points

These points are flagged for removal; treat them with caution.

- **"Name-dropping citation pattern" (from harsh critic):** The critic claimed the introduction cites "an unusually large number of references inline... in a pattern that suggests name-dropping." This is speculative and not a verifiable weakness. Removed.
- **"Typesetting anomalies in Wasserstein distance symbol" (from harsh critic):** The garbled notation on line 70 (`{\slash...}`) is attributable to PDF extraction artifacts, not the original submission. Removed per formatting-artifact rule.
- **"No code, no architecture diagram" (from harsh critic):** Requests for code release and architectural diagrams are reasonable reproducibility concerns, but the rule against nitpicking reproducibility (trivial implementation details, large artifacts) and the parser-stripped-appendix rule apply here. The paper's insufficient method description (Weakness #4) already covers the substantive issue. Removed.
- **Strength: "Consistent experimental protocol" (from strength finder):** Using identical hyperparameters across baselines is standard experimental practice, not a distinctive strength. Removed as generic.
- **"KAN = Kolmogorov-Arnold Networks, citation wrong" (from harsh critic, partial):** The paper defines KAN as "Knowledge-Aware Network," not Kolmogorov-Arnold Network. The reviewer's specific assumption about what KAN stands for is incorrect. However, the underlying concern (unclear module identity and inappropriate citation) is retained as Weakness #6.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Decide on a single coherent contribution.** If the paper's contribution is an empirical DTI prediction method, remove Section 2 entirely (or reduce it to a paragraph of motivation) and instead comprehensively describe the model architecture, loss function, input representations, and domain adaptation technique. Add state-of-the-art baselines, error bars, and statistical tests. If the contribution is the theoretical framework, implement it — show how the symplectic Wasserstein distance or quantum channels are computed and whether they improve prediction performance.

2. **Either provide actual proofs or remove the theorem framework.** If rigorous mathematical derivations are claimed, they must contain real calculations, not step outlines. Otherwise, the paper should not frame itself as containing theorems with proofs.

3. **Deliver what the abstract promises.** The Quantum Rao-Blackwell theorem and Quantum Bayesian Cramér-Rao bound need to appear in the paper or be removed from the abstract.

## Score and Decision

**MY FINAL SCORE:** <score>1.0</score>
**MY FINAL DECISION:** <decision>Reject</decision>