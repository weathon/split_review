# CG-Bench: Clue-grounded Question Answering Benchmark for Long Video Understanding

- Decision: Accept
- Avg Score: 6.20
- Scores: 5, 6, 6, 8, 6

## Abstract
Most existing video understanding benchmarks for multimodal large language models (MLLMs) focus only on short videos. The limited number of benchmarks for long video understanding often rely solely on multiple-choice questions (MCQs). However, because of the inherent limitation of MCQ-based evaluation and the increasing reasoning ability of MLLMs, models can give the current answer purely by combining short video understanding with elimination, without genuinely understanding the video content.
To address this gap, we introduce CG-Bench, a novel benchmark designed for clue-grounded question answering in long videos. CG-Bench emphasizes the model's ability to retrieve relevant clues for questions, enhancing evaluation credibility. It features 1,219 manually curated videos categorized by a granular system with 14 primary categories, 171 secondary categories, and 638 tertiary categories, making it the largest benchmark for long video analysis. The benchmark includes 12,129 QA pairs in three major question types: perception, reasoning, and hallucination.
Compensating the drawbacks of pure MCQ-based evaluation, we design two novel clue-based evaluation methods: clue-grounded white box and black box evaluations, to assess whether the model generates answers based on the correct understanding of the video.
We evaluate multiple closed-source and open-source MLLMs on CG-Bench. Results indicate that current models significantly underperform in understanding long videos compared to short ones, and a significant gap exists between open-source and commercial models. We hope CG-Bench can advance the development of more trustworthy and capable MLLMs for long video understanding.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a newly collected dataset that is intended for evaluating long-video (10min+) understanding capability of current models. The key is to introduce clue-grounded questions as question-answer-clue triplet, to minimize the possibility of models "cheating" by combining short-video understanding and elimination to "answer correctly" without genuinely understand long videos. The dataset contains 1219 manually selected videos and 12K QAC triplets with fine-grained category annotations. The authors also designed two clue-based metrics as complementatry to the multiple-choice accuracy metric, to better assess whether model understands the video before they can answer correctly. The authors evaluated the proposed dataset with multiple open-sourced and commercial LLMs and showed that existing LLMs still have much room for improvement on this novel dataset.

### Strengths
* Originality 

For long video understanding, the lack of appropriate benchmark dataset has been a main problem for properly evaluating modeling progress, and actually many concurrent work is aiming for filling this gap. This paper presents a novel dataset with high quality (human annotation) and novel setup (clue-guided), essentially a finer-grained segment-level annotation, which enabled more possibility such as the finer-grained evaluation (the two clue-based evaluation metrics). The idea is not entirely new but the dataset can be highly impactful for the community.

* Quality

The dataset is curated in mutiple rounds with a lot of human efforts, and the authors have done extensive experiments with modern MLLM models as well as human evaluations to prove its usefulness. 

* Clarity

The paper is well-written and is rather easy to follow.

* Significance

The proposed benchmark dataset could be a useful addition to the community.

### Weaknesses
 * In L151 the authors mention that videos are manually collected from Internet to "avoid using videos that have been used for pre-training", but no details is provided. Actually I'm curious how this can be guaranteed. Is it done by license? The human-annotated QAC might be novel but I feel it's hard to ensure that Internet videos are excluded from LLM pre-training.

* I fully understand the difficulty (e.g. high requirement for hardware) to evaluate long videos especially some long-tailed videos (longer than 60min), but using 16/32 or even 128 frames probably is far from enough. One possible mitigation is to perform human eval under the same constraints, e.g. only feeding human with 16/32 frames and ask them to answer the question. This probably can give a more informative sense about how challenging the dataset could be. Also it would be great to have finer-grained analysis, e.g. grouping video/questions based on the duration (10min, 10-20min, etc.) and show how severe the "undersampling" issue is for longer video. Actually this could be a quite important missing ablation.

* The two proposed metrics (white-box and black-box evaluations) are intuitive but really simple; it feels more like some analysis to provide insights but not as novel, e.g. the white-box evaluation is clearly an extension from video temporal grounding. Also even though the authors claim the acc@IoU to be a combined metric, but since $\tau=0$ it's effectively degraded to MCQ accuracy. A naive solution would be to predict the full video span as the clue, which would always satisfy the overlap condition, thus rendering the temporal aspect of the metric meaningless.

### Questions
* See my comments about weakness for questions.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces CG-Bench, a benchmark for assessing multimodal large language models on long video understanding, moving beyond traditional multiple-choice questions (MCQs). CG-Bench emphasizes “clue-grounded” question answering by focusing on models' ability to retrieve relevant video segments that support accurate question answering. The dataset includes 1219 long videos annotated with over 12K Q&A pairs spanning categories like perception, reasoning, and hallucination. CG-Bench not only support standard evaluation metrics such as accuracy, but also incorporates two novel metrics for credibility to measure the reliability of model predictions: (1) white-box evaluation, where models need to identify specific intervals related to questions, and (2) black-box evaluation, which measures the discrepancy in model performance when with access to the full video compared to solely relying on the clue interval.

### Strengths
- Originality:  The paper presents CG-Bench, a new benchmark specifically designed for clue-grounded question answering in long video understanding, which fills a notable gap in multimodal large language model (MLLM) evaluation on video understanding. In addition, the paper also proposed two novel metrics for measure reliability of model predictions specifically to the clue-grounded QA scenario in CG-Bench. 
- Quality: The quality of this work is reflected in the construction of the dataset, with 1,219 long videos, over 12,000 Q&A pairs, and a detailed three-tier tagging system, ensuring comprehensive coverage across categories like perception, reasoning, and hallucination. 
- Clarity: The paper is easy to follow.
- Significance: The proposed benchmark has great potential for MLLM research, as it exposes the limitations of current models in long video comprehension and sets a new standard for assessing MLLMs in real-world, temporally extended contexts.

### Weaknesses
The paper can be improved by incorporating more details regarding the construction of the benchmark, and more thorough evaluation of existing models to provide more insights on how and why existing models fail to solve CG-Bench, to inspire future works. Please refer to the Questions section for detailed concerns.

### Questions
- What is the distribution of the resolution of the raw videos used in this dataset?
- Can the authors provide more details about the video collection process? How to prevent the videos from overlapping with the pre-training data of existing MLLMs, especially if they are collected from the internet? The reviewer would imagine this as a difficult process especially with closed source models.
- As subtitles are provided with the videos, are all subtitles human uploaded or machine transcribed? Are all subtitles in English? 
- The reviewer is also curious about how the performance of both closed-source and open-source MLLMs can be affected by (1) the frame sampling strategy (e.g., uniform vs. key frames) and (2) the frame resolution (as it also affects how many frames can be fit in memory for open-source MLLMs given the computational limit). 
- For Black-Box Evaluation, the authors claim that "a model with access to the full video should yield higher accuracy compared to solely relying on the clue interval.". The reviewer find it a little counter-intuitive, though the full video may contain more information, however, it is a harder task (even for human) to search for the clue first then answer the question, than answer the question with clue provided. 
- How to think of the white-box credibility measures especially when the meta information such as timestamps is not available to the model?  For example, evaluation setting with only frames as inputs (F in Table 4), the accuracy is on par or slightly higher than the setting with both frames and frame time prompt (F+FT in Table 4), while the scores for white-box evaluation are significantly lower. 
- Regarding the quality control process, especially for the "small model & sparse frame check" step, can the authors provide more insights in terms of what kind of questions are being filtered?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper propose a new video language question-answering evaluation benchmark, featuring that each QA pair is grounded into a time interval. The QA and the time interval (as clues for the question) are manually annotated by human raters which are useful to answer the question. Having the correct time interval prediction ensures the MLLM finds the correct evidence to answer the question. The authors propose a various set of evaluation metrics, including overall QA accuracy, QA accuracy given ground truth time intervals, time intervals prediction IoUs, and GPT-guided open-ended evaluation. The authors evaluated a wide range of existing MLLMs and observed performance gaps between the models.

### Strengths
- The problem of evaluating multi-modal large language model is important, and I believe this paper provided a unique perspective of evaluating the temporal grounding for video question answering.

- The authors provided a comprehensive set of evaluation metrics which all make sense to me. The clue-acc, long-acc, and CRR metrics smartly shows how the model leverage temporal information without explicitly look at temporal grounding prediction. I also like how the authors use GPT-4o as a guide with optional visual inputs to save evaluation budgets.

- The authors evaluated a wide range of existing MLLMs (Table 3) and ablated several interesting settings (Table 4 and Figure 7), with interesting insights (e.g., how the models take use of more frames, how additional modality helps).

- The fact that Audio does not help much of the dataset is a good surprise to me, where I was under the impression that many existing long video datasets are heavily ASR-biased.

- I like the fact that the authors collect videos and questions all from scratch rather than reusing existing datasets or create by using LLM. This is important to reduce biases in existing datasets.

### Weaknesses
 - The mIoU scores in Table 3 for most models are low (<9%), and even the human performance is only 35.5%. This raises a question that how reliable are these temporal interval annotations are. At a high level, a model does not need to look at all frames within the interval to gather the necessary information, but only a few frame or a much smaller interval is sufficient. Therefore metrics like recall may help here (this is optional for the rebuttal).

- Following the above comment, it is unclear to me how good the current MLLMs are at following the specific output format instruction in supplementary Line 552 "Question-Clue Grounding". It will be helpful if the authors report how often the case "Any output that does not conform to this nested array format will be considered incorrect" happens, to get a better understanding of why mIoUs are low.

- Since the authors collect the videos manually, please make sure there are no license issues of releasing the videos.

### Questions
Overall this paper puts good effort in an important direction, with solid dataset designs and experiments. I have some concerns on the mIoU evaluation as discussed in paper weakness, and expect the authors to reply them. My current rating is a week accept, and I am happy to further raise the ratting in my concerns are addressed in the rebuttal.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces a new benchmark dataset for long video understanding called CG-Bench. In contrast to the few existing long video benchmarks, CG-Bench includes new metrics (white box and black box) that not only measure its ability to answer multiple choice questions, but also the models’ ability to ground its answer in the video by providing time intervals containing clues to the answer. With >12k multiple choice questions, the dataset is the largest of its kind and is fully manually annotated. It includes videos from a wide variety of domains, making it suitable for predicting model performance in many real-world applications. The paper provides an evaluation of >20 models, both open and closed source, across several metrics, providing interesting insights into the state of the art in long video understanding.

### Strengths
* There is a large gap between benchmark scores and human performance, showing that there is plenty of room for innovation.  
* CG-Bench is the largest long video understanding benchmark to date.  
* The ground truth is fully manually annotated.  
* Good video lengths: 10-60 mins with mode around 20 mins.  
* Good variety of video types and question types.  
* The Evaluation of \>20 current methods is a good reflection of the SotA in long video understanding.  
* Clue based credibility evaluation is a great contribution to video understanding metrics.  
* The paper is clearly structured and well written.

### Weaknesses
 * The source(s) of the videos are not disclosed and the collection process is not described in enough detail. It would be interesting to know what website(s) the videos come from, what search queries were used, and what the distribution of video types is. The paper says that videos were manually filtered, but filtering criteria were not mentioned. This information would be critical to understanding the composition and applicability of the benchmark. For instance, the presence of specific video styles, such as those with fast cuts or specific color grading, could significantly influence model performance, and knowing these details is crucial for interpreting the results. 
* Evaluations on closed-source MLLMs are only performed with up to 32 / 128 frames even though ablations show that performance keeps improving as more frames are used (Fig. 7). Note: Because cost might be a prohibiting factor here, and 128 frames are enough for the provided SotA analysis, I am not considering this shortcoming in my rating. If the benchmark gets publicly released, this could easily be done by groups with sufficient resources.
* Only three examples are provided in the text. It would be good to see a few more example questions from the benchmark, especially hallucination questions, to get a feeling for its quality and the difficulty of the questions. The current examples do not fully convey the complexity of the benchmark, and additional examples would help assess the variety of reasoning skills required to answer questions correctly.

### Questions
Overall I have no major concerns about this paper. I appreciate the effort the authors put into creating such a large and diverse benchmark and the contributions they are making to video understanding metrics. So I would recommend the paper for publication, but hope the authors could help answer my questions and fix the issues I found in the paper. Also a public release would be much appreciated by the community and increase the paper’s impact.

* Will CG-Bench be publicly released? This would be a major contribution and should be mentioned in the text.  (Though I understand links might need to be omitted due to anonymity reasons.)
* l. 161: Could authors describe what the “Hallucination” question type is and how its questions were designed? Some examples would be helpful too.  
* Fig. 5: Why is the clue coverage increasing almost linearly with the time bin index? Is there a reason that clues are more likely to be located towards the end of the video than the beginning?  
* l. 176 “To minimize expression loss, annotators use their native language during the annotation process.“ Are questions translated into English? If yes, how? If not, how many languages does the benchmark contain and what is their distribution?  
* Do the annotators have access to audio and/or subtitles of the video? If yes, were any measures taken to make sure the answers are grounded in visual content and not only in spoken / audio content?  
* l. 298: If \\tau is 0, doesn’t acc.@IoU degenerate to MCQ-acc? Is this a typo?  
* l. 305: “In other words, the accuracy of Long-Video MCQ (long-acc.) should be greater than or equal to the accuracy of Clue-based MCQ (clue-acc.).” This contradicts Tab.3, where clue-based accuracy is always greater than long video accuracy. Also the formula for CCC assumes that long video accuracy is smaller than clue based accuracy. My guess is that this is due to context dilution, i.e. the model not being able to extract relevant information when more irrelevant information is added to the context. So, CRR is actually a measure of robustness to context dilution and not a measure of the model’s ability to seek out clues outside the provided clue windows, as the “Black box evaluation” paragraph says. I would suggest rephrasing this paragraph accordingly.  
* l. 323: “To address this, we leverage a low-hallucination MLLM, such as GPT-4o” I’m curious why GPT-4o is called a low-hallucination MLLM. Is there any literature to back this up?  
* Tab. 3: Why are mIoU scores \> 1? According to Eq. 1, they should be \<=1.  
* Tab. 4:  
  * I was surprised that accuracy does not vary much as modalities are added. clue-acc changes from 66.0 to 66.5 and long-acc from 52.4 to 53.9 as subtitles and timestamps are added. I would assume that subtitles would give models a clear advantage since they are a strong semantic signal. Why do they have so little effect?  
  * It would be interesting to have an ablation that uses only subtitles and no frames.  
* Tab. 5:  
  * What is the unit for bias? What does a score of 1.0 mean?  
  * How are trigger rate and recall rate defined? This explanation could be expanded in the text.  
* Fig. 7d: GPT-4o’s CRR decreases at first and stays below other models until it catches up at 128 frames. I’m curious of authors have an explanation for this.  
* l. 458: What is the meaning of “refusal rate” here?  
* l. 464: “When evaluators were provided only with ground truth (GT) and visual information, the bias between human scores and model-based evaluations increased.“ Does this mean when only one of the modalities is provided?  
* l. 465: “While fully leveraging visual information improved evaluation accuracy \[...\]” What does “fully leveraging visual information” refer to here? Does this refer to the “GT+Vis” columns?

**Minor points:**

* l. 107: “Despite the continuous proposal of various MLLMs, their real-world performance in long video understanding is still unknown.” This statement is not entirely fair since other long video benchmarks such as Video-MME have provided evaluations of these models. I would suggest toning down the statement a little.  
* l. 192: “we align with annotators in real-time“ I am not sure I understand what this means.  
* l. 214: What are “option probabilities”?  
* In related work, it would help if all method/dataset names were mentioned alongside citations, e.g. Llava-Next (Zhang et al., 2024b).  
* In tables, please right-align numerical columns for easier comparison.  
* l. 232, use \\citep  
* l. 372: Tab. 3 has many more open source models. Maybe add “among others”.  
* Tab. 4: In row 2, long-acc column, the sign of the diff should be minus. In the following row, the diff is 1.0.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper focuses on the evaluation of MLLMs. The authors claimed that existing VideoLLM benchmarks merely focus on either short videos or black evaluation, i.e., simply leveraging MCQ accuracies to measure the model performance without further detailed analysis. Therefore, they proposed CGBench, a novel MLLM benchmark that not only requires the models to predict correct answers for MCQs, but also ground clues through predicting temporal boundaries. The CGBench was created by manually collecting videos and annotated by human annotators, ensuring high quality. Comprehensive evaluations on such a benchmark reveals the limitations of existing MLLMs.

### Strengths
1. Overall, the motivation is clear and reasonable: providing a more detailed evaluation for MLLMs rather than simply measuring MCQ accuracies.
2. The created benchmark seems to have good quality, as this was manually annotated by human annotators.
3. The evaluation settings (white box + black box) are reasonable and extensive, jointly provides a good starting point to encourage future research in this direction.

### Weaknesses
I have some minor concerns regarding the writing, comparison with existing work, and experiments.

1. The presentation about 'clue' is not very clear. To my understanding, this should be the temporal boundaries (represented by start and end timestamps) of the relative video segments that provide hints to correctly answer the question. If yes, it would be better to state such definition clearly in the main paper.
2. In table 2, a number of existing benchmarks/datasets that also contain the setting of QA + grounding are missing. Further discussion on the differences between CGBench and existing QA + grounding datasets (EgoTimeQA [1], MultiHop-EgoQA [2], ReXTime [3]) and a benchmark (E.T. Bench [4]) is required. And the methods proposed by these papers should also included in table 3, as they are specially designed for such settings.

### Questions
Please refer to the weakness part for my concerns and questions. In general, some further discussions shall be conducted.

### Soundness
3

### Presentation
2

### Contribution
3
