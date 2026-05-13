# Performant, Memory Efficient and Scalable Multi-Agent Reinforcement Learning

- Decision: Reject
- Scores: 3, 6, 6, 6

## Abstract
As the field of multi-agent reinforcement learning (MARL) progresses towards larger and more complex environments, achieving strong performance while maintaining memory efficiency and scalability to many agents becomes increasingly important. Although recent research has led to several advanced algorithms, to date, none fully address all of these key properties simultaneously. In this work, we introduce Sable, a novel and theoretically sound algorithm that adapts the retention mechanism from Retentive Networks to MARL. Sable's retention-based sequence modelling architecture allows for computationally efficient scaling to a large number of agents, as well as maintaining a long temporal context, making it well-suited for large-scale partially observable environments. Through extensive evaluations across six diverse environments, we demonstrate how Sable is able to significantly outperform existing state-of-the-art methods in the majority of tasks (34 out of 45, roughly 75\%). Furthermore, Sable demonstrates stable performance as we scale the number of agents, handling environments with more than a thousand agents while exhibiting a linear increase in memory usage. Finally, we conduct ablation studies to isolate the source of Sable's performance gains and confirm its efficient computational memory usage. Our results highlight Sable's performance and efficiency, positioning it as a leading approach to MARL at scale.\footnote{All experimental data and code will be made available soon.}

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents Sable, an approach based on a modified Retentive Network (RetNet) architecture that leverages attention mechanisms with a retention-based memory management approach. It is shown to improve the memory efficiency of MARL and scale well to large number of agents.

### Strengths
+ The proposed Stable considers MARL as a sequence modeling problem and leverages Retentive Networks. It is able to maintaining a long temporal context and leads to efficient memory usage.

### Weaknesses
While I like the idea presented in this paper, there are many issues with the experiments and evaluation.
- Formulating MARL as a sequence modeling problem has been an active area of research. The authors have cited (Wen et al., 2022) and  (Kuba et al., 2021). But since IPPO was considered as a main baseline, why not also consider baselines like independent decision transformers and other sequence modeling approaches? Further, there are also many decomposition based MARL algorithms that outperform QMIX (e.g., weighted-QMIX, FOP, DOP, PAC) and mean-field based MARL algorithms. These should not be ignored in the evaluation. 
- In Figure 1 - Middle, while the authors claim that Stable is more throughput efficient, but it is only 6.5x, compared to 45x by IPPO.
- In Figure 1 - Right, IPPO is 9x but the bar is much lower than Stable that is 7x. 
- In Figure 4, IPPO seems to consistently have lower memory usage than Stable. Doesn't it conflict with the main claim of the paper?
- In Table 1,  MASAC, HASAC, and QMIX have many missing return values. It is hard to believe these algorithms don't work in these environments.
- The comparison with baseline algorithms need to cover more complex MARL tasks with continuous action/state spaces, like Starcraft and MuJoCo, which are used by many of the baselines.
- Table 1 summarizes the return comparison with baselines. Since the main advantage of Stable is memory efficiency, a similar table on memory comparison should be provided. 

Further, the authors claim that Sable provides "theoretically grounded convergence guarantees". But I was not able to find any analysis or proofs in the paper. It simply cited (Kuba et al., 2021). It is unclear how it applies here.

### Questions
Please address my questions in the weakness section.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces Sable, a novel algorithm for multi-agent reinforcement learning (MARL) that aims to achieve strong performance, memory efficiency, and scalability. Sable adapts the retention mechanism from Retentive Networks to MARL, allowing for computational efficiency and the ability to maintain long temporal contexts. The authors demonstrate that Sable outperforms several state-of-the-art methods across diverse environments.

### Strengths
1. This paper introduces a novel approach by adapting retention mechanisms for multi-agent reinforcement learning (MARL), representing a creative solution to enhance memory efficiency and scalability as the number of agents increases. The experimental results are particularly impressive.

2. The study includes a comprehensive set of experiments encompassing six commonly used MARL environments and a total of 45 tasks. The results demonstrate robust performance, indicating that Sable significantly outperforms existing methodologies in 34 out of 45 tasks. Furthermore, the approach exhibits stability with over a thousand agents, which is a critical consideration for large-scale applications.

### Weaknesses
The related work section is insufficiently comprehensive, primarily focusing on recurrent nets and Transformers. It would be beneficial to include more detailed discussions on specific algorithms in multi-agent reinforcement learning (MARL). In the MABrax environment, the performance of Sable is significantly worse compared to other environments. A more in-depth analysis and discussion of the reasons for this disparity would be highly valuable.

### Questions
1. Table 1 is too small, affecting the overall aesthetics and clarity of the presentation. Could the structure be adjusted or some content trimmed to enhance its visual appeal and readability?

2. The ablation study fails to pinpoint the main design elements that influence Sable's performance. Although the modified MAT shows some improvement, it still falls short compared to Sable. Further analysis and experimentation would likely be beneficial for the community to effectively reuse these insights.

3. In Figures 4b, 4c, and 4d, the final reward continues to increase as the number of agents increases. I would like to understand the reason behind this because usually the performance will decrease as the number of agents increasing.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper begins by analyzing the broad categorization of current MARL approaches and addresses the issues of high computational and memory resource costs and the lack of capability to capture historical information in MAT. Inspired by Retention, the paper adapts the Retention architecture for MARL, introducing the Sable method. This method maintains high computational efficiency and low memory consumption while supporting a large number of agents, and it leverages historical knowledge to improve policy learning. The paper concludes with a comparison of SOTA models in the MARL domain across multiple environments, achieving excellent results that thoroughly validate the algorithm's performance. Overall, this paper mitigates the problems inherent in traditional MAT methods and proposes a new, efficient MARL architecture, providing a fresh direction and approach for research in this field.

### Strengths
1. The introduction succinctly outlines the general classification of MARL methods and their limitations, while also identifying the issues with current SOTA methods. This leads smoothly into the presentation of the paper's method and its advantages, ensuring a coherent flow and quick understanding of the current state of MARL and the paper's contributions.
2. Building on the shortcomings of previous MAT methods, the paper innovatively proposes the Sable method by adapting the Retention architecture to RL algorithms. This adaptation results in a method with lower computational and memory costs, scalability to a large number of agents, and the ability to incorporate historical observations for better policy learning. The method also provides new research directions and theoretical foundations for the MARL domain.
3. The paper conducts experiments in several classic and challenging environments, comparing multiple SOTA models in the MARL domain. The extensive experimental results demonstrate the effectiveness of the algorithm, and additional experiments with varying numbers of agents confirm its computational and memory efficiency.

### Weaknesses
1. The Related Work section lacks a thorough introduction to some classic MARL algorithms, which would help readers unfamiliar with the field understand the broader development and methodologies in MARL.
2. While the Introduction directly addresses the classification of MARL methods and their current limitations, it could benefit from more foundational background information to better contextualize the motivation and overall method design for readers.

### Questions
1. Can the method adapt to changes in the number of agents or significant variations in observation while maintaining the robustness of the overall policy?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a novel and theoretically sound algorithm Sable, adapting the retention mechanism from retentive networks to MARL. The authors demonstrate that Sable ranks first in 34 out of 45 tasks (roughly 75%), outperforming SOTA MARL algorithms across 6 environments: RWARE, LBF, MABrax, SMAX, Connector and MPE. Meanwhile, the advancements of Sable in memory efficiency and agent scalability are significant.

### Strengths
1. The motivation is well justified, the method is reasonable.
2. The problems are practical and relevant to the large-scale MARL community.
3. Well-written paper with comprehensive results reported.
4. Authors provide several experimental details and corresponding code on their proposed algorithm.

### Weaknesses
While I lean towards acceptance, I have a few concerns. I am willing to raise my score if the authors can resolve my concerns and questions.
1. The novelty of Sable should be further clarified, stating how it builds upon, differs from, and improves upon existing methods, and so on.
2. As stated in the abstract, “In this work, we introduce Sable, a novel and theoretically sound algorithm that adapts the retention mechanism from Retentive Networks to MARL.” Where is the theoretical convergence guarantee analysis in the main text?

### Questions
I have asked my questions in the Weaknesses section. I have no further questions.

### Soundness
3

### Presentation
3

### Contribution
2
