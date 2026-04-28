# FlyOrien: A bio-inspired model for incremental learning of object orientation

- Decision: Reject
- Avg Score: 4.33
- Scores: 5, 5, 3

## Abstract
Visual orientation detection helps navigation, especially without a reliable magnetic compass or GPS. Inspired by the neural mechanisms of the insect brain, particularly the mushroom body (MB) and the central complex (CX), we propose FlyOrien—a bio-inspired model for object orientation detection. The model mimics the MB for random feature extraction, sparse coding and associative learning, while the CX provides multi-clue sensory integration, enabling interpolation for finer orientation representation. FlyOrien's biologically plausible learning rule allows one-shot learning, reducing the need for large datasets and repeated training. We tested FlyOrien on a dataset containing images labeled with orientations, which introduce strong interferences because images of the same object have different labels. In this challenging context, FlyOrien achieves competitive performance compared to convolutional neural networks (CNNs), significantly reducing training time and computational resources. It also has the potential for real-world applications like robotics, where incremental learning is essential.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces FlyOrien, a bio-inspired model for object orientation detection that takes inspiration from insect neural circuits, specifically the Mushroom Body (MB) for sparse coding and the Central Complex (CX) for orientation integration. FlyOrien is designed for incremental learning, allowing it to recognize object orientations efficiently after minimal exposure while avoiding catastrophic forgetting. It was tested on a modified version of the COIL-100 dataset and real-world robotic tasks, showing strong performance in orientation retrieval and prediction, with reduced computational needs compared to CNNs.

### Strengths
The paper introduces FlyOrien, a bio-inspired model for learning object orientation, drawing from insect brain structures like the mushroom body and central complex. FlyOrien mimics biological neural circuits instead of traditional CNNs to learn object orientation after a single exposure. The model is well-explained, and experiments are robust, showing FlyOrien’s efficiency on modified datasets and real-world robotic tasks. Some sections could benefit from clearer explanations, particularly on specific model components.

The paper is mostly clear, though many structural and grammatical adjustments are needed to improve readability. FlyOrien’s lightweight, GPU-free design makes it a potential tool for resource-limited devices like drones, with promising applications in navigation, tracking, and surveillance.

In summary, FlyOrien offers an original approach, but a deeper comparison with existing methods and greater clarity in a few areas would strengthen the paper.

### Weaknesses
The paper could benefit from a more detailed comparison with existing orientation detection methods to better highlight its novelty and contributions. Claims about the model’s generalization to multimodal inputs (like olfactory and directional cues) are unsupported by the presented experiments. Some model components, like the modifications to the Continuous Attractor Neural Network, lack detail, making the implementation hard to fully understand or replicate. Also, the use of different hardware (CPU for FlyOrien and GPU for CNNs) creates an uneven comparison; training both on the same hardware would provide a clearer performance evaluation. Finally, grammatical and structural adjustments throughout would improve clarity and readability.


Clarity and Consistency
- Some phrases could be clarified. For example, use "visual orientation detection" instead of “orientation detection with vision.”
- The phrase "eliminating the need for large datasets and repeated training" might be too strong and could be replaced with "reducing the need for large datasets and repeated training."
- The statement “Our intention to retrieve orientation is related to object pose estimation, but different in many aspects” is vague and does not clearly delineate the differences.
- Claims like "perfect memory" are unrealistic and may misrepresent existing methods.
- The description "the same images are presented in the test" is confusing. Typically, retrieval involves querying with existing data, not reusing the same images. Please clarify whether the task involves retrieving orientations for previously seen images or something else.
- The term "catastrophic forgetting" is typically used in the context of incremental learning, not in relation to cross-validation. Please clarify the context in which catastrophic forgetting occurs or use a more appropriate term if applicable.

Methodology and Justification
- In the introduction, it would be beneficial to provide a short summary of the proposed method and how it differentiates from existing approaches.
- Briefly summarize the structure of the paper in the introduction to guide readers through the upcoming sections.
- The descriptions of Method 1 and Method 2 are vague and lack technical clarity.
- You assumed “MB uses similar ways for coding, and experiments shown it is functional.” The assumption is stated without sufficient justification or reference to supporting experiments.
- The modifications made to the Continuous Attractor Neural Network (CANN) for the CX component are not clearly explained.
- You mentioned “showing that it outperforms traditional artificial neural networks in terms of efficiency.” The term "efficiency" is broad and undefined. Specify which metrics are being referred to.
- The phrase “Both the first and second half of our model are set as a multi-class classification problem.” The distinction between the "first half" and "second half" is unclear.

Evaluation Criteria and Metrics
- "FlyOrien’s effectiveness in dataset and real-world applications" lacks specifics. The evaluation criteria, metrics used, and how effectiveness is measured are not clearly defined.
- Using the Top-5 accuracy metric for retrieval tasks is unconventional. Retrieval tasks often use metrics like precision, recall, or mean average precision. Please justify the use of Top-5 accuracy or consider using more standard retrieval metrics.
- You mentioned "FlyOrien is designed to learn object orientations efficiently after a single exposure and can generalize to multimodal inputs, such as visual, olfactory, and directional cues." However, the experiments described focus primarily on visual inputs, so claims about generalization to multimodal inputs are unsupported by the presented experiments.
- Comparing a model trained on a CPU to CNNs trained on a GPU is misleading because hardware significantly impacts training time and performance metrics.

Grammar and Typos
- There are several typos, including:
  1. “whose underline mechanism” should be “underlying mechanism.”
  2. “orientation but in the plan of the image” should be “plane of the image.”
  3. “dieerences” should be “differences.”
- Missing spaces are common throughout the paper.
- There are issues with Subject-Verb Agreement, verb tense inconsistencies, incorrect article usage, redundant words, and typos.
- Train on CPU not “trained in CPU.” Revising the sentence could improve clarity.
- Ensure clarity in phrases such as "a dataset modified for orientation detection." Specify the original dataset and the modifications made.

Structure and Flow
- The paper lacks a Conclusion section.
- Some sentences end abruptly without concluding the thought.
- The sections jump between high-level descriptions and detailed technical explanations without clear transitions. Add transitions to maintain logical flow.
- Conduct a thorough proofreading to correct typographical and grammatical errors.

### Questions
1. Could you clarify the claim about multimodal input generalization? The current evidence appears to be limited to visual data testing only.

2. The speed comparison between FlyOrien (CPU) and CNNs (GPU) needs clarification. How was the 45x speed difference measured considering the different hardware platforms used?

3. Please specify:
   - Whether the 45x speed improvement refers to training time, inference time, or both
   - How hardware differences were accounted for in this comparison

4. Can you elaborate on the specific modifications made to the CANN in the CX component? Please include details about how these changes contribute to orientation interpolation.

5. The claim of "perfect memory" requires substantiation. What evidence supports this characterization?

6. The description "the connection is almost random" needs clarification:
   - What metrics were used to determine this?
   - What evidence supports this characterization of the connections?

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
This paper proposes a neural network model inspired by the neural circuits of insects, for incremental learning of object orientation. The model called FlyOrien, consists of two main parts mimicking the insect brain's Mushroom Body (MB) and Central Complex (CX). The MB part is responsible for sparse coding and associative learning, while the CX part integrates multiple inputs to refine the orientation detection. The model's performance is compared to typical CNN architectures. The model runs much faster than CNNs even when executed on CPU rather than GPU, and the its number of parameters is 250 times smaller. The performance is similar to CNNs and in some cases, better.
Simulations mainly include 2 datasets: a modified version of COIL-100 and a propriety dataset of real objects acquired by a quadruped robot.

### Strengths
The paper has a very good and comprehensive introduction, which includes a strong motivation for studying the suggested bio-inspired model, and an extended review of the reference biological mechanism of the insect's brain.
The paper also has a clear mathematical description of the model (simplified Mushroom Body) and a good explanation of its learning rules.
In the experimental section, the model is applied to a public dataset as well as a propriety dataset collected by a robot in a real environment.

### Weaknesses
The paper has several weaknesses, one of them is a long list of English typos, which may result from the use of an automatic language translation model. However, this is mainly annoying, and may be easily corrected.
Another weakness is the design of the simplified MB model, in particular the selection of the model size and parameters (e.g., number of KC units), that was adjusted to maximize the accuracy on the evaluation dataset. This actually shows a very high correlation between the model size (number of parameters) and the model accuracy, which may suggest that a much larger model may be needed to support larger images, a larger number of object categories and a realistic range of lighting conditions. It is not clear if the size of a more robust and general model will still be competitive and economic in comparison with SOTA CNNs. Also, the authors did not compare the model's performance to small CNN models such as SqueezeNet, MobileNet and others.
Another weakness is a poor description of the attractor network modeling the CX mechanism in section 2.2. Adding a visualization scheme to describe better the integration with the first part of the model (MB) may be helpful, as well as a better example than the one provided in figure 2.
Lastly, the authors include in the supplementary some analysis (figures A4-A6) on the resilience of the model to introducing additional new objects (overcoming the catastrophic forgetting problem of alternative models). However, the evaluation is based on datasets including only a small number of objects. An ablation study on the scalability of the model to cases with many more objects (hundreds) and more realistic scenes, are needed if one claims that the suggested model (or similar) should replace SOTA CNNs in robotic systems.

### Questions
As described in the Weaknesses section of the review, here are some specific questions and suggestions for the authors.
1. Provide a better ablation of the size and scalability of the model for robustness and realistic scenarios with larger number of objects and lighting conditions. 
2. Compare the model's performance also to small CNN models such as SqueezeNet, MobileNet and possibly others, which has much less parameters than the currently evaluated CNNs (ResNet, AlexNet etc.).
3. Elaborate more on the modeling of the CX mechanism of the model (attractor network).
4. Correct the many typos in the paper (some examples: "sparse presentation", line 075; "inputs that are prepossessed", line 080; "an model", line 097; "a activity", line 103; "rules that enables", line 139; "there are dieerneces between", line 165; "layer is consists", line 171; "activities can active", line 201; etc.)
5. The equation in line 190 does not describe the mean of the samples, but merely the sum.
6. Lines 209-210 say: "Since a “KC” that is always active provides little useful information, we implemented a threshold to disable such “KCs”."
    It is not clear why you need this. Is this action taken because of replacing spiking neurons with firing-rate ones? If not, how is this issue resolved in the insect brain?
7. In equations (5) and (6) lines 244 and 254, the sentence "if j is the label and k actives," is not clear.
8. In figures A4 and A5 of the appendix, the y-axis title reads "training times", but the figures' caption says "the y-axis represents the index of the object being retrieved.". You need to clarify this discrepancy and modify either the titles or the captions.

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
This paper proposes a bio-inspired model based on the mushroom body and central complex of the insect brain. Their model consists of a sparse coding layer followed by a continuous attractor network. They introduce two variations of a Hebbian learning rule for updating model parameters, allowing for fast training. The authors apply their model to the task of object orientation detection, and compare it to convolutional neural network baselines on the COIL-100 O and AS datasets, as well as a custom datasets collected from a quadruped robot.

### Strengths
- The bio-inspired method has local learning rules which enables fast training.

### Weaknesses
 - I think there is a mismatch between the inspiration from biology (i.e. the insect brain) and the task setup (i.e. object orientation detection). I'm not convinced that insects/flies are evolved to estimate orientation of objects. Even if they would learn the orientation of objects, they'd typically only see a few orientations of an object, and then have to estimate a complete novel orientation; not first ingest a whole dataset of many orientations of a single object. A more intuitive application would be to predict the insect's own orientation / heading given the vision stream, which is effectively what bio-inspired navigation algorithms use a continuous attractor network for (e.g. https://ieeexplore.ieee.org/document/1307183, https://dl.acm.org/doi/10.1109/ICRA48506.2021.9560768 ). The final experiment goes in this direction, but still relies a 360 sweep first for "training" before it can start estimating its orientation.

- Given the experimental setup, the model basically needs to associate images to orientation bins. A different baseline that does this association (e.g. a Hopfield network) would be interesting to compare against.

- The train/test data is very correlated as the test data is basically gathered in the same "sweep" as the train data. Especially in the robot experiment it would be more convincing if the accuracy would be tested on other acquisitions with varying translation and distance of the robot to the object.

### Questions
- Looking at the examples of the COIL-100-AS dataset, it seems impossible to me to get a sensible orientation estimate given a symmetric object. Given that the methods still obtain a high accuracy for these objects seems to me that they are severely overfitting and looks rather undesired?

- For the robot experiments, how is the accuracy affected if the robot is put in a different position than the "train set"?

### Soundness
2

### Presentation
1

### Contribution
1
