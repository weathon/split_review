Now I have all the information needed. Let me synthesize the final review.

---

## Summary

This paper empirically compares three multi-objective optimization (MOO) formulations for multilingual multi-task ASR and speech-to-text translation (S2TT): single-level (VS-ASR), bilevel constrained (VC-ASR), and multilevel (VM-ASR). On CoVoST v2, the multilevel VM-ASR method achieves up to 23.7% WER reduction and 27.9% BLEU improvement over two-stage PT+FT baselines, with consistent gains over the single-level and bilevel alternatives. The paper also studies penalty parameter schedules and the distinction between task-based and language-based hierarchy.

## Strengths

- **Clear empirical comparison with consistent gains for the multilevel method (VM-ASR).** Across both model sizes (100M and 58M) and across languages, VM-ASR improves ASR WER by up to 23.7% and S2TT BLEU by up to 27.9% over two-stage PT+FT, and on average outperforms the best bilevel method (VC-ASR) by 5.6% and 5.9% respectively (Tables 1 and 2). These results are concrete and directly support the paper's practical claim about the benefit of separating conflicting objectives.

- **Systematic ablation of penalty parameter schedules.** Tables 3 and 4 demonstrate that increasing the penalty parameter too fast (0.02 vs. 0.002 per epoch) significantly hurts performance, while well-calibrated penalties improve ASR and S2TT by 8.3% and 2.2%. This provides actionable guidance for applying similar methods.

- **Well-specified update rules and hyperparameters.** The three formulations differ in which objectives receive MoDo dynamic weights vs. scalar penalty parameters, and the paper provides the update equations (Sections 4.2–4.4) and training details (Section 5) clearly enough to enable replication.

## Weaknesses

### Fatal
None. The core empirical finding — that VM-ASR outperforms VC-ASR and VS-ASR — is supported by the reported results. The weaknesses below concern framing, experimental controls, and missing evidence, but do not invalidate the observed performance hierarchy.

### Major

- **The gap between the claimed "multilevel optimization" framework and the actual algorithm undermines the conceptual contribution.** The formal definitions in equations (3) and (4) describe problems with nested structure (lower-level problems solved to optimality, upper-level conditioned on lower-level solutions). The actual update rules (equations 5, 7, 8) are weighted gradient sums where the only difference is *which* terms use MoDo dynamic weights (λ) vs. scalar penalty parameters (η). There is no iterative lower-level solve, no hypergradient, and no feedback loop between levels in the conventional bilevel/multilevel optimization sense. The penalty method is a standard technique for *approximating* constrained problems, but calling this "multilevel optimization" without addressing the gap oversells the novelty. The paper should either implement a genuine bilevel method (e.g., with inner-loop solves) or reframe the contribution around scheduled weighting of gradient groups.

- **The comparison between VC-ASR and VM-ASR confounds hierarchy with the number of tunable penalty parameters.** VC-ASR uses one scalar penalty parameter (η for SSL). VM-ASR uses two (η for SSL, η₁ for S2TT). Since VM-ASR has strictly more degrees of freedom in its weighting schedule, the reported improvement (5.6%/5.9%) cannot be confidently attributed to the "multilevel hierarchy" rather than to having an additional tunable scalar that happens to be beneficial. A controlled ablation — e.g., VM-ASR with η₁ = 1 fixed, or VC-ASR with an additional scheduled scalar weight on S2TT — is needed to isolate the effect of hierarchy from the effect of extra tuning parameters.

- **Results on LibriSpeech and AISHELL are mentioned in the abstract and contributions (F2, F3) but no results tables appear in the paper.** The paper says "we performed experiments with a combination of the LibriSpeech and AISHELL datasets" (line 162) and makes claims about language-based hierarchy involving English and Chinese (Remark 1), but provides no quantitative results for these datasets. This weakens the claimed generality across datasets — the main empirical case rests entirely on CoVoST v2.

### Minor

- **No statistical measures reported.** None of the tables include standard deviations, confidence intervals, or replication information. Given that the reported improvements are often 10–20% relative, error bars are needed to assess whether differences between methods are reliable.

- **The VC-ASR formulation (equation 4) uses the term min_θ l_u(θ) in the constraint, which requires knowledge of the global minimum of the self-supervised loss.** The paper never explains how this quantity is estimated or circumvented. The actual algorithm (equation 7) uses a simple penalty method with a scheduled η, which does not enforce the stated constraint. This gap between formulation and implementation is confusing.

- **Unsubstantiated claim about theoretical guarantees.** Finding F4 states that large penalty parameters "theoretically guarantee good convergence of lower-level objectives" but provides no reference, theorem, or reasoning. If this claim is established in the MOO literature, it should be cited; if not, it should be removed.

- **The penalty parameter ablation (Tables 3, 4) is only reported for VC-ASR and VM-ASR.** Since VS-ASR does not use penalty parameters, it is not included. This limits the ablation's ability to inform the broader comparison between all three methods.

- **The "objective soups" framing is metaphorical and carries no operational meaning.** Unlike rewarded soups (Rame et al., 2024) or model soups, which describe specific averaging procedures, the paper never defines what a "soup recipe" is computationally. The term appears in the title but does no work in describing the method.

### Trivial

- The MoDo algorithm (Chen et al., 2023) is referenced as the source of dynamic weights but is never summarized. A one-sentence description of how MoDo solves the minimax problem over the simplex would improve readability.

## Nice-to-Haves

- An ablation where VS-ASR is given the same number of scalar penalty parameters as VC-ASR and VM-ASR, to isolate whether the improvement comes from the multilevel *formulation* or from using differently scheduled scalars.
- A brief summary of the MoDo algorithm to make the paper more self-contained.
- If the LibriSpeech/AISHELL results exist in an appendix (stripped by the parser), a summary table in the main paper would strengthen the multi-dataset claim.

## Removed Points

These points are flagged to be removed, treat them with caution:

- The critic's characterization that "multilevel optimization is not actually implemented" is too absolute — penalty methods are a standard (if approximate) technique for constrained/bilevel problems. The gap between formalism and algorithm is real, but the critic overstates the severity by implying no valid connection exists.
- The critic's suggestion to "implement a genuine bilevel method" using AID/hypergradients is a valid research direction but is a nice-to-have, not a requirement for the paper as an empirical comparison of different training strategies.
- The criticism about the penalty parameter schedule ablation not including VS-ASR is noted but does not seriously undermine the paper, since VS-ASR does not use penalty parameters by design.

## Novel Insights

None beyond the paper's own contributions. The reviews surface concerns about experimental controls (confound between hierarchy and degrees of freedom) and framing (gap between multilevel formalism and penalty-based algorithm), but these are analytical critiques of the paper's claims, not novel insights that extend beyond the paper.

## Suggestions

1. Either reframe the paper as a comparison of different gradient-weighting strategies (MoDo vs. scheduled penalty scalars), removing the "multilevel optimization" framing that the algorithm does not faithfully implement, OR add a genuine bilevel optimization baseline with inner-loop solves.
2. Add a controlled ablation where VS-ASR and VC-ASR receive the same number of tunable scalar parameters as VM-ASR, to disentangle hierarchy from degrees of freedom.
3. Include results for LibriSpeech and AISHELL in the main text, or retract the multi-dataset generality claim if those results are insufficient to support it.
4. Add error bars (standard deviations or confidence intervals) to all main tables.
5. Clarify how the constraint in equation (4) (involving min_θ l_u(θ)) is actually handled, or revise the formulation to match the penalty algorithm used.

## Score and Decision

The paper addresses a practically important problem and provides clear empirical evidence that its proposed VM-ASR method works well on CoVoST v2. However, the conceptual framing is significantly oversold — the claimed "multilevel optimization" framework is not faithfully implemented, and the comparison confounds hierarchy with degrees of freedom. Additionally, results on two of the three datasets mentioned in the abstract are missing from the main paper, and no statistical measures are reported. These issues do not invalidate the core empirical finding but weaken the paper's contribution as stated. The paper would need substantial revisions (reframing, controlled ablations, and more complete results) to make a convincing case.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>