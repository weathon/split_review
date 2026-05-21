---
job_id: 5b99f555-bb59-40ae-86d5-d94198e65f92
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: blFpxJ3A08.pdf
paper: LPFQA: A Long-Tail Professional Forum-Based Benchmark for LLMs’ Evaluation
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The submission is a benchmark paper for evaluating large language models, which fits ICLR’s scope on datasets and benchmarks for machine learning.

## Minimum Quality
Pass ✅. The paper contains the expected components for a benchmark submission, including abstract, introduction, related work, benchmark construction, experiments, quantitative results, and conclusion. While the paper has substantial methodological and empirical weaknesses, they do not rise to the level of an immediate desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, reviewer-targeting instructions, or other manipulative content in the provided paper text.

# Expected Review Outcome:
## Summary
This paper introduces LPFQA, a benchmark built from professional forum discussions across 20 domains, with the goal of evaluating LLMs on long-tail knowledge and complex reasoning in more realistic, specialized settings. The benchmark construction pipeline combines forum scraping, MLLM/LLM-based question generation and filtering, expert verification, and empirical difficulty adjustment, and the paper reports results on 12 mainstream LLMs.

## Strengths
The paper tackles a real and relevant problem. Many current LLM benchmarks are either academically stylized, too easy, or weakly connected to real user needs, so the attempt to ground evaluation in professional forum discussions is reasonable and potentially useful.

The benchmark spans a broad set of domains. From **Figure 2** and the description in **Section 3.3, Page 6**, LPFQA covers 20 fields ranging from mathematics and physics to law, medicine, finance, and engineering. That breadth is valuable if the dataset is ultimately released in a usable form, because it pushes evaluation beyond a narrow set of academic QA categories.

The construction pipeline is easy to follow at a high level. **Figure 1, Page 4** gives a clear end-to-end picture of the workflow, from forum crawling and screenshot capture to question generation, filtering, expert correction, and difficulty adjustment. Even though many details are missing, the figure does help the reader understand what the authors are trying to operationalize.

The paper does include a nontrivial empirical sweep across many current models. **Table 1, Page 6** reports results for 12 LLMs, and this is more informative than evaluating on just two or three proprietary systems. The score spread is not huge, but it is enough to suggest the benchmark is not entirely saturated.

The benchmark construction is not purely synthetic. The use of authentic forum sources is a meaningful design choice, and the examples in the appendix suggest the authors are at least trying to preserve professional context rather than converting everything into trivial factoid QA.

## Weaknesses
1. **The central claim that LPFQA is a benchmark for “long-tail knowledge” is asserted much more than it is demonstrated.**  
   This is the biggest issue for me. Across **Abstract**, **Introduction (Pages 1–2)**, and **Sections 2–3**, the paper repeatedly emphasizes long-tail knowledge, but there is no operational definition of “long-tail” for this benchmark, no measurement of rarity, no analysis of pretraining exposure, and no head-vs-tail stratification. In other words, the benchmark is sourced from professional forums, but “professional forum-derived” is not the same thing as “long-tail” in any rigorous sense. The paper cites long-tail literature in vision and generic benchmark discussions, but it never shows why these 505 items are actually tail-distributed relative to LLM training corpora. This matters because the main advertised contribution is precisely the long-tail aspect; without evidence for that property, the paper is underspecified at the level of its main scientific claim.

2. **The benchmark construction methodology is too opaque to assess reliability.**  
   **Section 3.2, Pages 4–5** lists eight steps, but many details needed to judge dataset quality are missing. For example: How many raw posts were collected initially? How many were removed at each filtering stage? What proportion of items came from question-only posts versus posts with accepted replies? How many experts verified the benchmark, from which domains, and with what instructions? Was each question checked by one expert or multiple experts? Was there any agreement statistic or adjudication procedure? These are not cosmetic details, they are core to whether the benchmark can be trusted. Right now the pipeline reads more like a plausible data-processing recipe than a reproducible benchmark construction methodology.

3. **There are important internal inconsistencies in the paper’s presentation of the dataset and results.**  
   The abstract states **502 tasks** on **Page 1**, while **Pages 2, 3, and 6** state **505 questions**. This is not a trivial typo, because the paper later creates filtered variants with 436 and 421 items in **Section 4.2.1, Pages 8–9**, so exact counts matter. Also, **Table 2, Page 6** has two columns both labeled “LPFQA,” which appears to be a formatting or labeling error, presumably intended to distinguish the two filtered versions. As written, the table is ambiguous and difficult to interpret. These inconsistencies are small individually, but together they undermine confidence in a paper whose primary contribution is dataset curation.

4. **The evaluation protocol is under-specified, especially for scoring.**  
   The main paper does not clearly define how final benchmark scores are computed. Are all questions multiple-choice, all short-answer, or a mixture? If mixed, what is the ratio? Are all models evaluated with the same prompt template? Are they forced to output an option letter for MCQ items? How are short answers normalized before grading? The paper says on **Page 6** that “All results provided are averaged over three trials,” but there are no standard deviations, confidence intervals, or even a discussion of variance. For a benchmark paper, evaluation details are not an appendix-only luxury; they are central. The scoring mechanism shown in the appendix is also concerning: the judge prompt explicitly says it does **not** receive the original question and evaluates only against “Reference Answer” and “Evaluation Points” (**Appendix C, Pages 16–17**). That can be brittle for professional QA, where correctness often depends on task context. Even if I do not fully discount the appendix, the main paper should have specified the scoring rule more formally, for example with a simple definition like
   \[
   \text{Score} = \frac{1}{N}\sum_{i=1}^{N}\mathbf{1}[\hat{y}_i = y_i]
   \]
   plus clear handling for short-answer grading. As it stands, the scoring pipeline is not described at the level needed for a benchmark paper.

5. **The interpretation of the results is sometimes contradicted by the reported tables and figures.**  
   **Table 1, Page 6** clearly shows **GPT-5** with the highest overall score, 47.28, and **DeepSeek-V3** at 32.60. Yet **Page 8**, under “Overall performance,” states that “DeepSeek-V3 demonstrates the most balanced and consistent performance across disciplines, with no apparent weaknesses, and can thus be regarded as the overall best-performing model.” That is a strong statement, and it does not align with the headline result table. If the intended claim is “most balanced across fields,” that should be quantitatively justified, perhaps by lower variance across domains, not asserted as “overall best-performing.” This kind of mismatch between **Table 1** and the narrative analysis weakens the credibility of the empirical section.

6. **The field-level analysis is not very trustworthy because the dataset is highly imbalanced across domains.**  
   **Figure 2, Page 6** is quite revealing here. Mathematics, biology, and physics have around 60+ items each, while some fields are much smaller, especially **DS with only 3 items**. Several others have around 7 to 16. That means the radar plots in **Figure 3, Page 7** and the max/min summaries in **Figure 4, Pages 7–8** are mixing fields with radically different sample sizes. A model leading on a 3-question field is not comparable to leading on a 60-question field. The caption of **Figure 2** also says “Quality distribution,” but the figure is really showing counts per field, not quality. The imbalance matters because a large part of the paper’s analysis is disciplinary comparison, yet those comparisons are statistically fragile when some axes are based on single-digit sample counts.

7. **The post hoc filtered variants of the benchmark are methodologically questionable.**  
   In **Section 4.2.1, Pages 8–9**, the authors remove questions that none of the models solved, then remove questions that all models solved, arguing that these questions have low discriminatory value. I understand the intuition, but this is dangerously close to defining the benchmark in response to the very models being evaluated on it. At minimum, this should be framed as a diagnostic analysis, not as a stronger benchmark variant. Otherwise, the benchmark is partially tuned to the tested model set. This matters because a benchmark should ideally be stable and model-agnostic, not adaptively filtered based on the current generation of systems.

8. **The “reasoning vs knowledge” ablation is not convincing and the conclusion is overstated.**  
   On **Page 9**, the paper asks “Does LPFQA evaluate knowledge or reasoning ability?” and concludes from the code-interpreter setting in **Table 3** that LPFQA “primarily reflects a model's mastery of domain knowledge rather than its reasoning ability.” That conclusion is far too strong for the evidence provided. A performance drop with a code interpreter does not isolate reasoning as a latent variable; it may reflect poor tool use, mismatched prompting, increased latency/truncation, or the fact that many items are not code-friendly. Similarly, the search-tool experiment in **Table 4** does not establish that retrieval is intrinsically unhelpful for long-tail knowledge. It may simply show that the retrieval setup was noisy or poorly integrated. These analyses are interesting probes, but the causal claims on **Page 9** overreach.

9. **The paper does not position itself adequately against closely related long-tail QA benchmarks.**  
   The related work section discusses general benchmarks and some user-centric evaluations, but the literature positioning remains shallow for a paper whose novelty claim is benchmark construction for long-tail knowledge. There are benchmark directions specifically about long-tail or underrepresented knowledge that should be discussed more directly, because otherwise it is hard to understand what LPFQA adds beyond “forum-sourced and multi-domain.” This omission matters because benchmark novelty often lives in careful differentiation, not just in collecting another dataset.

10. **The benchmark’s answer format and uniqueness claims are not fully credible given the examples.**  
   The paper repeatedly claims “semantic clarity and answer uniqueness,” see **Page 2** and **Page 4**. But the appendix examples already make that claim look shakier than advertised. For instance, **Appendix B, Q&A 2, Pages 12–13** has multiple correct options, with answer “A, B, C, F,” which is not the conventional single-answer MCQ format implied elsewhere. That does not invalidate the whole benchmark, but it does suggest the paper is overstating answer uniqueness and uniformity of task design.

11. **Some mathematical and formal aspects of the evaluation are missing rather than wrong, but the absence still matters.**  
   This paper does not include a theorem or formal derivation, which is fine for a benchmark paper, but it still needs a precise evaluation formalization. There is no explicit definition of per-domain score, macro vs micro averaging, or how the reported numbers in **Table 1** and **Table 2** are aggregated from binary judgments. If the score is
   \[
   s_m = \frac{1}{N}\sum_{i=1}^N g(\hat{a}_{m,i}, a_i),
   \]
   then the grading function \(g\) should be clearly specified for both multiple-choice and short-answer items. Without this, the reader cannot tell whether differences like 44.42 vs 43.03 are meaningful or artifacts of an opaque judge pipeline. For benchmark work, that missing formal definition is a real technical weakness.

12. **Ethics and legality are addressed too lightly given the data source.**  
   The ethics statement on **Page 10** says the data are public and anonymized, but the construction pipeline in **Section 3.2, Pages 4–5** explicitly includes scraping forum links and capturing screenshots of discussions. Public availability does not automatically imply permission for redistribution, screenshot reuse, or benchmark release. Different forums have different licenses and terms of service. This is particularly relevant because **Appendix D, Pages 17–19** lists many heterogeneous sources, including Stack Exchange sites, independent forums, and other web communities. The paper should engage more concretely with licensing, consent, and redistribution constraints.

## Questions
1. **Can the authors provide a rigorous operationalization of “long-tail” for LPFQA?**  
   For example, what measurable criterion makes an LPFQA item tail knowledge rather than simply specialized knowledge? A convincing answer would include some quantitative rarity analysis, retrieval frequency statistics, or pretraining-exposure proxy.

2. **Please provide a full construction accounting table.**  
   I would like to see the number of raw posts, valid screenshots, generated QA pairs, filtered pairs, expert-corrected pairs, and final retained items, ideally broken down by domain. This would substantially increase confidence in the benchmark.

3. **How many experts were involved, in which fields, and what was the verification protocol?**  
   Was each question reviewed by one expert or several? How were disagreements handled? Any inter-rater agreement statistics would be helpful.

4. **What exactly are the two columns in Table 2?**  
   As written, both are labeled “LPFQA.” I assume they correspond to \(\mathrm{LPFQA}^{-}\) and \(\mathrm{LPFQA}^{=}\), but the current table is ambiguous.

5. **Please clarify the evaluation and prompting setup in full detail.**  
   Were all models given identical prompts? Were they forced into a fixed answer format? For short-answer items, how was the judge implemented and validated? Did the judge see the original question or only the reference answer and key points?

6. **Can the authors justify the claim on Page 8 that DeepSeek-V3 is the “overall best-performing model”?**  
   This seems inconsistent with **Table 1** unless “best” is being defined as something like lowest cross-domain variance. If so, that should be stated and quantified explicitly.

7. **Can the authors distinguish more carefully between benchmark diagnostics and benchmark definition?**  
   The filtered variants are interesting, but I would be more comfortable if these were presented as analyses of question discriminativeness rather than as benchmark refinements driven by the same evaluated model set.

8. **For the code-interpreter and search-tool experiments, can the authors provide the exact tool-use prompts and protocol?**  
   Without this, it is hard to know whether the negative results reflect benchmark properties or simply a weak tool-integration setup.

## Flag For Ethics Review
- Yes, Privacy, security and safety  
- Yes, Legal compliance (e.g., GDPR, copyright, terms of use)

## Details Of Ethics Concerns
The paper states on **Page 10** that the benchmark is built from publicly available professional forum data and is anonymized. However, **Section 3.2, Pages 4–5** describes scraping posts and capturing screenshots of discussion pages, and **Appendix D, Pages 17–19** lists a large number of heterogeneous external forums. This raises at least two concrete issues.

First, public visibility does not automatically imply that redistribution of screenshots, derived QA pairs, or forum content is permitted. Licensing and terms-of-service constraints can differ substantially across sites. The paper does not explain whether the benchmark release includes raw text, screenshots, paraphrased content only, or links, and that distinction matters legally.

Second, even if personally identifiable information was removed, screenshots of discussion pages can still preserve usernames, timestamps, or contextual clues if not carefully sanitized. The paper asserts anonymization but does not describe the anonymization process in sufficient detail.

I am not alleging misconduct, but I do think the ethics and legal review should verify that redistribution and anonymization are handled appropriately.

## Soundness Rating
2: fair. The paper has a plausible benchmark construction idea and some empirical evidence, but key claims about long-tail knowledge, reasoning evaluation, and benchmark reliability are not adequately supported by the methodology as presented.

## Presentation Rating
2: fair. The paper is readable at a high level and figures like **Figure 1** help, but there are notable inconsistencies, ambiguous tables, overstatements in the analysis, and insufficient specification of the evaluation protocol.

## Contribution Rating
2: fair. A forum-derived professional benchmark could be useful, and the problem is relevant, but the current paper does not yet make a sufficiently well-substantiated benchmark contribution for ICLR.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The idea is worthwhile and the benchmark may become useful, but in its current form the paper leaves too many core questions unanswered about what is being measured, how the benchmark was curated, and how reliable the reported conclusions really are.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. The main concerns are based on the paper’s own methodological omissions, internal inconsistencies, and overinterpretation of its results.