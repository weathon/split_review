Now I have a thorough understanding of the paper and the reviewer claims. Let me produce the final consolidated review.

## Summary

The paper introduces an unsupervised pipeline for discovering dynamic functional connectomes from calcium imaging data in *C. elegans*. The method: (1) computes time-varying pairwise "differential affinities" between neural activity traces, (2) organizes these affinities into a time × worms × pairwise-affinities tensor and applies non-negative tensor factorization (NTF), and (3) runs the nested weighted stochastic block model (NWSBM) on the resulting affinity factors to reveal transient neuronal communities. A prediction about the aversive neuron AWB's role in salt sensing was experimentally validated (p=5.7e-11, +25% effect size). The core idea—tensorizing pairwise affinities rather than individual traces—is well-motivated for the problem.

## Strengths

- **Novel tensor formulation (time × worms × pairwise affinities).** Instead of the conventional tensor built from raw neural traces (which restricts similarity to multi-linear forms), the paper constructs a 3-way tensor where the third mode is vectorized pairwise affinities (Section 2.2). This allows non-linear similarity measures to be computed before factorization and makes the temporal factor directly interpretable as experimental epochs (e.g., stimulus application). This is a genuine advance over prior multi-linear approaches.

- **Principled differential affinity concept.** The paper introduces a time-varying similarity measure based on monotonic changes (absolute derivatives of activity traces), motivated by biological intuition that coinciding increases/decreases indicate interaction (Section 2.1, Fig. 2). This avoids pitfalls of static metrics (e.g., high similarity from two silent neurons) and is a well-motivated departure from global-time correlation.

- **Two-stage pipeline combining NTF with generative community detection (NWSBM).** The paper proposes a novel combination: first factorizing the affinity tensor to extract time-localized functional motifs, then applying a Bayesian weighted community detection model on the resulting weighted graphs (Section 2.3). This is distinct from prior work that either analyzes static networks or uses less principled clustering methods.

- **Experimental validation of a surprising, testable prediction.** The algorithm predicted an unexpected role for the aversive neuron AWB in salt sensation. Silencing AWB significantly *increased* salt avoidance (p=5.7e-11, +25% effect size)—the opposite of what would be expected from an aversive neuron's canonical role (Section 3.2). This counterintuitive, statistically strong result confirms the method's ability to make biologically meaningful predictions that evade expert intuition.

- **Interpretability via reversion to original traces.** The paper shows that communities inferred for salt sensing can be traced back to original calcium traces, confirming the affinity measure reflects genuine coordinated activity during the relevant stimulus epoch (Fig. 5c,d).

- **Benchmark comparison of community detection methods.** The NWSBM was systematically compared against five alternatives on weighted LFR synthetic networks (Table 1), providing evidence for the choice of community detection algorithm.

## Weaknesses

### Major

- **The differential affinity measure lacks a precise mathematical definition.** The entire pipeline rests on the computation of $a_{ij}^{(t)}$, yet the paper never states an explicit formula. The description (Section 2.1) is entirely in prose: "compare two neurons' derivatives during intervals in which both had a constant sign," "in terms of their absolute derivatives," and "two neurons with very similar but opposite sign derivatives are still likely to be interacting." It is unclear whether the affinity is the product of absolute derivatives, their integral over the interval, a thresholded binary indicator, or something else. The notation $a_{ij}^{(t)}$ is introduced but never defined by an equation. This is not a trivial omission—it is the foundation of the pipeline—and prevents independent reproduction and full evaluation of the method.

- **Crucial tensor factorization details are not reported.** The paper does not state the number of components $R$ used, nor how it was selected (e.g., core consistency diagnostic, cross-validation, reconstruction error analysis). There is no discussion of initialization strategy, stability across random initializations, or potential degeneracy/collinearity among components—common issues with CP decompositions. Two interpretable components are shown (Fig. 4), but without knowing how many total components were extracted and whether the shown ones are representative, the reader cannot assess whether the decomposition is robust or selectively presented. These are standard reporting requirements for tensor factorization studies.

### Minor

- **The benchmark evaluates only the community detection step, not the full pipeline.** Table 1 compares NWSBM against alternatives on synthetic LFR networks, but this does not test the end-to-end method (affinity computation → NTF → community detection). The NMI scores are relatively low (most under 0.65, some below 0.3), and the paper does not discuss what this implies for the real data where no ground truth exists. While component-wise benchmarking is common and defensible, the paper would benefit from an explicit acknowledgment of this scope limitation and a discussion of how the synthetic graphs relate to the real affinity graphs.

- **The experimental validation, while striking, covers only one predicted neuron out of "multiple" claimed.** The paper states "our algorithm predicted the involvement of multiple neurons in the salt-sensing circuit" (Section 3.2), yet only AWB is tested and the remaining predictions are not even listed. The AWB result is compelling in its own right, but a single successful prediction—even a strong one—does not establish that a substantial fraction of the method's predictions are correct. The paper should acknowledge this explicitly and ideally list the other predicted neurons (with confidence measures) to give readers a sense of breadth.

- **Connection between affinity factors and NWSBM distributional assumptions is not discussed.** The paper states that affinities "can be readily treated as adjacencies" (Section 2.3) because they are non-negative and bounded, but does not characterize their empirical distribution or discuss whether it is compatible with the edge-weight model used by NWSBM. Given that NWSBM treats edge weights as covariates in a Bayesian framework (which is flexible), some diagnostic (e.g., comparing the affinity distribution to the model's assumptions for the inferred communities) would strengthen the methodological justification.

- **The "completing" missing data claim is mentioned once and never demonstrated.** Section 2.2 notes in passing that the tensor formulation "can also help with 'completing' affinity matrices containing missing data from a few neurons," but this capability is never used, analyzed, or mentioned again. It should either be demonstrated or removed.

### Trivial

- The number of neurons remaining after restricting to sensory and interneurons (from the original 189) is not stated, which affects understanding of the tensor dimensions and computational cost.
- The worm factor loadings (which worms contribute to each component) are described qualitatively in figure captions but not reported quantitatively.
- Software library versions (tensortools, graph-tool) are not specified.

## Nice-to-Haves

- A small worked example of the differential affinity computation (e.g., two toy traces with the resulting affinity values) would significantly improve reproducibility.
- Reporting the tensor reconstruction error and a stability analysis (e.g., similarity of factors across random initializations) would increase confidence in the decomposition.
- If feasible, testing one or two additional predictions from the salt-sensing community (even with a simpler behavioral assay) would substantially broaden the validation.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"Broad applicability claim is standard but unsupported."* — This is a generic remark about a standard concluding statement. Most methods papers make such claims without demonstration; singling this out as a weakness is not constructive.
- *"The paper should state software versions."* — Trivial implementation detail; the paper cites the specific libraries (tensortools, graph-tool). Version numbers are rarely included in conference papers and do not affect the scientific contribution.
- *The reviewer's framing that the benchmark "does not evaluate the full pipeline" was kept as Minor (not removed), but the reviewer's stronger language suggesting it "does not support the main claim" is downgraded* — benchmarking individual components is standard practice; the limitation is acknowledged but is not a structural flaw.
- *Several of the strength finder's claims about "broad applicability" are dropped as generic/superficial.* — The paper claims this but does not demonstrate it; listing it as a strength overstates its evidentiary basis.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a genuinely novel observation about the work that the authors themselves did not articulate.

## Suggestions

1. **Provide the explicit formula for $a_{ij}^{(t)}$.** This is the highest-priority revision. Include a concrete numerical example with two short traces showing how the affinity values are computed.
2. **Report $R$ and the method used to select it.** Include reconstruction error as a function of $R$ and a stability analysis (e.g., factor similarity across random initializations). State the initialization strategy used.
3. **Acknowledge the single-neuron validation scope explicitly**, and list all neurons predicted to be in the salt-sensing community (with loadings or confidence intervals) so readers can assess the method's breadth.
4. **Add a diagnostic** comparing the empirical distribution of affinity values in the extracted components to the NWSBM edge-weight assumptions.
5. **State the number of sensory/interneurons** remaining after the data restriction.

## Score and Decision

The paper presents a genuinely interesting conceptual framework and a compelling experimental validation. However, the two major weaknesses—(1) the core affinity measure lacks a mathematical definition, and (2) critical tensor factorization details (number of components, selection method, initialization, stability) are unreported—mean the method is not reproducible in its current form and its validity cannot be fully assessed. These are addressable in revision, but as submitted, the paper falls below the acceptance threshold.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>