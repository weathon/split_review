# Large Legislative Models: Towards Efficient AI Policymaking in Economic Simulations

- Decision: Reject
- Scores: 5, 5, 6, 3

## Abstract
The improvement of economic policymaking presents an opportunity for broad societal benefit, a notion that has inspired research towards AI-driven policymaking tools. AI policymaking holds the potential to surpass human performance through the ability to process data quickly at scale. However, existing RL-based methods exhibit sample inefficiency, and are further limited by an inability to flexibly incorporate nuanced information into their decision-making processes. Thus, we propose a novel method in which we instead utilize pre-trained Large Language Models (LLMs), as sample-efficient policymakers in socially complex multi-agent reinforcement learning (MARL) scenarios. We demonstrate significant efficiency gains, outperforming existing methods across three environments.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes a prompting-based agent framework for Economic policy-making problems. The paper first illustrates the over-complicated problems with previous RL-based methods. To address this issue, the authors leverage few-shot prompting and derive an LLM-based policy-making agent. Empirical evaluations demonstrate that their LLM-based method outperforms traditional RL-based baselines across various multi-agent environments.

### Strengths
Strengths:
1. The overall writing is clear to follow.
2. The paper offers a comprehensive overview of the background, previous methods, and proposed methods.
3. The paper validates the performance in 3 environments and the ablation study seems to be sufficient.

### Weaknesses
1.Prompting-based agents and techniques have been applied in a lot of fields (beyond economics) and the proposed method seems to be not that novel. Techniques like memory, reflection, are proposed and used in many other agent frameworks.

2. A lot of related work and citations are missing. For instance, the proposed algorithm seems to refer to ReACT [1], Reflextion [2], AutoGPT [3] and more agent frameworks. 

3. The writing logic is a bit messy, especially for section 3. I understand that section 3 is for analyzing the overcomplicating issue of previous methods. But it seems not that related to section 4 and cannot help strengthen your major proposed algorithm. I’d suggest try to move the main discussion into the appendix to improve writing fluency.

4. I am not an expert in this domain, but from the prompt example shown in the appendix, the problem the principle agent tries to solve has nothing to do with the multi-agent setting. It is, in fact, a bandit optimization (so just one-step decision-making by keeping all other follower agents as part of the environment). Also, these three environment settings look very similar. These two issues largely weaken their effectiveness in showing the algorithm’s performance on complex and general problems.

### Questions
1.Is there any other LLM-based baseline you can include to strengthen your comparison?
2.The MetaGrad baseline seems weird? Why it cannot improve in all environments.
3.The experimental results seem to be repetitive? Table 1 and Figure 1 seem to be the same results?

### Soundness
3

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
3

### Summary
This paper presents a method for economic policymaking that utilizes LLMs to overcome the sample inefficiencies found in current RL models. By incorporating LLMs into MALR environments, the authors showcase improvements in efficiency compared to existing RL-based models, such as AI Economist. The approach integrates contextual and historical data to optimize output in three test environments, achieving faster convergence and comparable or better performance than other methods.

### Strengths
1. The paper clearly outlines its motivation, highlighting that current SOTA methods face sample inefficiencies. This has led to the exploration of using LLM agents for policymaking.

2. The paper is well-structured, with a clear articulation of its methods and contributions.

3. Extensive experiments across multiple environments effectively validate the proposed approach with thorough and convincing results.

### Weaknesses
1. While using a Stackelberg game model is reasonable and straightforward for this policy-making problem, the observation that RL-based methods are unaffected by state observations raises questions about the environment’s simplicity; this suggests the need either for testing in environments where observations impact performance or for confirming that this lack of impact holds consistently across all environments.

2. The paper does not clarify whether LLM success arises from pre-trained strategies or from actual understanding of the policy-making environment.

3. LLMs may benefit from pre-training on diverse datasets, which could give them an edge over RL methods that train from scratch, raising questions about the fairness of comparisons.

4. While LLMs show rapid convergence, they often do not match the higher final performance achieved by RL-based methods in certain environments.

### Questions
1. One of this paper's major findings is that state observations don't affect performance in current SOTA methods, which is surprising and interesting; however, if observations are irrelevant to performance, why model the problem as a Stackelberg game which inherently assumes strategic interaction based on observation? This suggests the current policy-making might be reducible to a simpler fitting problem rather than requiring a complex game-theoretic framework, especially in relatively simple environments.

2. The paper's approach uses a simple LLM implementation yet achieves impressive results with rapid convergence. Whether LLMs have already acquired optimal policy-making strategies during pre-training or if they understand Stackelberg equilibrium concepts from the prompt. 

3. As the LLM approaches benefit from pre-training on diverse data, while the RL methods start from scratch (especially for the Meta-Griednat method, which needs huge exploration during the training). It is unclear whether LLM’s performance truly represents a better decision-making approach or reflects its pre-training advantage.

4. The experimental results show that while RL-based methods require significantly more time to converge, they ultimately achieve better final performance than LLM-based approaches in several environments (particularly noticeable in the clean-up environment). Does this suggest that RL-based methods, despite their slower convergence, have a higher performance ceiling than non-finetuned LLM approaches? Or, the LLM-based method may be limited in its ability to find truly optimal policies without fine-tuning.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper asks pre-trained LLMs to suggest a policy - for example to put incentives for cleaning up the river in the clean up environment - in such a way that individually trained RL agents trained on those tasks achieve high social welfare. The LLM can also observe the feedback of its policy and modify it in an iterative manner. For example, if the incentive to clean the river and abstain from harvesting apples is not enough, the LLM may increase the incentive in the next rounds. The authors find that while the LLM has a bias to do changes slightly and therefore slightly underperforms previous RL based methods, it can do so by observing much fewer samples from the environment, therefore being more sample efficient.

### Strengths
It is always a good idea to try the simple solutions on a benchmark and show how they perform. I think this is the main strength of the paper. What if instead of the complex RL mechanisms, we just ask a pre-trained instruct-tuned LLM to solve the task. If this outperforms all other methods, it is a valuable contribution to that field. I think that is the main strength of the paper.

In detail, this paper has three messages : 1) If we remove the conditioning of the policy on the state, other methods performance remains the same, suggesting the complexity was not needed at the first place 2) Asking an LLM to suggest the policy, and then refine the policy, works quite well and also does need much fewer samples 3) Asking the LLM to do so, has its drawbacks, for example, the LLM tries to suggest a conservative incentive even when a stronger one is needed. 

The paper is original in the sense that I have not seen a paper using LLMs to suggest policies before. It is also clearly written. However, the significance of the main message being the sample efficiency of the LLMs I think is a bit low which I will elaborate on in the weakness section. 

I think the main important consequence of the paper in the field is that we need much better benchmarks when discussing solving social dilemmas by LLMs. The current environments are toy-ish because we don't have the correct RL tools to solve even them. However, this paper shows that if we want to explore social dilemmas using LLMs as policy-makers, which is a valid approach, we don't have the benchmarks which their difficulty actually matches the strengths of these neural networks. We need environments which are large, hard to describe in short sentences, and need much more iterations to get the policy right.

### Weaknesses
The paper argues that using pre-trained LLMs is sample efficient. I have two main concerns about this statement. 

1) LLMs are not that sample efficient:
The paper argues that using pre-trained instruction-tuned LLMs is more sample efficient. But, I think we should also take into account all the pre-training and data the feeds into these models. Taking them into account, I don’t think using LLMs is sample efficient.  

2) LLMs have seen these environments possibly:
I am not sure of these. But for example, by asking chatgpt 4o at Nov 3rd of 2024 I can confirm that by just asking “do you know the RL clean up environment and what a good strategy would look like without search?” it can reiterate what the clean up environment is. Therefore, it is possible that they already know what the dilemma of the environment is and how to solve it in the sense that it is discussed in their pre-training data. I don’t know if this is what is actually wanted, because it is okay for example to look at how other countries fixed their economies when trying to propose a policy to another country. But also, these environments are so toyish that knwoing what the dilemma is, is most of the answer. Therefore, it is not clear if doing the same to complex environments or unseen environments shows the same sample complexity. 

The other important problem is, we are using the LLM as the learning algorithm here in the sense that we will put all the environment details and actions and previous proposed policies in the context. I am wondering if this is a scalable approach? Especially, when environments get larger, and the require optimization iterations steps also grow a lot, I think two issues arise. First, the prompt gets very long. Second, we need much more iterations to optimize the proposed policy. 

Also, at the end, the best final policies are reached by RL methods and not the LLMs, suggesting that the LLMs are not very good at imitating a learning algorithm, although their first guesses are much more educated which I think given their massive pre-training data and possible exposure to these environments, makes a lot of sense. 

I proposed a marginally behind acceptance threshold because I think the focus of the writing of the paper, the sample efficiency of this approach, is not significant. I think if the paper was written as an analysis of what happens if we try to use LLMs to solve current benchmarks social dilemmas, its contribution would be much more clear. The paper would discuss the attempts, the limitations, etc.

### Questions
1- Should we take the huge data, instructions, compute and RL post-training that these models needed into account when assessing if they are sample efficient?

2- There is a possibility that some texts discussing the environments may be on internet suggesting what is an optimal approach especially in the papers written in the field. Is there any way to assess this?

3- What would be the scalability properties of the paper's paradigm? Is there a chance that it scales well to more complex settings?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes using large language models (LLMs) as policy makers. The authors argue that LLMs can address the challenge of processing large amounts of data quickly. They use a Stackelberg-Markov game to model the problem, where the principal plays against other players it influences. The authors use LLMs to model the principal. The core argument of the paper is that LLMs can offer a more sample-efficient solution to this problem.

### Strengths
1. The use of LLMs as economic policy generators is a novel and potentially more efficient approach compared to training agents from scratch.
2. The authors demonstrate their method can converge to effective policies with significantly fewer training iterations compared to baseline methods.
3. The paper leverages a well-defined formal framework (Stackelberg-Markov games) to analyze and compare the various policymaking methods.

### Weaknesses
1. The authors do not do any training or optimization process for the principal LLM. The LLM is indeed used to generate a policy, but there is no feedback loop to improve its choices based on the observed outcomes. The feedback is only used to change the game and the new observations this policy would see. The underlying assumption that an LLM can do this effectively is problematic, as LLMs are not trained for this, and therefore require additional fine-tuning or sampling methods. One example would be to use a Best-of-N (BoN) strategy, where several policy options are generated and the best one is selected based on some verifier. Here the authors would not be required to fine-tune an LLM, but they can still build a selector policy to choose from a discrete action space of candidates, and thereby improve the policy maker agent. This is the weakest point of the paper.
2. The paper doesn't explore the possible biases of the LLM in the context of the chosen environments. A robust evaluation would require testing how the LLM's biases affect the policies generated and, potentially, creating more diverse and sophisticated environments to test generalizability.
3. Overall presentation could be greatly improved. The authors describe related work and other algorithms throughout, and there is an underlying assumption that these methods are known to the reader. Many of the practical implementation details of the LLM-based approach are unclear. There is a lack of clarity regarding prompt engineering, parameter selection, and the specific LLM prompts used makes it difficult to evaluate the proposed method.  
The Algorithm 1 block shows the general methodology that is used in previous work. Are the authors using that same methodology but only replacing the policy maker with an LLM? If that is the case, the authors should put more focus and emphasis on the LLM in the paper. There should be much more detail about how the LLM is being prompted, and potentially improved (see my first point above).

### Questions
See above

### Soundness
2

### Presentation
1

### Contribution
2
