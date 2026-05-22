Now I have a thorough understanding of the paper. Let me construct the consolidated review.

---

## Summary

This paper identifies an underexplored failure mode in LLM unlearning—"spurious unlearning"—where gradient-ascent-based methods suppress target responses but probability mass is redistributed into semantically similar rephrasings (the "squeezing effect"). To address this, the authors propose a bootstrapping (BS) framework that incorporates the model's own high-confidence predictions (its "model beliefs") as auxiliary forgetting targets. Two instantiations are provided: BS-T (token-level soft targets that penalize top-k alternative tokens) and BS-S (sequence-level augmentation with sampled high-confidence generations). Theoretical analysis using the AKG learning dynamics framework characterizes how BS-T reshapes gradient residuals. Experiments on TOFU, WMDP, and MUSE across multiple model scales (1B–8B) show that BS methods achieve better forget–retain trade-offs than several baselines.

## Strengths

- **Novel diagnosis of spurious unlearning and the squeezing effect.** Section 3.1 provides concrete case studies (Tables in Case 1 and Case 2) showing that NPO-produced responses retain semantic content despite low ROUGE/perplexity scores. Figure 2a quantifies this systematically: NPO's outputs have semantic similarity scores (~2.5) near the high-likelihood band (~1.0) and far above retrain (~4.5), demonstrating that spurious unlearning is not a corner case but a systematic problem. Figures 2b–2c trace the log-probability dynamics, empirically confirming the squeezing mechanism.

- **Well-motivated, modular bootstrapping framework.** The decomposition into token-level (BS-T, Eq. 5–6) and sequence-level (BS-S, Eq. 7) forms is clean and grounded in the belief analysis of §4.1. The approach is explicitly designed to be compatible with existing losses (GA, NPO, WGA, GradDiff), making it easy to integrate into existing pipelines.

- **Broad and consistent empirical gains.** Tables 1–2 show BS methods achieving the best aggregate scores across TOFU (all three model scales, all forget percentages) and WMDP (Zephyr-7B). BS-S consistently delivers the best trade-off (e.g., TOFU 10% 1B: Agg. 0.61 vs. next-best 0.58; WMDP: Bio 0.26 + MMLU 0.54 vs. NPO's 0.27 + 0.44). The gains are not limited to a single benchmark or architecture.

- **Theoretical characterization of the BS-T residual.** Theorem 5.2 formally shows how BS-T adds an extra belief term λ·q^i to the GA residual G_GA^i, spreading forgetting pressure over the top-k neighborhood rather than concentrating it on the target token. This provides a formal grounding for why BS-T should suppress semantically proximate alternatives.

## Weaknesses

### Fatal
None.

### Major

1. **BS-S's data augmentation confounds the comparison.** As described in Eq. 7 (Section 4.2), BS-S augments the forget set with N sampled high-confidence generations, giving it strictly more unlearning data than any baseline. No baseline receives an analogous augmentation (e.g., repeated sampling from the original model, paraphrasing). Since BS-S shows the clearest gains over baselines (e.g., TOFU 10% 1B: BS-S 0.61 vs. NPO 0.58; BS-T 0.59 vs. NPO 0.58), a control experiment that provides baselines with an equivalent amount of additional (but randomly or differently sampled) forget data is needed to attribute the improvement to the *model belief* mechanism specifically rather than to the increased volume of unlearning data. This is mitigated somewhat by BS-T (which does not augment data and still shows modest improvements), and by the WMDP results where BS-T itself improves retention substantially (MMLU 0.52 vs. NPO 0.44), but the core claim about BS-S's superiority remains partially confounded.

### Minor

1. **BS-T's improvements over strong baselines are modest in several settings.** On TOFU 10%, BS-T's aggregate scores are close to NPO's (1B: 0.59 vs. 0.58; 3B: 0.62 vs. 0.62; 8B: 0.63 vs. 0.63). The clearest evidence for the framework's effectiveness comes from BS-S, which introduces the data augmentation confound above. A clearer separation between BS-T and NPO on some settings would strengthen the paper's central claim.

2. **LLM judge (LaaJ) used without human validation.** The evidence that BS methods mitigate spurious unlearning (Fig. 4c) relies entirely on Gemini 2.5 Flash as an LLM judge. While the paper cites prior work establishing LLM-as-judge alignment (Zheng et al., 2023; line 152), no human evaluation or correlation analysis is provided for this specific task. Given that the paper's motivation partly rests on the unreliability of automated metrics, validating the judge against human judgments would strengthen the claims about spurious unlearning mitigation.

3. **Base loss for BS methods in experiments is not explicitly stated in the main text.** Section 4.2 states that BS-T and BS-S can be combined with NPO, WGA, etc. (line 214), and the theoretical analysis assumes L_BST as the base (line 250), but the main experiments do not state which specific loss is used for Tables 1–2. The appendix (Appx. F.5) studies "the influence of different unlearning losses in BS-S," but the core experimental setup is underspecified in the main paper, hampering immediate reproducibility.

4. **No variance or confidence intervals reported.** Tables 1–2 report single numbers without standard deviations. Given that several comparisons are close (e.g., BS-T 0.59 vs. NPO 0.58 at 1B 10%), it is unclear whether improvements are statistically reliable. While single-run evaluation is common practice in this benchmark setting, reporting variance would increase confidence in the results.

5. **Theoretical analysis is more descriptive than predictive.** Theorem 5.2 shows how BS-T modifies the residual term compared to GA, which is a formal restatement of the loss design. The theory characterizes the difference in gradient structure but does not prove that this difference leads to better unlearning outcomes or quantify the degree of squeezing mitigation. The practical insight is well-illustrated by Figure 3, but the formal contribution is limited.

### Trivial
None.

## Nice-to-Haves

- A control experiment for BS-S that gives baselines an equivalent volume of augmented forget data (e.g., from the original model or via back-translation) would cleanly isolate the benefit of model beliefs.
- Sensitivity plots for the key hyperparameters (λ_BST, λ_BSS, k, temperature) would help practitioners.
- A qualitative comparison table of model outputs across all methods (as mentioned in Appx. F.4) would be useful in the main paper.

## Removed Points

Points flagged for removal from the Harsh Critic's review, treated with caution:

1. **"The use of 'model beliefs' conflates two concepts (token-level and sequence-level)"** — The paper clearly distinguishes local beliefs (top-k at token level, Section 4.1) and global beliefs (sampled sequences, Section 4.2), so there is no conflation. REMOVED (factually incorrect/misreading).

2. **"Missing appendix content / proofs deferred to appendix"** — The parsing process strips appendices from all submissions; proofs deferred to appendix are standard practice and not a weakness. REMOVED (parser artifact).

3. **"Hyperparameters not given in main text"** — The appendix (referenced as Appx. F.5) contains hyperparameter details; the main paper references them. REMOVED (parser artifact; details exist in original submission).

4. **"MUSE results relegated to the appendix"** — The main paper summarizes experiments across three benchmarks (TOFU, WMDP, MUSE); MUSE results are explicitly referenced as in Appx. F.3. This is standard page-limit practice. REMOVED (scope creep / standard practice).

5. **General "evaluation lacks rigor" type statements without concrete anchors** — These are area-of-concern sweeps rather than specific weaknesses. REMOVED (filtering discipline).

## Novel Insights

None beyond the paper's own contributions. The identification of the squeezing effect as the mechanism behind spurious unlearning, and the connection to model beliefs as a natural countermeasure, constitute the paper's primary novel insight. The AKG-based theoretical framing provides a formal vocabulary for the phenomenon, but its results are largely descriptive of the loss design rather than surprising.

## Suggestions

1. In the experiments section, explicitly state which base loss (e.g., GA, NPO, or BST) is used as L in BS-S and as the foundation for both BS-T and BS-S. This is essential for reproducibility.

2. Add a controlled ablation where baselines receive an equivalent number of additional forget sequences (sampled randomly or via simple paraphrasing) to isolate the effect of the model-belief mechanism in BS-S from the effect of having more unlearning data.

3. Report results with variance (e.g., across 3 random seeds) for at least the main comparison settings, particularly where scores are close.

4. If possible, include a small-scale human evaluation of the LLM-judge scores for spurious unlearning to validate that the LaaJ proxy is reliable for this specific task.

## Score and Decision

**Originality:** The paper identifies a genuinely underexplored failure mode (spurious unlearning via squeezing effect) and proposes a novel, well-motivated solution.

**Importance of research question:** LLM unlearning is a practically important area, and understanding why existing methods fail is valuable.

**Claims supported:** The core claims are partially supported. The problem diagnosis is well-evidenced. BS-T shows modest but consistent improvements. BS-S shows clearer gains but is confounded by data augmentation.

**Soundness of experiments:** Broad coverage across benchmarks, models, and forget settings. Some concerns about data augmentation confound, missing variance, and underspecified base loss.

**Clarity of writing:** Generally well-written and clearly structured.

**Value to the community:** The problem identification and the bootstrapping framework are likely to influence future work in LLM unlearning.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>