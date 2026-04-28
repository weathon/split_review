# Vision Language Models are In-Context Value Learners

- Decision: Accept
- Avg Score: 7.50
- Scores: 8, 6, 8, 8

## Abstract
Predicting temporal progress from visual trajectories is important for intelligent robots that can learn, adapt, and improve. However, learning such progress estimator, or temporal value function, across different tasks and domains requires both a large amount of diverse data and methods which can scale and generalize. To address these challenges, we present Generative Value Learning (\ourmethod), a universal value function estimator that leverages the world knowledge embedded in vision-language models (VLMs) to predict task progress. Naively asking a VLM to predict values for a video sequence performs poorly due to the strong temporal correlation between successive frames. Instead, \ourmethod poses value estimation as a temporal ordering problem over shuffled video frames; this seemingly more challenging task encourages VLMs to more fully exploit their underlying semantic and temporal grounding capabilities to differentiate frames based on their perceived task progress, consequently producing significantly better value predictions. Without any robot or task specific training, \ourmethod can in-context zero-shot and few-shot predict effective values for more than 300 distinct real-world tasks across diverse robot platforms, including challenging bimanual manipulation tasks. Furthermore, we demonstrate that \ourmethod permits flexible multi-modal in-context learning via examples from heterogeneous tasks and embodiments, such as human videos. The generality of \ourmethod enables various downstream applications pertinent to visuomotor policy learning, including dataset filtering, success detection, and advantage-weighted regression -- all without any model training or finetuning.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents Generative Value Learning (GVL), a novel technique that utilizes Vision-Language Models (VLMs) to serve as a value function. In particular, by shuffling the order of frames within the video and utilizing few-shot prompting, GVL exceeds the performance achievable using VLMs without shuffling and without temporal dependence. Furthermore, the authors demonstrate that, by comparing the GVL value estimates with the true frame order, it is possible to identify and filter out low quality video demonstration data. The authors demonstrate that GVL can be used to train more effective policies via both data filtering and more accurate value estimation.

### Strengths
Although the proposed technique is simple, it seems (based on myriad experiments) to be effective. Figure 2 demonstrates a clear superiority of GVL over LIV, the baseline that the authors chose to test, for text-based goals. Figure 4 demonstrates that GVL can be decently effective at predicting values correctly over more complex videos. Finally, GVL was effective at training agents via both (1) data filtering for imitation learning and (2) advantage estimation for advantage weighted regression.

Breaking things down by category:
- Originality: Due to the simplicity of this technique, I think the originality is somewhat low, however the method is effective, especially in comparison with other simple alternatives.
- Quality: With the exception of the potential circularity I mention below, the experiments performed seemed to be of high quality, and they seem to demonstrate the quality of this technique.
- Clarity: There were some minor questions that I have detailed below, but for the most part, the paper was well-written and easy to understand.
- Significance: The authors provide solid motivation for the significance of this technique by demonstrating how it could be used for model training and dataset quality checks.

### Weaknesses
The use of Value Order Correlation (VOC)—the correlation between GVL and frame order—seemed somewhat circular. It is used on the OXE dataset to judge GVL’s performance, a choice that assumes that the contents of OXE are of sufficient quality. (If, for instance, OXE contained many sub-optimal trajectories, an ideal value estimator would show low VOC.) Later, there is a discussion about the use of GVL+VOC to identify sub-optimal datapoints/subsets within OXE. This seemed confusing to me since it seemed to contradict the earlier assertion that OXE was of sufficient quality for judging GVL. 

It would be good to see more analysis regarding GVL’s ability to accurately estimate values in videos where repetition is present. Currently, the existence of such an ability has to be inferred from downstream effects (e.g., the ability to use GVL for data filtering helps during imitation learning). It is not entirely clear if GVL is truly evaluating the quality of observations, or if it is simply learning to output a linear ordering of frames given the shuffled input. While the case studies provide some intuition, a more systematic evaluation is needed to confirm GVL's ability to handle non-monotonic progress.

### Questions
- It would be great to see LIV’s performance on the ALOHA dataset. I assume that, since GVL outperformed LIV on OXE, it would do so again on ALOHA, but it would be nice to see these results formalized.
- What is ALOHA-13? I see the descriptions of ALOHA-250, but I don’t see the same for ALOHA-13 for some reason.

### Soundness
3

### Presentation
4

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
The paper presents a method that enables existing VLMs to understand the task progress/completion, that could help in the use cases like dataset filtering, success detection and visuomotor control/policy learning. The authors also propose an autoregressive value prediction instead of the traditional bellman returns.

### Strengths
Pros:
1. The high-level of the paper is easy to understand because of the effort that the authors took to portray it on the figures.
2. The experiments that were performed to evaluate the method are easy to see how the proposed method is better than the baseline/(baselines in some cases).

### Weaknesses
Weakness
1. Currently, the block diagram only provides a high-level idea of what the paper is about, which is good. But it would to nice to have the language component of the model. For example, I get that you are trying to predict the value estimate of a frame, but without the task description, it’d be impossible to predict whats the value estimate.
2. The experiments are very limited, although the use cases are diverse enough. In each of these use cases, however, the comparisons are quite restricted. My understanding is that you are using a policy that is learnt on the downstream task. There are so many representation learning works that do that and I urge the authors to find more recent baselines for the use cases, especially, for the visuomotor control
3. Why are the authors not comparing with LIV on the visuomotor tasks?
4. Is there a plot/table that shows how much incorporating observation shuffling helps or using autoregressive value prediction helps than the traditional bellman returns? I think this is important to understand the efficacies of the 2 proposed incorporations

### Questions
Overall, I enjoyed reading the paper, but I'm just concerned with the strength of the experiment section. I'm willing to consider changing my score if the experiments section is made stronger.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents Generative Value Learning (GVL) a value function estimator for predicting task progress from visual trajectories. They show that without any task-specific training, their approach can in-context zero-shot and few-shot predict values for more than 300 real-world tasks across different embodiments. The approach is simple: autoregressive prediction, shuffle inputs, and provide in-context examples of task progress.

### Strengths
- Well motivated and set desideratas for a “universal value estimator”: accurately estimating state and consistency, highlighting the limitations of prior works
- Interesting finding; shuffling the video frames help mitigate the temporal bias found in videos ⇒ better value estimations
- Introduces a new evaluation metric: Value-Order Correlation which measures how well predicted values correlate with the ground-truth timestep in expert videos.
- Extensive evaluation of GVL’s value estimates across a large suite of real-world robot datasets with varying tasks and embodiments
- GVL can be applied to a wide variety of tasks such as dataset quality estimation, success detection, and weighted imitation learning.
- Good analysis and ablation studies to verify the importance of each component in the GVL approach and robustness to different environment factors.

### Weaknesses
 - The real-world results are not too impressive. Applying GVL to compute values only leads to a small improvement over the based diffusion policy baseline. It would be interesting to see more results showing how the value estimations of GVL help with downstream policy learning.
- Method itself is technically simple, but still well-motivated and supported with empirical results.

### Questions
- Can GVL be applied for online RL training?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper casts universal value estimation of video frames as a temporal ordering problem over shuffled video frames. To address this, the authors introduce Generative Value Learning (GVL), which leverages the world knowledge embedded in vision-language models (VLMs) to estimate task progress. Here, the value for each frame is represented as the VLM's prediction of task completion rate. Experimental results demonstrate that GVL can be effectively applied to various downstream tasks, using a Value-Order Correlation (VOC) metric that measures the rank correlation between the rank of estimated values and the original frame order.

Overall, I believe this paper is suitable for publication at ICLR, though there is room for further development, especially in the clarity of the writing.

### Strengths
- Framing value estimation as a temporal ordering problem over shuffled videos is a compelling approach.
- The proposed rank correlation metric is thoughtfully designed and well-suited to this problem setting.
- The experiments are extensive, covering a wide range of real-world tasks.

### Weaknesses
 - My primary concern is with the method's applicability. As I understand, calculating the value for each frame requires access to a complete video, which could limit its use in online policy learning without an offline dataset or expert demonstrations. This restricts the downstream tasks to scenarios where offline datasets are available, while the compared method [1] remains applicable in online policy learning. Specifically, the need for a complete video sequence to compute frame values makes it unsuitable for real-time decision-making in many robotic tasks, where actions must be taken based on the current observation, not the entire trajectory. This limitation significantly narrows the scope of potential applications compared to methods that can operate incrementally.
- The manuscript contains several typos and minor errors that should be addressed. I recommend a careful proofreading. A non-exhaustive list includes:
    - Line 163: missing comma.
    - Line 178: missing space after “2)."
    - Line 197: "meaningfully" should be "meaningful."
    - Line 393: "ataset" should be "dataset."

### Questions
- In Figure 1, some arrows are bidirectional. Replacing these with unidirectional arrows could improve consistency.
- In the Dataset Quality Estimation paragraph of Section 4.3, the reasoning feels incomplete. It may strengthen the experiment to directly train models with and without specific low-quality datasets and compare the resulting performance outcomes.

### Soundness
4

### Presentation
3

### Contribution
3
