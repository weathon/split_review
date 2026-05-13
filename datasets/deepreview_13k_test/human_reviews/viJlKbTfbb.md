# What If You Were Not There? Learning Causally-Aware Representations of Multi-Agent Interactions

- Decision: Reject
- Scores: 6, 6, 5

## Abstract
Modeling spatial-temporal interactions between neighboring agents is at the heart of multi-agent problems such as motion forecasting and crowd navigation. Despite notable progress, it remains unclear to which extent modern representations can capture the causal relationships behind agent interactions. In this work, we take an in-depth look at the causal awareness of the learned representations, from computational formalism to controlled simulations to real-world practice. First, we cast doubt on the notion of non-causal robustness studied in the recent CausalAgents benchmark. We show that recent representations are already partially resilient to perturbations of non-causal agents, and yet modeling indirect causal effects involving mediator agents remains challenging. Further, we introduce a simple but effective regularization approach leveraging causal annotations of varying granularity. Through controlled experiments, we find that incorporating finer-grained causal annotations not only leads to higher degrees of causal awareness but also yields stronger out-of-distribution robustness. Finally, we extend our method to a sim-to-real causal transfer framework by means of cross-domain multi-task learning, which boosts generalization in practical settings even without real-world annotations. We hope our work provides more clarity to the challenges and opportunities of learning causally-aware representations in the multi-agent context while making a first step towards a practical solution.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work focuses on the problem of causal representations in multi-agent forecasting problems.
After assessing the CausalAgents benchmark and its shortcomings, the authors employ the ORCA simulator to generate counterfactual scenes which results in a diagnostic dataset.
This dataset includes annotations of individual agents' causal effects on the ego agent through the euclidean distance of its trajectory in both scenes.
Two methods for promoting causal awareness are introduced, the basis of which is that latent representations of the ego agent should be invariant to the removal or addition of non-causal agents.
Since this approach heavily relies on the causal annotations, its application to real-world datasets is non-trivial.
To bridge this gap, this work proposes a sim-to-real causal transfer approach where data with annotated causal effects is used in conjunction with real human trajectory data to train a motion forecasting model.
Results are presented on the diagnostic dataset to evaluate the causal awareness of current motion prediction models, and how the proposed approaches affect the causal performance of such models.
Further results are presented to show how the proposed approaches can help current prediction models on real-world datasets using the proposed sim-to-real training.

### Strengths
- The literature review is complete and addresses the relevant categories for this work. These include multi-agent interactions, robust representations and causal learning. 

- The motivation for this work, presented in Section 3.1 and 3.2, is informative and provides the background for the subsequent sections. I particularly liked section 3.2 which outlined the shortcomings of the CausalAgents Benchmark.

- I thought the experiment showing how promoting causal invariance leads to better prediction accuracy with low amounts of real-world data interesting. This is possibly undersold in the paper, but an interesting result.

### Weaknesses
- The main issue I have is that the proposed approach seems to provide marginal improvements across all metrics. 
Perhaps this is down to the point made by the authors, that all methods are already pretty strong for non-causal agents, but not so much for causal agents. 
In Figure 6, the within quantile difference seems quite small. 
I think it would be much more interesting if the ACE metrics in Table 1 were replicated with the proposed approaches, showing how these values (particularly ACE-DC/IC) are presumably improved with the promotion of causal invariance. Why is the split done using quantiles here instead of spliting across the ACE-X metrics?

### Questions
- Figure 4 is not referenced anywhere.

- in Figure 8, what is the difference between baseline and vanilla? 

- In relation to the previous point, I think all Figure captions should include a legend telling the reader the different variants. For examples, Figure 6 has both a baseline and augment. But the text says that data augmentation is a baseline. This feels a little ambiguous. If I understood correctly, augment is the data augmentation baseline, and baseline is actually vanilla Autobots. Is this correct?

- I wonder if it would be interesting to also look at the number(or percentage) of ego-collisions in the sim-to-real experiments. It could give a better picture on the importance of promoting causal representations.

- What exactly is the unseen context variant in the OOD experiments? This and high density should be clearly defined.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper considers the problem of learning causally-aware representations in the context of multi-agent interactions. The authors first raise concern about the recently proposed social causality benchmark, pointing out the flaws in the annotation process and evaluation protocol. As a result, the authors introduce a diagnostic dataset based on ORCA, with fine-grained causal annotations where each agent is labeled as non-causal, direct causal, or indirect causal, and propose a new evaluation metric, namely average causal error (ACE). The paper then proposes two strategies exploiting fine-grained causal annotations: regularization using contrastive loss or ranking loss. For the real-world scenarios where obtaining counterfactual samples is impossible, they introduce sim-to-real causal transfer strategy where the model is jointly trained on the task in hand and its simulation counterparts. The experiments demonstrate the effectiveness of the proposed regularization strategy using fine-grained causal annotations and causal transfer.

### Strengths
- The paper is easy to follow and well-written. The problem of learning causally-aware representations is also significant.
- The paper raises concerns about the CausalAgents benchmark, i.e., the annotation process and evaluation protocol. These points seem reasonable to me and serve as a new perspective at minimum. It could also bring further development in the field (e.g., new benchmarks and evaluation metrics).
- Leveraging fine-grained annotations to further improve the robustness of the representations is convincing. The proposed two instantiations are intuitive and reasonable.
- The motivation and idea of sim-to-real causal transfer are convincing and interesting. It is simple and works well (at least in the ETH-UCY dataset).

### Weaknesses
- In the annotation process of the proposed dataset, each $i$-th agent is labeled as non-causal, direct causal, or indirect causal based on the influence the ego agent $\mathcal{E}_i$, i.e., measured by removing a *single agent*. However, the causal effect of the agent (to the ego agent) could be different based on the other agent (as Fig 2 illustrates).
    - For example, for indirect causal agents  $i, j$ (i.e., $\mathcal{E}_i, \mathcal{E}_j \gg 0$), it is possible that removing both of them does not influence the ego agent, i.e., $\mathcal{E}\_{ij} \simeq 0$.
    - For another example, it is also possible that $\mathcal{E}\_{ij} \gg 0$ when $\mathcal{E}_i, \mathcal{E}_j \simeq 0$ (e.g., when there are two bikes in the same lane in Fig 2, removing only one of them does not influence the ego agent but it does when removing them together).
- Similarly, the proposed evaluation metric ACE also considers removing only a single agent. It is not clear **why and how this metric serves as a reliable indicator** of the causal awareness and robustness of a learned representation. The authors argued that Eq. 3 using $\mathcal{E}_\mathcal{R}$ *overestimates* the robustness issue as described in Caveats in page 4 and Fig 3. However, one could also view that the proposed metric **ACE may *underestimate* the robustness issue**. This is related to “Takeaway 1” where the authors claim that recent methods are already partially robust w.r.t. non-causal agent removal. But this only considers a single agent removal and therefore may underestimate the robustness issue. It would be appreciated if the authors could provide justification for their annotation process and evaluation metric which is based on the influence measured by removing *a single agent*.
- The paper only considers a single dataset (ETH-UCY), and the proposed regularization strategy is only applied to a single backbone (AutoBots), which makes it difficult to assess its wide applicability. In other words, it is unclear how the proposed regularization strategy would work on other datasets and with other backbone methods.
- The paper lacks a detailed description of the proposed diagnostic dataset based on ORCA (in both the main body and the appendix). For example, what is the difference between OOD-Context and OOD-Density-Context? (They seem to be both dense.) Maybe a figure or illustration would be much appreciated. Also, as the one who is not directly working in this field, it is hard for me to understand the similarity and difference between ORCA simulation and ETH-UCY dataset, and thus it is difficult to assess how reasonable the proposed causal transfer strategy is.

**Justification for the rating**

Despite several concerns I listed above, my initial assessment weighed more on its positive (potential) values. I look forward to the feedback from the authors and discussions with other reviewers.

### Questions
My major concerns and questions are listed above. Some minor comments:

- Fig 2 is not color friendly (it is hard to distinguish cyan and blue).
- The paper sometimes interchangeably uses “causal representation” and “causally-aware representation”. They have different meanings in the literature and I think the latter fits the paper.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper investigates the extent to which modern representations can capture the causal relationships in agent interactions. It challenges the concept of causal robustness proposed by a recent work. With a new diagnose dataset, this paper shows that recent representations are partially resilient to non-causal agent perturbations but struggle with modeling indirect causal effects involving mediator agents. The study introduces two simple regularization approaches using causal annotations of varying granularity, which enhances causal awareness and out-of-distribution robustness. Additionally, they tested the effectiveness of the proposed method in a sim-to-real causal transfer scenario. This work aims to shed light on the challenges and opportunities in learning causally-aware representations in multi-agent scenarios and takes a step toward practical solutions.

### Strengths
(1) The definitions for social causality and the following computational methods are clearly defined and well motived. The overall logic flow is smooth and is a pleasure to read.
(2) The experiments evaluations are thorough.
(3) The writing is clear and helps the understanding of the motivation, desiderata, solution.

### Weaknesses
(1) The proposed method is highly confined to the simulator. As the author already noted, counterfactual data is impractical to collect in real world scenario and they instead took a sim-to-real transfer learning approach. But the assumption that the underlying causal mechanisms stay the same is simply too fragile to be true. For example, in simulation, the author define the visibility range as 210 degree in front of the driver ignoring the fact that drivers also check rearview mirrors for road information. And the simulator itself focuses heavily on collision avoidance. However, human drivers are not perfectly rational and have various driving preferences. Instead of “causally-aware” representations, it’s more accurate to say the proposed method learns “collision-aware representations”. Rather than assuming “the causal mechanisms” satisfying some vague constraints, I would recommend the authors model the problem more rigorously with causal theories [1,2]. 

(2) Even if we only consider the collision-free driving style, the proposed method’s effectiveness is not convincing enough. Firstly, if you have done multiple runs with different random seeds for the same experiment, I am expecting to see confidence intervals or error bars in the results. Secondly, the author introduced three metrics for evaluation, Average Displacement Error (ADE), FinalDisplacementError(FDE), and Average Causal Error (ACE). However, figure 6 is missing FDE and figure 8 is missing ACE. Thirdly, for the data reported, the contrastive method seems to be on par with the “augment”. When in sim-to-real, it’s sometimes even worse than “augment” and the improvement is rather marginal. We do see notable improvements of the “rank” method over baselines but I am not sure if it’s a fair comparison because the “rank” method actually provides way more labeling information than binary labels (causal/non-causal). Does those baselines also have access to such labels? At last, when using 100% percent data in the sim-to-real test, the proposed method (contrast) barely beats those baselines leaving doubts on whether the performance gaps in 25% and 50% scenarios are due to learning efficiency difference instead of representation quality.

[1] Bareinboim, Elias, and Judea Pearl. "Causal inference and the data-fusion problem." Proceedings of the National Academy of Sciences 113.27 (2016): 7345-7352.  
[2] Hernán, Miguel A., and Tyler J. VanderWeele. "Compound treatments and transportability of causal inference." Epidemiology (Cambridge, Mass.) 22.3 (2011): 368.

### Questions
(1) Could you extend the experiments to multiple random seeds and report the variances in the figures?
(2) Could you report all three metrics for figure 6 and 8?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good
