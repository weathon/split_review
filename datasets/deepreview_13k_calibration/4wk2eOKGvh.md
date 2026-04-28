# Test-Time Ensemble via Linear Mode Connectivity: A Path to Better Adaptation

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 8, 6

## Abstract
Test-time adaptation is a valuable approach for online adjustment of pretrained models to handle distribution shifts in test data. While existing research has focused primarily on optimizing stability during adaptation with dynamic data streams, less attention has been given to enhancing model representations for improved adaptation capability. This paper addresses this gap by introducing Test-Time Ensemble (TTE), which leverages two key ensemble strategies: 1) averaging the parameter weights of assorted test-time adapted models and 2) incorporating dropout to further promote representation diversity. These strategies encapsulate model diversity into a single model, avoiding computational burden associated with managing multiple models. Besides, we propose a robust knowledge distillation scheme to prevent collapse during adaptation, ensuring stable optimization. Notably, TTE integrates seamlessly with existing TTA approaches, advancing their adaptation capabilities. In extensive experiments, integration with TTE consistently outperformed baseline models across various challenging scenarios, demonstrating its effectiveness and general applicability.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a novel test-time ensemble approach that can be seamlessly integrated with existing TTA models to enhance adaptation. Specifically, the proposed framework reduces domain gaps through two ensemble strategies: weight averaging of TTA models and dropout. Additionally, a knowledge distillation strategy is employed to mitigate both noise and bias for improving model robustness under different distribution shifts. 
Extensive experiments are conducted in different TTA scenarios to demonstrate the superiority of the proposed method over existing baselines.

### Strengths
1. Writing quality is good. The paper is well-structured, and clearly written. 
2. Good insights. This paper explores TTA as a domain generalization problem, uncovering linear connectivity within TTA models. This perspective suggests that domain generalization techniques could enhance model representations for TTA tasks. 
3. SOTA performance. The proposed method achieves the state-of-the-art performance via the integration with different TTA models in various scenarios.
4. Ablations. Ablation experiments are provided to verify the effectiveness of the proposed modules.

### Weaknesses
1. Although the results presented in Tables 3 show the performance improvement achieved by the proposed framework in the continual TTA scenario, it is unclear how the method enhances baseline performance in later adaptation stages. Specifically, it's not clear if the improvement is consistent across all adaptation steps or if it's primarily due to the initial adaptation. Additionally, I would like to know if the proposed method addresses the issue of catastrophic forgetting in this context. Does the method prevent the model from losing previously acquired knowledge as it adapts to new data distributions, or does it simply mitigate the immediate performance drop on the current distribution?

Additional question:
Is it possible to extend the proposed benchmark construction method to dense prediction tasks, such as semantic segmentation? It would be very meaningful if it can be applied to various tasks.

### Questions
Please refer to the weaknesses above.

### Soundness
3

### Presentation
4

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
The paper proposes a method called Test-Time Ensemble (TTE), which uses an ensemble strategy to dynamically enrich model representations during online test-time adaptation (TTA). TTE constructs an ensemble network by averaging the parameter weights of different TTA models, which are continuously updated using test data. This weight averaging technology captures model diversity and improves representation quality without increasing the computational burden of managing multiple models. TTE further combines dropout to promote diverse collaboration of representations within TTA models, and also proposes a debiased and noise-resistant knowledge distillation scheme to stabilize the learning of TTA models in the ensemble. TTE can be seamlessly integrated with existing TTA methods, enhancing their adaptive capabilities in various challenging scenarios.

### Strengths
1. TTE utilizes an ensemble strategy to dynamically enrich model representations during online test-time adaptation (TTA), which is an interesting approach.
2. TTE constructs an ensemble network by averaging the parameter weights of different TTA models, and this weight averaging captures model diversity, improving representation quality without increasing the computational burden of managing multiple models.
3. TTE further promotes the diversity of representations within TTA models by combining with dropout, and proposes a debiased and noise-resistant knowledge distillation scheme to stabilize the learning of TTA models in the ensemble.
4. The experiments are extensive and the results are superior to other compared methods.

### Weaknesses
1. The TTE method involves multiple hyperparameters, such as the momentum coefficient , dropout ratio and temperature, which may affect the stability and generalization of the method. Further research on how to reduce the dependence on hyperparameters is crucial. Specifically, the interaction between these hyperparameters and their combined effect on the final performance is not well explored. For instance, how does the momentum coefficient affect the convergence of the ensemble when combined with different dropout ratios, and how does the temperature parameter in knowledge distillation interact with these settings? A systematic analysis of these interactions is needed to ensure the robustness of the method.
2. TTE integrates many well-established techniques such as ensemble, dropout, knowledge distillation, which have been utilized in TTA or few shot learning. The combination has weaken the novelty of the paper, and the unique contributions of the paper should be classified. While the paper combines these techniques, it does not clearly articulate how the specific combination and modifications lead to a novel approach compared to existing methods that use similar techniques. The paper needs to highlight the specific modifications and their impact on the overall performance, rather than simply stating that these techniques are combined.
3. How to conduct the weight-space ensemble without adding computational complexity? Will the technique increase storage consumption? The paper claims that the weight averaging reduces computational burden, but it does not provide a detailed analysis of the computational cost of the proposed method compared to other TTA methods. A clear analysis of the computational complexity, including the time and space complexity, is needed to justify this claim. Furthermore, the paper should discuss the memory overhead of storing multiple model weights, even if they are averaged.
4. The knowledge distillation-based debiasing and anti-noise strategies proposed in the paper may not be able to completely solve the problem of noisy test data. How to solve the scenario that the pseudo labels are incorrect? The paper does not provide a clear mechanism to handle the scenario where the pseudo labels generated by the ensemble are incorrect. The proposed debiasing strategy may not be sufficient to address this issue, and the paper should discuss alternative strategies or limitations of the proposed method in handling incorrect pseudo labels.

### Questions
1. Why the results of CoTTA in Continual TTA with non-i.i.d. conditions are only 2.2% and 3.4%?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces the Test-Time Ensemble (TTE), a method designed for TTA using the theory of weights space ensemble, which can be used on top of different TTA methods. The authors show different results for TTA over corruptions with different baselines, and the method seems to work pretty well. Furthermore, the authors also provided results for continual TTA, which is interesting.

### Strengths
The paper is well-written, easy to follow, and detailed. I liked how the authors presented the work and motivated toward the problem. Furthermore, the results are motivating, and the idea seems easy to implement on top of different methods (as demonstrated by the authors), which can be beneficial for the community if the authors also provide the full code for reproducibility.

### Weaknesses
Personally, I did not see many problems with the paper, but I would suggest the authors proofread again to avoid problems such as the following typo "with lager and more complex" -> "with larger and more complex" in the introduction or "Adaptvie momentum" ->  "Adaptive momentum."  

If the authors work on the following points, it will improve a lot the quality of the work: 
- I am not so convinced by section 3.2, DE-BIASED AND NOISE-ROBUST KNOWLEDGE DISTILLATION. Could you clarify this a bit more in this section? And maybe make it more clear in the paper.

-  In Equation 5, there is no hyperparameter to balance the terms. I think it should be included, right? 

- For Table 3, with continual TTA, the authors compared all other baselines with TTE with DeYO, but not TTE with other variants as well, and for continual TTA, I don't understand how the performance can still perform well in the direction of the adaptation without degrading too much as we can see in the other approaches (for example DeYO goes from 28.1 to 3.7 and then 7.2), for me it only make sense if you ensemble with zero-shot model as well (or reset the model weights) but if this is the case it should be done for all other baselines as well.
 
- For Table 4, column V2 seems strange, as almost all results in a) are 68.9, even DeYO and DeYO with TTE. Could you also add more results with other batch sizes? (the batch size can play an important role in different algorithms, which can benefit DeYO and not the others. For instance, I recommend taking a look at the paper "Bag of Tricks for Fully Test-Time Adaptation, IEEE/CVF Winter Conference on Applications of Computer Vision. 2024",  which shows the role of batch size in some of the TTA algorithms.

- I would suggest revisiting some of the baselines for Tab 1. I would also consider a baseline with other methods of the local ensemble as well, such as SWA with TTA, and for Tab 4. I would also add other methods with TTE (maybe in the supp. material).

### Questions
Here, I am adding the questions that I find relevant for improving the work quality; some of them were already discussed in the Weaknesses section:

- Could you clarify this a bit more in section 3.2? How is it important for the method?

- Do you think the batch size can impact the results, especially the ones provided for the continual TTA?

Please consider answering the points on the weaknesses as well. Furthermore, I am open to discussion, and I think that the work has a good potential for the community.

Rebuttal period: After carefully reading all the answers provided by the authors, I feel that my questions were answered, and I don't have any additional questions. I am confident to change my decision from "marginally above the acceptance threshold" to "accept, good paper".

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper considers a new problem, test-time ensemble (TTE), which aims at using multiple models generated during TTA. This paper first formulates the test-time ensemble problem. The paper also proposes the weight average and dropout as the baseline methods to evaluate the performances. 

The contributions can be summarized as: 

(1) The author revealed that TTA models exhibit linear mode connectivity, an in- triguing insight that simplifies and enhances the adaptation process.

(2) The author introduced Test-Time Ensemble (TTE), a novel and computationally efficient approach that not only enriches model representations but also stabilize TTA optimization through de-biased and noise- robust knowledge distillation.

(3) TTE integrated effortlessly with existing TTA methods, enhancing adaptation in diverse scenarios and showing potential for applicability to future TTA methods.

### Strengths
(1) This paper proposes the new problem, test-time problem, which is different from previous test-time adaptations. I believe this problem has some practical applications.

(2) The paper proposes some simple baseline methods that can effectively address the problem.

### Weaknesses
 (1) The analysis of test-time adaptation does not inspire the new methods. The moving average ensemble methods are popularly adapted in self-supervised learning and ensemble methods. I consider the Linear Mode Connectivity theory should tell the reason and the situation that the models generated during test-time adaptation.


(2) Limited technical novelty: this paper proposes the two-branch structure and leverage the weight average to improve the performance. Similar techniques are implemented in https://github.com/huggingface/pytorch-image-models. I do not see anything new compared to what have been proved in image classification.


(3) Unclear description. In section 3, the de-biased distillation subsection does not describe clearly where the bias comes from. I suggest the author should explain the bias again. Also, I can not understand what the connection between the spike phenomena of the accuracy curve and the bias.

### Questions
Please see the weakness.

### Soundness
3

### Presentation
2

### Contribution
2
