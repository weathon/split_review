# Enhancing the Cross-Size Generalization for Solving Vehicle Routing Problems via Continual Learning

- Decision: Reject
- Avg Score: 5.67
- Scores: 6, 5, 6

## Abstract
Deep models for vehicle routing problems are typically trained and evaluated using instances of a single size, which severely limits their ability to generalize across different problem sizes and thus hampers their practical applicability. To address the issue, we propose a continual learning based framework that sequentially trains a deep model with instances of ascending problem sizes. Specifically, on the one hand, we design an inter-task regularization scheme to retain the knowledge acquired from smaller problem sizes in the model training on a larger size. On the other hand, we introduce an intra-task regularization scheme to consolidate the model by imitating the latest desirable behaviors during training on each size. Additionally, we exploit the experience replay to revisit instances of formerly trained sizes for mitigating the catastrophic forgetting. Extensive experimental results show that the proposed approach achieves predominantly superior performance across various problem sizes (either seen or unseen in the training), as compared to state-of-the-art deep models including the ones specialized for the generalizability enhancement. Meanwhile, the ablation studies on the key designs manifest their synergistic effect in the proposed framework.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a learning-based approach for vehicle routing problems that aims to learn models that generalize well across instances of different problem sizes. The method uses a continual learning scheme that sequential trains the model with instances of ascending sizes. Furthermore, the method uses the following new components to improve the generalization performance: 1) An inter-task regularization scheme and intra-task regularization scheme that aim to retain knowledge from earlier training phases. 2) An experience replay mechanism that revisits smaller instances from earlier training phases. The authors train models for the TSP and CVRP on instances with 60 to 150 nodes and evaluate them on instances with 60, 100, 150, 200, 300 and 500 nodes. The experiments show that their approach generalizes well to instances with 60-150 nodes. On larger instances, the approach offers only very minor improvements over a standard model that has been trained on instances with 150 nodes only.

### Strengths
- The approach seems to succeed in learning models that work well across instances of different sizes. On test instances with sizes seen during training, the trained models come close to the performance of POMO models trained specifically for one size only. 
- The considered problem of improving the cross-size generalization performance of learning-based models is highly relevant.

### Weaknesses
 - In my opinion the main weakness of this paper is that it does not provide enough ablation studies that evaluate the different components of the approach. The authors only provide some experiments for the TSP and only evaluate the experience replay and the intra-task regularization scheme in the main paper. In the Appendix some additional results for the TSP are reported but the CVRP is not considered at all. To fully convince me of the effectiveness of their proposed approach, the authors should report more detailed results for both problems in the main paper.
- I find Figure 1 and Figure 2 difficult to understand. At the time they are mentioned in the text multiple components shown in the figure have not yet been explained. Overall, I find the semantic of figure elements confusing. For example, what is the output of the “experience replay with previous tasks” element and why is there a connection between the current model and the “size selection” element? I think that Figure 1 especially should be simplified significantly.
- On larger test instances with sizes not seen during training the model leads to only small performance improvements over existing methods.
- The paper is missing a comparison to a naive POMO variant that is trained on instances of different sizes (e.g., in the range [60, 150]). The authors compare to AMDKD-POMO and Omni-POMO but both approaches seem to focus on the generalization to larger instances and do not perform well on the tasks reported in Table 1.

### Questions
-

### Soundness
3 good

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
This paper proposes a model-agnostic continual learning framework to improve the cross-size generalization capabilities of deep models for VRPs.
This paper designs the inter-task regularization scheme and intra-task regularization scheme to expedite the training on new sizes.
The proposed approach is evaluated on TSP and CVRP across a broad spectrum of sizes and shows good results.

### Strengths
1. This paper proposes the intra and inter task regularity, which is a main contribution of this paper, and shows the originality.
2. The proposed method sounds reasonable for continual learning.
3. The description of the whole method is relatively clear.
4. The experiments show good results and are relatively complete.

### Weaknesses
1. Although this paper proposes the intra and inter task regularity, the whole process is not novel enough.
It's very similar to the ema method.
2. There needs to be a clear conclusion on when to use intra-task regularization and when to use inter-task regularization, rather than just using "or".
3. It is better to $L_R$ instead of $L_{KR}$ for consistency in Line9 of Algorithm 1.

### Questions
1. Is this the first paper to deal with the cross-size generalization issue?
Is there any other way to solve the cross-size generalization problem?
The reviewers think the baselines are all for the single-sized problem, which may lose some important baselines.
2. What is the  $L_R$ if using the intra-task regularization in Eq.5? Please give a clear explanation.

### Soundness
3 good

### Presentation
3 good

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
This work presents a continual learning-based framework to foster the cross-size generalization of deep models for VRPs. It leverages regularization schemes to retain the valuable insights derived from previously trained exemplar models to facilitate subsequent training. Experiments prove the effectiveness of the proposed method.

### Strengths
1. The proposed method is promising to use continual learning for vehicle routing problems.
2. The designed framework with inter-task regularization is reasonable.
3. This paper is well-presented with clear figures.

### Weaknesses
I'm not an expert in vehicle routing. And I list some concerns here for reference.

This work utilizes deep models and continual learning for vehicle routing problems. However, there is no detail on the adopted deep models in the paper. It makes me confused about how the framework in Figure 1 works.

### Questions
Please refer to the weakness section.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
