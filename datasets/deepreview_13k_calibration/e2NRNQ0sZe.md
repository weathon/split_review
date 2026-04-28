# Efficient Reinforcement Learning with Large Language Model Priors

- Decision: Accept
- Avg Score: 6.25
- Scores: 5, 8, 6, 6

## Abstract
In sequential decision-making (SDM) tasks, methods like reinforcement learning (RL) and heuristic search have made notable advances in specific cases. However, they often require extensive exploration and face challenges in generalizing across diverse environments due to their limited grasp of the underlying decision dynamics. In contrast, large language models (LLMs) have recently emerged as powerful general-purpose tools, due to their capacity to maintain vast amounts of domain-specific knowledge. To harness this rich prior knowledge for efficiently solving complex SDM tasks, we propose treating LLMs as prior action distributions and integrating them into RL frameworks through Bayesian inference methods, making use of variational inference and direct posterior sampling. The proposed approaches facilitate the seamless incorporation of fixed LLM priors into both policy-based and value-based RL frameworks. Our experiments show that incorporating LLM-based action priors significantly reduces exploration and optimization complexity, substantially improving sample efficiency compared to traditional RL techniques, e.g., using LLM priors decreases the number of required samples by over 90\% in offline learning scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper considers treating LLMs as prior action distributions and integrating them into RL frameworks. Specifically, authors proposes to use LLM for exploration,  Q target calculation and imposing conservatism. Experiments on the ALFWorld and Overcooked environments illustrates the effectiveness of the proposed framework.

### Strengths
1. This paper is clearly written and easy to follow.
2. The considered "incorporating the background knowledge of LLM into RL" is an interesting topic.

### Weaknesses
1. There are no convergence guarantees of sampling using LLM as prior for Exploration and Q-function update. Moreover, there is no guarantee that learning the Q-function as shown in Equation (7) will give us a conservative Q-function.
2. If the LLM can not provide a good prior, constraining the learned policy as shown in Equation (8) will result in sub-optimal policies.
3. The RL process has to query the LLM each time we update the policy, which is time-consuming and computation-consuming.

### Questions
1. The experiments are only conducted on simple environments with discrete action spaces. What if continuous action space (e.g., offline RL on the D4RL benchmark)?

### Soundness
2

### Presentation
3

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
In this work, the authors propose idea of using large language models (LLMs) for providing prior information about execution of a task, which simplifies exploration in reinforcement learning (RL) and improves sample efficiency. The core idea is to treat LLMs as prior distribution over actions and then apply variational inference in conjunction with posterior sampling. The authors demonstrate this technique on both value-based and policy-based approaches. In value-based implementation, a subset of the action space is chosen for Q-learning instead of using entire action space. This subset selection is done using LLM prior. Similarly, in the policy-based implementation, a KL-penalty is introduced with respect to the prior LLM action distribution, but implemented differently from regular KL penalty in RL from human feedback (RLHF), by posterior sampling of multiple candidate actions. The experiments are conducted on text-based RL environments with large action spaces and multi-step horizon (note this is crucial for demonstrating the difference against RLHF techniques). Value-based baselines include DQN for online learning and CQL for offline learning. For policy-based baseline, PPO algorithm is compared against.

The results demonstrate the superiority of the approach in (1) overall returns, (2) generalizing beyond seen tasks, (3) sample efficiency.

### Strengths
The paper is written very clearly with appropriate figures, well-formatted equations and more importantly lucid logical flow. The contributions of the paper are specified along with particular sections corresponding to individual contribution. Preliminaries provide enough details and are not overexplained. 

The core idea of the paper is pretty neat -- LLMs are trained on large amount of data and they have knowledge about tasks if not fine-grained controllability; this knowledge is useful to guide an RL training. 

I like how the value-based implementation is designed -- sampling a set of actions using LLM prior, taking Q estimates, sampling actions using their Q estimates. The method is well grounded in the theory where direct posterior sampling is shown to be proportional to LLM prior multiplied with soft-Q distribution. The idea being simple, can be plugged with both online and offline Q-learning approaches.

The versatility of the idea is shown by applying it to policy-based RL. The LLM prior guided learning takes form similar to KL-regularized RL, hence modifying PPO in a straightforward way would lead to easy access to prior knowledge. However, I do I have some contentions around the novelty of this part which is discussed in weakness section.


The choice of the experimental setup is also very apt. The environments are chosen so that LLMs can provide textual action descriptions which then can be executed through text to action conversion in the environment's processing.

### Weaknesses
Practicality of value based approaches: Although the value-based direct posterior sampling technique described in the paper is logically sound, I wonder about its practicality. Mainly, value-based approaches when applied to combinatorically large action spaces like text generation is practically infeasible. Hence, the paper's proposed method might be hard to apply beyond toy textual environments. Noticeably, these environments are designed to accept actions in a particular format or use rigorous action decoding, etc. to deal with the combinatoric complexity. Such environments are rare in reality.

Problems with choice of prior inducing LLMs: Two LLMs might produce semantically same action but different text. I am curious to know whether the Q-learning based approaches would assign similar values to both. In general, I feel that prior inducing LLM and its compatibility with the environment's action decoding plays major role when they are used to train RL policies in text-based sequential decision making.

Novelty of the additional KL penalty in policy-based RL: ELBO-based RL approaches [1, 2] have been already established in the RL literature. The additional KL-penalty proposed in the current paper is based on the same. In single step decision making, the KL-penalty on an LLM prior would be exactly same as KL-penalty used along with supervised fine-tuned (SFT) policy. Thus, in that setting, the paper's technique lacks novelty. Now, coming to the multi-step decision making, unless the proposed direct posterior sampling is also applied on top of PPO, additional KL-penalty is equivalent to using a good enough prior policy (e.g. behavior cloned policy). Therefore, the novelty of the paper is limited in policy-based RL.

Combined together,  I find that paper provides great insights into a direct posterior sampling paradigm for using prior knowledge present in the LLMs, but the approach might have limited applicability beyond hand-designed textual environments, its applicability is limited by limitations of value-based approaches, and its novelty in policy-based RL is not significant.

### Questions
Questions and Suggestions:

- Should the proportionality sign on line 147 be equal to? I understand the sentence is correct in its current form.

- The $p$ is overloaded on lines 112-113, especially, please change the "$p_{LLM}$ as the action prior $p$" sentence where the latter $p$ is said to be not confused with $p$ used for probability of start state or action given a state in the definition of probability of trajectory.

- I am not sure by what is meant by "Denote that the above …" in Proposition 1. Please rewrite this for clarification.

- Line 215 - "reply buffer" should be changed to "replay buffer" 

- Is the gamma in equation 8 the same as the discount factor?

- Line 323 - "avoiding full into holes". Please rectify this.

### Soundness
4

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
Authors present a new way to train LLM-based agents in interactive sequential environments. Their approach is based on leveraging a potentially large frozen LLM to generate action subsets for encountered states. The action subset is then used to simplify the RL finetuning of a smaller LLM. Their approach can be adapted to value-based (giving a subset of actions for the LLM Q-network) and policy-based scenarios (constraining the LLM policy with a KL-div loss over the subset of actions). Authors showcase how their approach outperforms baselines in TextWorld and Overcooked, both in online and offline learning settings.

### Strengths
This paper tackles a very important topic: how to leverage LLMs into sequential decision-making tasks incorporating language.
I enjoyed reading it.
Performance improvements over considered baselines are impressive.

### Weaknesses
### Value-based version

I am having trouble understanding how useful the value-based formulation is. What I mean is that, from my understanding, at inference time you need both the frozen LLM and the trained Q-network (which is a smaller LLM). This makes the approach quite expensive regarding memory. Regarding inference, it is also costly: the frozen LLM must provide k outputs before being able to use the Q-network LLM, for each step in the environment.
A good comparative study here to motivate this approach could be to have a baseline which discards the frozen-LLM. What happens in this scenario ? Is it what you call the DQN baseline ? Here, it would be interesting to see what happens if you use a larger LLM during training (something which induces a memory burden comparable to using a frozen LLM + a smaller trained Q-net LLM).

### Comparative study with GFlan from carta et al

The only baseline considered from the litterature is GFlan from carta et al. While I am not expert enough to assess whether this is sufficient, I have concerns about this comparative study.
In carta et al, GFlan is evaluated on a text-based version of the BabyAI gridworld environment:

Why not featuring this environment in the study ?

Any intuitions on why GFlan is failing completely in ALFWorld (TextWorld) while it does maintain some performances in Overcooked ?




### Clarity

While the paper is mostly clear, I had trouble understanding the exact training and inference pipeline. The paper could benefit an update of figure 1 (along with providing the policy-based version of figure 1 somewhere).The right side of Figure 1 could be improved: in the current version, it is hard to visually understand that the Q function is used to weight each input actions and that these weights are used for proportional sampling of the next action. Also in figure 1 it is hard to understand that there are two pre-trained LLMs being used, one frozen generating an action subset, and a smaller one trained and used as a critic. I only understood that there was two pretrained LLMs being used in the DQN-Prior baseline at line 395 "... by combining the Q-function, trained with Qwen-1.5 7B". I would suggest making it clear early on.

l.97-99 "we first generate a free-form output from the LLM, for example, a 7B LLM, which is then mapped to an executable action through a simple rule-based projection." 
--> I would recommend moving at least part of what is discussed in the appendix into the main body of the paper, to be clearer about this. 
Related to this: I only understood that you repeat this output-to-action mapping multiple times at line 166-167. It would be clearer to mention it sooner in the paper.


### Minor / Typos

There are 3 acronym definitions in the abstract, which is a lot. Consider reducing this number, e.g. dropping SDM which is used only once.

l31. "human-AI dialogue (McTear, 2022; Li et al., 2019)," --> make sure to sort citations in ascending order wrt year. This error appears multiple times.

l. 232 --> (Snell et al.) missing year in citation.
 
l.104 "by (Levine, 2018)" --> use \cite not \citep when directly mentioning the citation in the sentence.

l.304 "can be found in the Appendix" -->  refer to the appropriate appendix section(s) rather than a general reference

l.323 "while avoiding full" --> falling

l.352 "Behavior Clone(BC)." --> Behavioral Cloning ?

Results-related figures could be moved closer to the result analysis in section 4.3 to simplify reading

l.404 "k = 1 indicates the performance of the LLM on its own, without involving the Q-function" 
--> Why calling this scenario k=1 and not k=0 ? you could theoretically use your frozen LLM to create a single action subset.

### Questions
l.286 "We plot the rewards averaged over the final third of the training processes for trainable baselines" --> Evaluation of a model performance is not performed by conducting periodic performance measurements over a test set of tasks ? Could you elaborate on how performance is measured ?

In your policy-based version, which you present in section 3.3 as an extension of the work of Carta et al., 2023, I am not sure to understand what is trained is what is fixed. Are you, like in Carta et al, training all parameters of the LLM ? What is being trained by your modified PPO loss ? Would be good to have the policy-based version of figure 1 somewhere. My understanding after reading section 4.2 is that you have a large fixed pretrained model used to compute action priors, and you train another smaller Flan-T5 as the policy.

In your offline learning experiments, by looking at table 1 it looks like you are applying a vanilla DQN to offline datasets. It comes with the risk of overestimating values of actions that are not supported by the dataset. Would it make more sense to use value-based methods designed for offline learning, e.g. Implicit Q Learning from Kostrikov et al ?

In your offline learning results, I see that CQL underperforms wrt Behavioral Cloning. This is unusual: any ideas on why ?




Given the aforementioned questions and potential limitations of this paper, I will go for a weak reject, and look forward to the discussion to update my score.

### Soundness
3

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes an approach to leverage LLM priors for RL, both in the online and offline settings.
The setting is restricted to text-based observations. Specifically, they estimate a prior p(a|s) by sampling K actions from the LLM conditioned on the state, and use these to either restrict the Q-values to the actions with non-zero probability (for online or offline Q-learning based methods), or to enforce a KL penalty with respect to the policy’s distribution over actions. They evaluate on several text-based environments and show improvements in terms of sample efficiency over vanilla RL. Overall, the paper does a decent job of illustrating the benefits of the method within its scope, but the scope itself is quite limited (in terms of broad applicability and scalability - more on this below). Also, there are a number of alternate methods for incorporating LLM priors into RL systems, that are not discussed or compared to.

=====
Update after rebuttal: the authors have added several additional experiments which partially address the initial limitations I discussed. Although I still think the environments are on the simple side, and the method in its current form is difficult to scale to high-throughput settings, the results are convincing enough in demonstrating the approach's merits and give hints of wider applicability to meet the bar for acceptance.

### Strengths
- the method is simple and makes intuitive sense. Its benefits are clearly demonstrated, although in fairly simple text-based environments. Although other works have proposed ways to incorporate LLM priors into RL systems, to my knowledge this particular approach is new. 
- the paper is overall clearly written and easy to understand. I have a few suggestions below, but they are relatively minor.

### Weaknesses
 - the method is limited to settings where the observation consists of text, which is a big limitation. One could imagine workarounds to apply this to images, where one first uses a pretrained captioning model to extract textual captions and then feed these to the LLM. However, it’s not clear if this would give enough granularity to produce a reasonable action prior and this would need to be checked experimentally. Specifically, the granularity of the textual representation may not capture the nuances present in the raw pixel data, potentially leading to a suboptimal action prior. For example, in a navigation task, a textual description might not capture the precise location of obstacles or the subtle differences in visual cues that are critical for successful navigation. The reliance on a captioning model also introduces an additional layer of complexity and potential error, as the quality of the action prior is now dependent on the accuracy of the caption.
- the method, as I understand it, will have difficulty scaling to high-throughput RL settings because it requires a call to the LLM for each observation encountered by the agent (which is computationally expensive). This also limits its applicability to small tasks or offline settings where the LLM outputs can be precomputed in parallel and cached. Are there any ways to address this? For example, could you distill the LLM action prior into a lightweight model and use this instead? The computational cost of querying the LLM for every step in an online RL setting is a significant bottleneck. Even with caching, the initial overhead of generating the action priors for unseen states would still be substantial. Furthermore, the latency introduced by LLM queries could severely impact the real-time performance of the agent, making it unsuitable for applications that require fast decision-making. The authors should explore methods to reduce the computational burden, such as distilling the LLM's knowledge into a smaller, more efficient model.
- there are other ways to incorporate LLM priors into RL systems, namely through the reward function rather than the action distribution. See for example the references below [1, 2, 3, 4] (this is not a complete list). It is currently unclear what the pros/cons of the proposed method are compared to this other family of approaches. It would be helpful to include at least one method from this family as a comparison in the experiments. Also, these are not discussed in the related work section. Specifically, methods that use LLMs to generate reward functions can provide a more direct way to guide the agent's learning process by shaping the reward landscape. It's unclear whether restricting the action space is more or less effective than shaping the reward function, and a direct comparison would be highly beneficial. The authors should also discuss the potential limitations of using LLMs for reward shaping, such as the possibility of introducing biases or inaccuracies in the reward signal.

### Questions
If the authors can address any number of the points raised in the Weaknesses section, I would be willing to raise my score accordingly. I also have a few minor comments below:

- In Section 4.1, it would be helpful to give some more detail on the environments you use. The current descriptions are quite high level and not everyone may be familiar with these environments or have intuitions about them. Maybe include a figure with example observations/actions for each one - you still have half a page under the page limit so there should be space. 
- Some of the references are missing dates, for example (Snell et al), line 232. 
- This is a bit of a nitpick, but in Figure 1, is there a reason the OpenAI logo is on the LLM box? My understanding is that this paper does not use OpenAI’s LLMs, and instead uses open models (Qwen and Llama). I don’t think an institutional logo is necessary, but if you do want to include one, it would seem more fair to give credit to those that made the models that you use available.

### Soundness
3

### Presentation
3

### Contribution
3
