# Task-oriented Sequential Grounding in 3D Scenes

- Decision: Reject
- Scores: 3, 5, 6, 5

## Abstract
Grounding natural language in physical 3D environments is essential for the advancement of embodied artificial intelligence. Current datasets and models for 3D visual grounding predominantly focus on identifying and localizing objects from static, object-centric descriptions. These approaches do not adequately address the dynamic and sequential nature of task-oriented grounding necessary for practical applications. In this work, we propose a new task: Task-oriented Sequential Grounding in 3D scenes, wherein an agent must follow detailed step-by-step instructions to complete daily activities by locating a sequence of target objects in indoor scenes. To facilitate this task, we introduce \dataset, a large-scale dataset containing \textit{22,346 tasks with 112,236 steps across 4,895 real-world 3D scenes}. The dataset is constructed using a combination of RGB-D scans from various 3D scene datasets and an automated task generation pipeline, followed by human verification for quality assurance. We adapted three state-of-the-art 3D visual grounding models to the sequential grounding task and evaluated their performance on \dataset. Our results reveal that while these models perform well on traditional benchmarks, they face significant challenges with task-oriented sequential grounding, underscoring the need for further research in this area.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces a new visual grounding task called Task-oriented Sequential Grounding. It presents a large-scale dataset SG3D and its benchmark and makes efforts to move beyond traditional 3D visual grounding towards more practical, task-oriented applications. On this new benchmark, this paper implements different models to fit the sequential VG setting and analyze the new challenges with comprehensive experimental results.

### Strengths
1. It designs a Visual Grounding task more closely aligned with real-world applications.
2. The paper provides a detailed discussion of the process for generating the SG3D dataset, including the specifics of how prompts are designed to generate tasks and the measures taken to minimize potential biases during the generation process.
3. The paper provides the basic experimental results on the new benchmark and implements several baselines from different paradigms, and a human study further validates the benchmark's validity.

### Weaknesses
The main concern is that this benchmark does not fundamentally differ from traditional VG benchmarks, or at least does not justify what new significant challenges this benchmark brings (both in the data generation pipeline and experimental analysis). From my perspective, It simply incorporates a "task" narrative background into Visual Grounding, and the "Task-oriented" is reflected only in the (1) use of task information in samples and (2) sequential text inputs. However, how these two designs bring new fundamental problems to the VG problem needs further exploration. For example, the task-oriented setting can incorporate the situation information or more complex semantic understanding (wash hands -> find a sink) under this background, but this has also been discussed in Situated QA (SQA) and ScanReason. Or this setting involves navigation to make the setting different from pure VG / involves context understanding (among sequential actions) in a single-step solution.

In summary, the authors need to figure out how to better justify the fundamental value of this benchmark, showing it is not just a simple combination of several single-step VG with only task-related prompts. I strongly recommend that the author improve the paper and make this new benchmark more convincing. I would also consider raising the score if the author can provide a satisfied response or explanation regarding this concern.

### Questions
1. In this benchmark, could you provide examples of how context is demonstrated in its role? Is a model only required to have the ability to ground objects from the text of a single action step to complete this task? An ideal example would be when there are multiple instances with the same object type (distractors), where the model needs to use information from previous action steps to select the correct one among these, although this example may also be incremental compared to previous VG benchmarks (only longer context for VG). Are there such examples, and if they exist, can you provide and quantify the proportion of such cases in SG3D?
2. For the analysis of the effect of offering contextual information in the Ablation Study, to ensure consistency, I believe a reasonable approach is the following: Use the same model trained on the original training set and test it both on the original test set and a test set “with only the current action step,” then compare the results. Alternatively, train models separately on the original training set and a training set with “only the current action step” and test both models on the original test set to compare the experimental results.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
- The authors proposed a novel task, Task-oriented Sequential Grounding in 3D scenes, to address the gap between object-centric and task-driven grounding required for practical Embodied AI applications.
- The authors constructed a novel large-scale dataset for the Task-oriented Sequential Grounding in 3D scenes named SG3D, which contains 22,346 tasks with 112,236 steps across 4,895 real-world 3D scenes. They used GPT-4 based labeling of 3D-scenes from popular datasets: ScanNet, ARKitScenes, 3RScan, MultiScan, HM3D.
- The authors explored several representative approaches for solving the proposed task: the dual-stream multimodal model 3D-VisTA, the query-based model PQ3D, the 3D LLM LEO.
- The authors also made a working demonstration of the developed dataset available in an anonymous online project.

### Strengths
1. The authors created a large-scale SG3D visual grounding benchmark based on adding additional automated text markup to 3D scenes from well-known datasets ScanNet, ARKitScenes, 3RScan, MultiScan, HM3D. Such a dataset is useful for planning actions by an intelligent agent on static scenes. 
2. The authors clearly demonstrated the advantages of the task-oriented steps in SG3D and object-centric referrals they created, including using the example of markup from ScanRefer for the same target objects.

### Weaknesses
1. The introduction and abstract note the usefulness of the created dataset for intelligent agents and robots, but the task examples shown in Figure 1 look strange for a robot agent. They may be useful for NPC characters in computer games, but the authors do not mention this in the introduction. In this regard, the authors are asked to adjust the introduction to more accurately explain the motivation for the work done.

2. To demonstrate the quality of modern methods on the created dataset, the authors use only three models 3D-VisTA, PQ3D, and LEO (one model per category: Dual-stream, Query-based, 3D LLM). At the same time, their choice is not sufficiently justified. In Related Works, the authors also note the existence of other models that are not included in the comparison of approaches, which reduces the quality of the constructed benchmark. This also raises questions about the completeness and sufficiency of the results shown in Table 1. The Appendix section contains metrics for three other models: Vil3DRef, ViewRefer, MiKASA-3DVG, it is recommended to move them to the main text of the article, but the choice still requires explicit justification.

3. The article lacks an ablation study for the selected modifications of the 3D-VisTA, PQ3D, and LEO models, which would also add validity to the results obtained. Moreover, the adaptation of these models is noted as one of the contribution points.

4. During the benchmark, the authors considered the combination of only pre-trained GPT-4 (with closed code) and 3D object classifier. However, it would be interesting to see the same experiment with other open-source models, the results of which would be easier for researchers to reproduce.

### Questions
1 Why was GPT-4 chosen to generate diverse tasks when creating the dataset? Did the authors try using other LLMs (Mistral/LLAMA) for this?

### Soundness
2

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
3

### Summary
This paper introduces Task-oriented Sequential Grounding, where a long-horizon task with detailed steps is given, and the objects of interest need to be localized considering not only the current action step but the entire task context. This paper also introduces SG3D, a large-scale dataset for the above task, which includes over 22k tasks and 112k steps. This paper also finetunes and evaluates 3 typical 3D-VL models on SG3D, including a dual-stream model, a query-based model, and a 3D LLM, as well as the GPT-4 with an object labeler. Results show that these models struggle to transfer to SG3D without finetuning. After finetuning, their performance is still limited (<40%). This shows the open challenges existing in the proposed task and dataset.

### Strengths
1. The paper proposes the sequential grounding task and a new dataset for this task. Compared to existing visual grounding tasks, sequential grounding needs the agent to incorporate more environmental and instructional context. This is more challenging in terms of 3D visual grounding. 

2. The paper provides a detailed analysis of the introduced dataset. 

3. This paper evaluates several existing 3D vision-language model baselines on the proposed task. The results show that these models only show limited performance, and there is a research gap to be filled. Ablation studies also show the importance of contextual information and the effect of the amount of training data. 

4. This paper is well-written and easy to follow.

### Weaknesses
1. The definition of the sequential grounding task is limited. The only thing it provides is the links between each step in a sequential task plan and the 3D object involved. And several other factors important for real task planning are not provided. For example, how is each "step" decomposed into action (the action for agent to perform) and object (where the action is performed)? What are the pre- and post-conditions for each action? How can the agent assure that the desired object is really in the scene and how can it recover if it is missing? How to use tools (this paper assumes each step involves at most one object)?  Therefore, the proposed task and dataset are quite limited to the *3D object grounding (or navigation) with longer context* itself, and it does not seem to help much for real-world task planning.

2. It's not clear what's the embodiment of the proposed dataset, i.e. what agent is going to perform the task? Although the paper mentions "robot" several times, clearly some tasks/steps in the proposed dataset are not designed for robots, but for humans, like "enjoy reading before bed" and "wash your hands thoroughly in the sink". How can these instructions for humans be useful for AI? Later when it moves to the real-world execution and evaluation stage, how can the proposed dataset help task planning?

3. This paper does not propose a novel method (a stronger baseline) for the proposed task.

4. Images in Figure 9 Task 1 are too blurry. I cannot tell whether predictions are reasonable or not.

### Questions
Please see "weakness" section above.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a novel benchmark, SG3D (Task-oriented Sequential Grounding in 3D scenes), designed for task-oriented sequential grounding in 3D environments. This dataset, built on 3D scene data from sources such as ScanNet, ARKitScenes, and HM3D, includes 22,346 tasks with over 112,000 steps across 4,895 3D scenes. Unlike traditional 3D grounding tasks, SG3D emphasizes the sequential, task-oriented nature of grounding, where an agent must follow detailed multi-step instructions, each step requiring context-based object identification. The authors adapted existing models, including 3D-VisTA, PQ3D, and LEO, to this new setting, demonstrating that these models face significant challenges under SG3D’s task requirements. Their work highlights the gap in current models' ability to perform consistent, sequential grounding in complex environments, underscoring the need for specialized approaches.

### Strengths
The SG3D dataset is built on a diverse foundation, incorporating 4,895 3D scenes spanning five distinct categories, resulting in a robust and varied dataset. The task-centered design of textual instructions, focused on guiding sequential actions rather than mere object identification, is particularly valuable.

### Weaknesses
The experimental evaluation is somewhat unclear, making it difficult to discern whether the model outputs bbx or target IDs. If the output is bounding boxes, the supplementary material lacks the corresponding label data, while if it is target IDs, the origin of the bounding boxes in Figure 9 remains unexplained.
The proposed method outputs only target-specific information at each step, without addressing movement between steps, which raises questions about continuity. Specifically, is the scene input 𝑆 the same for each step? If so, this would contradict the perspective shifts caused by position changes in real-world applications.
Additionally, the dataset's purpose seems limited and somewhat misaligned. Fundamentally, it focuses on grounding tasks, where multiple steps appear unnecessary and potentially confusing, with their only purpose seeming to ensure consistency across objects. Without a memory mechanism, ensuring consistency without knowledge of prior steps feels unconvincing. The dataset thus lacks a strong rationale for multi-step grounding, as it does not effectively integrate planning or contextual continuity. Furthermore, the claim that the task requires understanding each step in the context of the whole plan is not adequately supported by the dataset design or experimental setup, as the models are not explicitly evaluated on their ability to leverage such contextual information.

### Questions
Is the scene input 𝑆 the same for each single-step grounding?

### Soundness
2

### Presentation
2

### Contribution
2
