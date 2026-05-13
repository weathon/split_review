# Intent3D: 3D Object Detection in RGB-D Scans Based on Human Intention

- Decision: Accept
- Scores: 5, 5, 6, 6

## Abstract
\vspace{-0.9em}
In real-life scenarios, humans seek out objects in the 3D world to fulfill their daily needs or intentions. This inspires us to  introduce 3D intention grounding, a new task in 3D object detection  employing RGB-D, based on human intention, such as "{\em I want something to support my back}". Closely related, 3D visual grounding focuses on understanding human reference. To achieve detection based on human intention, it relies on humans to observe the scene, reason out the target that aligns with their intention ("{\em pillow}" in this case), and finally provide a reference to the AI system, such as "{\em A pillow on the couch}". Instead, 3D intention grounding challenges AI agents to automatically observe, reason and detect the desired target solely based on human intention. To tackle this challenge, we introduce the new \textbf{Intent3D} dataset, consisting of 44,990 intention texts associated with 209 fine-grained classes from 1,042 scenes of the ScanNet~\cite{dai2017scannet} dataset. We also establish several baselines based on different language-based 3D object detection models on our benchmark. Finally, we propose \textbf{IntentNet}, our unique approach, designed to tackle this intention-based detection problem. It focuses on three key aspects: intention understanding, reasoning to identify object candidates, and cascaded adaptive learning that leverages the intrinsic priority logic of different losses for multiple objective optimization.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a new task named 3D-intention grounding, which is 3D object-detection from direct human-intentions. The paper collects Intent3D dataset which includes 1042 scenes from ScanNet and corresponding paired human-intentions questions and 3D object detections answers. IntentNet is proposed to tackle 3D-intention grounding task by candidate box-matching, verb-object alignment and cascaded adaptively learning.

### Strengths
1. The paper presents a clear motivation for 3D-intention grounding, and it includes clear illustrations and presentations of dataset collection procedure.

2. Soundness of each component design of the IntentNet, and thoroughly ablations on each component of the proposed pipeline design.

3. Extensive experiments and discussions demonstrate the effectiveness of the proposed framework compared to different types of baselines.

### Weaknesses
Major concern:

I am concerned about possible baseline unfair comparison in the experiment section. Most baselines are designed to tackle nouns-types of questions instead of human-intention types of questions. What if we pass the question to a finetuned LLM and let it infers what types of nouns/objects the question is targeting at from possible objects in a scene detected by existed 3D object detectors? The possible performance of these baselines might be much higher after it is given the object it is expected to detect in a scene. 

Minor concern:
It would be interesting if the author can provide some cases where IntentNet fails but other models succeed. Particularly if other models are fed with object/noun directly.

### Questions
Please see the weakness section. 

I am willing to increase my score if the author resolves my major concern with some additional baseline experimentations.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper introduces the task of 3D Intention Grounding (3D-IG), which aims to automate the reasoning and detection of target objects in real-world 3D scenes using human intention cues. To this end, the authors constructed the Intent3D dataset, comprising 44,990 intention texts across 209 fine-grained object categories, and developed several baseline models to evaluate various 3D object detection techniques. Finally, the authors proposed a novel method, IntentNet, which optimizes intention understanding and detection tasks through techniques such as verb-object alignment and candidate box matching, achieving state-of-the-art performance on the Intent3D benchmark.

### Strengths
1: A new task in 3D object detection employing RGB-D, based on human intention, facilitates smoother and more natural communication between humans and intelligent agents.

2:The author propose a high-quality vision-language dataset and focuses on the human’s intention for 3D object detection, which will facilitate the progress of 3D scene understanding.

### Weaknesses
1: There has been a few methods to combine 3D scene understanding with LLM beyond Chat3D v2, such as LL3DA, Grounded 3D-LLM, ReGround3D and so on.  The paper does not highlight the advantages compared to them.

2: The object selection method is too crude, as it removes some commonly used objects by humans when filtering Non-trivial Objects. Figures 3 (d) and (e) indicate that the dataset lacks sufficient diversity in the types of objects included.

3: The limited variety of object category included in the dataset, fails to demonstrate the grounding effect for the missing objects in the dataset.

### Questions
1：There has been a few methods to combine 3D scene understanding with LLM beyond Chat3D v2, such as LL3DA, Grounded 3D-LLM, ReGround3D and so on.  What are the advantages of this paper compared to theirs? More experimental evidence is needed to demonstrate the advantages of the this paper over other methods.

2: Current large language models can also directly infer human intentions; what are the advantages of this paper compared to them?

3：When filtering Non-trivial Objects, objects with more than six instances in fine-grained categories are directly removed, which may lead to the exclusion of commonly used objects. Could we consider adding more fine-grained descriptions for these objects instead of outright deletion?

4:  Figures 3 (d) and (e) indicate that the dataset lacks sufficient diversity in the types of objects included. Experimental validation is necessary to determine whether the variety of object types included in the dataset is sufficient for the model to learn effectively.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper introduces a 3D Intention Grounding (3D-IG) task and constructs a novel dataset called Intent3D (sourced from ScanNet data and generated using GPT). Additionally, it proposes a baseline model named IntentNet. I am not an expert in 3D-related fields, so my confidence in this review is not very high.

### Strengths
1. The overall quality of the paper is high, with clear writing and easy-to-understand presentation.
2. The contribution of the dataset is significant, as it is the first to construct a 3D detection task focused on intention understanding.

### Weaknesses
1. More comparisons with recent works should be provided in Tables 1 and 2. Additionally, there is a minor mistake: the detector names “GroupFree” and “Group-Free” in the first two rows of Tables 1 and 2 do not match.
2. The article gives a subtractive ablation experiment. I would like to see an additive ablation experiment, such as how the effect of verb alone works.
3. The article does not give the performance of the proposed IntentNet in traditional 3D grounding.

### Questions
1. Will the proposed dataset and code be open-sourced?
2. IntentNet seems to be a two-stage approach, where a pre-trained 3D detector first extracts proposals, which are then matched with text. Are there any one-stage methods that directly fuse 3D data and text to generate boxes? If so, the paper does not seem to provide comparisons with such methods.
3. Regarding the training process, on what hardware was the method trained, and how long did the training take?

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
This paper presents a novel framework for 3D object detection that integrates human intention into the detection process. The authors introduce the Intent3D dataset, aiming to enhance the model's understanding of human needs in real-world scenarios. The proposed method, named IntentNet, employs a multi-instance detection approach, where the model is tasked with identifying multiple instances of objects based on free-form textual descriptions of human intentions. The authors evaluate their approach against several baselines, including expert models designed for 3D visual grounding, foundation models for generic 3D understanding tasks, and Large Language Model (LLM)-based models. The evaluation demonstrates the effectiveness of IntentNet in achieving state-of-the-art performance on the Intent3D benchmark.

### Strengths
1. The introduction of the 3D Intention Grounding (3D-IG) task could contribute to the 3D visual grounding community.
2. The proposed Intent3D dataset is extensive, comprising 44,990 intention texts linked to 209 fine-grained object classes from 1042 3D scenes. This dataset provides a valuable resource for training and evaluating models in the context of human intention.
3. The proposed modules in IntentNet are generally technically sound.

### Weaknesses
1. Object detection based on human intention is indeed a new task. However,  why should we need to have a dataset and a model dedicated to this task? I think the detection based on human intention can be achieved in a modulized manner. For example, first, let the 3D detection module detect all types of objects in the scene. Then ask  LLM to decide the subsets of the detected objects that can fulfill the human intention. I think this could be more flexible compared with training a dedicated detection model based on human intention prompts.
2. In L210, it is mentioned that around six intention texts are generated per object. How do you determine this number (six)? Can it guarantee that all possible intentions can be covered and trained well?
3. The contents around Eq (3) are hard to understand for me. What is t in Eq(3)? Although the authors claimed that the code would be released to facilitate the understanding, it would be better to add a figure to illustrate the connections in the network.  
4. Figure 4 is too abstract. Even though many connections and modules are included, it is not very informative. I suggest more detailed diagrams can be provided for the key modules further.   
5. Figure 5 shows that the verb alignment is very helpful for the prediction quality. Do you think this is caused by the limited training data? If more data is available for training, would this module still be essential?

### Questions
Please refer to the weakness part/

### Soundness
3

### Presentation
2

### Contribution
3
