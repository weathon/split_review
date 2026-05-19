- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 8, 6
Now I have all the information needed. Let me construct the final consolidated review.

---

## Summary

This paper proposes EquiRNA, a hierarchical equivariant GNN for RNA structure evaluation. The model processes RNA at three levels (atom, subunit, nucleotide), reusing nucleotide representations to enable generalization from small training RNAs (50–100 nt) to larger test RNAs (100–200 nt). The authors also introduce rRNAsolo, a new benchmark designed to isolate the size-generalization problem, and demonstrate consistent performance improvements over several baselines on both rRNAsolo and the existing ARES dataset.

## Strengths

- **Hierarchical architecture with a clear biological motivation.** The three-level design (atom → subunit → nucleotide) is grounded in the fact that nucleotides are the shared building blocks across RNAs of all sizes. The ablation study (Table 4) confirms that the nucleotide level is the most critical component: removing it causes the largest performance degradation (+2.68 Mean RMSD on validation, +3.78 on test). This provides direct evidence that the representational-reuse mechanism is carrying weight.

- **rRNAsolo dataset is a rigorous contribution.** The dataset is built through a carefully documented pipeline: TM-score-based clustering to prevent data leakage, strict size split (training 50–100 nt, validation/test 100–200 nt), and multi-stage cleaning at both the atomic and nucleotide levels. Compared to ARES, it covers ~7× more RNAs, a wider size range, and includes more recent structures. This gives the community a purpose-built benchmark for studying size generalization that did not previously exist.

- **Consistent outperformance across all metrics and both datasets.** EquiRNA achieves the best results on Mean RMSD, Median RMSD, Relative Error, and Relative Ranking on both rRNAsolo and ARES. The margins are substantial (e.g., 2.00 improvement over dyMEAN on Mean RMSD; up to 17% relative error reduction). The Relative Ranking results (Table 3) are particularly informative: other methods' ranking degrades noticeably on rRNAsolo versus ARES, while EquiRNA's remains high, supporting the claim that its advantage is tied to handling larger RNAs.

- **Figure 5 provides fine-grained evidence of size-robust performance.** The breakdown of test RNAs into four size intervals (100–110, 110–120, 120–150, 150–200 nt) shows that EquiRNA maintains low RMSD across all intervals after training only on 50–100 nt, while baseline methods degrade on larger intervals. This is the strongest direct evidence in the paper for the size-generalization claim.

## Weaknesses

### Fatal
None.

### Major

- **The "size-insensitive K-nearest neighbor sampling strategy" is never described.** The term appears approximately 10 times across the abstract, introduction, method overview, figure caption, and ablation section — yet the paper provides no mechanism for what makes it "size-insensitive" or how it differs from standard KNN. The ablation (Table 4, Row 4) shows that removing it hurts performance (+1.42 Mean RMSD on validation, +0.57 on test), confirming it matters, but the reader cannot evaluate whether this is a novel contribution, a standard design choice, or something else entirely. The claim that this strategy "allows the model to engage with a more extensive range of local neighbors during training" is too vague to be informative. This is an evidential gap for a component presented as a key contribution in the abstract.

- **The size-generalization claim in the title is not fully commensurate with the experimental scope.** The paper trains on 50–100 nt and tests on 100–200 nt — a 1–2× size shift — and the best evidence for across-size robustness is Figure 5, which subdivides the test set. However, the test set covers only RNAs up to 200 nt, and the paper explicitly notes that RNAs beyond 200 nt are excluded "due to considerable time for candidate conformation generation." This is a reasonable practical constraint, but the title "Size-Generalizable" implies a capability that extends beyond a single, modest size shift. The paper would benefit from either (a) testing on at least a small set of RNAs >200 nt (even if computationally expensive), (b) demonstrating a monotonic relationship where EquiRNA's advantage over baselines grows with RNA size, or (c) tempering the title/abstract claims to match the demonstrated scope. As written, the headline claim outstrips the evidence.

### Minor

- **Efficiency claims are qualitative, not quantitative.** The Complexity Analyses section states that EquiRNA "costs much less inference time than ARES" and is "even faster than EGNN" due to hierarchical modeling enabling a smaller K. No actual runtime numbers or speedup ratios are reported. This is easily fixable but leaves an important practical claim unsupported.

- **The ARES dataset is a weak test of size generalization, and this is not acknowledged as a limitation.** The paper correctly reports that ARES has only 3 test RNAs over 100 nt out of 16. Given that the paper's central theme is size generalization, the strong ARES results could simply reflect that EquiRNA is a better architecture overall. The paper should explicitly note this limitation rather than treating the ARES results as supporting the size-generalization thesis.

- **"Full-atom" terminology is slightly imprecise.** The paper states "preserve full-atom representations" but then clarifies it excludes hydrogen atoms (following ARES protocol). This is not a technical error — the clarification is in the same sentence — but it could confuse readers on first pass.

### Trivial

- The phrase "much less inference time" (Complexity Analyses) is unnecessarily informal for quantitative exposition.
- Some figure references appear as images in the extracted text, making it impossible to verify exact numerical values from the main text alone.

## Nice-to-Haves

- An analysis showing that the nucleotide-level representations learned on small RNAs and large RNAs are similar (e.g., via CKA similarity or nearest-neighbor alignment) would directly evidence the transfer mechanism that EquiRNA relies on. This is the strongest missing experiment for the size-generalization claim.
- Adding a single experiment with a larger size gap (e.g., train on 50–100, test on a few RNAs >200 nt from the RNAsolo database) would substantially strengthen the title claim.
- Reporting confidence intervals or significance tests for the main results (Table 1) would help assess whether the improvements are statistically significant, especially given that the paper notes "small performance differences among SOTA models."

## Removed Points

These points were raised by reviewers but are removed or downgraded after verification against the paper:

- *"Testing on RNAs substantially larger than 200 nt is missing"* — The paper explicitly scopes this out due to computational constraints (line 50: "Given that RNAs with over 200 nucleotides require considerable time for candidate conformation generation"). This is a practical limitation, not a flaw in experimental design. Re-framed as a scope limitation in the Major weakness above rather than a standalone criticism.
- *"Performance gains may come from better architecture, not size generalization"* — The experiment IS a test of size generalization (training on small, testing on large). The critic's requested control experiment (train both on mixed-size data) would be a nice addition but is not necessary to support the conclusion that EquiRNA generalizes better across sizes. Removed.
- *"Standard KNN with fixed K is already size-insensitive"* — This is an assumption the reviewer makes without evidence. The paper never confirms or denies this. The actual mechanism is underspecified, which IS a problem, but speculating about what it might be is not a valid criticism. The KNN mechanism weakness above captures the real issue (under-description) without this speculation.
- *"Dataset not released / no download link"* — The paper constructs rRNAsolo from the publicly available RNAsolo database and describes the construction process in detail. Release status is irrelevant to evaluating the paper's contributions.
- *"Missing implementation details"* — Standard hyperparameters (layers, hidden dims, learning rate) are commonly deferred to the appendix and are not a core flaw.
- *"Statistical significance not reported"* — While desirable, this is not standard practice across all venues for this type of benchmark evaluation. Relegated to Nice-to-Haves.
- *"No mention of related works"* — I cannot verify the existence of missing works. Removed by instruction.
- *"Typos / formatting"* — Parser artifacts, not author errors.

## Novel Insights

The most genuinely novel observation that emerges from the reviews is the mismatch between the paper's rhetorical framing and the actual experimental scope. The paper positions itself as tackling "size generalization" — a broad, difficult problem in graph representation learning — but its experimental evidence is confined to a single trained-on-small/tested-on-larger setup within a 2× size range. This is not a flaw in the method (the results are consistently positive), but it is a gap between narrative and evidence. The hierarchical nucleotide-reuse idea is sound, and the ablation confirming that reusing nucleotide-level representations is the key (not just the equivariance or the KNN) is the paper's strongest empirical finding. A sharper paper would lean into this specific mechanism as the contribution rather than claiming to have "effectively addressed" the entire size-generalization challenge.

## Suggestions

1. **Provide a clear, self-contained description of the size-insensitive KNN strategy.** What is the algorithm? How does it differ from standard KNN? Is K fixed or adaptive? Is there an ablation comparing the "size-insensitive" variant to standard KNN? Without this, the claimed contribution cannot be evaluated.
2. **Add a brief experiment or analysis probing RNAs >200 nt.** Even a small number of test RNAs (e.g., 3–5) would significantly strengthen the generalization claim. If this is truly infeasible, consider adjusting the title from "Size-Generalizable" to something like "Generalizing to Larger RNAs via Hierarchical Nucleotide Representations."
3. **Acknowledge the ARES dataset limitation explicitly** when using it to argue for size generalization.
4. **Provide quantitative runtime comparisons** (wall-clock time per RNA or per candidate structure) rather than the current qualitative claim.
5. **Add an analysis of learned representation similarity** across RNA sizes (e.g., CKA between nucleotide embeddings from small vs. large RNAs) to directly support the claimed transfer mechanism.
