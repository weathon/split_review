# Unlearning-based Neural Interpretations

- Decision: Accept
- Avg Score: 8.00
- Scores: 8, 10, 8, 6

## Abstract
\normalsize Gradient-based interpretations often require an anchor point of comparison to avoid saturation in computing feature importance. We show that current baselines defined using static functions—constant mapping, averaging or blurring—inject harmful colour, texture or frequency assumptions that deviate from model behaviour. This leads to accumulation of irregular gradients, resulting in attribution maps that are biased, fragile and manipulable. Departing from the static approach, we propose \texttt{UNI} to compute an (un)learnable, debiased and adaptive baseline by perturbing the input towards an \emph{unlearning direction} of steepest ascent. Our method discovers reliable baselines and succeeds in erasing salient features, which in turn locally smooths the high-curvature decision boundaries. Our analyses point to unlearning as a promising avenue for generating faithful, efficient and robust interpretations.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper suggests a method for creating references for IG and other backpropagation-based explanation models. The reference is based on an untrained model with perturbations applied to the original image with respect to the model. The intuition, insights, and experimental results are presented as evidence.

### Strengths
Authors well-summarize the previous search, and clearly explain the required properties needed for the reference. The intution is clearly written, and well-evidenced by experimental results.

### Weaknesses
1. Even though they effectively present their intuition, there is no theoretical justification for their method. In particular, the pseudo-code is not explained enough. Additionally, it is unclear why the authors chose to implement it in the way they described in the code. The method itself needs further elaboration.

2. The suggested method is limited to explainable methods that require a reference, which restricts the broader applicability of the paper.

### Questions
1. The images shown in the figure may suggest that the white color appears relatively weaker compared to the black color. Is there any bias towards the white color? If not, why is the gray part of the swimsuit not highlighted? In Figure 2, the white swan also shows a similar tendency. Do you have any qualitative measures for this?

2. Why do you use KL divergence? Have you tried different methods as well?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
10

### Rating Number
10

### Confidence
4

### Summary
The authors identify that current baseline approaches in path attribution methods (like Integrated Gradients) inject harmful assumptions about color, texture, and frequency that can lead to biased and fragile attributions. UNI proposes computing baselines by perturbing inputs in an "unlearning" direction, to erase salient features while maintaining model-specific properties. The method demonstrates improved faithfulness, robustness, and stability compared to existing approaches across multiple model architectures and datasets.

### Strengths
The paper offers a well-structured analysis of an important problem in neural network interpretability. The authors identify a specific, previously overlooked issue: how static baseline approaches in attribution methods can introduce unintended biases in three distinct categories - color (shown through experiments with brightness/saturation changes), texture (demonstrated via gaussian/defocus blur tests), and frequency (validated through gaussian/shot noise experiments). 

This observation is methodically supported through experiments across a comprehensive set of modern architectures, including both CNN-based models and transformer-based models. Their UNI method shows measurable improvements in three key areas: faithfulness (with MuFidelity scores showing consistent improvements across architectures), robustness (demonstrated through FGSM adversarial attacks, achieving higher Spearman correlation coefficients), and stability (shown through detailed Riemann approximation experiments that work even with just one step). 

The theoretical foundation includes careful mathematical analysis where they provide explicit bounds on Riemann approximation error and prove how their approach maintains monotonicity and completeness properties. The extensive experimental results in the appendix, spanning all (20+!) detailed figures, provide clear visual evidence of how their unlearning-based approach improves upon traditional static baselines across different types of images and corruptions.

Well done!

### Weaknesses
 Largely this is a well written paper, here are a few potential avenues for improvement :
- Would it be possible to make stronger theoretical guarantees about the optimality of the unlearned baseline?
- Image classification baselines are pretty standard, I wonder how these baselines will look like in other domains such as NLP and audio.
- There could be some more discussion around hyperparameters, an often overlooked aspect in explainability literature
- It is mentioned that other techniques are inefficient, a detailed analysis of computational overhead might solidify contributions more strongly in that aspect.

### Questions
No particular questions

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors introduces a novel approach to enhance gradient-based post-hoc attributions.
The authors argue that static baselines (e.g., black images, blurred noise) impose unintended biases on attribution maps, leading to fragility and unfaithful interpretations. The proposed UNI framework generates a dynamic baseline by perturbing the input in an unlearning direction of steepest ascent, theoretically optimizing for a featureless reference that aligns with the model's predictive function. 
This adaptive baseline improves the path attribution by reducing curvature and enhancing robustness, demonstrated empirically through comparisons on benchmark datasets like IN and various baseline models.

### Strengths
1. **Innovative Baseline Approach**: The idea of using unlearning to create adaptive baselines is novel and addresses a known limitation in static baseline approaches.
2. **Robustness and Faithfulness**: The empirical results, including MuFidelity scores and robustness to adversarial perturbations, highlight the potential of the method to produce more reliable attributions.
3. **Comprehensive Experiments**: The paper includes evaluations on multiple models and datasets, adding credibility to the proposed approach.

### Weaknesses
However, I spotted some problems, some major (**M**) and minor (**m**):

**M1.** Literature Gaps: the related work section omits significant prior research on black-box interpretability (RISE, Sobol...) and miss some really important faithfulness metrics. Also a paper from last year that could be relevant (Saliency strike back) could be discussed.

**M2.** Faithfulness Metrics: while the paper discusses MuFidelity as a metric, it does not consider complementary metrics such as deletion and insertion, which could offer a broader validation of faithfulness and robustness. Including these would provide a more comprehensive evaluation of the method's performance. Also MuFidelity contain many Hyperparameter that are known to favorise certain method, could you state how did you approximate MuFidelity (number of sample)  and also the value of $|S|$ ?

**M3.** Theoretical Justification: the paper lacks a theoretical discussion on how UNI would perform under linear cases or simple functions. Providing proofs or theoretical insights for these cases would enhance the paper's depth and foundational strength.

**M4.** Broader Impact on Understanding Neural Networks: The practical implications of this method for gaining new insights into neural networks remain unclear. How much new knowledge / what have learn with this method that we haven't with other attribution methods ?

Now for the minor problem:

**m1.** Limited Baseline Comparisons: the paper mainly contrasts UNI with IG and a few other attribution methods. Expanding the baseline comparison to include more recent methods (including black-box one such as RISE or HSIC that are know to have good results on faitfhulness metrics) and varied methods would strengthen the experimental section.

**m2.** Minor Typos: I havent found a lot of typos, just line 468: "simultatenously".

### Questions
- Could you adapt the method to a low dimensional subspace path (eg delta is parametrized by 7x7 mask that we interpolate and then optimize?)
- How would the proposed method adapt if applied to models beyond image classification, such as language models or multimodal networks?
- Could the authors consider a variant of UNI that leverages multi-scale features for tasks involving more intricate hierarchical dependencies?


**Overall, I think the paper is well-executed with thorough analysis and comprehensive results. While the contribution may be of limited impact within the broader field of explainable AI (see Major issues), I tend to give a marginal accept.**

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies the specific problem of baseline selection in feature attribution. The authors argue that the optimal baseline choice depends on the task-model-input combination and propose an unlearning-based approach to improve baseline selection. By combining the baseline selection method with a well-known path method — IG, the resulting attribution method UNI demonstrates improved performance in various aspects according to the experimental results.

### Strengths
1. The paper is clearly motivated and easy to follow.
2. The authors collect a set of desired properties for the integration path, which could benefit following work on baseline selection.
3. The experiments are carefully designed, thoroughly evaluating the proposed method from different perspectives that support the authors’ claims.

### Weaknesses
1. The description of the proposed method is somewhat oversimplified, raising concerns about the overall depth of the work. It would benefit from further elaboration and discussions on each step in Algorithm 1. 
2. The reasoning behind why activation-matching ensures the removal of all salient features is unclear. Specifically, the method relies on finding a baseline that matches the activation of the unlearned model, but it's not clear why this specific matching is guaranteed to remove salient features, rather than simply finding another input with similar but potentially still informative activations. The process of finding such a match within the $\varepsilon$ budget also lacks theoretical justification.
3. Further clarification on some technical details about monotonicity would be beneficial. Please refer to questions 3, 4, and 5 for specific points.
4. There are some minor errors and formatting issues, for example: 
    - Different formats of $\varepsilon$ in Algorithm 1.
    - Citation wrapped by parenthesis as part of a sentence on line 261; repeated parentheses on line 269.
    - Line 349 refers to "Figure 3", which appears to be a mislabeling of "Table 3".

### Questions
1. Could the authors elaborate on why activation matching ensures the removal of salient features? Furthermore, given an activation vector $F(x;\hat{\theta})$, there may be multiple matches in the decision space within the budget $\varepsilon$. Is there any guarantee of the convergence for this matching, or is it based solely on empirical observations?
2. The goal of the unlearning is to derive $F(x;\hat{\theta})$ for matching. What advantage does it offer over directly adopting a non-informative activation, say $(\frac{1}{d_Y},\ldots,\frac{1}{d_Y})$? Could the latter be even more powerful as it removes features that are informative in general?
3. Could the authors clarify the meaning of $F_c(x_i)$ at lines 297-298 mean? It is unclear how the model processes a single feature $x_i$ instead of an instance $x$.
4. How are the two conditions in lines 297-298 satisfied? 
    - Assuming the authors intended $F_c(x)$ rather than $F_c(x_i)$, the monotonicity of the class confidence does not necessarily imply a consistent sign of the derivatives w.r.t. each feature $x_i$. This indicates that the sign of $\nabla_{\tilde{x}_i}F_c(\tilde{x})$ may vary along the path, which contradicts the claim of the first condition.
    - Solving the gradient saturation problem is one motivation for IG. However, if a feature $x_i$ has a saturated gradient at $x$, i.e. $\nabla_{x_i}F_c(x)\approx0$, the second condition becomes problematic as it requires the derivate of $x_i$ to remain 0 over the integration path, leaving gradient saturation unsolved.
5. Could the authors clarify the relationship between completeness and path monotonicity? Completeness, as given by the gradient theorem, should be path-independent.
6. Many attributions provided by UNI closely align with the details of the input images. To demonstrate that the explanations are not simply grayscale reproductions of the inputs, could the authors provide example attributions of different models on the same inputs to show whether they distinguish from each other (under the assumption that different models behave differently)?

### Soundness
3

### Presentation
3

### Contribution
3
