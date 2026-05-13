# Large Language Models Are Natural Video Popularity Predictors

- Decision: Reject
- Scores: 6, 3, 3

## Abstract
Predicting video popularity is typically formalized as a supervised learning problem, where models classify videos as popular or unpopular. Traditional approaches rely heavily on meta-information and aggregated user engagement data, but video popularity is highly context-dependent, influenced by cultural, social, and temporal factors that these approaches fail to capture. We argue that Large Language Models (LLMs), with their deep contextual awareness, are well-suited to address these challenges. A key difficulty, however, lies in bridging the modality gap between pixel-based video data and token-based LLMs. To overcome this, we transform frame-level visual data into sequential text representations using Vision-Language Models (VLMs), enabling LLMs to process multimodal video content—titles, frame-based descriptions, and captions—and capture rich contextual information for more accurate predictions. Evaluating on a newly introduced dataset of 17,000 videos, we show that while a supervised neural network using content embeddings achieved 80% accuracy, our LLM-based method reached 82% without fine-tuning. A combined approach, integrating the neural network's predictions into the LLM, further improved accuracy to 85.5%. Additionally, the LLM generates interpretable hypotheses explaining its predictions based on theoretically sound attributes. Survey-based manual validations confirm the quality of these hypotheses and address concerns about hallucinations in the video-to-text conversion process. Our findings highlight that LLMs, equipped with textually transformed multimodal representations, offer a powerful, interpretable, and data-efficient solution to the context-dependent challenge of video popularity prediction.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
1. The paper addresses a new video popularity prediction task of distinguishing between globally and locally popular content.
2. The authors develop a Video Popularity Dataset (VPD)  of 17,000 YouTube videos, with titles, descriptions, and detailed metadata, along with the countries the video was trending in amongst 109 countries.
3. The authors transform video content into textual representations using Vision-Language Models (VLMs) to bridge the modality gap between video data and LLMs. 
4. The authors test extensively on prompting paradigms for the video popularity prediction task, including Thinking, ICL, Hypothesis generation, and supervised signal into the prompt.

### Strengths
1. The paper introduces a new dataset and task for local and global popularity prediction.
2. The insights like reach vs popularity, ablation studies, are useful.
3. The authors conduct human studies to verify video verbalization and hypothesis generation.

### Weaknesses
1. The frame-to-text method is not novel, there are multiple works [1,2,3,4] that use titles, channel, generated visual captions, ASR of youtube videos for tasks like Views, Likes/Views, replay predictions [2,3,4].
2. There is no explanation of the 17k videos and metadata collection, one subsection on the tools and data sources is necessary.
3. The dataset consists of only global and local hits, and not negative samples, looking at locally/globally popular videos from the examples (and https://kworb.net/youtube/trending_overall.html#google_vignette , since any other source was not mentioned in the paper) there seems to be a huge language bias (Hindi/Korean/.. languages being local hits)
4. The human evaluation is not signifcant for both tasks,14,11 subjects passed the screening and they were only given 2 video-caption pairs, totalling 28, 22 interactions only.
5. The technical contributions are severely limited, the authors only show combinations of known prompting strategies for evaluation.

### Questions
1. What steps were taken to filter the videos for this dataset? Languages, Tags
2. How was the dataset collected
See weaknesses

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents an approach to predicting video popularity using LLMs. The authors argue that traditional methods, which rely on meta-information and aggregated user engagement data, fail to capture the contextual nuances that influence video popularity. To address this, the paper introduces a method that transforms visual data into sequential text representations using VLMs, allowing LLMs to process multimodal content. The authors evaluate their approach on a new dataset of 17,000 videos and demonstrate that their LLM-based method outperforms supervised neural networks and provides interpretable hypotheses for its predictions.

### Strengths
1. The paper propose an innovative use of VLMs to transform visual data into text, enabling LLMs to capture rich contextual information from video content, which traditional methods often overlook.

2. The proposed method achieved higher accuracy rates compared to supervised neural networks, with an 82% accuracy without fine-tuning and an 85.5% accuracy when combined with a neural network, showcasing the potential of LLMs in this domain.

3. The paper not only focuses on prediction accuracy but also on the interpretability of the predictions. The LLM generates hypotheses that explain its predictions, adding a layer of transparency and trust in the model's output.

4. The introduction of the Video Popularity Dataset, which includes a large number of videos with detailed metadata, view counts, and global reach metrics, is a significant contribution to the field.

5.  By considering both engagement intensity and geographic spread, the paper offers a more comprehensive understanding of video popularity than previous studies that focused solely on view counts.

### Weaknesses
The following are comments that combine my suggestions and PC's feedback for my suggestions! Thank you, PC!

1, It would be great for the authors to elaborate on the broader implications and potential applications of their work beyond just video popularity prediction. For example, you could ask how the techniques developed here might generalize to other multimodal prediction tasks, or how the interpretable hypotheses generated by the LLM could be applied in other domains requiring explainable AI. 

2, From machine learning perspective, It would be great for the authors to provide a more detailed comparison with existing multimodal fusion techniques or  elaborate on the specific innovations in your approach, such as how the VLM-to-LLM pipeline differs from traditional multimodal fusion methods, and what unique challenges they addressed in combining visual and textual data for this particular task. It would be also great to highlight the broader lessons or insights about multimodal fusion that can be drawn from their work.

### Questions
Please answer the question from the weakness part and I would be happy to discuss with the authors about the questions and change my score if necessary.

### Soundness
2

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
Previous approaches aiming at video popularity prediction have only considered engagement intensity, that is view count. However, due to cultural, social, and temporal factors, a video that is popular in one region may not be popular in another. Taking account of this, this paper proposes considering both view count and the number of countries a video has trended in (geographic spread) for predicting video popularity. With a well-designed sequential llm prompting method and hints from a supervised model, the proposed method predicts video popularity taking as input only the intrinsic video content, including title, description, caption and video frames. The empirical results show that how the proposed method improves over a supervised baseline model on a newly collected dataset, Video Popularity Dataset (VPD).

### Strengths
- Considering both engagement intensity and geographic spread makes sense.
- The authors collected a valuable dataset, VPD. This would foster future work.
- The empirical results explicitly show the improvements from the hybrid approach using both llm prompting and supervised signals for video popularity prediction.

### Weaknesses
This paper has the following issues:

1. The authors did not compare the proposed method with any previous approaches.
2. The main contribution of this paper is its consideration of geographic spread - how many countries a video has trended in - as well as engagement intensity, that is view count, in measuring video popularity. However, they seem to be quite orthogonal to me, but the authors used only a single score integrating both two factors. I am not sure why they used separate scores measuring each. Especially, While the authors mentioned in section A.3 that there is a positive correlation between them, but according to Figure A2, there are also non-negligible number of videos categorized into "locally ultra popular" and "globally moderately popular".
3. The writing needs to be improved. There are many redundant sentences aimed at increasing the length of the paper. For example, Section 5 contains too redundant statements about the hybrid approach using both llm prompting and supervised signals. Furthermore, there are too many cases where figures or tables contradict the text. To name a few, in Section A.3.2 (L803), the authors mentioned that the upper-right quadrant in Figure A3 is less populated than the lower-left quadrant, which contradicts the fact that there are 6,279 local hits videos and 7,360 global bit hits videos. There are also no 0.83 in Table A4 (L1187); the highest score is 0.78. The authors should also fix typos, e.g., please fix "red lines" in the Figure A3 caption to "blue lines". Overall, it feels as though the authors have submitted an unfinished draft that hasn’t been proofread.
4. There are too many missing details
- How did the authors differentiate the videos of classes 1 and 2 in the local hit cluster and the videos of classes 3 and 4 in the global big hit cluster? There are two defining factors, geographical spread and view count, and I am not sure about how they are integrated into a single score.
- The authors did not mention the training recipe and data for the supervised baseline model.
- L299: Please elaborate on the hypothesis generation function Phi_hypothesis, especially regarding the reinforcement learning technique used for it, if any (Section 5). And how many hypotheses are used for prediction?
- Please provide the exact final prompt text.
- How did the authors screen participants in the surveys?
- And please let me know exactly what questions were asked to the participants in the survey to score each metric.
- L508 "This feature enhances not only the performance but also the explainability of the model": This statement is not explicitly validated in the paper. The authors used only accuracy and precision/recall for evaluation.
5. While the authors claim that the main contribution lies in considering both geographic spread and view count for video popularity prediction, the model does not need to consider both factors to solve the given binary classification problem; you can get the correct answer by predicting either the view count or the geographic spread. The experimental setup, therefore, does not validate the core claim of the paper.

### Questions
Please address the above concerns and I have the following suggestions:

1. It would be good to explicitly mention in the abstract that the model predicts geographic spread as well as view count.
2. It would be great to ablate the model design choice for each component. One of them would be replacing the MPNet base v2 model with other recent models to generate embeddings for retrieving near examples (L289-290).
3. Figure 1 does show the entangled improvement from both 10-nearest examples and hypothesis generation. Even though Figure A8 compares the results of 1-nearest example and 10-nearest examples, it would be great to add the result with 10-nearest example only also to Figure 1.

One minor question:
L185-L186: I am not sure whether sampling an equal number of videos from each class is appropriate for testing; it does not reflect the real-world video distribution.

### Soundness
2

### Presentation
1

### Contribution
3
