## Summary

This paper identifies the problem of selection bias in interventional causal discovery — scenarios where subjects are pre-selected before interventions are applied. It argues that existing graphical paradigms (mutilated DAGs, augmented DAGs) fail because they do not model the temporal asymmetry where selection precedes intervention. The paper proposes the interventional twin graph, a graphical model that explicitly separates a counterfactual pre-intervention world (where selection occurs) from the observed post-intervention world, connected by shared exogenous noise. It characterizes Markov properties and equivalence criteria, and sketches an algorithm (CDIS) for causal discovery under this model.

## Strengths

- **Identifies and formalizes a genuinely unaddressed problem gap.** The paper correctly notes (Section 1, line 12) that "no existing work tackles selection bias in interventional causal discovery," and provides concrete reasoning for why naive extensions of the augmented DAG paradigm fail — specifically because the temporal ordering (selection before intervention) changes the statistical patterns in a way the augmented DAG misrepresents (contrast between Figure 1d's predictions and the correct behavior shown via the twin graph in Example 3, lines 98–99).

- **The Interventional Twin Graph (Definition 1) is a novel and principled modeling idea.** It cleanly captures the selection-before-intervention asymmetry by splitting each affected variable into observed post-intervention (X) and counterfactual pre-intervention (X*\_aff) copies, connected by shared noise (ε\_aff), with selection (S*) applied in the basal world. This is conceptually distinct from augmented DAGs and is inspired by twin networks/SWIGs. Example 3 (line 91) concretely shows the model correctly predicts that intervening on X₁ alters p(X₂|X₁) — which the augmented DAG fails to capture.

- **Theorem 1 provides a sound formal bridge between the graphical model and testable statistical implications.** It proves that d-separations involving ζ and X conditional on S* in the twin graph imply both (1) conditional independencies within each interventional distribution and (2) conditional invariances across interventions. This soundness guarantee is essential for any constraint-based discovery procedure built on this framework.

- **Theorem 2 and the worked examples (Example 4, line 171) provide concrete insight into identifiability boundaries.** For instance, they show that with only one intervention on X₁, a causal relation cannot be distinguished from a selection-induced correlation, but adding a second intervention on X₂ can. This goes beyond simply stating the equivalence criterion and gives practical intuition about what the model can and cannot identify.

## Weaknesses

### Fatal
None.

### Major

- **The CDIS algorithm is described at a level of abstraction that makes it non-reproducible and effectively a sketch, not a specification.** The algorithm (lines 173–179) is presented as three high-level bullet points: Step 1 ("Run FCI on p^{(0)}"), Step 2 ("orientations are derived from pooled data... Significant pruning is applied"), Step 3 ("information from M^{(k)} are used to orient uncertain edges"). Key operational details are absent: (a) what "significant pruning" means in Step 2 and how it is implemented, (b) how Step 2 specifically constructs a PAG from pooled data across two regimes, (c) exactly how Step 3 applies the twin-graph-specific rules from Lemmas 4–6, (d) what conditional independence test is used and how thresholds are set, and (e) no pseudocode or algorithmic skeleton is provided. The paper itself acknowledges (line 197) that "the completeness guarantee of the CDIS algorithm, though hypothesized, is yet to be proven." For a paper that claims an algorithmic contribution, this level of specification is insufficient for evaluation, reproduction, or building upon.

- **The real-world experimental evaluation (Section 5.2) is purely qualitative and does not constitute evidence that the algorithm "effectively identifies true causal relations" as claimed in the abstract.** The gene regulatory network analysis (lines 186–188) mentions discovered edges (RELA→RUNX1, JUNB→MAFF) and cites supporting literature, but reports no quantitative metrics — no precision, recall, F1, structural Hamming distance, or comparison to any baseline. There is no ground truth set, no discussion of false positives, and no comparison to what existing methods (e.g., ignoring selection bias) would find. The education dataset discussion (line 188) is an interpretive analysis of heterogeneous treatment effects that does not actually use CDIS to estimate a causal graph — it is unclear what the algorithm contributed to the analysis. For a paper that stakes a practical algorithmic claim, this evaluation falls far short of the standard needed to support that claim.

- **No comparison to any baseline method.** The paper argues that existing paradigms (augmented DAGs, standard FCI) fail when selection bias is present. This is the central motivation for the paper. Yet the experimental section includes no comparison against any of these methods, even as a naive baseline. A comparison showing that CDIS recovers correct structure where an augmented-DAG-based approach (or FCI ignoring selection) fails would directly validate the paper's core thesis. Its absence leaves the claimed advantage untested.

### Minor

- **The algorithm's three-step design is motivated by a single 3-variable example, and it is unclear how the principles generalize.** Example 5 (line 173) shows that orienting on the observational skeleton leads to a false edge X₁←X₂ in one specific DAG. The algorithm addresses this by orienting on "denser adjacencies from interventional data" and then refining. However, the paper provides no analysis of when this strategy succeeds or fails, no theoretical characterization of the conditions under which the denser interventional skeleton avoids the false propagation issue, and no ablation study isolating this mechanism. The algorithmic principle is stated but not validated or characterized beyond the single worked example.

### Trivial
- Line 173: "obatined" → "obtained" (typo in the available text).
- Line 177: The sentence "Significant pruning is applied since conditional dependencies from p^{(0)} must hold in ." appears to be incomplete.

## Nice-to-Haves
- Adding a proper simulation study that varies graph size/density, number and location of interventions, which variables are ancestrally selected, and sample size, with standard metrics (SHD, precision/recall, runtime) would substantially strengthen the paper.
- A comparison against a baseline that ignores selection (e.g., standard FCI on pooled data, or the augmented DAG approach of Yang et al., 2018) would directly validate the paper's central thesis that accounting for selection matters.
- The gene regulatory network analysis would benefit from a comparison against a known reference set of regulatory relationships or against results from a method that does not account for selection.

## Removed Points
These points are flagged to be removed; treat them with caution.
- **Missing Section 5.1 (synthetic experiments):** The harsh critic noted the absence of synthetic experiments from the available text. However, the paper's abstract and Section 1 reference these experiments, and their absence from the parsed text is likely a parser stripping artifact, not an author omission. Removed per the rule about parser-stripped content.
- **Missing proofs:** The harsh critic criticized the absence of proofs for theorems/lemmas. Per the hard rule, missing proofs in the parsed text are a parser artifact (likely in a stripped appendix). Removed.
- **Section 2 truncation:** The harsh critic noted that Section 2 ends mid-sentence ("However, does"). This is a parser artifact. Removed.
- **"Dear reviewer" notes:** Criticized as occupying space or being unprofessional. These are pre-submission revision markers. Removed per formatting/style nitpick rule.
- **Strength about real-world validation providing "concrete evidence":** The strength finder claimed that the gene regulatory network analysis provides "concrete evidence." This conflicts with the verified weakness that the real-world evaluation is purely qualitative and anecdotal. Removed per the rule that when a strength and weakness disagree, the weakness wins.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
- **Reframe the contribution.** The paper's strongest contributions are the problem identification and the interventional twin graph framework (Definition 1, Theorem 1, Theorem 2). These are publishable as a theoretical contribution. Consider restructuring to present the theoretical framework as the primary contribution, with the CDIS algorithm presented as a sketch or proof-of-concept rather than a fully validated algorithmic claim.
- **If retaining the algorithmic claim, provide complete pseudocode** for CDIS specifying: (a) the CI test used and its parameters, (b) the exact procedure for Step 2's "significant pruning," (c) how Step 3 applies Lemmas 4–6 as orientation rules, and (d) the output format.
- **Add at minimum one simulation study** that operationalizes the paper's motivating examples (Examples 1 and 2) as testbeds, comparing CDIS against a naive FCI approach that ignores selection. Report standard causal discovery metrics.
- **The gene regulatory network analysis would benefit from** a comparison against a known reference set of regulatory relationships or against results from a method that does not account for selection, to demonstrate that the selection-aware discovery actually improves upon the status quo.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>