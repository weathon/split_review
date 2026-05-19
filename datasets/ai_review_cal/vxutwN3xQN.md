- Decision: Reject
- Avg Score: 6.00
- Scores: 6, 6, 6, 6
Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

---

## Summary

MJ-Bench is a benchmark for systematically evaluating multimodal reward models (judges) used in text-to-image generation. It constructs a human-verified preference dataset covering four perspectives—text-image alignment (5 sub-objectives), safety (toxicity/NSFW with subtypes), quality (distortion/blur), and bias (occupation/education with demographic dimensions)—and evaluates 15+ judges including CLIP-based scoring models, open-source VLMs, and closed-source VLMs. The evaluation is further validated by fine-tuning SD-1.5 using judge feedback and obtaining human rankings. Key findings include that GPT-4o generally outperforms other judges, CLIP-based scoring models are competitive on alignment/quality, and VLMs perform better on safety/bias.

## Strengths

- **Comprehensive multi-perspective preference dataset with human-verified subcategories.** The dataset systematically covers alignment (object, attribute, action, spatial, count), safety (toxicity with 3 subtypes, NSFW with 3 subtypes), quality (distortion, blur), and bias (occupation with 5 demographic dimensions, education with 3 dimensions), with all preference pairs validated by human experts (Section 2.2, Figure 2). This provides structured, fine-grained evaluation that goes beyond prior benchmarks like DecodingTrust.

- **Cross-validated evaluation combining automatic metrics with human rankings of downstream fine-tuned models.** The paper evaluates 15+ judges on the preference dataset, then fine-tunes SD-1.5 using feedback from the top-6 judges via two RLAIF algorithms (DPO and DDPO), obtaining human evaluator rankings that confirm the same overall trends (lines 129–131, 152–156). This end-to-end validation ensures the benchmark's conclusions reflect real-world alignment utility.

- **Systematic analysis of feedback scale and input mode effects on judge accuracy.** The paper compares Likert-scale, numerical [0–5], [0–10] scales and single-image vs. multi-image input modes, finding that Likert scale improves open-source VLM accuracy while closed-source VLMs are more consistent across scales (lines 159–170). This provides actionable guidance for deploying VLMs as reward models.

- **Novel bias evaluation framework using three complementary fairness metrics.** The paper proposes ACC (pairwise reward equality), GES (Gini-based equality), and NDS (normalized dispersion) to quantify demographic bias in reward models (Section 2.3, line 127), going beyond win-rate by measuring both pairwise consistency and score distribution equality across demographic groups.

## Weaknesses

### Fatal

None.

### Major

- **Curation confound in the alignment subset.** The alignment dataset is constructed by using LLaVA-NeXT-34B to *select preference pairs* from public datasets, followed by human verification (line 94). The problem is that the selection mechanism is non-random: it retains examples where LLaVA's own judgments distinguish between two images. This creates a test set that is correlated with LLaVA's decision boundary. Since the paper later evaluates LLaVA-family models (LLaVA, LLaVA-improved, LLaVA-NeXT) on this same data and compares them against CLIP-based scoring models and closed-source VLMs (line 148), any conclusions about relative performance on alignment—especially the finding that "CLIP-based scoring models can provide better feedback than open-source VLMs regarding text-image alignment" (line 39)—could be affected by selection bias. Human verification fixes label errors but does *not* fix sample composition bias. The paper should either (a) demonstrate that the selected pairs are not biased toward any particular VLM family, or (b) use a robustness check with an alternative curation method. This primarily affects the alignment subset (one of four perspectives), and the human evaluation of fine-tuned models provides a partially independent validation, but the confound should be explicitly addressed.

### Minor

- **Bias metrics cannot distinguish unbiased from uninformative judges.** The three bias metrics (ACC, GES, NDS, defined at line 127) all measure *equality* of scores across demographic groups. A judge that returns the same score (e.g., 0.5) for every image regardless of demographics or occupation would achieve perfect scores on all three metrics (ACC=1.0, GES=1.0, NDS=1.0) but is completely uninformative for the actual task. In practice, the evaluated judges are also tested on the preference dataset, so degeneracy is unlikely, but the paper never reports even a sanity-check baseline (e.g., "does the judge discriminate occupation-relevant features at all?"). The bias metrics should be interpreted as measuring score *equality*, not task-appropriate fairness, and this limitation should be stated explicitly.

- **No statistical significance or confidence measures for key comparisons.** The main accuracy results (Table `exp:main_result`, human evaluation Tables 3–4) report point estimates without confidence intervals, standard errors, or significance tests. The claim that GPT-4o "outperforms other judges on average" (line 7)—how large is the gap relative to likely variance? For a benchmark meant to guide practitioner decisions, users need to know whether a few percentage point advantage is meaningful or within noise. Bootstrap confidence intervals or per-subcategory variance should be reported.

- **Dataset size and inter-annotator agreement not transparent in the main text.** The distribution bar chart (Figure 3) shows proportions, but the total number of examples per perspective is not stated in the main body (line 88 defers to the appendix). Similarly, the paper states that "human experts" verify each pair (line 65) but does not report how many annotators, their agreement rate, or the verification protocol. Both figures are standard for benchmark papers and affect how much trust readers can place in the gold labels.

- **Potential artifacts from image editing in bias and NSFW data construction.** The bias dataset uses image editing to vary demographic attributes (line 118), and the NSFW "chosen" images are produced by inpainting over inappropriate regions (line 104). Both techniques can introduce subtle visual artifacts (lighting inconsistencies, boundary artifacts, semantic inconsistencies) that a judge might detect, producing spurious score differences that could affect evaluation fidelity. Human verification addresses label correctness for preference pairs, but for the bias data (where there is no ground-truth preference, only an equality expectation), similar verification is not described. The paper should acknowledge this risk and ideally provide evidence that the edits are imperceptible or control for editing quality.

- **Some findings stated without supporting numbers in the main text.** For example, the claim that "PickScore-v1 consistently exhibits better accuracy and can distinguish chosen and rejected images by a larger margin" (line 174) is stated qualitatively, with supporting figures deferred to the appendix. The main text should include key numbers for such comparative claims.

### Trivial

- **Clarification on tie handling for VLM judges.** The paper discusses tie thresholds for scoring models (line 125, Figure `fig:score_model_w_tie`) but does not fully explain how ties are defined for VLMs that output discrete scores (e.g., Likert categories), where the concept of a "margin" is less natural.

## Nice-to-Haves

- **Expand the human evaluation to include a lower-performing judge.** The human evaluation currently tests only the top-6 judges. Including at least one low performer identified by the benchmark would demonstrate that the benchmark can *predict failures*, not just rank successes, significantly strengthening the validation claim.
- **Add a calibration check for the bias evaluation.** For each occupation, verify that judges assign higher scores to demographic groups statistically associated with that occupation (not to enforce stereotypes, but to confirm that judges are actually engaging with the occupation concept rather than outputting constant scores).
- **Run a robustness check on the alignment subset curation.** Replace the LLaVA-filtered alignment pairs with a version curated without VLM filtering (e.g., random sampling with only human labeling) and check whether judge rankings change. This would directly address the main structural concern.

## Removed Points

These points were raised by the reviewers but are removed or moved here with justification:

1. **Concerns about missing appendix content / appendix-stripped proofs** — REMOVED. The extraction parser strips appendices from all papers; the original submission contains them. Per instructions, these are not valid weaknesses.
2. **Concerns about missing related works** — REMOVED. Per instructions, the reviewer cannot confirm missing citations without external knowledge.
3. **Formatting/style nitpicks (typos, grammar, punctuation, whitespace)** — REMOVED. These are parser artifacts, not author errors.
4. **Criticism that "PickScore-v1 consistently exhibits better accuracy... stated without numbers" as a standalone complaint** — MERGED into Minor weakness #6 above (some findings lack supporting numbers in main text). The corresponding results exist in the appendix.
5. **The "Strengthening the Paper on Its Own Terms" section from the Harsh Critic** — MOVED to Nice-to-Haves. These are constructive suggestions, not weaknesses.
6. **Generic concern that "the evaluation lacks rigor" without a specific anchor** — REMOVED. This is area-category noise without a concrete, verifiable anchor point in the paper.

## Novel Insights

The reviews collectively surface a tension that the paper itself does not fully address: using a specific VLM (LLaVA-NeXT-34B) to scaffold dataset construction while later evaluating that same VLM family creates a potential self-validating loop in the alignment subset. This is a structural and methodological observation—not about the paper's honesty, but about a subtle form of benchmark contamination that can arise when the same model family serves as both data curator and evaluee. The reviews also correctly note that the bias evaluation metrics, while novel, are incomplete without a task-accuracy floor that verifies the judge is actually performing the requested discrimination. These two insights—(1) dataset curation models can imprint their own inductive biases on the evaluation of other models, and (2) equality metrics need a companion accuracy anchor—are valuable beyond this specific paper and apply to the broader practice of building evaluation platforms for reward models.

## Suggestions

1. **Address the curation confound directly.** Either (a) report a robustness study where the alignment subset is re-curated without LLaVA filtering (e.g., random sampling from the public datasets with human-only labeling) and show that judge rankings are unchanged, or (b) demonstrate via analysis that the selected pairs are not differentially easier for LLaVA-like models.
2. **Add a sanity-check baseline for bias metrics.** Report whether each judge's scores for an occupation actually distinguish different demographic groups from a null distribution (e.g., by comparing real scores against scores on a matched random-input baseline). A simple check: does the judge give different scores to images of people in different occupations at all?
3. **Report confidence intervals or bootstrap estimates** for all key accuracy numbers, particularly for comparisons involving the top-performing judges (GPT-4o vs. others) where gaps may be small.
4. **Provide the total N per perspective and inter-annotator agreement statistics** in the main paper, not only in the appendix.
5. **Explicitly discuss the risk of image-editing artifacts** in the bias and NSFW subsets, and ideally report a control experiment showing that editing quality does not systematically affect judge scores.
