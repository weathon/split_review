Now I have a thorough understanding of the paper and the calibration anchors. Let me produce the final consolidated review.

---

## Summary

This paper identifies post-treatment selection as an important but underexplored challenge in interventional causal discovery with latent confounders. Post-treatment selection (e.g., quality-control filtering after interventions) produces invariance/variance patterns indistinguishable from genuine causation under existing frameworks. The authors propose a new augmented-DAG formulation that explicitly models post-treatment selection via selection nodes, characterize the resulting fine-grained interventional Markov equivalence class (\(\mathcal{FI}\)-Markov equivalence), introduce a new graphical representation (\(\mathcal{F}\)-PAG) with novel edge marks, and develop the \(\mathcal{F}\)-FCI algorithm with soundness and completeness guarantees. Experiments on synthetic data and a single-cell gene perturbation dataset demonstrate improved precision and reduced SHD over baselines including FCI-interven and CDIS.

## Strengths

- **Novel and well-motivated problem formulation**: The paper convincingly demonstrates (Figure 1, §2.2) that post-treatment selection produces the same marginal-variant/conditional-invariant pattern as causation, rendering it non-identifiable within standard interventional Markov equivalence classes. This is a genuine gap in the literature that has real consequences in biological studies and clinical trials.

- **Clean theoretical framework**: The augmented-DAG formulation with intervention indicators and selection nodes (Definition 1) provides a principled way to unify observational and interventional data under post-treatment selection. Theorem 1 and Figure 4 systematically characterize how CI patterns involving intervention indicators (\(\psi\)) distinguish causation, latent confounding, and selection structures, providing the theoretical foundation for the algorithm.

- **Novel equivalence class and graphical representation**: The \(\mathcal{FI}\)-Markov equivalence class (Definition 2) and \(\mathcal{F}\)-PAG (Definition 5) go beyond standard PAGs by encoding whether observed dependencies arise from genuine causation, latent confounding, or selection-induced inducing paths. The introduction of Type I and Type II inducing nodes (Definition 6) provides a clean operational criterion for when further disambiguation is possible.

- **Empirical outperformance against relevant baselines**: On synthetic data (Figure 6), \(\mathcal{F}\)-FCI achieves higher precision and lower SHD than FCI-interven and CDIS — methods that already handle latent confounders — demonstrating that the post-treatment selection component provides gains beyond what existing latent-aware methods offer. The method also produces interpretable results on real single-cell perturbation data.

## Weaknesses

### Fatal

None.

### Major

- **No ablation isolating the contribution of the post-treatment selection component**: The paper compares \(\mathcal{F}\)-FCI against full baseline methods (GIES, IGSP, FCI-interven, CDIS, etc.) but never compares \(\mathcal{F}\)-FCI against itself without the selection-refinement steps (e.g., skipping Step 2.3, or disabling the Type I inducing node identification). Without this ablation, it is difficult to determine how much of the empirical gain comes from modeling post-treatment selection specifically versus from general advantages of the augmented-DAG formulation or implementation details. This weakens the central empirical claim that \(\mathcal{F}\)-FCI specifically solves the post-treatment selection problem. An ablation would be straightforward to add and would substantially strengthen the paper.

### Minor

- **Theorem statements are informal in the main text**: Theorems 3 and 4 (§4) state soundness and completeness in descriptive rather than formal language (e.g., "is consistent with the augmented DAG in arrowhead, tails, square…"). While the formal proofs presumably reside in the appendix, the main-text statements lack the precision needed to evaluate exactly what is guaranteed. The completeness claim in particular should explicitly condition on the availability of interventions on Type I inducing nodes — this limitation is acknowledged in §6 but not reflected in the theorem statement.

- **DAG Precision and DAG SHD metrics are ambiguous for PAG-like outputs**: \(\mathcal{F}\)-PAG outputs contain bidirected edges (↔) and novel edge marks. It is unclear from the main text how these are mapped to an adjacency matrix for computing precision and SHD. If bidirected edges are treated as false positives (no edge in the true DAG), this would systematically penalize methods that correctly represent latent confounding with ↔ edges while favoring methods that omit them. Clarifying this mapping is important for interpreting the quantitative results.

- **Real-world evaluation is qualitative only**: Section 5.2 applies \(\mathcal{F}\)-FCI to the Norman dataset and evaluates against Enrichr prior knowledge, but reports no quantitative metrics and no baseline comparison. This section provides a proof-of-concept rather than rigorous validation. This is a minor weakness since the synthetic experiments carry the main empirical weight.

- **Algorithm specification partially unclear**: Step 2.2 lists orientation rules with CI-pattern tuples, but due to what appear to be formatting artifacts, the distinguishing patterns are not visible in the extracted text. More importantly, the procedure for enumerating inducing paths and identifying Type I nodes in a partially oriented graph (Step 2.3) is described at a high level without algorithmic detail on how paths are found or how the stopping criteria are implemented. This does not threaten reproducibility given the available code, but limits clarity.

### Trivial

- Edge mark notation (\(\xrightarrow{\Delta}\), \(\xrightarrow{\blacktriangle}\)) is introduced with reference to Figure 5 but would benefit from a self-contained definition table mapping each mark to the structural configuration it encodes.

## Nice-to-Haves

- A controlled simulation that varies the amount and type of post-treatment selection while holding other parameters fixed, to demonstrate that \(\mathcal{F}\)-FCI's advantage scales with the strength of selection bias.
- A side-by-side figure showing a specific graph where FCI-interven produces a false positive due to post-treatment selection and \(\mathcal{F}\)-FCI correctly avoids it — this would make the benefit tangible to readers.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"Baseline comparisons are unfair because GIES/IGSP/UT-IGSP assume no latent confounders"** — REMOVED. While GIES and IGSP indeed assume causal sufficiency, the paper also compares against FCI-interven and CDIS, which DO handle latent confounders. Including methods that don't handle latent confounders as lower-bound baselines is standard practice, and the comparisons against FCI-interven and CDIS are fair and informative. The harsh critic's claim that ALL comparisons are unfair overstates the case.

2. **"The mapping between CI patterns and orientation rules lacks a completeness proof"** — REMOVED. Figure 4 provides an explicit table mapping 6 CI conditions to structures. The paper's claims about pattern coverage are stated as characterization results, and proofs are in the (stripped) appendix. Demanding an exhaustive case analysis in the main text is unreasonable.

3. **"The paper overstates the gap by not engaging with other approaches that also use multiple environments to detect selection"** — REMOVED. This is a generic criticism without specific citations of missing work. The paper does engage with the relevant interventional causal discovery literature (FCI-interven, CDIS, JCI, etc.).

4. **Formatting artifacts in the algorithm** (all CI tuples appearing as \((\perp,\perp,\perp,\perp)\)) — REMOVED. These are parser extraction artifacts. The original paper submission does not have this issue.

5. **"Scalability results not in main text"** — REMOVED. The paper references Figure 11 for scalability results. Whether this is in appendix or main text is a presentation choice, and the critic's assertion that it "should" be in the main text is a matter of preference, not a flaw.

## Novel Insights

The key novel insight emerging from this work — beyond the paper's own stated contributions — is that post-treatment selection and causation, while indistinguishable in their marginal/conditional invariance patterns, can be disambiguated by examining structural asymmetries along inducing paths, specifically through the behavior of non-endpoint "inducing nodes" under targeted hard interventions. This insight essentially shows that interventions on mediating/confounding variables (Type I nodes) can "break" the selection-induced spurious invariance, revealing whether an observed dependence is causal or selection-driven. This principle may generalize beyond the specific FCI-based algorithm presented here.

## Suggestions

- Add the ablation study comparing \(\mathcal{F}\)-FCI with vs. without Step 2.3 (the Type-I-inducing-node refinement). This is the single highest-impact improvement and would directly address the main empirical weakness.
- Make the theorem statements in §4 self-contained and precise, and explicitly condition the completeness claim on the availability of Type I inducing node interventions.
- Add a brief note explaining how bidirected and \(\mathcal{F}\)-PAG-specific edges are mapped to adjacency matrices for DAG Precision/SHD computation.
- Include a small table or paragraph defining all \(\mathcal{F}\)-PAG edge marks (\(\square\), \(\blacktriangle\), \(\xrightarrow{\Delta}\), \(\xrightarrow{\blacktriangle}\)) with their structural semantics, independent of the figure.

## Score and Decision

### Anchor comparison:

| Path | Avg Score | Decision | Comparison |
|------|-----------|----------|------------|
| `/home/wg25r/review_agent/human_reviews_2026/ssYeoL4ksl.md` | 5.50 | Reject | Pairwise-only causal discovery with cycles; strong theory but no multivariate extension. F-FCI provides a complete multivariate algorithm and addresses a comparably novel problem. **F-FCI is slightly stronger.** |
| `/home/wg25r/review_agent/human_reviews_2026/lejOV6j3cj.md` | 5.00 | Accept (Poster) | FLOP — efficient score-based discovery for linear models; strong empirical results but limited theoretical novelty. F-FCI has substantially stronger theoretical contribution but weaker empirical validation (no ablation). **Comparable overall, with different strength profiles.** |
| `/home/wg25r/review_agent/human_reviews_2026/bOfiLeoUJf.md` | 4.67 | Accept (Poster) | Graph pruning with tiered knowledge; sound algorithm. F-FCI addresses a more novel and overlooked problem with a more elaborate theoretical framework. **F-FCI is stronger.** |
| `/home/wg25r/review_agent/human_reviews_2026/HfiRzzmFt8.md` | 4.00 | Reject | ABCDEFG — Bayesian causal discovery; ambitious but poorly motivated with unclear benefits. **F-FCI is clearly stronger.** |
| `/home/wg25r/review_agent/human_reviews_2026/r4TvgVFo9L.md` | 3.50 | Reject | InvarGC — Granger causality with latent confounders; missing baselines, strong assumptions. **F-FCI is clearly stronger.** |
| `/home/wg25r/review_agent/human_reviews_2026/cP2nOl3t3W.md` | 3.20 | Withdrawn/Reject | Causal canonical models; insufficient empirical support. **F-FCI is clearly stronger.** |

The paper has genuine originality (the post-treatment selection problem is real and overlooked), a clean theoretical framework with soundness/completeness results, and outperforms relevant baselines. The main weakness — lack of an ablation study — is addressable in rebuttal and does not threaten the paper's core contribution. The paper sits above the Accept Poster threshold but below the strongest papers in the field. Relative to the anchors, a score of **5.5** is appropriate.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>