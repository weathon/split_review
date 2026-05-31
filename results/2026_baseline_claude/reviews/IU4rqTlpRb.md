## Summary

This paper challenges the prevailing explanation for *benign relearning* in LLM unlearning — the phenomenon whereby fine-tuning an unlearned model on benign data recovers forgotten content. Prior work (the BLUR benchmark) attributed benign relearning to the *topical relevance* of the relearn set with the forgotten target. Through controlled experiments, the authors argue that **syntactic similarity** (surface-level structural overlap between the relearn set and the target set) is the more decisive driver. They further provide mechanistic evidence via representation and gradient analyses, identify a template-vs.-keyword suppression imbalance during unlearning, and propose **syntactic diversification** — paraphrasing forget queries into structurally heterogeneous forms before unlearning — as an effective remedy.

---

## Strengths

- **Principled methodological critique of BLUR.** The authors identify two legitimate confounds in BLUR's evaluation: (1) unequal dataset sizes across relevance tiers ($D_{\text{hi}}, D_{\text{mid}}, D_{\text{low}}$) cause unequal gradient update budgets within a fixed epoch, and (2) single-epoch evaluation can miss or alias peak recovery. Their corrected protocol — standardizing step budget and reporting the best-step value — is well-motivated, and Figure 3 demonstrates concretely that BLUR's ordering disappears under fair comparison.

- **Clean, compelling empirical contrast.** The TOFU experiment (Section 5) contrasts $D_{\text{relearn}}^{\text{topic}}$ and $D_{\text{relearn}}^{\text{syntactic}}$ with controlled overlap properties. Figure 4 shows that across all three unlearning methods (GA, NPO, SCRUB), syntactically similar data achieves higher relearn success rates, and Figure 5 confirms that syntactic similarity correlates with both representational and gradient proximity to the target set.

- **Mechanistic explanation via loss ratio.** The template vs. keyword token analysis (Section 6, Figure 6) is a genuinely insightful contribution. The loss ratio shows that unlearning overwhelmingly suppresses *template tokens* rather than *keyword tokens* when the forget set has rigid, repetitive surface structure. This provides a principled explanation of *why* syntactically similar fine-tuning data re-opens a pathway to forgotten content.

- **Practical remedy with well-documented benefits.** Syntactic diversification (Section 7) is simple, principled, and effectively demonstrated: Figure 8 shows near-complete suppression of benign relearning across diverse unlearning step counts, Figure 9 shows that the loss ratio converges to 1 (balanced template/keyword suppression), and Table 2 documents consistent improvements in model utility across all metrics and evaluation sets.

- **Breadth of evaluation.** Findings are replicated across four benchmarks (TOFU, WMDP, WHP, RWKU) and three unlearning algorithms, and the broader implications section (Section 8) thoughtfully extends to LoRA-based relearning and the distinction between safety training and true unlearning.

---

## Weaknesses

### Fatal
None.

### Major

- **TOFU's synthetic rigidity may be a special case.** The core experiments rely on TOFU, which uses highly templated, synthetic QA pairs ("What is the full name of the author born in X on date Y?"). By design, these queries share an almost perfectly rigid surface structure, which maximizes the template-suppression effect and makes the syntactic pathway for recovery especially salient. In more naturalistic corpora — legal documents, biomedical records, web text — the forget set may already exhibit substantial syntactic variety, so the proposed "rigidity" problem may be far less pronounced. The paper acknowledges experiments in "a more realistic unlearning scenario in Appendix C," but this appendix is unavailable for review, and how substantially the findings transfer is unclear from the main body.

- **Confound in the topical vs. syntactic comparison.** In the TOFU setup, $D_{\text{relearn}}^{\text{topic}}$ asks non-name questions about *target authors* (birthplace, occupation), while $D_{\text{relearn}}^{\text{syntactic}}$ asks name-format questions about *different authors from the retain set*. The comparison conflates two differences simultaneously: syntactic form and entity type. Because $D_{\text{relearn}}^{\text{syntactic}}$ uses retain-set author names, it could partially activate name-generation behavior in general, not purely through syntactic alignment. An ablation using entirely novel entities (from outside both the forget and retain sets) would isolate the syntactic factor more cleanly.

- **Table 1 differences are quantitatively modest.** In the BLUR re-analysis, the syntactic similarity scores across $D_{\text{hi}}, D_{\text{mid}}, D_{\text{low}}$ differ by only 0.01–0.05 in absolute terms (e.g., WHP: 0.1894 / 0.1767 / 0.1818). Drawing strong causal conclusions about benign relearning from differences of this magnitude requires more careful uncertainty quantification or a demonstration of statistical significance.

### Minor

- **Best-step criterion can inflate recovery estimates.** Reporting the maximum ROUGE-L across all steps is a valid way to control for training budget, but it also picks the most favorable single point for each condition. A more complete picture (e.g., area under the recovery curve) would be a more stable summary statistic.

- **Syntactic diversification requires GPT-4o.** No analysis is given of the cost, scalability, or quality sensitivity of this step. For practitioners with larger forget sets or without commercial API access, the method's practicality is uncertain.

- **The "primary driver" framing is occasionally stronger than the data warrant.** In Figure 5(b) under NPO, $D_{\text{relearn}}^{\text{topic}}$ achieves a relearn success rate of 0.60 vs. 0.70 for $D_{\text{relearn}}^{\text{syntactic}}$ — a meaningful difference, but not one that implies topicality is negligible. A more calibrated framing would be that syntax is a *stronger* driver than topology rather than the *primary* one.

### Trivial

None worth noting.

---

## Nice-to-Haves

- An experiment with a truly non-templated forget set (e.g., excerpts from prose narrative or legal text) would substantially strengthen generalizability claims.
- A cost and quality-control analysis for the GPT-4o paraphrasing step would aid practitioners.
- Statistical significance tests or confidence intervals on relearn success rates would improve rigor.
- Extending the loss ratio analysis to the WMDP/WHP/RWKU benchmarks would show whether the template-suppression mechanism generalizes beyond TOFU.

---

## Novel Insights

The most genuinely novel contribution is the mechanistic account in Section 6: LLM unlearning on templated data disproportionately suppresses *template tokens* rather than the semantically meaningful *keyword tokens*, because gradient updates are dominated by the high-frequency, structurally rigid phrasing shared across all forget-set QA pairs. This is a nontrivial insight that reframes the unlearning failure mode in terms of *intra-forget-set syntactic homogeneity* rather than inter-set topical overlap. The consequence — that any fine-tuning on structurally similar data restores the template scaffold and thereby unlocks the suppressed keywords — is a clear, testable, and practically actionable hypothesis. The connection to the loss ratio is an elegant diagnostic that generalizes to other data-centric unlearning improvements beyond syntactic diversification.

---

## Suggestions

- Add an ablation in the TOFU setting where $D_{\text{relearn}}^{\text{syntactic}}$ uses entirely novel fictitious entities (not from the retain set) to confirm that the effect is purely syntactic and not driven by entity-type priming.
- Report area-under-the-recovery-curve in addition to best-step maximum for a more robust evaluation statistic.
- Apply the loss ratio analysis to at least one non-TOFU benchmark (e.g., WHP or RWKU) to show the template-suppression mechanism operates beyond synthetically structured QA data.
- Include a brief cost/quality analysis of the GPT-4o paraphrasing pipeline.
- Soften the "primary driver" language in the abstract and introduction to better match the empirical nuance (particularly the NPO results in Figure 5b).

---

## Score and Decision

The paper makes a clear, novel empirical contribution: a methodologically sound critique of prior evaluation, a strong empirical demonstration that syntactic similarity drives benign relearning, a compelling mechanistic account, and a practical remedy with well-documented benefits. The core limitation — that the main analysis relies on TOFU's unusually templated structure, and that the topical/syntactic confound is not fully resolved — prevents a higher score, but these do not invalidate the core claims. The work is sufficiently novel and well-supported to contribute value to the ICLR community.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>