# OMNI-EPIC: Open-endedness via Models of human Notions of Interestingness with Environments Programmed in Code

- Decision: Accept
- Avg Score: 6.75
- Scores: 3, 8, 8, 8

## Abstract
Open-ended and AI-generating algorithms aim to continuously \emph{generate} and \emph{solve} increasingly complex tasks indefinitely, offering a promising path toward more general intelligence. To accomplish this grand vision, learning must occur within a vast array of potential tasks. Existing approaches to automatically generating environments are constrained within manually predefined, often narrow distributions of environment, limiting their ability to create \emph{any} learning environment. To address this limitation, we introduce a novel framework, \ours{}, that augments previous work in Open-endedness via Models of human Notions of Interestingness (OMNI) with Environments Programmed in Code (EPIC). \ours{} leverages foundation models to autonomously generate code specifying the next learnable (i.e., not too easy or difficult for the agent’s current skill set) and interesting (e.g., worthwhile and novel) tasks. \ours{} generates both environments (e.g., an obstacle course) and reward functions (e.g., progress through the obstacle course quickly without touching red objects), enabling it, in principle, to create any simulatable learning task. We showcase the explosive creativity of \ours{}, which continuously innovates to suggest new, interesting learning challenges. We also highlight how \ours{} can adapt to reinforcement learning agents’ learning progress, generating tasks that are of suitable difficulty. Overall, \ours{} can endlessly create learnable and interesting environments, further propelling the development of self-improving AI systems and AI-Generating Algorithms. Project website with videos: \url{https://dub.sh/omniepic}.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents OMNI-EPIC, a system to design a large library of environments for reinforcement learning agents. OMNI-EPIC relies on Foundation Models, both large language models and vision language models. The system uses a pipeline where problems are specified in natural language, and then it uses an LLM as a synthesizer to generate programs encoding the environments. The environments are also evaluated with another LLM with respect to their interestingness; environments that aren't "interesting" are discarded. Finally, the system also has a module that checks whether a task was solved or not.

A few results of the system show that it is able to generate a diverse set of environments.

### Strengths
The paper attempts to tackle the ambitious problem of continually generating a diverse set of problems, from which an RL agent could learn. The idea of leveraging foundation models for this task is a promising idea. These models contain what one might call "general knowledge" that can be helpful in tackling this problem.

### Weaknesses
There are two key weaknesses with the paper that justifies my scores and recommendation.

**Scholarship**

First, the paper lacks scholarship, in the sense that the writing is sloppy (you read the sentences and say 'yes, I see what you mean, but what you wrote isn't technically correct.') and it lacks comparison with a very large body of works devoted to generating content in simulated environments: procedural content generation. I will give concrete examples and suggestions next.

The introduction of the paper talks about the grandiose plan of open-endedness, where systems would be able to come up with any computable environment. However, the paper is about generating environments in a restricted environment, with one specific simulator and small and discrete action spaces. It is not clear how the constrained experiments performed in this paper contribute to the grand goals of open-ended learning.

The environments that OMNI-EPIC generates could just be environments that humans implemented, made available online in GitHub, and an LLM was trained on. In this case, OMNI-EPIC is working as a retrieval system that can create different environments within a single codebase. While I see value in such a retrieval system, the paper is not about it. The paper doesn't even consider the possibility that the LLMs are simply retrieving knowledge and replicating it. From what I understand, this doesn't align with the open-ended goal of being... open-ended. A retrieval system will be bounded by whatever we created and made available online. The paper would have to go through a deep re-write to adjust these claims or to perform the proper evaluations to address these concerns.

Here are three examples of sentences that are sloppy.

1. *Because the model has distilled a sense of interesting from reading the internet.* The model does not read; we should use the correct technical terms. The model is trained on Internet data.
2. *Since code is Turing complete.* This is not true. You could have a language that is not Turing complete. The authors might be referring to commonly used general-purpose languages that are Turing complete.
3. *While our academic lab lacks the resources to train generalist agents on a large set of OMNI-EPIC-generated tasks, our findings suggest that this would be straightforward.* While I appreciate the use of the word "suggest," I don't see how we can conclude that learning a generalist agent is straightforward. Training RL agents is tricky (catastrophic forgetting and saturated neural networks are examples of issues one might come across). Evidence suggests that doing this in dozens of environments cannot be straightforward.

Overall, the paper currently reads like an informal report, which makes it difficult to pinpoint the problem that is being solved and the claims that are being made.

Finally, OMNI-EPIC is closely related to procedural content generation, an active research area in the computer games community. See the book *Procedural Content Generation in Games* by Noor Shaker, Julian Togelius, and Mark J. Nelson for an outdated overview.

**Evaluation**

The experiments are unfinished, as the environments generated with OMNI-EPIC are not used to actually evaluate RL algorithms and how such environments can potentialize them. The evaluation focuses on metrics of diversity of the environments used, instead of focusing on the actual goal of improving learning. If the goal is to learn a generalist agent (is that true?), then why not evaluate it that way? The current evaluation serves as a proxy for the actual evaluation, and it is not clear how good of a proxy this is.

The paper justifies why the evaluation is restricted by saying they do not have enough computational resources. While I sympathize with the issue, I cannot recommend acceptance of a paper that doesn't evaluate on the problem it is trying to solve.

### Questions
1. Is there a way you could have OMNI-EPIC design simpler problems for which you could thoroughly evaluate RL agents? Even with the amount of computational resources you have available in your research lab?
2. How can you verify whether OMNI-EPIC is solving a retrieval problem or an environment-generation problem?
3. Why is Darwin-completeness defined as the potential to generate any learning environment? How is Darwin's theory of evolution related to the ability to generate learning environments?

### Soundness
1

### Presentation
1

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
This paper uses an LLM to generate environment code for an RL agent. This is combined with another foundation model that serves as a proxy for human models of interestingness. Together, the first LLM generates code whereas the second guides this process towards novel and interesting tasks. Theoretically, treating the environment as code is a much less constrained way to generate environments compared to much of the prior work. The paper also provides two experiments, one with simulated learning to focus on the environment generation, and another with actual RL agent training to identify how these two components interact.

### Strengths
- I agree, using code as an environment representation is indeed much more expressive than changing hand-designed features within a very constrained environment, as prior work does.
- It is great that this paper does provide a full pipeline that theoretically can be run for a long time to continuously generate novel tasks.

I am not giving it a lower score because I think the idea of using code as an environment representation is a good idea that future work can build on. Furthermore, demonstrating a full end-to-end pipeline is useful.
I am not giving it a higher score because I think the results are not that compelling. That is not to say that this approach does not hold promise---and I hope future work/the authors build on this---but the outcomes in this work are not that open ended.

### Weaknesses
While code as a representation is expressive in theory, all of the different environments seem quite similar. This is partly due to the agent in all of these tasks being the same.
	- However, if you remove the restriction of using this particular robot in a particular simulator, then the task may become too difficult for current LLMs, or you could end up generating only a certain type of task.
- It feels like the claims made are that we can express any possible task, and that, when run long enough, we will eventually obtain a very large number of semantically diverse environments; however, the results do not seem to substantiate this claim.
- Figure 2 is very hard to understand and parse, is there a better way to show the same information?
- This sentence is a bit hard to parse/can be rewritten
> Because the model has distilled a sense of interesting from reading the internet, it has a model ofi nterestingness (MoI) that emulates the human capacity for nuanced judgments of interestingness in open-ended learning (Zhang et al., 2023), which it brings to bear when generating tasks.

### Questions
- Is the code open source?
- To what extent will this be limited by the dataset of the coding LLM? Will there ever be truly novel environments generated?
- It is a bit unclear to me, but when starting the process, do you first sample a random task from the archive, and then use this as the reference task to choose the N most similar ones.
- Consider the following case:
	- You have 10 tasks in the archive, say 5 of type A and type B. Type A tasks are all somewhat similar to each other, but different to type B. As an example, type A tasks involve kicking a ball and type B involves crossing a bridge. Suppose the number of tasks given to the LLM if 5, say.
	- Would the following cyclic behaviour be possible? Please comment/explain how or how not, and what possible solutions there are.
		- The task generator receives 5 tasks of type A, and is asked to generate a novel and new task. Then it does this by generating a type B task. However, the post generation MOI rejects this because the archive already has many of these, so the task is not added. Whenever the randomly-chosen task is type A, this happens, and the opposite for type B.
		- If this happens, it seems like the process will just remain stuck and never generate anything new.
- Would there be axes of variation that are not explored at all by an LLM, potentially due to the bias in its data, or by virtue of how it predicts the next token? Concretely, suppose you apply this to a more general environment representation (where the LLM can change everything), and it happens to generate a physics-based R2D2 environment. Then, when generating new tasks, will it ever do something very different, like generating a game like Pong (different controls, doesn't use a robot anymore, etc.) or will it continuously generate variations of R2D2 physics tasks? Please elaborate on this

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces OMNI-EPIC, an open-ended system that generates novel and learnable environments and tasks for RL agents. The method leverages current language and vision foundation models to generate the environments (through code) and filter the novel and learnable ones. The authors show how the system generates diverse, interesting, and learnable tasks for RL agents, starting from a very small set of initial environments. Experiments show the potential of the system to produce endless automatic curricula for increasingly complex agents.

### Strengths
- The paper is generally well written and the ideas are mostly clearly transmitted. The figures are clean and support the text, helping to transmit the paper's main ideas.

-  I think that the contribution is substantial. The fact that OMNI-EPIC can successfully generate diverse, novel, and learnable environments through code (Python+PyBullet) constitutes a valuable opportunity for the open-endeness community to analyze these systems and advance the field. 

- Moreover, OMNI-EPIC successfully employs foundation models to leverage notions of human interestingness. Generating novel, but interesting environments (that are relevant to humans) is a key challenge in unsupervised environment design and the open-endedness field. Although previous works have pointed to the possibility of using foundation models for this purpose [1], this work is an excellent example of how foundation models can be successfully used for this purpose, which is also a valuable contribution by itself. 

[1] Hughes, Edward, et al. "Position: Open-Endedness is Essential for Artificial Superhuman Intelligence", ICML24.

### Weaknesses
 **W1:** One of my main concerns with this work is the gap between the claims made and the actual demonstrations in the paper.
Authors claim multiple times that OMNI-EPIC can generate an endless stream of environments (e.g., L082, L151, L424). See line 424: *"[...] ensuring a progressive, never-ending curriculum for training"*, note that this is a **very** strong claim. However, the experimental results are far from demonstrating this capability. Experiments show the generation of 200 environments, but considering that all are solvable (which I consider a very strong assumption). When considering the performance of RL agents in the generated environments, the authors only show a sequence of 22 tasks.  These are some suggestions to address the issue:

- Use simpler alternatives to Dreamer V3 (e.g., PPO with simpler NN architectures) to reduce the computational cost of training the agent and demonstrate that the novelty and learnability of the tasks generated by OMNNI-EPIC hold for longer environment generation steps.

- Reduce the claims made in the paper. Under the current experimental results, there's no real evidence that OMNI-EPIC could continue to generate novel and learnable environments for very large runs.

**W2:** Although the performance of current LLMs is excellent for many coding and text generation tasks, these also present some limitations, which some relate to difficulties in generating novelty. The fact that OMNI-EPIC completely relies on these models, makes me believe that the presented method would especially suffer from the mentioned novelty issue. This weakness is related to the previous, as no evidence is shown on the capability of OMNI-EPIC to  "endlessly" generate novel and solvable environments.

**W3:** As many deep NN models, LLMs also suffer from brittleness. As OMNI-EPIC relies on multiple LLMs working together, this makes me believe that the presented system can greatly suffer from this brittleness issue, as there is no evidence for the contrary. Further experiments on this topic would greatly help to analyze the actual capabilities and limitations of the proposed method. What is the ratio between successful and failed attempts at generating working/solvable environments? This is only an idea, but many similar experiments could be included that would significantly improve the soundness of the paper.

**Minor issues:** 
- Authors mention multiple times that "code is Turing complete" (e.g., L93, L520). This is very vague, please be rigorous, as many types of "code" (i.e., programming languages) exist but not all are Turing complete. 
- Python being Turing complete does not guarantee that a foundation model (and by consequence, OMNI-EPIC) can generate any computable environment. There would be many computable environments that would have zero probability of being generated by a specific foundation model. Present rigorous arguments or remove/modify this claim.
- I think that the "cell coverage of archive diversity" metric is not explained in the main text. I think that the overall clarity of Section 6 could be improved.
- Check the coherence of the references. For example, some references include the proceedings with different styles: some use "In Proceedings [...]", others "In [...]", and others just directly mention the specific proceeding.

I want to emphasize that I think that the contribution of the paper is valuable to the field and that I'm willing to update my score if the mentioned issues are addressed.

### Questions
**Q1:** Do you have any result or hypothesis on how much the initial set of environments in the task archive conditions the generation of new environments?

**Q2:** How does the task similarity method scale with the number of tasks? If the idea is to endlessly generate tasks, this similarity method should be very computationally efficient.

**Q3:** Does the simplified action space limit the diversity and complexity of the generated environments? 

**Q4:** L283 states "We employ a success detector, instantiated as an LLM or VLM", later L304-305 mentions "Although our preliminary testing found that current VLMs are not yet accurate enough to be used as success detectors". Given the second sentence, I find very surprising the usage of VLMs as success detectors in  OMNI-EPIC. Why does OMNI-EPIC employ VLMs for this purpose even though the authors mention that VLMs are still not ready for the task?

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
OMNI-EPIC is a novel framework that aims to create truly open-ended learning environments by combining foundation models with reinforcement learning. The system generates new tasks (descriptions + code) with potential applications for open-ended learning.

Overall I really like the ambition of this paper, and I think it would be good to show new directions to the community. It's tackling a very important problem and proposes a sensible approach to tackle it.  This said, I think the claims made in the paper are strongly exaggerated and mostly unsupported. Below I will list ideas of follow-up experiments that could help support the claims. 

I feel like the computational constraints of the project associated to its ambition caused a necessary tradeoff between running the main experiments of this paper and running the sufficient set of side experiments (variations, ablations, baselines). 

I will assign a score of 6 as I think this paper is already valuable in its current state (if the claims were to be toned down). I'm willing to raise the score if new experiments are shown to support the claims.

I updated my score in light of the discussion (see below)

### Strengths
* The idea is original and forward-looking: this is making first steps towards the future of autotelic learning / open-ended learning by extending the space of tasks an agent can generate to drive its own learning.
* The paper is well written and well motivated, the methods are well described with many details in the appendix.
* Generated tasks are fun and I appreciate the accompanying website showing task descriptions and codes.

### Weaknesses
 * The paper doesn't make an explicit list of contributions. Is it about showing open-ended learning? Is it about extending task generation from goals and levels to full environments? Is it about this and tailoring task distributions to the agent's learning capabilities? I would appreciate a clear statement about the contributions of the paper.
* The paper makes a lot of strong claims about interestingness, diversity, curriculum learning and open-endedness, but I would argue that the experiments don't support most of them (see more below).

### questions:
 This section includes questions and comments. 

The "never-ending curriculum" claim:
* The approach does not train a single generalist agent to solve all tasks, why not? Was it tried and did it fail? I assume there would be issues with continual learning / catastrophic forgetting, did the authors find this was a problem?
* Is there transfer learning across tasks? Here, there is a different agent for each new task, but an agent for a new task is initialized to the weights of the agent for the nearest solved task. This supposedly enables some form of transfer learning, but I don't think this is empirically tested anywhere? 
  * Do agents initialized this way empirically learn faster than agents trained from scratch?
  * Is training an agent in a given task generally faster when this task is invented later, than earlier? When invented later, there should be a closer nearest neighbor and if there is transfer learning (previous point), then agents should learn faster and faster as the run progresses.  This would indicate that the overall agent (collection of agents) is actually learning something on the way (getting better at achieving tasks). 
* To show evidence for a curriculum effect driven by task generation, one would also need to show that the difficulty of tasks is increasing with time, i.e. by showing that the success rate of agents trained from scratch is decreasing as the experiment advances. In POET for instance, the latest tasks are shown to be out of reach for agents trained from scratch, is this the case here? Showing this would be strong evidence to support the "curriculum" claim (not sure about the "never-ending" bit).
* The claim that the task generator optimizes for learning progress is also not empirically verified, is it really shifting the distribution towards harder tasks as the experiment advances (point above)? Here one would need to show a baseline that doesn't leverage the success/failure feedback or simply is not prompted to generate tasks of intermediate difficulty and compare the relative abilities of the two algorithms to solve new tasks in the end (by taking the nearest neighbors in the respective archive and training from them). Is the "learning progress" bit actually helping training more competent agents?
* Since the agents don't seem to be trained again on past tasks, the archive does not contain any information about the current capabilities of the meta agent (population of agents). As a result, the task generator cannot generate "tasks of intermediate difficulty" for a progressing agent (it doesn't get information about the current agent). It can only generate tasks of intermediate difficulty for the "average" of all agents since the start of the experiment. 
* Without evidence for transfer learning across tasks, agent (population) improvement over time and task difficulty increase over time, the claim of a "never-ending curriculum learning" is not supported and should thus be removed.

Measuring success / performance
* Success is measured by a VLM, but this VLM is not validated. Does it agree with people? I see human judgements in the video on the website, is there an evaluation of how good the VLM is using these ground truth feedbacks?
* If this signal is not reliable (as suggested early in the paper), then the final metric measuring the number of different tasks solved is also not reliable. Having an unreliable fitness metric is fine during training, but becomes a problem when it's used for evaluation and algorithms comparison.
* The "long run without learning" experiment is interesting to get a sense of the diversity of the tasks, but it would be good to know how many of these tasks are actually learnable? I feel like there is a high chance that while the code is executable, the task might be purely impossible to solve. Maybe this could be obtained by subsampling generated tasks and estimating the proportion of tasks that can be solved? The second experiment does test for solvability (through learning and the solved/failed label), but it would be interesting to know if the in-context learning of the task generator (prompted to generate tasks with intermediate difficulty) is actually working, ie if the ratio of solvable tasks is higher in the second versus the first condition?


Measuring novelty, interestingness, diversity:
* The diversity metric in Figure 4 is computed on the simulated learning variants, which means that it's not filtered for solvable tasks and it's not clear which of these are actually solvable. I feel like we care more about the diversity of solved tasks (so the diversity of learned behaviors).
* Is the PCA computed over all tasks from all algorithms? The discretization size is very important here and I'm not sure these results would hold for different step sizes?
* Wouldn't sampling in context examples uniformly in the archive generate even more diversity by increasing the possibilities for recombinations?
* Is the MoI really doing its job? In Figure 3, tasks are considered novel enough if they just change the surface form of the goal, eg "jumping across platform" is considered new if it's above water, or above lava, although these don't change anything to the task, only the color of the background. More generally, this model is not validated against human judgements but is here also used for algorithm evaluations. 

Open-endedness claim:
* As far as I understand, this claim is only supported by the graph in Figure 4. I appreciate the extra criterion on whether a new problem is "interesting" but this decision mechanism is probably quite unstable, e.g. the order in which tasks are presented probably influences the judgment of whether a new task is deemed novel. 
* Stating that we don't see it plateauing considering there are only 13 environments generated is true but also not a strong marker for open-endedness and shouldn't be used to make this claim.
* Support for actual curriculum learning would help support the claim for open-endedness, although the "never-ending" aspect would probably require much longer runs of the algorithm.

Related Work: The related work mentions key research in environment design but does not acknowledge the older and wider field of intrinsic motivations, which I feel is foundational for the presented work. 

* Learning progress has an older history than Kanitscheider et al. LP in prediction networks dates from Schmidhuber's 91 work on curiosity (see history in https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=5508364), and was formalized in 2007 by Oudeyer and Kaplan (https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=4141061, https://pmc.ncbi.nlm.nih.gov/articles/PMC2533589/)
Around 2013 Oudeyer's lab has been using the "competence progress" form, measuring progress in goal-achievement / task completion to drive exploration and skill learning (https://www.sciencedirect.com/science/article/pii/S0921889012000644 and others in 2013-2014). Since 2018, it's been using with intrinsically motivated deep RL approaches too (http://proceedings.mlr.press/v97/colas19a/colas19a.pdf, https://proceedings.neurips.cc/paper_files/paper/2019/file/b6f97e6f0fd175613910d613d574d0cb-Paper.pdf)
* "Focusing on interesting tasks" is basically what intrinsic motivations are about. In Oudeyer and Kaplan's initial framework on IM, there is already the "competence-based IM" aiming at selecting the most useful goals for exploration and skill learning (https://pmc.ncbi.nlm.nih.gov/articles/PMC2533589/). Since 2018, it's been combined with deep RL and there is now a whole field of methods focusing on that (see review in https://arxiv.org/pdf/2012.09830). 
* VLM success detectors: https://arxiv.org/pdf/2303.07280, I don't think Christiano 2017 was a VLM? There is no language there and the model is for a single task.



Clarification questions and other suggestions:
* Do the authors plan on releasing the code? This approach has many components and many parameters, probably making it hard to reproduce. Releasing the code would ensure reproducibility.
* "Previous attempts have resulted in pathologies when optimizing against definitions and quantifications of interestingness" → which ones? How is the current approach overcoming these issues?
* Are the task embeddings computed from the linguistic descriptions? the code? the agent trajectories? combinations of these?
* It's not so clear what happens to tasks who keep on failing to compile, are they added as failed to archive? If not added to the archive, how is this information routed back to the task generator? If added as failed, shouldn't we differentiate "failed because of compilation" and "failed because the agent couldn't solve it"?
* It would be good to show somewhere the success rates at various stages, e.g. the % of tasks that are successfully turned into executable environment code, the % of these that are accepted by the post-hoc MOI checker, the % of the latter that are successfully solved. In the long run without training, how many of the 200 iterations led to executable environment code? And how is executability checked here? By running a random policy maybe?
* I think it would generally be good to conduct experiments for variants/ablations of the task generator:
  * does the LP prompt actually generate tasks more tailored to the agent?
  * does combining it with success/failure actually help generate tasks that are more solvable and not trivial?
  * does conditioning on nearby tasks help the LP modeling and the effects above compared to sampling tasks uniformly from the archive?


Typos
* L17: "narrow distributions of environment" → +s
* L175: "OMNI-EPIC continuously generate and solve new, interesting tasks in simulation." → generates, solves

### Questions
This section includes questions and comments. 

The "never-ending curriculum" claim:
* The approach does not train a single generalist agent to solve all tasks, why not? Was it tried and did it fail? I assume there would be issues with continual learning / catastrophic forgetting, did the authors find this was a problem?
* Is there transfer learning across tasks? Here, there is a different agent for each new task, but an agent for a new task is initialized to the weights of the agent for the nearest solved task. This supposedly enables some form of transfer learning, but I don't think this is empirically tested anywhere? 
  * Do agents initialized this way empirically learn faster than agents trained from scratch?
  * Is training an agent in a given task generally faster when this task is invented later, than earlier? When invented later, there should be a closer nearest neighbor and if there is transfer learning (previous point), then agents should learn faster and faster as the run progresses.  This would indicate that the overall agent (collection of agents) is actually learning something on the way (getting better at achieving tasks). 
* To show evidence for a curriculum effect driven by task generation, one would also need to show that the difficulty of tasks is increasing with time, i.e. by showing that the success rate of agents trained from scratch is decreasing as the experiment advances. In POET for instance, the latest tasks are shown to be out of reach for agents trained from scratch, is this the case here? Showing this would be strong evidence to support the "curriculum" claim (not sure about the "never-ending" bit).
* The claim that the task generator optimizes for learning progress is also not empirically verified, is it really shifting the distribution towards harder tasks as the experiment advances (point above)? Here one would need to show a baseline that doesn't leverage the success/failure feedback or simply is not prompted to generate tasks of intermediate difficulty and compare the relative abilities of the two algorithms to solve new tasks in the end (by taking the nearest neighbors in the respective archive and training from them). Is the "learning progress" bit actually helping training more competent agents?
* Since the agents don't seem to be trained again on past tasks, the archive does not contain any information about the current capabilities of the meta agent (population of agents). As a result, the task generator cannot generate "tasks of intermediate difficulty" for a progressing agent (it doesn't get information about the current agent). It can only generate tasks of intermediate difficulty for the "average" of all agents since the start of the experiment. 
* Without evidence for transfer learning across tasks, agent (population) improvement over time and task difficulty increase over time, the claim of a "never-ending curriculum learning" is not supported and should thus be removed.

Measuring success / performance
* Success is measured by a VLM, but this VLM is not validated. Does it agree with people? I see human judgements in the video on the website, is there an evaluation of how good the VLM is using these ground truth feedbacks?
* If this signal is not reliable (as suggested early in the paper), then the final metric measuring the number of different tasks solved is also not reliable. Having an unreliable fitness metric is fine during training, but becomes a problem when it's used for evaluation and algorithms comparison.
* The "long run without learning" experiment is interesting to get a sense of the diversity of the tasks, but it would be good to know how many of these tasks are actually learnable? I feel like there is a high chance that while the code is executable, the task might be purely impossible to solve. Maybe this could be obtained by subsampling generated tasks and estimating the proportion of tasks that can be solved? The second experiment does test for solvability (through learning and the solved/failed label), but it would be interesting to know if the in-context learning of the task generator (prompted to generate tasks with intermediate difficulty) is actually working, ie if the ratio of solvable tasks is higher in the second versus the first condition?


Measuring novelty, interestingness, diversity:
* The diversity metric in Figure 4 is computed on the simulated learning variants, which means that it's not filtered for solvable tasks and it's not clear which of these are actually solvable. I feel like we care more about the diversity of solved tasks (so the diversity of learned behaviors).
* Is the PCA computed over all tasks from all algorithms? The discretization size is very important here and I'm not sure these results would hold for different step sizes?
* Wouldn't sampling in context examples uniformly in the archive generate even more diversity by increasing the possibilities for recombinations?
* Is the MoI really doing its job? In Figure 3, tasks are considered novel enough if they just change the surface form of the goal, eg "jumping across platform" is considered new if it's above water, or above lava, although these don't change anything to the task, only the color of the background. More generally, this model is not validated against human judgements but is here also used for algorithm evaluations. 

Open-endedness claim:
* As far as I understand, this claim is only supported by the graph in Figure 4. I appreciate the extra criterion on whether a new problem is "interesting" but this decision mechanism is probably quite unstable, e.g. the order in which tasks are presented probably influences the judgment of whether a new task is deemed novel. 
* Stating that we don't see it plateauing considering there are only 13 environments generated is true but also not a strong marker for open-endedness and shouldn't be used to make this claim.
* Support for actual curriculum learning would help support the claim for open-endedness, although the "never-ending" aspect would probably require much longer runs of the algorithm.

Related Work: The related work mentions key research in environment design but does not acknowledge the older and wider field of intrinsic motivations, which I feel is foundational for the presented work. 

* Learning progress has an older history than Kanitscheider et al. LP in prediction networks dates from Schmidhuber's 91 work on curiosity (see history in https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=5508364), and was formalized in 2007 by Oudeyer and Kaplan (https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=4141061, https://pmc.ncbi.nlm.nih.gov/articles/PMC2533589/)
Around 2013 Oudeyer's lab has been using the "competence progress" form, measuring progress in goal-achievement / task completion to drive exploration and skill learning (https://www.sciencedirect.com/science/article/pii/S0921889012000644 and others in 2013-2014). Since 2018, it's been using with intrinsically motivated deep RL approaches too (http://proceedings.mlr.press/v97/colas19a/colas19a.pdf, https://proceedings.neurips.cc/paper_files/paper/2019/file/b6f97e6f0fd175613910d613d574d0cb-Paper.pdf)
* "Focusing on interesting tasks" is basically what intrinsic motivations are about. In Oudeyer and Kaplan's initial framework on IM, there is already the "competence-based IM" aiming at selecting the most useful goals for exploration and skill learning (https://pmc.ncbi.nlm.nih.gov/articles/PMC2533589/). Since 2018, it's been combined with deep RL and there is now a whole field of methods focusing on that (see review in https://arxiv.org/pdf/2012.09830). 
* VLM success detectors: https://arxiv.org/pdf/2303.07280, I don't think Christiano 2017 was a VLM? There is no language there and the model is for a single task.



Clarification questions and other suggestions:
* Do the authors plan on releasing the code? This approach has many components and many parameters, probably making it hard to reproduce. Releasing the code would ensure reproducibility.
* "Previous attempts have resulted in pathologies when optimizing against definitions and quantifications of interestingness" → which ones? How is the current approach overcoming these issues?
* Are the task embeddings computed from the linguistic descriptions? the code? the agent trajectories? combinations of these?
* It's not so clear what happens to tasks who keep on failing to compile, are they added as failed to archive? If not added to the archive, how is this information routed back to the task generator? If added as failed, shouldn't we differentiate "failed because of compilation" and "failed because the agent couldn't solve it"?
* It would be good to show somewhere the success rates at various stages, e.g. the % of tasks that are successfully turned into executable environment code, the % of these that are accepted by the post-hoc MOI checker, the % of the latter that are successfully solved. In the long run without training, how many of the 200 iterations led to executable environment code? And how is executability checked here? By running a random policy maybe?
* I think it would generally be good to conduct experiments for variants/ablations of the task generator:
  * does the LP prompt actually generate tasks more tailored to the agent?
  * does combining it with success/failure actually help generate tasks that are more solvable and not trivial?
  * does conditioning on nearby tasks help the LP modeling and the effects above compared to sampling tasks uniformly from the archive?


Typos
* L17: "narrow distributions of environment" → +s
* L175: "OMNI-EPIC continuously generate and solve new, interesting tasks in simulation." → generates, solves

### Soundness
2

### Presentation
4

### Contribution
3
