# Stagewise Development in Transformers and the Geometry of the Loss Landscape

- Decision: Reject
- Scores: 6, 5, 5, 6

## Abstract
Deep learning involves navigating a high-dimensional parameter space guided by the loss landscape. In the process, complex computational structures form and re-form inside the neural network, leading to shifts in input--output behavior. It is a priority for the science of deep learning to uncover principles governing the development of neural network structure and behavior. Drawing from the framework of singular learning theory, we propose that model development is governed by the local geometry of the loss landscape. We investigate this link by monitoring the geometry of the loss landscape throughout training for transformers trained as language models or for a synthetic in-context regression task. We divide training into ``developmental stages'' marking discrete shifts in loss landscape geometry. We then confirm that these stages coincide with significant changes in the internal computational structure and the input--output behavior of our models. Our findings provide new insights into transformer development and underscore the potential of a geometric perspective for understanding modern deep learning.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper investigates the emergence in stagewise development of internal structures in the training of transformer models, specifically for tasks like language modeling and in-context linear regression. The authors utilize the Local Learning Coefficient (LLC) to measure geometric degeneracy in the loss landscape and identify distinct training stages of the model’s behavior and internal structures. Beyond general loss decreases in model training, the authors discover several stages in which the geometry becomes more degenerate linking to a phenomenon named “layer normalization collapse”. These findings provide valuable insights into the complex processes of transformer training and underscore the importance of loss landscape geometry in understanding model development.

### Strengths
1. The paper introduces a novel method Local Learning Coefficient (LLC) to identify the stage boundaries
2. The evaluation methods proposed in this article have been verified for two different types of tasks providing an enhanced understanding of transformer model training.
3. Bring a new insight to the model stability and robustness by showing a phenomenon of “layer normalization collapse”.

### Weaknesses
1. This method has certain limitations in model selection. The language model only has 3 million parameters. Perhaps these methods cannot be directly generalized to large models such as GPT and BERT. Therefore, the universality of this model needs to be verified.

2. The LLC method has certain limitations. Because it's estimation will be affected by the training parameters. When the parameters are not the local minimum of the loss, the estimation of LLC might have some bias. Though the article attempts to estimate through the SGLD method, since LLC is sensitive to hyperparameter selection, this instability will affect the credibility of experimental results.

3. The author proposed the concept of "layer normalization collapse", but lacked some more in-depth discussions such as the causes and some quantitative analysis. These analyzes will add to the value of this study.

### Questions
1. Can this method be extended to a larger range of tasks such as image processing? Can similar patterns also appear?

2. Do you have theoretical reasons to believe your method would or would not scale to larger models?

3. Could you provide metrics on the rate or extent of collapse across different model sizes or training regimes.

For other questions, please refer to weakness.

### Soundness
3

### Presentation
2

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
This paper employs "Local Learning Coefficient" (LLC), a recently proposed metric, to measure the geometry of loss landscape during training transformers.

By conducting experiments on two-layer attention-only transformers on some simple tasks, the authors find that the training could be divided into several discrete development stages according the LLC features.  And then different behavioral and structural features are found among different stages.

This work could bring meanings to reveal the learning mechanistic (and decrete development) for transformers.

### Strengths
1. This work finds there are some discrete development stages for transformers via analyzing the geometry of loss landscape. It could bring insights for related works about mechenistic interpretability to transformers.

2. I like the analyses in Stage validation section, which tries to connect LCC trend and some visible important features, though I also have some questions about this section.

On the whole it is an interesting work and I expect to have more discussion in rebuttal period. I am open to improve the score if my following concerns are well addressed.

### Weaknesses
1. I am concerned about the theory adopted in this paper, LLC. It seems that the theory of LLC is not widely accepted in the research community and may subject to potential pitfalls and limitations. The lack of peer-reviewed studies on LLC means that we have a limited understanding of its applicability, reliability, and overall validity. Specifically, the paper does not adequately address the sensitivity of the LLC metric to various factors such as the choice of optimizer, batch size, and the specific SGLD implementation details. The paper should include a more thorough discussion of these potential confounding factors and their impact on the observed developmental stages.

2. In Section 4.3, the authors state that First-layer previous-token heads start to form, and the evidence is that Figure 2(b) top. However, I think it is more like a confuse cause and effect. After the authors discover that two specific heads start to have high previous-token score in LM3 stage, the previous-token heads, 1:2 and 1:5, are then indicated. Whilest, In LM2 stage, there are already many heads that get high scores, why aren't they the previous-token heads? Furthermore, LM3 seems less meaningful compared to other stages. The paper needs to provide a more rigorous definition of what constitutes a "previous-token head" beyond just a high previous-token score, and explain why other heads with high scores in LM2 are not considered as such. The connection to the induction circuit also needs to be made more explicit.

3. I think this paper might neglect the writing of some specific experimental implementation methods, which needs to be clarified more.
- LCC is based on the measure of loss. How do you measure loss? Specifically, what dataset or distribution (and how many samples) do you use to measure loss? Would different dataset lead to totally different results? (that is, different loss landscapes for different validation datasets). The paper should specify the exact dataset used for calculating the loss during LLC estimation, including the size of the dataset and the method of sampling. It should also discuss the potential impact of using different datasets on the resulting LLC curves and the identified developmental stages. A sensitivity analysis on the choice of validation dataset would be beneficial.

[1] Lau, Edmund, Daniel Murfet, and Susan Wei. "Quantifying degeneracy in singular models via the learning coefficient." arXiv preprint arXiv:2308.12108 (2023).

### Questions
1. In Figure 1, would the training process contain more stages (i.e. d(LCC)/dt = 0 points) if you lengthen the training? If there are more stages, what is the corresponding features (behavior and structure) and why do you think the first 5 stages are the most important?

2. What is the mathematical basis for d(LCC)/dt = 0 points? Why are these points critical and able to become the boundary of development stages (from mathematical perspective)? Otherwise, is this a target-guided results (that is, we have discrete stages first and we dig the math features of the boundary)?

3. I notice that this paper did not employ a learning rate scheduler throughout the training process. Though to some degree I acknowledge the setup for controlling variables, learning rate is a very important factor to determine the loss landscape. Many previous works point out that lower learning rate helps models to converge to a local minimum, and decayed learning rate can help models generalize better due to more flattened local minimum. What do you think about the impact of learning rate schedule on your work?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces the Local Learning Coefficient (LLC) as a novel approach to explain phase transitions in transformer training dynamics. LLC is calculated by measuring the expected difference between the posterior and local optimal solutions. The authors establish connections between LLC and the geometry of model likelihood, offering a new perspective on transformer learning behavior.

### Strengths
- Introduces a new metric (LLC) for analyzing transformer training dynamics and phase transitions, providing an alternative to traditional per-token loss measures

- Presents comprehensive experimental analysis with thorough ablation studies

- Provides detailed methodology and experimental setup documentation

### Weaknesses
 - The relationship between loss changes and LLC lacks clear description. While Table 1 presents changes in both ICL loss and LLC, it 
 does not establish a definitive connection to phase transitions. In Figure 1 the dynamics of ICL loss and LLC do not match or describe the phrase transitions.  The paper can benefit from quantitative correlation metrics between ICL and LLC to strengthen the qualitative observations.

- Despite extensive analysis, the paper primarily reinforces existing findings from Olsson et al. (2022) rather than presenting novel insights into transformer learning dynamics

### Questions
1. What are the specific advantages of LLC over per-token loss that justify its adoption as a preferred metric for analyzing transformer training dynamics?

2. The LLC computation relies on finding $w*$ (local minimum) through stochastic Langevin dynamics. How can LLC be reliably estimated with respect to weights $w_t$ during the actual training process?

### Soundness
2

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
2

### Summary
This paper leverages the LLC as metrics to establish the developmental stages for language modeling of transformer and in-context linear regression. These stages reveal the developmental changes of models in language modeling.

### Strengths
1.	The authors analysis the behavioral and structural changes of each stages to confirm the meaning of LLC, and each stage actually has the valuable behavioral changes to reveal the learning process in the language modeling.
2.	The paper uses the realistic data to train analysis the language modeling of transformer.
3.	The experiment is adequate and reasonable and the paper is well written.

### Weaknesses
1.	The used transformers are one and two layer attention-only. Whether the same behavioral and structural changes can be seen in more larger transformer. The scaling may affect the loss landscape.

### Questions
The same as above.

### Soundness
4

### Presentation
3

### Contribution
3
