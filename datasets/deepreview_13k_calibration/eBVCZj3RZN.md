# Prediction Via Shapley Value Regression

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 6, 6, 5

## Abstract
Shapley values have several desirable properties for explaining black-box model predictions, which come with strong theoretical support. Traditionally, Shapley values are computed post-hoc, leading to additional computational cost at inference time. To overcome this, we introduce ViaSHAP, a novel approach that learns a function to compute Shapley values, from which the predictions can be derived directly by summation. We explore two learning approaches based on the universal approximation theorem and the Kolmogorov-Arnold representation theorem. Results from a large-scale empirical investigation are presented, in which the predictive performance of ViaSHAP is compared to state-of-the-art algorithms for tabular data, where the implementation using Kolmogorov-Arnold Networks showed a superior performance. It is also demonstrated that the explanations of ViaSHAP are accurate, and that the accuracy is controllable through the hyperparameters.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces a novel approach to generating SHAP values by integrating SHAP value loss directly into the model’s training loss, enabling the simultaneous training of a predictor and a SHAP value generator in an end-to-end manner. This is done by considering the model prediction to be the sum of SHAP values, creating training dynamics that should help develop predictors that are also explainable through the inherent SHAP generator network.

### Strengths
The paper is well-structured and clearly written, making the methodology easy to follow. The authors provide a thorough experimental analysis on numerous dataset, including ablation studies on key components. They also experimented using KANs to learn SHAP values, and compared it with using standard MLPs to show where each method performs best. The authors show that their method is able to achieve comparable performance (in AUC) with classic ML models in tabular datasets, while generating the predictions off predicted SHAP values.

### Weaknesses
1. **Metrics for Comparing SHAP Values with Ground Truth:** The choice of cosine similarity as a metric for assessing SHAP values may not be the most effective, as it doesn’t capture absolute differences well and only reflects directional alignment. Similarly, while Spearman’s correlation can illustrate feature impact ranking, it doesn’t prove that the generated SHAP values are actually close to the ground truth, since it ignores their absolute values. Despite offering a limited view, the reported Spearman rank correlations in Table 3 are still relatively low for several datasets, which suggests that the generated SHAP values could be further improved. The use of $R^2$ would be more appropriate here, as it directly measures the proportion of variance in the ground truth SHAP values that is predictable from the generated SHAP values. This is particularly important since the goal is to generate SHAP values that are as close as possible to the true values, not just directionally aligned or similarly ranked. The lack of $R^2$ values makes it difficult to assess the practical utility of the generated SHAP values, as it is unclear how much of the true variance they capture. 

2. **Limited Comparison with Other Methods:** Reporting SHAP value accuracy only against the baseline could be sufficient, but generally only if the generated SHAP values align very closely with the ground truth across all datasets. Since that doesn’t seem to be the case here, it’s essential to compare with other methods to understand the quality of the generated SHAP values. Given the design choices made to enable end-to-end SHAP generation, it would still be practical to compare with post-hoc methods like FastSHAP. Although these methods require post-hoc computation (which this work aims to avoid), FastSHAP, for instance, is relatively easy to train and very efficient at inference. Such comparisons would provide a more complete picture of where this approach stands relative to others. The absence of such comparisons makes it difficult to gauge the practical advantages of this method over existing alternatives, especially since the reported SHAP value accuracy is not uniformly high across all datasets.

3. **Unclear Practical Scope and Complexity:** The practical scope of this method isn’t fully addressed in the paper. Using SHAP values as predictors, while shown to be effective in experiments, increases the model’s complexity and could make the training process more difficult to control. This approach also limits the range of possible predictors. It’s not fully convincing that avoiding post-hoc SHAP computation is a big enough advantage to justify these constraints. A discussion on practical considerations, such as where this approach might be preferable despite its complexity, would be useful. The paper does not adequately address the limitations imposed by forcing the model to predict using SHAP values, which inherently restricts the model's capacity to learn complex relationships in the data. This constraint could lead to suboptimal predictive performance compared to models that are not bound by this requirement. A more thorough discussion of these trade-offs is needed to fully assess the practical applicability of the proposed method.

### Questions
1.  You consider the output to be the sum of computed SHAP values of all features/columns ($f(x)=1^\top \phi$). However, SHAP values computed should sum up to the prediction minus expected predictions ($1^\top \phi=f(x) - E[f(x)]$). Are you assuming $E[f(x)]=0$?
2. Achieving high SHAP accuracy using a metric like $R^2$, which more directly measures how close the generated SHAP values are to the ground truth, would provide a more convincing validation of the model’s accuracy claims. If the authors could provide Table 2 with $R^2$ values, it would give a clearer view of whether the empirical results support the claims of accurately generated SHAP values.
3. It would be informative to evaluate the trained predictor from this work as the black-box model in FastSHAP. This should give a better view on the relative quality of generated SHAP values.

### Soundness
1

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a new machine learning approach where the model directly predicts the Shapley values and then uses them for prediction (by summation). This is in contrast to the traditional approach where Shapley values are calculated at inference time after the model is trained leading to additional computational cost.

### Strengths
- The paper is very clearly written and easy to follow. All necessary preliminaries are introduced and thoroughly discussed. This makes the paper mostly self-contained and thus appealing to a wide audience (even if they are not very familiar with Shapley values).
- The idea is simple to understand, novel, and creative. 
- Theoretical results justify validity.
- Experimental settings are thoroughly described.
- A few different implementations are presented and compared.
- Ablation studies are included.

### Weaknesses
As much as I like the general idea and the presentation, one question has not yet been fully answered for me: When should I use Shapley value regression instead of the traditional approach?

From what I can see the main reason for using Shapley value regression is to avoid additional computational overhead at inference time. However, to avoid that, we need to constrain our choice of architecture, adapt the training process, etc. Specifically, the method requires a neural network architecture with a custom final layer to output Shapley values, limiting the flexibility to use other models like tree-based methods, which can be used with FastSHAP. Overall, I would like to better understand when all of this is worth it. I would like to see experiments that compare the training times and inference times of the two approaches, Shapley value regression, and the traditional approach. How much more time do I need for training when using Shapley value regression? How much more time do I need at inference time if I want to calculate Shapley values in the traditional way? The paper only shows the training and inference times for Shapley value regression and does not compare it to the traditional approach. 

I would also be interested to know if there are any other advantages of directly predicting Shapley values beyond the reduction in inference time.

**Clarifications**
- Lines 430-432: Can you elaborate on what you mean by the sentence "KernelSHAP requires more than 2000 samples and model evaluations per data example to achieve the same accuracy level of ViaSHAP on the Adult, Elevators, and House16H datasets." What is the "accuracy level"? Earlier it was mentioned that the ground truth is computed using KernelSHAP, so I am not sure against what the accuracy is measured. 
- Lines 457-459: Why is that observation "remarkable"? It seems intuitive that the similarity will improve as $\beta$ increases.

**Minor**
- Figure 2. I think there is something wrong with the loss function $\mathcal{L}_{\phi}(\theta)$. It is defined as a pair of two numbers.

### Questions
As discussed in the Weaknesses section.

### Soundness
3

### Presentation
4

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
This paper proposes a new model and training loss for efficiently computing Shapley values in supervised machine learning. The central idea is to train the model to directly output Shapley values when making predictions.

To achieve this, the model learns a feature representation, $\phi(x; \theta)$, where the output is simply the sum of its coordinates, or the sum plus a link function. The goal is for each coordinate of the learned representation to correspond to the Shapley value of the $i$-th feature in the input data. To enable this interpretation, the authors introduce a “consistency” penalty alongside the standard training loss, based on the optimization problem used in Kernel Shap. Here, they plug in the learned representation, $\phi(x; \theta)$, where Shapley values are typically used in the standard loss. This consistency penalty can also be seen as an amortization of the Kernel Shap problem and is very similar to the loss in Fast Shap [1]. 

The authors validate their approach on various tabular datasets using both MLPs and KANs to learn the representation, $\phi$. Although predictive performance with MLPs is not great, KANs perform really well, achieving results comparable to state-of-the-art methods like XGBoost. They also show that their amortized approach performs favorably compared to Kernel Shap, which is ultimately what it should do.

[1] Jethani, N., Sudarshan, M., Covert, I., Lee, S.-I., & Ranganath, R. (2022). FastSHAP: Real-Time Shapley Value Estimation. arXiv. https://arxiv.org/abs/2107.07436

### Strengths
- The paper is well-presented and very clear. The explanation of Shapley values is generally easy to follow for newcomers to the field, while still highlighting key points for those familiar with it. The plots are compelling and help illustrate the algorithm, and I particularly liked the diagrams in figures 1-2.
- The evaluation is thorough, and there is sufficient evidence to support the authors’ claims.
- The application of KANs is interesting (and somewhat surprising); I didn’t expect them to outperform MLPs by such a margin. I think this has value to the community. 
- While the proposed loss is not entirely novel, the approach is an interesting extension of models designed to compute Shapley values. I especially appreciate how this approach frames learning Shapley values as a representation learning problem.

### Weaknesses
 - A more thorough discussion and comparison with FastShap would be valuable. This would clarify the similarities, as the proposed loss can be seen as almost an instantiation of FastShap’s loss (without the ViaShap component) as per equation (4) in [1]. A speed comparison with FastShap, for instance, would also be helpful.
- Related to this, the novelty is somewhat limited since the consistency penalty is quite similar to FastShap, although incorporating it into the training phase itself is innovative.



### Questions
- Does the “# samples” in figure 5 refer to the number of samples used to estimate the loss?
- What was your intuition for using KANs? Did you try different models and found that KANs worked well, or do you have an idea as to why they may be particularly suited to this problem? 
- Could you elaborate on your view of the main contributions of your method compared to FastShap?

**Nitpicks & Suggestions**
- Line 122: Incorrect use of “”.
- Line 168: Equation 4 should be capitalized.
- Line 218: Should “M” be “d”?
- Lines 329-353: Contains unnecessary detail that makes the text harder to read; suggest shortening for readability.
- Line 87: The explanation of additive models and their connection to Shapley values could be clarified.
- To improve focus, consider emphasizing KANs due to the weaker performance of MLPs. If you agree, consider moving the section on MLPs to the appendix.

### Soundness
4

### Presentation
4

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
This paper proposes ViaSHAP, whose goal is to incorporate (baseline) SHAP explanations in a deep learning architecture as the final layer, such that the sum of all values is used as the model's prediction. It is thereby an extension of FastSHAP, which fits a surrogate model (or uses a fine-tuned variant) to predict SHAP explanations. The key difference is that instead of using the FastSHAP model as a surrogate to explain the black-box model, ViaSHAP takes the FastSHAP (surrogate) model as the prediction model. The authors propose a similar learning procedure as FastSHAP (but fit on true labels instead of the model's prediction). This learning paradigm is based on sampling random maskings during training, which are obtained from re-writing the Shapley value as a solution to a weighted least-squares problem. ViaSHAP is then applied on two Kolmogorov-Arnold Networks (KANs) and two MLP architectures. The authors evaluate the performance of this new architecture and learning paradigm using 25 tabular datasets and XGBoost, random forests, and TabNet. The evaluation shows that the KAN networks perform best on many of the datasets. Moreover, the authors evaluate the SHAP explanations of the ViaSHAP computed with KernelSHAP and the (inherent) SHAP values obtained from the proposed ViaSHAP model.

### Strengths
1. This work aims to incorporate the SHAP explanations during training in the model, which can be viewed as a bridge between black-box  models and inherently interpretable models. The core idea to use the FastSHAP-paradigm directly as a prediction model is a novel, yet minor, extension of FastSHAP, which has not been explored so far.
2. The paper is easy to follow, details on implementations, and experimental results are clearly presented

### Weaknesses
1. One weakness is the novelty of the contribution. Training a black-box classifier, which incorporates the SHAP explanations, has already been proposed with FastSHAP. The main novelty in this work, to fit FastSHAP on the (FastSHAP-)predictions of masked training data, instead of the predictions of the black-box model is not a major contribution.
2. The paper benchmarks the performance of ViaSHAP models with competitors on tabular datasets. But a key comparison is missing. How does ViaSHAP perform compared with a model with **similar architecture** that uses a traditional learning paradigm (without maskings?). What are the consequences for the classification performance of the model?
3. The SHAP explanations computed by KernelSHAP on the ViaSHAP model differ from the ViaSHAP explanations. In fact, in Table 2 and 3 this discrepancy is often quite large. The paper does not address this discrepancy, nor any consequences for the produced explanations. For instance, it would be interesting to see, if it is possible to receive exact SHAP scores there (convergence of KernelSHAP) by increasing the number of maskings in training or state theoretical guarantees on the maximum discrepancy.
4. Possible technical errors in the proofs, see questions below
5. ViaSHAP only considers baseline imputations as the masked inputs in the learning paradigm. A discussion for marginal and conditional imputations (as given in FastSHAP) is missing. What are the consequences of this decision? How does ViaSHAP behave under other value functions?
6. A comparison on non-tabular data, such as images, is missing. This would be particularly interested, since FastSHAP unfolds its benefits on such data. A comparison on the benchmarks from the FastSHAP paper would be beneficial.

### Questions
1. What are the consequences of the novel training scheme. How does the performance compare to the **same architecture** but with usual training scheme?
2. Moreover, how does the training time of the novel training scheme (with maskings) compare with the usual training scheme to achieve similar performances for the **same architecture**?
3. Is there any guarantee to obtain exact SHAP explanations with ViaSHAP  (fully agreeing with KernelSHAP). How does the training scheme needs to be modified to guarantee this? Is there a trade-off between accuracy and computational feasability?
4. In the proof of Lemma 2, why should the global loss be minimized at zero and not some other non-negative value?
5. In the proof of Lemma 3, and in general, I do not understand why the prediction on the masked output $\mathcal V(x^S)$ should be equal to the sum $1^T_S \phi(x,\theta)$ - this should only be the case, if the loss is minimized at zero, which is highely unlikely. Does there exist any empirical evidence for this, or a formal assumption?

### Soundness
2

### Presentation
3

### Contribution
2
