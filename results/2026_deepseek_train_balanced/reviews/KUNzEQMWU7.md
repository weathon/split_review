## Summary

MathVista introduces a 6,141-example benchmark for evaluating mathematical reasoning in visual contexts, assembled from 28 existing multimodal datasets and 3 newly created ones (IQTest, FunctionQA, PaperQA), with fine-grained metadata annotation across 7 reasoning types, 5 tasks, and 19 visual context classes. The paper evaluates 12 foundation models across three tiers (text-only LLMs, augmented LLMs, and LMMs) and reports that the best-performing model (GPT-4V) reaches 49.9% accuracy vs. human performance at 60.3%.

## Strengths

- **Taxonomy-driven benchmark construction covering 31 source datasets with 3 new datasets filling specific gaps**: The paper systematically identifies gaps—logical reasoning on puzzle figures (IQTest), algebraic reasoning on function plots (FunctionQA), and scientific reasoning on academic paper figures (PaperQA)—and creates new datasets to fill them (§2.2). The final benchmark spans 7 reasoning types × 19 visual context classes (Table 1), a breadth no prior single benchmark achieves. Each source dataset is capped at 400 examples for balanced representation, and the testmini/test split is validated with KL divergence 0.008 and TV distance 0.035 against the full set (§2.4).

- **Rigorous data quality assurance with 99.2% inter-annotation consistency on new collections**: Three independent reviewers annotated the 736 newly collected examples, achieving only 6 disagreements out of 736 questions, resolved through team discussion (§2.2). Additionally, automatic metadata annotation was validated against human annotation on 1,000 examples, achieving 94.1% agreement at the set level and 98.79% at the individual label level (§2.3).

- **Controlled three-tier evaluation design isolating the contribution of visual grounding**: The evaluation cleanly separates text-only LLMs (~29.2%), augmented LLMs with captions+OCR (~33.9%), and native LMMs (up to 49.9%) on the same test set (§3.3, Table 3). This design cleanly quantifies how much performance gain comes from native visual understanding versus textual descriptions of images, and is more systematic than prior work.

- **Detailed breakdown of GPT-4V performance across sub-tasks, revealing where it surpasses humans and where it falls short**: GPT-4V exceeds human performance on algebraic reasoning (53.0% vs. 50.9%), geometry problem solving (50.5% vs. 48.4%), and textbook QA (65.2% vs. 63.2%) while drastically underperforming on logical reasoning (21.6% vs. 40.7%) and numeric commonsense (20.1% vs. 53.8%) (§3.3, Table 3). This granular portrait is more informative than aggregate scores alone.

- **Qualitative analysis of Bard's errors revealing a 49.6% hallucination rate in incorrect explanations**: Human evaluation of 250 Bard predictions (§3.4) finds that 44.6% had incorrect answers, and among incorrect explanations, 49.6% involved hallucination (introduction of facts not present in the image or question). This is a concrete, actionable finding for the community.

## Weaknesses

### Major

- **The GPT-4V evaluation is non-reproducible and methodologically incomparable to the other models' evaluations, yet it anchors the paper's headline claims.** The paper states (§3.2, line 158): "Since GPT-4V does not offer API access, we resorted to manually evaluating it using the playground chatbot." The headline result—GPT-4V at 49.9%, outperforming Bard by 15.1%—rests entirely on this manual evaluation. Every other model was evaluated via a standardized automated pipeline. The manual evaluation introduces uncontrolled confounds: unknown generation parameters (temperature, system prompt), potential for re-prompting or multiple attempts, and lack of documented protocol for how questions were administered or responses recorded. The paper is transparent about the limitation, but does *not* mitigate it—no inter-evaluator reliability, no protocol disclosure, and no caveat in the abstract or conclusion that the GPT-4V comparison is preliminary. Given that this result is prominently featured in the abstract, introduction, and conclusion, the evaluation methodology significantly weakens confidence in the paper's most prominent quantitative finding.

### Minor

- **The human performance baseline has limitations that are unaddressed.** Annotators were recruited from Amazon Mechanical Turk with a minimum of a high school diploma and asked to complete 5 questions within 20 minutes (§3.2, line 220). The benchmark includes college-level and scientific reasoning questions; MTurk workers under time pressure may not represent a valid ceiling for human performance, especially on specialized knowledge. The paper does not report how many annotators evaluated each question, inter-annotator agreement for the human baseline, or acknowledge these as limitations in interpreting the 60.3% figure.

- **The abstract and conclusion highlight self-verification, self-consistency, and chatbot interactions as contributions, but the main paper contains no quantitative results, experimental setup, or evidence for any of these claims.** All substantive discussion is deferred to the appendix (§A.4–A.6 references in lines 50–51). This is not about the appendix being missing—it is about the paper making prominent claims in the abstract without providing any support in the main text for a reader to evaluate. At minimum, a summary table or a brief experimental sketch belongs in the core paper.

### Trivial

None.

## Nice-to-Haves

- **Confidence intervals or error bars for the main results**: Single-point accuracy values are the norm for this type of benchmark evaluation, but the paper draws conclusions about fine-grained model rankings (e.g., small differences between augmented LLM variants) that would be more informative with basic statistical uncertainty estimates. This is a helpful addition, not a flaw.

## Removed Points

These points were flagged by reviewers but are excluded from the main weaknesses above for the reasons stated:

- *No variance/uncertainty reporting*: Single-point accuracy reporting without error bars is standard practice for large-scale benchmarks (MMLU, GSM-8K, etc.) in this field. Moved to Nice-to-Have.
- *Three new datasets are small* (12% of total): The benchmark's primary value is the curated compilation of 31 datasets. The new datasets serve gap-filling roles, which is appropriate. Not a genuine weakness.
- *Data contamination discussion missing*: The paper explicitly states (§2.4, line 85) that answer labels for the test set will not be publicly released to prevent contamination. The concern is addressed.
- *No analysis of answer distribution or biases*: The paper provides answer statistics (Table: avg answer length 1.2, max answer length 27, 55.2% multiple-choice). The focus on short-answer formats is an intentional design choice consistent with the benchmark's purpose.
- *Various speculative concerns about the GPT-4V evaluation* (e.g., "could the evaluator have re-prompted?", "unknown system prompt"): While the limitation is real and retained as a Major weakness, specific speculation about undocumented re-prompting behavior without evidence is removed. The retained criticism focuses on the documented, verifiable methodological gap.

## Novel Insights

The most striking finding that emerges from the reviews—and that is verified against the paper's Table 3—is the asymmetry in GPT-4V's strengths vs. weaknesses: it surpasses human performance on algebraic reasoning, geometry, and textbook QA simultaneously (three categories where pattern-matching and visual recognition of standard forms suffice) yet achieves barely half of human performance on logical reasoning (21.6% vs. 40.7%) and numeric commonsense (20.1% vs. 53.8%). This suggests that the model's apparent "mathematical reasoning" may in fact be primarily perceptual pattern completion on stereotyped visual inputs, collapsing when the task requires non-standard logical deduction or common-sense numerical estimation that a human would find trivial. The benchmark's granular annotation is what surfaces this dissociation, which is arguably more interesting than the aggregate 49.9% versus 60.3% comparison.

## Suggestions

1. **Restructure the paper to de-emphasize the GPT-4V comparison as the headline result, or replace it with a reproducible evaluation.** Since GPT-4V API was unavailable, the paper could present the GPT-4V results as an exploratory observation with explicit caveats in the abstract and conclusion, and anchor the paper's claims around the 11 non-GPT-4V evaluations and the benchmark itself. If GPT-4V API access is now available, a properly documented batch evaluation would resolve the issue.

2. **Provide at least one quantitative summary of the self-verification or self-consistency experiments in the main paper** (e.g., a single table comparing accuracies with and without these techniques) rather than deferring all evidence to the appendix. The abstract should not claim contributions that have no support in the main text.

3. **Acknowledge the human baseline's limitations explicitly** (MTurk population, time pressure, lack of domain expertise verification) and, if possible, report inter-annotator agreement for the human performance evaluation.

4. **Include confidence intervals or statistical significance tests for the key model comparisons** (e.g., Bard vs. augmented LLMs at ~34%) where the differences are small enough that readers cannot judge whether they are meaningful.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Reject</decision>