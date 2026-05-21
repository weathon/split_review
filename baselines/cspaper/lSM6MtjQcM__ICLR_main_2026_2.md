---
job_id: 95160633-e000-4d29-ae52-2e62101baa4d
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: lSM6MtjQcM.pdf
paper: AetherCode: Evaluating LLMs’ Ability to Win in Premier Programming Competitions
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. This is a benchmark and evaluation paper for LLM reasoning/coding, which clearly fits ICLR’s scope on datasets and benchmarks, language-related ML, and general machine learning evaluation infrastructure.

## Minimum Quality
Pass ✅. The paper has the expected structure for a benchmark paper, presents a concrete curation and evaluation methodology, includes substantial experiments and quantitative results, and is written in English with sufficient technical detail to clear the desk-rejection bar.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden prompts, suspicious reviewer-targeting instructions, or other manipulative content in the provided paper text or figures.

# Expected Review Outcome:
## Summary
This paper introduces AetherCode, a new benchmark for evaluating LLMs on competition-level programming, with 456 problems sourced from recent premier contests such as IOI-, OI-, and ICPC-style events. The benchmark emphasizes both harder problem selection and stronger evaluation reliability via a hybrid automated-plus-expert test case construction process, and the paper reports results for a range of reasoning and non-reasoning models. The main empirical conclusion is that current frontier models remain far from strong human competitive programmers on these tasks.

## Strengths
The paper addresses a real and important gap in code reasoning evaluation. The core motivation, namely that many existing coding benchmarks are either too easy, too narrow in source coverage, or evaluated with weak test suites, is convincing and well articulated in Section 1. I also appreciate that the paper does not just complain about prior benchmarks, it builds a concrete alternative around more challenging and contemporary competition problems.

The benchmark curation effort appears substantial. Collecting 456 recent problems from premier contests, converting statements into a machine-friendly format, proofreading them, assigning metadata, and curating over 30,000 human-written solutions is meaningful work. For a benchmark paper, this scale matters.

The test-case quality discussion is one of the more compelling parts of the paper. Framing a problem’s test suite as a binary classifier over correct vs. incorrect submissions in Section 2.3.1 is a clean way to operationalize verifier quality. Equations (1) and (2), defining TPR and TNR, make the intended evaluation criterion explicit, and this is more concrete than simply reporting the number of generated tests. I also like that the paper distinguishes validity of tests from coverage of failure modes, rather than collapsing them into one vague notion of “more tests is better.”

Figure 1 is useful and does real explanatory work rather than serving as decoration. It clearly lays out the three-stage pipeline, statement processing, categorization, and test case construction, and makes it easy to understand where human oversight enters the loop. In particular, the separation between the G-V agent, accuracy check, and expert audit in Figure 1 supports the paper’s claim that this is not a purely automated benchmark dump.

The empirical results are informative and, frankly, sobering in a useful way. Table 3 shows that even the best model only reaches 35.5 Pass@1 and 46.6 Pass@4 overall, with single-digit performance on the Hard and Extreme subsets. That is exactly the sort of result a hard benchmark should reveal if the benchmark is doing its job. The benchmark seems to separate models well, especially among stronger reasoning systems.

Table 4 is another strength because it goes beyond a single scalar leaderboard. The category-wise breakdown helps show that weaknesses are not uniform, for example, tree problems and computational geometry remain difficult for nearly all models. This makes the benchmark more diagnostically useful than a plain aggregate score.

The difficulty and category statistics in Figure 2 are helpful for understanding dataset composition. The figure suggests the dataset is not dominated by one trivial slice, and the category spread looks reasonably broad. For a benchmark paper, such transparency about composition is important.

The paper is also reasonably well positioned as a benchmark contribution rather than a methodological one. It does not oversell itself as solving competitive programming; it mostly claims to provide a more faithful measurement instrument.

## Weaknesses
My main concern is that the paper’s strongest claim, benchmark reliability through “100% TPR and 100% TNR,” is much less ironclad than the writing sometimes implies. In Section 2.3.1, these metrics are computed only on the authors’ collected solution set, not on the full space of possible correct and incorrect programs. This is fine as an internal validation proxy, but the phrasing in several places, including the abstract and conclusion, risks reading like a universal guarantee of correctness and comprehensiveness. That is too strong. A benchmark test suite can achieve perfect discrimination on a finite collected pool and still miss unseen bugs or pathological cases. This matters because the paper’s central narrative is that AetherCode fixes evaluation bias from poor test cases; if that claim is overstated, the scientific contribution becomes less secure than advertised.

Related to that, the paper does not quantify how representative the collected incorrect solutions actually are. Section 2.1 says each problem has at least 5 correct and 20 incorrect solutions, and Section 2.3.3 acknowledges that some problems have fewer than 50 incorrect solutions. But there is no systematic analysis of whether these incorrect solutions cover diverse failure modes or are clustered around a few common mistakes. A test suite validated against narrow negative examples can get an inflated TNR. This is not a minor bookkeeping issue, because the entire verifier-quality argument depends on the negative solution pool being meaningfully hard to discriminate.

The methodology around difficulty labeling is serviceable but still too heuristic for how prominently the paper uses those labels. Section 2.2 states that difficulty is based on numbers of successful human contestants within contests, plus expert judgment across contests, and then the overall ranking is split into three roughly equal categories, while “Extreme” is reserved for unsolved-by-humans problems. There are at least two issues here. First, the calibration across contests is underspecified, because contest populations differ substantially in strength and format. Second, the text is slightly inconsistent, since it says problems are divided into four levels but later says the overall ranking is split into three roughly equal categories, Easy, Medium, and Hard, with Extreme handled specially. Figure 2 shows the resulting counts, but it does not resolve the methodological ambiguity. Since a major advertised feature is evaluation “across difficulty,” the paper should define this more rigorously.

The comparison to prior benchmarks is a bit too rhetorical and not empirical enough. Table 1 gives a broad comparison of datasets, but much of it is schematic, for example, difficulty as stars and test case construction as coarse labels. The paper repeatedly argues that AetherCode is harder and more reliable than benchmarks like LiveCodeBench, CodeELO, and LiveCodeBench Pro, but it does not provide direct head-to-head evidence on overlapping model sets, overlapping time windows, or matched subsets. For a benchmark paper, that missing calibration matters. Without it, the reader is asked to accept “harder and better” mostly from dataset provenance and internal validation rather than comparative measurement.

The experimental protocol is underdeveloped for such a central benchmark paper. Section 3 says each model is evaluated four times per problem with maximum output length 32,768 and that “detailed settings” are in Appendix A, but the main paper omits several choices that affect fairness and interpretation: whether temperature differs by model family, how sampling parameters are set for Pass@N, whether system prompts or reasoning controls are standardized, whether compile-and-repair or retry logic is disallowed, and how special-judge tasks are handled in the reported numbers. For a benchmark intended as a community standard, these details should not be mostly deferred outside the main paper. Otherwise, it is harder to interpret Table 3 as a fair comparison rather than a snapshot under one lab-specific evaluation harness.

There is also a nontrivial issue with the interpretation of Pass@N in Table 3. The paper says each model is evaluated four times and “average numbers are reported,” but it does not clearly specify whether Pass@2 and Pass@4 are computed from independent samples under the standard unbiased estimator, or simply by empirical success over repeated runs. That distinction matters, especially when comparing exploration gains between models. The claim in Section 3.1 that stronger models exhibit greater “exploration potential” may be true, but without clear sampling methodology it is more of an observation than a robust conclusion.

The category analysis in Table 4 is potentially informative, but the paper’s interpretation overreaches a bit because category difficulty is confounded with category composition. The authors do include one caveat, noting that category distributions are inconsistent and some categories may simply be harder, which is good. But then the text still uses Table 4 to draw fairly strong conclusions such as “all models uniformly excel at pattern-based tasks such as Basic Algorithms and Strings.” That is not fully warranted without controlling for the difficulty mix within each category in the main paper. Appendix B reportedly contains category difficulty distributions, but the main paper’s conclusions should not hinge on appendix-only nuance.

The paper raises compliance and legal concerns about using Codeforces judging services, which is fair, but Appendix D reveals that some problems in AetherCode itself have “authorization or copyright status currently unverifiable.” That is a significant issue for an open benchmark release. Even if the authors are willing to remove content upon request, the current wording suggests the legal status of part of the benchmark is unsettled. For a dataset paper positioning itself partly as a clean alternative to others, this asymmetry deserves more transparent treatment in the main paper rather than a brief appendix caveat.

I also found some presentation issues that, while not fatal, hurt confidence. There are several naming inconsistencies and typos, for example “Aether-Code” vs. “AetherCode,” “Puss@4” on Page 7, and duplicated / inconsistent model names in Table 8 for the Claude series. Example 2 on Pages 21 to 23 appears malformed in places, including a broken truth table for the OR operator and a very messy example formatting. These are not just cosmetic annoyances, because benchmark papers live or die by careful specification. Sloppiness in presentation makes readers wonder where else details might be loose.

On the mathematical side, the TPR/TNR formalization is reasonable but still incomplete as an evaluation model. Equations (1) and (2) implicitly treat each collected solution as an equally informative i.i.d.-like sample of the correctness space, which is unlikely to hold in practice. At minimum, the paper should discuss that these are empirical rates on a curated pool, not unbiased estimates of some population-level verifier property. As written, the equations are correct arithmetically, but the inferential leap from empirical discrimination on a curated set to benchmark reliability in the wild is undertheorized.

Finally, some claims of being “the first” are too broad relative to the evidence in the paper. For example, “the first benchmark to systematically collect latest problems from premier programming competitions worldwide” is a strong statement. The related work in Section 4.2 does discuss several adjacent efforts, but the exact novelty boundary, especially “systematically,” “latest,” and “worldwide,” is not pinned down with enough care. Benchmark novelty claims should be made with a scalpel, not a shovel.

## Questions
1. The most important clarification is about the reported 100% TPR and 100% TNR. Please state very explicitly, in the main paper, that these are empirical rates on the collected solution pool. Also, can you provide per-problem distributions, for example, histogram or summary statistics over the number of correct/incorrect solutions used in this validation? That would substantially increase my confidence in the verifier-quality claim.

2. Can you better formalize the difficulty assignment procedure from Section 2.2? In particular:
   - how are problems compared across contests with very different participant pools,
   - what exact rule separates Hard from Extreme,
   - and can you report inter-annotator agreement or some measure of stability for expert difficulty judgments?
   A clearer definition here would make Figure 2 and the difficulty columns in Table 3 much more convincing.

3. For Table 3, please clarify exactly how Pass@1, Pass@2, and Pass@4 are computed. Are these based on four independent stochastic samples? If so, what decoding settings are used for each model, and is a standard estimator employed? This matters for the “exploration potential” interpretation in Section 3.1.

4. A direct comparative calibration against one or two existing competition-level benchmarks would strengthen the paper a lot. Even a small matched-model comparison on AetherCode vs. LiveCodeBench / CodeELO style benchmarks would help substantiate the claim that current popular benchmarks materially overestimate ability.

5. Can you provide more detail on decontamination? The benchmark is recent, which helps, but some models may still have seen parts of the data or editorial reproductions. I am not asking for a perfect contamination audit, but a more systematic description of what was checked would increase confidence.

6. For Table 4, could you report category scores normalized or stratified by difficulty, or at least provide a main-paper figure/table showing category-by-difficulty composition? Right now, the category analysis is interesting but hard to disentangle from category hardness.

7. On the legal side, can you clarify the release policy for problems with unverifiable copyright status mentioned in Appendix D? If those items remain in the public benchmark, that could complicate community adoption.

## Flag For Ethics Review
- Yes, Legal compliance (e.g., GDPR, copyright, terms of use)

## Details Of Ethics Concerns
Appendix D states that for some benchmark problems, the authorization or copyright status is currently unverifiable, and the authors plan to remove potentially infringing problems upon request. Since this is a benchmark release intended for community use, unresolved licensing status is a genuine concern. The paper also criticizes other benchmarks for potential compliance issues related to external judging services, so AetherCode should be held to a similarly clear standard regarding dataset legality and redistribution rights.

## Soundness Rating
3: good. The benchmark construction is thoughtful and the empirical results are meaningful, but several key claims, especially around verifier quality and difficulty calibration, are stronger than the evidence fully supports in the main paper.

## Presentation Rating
3: good. The paper is generally readable and well organized, and Figure 1 / Tables 3 and 4 are useful, but there are enough inconsistencies, underspecified details, and formatting issues that I cannot rate presentation as excellent.

## Contribution Rating
3: good. This is a valuable benchmark contribution with clear relevance to the community, especially because it raises the difficulty bar and takes test-case quality seriously, but the positioning and some of the stronger claims need tightening.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected.  
I lean positive because the benchmark is timely, useful, and clearly more demanding than many widely used coding evaluations, and the headline empirical result, namely that frontier models are still weak on elite contest problems, is worth sharing with the ICLR community. That said, this is not an easy accept for me. The paper would be stronger with more careful calibration against prior benchmarks, tighter framing of the 100% TPR/TNR claim, clearer difficulty methodology, and more explicit evaluation protocol details.

## Reviewer Confidence
4: confident. I am confident in the overall assessment and familiar with the relevant benchmark landscape, though I would still welcome clarification from the authors on verifier validation, Pass@N computation, and licensing.