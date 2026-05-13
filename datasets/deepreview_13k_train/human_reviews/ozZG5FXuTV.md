# Learning Causal Alignment for Reliable Disease Diagnosis

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Aligning the decision-making process of machine learning algorithms with that of experienced radiologists is crucial for reliable diagnosis. While existing methods have attempted to align their prediction behaviors to those of radiologists reflected in the training data, this alignment is primarily associational rather than causal, resulting in pseudo-correlations that may not transfer well. In this paper, we propose a causality-based alignment framework towards aligning the model's decision process with that of experts. Specifically, we first employ counterfactual generation to identify the causal chain of model decisions. To align this causal chain with that of experts, we propose a causal alignment loss that enforces the model to focus on causal factors underlying each decision step in the whole causal chain. To optimize this loss that involves the counterfactual generator as an implicit function of the model's parameters, we employ the implicit function theorem equipped with the conjugate gradient method for efficient estimation. We demonstrate the effectiveness of our method on two medical diagnosis applications, showcasing faithful alignment to radiologists.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses the problem of causal alignment, aiming to recover the causal mechanisms in a decision-making process. It specifically focuses on the classification of medical images, seeking to align the model's reasoning with the causal mechanisms used by experienced radiologists. With access to radiologist-annotated areas, the authors first use counterfactual generation to identify image regions that explain the classification result and then introduce a causal alignment loss to match these identified areas with the radiologist annotations. The alignment loss is optimized using the Implicit Function Theorem and the conjugate gradient algorithm. When attribute descriptions of abnormalities are available, they select the subset of attributes that causally determined the radiologists' labeling for each patient by maximizing the Conditional Counterfactual Causal Effect (CCCE). Finally, they propose a hierarchical alignment process to align both the annotated areas and attribute descriptions with expert annotations.

### Strengths
- To address the limitations in previous literature, where identified image regions align with expert behaviors only associationally, this paper proposes using counterfactual generation to identify regions that causally determine the model’s decision. The authors show that the generated counterfactual images maximize the probability of causation.
- To align the identified causal factors with radiologist-annotated areas, the paper introduces a causal alignment loss and an algorithm to estimate the gradient of this loss.
- The proposed method shows significant improvement over baseline methods in Class Activation Mapping (CAM) precision and classification accuracy. It effectively distinguishes spurious correlations from true causal factors.

### Weaknesses
 - The selection of the set of attributes that are causally related to the label requires further justification. The paper claims that the subset $S$ maximizing the CCCE represents the causally related attributes. However, if an attribute $A_k$ is not a cause of $Y$ for some $k \in \{1:p\}$, then we would have $Y_{A_k = 1, A_{-k} = a_{-k}} = Y_{A_k = 0, A_{-k} = a_{-k}}$ for any fixed $a_{-k}$. Thus, the CCCE would be the same for the true causally related subset $S$ and any superset of $S$. It seems that the full set $A$ might also maximize CCCE. However, since only six attributes are annotated in both the LIDC-IDRI and CBIS-DDSM datasets, the proposed algorithm may still work even if $r_i = (1, \dots, 1)^T$ for all $i$.
- The paper claims that previous methods, which regularize the model's input gradient to align with expert-annotated areas (lines 37–40), only capture associational factors. However, the paper later (lines 405–407) attributes the failure of these methods not to their inability to distinguish spurious correlations, but to the limited effectiveness of gradient-based approaches themselves. In fact, even if the identified image regions are only associational factors, regularizing the gradient to expert annotations will rule out spurious correlations. Although the explanation in Figure 1(a) is conceptually reasonable, the simulation does not explicitly demonstrate the advantage of causal factors over associational factors when expert annotations are leveraged.
- It would be helpful to clarify Figure 3, the causal diagram that illustrates radiologists' decision process. It should be emphasized that $A_{1:p}$ represents the experts' "decision" about image attributes, rather than the underlying true attributes of the image. It initially appears to me that the underlying true attributes are inherent features of the image, in which case no causal relationship would exist between $X$ and these true attributes. Besides, how the area marks $m$ fit into the causal diagram could be explained further.
- Could the authors provide the computation time for the proposed method compared to the baseline methods?


### Questions
- Is the loss function in line 194 optimized directly? From Algorithm 1, it appears that this loss function is optimized in a two-step process, i.e. finding $x_i^*$ by minimizing $L_{ce}$ and then finding $\theta$ by minimizing $L_{align}$.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a causality-based alignment framework to align the model’s decision with that of experts in disease diagnosis. The key components of the framework are counterfactual generation and causal alignment loss. Counterfactual generation highlights the areas that explain the model’s decision process, and the causal alignment loss minimized the distance between expert-annotated areas/attributes and the generated counterfactual. An optimization algorithm based on Implicit Function Theorem is designed to solve this two-stage problem. The authors then adapted the framework to two scenarios: area of interest annotations and attribute annotations, and develops a hierarchical alignment structure for attribute annotations. Various experiments are conducted and the results show that the causality-based alignment framework is robust against spurious correlation.

### Strengths
This is a good paper, I think. The presentation is concise, and the explanation of theory is clear. Numerical experiments are solid, with detailed description of implementation and comparison of baselines. Also, I think the idea of designing causal alignment loss based on counterfactual generation very fascinating.

### Weaknesses
My major question or concern for the causality-based alignment framework is computation cost, or scalability. For example, when solving for $x^*$, what if there are multiple counterfactual classes, or even more challenging, $y^*$ is continuous? I guess a straightforward solution would be to bin $y^*$ into binary classes, but that might sacrifice the granularity of counterfactual generation. Also, for hierarchical alignment, conditional counterfactual causal effect score is calculated for each attribute subset. What if the attributes are high-dimensional?

### Questions
Please see weakness.

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
4

### Summary
The authors present a novel method to help researchers achieve alignment of causal attributions in image analysis for, e.g., lung disease, with that of experts. The novelty is that the alignment is grounded in causal attribution rather than mere association.

### Strengths
The results are compelling, and the problem it takes up is relevant and timely and promises immediate practical benefits if other researchers pursue it. Further elaboration of the idea shows promise.

The math used makes sense, given the causal model employed. I have some questions about the causal model that can be fixed in the presentation, which I describe below.

I am especially impressed with Figure 4, which shows that the method can infer regions of interest that are closely aligned with those of experts, and with Table 1, which shows the overall accuracy of the method.

In short, the argument that taking causal structure into account in the problem of aligning image analysis with experts in the biomedical sciences is well-put.

### Weaknesses
The main weakness in the paper, which, as I said, can I think be addressed textually, concerns the causal diagram in Figure 3. This diagram implies that the attributes selected by the procedure are independent of each other and conditional on the existence of a mass. There is no reason I can think of that this must be the case. For example, there could be a latent variable L such that X -> L -> {A1, A2}, in which case conditioning on X would not be sufficient to separate A1 and A2. Also, there's no reason to think that relevant features cannot overlap in the image, at least not in principle, in which case they will not be independent. Some nuance needs to be added to this point. I don't believe the model needs to be changed, but I feel it needs to be presented as a heuristic choice or a choice about the types of feature sets the authors aim to discover.

A second comment is that causal search algorithms are available that, with appropriate background knowledge, could also achieve a result of finding models in the form of Figure 3, and these have not been compared directly for efficacy. I will not recommend such models, as we are not supposed to in these reviews to recommend our own work. Still, the authors could search for these in the literature and explicitly state that perhaps, while they may be effective, a different approach is being taken up and evaluated here, or at least to give reasons why they are not pursued. Some of these methods are highly accurate in terms of the causal graphs that they infer, though the assumptions of these methods could be discussed briefly.

A third comment is that nothing rules out, in principle, the possibility that multiple masses might occur in a single image, and it is not clear what the method would say in cases like this.

A fourth comment is that what model class is being assumed here must be explicitly stated. It's a mixed linear Gaussian/discrete regime, though this should be stated, and if that's not the case, then that should especially be stated up front at the beginning of the article. If it's there and I missed it, then I apologize.

### Questions
Could you clarify the points listed in the Weaknesses section in the text and put the causal model here in the appropriate context?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work addresses the problem of identifying medical diagnoses while also uncovering factors that indeed causally contribute to these diagnoses. The authors develop a novel learning and optimization framework that efficiently and accurately achieves this goal. Empirical results demonstrate its superior performance compared to other methods.

### Strengths
High Novelty/Quality: This work develops a novel causal alignment loss and provides an efficient optimization method for solving the learning problem.

High Significance: The empirical results show that their approach not only achieves high diagnostic accuracy but, more importantly, identifies causal factors that contribute to the diagnosis. Accurate identification of causal factors is of paramount importance in the medical field, as it provides informed and precise information for planning subsequent treatments.

### Weaknesses
Clarity:

1. In Figure 2 and Figure 1.b, I am confused about the terms "calcification," "margin," and "spiculation." Are these attributes? From my understanding, which was described in the problem setup in section 3  the attributes a_i are binary indicators for the image. Do you mean that each of the binary attributes a_i, for example, indicates the presence of "calcification" in the image? It would be great if the authors could provide a more clear descriptions/ explanations in Figure 2 and Figure 1. b captions.

2. In Equation (2) for counterfactual generation, which distance function are you using? Since the choice of the distance function will indeed affect the downstream causal factor identification and diagnostic accuracy, it would be great if the authors could provide a section for discussion or ablation study to analyze the effect of distance function on the model performance and interpretability. 

Besides common distance metrics (e.g., L1, L2, cosine similarity), possible prior-studied distance functions in the context of counterfactual generation are worthwhile for discussion [https://arxiv.org/pdf/1711.00399]:

Squared Euclidean Distance :
\begin{align} d(x_i,x^c_i) = \sum^d_{k=1} (x_{i,k} - x^c_{i,k})^2 \end{align}

Scaled Squared Euclidean Distance :
\begin{align} d(x_i,x^c_i) = \sum^d_{k=1} \frac{(x_{i,k} - x^c_{i,k})^2}{std_k(x)} \end{align}

Scaled L1 Norm :
\begin{align} d(x_i,x^c_i) = \sum^d_{k=1} \frac{|x_{i,k} - x^c_{i,k}|}{MAP_k} \quad \text{where,} \end{align} \begin{align} {MAP_k} = median_j (|x_{j,k} -median_l(x_{l,k})|) \end{align}

### Questions
Please see Weakness section.

### Soundness
3

### Presentation
3

### Contribution
3
