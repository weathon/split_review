## Summary

This paper proposes LACR (LLM-Assisted Causal Recovery), a method that uses LLMs to extract conditional associational relationships (CARs) from retrieved scientific literature, then formalizes inconsistency resolution as the MAXCON optimization problem (proved NP-hard with an approximation algorithm) to recover causal graphs via constraint-based principles. The core idea—using LLMs as literature-based associational extractors rather than direct causal reasoners—is clever and avoids well-known LLM weaknesses in causal reasoning.

## Strengths

- **Principled inconsistency resolution with formal guarantees**: The paper formalizes the reconciliation of conflicting CAR extractions as the MAXCON optimization problem (Definition 3), proves NP-hardness (Theorem 1), and provides Algorithm 2 with a proven approximation ratio of \(1/(\Delta+1)\). This goes beyond prior LLM-based causal discovery work, which typically handles inconsistency ad hoc or ignores it entirely.

- **Retrieval-augmented extraction consistently outperforms pure LLM knowledge**: On ASIA, DOC/CON settings (using retrieved literature) improve F1 by 13.1% vs. only 1.6% for BG (LLM background knowledge only) against the updated ground truth (Section 4.3, lines 163–164). This validates the paper's core design choice: LLMs as literature-based extractors rather than direct reasoners.

- **Superior performance on the challenging SACHS domain**: On SACHS (11 protein-interaction variables), LACR with BG and DOC settings outperforms both the pure LLM baseline and the hybrid method of Takayama et al. (2024) (Section 4.3, line 167), demonstrating the approach works where domain complexity challenges pure LLM reasoning.

- **Formal characterization of two distinct inconsistency types**: The paper carefully distinguishes causal existence inconsistency from d-separation inconsistency (Section 3.1), provides Lemma 1 connecting minimal d-separation sets to associations, and quantifies how many CAR pieces are filtered at each stage (Section 4.5). This analytical decomposition is more rigorous than prior work.

## Weaknesses

### Major

- **Circularity in the ground-truth-update experiment**: The paper's headline evidence that LACR is "sensitive to new evidence" is obtained by modifying the ASIA ground truth "based on evidence returned by LACR" (line 152) and then reporting improved F1 against this modified ground truth. While the paper does cite specific external papers (Horne et al., 2012; Wang et al., 2018, etc.), these were surfaced by LACR, and there is no independent validation (e.g., domain experts reviewing the updates blind to LACR's output). The evaluation conflates discovery with validation: the papers cited as evidence for updating the ground truth are themselves the ones LACR returned. Without an independently validated updated ground truth, the claim that LACR "recovers accurate causal graphs that are better aligned with the latest domain knowledge" is not convincingly supported by this experiment.

- **No comparison to standard causal discovery algorithms**: The entire evaluation compares LACR only against other LLM-based methods (Jiralerspong et al., 2024; Zhou et al., 2024; Takayama et al., 2024). The paper's motivation (lines 4, 13–14) criticizes statistical CD methods for data collection bias, yet never shows whether LACR outperforms even a simple PC algorithm or FCI on the same variables. Without baselines such as PC, FCI, GES, or NOTEARS, there is no evidence that the LLM-based literature approach adds value over what a standard algorithm would produce from the original observational data.

- **Unacknowledged biases contradict the "overcome data collection bias" claim**: The paper states LACR "helps us to overcome the data collection bias problem" (line 20), but never discusses three significant bias sources it introduces: (a) publication bias—literature over-represents positive results and well-studied relationships; (b) LLM extraction bias—the LLM may misinterpret or hallucinate relationships (no analysis of extraction accuracy is provided); (c) retrieval bias—the document retrieval step determines which evidence the LLM sees and is critically underspecified (no database named, no value of *k*, no matching function details). These are at least as serious as the data collection biases that motivate the paper.

### Minor

- **Experiment scale is extremely limited**: Evaluation uses only two tiny graphs—ASIA (8 nodes, 8 edges) and SACHS (11 nodes, 16 edges). For a causal discovery paper, this is insufficient to demonstrate general utility. Even a 20–30 variable synthetic graph would substantially strengthen the case.

- **Document retrieval pipeline is irreproducible**: The paper specifies "a fixed number of the most relevant scientific papers" (line 60, 66–67) without naming the database (PubMed? Semantic Scholar?), the value of *k*, or the matching function used. These details are essential for reproducibility.

- **MAXCON NP-hardness stated without proof**: Theorem 1 asserts NP-hardness without even a reduction sketch. While space is tight, some justification is expected for a central theoretical claim.

- **No variance or uncertainty reported**: All results are point estimates with no repeated runs or confidence intervals, even though LLM outputs are stochastic.

- **No limitations section or discussion of failure modes**: The paper concludes (lines 184–187) without addressing when the method would fail (e.g., when no relevant literature exists, when retrieved literature is contradictory, or when the LLM extracts incorrect information).

### Trivial

- Section 4.5 discusses the precision-recall trade-off from consistency checks (lines 178–180), which partially addresses one of the reviewer concerns—this is noted here for completeness.

## Nice-to-Haves

- A manual evaluation of LLM extraction accuracy on a sample of document-CAR pairs would address the extraction bias concern.
- Adding a moderate-sized synthetic experiment (20–30 variables with known ground truth) would demonstrate scalability.
- Reporting repeated runs with variance would strengthen empirical rigor.

## Removed Points

*"Suspiciously perfect orientation accuracy (1.0 TEA)"* — With only 8–16 edges, perfect orientation is entirely plausible and not suspicious. Removed as an unsubstantiated concern.

*"Approximation ratio 1/(Δ+1) is very weak"* — This is a known bound for the greedy independent-set algorithm. The paper does not claim the bound is tight; its value is in providing any guarantee. Removed as a misinterpretation of standard theoretical guarantees.

*"Proposition 1 carries no meaningful information"* — Proposition 1 is a routine surjectivity check that the CAR space maps to edge existence. This is standard sanity-check formalism and not claimed as a contribution. Removed.

*"Definition 1 notation is garbled"* — The garbled notation (e.g., "Assumptions $^{\,l}$ and 2") is a PDF parsing artifact, not an author error. Removed per formatting-artifact rule.

*"Lemma 1 is not novel"* — Lemma 1 is presented as a known property, not as a novel contribution. The criticism misunderstands its role. Removed.

*"Inconsistency reduction framed as purely beneficial"* — The paper explicitly discusses the precision-recall trade-off (lines 178–180: "can lead to an increase in AR...but may cause a decrease in AP"). The reviewer's claim is inaccurate. Removed.

*"Orientation NP-hardness proof missing"* — The paper at least states the reduction from FAS (line 128) and mentions page limits. This is a space constraint, not a flaw in the method. Demoted to the minor point about Theorem 1 above, which has no justification at all.

*"Pure LLM baseline higher on ASIA original ground truth"* — The paper transparently reports this (line 166: "both baseline methods slightly outperform LACR 1") and explains it. This is honest reporting, not a weakness.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Replace the circular ground-truth-update experiment with one where domain experts independently validate the updated graph, blind to LACR's output, and report agreement rates.
2. Add baselines including PC, FCI, and at least one score-based method (e.g., GES) run on the original observational data for both ASIA and SACHS.
3. Fully specify the retrieval pipeline: database name, *k* value, matching function, and provide representative prompt templates in an appendix.
4. Add a discussion of limitations addressing publication bias, extraction bias, and retrieval bias explicitly.
5. Report results from multiple runs (e.g., 5 runs with GPT-4o) with mean and standard deviation.

## Score and Decision

MY FINAL SCORE: <score>4</score>
MY FINAL DECISION: <decision>Reject</decision>