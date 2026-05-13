# WebRL: Training LLM Web Agents via Self-Evolving Online Curriculum Reinforcement Learning

- Decision: Accept
- Scores: 6, 8, 6

## Abstract
Large language models (LLMs) have shown remarkable potential as autonomous agents, particularly in web-based tasks. 
However, existing LLM web agents heavily rely on expensive proprietary LLM APIs, while open LLMs lack the necessary decision-making capabilities. 
This paper introduces \model, a self-evolving online curriculum reinforcement learning framework designed to train high-performance web agents using open LLMs. 
\model addresses three key challenges in building LLM web agents, including the scarcity of training tasks, sparse feedback signals, and policy distribution drift in online learning. 
Specifically, \model incorporates 1) a self-evolving curriculum that generates new tasks from unsuccessful attempts, 2) a robust outcome-supervised reward model (ORM), and 3) adaptive reinforcement learning strategies to ensure consistent improvements. 
We apply \model to transform open Llama-3.1 and GLM-4 models into proficient web agents. %
On WebArena-Lite, \model improves the success rate of Llama-3.1-8B from  4.8\%  to 42.4\%, and from 6.1\% to 43\% for GLM-4-9B. %
These open models significantly surpass the performance of GPT-4-Turbo (17.6\%) and GPT-4o (13.9\%)  and  outperform previous state-of-the-art web agents trained on open LLMs (AutoWebGLM, 18.2\%). 
Our findings demonstrate \model's effectiveness in bridging the gap between open and proprietary LLM-based web agents, paving the way for more accessible and powerful autonomous web interaction systems.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes WebRL: a framework for training agents that can navigate the web using reinforcement learning. They apply their framework to train Llama-3 8B and Llama-3 70B agents that navigate the web, with strong performance on WebArena-Lite.

The overall process for training the agents is:

1. Run the agent on an initial set of instructions from the WebArena-Lite training set, and score them with the WebArena-Lite reward function. Initialize the replay buffer with successful trajectories. Initialize the failure set with instructions from the failing trajectories. Train an outcome-supervised generative reward model (ORM) using these trajectories to predict whether a task has been successfully completed. 
2. Generate 500 new instructions using GPT-4o, prompting it to create instructions similar to the ones from the failure set, but more diverse.
3. Filter the generated instructions. First filter them using the trained critic (value function), keeping instructions which the critic predicts are difficult but possible (between 0.05 and 0.75). Then filter through manual human review, to eliminate bad instructions.
4. Run the agent on the instructions to generate a set of trajectories to generate a training set. Extend the training set with actions from the replay buffer whose perplexity is between 1/0.95 and 1/0.5.
5. Update the agent policy on these trajectories using an RL algorithm that combines policy gradients, advantage estimation, and replay buffers.
6. Add successful trajectories to the replay buffer, and add instructions from failing trajectories to the failure set.
7. Go back to step 2 to begin a new phase.

The authors compare against a variety of baselines, including imitation learning and DigiRL, as well as a variety of ablations of their method.

### Strengths
* Training LLMs to navigate the web is an important area of research
* The results in the paper appear to be quite strong.
* The experimental results involve a good variety of baselines and ablations.

### Weaknesses
## RL algorithm

There are a few weaknesses with the RL approach (Section 2.1):

*   It’s not clear to me why the authors derive a new RL algorithm. I don’t see what benefits this would have over the approach of using PPO with the KL-regularized reward (as in [Ziegler et al](https://arxiv.org/abs/1909.08593)). In fact, I believe that the authors’ algorithm is nearly equivalent to REINFORCE with a value function baseline – the only difference I see is that in the authors’ algorithm, the gradient is multiplied by a factor of $\beta$, which seems undesirable to me (ideally the scale of the gradient wouldn’t be sensitive to $\beta$). It is unclear why this scaling factor is necessary, and how it affects the convergence properties of the algorithm. Furthermore, the authors do not provide a clear justification for why they chose this particular form of the loss function, or why it is expected to lead to better performance than standard policy gradient methods.
*   In addition, this new algorithm is an on-policy algorithm – but it is used alongside a replay buffer, which is naturally off-policy. Presumably an off-policy correction term would be needed. The authors do not discuss how they handle the mismatch between the on-policy nature of their algorithm and the off-policy nature of the replay buffer. This is a critical oversight, as using a replay buffer with an on-policy algorithm can lead to instability and divergence. The lack of an off-policy correction term is a significant concern.
*   Also, the math used to derive the new algorithm is flawed. Specifically, to derive Equation (5) from Equation (4), the authors rely on the result that the optimal policy in an RL environment is unaffected by potential shaping. However, this result does not hold in the KL-regularized RL setting, so this step is invalid. The authors need to provide a more rigorous derivation of their algorithm, taking into account the specific properties of KL-regularized RL. The current derivation is not mathematically sound.

## Presentation

I found the paper somewhat hard to understand – it was hard to tell what the various components were and how they fit together. Figure 1 is quite helpful in clarifying this with an architecture diagram, but I would recommend that the authors also include an algorithm description, similarly to the outline provided in my summary above. (Please do also let me know if my summary is wrong.)

It is somewhat misleading to say that the task distribution is “self-evolving” when it involves a manual step (L261):

> Then, we manually check the instructions to eliminate instructions that are clearly unreasonable or impossible to accomplish.

## Other

**Single benchmark.** Since the authors only evaluate on a single task (WebArena-Lite) it is hard to tell which aspects of their setup are specific to WebArena and which are generalizable to any LLM control environment. Given the importance of browser control, and the diversity of tasks within WebArena, this is only a minor weakness. However, it could be addressed by applying the WebRL recipe to similar settings, such as Android (in which DigiRL was evaluated).

**Task complexity results.** On lines 392-396 the authors say:

> Our results show that WEBRL performs well across different complexity levels, particularly excelling in more complex instructions. In contrast, while DigiRL uses online learning, it struggles with higher complexity due to its focus on a fixed set of tasks, limiting its adaptability.

However, this doesn’t seem to be supported by Figure 5, where it appears that both WebRL and DigiRL see significantly lower task success rates at higher complexity levels.

**KL ablation.** The authors say they consider a version of WebRL without the KL regularization – however, they say that this involves running SFT. This seems like the wrong way to do it – instead, the policy should be trained with an RL algorithm, but without the KL regularization. This would produce a similar gradient as SFT, except that it would be weighted by the advantage function. The baseline reported in the paper is also interesting, though it should be called “WebRL-SFT” or something similar rather than “WebRL w/out KL”.

### Questions
* Why do you develop a new RL approach, rather than applying PPO (or a similar algorithm) to the KL-regularized reward?
* Why are the success rates in Figure 5 so low? Shouldn’t they be around 40% on average for WebRL, to be consistent with Table 1? Perhaps the denominator in Figure 5 was accidentally set to “all tasks” rather than tasks at the appropriate complexity level.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
Authors present WebRL, a new framework to fine-tune LLMs for interactive web tasks with sparse rewards. WebRL leverages a curriculum learning setup to perform online actor-critic RL over generated task sets of increasing difficulty. The completion of these generated tasks is assessed autonomously using a learned reward model. Experimental studies are conducted on WebArena-Lite. There, authors showcase the performance advantages of their approach wrt prompt-based method and learning-based methods such as imitation learning or reinforcement learning.

### Strengths
This paper tackles a very important topic.
It is well written, I enjoyed reading it.
Authors showcase an impressive performance gap over considered baselines.
Authors present an in-depth analysis of their approach, which is valuable

### Weaknesses
### Comparison to no-curriculum RL

The no-curriculum reinforcement learning baseline considered in this paper is Digi-RL. It is in my opinion the most important baseline. It would be good to better understand the differences between Digi-RL and WebRL. Is WebRL  == "Digi-RL with a Curriculum Learning (CL) setup, a KL loss and a replay buffer" ? If no, what are the differences ? What I mean behind this question is that ideally to propose a new CL method it is better to plug the CL method on a well known learner, rather than proposing a new learner AND a curriculum learning method.

### Reliance on human-filtering for curriculum steps

An important weakness is that the curriculum learning process is not autonomous: generated new tasks are ultimately curated by a human. It does not mean the approach is not interesting, but it might be good to emphasize a bit more this limitation, which is only mentioned on line l.261

### minor/typos

Be careful about citing journals/conferences and not arxiv, i.e. "Agentbench: Evaluating llms as agents" was published at ICLR 2024. Many arxiv citations in the current version

"(Rawles et al., 2024;Yang et al., 2023; Xie et al., 2024)." --> always cite from oldest to newest

l.162 "progressive" --> progressively

l257 "Detailed prompts are provided in the Appendix § A.3." --> Appendix A.3 is empty of text, although I managed to find the figures. Make sure to reference and briefly discuss each figure in the appendix text.0

### Questions
See weaknesses and the question about Digi-RL.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposed WebRL, an online RL framework to train LLM-based web agents. It applies a curriculum learning for agents’ continual improvement with a trained outcome reward model. It applies a KL divergence to prevent the actor from deviating too much from the previous policy and a replay buffer to prevent catastrophic forgetting. Empirical studies show that WebRL outperformed baseline methods on WebArena-Lite benchmark and also has the ability to scale up.

### Strengths
1. WebRL is an online RL framework, which greatly saves the need for dataset preparation in SFT.
2. WebRL outperformed baseline methods on WebArena-Lite benchmark and also has the ability to scale up.

### Weaknesses
1. The authors claimed that WebRL is a self-evolving framework, mainly due to its curriculum learning module. However, the generated instructions need to be checked manually to eliminate unreasonable or impossible instructions. This manual check greatly weakens the term, self-evolving, which is one of the key contributions in this paper. It is also unknown to what extent this manual check impacts the overall training process.

2. The experimental results are not conducted fairly. All the RL-based methods, except for WebRL are only trained on the generated 500 instructions in the first phase, whereas WebRL is trained iteratively on multiple phases. Training curves (steps VS success rate) and error bars are also not provided in the paper. The RL-based methods need to report the results with several seeds.

3. The ablation study is not sufficient. In lines 342-346, the authors contribute the limitation of DigiRL to the lack of self-evolving curriculum learning, however, in the ablation study, the authors did not ablate the curriculum learning.

4. Limited training details are reported in the paper and appendix, such as the hyperparameter for the experiments, observation and action space, how to train the ORM, how to use the replay buffer, etc. I am highly concerned with the reproducibility of this work.

5. The writing needs improving, which is confusing and difficult to understand, especially in the introduction of ORM and curriculum learning, where curriculum learning should be introduced first in the second section. Due to the lack of examples, it is difficult to understand the difference of the generated instruction and the original tasks in the benchmark and the necessity of the ORM model.

6. A number of RL for LLMs works are not mentioned in the related works, which are not limited to GLAM[1], TWOSOME[2], RL4VLM[3] and ArCHer[4].

### Questions
1. What is the performance of WebRL without curriculum learning and DigiRL with curriculum learning?
2. In lines 77-79 “those in WebArena are typically of long horizons, with oracle solutions averaging 10 steps. This characteristic introduces substantial sparsity in the available signals during online exploration”. How can 10-step-long tasks be counted as long horizons in decision-making tasks? 
3. What is the clear definition of phase? 
4. Could you provide more analysis and insight into how RL mitigates the issue in lines 365-366?
5. Why discount factor is not applied in the value function?
6. In Lines 243-244, how to calculate the perplexity of the action?
7. In lines 304-305, where do the data come from?
8. What is the advantage of the loss shown in equation (6) compared to the standard loss function with KL?
9. How is the generalizbility of WebRL. Can the trained agent be deployed to other tasks or even to the real PC?

### Soundness
2

### Presentation
1

### Contribution
2
