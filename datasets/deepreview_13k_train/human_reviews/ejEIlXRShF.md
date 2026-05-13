# Unveiling Molecular Secrets: An LLM-Augmented Linear Model for Explainable and Calibratable Molecular Property Prediction

- Decision: Reject
- Scores: 8, 6, 3, 3, 5

## Abstract
Explainable molecular property prediction is essential for various scientific fields, such as drug discovery and material science. 
Despite delivering intrinsic explainability, linear models struggle with capturing complex, non-linear patterns. Large language models (LLMs), on the other hand, yield accurate predictions through powerful inference capabilities yet fail to provide chemically meaningful explanations for their predictions. This work proposes a novel framework, called {\em MoleX}, which leverages LLM knowledge to build a simple yet powerful linear model for accurate molecular property prediction with faithful explanations. The core of {\em MoleX} is to model complicated molecular structure-property relationships using a simple linear model, augmented by LLM knowledge and a crafted calibration strategy. Specifically, to extract the maximum amount of task-relevant knowledge from LLM embeddings, we employ information bottleneck-inspired fine-tuning and sparsity-inducing dimensionality reduction. These informative embeddings are then used to fit a linear model for explainable inference. Moreover, we introduce residual calibration to address prediction errors stemming from linear models' insufficient expressiveness of complex LLM embeddings, thus recovering the LLM's predictive power and boosting overall accuracy. Theoretically, we provide a mathematical foundation to justify {\em MoleX}’s explainability. Extensive experiments demonstrate that {\em MoleX} outperforms existing methods in molecular property prediction, establishing a new milestone in predictive performance, explainability, and efficiency. In particular, {\em MoleX} enables CPU inference and accelerates large-scale dataset processing, achieving comparable performance 300$\times$ faster with 100,000 fewer parameters than LLMs. Additionally, the calibration improves model performance by up to 12.7\% without compromising explainability.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The article discusses a framework called MoleX, which aims to provide a granular interpretation of the impact of each feature on predictions. The framework uses a linear model to measure the contributions of decoupled n-gram features to molecular properties. It discusses the explainable component and residual component of a model and how they can be used to determine the contribution of each feature to the prediction.

### Strengths
This paper exhibits several notable strengths that contribute to its overall quality and impact.
- Well-Written and Clear Structure
  The author does an good job of discussing the main points in the article, providing a clear and concise overview of the framework, its theoretical background, and its advantages. The text is well-organized, making it easy to follow the author's reasoning and understand the key takeaways.
- Relevant Problem
  The problem addressed in the paper is relevant and timely, tackling a significant challenge in the field. The author provides a clear motivation for the research, highlighting the importance of understanding feature contributions in molecular properties.
- Advantages Over State-of-the-Art
  The proposed solution, MoleX, offers several advantages over existing state-of-the-art methods. By employing n-gram coefficients in a linear model, MoleX provides a more nuanced understanding of feature contributions, enabling researchers to better interpret the results. The author effectively highlights the benefits of MoleX, demonstrating its potential to improve the field.

### Weaknesses
 - Limited Experimental Evaluation
  The paper's experimental evaluation is limited, with a narrow focus on a specific dataset and task. To further demonstrate the effectiveness of MoleX, it would be beneficial to conduct more extensive experiments on diverse datasets and tasks. The current evaluation does not sufficiently explore the generalizability of the proposed method across different molecular property prediction tasks, such as regression tasks for continuous properties or tasks with varying data sizes and complexities. The lack of diverse datasets makes it difficult to assess the robustness and reliability of MoleX in real-world scenarios.
- Lack of Comparison to Other Methods
  The paper could benefit from a more comprehensive comparison to other state-of-the-art methods. While the author mentions some existing approaches, a more detailed analysis of their strengths and weaknesses would provide a clearer understanding of MoleX's advantages. Specifically, a quantitative comparison against methods that also provide feature importance scores, such as SHAP or LIME, would be valuable. This comparison should not only focus on overall performance but also on the quality and interpretability of the feature attributions.
- Future Work
  The paper concludes somewhat abruptly, without discussing potential avenues for future research. Outlining possible extensions or applications of MoleX would provide a clearer direction for future studies and encourage further exploration of the framework. For example, the paper could discuss the potential to extend MoleX to handle more complex molecular representations beyond n-grams, or to explore the use of different linear models or calibration techniques.

### Questions
Can you discuss the potential limitations of the linearity assumption in MoleX? How might non-linear relationships between features impact the accuracy of the framework?

How do you interpret the n-gram features in the context of molecular properties? Can you provide examples of how specific n-grams might be related to particular molecular properties or mechanisms?

How robust is MoleX to different types and levels of noise? Are there any mechanisms in place to mitigate the effects of noise or outliers on the computed feature contributions?

You mention that "Theoretically, we provide a mathematical foundation to justify MoleX's explainability". Could you clarify what you mean by "theoretically" in this context? Are you implying that the mathematical foundation is theoretical in nature, or is this a statement about the theoretical soundness of the foundation?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces MoleX, a framework designed to achieve accurate and interpretable molecular property predictions by leveraging the knowledge embedded in large language model (LLM) embeddings while maintaining a simple, interpretable linear model structure. MoleX combines the predictive power of LLM embeddings with the transparency of linear models, aiming to bridge the gap between complex models that excel in prediction and simpler models that offer more interpretability.

### Strengths
The paper stands out for its innovative approach to bridging the gap between prediction accuracy and interpretability in molecular property prediction. While explainability and accuracy have traditionally been seen as trade-offs, MoleX proposes a hybrid framework that leverages the strengths of both linear models and LLMs. This combination—using LLM embeddings to build a more interpretable linear model, while employing information bottleneck fine-tuning and sparsity to adapt these embeddings—is a creative solution to a long-standing problem. Furthermore, the introduction of a residual calibration strategy to enhance a linear model’s capacity in representing complex LLM-derived features demonstrates originality by addressing a specific limitation of linear methods. Overall, this paper is a meaningful contribution that combines originality with technical rigor, clarity, and significant practical implications.

### Weaknesses
While MoleX offers a creative use of LLM embeddings for interpretable molecular property prediction, the novelty might be limited as the work relies heavily on existing LLM representations and linear models. The use of embeddings from pre-trained LLMs combined with linear regression isn’t entirely new, as similar approaches have been applied in other fields for simplifying complex models while preserving interpretability. The authors could enhance the novelty by providing a clearer comparison of MoleX with similar hybrid approaches in other domains, or by further distinguishing their method’s unique aspects in the context of molecular property prediction. The authors can compare their method with prototype-based approaches as ProtoPNet [1] and xDNN [2].

### Questions
1. How is “faithfulness” in MoleX’s explanations quantified or evaluated? Could you provide more details on the metrics or assessment criteria used to determine that the model’s explanations are accurate and reliable from a chemical standpoint?

2. How does MoleX differ from or improve upon prototype-based approaches, which are also commonly used to enhance interpretability by referencing representative examples?

3. Could you provide more details about the residual calibration strategy? Specifically, how is it implemented, what types of prediction errors does it address, and how does it affect the interpretability of the final predictions?

4. Since MoleX relies on a linear model, are there cases where it struggles to represent the complexity of molecular data, even with LLM embeddings and residual calibration? How do you manage this limitation?

5. Which metrics were used to evaluate the explainability of MoleX compared to other interpretable models?

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
5

### Summary
This paper introduces MoleX, a framework for explainable molecular property prediction that combines large language model (LLM) embeddings with a linear model to achieve both accuracy and interpretability. MoleX leverages fine-tuned LLM knowledge and residual calibration to enhance prediction accuracy while enabling CPU-efficient inference, showing up to 12.7% improved performance and significant parameter reduction compared to standard LLMs.

### Strengths
1. **Reduced Complexity via Linear Model**: The use of a linear model effectively lowers overall computational complexity, making the framework suitable for large-scale applications.

2. **Efficient Dimensionality Reduction**: The dimensionality reduction technique minimizes computational demands, optimizing the handling of high-dimensional LLM embeddings.

3. **High Interpretability**: The model offers strong interpretability, providing reliable, chemically meaningful explanations for molecular predictions.

### Weaknesses
This paper, though innovative, exhibits certain weaknesses:

1.  **Lack of Comparison with Relevant Explainability Studies**: The authors did not compare their approach with other information bottleneck based methods, for example, SGIB and VGIB [1,2], which also employ IB techniques to identify explainable subgraphs most relevant to molecular properties. Including these comparisons would provide a more comprehensive evaluation of the proposed method.

2.  **Poor Presentation**: The presentation of the paper is lacking in clarity, with several areas insufficiently explained. This detracts from the paper’s readability and hinders a full understanding of the methodology. This is my primary reason for recommending rejection, as the paper requires major revision to improve clarity. Specific issues are detailed in the "Questions" section.

3.  **Omission of LLM-Based Method Comparisons in Table 2**: In Table 2, the authors do not compare LLM-based methods evaluated in Table 1. The reasons for this omission should be explicitly addressed within the paper to clarify the experimental choices and maintain consistency in the evaluation.

### Questions
1. **Line 261**: How are the $\ell_0$ penalty, $a_{kj}$, and $\phi_j(t)$ derived? These symbols should be explained in the main text rather than in the appendix to ensure readers understand their significance without having to refer to supplementary materials.

2. **Input Consistency for Explainable Model and Residual Calibrator**: Are the inputs for the explainable model and residual calibrator identical, specifically the reduced LLM embeddings after EFPCA? Clarifying this point would help readers better understand the workflow and the rationale behind the model architecture.

3. **Line 308**: How is $f$ defined, and are $f_H$ and $f_R$ the outputs of EFPCA? If so, why are they different, and how does EFPCA produce distinct outputs from the same input? Detailed clarification on this process would enhance the comprehension of the model’s internal mechanisms.

4. **Inconsistent Notation**: The notation varies across different sections and should be made consistent to avoid confusion.

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces MoleX, a framework combining linear models with large language model (LLM) embeddings for explainable and accurate molecular property prediction. The framework's unique features include:
- Information bottleneck-inspired fine-tuning and sparsity-inducing dimensionality reduction to enhance the informativeness of LLM embeddings.
- Residual calibration to address prediction errors, thereby boosting the performance of the linear model without sacrificing explainability.
- Quantification of functional group contributions to molecular properties through n-gram coefficients.

### Strengths
- Experimental results across seven datasets demonstrate that MoleX outperforms existing baselines (both GNN and LLM models) in predictive and explanation accuracy.
- The evaluation metrics, including classification accuracy, explanation AUC, and computational efficiency, present a holistic view of the model's advantages. The ablation studies reinforce the robustness of the method by exploring different parameter choices and model components.

### Weaknesses
 - The methodology section, while comprehensive, largely restates existing techniques without significant novel contributions. Many of the core ideas, such as the information bottleneck fine-tuning and dimensionality reduction via EFPCA, are established approaches adapted with minimal modification. This raises concerns regarding the originality of the proposed framework.
- The claims surrounding the methodological innovations appear overstated, given that the fundamental components, such as fine-tuning with variational information bottleneck and principal component analysis, are widely known and previously employed in similar contexts. The application of these techniques, while effective, may not sufficiently differentiate this work as a significant leap forward in the field.
- The paper does not adequately address the limitations of applying general techniques like information bottleneck and PCA to the specific problem of molecular property prediction. The justification for why these particular methods are well-suited for this task, beyond their general effectiveness, is lacking. The paper needs to provide a more detailed analysis of how these methods interact with the chemical data and the LLM embeddings to achieve the reported results.

### Questions
- I think the authors would want to reformulate the problem and reorganize the paper to clearly and precisely state their contributions and claims, and describe their method framework, better following academic integrity.

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The authors are interested in learning a molecular property prediction model using a large language model (LLM) with explainability. The proposed framework called MoleX consists of four components.

First, it extracts a useful feature from LLM embedding using the variational information bottleneck (VIB) principle (Section 4.1).
Second, it applies dimensionality reduction to the feature extracted in the first step based on the explainable functional principal component analysis, which roughly corresponds to PCA with sparsity-inducing penalty to each component (Section 4.2).
Third, using the explainable feature obtained in the second component, it fits a linear model that maps the explainable feature to the target variable (Section 4.2).
Fourth, with the predictive model fixed, it fits another linear model using the features not used in the third component for residual calibration (Section 4.2).

The authors evaluate the effectiveness of MoleX in terms of its predictive power as well as its explainability and computational efficiency.
The experimental results suggest MoleX is better than baseline methods in every aspect.
Sensitivity analyses on hyperparameters are conducted in Section 5.3, but most of the details are sent to the appendix.

### Strengths
- The problem setting to seek for a predictive model for molecules with explainability is a high-demand setting for practitioners, and I would appreciate the authors for achieving the state-of-the-art performance on this problem setting.
- The experiments are exhaustive in terms of the methods compared and experiments conducted, although many of the details are not in the main part of the paper.

### Weaknesses
 - The overview of MoleX is not clear, especially, how we train it and use it for obtaining prediction with explanations in a step-by-step manner. Although Figure 1 suggests a vague overview of it, as far as I am aware of, there is no rigorous explanation of it. Since it is very essential to describe MoleX, I would like to request the authors to explain it in an algorithmic way in the main part of the paper (not in the appendix).
- There are many mathematically incorrect/unclear descriptions, which pose challenges in understanding the paper.  A few examples are as follows:
  - Line 152: Since $g$ and $y$ are not sets, $f\colon g\to y$ should be $f\colon g\mapsto y$.
  - Definition 4.1: There are multiple concepts that are not explained, namely, an operator $\mathcal{D}^2$ and an inner product $\langle \cdot, \cdot \rangle_{\gamma}$. $k$ appears both in the objective function and constraints, but there is no explanation about it.
  - Line 260: $\ell_0$ penalty does not directly appear in Def. 4.1 (in a finite dimensional case, the regularization term boils down to the $\ell_0$ penalty, but the definition is given for the infinite dimensional case).
  - Lines 309-311: Given that $f_H(x)\in\mathbb{R}^{d_c}$ and $f_R(x)\in\mathbb{R}^{d_r}$, $\langle f_H(x), f_R(x) \rangle$ cannot be defined in a natural way.
- The definitions of $f_H$ and $f_R$ remain unclear. The pseudo code provides no explanation of these terms, and line 288 incorrectly refers to Equation 3.1, which defines the objective for learning $r$, not $f_H$. The lack of clarity around these core components hinders understanding of the method.

### Questions
- Please add an algorithm describing the whole procedure of MoleX including both its training and inference.
- I still don't understand why the explanation accuracy of the proposed method improves when with calibration. Could it be because the dimensionality reduction was too aggressive that a part of the features necessary for explanation was removed? I would appreciate it if the authors could point out any misunderstanding of mine if any / provide explanation on it.

### Soundness
2

### Presentation
1

### Contribution
2
