# Attention-Guided Contrastive Role Representations for Multi-agent Reinforcement Learning

- Decision: Accept
- Avg Score: 5.00
- Scores: 5, 3, 6, 6

## Abstract
Real-world multi-agent tasks usually involve dynamic team composition with the emergence of roles, which should also be a key to efficient cooperation in multi-agent reinforcement learning (MARL). Drawing inspiration from the correlation between roles and agent's behavior patterns, we propose a novel framework of \textbf{A}ttention-guided \textbf{CO}ntrastive \textbf{R}ole representation learning for \textbf{M}ARL (\textbf{ACORM}) to promote behavior heterogeneity, knowledge transfer, and skillful coordination across agents. First, we introduce mutual information maximization to formalize role representation learning, derive a contrastive learning objective, and concisely approximate the distribution of negative pairs. Second, we leverage an attention mechanism to prompt the global state to attend to learned role representations in value decomposition, implicitly guiding agent coordination in a skillful role space to yield more expressive credit assignment. Experiments on challenging StarCraft II micromanagement and Google research football tasks demonstrate the state-of-the-art performance of our method and its advantages over existing approaches.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces a method that combines a multi-head attention structure and the InfoNCE contrastive learning framework to enhance learning efficiency in MARL tasks by learning and utilizing role representations.

### Strengths
1.	The description of the methodology is clear and accurate.
2.	The performance of the experiments' results is really promising and impressive.
3.	The chapter of related works is rich and comprehensive.

### Weaknesses
1.	Extremely Lack of Experiments. There is a lack of experiments as the author only conducted experiments on 6 maps in SMAC. The same applies to the ablation experiments. Hope there will be additional experiments in a wider range of environments and on more maps within SMAC. Specifically, the limited number of scenarios makes it difficult to assess the generalization capability of the proposed approach. The choice of SMAC maps seems somewhat arbitrary, and it's unclear if these maps are sufficiently diverse to thoroughly evaluate the method's performance across different types of multi-agent coordination challenges.
2.	The author did not provide the source code to verify.
3.	There might be some errors in the analysis. Such as the analysis in Appendix D, there is room for debate regarding the phenomenon of sub-groups. It is incorrect to measure the distance between 2 points within 1 cluster in the original space based on their proximity in the t-SNE space. Evaluating the emergence of sub-groups should start from the original space rather than the two-dimensional space after t-SNE reduction. Similarly, after t-SNE reduction, the distance between clusters still does not reflect the real distance. Therefore, the conclusion of 'their role representations are still closer to each other' in the later part still requires the author's reconsideration. The reliance on t-SNE for analyzing cluster structure is problematic because t-SNE is primarily a visualization technique and does not preserve distances or densities in the original high-dimensional space. This makes any conclusions drawn from the t-SNE plots questionable.
4.	The relationship between the two parts, MHA and CL, in the article is not particularly close; they seem more like two relatively independent components. The integration of the multi-head attention (MHA) mechanism and contrastive learning (CL) framework appears somewhat superficial. The paper does not provide a strong justification for why these two components are necessary to work together, and it's not clear how they interact to achieve the claimed improvements in learning efficiency. The MHA seems to be used for credit assignment, while CL is used for role representation, and the connection between these two is not well-established.
5.	There are some typos and the writing of the paper needs some improvement.

### Questions
1.	In Fig 4. (c), both Agent 5 and 8 are 'Dead Marines'. Why are they clustered into different classes?
2.	Why was a new map, 2s3z, introduced for the experiments in MAPPO? Why not directly use the previously employed 3s5z_vs_3s6z map? I would like to see an additional MAPPO experiment on 3s5z_vs_3s6z.
3.	How is the setting cluster_num = 3 applied on the map 2c_vs_64zg when there are only 2 agents available for control on this map? Besides, why didn't the performance decline since it forces the strategies of each agent to diverge as same as the experiment about cluster_num = 5 applied on the map 5m_vs_6m?
4.	In the derivation, both the approximation and logK indicate that a larger value of K yields better results. The experiments conducted in the selected maps have a limited number of agents. It is suggested to have more agents and experiment with larger values of K. For example, experiments with larger K values, such as K=2, 4, 8, 16, can be run in scenarios like 30m and bane_vs_bane.
5.	The paper doesn't explicitly clarify the difference between clustering directly on agent embeddings and on role representations. As it considers role representations to be more discriminative, it's important to further elucidate the necessity of obtaining discriminative representations through contrastive learning.
6.	The model has been added with a global state GRU and a MHA structure. Therefore it increase the number of parameters of the networks. It is recommended to conduct ablation studies with the same network size.

Minor: Bigger size of networks and additional contrastive learning procedure may limit the application. The theoretical derivation of Theorem 1. is very similar to previous work.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces the ACORM framework, which utilizes mutual information maximization to formalize role representation learning through a contrastive learning objective. It also incorporates an attention mechanism to encourage the global state to attend to learned role representations.
Empirical evaluations carried out on SMAC scenarios demonstrated that ACORM surpasses the performance of baseline methods. Additionally, visualizations and ablation studies show the pivotal roles played by the contrastive role representation and attention mechanism in this task.

### Strengths
* The proposed ACORM framework integrates representation learning, encoding the trajectory history from the traditional framework into a latent variable z. This representation associated with the role is learned through clustering and using positive-negative samples.
* Compared to the traditional framework, the global state used incorporates role-related representations through an attention mechanism.

### Weaknesses
 * **Novelty and Reliability**: ACORM is not the first work to introduce the attention mechanism in the mixing network. For instance, works like [Qatten](https://arxiv.org/pdf/2002.03939.pdf) have introduced certain constraints in the network to satisfy the IGM principle. However, this paper does not provide evidence of complying with the IGM principle or any explanations. The use of attention, while beneficial, appears to be a relatively straightforward application without significant novel modifications to the mechanism itself. The paper does not delve into the specific challenges of applying attention in this context, such as potential instability or sensitivity to hyperparameters, which would strengthen the contribution.
* **Experimental Evaluation**: The experiments in the article are conducted solely on SMAC. To my knowledge, various versions of SMAC exist, and different algorithm implementations often involve custom modifications to this environment. Relying solely on SMAC for experiments may not be sufficiently persuasive. It might be beneficial to include experiments from other environments such as GRF and Ma-MuJoCo. The lack of diversity in environments raises concerns about the generalizability of the findings. Furthermore, the paper does not include a detailed analysis of the computational cost or efficiency of ACORM, which is important for practical applications.
* **Reproducibility**: The supplementary materials do not include the source code, making reproducibility uncertain.

### Questions
* As previously mentioned, ACORM does not impose constraints on the attention mechanism, and it even utilizes the learned latent variable $z$. How can we ensure its correct execution under the CTDE paradigm?
* Regarding the analysis of Contrastive role representation, Figure 4 is not particularly convincing:
    * In subfigure (b), *(0) is even further from other points in its cluster compared to *(5). While I understand that clustering is done in higher dimensions, this example can be confusing.
    * While it's claimed that the role representation better forms coordination teams, in actuality, in subfigure (b) and (c), it seems just the agent embedding alone might suffice.
* Additional experiments are needed to bolster the paper's persuasiveness.
* The supplementary materials do not include the source code, making reproducibility uncertain.

I would like to raise my score if my concerns are addressed.

### Soundness
3 good

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
This paper proposes a novel framework of attention-guided contrastive role representation learning for multi-agent reinforcement learning, ACORM. On the one hand, the role representation of each agent is inferred from the agent embedding through contrastive learning and clustering algorithms. On the other hand, the paper introduces an attention mechanism in value decomposition to enhance agent coordination in the role space. By introducing the above two contributions, ACORM performs better than other role-based multi-agent reinforcement learning algorithms in the SMAC environment. The paper also has intuitive visualizations to illustrate the role of the corresponding modules.

### Strengths
1. The paper is well-organized and easy to understand.
2. The experimental part has detailed case studies, which is very important for understanding the role of the two modules proposed in the paper. The figures about the t-sne embedding or weights corresponding to each snapshot have reasonable analysis.
3. The proposed framework is suitable for reinforcement learning algorithms based on value functions and those based on policy gradient. The relevant algorithms have been tested on SMAC and show that the ACORM variant is much better than the vanilla algorithm.
4. The proof of the ELBO is given in the appendix, which is correct to me and improves the soundness of the submission.

### Weaknesses
1. In cooperative multi-agent reinforcement learning, inferring the role of an agent based on its trajectory is not a novel method and has been proposed in many previous works [1, 2]. Moreover, none of the above-mentioned important papers are cited in the paper.
2. The number of baselines used for comparison with ACORM is relatively tiny. Why not use CDS [3] as a baseline, since you mentioned it in the paper?
3. SMAC is a relatively old multi-agent testbed. Recently, it has been pointed out that it has a series of problems [4]. I am not against the author evaluating the performance of the algorithm on SMAC, but I feel that the performance of the algorithm should be tested in multiple different domains. Many environments, such as the Google Research Football [5] mentioned in the paper, can be used to enhance the credibility of experimental results.
4. Ablation experiments are insufficient. Compared with the vanilla QMIX, ACORM_w/o_MHA still has an additional MLP and GRU for the global state. One wonders whether what really works is just the representation learning of the state trajectory before input to the Mixing Network.
5. It is not possible to reproduce the results from the description given in the paper. Some key details (such like $T_{cl}$) are unclear, and some key resources (code) are not furnished.

### Questions
Please see the questions in the weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a method of attention-guided promotion (incorporating attention mechanisms in the global state to participate in value decomposition) to maximize mutual information to formalize role representation and derive a contrastive learning objective function. ACORM choose the StarCraft multi-agent challenge (SMAC) benchmark and achieves state-of-the-art performance on most hard and superhard maps.

### Strengths
Using mutual information to distinguish roles

The experiment was conducted on a difficult map in StarCraft

The experimental diagram is very detailed

### Weaknesses
There is no reasonable explanation or formula for the promotion of credit assignment  by attention, and the paper only demonstrates the effectiveness of the method through experiments. The paper lacks a clear theoretical justification for why attending to role representations should improve credit assignment in the mixing network. While the experiments show improved performance, it's unclear if this is a direct result of the attention mechanism or other factors. The paper does not provide a rigorous analysis of how the attention weights are learned and how they influence the mixing network's behavior. It is also not clear how the learned role representations are disentangled from the global state, and whether the attention mechanism is truly capturing distinct role information or simply overfitting to the training scenarios. Furthermore, the experiments could benefit from additional ablation studies to isolate the impact of the attention mechanism from other components of the model.

### Questions
1. Does GRU encoding S play a more significant role in the effect ?

2. How do you know the state encoding after this attention, input to the mix network can have an impact on credit assignment ?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
