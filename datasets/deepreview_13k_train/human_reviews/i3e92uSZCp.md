# Language Guided Skill Discovery

- Decision: Accept
- Scores: 6, 6, 8, 8

## Abstract
Skill discovery methods enable agents to learn diverse emergent behaviors without explicit rewards. To make learned skills useful for unknown downstream tasks, obtaining a semantically diverse repertoire of skills is essential.
While some approaches introduce a discriminator to distinguish skills and others aim to increase state coverage, no existing work directly addresses the ``semantic diversity'' of skills. We hypothesize that leveraging the semantic knowledge of large language models (LLMs) can lead us to improve semantic diversity of resulting behaviors. 
In this sense, we introduce \methodname\ (\methodabbr), a skill discovery framework that aims to directly maximize the semantic diversity between skills. \methodabbr\ takes user prompts as input and outputs a set of semantically distinctive skills. The prompts serve as a means to constrain the search space into a semantically desired subspace, and the generated LLM outputs guide the agent to visit semantically diverse states within the subspace. 
We demonstrate that \methodabbr\ enables legged robots to visit different user-intended areas on a plane by simply changing the prompt. Furthermore, we show that language guidance aids in discovering more diverse skills compared to five existing skill discovery methods in robot-arm manipulation environments. Lastly, \methodabbr\ provides a simple way of utilizing learned skills via natural language.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposed to incorporate semantic diversity in skill discovery.  The authors show that the proposed approach with language guidance from LLMs outperforms existing skill discovery baselines. The proposed approach is demonstrated in both locomotion and manipulation tasks.

### Strengths
- A theoretical proof of language-distance as a valid pseudometric is provided.
- Both locomotion and manipulation tasks have been demonstrated, showing the effectiveness of the proposed approach.
- The paper is well presented.

### Weaknesses
 - More complex scenarios should be designed to make the use of LLMs necessary rather than simple positions.
- The lack of real-world experiments makes the proposed approach less convincing.
- A video showing the robot in action should be included to give readers an intuitive understanding of learning performance.

### Questions
- In Fig. 4, the coverage for the manipulation task is worse than the locomotion task. More analysis or explanations would be necessary to understand the limitations of the proposed approach.
- In Fig. 7, showing the coverage for LGSD in the whole space would be better. Although the proposed approach may have a larger coverage than the baselines, it is less evenly distributed compared to CSD. Is this always the case for different training runs? Any analysis or explanations would be helpful.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Rather than to maximize state coverage, this work introduces LGSD to constrain skill discovery inside a semantically meaningful subspace, created by LLMs with crafted user prompts.

### Strengths
- The method tried to link skill states with their semantic meaning, resulting in meaningful and language-controllable skills.
- LGSD provides a theoretical foundation for the language-distance metric as a pseudometric, detailing how it can approximate semantic diversity.

### Weaknesses
 - The experimental scenarios are simple, in which the exampled prompts and semantically controlled spaces are easy to follow yet fail to demonstrate the generalizablity and scalability --- after all, the method relies much on the description of states. LGSD’s dependence on LLMs for real-time distance evaluation might limit scalability to complex, real-time environments.
- As I understand, users have to provide specified "skill constraints"  (via prompts, such as "move north" etc.), then how can it still be called "skill discovery" since users are specifying skills?
- The comparison with some baselines is somehow unfair since they lack the prior knowledge of users or any language embedding computation. A better comparison should be considered.

### Questions
- Is it correct that for each state $s_t$, the LLM will be called to generate a description in order to compute $d(s_{t-1}, s_t)$? If so, how fast is the training?
- How will LGSD generalize to complex scenarios? Is it necessary for experts to compose (skill)prompts for each possible skill?

### Soundness
3

### Presentation
3

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
“Language Guided Skill Discovery” proposes a method for learning diverse skills with unsupervised reinforcement learning by aligning skills with latent space transitions under a distance constraint. The novelty in the proposed method stems from the use of language distance as the constraint. This is done by a Large Language Model (LLM) which describes the robot state, and a language embedding model which encodes this description in a fixed real-valued vector where the distance between descriptions can be measured. The results show successful skill discovery on locomotion and robot manipulation environments.

### Strengths
- Interesting and novel contribution - while using LLMs is not rare, this is an interesting way of using them for encouraging skill discovery.

- The proposed method is well-supported mathematically.

- Good zero-shot language-specified goal tracking with the learned skill predictor network.

### Weaknesses
 - Not fully convinced that LLMs are necessary for the proposed scenarios. Showing the performance on more complex situations where the semantic understanding of LLMs is necessary would make the case much stronger.

- More qualitative evaluation (i.e. videos) would be good for evaluating the learned skills.

- The performance of other skill discovery methods seems quite poor on downstream Ant tasks, which is surprising especially for LSD/CSD/METRA. Are the tasks or rewards defined here differently from their original papers?

- I am curious if specifying just the object’s Cartesian position as the sole encoder observation under a Euclidean distance constraint (LSD) would yield similar results. I guess it might struggle more with exploration (no signal before the end-effector has collided with the object), but it would be interesting to see.

- I like the visualizations (and analysis) in Appendix D. As I understand, the language distance d_lang stays quite small when the object is at the origin, but increases when the object is pushed. Is there a specific reason why changes in the LLM output for the former (“The object’s x, y position is A,B”) results in smaller language distance than the latter (“The distance is X units.”)? On this note, it would be interesting to see how the language distance changes as a function of the robot state - is it more or less linear? 
Since the LLM output is constrained to the “’Description: The cube’s x, y position is ___ .’” and “’Description: the distance is ___ units.’”, I can see how the language distance could serve as a metric between the two behaviors, but would it really correspond to something much different than Euclidean distance on description-level? For example, “The distance is 4 units” vs “The distance is 6 units”.

### Questions
## Questions:
1. What is the dimensionality of the skill-space here? Is there any benefit to having higher dimensions / are more skills learned?

2. The performance of other skill discovery methods seems quite poor on downstream Ant tasks, which is surprising especially for LSD/CSD/METRA. Are the tasks or rewards defined here differently from their original papers?

3. Is the LLM necessary given those prompts? Could these examples not be done just as well with simple logic gates? For example, prompt G.3 could be defined as “if object not at origin, return position of object, else return distance between end effector and object” without any LLM. 
I understand that this is more or less a proof of concept, but I think it would go a long way if you can show some examples where the “common knowledge” of LLMs can be properly utilized. 


4. I am curious if specifying just the object’s Cartesian position as the sole encoder observation under a Euclidean distance constraint (LSD) would yield similar results. I guess it might struggle more with exploration (no signal before the end-effector has collided with the object), but it would be interesting to see.


5. I like the visualizations (and analysis) in Appendix D. As I understand, the language distance d_lang stays quite small when the object is at the origin, but increases when the object is pushed. Is there a specific reason why changes in the LLM output for the former (“The object’s x, y position is A,B”) results in smaller language distance than the latter (“The distance is X units.”)? On this note, it would be interesting to see how the language distance changes as a function of the robot state - is it more or less linear? 
Since the LLM output is constrained to the “’Description: The cube’s x, y position is ___ .’” and “’Description: the distance is ___ units.’”, I can see how the language distance could serve as a metric between the two behaviors, but would it really correspond to something much different than Euclidean distance on description-level? For example, “The distance is 4 units” vs “The distance is 6 units”.

## Summary:
Overall I think it’s a very well-written paper, with a good mathematical basis and satisfactory results. The results are promising, and I think there are good direction for building upon the methods, for example with VLMs. In my opinion, the proposed method has a lot of potential which is not fully utilized. My main concern is that the examples shown in the paper can be easily represented in a simpler way without an LLM. I can see that there are situations where this might not be the case, and showing these will make a much stronger argument for the proposed approach.

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents a novel skill discovery framework called Language Guided SKill Discovery (LGSD). LGSD aims to maximize the semantic diversity of discovered skills by utilizing language guidance from LLMs. In LGSD, the interactions between human experts and LLMs are utilized for 1) constraining the skill search space into a semantically desired subspace, and 2) encouraging the agent to visit semantically diverse states within the subspace. Various experiments are conducted to demonstrate the capability of the LGSD framework to find more diverse and distinctive skills compared to previous methods.

### Strengths
- This paper is pretty clear wrt the high-level topic and what the high-level intuitions are. The idea of incorporating LLMs to guide the skill discovery is novel and intuitive. Figure 2 is a very clear figure except one minor issue (see weakness).
- By introducing the representation function \phi which transform the state space s to latent space z, the skill discovery problem in the Euclidean space is transformed to an equivalent problem in the latent space. Figures in Appendix D show that identifying skills in the latent space is much easier than in the original space. Furthermore, by formulating the reward as $r(s, z, s^\prime) = ( \phi(s) - \phi(s^\prime))^Tz$, LGSD successfully transform the problem of finding diverse skills to a problem of maximizing the culmulative designed reward.
- The section 2.1 is a great section that summarizes works related to unsupervised skill discovery.  Researchers might already read some related articles, but such a classification (definition)  as "mutual information based " and "distance maximization" approaches is still helpful to the whole community yet very accurate.
- Experiments results show LGSD is effective and competitive in discovering semantically distict skills compared to other skill discovery baselines.

### Weaknesses
 - Figure 1 shows a set of discovered semantically distinctive skills but the caption is not very informative. It could be better if description of each skill can be presented.
- Figure 2 is very good. However, it is unlikely for reader to understand $d_{lang}(s, s^\prime)$ without any additionally context. People may mistakenly treat this as some Euclidean distance between s and s^prime in the original space until they encounter equation (2). I would like to see some quick explanation that the $d_{lang}$ here happens in latent space, and this procedure requires LLMs.
- Prompts are required in this work to interact with LLMs to acquire the semantic knowledge. The design of the prompt is critical to the direction or subspace of skill discovery. However, what if we only want to leverage the semantic knowledge from LLMs without setting up to much language prior? From my understanding, too much control from human means less diverse and improvising skills.
- This is minor. In Line 319, it is unclear what is $s$ and $g$ without defining them.

### Questions
- Why enforcing $\phi$ to be 1-Lipschitz continuous under $d_{lang}$? Is there any other way to constrain the difference in the latent space?
- In Section 5.1. In FrankCube environment, the intended half plane is only for NSEW directions. Can we see arbitrary directions, e.g., north-east or south-west?

### Soundness
3

### Presentation
3

### Contribution
3
