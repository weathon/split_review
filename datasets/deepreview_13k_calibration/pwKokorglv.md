# Embodied Instruction Following in Unknown Environments

- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 5, 5, 3

## Abstract
Enabling embodied agents to complete complex human instructions from natural language is crucial to autonomous systems in household services. Conventional methods can only accomplish human instructions in the known environment where all interactive objects are provided to the embodied agent, and directly deploying the existing approaches for the unknown environment usually generates infeasible plans that manipulate non-existing objects. On the contrary, we propose an embodied instruction following (EIF) method for complex tasks in the unknown environment, where the agent efficiently explores the unknown environment to generate feasible plans with existing objects to accomplish abstract instructions. Specifically, we build a hierarchical embodied instruction following framework including the high-level task planner and the low-level exploration controller with multimodal large language models. We then construct a semantic representation map of the scene with dynamic region attention to demonstrate the known visual clues, where the goal of task planning and scene exploration is aligned for human instruction. For the task planner, we generate the feasible step-by-step plans for human goal accomplishment according to the task completion process and the known visual clues. For the exploration controller, the optimal navigation or object interaction policy is predicted based on the generated step-wise plans and the known visual clues. 
The experimental results demonstrate that our method can achieve 45.09\% success rate in 204 complex human instructions such as making breakfast and tidying rooms in large house-level scenes.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a hierarchical approach for embodied instruction following in unknown environments where room configurations may change due to human activities. The proposed approach consists of a high-level planner, a semantic feature map, and a low-level controller. Given an egocentric RGBD image, the agent updates its semantic feature map by weight-summing the newly obtained pixel-wise pretrained LongCLIP features and the old ones. The high-level planner receives as input a human instruction and the updated semantic feature map to generate high-level plans. For each high-level plan, the low-level controller predicts the target next location based on the semantic feature, text feature, and the high-level plan. The paper builds training and evaluation datasets based on ProcTHOR with GPT-4 and shows that the proposed approach achieves strong performance over the baselines.

### Strengths
- The paper is generally written well and easy to follow.
- The paper aims to address a challenging problem of EIF in environments that may change during the agent's task completion.
- The proposed approach achieves strong performance over the baselines.

### Weaknesses
 - Unknown environments are not well defined. An environment is comprised of many elements, such as layouts, textures, object classes and instances, *etc.* It is not clear what is unseen to the agent. In addition, existing EIF benchmarks, like ALFRED, also evaluate agents in "unseen" setups. What is the difference between the unseen environments used here and the existing EIF benchmarks?

- Unlike prior EIF literature, the paper uses depth as additional input, but such depth information is unreliable in many cases. It is unclear if the proposed approach can be applied to RGB-only scenarios like prior EIF benchmarks and noisy-depth scenarios.

- The proposed approach maintains a semantic "feature" map as scene representation. Why not directly use the projected depth map and semantics (*e.g.*, object classes) associated with the corresponding pixels? The features in the map are updated in a weight-sum manner, but we can simply replace the part of the semantic map of what the agent is currently seeing with the old one.

- The low-level policy is learned to predict the target navigational location in a supervised manner. While simulated environments can provide such labels, obtaining them in real-world scenarios may not be available. Can this proposed approach applied to these scenarios as well?

- In Table 3, Ours vs. Random Attention and No Attention show marginal drops. I'm not sure if the proposed component is indeed effective.

- It looks like the proposed task setup closely resembles the ALFRED benchmark. Incorporating the proposed approach to more recent state-of-the-art methods here may imply the generalizability of the proposed setup.

### Questions
See weaknesses above.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces a hierarchical embodied instruction following (EIF) framework for autonomous systems to complete complex tasks in unknown environments. It addresses the limitation of conventional methods that fail to generate feasible plans when deployed in environments with unknown objects. The proposed solution includes a high-level task planner and a low-level exploration controller, informed by multimodal large language models (LLMs). A semantic representation map with dynamic region attention aligns task planning and scene exploration with human instructions. The framework efficiently explores unknown environments to discover relevant objects and generate feasible task plans. The authors report a 45.09% success rate in executing 204 complex instructions in large house-level scenes, demonstrating the effectiveness of their approach over existing methods.

### Strengths
1. The motivation of the paper is very good, taking into account situations in real environments where items may not be present at the time of planning. 
2. The proposed framework is effective and also well-motivated. Combinations between high-level planners and low-level controllers are common, but the feature maps used in this work are interesting.
3. The paper is written in a fluid and well-organized manner.

### Weaknesses
1. In the main experiment the authors only compared LLM-P and FILM, the lack of other baselines weakens the superiority of the proposed approach. Here are three different types of baselines:

   (1) I would suggest adding some Object Navigation Method with LLM as Planner, such as MOPA[1], LGX[2].  

   (2) Another very similar work, Demand-driven Navigation [3] also uses human instructions as input, has similar tasks, e.g., "I am thirsty" with "I need to drink water" and similar task motivation. I would suggest for baseline comparison or discussion at related work. 

   (3) Multimodal LLM like GPT-4o, Gemini, LLaMA-3.2, Qwen2-VL can be directly used as baselines.

2. Need more details on task setting: 

   (1) What is the step limit for each task? 

   (2) How to determine task success and failure? If the agent completes the task with an undocumented solution (i.e., it was successful in the human viewpoint, but was not judged successful in simulator), how should the result be determined, or is there a high probability of this occurring?

   (3) If the task is partially successful, e.g. I want drink a cup of water, find the cup, but not the water, how should it be determined? Or conversely, would it make a difference if the water source is found but not the cup? 

3. How much time and computational resources are needed for inference per task execution and how does it compare to baselines? Since the method uses a multimodal LLM like LLAVA, the speed of inference and computational resources are very important if it is to run in a real environment.

4. I believe the superiority of the methodology could have been enhanced if the authors could supplement experiments in real environments.

5. Need more details on the action space:

   (1) Does the agent need to have a knife in its hand to perform the Slice action? What happens if the agent does not have a knife in its hand but outputs a Slice? For other action, is there any precondition?

   (2) Can an agent only PickUp one item in hand at a time? Will it fail if it first PickUp item A and then item B?

   (3) How are Navigation low-level actions generated?

### Questions
see weaknesses.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a novel embodied instruction following (EIF) method focused on scenarios that require executing complex tasks in unknown environments. The approach leverages a hierarchical EIF framework with a high-level task planner and a low-level exploration controller based on multimodal large language models. Utilizing semantic feature maps and dynamic region attention mechanisms, the method aligns task planning with the exploration process to fulfill complex human instructions. In extensive experiments within a large simulated environment, the approach demonstrated significantly improved success rates for complex tasks, such as preparing breakfast and organizing rooms, showing clear advancements over existing methods.

### Strengths
The use of scene feature maps to facilitate exploration in unknown environments, serving as visual input for VLMs while integrating textual instructions, presents an intriguing, well-founded, and promising approach. This framework combines planning and action seamlessly through the high-level task planner and low-level exploration controller, resulting in a cohesive and efficient system for embodied instruction following.

### Weaknesses
Experimental Environment Limitations: This method has been validated on a single simulator. It would strengthen the evaluation to include additional simulators, such as Habitat or iGibson, or to test the method on a real-world robotic platform to further demonstrate its robustness.
Limited Scalability and Computational Efficiency: The approach currently shows limited scalability and relatively low computational efficiency, which could impact its practical deployment in larger environments.
Lack of Comparative Models: The paper does not compare against certain state-of-the-art general models. For example, it would be interesting to see how a zero-shot baseline like GPT-4o performs across the various evaluation metrics.

### Questions
When will the code be open-sourced? Can the 7B version of LLaVA really handle such complex and diverse tasks that require precise outputs? Additionally, as far as I know, the 7B model of LLaVA has limitations in understanding depth maps. I’m surprised by the performance described in your paper!

### Soundness
1

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper introduces a modular approach for embodied instruction following tasks, which consist of three components: 1) high-level planning, 2) low-level control, and 3) building semantic feature maps. The proposed approach employs the LLaVA models and fine-tunes them on data generated by GPT-4 and the ProcTHOR simulator. Experiments show the comparison with baselines, ablation studies, and qualitative analysis to verify the effectiveness of the proposed approach.

### Strengths
Strengths
- The paper presents a new modular approach for embodied instruction following tasks, consisting of a high-level planner, low-level controller, and online semantic feature map. 
- The paper conducts diverse analysis, including ablation studies and qualitative analysis, which helps to understand the proposed method.

### Weaknesses
Weaknesses
- I find no clear distinction between the “unknown environments” mentioned in this paper and existing test environments. Existing studies have also validated their proposed approach in unseen environments where embodied agents do not observe during training. Furthermore, prior work like LLM-Planner leverages the off-the-shelf object detector to feed the detected objects into LLMs, rather than providing all object categories with LLMs. How unknown environments are qualitatively or quantitatively different from unseen environments? Can authors verify the difference?

- In my current understanding, the paper conducts unfair comparisons. The proposed approach based on LLaVA is fine-tuned on 2k instructions generated by GPT-4, but the baseline model (LLM-Planner [1]) is a few-shot learning method that just uses 9 samples for in-context learning. The authors should compare their proposed method with more powerful models like EPO [2] which is trained on the in-domain data.  



### Questions
- In the paper, the train and test data share the same data distribution. Why do the authors use the word unknown environments?
- How the performance will be if the LLaVA model is trained on limited amounts of data (i.e., few-shot or zero-shot)?

### Soundness
1

### Presentation
2

### Contribution
2
