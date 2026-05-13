# Proposer-Agent-Evaluator (PAE): Autonomous Skill Discovery For Foundation Model Internet Agents

- Decision: Reject
- Scores: 5, 5, 8, 3, 8

## Abstract
The vision of a broadly capable and goal-directed agent, such as an Internetbrowsing agent in the digital world and a household humanoid in the physical world, has rapidly advanced, thanks to the generalization capability of foundation models. Such a generalist agent needs to have a large and diverse skill repertoire, such as finding directions between two travel locations and buying specific items from the Internet. If each skill needs to be specified manually through a fixed set of human-annotated instructions, the agent’s skill repertoire will necessarily be limited due to the quantity and diversity of human-annotated instructions. In this work, we address this challenge by proposing Proposer-Agent-Evaluator(PAE), a complete working system that enables foundation model agents to autonomously discover and practice skills in the wild. At the heart of PAE is a context-aware task proposer that autonomously proposes tasks for the agent to practice with context information of the websites such as user demos or even just the name of the website itself. Then, the agent policy attempts those tasks with thoughts and actual web operations in the real world with resulting trajectories evaluated by an autonomous model-based success evaluator. The success evaluation serves as the reward signal for the agent to refine its policies through RL. We validate PAE on challenging vision-based web navigation, using both real-world and self-hosted websites from WebVoyager (He et al., 2024) and WebArena (Zhou et al., 2024a). Our results show that PAE significantly improves the zero-shot generalization capability of VLM Internet agents (more than 30% relative improvement) to both unseen tasks and websites. Our model also achieves an absolute advantage of over 10% (from 22.6% to 33.0%) comparing to other state-of-the-art open source VLM agents including Qwen2VL-72B. To the best of our knowledge, this work represents the first working system to apply autonomous task proposal with RL for agents that generalizes real-world human-annotated benchmarks with sota performances. We plan to release our models and code to facilitate further research.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a framework, Proposer-Agent-Evaluator(PAE), to boost the performance of agents in web tasks. In more detail, it uses a foundation model to automatically generate task instructions and another model to evaluate task completion and generate a reward. Lastly, RL is used to train a policy model.

### Strengths
1. The experiments are extensive. This paper compares with many SOTA baselines and makes many useful analyses. It shows the effectiveness of the proposed framework. 
2. This paper is easy to follow.

### Weaknesses
1. The main weakness is still the novelty. The method can be divided into two parts. Utilize existing foundation models to process data or automatically generate data. This part is not novel. Many other works have tried similar pipelines to collect data. The second part is using RL to fine-tune a model, which is also a standard procedure.


### Questions
Will the author build a large-scale dataset that can be released to the public?
The author mentioned the model only generates sparse rewards, will the batch RL be affected since only parts of the data have rewards?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents Proposer-Agent-Evaluator (PAE), a framework enabling autonomous skill discovery for vision-language model (VLM) internet agents. By employing a context-aware task proposer and an autonomous evaluator, PAE allows VLM agents to independently explore and refine skills for web navigation tasks, demonstrating improvements in success rates on benchmarks like WebVoyager and WebArena Easy compared to other open-source models. However, the model still relies on closed-source VLMs for effective task generation and evaluation, thus partially constraining the proposed framework’s open-source utility.

### Strengths
- Demonstrates an increase in performance for open-source model weights compared to previous open-source models.
- PAE framework leverages self-generated tasks, avoiding static human-annotated instructions.

### Weaknesses
 - The term "model-based task proposer" is used ambiguously. In reinforcement learning (RL), "model-based" generally implies use of a dynamics model for planning, whereas in this paper it refers to LLM prompting, which can lead to confusion in terminology.
- The novelty and motivation of the contributions are limited. Although the paper claims state-of-the-art (SoTA) for open-source models, it requires closed-source models for generating and evaluating tasks. This reliance on closed-source models highlights that the bottleneck remains the quality of these closed-source models, rather than any specific methodological improvement introduced by PAE. The paper does not adequately address the fundamental limitation that the performance gains are intrinsically tied to the capabilities of the closed-source models used for task generation and evaluation, making it unclear if the proposed method offers any advantage beyond leveraging these powerful models.
- The paper makes an assumption that the ground-truth task distribution and reward functions are inaccessible, even though in simulated environments, these can often be directly obtained (e.g., verifying if a button was clicked). If the goal is to improve policy generalization skills, and use ground-truth distributions and rewards only as a way to evaluate the method, the paper would benefit from a clearer rationale and explanation for this assumption (Section 3.1). The paper should clarify why a simulated environment with accessible ground truth is not used for training, and why the method is designed to learn from a self-generated task distribution when the true task distribution could be used for training.
- The paper lacks references to relevant prior work in autonomous task proposal and RL, and some claims of novelty are inaccurate, given that similar approaches have been explored [1, 2, 3, 4].

### Questions
- In PAE, why sample tasks uniformly rather than prioritizing by difficulty or learning progress?

Edit: updated score from 3 to 5

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces Proposer-Agent-Evaluator (PAE), a novel framework for autonomous skill discovery in foundation model agents, particularly focusing on Internet agents. PAE consists of three key components: a context-aware task proposer, an agent policy, and an autonomous evaluator. The framework enables agents to autonomously discover and practice skills without human supervision, potentially leading to a more diverse and scalable skill repertoire. The authors validate PAE on challenging vision-based web navigation tasks using both real-world and self-hosted websites. Results show that PAE significantly improves the zero-shot generalization capability of VLM Internet agents. Notably, the PAE-trained model outperforms other state-of-the-art open-source VLM agents. The authors claim this work represents the first attempt to apply autonomous task proposal with reinforcement learning for agents, achieving state-of-the-art performance among open-source models.

### Strengths
This paper demonstrates several notable strengths. The authors conducted comprehensive evaluations of their PAE framework across multiple challenging benchmarks, including WebVoyager and WebArena. They compared their method against a range of baselines, including proprietary models, state-of-the-art open-source vision-language models, and supervised fine-tuning approaches. This thorough evaluation provides a clear picture of PAE's performance in relation to existing methods.

The paper also presents a detailed analysis of the results, including error analysis and generalization studies. The authors break down different types of errors made by the models, providing insights into where improvements are made and what challenges remain. They also examine how well the skills learned through PAE transfer to unseen websites, demonstrating the framework's ability to develop general web browsing capabilities. Additionally, the authors investigate how PAE scales with larger base models and explore the impact of different context information on performance. This level of analysis and discussion significantly strengthens the paper by providing a nuanced understanding of the method's capabilities and limitations.

### Weaknesses
I am a little unclear about the novelty of the actual algorithm underlying PAE in comparison to something like OMNI (https://arxiv.org/pdf/2306.01711) and subsequent work. I think applying this kind of open-ended task selection for skill discovery to the internet agent case is definitely unique, but how does PAE differ from other open-ended skill discovery algorithms in other RL domains? If the authors could clarify this either in the related work section or after introducing their method in section 3.3 that would be really helpful.

Overall the results of the paper are strong, but framing the algorithmic novelty can be done with more clarity. If the novelty arises from the domain then this point and the difficulties of internet-based environments should be emphasized more rather than as just a potential application case as section 4 treats it as.

### Questions
How does PAE differ from other methods for skill discovery via foundation models such as OMNI?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a new framework called Proposer-Agent-Evaluator (PAE) which allows foundation model agents to autonomously discover and practice skills in the wild. The framework consists of a context-aware task proposer that suggests tasks for the agent to practice with website context information, an agent policy that attempts these tasks in the real world, and an autonomous model-based success evaluator that evaluates the resulting trajectories. The success evaluation serves as the reward signal for the agent to refine its policies. The authors validate PAE on challenging vision-based web navigation using real-world and self-hosted websites and demonstrate significant improvements in the zero-shot generalization capability of VLM Internet agents compared to state-of-the-art open-source VLM agents.

### Strengths
1. The paper is well written and easy to follow. The problem of foundation model agents and the PAE method is formally defined and clearly illustrated with figures. The idea of the Proposer-Agent-Evaluator framework seems reasonable in that the proposer should approximate the real-world task distribution and the agent learns to maximize the autonomous reward function.
2. Extensive and systematic experiments are carried out to verify the effectiveness of PAE compared with untrained VLMs and SFT training. Error analysis and the study of context complexity also show that the context-aware method can discover low-level web skills.

### Weaknesses
1. While the PAE framework seems reasonable, the method itself is naive and lacks novelty. Basically, the authors train a VLM with data containing instructions and successful trajectories relying on the proprietary VLMs, which is a common approach and does not include inspirational techniques. Although human annotation may overlook some long-tail real-world tasks, it's unclear why VLMs provided with web context can approximate the real-world task distribution. Also, behavior cloning the successful trajectories labeled by a VLM should not be described as reinforcement learning (line 117).
 2. It's not explained why behavior cloning is adopted instead of other training methods including SFT to discover web skills. Is the LLaVa-SFT baseline trained on the same trajectories as the proposed PAE model? What are the performances of other leading-edge VLMs such as GPT-4o? Comparisons with other trained web agents on Web Voyager or Web Arena are also missing.
3. Several typos in line 91 ('a foundation model agents') and line 191 (task distribution R).

### Questions
Response to the questions and concerns mentioned in the Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces a framework for autonomous skill discovery for real-world Internet agents, called PAE (Proposer Agent Evaluator). Compared to existing approaches, this method allows for the agent to collect, explore and refine new skills automatically, without relying on a limited set of predefined human-annotated instructions. The author(s) show how the additional PAE components introduced (the task proposer, the agent policy and the autonomous evaluator) allow for zero-shot SOTA generalization performance, as well as better success rates against opensource VLMs and finetuned opensource VLMs on 2 environments, WebVoyager and WebArena.

### Strengths
- The author(s) highlight and prove the feasibility of using much smaller VLMs and thus significantly lowering the test-time compute through their method, as opposed to finetuning larger models.

- The author(s) are willing to opensource the code and models to encourage further development in the research community.

- Overall, the paper is easy follow and clearly motivates the research question addressed and the main contribution in relation to existing literature. Concepts introduced in the main paper nicely point to corresponding appendix sections when needed which provide .

- The author(s) are doing a great job explaining how their work differentiates itself from existing research along 3 separate dimensions: foundation model agents, self-generated instructions and unsupervised skill discovery in RL. I particularly appreciate the focus on enabling the community to use much smaller sized models in terms of parameters, and therefore significantly less test-time compute.

- I appreciated the analysis on failure modes in Section 6, highlighting the value added by the PAE method, as opposed to SFT.

 - It is very good to see that each action contains chain of thought element, aiding interpretability of the model choices. The author(s) also take preventive measures, as highlighted in their Ethics statements.

### Weaknesses
 - To strengthen the submission/contribution, it would be good to elaborate on why proprietary VLMs outperform all opensource methods.

- It would be great to add some details/discussion on inference times, comparing the opensource VLMs, the SFT variation and PAE.

- It wasn't very clear to me how you define the reward for the agent policy, could you elaborate on that?

### Questions
Clarification Questions:

-	For all components, the task proposer, autonomous evaluator and agent policy, could you elaborate more on the choice of VLMs: Claude-3-Sonnet and the LLaVa models? Why those and not others?
-	For evaluation, could you elaborate on your choice of open-source VLMs? Why are they chosen as opposed to others?
-	In the main results, under the scaling paragraph, line 400, I’m not quite clear on the following statement “Again, LLaVa-34B PAE beats LLaVa-7B SFT on 12 out of 13..”. Is that the intended comparison, or did you mean to compare across PAE models only?
-	In the main results, under the generalization paragraph, line 405,  why is LLaVa-7B PAE highlighted, when actually you present results for the larger LLaVa-34B PAE as well in Table 3? Also in Table 3, why did you drop some of the other models from Tables 1 and 2 (Claude 3.5, InternVL and vanilla LLaVa-7/34B)?
-	In the alignment with human judgements, could you elaborate on how many human annotators were included in the user study and if possible how many hours they allocated to the task?

Minor comments/suggestions:

-	There are a few minor typos: on line 91 “for foundation model agents” (remove “a”), on line 191 in section 3.2, task distribution should be C instead of R, on line 485 “LLaVa-7B SFT knows that”
-	For consistency across the entire paper, use Claude-3-Sonnet – on line 269 in section 4.3, it is referred to as Claude-Sonnet-3.
-	Line 317 the LLaVa model name needs to be in bold to align with the others.

### Soundness
3

### Presentation
4

### Contribution
4
