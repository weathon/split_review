## Summary
This paper proposes *MetaMath*, a family of fine-tuned LLaMA-2 models for mathematical reasoning, together with a data-augmentation method called *question bootstrapping* that generates diverse training data from existing math problems. The bootstrapping operates along two reasoning directions: forward (original questions and LLM-rephrased variants) and backward (Self-Verification and FOBAR questions where a masked variable must be inferred given the answer). Combined with answer augmentation (rejection sampling), this produces the MetaMathQA dataset (395K samples from GSM8K and MATH). MetaMath-7B achieves 66.5% on GSM8K and 19.8% on MATH, surpassing prior open-source 7B models by 11.6 and 9.1 points respectively, and MetaMath-70B reaches 82.3% on GSM8K, slightly exceeding GPT-3.5-Turbo.

---

## Strengths
- **Large and consistent accuracy gains across three model scales.** Table 1 shows MetaMath-7B outperforms WizardMath-7B by 11.6 points on GSM8K (66.5% vs. 54.9%) and 9.1 points on MATH (19.8% vs. 10.7%). The improvements hold at 13B and 70B scales, with MetaMath-70B reaching 82.3% on GSM8K — exceeding GPT-3.5-Turbo (80.8%). These are well-documented in the main results table.

- **First use of backward reasoning questions as training data (not just inference verification).** Section 3.3 explicitly distinguishes this from prior work (Weng et al. 2023, Jiang et al. 2023) that applied Self-Verification and FOBAR only at inference time. The paper repurposes them to generate fine-tuning samples, which is a clear methodological shift validated by the ablations.

- **Systematic ablation isolating each bootstrapping component.** Table 2 shows that AnsAug-only achieves 59.6% on GSM8K, adding rephrasing reaches 60.6%, and adding all four components (AnsAug+Rephrasing+SV+FOBAR) reaches 64.4%. The same pattern holds for cross-domain transfer (GSM8K→MATH). This cleanly validates that each augmentation type contributes non-trivially.

- **Empirical link between question diversity and accuracy.** Section 4.4 reports that adding 20K samples from rephrasing, SV, and FOBAR yields diversity gains of 0.02, 0.13, and 0.14 respectively, corresponding to accuracy gains of 0.4%, 2.3%, and 2.6%, with a Pearson correlation of 0.972. This directly connects the augmentation strategy to performance improvement.

- **Creation of a backward-reasoning test set (GSM8K-Backward, 1,270 questions) and demonstration of targeted improvement.** Section 4.5 shows that existing models (SFT, RFT, WizardMath) suffer large accuracy drops on backward questions relative to forward ones, while MetaMath maintains much smaller degradation — showing the method addresses a concrete reasoning weakness.

- **Counterintuitive finding that more data is not always better.** Section 4.7 shows that adding the RFT dataset (47K samples) to MetaMathQA actually degrades performance across multiple dataset sizes. This provides direct evidence that augmentation design (not mere volume) drives the gains.

---

## Weaknesses
### Fatal

None.

### Major

None. The paper's core claims are well-supported by the experimental evidence.

### Minor

- **The dependence on GPT-3.5-Turbo for all data generation is not analyzed.** Lines 366–368 state that GPT-3.5-Turbo is used for both question bootstrapping and answer augmentation across all four data types. The paper does not conduct a control experiment using an open-source generator to assess how much of the gain comes from the augmentation method vs. the teacher model's quality. The release of the dataset and models largely mitigates this for practical use, but it limits understanding of the method's generality.

- **No controlled experiment separating reasoning-direction diversity from data volume.** The ablation (Table 2) shows that adding SV+FOBAR to AnsAug+Rephrasing improves accuracy by ~3.8% on GSM8K. However, because this also increases total training samples, the specific contribution of backward reasoning *per se* is not isolated from simply having more diverse forward data of matched quantity. A comparison adding an equivalent number of additional rephrased (forward) questions would strengthen the claim that backward reasoning is uniquely beneficial. The paper's correlational evidence (Pearson 0.972) is suggestive but not causal.

- **No confidence intervals or significance tests.** All results in Tables 1–2 are reported as single accuracy values. Given the multiple comparisons across model sizes and ablations, variance estimates (even a single additional run or bootstrap intervals) would increase confidence that the reported improvements are robust.

- **The "more data is not always better" finding is tested with only one external dataset (RFT).** Section 4.7 is clean within its scope, but generalizing the claim would require testing with additional augmented datasets (e.g., WizardMath's generated data) to rule out dataset-specific interactions.

- **Circularity in rephrasing quality evaluation.** The same model (GPT-3.5-Turbo) both generates rephrased questions and evaluates their correctness via Complexity-based CoT (line 147). The reported accuracy of 76.30% (vs. 80.74% on original questions) is reassuring, but a human-verified subset would provide stronger evidence that rephrasing does not introduce systematic errors.

### Trivial

- **Hyperparameter sampling details are incomplete.** The paper defines symbolic parameters \(K_{\text{AnsAug}}, K_{\text{rephrase}}, K_{\text{SV}}, K_{\text{FOBAR}}\) and gives final dataset sizes (Table, lines 262–265), but does not report the raw sampling counts before answer-based filtering. This is a minor reproducibility gap.

---

## Suggestions
- In the ablation study, add a condition that matches the total number of additional forward-only (rephrased) tokens to the SV+FOBAR quantity. This would directly test whether the backward-reasoning benefit is driven by the reasoning direction or simply by having more diverse data.
- Report at least one additional run or a bootstrapped confidence interval for the main results (Table 1) to address reproducibility concerns.
- Detail the raw sampling counts \(K\) for each augmentation type (before answer filtering) to improve reproducibility.
- Consider validating a small sample of rephrased questions with human annotators to strengthen the quality claim.

---

## Score and Decision

This is a strong, well-executed paper with a simple but effective methodological contribution, comprehensive experiments across three model scales, clean ablations, and several auxiliary analyses that support the main narrative. The weaknesses are real but minor — none threaten the core claims, and most are either mitigated by the released artifacts or suggest directions for future work rather than flaws in the current paper.

MY FINAL SCORE: <score>8.0</score>
MY FINAL DECISION: <decision>Accept</decision>

## Questions


## Decision
Accept
