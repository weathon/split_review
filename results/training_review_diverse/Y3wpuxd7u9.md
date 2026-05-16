Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

GoLLIE proposes fine-tuning a CodeLLaMA-based LLM to follow annotation guidelines for zero-shot Information Extraction (IE). The key idea is to represent IE schemas as Python classes with docstrings (guidelines) and annotations as executable lists, then train the model with regularization techniques that force it to attend to the guidelines rather than memorize label names or datasets. Evaluated on 17 unseen IE tasks, GoLLIE (7B) achieves 55.3 average F1, outperforming the same-backbone baseline without guidelines (42.3) and prior SoTA (Instruct-UIE, 42.6). The ablation identifies representative annotation candidates as the critical component.

## Strengths

1. **Clear and significant zero-shot gains over the same-backbone baseline.** The 13.0 F1 improvement (Table 2, 55.3 vs. 42.3) cleanly demonstrates that fine-tuning to follow guidelines provides substantial benefit, holding the model architecture, training data, and all other factors fixed. This is the paper's strongest and most controlled result.

2. **Ablation study cleanly isolates the key ingredient.** Removing representative annotation candidates drops zero-shot F1 from 55.3 to 49.9 (p=2.2e-10), while removing all guideline information drops it to 42.3 (p=5.1e-13) (Table 3). This rigorous decomposition validates the design intuition that concrete annotation examples in the guidelines are critical.

3. **Python code-based representation is a practical design choice.** Representing schemas as classes with docstrings and output as executable Python lists (Section 3.1, Figure 2) leverages code pretraining, unifies diverse IE tasks (NER, RE, EE, EAE, SF) under one format, and makes parsing trivial via code execution. This is a clean engineering contribution.

4. **Honest error analysis with concrete failure modes.** The paper systematically examines where GoLLIE succeeds (polysemous labels like Media, Vulnerability Patch) and fails (ambiguous Miscellaneous categories, conflicts between fine/coarse entities, strong label preconceptions from pretraining). This provides a grounded understanding of the method's limitations rather than glossing over them.

## Weaknesses

### Fatal
None.

### Major

1. **Guideline creation from evaluation-data dev splits compromises the strictness of the zero-shot evaluation.** The paper states that "when such guidelines are not publicly available, we ask human experts to create them, based on the annotations from the development split" (§ Experimental Setup, line 137). For zero-shot evaluation datasets where official guidelines did not already exist, human experts wrote guidelines informed by the dev-split annotations of those same datasets. The model then receives these guidelines at test time. While this does not constitute direct data leakage (the model never sees target examples), it means the guidelines encode dataset-specific annotation conventions (e.g., whether pronouns count as Person, whether years are labeled as Time) that were derived from the evaluation data's own distribution. This departs from a strict zero-shot protocol where the model should have no information about the target annotation scheme beyond label names.

   **Why this matters:** The claim of "zero-shot" generalization to unseen schemas is weakened if the guidelines used at inference were themselves crafted with knowledge of those schemas' annotations. The paper does not provide a per-dataset breakdown of which zero-shot datasets had pre-existing official guidelines and which had guidelines created post-hoc from the dev split, making it impossible for the reader to assess which evaluations are affected.

2. **Evaluation metrics are not specified for most tasks, hindering reproducibility and fair comparison.** The paper specifies metrics only for CASIE (partial matching for arguments, line 135). For NER on CrossNER, MultiNERD, FabNER, etc., the paper never states whether exact span match, partial span match, or token-level F1 is used. Since Table 2 compares GoLLIE against prior SoTA numbers (Instruct-UIE, PromptNER, etc.), the reader cannot verify whether the same metric was used across systems. If GoLLIE uses a more lenient criterion, the reported gains could be partially artifactual.

### Minor

1. **Label overlap between training and evaluation datasets inflates the zero-shot numbers, and the per-dataset breakdown for unseen labels is absent.** The paper acknowledges this overlap (lines 254–255) and provides an aggregate seen/unseen comparison in Figure 2. However, this figure is relegated to a small wrapfigure with no exact F1 numbers. The reader cannot tell, for example, whether the strong result on MultiNERD (76.0) is driven by seen labels or truly reflects generalization to novel labels. A table with per-dataset seen/unseen F1 scores would be far more informative.

2. **The baseline definition (no guidelines) is underspecified.** The paper defines the baseline as "the model without guidelines" (line 80), but it is not stated whether this baseline receives class definitions (without docstrings) or just label names. Figure 3 (an image) suggests the baseline gets class names only, but this should be explicit in the text. The baseline sets the bar for the entire contribution, so clarity here is important.

3. **Statistical test for ablation p-values is not specified.** The paper reports one-sided p-values (line 297) but does not state which test (e.g., paired bootstrap, permutation test) was used. The "w/o Shuffling" row shows a *higher* score (55.9 vs. 55.3) with p=0.072, which the paper correctly notes as non-significant. However, the lack of test specification makes the other significant results (Dropout, Candidates) harder to fully evaluate.

4. **Data modifications to Ontonotes 5 and TACRED are not quantified.** The paper says Ontonotes 5 training data was "reduced drastically" and TACRED was converted from RE to SF (line 135), but provides no numbers. This limits the reader's ability to assess the comparability of these supervised results.

5. **Figure 1's caption is vague.** "GPT results are not available for all domains" does not clarify which domains are covered, which are missing, and why. Since this figure is used to motivate the paper, the incompleteness should be explained.

### Trivial
- The "w/o Shuffling" result (55.9) being non-significantly higher than the full model (55.3) mildly undercuts the motivation for including this regularization, though the paper does acknowledge it.

## Nice-to-Haves
- A table showing per-dataset F1 on the strictly unseen label subset (separate from seen labels) would directly test the claim of generalization to new schemas.
- A limitations paragraph discussing the requirement for high-quality guidelines and the practical scenarios where such guidelines might or might not be available would strengthen the paper's honesty.
- A per-dataset breakdown of which zero-shot evaluation datasets had pre-existing official guidelines vs. post-hoc created guidelines from the dev split.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism about SoTA column mixing methods without indication**: The SoTA column in Table 2 has clear citations per entry (e.g., \citep{DBLP:journals/corr/abs-2304-08085}). The paper is sufficiently transparent. Removed as factually inaccurate.
- **"Label overlap inflates zero-shot results" framed as a fatal flaw**: The paper acknowledges and partially addresses this with Figure 2 (seen vs. unseen). The remaining concern is about presentation (exact numbers, per-dataset), which is moved to Minor.
- **"Guideline sourcing is a structural flaw that cannot be fixed"**: The paper discloses the practice. While a valid concern, the framing as an unfixable structural flaw is overstated — even with this concern, the controlled comparison against the same-backbone baseline remains valid, and the concern can be addressed with better transparency and re-evaluation on strictly pre-existing guidelines. Downgraded from "fatal" to Major.
- **Error analysis described as purely anecdotal**: The paper provides a systematic table (Table 4) with label-level F1 scores and categorizes failure modes. This is a reasonable error analysis for an empirical paper. Moved to Removed Points as incorrect.
- **Demand for a "dedicated appendix paragraph" for metric definitions**: Not having a dedicated paragraph is a minor clarity issue, not a fatal omission. Already covered in Minor weakness #2.
- **"Run controlled zero-shot using only publicly available guidelines" as a required action**: This is a strengthening suggestion, not a weakness. Moved to Nice-to-Haves.

## Novel Insights

None beyond the paper's own contributions. The review process confirms the paper's main findings while highlighting the need for greater transparency in the evaluation protocol.

## Suggestions

1. Add a supplementary table specifying, for each zero-shot evaluation dataset: (a) whether official guidelines existed prior to this work or were created from the dev split, (b) the exact evaluation metric used (exact span match, partial match, etc.), and (c) F1 on the strictly unseen label subset per dataset.
2. Explicitly state in §3.2 what information the baseline receives (label names only? class definitions without docstrings?).
3. Specify the statistical test used for p-values in the ablation.
4. Clarify the Figure 1 caption to state which domains GPT results cover and why others are missing.

## Score and Decision

Assign a score based solely on your assessment of the paper's quality after review.

The paper makes a genuine contribution: showing that fine-tuning an LLM specifically to follow annotation guidelines yields substantial zero-shot IE gains, with a clean ablation identifying the key component. The code-based representation is practical and well-designed. The error analysis is honest and informative.

However, the zero-shot evaluation is partly compromised by the creation of guidelines from evaluation-data dev splits for datasets without pre-existing guidelines, and the evaluation metrics are underspecified. These issues do not invalidate the core claims (the controlled baseline comparison is robust), but they do weaken the comparison against prior SoTA (Instruct-UIE) and limit the strictness of the zero-shot claim.

The paper is solid but has real methodological concerns that need addressing. It should be accepted contingent on these being resolved in the final version.

Score: 6.5
Decision: Accept

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>