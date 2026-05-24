Now I have a thorough understanding of the paper. Let me construct the final consolidated review.

---

## Summary

This paper investigates three multi-objective optimization (MOO) formulations — single-level vector (VS-ASR), bilevel with a lower-level constraint (VC-ASR), and multilevel (VM-ASR) — for multilingual multi-task ASR and speech-to-text translation. The core idea is that separating highly conflicting objectives (e.g., self-supervised vs. supervised, ASR vs. S2TT) into different optimization levels improves performance. The paper reports that VM-ASR achieves up to 22.3% relative WER reduction and 27.9% BLEU improvement over baselines on the CoVoST v2 dataset with Conformer models.

## Strengths

- **Systematic comparison of three MOO formulations on a consistent multilingual multi-task setup.** The paper evaluates VS-ASR (single-level), VC-ASR (bilevel with constraint), and VM-ASR (multilevel) under the same model architectures and dataset, providing a clear ladder of increasing performance. This directly supports the claim that adding hierarchy helps (Tables 1, 2 in the paper, with textual summaries of improvements).

- **Non-trivial performance gains over baselines.** The reported improvements — up to 22.3% relative WER reduction (VM-ASR USA vs. Joint PT+FT without MOO on 100M model) and up to 27.9% BLEU improvement — are substantial and consistent across two model sizes (100M and 58M). If these numbers hold under proper statistical evaluation, they represent a practically meaningful advance.

- **Transparent reporting of training cost.** The paper reports that MOO models require ~11.6 GB GPU memory and ~2.8 hours/epoch vs. ~8.7 GB and ~2.25 hours for standard PT+FT, clarifying the computational trade-offs.

## Weaknesses

### Fatal
None.

### Major

- **Headline finding F3 ("task-based hierarchy outperforms language-based hierarchy") is asserted without supporting experimental evidence.** The paper claims this as a key contribution in the introduction (Section 1) and states "Refer to Figure 3 for an illustration of gradient conflicts." However, the only experimental comparisons presented (UAS and USA sequences in Tables 1 and 2) both compare different orderings of *tasks* (SSL→ASR→S2TT vs. SSL→S2TT→ASR). No table or figure in the main paper reports results for language-based MLO, which Remark 1 describes as "involv[ing] English (LibriSpeech) and Chinese (AISHELL)." The claim about language-based hierarchy performance cannot be verified from the presented evidence. This invalidates one of the paper's four headline findings as currently written.

- **No statistical significance or variance reported.** All results are single numbers without confidence intervals, standard deviations, or evidence of multiple independent runs (no mention of seeds or repetitions). Given the modest model sizes (58M–100M) and the limited number of languages (4–5), the claimed improvements (e.g., "22.3% relative WER reduction") could be within the noise of a single run. This weakens every quantitative claim in the paper.

- **The MoDo algorithm used to compute dynamic weights (λ) is not described, conflating the contribution of the multilevel structure with that of the dynamic weighting itself.** The λ values in all three formulations are "computed using the MoDo algorithm (Chen et al., 2023)" with zero explanation of what MoDo does, how it resolves conflicting gradients, or how it differs from standard MOO solvers. Since the baseline "Joint PT+FT without MOO" presumably lacks dynamic weighting (or uses static weighting), any improvement over that baseline could be attributed entirely to dynamic weighting rather than the multilevel hierarchy. An ablation that keeps the MOO aggregation method fixed across all three formulations and varies only the level structure is missing. Without this, the paper's central claim about hierarchical separation being beneficial is not cleanly isolated.

### Minor

- **Abstract overclaims relative to presented results.** The abstract states "extensive investigation using the LibriSpeech and AISHELL v1 datasets," and line 162 mentions experiments with "a combination of the LibriSpeech and AISHELL datasets." However, the main results (Tables 1–4) only report CoVoST v2 results. No LibriSpeech or AISHELL results appear in the main body. If these exist only in the (stripped) appendix, the main text should still reference them explicitly.

- **Penalty parameter analysis is too thin to support the claimed "crucial role."** The paper compares only two increase rates (0.002 vs. 0.02 per epoch) for the penalty parameter and uses this to claim "well-calibrated penalty parameters can improve overall ASR and S2TT performance by 8.3% and 2.2%." A comparison of two values is insufficient to establish the importance of the parameter or to provide meaningful design guidelines. Further, the threshold ε in the VC-ASR constraint formulation is never specified, and its relationship to the penalty schedule is unclear.

- **CTC loss for S2TT is non-standard and not justified.** The paper uses Connectionist Temporal Classification (CTC) loss for both ASR and speech-to-text translation tasks (line 110). CTC is the standard for ASR but is not the typical loss for sequence-to-sequence translation, which usually uses attention-based decoding or cross-entropy. This choice is not explained or justified, and it may limit the generality of the findings.

### Trivial
None.

## Nice-to-Haves

- An ablation that controls for the MOO aggregation method (e.g., keep MoDo dynamic weighting fixed and vary only whether the objectives are in one level or split across levels) would cleanly isolate the contribution of the hierarchical structure.
- If F3 (task-based vs. language-based hierarchy) is to remain a headline finding, the relevant experimental results must be included and explicitly discussed in the main paper.
- Including variance estimates from multiple seeds for at least the best and baseline methods would significantly improve credibility.

## Removed Points

These points were flagged by the reviewers but are removed from the main assessment with justification:

1. **Section 5.2 being empty.** → This is a PDF parsing artifact; the original submission likely contained content there. Removed per formatting-artifact rule.
2. **Definition 1 formatting (ℝ^⊤ should be ℝ^M).** → Formatting artifact from extraction. Removed.
3. **Figure 1 radar plots not interpretable.** → Images are not rendered in extracted text; this is a parser issue. Removed.
4. **Tables not legible in extracted text.** → Parser artifact; the original submission had properly formatted tables. Removed.
5. **Missing comparison with MGDA, PCGrad, uncertainty weighting, GradNorm.** → The hard rule prohibits citing missing related works. These are well-known methods, but under the rules, this concern is removed.
6. **Strength Finder claim that F3 is "substantiated by the experimental comparison of UAS/USA sequences."** → Factually incorrect. UAS/USA compare different orderings of tasks (both are task-based hierarchies), not task-based vs. language-based. Removed as an invalid strength.
7. **Criticism that "language-based hierarchy experiments are not presented" is kept as a weakness** (since F3 is a headline claim that requires support in the main body), but the speculation about where they might exist in a stripped appendix is removed.
8. **"The baseline Joint PT+FT without MOO is not described"** — The paper does reference Saif et al. (2024) and describes the relation to that work in lines 69–70: "Unlike (Saif et al., 2024), which employs SSL objective as a lower-level constraint... we leverage SSL objective to narrow the search space." While more detail would be helpful, the baseline is cited and contextualized.

## Novel Insights

None beyond the paper's own contributions. Both reviews largely recapitulate the paper's claims and identify gaps without offering genuinely novel interpretations outside the paper's framing. The pattern of results (single-level < bilevel < multilevel) is consistent with what one would expect if the approach is valid, but the lack of controlled ablations prevents distinguishing the hierarchy effect from the dynamic-weighting effect — a point both reviews converge on independently.

## Suggestions

1. **Address the F3 evidence gap.** Either present the language-based hierarchy experimental results in the main paper, or remove/weaken the claim. If the comparison is in the appendix, add an explicit table reference and a brief summary in the main text.
2. **Add an ablation fixing the MOO aggregation method.** Run VS-ASR, VC-ASR, and VM-ASR with the same dynamic weighting procedure (MoDo) but varying only the number and assignment of levels. This would isolate whether hierarchical separation per se is beneficial.
3. **Repeat experiments with multiple seeds and report variance.** Even 2–3 seeds for the best configuration and the strongest baseline would substantially improve credibility.
4. **Expand the penalty parameter study.** At minimum, include a zero-increase case, a few intermediate rates, and a discussion of convergence behavior.

## Score and Decision

Based on the evaluation:

The paper investigates a meaningful question and presents a systematic comparison of three MOO formulations. The core idea — that hierarchical separation of conflicting objectives improves multilingual multi-task ASR — is well-motivated and potentially valuable. However, the experimental validation has three significant gaps that collectively undermine confidence in the headline claims: (1) F3 is asserted without the required supporting evidence; (2) no variance or statistical significance is reported; (3) the MoDo dynamic weighting is not described, making it impossible to attribute gains to the hierarchical structure rather than the aggregation method. These are not fatal flaws (the core approach may be sound), but they are serious enough that the paper's central claims are not adequately supported in its current form. With substantial revisions, this could be a useful contribution.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>