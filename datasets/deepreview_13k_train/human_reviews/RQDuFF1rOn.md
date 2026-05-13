# Solving Robotics Problems in Zero-Shot with Vision-Language Models

- Decision: Reject
- Scores: 5, 3, 3

## Abstract
We introduce Wonderful Team, a multi-agent Vision Large Language Model (VLLM) framework designed to solve robotics problems in a zero-shot regime. In our context, zero-shot means that for a novel environment, we provide a VLLM with an image of the robot's surroundings and a task description, and the VLLM outputs the sequence of actions necessary for the robot to complete the task. Unlike prior work that requires fine-tuning parts of the pipeline -- such as adjusting an LLM on robot-specific data or training separate vision encoders -- our approach demonstrates that with careful engineering, a single off-the-shelf VLLM can autonomously handle all aspects of a robotics task, from high-level planning to low-level location extraction and action execution. Crucially, compared to using GPT-4o alone, Wonderful Team is self-corrective and capable of iteratively fixing its own mistakes, enabling it to solve challenging long-horizon tasks. We validate our framework through extensive experiments, both in simulated environments using VIMABench and in real-world settings. Our system showcases the ability to handle diverse tasks such as manipulation, goal-reaching, and visual reasoning---all in a zero-shot manner. These results underscore a key point: vision-language models have progressed rapidly in the past year and should be strongly considered as a backbone for many robotics problems moving forward.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces wonderful team, a multi-agent system that uses several VLMs to perform various tasks in a robotic system, including high-level planning, subgoal verification, target grounding, iterative refinement and memory updates. The system is able to perform long-horizon rearrangement tasks in a zero-shot manner and outperforms baselines without multi-agent interactions.

### Strengths
- Very good system design. Things like iterative refinement and memory updates are very important for tasks requiring long-horizon reasoning and precise actions, and are often overlooked in prior works using multi-agent VLM systems for robotics.
- Detailed appendix which amends a lot of missing contexts in the main text, including task details, ablation studies and comparisons to additional baselines like PIVOT. It is interesting to see that PIVOT underperforms direct-outputGPT-4o. I also really like Sec. A, which shows the amazing progress of VLM backbones.

### Weaknesses
- The paper is overclaiming. Wonderful team is not a complete robotic system, and it does not “solve robotics problems” on its own. It outputs 2D/3D point targets that need to be converted to joint torques for execution on a real robot. The closest analogous system is probably RoboPoint [1]. The title, abstract, and introduction should be re-written with appropriate scope.
- Lots of details are missing details on the set up of low-level robotic systems. How does the robot execute the output of the VLMs in the implicit goal planning (Sec. 5.2) and spatial planning (Sec. 5.3) tasks. By the way, spatial planning is a really bad name, since none of the tasks in Sec. 5.3 involves reasoning about spatial relationships.
- If I interpret Sec. B.2.2 in Appendix correctly, almost half of the tasks in VIMA bench are not included in the comparison with baselines in Fig. 9. This is absolutely a red flag and raises questions about the validity of other comparisons in the paper as well. Please clearly state in the main text which tasks are used for comparison, and how many trials are performed for the proposed method and for each baseline.
- Some limitations are not clearly stated. For example, the system only works with well-calibrated front and overhead views. This is my interpretation from the experiment set up in Sec. B of the Appendix.

[1] Yuan, Wentao, et al. "RoboPoint: A Vision-Language Model for Spatial Affordance Prediction for Robotics." arXiv preprint arXiv:2406.10721 (2024).

### Questions
- Is the low-level system robust? Are there cases where the proposed method/baseline fail because of e.g. object slipping from grasp, motion planning failures, or failure to maintain contact during execution (for tasks like drawing and wiping)?
- It would be nice to have some examples visualizing the feedback loop between the verification agent and the supervisor, and between different agent in the grounding team. Are the examples in Fig. 3, 4 and 5 for illustration only or are they actual outputs from the eval runs? I am curious what kind of clarification questions would the verification agent ask, also how the G-checker gives feedback to move the target in the correct direction.

### Soundness
2

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents “Wonderful Team,” a framework using multi-agent Vision-Language Models (VLMs) to address robotics tasks in a zero-shot setting. This system integrates high-level planning and low-level action execution within a single VLM framework, leveraging interconnected agents to coordinate tasks without fine-tuning on specific environments. The authors validate the framework on both simulated and real-world tasks, such as object manipulation and spatial planning, aiming to showcase VLMs as a robust solution for zero-shot robotics.

### Strengths
1. Integrating task and motion planning is important. 
2. The system utilizes VLMs’ reflection capabilities, allowing iterative refinement and self-correction, beneficial in long-horizon tasks.

### Weaknesses
1. While this work demonstrates a valuable application of VLM for task planning, its novelty appears somewhat limited, as it omits several key references from the literature review. Recent advancements in visual prompting methods, particularly MOKA [1], are notably absent. This omission is particularly significant because the approach presented in this paper exhibits substantial overlap with MOKA’s methodology, especially in terms of employing Vision-Language Models (VLMs) for task planning and action grounding. Both works leverage affordance-based reasoning mechanisms to facilitate task execution, but this paper fails to distinguish how its contributions diverge from or advance beyond those in MOKA. In addition, MOKA extends its capabilities beyond simple pick-and-place tasks by incorporating tool functionality and waypoint planning. This is entirely missing from the current work, which limits its applicability and breadth in real-world scenarios.  
2. Certain aspects of the writing could benefit from clarification, and a few claims appear overstated. A few suggestions:
  1. The term “robotics problems” in the abstract could be more specific. Does it refer to manipulation tasks specifically? The current phrasing may imply a broader scope than the evaluation supports.  
  2. The claim of handling “unstructured environments,” such as cluttered scenes, appears unsubstantiated by the presented evidence (Lines 37-38).
  3. Terms like ‘low-level coordinates generation’ might not accurately describe the perception components; alternative phrasing could improve clarity.
  4. Bold text is overused and using it selectively may help in emphasizing key points more effectively.
  5.  In Line 59, the meaning of ‘abstract’ tasks could be further elaborated to clarify its context within this work.
  6. The heading in Section 6.1 (“COMPARISON WITH METHODS THAT TRAIN”) feels somewhat casual; a more formal title might enhance readability.

3. Additionally, the literature review lacks a discussion on the extensive work in task and motion planning (TAMP), which would be especially pertinent when addressing integrated task and motion planning approaches.  
4. The evaluation could be more comprehensive and clearer in several areas:
  1. The evaluation predominantly addresses simple pick-and-place tasks. For a claim of addressing “robotics problems in a zero-shot regime,” broader task diversity would strengthen support for this assertion.
  2. The action primitives used in the evaluation remain somewhat ambiguous. In VIMABench tasks, for instance, it seems that the primary primitive is pick-and-place. It would be useful to clarify whether the VLM can generate more complex actions, such as unscrewing a cap, using image coordinates.
  3.  Finally, it is unclear how the model determines depth during execution. If it directly relies on depth estimation, a discussion on handling potential occlusions would add clarity and demonstrate robustness.

[1] MOKA: Open-World Robotic Manipulation through Mark-Based Visual Prompting

### Questions
see weakness.

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors propose to use large vision-language models for zero-shot robot control, specifically by using them as simulacra of a team of agents that each are responsible for a step in the planning, grounding, and execution process.

### Strengths
- The authors adopt an interesting presentation structure, wherein they present rhetorical questions meant to explicitly discuss the problems in using (V)LMs for robot control and their potential solutions to them. I greatly appreciate this.
- The idea of breaking up robotic control stacks into sub-”teams” is very sensible. It is inherently supported by e.g., ROS’s node communication architecture. It makes sense to break up a zero-shot (V)LM based control stack in a similar way.

### Weaknesses
- As I stated above, I do appreciate the motivating examples’ rhetorical questions for communicating and justifying the authors’ approach. However, a lot of the time, the examples seem poorly motivated or insufficiently empirically supported. 
  - For instance, we see that the VLM fails at generating bounding boxes for some grapes on a table. This seems exactly like the kind of thing that grounding DINO, SAM, OWL, etc would be able to handle with minimal issues zero-shot.
  - Given that, why not use some kind of hybrid approach, where the VLM critiques the output of some other vision model? That way, you enjoy the benefits of the specialized vision model, but can also have the VLM detect edge cases where the detections are not very good. Basically, it does not seem justified to exclusively use VLMs in the “team.”
  - More citations showing that the presented issues are actually issues that affect many approaches for integrating VLMs with robots would be appreciated. As it stands, a lot of them seem to just be from the authors’ empirical experience, and even then, there are often insufficient examples for demonstrating this.
- Additionally, despite their deficiencies, the rhetorical motivating examples take up a lot of space. Even with the extended page limit for this ICLR, it seems like the authors have very limited descriptions of what agent modules they include (and details like what they do, how they achieve that, etc) in the main body of the paper. Given that this is the main contribution, I do not think that information should be relegated to the appendix. 
  - I likewise think that the team descriptions in the appendix can be condensed significantly.
- Even after looking at the details in the appendix, several critical pieces of information remain very unclear. For instance, what’s the action space for the robots? How is that parametrized? How does the VLM choose them (I see that the supervisor does so, but I am not sure what it specifically outputs)? The authors mention specific agents on each team (for example, “when a verification agent (or box checker) evaluates the outputs from the supervisor (or box mover)”), but I can’t seem to find a comprehensive list? 
- The evaluated tasks seem extremely contrived. 
  - For example, the superhero snack one does not require much semantic reasoning, just some fuzzy kind of color matching. I'm not really sure why the superheroes are needed (why not just have 3 bins with one snack in them each and say to match the colors?).
  - Likewise, the fruit price task seems to largely test GPT-4o’s ability to look at an image and perform some rudimentary math. This seems tailored to systems that can perform such reasoning. While such tasks are difficult for present robot control stacks, it does not show much about the ability for the system to perform complex or generalizable physical motions.
- There are numerous small mistakes in formatting and presentation: App E.1 has a part missing a reference (“Figure ?? shows this fact”), grounding team description says “The agent can not corre ctly identify”, etc. Significant polishing is needed.
- Missing comparisons with (or at least citations of) robot foundation models trained on robot data, especially VLAs that actually make use of vision-language models (see [RT-2](https://robotics-transformer2.github.io/), [OpenVLA](https://openvla.github.io/), [Embodied Chain-of-Thought](https://embodied-cot.github.io/), etc).
- Likewise missing comparison with or discussion of [MOKA](https://arxiv.org/abs/2403.03174), which is similar to PIVOT, but goes a long way towards showing how zero-shot VLMs can be used to smoothly control robots.

I think a view expressed in lots of past papers on integrating (V)LMs with robotics is that, while VLMs do enable complex semantic reasoning that’s useful for robotics, it’s unclear how to best interface that with robot motions: learned robot controllers (such as RT-2, OpenVLA, etc) or even classical optimization-based controllers (formulating walking, running, grasping, flying as mathematical programs, etc) tend to be much smoother than, e.g., a (V)LM equipped with a suite of code tools for controlling the robot (as with Code as Policies) – in the latter case, your policy is only as good as the code API motion primitives it enjoys. 

How to best enjoy the benefits of graceful “reactive” motion while maintaining the “system 2” benefits of VLMs is an open problem, and as it stands, it is unclear if this paper goes any way towards bridging that gap. Not only is it missing (or, at the very least, not very clear in conveying) crucial information for determining its impact like the action space.

### Questions
Please see weaknesses.

### Soundness
2

### Presentation
1

### Contribution
1
