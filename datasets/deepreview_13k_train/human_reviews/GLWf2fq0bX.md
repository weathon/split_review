# Skill Expansion and Composition in Parameter Space

- Decision: Accept
- Scores: 6, 6, 8, 6

## Abstract
Humans excel at reusing prior knowledge to address new challenges and developing skills while solving problems. This paradigm becomes increasingly popular in the development of autonomous agents, as it develops systems that can self-evolve in response to new challenges like human beings. However, previous methods suffer from limited training efficiency when expanding new skills and fail to fully leverage prior knowledge to facilitate new task learning. We propose Parametric Skill Expansion and Composition (PSEC), a new framework designed to iteratively evolve the agents' capabilities and efficiently address new challenges by maintaining a manageable skill library. This library can progressively integrate skill primitives as plug-and-play Low-Rank Adaptation (LoRA) modules in parameter-efficient finetuning, facilitating efficient and flexible skill expansion. This structure also enables the direct skill compositions in parameter space by merging LoRA modules that encode different skills, leveraging shared information across skills to effectively program new skills. Based on this, we propose a context-aware modular to dynamically activate different skills to collaboratively handle new tasks. Empowering diverse applications including multi-objective composition, dynamics shift, and continual policy shift, the results on D4RL, DSRL benchmarks, and the DeepMind Control Suite show that PSEC exhibits superior capacity to leverage prior knowledge to efficiently tackle new challenges, as well as expand its skill libraries to evolve the capabilities.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces the Parametric Skill Expansion and Composition (PSEC) framework, which allows RL agents to learn and combine new skills by efficiently using a "skill library". Instead of relearning tasks from scratch, PSEC uses LoRA modules—compact, adaptable components—that can be added to this library as plug-and-play skills. This design enables agents to adapt to new tasks by combining skills directly within the model's parameters, allowing them to leverage shared knowledge from previous tasks while avoiding "catastrophic forgetting", since each "skill" is stored as an independent "frozen" module. 

Authors test across different environments, including multi-objective tasks (where skills must be blended to meet multiple goals), settings with continual learning demands, and dynamic scenarios where the environment changes. Results show that PSEC enables efficient, flexible learning compared to vanilla RL.

### Strengths
The paper is easy to follow and clearly written. The experiment suite is diverse and proves the ability of SPEC to learn and compose skills.

Regarding originality and significance I particularly found interesting the usage if diffusion models to adjust the weight levels of the compositions of skills and the study for skill composiiton on the differenc spaces (parameter, noise and action spaces). It made very clear the thought process of the authors to design the framework.

### Weaknesses
My biggest concern with this paper is that this is not the first paper proposeing using LoRa for multiple task leanring, e.g. [1,2] and while SPEC is clearly different from previous existing approaches, some level of  comparison, theorethical or empirical would be greatly benefitial. Specifially, at present is difficult to discern what are the novel components within SPEC wrt previous skill learning frameworks.

It would be also good if authors could provide their though contrasting SPEC with existing works on RL agents that learn skills compositionally such as [3-6]. Particularly, [5] even points as an advantage over previous frameworks not having to learn and storing a different set of weight for every skill/sub-task. Since SPEC goes back to this form of learning it would be good that authors include a discussion on this topic.

### Questions
Please refer to the questions above.

--- Post discussion ---
Authors correctly addressed my concerns during the rebuttal incorporating relevant discussion on related works and limitations, while I would aprreciate some of this to be present not only in the appendix, I believe the strenghts of the work outweight the weaknesses in the revised version

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This is a paper presents a new skill composition method, which 
composes skills in the parameter space. Concretely, the paper 
introduces PSEC, which fine-tunes new skills using low-rank adaptation 
(LoRA) and argues the actions synthesized through this parameter-space 
composition greatly improves the performance, compared to two other 
composition methods termed noise-level composition and action-level 
composition.

### Strengths
o This paper presents an interesting idea of how to compose skills in 
the parameter space, and provide a clear categorization of skill 
composition: parameter-level, noise-level, and action level. This 
paper shows a way where neural network-based skills can be composed at 
the parameter space level, instead of composing at the action output 
level. 
 
o In the long run, the proposed method can open up the possibility for 
efficient skill learning based on large models in decision-making 
domains

### Weaknesses
o While the general motivation in the first paragraph makes sense, the 
example needs to be justified a bit better From online statistics, the 
time difference between child learning to walk and learning to stand 
without support is on average 2-2.5 months. Not everyone would call 
this "rapid" (Ln 32) 
 
o While the idea of parameter-level composition is interesting and 
also introduces fewer bottlenecks compared to methods like action 
level, the argument of parameter-level composition being superior is 
not well-grounded. The explanation from line 256 to line 304 lacks 
convincing evidence. Specifically, the authors do not provide a clear theoretical justification for why parameter-space composition should inherently lead to better skill sharing or performance compared to action-level or noise-level composition. The current explanation relies on an intuitive argument about shared knowledge, but this lacks rigorous support.
 
o The t-SNE plot (Figure 4) does not directly reveal that the 
parameter space "shares knowledge" - if 4(a) can be explained to have 
shared knowledge, why is 4(b) not a plot that shows "shared 
knowledge"? The authors might try to design a more specific 
visualization that clearly illustrates the idea of "shared 
knowledge." The current visualization is insufficient to support the claim of knowledge sharing, as it only shows clustering of parameters, not the actual transfer of learned behaviors or skills.
 
o In the experiment sections, there are a lot of terms that authors 
either didn't specify clearly or misuse the words. 
 
    o It is unclear what "versatility" means. Authors should provide a 
    clear definition of this term(Line 354&473) 
 
    o Line 397, the authors shouldn't use the word "generated" to 
    describe other comparison methods, especially when the results 
    haven't been revealed. 
 
    o Line 374 "popular safe offline RL benchmark" is not 
    informative. The authors should replace this with  an explanation 
    of what problems does it contain (robot manipulation? autonomous 
    driving? a collecition of them?) and why is it a good benchmark to 
    test on (large-scale? diverse? or any other key features that make 
    them special) 
 
    o What does "safety" refer to? It's not explained well. The only 
    thing I can take a guess is the cost that shows in the table, 
    which does not really provide much information on how to interpret 
    those numbers. The authors need to clearly define what constitutes a 'safe' policy within the context of their experiments, and how the cost metric relates to this definition. Without this, the results are difficult to interpret.

o The paper touches on multi-task learning and continual learning, and 
uses a skill library. 
All of these topics have been studied to some degree for decades.  Yet 
the majority of citations are from 2023 and 2024, with only two 
citations to work prior to 2016 - and those are just to energy-based 
models and t-SNE.   
Without putting the work in the proper context of prior work, its 
novelty and significance can't be properly assessed. The lack of citations to foundational works in modular and hierarchical reinforcement learning makes it difficult to understand the true contribution of this paper.
 
o Minor: There are many small grammatical errors throughout the paper 
- including in the first sentence of the abstract!

### Questions
o See the concerns and questions from Weaknesses 
 
o If I understand correctly from the paragraph "Context-aware 
Composition" (Line 244-254), only $W_{k}$ is updated at skill k. If 
that's the case, What would be the impact of existing pre-trained LoRA 
weights? Is it possible that because there are two skills that are 
contradictory to each other, the LoRA fine-tuning on a new skill might 
be harder to train? It will be good to see such experiments, and see 
if the method still applies; or an additional experiment can conducted 
where the learning curriculum is shuffled. Will the result be 
consistent with the existing ones where learning happens from standing 
to walking, running? 
 
o Can this method scale to dozens of skills instead of three skills 
presented in this paper? An experiment on stress testing the number of 
skills it can handle will be able to support the effectiveness of the 
proposed method.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces a novel framework called Parametric Skill Expansion and Composition (PSEC). PSEC employs Low-Rank Adaptation (LoRA) to learn and store new skills, and directly synthesizes skills in the parameter space. It incorporates a context-aware module to adaptively compose skills in dynamic environments and utilizes diffusion models for policy modeling. The framework has been evaluated across various scenarios, including multi-objective composition, policy shifts, and dynamics changes.

### Strengths
The key features of PSEC include efficient skill learning and storage utilizing LoRA, direct skill synthesis in parameter space, adaptability through a context-aware module, and the ability for continuous skill expansion. Its effectiveness has been validated through various experiments, demonstrating versatility across different scenarios.

### Weaknesses
 * While the strong assumption about the expressiveness of the pre-trained policy and the scalability issue of the skill library appear to be weaknesses, these seem to have been addressed in the paper's appendix.
* A potential limitation of the authors' proposed framework is its applicability only to environments where data is available. This could be considered a weakness of the paper. It is conceivable that if the framework could be extended to unseen tasks through transfer learning or fast adaptation techniques, it would demonstrate greater differentiation from previous research.
* Minor:
    * Generally, skill learning, as in  [1] and [2], refers to 'temporal abstraction', but the skill defined by the authors seems to differ from this. This may lead to confusion with existing skill learning concepts.

### Questions
* One of the main strengths claimed for PSEC is that it "reduced computational costs and memory usage". How does this compare to the baselines?

### Soundness
4

### Presentation
4

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
This paper proposes Parametric Skill Expansion and Composition framework, which encodes skill primitives offline using LoRA modules and learning skill compositions with the generated LoRA library. The PSPEC framework is designed to cope with multi-objective composition as well as adapting to shift in policy and dynamics. The authors provides extensive experimentation on their proposed algorithm on the D4RL, DSRL, and DeepMind Control Suite.

### Strengths
- PSEC has a very intuitive and stright-forward design that utilizes LoRA structure. While PSEC wouldn't be the only structure to use the LoRA as building blocks for skills composition, the authors provides tSNE analysis to show why their method encodes skills better than the alternatives
- The paper is very pleasant to read and the paper structure too, is very straightforward. The authors also covers the related works very well which makes PSEC's design choices to be convincing.
- The experimentations are very extensive.
- I found the graphics very easy to understand and they summarize the key points very well. From intro to methods, I could very easily follow the keypoints by reading the details and captions in the graphics beforehand.

### Weaknesses
 - LoRA is one of the key elements of the PSEC's structure, and while LoRA is mentioned in the abstract, the authors do not explain what LoRA is until page 2. I think it would be better to say in the abstract what LoRA stands for or simply refer to the module as a skills module if not explaining what LoRA is.
- While the experiments are extensive, I think some of the assumptions and motivations were not well explained. I have included the details in the questions section.
- I think one of the possible limitations of composing skills as a weighted some of LoRA actions is that some skills are not simply some of sub-skills. For example, the skill of throwing a ball is more of a fluid movements where the a person builds up the momentum and transfer the kinetic energy to the ball, instead of some combinations of walking forward and rotating torso. I am curious how the PSEC would perform with more complex tasks.

### Questions
- I think the paper lacks general motivations and overview on the benchmarks used. Why does this paper uses an offline safe RL benchmark instead of just an offline RL benchmarks in general? What are the tasks and what do the recorded data look in the offline benchmarks? Why would they provide a characteristic examples to highlight the pros and cons of PSEC?

### Soundness
3

### Presentation
4

### Contribution
3
