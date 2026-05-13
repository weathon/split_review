# Riemann-Lebesgue Forest for Regression

- Decision: Reject
- Scores: 5, 3, 8, 5

## Abstract
We propose a novel ensemble method called Riemann-Lebesgue Forest (RLF) for regression. The core idea in RLF is to mimic the way how a measurable function can be approximated by partitioning its range into a few intervals. With this idea in mind, we develop a new tree learner named Riemann-Lebesgue Tree (RLT) which has a chance to perform Lebesgue type cutting,i.e splitting the node from response $Y$ at certain non-terminal nodes. We show that the optimal Lebesgue type cutting results in larger variance reduction in response $Y$  than ordinary CART \cite{Breiman1984ClassificationAR} cutting (an analogue of Riemann partition). Such property is beneficial to the ensemble part of RLF.  We also generalize the asymptotic normality of RLF under different parameter settings.  Two one-dimensional examples are provided to illustrate the flexibility of RLF. The competitive performance of RLF against original random forest \cite{Breiman2001RandomF} is demonstrated by  experiments in simulation data and real world datasets.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces a new ensemble regression method called the Riemann-Lebesgue Forest (RLF), which leverages a novel tree structure, the Riemann-Lebesgue Tree (RLT). RLF improves traditional Random Forests by utilizing "Lebesgue-type" partitioning, which splits based on response values rather than predictor values alone. This approach, combining both Riemann and Lebesgue partitioning, is shown to reduce variance in predictions and improve mean squared error, particularly in sparse or noisy data scenarios. The authors provide theoretical analyses, demonstrating the asymptotic normality of RLF and evaluating its performance on both simulated and real-world data, highlighting RLF's competitive edge in regression tasks over conventional method.

### Strengths
- **Originality**: The paper introduces a novel ensemble method, the Riemann-Lebesgue Forest (RLF), which creatively combines Riemann and Lebesgue partitioning within decision trees. This innovative approach, applying response-based splits (Lebesgue-type) rather than traditional feature-based splits, offers a fresh perspective on ensemble methods, especially in handling regression tasks in sparse models.

- **Quality**: The research is thorough, with extensive theoretical analysis and rigorous experimentation. The authors carefully examine the variance reduction and asymptotic normality properties of the RLF, providing proofs that establish the foundation of the method's performance. 

- **Significance**: The introduction of the Lebesgue-type partitioning extends the applicability of ensemble methods to settings where traditional Random Forests might underperform, particularly in high-dimensional or noisy environments.

### Weaknesses
 - **Clarity in the Splitting Criteria**: The connection between Eq. (2) (simple function approximations) and Eq. (5) (the splitting criterion) is unclear, which weakens the reader's understanding of the novel splitting mechanism. It is really needed to expand the explanation on this connection.

- **Overly Strong Claims**: The claim that "a RLT will have smaller \(L_2\) training error than an ordinary CART tree" is not straightforward and needs more explanation. Furthermore, the expected reduction in mean squared error due to bias-variance decomposition analysis does not explain the fact that the new proposed method overfits. This overfitting is usually the result of a method having high variance. This needs to be much better explained.

- **Limited Experimental Improvements**: The empirical results, while promising, show only modest improvements over traditional Random Forests. 

- **Dependency on a Local Model**: The requirement of a secondary random forest model within each Riemann-Lebesgue Tree as a local model presents computational and interpretative limitations. This reliance could be explored in greater depth, addressing alternative local models or the impact of this dependency on scalability and performance. This limitation should, at least, much better discussed.

### Questions
Please try to answer each of the weaknesses discussed above.

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper considers learning a variation of Random Forests, where each decision tree is learned using CART-type tree induction, but instead of considering only input features to split, it considers the target output also as a splitting criteria. But during the test time, we need the value of the target during inference (at decision nodes that splits on the target), and those are computed (predicted) using Random Forest (which will also be trained locally at decision nodes that splits on target). The paper has some theoretical analysis, and experimental comparison with Random Forests.

### Strengths
Using target values as one of the splitting criteria in tree learning is an interesting idea.

### Weaknesses
1. The novelty of the paper is not on learning a forest in a novel way but rather learning a single decision tree using splits on the target. As such, the new tree learning method should be compared on its own with other tree learning methods such as CART, C5.0, GUIDE, TAO and PyDL8.5. According to theorem 3.1, shouldn't it be better than CART?
2. Using local Random Forest to predict the output that is used at a decision node splitting on the target is quite a heuristic approach. Is there any theory or intuitive motivation behind it? The choice of Random Forest as the local model seems arbitrary; why not other methods like linear regression or k-nearest neighbors? What are the trade-offs of using a Random Forest as a local model in terms of computational cost and prediction accuracy?
3. No comparison with gradient boosting. XGBoost and LightGBM are the widely established methods in tree ensembles. Given the fact that tree ensembles are mostly evaluated empirically, having a comparison with gradient boosting is important. The lack of comparison makes it difficult to assess the practical value of the proposed method.
4. Theoretical analysis of section 3 looks very complicated, especially the bounds of theorem 3.2. They do not seem to add any practical value. The practical implications of the theoretical results are not clear, and it is difficult to see how these bounds would be used in practice. The analysis seems to focus on asymptotic properties, which may not be relevant for real-world datasets with limited sample sizes.

### Questions
No questions.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors introduce Reimann-Lebesgue Forest (RLF), a new ensemble method for regression that mimics Lebesgue integration by occasionally splitting nodes based on the response variable Y. They also establish the asymptotic normality of RLF and demonstrate its competitive performance against Random Forests on both simulated and real-world datasets.

### Strengths
1. The authors propose an interesting “Riemann-Lebesgue” splitting criterion for CART that directly incorporates the response variable splitting, making it a novel approach worth exploring.
2. The authors provide a solid theoretical justification for their approach.
3. The approach demonstrates effectiveness compared to traditional Random Forests across various synthetic and real datasets.

### Weaknesses
1. The notation in Section 2.1 could be clarified. In lines 112 and 133, the dimension is denoted as d, whereas in lines 127 and 136, it appears to be represented by p. For better readability, it would be preferable to use consistent notation for dimension throughout. Additionally, since  m_{try}  is an integer, the set  C_R  in line 135 is not well defined. It would be more precise to define C_R as a set of tuples where each tuple contains a feature index and a corresponding split point, rather than just a set of feature indices.
2. I don’t believe it’s impractical to keep partitioning in practice, as suggested in line 53. For example, the default min_samples_leaf parameter in Scikit-Learn’s Random Forest Regressor is set to 1 (M_node = 1), which allows the trees to grow very deep. A follow-up concern is whether the difference between RLF and RF would diminish if RF trees were allowed to go deeper, while it runs faster than RLF. Specifically, the paper used a minimum node size of M_node = 5 for real datasets, as shown in Appendix A.10. What would happen if M_node were reduced to 1? Furthermore, the choice of M_node = 5 seems somewhat arbitrary and lacks justification. A more thorough exploration of how M_node impacts both RLF and RF performance is needed.
3. While Section 3.3 addresses the training complexity, I believe the contrast in prediction complexity is even more significant. Has any analysis been conducted on the prediction time complexity? The use of local random forests within the Lebesgue splitting process introduces a significant computational overhead during prediction, which should be analyzed more rigorously. This overhead is not just a constant factor; it scales with the depth of the tree and the number of local forests that need to be traversed for a single prediction, potentially making RLF impractical for large-scale deployment.
4. The introduction of ‘Lebesgue’ partitioning could complicate interpretation, particularly for calculating values like TreeSHAP [1], although the paper’s primary focus is on predictive performance. The local random forests used in Lebesgue splitting make it difficult to trace the decision path and attribute feature importance, which is a critical aspect for many real-world applications where interpretability is as important as accuracy.

### Questions
When noise levels are high, splitting on signal features tends to be less effective, and intuitively, ‘Riemann’ type splitting might also be expected to underperform. Could the authors provide intuition for why ‘Riemann’ type cuttings achieve better performance at higher noise levels, as suggested in lines 434-435?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The author(s) present a new ensemble learning method named Riemann-Lebesgue Forest (RLF) for regression tasks. Traditional random forest methods use "Riemann" sense partitioning to approximate a function that best fits the observed data. The proposed method applies a "Lebesgue" sense partitioning based on the range of the response variable Y, aiming to achieve a more accurate model with reduced error. Additionally, the paper addresses the proposed method from a theoretical points, including proofs of asymptotic normality and a complexity analysis.

### Strengths
- RLF introduces a new way of dividing data in regression trees, called "Lebesgue" cutting, which enhances accuracy in situations where traditional random forests (RF) struggle, especially in high-noise or low-data scenarios.
- The paper explains the main theories behind RLF, giving a solid mathematical base.

### Weaknesses
 - The paper lacks a publicly accessible GitHub repository or similar platform for the proposed methods.
- RLF generally requires more wall-clock time than RF, especially for large datasets, and does not show significant performance improvements in terms of time complexity. The time complexity of RLF, stemming from the local random forest and the nature of tree ensemble methods, is a significant concern. While the paper mentions the potential for parallelization, the current implementation's computational cost is a barrier to practical application, especially when compared to the established efficiency of RF. The lack of a detailed analysis of the computational overhead introduced by the Lebesgue splitting further obscures the practical limitations of the method.

### Questions
RLF is more accurate but takes more time to run. Is this extra accuracy worth it for real-life use, especially when time is important? It would help to explain and show the level of contribution the approach makes to accuracy.

### Soundness
3

### Presentation
2

### Contribution
1
