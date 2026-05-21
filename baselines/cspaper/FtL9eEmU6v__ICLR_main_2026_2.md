---
job_id: eb91a5b6-f60c-4aa0-b066-ae3c36354ef8
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: FtL9eEmU6v.pdf
paper: EDIT-Bench: Evaluating LLM Abilities to Perform Real-World Instructed Code Edits
main_score_norm: 0.8
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. This submission is clearly in scope for ICLR as a benchmark and evaluation paper for ML systems, specifically LLM-based code editing, with relevance to datasets/benchmarks, language modeling, and realistic evaluation of AI assistants.

## Minimum Quality
Pass ✅. The paper has the core components expected for a benchmark paper, including abstract, introduction, related work, benchmark construction methodology, evaluation, quantitative results, and conclusion/limitations. The work is complete enough to assess scientifically, and while I have several substantive concerns, none rises to the level of a desk reject.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find evidence in the provided paper text of hidden prompts, reviewer-targeted instructions, or other manipulative content.

# Expected Review Outcome:
## Summary
This paper introduces EDIT-Bench, a benchmark for instructed code editing built from in-the-wild user interactions collected through a VS Code extension. The benchmark contains 540 problems spanning multiple natural languages and two programming languages, and each task includes realistic contextual signals such as file context, highlighted code, and cursor position. The authors evaluate 40 LLMs on the benchmark, analyze performance by edit category and context condition, and compare results against existing edit-oriented benchmarks.

## Strengths
The biggest strength is the problem formulation itself. The paper is targeting a very real and increasingly important interaction mode, namely editing existing code under underspecified user instructions, rather than generating functions from scratch. That distinction matters, and the paper motivates it well in Sections 1 and 3.

The data source is meaningfully stronger than most prior edit benchmarks. Collecting tasks from a live VS Code extension, rather than asking annotators to write synthetic instructions, gives the benchmark a more realistic distribution of instructions and contexts. The examples in **Table 2** make this point effectively. The EDIT-Bench prompts are visibly messier, shorter, and more context-dependent than the heavily specified prompts shown from CanItEdit and EditEval. This is one of the clearest pieces of evidence in the paper that the benchmark is not just a rewrapping of existing data.

The benchmark captures contextual signals that are actually used in editor workflows. **Figure 1** is a simple but useful overview of the task interface, and the paper consistently emphasizes that the model may need the instruction, whole-file context, highlighted span, and cursor position together. This is a practical contribution because many coding evaluations ignore exactly these disambiguating cues.

I also appreciated the benchmark comparison in **Table 1**. It makes a concise and convincing case that EDIT-Bench differs from prior edit benchmarks not only in source, but also in instruction diversity, context length, and the availability of highlighted code. The fact that the benchmark includes highlighted regions while the listed alternatives do not is particularly important for this task setting.

The empirical evaluation is broad. Testing **40 models** across multiple families gives the benchmark immediate utility as a comparative evaluation suite rather than a paper artifact waiting for others to use it. **Figure 4** is effective here, because it quickly shows both the overall difficulty of the benchmark and the open-vs-closed gap. Even without every exact number in the figure text, the ranking pattern is easy to interpret.

The paper goes beyond a single leaderboard and includes several targeted analyses. The context ablation in **Table 3** is useful because it directly tests whether the added realism of the benchmark matters. Likewise, **Figure 5** adds value by showing that performance varies substantially by edit category, rather than merely preserving one global model ranking.

The benchmark appears thoughtfully curated rather than naively dumped from user logs. The authors describe a two-stage process involving filtering trivial/ambiguous examples, writing test harnesses, and second-pass review by another annotator. For a benchmark paper, that curation effort is important and is clearly described in Section 3.

The paper is generally well written and easy to follow. The narrative from motivation, to collection pipeline, to curation, to evaluation is coherent. **Figure 2** helps ground the collection setup and makes the benchmark construction story more concrete.

## Weaknesses
1. **The paper does not provide enough evidence that the final test harnesses are robust enough to support strong leaderboard conclusions.**  
   This is my main concern. The benchmark lives or dies by test quality, yet the main paper gives only a high-level description of how tests were written in **Section 3.3**. We learn that five programmers created tests, that a second annotator reviewed them, and that an agent was used for environment setup, but the paper does not report basic quality statistics for the final test suites: number of tests per problem, distribution of assertion counts, code coverage, mutation sensitivity, inter-annotator disagreement rates, or the fraction of candidate solutions rejected by second review. Without these details, it is hard to judge whether pass/fail outcomes are truly measuring edit correctness or just partial proxy behavior. This matters because the central claims, especially model rankings in **Figure 4**, rely entirely on the test harnesses being faithful and sufficiently discriminative.

2. **The curation pipeline introduces substantial subjectivity, and the paper does not quantify how much that subjectivity affects the benchmark.**  
   In **Section 3.2**, the authors remove problems that are “too similar,” “trivial,” “stylistic,” or “ambiguous.” Those filters are reasonable in spirit, but they are also exactly where benchmark bias gets introduced. The final path is quite aggressive: from 2672 accepted responses, to roughly 1700 Python/JavaScript problems, to around 470 curated problems, to 109 unique problems in the core benchmark, later expanded to 540 via translation. This is a large reduction. The paper does not report annotation agreement on what counts as ambiguous or trivial, nor does it characterize how the retained set differs from the original distribution. That omission matters because the benchmark is presented as “real-world,” yet a large portion of realism may have been filtered out by hand. A benchmark can be curated, of course, but then the paper should quantify the curation effect rather than treating it as a neutral step.

3. **The multilingual expansion is useful, but scientifically weaker than the paper’s framing suggests.**  
   The core benchmark seems to contain 109 unique underlying problems, and **Section 3.2** says these are translated to create the 540-problem complete benchmark. This means the multilingual dimension is largely a prompt-translation expansion, not 540 independently collected in-the-wild tasks. That is still useful, but it is not the same as having organically collected multilingual user instructions at that scale. The paper somewhat blurs this distinction. Also, translation validation is limited: the authors mention native-speaker evaluation of “a subset,” primarily Chinese and Spanish, but there is no systematic translation quality analysis for all target languages. This matters because language-specific results could be driven by translation artifacts rather than genuine multilingual editing difficulty.

4. **Programming-language coverage is still quite narrow for a paper making broad claims about real-world code editing.**  
   The benchmark ultimately focuses only on Python and JavaScript, with the appendix indicating that JavaScript is particularly small in the core set. The paper acknowledges this limitation, but it still somewhat overstates generality in places. Real-world coding assistants are heavily used in TypeScript, Java, C/C++, Go, and web stacks with multi-file structure, and the collected raw data in **Page 5 / Section 4** itself shows notable presence of PHP and HTML that were not carried forward. As a result, the benchmark is better viewed as a realistic benchmark for single-file Python/JavaScript edit tasks, not yet for “real-world instructed code edits” writ large.

5. **The evaluation setting only partially matches the data collection setting, and this gap is under-discussed.**  
   In **Section 5**, the authors say all prompts ask the model to regenerate the entire file. But the collection prompt in Appendix A is a span-rewrite interaction, and the benchmark motivation repeatedly emphasizes highlighted code and cursor position. Full-file regeneration may be convenient for evaluation, but it changes the task. It can both help and hurt models, for example by enabling broader refactoring or by increasing the chance of unrelated regressions. The paper should discuss this mismatch more directly. In fact, **Figure 1** frames the problem as editing a highlighted region, while the actual benchmark inference protocol is “rewrite the entire file.” Those are not identical tasks.

6. **The difficulty split is circular and should not be treated as an independent analysis axis.**  
   In **Section 5**, a problem is marked Hard if it is solved by at most \(k=20\) models, otherwise Easy. Formally, if one defines per-problem difficulty as  
   \[
   d_i = \sum_{m=1}^{M} \mathbf{1}\{\text{model } m \text{ solves problem } i\},
   \]
   then the paper sets  
   \[
   \text{Hard} = \{ i : d_i \le 20 \}, \quad \text{Easy} = \{ i : d_i > 20 \}.
   \]
   This is not wrong, but it is endogenous to the evaluated model set, so conclusions about “hard prompts” are partly definitional. For example, statements like hard problems having shorter instructions are descriptive of what the chosen 40 models struggle with, not evidence of some benchmark-intrinsic hardness notion. The paper should present this more cautiously and ideally complement it with a model-independent proxy, such as annotator-rated ambiguity, context dependency, or test-suite complexity.

7. **The ablation in Table 3 is interesting but too underpowered to support broad conclusions about context usage.**  
   The authors evaluate only 7 models, one per “top” family, under different context conditions. That is a reasonable start, but the table reveals a more complicated picture than the text admits. Highlighted code helps several models, but not all; cursor information is mixed; and for at least one model, the combined context hurts substantially. In particular, **Table 3** is also a bit confusing in its layout, with duplicated “+Highlight” / “+Cursor” headers and one row showing a large negative swing for glm-4.6 that deserves explanation. The takeaway should be more restrained than “highlighted code is crucial,” because the evidence is heterogeneous and model-dependent. This matters because one of the paper’s headline claims is that realistic context materially changes evaluation outcomes.

8. **Some empirical claims would benefit from uncertainty estimates or significance testing.**  
   The benchmark is evaluated with pass@1 from a single sample per problem, usually at temperature 0. For many of the reported differences, especially small deltas in **Table 3** such as \(+0.37\), \(-0.18\), or \(+0.74\), it is unclear whether these are meaningful or just noise from API nondeterminism, provider instability, or benchmark variance. Confidence intervals via bootstrap over problems would have been easy and would greatly strengthen the conclusions. This is especially relevant when the paper interprets small differences between prompt settings or neighboring models.

9. **The comparison to existing benchmarks is suggestive, but the correlation analysis is too shallow.**  
   In **Section 5.2**, the paper reports weak correlations with Aider Polyglot and Chatbot Arena. That is plausible and potentially interesting, but the analysis is fairly thin. Since these comparisons are used to argue that EDIT-Bench captures distinct capabilities, I would have liked more than two Pearson correlations. Rank correlations, per-family analyses, or even a scatter plot would help. Also, given that the benchmark differs from Chatbot Arena in both input modality and output structure, a weak correlation is not especially surprising on its own. The claim is directionally fine, but the evidentiary bar should be higher.

10. **There are a few presentation inconsistencies that are small individually but nontrivial in aggregate for a benchmark paper.**  
   The paper states different natural-language sets in different places. On **Page 2**, the benchmark is said to include English, Spanish, Russian, Chinese, and Portuguese. On **Page 4 / Section 3.2**, the listed languages are English, Russian, Chinese, Polish, and Spanish. That inconsistency is not minor, because multilingual composition is one of the advertised contributions. There are also a few naming inconsistencies in model names and prompt descriptions, and **Table 3** is genuinely hard to parse from the header structure. These issues do not invalidate the paper, but they reduce confidence in the exact benchmark specification.

11. **The paper could position itself better relative to repository-scale and interaction-rich editing settings.**  
   The related work section covers benchmark neighbors reasonably well, but the paper’s own claims should be scoped more carefully. EDIT-Bench is focused on single-file edits with localized context, and that is a valid and useful niche. Still, the manuscript sometimes reads as if it is broadly representative of realistic software maintenance. It is not yet addressing multi-file edits, repository navigation, or longer-horizon interactions. This is not a fatal omission, but it is an important boundary condition on the benchmark’s external validity.

12. **Ethics and privacy safeguards are described, but benchmark release risks remain underexplored in the main paper.**  
   The collection pipeline uses user code from real development environments. The paper notes IRB review and privacy controls in **Section 3.1** and Appendix A, which is good. But the main paper is fairly light on release-risk specifics: what exact code/context is distributed, whether licenses are tracked, whether translated tasks can still leak proprietary structure, and how often PII/manual screening found issues. Because the benchmark’s main selling point is real-world code, these details matter more than they would for a synthetic benchmark.

## Questions
1. Can the authors provide quantitative statistics about the final test suites for the 109 core problems, for example median number of unit tests per problem, assertion counts, code coverage where applicable, and any measure of mutation sensitivity or adversarial robustness? This would significantly increase my confidence in the leaderboard results.

2. How much annotator agreement was there in the filtering stage in **Section 3.2** for labels such as “trivial,” “stylistic,” and “ambiguous”? If no formal agreement was measured, can the authors at least provide a retrospective double-annotation study on a subset?

3. Please clarify the language composition inconsistency between **Page 2** and **Page 4**. Is the final benchmark language set English/Spanish/Russian/Chinese/Portuguese, or does Polish replace Portuguese at some stage?

4. For the multilingual expansion, can the authors explicitly separate results on organically collected non-English problems from translated variants? That distinction would help readers interpret whether multilingual performance reflects true in-the-wild robustness or primarily translation robustness.

5. Why was full-file regeneration chosen as the primary inference protocol rather than localized rewrite of the highlighted span? Have the authors compared the two evaluation modes on a subset? A short controlled comparison would be very informative.

6. For **Table 3**, please clarify the exact four prompt conditions, since the header appears ambiguous. Also, can the authors add confidence intervals or bootstrap standard errors over problems for the reported pass@1 values and deltas?

7. The “easy vs hard” split is defined based on how many of the 40 evaluated models solve each problem. Can the authors present one more difficulty analysis based on a model-independent property, such as annotator-rated ambiguity, context length, test complexity, or highlight length bins?

8. The paper mentions that some problems were removed as ambiguous because the intended edit could not be inferred even with context. Could the authors report what fraction of initially promising problems were discarded for this reason, and perhaps give a taxonomy of ambiguity types? That would be useful both scientifically and for future benchmark design.

9. Since **Figure 5** suggests strong category-specific variation across models, did the authors check whether these differences persist after controlling for instruction length or context length? Otherwise, category effects may be confounded by prompt complexity.

10. Can the authors state more explicitly what artifacts will be released, including raw code context, test harnesses, translated prompts, and metadata about the original collection source and privacy filtering?

## Flag For Ethics Review
- Yes, Privacy, security and safety  
- Yes, Legal compliance (e.g., GDPR, copyright, terms of use)  
- Yes, Responsible research practice (e.g., human subjects, data release)  

## Details Of Ethics Concerns
The benchmark is built from real user code collected via a VS Code extension, so privacy and release governance matter. The paper states in **Section 3.1** and Appendix A that the process received IRB approval, users had privacy controls, and PII screening is performed, which are all positive steps. Still, there are unresolved questions that merit ethics review: whether released code snippets may contain proprietary or licensed material, how consent and deletion rights are operationalized across jurisdictions, whether translated prompts preserve sensitive details from source code/comments, and how much of the original context is exposed in the public benchmark. Because the paper’s contribution depends on real-world code, these concerns are not peripheral.

## Soundness Rating
3: good. The paper is methodologically solid overall and the main claims are generally supported, but confidence is limited by the lack of detailed test-suite quality evidence and some over-interpretation of small empirical differences.

## Presentation Rating
3: good. The paper is clearly written and mostly easy to follow, though there are some specification inconsistencies and at least one results table, **Table 3**, that needs cleanup.

## Contribution Rating
4: excellent. A realistic, in-the-wild benchmark for instructed code editing with contextual editor signals is a meaningful contribution that the community is likely to find useful.

## Overall Rating
8: Accept, good paper (poster). I have real reservations about test-harness characterization, curation subjectivity, and the scope of the benchmark’s claims, but the core contribution is important, timely, and substantially stronger than most existing edit benchmarks in realism. I would support acceptance.

## Reviewer Confidence
4: confident. I am confident in this assessment and familiar with the benchmarking/evaluation space for code LLMs, though some confidence would increase further with more concrete evidence about test quality and curation reliability.