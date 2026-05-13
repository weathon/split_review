Now I have a thorough understanding of the paper. Let me compose the final review.

## Summary

The paper introduces Gramtector, a framework for detecting AI-generated text using sparse PoS n-gram patterns selected via L1-regularized logistic regression. The key idea is that 20 interpretable grammatical patterns can serve both as features for an automated classifier and as guidance for human decision-makers in a human-in-the-loop setting. A human trial evaluates three levels of AI assistance, finding that engaged participants using the patterns improve detection accuracy compared to an unassisted baseline.

## Strengths

- **Superior adversarial robustness compared to alternative interpretable features**: Table 2 demonstrates that while vocabulary- and stylometric-based detectors see their TPR collapse from 98% to 4% under paraphrasing, Gramtector's performance remains essentially unchanged. This is a concrete, well-demonstrated advantage over alternative interpretable approaches.

- **Counterintuitive finding on assistance levels**: The human trial reveals that Level 1 (requiring active pattern comprehension) yields higher accuracy among engaged participants than Level 3 (color-coded red/blue highlights), suggesting over-reliance on simplified AI guidance degrades human judgment (Table 4, Section 5.2). This is a genuinely interesting result about the downsides of excessive automation in human-AI collaboration.

- **Clear and practically motivated research question**: The dual goal of accuracy and interpretability for AI text detection is well-motivated, and the paper correctly identifies that existing methods largely fail on interpretability.

## Weaknesses

### Fatal

None.

### Major

- **The headline "43% → 86%" claim is misleadingly presented**: The abstract states an improvement "from 43% to 86%" without specifying that 86% is conditional on a self-selected subgroup—participants classified post-hoc as "engaged and employing the provided grammatical patterns" (Figure 4b). The introduction similarly states "40% to around 86%." Only in the body does the paper clarify this conditioning. Table 3 reports overall participant accuracy, which (per the paper's own data) shows more modest improvement. Comparing a motivated, self-selected subgroup against the entire baseline population is not a valid experimental comparison, as the engaged subgroup may simply consist of more careful annotators regardless of the patterns. The paper's central quantitative claim needs to be stated honestly in the abstract and conclusions, with the subgroup caveat made prominent.

- **No control condition isolates the effect of Gramtector's patterns**: The human trial has no condition providing participants with non-diagnostic or random patterns/guidance. Without this, it is impossible to determine whether improvement comes from Gramtector's specific grammatical patterns or from any structured framing that encourages more careful reading. The finding that the least-assisted condition (Level 1) gives the best performance among engaged participants actually suggests the improvement may stem from engagement with the text rather than from the patterns' diagnostic value. This is a fundamental gap in causal attribution.

- **Below-chance baseline (40–43%) on a balanced binary task is unexplained and inflates apparent gains**: The baseline accuracy of 40–43% on a 50/50 task is below chance. The paper acknowledges this ("worse than random guessing") but never investigates why participants systematically err. Any intervention that encourages more careful reading could produce gains from this floor, making it difficult to isolate the specific contribution of the patterns. The size of the claimed improvement is partially an artifact of the anomalous baseline.

### Minor

- **Engagement classification is post-hoc and subjective**: The paper classifies participants as "unengaged," "engaged," or "engaged with patterns" after the fact, and the paper's headline result depends on this classification (Section 5.2, line 121). The classification criteria are not rigorously defined, and sample sizes for the "engaged with patterns" subgroup are not reported, making reliability difficult to assess.

- **Feature stability from 100K candidates to 20 is not analyzed**: Selecting 20 features out of 100,004 PoS n-grams via L1 regularization raises overfitting concerns, especially given near-perfect AUROC. The paper does not analyze whether the same features are consistently selected across cross-validation folds or data perturbations—if the 20 features are unstable, the interpretability claim (that specific patterns are informative) is undermined.

- **Adversarial evaluation tests only generic prompting, not pattern-aware attacks**: If an adversary knows the 20 detected patterns, they could prompt the LLM to avoid them. The paper's adversarial evaluation (Section 5.1, Table 2) uses generic "write more human-like" instructions rather than pattern-targeted attacks. The claim that "grammatical sentence structure is an intrinsic characteristic... challenging to alter" is asserted but not tested against the most natural threat model.

- **Same-domain AUROC near 1.0 is not distinctive**: Near-perfect AUROC for same-domain, same-model detection is expected for any reasonable classifier given the distribution shift between human and LLM text. The paper does not sufficiently contextualize this, and cross-model generalization is tested on only one dataset per model (arXiv abstracts).

### Trivial

- None.

## Nice-to-Haves

- Report human trial sample sizes and confidence intervals for subgroup analyses, which would strengthen reliability claims without changing the design.
- Show the 20 selected PoS patterns and their coefficients with qualitative analysis of why they distinguish human from AI text; this would substantiate the "interpretability" claim beyond feature importance scores.
- Conduct a follow-up human trial with a control condition (random/shuffled patterns) and matched comparison groups to establish valid causal estimates of the patterns' contribution.

## Removed Points

*These points are flagged to be removed, treat them with slight caution—they may contain legitimate observations but were deemed not sufficiently grounded or too minor for the main review.*

- **Strength claim "Large, empirically validated improvement from 43% to 86%"**: Removed because this conflates the overall baseline with a conditional subgroup result, which is precisely the overclaim identified as a major weakness above. Keeping this as a strength would contradict the verified weakness about misleading comparison.

- **Strength claim "Competitive performance with non-interpretable baselines"**: Near-perfect same-domain AUROC is expected for any classifier given distribution shift, so beating RoBERTa on specific datasets is not strong evidence of a genuine accuracy–interpretability trade-off being overcome.

- **Critic point about "the formalization overclaims—the explanations are just coefficient signs"**: The paper is straightforward about using logistic regression coefficients and PoS n-grams. The formalization naturally abstracts the implementation. This is a mild presentation mismatch, not a substantive flaw.

- **Critic point requesting reproducibility details (hyperparameters, training logs, etc.)**: Per policy, these are trivial implementation details not required in a submission.

- **Critic point about missing related works**: Per policy, we do not flag missing related works.

- **Critic point about "the 86% figure comes from Figure 4b and Table 4 showing self-selected subgroup"**: This observation is valid and incorporated into the major weakness above about the headline claim, but the specific statistical detail about Figure 4b is partially unverifiable without the actual data from the tables (which are rendered as images). The core concern is captured in the major weakness.

## Novel Insights

The most novel empirical finding is the counterintuitive "less is more" result in human-AI collaboration: providing humans with interpretable patterns they must actively apply (Level 1) outperforms providing color-coded automated decisions (Level 3). This challenges the common assumption that more AI assistance is better, and suggests that forcing human engagement with diagnostic features may be more effective than simplifying the interface. However, without a control condition, it remains unclear whether this benefit comes from the patterns' diagnostic content or simply from the cognitive engagement they demand.

## Suggestions

- Re-represent the headline result honestly: report the full-population improvement alongside any subgroup results, and make the conditioning on engagement prominent in the abstract and conclusion.
- Design and run a follow-up human trial with a control condition (random or shuffled patterns) to establish whether the improvement is attributable to Gramtector's specific patterns or to engagement effects.
- Investigate and explain the below-chance baseline: is there a systematic bias in how participants classify certain text types?

## Score and Decision

The paper makes a reasonable contribution in proposing interpretable PoS-based detection and demonstrating adversarial robustness, but the central human-trial claim is undermined by three compounding methodological issues: a misleading headline comparison (conditional subgroup vs. full-population baseline), no control condition to isolate the patterns' contribution, and an unexplained below-chance baseline that inflates apparent gains. The automated detection results are solid but not surprising (near-perfect same-domain detection is expected). The adversarial robustness finding is the strongest element. These methodological weaknesses in the human trial—where the paper stakes its interpretability claims—are significant but not fatal, as the framework and robustness results hold independent value.

**Originality**: Moderate—PoS features for authorship attribution have precedent, but the human-in-the-loop framing and adversarial comparison add novelty.

**Importance of research question**: High—interpretable AI detection is a pressing problem.

**Claims well supported**: Partially—automated detection claims are well supported; human-trial claims are overclaimed relative to the evidence.

**Soundness of experiments**: The automated experiments are sound; the human trial has significant methodological gaps.

**Clarity**: Generally clear, though the headline result presentation is misleading.

**Value to community**: Moderate—contributes a useful framework and robustness comparison, but the human-trial contribution is weaker than claimed.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>