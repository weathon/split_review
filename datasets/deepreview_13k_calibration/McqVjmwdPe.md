# How to Weight Multitask Finetuning? Fast Previews via Model Merging

- Decision: Reject
- Avg Score: 5.75
- Scores: 8, 6, 6, 3

## Abstract
When finetuning multiple tasks altogether, it is important to carefully weigh them to get a good performance, but searching for good weights can be difficult and costly. Here, we propose to aid the search with fast previews to quickly get a rough idea of different reweighting options. We use model merging to create previews by simply reusing and averaging parameters of models trained on each task separately (no retraining required). To improve the quality of previews, we propose a Bayesian approach to design new merging strategies by using more flexible posteriors. We validate our findings on vision and natural-language transformers. Our work shows the benefits of model merging via Bayes to improve multitask finetuning.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes to create previews to identify optimal weightings for tasks in multi-task finetuning setting. The approach creates previews of performance under various weight configurations and uses bayesian model-merging approach to combine separately fine-tuned models via baysian posteriors model weights merging. The proposed method allows practitioners to get an rough performance estimation without trying various weighting exhaustively.  The approach is experimented on both vision and language tasks, demonstrating its efficacy across different model types and tasks.

### Strengths
1. Motivation of this paper is strong. Finding proper balance between tasks in multitask finetuning has always been challenging for heavy training jobs (large models or large amount of data). The paper focuses on a very important research problem. 
2. The proposed approach is novel - a bayesian merging strategy using flexible posteriors (gaussian) and use misxtured-based merging for better accuracy. 
3. The paper is well written.
4. The proposed approach is effective on various tasks and architectures, demonstrating good generalization.

### Weaknesses
1. There isn't enough analysis of computation overhead of the proposed approach. Specifically, the paper lacks a detailed breakdown of the computational cost associated with each step of the proposed method, such as the cost of computing the Hessian approximations, the merging process itself, and how these costs scale with the number of tasks, model parameters, and dataset size. A comparison against standard multi-task training methods in terms of FLOPs or wall-clock time would be beneficial.
2. The paper doesn't have enough discussions of its limitations. While the paper demonstrates the effectiveness of the approach, it does not adequately discuss scenarios where the method might fail or underperform. For example, it is unclear how the method would perform if the tasks are highly conflicting or if the optimal weight configuration lies outside the space explored by the preview method. Furthermore, the paper does not discuss the sensitivity of the method to the choice of hyperparameters, such as the number of mixture components or the number of training steps for the surrogate models.

### Questions
Can this approach be widely adopted for multitask learning training? 


Do you plan to release the code? Is it easy for people in the community to use your code for their own multitasks training jobs?

What are the limitations?

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
This paper presents a novel approach for efficiently identifying task weightings in multitask finetuning by quickly previewing/estimating the performance of different tasks using Bayesian model merging techniques. The authors propose to use Bayesian posteriors as surrogates to estimate performance across various weightings. In addition, the exponential family distributions are further introduced to create more flexible and accurate surrogates. The approach is validated through experiments on diverse tasks including a series of CV and NLP tasks to demonstrates that the effectiveness of the previews on multitask weightings.

### Strengths
1. The paper is overall well-written and the motivation is clear.
2. The Bayesian learning method establish a rigorous mathematical framework, providing a principled approach to derive and enhance the weighting selection strategy on model merging.

### Weaknesses
 - There is limited quantitative analysis of the computational savings(or practical time savings) across different tasks compared to exhaustive grid search. The mixture-based approach may become computationally intensive for large models or when dealing with a large number of tasks.
- Some trends have not been precisely captured by either Hessian-weighted merging or simple merging (Fig 6(b) & Fig 6(c)).

### Questions
Questions have been covered in the weaknesses section.

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
2

### Summary
The paper leverages model merging to create fast previews for identifying optimal weights for each task in multitask finetuning. This approach enhances efficiency and effectiveness by providing quick guidance on reasonable search areas. Specifically, the paper proposes a Bayesian method that employs more flexible posteriors to improve the quality of these previews. Various experiments demonstrate that the method can effectively preview suitable multitask finetuning weightings.

### Strengths
The method can alleviate the costly burden of exhaustive searching in multitask finetuning by reusing the parameters of models trained on each task separately, eliminating the need for retraining to find the optimal weights. It also provides insights that focusing solely on the best-performing weights in model merging may not always yield high-quality previews.

### Weaknesses
It is unclear whether the weights chosen for each task by the method will be used for further multitask finetuning. If they are, the method appears to be less computationally efficient because it requires training the models for each task initially. If they are not, the accuracy of the merged model seems to lag significantly behind joint training on average, as shown in Figures 4, 5, and 6, suggesting that a simple grid search of joint training could outperform model merging. Additionally, the paper lacks comparisons with other reweighting or model merging methods.

### Questions
On average, how long does it take to converge for Simple Merging, Hessian-Weighted Merging, and Mixture-Weighted Merging?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper focus on selecting optimal weights in multitask fine-tuning. The authors propose a Bayesian model-merging approach that previews different weighting configurations efficiently by leveraging model merging, thus reducing the need for exhaustive retraining on each configuration. The steps can be decomposed to:
1. Finetune $T$ models (denoted by $\boldsymbol\theta_t)$ each seprately over their own task $\ell_t(\boldsymbol{\theta}).$
2. Use Bayesian learning to build surrogate $\ell_t\approx\widehat{\ell}_t$ by using $\boldsymbol{\theta}_t.$
3. Create previews by fınetuning over $\sum_t\alpha_t\widetilde{\ell}_t$ for many $\boldsymbol{\alpha}$ values.

### Strengths
The Bayesian optimization based model-merging allows for quick performance previews by averaging parameters from separately trained task-specific models, avoiding full retraining.

### Weaknesses
 - The method relies on a standard application of Bayesian optimization with a surrogate model, lacking novel contributions or distinctive techniques.

- In the steps listed between lines L148 and L151, while the three initial steps are understandable, the sequence is left open-ended. It’s unclear what action follows the third step—what process or computation does the algorithm proceed with after generating the previews?

- In the section between lines L270 and L280, the definitions and relationships among variables are unclear. For instance, the connection between $\hat{\pi}{tk}$ and $\pi{k}$ should be clarified. Additionally, if $h_{tk}$ is a scalar, it should not be in bold, as this can lead to confusion.

- There is a lack of a clear evaluation criterion. What mathematical definition is used to judge “better previews,” and what specific objective or performance metric is this algorithm designed to optimize?

- The numbers in the figure (e.g., 90, 85, 80, ...) are labeled as accuracy, but it is unclear what these accuracy values represent. Are they calculated based on an equal weighting across three tasks? Please define the metrics and explain the weighting, if any, to clarify the interpretation.

- The three tasks listed—French, Spanish, and English—are somewhat unclear in meaning. What does “accuracy for English” specifically indicate in this context? Please provide a clear explanation of how accuracy is determined for each language task and what each result represents.

- As a reader, the takeaway from the experimental section remains ambiguous. There doesn’t appear to be a consistent or clearly stated conclusion. Could you provide a concise summary of the findings or implications drawn from this section to clarify its purpose and insights? Otherwise, the paper seems to give me an impression of an application of Bayesian optimization.

### Questions
- The numbers in the figure (e.g., 90, 85, 80, ...) are labeled as accuracy, but it is unclear what these accuracy values represent. Are they calculated based on an equal weighting across three tasks? Please define the metrics and explain the weighting, if any, to clarify the interpretation.

- The three tasks listed—French, Spanish, and English—are somewhat unclear in meaning. What does “accuracy for English” specifically indicate in this context? Please provide a clear explanation of how accuracy is determined for each language task and what each result represents.

- As a reader, the takeaway from the experimental section remains ambiguous. There doesn’t appear to be a consistent or clearly stated conclusion. Could you provide a concise summary of the findings or implications drawn from this section to clarify its purpose and insights? Otherwise, the paper seems to give me an impression of an application of Bayesian optimization.

Please kindly try to answer my questions in both weakness and questions part. Thank you!

### Soundness
2

### Presentation
2

### Contribution
1
