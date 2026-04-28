# AHA: A Vision-Language-Model for Detecting and Reasoning Over Failures in Robotic Manipulation

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 5, 6, 8

## Abstract
Robotic manipulation in open-world settings requires not only task execution but also the ability to detect and learn from failures. While recent advances in vision-language models (VLMs) and large language models (LLMs) have improved robots' spatial reasoning and problem-solving abilities, they still struggle with failure recognition, limiting their real-world applicability. We introduce \name, an open-source VLM designed to detect and reason about failures in robotic manipulation using natural language. By framing failure detection as a free-form reasoning task, \name identifies failures and provides detailed, adaptable explanations across different robots, tasks, and environments. We fine-tuned \name using \texttt{FailGen}, a scalable framework that generates the first large-scale dataset of robotic failure trajectories, the \name dataset. \texttt{FailGen} achieves this by procedurally perturbing successful demonstrations from simulation. Despite being trained solely on the \name dataset, \name generalizes effectively to real-world failure datasets, robotic systems, and unseen tasks. It surpasses the second-best model (GPT-4o in-context learning) by 10.3\% and exceeds the average performance of six compared models—including five state-of-the-art VLMs—by 35.3\% across multiple metrics and datasets. We integrate \name into three manipulation frameworks that utilize LLMs/VLMs for reinforcement learning, task and motion planning, and zero-shot trajectory generation. \name’s failure feedback enhances these policies' performances by refining dense reward functions, optimizing task planning, and improving sub-task verification, boosting task success rates by an average of 21.4\% across all three tasks compared to GPT-4 models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work targets the task of open-world failure detection and reasoning under the scenario of robotic manipulation, which is critical and valuable for diverse downstream tasks. Specifically, the authors propose a procedural pipeline for generating failure demonstration data for robotic manipulation in simulation, upon which they fine-tune a vision-language model (VLM) for failure detection and reasoning. Moreover, they demonstrate improved performance brought by the fine-tuned VLM in three downstream tasks, namely reward function design, task-plan refinement, and sub-task verification. Comprehensive comparison with the other six VLMs also shows the superior performance of the proposed technique on this task.

### Strengths
- The paper tackles an important problem that is highly beneficial and safety-critical when learning-based robotic algorithms are deployed in the real world;

- The developed procedural pipeline of simulation data generation is useful for researchers in the community who are willing to contribute to this direction;

- It is inspiring to see that not only improved performance is shown on the standalone task, but to see the strong benefits brought by such improvement on different related and popular downstream tasks.

- Though failure detection is an important prerequisite for the reasoning part, I am still glad to see the efforts in investigating the failure reasoning and especially its usage in the downstream tasks.

- The presentation is generally well-structured and easy to follow.

- Though benchmarking experiments are conducted in the simulation, their results are comprehensive and informative.

### Weaknesses
Presentation:
- It would be clearer if subsection 4.1. can be shortened a bit and described with a more concise mathematical formulation. 

- To reinforce the contribution, I would suggest adding a subsection in the method section to explain how improved failure detection and reasoning performance can help these downstream tasks. In the current draft, putting this part in the experiment section is less apparent and inspiring for potential readers in these fields. 

- Closely related to the point above, it seems that the usage of the proposed idea in downstream task 2 (refine task plans in TAMP) and task 3 (improve task verification) is essentially similar, i.e., detect and reason for the failure of the sub-tasks. It might be more lucid for the readers to group these two tasks together along with the reward design task and make a taxonomy for different high-level manners of how failure detection and reasoning can help. 

- in sub-section 4.1., "Unlike previous works that primarily focus on detecting task success as binary classification problem, we approach failure reasoning by first predicting a binary success condition ("Yes" or "No") of the given sub-task based on a language specification and an input image prompt." seems less straightforward to understand. Logically, I suspect the author wants to express that they have an additional reasoning part after the detection step. 


- Fig.1 and Fig.2 are hard to read. It would be better to reorganize the sub-figures and increase the sizes of the images and texts.

Methodology:

- The first point I would like to raise is the lack of discussion of hallucination in LLM/VLMs. In the introduction, the authors motivate the failure recognition with the shortcoming of hallucinations in LLMs/VLMs. However, the proposed fine-tuned VLM will still suffer from this issue. It would be important to discuss how to mitigate this issue in detecting failures. In this regard, there is a missing citation that is closely related to this work, which made an initial attempt in this direction based on the uncertainty derived from the VLM. I would suggest the authors add a discussion on this aspect. It would also be meaningful to see the influence of fine-tuning with the proposed data set on the performance of uncertainty estimation. Will there be a trade-off between the performance of the prediction accuracy and uncertainty estimation?  

- The second point is related to the design of the technique. In [1], it has been observed that using the "chain-of-thoughts" (CoT) analysis in the prompt template can improve the performance of failure detection. Therefore, related to the reasoning part of this work, will the reasoning part be able to help improve the performance failure detection? Will the performance be influenced by the different prompting templates, e.g., with and w/o CoT?

Experiments:

- Due to missing real-world experiments, therefore, it is hard to evaluate the performance loss during sim-to-real transfer and the actual practicality of the proposed technique. 


### Questions
Side questions (major ones in the Weaknesses section above)

- In subsection 3.1., why separate the rotation failure into incorrect and missing ones? Should these two belong to the same category?  

- An ablation study on how many camera viewpoints would be insightful for the real-robot applicability of the proposed method.

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
3

### Summary
This paper introduces AHA, a new VLM model to identify and describe failure modes in robot manipulation. The authors introduce a pipeline called FailGen to generate failure demonstrations and use the data to train AHA. In the experiments, AHA demonstrates improved performance in failure reasoning. The authors also show its effectiveness in downstream application including VLM-based reward design, planning, and subtask verification.

### Strengths
1. The idea of using failure detection VLM to improve VLM-based robotic application is interesting.
2. The effort in developing a failure dataset is valuable towards building robust large models that can understand the physical world.

### Weaknesses
1. [Soundness] It remains unclear to me whether incorporating failure descriptions is a reliable approach to improve VLM in reward design, planning, and subtask verification. For example, in the VLM-based reward design, although VLM can provide some penalty reward terms based on AHA input to correct behavior, there is no guarantee the new reward can make robot perform better than the previous one (e.g. the penalty can be too large and hinder skill learning). In this case, I would like to see if the proposed method can show some iterative reward tuning behavior based on failure feedback and the procedure can converge (i.e., tuning the strength of new terms or number of terms to correct behavior).

2. [Clarity] The paper can be much clearer and convincing if the authors can show more extensive comparisons between AHA and GPT4 to understand what leads to the improvements. For example, is the improvement due to GPT4 not being able to generate accurate failure description? Or, is it simply because the generated failure text is too lengthy for the downstream VLM model to understand? I encourage more explicit discussion on what a good failure description looks like (for downstream task VLMs). I also suggest comparing to human oracles with different writing styles.

3. [Result: Generalization] The paper is focusing on simple pick-and-place style tasks in clean backgrounds. How about more challenging and dexterous tasks? I would like to see the results on more challenging task such as guiding a robot hand to perform grasping and reorientations where the failure modes can be more fine-grained and complex. Besides, explicitly discussing generalization to diverse backgrounds / objects is also necessary. The results on these harder setups can help readers to understand the opportunities and challenges of AHA in application.

### Questions
See the weaknesses part. The idea is interesting and I would like to raise my score if the authors can show some rigorous results to clarify the points above, especially 1 and 2. I also encourage discussion on negative results to help readers see the limitation and potential of the current version.

### Soundness
2

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work proposes a VLM for detecting and reasoning about failures in robotic manipulation, which can be applied in various downstream tasks.

### Strengths
1. The motivation is meaningful, and I agree that addressing failures in robotics is important.
2. It can be utilized in downstream tasks.
3. The website has many great demos.

### Weaknesses
I think the types of failure modes and the reasoning responses are somewhat rough. And more details and experiments need to be conducted. For further details, please refer to the "Questions" section.

### Questions
1.What is the difference between rotation and no rotation?
2.What are the details of your baseline settings? I couldn't find them in your paper.
3.Are you using the REFLECT framework for your baseline? If not, I believe REFLECT is highly relevant to your work, so I would like to see a comparison of its performance with your model.
4.How do you plan to extend your failure types? As of now, I still find them somewhat rough.

My main concern is the sufficiency of the experiments and the work still seems somewhat preliminary. However, if you address my concerns, I will be inclined to raise my score.

### Soundness
2

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
5

### Summary
The paper presents a Vision-Language Model (VLM) for robotic failure reasoning, introducing a failure dataset and fine-tuning the VLM to achieve this goal. The approach demonstrates promising performance.

### Strengths
Failure trajectory generation can be extended to other scenarios (simulatores), encompassing a comprehensive set of failure categories. Failure reasoning plays a critical role in downstream policy learning, which is essential for advancing the entire community

### Weaknesses
Baseline Comparisons:
 - Clarity of Baseline Implementation: The implementation details of the baselines are unclear. What type of input data are the baselines using? Is it a single image, a sequence of images, images from multiple views, or video? This distinction significantly affects baseline performance. For instance, Gemini excels at reasoning for robotic manipulation when using video inputs, but its performance would likely degrade if multiple-view images were used instead. The paper needs to specify the exact input format for each baseline, including the number of views, the temporal sequence length (if any), and whether the images are processed individually or as a sequence. Without these details, it's impossible to determine if the comparison is fair and if the reported performance differences are due to the model architecture or the input data format.

 - Lack of Comparison with Robotic-Specific Methods: Why not compare your approach with other robotic-oriented reasoning methods mentioned in the 'Introduction' or 'Related Work' sections? The current experiments only compare against general Vision-Language Models (VLMs), which are not specifically designed for robotic tasks. The paper should include comparisons with methods that explicitly address robotic failure reasoning, such as those that incorporate state information or use specific robotic datasets. This would provide a more relevant benchmark and better demonstrate the advantages of the proposed approach.

View Angle Concerns: The camera view angles during training are fixed according to the RLBench settings. This raises concerns about the view angles during testing. Specifically: 1) How many views does the model require during testing? 2) Should the view angles during testing match the exact poses used in the RLBench training setting?

- Missing Reference to Figure 1: Figure 1 is not referenced or discussed anywhere in the paper, which needs to be addressed for clarity and completeness.

### Questions
- View Angle Concerns: The camera view angles during training are fixed according to the RLBench settings. This raises concerns about the view angles during testing. Specifically: 1) How many views does the model require during testing? 2) Should the view angles during testing match the exact poses used in the RLBench training setting?

- Missing Reference to Figure 1: Figure 1 is not referenced or discussed anywhere in the paper, which needs to be addressed for clarity and completeness.

### Soundness
3

### Presentation
3

### Contribution
3
