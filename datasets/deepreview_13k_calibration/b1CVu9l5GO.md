# TraceVLA: Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 8, 6, 6

## Abstract
Although large vision-language-action (VLA) models pretrained on extensive robot datasets offer promising generalist policies for robotic learning, they still struggle with spatial-temporal dynamics in interactive robotics, making them less effective in handling complex tasks, such as manipulation. In this work, we introduce visual trace prompting, a simple yet effective approach to facilitate VLA models’ spatial-temporal awareness for action prediction by encoding state-action trajectories visually. We develop a new TraceVLA model by finetuning
OpenVLA on our own collected dataset of 150K robot manipulation trajectories using visual trace prompting. Evaluations of TraceVLA across 137 configurations in SimplerEnv and 4 tasks on a physical WidowX robot demonstrate state-of-the-art performance, outperforming OpenVLA by 10% on SimplerEnv and 3.5x on real-robot tasks and exhibiting robust generalization across diverse embodiments and scenarios. To further validate the effectiveness and generality of our method, we present a compact VLA model based on 4B Phi-3-Vision, pretrained on the Open-X-Embodiment and finetuned on our dataset, rivals the 7B OpenVLA baseline while significantly improving inference efficiency.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposed a visual trace prompting method called TraceVLA to enhance VLA models in manipulation tasks. 
By incorporating Co-Tracker to visually prompt keypoint trajectories into existing VLA frameworks, TraceVLA achieves better performance than baselines in simulated and real robot experiments. It also shows better generalziation across environmental variations than vanilla VLA model and text prompted ones, further proves the advantage of the proposed visual trace method.

### Strengths
1. Clear description of the method. Comprehensive ablation on prompt setting and trace length, as well as analysis of memory and speed. 
2. Regarding the drawback in VLA practice, this work creatively applies tracking as visual prompting for VLAs to learn the invariance across different scene settings in manipulation.

### Weaknesses
 1. Sec 4.1 is a bit hard to read. Mixing figures, tables, and your main context together with reduced blanks is not a good idea to present your experiment results clearly. 
 2. Lack of details in experiments. For example, how do you define success, especially in real robot experiments? When you add noise to the environment, do you have a limit over related parameters? Is there any case study that qualitatively shows the advantage of applying visual tracking prompts? Please add them to your revision, which is also good for reproducibility.

### Questions
1. How does this method generalize under camera orientation changes? By nature it helps the model against illumination/background changes, but how can VLA remain effective when the camera moves, given only 2D tracking result? If the change is small, then to what degree do you vary? You mentioned in the real robot section that finetuning is needed due to domain shift, but not for the simulation. Is that also due to the domain gap being small in simulated experiments?
2. Regarding the active point selection, did you choose the $\kappa$ so that $M=5$ takes a reasonable ratio in the active points, and therefore similar traces are learned in the training set? If not, does it have the potential to generalize across visually different robots?
3. Will the color, thickness, or even transparency of the visual prompt affect the performance? 
4. Is K somehow related to the size of the image patch size? 
5. Will the performance drop if the action is moving into/out of the camera frame, or rotating in/out of it?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work leverages visual trace prompting to enhance VLA models' spatial-temporal awareness for action prediction by visually encoding state-action trajectories. The authors curated a dataset of 150K robot manipulation trajectories using visual trace prompting and fine-tuned it on OpenVLA.

### Strengths
- The paper introduces visual trace prompting, a novel technique that enhances spatial-temporal reasoning in VLA models for manipulation tasks by representing spatial-temporal relationships in robotic contexts.

- A curated visual trace prompting dataset was developed, with state-of-the-art 7B and 4B VLA models fine-tuned using this approach, providing an efficient method to improve VLA model performance.

- Their approach was rigorously validated through extensive evaluations across diverse simulated and real-world robot tasks, demonstrating superior generalization by leveraging spatial-temporal information.

### Weaknesses
 - While the author presented results highlighting the importance of historical information from the trace, there were no results demonstrating spatial reasoning capabilities as claimed in the "spatial-temporal" contribution. One potential approach could involve fine-tuning a Vision-Language Model (VLM) for line-drawing tasks, connecting it to low-level policy, and leveraging the VLM independently for spatial reasoning, similar to the RoboPoint framework.
  
- The author relied entirely on real-world data to generate the trace, which may have introduced variability from environmental factors such as lighting. Generating trace data in simulation could mitigate these issues, potentially minimizing the sim-to-real gap. Additionally, evaluating performance would be easier with ground truth data generated from a platform like RLBench across diverse tasks.

- Generalization in the Vision-Language Alignment (VLA) could be a strong aspect of this approach, as the data captures a general representation of actions conditioned on language. It would be beneficial for the author to test generalization on simulation benchmarks, such as the Colosseum, to showcase its robustness.

### Questions
Please refer to weakness section for my questions. I would consider raising my rating if the weaknesses mentioned in my questions can be addressed. Overall, I find this to be a strong paper that offers a valuable perspective on training VLA models beyond simply adding more data.

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
This paper introduces TraceVLA, a novel method which leverages visual traces to enhance the spatial-temporal awareness of VLA models. 
Specifically, the VLA model takes as inputs two images: a plain image and an image overlaid with traces of a set of active points.
The traces are generated by CoTracker and the active points are selected from a grid of dense points based on the changes in pixel locations.
The state-action history can be effectively communicated to the model through the provided visual traces.
Experiment results show that the proposed method outperforms comparing baseline methods in the SimplerEnv simulation environment and four real-robot tasks.
Ablation studies show that using visual traces is a more effective method for conveying historical information than prompting with text traces or appending historical image observation.

### Strengths
The proposed method, TraceVLA, is a neat and effective approach for providing large VLA models with historical state-action information.
Visual traces help VLA models to maintain awareness of the robot movements and do not introduce redundant information compared to appending historical image observations.
Experiments in SimplerEnv show that TraceVLA outperforms multiple comparing baseline methods in overall performance.
The paper also evaluates on real-robot tasks to validate the proposed method in the real world.
Ablation studies offer good insights on how leveraging visual trace prompts compares to other prompting strategies.

### Weaknesses
1. The experiments in the real world contains only one task for generalization assessment. It would be better to evaluate the proposed method in more generalization settings, including novel backgrounds and more novel tasks. This would provide a more comprehensive insight on the generalization capabilities of the proposed method.

2. RT1-X, despite having a much small number of parameters, outperforms TraceVLA-Phi3 with 3B parameters in SimplerEnv. The advantage of TraceVLA with 7B parameters is also not substantial. Is it possible to provide more discussions on potential reasons? Additionally, it would be beneficial to include RT1-X in real-robot experiments for comparison. In particular, observing how these two methods perform in generalization settings would be informative.

### Questions
1. The proposed method leverages CoTracker to provide visual traces. Were any failure cases due to inaccurate tracking observed during experiments? How robust is TraceVLA in handling these inaccuracies?

2. As the active points are selected based on changes in pixel locations, will points on moving background objects be chosen as active points? And how does the proposed method perform when the active points are located on irrelevant background?

3. How many iterations were used for training during fine-tuning on the data in real-robot experiments? Is the data from the pre-training stage also included in fine-tuning as well?

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
3

### Summary
This paper proposes overlaying the history trace on the RGB image as an indicator of spatial and temporal information to help large foundation models better manipulate objects. Experiments are conducted in both simulation and the real world.

### Strengths
Although trace has been implemented in various aspects, from my knowledge, this is the first time it serves as a history spatial-temporal information indicator. Comprehensive experiments and analyses are conducted to demonstrate its effectiveness, and the authors also consider real-time inference by optimizing the inference process.

### Weaknesses
1. The choice of active points depends on a threshold. Does this threshold need to be chosen differently for each robot or dataset? The paper does not provide sufficient detail on how this threshold is determined or if it requires tuning for different environments or robot embodiments. It's unclear if a single threshold value is universally applicable or if a more adaptive approach is needed.

2. In the analysis of trace length, the authors mention that a longer trace length can obscure key information. However, in the method, they state that they mitigate this by inputting both the original and overlay images. In that case, a longer trace length should not lead to worse results. This explanation seems self-contradictory. The paper needs to clarify how the dual input strategy truly mitigates the information loss from longer traces, especially considering potential overlap and visual clutter in the overlaid image.

3. For fine-tuning OpenVLA with history images, six history frames work best for TraceVLA, but this might be too redundant when using image. Would using three or two history frames be better when using history images as input? The paper lacks an ablation study on the number of history frames used as input to OpenVLA. It's not clear if the optimal number of history frames for TraceVLA directly translates to the optimal number when using raw images as input. The redundancy of information across multiple frames needs to be explored.

### Questions
Does the dataset used for fine-tuning OpenVLA contain scenes similar to those in simplerEnv? That is, are all the testing scenes entirely unseen in the training dataset?

### Soundness
3

### Presentation
4

### Contribution
3
