Now I have all the information needed. Let me write the final consolidated review.

---

## Summary

This paper presents the first systematic study of scale shift in domain generalization for crowd localization. It constructs ScaleBench, a benchmark with 17,138 images (including 1.5M manually annotated bounding boxes) partitioned into four scale-differentiated domains via a novel GMM-based patch splitting and domain partitioning method. The paper benchmarks 20 DG algorithms on ScaleBench, finding most underperform compared to simple ERM. A theoretical analysis frames scale shift as a mixture of diversity and correlation shifts. A case-study method (SemanticHook) is proposed and analyzed, yielding three empirical insights about data scaling, scale as a primary attribute, interpolation efficacy, and effective components.

## Strengths

- **First dedicated benchmark for scale shift in crowd localization DG.** The paper manually annotates bounding boxes for 1.5M objects across 2,700 images from SHHA, SHHB, and QNRF, integrating them with three existing datasets into ScaleBench (17,138 images). The domain partition method using 2D GMM on scale × vertical location, followed by patch filtering and equal-size domain splitting with Gaussian smoothing, is a thoughtful and creative solution to a non-trivial problem (Section 2.2.2).

- **Theoretical framing of scale shift as a mixed domain shift.** Theorem 1 (Section 3.1) formally connects scale shift to established DG concepts by showing that when scale distributions differ ($p_1(c|z) \neq p_2(c|z)$), both diversity shift ($Div_{div} > 0$) and correlation shift ($Div_{cor} > 0$) arise simultaneously. This provides a principled explanation for why methods targeting only one type of shift underperform.

- **Empirical analysis (Q1–Q4) yields actionable insights.** The four controlled experiments generate genuinely useful findings: (i) adding in-distribution data beyond what is already present provides marginal benefit (Table 3, e.g., TN→S 77.92% vs. TNB→S 77.94%); (ii) scale is a primary attribute — 30% IID-sampled data achieves comparable performance to the full dataset (Figure 4); (iii) interpolation helps primarily for extreme scale shifts (Table 4, Tiny: 13.84→33.73 with RA). These insights are valuable for future work.

## Weaknesses

### Fatal
None.

### Major

- **Insufficient transparency on how the 20 DG algorithms were adapted for dense prediction.** The paper's central empirical claim — that most DG algorithms underperform ERM on scale shift — depends critically on fair and competent adaptation of each method from its original setting (typically classification) to the dense-prediction crowd localization architecture. The paper provides essentially zero detail on: (a) which specific layers/modules were modified for each algorithm (e.g., where CORAL aligns feature statistics, how DANN's domain discriminator interfaces with encoder-decoder features); (b) whether and how hyperparameters (alignment weights, learning rates, momentum) were searched; (c) how algorithms requiring specific optimization schemes (e.g., IRM's two-phase procedure) were handled. The paper states it "reproduced 20 state-of-the-art domain generalization algorithms and integrated them with a robust crowd localization baseline" (line 112) and uses DomainBed's Leave-One-Out protocol, but no adaptation methodology is described. Without this information, a reader cannot distinguish between genuine limitations of DG algorithms and artifacts of poor integration. This is the most consequential gap because it undermines the paper's most attention-grabbing claim.

- **No variance or confidence intervals reported for any quantitative result.** The paper makes comparative claims throughout (e.g., "marginal improvement," "limited help") without any measure of uncertainty. Table 3 shows a 0.02 F1 difference (77.92% vs. 77.94%) used to support the claim that adding domain B offers "minimal" benefit — this is well within likely noise. No seed repetitions are reported. For a benchmark paper whose main currency is quantitative comparisons, this is a significant omission that prevents readers from assessing the reliability of the conclusions.

### Minor

- **SemanticHook's claimed mechanism is not well-justified.** The paper asserts "the added perturbation ε affects only the pixel values, which primarily influences the semantic information of the original image" (Section 3.2, Intuitive Remark). This claim is unsupported: pixel-level Gaussian noise perturbs *all* visual features (texture, edges, scale), not selectively semantic information. The ablation study in Table 5 compares "semantic concentrated" vs. "scale concentrated" perturbation, but neither perturbation type is defined — the paper simply states "we opt for two perturbations conducted on semantic concentrated feature" without specifying how they were constructed. This weakens the case study and the derived insight #1.

- **Theoretical analysis is informal and the connection to SemanticHook is tenuous.** The decomposition in Eq. 6 is presented as a chain-rule integration over attributes $s, c, \ldots$ without a clear generative model, and the derivation of spurious association $c \mapsto y$ is intuitive rather than rigorous. More importantly, SemanticHook does not explicitly address either diversity shift or correlation shift (it does not enforce invariance or decorrelation), so the theoretical framing and the proposed method are not directly connected. The paper acknowledges SemanticHook is a "case study" rather than a solution, which mitigates this, but the disconnect remains.

- **Several implementation details needed for reproducibility are missing.** The number of GMM components $K$ used for patch splitting is never specified (Section 2.2.2 only says it is "pre-defined"). The "minimal height" threshold for filtering unqualified patches is not quantified. The heuristic search for optimal $\sigma_m$ in Eq. 5 is mentioned but not described (cost, stability, search range). The annealing schedule for $\gamma$ is discussed qualitatively ("starts from 0, then increases") but no schedule or bounds are given.

- **Interpretation of Q3 (interpolation) results is slightly inconsistent.** The paper states "image interpolation provides modest benefits" but the Tiny domain improves from 13.84 to 33.73 with Random Augmentation — a substantial gain. The paper acknowledges this ("the improvement on Tiny domain is because its original poor performance") but this reasoning is somewhat circular. A more precise characterization would be that interpolation helps substantially for extreme shifts but less for moderate ones, which is itself an interesting finding.

### Trivial

- The garbled text fragments (e.g., "432 433 434...", "rsity Shift)") are parser artifacts and do not appear in the original submission.
- The sentence "While we could not reproduce every algorithm, we welcome contributions" (line 112) is unusual for a benchmark paper — it would be more transparent to state which algorithms could not be reproduced and why.

## Nice-to-Haves

- Sensitivity analysis on the number of domains $M$: the paper fixes $M=4$; exploring $M=3$ or $M=5$ would test whether conclusions are robust to this choice.
- Analysis of learned representations (e.g., feature visualization or probe experiments) to directly verify whether SemanticHook actually reduces scale information in the feature space, rather than relying on the indirect perturbation-ablation argument.
- Clarification of whether "Inference Augmentation" in Table 4 is intended as an adversarial attack or a test-time robustness evaluation — the current description is ambiguous.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *Criticism that Table 2 shows only a subset of algorithms.* This is a parser artifact — the table is embedded as an image; the full table with all algorithms exists in the original submission.
- *Criticism that the benchmark dataset is not released or described with access information.* Per the hard rules, questioning availability of a cited entity is removed. The paper states ScaleBench is established; release details are assumed to be handled outside the review format.
- *Criticism requesting missing appendix content.* The parser strips appendix sections; these are assumed to exist in the original submission.
- *Formatting/style nitpicks* — these are parser artifacts, not author errors.

## Novel Insights

Beyond the paper's own contributions, two observations from this review stand out. First, the paper's central tension — a well-constructed benchmark paired with insufficiently documented algorithm adaptation — is a recurring pattern in domain generalization research that attempts to benchmark methods not designed for the target task. The community would benefit from standardized adaptation protocols for migrating classification DG algorithms to dense prediction architectures. Second, the finding that scale shift constitutes a *simultaneous* diversity and correlation shift (Theorem 1) is a genuinely useful conceptual contribution: it predicts that neither invariant feature learning (targeting correlation shift) nor data diversification (targeting diversity shift) alone will suffice, explaining the observed ERM competitiveness and pointing toward hybrid strategies.

## Suggestions

1. **Document the DG algorithm adaptation in full detail.** For each of the 20 algorithms, specify: which layers/feature maps were modified, how hyperparameters were searched (method, ranges, budget), and whether any algorithms required non-trivial architectural changes. Even a table in the main paper summarizing this would dramatically improve credibility.
2. **Add variance estimates.** Report results over at least 3 seeds with mean and standard deviation for all main tables. This is standard for benchmark papers and would allow readers to distinguish signal from noise in comparative claims.
3. **Define the perturbation types in the ablation study.** Specify what "semantic concentrated perturbation" and "scale concentrated perturbation" actually are — how they are generated, and why they are believed to affect one attribute more than the other.
4. **Softened the theoretical claims.** The "proof" language for Theorem 1 is strong for what is essentially an application of existing definitions (Ye et al., 2022) to the scale shift setting. Clarify that the contribution is in *identifying* scale shift as a mixed shift, not in deriving new OOD theory.
5. **Reconciled the Q3 narrative with the results.** The Tiny improvement (13.84→33.73) is striking and deserves emphasis, not downplaying. A more nuanced conclusion — "interpolation is highly effective for extreme scale shifts but marginal for moderate ones" — would be both more accurate and more informative.

## Score and Decision

**Originality:** 7/10 — First study on scale shift DG in crowd localization; the mixed-shift framing is conceptually novel.
**Importance of research question:** 8/10 — Scale shift is a real, practical problem for deployed crowd models.
**Claims well supported:** 4/10 — The central empirical claim about DG algorithms is undermined by insufficient documentation; some analytical claims are overstated relative to evidence.
**Soundness of experiments:** 5/10 — Benchmark construction is sound, but missing variance estimates and insufficient algorithm adaptation details weaken confidence.
**Clarity of writing:** 6/10 — Generally clear despite parser artifacts; the SemanticHook mechanism section needs better justification.
**Value to the research community:** 7/10 — ScaleBench and the empirical insights are valuable; the benchmark fills a gap.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>