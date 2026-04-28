# Multi-Task Learning for Routing Problem with Zero-Shot Generalization

- Decision: Reject
- Avg Score: 5.75
- Scores: 3, 8, 6, 6

## Abstract
Vehicle routing problems (VRPs), which can be found in numerous real-world applications, have been an important research topic for several decades. Recently, the neural combinatorial optimization (NCO) approach that leverages a learning-based model to solve VRPs without manual algorithm design has gained substantial attention. However, current NCO methods typically require building one model for each routing problem, which significantly hinders their practical application for real-world industry problems with diverse attributes. In this work, we make the first attempt to tackle the crucial challenge of cross-problem generalization. In particular, we formulate VRPs as different combinations of a set of shared underlying attributes and solve them simultaneously via a single model through attribute composition. In this way, our proposed model can successfully solve VRPs with unseen attribute combinations in a zero-shot generalization manner. Extensive experiments are conducted on eleven VRP variants, benchmark datasets, and industry logistic scenarios. The results show that the unified model demonstrates superior performance in the eleven VRPs, reducing the average gap to around 5\% from over 20\% in the existing approach and achieving a significant performance boost on benchmark datasets as well as a real-world logistics application.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a unified model for solving routing problems with cross-constraints in a zero-shot manner. The model is based on multi-task learning and can effectively solve VRPs with different underlying attributes. The authors compare the performance of their model to single-task models trained specifically for each problem and show that their approach outperforms these models. The potential real-world applications of this approach to solving VRPs are also discussed.

### Strengths
1. The paper proposes a novel approach to solving VRPs using a unified model based on multi-task learning, which can effectively solve diverse VRPs in a zero-shot manner.
2. The authors provide experimental results on eleven VRPs to demonstrate the effectiveness of their approach. They compare the performance of their model to single-task models trained specifically for each problem and show that their approach outperforms these models.

### Weaknesses
 1. The paper seems to simply add some VRP attributes as input to POMO and introduce an REINFORCE loss as multi-task loss. The novelty and contribution are relatively low. More analysis on the relations and effects of learning different tasks is expected. 
 2. In Table 2, the performance of LKH3 should be given for VRP variants except for CVRP. 
 3. The problem scale is relatively small, only up to 100. 
 4. In Table 3, for evaluation results on VRPBTW, POMO-VRPTW outperforms the proposed method. The result is not logical since the proposed method learns more features and information but leading to inferior performance in comparison with POMO-VRPTW. More analysis on this result is expected. 
 5. For all the VRP variants in Table 2 and Table 3, the baselines may not include all the corresponding state-of-the-art methods for multiple problems.

### Questions
1. How do different VRP attributes collaborate in the learning process?
2. Are the baseline methods in Table 1 and Table 2 are. the state-of-the-art methods for all VRP variants?
3. How does the proposed method perform on more large-scale problems?
4. Is the proposed method model-agnostic to other neural methods?
5. How does the proposed method encounters unseen attributes? Could the method be adapted quickly to new attributes with relatively small training samples?

### Soundness
1 poor

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a novel learning-based method to tackle cross-problem generalization in vehicle routing problems (VRPs), where the VRP variants are regarded as different combinations of a set of shared underlying attributes and solved by multi-task reinforcement learning. The experiments show the promising performance on unseen VRPs.

### Strengths
Cross-problem generalization is an important challenge for neural combinatorial optimization. This paper is an inspiring attempt at this leading direction.

### Weaknesses
A fly in the ointment is that the proposed method might be a little simple. Thus, I encourage the authors to explore more contributions on the methodology, so as to further improve the performance.

1. This paper emphasizes zero-shot generalization, e.g., in the title. More discussions in experiments refer to fine-tuning, which seems to be inconsistent with the “zero-shot”. It is better to give more descriptions about this point.
2. As illustrated, different VRPs need to use different masking mechanisms to handle constraints. If a VRP variant is very complex, would it be hard to design a masking mechanism? Or even would there be some complex constraints that cannot be handled directly by masking?
3. Some typos still exist, such as the beginning of Section 3 and the reference “Select and optimize: Learning to aolve large-scale tsp instances”. Please check carefully.

### Questions
1. This paper emphasizes zero-shot generalization, e.g., in the title. More discussions in experiments refer to fine-tuning, which seems to be inconsistent with the “zero-shot”. It is better to give more descriptions about this point.
2. As illustrated, different VRPs need to use different masking mechanisms to handle constraints. If a VRP variant is very complex, would it be hard to design a masking mechanism? Or even would there be some complex constraints that cannot be handled directly by masking?
3. Some typos still exist, such as the beginning of Section 3 and the reference “Select and optimize: Learning to aolve large-scale tsp instances”. Please check carefully.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work focuses on multi-task learning for vehicle routing problems. It proposes to build a unified model to solve these related problems in an end-to-end way, which is extended from the attention model with a unified encoder-decoder framework and attribute composition. Experiments prove the effectiveness of the proposed method.

### Strengths
1. The proposed multi-task solution for the routing problem is promising and could benefit downstream tasks.
2. The whole framework is well presented with good writing.
3. Experiments prove effectiveness on several problems.

### Weaknesses
I'm not an expert on vehicle routing. And I list my concerns here for reference.

This work adopts multi-task learning to solve various problems. Are there any related tasks or conflict tasks that are affected by this paradigm? I cannot find any discussion on it.

### Questions
Please refer to the weakness section.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a unified neural model based on multi-task learning for solving various VRPs. The underlying structure includes encoder, decoder, and attribute composition block. The experiments are conducted on 11 VRP variants, and showed effectiveness against the selected baseline methods.

### Strengths
1- The writing is good, and the paper is easy to follow;
2- This paper is well-motivated;
3- It is evaluated on eleven VRP variants.

### Weaknesses
1- While this work is well motivated, there is no novelty from the methodology perspective. It seems like simple adaption of multitask learning and AM. Although the authors claim the attribute composition is novel, it looks quite naive and trivial.
2- The baseline POMO is classic, but not the SOTA. Quite a number of subsequent works surpass it, such as Efficient Active Search and 'Simulation-guided Beam Search for Neural Combinatorial Optimization'. In this sense, the comparison is not that convincing.
3. Although the authors reviewed and criticized 'Efficient Training of Multi-task Combinarotial Neural Solver with Multi-armed Bandits', it is the most relevant baseline to this paper. It is good to compare with it in some adapted or tailored experimental settings.
4. In table 2, where the proposed method is inferior to other neural baselines should be analyzed and explained.
5. In table 3, the generic traditional methods like LKH-3 and OR-tools should be included.
Overall, the methodological novelty and the experimental results are not significant.

### Questions
Please see the above Weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
