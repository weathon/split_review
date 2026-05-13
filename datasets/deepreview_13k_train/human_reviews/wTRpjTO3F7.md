# Quantifying Zero-shot Coordination Capability with Behavior Preferring Partners

- Decision: Reject
- Scores: 6, 5, 6, 3

## Abstract
Zero-shot coordination (ZSC) is a new challenge focusing on generalizing learned coordination skills to unseen partners. 
Existing methods train the ego agent with partners from pre-trained or evolving populations. The agent's ZSC capability is typically evaluated with a few evaluation partners, including human and agent, and reported by mean returns. Current evaluation methods for ZSC capability still need to improve in constructing diverse evaluation partners and comprehensively measuring the ZSC capability. We aim to create a reliable, comprehensive, and efficient evaluation method for ZSC capability. We formally define the ideal 'diversity-complete' evaluation partners and propose the best response (BR) diversity, which is the population diversity of the BRs to the partners, to approximate the ideal evaluation partners. We propose an evaluation workflow including 'diversity-complete' evaluation partners construction and a multi-dimensional metric, the **B**est **R**esponse **Prox**imity (BR-Prox) metric. BR-Prox quantifies the ZSC capability as the performance similarity to each evaluation partner's approximate best response, demonstrating generalization capability and improvement potential.  We re-evaluate strong ZSC methods in the Overcooked environment using the proposed evaluation workflow. 
Surprisingly, the results in some of the most used layouts fail to distinguish the performance of different ZSC methods.
Moreover, the evaluated ZSC methods must produce more diverse and high-performing training partners. Our proposed evaluation workflow calls for a change in how we efficiently evaluate ZSC methods as a supplement to human evaluation.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The performance of the agent's Zero Shot Coordination (ZSC) capability is difficult to measure and quantify. The difficulties are twofold: (1) how to construct sufficient diverse evaluation partners? (2) how to measure the performance? Most previous methods focus on designing superior ZSC algorithms while not paying much attention to the evaluation metric. 

This paper first proposes to construct 'diversity-complete' evaluation partners by maximizing the best response diversity (the population diversity of the BRs to the evaluation partners). Then the paper proposes a Best Response Proximity (BR-Prox) metric, which quantifies the ZSC capability as the performance similarity to each evaluation partner’s approximate best response, demonstrating generalization capability and improvement potential.

Evaluations conducted on the overcooked environment validate the effectiveness of the proposed evaluation workflow and show some interesting results.

### Strengths
* The paper may be the first to systematically study how to measure and quantify the agent's Zero Shot Coordination (ZSC) capability. The proposed evaluation workflow is technically sound. 
* Sufficient experiments are designed to demonstrate the effectiveness of the method. The results find that the most used layouts in the overcooked environment cannot show the ZSC capability difference among the ZSC methods.
* Overall, the writing of the article is relatively clear.

### Weaknesses
 * Some parts of the paper are not very clear. For example, the motivation for introducing the event-based rewards is not clear. 
* In practical implementation, the method requires humans to manually define some triggered events so as to derive diverse behaviors, which is difficult to obtain in complex tasks.
* Comparisons with previous baselines listed in Table 1 may be missing.

### Questions
Please see the weakness above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the evaluation metric for zero-shot coordination. The authors propose to construct diverse evaluation partners with their approximate BRs, and then compute the proposed BR-Prox across these evaluation partners as the metric. BR-Prox measures the performance similarity between the ego agent and the approximate BRs of the evaluation partners.

### Strengths
- The studied question is important and interesting for zero-shot coordination
- The paper is easy to follow

### Weaknesses
 - The main concern is the practicality of the proposed evaluation method. It evolves complicated steps to construct such evaluation agents and prepare their approximate BRs. The idea of computing the BR diversity is straightforward, but it is not easy to really use such a metric in practice. And the huge implementation effort would definitely reduce its impact on the community.
- The design of reward space is crucial for the proposed evaluation partners. However, it is clearly discussed, at least I didn’t find it yet in the main text. What’s more, it is hard to say the resulting partners would show expected reasonable behaviors.
- In addition to the evaluation agents, the proposed method requires users to compute the approximate BRs. In simple tasks like Overcooked, it could be fine. However, it could be hard to obtain in complex robot tasks.

### Questions
- How to compute the approximate BR, $\widehat{BR}(\pi_{\omega})$ ?
- How to design the reward space?
- If all of these evaluation agents can constructed, why not use them to train the ego agents?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper proposes a new evaluation metric for the zero-shot coordination problem. The method involves first training diverse policies and the corresponding best responses, employing the similar method as HSP, and then select evaluation partners based on the best response diversity metric. 
The ego agent is then evaluated with the selected partners and a metric called best response proximity is calculated based on the performance of the ego agent versus the best response policy. The experiment results demonstrate that some widely used layouts in the literature may lack enough complexity to evaluate the effectiveness of different methods.

### Strengths
1. In general, the authors propose an important question that the evaluation protocol should be improved in the literature of ZSC problem. 
2. The idea that uses a set of sufficiently diverse policies as evaluation partners is straightforward and promising. 
3. The experiment result demonstrates the effectiveness of the proposed metric to distinguish different methods in conflicts layouts.

### Weaknesses
A significant limitation is the absence of a crucial baseline, specifically HSP. Since the paper's approach to training evaluation candidates and best response policies closely mirrors that of HSP, it should not pose a substantial challenge to also train an ego agent for HSP. I would consider increasing my score if this limitation is addressed.

Additionally, the paper's argument for using Best Response Diversity (BR-Div) over Population Diversity (P-Div) is not entirely convincing. While the authors claim that BR-Div is a novel metric for population diversity in the ZSC domain, the justification provided is somewhat circular. The argument that an ego agent with higher ZSC capability emulates more BRs, and therefore should be evaluated against partners with diverse BRs, assumes the very thing it is trying to prove. The paper needs to provide more rigorous justification for why BR-Div is a more appropriate measure of diversity for evaluating ZSC than P-Div, especially given that P-Div is a more direct measure of the variety of policies in the population.

### Questions
1. In figure 3, how would the population diversity of selection with population diversity lower than that of selection with BR-Div? This seems to be counterintuitive as it is expected to find the subset with largest population diversity if P-Div is used as the selection metric.
2. Please explain the difference among different layouts in more details.  Are there other kinds of events except conflicts should be considerred to influence the perfomance of different methods in the introduced layouts?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper aims to create a reliable and comprehensive evaluation method for zero-shot coordination. The authors design an evaluation workflow includes three stages. Firstly the method generates behavior preferring agents with corresponding BRs. Secondly representative policies are selected based on a BR-diversity. Finally the selected policies and their BRs are used to evaluate the ego policy. The overall framework has potential to provide a more effective metric (BR-Prox) and also indicates some shortcuts of overcooked scenarios.

### Strengths
1. The methodology of constructing a "diversity-complete" set of BRs is reasonable and meaningful.
2. The authors propose the BR-Prox metric to measure the performance of an ego policy under the ZSC manner and use this metric to benchmark previous methods on ZSC.
3. The authors propose an algorithm to construct an evaluation population by first generating adequate policies and then selecting diverse ones.

### Weaknesses
1. Though the authors claim that a "diversity-complete" set may be intractable for complex environments, the proposed methodology (generation and selection) fails to well adhere to the exact definition in the desiderata (Section 3.2) with the lack of revealing the gap with a real "diversity-complete" set. The division of diversity into 'skill-style' and 'skill-level' lacks clear justification, and it's not evident that the construction process using BR-Div actually generates a diverse population that covers the full spectrum of possible behaviors. Specifically, the method's ability to generate diverse behaviors is not rigorously demonstrated, and it is unclear how the chosen events and weights influence the diversity of the generated policies.
2. The proposed metric and evaluation workflow lack necessary discussions with previous approaches (e.g., methods in Table 1). While the paper mentions limitations of existing methods, it doesn't provide a practical comparison of how the Behavior Preferring Evaluation method improves upon them. It is unclear what specific emerging behaviors are captured by this method that cannot be found by other evaluation methods, and how the proposed method addresses these limitations.
3. The presentation of this paper is generally obscure. The authors involve a sort of techniques during the evaluation workflow but do not well explain the necessity and details (e.g., how to represent the behavior feature of a policy and reasons to involve event-based rewards). The dependence on the design of events and weights makes the method seem ad hoc, potentially overfitting the Overcooked environment. The paper does not explain how the weights are chosen, nor the meaning of multiple weights for one event. The current approach may restrict its use cases, as there can be various evaluation designs for an environment, with different implementations of events and weights.
4. The evaluated baselines seem not distinguishable in the evaluation setting while the authors do not provide further insights of what kinds of approaches are generally useful on ZSC. The lack of clear distinctions between baselines suggests that the evaluation setup might not be sufficiently challenging or diverse to differentiate various ZSC methods.
5. The evaluation workflow is restricted to a two-agent form while previous ZSC methods can generalize to multi-agent settings.

### Questions
1. How can we extend the evaluation manner to multi-agent settings?
2. In Figure 2, how are the high-level behaviors visualized? What is the meaning of different data points in Figure 2?
3. In Figure3, why does the population diversity first rise and then drop with the population size increasing? As near 0 values mean linear correlation, why is the diversity low in a small population size?
4. Does the P-Div metric mean $\text{PD}$ on $\pi_i$ instead of $BR(\pi_i)$?
5. In Section 5.2, how do Figure 4 and 5 show "increasing population size contributes to the improvement of performance under the condition that the diversity of the population is also grown". 
6. How do the event-based rewards contribute to behavior preferring policies? Specifically, how do the method design and adjust $w$? How is this approach related to proposed "skill-level diversity"?
7. At the end of Section 3.2, "by selecting earlier checkpoints of the evaluation partners, it is simple to acquire evaluation partners with diverse skill levels." What is the actual method of selecting earlier checkpoints of the evaluation partners?
8. How can we represent the behavior feature $\theta$ of a policy?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair
