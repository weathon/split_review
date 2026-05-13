# Incentivized Collaborative Learning: Architectural Design and Insights

- Decision: Reject
- Scores: 3, 5, 5

## Abstract
Collaborations among various entities, such as companies, research labs, AI agents, and edge devices, have become increasingly crucial for achieving machine learning tasks that cannot be accomplished by a single entity alone. This is likely due to factors such as security constraints, privacy concerns, and limitations in computation resources. As a result, collaborative learning (CL) research has been gaining momentum. However, a significant challenge in practical applications of CL is how to effectively incentivize multiple entities to collaborate before any collaboration occurs. In this study, we propose ICL, an architectural framework for incentivized collaborative learning, and provide insights into the critical issue of when and why incentives can improve collaboration performance. Then, we apply the concepts of ICL to specific use cases in federated learning, assisted learning, and multi-armed bandit, corroborated with both theoretical and experimental results.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work investigates incentivized collaborative learning where there are candidates that are potentially looking into joining the federation, the participants who will get the reward from the actual outcomes of the collaboration, and the active participants who participate in the training. The work defines a coordinator who orchestrates the participation of the clients and the pricing plan and profit, and depending on these components, propose to maximize the system-level profit under constraints of individual clients' incentives. The work investigates different use cases of the proposed incentivized collaborative learning framework along with analysis on robustness and accuracy.

### Strengths
- The work investigates an interesting area in collaborative learning regarding client incentives and monetary compensations and cost analysis. The work proposes a framework for incentivized collaborative learning where federated learning, assisted learning, and MAB all come under their umbrella.

- The work provides theoretical results, although limited to specific scenarios such as the three-entity setting. 

- The work evaluates their framework under robustness against byzantine attacks and scenarios where there are both competing and non-competing clients.

### Weaknesses
 - A major concern I have over the work is that in stage 1 of the method, the coordinator needs to set a pricing plan based on prior knowledge of candidates potential gains from previous rounds. This means that first the client needs to participate first to know its incentives, and moreover, if the potential gain is erroneous, the ICL framework may not be able to properly incentivize the clients. This becomes even more trickier when clients have the flexibility to opt-in or opt-out which can often be the case for incentivized collaborative learning settings.

- Another concern I have is that the work did not compare their method against other relevant work for incentivization in collaborative learning such as 
 [1] Yae Jee Cho, Divyansh Jhunjhunwala, Tian Li, Virginia Smith, and Gauri Joshi. To federate or not to federate: Incentivizing client participation in federated learning. arXiv preprint arXiv:2205.14840, 2022. 
[2] Avrim Blum, Nika Haghtalab, Richard Lanas Phillips, and Han Shao. One for one, or all for all: Equilibria and optimality of collaboration in federated learning. In International Conference on Machine Learning, pp. 1005–1014. PMLR, 2021. 
[3] Rachael Hwee Ling Sim, Yehong Zhang, Mun Choon Chan, and Bryan Kian Hsiang Low. Collaborative machine learning with incentive aware model rewards. In International Conference on Machine Learning, pp. 8927–8936. PMLR, 2020.
Especially for parts of the work such as 3.1.1 which aims for large participation approximation works like [1] seem relevant and other parts such as section 3.2, [2,3] seems relevant. It seems strange to me that the work does not compare their work with such relevant line of work.

- Lastly, the work seems mainly theoretical since the experimental validation is rather limited. However, the assumptions they use for the theoretical work such as having a three entity setting is rather restrictive. Moreover the implications of the main theoretical results such as Theorem 2 and 4 is unclear to me. In what conditions it is guaranteed that the clients benefit from the system for each corresponding theorems?

### Questions
See weaknesses above.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Starting from the significant challenge of collaborative learning, this paper aims to solve how to effectively motivate multiple entities to collaborate before any collaboration occurs. And proposed ICL framework. This work elaborates on the roles, processes, and principles of the games used in the framework, and proved the effectiveness of ICL through mathematical derivation. By using different pricing or selection plans in the experiments, the authors discussed how incentive settings affect the effectiveness of the framework.

### Strengths
1.	The authors proposed a clear incentivized collaborative learning framework, along with detailed descriptions of the roles and principles of ICL.
2.	The authors gave sufficient and detailed mathematical derivation to prove the effectiveness of ICL.
3.	Many experiments were conducted to validate the effectiveness of the proposed ICL framework and analyse the influences from pricing and selection plans.

### Weaknesses
1. The discussion in the paper cannot fully reflect the superiority of the proposed framework compared to previous methods. For example, there seems no specific comparative experiment to confirm that the proposed ICL framework is more efficient than previous works.
2. It’s kind of confusing that the description of the experiements is less detailed about their design. For example, the employed model and the meaning of the metrics in the first experiment are not very clear.
3. Experiment settings are kind of insufficient to support all the contributions, such as the discussion about the influences from the selection plans, while most of the selection plan is based on Bernoulli distribution. The discussion about how to select appropriate pricing and selection plans is also insufficient.

### Questions
1.	Can you give more explicit evidences that the proposed ICL framework utilizes the incentive mechanism more effectively than previous works?
2.	I wish the experiment settings can be more detailed written in the main body of the paper.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes an architecture framework for collaborative learning with the aim of incentivizing collaboration among multiple entities while maximizing the utility of the coordinator. The framework is realized by formulating a pricing plan, which determines participants’ participation cost, and a selection plan, which selects active participants to determine the collaboration outcome. The conditions of Nash equilibriums and also the optimization objectives for the system are derived in the paper. The authors have also empirically shown the versatility of the framework by applying it to three concrete learning scenarios of interests, including federated learning, assisted learning and multi-armed bandits.

### Strengths
1. The motivation considering the incentives of both the coordinator/system and the participants is sound.
2. The framework includes important stages of the incentivized learning pipeline, such as pricing, selection and rewarding, which is rather comprehensive.
3. The paper has shown the application to three scenarios to incentivize FL, AL and MAB and presented empirical evidence for the effects of pricing and selection designs in the framework.

### Weaknesses
1. The novel contributions and the new insights from the unified framework need further clarification. The paper presents a general framework for incentivized collaborative learning, but it's not immediately clear what new understanding or capabilities this framework provides beyond existing approaches. The core concepts of Nash equilibrium and individual rationality constraints, along with the goal of maximizing system utility, are already well-established in the literature. While the framework aims to unify these concepts, the paper needs to more clearly articulate what novel insights arise specifically from this unification that could not be observed otherwise. The claim of mutual benefit between the coordinator and participants also requires more substantial justification, as this is not a novel concept in itself.
2. The pricing plan formulation and its dependency on the individual outcomes of active and non-active participants is not clearly elaborated in the paper. The pricing plan $\mathcal{P}$ is defined based on the realized collaboration gain from the outcomes of active participants $I_A$, and it charges all participants in $I_P$. However, the paper does not sufficiently explain how the pricing differentiates between participants with high $z_m$ (high contribution) and those with low $z_m$ (low contribution). The dependency of pricing for non-active participants on the individual gains $z_m$ of active participants, as stated in (1), is also not clearly justified. It is unclear why the pricing of non-active participants should be directly linked to the individual gains of active participants, and this aspect needs further clarification.
3. The incentive of participation for a participant $m$ is solely based on their own utility income minus participation cost, as defined by (9). This formulation does not account for the influence of other participants' potential gains on an individual's decision to participate. In practice, a candidate's incentive to participate may be affected by the expected gains of other candidates, especially if they perceive others to have higher potential gains with lower-quality data. This aspect of competitive incentive is not addressed by the framework.
4. The paper states that inactive participants will have zero gain, which contributes to the system's profit without harming the collaboration. This statement is confusing because all participants are said to receive $z_{I_A}$, and an inaccurate candidate might still experience a large utility income gain. This needs clarification.
5. The paper lacks clarity on how Theorem 1 translates to functional forms of the pricing plan in practice. While the theorem provides conditions for the pricing plan, the paper does not provide sufficient details on how these conditions can be used to derive concrete pricing functions in practical scenarios. The connection between the theoretical results and practical implementation is not well-established.
6. The assumption that the system knows the utility functions of the candidates for pricing and selection is not well-justified. The paper does not address the practical challenges of obtaining or approximating the utility functions of participants. Furthermore, the calculation of $E [ \mathcal{U}(z_{I_A}) - \mathcal{U}(z_m) ]$ is not explained in sufficient detail, especially given that the utility functions are not assumed to be known.
7. The paper mentions that the optimized selection plan will not select entities with low potential contributions, but the main text only describes randomized selection. The selection plans that make decisions based on prices or local gains are not clearly described, and the connection between the optimized selection plan and the randomized selection is not well-defined.
[Minor]
1. The collaborative gain function $\mathcal{G}$ should not take an individual $z_m$ as input, since $z_m$ should depend on the outcomes of other active participants in $I_A$.
2. Some notations are confusing. For example, $I_P = Incent_m (\mathcal{P})$, here $I_P$ is a set while $Incent_m()$ outputs whether a client $m$ is incentivized to participate.

### Questions
1. This work proposes a grand framework with abstract terminologies that unifies existing formulations for the incentivization problem into a unified framework. However, what are the new insights that can be derived because of this unification and cannot be observed otherwise? I can see that the work still mainly relies on deriving Nash equilibriums with individual rationalities (IR) constraints, and strives to maximize some system utility (maybe more flexible with hyperparameters). These concepts are commonly seen in the existing literature that the authors have cited. And mutual benefits of the coordinator (or, system) and the participants (or, clients) are not rare in existing works, either. Therefore, I wonder what are the new insights? This point is important to assess the significance of this paper.
2. Could you elaborate on the specific meaning and implications of “prior works has often focused on designing an incentive as a separate problem based on an existing collaboration scheme, instead of treating incentive as part of the learning itself”? This is stated at the end of the “Related Works” section.
3. The pricing plan $\mathcal{P}$ looks at the realized collaboration gain from the outcomes of the active participants in $I_A$ to charge all participants in $I_P$. Does the pricing differentiate participants with high $z_m$ from those with low $z_m$?
4. It appears strange to me that the pricing for the non-active participants depends on the individual gains of the active participants $z_m$, stated in (1). Please correct me if I am mistaken.
5. Under the formulation of this paper, the incentive of participation for $m$ only depends on the utility income of $m$ himself minus the participation cost. This means that the client is incentivized as long as (9) is fulfilled. However, in practice, a candidate’s incentive should also depend on other candidates. For example, knowing that others have a higher expected gain with lower-quality data can deter participation. How does the framework address this scenario?
6. Clarification: At the end of Page 5, it is stated that “if not selected, it will become an inactive participant with zero gain, which will contribute to the system’s profit but not harm the collaboration.” Why would the gain be zero? All participants will receive $z_{I_A}$ and there might be a large utility income gain for this “inaccurate candidate”. 
7. How does Theorem 1 translate to functional forms of the pricing plan in practice?
8. Why is it acceptable and reasonable to assume the utility functions (e.g., utility income $\mathcal{U}$) of the candidates are known to the system for pricing and selection? Also, how practical is it to calculate $E [ \mathcal{U}(z_{I_A}) - \mathcal{U}(z_m) ]$?
9. It was mentioned in Remark 5 that “if following the above-optimized selection plan, will not select it as active”. However, I could not find descriptions in the main text about the selection plans that make a decision based on the prices $\mathcal{P}_m$ or local gain $z_m$. I only see descriptions about randomized selection. Could you point me to the relevant sections or elaborate here?

[Minor]
1. Better not to overload the collaborative gain function $\mathcal{G}$ to take an individual $z_m$ as input, since $z_m$ should also depend on the outcomes of other active participants in $I_A$?
2. Some other notations are confusing. For example, $I_P = Incent_m (\mathcal{P})$, here $I_P$ is a set while $Incent_m()$ outputs whether a client $m$ is incentivized to participate.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
