# Toward $\textbf{F}$aithfulness-guided $\textbf{E}$nsemble $\textbf{I}$nterpretation of Neural Network

- Decision: Reject
- Avg Score: 4.67
- Scores: 3, 5, 6

## Abstract
Interpretable and faithful explanations for specific neural inferences are essential for understanding and evaluating the behavior of models. For this purpose, feature attributions are highly favored for their interpretability. To objectively quantify the faithfulness of an attribution to the model, a widely used metric uses perturbations of the input that mask either the highly salient or highly non-salient features. These metrics, however, neglect the faithfulness of the attribution to the hidden-layer encodings of the model, and hence ignore its internal structure. In response, we propose a novel attribution method, $\textbf{FEI}$, which targets faithfulness to hidden layer representations. Moreover, the method optimizes the quality of the attribution according to the perturbation metrics using a novel smooth approximation of the metrics that allows effective optimization by gradient decent. This improve its performance on faithfullness evaluation. The method provides enhanced qualitative interpretability, while also achieving superior scores in quantitative faithfulness measurements.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a new framework for faithfulness based attribution. They use a differentiable approximation of fractiles to allow them to optimize an otherwise non-differentiable objective. They then optimize this and average over different fractiles and use the resulting attribution map to evaluate several metrics.

### Strengths
- The paper improves the Q_P metric over the selected baselines.

### Weaknesses
 - Section 3 is difficult to understand, at least partially due to notation. For example, the LHS of (2) seems to be a scalar based on notation (dot products on the RHS), but from context it seems that the authors are using the \cdot to mean element-wise multiplication (Hadamard product).  There are other things that are confusing like having $\alpha_f(p)$ and then $\alpha_p$, where $p$ presumably means different things in each context - it's an argument, but then it's also used as the fractile. Another example; in (3), $\tilde x$ and $l_{faith}$ should be notated to depend on $f$.

- The relation between faithfulness metrics and faithfulness optimization is unclear

- The results seem mixed at best; there is improvement in Q_P, but overall Q_D is not improved and their defense mechanisms seem to be worse than baseline (this section was difficult to interpret, but based on the text it seems that lower is better).

### Questions
1. In 3.2, you define a consistency constraint $\alpha_1 \le \alpha_2$ and then state that optimizing under these constraints is challenging. Have you considered parameterizing $\alpha$ as a cumulative sum? e.g. $\alpha_i = \sum_{j\le i} \delta_j$ In this case, the constraints becomes $\delta_j > 0$ and $\alpha_N=1$, which is easier to handle in an SGD framework.

2. Since there are two faithfulness metrics Q_P and Q_D, how does l_faith relate to them? Is it only optimizing perturbation (a hunch based on table 1 results)?

3. What is $\bar x$ in (5)? Is it the same as $\tilde x$?

4. Are the gradients clipped at every single layer? if not, how do you define the decomposition of the network?

### Soundness
2 fair

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
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a novel neural network explanation method driven by faithfulness in both model decisions and internal model functioning. It combines ensemble approximation with gradient clipping. Additionally, it proposes a new qualitative metric that implicitly assesses internal faithfulness. Reasonable qualitative and quantitative results are reported.

### Strengths
1. The proposed method makes sense to me.
2. The paper is generally well-written.
3. The qualitative results are reasonable.

### Weaknesses
I am not familiar with interpretable deep learning, so I am not sure if the quantitative results are sufficient and significant. The baselines are outdated - Extremal Perturbation(EP) Fong et al. (2019), RISE Petsiuk et al. (2018), FGVis Wagner et al. (2019), GradCam Selvaraju et al. (2017) and Integrated Gradient Sundararajan et al. (2017), so I do not take them as competitors powerful enough. Though the qualitative results with several images make sense to me, I cannot be fully convinced by such an insufficient quantitative comparison.

### Questions
I would suggest the authors include quantitative results with recently proposed competitors.

I will lower my rating if the other reviewers' comments on the quality of the quantitative analysis agree with mine.

If the AC and other reviewers are familiar with this research area and believe that the presented results are sufficient enough, please let me know and I will be happy to raise my rating.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper targets interpretable and faithful explanations for specific neural inferences. Currently, feature attribution is a commonly used technique for interpretability and input perturbation is used to objectively quantify the faithfulness of an attribution to the model by masking out salient or monotonous features. These approaches overlook the faithfulness of attribution to the hidden-layer encodings. Thus, this paper tries to measure the faithfulness of hidden layer representations, leading to an optimization method for attribution.

### Strengths
Pros:
- This work focuses on an overlooked problem: faithfulness to hidden layer representations, which is worth exploring.
- The ensemble method can remove the need for hyper-parameters and is effective as well.
- Gradient clipping is able to maintain internal faithfulness as shown with visualization results.

### Weaknesses
Cons:
- Lack of in-depth discussion of the visualization result. It seems that EP can also obtain good visualization and locate the Submarine better than FEI. It would be better to discuss the impact of 'hot' and 'cold' areas in heat map. Specifically, the paper does not provide a detailed analysis of why certain regions are highlighted as salient while others are not. The paper should investigate whether the 'hot' areas consistently correspond to semantically meaningful parts of the input that are crucial for the model's decision. Furthermore, the paper does not explore the implications of 'cold' areas. Are these regions truly irrelevant, or do they play a subtle role that is not captured by the attribution method? A more thorough investigation into the relationship between the attribution maps and the model's internal representations is needed.


### Questions
-

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
