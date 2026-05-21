---
job_id: 3ccd4d8c-5f4e-431e-8a8c-8ec4035f734c
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: XHzrBDzKaX.pdf
paper: Castle-in-the-Air: Evaluating MLLM Visual Abilities on Human Cognitive Benchmarks
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope as a benchmark and empirical evaluation paper for multimodal large language models, with direct relevance to representation learning, multimodal reasoning, evaluation, and AI applications to cognitive science.

## Minimum Quality
Pass ✅. The paper contains the expected components for a benchmark/evaluation submission, including abstract, introduction, benchmark design and methodology, experiments, quantitative results, failure analysis, related work, and conclusion. While I have substantial concerns about some claims, presentation choices, and parts of the evaluation methodology, these are not so fundamental as to warrant desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, suspicious reviewer-targeting instructions, or other manipulative content in the provided paper text.

# Expected Review Outcome:
## Summary
This paper introduces **VisFACTOR**, a benchmark derived from 20 vision-centric subtests of the Factor-Referenced Cognitive Test (FRCT), adapted into an image-text evaluation setting for MLLMs. The benchmark covers four broad domains of human visual cognition, includes format modifications to reduce chance performance, and additionally provides parametric generators for a subset of tasks to create controllable-difficulty synthetic items. The authors evaluate 23 frontier MLLMs and report that even the strongest model achieves only 30.17% overall accuracy, far below a reported human baseline of 78.8%, with especially poor results on mental rotation, spatial relation, and figure-ground style tasks.

## Strengths
1. **The paper addresses a real and important gap in current multimodal evaluation.**  
   The central motivation is compelling. Existing multimodal leaderboards often conflate visual understanding with text priors, OCR, world knowledge, or benchmark artifacts. A benchmark that explicitly targets lower-level and mid-level visual cognition, rather than broad downstream competence, is useful and timely.

2. **The benchmark design is broader than many recent “single-skill” diagnostic sets.**  
   VisFACTOR spans 20 subtests across perceptual/closure, memory, reasoning, and spatial/visualization domains. That breadth is a genuine strength, especially compared to papers that focus on only one family of puzzles. The examples in **Figure 1** help make this diversity concrete: the paper is not just another mental-rotation benchmark, but a collection of qualitatively different visual demands, including CF/CS tasks, map/path reasoning, and paper folding.

3. **The attempt to reduce chance accuracy is thoughtful and, in spirit, well motivated.**  
   Section 2.3 goes beyond standard multiple-choice reformulation and tries to make random guessing meaningfully less likely. This is especially welcome in a setting where many models can exploit superficial output patterns. The dataset statistics in **Table 6** are useful here, because they make the benchmark scale and per-task guess rates explicit rather than burying them in prose.

4. **The empirical sweep is broad and practically relevant.**  
   Evaluating 23 proprietary and open-source models is a substantial effort. Even if some protocol details need tightening, the broad picture that current MLLMs remain weak on these tasks is supported by the results. **Table 1** conveys an important and sobering result: performance is poor across essentially the whole frontier, and improvements do not monotonically track model family, size, or release recency.

5. **The paper includes useful failure analysis instead of stopping at leaderboard numbers.**  
   Section 4 is one of the better parts of the paper. The MA1 analysis, especially the contrast between semantically rich memorization stimuli and abstract line-based stimuli, is interesting. **Figure 3** is effective in illustrating this intervention, namely replacing concept-rich memorization items with abstract patterns. Similarly, **Figure 4** supports the claim that saliency of the start marker in CF3 matters and that some failures may come from low-level localization rather than “reasoning” per se.

6. **The controllable-difficulty generation component is potentially valuable.**  
   The generated examples shown in **Figure 2** make it plausible that at least some tasks can be systematically scaled in difficulty. This increases the benchmark’s long-term usefulness beyond the finite FRCT item pool.

## Weaknesses
1. **The core scientific claim is stronger than what the evidence really supports.**  
   The paper repeatedly moves from “models perform poorly on this benchmark” to much broader conclusions such as existing progress being “castles in the air” and models lacking “genuine” or “human-like” visual cognition. That rhetorical leap is not fully justified by the experiments. VisFACTOR is a carefully curated diagnostic benchmark, but it is still a particular operationalization of visual cognition through static 2D tasks with text outputs. Poor performance on these tasks is strong evidence of important limitations, but not sufficient evidence for the broader thesis that progress on existing multimodal benchmarks is largely illusory. This matters because the headline claim is much larger than the validated empirical statement.

2. **The paper underspecifies how faithful the digitized tasks remain to the original cognitive constructs after substantial interface and scoring changes.**  
   Section 2.2 explicitly states that instructions were shortened with help from GPT-4o and Gemini, then reconciled by a human. Section 2.3 further changes the original tasks by decomposing multiple-choice items, grouping repeated items into all-or-nothing clusters, and introducing additional symmetry variants or specialized rewrites. These changes may be reasonable for model evaluation, but they also change the psychometric object being measured. The paper acknowledges this partially in the appendix limitations, yet the main paper still presents VisFACTOR as directly grounded in FRCT factors. That positioning is too clean. Once prompts, scoring rules, and task decompositions change substantially, the benchmark becomes FRCT-inspired rather than a straightforward digital FRCT proxy. This matters because much of the paper’s novelty and significance argument rests on psychometric grounding.

3. **Several evaluation and reporting choices reduce confidence in the quantitative conclusions.**  
   The paper reports many percentages but almost never gives uncertainty estimates, confidence intervals, or significance tests. This is especially important because several subtests have small numbers of scored questions, as seen in **Table 6**. For instance, conclusions about model-family differences or “no consistent correlation with model scale or version” are weak without uncertainty quantification. Some observed deltas in **Table 1** are small enough that they may not be stable under repeated API calls or minor protocol variations. For a benchmark paper, stronger treatment of statistical uncertainty is not optional, it is part of the evidence.

4. **Table presentation is poor enough to impede interpretation of the main results.**  
   **Table 1** is the paper’s central quantitative result, yet the columns are labeled only as “1, 2, ..., 19”, while the benchmark contains 20 subtests. The mapping from column index to subtest is not provided in the table itself, which makes careful interpretation needlessly difficult. Worse, the mismatch between “20 subtests” and the 19 visible indexed columns raises avoidable confusion about whether a task is missing from the table or whether one column was omitted in formatting. This is a serious presentation problem for the main result table, not a cosmetic issue.  
   **Table 2** has a similar problem. The caption says it reports performance under temperatures $\{0.0, 0.5, 1.0\}$, but the columns are shown as “0.0, 0.5, 1.0, 1.5, ..., 8.5,” which appear to be subtest slots rather than temperatures. As written, the table is malformed or mislabeled, and therefore does not support the robustness claim cleanly.

5. **There is at least one concrete mathematical / formal inconsistency in the chance-reduction section.**  
   In Section 2.3, item 3 (“Symmetry variants”), the paper says that MV1, MV3, and S2 generate *three* variants per item, then states “The probability of guessing all three correctly by chance is $(0.5)^4 = 6.25\%$.” This is internally inconsistent. If there are three binary variants, then the chance should be $(0.5)^3 = 12.5\%$; if the intended total is four binary queries including the original phrasing, then the text should say so explicitly. This is not a trivial typo, because Section 2.3 is the formal basis for the paper’s “2.89% overall chance” claim. A benchmark paper that foregrounds its chance-level rigor should have this accounting airtight.

6. **The generation component is only partially validated in the main paper.**  
   Section 2.4 and **Figure 2** suggest that generated tasks can vary difficulty in controllable ways, but the validation is thin in the main paper. In Section 3.3, generated subsets are evaluated only with GPT-4.1, not across multiple model families or humans. The claim that difficulty is being systematically controlled is therefore under-supported. An increase or decrease in model performance under parameter changes does not by itself prove that the synthetic items preserve the intended cognitive demands or are well calibrated to human difficulty. This matters because the generation module is pitched as a key contribution and as a way to “future-proof” the benchmark.

7. **The human evaluation is useful but still too limited to anchor some of the stronger comparative claims.**  
   The paper reports a human average of 78.8% in **Table 4**, based on 31 undergraduate students, with each question completed by three independent participants. That baseline is directionally useful, but several details needed for interpretation are missing from the main paper: time limits, device/viewing conditions, recruitment protocol, compensation, and whether participants saw exactly the same decomposed yes/no variants and all-or-nothing grouped scoring as models. Since the benchmark modifies original FRCT items substantially, the human baseline should be described much more carefully. Without that, the human-model gap is suggestive but not as definitive as the paper implies.

8. **Some of the paper’s own analyses point to confounds that are not cleanly disentangled.**  
   Section 4 argues that models rely on concept recognition rather than low-level visual processing. That may be true, but the interventions do not isolate this as cleanly as claimed. Replacing semantically rich MA1 images with CF2-style abstract images changes multiple things at once, including visual familiarity, memorability, verbalizability, and possibly rendering style. Similarly, the marker-size experiment in **Figure 4** is interesting, but it diagnoses low-level saliency/localization issues rather than necessarily a general visual-cognition bottleneck. These analyses are good exploratory evidence, but the paper sometimes writes as if they are decisive mechanistic explanations.

9. **The psychometric analysis in the appendix is not persuasive enough to support the benchmark’s factor-structure claims in the main paper.**  
   The main text leans heavily on “factor-grounded” evaluation, but the reported appendix evidence is limited to internal consistency and correlation patterns. That is far weaker than showing that the adapted digital tasks recover the intended latent structure. Also, the description around **Figure 6** is confusing: it first says the figure is the “task-task Pearson correlation matrix,” then says “for most models, pairwise correlations fall in the 0.6-0.8 range,” which sounds like model-model rather than task-task statements. This ambiguity matters because psychometric validity is central to the benchmark’s framing, not a side note.

10. **The literature positioning is decent but not yet fully convincing relative to the growing space of synthetic visual-cognition benchmarks.**  
    The paper cites several relevant works, including Blink, CoreCognition, VisualSphinx, and recent spatial reasoning papers, but the differentiation remains somewhat broad-brush. The main novelty claim is “first benchmark grounded directly in human cognitive factors,” which may be fair in a narrow sense, yet the manuscript would benefit from a sharper side-by-side comparison to recent synthetic visual reasoning and puzzle benchmarks on exactly what is new: factor grounding, answer format, anti-guessing design, human baseline, or controllable generation. Right now, the positioning is directionally correct but not as crisp as it should be for an evaluation paper.

11. **There are multiple writing and editing issues in the main paper.**  
    Examples include “prove” instead of “proves” in Section 2.2, “aske” instead of “ask,” “Perason” in the caption of **Figure 6**, “Temperatures bring marginal influence,” and inconsistent model naming such as “Maonshot” in **Table 1**. None of these alone is fatal, but together they make the manuscript feel less polished than expected for a benchmark paper whose main contribution is careful evaluation design and reporting.

## Questions
1. **Please clarify the exact accounting behind the 2.89% overall chance rate.**  
   In particular, for Section 2.3 item 3, is the effective number of binary queries for MV1/MV3/S2 equal to 3 or 4? The current text says “three variants” but uses $(0.5)^4$. A precise table mapping each subtest to the number of scored atomic queries and the final chance rate would materially increase confidence.

2. **Can you provide a corrected and fully labeled version of Table 1 and Table 2?**  
   For Table 1, please map each numbered column to its subtest ID and explain the apparent 19-column vs 20-subtest mismatch. For Table 2, please clarify whether the columns are temperatures or subtests and report the overall totals explicitly. This would substantially improve interpretability.

3. **How exactly were human participants evaluated under the digital protocol?**  
   Please specify timing, device conditions, whether the all-or-nothing grouped scoring in Section 2.3 was used identically for humans, whether participants saw the exact same prompt wording as models, and whether there was any screening or training phase. A stronger main-paper description here would increase my confidence in the human-model comparison.

4. **What evidence supports the claim that the generated items preserve the intended cognitive factors and provide calibrated difficulty control?**  
   Evaluating only GPT-4.1 on generated subsets is not enough to establish this. Did you check human difficulty monotonicity, item validity, or cross-model consistency on generated tasks? Even concise additional evidence in rebuttal would help.

5. **Can you temper or better justify the strongest conclusions about “human-like visual cognition” and “castles in the air”?**  
   I agree the benchmark exposes serious weaknesses, but the current wording reads broader than the evidence. I would be more positive if the claims were narrowed to what the benchmark directly demonstrates, or if the authors offered stronger argumentation for why this task family should be seen as foundational rather than merely diagnostic.

6. **Can you provide uncertainty estimates or repeated-run stability for at least the headline results?**  
   Since API-based models can exhibit nontrivial variance even at low temperature, confidence intervals or repeated evaluations on a subset would make the conclusions substantially more robust.

7. **Please clarify the relation between FRCT faithfulness and your modified protocols.**  
   Which parts are preserved exactly from FRCT, which are reformulated, and which are newly constructed? A concise “fidelity table” would help separate “digitization” from “benchmark redesign.”

## Flag For Ethics Review
- Yes, Legal compliance (e.g., GDPR, copyright, terms of use)  
- Yes, Responsible research practice (e.g., human subjects, data release)

## Details Of Ethics Concerns
The paper itself raises copyright concerns in **Appendix F**, acknowledging that the original FRCT items are not necessarily in the public domain and that redistribution of original items may be restricted. This is appropriate to disclose, but it also means the paper’s legal basis for using scanned test content should be handled carefully and documented clearly in the final version.

There is also a human study in Section 3.4, but the main paper does not report basic responsible-research details such as consent procedure, compensation, or ethics/IRB review status. I am not assuming misconduct, but the paper should state these details explicitly if humans were recruited.

## Soundness Rating
2: fair. The benchmark idea is reasonable and the empirical evidence is substantial, but several reporting problems, an internal inconsistency in the chance-level derivation, limited validation of generated items, and over-strong interpretation reduce confidence in the strength of the central claims.

## Presentation Rating
2: fair. The paper is readable overall and some figures are effective, but the main result tables are inadequately labeled, there are several editing issues, and some key methodological details are either ambiguous or pushed out of the main narrative.

## Contribution Rating
2: fair. The benchmark is useful and the topic matters, but the contribution is weakened by insufficient validation of the psychometric and generation claims, plus positioning and interpretation that are stronger than the evidence warrants.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper tackles an important problem and has a genuinely useful benchmark flavor, but for ICLR I think the current version overclaims, under-validates key parts of the benchmark design, and presents its main empirical results less cleanly than it should. With tighter claims, corrected formal details, stronger validation of generated items and human protocol, and substantially improved tables, I could imagine moving more positive.

## Reviewer Confidence
4: confident. I am confident in the overall assessment and checked the paper carefully, including the benchmark design choices, equations/chance-level derivations, figures, and result tables, though I did not independently verify appendix algorithms or reproduce experiments.