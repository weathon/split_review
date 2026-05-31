Now I have all the information needed. Let me write the consolidated review.

---

## Summary

This paper addresses a well-motivated problem: enabling fine-grained bar-level control (chord and rhythm intensity) in pretrained autoregressive symbolic music models. The authors identify that straightforward fine-tuning with new control tokens (BFT) produces poor adherence to bar-level prompts, and propose two strategies to remedy this: (1) a pre-adaptation (PA) auxiliary task that forces the model to classify whether bar-level attributes match the music, and (2) a counterfactual loss (CF) that penalizes the model when changing a bar-level attribute does not reduce the likelihood of that bar's music tokens. On the POP909 dataset, the combined method (ControlMuse) improves chord accuracy by 13.06% absolute over BFT while preserving subjective musical quality.

## Strengths

- **13.06% absolute chord accuracy improvement over the BFT baseline is well-supported.** Table 1 shows 78.33% vs. 65.27%, and this improvement is the paper's core empirical claim. The ablation in Table 3 confirms that both PA and CF individually contribute (PA: +6.95%, CF: +5.88%), and the combination yields the best result. This is clean, internally consistent evidence for the paper's central thesis.

- **The ablation study (Table 3) is the strongest part of the evaluation.** It systematically isolates the contribution of each component, showing that PA and CF each improve both chord and rhythm intensity accuracy, and that their combination further boosts performance. This gives clear evidence that both strategies are individually effective and complementary.

- **Figure 5 systematically characterizes the effect of inference-time sampling (K).** The plot shows chord accuracy improving with K for both BFT and ControlMuse, with the gap widening at higher K. This provides useful insight into how the inference policy interacts with the method.

- **Subjective evaluation confirms that improved control does not degrade musical quality.** The survey (16 piano teachers) shows 43.75% preferring ControlMuse vs. 40.63% preferring MuseCoco, with 15.63% finding them similar. While not rigorous enough alone, this reasonable sanity check supports the claim that control gains are not achieved at the expense of musicality.

## Weaknesses

### Fatal
None.

### Major

- **The comparison against FIGARO and Polyffusion (Table 2) lacks essential experimental context.** The paper states that these models "utilize chord or rhythm intensity as fine-grained control signals" but never specifies whether they were trained/fine-tuned on the POP909 dataset, with the same train/validation/test splits, comparable parameter budgets, or the same evaluation pipeline. If used off-the-shelf, the comparison is uninformative because the models were not designed or trained for this specific bar-level control setup. If they *were* adapted, the procedure must be described. As presented, the reader cannot interpret Table 2, and the claim that ControlMuse "outperforms existing conditional generative models" is unsupported by the information provided. This comparison should either be removed or substantially revised with full experimental details.

### Minor

- **Asymmetric evaluation of chord accuracy (K=15) vs. rhythm intensity accuracy (K=1) is disclosed but not justified.** The paper consistently reports chord accuracy with K=15 and rhythm intensity accuracy with K=1 (Tables 1 and 3). While the asymmetry is stated, no rationale is provided. Since Figure 5 shows that chord accuracy improves substantially with K (e.g., from ~60% at K=1 to ~78% at K=15 for ControlMuse), the reader cannot directly compare the two metrics, and the ablation results for rhythmic intensity are measured under a less demanding inference regime. The core improvement over BFT is still valid, but the paper would be stronger by reporting both metrics under both K=1 and K=15, or at minimum providing a justification for the asymmetry.

- **No measures of statistical significance or run-to-run variability.** All objective results are reported as single numbers with no confidence intervals, standard deviations, or multiple seeds. Given the dataset size (~2700 clips, 909 songs split 8:1:1) and the stochasticity in training (random initialization of control prompts, random modifications in PA, LoRA fine-tuning), the reliability of the reported improvements is unknown. While single-run evaluation is common in this area, adding at least a bootstrap or 3-run variance would significantly strengthen the evidence.

- **The chord extraction algorithm used to compute the primary objective metric is not specified.** The paper mentions "existing algorithms [3]" to extract chords from note distributions per bar, but in the extracted text the specific algorithm is never cited or described. Since chord accuracy is the headline objective metric, reproducibility depends on knowing exactly how chords are determined from the symbolic output. A precise citation or a brief description of the chord extraction rule is needed.

- **Full fine-tuning (without LoRA) is not explored as a baseline.** The paper uses LoRA (rank 8) for parameter-efficient fine-tuning but never evaluates whether full fine-tuning would yield different results. Given the small fine-tuning dataset (POP909) relative to the foundation model, LoRA is reasonable, but a full fine-tuning baseline would rule out the concern that LoRA's limited capacity contributes to BFT's poor performance.

- **The subjective evaluation (16 raters) is a useful sanity check but not statistically reliable.** With only 16 raters and three response options, the 43.75% vs. 40.63% split carries little statistical weight. The paper appropriately does not overclaim here, but a larger study or an objective fluency metric would be stronger.

### Trivial
- **Table 5 (complexity analysis) reports inference time for MuseCoco and ControlMuse but omits the BFT baseline.** The overhead of the PA and CF strategies relative to the straightforward BFT approach cannot be isolated. A timing row for BFT would complete the picture.

## Nice-to-Haves

- Analyze the counterfactual loss condition more carefully: report how often consecutive bars share the same attribute (making $\overline{X_i} = X_{i-1}$ uninformative) and provide a sensitivity analysis for the margin $\eta$.
- Show loss curves and controllability metrics over training steps for BFT vs. ControlMuse to empirically demonstrate the hypothesized divergence between loss minimization and control adherence.
- Report chord accuracy at K=1 in the ablation study (Table 3) to isolate the method's inherent improvement from the inference procedure's contribution.
- Report the average number of resamples per bar during inference to clarify the effective cost of the sampling policy.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **Criticism about position embeddings for global tokens** — REMOVED. The paper clearly explains that global tokens describe the entire piece and do not carry bar-level positional identity. This is a reasonable design choice, not a weakness.
2. **"First study" claim concern** — REMOVED. The reviewer speculates about prior work without evidence. The paper's related work section adequately surveys the landscape. This is not a verified weakness.
3. **Criticism that PA task specification is under-specified (where projection heads are applied)** — REMOVED. The paper states "linear projection heads that are trained on the output embeddings of the bar-level control prompts" and Figure 3 illustrates the setup. The description is sufficient for reproducibility.
4. **Strength about outperforming FIGARO/Polyffusion** — REMOVED. This strength conflicts with the verified weakness that the comparison lacks essential experimental context, making the claimed outperformance uninterpretable.
5. **Generic strength about addressing an important problem** — REMOVED. Generic; not concrete or specific to this paper's evidence.

## Novel Insights

None beyond the paper's own contributions. The key insight — that naive bar-level fine-tuning with new control tokens fails because the model ignores them, and that an auxiliary classification task plus counterfactual loss can rectify this — is the paper's own contribution, not a novel synthesis from the reviews.

## Suggestions

1. **Revise or remove the FIGARO/Polyffusion comparison.** Either provide full experimental details (training data, adaptation method, evaluation pipeline) so the comparison is interpretable, or drop it entirely — the paper's core claims do not depend on it.
2. **Report both chord and rhythm intensity accuracy under consistent inference conditions** (e.g., K=1 and K=15 for both), or provide a clear justification for the asymmetry.
3. **Add measures of variability** — at minimum bootstrap confidence intervals or results across 3 random seeds.
4. **Cite and briefly describe the chord extraction algorithm** used to compute the primary metric.
5. **Add a full fine-tuning baseline** to confirm that the BFT failure is not caused by LoRA's capacity constraint.

## Score and Decision

The paper makes a real and practical contribution: the PA and CF strategies clearly improve bar-level control over the BFT baseline, and the ablation study is clean and internally consistent. The core claim is supported. However, the evaluation has meaningful gaps — most critically, an uninterpretable comparison to FIGARO/Polyffusion, an asymmetric evaluation protocol, and absent statistical rigor. These are fixable, and should not prevent acceptance given the solid evidence for the main contribution.

**Score:** 6.5

**Decision:** Accept

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>