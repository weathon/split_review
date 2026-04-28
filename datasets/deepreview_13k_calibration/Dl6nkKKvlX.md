# Balancing Act: Diversity and Consistency in Large Language Model Ensembles

- Decision: Accept
- Avg Score: 6.25
- Scores: 8, 5, 6, 6

## Abstract
Ensembling strategies for Large Language Models (LLMs) have demonstrated significant potential in improving performance across various tasks by combining the strengths of individual models. However, identifying the most effective ensembling method remains an open challenge, as neither maximizing output consistency through self-consistency decoding nor enhancing model diversity via frameworks like "Mixture of Agents" has proven universally optimal.  Motivated by this, we propose a unified framework to examine the trade-offs between task performance, model diversity, and output consistency in ensembles. More specifically, we introduce a consistency score that defines a gating mechanism for mixtures of agents and an algorithm for mixture refinement to investigate these trade-offs at the semantic and model levels, respectively. We incorporate our insights into a novel inference-time LLM ensembling strategy called the Dynamic Mixture of Agents (DMoA) and demonstrate that it achieves a new state-of-the-art result in the challenging Big Bench Hard mixed evaluations benchmark. Our analysis reveals that cross-validation bias can enhance performance, contingent on the expertise of the constituent models. We further demonstrate that distinct reasoning tasks—such as arithmetic reasoning, commonsense reasoning, and instruction following—require different model capabilities, leading to inherent task-dependent trade-offs that DMoA balances effectively.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces a unified approach to explore the balance between diversity and consistency in LLM ensembles. It addresses the challenge of finding optimal ensembling methods, where traditional strategies like self-consistency decoding (focusing on output consistency) and Mixture of Agents (MoA, focusing on model diversity) each have limitations. The authors propose the **Dynamic Mixture of Agents (DMoA)**, a novel inference-time ensembling strategy that integrates insights on the interplay between diversity and consistency. 

1. The paper establishes a framework for examining trade-offs between task performance, diversity, and consistency within LLM ensembles.
2. Introducing a consistency score enables selective filtering within model outputs, enhancing ensemble consistency.
3. This method refines mixtures of agents by considering semantic and model-level adjustments, optimizing task performance.
4. DMoA dynamically selects models based on task-specific needs, achieving state-of-the-art results on the Big Bench Hard benchmark, demonstrating effective balance across tasks.

### Strengths
1. This paper addresses an intriguing and nuanced problem—how to balance consistency and diversity within LLM ensembles. This issue is fundamental, as different tasks often require prioritizing one over the other. 
2. The paper is well-structured and logically rigorous. The authors provide clear, precise definitions of both DMoA and GMoA frameworks, enabling readers to fully understand the distinctions and specific innovations in each method.
3. The authors show that DMoA achieves state-of-the-art results on the Big Bench Hard (BBH) benchmark, indicating the framework's efficacy across various challenging tasks.

### Weaknesses
While the paper demonstrates the effectiveness of GMoA and DMoA in achieving high performance, it does not analyze the computational costs associated with these methods. Cost considerations are essential in ensemble approaches, particularly with LLMs, where scaling and inference-time model selection can be computationally intensive. For a comprehensive comparison, the authors should evaluate the total cost associated with GMoA and DMoA, including resource utilization during inference and model selection. This cost analysis should include a breakdown of the cost of each component, such as the number of forward passes required for each model in the ensemble, the overhead of the consistency scoring mechanism, and the cost of the dynamic model selection process. Furthermore, the analysis should consider the latency implications of these methods, as the time taken for inference is a critical factor in practical applications. This cost analysis would offer a more balanced view of the trade-offs between performance gains and computational expense, especially compared to other ensemble strategies and Chain-of-Thought (CoT) approaches.

### Questions
1. I am curious if the proposed methods, particularly DMoA and GMoA, align with test-time scaling laws. Specifically, does performance consistently improve as the number of models in the ensemble or the length of inference chains increase?
2. In the experimental setup, the paper mentions constructing a "MoA-Lite" variant with a limited number of layers. What would happen if additional layers were added to MoA?
3. In what specific scenarios are GMoA and DMoA each most effective? Can these methods be combined within a single framework to further improve performance?

### Soundness
3

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
The paper proposes a new model ensemble strategy that builds on top of a Mixture of Agents called Dynamic Mixture of Agents (DMoA). First, the authors attempt to unify model ensemble methods with a formal definition. The overall hypothesis for all the experiments are that different tasks require different ensemble diversity/consistency. With that, they first do an experiment where they propose a divergent metrics EigenScore and EigenDivergence that measure how semantically consistent/inconsistent LLM outputs are to the overall semantics. The effect of this Gated MoA is nuanced. For the next experiment, they try to optimize MoA structure by proposing a model delta that correlates with task performances. They found that there are trade-offs between each task. If they optimize for one task, it would decrease for another task. Lastly they tried DMoA, which chose mixtures based on some criteria. They showed that DMoA outperforms MoA on BBH.

### Strengths
- The authors design and execute a pretty comprehensive analysis and extensions to the model ensembling method Mixture-of-Agents. The analysis and conclusions are useful because they give intuitions on what may work and may not work in a mixture of model frameworks. 
 They first investigate whether reducing semantic inconsistency would help (it didn't, I wonder if the reverse would help though -- increase the diversity). Then a mixture optimization method is proposed and they found some useful insights, e.g., aggregate and synthesis works better than ranking and self-consistency. They then tested DMoA which dynamically uses different expertise models for the mixture.
- It is quite important to dive deeper into what makes model collaboration work as model ensemble methods are a promising way to inference-time scaling.
- The tasks are pretty comprehensive.

### Weaknesses
 - The purpose of the first experiment is a bit questionable. The result from divergent filtering is nuanced, as it only slightly improves four out of five reasoning tasks, and decreases performances on three tasks. I understand you use this experiment's result as insights to build DMoA in section 4.4, but I question whether those insights are actually correlated. 
  - For insight 1 in section 4.4, divergent filtering is used as a supporting evidence as "As shown in Sec. 4.1, LLM ensembles outperform individual models regardless of divergence filtering, across both open- and close-ended tasks." If the conclusion arrived "regardless of divergence filtering" then it doesn't really add much value to the argument.
  - For insight 2, it says "We found in Sec. 4.1 that removing information from an ensemble can improve task-specific performance." But it improves four and hurts three.
  - For insight 3, it says "Performance varies when semantic diversity is altered within a fixed ensemble (Sec. 4.1)." This claim is not that clear and doesn't provide much insight since performance can vary if you change anything about the mixture. It would be more useful if more patterns could be discovered. 
- Similarly, I am concerned about the claim in section 4.3: "two GMoA variants...one with the two most semantically divergent outputs removed (maximizing consistency), and one with the two most consistent outputs removed (maximizing diversity)...indicating that some semantic consistency is necessary for high-quality results, even in open-ended instruction-following queries." I don't think removing two most consistent outputs would maximize diversity. You could very well be removing two very similar outputs that are very distinctive from other outputs. This also has the unwanted effect of removing output that's more correct (since more models output it).
  - This leads to insight 1 in section 4.4 that "Maximizing semantic diversity harms performance (Sec. 4.3), indicating that some cross-validation between outputs is necessary for high-quality results, even in open-ended instruction-following tasks." This can be problematic since the premise is wrong.
- The structure of the paper gives a strong vibe that the first two experiments are very disconnected from the third as neither divergent filtering (GMoA) nor the mixture optimization methods are used in the third. And the insights they provide are also very limited which I elaborated above. I would encourage maybe downplaying the portion of the first two experiments and focusing more on the third.

### Questions
- I wonder about the performance of DMoA on seven tasks used in the first two experiments. This should be a natural progression. It feels weird that for the first two, we are using the same set of seven and for third, we are using BBH.

### Soundness
2

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
3

### Summary
The authors in this work look at Mixture of Agents (MoA) and propose:
1) A framework that captures different variations of possible MoAs
2) Divergence metric called `EigenDivergence` based on the hallucination detected in K sampled outputs with the additional proposition of using an external embedding instead of the model's internal embedding
3) Propose an optimization algorithm based on incremental performance gains and usage
4) Propose DMoAs that dynamically select the models

Results of this work are shown as follows: 1) Gated MoA against standard MoA and other openly-available models, with GMoA only providing marginal improvement on settings with some models performing reasonably better while underperforming in settings where all models perform close to each other; 2) Show that mixtures do not translate the same across various tasks and 3) DMoAs perform better on the BBH

### Strengths
1. Methodology, presentation, and results are good for the first 3 / 4 proposed contributions - I quite liked the idea of EigenDivergence and the analysis around it
2. The takeaways on diversity and consistency are clear and well presented

### Weaknesses
 1. Sections 3.3 and 4.4 were both unclear and unnecessary, in my opinion - I couldn't quite understand how these sections tie to the main point of this paper. The presentation and motivation around this subset of contribution requires significant re-write 
 2. No critical focus on looking at the intermediate reasoning - while I get that semantic diversity was a focus, I would have liked to see a deeper look at how diverse semantic reasoning looked at with a few examples - were there instances were correct reasonings by multiple models were still judged to be semantically diverse, etc. I liked Appendix H - it was a good start, but a detailed, controlled experiment could've provided readers with much more about EigenDivergence

Nitpicks that can be easily fixed and does not affect the review/score:
1. Typos in some parts - line 182 for example
2.

### Questions
1. Can the details of 3.3 and 4.4 be clarified? (see weaknesses for comments)
2. Can Appendix F.2 be expanded to understand the behaviour of multiple sentence embeddings ? The 0.78 doesn't make much sense as an individual number - it is unclear if it a consequence of choice of embedding models / how much variance can exist, etc.
3. Is there a reason why closed-source models weren't used since the eigendivergence doesn't require access to the weights ?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a unified framework to examine the trade-off between diversity and consistency to the final performance of model ensemble. The author proposes a dynamic mixture of agent approach to optimize the balance between task-specific capabilities, ultimately enhancing overall performance.

### Strengths
1. The motivation of balancing the model diversity and output consistency in model ensemble is compelling and well-founded.
2. The unified dynamic mixture of agent framework effectively addresses the trade-off between diversity and consistency across various tasks.

### Weaknesses
1. The proposed dynamic mixture of agent framework necessitates the individual search and optimization of MoA structures for each distinct task. The process relies on divergence filtering and mixture optimization, which is costly and requires additional task-specific datasets for evaluation. The computational expense is a significant concern, as the method requires multiple inferences across diverse models and subsequent aggregations. This is particularly problematic given that the efficacy of the MoA approach is heavily contingent upon the final aggregation model employed. The fact that performance drops substantially when Claude-3.5-Sonnet is not used as the aggregation model highlights this dependency and raises questions about the practical applicability of the approach in resource-constrained settings.
2. The application of EignScore originally proposed for hallucination detection in a single model presents inherent limitations when extended to an ensemble of multiple models. This is primarily due to the fact that the sentence-embedding spaces of various models are not aligned during their pre-training or fine-tuning phases. Consequently, these embeddings do not inhabit the same representational space, which poses challenges for direct comparison and aggregation across different models. While the authors may project the embeddings into a shared space, the effectiveness of this projection, and the potential loss of information during this process, needs to be more thoroughly examined.
3. The design of mixture optimization leads to a scenario where the final MoA model is absolutely dominated by a single model, as shown in Fig. 3, left. Since the search process for each run is determined by a greedy algorithm that replaces the model with the lowest delta to the one with highest delta, this can lead to a suboptimal solution where the diversity of the ensemble is sacrificed for a marginal gain in performance on a specific task. This raises concerns about the generalizability of the approach and its ability to effectively leverage the strengths of different models.

### Questions
1. In Section 4.4, Table 2 presents a comparison between DMoA/Sonnet and the Claude-3.5-Sonnet baseline. While DMoA/Sonnet demonstrates a marginal performance improvement (91.85 vs. 90.20 normalized accuracy on BBH), it is important to consider the associated computational costs. DMoA/Sonnet necessitates multiple inferences across diverse models and subsequent aggregations using Claude-3.5-Sonnet. This process incurs significantly higher expenses compared to the baseline due to the additional model inferences and the substantially longer input required for aggregation. Moreover, the efficacy of the MoA approach is heavily contingent upon the final aggregation model employed. When Claude-3.5-Sonnet is not utilized as the aggregation model in the DMoA approach, a substantial performance degradation is observed (90.20 vs. 83.63 normalized accuracy on BBH).
2. What if testing DMoA on the seven benchmarks (AlpacaEval 2.0, MT-Bench, GSM8K, MATH, CSQA, ARC-C, ARC-E) in accordance with the experimental setups in Sections 4.1 and 4.2? 
3. Based on the experimental findings presented in Section 4.3, several key conclusions can be drawn regarding the impact of diversity and consistency on various cognitive abilities. Firstly, high levels of diversity appear to have a detrimental effect across all measured abilities. Secondly, strong consistency enhances reasoning and mathematical capabilities, but impairs the instruction-following proficiency. Lastly, when strong consistency is coupled with an appropriate degree of supplemental diversity, there is an observed improvement in instruction-following abilities, though this comes at the cost of diminished mathematical and reasoning skills. Compared to the discussion in current version, the above summary appears to more accurately reflect the core idea of this paper: balancing diversity and consistency for model ensemble across various tasks.

### Soundness
3

### Presentation
3

### Contribution
3
