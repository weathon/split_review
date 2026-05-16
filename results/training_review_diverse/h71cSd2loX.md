Now I have a thorough understanding of the paper. Let me construct the final consolidated review.

## Final Review

## Summary

This paper derives two DPO variants — DPO-RK and DPO-D — that replace the Bradley-Terry preference model with the Rao-Kupper and Davidson models, respectively, enabling the explicit modeling of tied preference judgments. The key theoretical contribution is that these models assign probability to ties alongside wins/losses, and the resulting loss functions naturally drive reward margins toward zero on tied pairs. Experiments on NMT (WMT21 ZH-EN, IWSLT FR-EN) and summarization (TL;DR) show that DPO-RK and DPO-D incorporate artificially constructed tied pairs without the task performance degradation observed when adding the same pairs to standard DPO, and produce better-calibrated reward margins and improved classification of ties versus clear preferences.

## Strengths

1. **Principled and theoretically grounded extension.** The paper derives DPO-RK and DPO-D by substituting the Bradley-Terry model with Rao-Kupper and Davidson models — well-established statistical frameworks for handling ties. The resulting loss functions (Eqs. 10–11) and gradient analysis (Eqs. 12–15) clearly show how ties receive opposing gradient signals that drive the reward margin toward zero, a mechanism absent in standard DPO. The paper correctly notes (line 73) that the reward margin decomposition from DPO carries over without additional assumptions, making the integration clean and non-trivial.

2. **Clear empirical demonstration that DPO-RK/DPO-D avoid degradation from ties.** In all three experimental settings (Figures 3a–c), DPO-RK(CP+TP) and DPO-D(CP+TP) reach task performance levels comparable to DPO(CP), while DPO(CP+TP) — standard DPO trained on the same data including ties — consistently underperforms. This is the paper's central empirical claim and it is well-supported across tasks and metrics (BLEURT for NMT, PairRM win-rate for summarization).

3. **Improved calibration and regularization from modeling ties.** The paper shows that including ties in DPO-RK/DPO-D shifts the performance-vs-KL Pareto frontier leftward (same performance at lower KL), and Table 3 demonstrates that reward margins on tied pairs have near-zero mean *and* low variance for DPO-RK/DPO-D, whereas DPO(CP) produces extreme margins with very high standard deviation (e.g., std ≈ 174 on CPs at β=0.5). This is a concrete, measurable benefit of the proposed approach.

4. **Improved classification accuracy for ties.** Using the trained policy as a classifier (Section 3.3.2), DPO-RK and DPO-D achieve balanced accuracy on both clear preference and tied pairs (Table 2: 73.1% overall for DPO-RK at β=0.1, with CP acc 74.5% and TP acc 71.7%), whereas DPO(CP) heavily misclassifies ties (TP acc as low as 13.3%). This demonstrates that the models genuinely learn to discriminate wins from ties.

## Weaknesses

### Fatal
None.

### Major

1. **The central practical motivation is not directly tested.** The paper motivates its work on the grounds that real human-annotated ties are "wastefully discarded" (lines 15–18), yet every experiment uses *artificially constructed* ties: in NMT, ties are the pair with minimum BLEURT difference; in summarization, ties are the pair with minimum reward margin under a DPO model. Neither construction necessarily corresponds to how ties arise in real human annotation. The NMT construction (minimum BLEURT difference) is a defensible proxy for "similar quality," but it does not capture genuine human uncertainty or the "no preference" judgments the paper cites from Llama 3 and Qwen2. The summarization construction (DPO-selected) has an additional circularity issue (see Minor point 2). Without *any* experiment using actual human-annotated ties, the paper's evidence supports the claim that the methods work on *these particular operationalizations* of ties, not that they solve the real-world problem that motivates the work. This is the most significant gap in the paper.

### Minor

2. **Summarization tie construction has a selection confound.** In the TL;DR experiments, tied pairs are selected as the pair with minimal reward margin under a preliminary DPO model (lines 231–232). Since DPO-RK and DPO-D are designed precisely to handle pairs with small reward margins, this selection procedure favors the proposed methods. The NMT results (which use an independent BLEURT-based construction) are free of this confound and show the same qualitative pattern, which mitigates this concern. However, the paper does not acknowledge this confound or justify why the DPO-based selection is appropriate.

3. **No sensitivity analysis for the tie-strength parameter ν.** The parameters ν_RK=3 and ν_D=1 are set based on the assumption that equally-matched items tie with probability 1/2 (line 145). While this is a principled default, ν directly controls the trade-off between win and tie probability in the objective, and the paper provides no sensitivity analysis (e.g., varying ν on a held-out validation set). Without such analysis, it is unclear whether the observed benefits are robust across ν values or whether the results would degrade under different plausible settings.

4. **No statistical uncertainty estimates.** The paper reports task performance vs. KL curves and classification accuracies without variance bars, confidence intervals, or results from multiple random seeds. Given that DPO training can be sensitive to stochastic factors, this omission weakens the reliability assessment of the results. This is standard practice in the DPO literature rather than a fatal flaw, but it is worth noting.

5. **Evaluation metric for summarization could be clarified.** The text (line 230) states "Previous works use GPT-4 to compute the win-rate," while the figure caption (Figure 2, line 257) reads "TL;DR PairRM Win-Rate." This leaves it ambiguous whether the paper uses PairRM or GPT-4 as the evaluator, and if PairRM, why the weaker evaluator was chosen. The paper should explicitly state which evaluator is used and justify the choice.

### Trivial

6. **Minor normalization verification.** The paper states (line 98) that the Rao-Kupper and Davidson probabilities sum to one, addressing a concern the reviewer raised. No further issue.

## Nice-to-Haves

- **Experimental comparison to ODPO with ties.** The paper notes (lines 427–428) that ODPO's offset parameter plays a role similar to Rao-Kupper's sensitivity threshold. An experimental comparison of DPO-RK/DPO-D against ODPO trained with ties treated as "no preference" would sharpen the evaluation and better position the contribution.
- **Varying the proportion of ties.** The paper uses fixed tie proportions (50% in NMT, ~15% in summarization). Varying this proportion would reveal when the proposed methods start to degrade and characterize their robustness.
- **A small human-annotation validation.** Even a modest human-annotated tie experiment (e.g., a few hundred pairs for one task) would significantly strengthen the paper's claim that the methods handle realistic ties.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Classification accuracy is partly self-consistency"** (Harsh Critic point 5): The reviewer acknowledges the paper provides cross-condition comparisons. The paper's Table 2 shows DPO-RK(CP+TP) with RK classifier (73.1%) vs DPO(CP+TP) with RK classifier (67.0%) — a meaningful gap beyond self-consistency. The paper also reports DPO(CP) results for both classifiers. This criticism does not hold up: the improvements are genuine.
- **"Missing related work"** (not raised but removed as per instructions): No such claim was made.
- The observation about normalization being unverified (Harsh Critic's Section-by-Section note on Methodology): The paper explicitly states "The probabilities of the three outcomes sum to one for both of these Bradley-Terry extensions" (line 98). The concern is already addressed.

## Novel Insights

Beyond the paper's own contributions, the most interesting observation from this review process is the tension between the paper's clean theoretical framing and the gap in experimental validation. The DPO-RK/DPO-D derivation is genuinely principled — it takes well-studied statistical models of ties (Rao-Kupper and Davidson) and shows they fit naturally into the DPO framework via the reward-margin reparameterization. The gradient analysis revealing that tied pairs drive margins toward zero (while wins drive margins positive) is insightful and mechanistically clear. However, the paper's experiments operationalize "ties" in a way that sidesteps the very phenomenon the work is motivated by (genuine human uncertainty). This reveals a broader pattern in the preference optimization literature: methods for handling "noisy" or "ambiguous" preferences are typically validated on clean, artificially constructed data, leaving open the question of whether they address the real-world annotation challenges they claim to solve. The paper would be significantly strengthened by directly confronting this gap.

## Suggestions

1. Add at least one experiment with human-annotated ties (or ties derived from known human rating distributions) to directly test the central motivation.
2. Include a sensitivity analysis for ν (Rao-Kupper/Davidson tie parameter) on a validation set.
3. Report results with statistical uncertainty (multiple seeds or bootstrapped confidence intervals).
4. Clearly state the evaluation metric for summarization (PairRM) and justify its use relative to GPT-4 evaluation.
5. Discuss the potential confound in the summarization tie construction explicitly.

## Score and Decision

The paper presents a clean, well-motivated theoretical contribution with reasonable initial experiments. However, the gap between the real-world motivation (human-annotated ties being wastefully discarded) and the experimental validation (purely artificial ties) is significant enough that the practical claims are not fully substantiated. The theoretical contribution is solid, but the evidence for practical utility is incomplete.

**Score:** 6.0  
**Decision:** Weak Accept — the paper has a clear theoretical contribution and clean derivations, but the experimental validation does not fully address the stated motivation. Major revisions focused on tie construction realism would strengthen the paper substantially.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>