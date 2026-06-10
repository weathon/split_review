## Summary

This paper presents an empirical study comparing Visual Prompt Tuning (VPT) against Full Finetuning (FT) across 19 datasets from VTAB-1k, aiming to characterize *when* and *why* VPT outperforms FT. The main analysis organizes transfer scenarios into a 2×2 quadrant framework along task-objective disparity and data-distribution similarity, and investigates causal mechanisms through controlled ablations (Mixed and FT-then-PT variants). The paper concludes VPT is preferable in 3 of 4 quadrants when data is limited, and that its advantage stems from a "unique manner" of preserving original features while adding parameters.

## Strengths

- **Well-designed controlled ablations (Mixed and FT-then-PT) that rule out plausible alternative explanations (§5.2, Tables 1–2).** The Mixed variant (prompts + full finetuning of all parameters) underperforms both FT and VPT on all three dataset groups (e.g., Natural mean: VPT 79.53, FT 75.19, Mixed 72.80). The FT-then-PT variant (FT first, then add prompts) also underperforms VPT. These experiments are carefully constructed and convincingly show that VPT's advantage is not simply from extra optimization dimensions or sequential feature preservation — a genuinely useful negative result that advances understanding beyond prior work.

- **Empirical disentanglement of overfitting as a cause (§5.1, Figure 3).** The paper examines training/testing loss curves across all 19 tasks and finds that overfitting is observed in only 1 of 10 Natural/Specialized tasks, yet VPT still outperforms FT in most of these cases. This directly refutes the simple explanation that VPT's advantage reduces to FT overfitting with many parameters, providing a more nuanced picture.

- **Systematic dataset-scaling analysis (§4.4, Figure 4).** The paper evaluates both methods across training set sizes from 400 to 20,000 samples, showing that FT catches up and surpasses VPT in 9 of 12 cases as data grows. This offers practical guidance about the data regimes where each method is preferable — an informative dimension absent from the original VPT paper (Jia et al., 2022).

## Weaknesses

### Major

- **The "four-quadrant" framework that structures the paper's central "when" claim is not established by the evidence presented.** The framework rests on two binary dimensions: task-objective disparity (Natural/Specialized = low, Structured = high) and data-distribution similarity (measured by FID). This reduces to a two-group comparison (low- vs. high-disparity tasks) with a secondary FID variable that only discriminates within one group. All 8 Structured datasets are in one bucket with VPT winning uniformly, and the FID-based split within the 11 low-disparity tasks is a qualitative reading of a scatter plot. No decision boundary, statistical test, or validated threshold is offered. The paper's own one-shot experiments further undermine the robustness: on Structured tasks, FT actually beats VPT in mean accuracy (17.11 vs. 16.83, Table 3). Given only 19 data points and a non-standard use of FID (computed between real datasets, acknowledged in a footnote), the claimed 3-out-of-4-quadrant pattern is over-interpreted relative to the evidence strength.

- **Missing variance reporting undermines the headline win/loss counting claim.** The paper reports running five trials (line 126) but the main results tables (Tables 1 and 2) present only single point estimates without standard deviations or confidence intervals. On tasks where the FT-VPT gap is small (e.g., Resisc45: 83.2 vs 83.4; Retinopathy: 73.3 vs 73.1; EuroSAT: 95.7 vs 96.2), it is impossible to assess whether these differences are meaningful or within measurement noise. The paper's central empirical claim — "VPT outperforms FT in 16 of 19 instances" — cannot be verified from the reported data. This is a straightforward issue to fix and significantly affects the credibility of the paper's quantitative narrative.

- **The positive "why" conclusion is underspecified and not tested against alternative PEFT methods.** The paper concludes that VPT's "unique manner" of preserving original features and adding parameters is "pivotal," but this claim is never tested against other parameter-efficient approaches (e.g., LoRA, adapters, bias tuning) that also freeze the backbone while adding small trainable modules. Without these baselines, the paper cannot distinguish between "VPT's specific prompting mechanism matters" and "any method that freezes most parameters works well within similar data regimes." This gap limits the specificity of the paper's core explanatory claim.

### Minor

- **The abstract and introduction frame VPT as having "superior performance" overall, but on Specialized tasks FT achieves a higher mean accuracy (83.48 vs. 82.65, Table 1).** The results are more mixed than the title and abstract suggest, and this over-framing weakens the paper's otherwise balanced empirical presentation.

- **The use of FID between real datasets as a proxy for transfer-learning difficulty is unvalidated.** FID is computed on Inception-v3 features trained on ImageNet-21k (the same pretraining distribution), so it conflates "this dataset looks different from ImageNet in pixel statistics" with "Inception features don't represent this domain well." The paper acknowledges the non-standard usage in a footnote but does not validate that FID correlates with any meaningful measure of transfer difficulty. This does not invalidate the analysis, but it weakens the confidence one can place in the FID-based observations.

- **GradCAM visualizations (§5.4, Figure 6) are illustrative rather than evidential.** A few selected examples where VPT succeeds and FT fails do not constitute evidence for the claimed mechanism. The paper does not over-claim here, but the visualizations add little rigor.

### Trivial

- None.

## Nice-to-Haves

- Compare VPT against other parameter-efficient methods (LoRA, adapters) to sharpen the "why" analysis.
- Report standard deviations in all main tables, especially for borderline cases.
- Validate FID against a standard measure of distribution shift (e.g., linear probe accuracy drop) if it is to be used as a key dimension in the framework.
- Consider presenting the one-shot results with explicit caveats about variance given the acknowledged randomness.

## Removed Points

These points were identified by reviewers but removed because they do not survive verification against the paper or violate filtering rules:

1. *Criticism about related work overclaiming that other PEFT methods "generally cannot reach competitive results to full finetuning"* — This claim is cited to Jia et al. 2022 and is a restatement of prior work, not an unsubstantiated claim by this paper. Removed as factually grounded in a citation.

2. *Criticism about no statistical test for the quadrant framework* — The paper is an empirical study, not a formal hypothesis-testing paper. Demanding a statistical test for a qualitative observation is scope creep. Removed per soft rule about field-appropriate standards.

3. *Criticism that GradCAM examples are "cherry-picked"* — The paper presents these as illustrative visualizations, not as primary evidence. Removed per instruction to not treat qualitative illustrations as claimed evidence.

4. *Claim that "task disparity is treated as binary" is a weakness* — This is an accurate description of the paper's operationalization. The real concern (inadequate granularity) is already captured in the first Major weakness above.

## Novel Insights

The interaction between the two reviewer inputs yields a novel observation: the paper's strongest contribution is actually its *negative* findings (MIXED and FT-then-PT ruling out optimization-based explanations; overfitting analysis ruling out a simple parameter-count story), while the positive *when* framework is the weakest link. This is somewhat inverted relative to the paper's own presentation emphasis. The paper would be stronger if it foregrounded the well-designed causal ablations and positioned the quadrant framework as a suggestive but preliminary qualitative observation rather than a core contribution.

## Suggestions

1. Report standard deviations alongside means in all main tables. This is the single highest-impact change — it directly addresses the verifiability of the headline win/loss claim and costs minimal space.
2. Either (a) validate the FID-based quadrant analysis with a correlated measure of transfer difficulty and a formal decision rule, or (b) reframe it as a qualitative observation rather than a central contribution.
3. Add at least one other PEFT baseline (e.g., LoRA) to the "why" analysis to test whether the claimed mechanism is specific to VPT or general to parameter-efficient approaches.
4. Adjust the abstract and introduction to more accurately reflect the mixed results on Specialized tasks.

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>