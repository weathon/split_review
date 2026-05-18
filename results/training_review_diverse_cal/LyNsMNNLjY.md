Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

---

## Summary

This paper formalizes the problem of LLM routing (selecting the best model for a new task) by repurposing per-sample benchmark evaluation data. The key idea is to train a binary correctness predictor per LLM (using kNN on sentence embeddings) that estimates whether the LLM will be correct on an input. The paper proposes three routing scores (S₁, S₂, S₃), where S₃ incorporates an OOD confidence model that accounts for the accuracy of the correctness predictor on the new task. Experiments on HELM (29 datasets, 18 models) and MixInstruct (11 models) show that S₃ can match or slightly exceed the best model on average (BMA) while selecting smaller models on average, and that a small number of in-distribution samples further improves routing quality.

## Strengths

1. **Novel problem formulation repurposing benchmark byproducts.** The paper formalizes LLM routing as learning per-LLM binary correctness predictors from per-sample benchmark evaluations (Section 3, eq. 1), avoiding the need to generate outputs from every candidate LLM at test time. This contrasts with prior routing work (PairRanker, SimCLS, FrugalGPT) that requires generations from all models per input.

2. **OOD-aware score S₃ with a principled meta-learning connection.** The proposed score S₃ (eq. 8) explicitly models the out-of-distribution accuracy of correctness predictors via a task-distance regressor. The theoretical framing (Lemma 1, eq. 9–13) connects adaptive shrinkage to meta-learning, going beyond purely empirical prior routing work.

3. **Empirical gains over the best single model while reducing average model size.** On HELM (Table 1), S₃ achieves 0.694 average accuracy and 0.898 ratio-to-best, outperforming the best model on average (BMA: 0.688/0.884) while selecting smaller models on average (49.8B vs. 70B parameters). This demonstrates that routing can simultaneously improve performance and efficiency.

4. **Practical OOD gap analysis with error bars.** The experiment moving small amounts of in-distribution data (Figure 2) quantifies how even 5% of labeled samples from the new task substantially improve routing, with variance estimates from repeated subsampling. This provides actionable insight for practitioners.

5. **Dramatic efficiency advantage on MixInstruct.** In the per-instance routing setting (Table 2), the proposed method achieves the best BERTScore (74.75) among all methods with only 2 model calls per instance, compared to N=11 calls for all baselines. This highlights a significant inference-time efficiency advantage.

## Weaknesses

### Fatal
None.

### Major

1. **No uncertainty quantification in the primary HELM results (Table 1).** Table 1 reports point estimates over 29 leave-one-task-out experiments without any standard deviation, confidence interval, or statistical test. Since the core claim—that the routing framework improves over BMA—rests on a small margin (S₃ accuracy 0.694 vs. BMA 0.688, a difference of 0.006), the absence of variance estimates makes it impossible to assess whether this improvement is reliable or within noise. The later experiments (Figure 2, Figure 4) include error bars from repeated subsampling, but the central result in Table 1 does not. This is the most significant weakness: a paired bootstrap test or jackknife variance estimate across the 29 hold-one-out folds would immediately clarify the practical significance of the claimed gains.

### Minor

1. **OOD confidence model's homoscedasticity assumption is unvalidated.** The model assumes that $p(d',m)$—the probability that the binary predictor $\bar{g}_m$ is correct on a new task $d'$—does not depend on the input $x$ after conditioning on the task. The paper acknowledges this is approximate (line 104), but does not validate it empirically. The estimator's MAE of 0.116 is reported without specifying over which tasks/splits it is computed, and there is no analysis of sensitivity to the kernel bandwidth or distance metric. That said, this is not fatal: S₃ with *true* $p$ (bypassing the estimation) shows even stronger results (0.735), indicating the score itself is sound and the estimation gap is a separate engineering challenge.

2. **S₃ selection threshold $\eta=0.6$ is used without justification or sensitivity analysis.** The rule in eq. (15) falls back to BMA when the probability that the S₃-chosen model beats BMA is below $\eta$. This design choice directly affects whether S₃ diverges from BMA, yet no analysis of how varying $\eta$ changes routing performance is provided. A sensitivity plot would demonstrate robustness or reveal artifacts.

3. **Choice of $k=5$ for kNN is fixed without rationale or sensitivity analysis.** While kNN is a reasonable choice for a simple non-parametric predictor, $k$ is known to affect OOD generalization. A brief sensitivity analysis or even a rationale for the chosen value would strengthen reproducibility, though this does not threaten the core claims.

4. **Minor overclaim in the abstract.** The abstract states the approach "consistently improve[s] performance upon using any single model for all tasks." In Table 1, S₁ (0.662) and S₂ (0.676) both underperform BMA (0.688); only S₃ (0.694) outperforms it. The claim is directionally true for S₃ but not for all variants, so "consistently" is slightly overstated.

### Trivial

- None beyond the minor points above. The paper is clearly written and well-structured.

## Nice-to-Haves

- **Cost analysis beyond parameter count.** The paper motivates routing as a way to reduce inference cost but only reports average parameter count. Reporting estimated FLOPs or actual latency/throughput comparisons would make the cost argument more concrete.
- **Validate the $p(d',m)$ estimator with a scatter plot** of estimated vs. true accuracy across held-out tasks and models, showing calibration. This would directly reveal whether the estimation errors are systematic.
- **Clarify the embedding model.** The paper uses "a sentence transformer" but does not specify which model. Mentioning the specific model (even in an appendix) would aid reproducibility.

## Removed Points

These points were flagged by reviewers but removed for the reasons stated below. They are included here for completeness but should not affect the assessment.

- **Criticism about missing proof for Lemma 1 in the main text**: Removed per instructions — proofs deferred to appendices are standard practice and the parser strips appendix content. They exist in the original submission.
- **Criticism about MixInstruct binarization not being specified**: Removed per instructions — the paper references appendices for experimental details, which are stripped by the parser.
- **Criticism about the improvement being too small to matter**: Not removed as a separate point, but integrated into Major Weakness 1 (lack of error bars makes the small margin uninterpretable). As an isolated criticism it would be an evaluation of magnitude, not a methodological flaw.
- **Generic strength about "addressing an important problem"** (from Strength Finder): Removed for being generic and lacking specific content tied to the paper.

## Novel Insights

The reviews surface a tension between the paper's clean theoretical framing (meta-learning connection, Lemma 1, adaptive shrinkage) and the fragility of its empirical support. The theoretical motivation for S₃ is arguably the paper's most novel intellectual contribution, yet the empirical validation relies on a single unadorned table without variance estimates. This gap between theory and evidence is the review's key takeaway: the idea is sound and well-motivated, but the experiments, as presented, do not yet meet the bar for establishing reliable practical advantage. The MixInstruct results (Table 2) are actually stronger evidence for the approach than the HELM results, which is somewhat obscured by the paper's focus on HELM as the primary experiment.

## Suggestions

1. **Add variance estimates to Table 1.** The leave-one-task-out design naturally supports jackknife or bootstrap standard errors. Report these for accuracy, ratio-to-best, and Spearman correlation. Even reporting the range or interquartile range across the 29 folds would help.
2. **Add a sensitivity analysis for $\eta$.** Show routing accuracy as a function of $\eta$ (e.g., from 0.5 to 0.9) to demonstrate whether the method is robust to this choice.
3. **Provide a direct validation of the $p(d',m)$ estimator.** A scatter plot of estimated vs. true $p$ across held-out tasks (colored by model) would reveal systematic biases and calibrate reader confidence in S₃.
4. **Tone down the abstract's "consistently improve" claim** or qualify it to refer specifically to S₃, not all scores.

## Score and Decision

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>