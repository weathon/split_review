# X-Gen: Ego-centric Video Prediction by Watching Exo-centric Videos

- Decision: Accept
- Scores: 8, 6, 6

## Abstract
Generating videos in the first-person perspective has broad application prospects in the field of augmented reality and embodied intelligence.
In this work, we explore the cross-view video prediction task, where given an exo-centric video, the first frame of the corresponding ego-centric video, and textual instructions, the goal is to generate future frames of the ego-centric video. 
Inspired by the notion that hand-object interactions (HOI) in ego-centric videos represent the primary intentions and actions of the current actor, we present X-Gen that explicitly models the hand-object dynamics for cross-view video prediction. 
X-Gen consists of two stages. First, we design a cross-view HOI mask prediction model that anticipates the HOI masks in future ego-frames by modeling the spatio-temporal ego-exo correspondence. 
Next, we employ a video diffusion model to predict future ego-frames using the first ego-frame and textual instructions, while incorporating the HOI masks as structural guidance to enhance prediction quality.
To facilitate training, we develop a fully automated pipeline to generate pseudo HOI masks for both ego- and exo-videos by exploiting vision foundation models. 
Extensive experiments demonstrate that our proposed X-Gen achieves better prediction performance compared to previous video prediction models on the public Ego-Exo4D and H2O benchmark datasets, with the HOI masks significantly improving the generation of hands and interactive objects in the ego-centric videos.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a novel approach ( X-Gen) for generating future frames in ego-centric videos based on exo-centric footage and textual instructions. By modeling hand-object interactions (HOI) and employing a two-stage process that predicts HOI masks and utilizes a video diffusion model, X-Gen enhances prediction quality. Extensive experiments show that X-Gen outperforms existing models, particularly in generating realistic hand and object interactions.

### Strengths
--> The paper is well-written and easy to understand. All the key contributions are clearly presented with individual sections describing the components of the model in detail.
--> Experimental evaluation is thorough with a detailed ablation study. These experiments clearly show the impact of cross-view HOI mask prediction on the overall performance.
--> The automated approach to generate Ego-Exo HOI masks is also a good contribution.

### Weaknesses
--> ConsistI2V trained on Ego-Exo4D achieves SSIM of 0.532, compared to X-Gen which achieves 0.537. The difference is not significant. Also ConsistI2V only need the first frame (in ego view) and the text to generate the output, whereas X-Gen would also need the entire exo video and have to perform cross-view HOI mask prediction to generate the output. Given the overhead and the additional requirements of X-Gen, along with the marignal improvement in performance,  the novelty and adoption of this method are called into question.
--> Adding the details about the training time, inference time, number of trainable parameters and the compute resources required for training would improve the paper.

### Questions
--> Inputs to your model are the exo video, first frame of the corresponding ego video and the textual description. How will your approach perform if the inputs are the exo video and the first frame of a random ego video and the textual description? If the correspondence between the exo video and ego frame is required, then what is the need usecase where this method will be useful.

### Soundness
3

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
The paper aims to generate the ego-centric videos given the first frame of the ego-centric video, a text instruction, and a synchronized exo-centric video. The proposed model, X-Gen, involves two components: i) an exo-to-ego HOI mask prediction framework, and ii) an ego-centric video diffusion model given the first frame of the ego view, the text instruction, and the predicted ego HOI mask from the first component. Experiments were mainly conducted with the Ego-Exo4D dataset, where the authors adopted off-the-shelf models (e.g. EgoHOS, SAM2) to generate HOI mask annotations. The zero-shot performance of X-Gen was also evaluated with the H2O dataset.

### Strengths
1.	The manuscript is well organized in general.
2.	The paper introduces high-level novelty on using cross-view HOI mask prediction to guide the video diffusion model.
3.	Several ablations and visualizations were shown in the experiment section.

### Weaknesses
1.	The justification for the need of the proposed cross-view mask prediction network is not strong. For example, given that Ego video frames are available during training, one baseline can be using a HOI mask predictor for only the Ego views, either with off-the-shelf HOI detectors (e.g. EgoHOS+SAM2) or training one with the dataset. Another can be using Exo-Ego video frames without Exo HOI mask.  

2.	Given that the average video duration is only 1 second (L268), it is unclear how much dynamics the model is learning. What are the evaluation metrics in Table 1 if only the HOI mask of the first Ego video frame is used as the condition? Also, what about using the first Ego video frame directly as the predictions?  

3.	It is unclear why prior cross-view transformation modules (e.g. [a]) cannot be used as a baseline for the first component.  

4.	In L269, the authors claimed that the object masks from the cross-view relation benchmark are not guaranteed to be interacting objects, and the hand masks are not annotated. However, there is no justification that using HOI masks is a better option.  

5.	It is unclear how alpha was annealed during training (L175) and there is no experiment showing that whether it is important.

### Questions
In addition to the questions in the weakness section,  

1.	Can the authors provide more details about the pipeline at the inference time? E.g., what are the inputs? What will Eq. (2) turn to? Do you take the predicted Ego frames from the second component to the first component, why or why not?
2.	Can the authors elaborate more details about the temporal attention blocks in the video diffusion part? How was the temporal information fused here?
3.	What does it mean by “we apply the hand-object masks extracted from the future video frames instead of cross-view mask predictions” in Table 2 and 3? Are they ground truth HOI masks?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
- The paper addresses cross-view video prediction, where the goal is to animate an ego-centric video starting from a single frame and guided by a corresponding exo-centric video and textual commands.
- The paper introduces an "ego-exo memory attention" mechanism that enhances the ability to transfer relevant features from exo-centric to ego-centric frames, aiding in the accurate prediction of interactions.
The proposed model is evaluated on Ego-Exo4D and H2O and shows superior performance over previous models, particularly in generating realistic hand and object interactions in ego-centric videos.

### Strengths
- X-Gen effectively leverages information from exo-centric videos to predict ego-centric video frames. This innovative approach bridges the gap between different perspectives, using third-person videos to enhance first-person video prediction. 
- The paper introduces a novel approach to predict hand-object interaction (HOI) masks in future frames, which is critical for accurately generating frames that involve interactions with objects. 
- The fully automated pipeline for generating HOI masks using vision foundation models reduces the reliance on manual annotations and increases the scalability of the training process. 
- X-Gen demonstrates strong zero-shot transfer capabilities, performing well on unseen actions and environments in benchmark datasets.

### Weaknesses
See the questions below.

### Questions
- What were the key factors that influenced the architectural design of the X-Gen model, particularly the integration of the cross-view HOI mask prediction with the video diffusion process?
- Can you discuss specific instances where X-Gen failed to predict accurate video frames?
- Can you provide more detail on how the HOI mask prediction model handles the temporal dynamics and variability in human-object interactions across different video frames?
- What are the computational performances for training and testing the X-Gen mode?

### Soundness
3

### Presentation
3

### Contribution
2
