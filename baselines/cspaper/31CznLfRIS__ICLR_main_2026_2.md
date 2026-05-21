---
job_id: 3cfbf6f8-208a-4f78-8110-7d07703a4682
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: 31CznLfRIS.pdf
paper: VideoJudge: Bootstrapping Enables Scalable Supervision of MLLM-as-a-Judge for Video Understanding
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅ The paper is clearly within ICLR scope, focusing on multimodal evaluation, video understanding, learned evaluators, and benchmark construction for MLLM-as-a-judge.

## Minimum Quality
Pass ✅ The paper contains the necessary scientific sections, presents a concrete method, reports substantial experiments, and does not exhibit a fatal methodological flaw that would warrant desk rejection, although there are several important concerns about evaluation design and clarity.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅ I did not find any hidden prompts, suspicious reviewer-directed instructions, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper proposes VideoJudge, a video-specialized MLLM judge trained using a bootstrapped generator-evaluator pipeline that synthesizes candidate responses across a discrete rating scale and retains or refines them based on evaluator agreement. The paper trains 3B and 7B pointwise and pairwise judge models, introduces bootstrapped meta-evaluation benchmarks, and reports results against unimodal and multimodal judge baselines on both synthetic and human-annotated evaluation sets. The work also explores test-time generation of instance-specific rubrics for video response evaluation.

## Strengths
The paper tackles a meaningful and timely problem. Reliable evaluation for open-ended video understanding is genuinely underdeveloped relative to text and image settings, and the submission addresses a real bottleneck: human evaluation is expensive, while off-the-shelf metrics are often not aligned with semantic correctness or grounding.

The overall framing is practical and coherent. The generator-evaluator-refinement loop in **Figure 1** makes the proposed pipeline easy to follow at a high level, and it usefully connects data construction, quality control, and downstream judge training. Even though some details remain underspecified, the main idea is understandable and operationally relevant.

The empirical section is broad. The paper evaluates both pointwise and pairwise judges, compares against multiple unimodal and multimodal baselines, includes long-video evaluation, and adds several analyses beyond the main headline numbers, including temperature robustness and max-frame ablations. This is more comprehensive than many evaluator papers that only report a single benchmark or a single evaluation protocol.

Some of the results are genuinely strong. In **Table 1**, VideoJudge-7B is competitive with or better than much larger Qwen2.5-VL variants on several metrics, especially on VideoJudgeVCG and LongVideoBench, where it reaches the best reported \(\Delta(\mathrm{C-D}) = 1.16\). Likewise, in **Table 3**, the pairwise VideoJudge models are consistently strong, especially on the VideoJudge-derived pairwise sets, and the 7B model performs near the top across all three benchmarks. Even if one discounts the closed-loop benchmarks, the results suggest that fine-tuned smaller judges can become surprisingly capable.

I appreciated that the paper does not just report wins and move on. The error analysis on **Page 9** explicitly acknowledges overestimation bias and poor calibration in the mid-to-high rating range. That honesty helps, and it points to concrete next steps rather than pretending the problem is solved.

The rubric-generation extension is interesting. The results in **Table 2** suggest that training a smaller model to generate instance-specific rubrics can materially improve evaluation quality. This is a useful direction for interpretable judge models, especially in open-ended multimodal tasks where generic rubrics are often too blunt.

The human evaluation component, while limited, is still helpful. **Table 7** reports high agreement and strong correctness on the difficult 2-vs.-3 setting, which at least provides some evidence that the bootstrapped pairwise labels are not arbitrary.

## Weaknesses
1. **The evaluation story is still too closed-loop, and this matters for the core claim of “alignment with human judgment.”**  
   The paper itself acknowledges this limitation in **Section 7 / Page 10**, but it is not a minor caveat, it is central. A substantial fraction of the supervision and several of the evaluation benchmarks are produced by the same generator-evaluator pipeline. The resulting risk is not merely “distribution overlap,” but evaluator preference imprinting: the trained judge may learn to emulate the biases and granularity of the synthetic pipeline rather than acquiring robust evaluation ability. This is especially salient for the strongest gains reported on the VideoJudge-derived benchmarks in **Table 1** and **Table 3**.  
   Why this matters: if the benchmark and the training signal share the same construction logic, strong scores do not cleanly establish generalizable judging ability. They may instead measure compatibility with the synthetic rubric implicit in the bootstrapping process. The paper does evaluate on VATEX, LongVideoBench, and VideoAutoArena, which is good, but the independent evidence remains relatively sparse compared with the amount of emphasis placed on the bootstrapped benchmarks. I would have liked a stronger separation between training-data construction and evaluation claims.

2. **Several core methodological details are underspecified, especially around the synthetic-label generation process.**  
   The core pipeline is formalized in **Equations (1) to (4)** on **Pages 3-4**, but important implementation details are missing from the main paper. For example, the evaluator \(E\) produces a rating \(\hat r\), yet the paper does not specify whether \(\hat r\) is always parsed as a single deterministic integer, how invalid generations are handled, whether multiple samples are used, or how often the evaluator fails to follow the required format. The acceptance threshold \(\alpha\) is introduced, but only some datasets use \(\alpha=0\), and it is not clear what values are used elsewhere in the main experiments. Likewise, the maximum refinement iterations \(T\) is introduced but never given in the main text, and the acceptance rate as a function of iteration is absent.  
   There is also a notation inconsistency: the seed triplet is written as \((\hat v, x, y^*)\) in the text on **Page 3**, but **Equation (4)** uses \(\tilde v\) rather than \(\hat v\). In **Algorithm 1** on **Page 24**, the input also switches to \(\tilde v\). This is not a catastrophic issue, but for the central object in the method, the notation should be stable. More importantly, the description “generate responses conditioned on a target rating, then refine until \(|r-\hat r|\le \alpha\)” is not enough to assess label fidelity without knowing how often the process converges, how often it collapses to generic low-quality text, and whether specific rating levels are harder to realize than others.

3. **The mathematical formulation of training is too coarse relative to what the models actually output.**  
   In **Section 3.2 / Page 4**, the training objective is written as a standard token-level autoregressive negative log-likelihood,
   \[
   \mathcal{L}(\theta)=-\frac{1}{M}\sum_{i=1}^{M}\sum_{j=1}^{|t_i|}\log P_\theta(t_{i,j}\mid t_{i,<j},v_i,x_i,y_i).
   \]
   But \(t_i\) is described as “the associated target annotation, such as a rating or a preference label,” while the actual outputs include rich structures such as `<rubric>`, `<thinking>`, and `<score>` for pointwise evaluation. This creates ambiguity about what exactly is supervised. Is the model trained on gold reasoning traces produced by an external teacher? Is the score token weighted differently from reasoning tokens? Are invalid or missing tags penalized the same way as mis-scored predictions? If the rubric-generating model is trained with synthetic rubrics plus scoring, is the loss simply concatenated-token NLL over rubric, reasoning, and score, or are there separate objectives?  
   Why this matters: the reported gains in **Table 2** are attributed to rubric supervision, but without a precise formulation the reader cannot tell whether the improvement stems from better representations, additional synthetic targets, longer supervised chains, or simply easier decoding constraints. Since the paper places considerable emphasis on reasoning and rubric generation, the training objective needs to be specified more carefully.

4. **The evidence for the claimed benefit of “reasoning” and rubrics is suggestive but not isolated cleanly.**  
   The pointwise models are trained to emit `<thinking>` plus `<score>`, and optionally `<rubric>` first. The paper also compares against “thinking mode” in Qwen3 baselines and concludes that long chain-of-thought does not help as much as access to video. However, this comparison is not especially clean. The unimodal “thinking mode” baselines in **Table 1** still rely on text descriptions rather than video inputs, so the experiment conflates modality access, backbone differences, and reasoning style.  
   Similarly, the rubric experiment in **Table 2** uses only Qwen2.5-VL-3B, only \(10\%\) of the pointwise data, and only 1,000 examples from two VideoJudge-derived benchmarks. That is an interesting pilot result, but it does not justify broad claims about rubric-driven evaluation more generally. A more convincing analysis would compare: plain scoring vs reasoning+scoring vs rubric+reasoning+scoring, under matched data and compute, on both synthetic and independent human-annotated benchmarks.

5. **The pairwise results are strong, but the interpretation around feedback is inconsistent and under-analyzed.**  
   In **Table 3**, “with feedback” does not consistently help. For example, Qwen2.5-VL-32B drops from \(90.59\) to \(80.78\) on VAA when using feedback, and VideoJudge-7B is slightly worse with feedback on VAA and VJ. Yet the surrounding discussion on **Pages 8-9** is fairly loose, stating that feedback improves smaller baselines and is mixed for VideoJudge variants. That is true but incomplete. The much bigger issue is that the paper does not explain what “with feedback” means at inference time in enough detail, nor why stronger models sometimes degrade sharply.  
   Why this matters: if feedback is a key ingredient in the training pipeline and in some evaluation settings, the paper should analyze failure modes. Is feedback introducing verbosity that hurts pairwise decision quality? Does it amplify positional or formatting biases? Or is the comparison not apples-to-apples because the “with feedback” prompt changes task structure substantially? Right now the table raises more questions than the text answers.

6. **The automatic data-quality validation is fairly weak and, in one case, unintentionally exposes dataset artifacts.**  
   The paper uses BLEU and BERTScore in **Figure 2** to show monotonic degradation as ratings go from 5 to 1. This does verify that lower-rated responses become less similar to the gold answer, but that is a very limited notion of validation. It does not establish that rating 4 is genuinely “better” than rating 3 in a human-meaningful sense, only that it is lexically or semantically closer to the reference. A generator trained or prompted to create degraded responses could satisfy this monotonicity almost by construction.  
   Worse, **Table 6** contains a representative example where the instruction asks, “What is the man wearing while ironing the dress shirt?” but the \(R5\) response is about a ballet studio and children dancing, with \(R4\) through \(R1\) following the same unrelated scene. This is not a small typo because it appears in the section meant to demonstrate data quality. It raises concern about data assembly, prompt-response alignment, or table construction. If the showcased example is mismatched, readers will naturally wonder how often such mismatches occur in the actual training set. At minimum, the paper should acknowledge and quantify this issue.

7. **The independent human evaluation is too narrow to support strong claims of human alignment.**  
   The human study in **Section 5.2** focuses exclusively on 2-vs.-3 pairwise comparisons, with 250 samples and only two annotators, then keeps only full-agreement cases for one derived benchmark. This is useful as a spot-check, but it is not enough to support broad claims that the judge aligns with human preferences across task types and rating levels. There is no pointwise human calibration study across all 1-5 scores, no analysis of disagreements between VideoJudge and annotators on difficult open-ended examples, and no estimate of whether the synthetic ratings are ordinally consistent beyond that narrow band.  
   Why this matters: the paper repeatedly frames its contribution as scalable supervision that can replace costly human annotation, so the amount of direct human validation is arguably the most scientifically important issue. Right now it is present, but too limited.

8. **The use of dense video descriptions is both a strength and a conceptual complication that the paper under-discusses.**  
   On **Page 3**, the bootstrapping process uses dense descriptions \(\hat v\) generated by strong vision-language models for both the generator and evaluator, rather than raw video. On **Page 16**, those descriptions are generated partly by GPT-4o-mini and partly by Qwen2.5-VL-32B. This is perfectly reasonable as an engineering choice, but it complicates the narrative that the system is learning “video understanding evaluation.” In fact, part of the supervision pipeline is mediated through high-quality textual summarization produced by strong external models.  
   Why this matters: some of the resulting judge quality may come from inheriting the abstraction and filtering already performed by those description generators. This does not invalidate the method, but it does blur where the “video-specialized” capability is really coming from. A stronger ablation would compare bootstrapping with raw video only, description only, and both, or at least report how description source affects downstream judge quality.

9. **Presentation quality is uneven, with several concrete issues in notation, formatting, and editing.**  
   There are numerous small but cumulative problems: “shown in 1” instead of “shown in Equation 1” on **Page 3**; inconsistent use of \(\hat v\) and \(\tilde v\); “basielines” typo on **Page 8**; malformed output tag in **Figure 14**, which says `<answer>{{A_or_R}}</answer>` instead of A or B; references with duplication and formatting problems in the bibliography, including repeated Qwen2.5-VL entries and visibly noisy citation formatting on **Pages 10-16**; “Scale 1(5)” in **Figure 10** instead of 1-5; and a dangling “Figure ??” mention on **Page 19**.  
   None of these alone would sink the paper, but together they make the work feel less polished than it should be for a top conference, especially because some of them occur in the core method and prompt definitions.

10. **Some baseline and exclusion decisions deserve better justification in the main paper.**  
   The authors state on **Page 5** that several video models were excluded because they “failed to follow instructions or produce valid scores under the same evaluation setup.” That may well be true, but from a benchmarking perspective this is delicate. Judge tasks are prompt-sensitive, and excluding recent models without reporting even a simple invalid-rate table or rescue prompt leaves readers unsure whether the comparison is fair or merely convenient. Since the paper’s claims are comparative, clearer reporting on exclusion criteria would strengthen credibility.

## Questions
1. For the bootstrapping process in **Equations (1)-(4)** and **Algorithm 1**, please report the actual values used for \(\alpha\) and \(T\) in the main experiments, plus the distribution of refinement iterations required before acceptance. What fraction of candidates are accepted at \(t=0\), after one refinement, and not accepted at all? This would materially increase my confidence in the synthetic-label quality.

2. Can the authors provide a clearer decomposition of the training targets in **Section 3.2**? Specifically, for the pointwise and rubric models, is the supervised target
   \[
   t_i = [\texttt{<rubric>}, \texttt{<thinking>}, \texttt{<score>}]
   \]
   as one concatenated sequence under a single NLL, or are there separate losses / weights for rubric tokens, reasoning tokens, and the final score token? If the latter, please specify them. This is important for interpreting **Table 2**.

3. How much of the gain remains on strictly independent benchmarks if the VideoJudge-derived meta-evaluation sets are excluded? A compact summary table for only VATEX, LongVideoBench, VideoAutoArena, and the human-validated VJ-H subset would make the generalization claims much more convincing.

4. Relatedly, can the authors quantify possible closed-loop inflation? For example, if one trains with bootstrapped data from one generator/evaluator configuration and evaluates on a benchmark generated by a different generator/evaluator pair, how much does performance drop? That would directly probe whether the model is learning general evaluation behavior or pipeline-specific preference structure.

5. The data example in **Table 6** appears mismatched, with an ironing-related instruction paired with ballet-scene responses. Is this a table assembly error, or does it reflect noise in the underlying dataset? Please quantify the frequency of such instruction-response mismatches in the bootstrapped data. This point matters because the table is intended as evidence of data quality.

6. For the pairwise “with feedback” setting in **Table 3**, what exactly is fed back at inference time, and why do some strong models degrade substantially, especially Qwen2.5-VL-32B on VAA? A short failure analysis with examples would help.

7. Since dense descriptions are generated by external strong models, can the authors isolate the effect of description source? For example, does a dataset bootstrapped entirely with Qwen2.5-VL-32B descriptions yield similar results to one bootstrapped with GPT-4o-mini descriptions? This would help clarify how much the pipeline depends on the quality of the proxy descriptions.

8. The rubric experiment is promising but narrow. Would the authors consider adding a matched ablation comparing score-only, reasoning+score, and rubric+reasoning+score under the same data budget and benchmark set? That is the cleanest way to substantiate the claimed value of rubric supervision.

## Flag For Ethics Review
- Yes, Discrimination / bias / fairness concerns  
- No ethics review needed.

## Details Of Ethics Concerns
The paper studies learned judges and proposes them as scalable evaluators for video understanding systems. That naturally raises fairness and bias concerns, even if no immediate deployment risk is described. In this submission, the most relevant issue is evaluator bias induced by the synthetic generator-evaluator pipeline and by the use of strong external models to produce dense descriptions. If the judge internalizes systematic preferences for certain answer styles, verbosity levels, or model families, then downstream evaluations could become biased in ways that are difficult to detect. The paper does discuss overestimation bias in **Section 6.2 / Page 9**, which is good, but a broader bias and fairness discussion would still be helpful.

## Soundness Rating
3: good. The paper presents a reasonable method and substantial experiments, but several central claims, especially around human alignment and generalization beyond the synthetic pipeline, are not supported as strongly as the paper suggests.

## Presentation Rating
2: fair. The paper is readable overall and the main idea comes through, but there are enough notation inconsistencies, missing methodological details, formatting problems, and benchmark/reporting ambiguities that the presentation falls below what I expect for a polished ICLR paper.

## Contribution Rating
3: good. The problem is important, the video-specific judge framing is useful, and the empirical results are interesting, especially for small fine-tuned evaluators. However, the contribution is held back by the closed-loop evaluation design and by insufficient isolation of which ingredients drive the gains.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected.  
I see real value here: the problem is important, the proposed bootstrapping recipe is practical, and several empirical results are strong enough that the work is worth discussion by the community. At the same time, the paper overreaches a bit relative to its evidence. The biggest issue is that too much of the validation remains entangled with the same synthetic pipeline used to create the supervision. If the authors can convincingly address the closed-loop concern, clarify the training objective and bootstrapping details, and explain the apparent data-quality glitch in **Table 6**, my confidence would increase substantially. As written, I lean positive, but not comfortably.

## Reviewer Confidence
4: confident. I am confident in the overall assessment and familiar with the surrounding judge-model literature and multimodal evaluation setting, though some implementation details are missing from the paper and limit how far the technical verification can go.