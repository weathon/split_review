# A Scalable Transformer-based Framework for Fault Detection in Mission-Critical Systems

- Decision: Reject
- Scores: 8, 5, 3, 5

## Abstract
Detecting underlying faults is crucial in the development of mission-critical planning systems, such as UAV trajectory planning in Unmanned aircraft Traffic Management (UTM), which is vital to airspace safety. 
Inevitably, there exists a small set of rare, unpredictable conditions where the UTM could suffer from catastrophic failures. 
Most traditional fault detection approaches focus on achieving high coverage by random input exploitation. 
However, random methods are struggling to detect long-tail vulnerabilities with unacceptable time consumption. 
To tackle this challenge, we propose a scenario-oriented framework to search long-tail conditions, accelerating the fault detection process. 
Inspired by in-context learning approaches, we leverage a Transformer-based policy model to capture the dynamics of the subject UTM system from the offline dataset for exploitation acceleration. 
We evaluate our approach over 700 hours in a massive-scale, industry-level simulation environment. 
Empirical results demonstrate that our approach achieves over 8 times more vulnerability discovery efficiency compared with traditional expert-guided random-walk exploitation, which showcases the potential of machine learning for fortifying mission-critical systems. 
Furthermore, we scale the model size to 2 billion parameters, achieving substantial performance gains over smaller models in offline and online evaluations, highlighting the scalability of our approach.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes a scenario-based framework to search for long-tail cases to accelerate the fault detection process. By leveraging a transformer-based policy to capture the dynamics of tested system from the offline dataset, the paper is able to achieves over 8 times more vulnerability discovery efficiency compared with traditional expert-guided random-walk exploitation.

### Strengths
(1) The paper is pretty novel to leverage decision transformers to model thescenario generation problems.
The integration of context-aware scenario generation improves the model's generalization capabilities, allowing it to adapt better to novel situations. The authors also demonstrate the scalability of their model, effectively showcasing performance improvements as they increase the model size up to 2 billion parameters. 

(2) The extensive empirical evaluation over 700 hours in a simulated environment provides strong evidence for the framework's effectiveness. The reported results of over 8 times more vulnerability discovery efficiency compared to traditional methods underscore the framework's practical utility. I like the fact that it also employs a variety of metrics for both offline and online evaluations, providing a well-rounded assessment of the framework's performance.

### Weaknesses
(1) The paper mentions the importance of diversity in generated scenarios, however, how do you plan to evaluate the diversity of generated scenarios? The approach will be of less meaningful if the generated scenarios are too similar. Specifically, the paper lacks a clear quantitative metric for assessing the diversity of the generated scenarios. Without such a metric, it's difficult to ascertain whether the model is truly exploring a wide range of potential failure modes or merely generating variations of a limited set of scenarios. The high-dimensionality of the state space makes this a non-trivial problem, and the paper should address this challenge with a concrete approach.

(2) Although the paper highlights generalization capabilities, it does not adequately discuss potential overfitting issues, particularly with the larger model. An analysis of the balance between model capacity and overfitting in various environments would strengthen the paper. The paper should include a more detailed analysis of the model's performance on both in-distribution and out-of-distribution data, including learning curves and performance metrics that explicitly demonstrate the model's ability to generalize. Without this, it is difficult to assess whether the reported performance gains are due to genuine generalization or overfitting to the training data.

(3)  While the authors compare their approach with expert-guided testing, it would be useful to include comparisons with other recent state-of-the-art methods in the fault detection domain (see questions), to better situate the contributions of their framework. The current comparison with random-walk exploration is not sufficient to demonstrate the superiority of the proposed method. The paper should benchmark against other relevant scenario generation techniques, such as those based on reinforcement learning or black-box optimization, to provide a more comprehensive evaluation of the proposed framework.

### Questions
(1) my biggest concerns are the overfitting. How you ensured that the model does not overfit to the training scenarios, given the huge training datasets you are using? What strategies are in place to evaluate generalization to unseen environments? 

(2) The random approach is pretty weak baselines, have you considered other scenario generation approach as well? Like black-box optimization, RL? Could you also clarify how the metrics chosen for evaluation were determined? Are there other metrics that could provide additional insights into the framework’s effectiveness?

(3) What are the possible fault injection operations? Are they all included in Table 5 in the Appendix?

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
3

### Summary
This paper presents a promising application of Transformer-based reinforcement learning for UTM fault detection, with clear potential for improving safety in mission-critical UAV systems. The writing is clear and easy to follow. However, it seems to lack real-world validation, reproducibility, and practical deployment guidance. Also, it doesn't adequately address ethical issues for safe-critical applications. Addressing these concerns in a revision could substantially improve the work’s impact and relevance. If the authors follow the recommendations above and address the noted concerns, I would like to raise the score.

### Strengths
1. Well-designed Transformer-Based Fault Detection Framework for Unmanned Aircraft System Traffic Management (UTM):
This paper introduces an innovative Transformer-based framework specifically designed to detect faults in mission-critical Unmanned Aircraft System Traffic Management (UTM) environments. The paper proposes a scenario-oriented approach for generating fault scenarios using a Transformer-based policy model (PM) combined with an action sampler (AS) for safe, targeted testing. This approach leverages reinforcement learning in a high-dimensional, temporal environment.
 2. Scalability and Robust Empirical Validation:
The model’s scalability is demonstrated by training versions with up to 2B parameters. Empirical validation through 700 hours of simulations in a large-scale, industry-grade UTM environment is a strong point, providing evidence that the proposed framework could significantly outperform traditional testing methods by detecting critical faults more efficiently. Results indicate an 8x improvement in vulnerability detection compared to expert-guided testing and a clear scaling effect between model size and performance. Also, the larger model could better leverage more training data based on the experimental observations. This thorough evaluation across diverse UTM scenarios and environments underscores the potential utility of this approach in mission-critical settings.
 3. Rigorous Well-formulated Evaluation Metrics and Comprehensive Experiments:
The authors employ a diverse set of evaluation metrics—Action Probability per Observation (APO), Action Probability Distribution (APD), Hazard Action Ratio (HAR), and Bugs per Million Flights (BPM)—to measure the efficacy and robustness of the testing framework. This sounds very rigorous and well-formulated. Besides, comprehensive testing is conducted on in-distribution and out-of-distribution environments, adding further robustness to the study. The systematic inclusion of both offline and online evaluations also provides a more holistic view of model performance, strengthening the empirical validation.

### Weaknesses
1. Lack of realistic real-world empirical study: I am particularly interested in whether the authors could include a realistic or real-world case study to complement their evaluation. As presented, the submission’s evaluation appears to be conducted solely within simulated, controlled environments, which may not fully capture the complexities or variances that arise in real-world scenarios. Incorporating a case study that applies the system or approach in a real-world setting would significantly enhance the paper’s impact by demonstrating its practical viability and relevance. Additionally, I would encourage the authors to address the Sim2Real (simulation-to-reality) gap, which often poses a significant challenge when transferring solutions from simulated environments to real-world applications. Understanding how the proposed methods or systems perform outside controlled simulations, and identifying potential limitations or adaptations required for practical deployment, would add substantial value to the paper and its contribution to the field.

2. Deployment concern: When deploying to resource-constrained embedded hardware such as UAVs, in addition to the accuracy of the task itself, real-time constraints should also be considered. Although the authors claim that validation accuracy can be significantly improved on a larger model (PM-2B) compared to a small model or traditional methods, the corresponding model's inference time may be significantly extended, making it impossible to meet real-time constraints, which in turn limits the deployment availability on real systems. In this case, solution efficiency is very important. Can the author provide some potential ideas to solve this concern? This raises a question: the evaluation metrics introduced by the author do not seem to take into account the cost of model inference. If it is taken into account, will the observed scaling law still hold? Or will Sweetspot be a specific model size?

3. Ethical concerns: The authors have not fully explored the ethical considerations involved in safety-critical applications, which is a significant oversight given the potential dual-use nature of adversarial fault detection models. In safety-critical fields, such as autonomous vehicles or medical diagnostics, ensuring that models are used responsibly and safely is essential. The dual-use nature of these models implies that they could potentially be misused if adequate safeguards are not in place. I recommend that the authors discuss strategies for preventing misuse and promoting ethical, responsible deployment practices. Moreover, it would be beneficial if the paper included a more thorough discussion on potential defensive mechanisms designed to detect or mitigate faults and adversarial attacks during the model’s deployment. Such considerations could bring the paper in line with current safety standards in the field, emphasizing the importance of robustness and reliability under real-world conditions.

### Questions
1. I am curious about whether the authors could provide any realistic/real-world case study. In this submission, it seems that the evaluation is conducted entirely in simulated controlled environments.

2. The evaluation metrics introduced by the author do not seem to take into account the cost of model inference. If it is taken into account, will the observed scaling law still hold? Or will Sweetspot be a specific model size?

2. The authors do not adequately address the ethical issues of safe-critical applications. Given the dual-use potential of adversarial fault detection models, the authors should discuss strategies for preventing misuse and ensuring responsible deployment. Additionally, having more discussion / considering defensive mechanisms for detecting or mitigating issues during model deployment would be valuable to align with safety standards in the field.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper presents a novel Transformer-based framework for fault detection in mission-critical systems, specifically for Unmanned Aircraft System Traffic Management (UTM). The framework addresses fault detection in UTM by focusing on rare, high-risk failure scenarios, often missed by conventional testing techniques. Leveraging a Transformer-based policy model within a reinforcement learning (RL) framework, it generates high-risk scenarios. The approach includes a rule-based Action Sampler to enforce safety constraints, refined with human alignment, enhancing the realism of generated test scenarios. Empirical evaluations demonstrate an 8x improvement in vulnerability detection compared to traditional methods, with scalability confirmed by increasing the model size up to 2 billion parameters.

### Strengths
1. The problem is challenging and very important to the community.
2. The scenario-based framework seems promising.

### Weaknesses
1. The motivation of using transformer is unclear to me.
2. There is no formal problem statement and assumptions.
3. The evaluations are not sufficient to support the claims.

### Questions
1. I think it is important to clearly define what kinds of faults you are referring to. Do you mean a fault is a series of actions? If so, I don't understand why this framework is confined to MDP settings. If you are pointing to just the very first action, then it is very hard to determine whether it is a fault or not, maybe it is required to introduce some causality theory under this assumption.
2. I don't understand why a transformer-based architecture is required. Maybe it is better to include more insights and elaborate it with a motivating example?
3. Where would you deploy this model? I'm pretty sure this model cannot be deployed on each vehicle, and I'm not sure how this policy model can be updated in real-world applications.
4. I'm not entirely convinced by the experiments. First, the dataset is private and there is no evidence showing that faults are the 'long tails'. Therefore, it is hard to claim that the results support the claims in this paper. I think it is better to show some statistics about the dataset to help readers having a better understanding of it.

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents a framework for detecting faults in Unmanned aircraft Traffic Management (UTM) systems using a Transformer-based architecture. The authors propose a scenario-oriented approach that combines a Policy Model (PM) with an Action Sampler (AS) to identify vulnerabilities in mission-critical systems. The work demonstrates improvements over traditional testing methods.

### Strengths
1. The paper tackles a critical problem: detecting rare, high-risk faults in Unmanned Aircraft System Traffic Management (UTM) systems.

2. Using a Transformer-based approach to capture long-term dependencies in system data is a smart choice, as the self-attention mechanism helps identify patterns over time.

3. The framework includes a preference bias and an Action Sampler to guide the model in selecting meaningful actions, reducing bias from the offline data.

### Weaknesses
1. The description of the state, action, and reward is too general, making it difficult to grasp the specific types of faults being tested and their impact on the UTM system. It would be helpful if the authors provided clearer examples or detailed scenarios, showing how particular actions (like network disruptions, obstacles, or drone malfunctions) are modeled and what consequences they produce in the system. For instance, how are network disruptions modeled—are they complete outages or packet loss? What specific types of obstacles are considered, and how do they interact with the simulated drones? What are the various modes of drone malfunction, and how are they triggered by the action sampler?

2. Some of the evaluation metrics are difficult to interpret. e.g., unclear definition of "bugs" in metrics. The term "bugs" is vague and lacks a clear definition within the context of UTM systems. It is unclear whether this refers to software bugs, system-level failures, or deviations from expected behavior. A more precise definition of what constitutes a "bug" in this context is needed to properly assess the evaluation metrics.

3. Missing comparisons with other ML-based testing approaches (e.g., RNNs, LSTMs). The paper lacks a thorough comparison with other established machine learning techniques for sequential data modeling, such as Recurrent Neural Networks (RNNs) and Long Short-Term Memory networks (LSTMs). These models are commonly used for time-series analysis and could provide a valuable baseline for evaluating the performance of the proposed Transformer-based approach. A comparative analysis would help to highlight the specific advantages and disadvantages of using Transformers in this context.

4. The accuracy shown in Figure 5 is relatively low (max ~10.8%), which may impact the reliability of the framework. The low top-1 prediction accuracy of the Policy Model (PM) raises concerns about its ability to reliably generate meaningful test scenarios. While the authors mention using Top-K sampling, the low accuracy suggests that the model may struggle to capture the underlying patterns in the data, potentially limiting its effectiveness in identifying critical vulnerabilities.

5. While the application of Transformers in UTM systems is interesting, the novelty of the approach feels limited, especially as the methods used (Transformer-based modeling, reinforcement learning, and scenario testing) are relatively well-established in similar problem spaces.

### Questions
1. Could you provide more details on this industry level simulator?
2. The paper references a "smoke test" as a baseline for comparison. Could you explain what this entails in the context of UTM testing?
3. Typically, validation sets are used for tuning hyperparameters, and the Figure 5 results should ideally be shown on test sets to evaluate the model's true generalization ability. Could you clarify/rename the exact setup here?

### Soundness
2

### Presentation
2

### Contribution
2
