Now I have a thorough understanding of the paper and the calibration anchors. Let me write the final review.

---

## Summary

This paper investigates the phenomenon of benign relearning in machine-unlearned LLMs, where forgotten information resurfaces after fine-tuning on seemingly unrelated data. The authors challenge the prevailing view that topical relevance drives this effect, and instead demonstrate through controlled experiments that syntactic similarity — surface-level structural overlap between the relearn set and the forget target — is the primary driver. They provide mechanistic evidence via representation and gradient alignment analysis, and propose syntactic diversification (paraphrasing forget-set queries to break structural homogeneity) as a practical mitigation that suppresses relearning, accelerates forgetting, and preserves model utility.

## Strengths

- **Controlled isolation of syntactic vs. topical relearning (Section 5).** The paper constructs two carefully designed relearn sets within TOFU: D_relearn^topic (same entities, different question format) and D_relearn^syntactic (same question format, different entities). Across GA, NPO, and SCRUB, the syntactically similar set consistently triggers stronger recovery of forgotten keywords (Figure 4), directly demonstrating that syntactic similarity alone is sufficient to drive benign relearning even without topical overlap. This experimental design is the paper's strongest contribution — it cleanly disentangles two confounded factors.

- **Mechanistic evidence from representation and gradient alignment (Section 6).** The paper quantifies cosine similarity between the unlearned model's last-token hidden states and gradients on D_target versus each relearn set. The syntactically similar set exhibits substantially higher alignment with the target set in both representation space and gradient direction across all three unlearning methods, and this alignment directly tracks relearn success rates (Figure 5). The template-vs-keyword loss ratio analysis (Figure 6) further reveals that standard unlearning disproportionately suppresses template tokens while under-suppressing keywords, providing a concrete optimization-level explanation for the syntactic pathway.

- **Fair re-evaluation of the BLUR benchmark (Section 4).** The paper identifies that prior BLUR conclusions were confounded by unequal training budgets (different dataset sizes) and non-monotonic recovery trajectories (evaluation at fixed epochs misses peaks). By standardizing step budgets and reporting peak recovery, the apparent advantage of highly topical relearn sets largely vanishes (Figure 3, Table 1), and the paper shows that syntactic similarity scores better align with observed recovery patterns. This is a well-executed methodological correction.

- **Practical and effective mitigation (Section 7).** Syntactic diversification — using GPT-4o to paraphrase forget-set queries into heterogeneous structures before unlearning — is intuitive given the paper's findings and is convincingly shown to suppress benign relearning (Figure 8), balance template-vs-keyword suppression (Figure 9 top), and improve model utility (Table 2). The approach is simple to implement and directly addresses the identified mechanism.

## Weaknesses

### Fatal

None.

### Major

- **Controlled isolation limited to TOFU.** The paper's strongest evidence — the controlled experiment isolating syntax from topic — is conducted exclusively on TOFU, a synthetic QA dataset built from rigid templates. While the BLUR re-analysis in Section 4 provides correlational evidence across WMDP, WHP, and RWKU, it does not perform the same controlled isolation (there is no D_relearn^topic vs. D_relearn^syntactic split on those benchmarks). The paper's central claim that "syntactic similarity is the primary driver" of benign relearning is most directly supported only in a highly templated setting. The generalization to free-form text remains an open question that the paper does not experimentally address. A pilot experiment on a less templated benchmark, or more cautious framing of the claim's scope, would substantially strengthen the contribution.

### Minor

- **ROUGE-L sensitivity in BLUR re-analysis (Section 4).** The BLUR re-analysis measures recovery using ROUGE-L, a longest-common-subsequence metric that naturally favors outputs sharing surface form with the baseline. Since syntactic similarity and surface-form overlap are correlated, ROUGE-L may partially inflate apparent recovery for syntactically similar relearn sets. This concern is substantially mitigated because (a) the paper's core finding is established in Section 5 using keyword-based metrics that avoid this confound, and (b) the syntactic similarity scores in Table 1 are computed independently via normalized Levenshtein distance. However, the BLUR section's recovery measurements should be interpreted with this limitation in mind, and the paper would benefit from explicitly discussing it.

- **Abstract slightly overclaims scope.** The abstract states that "across benchmarks, syntactically similar data consistently trigger recovery even without topical overlap." However, the controlled isolation experiment (where syntax is manipulated independently of topic) exists only on TOFU. Across BLUR benchmarks, only correlational evidence is presented. The phrasing could be more precisely scoped.

### Trivial

- The syntactic diversification procedure (prompt templates, number of paraphrases per query, filtering criteria for low-similarity cases, answer correctness verification) is deferred to Appendix G. While this is standard practice, a one-sentence summary of the quality-control approach in the main text would improve self-containedness.

## Nice-to-Haves

- A controlled utility comparison at equalized forget rates (rather than comparing at the unlearning steps where each method achieves forgetting) would strengthen the claim that diversification provides intrinsic utility benefits beyond just faster forgetting.
- The template-vs-keyword token categorization is currently manual for TOFU. A brief discussion of how this analysis could be adapted to free-form text would help readers assess the generality of the mechanistic explanation.
- The LoRA-based relearning observation in Section 8 is intriguing but presented only as a remark. A brief controlled experiment or more detailed analysis would add value.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh critic: "Crucial implementation details are deferred to an appendix that is not available for review."** Removed per instructions — the appendix exists in the original submission; its absence is a parser artifact, not an author error. The paper explicitly references Appendix G for diversification details.

- **Harsh critic: "Unverified quality of the diversified forget set" with demand for validation evidence.** The paper states that quality-control filtering is applied and references Appendix G. Demanding that all validation evidence appear in the main text is excessive for a submission; the appendix is the appropriate place. The main text does report the quantitative similarity drop (0.4513 → 0.2241), which provides some validation.

- **Strength Finder: generic strengths about "important problem."** Removed as superficial — filtered to keep only concrete, evidence-backed strengths.

- **Harsh critic: "The paper would benefit from a short discussion of the limitations imposed by the highly templated nature of TOFU."** This is valid but was merged into the Major weakness about scope rather than kept as a separate point.

## Novel Insights

The paper's most striking finding — that surface-level syntactic patterns, rather than semantic content, are the hidden pathway through which forgotten knowledge resurfaces — recasts benign relearning as a structural rather than semantic phenomenon. The template-vs-keyword loss ratio analysis (Figure 6) is particularly insightful: it shows that standard unlearning methods concentrate their optimization budget on suppressing generic phrasing patterns while leaving the actual content keywords relatively intact, and that syntactically similar fine-tuning data restores those suppressed templates and thereby unlocks the keywords. This suggests that the vulnerability is not in the unlearning methods per se but in the homogeneity of the data they are applied to — a perspective that shifts the remedy from better algorithms to better data preparation.

## Suggestions

- Add a controlled experiment on at least one less-templated benchmark (e.g., WHP or a custom free-form dataset) with a syntax-vs-topic split similar to the TOFU design, or explicitly scope the claims to templated settings.
- Include a brief discussion of the ROUGE-L surface-form sensitivity in Section 4 and why the TOFU keyword-based evaluation avoids it.
- Add a one-sentence summary in Section 7.1 of the quality-control approach used for the diversified forget set (e.g., "We filter paraphrases that alter the target answer or retain high similarity to the original query").
- Consider equalizing forget efficacy in the utility comparison, or explicitly clarify that Table 2 compares models at the unlearning steps where each achieves forgetting.

## Score and Decision

**Calibration anchors used:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| Jogging the Memory of Unlearned LLMs (fMNRYBvcQN) | 6.75 | R1, R2 | Studies relearning attacks empirically; our paper goes further with mechanistic explanation and mitigation |
| Do Unlearning Methods Remove Information (uDjuCpQH5N) | 5.50 | R1 | Evaluation framework for unlearning; our paper has stronger experimental design and proposes a solution |
| A Closer Look at Machine Unlearning (Q1MHvGmhyT) | 6.00 | R1, R2 | Proposes metrics and methods; comparable scope but our paper has a cleaner central finding |
| Dissecting Language Models: Selective Pruning (8SPSIfR2e0) | 5.75 | R2 | Method-focused; less relevant to our paper's analytical contribution |
| A Probabilistic Perspective on Unlearning (51WraMid8K) | 8.00 | R2 | Formal probabilistic framework with theoretical guarantees; our paper is more empirical and less theoretically grounded |

**Bracketing:** Round 1 placed the paper between approximately 6.0 and 8.0. The paper is clearly stronger than the 6.00 "A Closer Look" (which primarily proposes metrics) and the 5.50 "Do Unlearning Methods Remove Information" (which is primarily an evaluation). Round 2 narrowed the comparison: the paper is stronger than "Jogging the Memory" (6.75) — which demonstrates relearning but lacks mechanistic depth and a mitigation — but does not reach the theoretical rigor of "Probabilistic Perspective" (8.00). The controlled experimental design, mechanistic evidence, and practical mitigation place this paper firmly in the 7.0 range.

**Final score: 7.0.** The paper makes a genuinely novel and well-supported contribution with a clever experimental design and a practical remedy. The primary limitation is the TOFU-specificity of the controlled experiments, which tempers the generality of the claims but does not undermine the core finding within its demonstrated scope.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>