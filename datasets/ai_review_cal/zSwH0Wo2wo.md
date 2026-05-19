- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 3, 8, 5
Now I have a thorough understanding of the paper. Let me write the final consolidated review.

---

## Summary

This paper introduces a three-stage framework (Explore, Establish, Exploit) for automated red-teaming of language models when the red team does not start with a pre-existing classifier of harmful outputs. The framework is demonstrated in two settings: eliciting toxic text from GPT-2-xl (achieving a ~30× increase in toxicity rate) and eliciting false statements from GPT-3-text-davinci-002 (increasing the classifier-marked false rate from 30% to 74%). The paper also introduces a diversity reward to prevent mode collapse in RL-based prompt generation and constructs the CommonClaim dataset of 20,000 human-labeled statements.

## Strengths

1. **Well-structured framework for a practical problem.** The Explore/Establish/Exploit pipeline directly addresses a realistic gap in prior red-teaming work: most methods assume a pre-existing classifier, but in practice red teams often need to define and measure the target behavior from scratch. The three-step framing cleanly separates exploration, measurement construction, and exploitation.

2. **Diversity reward ablation is clean and convincing.** The paper demonstrates that without the cosine-distance diversity term, the prompt generator collapses to repetitive, ineffective prompts (e.g., 0% toxic rate for GPT-2-xl; the same prompt appearing in 61/100 samples for GPT-3). With the diversity term, toxicity rises to 31% and prompt topics are varied. This is a genuine methodological contribution validated by controlled ablation.

3. **Contextual vs. generic classifier comparison demonstrates the framework's value.** The CREAK control is a strong experiment: a classifier trained on a pre-existing binary true/false dataset is substantially easier to game (95% false-classification rate, but completions are toxic/nonsensical rather than false). In contrast, the CommonClaim classifier (with three labels including "neither" and trained on target-model data) produces adversarial prompts focused on political misinformation topics. This provides concrete evidence that contextual red-teaming (the paper's central thesis) matters.

4. **CommonClaim dataset is a useful resource.** The 20,000 examples with three-label human annotations (true/false/neither by common knowledge) and two independent labels per example is a genuine contribution. The "neither" category addresses choice-set misspecification that plagues binary factual-claim datasets.

5. **ChatGPT-label comparison is insightful.** The finding that classifiers trained on ChatGPT-3.5-turbo labels (rather than human labels) produce a hackable reward signal strengthens the argument that human judgment is key to the Establish step, and also provides practical guidance for practitioners.

6. **First demonstration of automated red-teaming for false text at scale.** While the evaluation has limitations (discussed below), the paper presents a working end-to-end pipeline that discovers prompts eliciting politically-themed completions classified as false — a task not previously demonstrated with automated methods.

## Weaknesses

### Fatal
None.

### Major
1. **No human evaluation of false-text adversarial outputs.** This is the paper's most significant weakness. The claim "we successfully elicited false statements from GPT-3" is supported primarily by the *same classifier* used as the RL reward signal (44% accuracy on `false`, 19% on `neither`), not by human validation of the generated adversarial completions. The qualitative examples in Table 6 are about political topics but are not verified as false. The paper argues that "accuracy is not important, but rather the ability of the classifier to provide a suitable reward signal" — this is a reasonable methodological stance for the framework-level contribution, but it leaves the stronger claim ("first work to elicit false text at scale") under-supported. Human annotation of even a few hundred adversarial completions (computing e.g., precision/false-discovery rate) would substantially strengthen the paper's headline result.

   *Why this is major, not fatal:* The paper's core framework-level contribution does not collapse without this validation. The toxicity experiment (using a well-established classifier) independently validates the pipeline. The CREAK comparison still demonstrates the value of contextual classification. However, the paper's strongest claim about false-text red-teaming is weakened by the absence of this validation.

2. **Low classifier accuracy on key classes is hand-waved.** The CommonClaim classifier achieves only 44% accuracy on `false` and 19% on `neither` in the validation set (line 186). The paper asserts these numbers don't matter because the classifier must only provide a suitable reward signal, but this assertion is not backed by analysis. For example, the paper could analyze whether classifier errors correlate with annotator disagreement, or show that despite low per-class accuracy, the ranking of completions by classifier score correlates with human judgment. As written, the reader cannot assess whether the 30%→74% increase in false-classification rate reflects actual falsehood discovery or systematic bias in the noisy classifier.

### Minor
1. **Diversity is not quantitatively measured.** The paper demonstrates that the diversity reward prevents mode collapse (0%→31% toxic rate in the toxicity experiment), which is compelling. However, it does not quantify diversity itself (e.g., embedding variance, n-gram diversity, cluster counts). A quantitative diversity metric would strengthen the methodological contribution and allow comparison across runs.

2. **Switch from internal activations to ada-002 embeddings is not discussed.** The Explore step for GPT-2-xl uses last-token internal activations; for GPT-3 (where activations are unavailable via API), the paper switches to ada-002 embeddings. The paper notes this change but does not discuss whether the embedding quality difference affects the diversity of the sampled outputs. This is a minor methodological gap.

3. **Only 2 RL runs per condition with no variance reporting.** Key numbers (toxic rate, false-classification rate) are reported as averages across 2 runs with no confidence intervals, standard deviations, or per-run breakdowns. This makes it impossible to assess the stability of the results.

### Trivial
- The paper claims its approach is "inherently competitive with simply using a pre-existing classifier to filter training data and/or model outputs" (line 321), but this claim is a logical argument, not an empirical demonstration. This is a framing issue, not a technical flaw, and the logical argument is reasonable.

## Nice-to-Haves

- **Human evaluation of a random sample of adversarial completions** from the false-text experiment (addressing the major weakness above). Even a few hundred labels would allow the paper to report precision and compare against the Explore-step baseline.
- **Testing the filtering baseline empirically:** taking the discovered adversarial prompts and checking whether filtering model outputs with the CommonClaim classifier would block them would directly substantiate the claim about being "competitive with filtering."
- **Quantifying prompt diversity** (embedding variance, n-gram diversity, etc.) rather than only reporting mode collapse as a binary outcome.
- **Comparison with additional factual-claim datasets** (e.g., TruthfulQA, FEVER) beyond CREAK would strengthen the generality of the finding that generic classifiers are more hackable.

## Removed Points

- **Criticism about missing appendix details** (labeling instructions, contractor selection, CREAK experiment examples, ChatGPT ablation details). The parser strips these sections from all papers; they exist in the original submission and are cited in the main text.
- **"The 'filtering baselines' argument is compelling but never empirically tested"** treated as a missed opportunity. This is framed as a "missed opportunity" in the harsh review, not a weakness. The paper's claim is logical/theoretical, not empirical. Moved to Nice-to-Haves.
- **Criticism that the paper overstates the framework's findings** ("we have found that red-teaming is possible and can even be more effective when done from scratch"). The paper's evidence (CREAK comparison, diversity ablation, toxicity experiment) supports this claim. The phrase "more effective" is justified by the CREAK control showing that the contextual classifier is harder to game.
- **Criticism about no comparison with TruthfulQA/FEVER** — this is a suggestion for additional experiments, not a weakness of the paper as written. The CREAK dataset is an appropriate control (binary true/false, same format as prior work).
- **Strength Finder's generic strengths about "importance of the problem"** — these are vacuous and filtered. Only concrete, evidence-backed strengths are retained.

## Novel Insights

A genuinely novel synthesis emerges from the harsh critic's and strength finder's readings that goes beyond the paper's own claims: the paper demonstrates that **the act of constructing a classifier (not just using one) is itself a form of red-teaming.** The Establish step forces the red team to interact with model outputs, discover that "neither" is a necessary category, and confront choice-set misspecification. This is a significant conceptual contribution — red-teaming is not just about finding adversarial inputs, but about the *process of preference formation* around what counts as a failure. The paper gestures at this in the Discussion (Section 5) but does not foreground it as a core contribution. The CREAK comparison reinforces this: a pre-existing label set (true/false) fails not because the classifier is inaccurate, but because the label set itself is misspecified for the task.

## Suggestions

1. **Add human evaluation of a sample of adversarial completions from the false-text experiment.** This is the single most impactful improvement. Report precision (fraction of adversarial outputs that human annotators judge false by common knowledge) and compare against the Explore-step baseline rate. This would directly address the major weakness.
2. **Report quantitative diversity metrics** (e.g., average pairwise embedding cosine distance, number of distinct bigrams, or cluster coverage) for the adversarial prompts with and without the diversity reward.
3. **Add confidence intervals or per-run results** for the key quantitative claims (toxicity rates, false-classification rates) across RL training runs.
4. **Discuss the implications of the 44%/19% classifier accuracy** on the false-text experiment more thoroughly. For instance, analyze whether the classifier's false-positive errors correlate with annotator disagreement or whether the ranking of completions by classifier score is reasonable.
5. **Clarify the claim about "eliciting false text."** The paper currently uses "eliciting false text" and "eliciting outputs classified as false by the CommonClaim classifier" somewhat interchangeably. Explicitly distinguishing these would preempt the criticism.

---
