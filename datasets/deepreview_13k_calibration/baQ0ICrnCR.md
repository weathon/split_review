# Robotic Programmer: Video Instructed Policy Code Generation for Robotic Manipulation

- Decision: Reject
- Avg Score: 4.25
- Scores: 6, 5, 3, 3

## Abstract
Zero-shot generalization across various robots, tasks and environments remains a significant challenge in robotic manipulation. Policy code generation methods use executable code to connect high-level task descriptions and low-level action sequences, leveraging the generalization capabilities of large language models and atomic skill libraries. In this work, we propose Robotic Programmer (RoboPro), a robotic foundation model, enabling the capability of perceiving visual information and following free-form instructions to perform robotic manipulation with policy code in a zero-shot manner. To address low efficiency and high cost in collecting runtime code data for robotic tasks, we devise Video2Code to synthesize executable code from extensive videos in-the-wild with off-the-shelf vision-language model and code-domain large language model. Extensive experiments show that RoboPro achieves the state-of-the-art zero-shot performance on robotic manipulation in both simulators and real-world environments. Specifically, the zero-shot success rate of RoboPro on RLBench surpasses the state-of-the-art model GPT-4o by 11.6\%, which is even comparable to a strong supervised training baseline. Furthermore, RoboPro is robust to different robotic configurations, and demonstrates broad visual understanding in general VQA tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a method, RoboPro, that utilizes action-free video for zero-shot policy code generation in robotic manipulation tasks. The method consists of two components: a video-to-code model that generates robotic runtime code, and a code-generation policy trained on the synthesized code. In experiments, RoboPro was shown to be effective in performing tasks in unseen environments in a zero-shot manner.

### Strengths
1. The idea and motivation of using action-free data videos to synthesize robotic runtime code, which was then used to train a code policy is novel and interesting.

2. The experimental results demonstrate that RoboPro can perform the task in a zero-shot manner, which is compelling.

### Weaknesses
1. [Major] While the paper compares its approach to BC-based and code-generation methods, I’m curious how it performs compared to recent methods that use VLM prompting without model training, like MOKA [1], which leverages VLM reasoning and motion primitives, and PIVOT [2], which uses iterative visual prompting. These methods generally make fewer computational assumptions than RoboPro since they don’t require any module training.


2. [Major] In the real-world experiments, there is no comparison to other baselines. Would it be possible to include a comparison against at least GPT-4o to see if RoboPro performs better?


3. [Major] While the idea of using action-free video to synthesize runtime code data is interesting, the impact of the chosen video datasets remains unclear. In this paper, the authors use DROID as their dataset—was there any specific reason for this choice? How do the type and size of the dataset affect the final performance? If I’m understanding correctly, in principle, the video data doesn’t even need to be robotic. How would the approach perform if human videos, such as Ego4D or Something-Something, were used instead? It would be interesting to include the ablation over these points.


4. [Minor] The downstream performance appears to be sensitive to the choice of VLMs used for draft/code generation, as shown in Table 6. Specifically, there is a large difference in results between using Gemini and DeepSeek for code generation. This sensitivity to the VLM choice may be a weakness of this approach.

### Questions
1. How accurate is the generated code from the data curation pipeline? Are there any errors or failure cases and how are they handled?


2. Could the authors provide more details on the training procedure? – e.g. hyperparameters, training steps, and the computational resources and time required for training, etc


3. During the deployment phase, is it correct that only the initial image of the environment is used to generate the entire execution code, without using the newest images at each time step?

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
4

### Summary
This paper presents RoboPro (Robotic Programmer), a robotic foundation model that generates executable policy code from visual information and language instructions to perform robot manipulation tasks without additional fine-tuning. The authors propose Video2Code, an automatic data curation pipeline that synthesizes code execution data from large-scale instructional videos. Extensive experiments are conducted in both simulators and real-world environments to validate the model's effectiveness. In short, the reviewer thinks this paper has good presentation, thorough evaluations, but lacks novelty and insights.

### Strengths
1. The Video2Code pipeline bridges the gap between visual understanding and code generation by combining the visual reasoning ability of VLMs and the coding proficiency of code-domain LLMs. This low-cost and automatic method reduces reliance on manually constructed datasets and expensive simulation environments.

2. RoboPro shows adaptability to different API configurations and compatibility across environments (simulators like RLBench and LIBERO, as well as real-world settings), underscoring its robustness and usability in diverse practical scenarios.

3. Extensive experiments in simulations and real-world scenarios verify the model's code generation abilities, with analysis on how different code LLMs affect performance.

### Weaknesses
1.The auto code data collection is intuitive and simple, which does not count as "novel" for the VLM agent training. The auto code collection pipeline is natural by itself and has been adopted in many applications like multi-modal OS agents and game agents. However, since you have real-time feedback from the real worlds, if would be of more interesting how you could accelerate this data collection and enhance the code quality from the multi-modal reflection on the world feedback.  

2.The use of a foundation model for code generation lacks methodological innovation, as has been cited by the authors, there are already published papers that can fall into this category. The authors should try to highlight the difference of this work among other reference methods.  

3.The model's zero-shot capability is restricted by the predefined API library it can call.

### Questions
1. Since the authors have conducted comprehensive experiments, maybe they can share more insight about the limitations of code generation approaches compared to VLAs? By comparing the difference between these two approaches, it would be more interesting for the authors to share some insights about what can be done or what cannot be done by their approach and where direction we could go for the future work. 

2. Include a more detailed analysis of failure cases, distinguishing between issues related to LLM reasoning and API limitations. This could provide more insight for this paper. It's unclear whether failures are due to issues with LLM Chain-of-Thought reasoning or problems with the API itself, etc.

### Soundness
3

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
The paper presents RoboPro which enables zero-shot performance on robot manipulation tasks by converting observations and language instructions into executable policy code. RoboPro's code generation is enhanced by Video2Code, a data curation pipeline that outputs executable code from input videos.

### Strengths
1.  Experiments are comprehensive, with both simulation and real-world tasks, as well as general VQA tasks.

### Weaknesses
1. Performance on more complex long-horizon tasks is not thoroughly explored.

2. RoboPro depends on consistent API libraries. It's unclear how this method scales with open-ended real-world tasks of arbitrary complexity.

### Questions
1. Can the authors provide additional contextualization in lines 122-136 with prior works such as [1]?

2. I'm also not sure how scalable this method actually is. Certainly the generalizability of LLMs is well-leveraged, but the interface between various components seems like a bottleneck. Can the authors explain how the code API returned by Video2Code can be adapted if new functions are required to describe tasks in new video demonstrations? It seems like changing the code API requires re-running the Video2Code pipeline on the entire video dataset?

[1] [Programmatically Grounded, Compositionally Generalizable Robotic Manipulation](https://arxiv.org/abs/2304.13826)

### Soundness
2

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
4

### Summary
This work proposes RoboPro, a high-level planner that generates sequences of low-level API calls based on language instructions and observations. It leverages a two-stage approach, using a Vision-Language Model (VLM) and a code Language Model (code LLM) to process videos and generate runtime code data, which is then used for fine-tuning RoboPro. Experiments cover nine tasks from RLBench, eight tasks from LIBERO, and several real robot tasks, demonstrating RoboPro's zero-shot planning generalization when low-level skills and APIs change.

### Strengths
This work processes videos to generate robot planning data using a two-stage approach.
The experiments demonstrate the model's planning generalization ability across two benchmarks.

### Weaknesses
1. The contributions of this work are not clearly summarized.
2. The writing could be improved, as there are many redundant sentences that convey the same ideas. The structure and presentation are somewhat difficult to follow.
3. The implementation of low-level skills is not well-explained for both simulation and real work experiments. The assumption of predefined API calls and low-level skills is too strong for developing effective manipulation policies.
4. The experiments are primarily limited to low-precision, open-loop pick-and-place tasks.

### Questions
Since RoboPro is pre-trained on related robot runtime code data, were the baseline planners also fine-tuned on this data?

Peract is a multi-task policy learned from demonstrations, directly outputting the keyframe action without a high-level planner. How is it an apples-to-apples comparison with RoboPro which uses a high-level planner equipped with low-level skills?

RoboPro is referred to as a generalist. However, popular generalist baselines like RT-2[1] and Open-VLA[2] are missing from the comparisons.

Can RoboPro complete tasks when a target is moving during planning? Is there some way to address it?

Could you briefly explain how RoboPro might be extended to solve deformable object manipulation tasks, such as folding cloth?

What is the main difference between RoboPro and RoboCodeX, aside from the pre-training on robot runtime data?

[1] RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control
[2] Open-VLA: An Open-Source Vision-Language-Action Model

### Soundness
2

### Presentation
1

### Contribution
2
