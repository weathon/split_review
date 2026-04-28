# MMEval: Evaluating Video Generation Models for Motion Quality

- Decision: Reject
- Avg Score: 4.50
- Scores: 3, 5, 5, 5

## Abstract
Recent advancements in video generation, especially with diffusion models, have led to new challenges in evaluating the generated outputs, highlighting the need for well-curated evaluation metrics and benchmarks. While prior work has focused on assessing text-to-video models for overall video quality, such as temporal coherence and prompt consistency, they overlook a crucial aspect: motion modeling abilities of generative models. To address this gap, we propose a structured approach to evaluate image-to-video generation models, with a focus on their motion modeling abilities. For example, we assess how accurately models generate motions like "circular movement for a rotating ferris wheel" or "oscillatory motion for a pendulum". We categorize videos  into linear, circular, and oscillatory motion-types and formulate metrics to capture key motion properties for each category. Our benchmark, MMEval, along with the code and image-prompt-video sets, will be publicly released.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes an evaluation method to assess the quality of generated videos, focusing specifically on motion modeling performance.

### Strengths
1. It introduces a set of quantitative scores to evaluate the motion quality of generated videos.

### Weaknesses
 **Weaknesses/Discussion:**

1. The core issue is that the proposed metrics calculate certain quantities based solely on the generated videos. These scores are specific to particular motion properties within the video. How can we use these scores to conclusively determine if the generated videos are good or bad? Ideally, a conclusive metric would indicate quality with a clear interpretation—for example, "the higher, the better." The lack of a clear, universally interpretable scale makes it difficult to use these metrics for direct comparison or to establish absolute quality benchmarks. The metrics, as they stand, seem more like motion descriptors than quality indicators.

2. Compare the proposed method with FVMD [1], a recent metric that also focuses on motion evaluation.

3. Why use discrete classifications based on motion type? Is this approach comprehensive and universal? The use of discrete classifications, such as linear, rotational, and oscillatory, may not fully capture the complexity of real-world motions, which often involve combinations and transitions between these categories. The method needs to justify why these specific categories are sufficient and how it handles videos with more complex motion patterns.

4. The typographic presentation of equations needs improvement. It is recommended to avoid italic fonts for text descriptions within equations, and many symbols remain unexplained after appearing in equations. The lack of clarity in the equations hinders understanding and reproducibility. For instance, the specific meaning of variables and their units should be explicitly defined.

5. Provide more visualizations of different motion types within the main text.

6. The evaluation pipeline uses several pre-trained models, such as RAFT, GroundingDINO, and the ViT-B/32 CLIP model. Does this make the evaluation pipeline slow? How efficient is it?

### Questions
See above.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a structured approach to evaluate image-to-video generation models, with a focus on their motion modeling abilities. Specifically, it categorizes videos into linear, circular, and oscillatory motion-types and formulates metrics to capture key motion properties for each category.

### Strengths
1. It classifies videos by various motion types like linear, rotational,oscillatory, and propose category-specific evaluation metrics.
2. It analyzes three essential motion characteristics, such as smoothness, direction, and speed, which along with the overall quality of the video to identify the strengths and weaknesses of image-to-video models.

### Weaknesses
1. The evaluation is limited to static cameras and lacks camera motion, which is also important in video generation.
2. The evaluation is restricted to image-to-video models and does not assess text-to-video models, which typically can generate more dynamic actions.

### Questions
As seen in weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes MMEval, a benchmark to evaluate motion in image-to-video generation. The benchmark rigorously splits motion into different types and design metrics for each type. There are three major types: linear, rotational, and oscillatory, and some sub-types for some of them. 1000 ground truth videos are collected to reflect these motions and serve as references for inference or evaluation. Extensive benchmark results on several models are presented.

### Strengths
- The paper focuses on evaluating motion in generated videos, which is the most important aspect of video generation.
- The paper makes huge efforts to rigorously categorize motion into different types and control the changing factors in a video to collect many ground truth videos. 
- The paper also makes great efforts to design metrics for each of the motion types and present the interpretability of the metrics.

### Weaknesses
 - I am unsure if the types of motion considered in this paper are broad or general enough for the community's interests. It seems to me that the community is more concerned about open-domain motion that could happen on any object or come from any dynamics. It's hard for me to imagine what ground truth videos would look like for some of the types, e.g., linear motion - rigid bodies or Oscillatory Motion - Large/Small Displacements -- no example videos are shown throughout the whole paper. The benchmark targets only image-to-video generation but also requires the model to accept text prompts. While I appreciate the attempt to categorize these motions and design dedicated metrics for each, I am not convinced by the scope and reliability of the benchmark. 
- I am not sure whether the designed metrics can generalize to any videos of the same type. It seems that there are many assumptions made explicitly and implicitly. For example, no camera motion is allowed in the video. Fluid motion is assumed to have no shape change (also see my questions below). The assumption of static camera severely limits the applicability of the benchmark to real-world scenarios, where camera motion is common. Furthermore, the assumption of no shape change in fluid motion is a strong constraint that may not hold true for many fluid dynamics, such as splashing or turbulent flows. These assumptions raise concerns about the benchmark's ability to evaluate the full spectrum of motion generation capabilities.
- Experimental results are questionable. 
  - No human correlation was reported. I am not sure about the reliability of the metrics. The lack of human evaluation makes it difficult to ascertain whether the proposed metrics align with human perception of motion quality. Without such validation, the metrics' practical relevance is uncertain.
  - Sometimes, metric scores of the ground truth videos are lower than the generated videos, e.g., in Tables 3, 4, and 5. This is not possible as SOTA video generators are still far from realistic. The fact that generated videos sometimes outperform ground truth videos on the proposed metrics is a major red flag, suggesting that the metrics may not be measuring the intended aspects of motion quality. This undermines the credibility of the benchmark.
  - As mentioned above, all these metrics are too specific to certain types or sub-types of motions. As a result, there are too many values to report for the whole benchmark. It is hard to grab the main focus of the experiment results with so many different tables and aspects. The excessive number of metrics and their specificity to narrow motion types make it challenging to draw meaningful conclusions from the experimental results. A more holistic approach with fewer, more generalizable metrics would be beneficial.
- Writing could be improved:
  - The reference format does not follow the requirements throughout the whole paper. 
  - Notation could be improved: e.g. i_{gen_0} -> i^{\text{gen}}_{0}. What is x_{1_0}, x_{2_0}...? What is \tilde{S}_{k} in line 220?
  - Please avoid abuse of in-line equations as they sometimes impede understanding and are inconvenient to refer to.
  - CLIP-Temp is not new. It is also called cross-frame consistency. Please see Runway's Gen-1 paper. 
  - No visualization of ground truth images/videos or generated videos. 
  - Please highlight the best performance in the tables. Please annotate the trend of the metric values in the tables.

### Questions
- For fluid motion, mask_0 is applied to all frames, which assumes that fluid will maintain the same shape across frames. Why is that reasonable?
- Line 209 states that *However, note that it is crucial to also check motion magnitude, as a still video may exhibit a high F C − Score despite no actual motion*. Does that mean the proposed FC-Score has flaws and cannot distinguish still videos from dynamic videos?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper tackles the evaluation challenges in video generation, particularly regarding motion modeling, which has been overlooked in existing metrics. The paper proposes a new benchmark, MMEval, focusing on three motion types: linear, rotational, and oscillatory. They develop specific metrics to assess motion properties like smoothness, direction, and speed. MMEval consists of 1,000 curated image-video pairs and about 5,000 image-prompt pairs, providing a comprehensive evaluation framework. The results indicate that while some models perform well in specific motion types, none excel across all categories, especially in linear motion of rigid bodies or rotational movements. This work aims to enhance the evaluation of video generation models by emphasizing motion modeling.

### Strengths
1.	This is the first work to focus on the evaluation of motion modeling in video generation task, offering a new perspective.

### Weaknesses
1.	MMEval has the limitations of static camera, single object and no object interactions.
2.	The paper does not explain the rationale behind the design of each metric. It also does not analyze the effectiveness of the various metrics, or prove the alignment of the metrics to the human preference.
3.	In practice, it is complex to evaluate the overall performance of a model with too many scores. Although evaluating various dimensions of motion modeling is reasonable, the paper does not provide advice or insight on how to combining various scores or how evaluate the motion with an overall metric. CLIP-Score and CLIP-Temp are not enough, since they have no direct relation between other scores.
4.	Lack of the visualization of videos with corresponding scores.

### Questions
1.	Is there some evidence to validate the effectiveness of each score?
2.	Are there some insights on overall evaluation of motion modeling?

### Soundness
3

### Presentation
3

### Contribution
2
