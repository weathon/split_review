# Language-Image Models with 3D Understanding

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Multi-modal large language models (MLLMs) have shown incredible capabilities in a variety of 2D vision and language tasks.
We extend \mmfm{}s' perceptual capabilities to ground and reason about images in 3-dimensional space. 
To that end, we first develop a large-scale pretraining dataset for 2D and 3D called \dataset{} by combining multiple existing 2D and 3D recognition datasets under a common task formulation: as multi-turn question-answering.
Next, we introduce a new \mmfm{} named \ours and pre-train it on \dataset{}. 
We show that pure data scaling makes a strong 3D perception capability without 3D specific architectural design or training objective. 
\ours exhibits intriguing properties similar to LLMs: (1) \ours can apply chain-of-thought prompting to improve 3D understanding from 2D context information.
(2) \ours can follow complex and diverse instructions and adapt to versatile input and output formats. 
(3) \ours can be visually prompted such as 2D box or a set of candidate 3D boxes from specialists.
Our experiments on outdoor benchmarks demonstrate that \ours significantly outperforms existing baselines by 21.3 points of AP$_{\text{BEV}}$ on the \ttc dataset for 3D grounded reasoning and 17.7 points 
on the \dLM dataset for complex reasoning about driving scenarios, respectively. 
\ours also shows competitive results in general MLLM benchmarks such as refCOCO for 2D grounding with (87.0) average score, as well as visual question answering benchmarks such as VQAv2, GQA, SQA, POPE, etc. for complex reasoning.  
Our project is available at \url{https://janghyuncho.io/Cube-LLM}.

\keywords{Multi-modal Large Language Models \and 3D Scene Understanding \and Foundation Models \and Autonomous Driving}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces CUBE-LLM, extending LLAVA to 3D using the new LV3D dataset, which unifies 2D and 3D data in a question-answer format. This allows smooth 2D-to-3D generalization without changing the model’s architecture. Instead of specialized design, CUBE-LLM achieves 3D reasoning through diverse data, using iterative 2D predictions to boost 3D accuracy. It sets new benchmarks in 3D grounding on tasks like Talk2Car and DriveLM while staying competitive on standard 2D tasks.

### Strengths
1. The overall data pipeline is well-structured, extending LLAVA to a 3D data format with large-scale pretraining. It incorporates standardization of 2D/3D data labels (as shown in Fig. 3), unification of model I/O inputs, and the implementation of visual chain-of-thought (CoT) reasoning for step-by-step analysis.

2. The evaluation is comprehensive, covering various tasks such as 3D grounding (Talk2Car, DriveLM-grounding, Indoor Objectron, ARKitScenes, SUN-RGBD), QA (DriveLM-QA), 3D grounding and captioning (LV3D), and 2D grounding (RefCOCO).

3. A good portion of the visualizations effectively enhances understanding across all tasks.

4. Visual CoT achieves a 3.2-point improvement.

### Weaknesses
1. The paper lacks an in-depth analysis of joint 2D and 3D training. It closely follows LLAVA1.5, with DINOv2 as the vision model and primarily contributes by consolidating 2D and 3D datasets. While 3D performance improvements could add value, the impact seems insufficient for acceptance. I would like more analysis on the effects of excluding 2D and 3D box pretraining on 3D/2D QA/grounding performance.

2. In my view, the Visual CoT would benefit from zooming in on selected parts (SoM [1]) to enhance model understanding with enlarged object details in a second stage. While the 3.2-point performance improvement (Line 423-424) is reasonable, it comes at the cost of additional tokens and computation, similar to test-time augmentation.

[1] Yang, Jianwei, et al. "Set-of-mark prompting unleashes extraordinary visual grounding in gpt-4v." arXiv preprint arXiv:2310.11441 (2023).

### Questions
See the weakness.

A few corrections:
Line 422: Change "Table 5" to "Figure 5."
Figure 5 (bottom right): Why is the performance bar at 32% different between the two sub-figures?

### Soundness
3

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
4

### Summary
In this work the authors proposed a method to extend vision-language models (LLaVA-v1.5) for 3D understanding. Specifically the authors constructed a large pretraining dataset LV3D (by unifying the data formats of multiple previous datasets), and a new Cube-LLM. With data and task scaling the authors show that Cube-LLM achieve improved performance for 2D and 3D grounding tasks. Results also show that Cube-LLM has some 3D reasoning capabilities.

### Strengths
1. The authors proposed a new MLLM for 3D understanding, *i.e.*, Cube-LLM. To enable joint learning from both 2D and 3D domain knowledge, the authors proposed datasets with unified 2D and 3D formats, as well as training tasks on different data modalities.
2. Experiments results show the benefit of the proposed data+task training paradigm, with improved performance on 2D and 3D visual grounding, as well as tasks that require certain reasoning.
3. The proposed framework will enable future research on 2D and 3D reasoning, with a unified interface of 2D and 3D representations. This can enable models to interact with 2D and 3D data, and to perform explicit reasoning on 3D layouts.

### Weaknesses
1. Experiments on DriveLM QA is comparing with weak baselines and the reasoning examples on DriveLM are with finetuning. For instance, how is the reasoning capabilities of the proposed Cube-LLM compared to methods with spatial reasoning training data, such as SpatialRGPT and SpatialVLM. I think this is an interesting topic to study the reasoning capabilities of the proposed method but current results are not very promising.
2. Table 4 shows that Cube-LLM outperforms previous specialist and generalist models. However, Cube-LLM is trained on RefCOCO annotations as stated in Table 1, which makes the results not a fair comparison?

### Questions
1. Will the datasets be released to benefit future research?

### Soundness
3

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
This work presents a vision-language model designed for both 2D and 3D understanding tasks. The authors begin by reformatting existing datasets into a standardized structure, representing objects with 2D/3D bounding boxes and constructing multi-round question-answer pairs to facilitate model training. For evaluation, a chain-of-thought prompting technique is applied at the test stage, enabling the model to perform progressive reasoning on 3D tasks from simpler to more complex questions. Experiments conducted on two 3D reasoning datasets—Talk2Car and DriveLM—demonstrate promising performance for the proposed method. Additionally, the method shows competitive results on 2D vision-language (VL) tasks.

### Strengths
1. The exploration of LLM-based 3D reasoning is timely and relevant, given the nascent stage of 3D language-vision models compared to their 2D counterparts. One significant contribution lies in the authors’ pipeline for collecting datasets suited for training multimodal LLMs, which addresses the challenge of limited large-scale datasets for 3D tasks.

2. Experiments on two established 3D reasoning benchmarks, Talk2Car and DriveLM, show that the proposed method achieves superior performance, indicating the model’s strength in handling 3D reasoning tasks.

### Weaknesses
1. The collected dataset primarily focuses on 3D captioning and grounding tasks, which restricts the breadth of 3D capabilities the model can support. Expanding the dataset to include other essential 3D reasoning capabilities, such as depth ordering, neighborhood relationships, object sizing, and directionality, would better align with real-world 3D applications.

2. While the experiments indicate that the proposed method performs effectively for 3D visual grounding, it remains unclear if the model can fully comprehend and reason within the 3D environment.

3. Although this paper focuses on 3D reasoning with LLMs, it could benefit from a more thorough discussion of related recent works in 3D LLMs, such as 3D-LLM, Scene-LLM, Point-LLM, Uni3DL, and 3D visual grounding efforts, including ScanRefer and ReferIt3D.

4. In Figure 3, the input-output formats do not appear to include point_3d as a possible question or answer type, which seems inconsistent with Equations (6) and (7).

5. A recently introduced work, Cambrian, includes a 3D reasoning subset. Evaluating the proposed model on this subset could provide an insightful comparison and demonstrate the robustness of the model.

### Questions
It would be better to show performance on more 3D reasoning datasets/tasks.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper focuses on fine-tuning LLAVA using a specially constructed 3D visual chain-of-thought (CoT) prompting data for 3D grounding tasks. The CoT data is created by arranging multiple questions about the same object in an easy-to-hard order, such as progressing from 2D box center prediction to 2D box coordinate generation, and eventually to 3D box coordinate prediction. The effectiveness of this proposed CoT data is demonstrated by training on a mixture of indoor and outdoor datasets and evaluating the results on Talk2Car and DriveLM datasets.

### Strengths
1. The concept of a 3D visual chain-of-thought is well-founded and logical.
2. Ablation studies effectively highlight the benefits of both the proposed training dataset LV3D and the visual chain-of-thought approach.

### Weaknesses
1. For the experiments, the manuscript does not provide enough comparison with recent progress in specialists, such as Grounding DINO (ECCV'24), and its follow-ups.
2. The manuscript employs a virtual camera for handling camera intrinsics. A key advantage of specialized models is their ability to process images with varying resolutions and aspect ratios once trained. Does this capability extend to virtual camera-based MLLMs? If not, what methods do you use to handle inputs with different resolutions and aspect ratios?
3. The engineering effort involved in curating data on LV3D is commendable. Do you plan to release the relevant code scripts?

Minor Typos: Inodoor -> Indoor, L432.

### Questions
Please see the section of weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3
