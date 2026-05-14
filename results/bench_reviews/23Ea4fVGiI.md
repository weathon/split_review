## Summary

This paper introduces TMK (Task-Method-Knowledge) structured prompting — a framework borrowed from cognitive science — to improve LLM performance on formal planning tasks. Evaluated on PlanBench's Blocksworld domain (Classic, Mystery, Random variants), the approach yields impressive headline numbers, most notably raising o1's accuracy on Random Blocksworld from 31.5% to 97.3% (a 65.8 pp gain). The paper also observes a "performance inversion" where Random (opaque tokens) becomes easier than Mystery (semantically misleading tokens) under TMK, which it interprets as evidence that TMK acts as a symbolic steering mechanism shifting the model from linguistic approximation to code-like formal manipulation.

---

## Strengths

- **Dramatic and systematic empirical gains on the hardest domain variant.** TMK prompting raises o1's accuracy on Random Blocksworld from 31.5% to 97.3% (Table 2). This result is the paper's headline finding and directly supports the claim that TMK can help models handle fully opaque symbolic tasks. The magnitude of improvement (65.8 pp) is large enough to be practically and scientifically interesting regardless of explanatory uncertainties.

- **The "performance inversion" is a genuinely intriguing observation.** Under plain text, o1 scores higher on Mystery (74.3%) than Random (31.5%) — the expected pattern given semantic priors. Under TMK, the ordering flips: Random (97.33%) surpasses Mystery (83.3%). This reversal is non-trivial and is used to argue that TMK changes the underlying reasoning modality rather than merely providing more context. Even if alternative explanations exist, this pattern invites further investigation and is a genuinely novel empirical observation.

- **The paper is well-motivated and responsive to known criticisms of prior prompting work.** Section 5.1 explicitly addresses three common critiques (pattern-matching from n-shot examples, contradictory CoT traces, and lack of planning gains across models) and explains how the experimental design mitigates each. The one-shot example is randomly chosen and does not match specific problem instances, which helps address the pattern-matching concern. The paper also uses full plan-sequence evaluation (not just final state), following PlanBench's rigorous validation.

- **Borrowing TMK from cognitive science is a creative and novel direction.** While hierarchical task decomposition is not new (HTN, BDI), TMK's explicit representation of teleology ("why") and its prior success in educational contexts (Sushri et al., 2024; Dass et al., 2025) makes this a distinctive hypothesis worth exploring. The paper introduces this synthesis to the LLM planning literature for the first time, to the best of my knowledge.

---

## Weaknesses

### Fatal

None. The paper has serious methodological gaps, but they are addressable with additional experiments rather than reflecting a fundamentally flawed premise.

### Major

- **Missing control for information content vs. structure.** The TMK prompt provides a full, hierarchical specification of every action's preconditions, effects, parameters, and domain ontology. The plain-text prompt (from PlanBench) does not provide this level of detail. The paper never tests whether the *same* information expressed in a non-TMK format (a flat list, a plain paragraph, a simple JSON without TMK's task-method-knowledge decomposition) produces similar gains. The paper's central claim — that TMK functions as a "symbolic steering mechanism" with special structural properties — requires this control. Without it, the observed improvement could simply reflect providing more complete domain knowledge rather than TMK's specific hierarchical/teleological structure. The paper partially addresses this by arguing that if TMK only added information, gains would be uniform (the performance inversion argues against a mere-information effect), but this is indirect evidence. A direct control is needed. This is the most consequential gap in the paper.

- **Baseline comparison confounds the core quantitative results.** Two issues interact here: (a) TMK uses one-shot prompting while the Table 2 "Plain Text" baseline is the best of zero-shot and one-shot from the PlanBench leaderboard. The paper argues this is conservative (zero-shot > one-shot for plain text) and cites sample testing in the OSF repository, but the one-shot plain-text numbers are not shown in the paper itself. (b) More critically, the extraction pipeline was modified for the TMK results (to handle stochastic outputs with extra words, symbols, and variant phrasings in the Random domain, as described in §3.2), but the baseline results were not re-evaluated with the same extraction. The paper notes this extraction change explicitly but does not assess whether the baseline numbers would shift under the same pipeline. While the magnitude of the o1 Random improvement (65.8 pp) is so large that it is unlikely to be an artifact of extraction leniency alone, the lack of an apples-to-apples comparison weakens the quantitative foundation of every result in Table 2. These issues are fixable (re-run baselines with same extraction, report one-shot plain text in the paper) but must be addressed before the headline numbers can be taken at face value.

### Minor

- **No experimental comparison against CoT or ReACT.** The paper discusses CoT and ReACT in the related work section (§2.1) and cites literature documenting their limitations for planning (Stechly et al., 2024; Bhambri et al., 2025). However, it never benchmarks TMK against these methods in the *same* experimental setup. Given that the paper's contribution is about prompting for planning, and given that the PlanBench leaderboard includes CoT results for some models, the absence of a direct head-to-head comparison is a noticeable omission. It leaves open the question of whether TMK offers anything beyond what prior prompting methods already provide (or fail to provide) on these exact problems.

- **Single domain (Blocksworld) and single model family (OpenAI) limit scope.** The paper acknowledges this in §5.3 and mentions Logistics as future work. However, the paper's title and framing ("LLM Performance on Planning Tasks") imply broader applicability. Combined with the other methodological gaps, the narrow scope weakens the generality of any claims.

- **No ablation of TMK components.** The paper claims that TMK's teleological "why" links and hierarchical decomposition are important, but provides no ablation experiments that remove components (e.g., Knowledge section, teleological goal-method links) to test what drives improvement. Without ablation, attributing gains to specific properties of TMK rather than to any structured JSON representation is speculative.

- **No statistical significance or variance reporting.** All results in Table 2 are single percentages without confidence intervals, standard deviations, or multiple-run means. Given the stochasticity of LLM outputs, this is a standard expectation.

### Trivial

- The paper mentions prompt differences across Classic/Mystery/Random variants for TMK (§3.1.4) and notes that PlanBench prompts themselves evolved — this is an acknowledged confound. The paper's transparency on this point is appreciated, but the issue is not resolved.

---

## Nice-to-Haves

- **Information-content control experiment** (as described above under Major weaknesses): Provide the same domain knowledge in a flat non-TMK format (plain paragraph, simple JSON without decomposition) and show that TMK outperforms it. This is the single most important experiment that would strengthen the paper.
- **Ablation of TMK components**: Test TMK without the Knowledge section, or without teleological goal-method links, to isolate which part of the structure drives gains.
- **Qualitative examples** showing o1's reasoning traces under plain text vs. TMK on the same Random Blocksworld problem, to illustrate whether the model actually uses the TMK structure.
- **Test on at least one additional PlanBench domain** (e.g., Logistics) to establish generality beyond Blocksworld.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"The exact JSON used for each domain variant is not given in the main text (presumably in appendix, which is stripped)"** — Removed per instructions: appendices are stripped by the parser; they exist in the original submission.
- **"The paper omits that some PlanBench results in Valmeekam (2023) include CoT baselines"** — The paper's claim is about the specific PlanBench leaderboard results it compares against, not about all PlanBench experiments in the literature. Minor inaccuracy in the reviewer's characterization.
- **"The critique of CoT and ReACT is reasonable but incomplete"** — Generic observation, not a concrete weakness.
- **"The paper would need to probe model internals, analyzing token embeddings, internal activations"** — Unrealistic methodological expectation for a prompting paper; moved to nice-to-have.
- Various formatting/style nitpicks and generic criticisms.

---

## Novel Insights

The most interesting observation in the reviews — one that goes beyond the paper's own contributions — is the tension between the paper's striking empirical results and the uncertainty about their cause. The 97.3% accuracy on Random Blocksworld is not in doubt, but whether it stems from TMK's specific hierarchical-teleological structure, from the JSON formatting activating code-execution pathways, from simply providing more complete domain information, or from a combination of factors, is entirely unresolved. This highlights a broader methodological challenge in the LLM prompting literature: a "prompt" is a high-dimensional intervention, and attributing improvement to any one of its features requires careful factorial design that most papers (including this one) do not provide. The paper's performance inversion is a step in the right direction (it argues against a pure "more information" hypothesis), but the absence of a proper information-content control means the paper cannot distinguish between rival explanations.

---

## Suggestions

1. **Run the information-content control experiment.** Express the same domain knowledge (same preconditions, effects, parameters, concepts) in a flat JSON or structured paragraph that does *not* follow TMK's task-method-knowledge decomposition. If TMK still outperforms this control, you have evidence for the structural hypothesis. If not, the contribution needs reframing.
2. **Re-run all baselines with the same extraction pipeline** used for TMK results, and report them alongside the TMK numbers. Include one-shot plain-text results (already collected per the OSF link) explicitly in the main table.
3. **Add CoT and ReACT baselines** evaluated under identical conditions (same extraction, same models, same problems). The literature you cite suggests they underperform, but demonstrating this directly in your setup would meaningfully strengthen the paper.
4. **Report variance.** Run each condition at least 3 times and report means with standard deviations or confidence intervals.
5. **Add an ablation study** removing one TMK component at a time (e.g., remove Knowledge section, flatten the task-method hierarchy) to identify what drives the gains.
6. **Tone down mechanistic claims.** The evidence does not yet support strong claims about "code-execution pathways" or "symbolic steering" as the causal mechanism. Frame these as hypotheses consistent with the data rather than conclusions.

---

## Score and Decision

**Calibration anchors** (all from the human reviews corpus):

| Path | Avg Human Score | Comparison |
|---|---|---|
| `/home/wg25r/review_agent/human_reviews_2026/WIXohR7mEo.md` | 6.00 (Accept Poster) | ACPBench Hard benchmark paper with comprehensive 15-model evaluation but limited prompting strategies. My paper has a more novel approach but weaker experimental methodology. |
| `/home/wg25r/review_agent/human_reviews_2026/TS9BsfzjOJ.md` | 5.00 (Reject) | Multi-token prediction for planning; mixed reviews (2,6,8,4). Similar pattern of interesting idea + incomplete evaluation. Rejected. My paper has more striking results but similar methodological concerns. |
| `/home/wg25r/review_agent/human_reviews_2026/FKhMrV1nvz.md` | 4.50 (Reject) | Instruction tuning for planning (94% accuracy). Rejected for limited baselines and missing comparisons. My paper has comparable strengths and weaknesses. |
| `/home/wg25r/review_agent/human_reviews_2026/oBlaD4PCej.md` | 5.00 (Reject) | VLM-as-formalizer for planning. Systematic comparison but limited novelty. My paper has more novelty but weaker baselines. |
| `/home/wg25r/review_agent/human_reviews_2026/HRH9m3MWYT.md` | 3.50 (Reject) | BabyAI planning benchmark. Infrastructure contribution; limited insight. My paper has a stronger conceptual contribution. |
| `/home/wg25r/review_agent/human_reviews_2026/LOqTK59rxd.md` | 2.00 (Reject) | Cut-based reprompting for planning. Severely flawed: unclear claims, flawed theory, very limited experiments. My paper is significantly stronger. |
| `/home/wg25r/review_agent/human_reviews_2026/VKGTGGcwl6.md` | 8.00 (Accept Oral) | Multi-turn conversation. Different area, but shows the quality bar for strong acceptance. My paper does not meet this bar. |

**Score rationale**: The paper introduces a genuinely novel and well-motivated prompting approach with striking empirical results (97.3% on Random Blocksworld). However, two major methodological gaps — the missing control for information content vs. structure, and the baseline comparison confounds (different shot count, different extraction pipeline) — prevent the paper from establishing its core claims about TMK as a "symbolic steering mechanism." These are fixable with additional experiments, but in the current form the paper does not meet the acceptance bar. Compared to calibration anchors, the paper sits between the 5.0 and 4.5 rejected papers — interesting idea, compelling preliminary results, but insufficiently rigorous evaluation.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>