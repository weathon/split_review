# ConLUX: Concept-Based Local Unified Explanations

- Decision: Reject
- Scores: 5, 3, 6

## Abstract
With the rapid advancements of various machine learning models, there is a significant demand for model-agnostic explanation techniques, which can explain these models across different architectures.
Mainstream model-agnostic explanation techniques generate local explanations based on basic features (e.g., words for text models and (super-)pixels for image models). However, these explanations often do not align with the decision-making processes of the target models and end-users, resulting in explanations that are unfaithful and difficult for users to understand.
On the other hand, concept-based techniques provide explanations based on high-level features (e.g., topics for text models and objects for image models), but most are model-specific or require additional pre-defined external concept knowledge. 
To address this limitation, we propose \toolname, a general framework to provide concept-based local explanations for any machine learning models. 
Our key insight is that we can automatically extract high-level concepts from large pre-trained models, and uniformly extend existing local model-agnostic techniques to provide unified concept-based explanations.
We have instantiated \toolname on four different types of explanation techniques: LIME, Kernel SHAP, Anchor, and LORE, and applied these techniques to text and image models.
Our evaluation results demonstrate that 1) compared to the vanilla versions, \toolname offers more faithful explanations and makes them more understandable to users, and 2) by offering multiple forms of explanations, \toolname outperforms state-of-the-art concept-based explanation techniques specifically designed for text and image models, respectively.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes to use foundation models to discover concepts to augment on methods like LIME to provide concept-based local explanations. The method is evaluated on sentiment analysis and image classification tasks.

### Strengths
The proposed framework is interesting and can be useful if validated rigorously. The paper explores two different modalities. The framework is applied across multiple established methods (LIME, Kernel SHAP, Anchor, and LORE).

### Weaknesses
Concept discovery using LLM is the key aspect of the proposed framework. This calls for a human evaluation to answer the question: are the concepts discovered by the foundation models indeed aligned with a human-understandable representation? Currently, it sounds like it is assumed that the prompt will take care of this.


How faithful is the backtracking from the perturbed concept space to the original space? This also done by the LLM?

Methods like LIME create a local approximation of the original function to a human-understandable form and explain the decision. This is the reliable yet explainable part of the method. By using LLM for discovering concepts, (given each task and the sample), it becomes difficult even locally to explain the predicates. The decision-making is not fully explained, i.e., the choice of predicates cannot be explained. For instance, in case a poor predicate is chosen by an LLM, the user may be confused by the explanation. I think the proposed method, by using foundation models for concept discovery, makes the framework less reliably explainable.

To prove the robustness of the method, it would be useful to try intervention-based causal metrics, especially since the concept discovery is done by foundation models. C-insertion and deletion are often used to evaluate concept importance and fidelity in concept-based explanations.

Robustness to the prompt: how robust is the framework to the construction of the prompt? Also, given the literature around prompt engineering, the framework could explore what might be the optimal prompting strategy for discovering human-interpretable concepts.


The paper proposes a new framework for explanation where concept discovery is done by foundation models. For the text modality, the experiments are restricted to sentiment analysis, and 1000 images from the ImageNet dataset are used for classification for images. The method calls for more experiments for validation. However, this is not the sole reason for the decision.


There is no baseline comparison. Though the method is a new paradigm, it could be compared with concept bottleneck methods or predicates selected by other methods. There could also be an ablation study on different LLM model combinations. Additionally, the authors could discuss concept bottleneck-based methods. What do you think about a method where task-specific concept bottlenecks are chosen by the LLM? This is not a weakness or a mandatory experiment for the text.


Minor comments:

L44: Please provide a citation, as not all visual explanation methods using attribution mapping follow this principle.
L80: "Moreover, we observe that ... across different tasks." given the restricted number of tasks evaluated it might be a good idea to tone down this claim.
Teaser figure: I think, this can be made more comparable if the attribution method is shown with certain thresholding. When shown post-thresholding, the viz can clearly demonstrate the benefit of the proposed method, even allowing for certain comparative evaluations later.
L93: This is a tradeoff between reliability of explanation to prediction and understandability. If the model is indeed making a decision based on the token, pivoting the explanation on different concepts can change it. 
Figure 2: Comparison of LIME and ConLUX-augmented LIME; the ConLUX highlights the kid! Is this a good explanation? Of course, SAM performs a good segmentation of the image, providing an object-level explanation, but the attribution seems incorrect to me. Or did I miss something?

### Questions
For each data point, the concept used can be different. Given that it comes from an LLM, there can even be stochasticity over it (it may also be worth mentioning the LLM temperature setting for this, if not already mentioned). Even otherwise, two very similar reviews can have different concepts chosen for explanation, with no theoretical guarantee on the LLM choosing similar predicates. This lack of control makes the explanation less robust. In theory, changing a token (may be an adversarially crafted one in practice) can change the entire explanation, as the choice of predicates is left to the LLM. One cat may be identified by its ears and a similar one by its eyes. Can you propose an experiment to study this robustness?

### Soundness
2

### Presentation
2

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
- The paper introduces ConLUX a framework designed to enhance model-agnostic explanation methods by transforming traditional feature-level explanations into concept-level ones. 
- The authors argue that mainstream model-agnostic explanation techniques often provide explanations based on low-level features that don't align well with model decision processes or user understanding so ConLUX elevates explanations to the concept level.
- The framework applies ConLUX to different explanation methods (LIME, Anchors, LORE, and Kernel SHAP) across text and image models.

### Strengths
- ConLUX shows promise in being adaptable to multiple existing explanation methods (LIME, SHAP, Anchors, LORE), broadening its application across varied model types.
- ConLUX aims to make model behaviors more intuitive and accessible for end-users, addressing a limitation in feature-based explanations.

### Weaknesses
 **Major**
- One key weakness of ConLUX I felt was that since it shifts to a concept-level perturbations, which are broader and may disrupt the local fidelity of explanations. Unlike small feature-level adjustments (e.g., word or pixel changes in LIME), concept-level changes can alter the input more drastically, potentially leading to explanations that do not accurately reflect the model’s behavior around the specific input instance. To investigate whether these concept-level perturbations maintain local fidelity, I suggest running controlled experiments comparing concept-level and feature-level perturbations. For example, the authors could measure fidelity loss or gain across a gradient of perturbation scales, allowing for a comparison between the fidelity of feature-level and concept-level explanations.
- The paper relies on pre-trained models to extract high-level concepts but does not fully explore whether these concepts are consistently relevant across diverse domains. Variability in concept quality could impact the explanation's reliability. I recommend testing concept quality across datasets from different domains and introducing a metric or using existing ones like TCAV[1] to measure concept relevance and coherence within each domain. 
- Since ConLUX relies on pre-trained models to extract high-level concepts, it inherits any biases present in these models. This reliance could skew the explanations based on the biases embedded in the pre-trained models, which might limit the fairness and reliability of the generated explanations.
- Observed improvement in fidelity metrics, such as AOPC, coverage, and precision, may partly result from the broader concept-level perturbations rather than genuinely enhanced explanation quality. Since larger perturbations at the concept level likely introduce more drastic changes to the model output, they could artificially inflate these scores, making the explanations appear more effective than they might be with finer, feature-level adjustments. To address this, the paper could benefit from controlled experiments using varying perturbation scales, comparing small and large concept-level shifts, to ensure that the fidelity improvements genuinely reflect enhanced interpretability rather than the impact of larger perturbations. I suggest implementing a normalized fidelity metric that adjusts for the magnitude of perturbations.

**Minor**
- A few typos in page 2 "ConLUX-agumented LIME" should be "ConLUX-augmented LIME"

### Questions
- Don’t have much in terms of questions on the methodology itself, but a few conceptual issues stood out, as mentioned in the weaknesses.
- It’d be interesting to see if the authors could run additional experiments with different scales of perturbation to make sure these fidelity gains are actually about better explanations, rather than just larger shifts.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a concept based local explanation method ConLUX that is model agnostic. The authors essentially propose a modality specific concept representations of inputs (concept predicates). These representations also readily provide a procedure to perform perturbation on the predicates and subsequently the input. Combining these two, the method is able to augment the traditional model-agnostic approaches to provide concept based explanations. The authors provide experiments on text (sentiment prediction) and images (classification) with multiple black-box models and explanation techniques and essentially show a clear improvement in terms of various forms of fidelity.

### Strengths
1. The problem setup, what the authors want to solve, and why, is quite clear.
2. The core idea of using a concept-friendly representation for input and combining it with black-box explanation methods is simple and its positive implications are easy to see. 
3. The experiments are reasonably strong. They cover both text, images, and on multiple black-box models, with positive results in all cases. Also, via the existing black-box explainers, the method can generate different types of explanations (attribution, counterfactual etc.)
4. While it has its own weaknesses, the proposal to build visual concept predicates is a principled way that could be readily validated by a user if the concept extraction is incorrect. This aspect of simplicity should positively reflect in its application

### Weaknesses
1. Twice the authors describe (Fel et al. 2023) as using external knowledge to learn concepts. To my understanding, this is a wrong description. They propose a unified class of methods based on dictionary learning that is completely unsupervised. 
2. Typos/Errors: 
    * Rednet (line 448)
    * line 351 should not be in past tense
    * Table 3 caption does not correspond to the table content
3. The method seems only capable to extract coarse visual concepts. Also it can only admit concepts that can be represented as a segmentation mask. In case of text concept predicates, potential risk of some issues arising from using language models for concept detection and predicate-feature mapping. 
4. I felt a lack of examples/illustrations of visual explanations and any deeper qualitative insights the authors might have.

### Questions
1. I am not completely convinced by the strategy of using language models for text concept predicates. While I assume it probably provides the best performance and our generally more than good enough for text-only tasks, they could still be prone to hallucinations in terms of incorrect concept extraction or during generations for perturbation. Did you consider some other method (maybe traditional topic modelling approaches) to validate its concept detection or perturbation outputs. In this sense I like the visual predicates lot more than textual ones.

2. I wonder if you considered an ACE (Ghorbani et al.) + LIME method to compare ConLUX against a concept based reference where you use activation space of an external encoder to cluster superpixels instead of the original model. The concepts can be defined as clusters of superpixels, as in original method. 

Overall, comparing the strengths and weaknesses, I find the method to be just sound and strong enough that I would tilt slightly towards acceptance.

### Soundness
3

### Presentation
3

### Contribution
2
