# Agent Q: Advanced Reasoning and Learning for Autonomous AI Agents

- Decision: Reject
- Avg Score: 5.60
- Scores: 5, 5, 5, 5, 8

## Abstract
Large Language Models (LLMs) have shown promising capabilities in natural language tasks requiring complex reasoning. However, they still struggle with generalizing to multi-step reasoning tasks in long-horizon interactive environments like web navigation. This is primarily due to their imitation-based pre-training on datasets which do not include the behaviors needed for interactive decision-making. Recent works have tried to overcome this challenge by supervised-fine tuning on curated expert demonstrations in such environments, however such behavior cloning objectives, suffer from compounding errors and yield sub-optimal policies due to limited exploration data. To address these challenges we build a Monte-Carlo Tree Search approach on top of an LLM Agent, which serves as a proposal distribution. To guide the search we utilize the same model as a zero-shot critic evaluator at each node branch in a form of AI self-critique. While this approach address prior issues with web agents, it is still expensive at inference time, hence we further refine the base agent on the MCTS traces using an off-policy variant of the Direct Preference Optimization (DPO) algorithm at the node level. Our method allows LLM agents to learn effectively from aggregate datasets of both successful and unsuccessful trajectories, improving their generalization in multi-step reasoning tasks. We validate our approach in the WebShop environment, where an agent navigates a simulated shopping website. Starting with an LLM with an SFT-based pre-training, our iterative fine-tuning boost zero-shot performance by \textbf{50\%} relatively to the baseline. In our long-horizon real world booking experiments, we boost LLaMa-3 zero-shot performance from \textbf{18.6\% to 81.7\%} success rate after a single day of data collection outperforming GPT-4.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes Agent Q, an online fine-tuning framework for enhancing reasoning capabilities in autonomous AI agents for web navigation tasks. Agent Q combines DPO, MCTS, and process supervision to improve the agent's performance. The experimental results show that Agent Q outperforms the baselines on two benchmark tasks, highlighting its potential for real-world applications.

### Strengths
- The paper proposes a method for online fine-tuning a web navigation agent and the empirical results show that the proposed method outperforms the baseline methods.
- The paper evaluates Agent Q on both simulated and real-world tasks, demonstrating its effectiveness in various scenarios.

### Weaknesses
 - The idea is not novel enough since Agent Q uses a combination of DPO, MCTS, and process supervision for web navigation task.
- Lack of experimental details, such as hyperparameters, and the significance of the results. Also, the code is not provided.
- Lack of ablation studies to analyze the effects of number of iterations in Agent Q.

Format and writing issues:

- The paper cites papers using wrong LaTeX commands. For example, "(Zhou et al., 2024c) has shown success
formulating the RL problem at a step level" should be changed into "Zhou et al. (2024c) has shown success
formulating the RL problem at a step level" by using the `\citet` command. "Classical RLHF has used policy gradient type of algorithms, such as PPO Schulman et al. (2017), ... " should be changed into "Classical RLHF has used policy gradient type of algorithms, such as PPO (Schulman et al., 2017), ... " by using the `\citep` command. I strongly recommend the authors to use the correct LaTeX commands for citations.
- "will produce actions $\mathbf{a}_t \sim \pi \mathbf{a} | \mathbf{h}_t)$" should be "will produce actions $\mathbf{a}_t \sim \pi(\mathbf{a} | \mathbf{h}_t)$". The same issue in Eq. (2).
- Inconsistent equation referencing: In Algorithm 1, the equation is referenced as (9) and Eq. (4), but in the text, it is referenced as Eq. 2. The same issue for figures. There are "Figure 1" and "Fig. 1" in the text. I recommend the authors to check the consistency of the referencing.
- Replicated references in the paper, such as "Appagent: Multimodal agents as smartphone users", "Chain of preference optimization: Improving chain-of-thought reasoning in llms".
- "In this environment, training with outcome-supervision only DPO further improves performance by 4.6% to 71.8% but significantly under-performs the full Agent Q pipeline which achieves a zero-shot success rate of 81.7%" does not have a period at the end of the sentence. I recommend the authors to check the punctuation of the sentences in the paper.

### Questions
Besides the weaknesses above, further questions are as follows:

- "RFT and DPO over xLAM-v0.1-r demonstrate improvements in performance from 28.6% to 31.3% and 37.5% respectively." However, 37.5% is the result of GPT-4 in Figure 1, not DPO. So what are the correct results of GPT-4 and DPO?
- "We use the base model to produce a feedback score for each action by asking it to rank the generated actions by its perceived utility in helping the agent complete the user task." Can the authors provide more details on how the feedback score is generated?
- How does the number of iterations in Agent Q affect the performance? Are there any ablation studies on this?
- How does the computational complexity of Agent Q compare to the baseline methods?

### Soundness
2

### Presentation
1

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
The authors introduce an approach to train web agents, named *Agent Q*. It generates training data with MCTS over web pages and performs preference-based learning (DPO) over probable actions in each web page. As they assume sparse, trajectory-level success-or-failure feedbacks from the environment, the LLM-based critic is employed to generate such step-level feedback. The authors perform evaluation of the proposed approach on one existing benchmark, WebShop, and their own benchmark on OpenTable, and they demonstrate that their approach outperforms the employed baseline methods.

### Strengths
- The proposed approach is mostly sound (except for the open-loop planning component). MCTS can be an effective method for gathering trajectory data for agent training, and preference-based learning could be useful in web agent training scenarios.
- Overall, the manuscript is clear and easy to follow. The figures are made well for fair overviews. The writing is clear in general.

### Weaknesses
 - The proposed approach generates a plan at the beginning of each trajectory, which seems to stay frozen for the rest. This open-loop planning can be a bottleneck for improving agents' capabilities in more general, complex scenarios.
- Despite the expressions such as "real-world booking scenarios" (Abstract) and "Scaling To Real World Websites" (Section 6), the proposed OpenTable experiment doesn't seem ideal for testing the proposed approach's "real-world" capabilities. The set of tasks are generated "by combining the restaurant name, desired date and time, and user information" (L1061), and the evaluation is done based on "(1) date and time set correctly, (2) party size set correctly, (3) user information entered correctly, and (4) clicked complete reservation" (L1053). These imply that the training and test tasks (and thus correct trajectories) all share similar structures with the same set of constraints, and it can make it hard to assess the generalization capabilities of the approach, which is an important part of being "real-world." Besides, the proposed approach uses a frozen plan for each trajectory, which can be a suitable design for OpenTable but not for most of real-world websites and scenarios.
- According to the WebShop results, the advantage of the proposed approach, especially over the trajectory-level DPO baseline doesn't seem very clear to me (40.6% vs 41.5% from Figure 1).
- Combining MCTS, self-evaluation, and step-level preference learning for training has already been explored in prior work (e.g., Xie et al., 2024, as mentioned in this submission).

### Questions
Please check out the weaknesses section.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces AgentQ, an approach to enhance the capabilities of LLM agents in executing complex, multi-step planning and reasoning tasks within interactive environments. The integration of Monte Carlo Tree Search (MCTS) and iterative fine-tuning using step-level Direct Preference Optimization (DPO) has been demonstrated to be effective in LLM reasoning tasks. The authors apply the approach to both a simulated e-commerce task and the real-world booking scenario, incorporating several agent-related components. Empirical results demonstrate that AgentQ shows significant improvements over baseline methods and even surpassing average human performance under certain conditions.

### Strengths
The proposed method is successfully applied to the real-world booking scenario and achieve a $95.4\%$ success rate after a single day of data collection.

### Weaknesses
The experimental section is incomplete. The ablation study is entirely missing, providing no concrete indications of the strength of each component or design choice, such as the self-critique mechanism, the four types of actions, the effects of training sample sizes, and the weighted coefficient $\alpha$. While I understand the challenges of conducting experiments in real scenarios, ablations in the WebShop context are essential to validate the method's effectiveness. Furthermore, there is no analysis of the generated trajectories, nor are there case studies demonstrating the proposed method's efficacy.

The success rate of AgentQ+MCTS remains significantly lower than that of human experts. The authors attribute this discrepancy to short trajectories. More advanced LLMs should be evaluated to support this conclusion, such as LLaMA-3-70B-Instruct used in the booking scenario.

Many critical descriptions of the methods are lacking; please refer to the questions section.

Several important hyperparameters, such as $\theta_{threshold}$, are not listed.

The definition of $\tau$ in Equation 5 is missing.

### Questions
The authors state that the agent trained by DPO behaves greedily (Line 288). Does the step-level DPO address this issue?

Utilizing planning actions could deteriorate performance[1]. Did the authors observe similar outcomes?

How is the ranking of responses transferred to $\hat Q$?

How are the success rates of Human (average) and Human (expert) shown in Figure 1 obtained?

Which correspond to the explanation action in Figure 4?

References:
[1] Liu Z, Yao W, Zhang J, et al. Bolaa: Benchmarking and orchestrating llm-augmented autonomous agents[J]. arXiv preprint arXiv:2308.05960, 2023.

### Soundness
4

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper tackles the problem of building autonomous agents for web navigation tasks, including webshop and OpenTable. The proposed approach, AgentQ, leverages MCTS to generate an offline dataset and adopts DPO to fine-tune a base model based on both positive and negative trajectories. Finally, by combining AgentQ and online MTCS, the final performance substantially outperforms existing baselines.

### Strengths
1. The final web agent presented in this paper achieves state-of-the-art performances in particularly challenging environments. The result, I believe, is impressive.

2. The idea of combining search and RL to improve LLM's reasoning capabilities is novel. This project is one of the pioneer works that make this combination work. It would be inspiring for the community. 

So, in principle, I believe this project is worth a presentation opportunity at top-tier ML conferences.

### Weaknesses
My biggest complaint about this paper is its writing. This paper is particularly poorly written. It is such a great project but presented as an arbitrary technical report. Let's take the STaR (https://arxiv.org/pdf/2405.00451) paper as a good writing reference and I will leave a few detailed comments below. 

1. There is a significant lack of definitions. Throughout the paper, there is no definition of AgentQ. What do you mean by AgentQ? What is the difference between AgentQ and other baselines like DPO/STaR/XLaM? In the experiments, you use both AgentQ and AagentQ+MTCS as method names in the plot. What are the differences? It seems AgentQ itself requires MTCS for data generation. I spent a long time figuring out that the "MTCS" in Figure 1 refers to inference-time MTCS. Let's take the STaR paper as a reference. The STaR paper has a rigorous method section, where the definition of the method (including why it is named STaR) is clearly stated in Section 3. It even shows an overview plot in Figure 1 to make a reader understand the method better. 

2. Many experiment and baseline details are lacking. In general, each paper should have a separate experiment section (like Section 4 in the STaR paper) to present the baselines, environment, and main results. However, in this paper, all the presentations are sequential without even a centralized experiment section, which brings substantial difficulties for readers to follow. It is also unclear to me how these baselines are selected. For example, why is there no RFT + MTCS demonstrated in Figure 1? Note that this baseline is listed in Figure 3. What are the current state-of-the-art numbers on these two benchmarks?

3. Lack of ablation studies. For example, for AgentQ, it is unclear to me how effective each component is. I think a separate ablation studies section should be presented. What if we run RFT with the same data collection pipeline? Does the same conclusion still hold for Webshop if we turn the AI-based action section off? What if we directly run the Q function as the final deployed policy without DPO training a policy? Moreover, since MTCS is involved, it is critical to me to see the performance growth w.r.t. the computation budget used by MTCS, both online and offline. I cannot see any detailed specifications of MTCS in the main paper. If we allocate an infinite amount of time, what's the limit of this approach? Any concrete case study?

4. The AI-based action selection protocol looks unclear to me. This protocol only ranks agents. But MTCS expands the actions using the UCB criteria. The data generation also depends on the Q function only. The ranking does not help learn the Q function. Why do you need an AI to rank the policies? My understanding of it is that it works as a branching mechanism to allow MTCS to only traverse those most promising actions. Is my understanding correct? 

5. The theorem is good as it is but I don't think it makes too much sense for the overall project. You are not sampling data according to the  Q-induced distribution. The theorem and your algorithm aren't strongly connected. I would suggest you put more content on ablation studies and fine-grained controlled experiments.

6. Another minor point is that the citation formats are not consistent across the paper. Please update accordingly.

### Questions
See comments above.

In general, I would like to show my support for this project. It is a good one. However, the paper should be rewritten to get accepted.

I'm happy to raise my score after seeing the revised version.

### Soundness
2

### Presentation
1

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents Agent Q, a framework that improves the multi-step reasoning abilities of AI agents in interactive environments by combining guided MCTS with self-critique and an off-policy variant of DPO. It achieves superior performance in web navigation tasks, significantly outperforming standard methods and nearing human-level competence.

### Strengths
**Originality:**

The paper introduces a unique approach by combining MCTS with self-critique and DPO to enhance the decision-making abilities of AI agents. This innovative blend of techniques addresses the limitations of traditional LLMs in dynamic environments, making it a fresh contribution to the field.

**Quality:**

The research is thorough and well-executed, with rigorous experiments conducted in both simulated and real-world settings. The significant improvements in success rates, particularly in complex web navigation tasks, demonstrate the robustness and effectiveness of the proposed framework.

**Clarity:**

The paper is clearly written and well-structured, making complex concepts accessible. The methodology and results are presented in a straightforward manner, supported by clear figures and discussions that highlight the framework's advantages.

**Significance:**

Agent Q's ability to outperform existing methods and approach human-level performance in certain tasks is highly significant. It represents a substantial step forward in creating more autonomous and reliable AI systems, with broad implications for various applications, from web navigation to real-world decision-making.

### Weaknesses
 **Concerns Regarding Multi-turn DPO Loss:**

This paper extends the DPO loss to accommodate multi-turn interactions, as shown in Eq 5. However, recent literature [1], specifically in section 2.2, suggests that the expected multi-turn DPO loss is predicated on deterministic environment transitions. When transitions are stochastic, as is often the case in complex, real-world environments, the efficacy of the multi-turn DPO loss becomes unpredictable. It would be beneficial to see an analysis or empirical evidence that your approach is effective for the stochastic environment.
    
**Scalability and Computational Cost:**

The integration of MCTS, while enhancing performance, comes at a significant computational cost. For real-time applications or large-scale deployments, this could be prohibitive. A deeper analysis of the computational overhead and potential optimizations to mitigate this would be valuable. Could you elaborate on any strategies you've considered or implemented to address this?

**Limited Real-World Validation:**

Your experiments in WebShop and a real-world booking scenario are impressive, but they represent a limited scope of real-world environments. It's unclear how your framework would generalize to other domains or more complex applications. Broadening the range of scenarios tested would provide a more thorough validation of your framework's robustness and versatility.

**Sparse Reward Challenges:**

The sparsity of rewards in long-horizon tasks poses a significant challenge for your framework. While AI feedback and self-critique offer some mitigation, there's still a noticeable struggle with credit assignment. Exploring more sophisticated reward shaping or alternative methods to provide denser feedback could significantly enhance performance in these scenarios.

### Questions
Please refer to the weaknesses.

### Soundness
3

### Presentation
4

### Contribution
3
