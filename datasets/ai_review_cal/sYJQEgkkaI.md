- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 6, 5
Now I have a solid understanding of the paper and all the reviewer claims. Let me compose the final consolidated review.

## Summary

This paper identifies a key limitation in Representation Engineering (RepE) — the implicit assumption that LLMs consistently follow assigned role instructions during neural activity collection — and proposes CARE, a method that uses content moderation models (Llama Guard-2) to filter out stimulus pairs where the model's behavior contradicts the assigned role. By ensuring that only pairs with genuinely opposite behaviors (safe vs. unsafe) are used for training, CARE aims to produce steering vectors that more reliably control model behavior. Results on ALERT safety subsets with Llama-3 8B show improved manipulation scores compared to baselines while maintaining faithfulness.

## Strengths

1. **Identifies a real and underappreciated limitation of RepE.** The paper demonstrates empirically (Figure 2) that RepE accuracy degrades substantially when the model exhibits behavior inconsistent with the assigned role, and that control outcomes are sensitive to the stimulus set. This is a genuinely useful critique that prior RepE work has not systematically addressed.

2. **Simple, practical, and low-cost fix.** Using an off-the-shelf content moderation model to filter inconsistent stimulus pairs is elegant in its simplicity. It requires no additional training, human annotation, or model modification, making it immediately usable by practitioners (Section 3.1).

3. **Consistent quantitative improvements in controllability.** The aggregate results (Figures 4-5) show CARE achieving higher median and IQM manipulation scores with narrower confidence intervals than both BASE and PAIR baselines across all datasets. On Suicide & Self-Harm and Weapons & Regulated Substances, CARE achieves near-100% manipulation success (unsafe) (Section 5.2).

4. **Introduces causality-grounded evaluation metrics for RepE.** The manipulation and termination scores (Section 3.4), inspired by neuroscience paradigms for establishing causality, are a meaningful addition beyond the faithfulness metrics (accuracy, precision) used in prior RepE work. Even though termination scores are low, reporting them honestly is a strength.

## Weaknesses

### Fatal
None.

### Major

1. **Same content moderation model used for filtering, labeling, and evaluation — circularity concern unaddressed.** Llama Guard-2 is used to (a) filter training stimulus pairs, (b) label neural activity data for training the linear model, and (c) evaluate manipulation/termination success. If Llama Guard-2 has systematic biases (e.g., classifying outputs as safe when the instruction is safe), both the filtering step and the evaluation metric could reflect alignment with the classifier's regularities rather than genuine behavioral change in the model. The paper acknowledges this in the conclusion (line 162: "this may unintentionally amplify some inherent biases of the moderation model") but does not provide any experimental cross-check. A validation using a different classifier (e.g., Llama Guard 3, GPT-4 as annotator, or a small-scale human sample on a random subset) is needed to establish that the improvement reflects genuine behavioral control, not evaluation artifact. This is the most significant evidential gap.

2. **Causal framing of the filtering step is overstated.** The paper describes the matched-pair trial design as "remov[ing] the edge from confounding factors to the treatment variable in the causal graph" (line 43) and claims the method "isolate[s] the impact of confounders on neural activities and model behaviors" (abstract). In reality, the filtering step conditions on the *outcome* (model behavior) to select training data — it removes noisy/contradictory instances. This is a sensible preprocessing step that improves the signal in the training data, but it is not a causal identification strategy in the standard sense (where matching on covariates precedes outcome observation, and treatment is randomized within pairs). The actual causal evidence comes from the intervention evaluation (manipulation/termination), not from the training data selection. The paper should reframe the filtering step as "data cleaning to ensure training instances reflect the intended behavioral contrast" rather than as a "principled causal framework."

### Minor

1. **Only one base LLM (Llama-3 8B) tested, and only safety behaviors evaluated.** The paper claims applicability to "a wide range of cognitive functions and complex behaviors" (line 162) but provides evidence only for safety on one model. Safety is a domain where role instructions are relatively unambiguous; the method's transfer to more ambiguous dimensions (honesty, power-seeking) is untested. The paper acknowledges this limitation, but it tempers the generality of the contribution.

2. **Filtering rate (number of pairs removed) not reported.** The entire method hinges on filtering out inconsistent stimulus pairs, yet the paper never reports what fraction of pairs are removed. If only 5% are filtered, the improvement comes from a small change; if 80% are filtered, the effective training set shrinks substantially, which could affect generalization. This is essential practical information missing from the experimental setup.

3. **Unclear which linear approach (PCA/DM/LR) is used for the main results.** Section 5.1 describes PCA, DiffMean, and Logistic Regression as candidate linear approaches, but the main results (Section 5.2) never specify which one is used. If all three are evaluated and CARE works for all, that strengthens the claim; if only one is used, that should be stated. This omission weakens experimental transparency.

4. **Baseline naming is confusing.** The paper says "The original RepE implementation lies between these two baselines" (line 117), but PAIR (paired stimuli + role-based pseudo-labels) appears to *be* the original RepE (Zou et al., 2023). If PAIR is the original RepE, it doesn't "lie between" — it is one of the two comparison points. This is a minor clarity issue.

### Trivial
None.

## Nice-to-Haves

- **Deeper analysis of low termination scores.** The paper correctly reports that termination scores are low (line 138-139), but a more systematic investigation — e.g., checking whether the projection removal is too aggressive, or whether it affects unrelated behaviors — would deepen the contribution. This is in the same direction the paper is already heading.
- **Results on a second model family** (e.g., Mistral, or a smaller Llama variant) would strengthen generality claims without changing scope.
- **Concrete examples of filtered vs. retained stimulus pairs** would help readers understand the method's behavior in practice.

## Removed Points

- **"Missing direct RepE baseline" (from Harsh Critic):** Removed because PAIR (paired stimuli + role-based pseudo-labels) *is* effectively the original RepE; the comparison is between CARE and what the original RepE does. The naming confusion is retained as a Minor weakness above, but the claim that an entire baseline is missing is not supported.
- **"OOD experiment not fully detailed":** Removed because the OOD results may be present in embedded figures/tables not extractable from the parsed text; the claim cannot be verified.
- **"Selection of stimulus pairs not fully specified":** Removed because the paper does describe the method: "assign opposite roles in the instructions" (line 48) on the ALERT benchmark stimuli. The description, while not exhaustive, is sufficient for the paper's level of methodological exposition.
- **"Suspiciously high 100% manipulation scores" (speculative artifact):** Removed because this is speculation without evidence; the scores are reported and the paper honestly reports low termination scores alongside.
- **Strength Finder strengths about "importance of the problem" or generic framing:** All six strengths from the Strength Finder are retained as they are concrete, specific to the paper, and grounded in evidence.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the circularity concern as the most critical evidential gap and identify the tension between the paper's strong causal framing and what the method actually achieves (data cleaning), but these are critical observations about the paper's presentation rather than novel scientific insights.

## Suggestions

1. **Address the circularity concern experimentally.** The single highest-impact revision would be to validate manipulation scores using a different content moderation model (e.g., Llama Guard 3, or GPT-4 as annotator) or a small human evaluation on a random subset of generated responses. This directly addresses the most significant evidential gap.

2. **Reframe the matched-pair trial language.** Replace claims about "removing the edge from confounding factors" (line 43) and "isolating confounders" (abstract) with more precise language: the filtering step ensures that training instances reflect genuine behavioral contrast, reducing noise in the neural activity data. The causal evidence comes from the *intervention* evaluation, not from the data selection method.

3. **Report the filtering rate.** Add a simple table or note showing, for each dataset, how many stimulus pairs were initially constructed and how many were retained after filtering.

4. **Specify which linear approach is used for main results.** State clearly whether PCA, DM, or LR is used for the primary results in Section 5.2, and ideally show results for all three.

5. **Clarify the baseline relationship.** Either state that PAIR is the original RepE implementation, or explain how it differs and why the original RepE "lies between."
