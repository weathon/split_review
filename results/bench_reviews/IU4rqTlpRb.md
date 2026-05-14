Now I have a thorough understanding of the paper and the calibration anchors. Let me write the consolidated final review.

---

## Summary

This paper investigates why benign relearning—the recovery of forgotten information after unlearning via fine-tuning on benign data—occurs. The authors argue that syntactic similarity between the relearn and forget sets, rather than the previously assumed topical relevance, is the primary driver. Through controlled experiments on the TOFU benchmark, they demonstrate that syntactically similar but topically disjoint data triggers far stronger recovery than topically relevant but structurally different data. They provide mechanistic evidence through representation/gradient alignment analysis and a template-vs-keyword suppression decomposition, and propose syntactic diversification—paraphrasing forget-set queries into varied surface forms before unlearning—as an effective mitigation that also improves model utility.

## Strengths

- **Controlled isolation of syntactic vs. topical factors (Section 5, Figure 4):** The paper constructs two carefully designed relearn sets on TOFU: a topically relevant set sharing entities with the forget set, and a syntactically similar set (name-format QA pairs from different authors) preserving surface form without topic overlap. Across GA, NPO, and SCRUB, the syntactically similar set consistently triggers far stronger recovery. This is a clean experimental design that directly isolates the claimed mechanism.

- **Mechanistic account via template-vs-keyword suppression (Section 6, Figure 6, Appendix F):** The decomposition of target answers into template tokens and keyword tokens, with the loss ratio metric, reveals that standard unlearning disproportionately suppresses templates while leaving keyword-level knowledge under-suppressed. The causal template-injection experiment (Appendix F) confirms this: when the template is provided as a prefix, the model still outputs the correct keyword, demonstrating that keywords survive unlearning.

- **Representation and gradient alignment analysis (Section 6, Figure 5):** The syntactically similar relearn set exhibits substantially higher cosine similarity to the target set in both hidden-state representations and loss gradients compared to the topically relevant set, and this alignment correlates with higher relearn success rates. This provides a plausible mechanistic link between surface-structure overlap and recovery.

- **Syntactic diversification as a principled remedy (Section 7):** The proposed method—paraphrasing forget queries into diverse surface forms—directly addresses the identified vulnerability by breaking structural homogeneity. It yields balanced template/keyword suppression (Figure 9), robustness to syntactic relearning (Figure 8), and improved utility across Real Authors, World Facts, and Retain set metrics (Table 2). The method is simple, well-motivated by the preceding analysis, and effective within the evaluated setting.

- **Robustness of the syntactic similarity claim across metrics (Appendix I):** The finding that syntactically similar data drives relearning holds across three distinct similarity metrics (template-mining, parse-tree, and Levenshtein), confirming that the result is not an artifact of a single metric choice.

## Weaknesses

### Fatal

None.

### Major

- **Limited evidence for generalization beyond templated synthetic data:** The central experimental demonstration (TOFU, Section 5) uses a synthetic dataset where both forget and relearn queries follow rigid, predictable templates (e.g., "What is the full name of the author born in...?"). While the WHP experiment (Appendix C) and WMDP experiment (Appendix D) attempt to broaden the evidence, they are limited: WHP uses only 10 target questions and one unlearning method (GA), and WMDP also uses a single method. The paper's headline claim—that syntactic similarity is the primary driver of benign relearning—would be substantially strengthened by systematic evaluation on at least one additional benchmark with a full suite of unlearning methods and a larger, more naturalistic forget set. The current evidence is convincing for template-heavy settings but does not yet establish the claim's breadth.

- **Conflation of syntactic similarity with task-format similarity in the TOFU experimental design:** The syntactically similar relearn set on TOFU consists of name-format QA pairs drawn from the retain set. These not only share surface syntax with the target queries but also preserve the identical task format (retrieving an author's full name given biographical cues). The observed recovery may therefore partially reflect reactivation of the underlying name-retrieval task rather than purely surface-form overlap. The paper does not discuss or control for this confound, which weakens the interpretation that syntax alone is the driver. A control using syntactically similar data that does not share the name-retrieval task format would help delineate syntax from task similarity.

### Minor

- **The BLUR reassessment (Section 4) uses a protocol whose own biases are not fully examined:** The authors equalize step budgets and report max ROUGE-L to correct confounds in the original BLUR evaluation. However, reporting only the maximum across steps can inflate noise and does not reflect typical behavior. While the reassessment raises valid questions about BLUR's conclusions, the evidence is suggestive rather than definitive. Notably, Figure 2c for RWKU still shows a visible ordering by topical relevance, which the paper does not discuss. The role of this section in motivating the main investigation could be preserved while acknowledging its limitations more openly.

- **No ablation comparing GPT-4o paraphrasing to simpler diversification baselines:** The syntactic diversification method relies on GPT-4o for paraphrasing. The paper shows in Appendix G.4 that diversification also works with open-source models, but does not compare against simpler, non-LLM-based diversification strategies (e.g., rule-based reordering, synonym substitution, multiple handwritten templates). Without such baselines, it is unclear whether the sophisticated paraphrasing is necessary or whether any form of structural variation would suffice.

### Trivial

- The Levenshtein distance, while adequate as a rough indicator and supplemented by alternative metrics in Appendix I, captures character-level sequence overlap rather than syntactic structure per se. The paper acknowledges this (footnote in Section 5.1) but could more explicitly note the metric's limitations in the main text.

## Nice-to-Haves

- A direct comparison of GPT-4o paraphrasing against simpler diversification baselines (e.g., rule-based reordering, synonym substitution) to demonstrate that the specific form of diversification matters beyond just introducing variability.
- A discussion of how the syntactic similarity effect might interact with model scale, given that only Llama-2-7B and Phi-1.5B are tested.
- Examples of recovered answers from both relearn sets to make the qualitative difference more concrete for readers.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **"The reassessment of BLUR's findings is not robust enough... the protocol may be insufficient" (from Harsh Critic, point 1):** Partially kept as a minor weakness. The harsh critic's framing that the BLUR reassessment is entirely unconvincing is too strong; the controlled-step-budget correction is a legitimate improvement over the original evaluation. The key point about max-over-steps potentially inflating noise is retained as a minor concern. The claim that Levenshtein distance is "not a meaningful measure of syntactic structure" is weakened given Appendix I's demonstration of consistency across three metrics.

2. **"The experimental demonstration may not generalize to real-world unlearning settings" (from Harsh Critic, point 2):** Kept as a major weakness but with more precise framing. The harsh critic's concern about WHP having only 10 target questions and one method is accurate and incorporated. The claim that LLM-as-judge evaluation is "not tightly standardized" is removed because the paper uses the established prompt from Zheng et al. (2023) following Hu et al. (2025a), which is a standard practice in the field.

3. **"Missing experiments" from the Harsh Critic regarding a systematic comparison across more diverse forget sets and an ablation of the diversification strategy:** The diversification ablation concern is kept as a minor weakness. The demand for systematic comparison across "a benchmark like RWKU or a naturally written forget set" is moved to nice-to-have since the paper already provides evidence on WHP and WMDP beyond TOFU.

4. **All Strength Finder strengths about generic importance:** Removed items like whether the problem is "important" or "interesting" as these are generic and not concrete.

5. **Harsh Critic's note that "this appendix needs a clearer statement of what is being compared and why":** This is a presentation suggestion; moved to Trivial.

6. **"The description of the proposed diversification as 'effective' and that it 'substantially alleviates the trade-off' is supported by the experiments, but the scope is narrow (TOFU)":** Already captured by the major weakness about limited generalization.

## Novel Insights

The paper's key novel insight is the template/keyword asymmetry in unlearning: standard gradient-based unlearning methods disproportionately suppress templatic surface patterns while leaving the factual keywords largely intact. This provides a structural explanation for why benign relearning occurs—fine-tuning on syntactically similar data restores the suppressed templates, creating a pathway for the surviving keyword knowledge to re-emerge. This framing goes beyond prior work that attributed relearning to topical relevance and offers a more mechanistic account. The template-injection experiment (Appendix F) is a particularly elegant causal test of this hypothesis.

## Suggestions

- Conduct the TOFU experiment with an additional syntactically similar set that does NOT share the name-retrieval task format (e.g., syntactically similar QA pairs about different kinds of facts), to disentangle syntax from task similarity.
- Extend the WHP or WMDP evaluation to include at least one additional unlearning method (e.g., NPO) to show that the syntactic relearning effect generalizes across methods in realistic settings.
- Include a simple non-LLM diversification baseline (e.g., multiple hand-written templates) to establish the necessity of sophisticated paraphrasing.
- Acknowledge more openly that the BLUR reassessment, while raising valid concerns about confounds, uses a protocol (max-over-steps) that has its own limitations, and that the RWKU benchmark still shows some residual topical ordering.

---

Now, comparing to the calibration anchors:

- **`/home/wg25r/review_agent/human_reviews_2026/7cEMkTu7Lf.md` (avg 4.00, Reject):** "Unlearning Isn't Deletion" studied relearning/reversibility but was criticized for lacking novelty (confirming known problems) and providing no actionable insights or methods. The paper under review is stronger: it identifies a novel factor (syntax), proposes a method (diversification), and provides mechanistic analysis. **This paper is clearly stronger.**

- **`/home/wg25r/review_agent/human_reviews_2026/EyXBv291ST.md` (avg 3.50, Reject):** "Effective Unlearning in LLMs Relies on the Right Data Retention Strategy" explored retain-set selection strategies for unlearning. The paper under review is substantially stronger in terms of novelty, mechanistic depth, and methodological contribution. **This paper is clearly stronger.**

- **`/home/wg25r/review_agent/human_reviews_2026/BcjZCertEk.md` (avg 4.67, Accept Poster):** "Learning-Time Encoding Shapes Unlearning" studied how data encoding affects unlearning difficulty, with controlled experiments and a novel perspective. It had one very negative review (2) and two positive ones (6,6). The paper under review is comparable: both identify under-explored factors in unlearning (encoding vs. syntax), both provide controlled experiments and practical insights, and both have limitations in scope/generalization. The paper under review arguably has a stronger mechanistic story (template/keyword analysis) and a more directly actionable method (diversification). **Comparable quality.**

- **`/home/wg25r/review_agent/human_reviews_2026/pZsUT3QB69.md` (avg 4.50, Reject):** "On the Fragility of Latent Knowledge" provided layer-wise analysis of unlearning with a proposed method (CRU). Had mixed reviews (2, 8, 4, 4). The paper under review has a cleaner experimental design, a more coherent narrative, and a method that directly follows from its analysis. **This paper is comparable or slightly stronger.**

- **`/home/wg25r/review_agent/human_reviews_2026/K4pQPqibC3.md` (avg 4.00, Reject):** "From Theft to Bomb-Making" studied ripple effects in unlearning for jailbreak defense. The paper under review has a more focused investigation and clearer contribution. **This paper is stronger.**

- **`/home/wg25r/review_agent/human_reviews_2026/25F5ot3UWg.md` (avg 4.00, Reject):** "The Role of Learning and Memorization in Relabeling-based Unlearning" studied relabeling-based unlearning. The paper under review has broader scope and more actionable insights. **This paper is stronger.**

- **`/home/wg25r/review_agent/human_reviews_2026/r6Z3BXDrzO.md` (avg 4.50, Reject):** "On the Impossibility of Retrain Equivalence in Machine Unlearning" provided theoretical analysis of unlearning limitations. The paper under review is more empirical but has a more complete story (insight → analysis → method). **Comparable but different in approach.**

The paper under review is most comparable to "Learning-Time Encoding Shapes Unlearning" (4.67, Accept Poster) in terms of contribution type and quality. Given the stronger mechanistic analysis and actionable method in the paper under review, but tempered by the limited generalization evidence (major weakness), I would place it slightly above that anchor. 

**Final score: 5.5.**

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>