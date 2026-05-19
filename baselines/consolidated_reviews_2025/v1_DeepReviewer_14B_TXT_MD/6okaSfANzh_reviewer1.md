### Summary

This paper investigates the use of consistency of answers from weaker models as a proxy to the difficulty of questions. The motivation is to use the answers from weaker models when the question is easy and refer to stronger and more expensive models only when the questions are difficult. The proposed approach explores a few variations of routing the questions to the stronger model based on the confidence of the weaker model. The results on several reasoning datasets show the proposed approach can achieve comparable accuracy to always using the stronger model but at a much lower cost.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The proposed idea is interesting and can be useful in many applications. 
- The experiments are performed on multiple datasets. 
- The results show the proposed approach can achieve comparable accuracy to always using the stronger model but at a much lower cost. 
- The paper is written clearly.

### Weaknesses

#### Some Related Works


#### comment

 - The paper can benefit from more in-depth analysis of the cases when the weaker model is not able to answer correctly. Would the proposed approach be able to route the questions to the stronger model in those cases? 
- Is the proposed approach able to generalize to other weaker models? This can be evaluated by selecting different combinations of weaker and stronger models. 
- The proposed approach can be compared with some other heuristics to route the questions to the stronger model. For example, the difficulty of the questions can be estimated based on the length of the questions, and the questions can be routed to the stronger model based on the length.

### Suggestions

The paper would benefit from a more detailed analysis of the failure modes of the weaker model and how the proposed cascading approach handles these. Specifically, it is crucial to understand the types of questions that the weaker model consistently fails on and whether these failures are correctly identified by the consistency check, leading to routing to the stronger model. A breakdown of error types made by the weaker model, and the correlation between these error types and the consistency score, would provide valuable insights. For example, are errors due to logical reasoning failures more likely to be caught by the consistency check than errors in factual recall? Furthermore, the analysis should explore the trade-off between the number of samples used for consistency checking and the accuracy of the routing decision. A higher number of samples might improve the accuracy of the consistency check but would also increase the cost, thus negating the main benefit of the proposed approach. It would be beneficial to analyze the impact of the number of samples on the overall cost and accuracy of the system. This analysis should also consider the computational overhead of the consistency check itself. 

To further strengthen the paper, the generalization of the proposed approach to different weaker models should be explored more thoroughly. While the paper uses a single pair of weaker and stronger models, it is important to evaluate the approach with different weaker models having varying capabilities. This would involve selecting several weaker models, perhaps from different model families or with different architectures, and evaluating the performance of the proposed cascading approach with each of them. This would help to understand how the consistency threshold needs to be adjusted for different weaker models and whether the approach is robust to changes in the weaker model's performance. The paper should also investigate the impact of the choice of the consistency metric on the performance of the cascading approach. It is possible that other consistency metrics, such as the variance of the answers or the entropy of the answer distribution, might be more effective in identifying difficult questions. A comparison of different consistency metrics would provide valuable insights into the robustness of the proposed approach. 

Finally, the paper should compare the proposed approach with other heuristics for routing questions to the stronger model. While the paper mentions the length of the question as a potential heuristic, it does not explore it in detail. It would be beneficial to compare the proposed approach with other simple heuristics, such as routing questions based on the presence of specific keywords or the complexity of the question structure. This comparison would help to understand the advantages and disadvantages of the proposed approach compared to other simpler methods. Furthermore, the paper should also consider comparing the proposed approach with other more sophisticated methods for estimating question difficulty, such as using a separate model to predict the difficulty of the question. This comparison would provide a more comprehensive evaluation of the proposed approach and help to understand its strengths and weaknesses.

### Questions

Please see the weaknesses above.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
