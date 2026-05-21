---
job_id: 19936e2d-dc25-4e25-bb73-ae2a154455f1
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: khHNHzRjMy.pdf
paper: EmoSign: A Multimodal Dataset for Understanding Emotions in American Sign Language
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The submission is clearly within ICLR scope as a multimodal dataset/benchmark paper for emotion understanding in sign language, with relevance to representation learning, multimodal ML, evaluation, and societal accessibility concerns.

## Minimum Quality
Pass ✅. The paper includes the expected components for a dataset/benchmark submission, namely abstract, introduction, related work, dataset construction methodology, benchmarking experiments, results, limitations, and conclusion. While there are substantial weaknesses in experimental design and evidence strength, these are review-level concerns rather than desk-reject-level fatal flaws.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, reviewer-targeting instructions, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper introduces EmoSign, a dataset of 200 ASL video clips annotated for sentiment, emotion categories, and free-form descriptions of emotion cues by three Deaf native ASL signers with professional interpretation experience. The paper also provides benchmark results on sentiment and single-label emotion classification using several multimodal LLMs under caption-only, video-only, and video+caption settings, with the goal of studying whether current models can recognize emotion from sign videos rather than leaning on text captions.

## Strengths
The main strength is that the paper targets a real and underexplored problem. Emotion understanding in sign language is both scientifically interesting and practically important, and the paper makes a credible case in Sections 1 and 2 that sign-language emotion recognition is not a straightforward extension of spoken-language affect recognition because the same visual channels carry both grammatical and affective information.

The dataset contribution is meaningful despite its modest scale. Table 1 makes the positioning reasonably clear: existing ASL resources largely focus on translation or captioning, whereas EmoSign adds sentiment, emotion labels, and qualitative cue descriptions. The decision to involve Deaf native ASL signers rather than hearing crowdworkers is a genuine strength, especially given the paper’s own motivation that hearing observers often misread signers’ facial expressions.

I also appreciated that the paper goes beyond labels and collects open-ended cue descriptions. The qualitative discussion on Page 5 about non-manual markers, signing speed, emphasis, and contextual disambiguation is useful and gives the dataset more research value than a bare classification benchmark. That part is one of the more interesting aspects of the submission.

Figure 1 is a helpful high-level overview of the pipeline, and it makes the overall process easy to follow: source selection, VADER-based filtering, expert annotation, then post-processing. For a dataset paper, having this end-to-end picture is useful for readers trying to understand what was actually curated versus inherited from ASLLRP.

Figure 2 is also informative. In particular, Figure 2B honestly shows that the sentiment distribution is strongly polarized rather than naturally distributed, which is important context for interpreting the benchmark numbers. Figure 2C also gives a quick sense that some emotions are far more represented than others, which helps explain why some classes are much harder in Table 4.

The benchmarking section, while limited, is still useful as a first pass. The caption/video/video+caption ablations are the right instinct for this problem, because they directly probe whether models are using visual evidence or simply textual shortcuts. Table 3 and Table 4 do support the narrow claim that current off-the-shelf MLLMs struggle badly in video-only settings on this benchmark.

The paper is generally readable, and the qualitative examples in Figure 3 help illustrate the central thesis. That figure is especially effective at showing that models can produce plausible-sounding explanations that shift with textual context. Even though the evidence is anecdotal, the figure does convey the type of failure mode the authors care about.

## Weaknesses
1. **The dataset construction introduces a strong and somewhat troubling selection bias, because the final sample is chosen via a text-based sentiment filter rather than a sign-based emotional criterion.**  
   Section 3.1 states that the authors selected the final 200 clips as the 100 most positive and 100 most negative utterances according to VADER scores on English captions. This matters a lot, because the paper’s central claim is about emotion in ASL videos, not emotion in English translations of those videos. If the initial sampling criterion is driven by caption sentiment, then the benchmark is predisposed to favor text-aligned emotional content and may underrepresent exactly the hard cases the paper claims to care about, namely cases where visual affective cues diverge from caption semantics or where grammar and emotion are confounded in the signing itself. Figure 1 makes this pipeline explicit, which is good for transparency, but it also exposes the conceptual weakness. At minimum, the paper should quantify how often caption polarity and signer-annotated sentiment disagree, because without that, it is hard to know whether the benchmark genuinely measures sign-language emotion understanding or partly measures caption sentiment recovery.

2. **The scale of the dataset is very small for the breadth of claims made, and the class support is thin enough that several benchmark conclusions feel overstated.**  
   The paper has 200 utterances totaling about 16 minutes of video, with only 140 clips in the single-expression subset and 37 clips in the multi-expression subset after filtering (Page 6). Table 4 then reports per-class accuracies over 10 emotion labels plus neutral, but Figure 2C already suggests substantial imbalance, and the appendix figures reinforce that some categories have very small counts. When support is this low, class-wise accuracy can swing wildly with just a few examples, and broad claims such as models “fail to integrate visual cues” or “exhibit bias towards positive emotions” become fragile unless accompanied by uncertainty estimates, bootstrap confidence intervals, or repeated-evaluation variance. Right now the evidence is suggestive, not decisive.

3. **The annotation aggregation and reliability analysis are not strong enough for several labels, yet the paper proceeds as if the labels were equally stable across the board.**  
   Table 2 is one of the most concerning parts of the paper. Some label-wise Krippendorff’s alpha values are respectable, for example sentiment at 0.738 and joy at 0.699, but others are very weak: surprise\_neg at 0.119, disgust at 0.166, frustration at 0.330, sadness at 0.333, anger at 0.370. These are not minor fluctuations. They indicate that for a substantial subset of the label space, the ground truth itself is uncertain or poorly operationalized. The paper acknowledges lower agreement for negative emotions, but then still uses these labels as benchmark targets without any stratified analysis that separates high-reliability classes from low-reliability ones. This matters because poor model performance on a low-agreement label is much less informative scientifically. A more careful treatment would either downweight low-reliability categories, report performance as a function of annotation agreement, or define a consensus/ambiguous split. As written, the benchmark conflates model failure with label instability.

4. **The benchmark methodology is not sufficiently controlled to support strong conclusions about multimodal integration.**  
   The core claim in the abstract and results is that “current multimodal models fail to integrate visual cues into emotional reasoning.” But the empirical setup does not isolate integration cleanly. Different models use different prompting strategies, and Section 4.2 admits that GPT-4o used one structured multi-task prompt, while AffectGPT, Qwen2.5, and MiniGPT4 required separate prompts because they could not reliably follow the same format. That means the comparison is not apples-to-apples across models, and it also weakens any cross-model conclusions about multimodal behavior. Even within a model, caption-only versus video+caption differences could reflect prompt formatting and instruction-following artifacts, not only modality use. This is especially important because the paper interprets small or moderate metric changes as evidence of visual grounding behavior. That inference is currently too strong for the experimental design.

5. **Several evaluation details are underspecified or confusing, especially the metric definitions and task formulation.**  
   Table 3 reports “wAcc” and “wF1”, but the exact definition of weighted accuracy is never clearly specified. Some values are also eyebrow-raising, such as MiniGPT4 caption-only obtaining 1.92 wAcc and 5.92 wF1 on 3-class sentiment, or AffectGPT video-only giving 33.33 wAcc and 0.04 wF1. These may be numerically possible under a particular weighting scheme and percentage scaling, but the paper does not explain the computation clearly enough for the reader to verify what these numbers mean. The same issue appears in Table 4, where class-wise accuracies and total weighted scores are shown, but the relation between them is opaque. For a benchmark paper, metric clarity is not a cosmetic issue. If readers cannot reconstruct how the headline numbers were computed, the benchmark becomes harder to trust and reuse.

6. **The single-label emotion classification task seems to discard important structure in the annotations, and the subset construction is too ad hoc.**  
   Section 4.1 says the original emotion labels are intensity scores for 10 categories, then joy and excited are merged into happiness, then videos with no emotions become neutral, then the benchmark focuses on a “single-expression set” of 140 clips and a “multi-expression set” of 37 clips, while combinations appearing only once are filtered out. This is a lot of post hoc restructuring of a small dataset. It is understandable for benchmarking convenience, but it also means the main experimental task no longer fully reflects the original annotation richness. More importantly, the paper does not justify why these transformations preserve the scientific target. If ASL emotion expression is inherently multi-cue and often mixed, then reducing the problem to a single dominant label may produce a cleaner table while sidestepping the more realistic part of the dataset.

7. **The qualitative grounding analysis is interesting but methodologically weak, and the paper draws stronger conclusions from it than the evidence supports.**  
   Section 5.3 is framed as a “preliminary understanding,” which is fair, but the surrounding claims sometimes go beyond that. Figure 3 provides a single compelling example of models shifting their explanations depending on whether the caption is available. However, manually inspecting “several randomly selected videos” is not enough to support a general conclusion about grounding failure modes. There is no annotation protocol for grounding, no quantitative measure, no inter-rater verification of what counts as a correct cue, and no systematic sample size. So while Figure 3 is illustrative, it is anecdotal evidence, not a robust evaluation. The paper should present this as a motivating case study, not as strong empirical backing for broad claims about model reasoning.

8. **The results in Table 3 and Table 4 do not consistently support the paper’s strongest interpretation that visual information contributes meaningfully.**  
   In Table 3, video+caption is usually best, but the margins are uneven and sometimes modest, especially for 7-class sentiment. In Table 4, the paper itself notes that caption-only is similar to or sometimes better than video+caption. This is not a minor caveat, it cuts directly against the stronger framing that visual integration is helping in a meaningful way. A harsher reading is that the current benchmark largely shows models can use caption semantics, while the additional video stream sometimes helps, sometimes hurts, and often remains hard to interpret. The authors do mention this tension, but the abstract and conclusion lean harder on the “multimodal integration” story than the evidence comfortably supports.

9. **The paper does not adequately separate dataset contribution from benchmark contribution, and the latter is relatively weak.**  
   As a dataset paper, the main value is the curated annotation resource. As a benchmark paper, however, the modeling side is fairly thin: four off-the-shelf MLLMs, no sign-language-specific encoder baseline, no pose/landmark baseline, no simple supervised classifier over extracted visual features, and no adapted non-manual facial model. This matters because the current negative result, namely that generic MLLMs do poorly, may simply reflect a weak baseline choice rather than a deep property of the task. Table 4 in particular would be much more informative if the paper included even a basic task-specific baseline rather than only instruction-tuned generalist systems. Without that, the benchmark says more about current MLLMs than about the dataset’s full research potential.

10. **The literature positioning is thinner than it should be for a paper claiming a first benchmark in this area.**  
   The paper does discuss FePh and sign-language translation datasets, but the positioning around sign-language emotion recognition and facial-expression analysis in signing feels incomplete. Given the centrality of non-manual markers to the paper’s motivation, I expected a broader discussion of work on emotionality and facial-expression modeling in sign language beyond the one closest dataset comparison in Section 2. This matters because the novelty claim is not only about new labels, it is also about how this work fits into a growing line of sign-language affect and non-manual understanding research. Stronger positioning would help readers understand exactly what is first here: first ASL video dataset with sentence-level sentiment labels, first Deaf-annotated multimodal affect benchmark, first resource with cue descriptions, or something narrower.

11. **The paper raises an important conceptual issue, grammatical versus affective use of facial expressions, but never operationalizes it in the dataset or evaluation.**  
   This is one of the most compelling motivations in the introduction, yet by the time we get to the actual benchmark, there is no annotation or analysis that identifies grammatical facial markers separately from emotional ones. As a result, the paper repeatedly invokes this dual-function challenge, but the dataset does not yet let us measure whether models are failing because they confuse grammar and emotion, or because they simply cannot parse the signing. This is a missed opportunity and weakens the connection between the motivating problem statement and the delivered benchmark.

12. **There are some presentation issues and overclaims that, while not fatal, reduce confidence.**  
   A few examples: on Page 8 the paper says “we verified” certain cues were truly present in videos, but does not explain the verification protocol; in Section 4.2 there is a typo, “these model were seeded”; and there are places where the wording suggests stronger inference than the data warrants. None of these alone would sink the paper, but together they contribute to the sense that the paper is stronger as an initial dataset release than as a tightly validated benchmark study.

## Questions
1. Can the authors quantify the mismatch between VADER-based caption selection and final signer-provided sentiment/emotion labels? A table showing how often caption polarity disagrees with Deaf annotator sentiment would substantially increase my confidence that the benchmark is not merely a caption-sentiment proxy.

2. Please clarify the exact definition of weighted accuracy used in Table 3 and Table 4. Is it balanced accuracy, class-frequency-weighted accuracy, or something else? A formula would help, especially given some unusual score patterns.

3. For the labels with very low agreement in Table 2, did you consider marking samples as ambiguous, reporting per-class confidence intervals, or stratifying results by agreement level? I would find such an analysis very valuable.

4. Why were the final 200 clips chosen as the top 100 positive and top 100 negative by VADER rather than, for example, selecting a broader sample and then balancing according to human ASL-based annotations? If this was mainly a budget constraint, please say so explicitly and discuss the implications more directly.

5. Can you provide a clearer justification for the single-expression subset construction in Section 4.1? In particular, how many samples were lost at each filtering step, and how sensitive are the reported numbers to the decision to merge joy/excited and to exclude certain multi-label combinations?

6. Since the main claim is that generic MLLMs are poorly grounded on sign-language emotion, could you add at least one simple sign-specific baseline, for example a classifier over pose, facial landmarks, or frozen video features? Even a modest task-specific baseline would help distinguish “the task is hard” from “the chosen models are a poor fit.”

7. Figure 3 is compelling, but can you make the grounding analysis more systematic? For example, annotate a small subset of clips with cue spans or cue categories and report agreement between model-mentioned cues and human-mentioned cues.

8. The introduction repeatedly emphasizes the distinction between grammatical and affective facial expressions. Do you have any annotation signal, even coarse, that could help separate these in future versions of the dataset? If not, I would encourage you to frame that point more explicitly as future work rather than as something the current benchmark already addresses.

## Flag For Ethics Review
- Yes, Discrimination / bias / fairness concerns  
- Yes, Privacy, security and safety  
- Yes, Potentially harmful insights, methodologies and applications  
- Yes, Responsible research practice (e.g., human subjects, data release)  

## Details Of Ethics Concerns
The topic itself involves inferring emotions from signed communication, which is a sensitive inference task. Errors here can reinforce stereotypes about Deaf signers or encourage overconfident affect inference systems in high-stakes settings such as healthcare, legal, or educational contexts, all of which the paper itself references in the introduction. That raises fairness and potential harm concerns even if the paper’s intent is constructive.

There is also a responsible-release question around dataset publication. The paper states that data and code will be released after acceptance and mentions IRB approval in Section 3.2, which is good, but it does not clearly discuss consent, downstream-use restrictions, or whether the original ASLLRP participants agreed to emotion-analysis reuse specifically. Since videos of identifiable people are involved, the release and reuse conditions deserve explicit discussion.

Finally, because the benchmark could be used to build systems that infer emotions from visually observed signers, the paper should more explicitly caution against deployment in decision-making settings without stronger validation and community governance.

## Soundness Rating
2: fair. The dataset creation effort is real and the central empirical observations are plausible, but several claims are supported only partially due to small scale, selection bias, weak reliability for some labels, and limited benchmark methodology.

## Presentation Rating
3: good. The paper is generally readable and the figures/tables are useful, but important evaluation details remain unclear, and some claims are framed more strongly than the evidence supports.

## Contribution Rating
2: fair. The dataset fills a real gap and is likely useful to the community, but the benchmark side is limited and the current paper does not yet fully deliver on the more ambitious scientific claims it raises.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted.  
My view is that the dataset idea is worthwhile and the community may benefit from the release, but in its current form the paper falls short of ICLR standards because the benchmark conclusions are stronger than the evidence, the sampling pipeline injects caption-based bias into a sign-language emotion task, and the evaluation methodology is not yet rigorous enough to support the headline claims.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. The dataset and benchmark setup are clear enough to evaluate, and I carefully checked the main tables, figures, and methodological choices.