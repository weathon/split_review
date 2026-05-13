# MaestroMotif: Skill Design from Artificial Intelligence Feedback

- Decision: Accept
- Scores: 5, 8, 10, 8

## Abstract
Describing skills in natural language has the potential to provide an accessible way to inject human knowledge about decision-making into an AI system. We present MaestroMotif, a method for AI-assisted skill design, which yields high-performing and adaptable agents. MaestroMotif leverages the capabilities of Large Language Models (LLMs) to effectively create and reuse skills. It first uses an LLM's feedback to automatically design rewards corresponding to each skill, starting from their natural language description. Then, it employs an LLM's code generation abilities, together with reinforcement learning, for training the skills and combining them to implement complex behaviors specified in language. We evaluate MaestroMotif using a suite of complex tasks in the NetHack Learning Environment (NLE), demonstrating that it surpasses existing approaches in both performance and usability.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper introduces a method called MaestroMotif for designing and using AI-assisted skills that enhance agent performance and adaptability, particularly for complex tasks in environments like NetHack. MaestroMotif leverages Large Language Models (LLMs) to translate natural language skill descriptions into reward functions, which are then used to generate code for skill initiation and termination and to create a policy over these skills. This allows the AI to perform specified behaviors through a combination of reinforcement learning (RL) and LLM-based code generation. 
The paper evaluates MaestroMotif on the NetHack Learning Environment (NLE) and demonstrates its effectiveness in handling complex navigation, interaction, and composite tasks. MaestroMotif’s zero-shot approach, using skills without additional training, outperformed both LLM-only and reward-based RL baselines, highlighting the value of hierarchical skill composition and the LLM’s role in skill design.

### Strengths
Overall, I believe MaestroMotif presents an effective approach to incorporating human prior knowledge to solve specific tasks. Given that NetHack tasks involve a variety of challenges, including understanding natural language descriptions, planning over high-level abstractions, and exploration, it is notable that the authors demonstrated improved performance in the NetHack environment using their method.
Additionally, I find it interesting that the authors showed that learning skills simultaneously is essential for acquiring skills more efficiently, thanks to the emergence of curriculum-based learning.

### Weaknesses
- **Source of Performance Gains**

  I wonder whether the performance gain primarily comes from the human domain knowledge or the method itself. It appears that the method relies heavily on human effort and domain knowledge to solve individual tasks. For instance, humans select a set of skills such as *Discoverer, Descender, Ascender, Merchant,* and *Worshipper,* and they even required to modify prompts for acquiring each of these skills. Therefore, when comparing this work with baselines, it’s difficult to determine whether the performance gain is due to the method itself or the expertise of human contributors. While the core of this work aims to incorporate human priors, the baseline algorithms should ideally leverage human priors at a comparable level. It's unclear if the baselines are given the same level of task decomposition as the proposed method, which could be a significant confounding factor.

- **Concerns about Generalizability**

  I'm not entirely convinced that the proposed five skills are general enough to tackle any downstream task in the NetHack environment, or if they are instead a highly targeted set of skills specifically suited for the benchmark tasks. The skills seem very specific to the NetHack environment, such as 'Descender' and 'Ascender,' which might not translate well to other environments. To better demonstrate the method’s generalizability, one approach could be to train reusable skills across a broader range of environments, such as robotics tasks. For instance, training foundational skills on a robotic platform, like a humanoid or robotic arm, and performing zero-shot evaluations on new tasks that require combinations of these learned skills could provide stronger evidence of generalizability. The current evaluation is limited to a single, albeit complex, environment.

- **Need for Pseudocode**
        
  It is challenging to understand the entire concept concretely without pseudocode for the full process, and some aspects remain unclear. For example:
        
    - If certain agent states satisfy instantiation conditions for more than one skill, how does the LLM prioritize among different skills? The paper does not specify the mechanism for resolving conflicts when multiple skills are applicable.
    - What happens if none of the skills satisfy the instantiation conditions? It's unclear how the agent behaves when no skill is deemed appropriate for the current state.
    - Does the training-time policy over skills adapt/evolve during training? I wonder because, as each individual skill is being changed along the training process, it might be helpful for a policy-over-skills adapts to the current set of learned skills. The paper does not discuss any adaptive mechanism for the policy over skills.

  I understand that the specific prompts in the Appendix may partially address these questions; however, I believe it would be beneficial to clearly state them in the main sections.

- **Relationship to Related Work**
     - It would be helpful if the relationship between this work and Motif (Kilssarov, 2024) were more explicitly stated. The paper mentions Motif, but the precise way in which it is integrated into the proposed method is not fully clear.

- **Minor Corrections**
     - *Line 196:* "crafts aploicy" → "crafts a policy"
     - *Line 239:* *Llama 3.1 70b* → *Llama 3.1 70B*
     - *Figure 8(c):* It is difficult to compare the performance of the two different approaches, as they are visualized in separate plots.
     - *Appendix A.2 and A.3* : title of these subsections are same
     - *Line 269:* What negative impact? Additional clarifications would be helpful for better understanding

### Questions
Could you please eloborate more about the concerns that I made on the Weakness sections? Especially, follwoing three.

- Source of Performance Gains
- Concerns about Generalizability
- Need for Pseudocode

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces MaestroMotif, an extension of the recent Motif framework that accepts datasets of unlabeled demonstrations to first learn a set of labeled options, then query an LLM to write Python programs that trigger these learned options to satisfy an arbitrary objective in the given domain. MaestroMotif is compared to Motif, ordinary PPO, and expert behavior-cloning to see how well each method can satisfy arbitrary unseen objectives, and the results indicate that MaestroMotif is better than these baselines at solving long-horizon, complex requests (e.g., "go to area X, obtain item Y, wait until condition Z is met and then take action A").

The authors also present an ablation of MaestroMotif for different approaches to learning options/skills for the framework, showing the importance of learning their skills jointly and without separate policy heads. The authors also look at the scaling performance of MaestroMotif, showing that smaller LLMs produce predictably smaller returns on the complex tasks.

I thank the authors for their thorough rebuttal and for their comments on the work. After reviewing the rebuttal, I have updated my score to 8 and advocate for acceptance of the work.

### Strengths
* MaestroMotif fits in well with the presented prior work and literature, and is a logical extension of much of the "code-as-policies" literature from LLMs, combining human demonstrations and data with AI planning and code-synthesis.
* The baselines used (LLM as policy, PPO, etc.) are sensible baselines and suitable cover the different methods that one might employ to attempt to learn arbitrary NetHack policies for zero-shot transfer to new skills or tasks.
* The paper presents an approach that combines large labeled datasets, human expertise, and LLM code synthesis/planning into one framework, neatly exemplifying human-AI collaboration for task completion with LLMs.
* The full details for reproducibility are in the appendix (importance of unit tests, specific prompts, re-prompting strategies, etc.), which is a useful resource for future work.

### Weaknesses
 * Learning the options networks seems to require intense manual effort, as a human must label different states with preferences/task-alignment to learn different options.
* While MaestroMotif outperforms the baselines for arbitrary tasks, it does seem to be pitted against methods that have no real way of generalizing to such tasks (for example, are the score-maximization approaches capable of receiving sub-goals or goals in any way?). The success of MaestroMotif is noteworthy, but the delta over prior work is less impressive given the prior work is, at times, apparently severely hamstrung.
* The overall framework relies on significant prompting/re-prompting of a 405b model, which could quickly become prohibitively expensive. It would be nice to see results or metrics on the cost (in time, memory, or money) of running MaestroMotif for each of the specified tasks, or for generalization to a new task or domain.
* Much of this paper is tailored to NetHack, so the line between "core requirement/contribution of MaestroMotif" and "tweak made to adapt to NetHack" is blurry.

### Questions
* Are the baselines in any way capable of accepting goals, or is their failure to generalize to new tasks fairly expected behavior?
* What is the cost of running MaestroMotif for a single task (i.e., how much time and memory is required, or what type of hardware is needed?)
* How would MaestroMotif be applied to a new domain? My interpretation is: 1) identify necessary core skills (ask an expert), 2) gather a large unlabeled dataset of gameplay, 3) label that dataset with preferences for each task, 4) learn options over the data, 5) prompt an LLM to combine the learned options. Have I missed something?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
10

### Rating Number
10

### Confidence
4

### Summary
This work presents a system for learning skills that humans describe in language. The system, called MaestroMotif, (1) trains per-skill reward functions using an LLM annotator of interaction datasets, (2) generates code describing the initiation and termination functions of skills, (3) generates code describing how to choose between skills during "training time", and (4) trains a skill-conditioned RL policy based on PPO. There are multiple experiments on the complex NetHack environment, where the proposed system is significantly stronger than other baselines.

### Strengths
- The experiments are comprehensive, covering most baselines one would expect and extensive ablations (like comparing skills learned in isolation vs simultaneously, LLM scale, and the architecture). Furthermore, the results clearly demonstrate the effectiveness of MaestroMotif.
- To me, the results of this paper mark a big improvement in the domain of hierarchical RL, where LLM-generated code is used to conduct high-level planning while a small RL network controls low-level actions.
- The proposed technique is quite general, being applicable across many domains outside of NetHack.
- The writing is very clear and the presentation is excellent overall.

### Weaknesses
 - The technique only trains reward functions on an existing offline dataset, which may be out of distribution with respect to the distribution of states encountered by the trained RL agent. This choice is borrowed from the original Motif paper (which said that the reward model was not fine-tuned during RL training due to simplicity), but based on the poor performance of the RL baselines (used to collect the original dataset) it seems like there may be a greater distribution shift in this work. Results determining whether the trained reward model generalizes to the online distribution would be appreciated (i.e. checking how much the annotator agrees with the reward model on trajectories generated by the final policy).
- The technique relies heavily on the LLM's ability to generate code. However, even with unit tests and code refinement this seems to be difficult for many LLMs according to Figure 9. It is unclear from the paper whether the 405B model has achieved close to "perfect" performance or if there are still key issues with the generated code. Further analysis of the failure modes of the LLM coders would be useful for readers.



### Questions
- MaestroMotif performs very well relative to all baselines, but still performs poorly in settings like Minetown, where only a 7.2% success rate is achieved. What are the bottlenecks to better performance? I.e. is the RL policy unable to complete the skills in this setting or is the generated "skill chooser" code bad for some tasks?
- What architecture is used for the reward functions? Prior RLHF literature initialized RMs from smaller LLMs, but it would be interesting to see if different sized RMs would lead to different results from RL training.

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents MaestroMotif, a novel method for AI-assisted skill design in RL that enables zero-shot adaptation to log-horizon tasks in NetHack. The key idea is using LLMs to map human-generated description of skills and high level policies to corresponding to skill specific reward functions, initiation and termination functions on the first hand, and high-level code-based policies on the other hand. 
The method is evaluated on NetHack, where it significantly outperforms existing approaches on a series of tasks.

Overall I really like the approach and I think this paper provides an interesting contribution to the field. This said, there are several missing information and several points I'd like to see discussed in the paper (see weaknesses and questions fields).

I'm going to give a rating of 6 for now and I'm willing to increase it if the authors address my concerns below.

Update: I increased the score to an 8 after the rebuttal (see discussion below)

### Strengths
The paper is well written and the approach is well motivated. 

The approach allows to construct high-performing policies for complicated, long-horizon tasks with high-level human inputs, which is quite impressive. 

Many connections with the option framework, makes the paper easy to parse and understand.

I liked the experiments comparing different methods for skill learning and the emphasis on transfer learning across different skills learned in the same network. 

Methods are rather clear and the appendix contains a lot of important information.

### Weaknesses
There is not much discussion about how robust the system is to the quality of human feedback, and my guess is that the system could be quite brittle.

The reliance on pre-collected expert / exploratory trajectories to generate the skill-specific reward function is a limitation of the approach that is not discussed.

Results are limited to a single environment, and the authors do not discuss how this approach would work in other environments, where it might be useful or not, what the cost of generating this human feedback is in the first place, etc.

The authors did not specify whether the code will be released publicly.

### Questions
These are questions and comments

Experiments comparisons:
* MaestroMotif is first training the skills, which costs GPU time too. So we should ideally compare this training resources and sample efficiency to the one of training a policy for the final downstream task. For fair comparisons, the "RL from scratch" approaches should be given the same training time and environment interactions as is used for MaestroMotif pretraining; is that the case?
* I do get the argument that when targeting a new task, there is no additional cost for MaestroMotif and there is one for the "RL from scratch" approach, but this also assumes that the test task can be decomposed with the existing skills, which is conveniently the case here, but might not be in general.
* Is the performance reported for task-specific training the training performance (with exploration noise), or performance measured outside of training with no exploration noise? In some environments where one mistake can be costly, using training performance with exploration noise would under-estimate true performance (eg crossing a bridge requires walking straight but exploration noise could throw you off). 

Online skill learning
* The approach here assumes access to a list of skill descriptions that when combined, allow to achieve any testing task, this is mentioned in the discussion. 
* This is an important assumption and I would like to see a discussion of how to move past it. 
  * Can we imagine the LLM generating candidate skill descriptions instead of using human-generated ones, and learn these? How good would that be? Could that only work if conditioned on a set of test tasks, or could an LLM intuitively figure out a good set of skills that can easily be combined to solve many downstream tasks?
  * What happens if a test task requires skills that were not pre-trained? The current architecture cannot recover from that, but could we imagine letting the LLM generate a missing skill description, pre-training a new skill and then adapting to that OOD task? Would that work?
* Providing feedback about how to best execute the skills in the training phase seems rather unnatural for a human user, could we imagine a way of automatic this process?
* Maybe we could learn a high-level transition model: which termination state distribution leads to which initiation state distribution, ie a graph model of skill chaining. Once we have that we could generate paths in that graph optimizing for some intrinsic metrics (active learning)? This paper does something a bit in that vein: https://arxiv.org/pdf/2402.15025 

Data annotation to synthesize reward functions: 
* "we independently annotate pairs of observations collected by a Motif baseline" → this sentence sounds like the authors did some of the annotation, is that the case?
* The fact that we need a dataset of expert / exploratory trajectories to train the reward functions so we can explore better seems like a limitation of this approach that should be discussed. How could the reward functions be synthesized without such data?
* How many trajectories are required to enable the training of the reward functions? What are the requirements in terms of data quality / diversity?

Robustness of the approach:
* The high-level policy is generated zero-shot (with couple of refinements), but what happens if it fails? Could the authors discuss how one could train this high-level policy? Maybe the algorithm sometimes needs to go back to the pretraining phase and add a new skill or refine a skill, maybe it needs to try another high-level strategy, how could it detect what's wrong and improve?
* There is no discussion about the impact of human-generated feedback on the success of the approach. How much time and effort has been put in the design of this feedback? Would it work with feedback generated by non-AI researchers NetHack experts? Here the skill descriptions seem rather finetuned. 

Results:
* Why is the Reward Information baseline performing worse than the Motif task-specific training? Doesn't it have access to the true task reward? What are the reward functions Motif generates here and how do these explain the higher performance?

Links with the planning literature
* The paper makes interesting connections with the option framework but doesn't mention connections with the planning literature, which I feel might be just as relevant. I especially think of PDDL approaches and task and motion planning (hierarchical planning)
* MaestroMotif indeed resembles approaches using LLM to generate PDDL domain descriptions: where skills are operators with initial and terminal functions, and the LLM is used to generate the high-level policy (bypassing planning) conditioned on code-based conditioned (equivalent to PDDL predicates), eg https://arxiv.org/pdf/2305.11014
* Chaining issues: although this does not seem to occur in the experiments, pretrained skills can often have the problem where the distribution of final state of an operator (/option), is different from the initiation states of the skill we may want to chain it with, such that the next skills stochastically can or cannot be applied. How would your approach handle this? Would it require coming back to the definition of termination function to have them be more constrained?

Typo: implemenetation (L508)

### Soundness
4

### Presentation
4

### Contribution
3
