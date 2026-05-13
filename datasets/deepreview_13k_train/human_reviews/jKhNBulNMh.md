# Rethinking Branching on Exact Combinatorial Optimization Solver: The First Deep Symbolic Discovery Framework

- Decision: Accept
- Scores: 6, 8, 6

## Abstract
Machine learning (ML) has been shown to successfully accelerate solving NP-hard combinatorial optimization (CO) problems under the branch and bound framework. 
However, the high training and inference cost and limited interpretability of ML approaches severely limit their wide application to modern exact CO solvers. In contrast, human-designed policies---though widely integrated in modern CO solvers due to their compactness and reliability---can not capture data-driven patterns for higher performance. To combine the advantages of the two paradigms, we propose the first symbolic discovery framework---namely, deep symbolic discovery for exact combinatorial optimization solver (Symb4CO)---to learn high-performance symbolic policies on the branching task. Specifically, we show the potential existence of small symbolic policies empirically, employ a large neural network to search in the high-dimensional discrete space, and compile the learned symbolic policies directly for fast deployment. Experiments show that the Symb4CO learned purely CPU-based policies consistently achieve *comparable* performance to previous GPU-based state-of-the-art approaches. 
Furthermore, the appealing features of Symb4CO include its high training (*ten training instances*) and inference (*one CPU core*) efficiency and good interpretability (*one-line expressions*), making it simple and reliable for deployment. The results show encouraging potential for the *wide* deployment of ML to modern CO solvers.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduce a neural-symbolic approach to discover branching heuristics for MILP solving. Instead of directly using a neural network as the branching heuristics, they propose to use a neural network to predict a symbolic expression, which is more efficient to invoke online.

### Strengths
- The idea of not directly using a neural network for branching prediction, but rather using it to produce a symbolic expression is quite interesting and plausible.
- The paper shows a substantial performance gain over the other methods.

### Weaknesses
 - The paper relies on manual feature extraction. This leaves open the question what are useful features, which is difficult to answer. Presumably the choice of the features are dependent on the particular benchmarks and can have significant impact on the performance. I get that the alternative deep representation makes the inference more expensive though.
- It is unclear how the training instances are selected and how similar to the test/validation instances the training instances are.

### Questions
- In the experiments, are the proposed branching heuristics invoked at each node, or only the top node?
- What is the cost of the training?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces an approach that combines the advantages of using machine learning (ML) and human-designed policies in solving combinatorial optimization (CO) problems. Symb4CO leverages deep symbolic optimization to learn interpretable symbolic expressions, transforming complex ML models into compact and efficient decision-making policies. The key strengths of Symb4CO lie in its efficiency, both in terms of training and inference, making it suitable for practical deployment on CPU-based devices. The paper shows that Symb4CO outperforms existing ML-based and human-designed policies. 

Novelty:
The paper introduces the concept of using deep symbolic optimization for solving CO problems, specifically focusing on the branching task. This is a novel approach that combines symbolic representations with optimization tasks, making it distinct from traditional machine learning techniques applied to CO problems.It is designed to be highly efficient, particularly in terms of training and inference, and the learned symbolic policies are interpretable. The paper highlights the importance of these features for practical deployment in real-world applications. Symb4CO's ability to perform well on purely CPU-based devices is quite practical. Most previous ML approaches for CO problems require GPU acceleration, but Symb4CO demonstrates that it can achieve comparable performance with CPU-based resources. The paper explores the concept of using compact symbolic policies for CO tasks. This is in contrast to complex machine learning models, which are often resource-intensive. Symb4CO's approach leads to concise, one-line mathematical expressions for decision-making.

Impact:
The impact of this work is significant, especially within the field of combinatorial optimization and machine learning. Symb4CO's ability to achieve competitive performance on CPU-based devices with limited training data can make it accessible to a broader range of real-world applications. The emphasis on interpretability in Symb4CO's learned policies addresses a critical concern. Symb4CO's success on CPU-based devices reduces the need for GPU resources. 

Quality of writing and experiments:
The quality of writing in the paper needs improvement. Here are some detailed comments:
- Section 4.3 talks about the fitness function, which is a crucial part of the training pipeline. So, it would be helpful to expand on the explanation of Equation 2. 
- Since the authors use an FSB-based fitness function, why does the FSB model perform so poorly (Table 1) compared to their tool?
- Table 2 mentions the use of one training instance. How was this training instance chosen? How do the results vary if a different training instance was chosen? Providing a standard deviation in Table 2 would be helpful. Similarly, how were the ten instances chosen (Section 5.1)?
- Authors mention discovering more complex working flows like RPB can be an interesting future work. Since RPB is compared against in Table 1, why do the authors think RPB performs so poorly compared to Symb4CO?
- In Section 5, what is the reason for using 1-shifted geometric mean?
- The interpretability claim in Section 5.2 needs some clarity. E.g., "RPB ... uses a scoring function with human-designed features and expressions rather than vanilla pseudocosts." Why is this relevant to the interpretability claim?
- How do the authors ensure the output expression from the RNN (Figure 2) is syntactically correct?
- Providing a concrete example and comparing the results with some of the other tools might be helpful to improve clarity.
- RNNs are usually not considered suitable for long-term sequences. How did the authors tackle that problem? How long are the output expressions from the RNN model?
- Part 3 in Figure 2 is challenging to understand. The fitness measure can include concrete values to improve clarity. 

Ablation studies explore the choice of mathematical operators and constants. Nevertheless, I believe it is important to address the following questions as well:
- Section 4.2 briefly mentions applying constraints during the training process. How is the length constraint implemented? Do the authors allow only a fixed length? Was there any ablation performed for the use of this constraint?
- Section 3.2 talks about 80% masking, but Section 4.1 mentions using all 91 features. How is the masking performed during training and evaluation across different benchmarks? Were any ablation studies performed on a different subset of features?
- How sensitive is the approach to different hyperparameter choices for the sequential model?
- Comment on the scalability of the approach. Do medium and hard problems have significantly larger search spaces? 

Additional comments:
- Out of curiosity, did the authors explore the extent to which the learned symbolic policies generalize across different problem domains within combinatorial optimization? For example, test the policies trained on one benchmark on a different but related benchmark to assess their transferability.
- The paper discusses the efficiency and interpretability of Symb4CO. Can the authors provide insights into any trade-offs when prioritizing efficiency and simplicity over complex but potentially more accurate models?

Minor nitpick - Expand FSB in Figure 2 as it has not been used till page 3

Review summary:
The paper introduces Symb4CO, a novel approach for solving combinatorial optimization problems by combining machine learning and interpretable symbolic expressions. It leverages deep symbolic optimization to generate efficient and interpretable decision-making policies. Symb4CO is highly efficient for inference, making it suitable for CPU-based devices. The paper provides a comprehensive experimental evaluation, demonstrating its superiority over existing methods. The key strengths include its innovative use of deep symbolic optimization, efficiency, interpretability, and the potential for real-world applications. However, the paper could benefit from improved clarity, expanded related work discussion, and addressing potential limitations. The ablation studies exploring mathematical operators and constants are valuable, but additional questions and considerations should be addressed for a more comprehensive understanding.

### Strengths
- Symb4CO is shown to be efficient, both in terms of training and inference, making it suitable for deployment in real-world scenarios on CPU-based devices.

- The paper emphasizes the interpretability of Symb4CO's learned symbolic expressions.

- The paper presents a thorough experimental evaluation, comparing Symb4CO with various baselines and showcasing its superior performance in terms of training efficiency, inference efficiency, and overall effectiveness.

### Weaknesses
The quality of writing in the paper needs improvement. Here are some detailed comments:
- Section 4.3 talks about the fitness function, which is a crucial part of the training pipeline. So, it would be helpful to expand on the explanation of Equation 2. Specifically, the paper should clarify how the fitness is calculated for each symbolic expression, including the specific comparison with the full strong branching (FSB) scores. A more detailed explanation of how the average fitness is computed across the expert dataset would also be beneficial.
- Since the authors use an FSB-based fitness function, why does the FSB model perform so poorly (Table 1) compared to their tool? The paper needs to elaborate on the computational overhead of FSB, and why its direct application is impractical despite its use in the fitness function. A discussion on the trade-off between the accuracy of FSB and its computational cost is needed.
- Table 2 mentions the use of one training instance. How was this training instance chosen? How do the results vary if a different training instance was chosen? Providing a standard deviation in Table 2 would be helpful. Similarly, how were the ten instances chosen (Section 5.1)? The paper should clarify the instance selection process and justify why the results are not sensitive to the choice of training instances. The potential variance in performance due to different training instances should be addressed.
- Authors mention discovering more complex working flows like RPB can be an interesting future work. Since RPB is compared against in Table 1, why do the authors think RPB performs so poorly compared to Symb4CO? The paper should provide a more detailed analysis of the limitations of the RPB policy, especially regarding its warm-start mechanism and the computational overhead of strong branching. A comparison of the computational steps between RPB and Symb4CO would be beneficial.
- In Section 5, what is the reason for using 1-shifted geometric mean? The paper needs to justify the use of the 1-shifted geometric mean over other metrics, explaining its advantages in the context of combinatorial optimization and why it is preferred over arithmetic or standard geometric means.
- The interpretability claim in Section 5.2 needs some clarity. E.g., "RPB ... uses a scoring function with human-designed features and expressions rather than vanilla pseudocosts." Why is this relevant to the interpretability claim? The paper should clearly define what it means by interpretability in the context of symbolic policies and explain how the learned expressions provide more insights compared to the human-designed scoring functions in RPB. The paper should also clarify how the learned symbolic policies can help in refining the human-designed working flows.
- How do the authors ensure the output expression from the RNN (Figure 2) is syntactically correct? The paper should provide more details on the constraints applied to the RNN outputs, such as length constraints, inverse operator constraints, and non-trivial expression constraints. A discussion on how these constraints ensure the syntactical correctness of the generated expressions is needed.
- Providing a concrete example and comparing the results with some of the other tools might be helpful to improve clarity. The paper should provide a detailed example of how Symb4CO works on a specific instance, including the learned symbolic expression and its impact on the branching decisions. A step-by-step comparison with other tools would also be helpful.
- RNNs are usually not considered suitable for long-term sequences. How did the authors tackle that problem? How long are the output expressions from the RNN model? The paper should discuss the limitations of using RNNs for long sequences and justify why it is still suitable for learning symbolic expressions. The typical lengths of the learned symbolic policies should also be reported.
- Part 3 in Figure 2 is challenging to understand. The fitness measure can include concrete values to improve clarity. The paper should provide a more detailed explanation of the fitness calculation, including concrete examples of how the fitness is computed for different symbolic expressions. The process of averaging the fitness over the expert dataset should also be clarified.

Ablation studies explore the choice of mathematical operators and constants. Nevertheless, I believe it is important to address the following questions as well:
- Section 4.2 briefly mentions applying constraints during the training process. How is the length constraint implemented? Do the authors allow only a fixed length? Was there any ablation performed for the use of this constraint? The paper should provide details on the implementation of hard and soft length constraints, and discuss the impact of different length constraints on the performance of Symb4CO. The specific hyperparameters used for the length constraints should also be reported.
- Section 3.2 talks about 80% masking, but Section 4.1 mentions using all 91 features. How is the masking performed during training and evaluation across different benchmarks? Were any ablation studies performed on a different subset of features? The paper should clarify whether the masking technique is used in the final Symb4CO model and if not, why it was removed. If the masking technique is used, the paper should provide more details on how it is applied during training and evaluation.
- How sensitive is the approach to different hyperparameter choices for the sequential model? The paper should discuss the sensitivity of Symb4CO to the hyperparameters of the sequential model, such as the number of layers, hidden units, and learning rate. The specific hyperparameters used in the experiments should also be reported.
- Comment on the scalability of the approach. Do medium and hard problems have significantly larger search spaces? The paper should discuss the scalability of Symb4CO to larger problem instances and clarify whether the search space of the symbolic policies increases with the size of the problem instances.

Additional comments:
- Out of curiosity, did the authors explore the extent to which the learned symbolic policies generalize across different problem domains within combinatorial optimization? For example, test the policies trained on one benchmark on a different but related benchmark to assess their transferability.
- The paper discusses the efficiency and interpretability of Symb4CO. Can the authors provide insights into any trade-offs when prioritizing efficiency and simplicity over complex but potentially more accurate models?

Minor nitpick - Expand FSB in Figure 2 as it has not been used till page 3

### Questions
- Out of curiosity, did the authors explore the extent to which the learned symbolic policies generalize across different problem domains within combinatorial optimization? For example, test the policies trained on one benchmark on a different but related benchmark to assess their transferability.
- The paper discusses the efficiency and interpretability of Symb4CO. Can the authors provide insights into any trade-offs when prioritizing efficiency and simplicity over complex but potentially more accurate models?

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces Symb4CO, the first symbolic discovery framework, to learn high-performance symbolic policies on the branching task in CO solvers. Symb4CO's CPU-based strategies match the performance of top GPU-based methods. With efficient training, quick inference, and clear interpretability, Symb4CO offers a promising way to integrate machine learning into modern CO solvers.

### Strengths
1. The problem the paper is trying to address is important. Indeed, we should have a light-weight machine learning approach to facilitate CO solvers. The directions that the author tries to improve, including requiring less training data and producing interpretable policies, are reasonable to me. 
2. The authors of Symb4CO apply reinforcement learning to make training efficient with much less data needed.

### Weaknesses
1. Symb4CO, although data efficient during the training, requires feature extraction by human. I have concerns about if the extracted features are expressive enough, and how much efforts does it take for these feature extractions. Does it really the so-called training efficient?
2. From the experimental results, I can observe that GPU based GNN approach can make CO solvers perform faster than CPU based Symb4CO. The overall goal is to facilitate CO solvers in efficiency, if GPU based approach can facilitate it more, than why not prefer GPU based approach? Besides, today’s machine can make very fast GPU-CPU interactions. I think we should be open to bringing in machine learning models inside CO solvers (not just adding the learned interpretable policies inside CO solvers) and making use of GPU’s high computation to facilitate logical reasoning tools.

### Questions
Please refer to the questions in the weakness section

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
