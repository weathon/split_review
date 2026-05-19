- Decision: Reject
- Avg Score: 4.67
- Scores: 5, 6, 3
Now I have all the information needed to produce the consolidated review.

## Summary
This paper proposes Cross-Risk Minimization (XRM), an environment discovery method that trains twin networks on random halves of data with label flipping based on confident held-out mistakes. XRM requires no human environment annotations and provides a hyper-parameter selection criterion (counting label flips) and a cross-mistake formula to annotate both training and validation data. Experiments across multiple OOD benchmarks show XRM enabling downstream algorithms to achieve worst-group accuracies competitive with human-annotated environments.

## Strengths
- **Achieves oracle-competitive worst-group accuracy without human environment annotations**: Table 1 shows GroupDRO+XRM obtains 88.1% (vs. human-annotated GroupDRO's 86.5%) on Waterbirds, 89.1% (vs. 88.3%) on CelebA, and the average over the commonly-reported quartet (Waterbirds, CelebA, MultiNLI, CivilComments) is 80.4% vs. 80.6% with human annotations.
- **Substantially faster than prior environment discovery methods**: The paper reports a single LS run on Waterbirds took 20 hours, whereas an XRM run on the same GPU takes 10 minutes (line 308-309).
- **Annotates both training and validation data with a single cross-mistake formula** (Eq. 3 / line 263): Because every example is held-out for at least one twin, the logical-OR operation assigns environment labels to all training and validation points without requiring a separate annotation procedure.
- **Eliminates surgical early stopping**: Figure 2 (top-right) shows label flipping occurs almost exclusively for minority groups and stabilizes by convergence, removing the need for the precise early-stopping that prior discovery methods depended on.
- **Includes an honest failure analysis** (Section 6): The paper identifies four ColorMNIST variants where XRM works or fails, tying results to an impossibility result. This demonstrates awareness of limitations rather than overclaiming universality.

## Weaknesses

### Fatal
None.

### Major
- **Factual inaccuracy in competitor comparison**: The paper states "The second best method with no access to environment information, JTT, drops to 58.9%" (line 305). However, Table 2 lists BAM under the same (✗ training annotations, ✗ validation annotations) column, achieving an average worst-group accuracy of **79.8%** — far exceeding JTT's 58.9% and nearly matching XRM's 80.4%. BAM is included in the table but never mentioned in the text comparing methods. This is a factual misrepresentation of the baseline landscape. XRM still outperforms BAM (80.4 vs. 79.8), but the paper's narrative that prior no-annotation methods trail by over 20 points is incorrect. The authors should either explicitly compare with BAM or explain why BAM is not considered a directly comparable method.

- **Anomalously low ColorMNIST human-annotation baseline requires explanation**: In Table 1, GroupDRO with human-annotated environments achieves only 10.1% worst-group accuracy on ColorMNIST — essentially no better than ERM without any annotations (10.0%). In the standard ColorMNIST setup (Arjovsky et al., 2019), the two human-defined environments (based on color-label correlation strength: 90% and 10%) should allow GroupDRO to substantially improve over ERM. The paper attributes XRM's success to discovering "environments conducive of stronger generalization than the ones originally proposed by humans" (line 296), but does not clarify what the "Human" environments are in this experiment or why GroupDRO fails so completely with them. Without this clarification, the dramatic XRM advantage on ColorMNIST is suspect — it could reflect a non-standard definition rather than a genuine limitation of human annotations. The authors should describe the exact ColorMNIST setup, the "Human" environment definition used, and explain the 10.1% result.

### Minor
- **Model selection criterion validated on one dataset only**: The proposed hyper-parameter tuning method (counting label flips at convergence) is justified via correlation with downstream worst-group accuracy in Figure 2 (top-left panel) **only on Waterbirds**. Since this criterion is presented as a central component replacing validation-set-based selection, showing the correlation holds across additional datasets (CelebA, CivilComments, etc.) would significantly strengthen the claim.

- **No ablation of the cross-mistake formula's logical-OR**: Equation 3 (line 263) uses logical-OR, meaning any example misclassified by either twin falls into the minority environment. This means an example both twins get wrong for different reasons still lands in the same environment. No ablation compares OR vs. AND vs. XOR to justify this choice (line 265 mentions the design choice but does not test alternatives).

- **Sensitivity to the single random data split not studied**: The paper uses a single Bernoulli draw per example to assign each twin's held-in data (line 175). While results are averaged over 10 runs (each with a different split), the paper does not analyze how much variability is attributable to the split itself versus training stochasticity.

- **CIFAR-10 result is qualitative only**: Figure 3 shows interesting spurious correlations discovered by XRM on CIFAR-10, but no quantitative OOD generalization results are provided for this dataset.

- **"Oracle-like performance" claim is overstated for specific cases**: While the average across datasets supports the claim, individual algorithm-dataset combinations show large gaps (e.g., SUBG on CivilComments: Human=71.1 vs. XRM=44.6 in Table 1; DomainNet in Table 3: CORAL+Human 13.25 vs. CORAL+XRM 11.60).

### Trivial
- The abstract says "endow OOD generalization algorithms with oracle-like performance" — the paper could benefit from qualifying this with the specific conditions under which it holds (e.g., when the invariant feature is more complex than the spurious one).

## Nice-to-Haves
- **Study flip-count correlation across more datasets** to strengthen the model selection criterion.
- **Ablation of split variability**: report variance components from split randomization vs. training seed.
- **Quantitative CIFAR-10 evaluation**: construct test environments via some heuristic and report worst-group accuracy.
- **Explore the OR vs. AND vs. XOR ablation** for the cross-mistake formula.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"The CORAL with XRM vs. human gap on DomainNet is real and unaddressed"** — The paper says XRM is "comparable" to human annotations (line 365), which is a reasonable characterization: CORAL+XRM (11.60) improves over ERM (9.30) and moves toward CORAL+Human (13.25). The gap exists but the claim is not that XRM matches human annotations everywhere. Removed because the characterization is accurate and the weakness is overstated by the reviewer.

2. **"No comparison with XRM on the 'hard' ColorMNIST variants"** — The failure analysis (Section 6) explicitly tests XRM on the four ColorMNIST variants and discusses where it fails (InveCOLOR, MCOLOR). This criticism is factually incorrect; the paper does exactly this comparison.

3. **Strength: "this paper addresses an important problem"** — Generic, not a specific strength of the paper itself. Removed per filtering rules.

4. **"No discussion of the number of flips as a function of model architecture"** — This is a direction for future work, not a weakness of the current paper. The paper's scope is on the algorithm's effectiveness, not on architectural analysis.

5. **Weakness about XRM not reporting "which hyperparameters were selected via the flip-count criterion"** — The paper's flip-count criterion IS the model selection method; the hyperparameters are selected to maximize flips at convergence. The paper describes this process in Section 3.3. The question of how the selected hyperparameters compare to oracle-selected ones is a reasonable research question but not a missing ablation.

6. **Strength about "Eliminates the need for early stopping" from the Strength Finder** — This is kept in the main strengths as it is verified (Figure 2, top-right, and lines 433-435).

## Novel Insights

None beyond the paper's own contributions. The reviews surface a useful factual correction (the BAM oversight) and a genuine concern about the ColorMNIST human baseline, but neither reviewer identifies a novel limitation or implication that the paper itself does not already acknowledge. The failure analysis (Section 6) is the most insightful part of the paper and neither reviewer adds to it.

## Suggestions
1. **Acknowledge BAM in the main comparison text** and explicitly state whether it is or is not comparable to XRM. The current framing (JTT as the closest competitor) is factually incorrect and erodes trust.
2. **Clarify the ColorMNIST experimental setup** — specify exactly what the "Human" environments are, cite the source, and explain why GroupDRO achieves only 10.1% with them. If this is a non-standard ColorMNIST variant, state that clearly.
3. **Add at least one additional dataset correlation plot** (e.g., CelebA or CivilComments) to the flip-count model selection analysis in Figure 2 to demonstrate generalizability of the criterion.
4. **Tone down the "oracle-like performance" language** or qualify it more carefully (e.g., "on the commonly-reported quartet of benchmarks").
