Here is my final consolidated review.

## Summary

The paper proposes Cross-Risk Minimization (XRM), a method for automatic environment discovery in OOD generalization without requiring any human-annotated environments. XRM trains two twin networks on random halves of the training data, using a label-flipping "echo chamber" mechanism to amplify reliance on spurious correlations, then derives binary environment labels via a cross-mistake formula. The method provides a flip-count-based hyper-parameter selection criterion and can annotate both training and validation data. Experiments on sub-population shift and domain generalization benchmarks show that XRM-discovered environments enable downstream algorithms to achieve worst-group-accuracies competitive with human-annotated environments.

## Strengths

1. **Genuinely novel and well-motivated architecture.** The twin-network setup with held-out splits and label flipping is a clever departure from prior environment discovery methods. The "echo chamber" intuition — where twins reinforce each other's reliance on spurious correlations through confident held-out mistakes — is clearly explained and grounded in the simplicity bias of neural networks. The ability to annotate both training and validation examples (line 267–268) is a real advantage over prior methods.

2. **Flip-count hyper-parameter selection replaces human-annotated validation.** The paper proposes a concrete criterion — maximize label flips at the last iteration — that correlates with downstream worst-group-accuracy (Fig. 4, top-left panel). This is a genuine replacement for human-annotated validation sets, solving a problem the paper correctly identifies as a limitation of prior work (lines 55–59).

3. **Competitive empirical results across multiple benchmarks.** On the four standard sub-population shift datasets (Waterbirds, CelebA, MultiNLI, CivilComments), XRM+GroupDRO averages 80.4% worst-group accuracy vs. 80.6% with human annotations (line 297–298). The method shows particular strength on ColorMNIST (69.7% vs. human 10.1%), where human annotations are themselves poor.

4. **Computational efficiency.** XRM takes 10 minutes on Waterbirds vs. 20 hours for LS (lines 308–309), making it practical for large-scale use.

5. **Principled failure analysis grounded in causal theory.** Section 6 honestly acknowledges the fundamental impossibility of the task (citing Lin et al., 2022) and provides a concrete causal analysis with four ColorMNIST variants to characterize when XRM succeeds (invariant feature is more complex) and fails (invariant feature is simpler). This level of rigor is rare in environment discovery papers.

## Weaknesses

### Major

- **BAM comparison is selectively ignored, distorting the empirical picture.** The paper states (line 305): "The second best method with no access to environment information, JTT, drops to 58.9%." However, Table 2 (line 352) shows BAM achieving 79.8% worst-group accuracy without any environment annotations — substantially better than JTT (58.9%) and nearly matching XRM's 80.4%. The paper lists the compared methods (line 303) as "LfF, EIIL, JTT, CnC, AFR, and LS" — omitting BAM from the text while including it in the table. This is a factual inaccuracy in the reported results and makes XRM appear far more dominant (21.5-point gap to JTT) than it actually is (0.6-point gap to BAM). The authors should either discuss BAM explicitly or explain why BAM is not a fair comparison.

### Minor

- **"Oracle" language overstates the results.** The abstract claims XRM enables "oracle worst-group-accuracy" (line 12), and "oracle-like" or "oracle-level" appears throughout (lines 44, 67, 140, 186, 295, 574). But on MultiNLI (72.1 vs. 73.4), CivilComments (72.2 vs. 73.8), and MetaShift (77.5 vs. 80.3), XRM+GroupDRO underperforms Human+GroupDRO. The paper's own measured statement — "closely matching 80.6%" (line 298) — is accurate, but "oracle" rhetoric invites scrutiny that undermines an otherwise solid empirical story.

- **CivilComments+SUBG collapse is unexplained.** XRM+SUBG on CivilComments drops to 44.6% worst-group accuracy — far below even ERM+None (67.2%) and Human+SUBG (71.1%) (Table 1, line 209). This is the worst result in the entire table. The paper includes a dedicated "When Does XRM Fail?" section (Section 6) but does not analyze this failure or discuss why XRM's binary environments interact poorly with SUBG on this particular dataset.

- **DomainBed results are notably weaker on DomainNet.** In Table 3, CORAL+XRM on DomainNet achieves 35.87/11.60 vs. CORAL+Human at 41.97/13.25 — a gap of over 6 points in average accuracy. The paper describes results as "comparable" (line 365), which is reasonable for VLCS, PACS, OfficeHome, and TerraInc, but not for DomainNet.

- **"Class-balanced cross-entropy loss" is underspecified.** Algorithm 1 (line 162) uses a "class-balanced cross-entropy loss" but the paper does not specify whether this is implemented via resampling, reweighting, or another mechanism. This matters for reproducibility.

### Trivial

None.

## Nice-to-Haves

- The logical-OR in the cross-mistake formula (Eq. 6) is a conservative choice (any example misclassified by at least one twin is flagged). A brief discussion of the alternative (logical-AND) and why OR is preferred would strengthen the method description.
- An ablation comparing the flip-count model selection criterion to simple baselines (e.g., fixed training budget) would further justify the design choice.

## Removed Points

Points from the reviewers that were filtered out with justifications:

- *"Convergence criterion is underspecified and may rely on human annotations"* — The critic argued that "Until convergence" (Algorithm 1) needs a concrete definition and that the method may still need human annotations for early stopping. The paper explicitly references the appendix for implementation details (line 178: "See app:code for implementation details"). Since the parser strips appendices and this detail exists in the original submission, this criticism is removed per policy. The main paper also provides a non-human-dependent model selection criterion (flip count at last iteration, lines 252–253) and Fig. 4 top-right panel shows flips stabilize naturally.

- *"Cross-mistake formula doesn't capture uncertainty"* — The critic noted that the argmax-based formula only captures explicit misclassifications, not uncertainty. This is by design: the method checks whether a twin makes an *error*, not whether it is uncertain. Removed as a misunderstanding of the method's design.

- *"Comparison table mixes reproduced and quoted numbers in an unfair way"* — The paper is transparent about this with the † notation (line 313: "Symbol † denotes original numbers"). This is standard practice at top venues. Removed.

- *"LS runtime comparison confounded by architectural choices"* — Both methods were run on the same 32GB Volta GPU (line 309). The critic's speculation about architectural confounds is not grounded in the paper. Removed.

- *"Binary environment assignment insufficient for complex spurious correlations"* — The critic's argument about "multiple spurious features" is speculative and not substantiated by the paper. The concrete evidence (CivilComments+SUBG collapse) is kept as a verified weakness above. The broader claim about binary assignments being fundamentally insufficient is removed.

- *"Prior methods could theoretically work without human annotations"* — The critic suggested that JTT et al. might not inherently require human-annotated validation sets. This is scope creep — the paper's contribution is evaluated on whether XRM works, not on re-analyzing prior work's requirements. Removed.

- Various formatting nitpicks, speculative "could this be a problem" concerns, and generic area-of-concern sweeps from the harsh critic. Removed.

## Novel Insights

The key tension revealed by merging these reviews is that XRM's strongest claimed advantage — achieving "oracle" performance without human annotations — is both its most compelling selling point and its most vulnerable rhetorical overreach. The paper would be stronger by leaning into the nuance: XRM is competitive with human annotations on some datasets, substantially better on ColorMNIST (where human annotations are themselves poor), and demonstrably worse on others. The BAM comparison (which the paper itself includes in Table 2 but ignores in the text) further complicates the narrative by showing that a prior method achieves 79.8% without any annotations — only 0.6 points behind XRM. The paper's honest failure analysis (Section 6) stands in tension with its overstated "oracle" rhetoric; the former is the paper's real strength and the latter is its biggest vulnerability.

## Suggestions

1. **Correct the BAM discussion.** Acknowledge that BAM achieves 79.8% without environment annotations (Table 2 line 352), discuss why XRM's 80.4% is or isn't practically meaningful compared to BAM, and either reproduce BAM under the same conditions or explain why the comparison is not apples-to-apples.

2. **Tone down the "oracle" language.** Replace "oracle worst-group-accuracy" and similar phrasing with "competitive with human annotations" or "closely matching human-annotated performance." The empirical evidence supports the latter, not the former.

3. **Analyze the CivilComments+SUBG collapse.** This is the most striking failure in Table 1 and directly relevant to understanding XRM's limitations. A brief analysis (even a speculative one) would strengthen the paper's otherwise thorough failure analysis section.

4. **Specify how class balancing is implemented** in the class-balanced cross-entropy loss (Algorithm 1 line 162).

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>