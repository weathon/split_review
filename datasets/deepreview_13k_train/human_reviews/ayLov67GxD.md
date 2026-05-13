# Video2Demo: Grounding Videos in State-Action Demonstrations

- Decision: Reject
- Scores: 3, 3, 5, 5

## Abstract
Vision-language demonstrations provide a natural way for users to teach robots everyday tasks. However, for effective imitation learning, these demonstrations must be perceptually grounded in the robot's states and actions. While prior works train task-specific models to predict state-actions from images, these often require extensive manual annotation and fail to generalize to complex scenes. In this work, we leverage pre-trained instruction-following Vision-Language Models (VLMs) that have shown impressive zero-shot generalization for detailed caption generation. However, VLM captions, while descriptive, fail to maintain the structure and temporal consistency required to track object states over time. We propose a novel approach, Video2Demo, that uses GPT-4 to interactively query a generative VLM to construct temporally coherent state-action sequences. These sequences are in turn fed into a language model to generate robot task code that faithfully imitates the demonstration. We evaluate on a large-scale human activity dataset, EPIC-Kitchens, and show that Video2Demo outperforms pure VLM-based approaches, resulting in accurate robot task code.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose using a video language model and a large language model in tandem to label videos from the Epic-Kitchens dataset with descriptions of the various subtasks demonstrated in the video in pseudo-code. They evaluate the ability of their method on this task using a handful of videos with hand-labeled pseudo-code descriptions.

### Strengths
**Well-written**: The paper is clear with good presentation, sound descriptions of the idea and clear experiments. The authors clearly state their setups.

### Weaknesses
Unfortunately, I am not fully convinced of the motivation behind this work. I enlist the weaknesses of this work below:
1. **Not enough evaluation**: it's very difficult to get a signal for the method's abilities given that evaluations are performed on contrived code for 7 videos. The evaluation set is extremely small, and the pseudo-code generation task is not a standard benchmark. This makes it difficult to assess the generalizability of the proposed approach. Furthermore, the lack of quantitative metrics for the pseudo-code generation makes it hard to compare against other potential methods.
2. **Choice of action space perhaps makes this task too easy**: Generating code is generally useful but in this setup, it's difficult to apply to real-life scenarios due to the level of abstraction. For instance, the reference code uses functions like “check_if_dirty(object)”, a level of abstraction for which we do not have good robot behaviors. In a sense, the method performs a kind of task-level planning. But the level of abstraction of this planning makes it impossible to test in a control setup. The action space is too high-level and symbolic, lacking the necessary grounding in the physical world to be directly useful for robotic control. The method essentially performs a form of symbolic planning, which is far removed from the low-level control required for real-world robotic tasks.
3. **Unclear motivation**: The authors claim that this work tries to ground videos into state actions and states for robot demos. Unfortunately, this is simply not true. They describe the state in videos using text and ground actions into pseudo-code. This far from the promise of a state-action demonstration. The method does not actually ground actions in a way that is directly usable for robots; instead, it translates video content into text-based state descriptions and pseudo-code, which is a symbolic representation, not a grounded one.
4. **No robotic evaluations**: The paper does not run any experiments on robots - neither in simulation nor on real robots. Therefore, I believe calling this a method to generate state-action demonstrations is an overclaim. The lack of any robotic evaluation, either in simulation or on real hardware, makes it impossible to validate the practical utility of the proposed approach for robotic tasks. The claim that this method generates state-action demonstrations is not substantiated by any empirical evidence in a robotic context.
5. **Extremely expensive to deploy on a robot**: The method requires making several calls per time step of execution to GPT-4 making this very very expensive.

### Questions
1. What was the cost of running these experiments?
2. Do you have one state for every image?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper aims to propose a model that can extract temporal-consistent (text) state and (text) action pairs from videos. In order to do so, the paper proposes the let VLM and LLM talk with each other to extract descriptions. Since LLM can see past communications and can be prompted to take VLM output critically, the extracted description can consistently track objects. To evaluate the method, the authors provides a human annotated state-action predicates for EPIC-Kitchens. Finally, the authors show that LLM can use such extraction as demonstrations to prompt LLM to synthesize robot code.

### Strengths
- The paper is well written and is easy to understand.

- The paper not only shows the perception power but also demonstrates downstream applications like code synthesis and planning.

- The paper contributes a small human-annotated validation set for EPIC-Kitchens, a nice contribution to the community who hopes to do similar work.

- All design choices are logical and sounds.

### Weaknesses
 - My main criticism for this paper is its contribution's significance. Using LLM and VLM with text as history seems like an obvious design choice. The techniques the authors introduced over the Socratic Model, namely the way to structure and prompt the LLM / VLM interaction doesn't seem to constitute enough contribution to be an ICLR paper.

- The evaluation itself relies on GPT, which is a bit weak despite the human annotation the authors provide. If the authors had proposed a structured output format like those used in VQA and have more annotations the evaluation would be much stronger. 

- There are also a few misleading claims. Throughout the paper, the authors talks about constructing "state-action" pairs, while in reality what they extract are some loose-form text predicates as well as loose-form text actions. Such abusive use of terms misleads the readers when they read the abstract.

Overall, I think the current status of the paper lacks the significance an ICLR paper would need.

### Questions
1. How big is the "Human-annotated state and action predicates" in claimed contribution 2? I think this is a nice contribution but from what I read in the paper, this doesn't seem to be very big. Could you clarify?

2. Could you clearly define "structure and temporal consistency" in the abstract?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper "Video2Demo" addresses the challenge of teaching robots everyday tasks through a novel approach using a combination of GPT-4 and Vision-Language Models (VLMs) like LLaVA. The approach consists of 2 phases. First, GPT-4 is prompted to  interact with the VLM to create temporally coherent state-action sequences from descriptive VLM captions. Moreover, GPT-4's capacity to follow up with the VLM for additional information or clarification further enhances the quality of the obtained responses. Second,  GPT-4 is prompted to generate robot task code that imitates the demonstrated actions. The approach is evaluated on the EPIC-Kitchens dataset, outperforming other methods. Key contributions include a new framework for transforming vision-language demonstrations into state-action sequences, annotated data for benchmarking, and superior performance in both state-action and code generation tasks.

### Strengths
Originality:  Video task description requires a combination of object identification, contextual analysis over time, and the application of common knowledge and reasoning to provide a comprehensive and coherent account of the video's content and events.
The paper introduces a useful system design with prompt engineering for interactive dialog between Vision-Language Models (VLMs) and Language Models (LLMs), providing a fresh perspective on task planning based on video data.

Quality:  The paper frames the problem of decoding what is happening in a video in the form of iterative dialog between VLM (like LLaVA) to answer queries about a frame and LLM (like GPT-4) for asking questions, and  deciding state-action predicates. 
The research is validated on real-world data (EPIC-Kitchens), and outperforms baselines in both state-action and code generation.

Clarity: The paper is well-structured and accessible, making it easy for a wide audience to understand. The key research questions and the failure cases are well discussed. The paper brings the problem of spatial grounding and hallucinations in LLMs and VLMs to the community's attention. This is reflected in the lower accuracy in symbolic state recall and action prediction. 

Significance: The paper addresses a significant challenge in robotics and AI, with potential applications in various domains, and introduces a valuable approach for interactive AI systems.

### Weaknesses
1. The paper motivates the problem of "teach robots everyday tasks". But there are no simulated or real robots experiments which makes it hard to assess the practicality of proposed approach and the possible failure scenarios. For example, how would the generated task plan compare to execute task in simulated environments like ALFRED [1].  The scope and possible future implication can be clear, like the proposed solution seems well suited for video comprehension, that can facilitate task planning.  
1. One of the reasons why the proposed approach may be unsuitable for robot is the possibility of compounding error over interactive dialog and the corresponding latency. 
1. Video2Demo relies heavily on prompt engineering, which requires considerable effort. It is unclear if the presented prompts are applicable to just EPIC kitchen videos only, or can be applied more broadly to other activity videos.

### Questions
1. Can it scale to beyond egocentric videos in EPIC kitchen to third-person tutorial videos? How would the prompt change, especially in the phase 2 where the prompts and state-action predicates seems to be centered on the human in the videos?
1. How does ChrF compare to other code generation metrics [1]? Does the generated code with high ChrF score correlate with human preference? How much of the generated code follow required syntax and physical feasibility to execute successfully on a simulator?  
[1] Zhou et al, 2023. CodeBERTScore: Evaluating Code Generation with Pretrained Models of Code. https://arxiv.org/abs/2208.03133

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes to use GPT-4 to interactively query a VLM to construct temporally coherent state-action sequences. Then it uses a prior method, Demo2Code, to generate robot task code that faithfully imitates the demonstration. Experiments on EPIC-Kitchens show it outperforms prior VLM-based approaches.

### Strengths
* The paper proposes an effective way to convert human video demonstrations to state-action sequences, which are useful for generating executable robot policies.
* The paper conducts extensive experiments on EPIC-Kitchens.
* The paper is well-written and easy to follow.

### Weaknesses
 * **Other LLMs and VLMs**: How do other LLMs and VLMs perform on this task? I am curious to see how this framework is generalized to other models.
* **GPT4-V**: It would be good to include some results of GPT-4V. I know its API is not released yet, but some quick experiments through ChatGPT's UI are sufficient.
* **Execution-based evaluation**: I wonder whether you can provide some execution-based results of robot code to prove the generated state-action sequences are really useful.
* **Prior works**: It would be good to discuss the paper's relationship to some additional prior works:

[1] ProgPrompt: Generating Situated Robot Task Plans using Large Language Models. Singh et al.

[2] VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models. Huang et al.

[3] Voyager: An Open-Ended Embodied Agent with Large Language Models. Wang et al.

### Questions
See weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
