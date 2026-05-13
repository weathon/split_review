# Exploring Large Action Sets with Hyperspherical Embeddings using von Mises-Fisher Sampling

- Decision: Reject
- Scores: 5, 5, 5, 6

## Abstract
This paper introduces von Mises-Fisher exploration (vMF-exp), a scalable method for exploring large action sets in reinforcement learning problems where hyperspherical embedding vectors represent actions. vMF-exp involves initially sampling a state embedding representation using a von Mises-Fisher distribution, then exploring this representation's nearest neighbors, which scales to virtually unlimited numbers of candidate actions.
We show that, under theoretical assumptions, vMF-exp asymptotically maintains the same probability of exploring each action as Boltzmann Exploration (B-exp), a popular alternative that, nonetheless, suffers from scalability issues as it requires computing softmax values for each action.
Consequently, vMF-exp serves as a scalable alternative to B-exp for exploring large action sets with hyperspherical embeddings. 
In the final part of this paper, we further validate the empirical relevance of vMF-exp by discussing its successful deployment at scale on a music streaming service. On this service, vMF-exp has been employed for months to recommend playlists inspired by initial songs to millions of users, from millions of possible actions for each playlist.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The authors propose to utilize the von Mises-Fisher (vMF) distribution to efficiently handle large action spaces in high-dimensional settings. The approach combines strong theoretical support with real-world validation, showcasing its effectiveness and practical applicability.

### Strengths
1. The authors presents a novel application of the von Mises-Fisher (vMF) distribution to efficiently explore large action spaces, improving scalability in high-dimensional environments.
2. The authors offers solid theoretical support, showing that the method achieves similar exploration efficiency to traditional approaches with lower computational costs.
3. Practical validation demonstrates the method’s relevance and potential for real-world impact

### Weaknesses
Novelty and Related Work: There is no section on related work to contextualize previous studies. I have noticed that some works[1-3] utilize Von Mises-Fisher or have a similar motivation to this work, especially [1,4]. Some of [1-3] employ vMF distribution to enable efficient, directed exploration in high-dimensional environments, aligning exploration toward relevant states or actions. Then by producing directionally aligned samples, vMF could find the optimal paths or guided trajectories, minimizing exhaustive search in large action spaces. I suggest the authors review this field and add more discussion of previous works to highlight this work’s unique contributions.

[1] APS: Active Pretraining with Successor Features. Hao Liu, Pieter Abbeel Proceedings of the 38th International Conference on Machine Learning, PMLR 139:6736-6747, 2021.

[2] Mecanna, Selim, Aurore Loisy, and Christophe Eloy. "Applying Reinforcement Learning to Navigation In Partially Observable Flows." Seventeenth European Workshop on Reinforcement Learning.

[3] Guo X, Chang S, Yu M, et al. Faster Reinforcement Learning with Expert State Sequences[J]. 2018.

[4] Zhu, Yiwen, et al. "vMFER: Von Mises-Fisher Experience Resampling Based on Uncertainty of Gradient Directions for Policy Improvement." arXiv preprint arXiv:2405.08638 (2024).

### Questions
Refer to the weaknesses.

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
This paper introduces a tailored exploration strategy for a unique setting where hyperspherical embedding vectors represent actions, and the number of possible actions can scale to millions. The paper is well-structured and offers a robust theoretical guarantee framework. The proposed method demonstrates improved scalability compared to B-exp.

### Strengths
Please see the questions

### Weaknesses
1.	While the approach is interesting, the novelty seems somewhat limited. The authors incorporate hyperspherical embedding vectors into reinforcement learning, with the exploration based on a nearest-neighbor (NN) method. This approach leverages existing techniques to address a domain-specific problem, which may make the technical novelty appear modest.
2.	The method assumes that action embeddings are i.i.d. and uniformly distributed vectors. This assumption could be challenging, particularly for the recommendation scenario in this study, where actions are often interdependent. Further examination or relaxation of this assumption might enhance applicability.
3.	The motivation for employing von Mises-Fisher (vMF) exploration could be elaborated. Clarifying why this approach is particularly suitable for this setting would strengthen the rationale behind the method.
4.	The experimental setup could benefit from additional information and a broader scope:
o	Since scalability in large action spaces is a key advantage of this method, providing details on the dataset—such as size and relevant statistics—would be informative.
o	Only one unpublished dataset is used without providing sufficient details. Given that the authors claim the method as a general solution for large action spaces, validating it on benchmark datasets or RL simulations would be valuable.
o	Information on any A/B testing would add context, and including offline test results could offer additional insights.
o	Expanding the comparison methods to include recent advancements in deep reinforcement learning, which can better model large state and action spaces, would create a more comprehensive evaluation to better position the contribution of this work.
5.	It would also be helpful to include further discussion on the method’s limitations, such as challenges related to deep reinforcement learning or considerations around the exploration-exploitation trade-off in reinforcement learning.

### Questions
1.	While the approach is interesting, the novelty seems somewhat limited. The authors incorporate hyperspherical embedding vectors into reinforcement learning, with the exploration based on a nearest-neighbor (NN) method. This approach leverages existing techniques to address a domain-specific problem, which may make the technical novelty appear modest.
2.	The method assumes that action embeddings are i.i.d. and uniformly distributed vectors. This assumption could be challenging, particularly for the recommendation scenario in this study, where actions are often interdependent. Further examination or relaxation of this assumption might enhance applicability.
3.	The motivation for employing von Mises-Fisher (vMF) exploration could be elaborated. Clarifying why this approach is particularly suitable for this setting would strengthen the rationale behind the method.
4.	The experimental setup could benefit from additional information and a broader scope:
o	Since scalability in large action spaces is a key advantage of this method, providing details on the dataset—such as size and relevant statistics—would be informative.
o	Only one unpublished dataset is used without providing sufficient details. Given that the authors claim the method as a general solution for large action spaces, validating it on benchmark datasets or RL simulations would be valuable.
o	Information on any A/B testing would add context, and including offline test results could offer additional insights.
o	Expanding the comparison methods to include recent advancements in deep reinforcement learning, which can better model large state and action spaces, would create a more comprehensive evaluation to better position the contribution of this work.
5.	It would also be helpful to include further discussion on the method’s limitations, such as challenges related to deep reinforcement learning or considerations around the exploration-exploitation trade-off in reinforcement learning.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
In this paper, the authors propose a new exploration strategy for reinforcement learning problems. I find the idea intriguing, but my primary concerns center on the evaluation of the proposed approach.

### Strengths
1. The topic of this paper is highly interesting.
2. The paper provides theoretical results.

### Weaknesses
1. Exploration is a key challenge in reinforcement learning, with wide-ranging applications in areas such as gaming and robotics.
2. While the paper discusses solutions for addressing high-dimensionality issues, it lacks empirical results to substantiate these claims.

### Questions
Sorry, I did not closely examine the mathematical derivations in this paper. I appreciate the authors’ contributions, particularly the theoretical results provided. However, my main concerns lie in the evaluation section of the paper. As the authors mention, exploration is a fundamental issue in RL. I would expect the authors to include simulations to empirically assess the exploration performance of their proposed technique. These simulations could involve game AI environments, such as those used in [1], or even synthetic data environments to provide a controlled setting for evaluation. Additionally, I strongly recommend comparing their approach with established RL exploration methods, such as count-based exploration [1] and reward-free exploration [2], as baselines.

[1] #Exploration: A Study of Count-Based Exploration for Deep Reinforcement Learning
[2] Reward-Free Exploration for Reinforcement Learning.

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
2

### Summary
Hyperspherical embeddings are increasingly important to represent actions in a variety of settings such as recommender systems (due to various convenient theoretical properties). This paper develops scalable methods to handle large action sets of hyperspherical embedding vectors in RL problems.

Although I'll admit this paper is well outside of my expertise, it does have proven success in terms of deployment on a large music platform, demonstrating that the method is indeed scalable and performant.

### Strengths
-- Strong theoretical basis of the described research.
-- Real, significant contribution in what's an important space. Hyperspherical embeddings are commonly used, and this paper provides a framework for using this in RL settings that other authors will likely follow up on.
-- Actually deployed at scale with much more by the way of "proven" success than most other papers.
-- Although the paper was admittedly mostly over my head, the presentation is very clear and walks the user through the relevant details quite clearly. It's certainly possible that I missed something, but I feel that my hand was sufficiently held.

### Weaknesses
 -- Certainly reads more like an industry paper: it is very hard to distill any real results from the experiments, or comparison to baselines etc. Statements like "this resulted in 11% more songs added to playlists than a reference cohort" obfuscates many details in order to hide the real results from readers. I understand this is a constraint when writing an industry paper, but I certainly don't like it!

-- Likewise, not much by way of real baselines, or really any experimental details.

-- Even though the presentation is good, I don't like a reader's chances of reproducing or comparing against what's written here, mainly due to the above reasons

### Questions
-- What are the chances of releasing code (sorry if I missed this)?

-- This paper is somewhat below the expected standards for reproducibility, even if strong in other ways. What's to stop you from, e.g., generating a synthetic data, or using a public dataset other than your own, just for the sake of reporting some real numbers (in addition to the "secret" numbers which you already report, but vaguely)? I think an ideal paper of this sort can combine both "secret" results with reproducible components, but this paper seems to fall short in that regard

### Soundness
4

### Presentation
4

### Contribution
4
