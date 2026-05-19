- Decision: Reject
- Avg Score: 5.67
- Scores: 6, 3, 8
Now I have a complete picture. Let me produce the final review.

## Summary

This paper introduces GDL-DS, a benchmark for evaluating geometric deep learning (GDL) models under distribution shifts across three scientific domains (particle physics, materials science, biochemistry). It categorizes shifts causally (covariate, concept, conditional), studies three levels of OOD information availability (No-Info, O-Feature, Par-Label), and evaluates 3 backbones × 11 algorithms across 10 distribution shift scenarios (30 settings). The benchmark design is thoughtful, combining causal reasoning with practical OOD info levels.

## Strengths

- **Comprehensive multi-domain scope**: Table 1 shows GDL-DS is the only benchmark spanning particle physics, materials science, and biochemistry while covering covariate, concept, and conditional shifts under all three OOD-info levels. Prior benchmarks (DrugOOD, WILDS, etc.) are confined to single domains or shift types.
- **Causal categorization of distribution shifts**: Section 3.1 introduces a principled data model decomposing inputs into causal ($X_c$) and independent ($X_i$) parts, providing rigorous formal definitions of covariate, concept, and conditional shifts. The sub-typing of conditional shift into $\mathcal{C}$- and $\mathcal{T}$-conditional is a novel conceptual contribution beyond ad-hoc shift labels (e.g., "scaffold shift").
- **Realistic shift sources grounded in genuine scientific challenges**: Each dataset's shift arises from a real application scenario—varying pileup levels at the LHC (Track), DFT fidelity gaps (QMOF), and scaffold/size/assay shifts in drug discovery (DrugOOD-3D)—rather than synthetic perturbations.
- **Consistent experimental protocol across methods**: The same validation/OOD splits and tuning regime are applied across all backbones and algorithms, enabling fair comparisons that are rare in the fragmented prior literature.

## Weaknesses

### Fatal

None. The benchmark's conceptual framework and dataset curation are fundamentally sound.

### Major

1. **Section 4.3 ("Insightful Conclusions") is effectively empty.** The section header promises detailed analysis of the three headline takeaways from the introduction, but after the framing sentence ("We structure this subsection by first presenting our conclusions, exemplified by representative observations and rational explanations"), the subsection contains no actual content—it immediately transitions to Section 5 (Conclusion). The three takeaways listed in the introduction (TL methods for concept shifts, DA methods for critical features, OOD generalization with good group partitions) are never systematically analyzed, evidenced, or connected to specific rows in Table 3 within the main paper body. These claims are presented as key contributions but lack the substantive analysis section that would support them. For a benchmark paper whose value proposition is providing "actionable insights," this is a critical gap.

2. **Missing Point Transformer results with no explanation.** The paper states "Experimental results on 2 of 3 backbones are shown in Table 3" (line 149) and lists Point Transformer among the included backbones (line 131), but never explains why results for the third backbone are absent. For a benchmark paper claiming coverage of "3 GDL backbones," omitting results for one backbone without any justification (e.g., computational cost, training instability, or that results are deferred to an appendix) undermines the completeness claim and limits the generalizability of findings. The reader cannot assess whether the observed patterns hold for Point Transformer.

3. **Empty "Hyperparameter Tuning" subsection (line 145).** The section header appears with no content whatsoever. Hyperparameter tuning strategy (search ranges, validation criteria, compute budget) is essential for reproducibility and for assessing whether comparisons across methods are fair. This is a concrete reproducibility gap that should be filled.

4. **Causal data model assumptions are stated but not validated for individual datasets.** The paper acknowledges (line 63) that the data model "does not aim to cover all possible causality relationships," but the entire analytical framework (categorizing each shift as covariate/concept/conditional, decomposing features into $X_c$ and $X_i$) depends on these assumptions holding for each specific dataset. No empirical validation is provided—for example, verifying that $\mathbb{P}_S(Y|X_c) = \mathbb{P}_T(Y|X_c)$ holds for datasets classified as covariate shift, or testing whether the $X_c/X_i$ decomposition is stable across domains. While demanding full causal discovery is beyond scope, the paper should at minimum discuss which datasets are most likely to violate the assumptions and how that could affect the conclusions drawn.

### Minor

1. **Conformer generation method for DrugOOD-3D is unspecified.** The paper states "We leverage a conformer for each molecule and then assign a 3D coordinate to each atom" (line 116) but does not state which conformer sampling algorithm (e.g., ETKDG, RDKit) was used. Different conformer generators produce different geometries and can affect GDL model performance, which is a reproducibility concern for this particular dataset.

2. **Section 4.2 observations are generic and the "second recommendation" is unsupported.** The observation that OOD generalization methods in the No-Info level "find it hard to provide significant improvement" is consistent with prior work. The subsequent recommendation to "proposing novel OOD methods based on assumptions that better match the scientific applications" (line 153) is a generic suggestion not justified by experiments in this paper—it reads as boilerplate rather than a finding.

3. **The analysis does not discuss when takeaways fail.** For example, the paper states TL methods help under concept shifts, but even a cursory look at the takeaways framework suggests boundary conditions (e.g., when few OOD labels are available, TL can hurt). The paper acknowledges this for pileup shifts (TL$_{100}$ underperforms ERM) but does not systematically map when each takeaway holds or breaks.

### Trivial

- No "Limitations" section in a benchmark paper that would benefit from one.
- Section 4.3 is extremely brief (one framing sentence before jumping to the conclusion).

## Nice-to-Haves

- Including Point Transformer results or a clear justification for their omission.
- A figure or scatter plot showing ID vs. OOD performance across all methods and backbones would improve readability over the dense results table.
- Release of code and datasets (if not already done in supplementary materials).

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"Table 1 content not visible (parser artifact)"** — This is a PDF parsing issue, not an author error. The actual submission contains the table.
2. **"DrugOOD already covers GDL and distribution shifts"** — The paper acknowledges DrugOOD (line 37, 116) and its claim is about "numerous scientific applications" (plural); DrugOOD covers only drug discovery. The paper's claim is accurate.
3. **"Reproducibility concerns about not disclosing all hyperparameters"** — The harsh critic's list of missing details (e.g., seeds, ratios) is standard for a main paper; these are typically in an appendix or supplementary that the parser may have stripped. The concrete gap is the empty "Hyperparameter Tuning" section, which is kept as Major weakness #3.
4. **"Statistical rigor needed (t-tests)"** — Single-run evaluation with 3 replicates is standard for this type of benchmark work. Not a required practice.
5. **"Strengthening the Paper on Its Own Terms" suggestions about measuring feature criticality** — These are suggestions for additional experiments, not identifiable weaknesses in the paper as written. Moved to Nice-to-Haves implicitly.
6. **Strength Finder's "actionable recommendations" claim** — The recommendations are stated in the introduction, but as noted in Major weakness #1, they lack systematic analysis support. The strength is partially valid (the design enables them) but overstated. 
7. **Criticism that the paper does not analyze surgical fine-tuning** — The paper mentions surgical fine-tuning as a "potential solution" (line 151), appropriately flagging it as future direction. It does not claim to have tested it.
8. **"The causal data model is a strong assumption" framed as fatal** — The paper acknowledges limitations (line 63). Demanding causal discovery validation goes beyond what benchmark papers typically provide. Demoted from critical to Major (#4) to reflect the real concern (lack of dataset-specific validation) without overstating severity.
9. **"Track simulation details not specified"** — The paper provides a thorough description at a level appropriate for its scope (lines 93-99). Excessive simulation details are supplementary material.
10. **"AUC vs accuracy for Track unclear"** — Table 3 headers (which are rendered as an image, not fully parseable) likely clarify this. The paper text explains the task correctly.

## Novel Insights

None beyond the paper's own contributions. The harsh critic and strength finder largely restate the paper's content rather than generating new synthetic insights. The most important observation from merging the reviews is the severity of the missing analysis section (4.3 being effectively empty), which both reviews touched on but neither fully emphasized as the central structural weakness.

## Suggestions

1. **Fill in Section 4.3** — This is the single highest-impact fix. Use the three takeaways from the introduction as organizing headings. For each takeaway, walk through the relevant rows of Table 3, show the evidence (e.g., "for concept shifts, TL$_{1000}$ improves over ERM by X% on Assay and Y% on Fidelity, but degrades when..."), and discuss boundary conditions. This is what the paper promised and needs to deliver.
2. **Explain or supply the missing Point Transformer results** — Either include results (even a summary table or appendix) or clearly justify why they are absent (e.g., compute constraints) and discuss whether the observed patterns are expected to generalize.
3. **Fill the "Hyperparameter Tuning" section** — At minimum, summarize the search ranges, validation metric, and budget. This is critical for reproducibility.
4. **Add a Limitations subsection** to the conclusion covering: (a) the causal assumptions and which datasets may violate them, (b) that only 2 of 3 backbones are reported, (c) synthetic nature of the Track dataset, and (d) the limited number of DA and TL algorithms evaluated.
5. **Specify the conformer generation method** used for DrugOOD-3D.
