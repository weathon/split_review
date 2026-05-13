# HandsOnVLM: Vision-Language Models for Hand-Object Interaction Prediction

- Decision: Reject
- Scores: 5, 6, 8

## Abstract
How can we predict future interaction trajectories of human hands in a scene given high-level colloquial task specifications in the form of natural language? In this paper, we extend the classic hand trajectory prediction task to two tasks involving explicit or implicit language queries. Our proposed tasks require extensive understanding of human daily activities and reasoning abilities about what is happening next given cues from the current scene. We also develop new benchmarks to evaluate the proposed two tasks, Vanilla Hand Prediction (VHP) and Reasoning-Based Hand Prediction (RBHP). We enable solving these tasks by integrating high-level world knowledge and reasoning capabilities of Vision-Language Models (VLMs) with the auto-regressive nature of low-level ego-centric hand trajectories. Our
model, HandsOnVLM is a novel VLM that can generate textual responses and produce future hand trajectories through natural-language conversations. Our experiments show that HandsOnVLM outperforms existing task-specific methods and other VLM baselines on proposed tasks, and demonstrates its ability to effectively utilize world knowledge for reasoning about low-level human hand trajectories based on the provided context.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
To avoid previous works which predict hand trajectories based on high-level language task command, this paper aims to extend the classic hand trajectory prediction task to two tasks involving explicit or implicit language queries. By developing new benchmarks to evaluate the proposed two tasks named Vanilla Hand Prediction (VHP) and Reasoning-based Hand Prediction (RBHP), this paper requires the model to acquire extensive understanding of human daily activities and reasoning abilities about what is happening next given cues from the current scene. To be specific, this paper propose a model named HandsOnVLM which generates textual responses and produce future hand trajectories through natural-language conversations. The experiments validate that the model outperforms existing methods on the proposed tasks.

### Strengths
(1) This paper iseasy to follow and well-written. (2) The tasks proposed in this paper sound interesting and I do believe they play an important in egocentric-relavent tasks, such as VR/AR, robotics.

### Weaknesses
Although the proposed tasks are interesting, I find that some critical details are either missing or require further elaboration in this paper, such as:
(1) Definition of Hand Pose: It remains unclear how the authors define the hand pose—whether it is based on joint positions, bbox or another representation. The paper merely includes two red and blue curves on images as qualitative results, which is ambiguous and lacks clarity. Specifically, are these curves representing the trajectory of a single point on the hand, such as the wrist or the centroid of the hand bounding box, or are they a more complex representation? The lack of a precise definition makes it difficult to reproduce the results or compare them with other methods that may use different hand pose representations.
(2) Details of H2O and FPHA Datasets: The paper provides insufficient information about the specifics of the H2O and FPHA datasets, particularly regarding the labels used in the study. This omission makes it challenging to fully understand the data, leaving readers to infer these details from the training objectives alone. For example, are the hand poses in these datasets represented in the same way as in the Epic-Kitchen dataset? Are there any differences in the annotation process or the quality of the labels that might affect the performance of the model? Without this information, it is hard to assess the generalizability of the proposed approach.
(3) Experiments: it's difficult to observe stable improvement from the experiments (such as in Table.1)

### Questions
In A.1, the training set of VHP and RBHP only contains Epic-Kitchen, as far as I know, this dataset does not contain hand pose labels. So where does the authors obtain the hand pose labels?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors propose HandsOnVLM, a VLM-based framework to reasoning hand activities and predicting hand motions. In this framework, the hand trajectories  The HandsOnVLM achieves SOTA on the proposed benchmark for Vanilla Hand Prediction (VHP) and Reasoning-based Hand Prediction (RBHP) tasks.

### Strengths
1. The proposed task appears engaging, as egocentric hand activities and motion prediction present challenging problems.
2.  The idea that encodes the hand as embedding is novel

### Weaknesses
1.  The authors only compare their method with naive baselines and traditional methods for hand motion prediction. One potential additional baseline would be using foundation models for video prediction and then track the motion as predictions.



### Questions
1. The authors report the results on Epic-Kitchen dataset which includes lots of ego motion. The egomotion would make the hand motions change significantly but they are barely unpredictable. How did the authors handle this problem?
2. How the <HAND> token is decoded to hand motions is not clear to me.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors propose training a video-language model which can reason about hand trajectories (curves, not poses) given videos and user queries as language input. Two associated benchmarks, Vanilla Hand Prediction (VHP) and Reasoning-Based Hand Prediction (RBHP) are introduced. VHP consists of predicting hand trajectories given an input video segment and a clear description of the object to be manipulated and the action to be performed. RHBP consists of predicting hand trajectories given less straightforward language input for which more complex reasoning must be performed. The authors curate datasets for both benchmarks, and promise to release these to the community. Evaluation on kitchen settings, as well as zero-shot evaluation on not (fully) kitchen-related datasets for the VHP benchmark shows the superiority of the method against state-of-the-art baselines.

### Strengths
The paper is well-written.

The proposed method has useful applications in research and industry.

The authors promise to release two new, relevant benchmarks to the community.

The proposed method is evaluated on multiple datasets and makes qualitatively sound predictions on unseen datasets.

The proposed method outperforms most state-of-the-art architectures.

### Weaknesses
The RBHP benchmark only includes kitchen scenes, and numerical validation is hence performed on kitchen settings only.

A comparison with a static-frame version of the proposed architecture would be appropriate to ensure fairness in Tabs. 1 and 2, as the baselines do not have access to the context provided by the observation history. Additionally, the need to use videos is a limitation, as in many settings we do not have a history of frames available. The absence of a static-frame baseline makes it difficult to isolate the benefit of the temporal modeling component of the proposed method. It is unclear if the performance gain is due to the video input or the architecture itself.

Typing errors in lines 208 (l_hand) and 325 (FPGA).

The prediction is limited to curves. A version involving hand poses would be very useful for many settings. The current curve-based representation, while suitable for trajectory prediction, lacks the detailed articulation information that hand poses provide. This limits the applicability of the method in scenarios requiring precise hand-object interaction modeling.

### Questions
Did you test your method with different numbers of input frames? What happens when you use only one frame? How well does your model handle the case of using a different number of tokens than what was used during training? Maybe the weakness I listed does not apply if the method performs well even when operating on a single frame.

### Soundness
3

### Presentation
3

### Contribution
3
