# ANOVA-NODE: An identifiable neural network for the functional ANOVA model for better interpretability

- Decision: Reject
- Scores: 6, 3, 6, 5

## Abstract
Interpretability for machine learning models is becoming more and more important as machine learning models become more complex. 
The functional ANOVA model, which decomposes a high-dimensional function into a sum of lower dimensional functions so called components, is one of the most popular tools for interpretable AI, and recently, various neural network models have been developed for estimating each component in the functional ANOVA model. 
However, such neural networks are highly unstable when estimating components since the components themselves are not uniquely defined. 
That is, there are multiple functional ANOVA decompositions for a given function. 
In this paper, we propose a novel interpretable model which guarantees a unique functional ANOVA decomposition and thus is able to estimate each component stably. 
We call our proposed model ANOVA-NODE since it is a modification of Neural Oblivious Decision Ensembles (NODE) for the functional ANOVA model. 
Theoretically, we prove that ANOVA-NODE can approximate a smooth function well.
Additionally, we experimentally show that ANOVA-NODE provides much more stable estimation of each component and thus much more stable interpretation when training data and initial values of the model parameters vary than existing neural network models do.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a novel methodology within an interpretable framework. The proposed model belongs to the class of functional ANOVA models, structured as a parallel sum of independent functions for each main effect and higher-order interaction effects. Additionally, the model uses NODE based on Oblivious Decision Trees (ODT) for each effect-specific function. This approach addresses the common identifiability issue in functional ANOVA models. Through experimental design, the paper demonstrates the method's effectiveness in resolving identifiability issues using a similarity measure based on the variance of predictions across multiple functions. Furthermore, the authors reveal a connection between SHAP, a post-hoc explainable AI method, and ANOVA-SHAP, showing that ANOVA-SHAP can serve as an effective explainability technique grounded in the proposed method.

### Strengths
1. The proposed model $ANOVA-NODE$ is described clearly and is easy to understand, further it seems technically solid.
2. The contributions of this research to the field are well-defined, and the experimental results strongly support the claims made in the paper.
3. The experiments designed to demonstrate the advantages of the proposed method are well-constructed and effectively highlight the strengths of the approach.

### Weaknesses
Weakness 1. Reproducibility issue 

In this paper, the description of the proposed method is clear, and the experimental results seem to strongly support the paper’s contributions. Nevertheless, one remaining concern in evaluating this paper is the lack of distributed code or guidelines, which would include research artifacts or data preprocessing steps.

- To address this concern, it would be advisable to release supplementary materials.
- If there are reasons preventing the release of materials including code and guidelines, those reasons should be explained.

Weakness 2.  Inconsistency between subsection title and Content

In subsection 2.3, "Neural Oblivious Decision Ensembles," the paper contains only a description of ODT without any mention of NODE. Did I observe this correctly? If so,

- The paper should provide an explanation of NODE. Alternatively, the subsection title should be changed, and an additional subsection should be dedicated to describing NODE.

Weakness 3. Need for Enhancements in Interpretability

The experimental results in the paper, along with those in the appendix, effectively demonstrate that the proposed method is more stable in terms of interpretability compared to other techniques such as $NAM$ and $NBM$. This stability is also observed in comparisons with second-order functional ANOVA models. However, given that the proposed method is an XAI model, would it be possible to provide interpretable plots (e.g., contour plots) for second-order interaction effects? (I understand that presenting interactions beyond second-order may be challenging.)

- Quantitatively representing the importance of second-order interaction effects compared to main effects could further enhance the interpretability aspect of the proposed method.

- Providing contour plots that illustrate changes in output with respect to variations in input for individual second-order interaction effects could improve explainability.

### Questions
Question 1. Is it possible to compare the computational complexity with $NAM$ and $NBM$ ? If so, I am curious about the differences in computational complexity.

Question 2. In terms of training strategy, many GAM-based additive models often first learn lower-order effects and then subsequently learn higher-order interaction effects. If my understanding is correct, it seems that $ANOVA-N^{d}ODE$ learns all orders of effects simultaneously. Would a sequential training strategy allow for more stable learning?

Question 3. Using NID, interactions targeted for learning were selected on a high-dimensional dataset. If we also select second-order or higher interactions on low-dimensional datasets (e.g., CALHOUSING, ABALONE, etc.), it seems that stability could be further improved, as with the previous question. Could we verify if my suggestion is correct?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces a groundbreaking model that enhances the interpretability of machine learning models by addressing the instability in component estimation within the functional ANOVA framework. ANOVA-NODE ensures a unique decomposition of high-dimensional functions into lower-dimensional components, thereby providing a stable and interpretable model. 

The authors demonstrate the model's ability to approximate smooth functions and establish a theoretical connection with SHAP values, facilitating the calculation of individual contributions to model predictions. Empirical experiments on various datasets verify the model's superior stability in component estimation and its competitive prediction performance compared to existing methods.

### Strengths
1. Writing: The structure of this work is well-crafted and stylistically sound, which could enhance the comprehension of the paper's modeling and computational aspects. However, there exist minor spelling and grammatical errors.
2. Theory: ANOVA-NODE can approximate smooth functions effectively and have established an interesting relationship between ANOVA-NODE and SHAP, a well-known interpretable method. This theoretical groundwork is crucial for the model's credibility, but with limited novelty compared to the existing representation theorem by Kolmogorov–Arnold. The proof seems solid but I have not checked carefully.
3. Experiments: Under several empirical validations, ANOVA-NODE offers more stable estimation of components compared to existing models, such as NAM and NBM, under variations in training data and initial model parameters. This is a valuable practical validation of the model's stability and interpretability. An interesting application to high-dimensional data uncovers its prediction performance and component stability, which is an important step towards real-world applicability.
4. Interesting extension: A new approach, ANOVA-SHAP, is developed to calculate SHAP values from the estimated ANOVA-NODE model, offering a computationally efficient alternative to existing SHAP calculation methods.

### Weaknesses
1. Wrong definitions for (generalized) additive models. As classical statistical models, additive models and their generalized version have been widely investigated from theoretical or empirical views. In line 111 (Page 3), the formulation indeed is the additive model instead of GAM, where GAM may involve a link mapping function g(*) like $f(x) = g(\sum_i f_i(x_i))$. The paper should clarify that the presented model is a specific form of additive model, and not a general representation of GAMs, which can include a link function. This distinction is crucial for accurately positioning the work within the broader statistical modeling literature.

2.	Novelty in modeling. The contribution of integrating neural networks in approximating component functions for ANOVA seems limited, compared to some existing work like Kolmogorov–Arnold network. There may require more discussions and empirical comparisons with some state-of-the-art additive models, neural additive models and recent ANOVA series. The paper needs to more clearly articulate the specific advancements over existing neural network-based additive models, particularly in how it addresses the limitations of these methods. A more detailed comparison with models that also leverage neural networks for function approximation is needed to justify the proposed approach's novelty.

3.	Missing crucial mathematical background. The Kolmogorov–Arnold theorem is necessary for demonstrating the rationality of summing component functions with individual feature. Thus it is kindly suggested to add comments to help the readers to understand the background and contributions. The paper should include a more thorough discussion of the Kolmogorov-Arnold theorem and its implications for the functional ANOVA decomposition. This discussion should clarify how the theorem supports the model's architecture and why it is a suitable framework for approximating high-dimensional functions.

4.	Theory. The sum2zero condition is commonly used for ANOVA modeling. However, there may exist some limitations. First, as stated in Lime178 (Page 4), this constraint may lead to nonunique or nonoptimal results. Besides, it is necessary to state the key assumptions before presenting these theorems to avoid misunderstandings, as some assumptions or conditions are merely present in the appendix. Furthermore, to better highlight the contributions, it is kindly suggested to summarize the challenges among the proof. Especially for Theorem 3.3, only $d=1$, sigmoid induced auxiliary function and bounded conditions are presented. It would be necessary to analyze more scenarios to support Theorem 3.3, like d=2 or more. What is the meaning of $K_S S$ in Line 282?

5. Optimization & Experiments. The dimensions of these used synthetic or real datasets are not high enough, indeed. Although such additive modeling scheme is declared to relieve the curse of dimensionality, individual modeling w.r.t. each input feature inevitably reduces prediction accuracy and often leads to non-convex target loss. Thus I wonder if the ANOVA-NODE enjoys some properties like smoothness or convexity? The paper should provide a more detailed analysis of the optimization landscape, including whether the loss function is convex or non-convex, and how the model addresses potential issues with local minima. Additionally, the paper should justify the choice of datasets and discuss the potential impact of higher dimensionality on the model's performance.

6. Moreover, how to determine the threshold $K_S$? Is it possible to uncover the relationship between prediction accuracy and the interpretability based on the theoretical or empirical perspectives?

### Questions
Please see the comments in Weakness.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper examines G${}^d$AMs with Neural Oblivious Decision Ensembles (NODEs). After presenting general proofs of functional ANOVA (fANOVA) and its connection to SHAP values, the authors propose a novel architecture to enable a fANOVA-style framework for NODEs. Experiments demonstrate improved stability of this method over alternative approaches, along with competitive predictive performance.

### Strengths
- **Clarity**: The mathematical and technical exposition is generally precise and informative.
- **Experiments**: The empirical experiments offer valuable insights into the approach's strengths and advantages.

### Weaknesses
## Major Comments

- **Novelty/Contribution [NC]**: It is unclear what aspects of the paper are novel. Specifically:
    - **[NC1]**: Theorems 3.1 and 3.2 address functional ANOVA itself without focusing on NODEs and, if I understand correctly, are established results. Theorem 3.1 is a direct consequence of the sum-to-zero condition (Hooker, 2007), and Theorem 3.2 can be found, for example, in Herren and Hand (2022).
    - **[NC2]**: How does ANOVA-NODE differ in terms of computation from the approach proposed by Lengerich et al. (2020) or from the NODE-GAM method (including purification) presented by Chang et al. (2022), which includes fANOVA in Appendix D? It is not clear if the proposed approach offers any computational advantages over these existing methods, especially considering the overhead of training a neural network.
    - **[NC3]**: 
        1. Since Theorem 3.3 addresses expressivity, why is the sum-to-zero constraint necessary? As ANOVA-NODE serves as a functional reparametrization of NODE-GAM, Theorem 3.3 should apply equally to NODE-GAMs of order $d$. The authors should clarify the necessity of this constraint in the context of the approximation theorem.
        2. If the optimal function is a GA${}^d$M, which naturally allows for an ANOVA decomposition (Wood, 2006), and efficient approximation methods for order-$d$ GAMs exist (Rügamer, 2024), what practical benefits do ANOVA-NODEs offer? The paper needs to justify the use of ANOVA-NODEs over existing, well-established GAM techniques.
        3. The authors write as a contribution: "We prove the universal approximation property in that ANOVA-NODE can approximate any continuous function up to arbitrary precision" but not all continuous functions are Lipschitz, which is required. The statement should be revised to reflect the necessary conditions for the approximation theorem.

- **Related Literature [R]**: An extended discussion of related literature would enhance readability and clarify the novelty of this work, particularly concerning the points above. See *References* for a starting point. The current literature review is insufficient to position the work within the broader context of interpretable machine learning and functional ANOVA methods. A more thorough comparison with existing approaches is needed.

- **Experiments/Presentation [E]**: 
    - **[E1]**: The finding that enforcing functional orthogonality consistently improves prediction performance is unexpected. Literature suggests that enforcing this constraint during training can sometimes reduce predictive accuracy. In contrast, post-hoc identifiability approaches (as e.g. discussed by the authors in the Appendix) do not influence the optimization while constituting a simpler optimization problem. The authors should provide a more detailed analysis of why the imposed constraint improves performance in their specific setting.
    - **[E2]**: Including GAMs as a benchmark could make the results more informative. The lack of comparison with standard GAMs makes it difficult to assess the practical utility of the proposed method.
    - **[E3]**: A plot comparing stability to prediction performance could help explore any potential relationship between these metrics. Such an analysis would provide valuable insights into the trade-offs between stability and accuracy.
    - **[E4]**: If the ANOVA is functioning as expected, an analysis of variance (across all orders $d$ to show how much of the variation in the outcome can be explained by every complexity level) would add value to the results. This would help to validate the ANOVA decomposition and provide a better understanding of the model's behavior.

- **Presentation [P]**: 
    - **[P1]**: (Related to NC) If the **NC** points are valid, restructuring the paper to focus primarily on ANOVA-NODE and its properties may enhance clarity. The current structure does not clearly highlight the unique contributions of the proposed method.
    - **[P2]**: The motivation in Sec. 3 reads awkwardly. It states, "An unsolved but important problem in neural functional ANOVA algorithms is the identifiability of each component" followed by "A simple remedy... is to impose constraints" and then the sum-to-zero constraint, which "is neither a unique nor optimal identifiability condition." So eventually, the initially stated problem remains, doesn't it? The authors should clarify how the chosen constraint addresses the identifiability problem.
    - **[P3]**: Adding axis labels and facet titles (especially in Figures 2 and 3) would significantly improve readability. Additionally, Figure 2’s caption mentions **stability scores**, while the text refers to **similarity scores**. Consistency in terminology is needed.

### Questions
- It would be great if authors could comment on the mentioned weaknesses and whether I missed or misunderstood anything.
- Would it make sense to use an ANOVA kernel as in Blondel et al., 2016 to improve the scaling of ANOVA-N${}^d$ODES?
- Could a factorization approach as in Rügamer, 2024 incorporated to improve scalability?

### Soundness
3

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
4

### Summary
The paper introduces ANOVA-NODE, a novel model designed for better interpretability in AI by improving the stability of functional ANOVA model estimations. Traditional neural network models for ANOVA suffer from instability due to non-unique decompositions, but ANOVA-NODE addresses this by ensuring a unique functional decomposition through a modification of Neural Oblivious Decision Ensembles (NODE). The authors theoretically prove that ANOVA-NODE approximates smooth functions well and is related to SHAP values, a popular interpretability method. Experimental results demonstrate that ANOVA-NODE provides more stable and interpretable component estimates compared to existing methods.

### Strengths
- **Theoretical Contributions**: The authors provide a solid theoretical foundation, including proofs.
- **Innovative Solution**: The paper presents an innovative approach to addressing the unidentifiability problem in functional ANOVA models, offering stability in component estimation.
- **Experimental Validation**: While there are some concerns about the experimental setup (discussed below), the results demonstrate that ANOVA-NODE outperforms baseline models in both stability and prediction accuracy.
- **SHAP Link**: The connection between the sum-to-zero constraint and SHAP values offers a novel perspective on component-based interpretation, presenting an efficient alternative to existing SHAP calculation methods.

### Weaknesses
## Major Concerns / Questions
- **Motivation and Relevance**: Although the paper addresses the technical issue of unidentifiability in functional ANOVA models, it does not provide a clear explanation of why this problem is significant in practical applications. Including practical examples that demonstrate where current methods fail and how ANOVA-NODE offers concrete improvements would greatly enhance the impact of the paper. Although Appendix E discusses interpretability, the advantage of using ANOVA-NODE over existing methods (e.g., applying SHAP to other models) remains unclear. Clarification on this point would be beneficial.
- **Hyperparameter Tuning**: The ranges for tuning the hyperparameters and the selection process are not clearly described. Additionally, the chosen hyperparameters for the benchmarks raise concerns. For NODE, only five trees are used, which is an unusually small number, inconsistent with the original paper and other related works, where values like 1024 are more typical. Similarly, for XGBoost, both the tree depth and the number of estimators are surprisingly low, often limited to just 100 estimators with a depth of 3. Moreover, the learning rate is the same for all datasets except one. Although the authors state that the learning rate was chosen "by empirical trials," it is difficult to believe that this reflects a thorough tuning process. Other key hyperparameters are neither reported nor seemingly optimized, which likely affects the models' performance. Yet, the results based on these suboptimal hyperparameters are used to support claims that "ANOVA-NODE provides more stable estimation and interpretation of each component compared to the baseline models [...] **without losing prediction accuracy**" and that "ANOVA-NODE is the best." Given the current configuration, I find these claims unconvincing and poorly supported. To properly substantiate them, I strongly recommend a comprehensive hyperparameter tuning of the existing benchmarks, following best practices and relevant literature.
- **Code Availability**: The absence of the source code for review intensifies concerns about the evaluation setup, especially the selection of hyperparameters.

 
## Further Concerns / Questions
- **Baseline Comparison**: Including performance metrics for intrinsically interpretable models like linear or logistic regression and simple decision trees would provide a clearer baseline for comparison.
- **Related Work**: A section on related work is missing. The paper does not clearly distinguish ANOVA-NODE from existing methods. E.g. the authors claim that "The main idea of the proposed neural network is to model each component as the sum of special but simple neural networks that satisfy the sum-to-zero condition". What is the difference to NAM here?
- **Complexity of Presentation**: Certain sections, particularly those involving mathematical formulations (e.g., p.5), are dense and challenging to follow. More intuitive explanations and clearer descriptions of the model’s workings would improve accessibility.
- **Runtime and Efficiency**: The paper lacks information about the runtime of the proposed method and how it compares to existing benchmarks.
- **Performance Reporting**: The reporting of only normalized scores (Table 1) may be misleading. Providing unnormalized scores, at least in the appendix, would be more informative. Additionally, reporting only ranks in Table 2 can obscure performance differences. Including the averaged normalized distances to the best-performing model would strenghten the comparison.

### Questions
**Please see Weaknesses.**

### Further Questions:
- The performance of ANOVA-NODE is significantly lower than XGBoost for certain datasets (e.g., California Housing and Wine, Table 2). Is there an explanation for this comparatively poor performance?
- The results for the feature importance scores on California housing dataset (Tables 14 and 15) are confusing to me. Why is the importance of feature 6 very small for ANOVA-N1ODE while it has the by far highest importance for ANOVA-N2ODE?
- In the CBM example, how does the explanation of ANOVA-NODE differ from a simple linear model? Does it offer better performance? The results regarding monotone constraints also appear counterintuitive. Why is such a relation observed at all and how can enforcing monotonic constraints cause such a significant shift in results? A more detailed explanation is needed.

### Soundness
2

### Presentation
3

### Contribution
2
