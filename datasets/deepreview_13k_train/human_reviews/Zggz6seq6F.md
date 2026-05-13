# Can LVLMs Describe Videos like Humans? A Five-in-One Video Annotations Benchmark for Better Human-Machine Comparison

- Decision: Reject
- Scores: 6, 5, 3, 6

## Abstract
Large vision-language models (LVLMs) have made significant strides in addressing complex video tasks, sparking researchers' interest in their human-like multimodal understanding capabilities. Video description serves as a fundamental task for evaluating video comprehension, necessitating a deep understanding of spatial and temporal dynamics, which presents challenges for both humans and machines. Thus, investigating \textit{whether LVLMs can describe videos as comprehensively as humans}—through reasonable human-machine comparisons using video captioning as a proxy task—will enhance our understanding and application of these models. However, current benchmarks for video comprehension have notable limitations, including short video durations, brief annotations, and reliance on a single annotator's perspective. These factors hinder a comprehensive assessment of LVLMs' ability to understand complex, lengthy videos and prevent the establishment of a robust human baseline that accurately reflects human video comprehension capabilities. To address these issues, we propose a novel benchmark, \textbf{FIOVA} (\textbf{F}ive \textbf{I}n \textbf{O}ne \textbf{V}ideo \textbf{A}nnotations), designed to evaluate the differences between LVLMs and human understanding more comprehensively. FIOVA includes 3,002 long video sequences (averaging 33.6 seconds) that cover diverse scenarios with complex spatiotemporal relationships. Each video is annotated by five distinct annotators, capturing a wide range of perspectives and resulting in captions that are 4 $\sim$ 15 times longer than existing benchmarks, thereby establishing a robust baseline that represents human understanding comprehensively for the first time in video description tasks. Using the FIOVA benchmark, we conducted an in-depth evaluation of six state-of-the-art LVLMs (VideoLLaMA2, LLaVA-NEXT-Video, Video-LLaVA, VideoChat2, Tarsier, and ShareGPT4Video), comparing their performance with humans. Results show that while current LVLMs demonstrate some perception and reasoning capabilities, they still struggle with information omission and descriptive depth. Moreover, we found significant discrepancies between LVLMs and humans in complex videos, particularly where human annotators exhibited substantial disagreement, whereas LVLMs tended to rely on uniform strategies for challenging content. These findings underscore the limitations of using a single human annotator as the groundtruth for evaluation and highlight the need for new evaluation perspectives. We believe this work offers valuable insights into the differences between LVLMs and humans, ultimately guiding future advancements toward human-level video comprehension.
More related resources will be released at:  \href{https://huuuuusy.io/fiova/}{https://huuuuusy.io/fiova/}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this paper, the authors propose FIOVA benchmark, designed to evaluate the video description capabilities of LVLMs in comparison with human understanding. The authors address the limitations of current benchmarks by introducing a long-video dataset with diverse scenarios, and annotations from multiple annotators. The paper reports an in-depth evaluation of six state-of-the-art LVLMs and compares their performance with human annotations across various metrics. The findings highlight the discrepancies between LVLMs and human annotators, particularly in complex videos.

### Strengths
- The paper is clearly written and presents a well-structured methodology, results, and analysis.
- The collected dataset is of high quality, featuring perspectives from multiple annotators.
- The authors provide comprehensive evaluations of LVLMs using traditional metrics and AutoCQ-based metrics.

### Weaknesses
The overall paper reads more like a collection of experimental analyses rather than a benchmark for the following reasons:
- There are no experiments that demonstrate why the authors' dataset is superior to other datasets. For instance, is the FIOVA dataset better than the DREAM-1K dataset used in Tarsier for evaluation? Do the models that perform better on FIOVA also perform better in human evaluations?
- No new metrics are proposed. Traditional metrics are not well-suited for current LVLMs due to the nature of long responses. Additionally, is AutoCQ sufficient for evaluating dense captioning?

### Questions
See Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces FIOVA, a novel benchmark for evaluating the video description capabilities of LVLMs in comparison to human understanding. The work provides a dataset of 3,002 long, diverse video sequences, each annotated by five distinct annotators, resulting in more comprehensive and longer captions. The paper conducts an in-depth evaluation of six state-of-the-art LVLMs, revealing that while they show some perception and reasoning capabilities, they still struggle with information omission and descriptive depth, especially in complex videos. The findings underscore the need for new evaluation perspectives that capture semantic understanding, fluency, and content relevance, guiding future advancements toward human-level video comprehension.

### Strengths
1. The work provides extensive materials (video theme definition, representative data, annotation rules, prompts) to make it less difficult to reproduce.
2. FIOVA will be a valuable resource for evaluating the video understanding capabilities of LVLMs.

### Weaknesses
1. Some settings are not easy to follow, like the `Batch Ranking` in Sec 4.3. 
2. `Describe Videos like Humans` might be an interesting evaluation setting. However, it does not stand alone as a task. It would be meaningful to include further analysis to show the correlation between performance  of `Describe Videos like Humans` and other video understanding tasks (VideoQA, etc.). 
3. While this work has adopted multiple metrics to demonstrate the video caption performance, it lacks analysis of how those metrics align with human preference.
4. Sec 2.2 shows that GPT-3.5-turbo is adopted to assess the quality of video caption, while that does not sound make sense to me. How can GPT-3.5 (a legacy text-only model) evaluate dimensions like Context, Correctness for video captions without accessing the visual parts? Can you provide more evaluation samples?

### Questions
Sec 2.2 shows that GPT-3.5-turbo is adopted to assess the quality of video caption, while that does not sound make sense to me. How can GPT-3.5 (a legacy text-only model) evaluate dimensions like Context, Correctness for video captions without accessing the visual parts? Can you provide more evaluation samples?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a new benchmark called FIOVA to evaluate LVLMs in their ability to describe videos with a depth and breadth comparable to human understanding.  FIOVA includes 3,002 long video sequences averaging 33.6 seconds, each annotated by five different human to provide multi-perspective detailed descriptions. The benchmark analyzes the quality and variability of human annotations and compares the performance of several LVLMs. on FIOVA, revealing their strengths and weaknesses. Overall, FIOVA provides a more rigorous and comprehensive framework for assessing the differences in video description capabilities between LVLMs and humans. The benchmark addresses the limitations of existing video captioning datasets, which often feature short video durations, brief annotations, and reliance on a single annotator's perspective. These limitations hinder the assessment of LVLMs' performance on complex, long-duration videos and the establishment of a robust human baseline.

### Strengths
1. The paper collects a new benchmark with richer video descriptions, focusing on long-duration videos with complex spatiotemporal relationships, providing a more realistic and challenging test case for LVLMs. By consistency, context, correctness, detailed orientation, temporality, length, CV and other dimensions and grouping videos according to difficulty, observe the video caption capabilities of different models, showing the advantages and disadvantages of the model, which is more comprehensive than the previous benchmark.
2. The results are clearly presented and supported by quantitative metrics, providing a comprehensive comparison of model performance. A variety of evaluation methods are also introduced, and a baseline assessment of human annotations is conducted. This approach helps to understand the diversity and consistency of human annotations, which is essential for establishing a reliable human baseline. The discussion section provides an in-depth analysis of the findings and their implications. These conclusions are well supported by the results and provide direction for future research.

### Weaknesses
1. The evaluation model has limitations. This article evaluates some selected LVLMs, but does not explore broader models, such as the business model Gemini-1.5-Pro, which has a strong understanding of long videos.
2. There are doubts about the collection of groundtruth in FIOVA. FIOVA carefully designed manual annotations composed of five human annotator annotations, and merged and rewrote human annotations with GPT-3.5-Turbo. However, since GPT-3.5-Turbo cannot directly see the video, induction based on human text order alone can easily bring errors such as illusions to groundtruth. As in Figure 4, the actions of the little boy riding a bicycle are described twice in the text, including the actions on the ground are repeated twice, which is inconsistent with the word order of normal human speech. Without the video frames in Figure 4, it is easy to lead to misunderstandings. At the same time, there is no verification for behaviors such as smiling and pointing at the camera, and it is uncertain whether there will be new errors. The results of relevant experiments performed on the benchmark of video descriptions with errors are not necessarily reliable.
3. This paper provides an overview of performance metrics, but lacks detailed error analysis to explain the types of errors made by LVLM and the reasons behind them. The authors should build on the proposed benchmark with a more fine grained error analysis and explore potential causes. This will provide valuable insights for improving the model and the benchmark itself. At present, both traditional metrics (e.g. METEOR, BLEU) and automated measurement methods that rely on GPT models (e.g. AutoDQ) have limitations. I hope the authors can conduct further research on metrics.
4. There are still many typos in the text, one of the most obvious being that the evaluation metric proposed by Wang et al. (2024) is AutoDQ, not AutoCQ.

### Questions
1. Ensure the accuracy of the ground truth of FIOVA, and ensure that the evaluation metrics can truly reflect the model's capabilities based on the ground truth.
2. Include more LVLMs for experiments and conduct in-depth analysis, preferably summarizing directions to improve the long video description capabilities of LVLMs.
3. If possible, improve existing evaluation metrics to enhance their objectivity.
4. There are still many typos in the text, one of the most obvious being that the evaluation metric proposed by Wang et al. (2024) is AutoDQ, not AutoCQ.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors of the paper investigate whether large vision-language models (LVLMs) can describe videos as comprehensively as humans. To facilitate the investigation, the authors propose a benchmark, FIOVA, designed to evaluate the differences between captions from LVLMs and humans, with 3,002 videos (averaging 33.6 seconds) that cover diverse scenarios.

Using the FIOVA benchmark, the authors conducted an in-depth evaluation of six state-of-the-art LVLMs (VideoLLaMA2, LLaVANEXT-Video, Video-LLaVA, VideoChat2, Tarsier, and ShareGPT4Video), comparing their performance with humans.

### Strengths
1. FIOVA is unique and important for advancing video-language models further. Each video in FIOVA is annotated by five distinct annotators, establishing a robust baseline that, for the first time, comprehensively represents human understanding in video description tasks.

2. In-depth evaluations of six open-source SOTA models were performed, and details of the algorithms and implementations were provided.

3. Many useful insights are provided through fine-grained evaluation and analysis. For example:
- Current LVLMs still struggle with information omission and descriptive depth.
- Different LVLMs employ varying strategies for video captioning—some prioritize completeness, while others focus on accuracy.
- For videos that are relatively easy to describe, the models show significant variability in performance. In contrast, for more challenging videos, their performance becomes more consistent.
- Significant discrepancies exist between LVLMs and humans in complex videos, particularly where human annotators exhibit substantial disagreement, whereas LVLMs tend to rely on uniform strategies for challenging content.

### Weaknesses
LLM hallucination and detail omission issues may be present in the ground truth description of each video, as the ground truth for each video is generated by an LLM, GPT-3.5-turbo, which synthesizes the five human-provided descriptions into a single, comprehensive video description. The use of an LLM for this integration is concerning because LLMs are prone to generating content not present in the source material, and they lack direct access to visual information, potentially leading to inaccurate summaries. The LLM-based integration process may introduce new hallucinations, which is concerning given that FIOVA serves as an evaluation benchmark. The quality of the final, integrated ground truth is a significant concern, particularly because the LLM may not accurately resolve conflicting information in the five human captions. For example, in Figure 4, Human3 notes that the little boy cries at the end, while Human5 states that the boy smiles at the end. Since an LLM cannot 'see' the video, it may simply guess or generate a description that does not accurately reflect the video content. This is further compounded by the fact that the five human annotators may have differing levels of expertise or may have focused on different aspects of the video, leading to a ground truth that may not be truly representative of the video's content. 

Additionally, using an LLM instead of a VLM to summarize the five human captions is insufficient because an LLM cannot properly handle conflicting information in the five human captions. For example, in Figure 4, Human3 notes that the little boy cries at the end, while Human5 states that the boy smiles at the end. Since an LLM cannot 'see' the video, it may simply guess that the boy smiles at the end. Furthermore, the method described in Section 2.2 appears to be adapted from the Video-ChatGPT evaluation metrics, with slight modifications to the prompts and the removal of the reference caption. The lack of a reference caption is concerning. For instance, the definition of "Detail Orientation" is "Whether the description captures critical details," and the definition of "Temporality" is "Whether the description follows the chronological order of events without skipping or over-summarizing." Without a reference caption, it is unclear how GPT-3.5 can evaluate whether the provided human caption captures critical details or follows the correct chronological order. The reliance on an LLM for these evaluations, without a visual grounding, raises concerns about the validity of the analysis in Section 2.2.

### Questions
1. Were the same five distinct annotators used to annotate all 3,002 videos? I assume the answer is 'No.'

2. What are the sources of the videos? 

3. How do you collect and process the videos in order to obtain and control the resulting varied video complexity?

4. How does the GPT-summarized caption affect the distributions shown in Figure 3?

5. Line 306 states that each model was fine-tuned for video caption generation. Do you mean you further fine-tuned these models? On which dataset was the fine-tuning performed?

6. When the SOTA models were evaluated, 8 frames per video were used. Were 8 frames sufficient for FIOVA? Did the human annotators watch the actual video files, or were they presented with sampled frames?

7. AutoCQ only provides event-level evaluation. Why were the five dimensions (e.g., consistency, context, etc.) from Sec. 2.2 not considered in the model response evaluation metrics?

8. It appears that the comparison of an LVLM against humans is conducted by comparing the LVLM’s response with the GPT-synthesized human caption summary in the main paper. However, in the image-language domain, having multiple human annotators for each image is not new (e.g., COCO captions include 5 human captions per image), and researchers often compare a model’s caption with each human caption individually, then aggregate the metric values (e.g., averaging the 5 metric values obtained by comparing with each human caption). Is there a reason for not taking this approach?

9. In Table A.3 in the Appendix, comparing the model's response with the GPT-synthesized human caption summary tends to produce higher metric values than directly comparing the model's response with a single human caption. Do the authors have any comments or insights regarding this observation?

Minor comments:
In the qualitative results shown in Figures A12–A17, it would be helpful to highlight any hallucinated content in the model responses.

### Soundness
3

### Presentation
3

### Contribution
4
