# Resolving Complex Social Dilemmas by Aligning Preferences with Counterfactual Regret

- Decision: Reject
- Avg Score: 4.33
- Scores: 5, 5, 3

## Abstract
Social dilemmas are situations where gains from cooperation are possible but misaligned incentives make it hard to find and stabilize prosocial joint behavior. In such situations selfish behaviors may harm the social good. In spatiotemporally complex social dilemmas, the barriers to cooperation that emerge from misaligned incentives interact with obstacles that stem from spatiotemporal complexity. In this paper, we propose a multi-agent reinforcement learning algorithm which aims to find cooperative resolutions for such complex social dilemmas. Agents maximize their own interests while also helping others, regardless of the actions their co-players take. This approach disentangles the causes of selfish reward from the causes of prosocial reward. Empirically, our method outperforms multiple baseline methods in several complex social dilemma environments.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper focuses on the challenge of aligning individual desires with group objectives in situations known as Sequential Social Dilemmas (SSDs). Current research efforts to promote cooperation in SSDs are discussed, highlighting approaches that model agent interactions or incentivize altruistic behavior. 

The authors propose a reinforcement learning algorithm that leverages counterfactual regret and a causal model to better align individual incentives with group goals. This approach aims to minimize biases in reward estimation by understanding the true causes of individual rewards and considering the impact of each agent's actions on others. The key contributions of this work include the development of a generative causal model for reward processes and the introduction of counterfactual regret to enhance cooperation.

### Strengths
1. The paper effectively highlights the limitations of previous methods in capturing the true causal relationships between agents' actions and their outcomes. By recognizing that earlier approaches often result in ineffective cooperation strategies due to delayed or spurious correlations, the authors provide a clear rationale for their research. It is reasonable to study the entanglement of agents' policies and the resulting biases in reward estimation.

The reviewer finds this argument convincing as the reviewer believes that the difficulty of SSDs lie in that the rewards are delayed and the causes of these rewards are difficult to analyses.

2. The introduction of counterfactual regret as a mechanism to align individual incentives with group objectives is a, as far as the reviewer is concerned, interesting contribution. By calculating the difference between the maximum counterfactual rewards and the actual rewards of other agents, the algorithm encourages agents to consider the broader impact of their actions.


3. The paper is well-organized, with a logical flow that makes complex concepts accessible.

### Weaknesses
1. By employing a causal model to guide counterfactual reasoning, the proposed method target at ensuring that counterfactual rewards are grounded in realistic and causally valid scenarios. This approach aims to minimize the risk of learning spurious relationships, thereby fostering genuine cooperative behavior among agents. 

However, the proposed framework appears to lack comprehensive theoretical support. Proposition 1 does not fully—and understandably, given its complexity—rigorously substantiate the entire workflow of the proposed method.

2. As the paper is predominantly empirical, the authors should consider explicitly presenting the causal structures learned by their proposed method. Providing a clear depiction of these structures would strengthen the empirical findings and offer deeper insights into how the model operates.

3. The selection of baseline methods is currently insufficient. As the introduction references numerous related works, the paper would benefit from additional experiments to more effectively support the authors' arguments. 

Incorporating a broader range of baselines would provide a more comprehensive evaluation of the proposed method's performance.

### Questions
Sea the previous section.

### Soundness
2

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
The paper focuses on sequential social dilemmas.  It designs a causal model to predict counterfactual individual rewards and uses counterfactual regret as an intrinsic reward to encourage prosocial behaviors. Experiments on several SSD scenarios show that the proposed method achieves higher team rewards than the baselines.

### Strengths
1. This paper focuses on the sequential social dilemmas that are of interest to the community. 
2. The authors design a casual model to capture the generation process of individual rewards in SSDs.
3. This paper provides some theoretical analysis of the process of individual reward generation.

### Weaknesses
1. Some symbols appear suddenly without explanation, making them difficult to read. The sentence “To interpret the phrase: had collective actions…” seems odd and shows clear signs of AI-generated text. The entire second paragraph of Section 3 is quite confusing.
2. The paper mentions the causal model and generative model, but they seem to refer to the same model. What is the network structure of the causal model? Is the Dynamic Bayesian Network considered part of the causal model?
3. The baseline for comparison is somewhat outdated. 
4. The figures in the ABLATION RESULTS are difficult to read. I recommend using more distinct colors to differentiate the curves.

### Questions
1. Could you give a more detailed analysis of how counterfactual regret promotes cooperation?
2. How about comparing it with the auto-aligning multi-agent incentives (Kwon et al., 2023) method mentioned in related work?
3. Why does SVO exhibit significant fluctuations in Common_Harvest_7 and Cleanup_5?

### Soundness
3

### Presentation
2

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
The paper proposes an incentivization method for cooperation in sequential social dilemmas (SSDs) using counterfactual reasoning about the rewards of other agents. A generative model is learned to capture the reward dynamics to calculate a counterfactual regret as an intrinsic reward for prosocial learning. The proposed approach is evaluated in a variety of benchmark domains, such as Coin, Cleanup, Level-Based Foraging, and Harvest, and compared with a selection of prior methods.

### Strengths
The paper addresses a relevant and popular topic regarding cooperation incentivization in social dilemmas.

It is well-written and easy to understand.

### Weaknesses
 **Soundness**
- The paper explicitly assumes a partially observable Markov game. However, given the proposed method, there is no true partial observability: Joint observations, actions, and even rewards are observable to all agents, so there is practically no privacy and all agents can fully observe each other. While they are required for the generative model, I am uncertain about potential applications where such an assumption (everything is observable) would hold.
- The observations are assumed to be Markovian since the policies condition on them directly (prior literature on POMDPs or Dec-POMDPs always consider the history of past actions and observations to mitigate this)
- All agents need to have the same "currency" of rewards. Otherwise, some agents with a significantly larger reward scale could skew the regret calculation.

**Experiments**
- Despite promoting causal inference as a main tool for the proposed approach, the paper does not compare with Social Influence, which is also based on causal inference (and cited in the paper). The paper also does not compare with alternative incentivization approaches like Gifting. Both Social Influence and Gifting achieve higher collective rewards in Harvest (over 800) than the performance reported in the paper. Social Influence also achieves higher collective rewards in Cleanup (at least 200) which is higher than the maximum performance reported in the paper.
- It is surprising that the Selfish baseline performs rather well in Coin despite performing poorly in prior works [1,2], while other approaches like SVO perform poorly despite being designed to incentivize cooperation.
- While the regret evaluations include alpha-values >= 1 (indicating selflessness), it would be interesting to see how the agents behaved if the alpha was set to something < 1, i.e., how selfish can the proposed approach be without compromising overall cooperation?
- All benchmark domains have alternative cooperation measures that can give more insight into the behavior of the agents, e.g., matching coin rate in Coin, peace/sustainability in Harvest, etc., which are not reported in the paper or appendix. I suggest to provide such plots in the main paper to strengthen the contribution and claims.

**Typos**
- "In SSDs, naively using individual for each agent" -> "reward" is missing
- "theorical" -> "theoretical"
- "rewards(For brevity" -> rewards (For brevity
- "Baselinses" -> "Baselines"

### Questions
1. What would be examples where full observability of all agents, i.e., their observations, actions, and rewards, is a realistic assumption?
2. How would the approach behave if, e.g., one agent in Coin would get a reward scaled by a constant factor (let's say 10), in contrast to other agents? What would need to be done to avoid bias toward that particular agent?

### Soundness
2

### Presentation
2

### Contribution
2
