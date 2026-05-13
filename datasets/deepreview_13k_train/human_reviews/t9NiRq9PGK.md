# Multiplayer Federated Learning: Reaching Equilibrium with Less Communications

- Decision: Reject
- Scores: 6, 5, 5, 6, 6

## Abstract
Traditional Federated Learning (FL) approaches assume collaborative clients with aligned objectives working towards a shared global model. However, in many real-world scenarios, clients act as rational players with individual objectives and strategic behaviors, a concept that existing FL frameworks are not equipped to adequately address. To bridge this gap, we introduce *Multiplayer Federated Learning (MpFL)*, a novel framework that models the clients in the FL environment as players in a game-theoretic context, aiming to reach an equilibrium. In this scenario, each player tries to optimize their own utility function, which may not align with the collective goal. Within MpFL, we propose *Per-Player Local Stochastic Gradient Descent (PEARL-SGD)*, an algorithm in which each player/client performs local updates independently and periodically communicates with other players. We theoretically analyze PEARL-SGD and prove that it reaches a neighborhood of equilibrium with less communication in the stochastic setup than its non-local counterpart. Finally, we experimentally verify our theoretical findings.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This studied the multiplayer federated learning problem, which means that each client learn the model with the knowledge of other clients' model while the master server does not need to do aggregation. The authors called this algorithm as per-player local SGD (PEARL-SGD) and analyze the convergence of it for mainly convex functions.

### Strengths
1. The PEAR-SGD is new and interesting. 

2. The authors provided the convergence analysis of PEAR-SGD under different settings including convex and its variations.

### Weaknesses
1. Although PEAR-SGD is new, I don't see much novelty of it. It is not surprising that the individual model can converge fast by knowing all others' model unless my understanding is wrong. The core idea of using other players' models to inform local updates seems like a straightforward extension of existing multi-agent optimization techniques. The method's effectiveness appears to stem from the information sharing rather than a fundamentally novel algorithmic approach. The analysis does not clearly demonstrate why this specific method is superior to other possible ways of incorporating information from other players.

2. The analysis only focused on convex and its variations. There is no analysis on general non-convex objective functions. This significantly limits the practical applicability of the results, as many real-world machine learning problems involve non-convex objectives. The theoretical guarantees are therefore restricted to a narrow class of problems, and it is unclear how the method would perform in more realistic scenarios. The lack of analysis for non-convex settings is a major limitation.

3. Since the master server needs to distribute all the individual models in each round, I didn't see how this can save communication cost. The paper does not provide a clear explanation of how the proposed method reduces communication overhead compared to standard federated learning approaches. The communication of full models in each round seems to be a bottleneck, and the paper does not adequately address this issue. The claim of reduced communication cost is not well supported by the current analysis.

### Questions
In the experiments, I suggest the authors could compare the proposed algorithm with other federated learning learning algorithm in terms of convergence rate, accuracy and communication cost.

### Soundness
3

### Presentation
3

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
The paper introduces Multiplayer Federated Learning (MpFL), a framework designed to address the limitations of traditional Federated Learning (FL), which assumes collaborative clients with aligned goals. However, in many real-world settings, clients act as rational players with individual objectives, making a game-theoretic approach more appropriate. MpFL models clients as players aiming to reach an equilibrium, where each optimizes their own utility function, which may diverge from the collective goal. The authors propose a new algorithm, Per-Player Local SGD (PEARL-SGD), in which clients perform local updates independently and periodically communicate with one another. Theoretical analysis, according to the authors, shows that PEARL-SGD reaches equilibrium with fewer communication rounds compared to non-local methods, and numerical experiments are reported to support these findings.

### Strengths
1) This paper is generally well-written and accessible, even for those not deeply versed in game theory. Despite my limited background in that area, I was able to follow the main contributions and narrative of the work with ease. The core idea, as well as the supporting results, are conveyed in a clear and structured manner.

2) The introduction provides a strong foundation for the paper, presenting the key contributions in well-organized bullet points that make the novel aspects easy to identify. The inclusion of a more detailed literature review in the appendix is especially appreciated, as it gives interested readers a broader context. Table 1 is highly informative and supports quick understanding, and Figure 1, with its clear diagram, adds helpful visual clarity.

3) The assumptions, lemmas, theorems, and corollaries throughout the paper are presented in a straightforward and precise way. Their formulation is both rigorous and accessible, making it easy to understand the logical flow.

4) Including a draft of the proofs in the main body of the paper is a thoughtful choice. This addition provides readers with helpful intuition, aiding in a deeper understanding of the theoretical claims.

5) The experimental setup is particularly effective, as it clearly demonstrates the theoretical results. I also appreciate the inclusion of results both with theoretically-derived and tuned parameters, allowing for a more comprehensive view of the findings.

6) The conclusion is well-written and provides a concise yet informative summary, reinforcing the contributions and implications of the study.

7) Overall, I find the topic both timely and compelling. This paper appears to be one of the pioneering efforts to explore the integration of game theory into Federated Learning, making it a significant contribution to the field.

### Weaknesses
1) The extended introduction is comprehensive, yet it would benefit from including some key recent contributions on client drift reduction. Specifically, the following papers could enrich the discussion, as they address related topics and offer relevant insights:

   - Hu, Zhengmian, and Heng Huang. "Tighter analysis for proxskip." International Conference on Machine Learning. PMLR, 2023.
   - Grudzień, Michał, Grigory Malinovsky, and Peter Richtárik. "Can 5th generation local training methods support client sampling? Yes!" International Conference on Artificial Intelligence and Statistics. PMLR, 2023.
   - Condat, Laurent, and Peter Richtárik. "RandProx: Primal-dual optimization algorithms with randomized proximal updates." arXiv preprint arXiv:2207.12891 (2022).
   - Zhang, Siqi, and Nicolas Loizou. "ProxSkip for Stochastic Variational Inequalities: A Federated Learning Algorithm for Provable Communication Acceleration." OPT 2022: Optimization for Machine Learning (NeurIPS 2022 Workshop).

   The last two references are particularly relevant, as they deal with settings related to minimax problems. It would be beneficial to consider and discuss these works for a more thorough literature grounding.

2) While Table 1 is quite informative, it would be even more helpful if it included a direct comparison with previous approaches. Although some comparative discussion is in the text, incorporating this within the table itself could provide readers with a more immediate visual reference.

3) The assumptions are clearly presented; however, the problem statement itself could be more rigorously defined. A more precise formulation would enhance the clarity and accessibility of the paper.

4) In Algorithm 1, the aggregation step is somewhat underexplained. Furthermore, it’s not emphasized that the server needs to send all client models to each participant. This is a significant concern in Federated Learning, where communication costs are a key bottleneck. It would be beneficial to expand the discussion on this issue, considering its practical implications.

5) In Theorems 3.3 and 3.4, with constant step size, the step size depends not only on $l$, $\tau$, and $L_\max$, but also on $\kappa$. Although Lipschitz constants can generally be estimated, $\kappa$ depends on $\mu$ (strong monotonicity), which is challenging to estimate, potentially weakening the practical applicability of the result.

6) In Theorem 3.3, the contraction factor $(1-\gamma \tau \mu \zeta)^R$ suggests that the step size $\gamma$ is multiplied by $\tau$. However, $\gamma$ is of the order $O(1/\tau)$, which implies that varying the number of local steps does not impact the convergence bound. This indicates that, theoretically, this approach is not more effective than a non-local approach with $\tau = 1$. A similar effect is noted in the stochastic setting. This discrepancy seems to contradict the claim in the abstract: *“We theoretically analyze PEARL-SGD under different step-size selections and prove that it reaches an equilibrium with less communication compared to its non-local counterpart.”* Could you provide clarification on this point?

7) The analysis is conducted under the assumption of quasi-strong monotonicity. Would it be feasible to relax this assumption or perhaps even the convexity assumption? An exploration of less stringent assumptions could broaden the applicability of the findings.

8) In the plots with theoretical parameter settings, the performance lines appear nearly identical. This suggests that the claim that the proposed method outperforms non-local approaches may not hold as strongly as suggested, similar to the issue raised in point 6. Could you comment on this observation?

9) The experiments are conducted primarily on quadratic games. It would be valuable to include additional experiments with more practical objective functions to better represent real-world applications.

10) I am not deeply specialized in this field, but the analysis appears to share similarities with the methods in the following papers:

   - Khaled, Ahmed, Konstantin Mishchenko, and Peter Richtárik. "Tighter theory for local SGD on identical and heterogeneous data." International Conference on Artificial Intelligence and Statistics. PMLR, 2020.
   - Karimireddy, Sai Praneeth, et al. "SCAFFOLD: Stochastic controlled averaging for federated learning." International Conference on Machine Learning. PMLR, 2020.

   Could you please clarify the unique elements of the technical analysis in your proofs compared to these works? Highlighting these distinctions would help underscore the novelty and significance of your theoretical contributions.

### Questions
Could you please review the Weaknesses section? I believe some of the points raised may not be entirely accurate. However, since I am not a specialist in this area, I may have overlooked certain details. I am open to reconsidering my score if my concerns can be addressed. As it stands, though, I feel that the paper is not ready for acceptance in its current form.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
- This paper introduce a framework, referred to as Multiplayer Federated Learning (MpFL), that models clients as players in a game-theoretic setting and aim to reach an equilibrium.
- Within MpFL, the authors propose an algorithm where each client updates local parameters independently and communicate with other clients periodically. 
- The algorithm under different step-sizes are analyzed theoretically that the proposed algorithm needs fewer communications than its non-local counter part, which is verified empirically over simulated data.

### Strengths
- The introduction is organized and logical
- The writing is generally easy to follow

### Weaknesses
 - Unclear definition of MpFL:
	- Despite the introduction and discussion in Section 2.1, there is no rigorous definition of what MpFL is, and how that is different from FL. While the authors describe the setup, a formal mathematical definition is missing, unlike the definitions provided for related works such as FL and Federated Min-max formulations. This makes it difficult to precisely understand the scope and contribution of MpFL. A clear, concise mathematical definition, similar to those in lines 204 and 220, is needed to establish the framework rigorously.
	- The definition of FL should be in the preliminaries before introducing MpFL. Instead, it is delayed to Section 2.2.
	- Suggestions
		- Provide a concise, formal definition of MpFL, perhaps in a dedicated subsection or as a numbered definition. This would help clarify exactly what elements constitute the MpFL framework and appreciate the value of such formulation.
		- Discuss how the motivation lead to this formulation. Why communicating only once in a while? How does this falls into the federated learning framework?
		- Discuss the problem formulation itself. Does the problem exists a solution? Is it unique? Does the solution depends on the order of the optimizations of different players?
 - Grammatical errors, typos
	- L22: less communications -> "less communication" or "fewer communications"
 - Definition of \(f_{i, \xi_{i}}\): The notation \(f_{i, \xi_{i}}\) is not clearly defined. The text in lines 165-167 describes the data setting but does not provide a mathematical definition of \(f_{i, \xi_{i}}\) or its relationship to \(f_i\). This lack of clarity makes it difficult to understand the precise problem formulation.

### Questions
- Why is "communicating through a central server" important in MpFL? Instead of concatenate the strategies of all players via a central server in the aggregation round, can we just assume each player can observe other players' strategies?
-  L167: What does the additional subscript $\xi_{i}$ in $f_{i, \xi_{i}}$ mean? Please explicitly define the notation $f_{i, \xi_{i}}$ and explain its relationship to $f_i$.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies the federated learning in a game-theoretic context by modeling the multiple agents as multiplayers trying to reach an equilibrium point. Theoretical proof and experiments are proved for the proposed local stochastic gradient based algorithm.

### Strengths
The motivation that in many practical FL settings agents may have individual objectives that do not align with the collective goal is interesting and worth studying if well defined.

### Weaknesses
1. The paper states that each agent only has access to its own local objective function while in the algorithm it has been shown that the master server collects and distributed all actions to all agents. Also, from the definition of the local utility function in equation (5), all other agents actions are required to compute the local gradient. Therefore, the statement is contradicting.  The core issue is that while agents might not directly access each other's objective functions, the algorithm requires them to have access to each other's actions to compute their own gradients, which contradicts the idea of isolated local information. The algorithm's reliance on global action information undermines the claim of agents operating solely with local objective function knowledge.

2. The experiment part is limited. Only the relative error is shown, which is not easy for readers to tell the benefits of the proposed method in the multiplayers environment. For example, can this algorithm make all agents satisfy their learning results? This can be shown by comparing the proposed method with FL using the local losses and the overall losses. It would also be better if some real datasets can be tested. The lack of clear performance metrics beyond relative error makes it difficult to assess the practical value of the proposed method. Specifically, the absence of comparisons with standard Federated Learning approaches using local losses and overall losses leaves a gap in understanding how the proposed method performs in a multi-agent setting. The experiments should demonstrate whether individual agents achieve their learning objectives, and real-world datasets would enhance the practical relevance of the results.

3. Writing needs to be polished. A thorough review of the abbreviation usage throughout the paper is needed, ensuring each term is defined only once and then used consistently thereafter. For example, Multiplayer Federated Learning (MpFL) appears 3 times in section 1 and 2 times in section 2. This would help improve the overall readability and professionalism of the paper.

### Questions
1. How the privacy of each agent's objective function is maintained if the master server is distributing all actions?  
2. Can you include comparisons of individual agent performance using local losses to show that all agents achieve their desired learning objectives or can you provide a metric or visualization that shows how well each agent's objectives are satisfied.
3. Consider adding experiments with real-world datasets to demonstrate practical applicability.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces a new setting, called Multiplayer Federated Learning (MpFL), in which each client does not share the same objective. More precisely, unlike the standard FL setting where the common objective is to minimize the average of all local losses, in MpFL, each client optimizes its own local loss, which depends on both the client’s model and the models of other clients. Given this setup, the goal is to converge to a Nash equilibrium and the authors propose PEARL-SGD, where each client computes the gradient of its local loss on its own model parameters and apply a (stochastic) gradient descend. The server collects and communicates the updated model parameters of all the clients without aggregating them. The authors analyse PEARL-(S)GD, studying cases with constant or decreasing learning rates, and demonstrate that it converges (sub)linearly to a Nash equilibrium (or a neighborhood of it) depending on the learning rate and the method chosen (SGD vs. GD). All theoretical results are derived under the assumptions of convex and smooth local loss functions. The authors validate their theory through two experiments simulating a 2-player and an n-player game.

### Strengths
- The paper is well-written and easy to read.
- The authors introduce MpFL, a new setting that may open up opportunities for future research.
- Convergence guarantee of PEARL-SGD to a Nash equilibrium for convex and smooth local losses.

### Weaknesses
 - The problem is technically interesting, but I am not convinced by the real-world motivations presented in the paper—specifically, the idea that banks (or pharmaceutical companies) would collaborate and learn together as competitors while maintaining their competitive edge. If these problems are indeed real, the proposed solution may not be well-suited. 
First, I find it unlikely that competing companies would be willing to share learning and potentially benefit a competitor, especially without guarantees that the collaboration would be mutually beneficial or at least better than learning alone. Secondly, given that this FL setting is now a multiplayer game where the clients are not from the same entity, expecting competitors to follow the same PEARL-SGD algorithm seems unrealistic. Any client might want to deviate from PEARL-SGD to take advantage over the competitors, or, if the collaboration does not give good results for one of the clients (since Nash equilibriums are not necessarly good for all), the client can simply sabotage the learning. While I find the MpFL setting very intriguing, PEARL-SGD seems incomplete without considering potential adversarial behavior from clients (or perhaps I am missing real-world cases where it cannot be the case?). At present, I struggle to see how this setting or algorithm aligns with a practical problem. Could the authors comment on this?

- The paper addresses only the case of convex functions (I consider this as a "weakness", but my primary concern lies with the first point).

### Questions
As said previously my main concerns lies in the motivation of the paper. I am willing to change my score if the authors could address this concern.

### Soundness
3

### Presentation
3

### Contribution
2
