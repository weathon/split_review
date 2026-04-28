# Interactive-Action Image Generation via Synthetic Physical Priors

- Decision: Reject
- Avg Score: 5.20
- Scores: 6, 8, 3, 6, 3

## Abstract
While diffusion-based text-to-image generation has made notable advancements, generating accurate images containing interactive actions remains a challenge due to the lack of inherent physical and spatial priors. To address this problem, we propose a novel pipeline that synthesizes a dataset enriched with physical priors using a graphics engine, combined with a captioning technique. Building on the dataset, we introduce a distillation-structured fine-tuning method, where a teacher network assists in inverting the semantics of interactive actions, leveraging the synthesized priors effectively. This fine-tuning method disentangles the synthetic data features while mitigating random misalignment during the fine-tuning process. Extensive experiments demonstrate that our method not only achieves state-of-the-art results but also highlights the synthetic data's potential to be applied more broadly in enhancing the generation of interactive action images.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work focuses on the interactive actions image generation based on pretrained text-to-image diffusion models, where a customized synthetic dataset with interactive actions is provided to finetune the pretrained model to improve the spatial and interactive action aware diffusion models.The finetune stage is akin to distillation procedure to address the problem of disentanglement and text-visiual misalignment. The experimental results demonstrate the effectiveness, especially the interactive actions between objects, of the proposed model.

### Strengths
- The paper is easy to follow. This work clearly identifies the weakness of generating interactive actions in current t2i models and proposes a effective solution to address the limitation.
- The method design is well-motivated, including the usage of curated dataset and the specific distillation training framework to take advantage of both pretrained prior and the new learned knowledge.

### Weaknesses
 - While this work demonstrates the effectiveness on several interactive actions, it is unclear how well the method generalizes to a wider range of more complex interactions. Specifically, the paper does not explore the limitations of the proposed method when dealing with more intricate scenarios, such as those involving multiple objects interacting simultaneously or actions that require a deeper understanding of physical constraints and affordances. Moreover, is the model capable of dealing with actions related to more than two objects, and if so, what is the performance degradation as the number of interacting objects increases?
- The motivation of IAScore is clear, however, its reliance on detection introduces potential errors. The paper does not provide a thorough analysis of the impact of object detection inaccuracies on the final IAScore. A more detailed analysis of the reliability and limitations of this metric would make it more credible, including a discussion of how detection errors (e.g., false positives, false negatives, inaccurate bounding boxes) propagate and affect the evaluation results. It would also be beneficial to see a comparison of IAScore with other metrics that do not rely on object detection.

### Questions
Please refer to the weakness part for more details.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper first points out that existing diffusion models tend to struggle with verbs that describe relationships between objects. To address this, the authors propose a method for fine-tuning these diffusion models to better capture action-related information. They generate synthetic data representing actions using robot simulation model, SAPIEN, and train a special token following a textual inversion framework. To account for the domain gap between synthetic and real images, they employ a distillation learning approach for fine-tuning. The proposed method shows improved results compared to previous studies on the evaluation benchmark designed by the authors.

### Strengths
- The use of robot simulation to generate datasets for certain actions is an interesting and innovative approach.
- The paper clearly explains the challenges encountered during the development and the method is well described without ambiguity.
- The authors introduce new metric for evaluating the proposed task, and clearly present comparison results with previous studies.

### Weaknesses
 - The proposed method is limited to simple actions that can be performed in robot simulations, such as picking up or pulling something. More complex actions like tickling or shaving cannot be represented in this way, making it difficult to train on broader action concepts.
- The use of distillation learning increases the training load compared to previous studies.

### Questions
Regarding the weakness mentioned above, how can a dataset be generated for more complex actions?

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
4

### Summary
This paper proposes a method to improve the capacity of text-to-image diffusion models to generate interactions by fine-tuning the model on synthetic data. To address the domain gap between the synthetic data and real images, the author developed a distillation approach to preserve the performance of the mode in generating the realistic style while still learning the interactions from the synthetic data.

### Strengths
This paper studies the interesting and important problem that visual generative models lack the proper knowledge about the physical world and are not able to properly generate physical-plausible actions. The authors propose reasonable fine-tuning-based methods and collect synthetic data from a simulator to address this problem. The authors show that the existing methods do not work well due to the synthetic-real domain gap. Ablation studies are performed to help understand the function of each component.

### Weaknesses
My major concern about this paper is its motivation to improve the ability of text-to-image models to generate human/animal-object interactions. With the improved performance of the base generation, I have been seeing this as less and less of a problem. In many of the examples shown in the papers where SD1.5 fails to generate correct interactions, the latest models, like SD3 and Flux, can do pretty well. That being said, I do believe that there are many actions that cannot be accurately described by the language. However, I don't see current methods as a solution to that, as there are cases where the learned motions are not clearly matched with the training images. For example, in the third row of the teaser image, the robot arm picks up the objects with two hands, while the generated images mostly contain a subject holding an object with one hand. Also, I also have the following concerns:

1. There are some conflicts between the different losses, i.e., the distillation loss would conflict with learning the interaction through the synthetic data, which is also verified by the ablation study in Figure 8 (c). The optimal trade-off between two losses may not be the same for different interactions.

2. The issue with overfitting the synthetic data has been studied, and the function of the proposed distillation loss is quite similar to the class-specific prior preservation loss. Although the authors claim that real data is not common, robot manipulation datasets like BridgeDatav2 and DROID datasets do exist. 

3. There exists another gap that the interaction between the robot arm and objects is quite different from how humans interact with objects - the robot arm typically does not have a similar structure compared with human hands. Instead, one could just collect more human-object interaction data. And there do exist such datasets, like Epic Kitchen, Hands23, and Ego4D.

### Questions
I do not have additional questions.

### Soundness
2

### Presentation
2

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
The paper presents a method to enhance diffusion-based text-to-image generation for interactive actions by synthesizing a dataset with physical priors using a graphics engine. It introduces a distillation-based fine-tuning approach that improves understanding of interactive actions and reduces misalignment. Experiments show that this method achieves state-of-the-art results and expands the use of synthetic data in generating interactive images.

### Strengths
1. This paper propose a novel method that synthesizes a dataset enriched with physical priors using a graphics engine.
2. This paper introduce a distillation-structured fine-tuning method using SD.
3. Qualitative results are good compared to the baselines.

### Weaknesses
1. It is challenging to evaluate this as a new approach. However, the authors propose a new metric, the IAS score, and evidence is needed to demonstrate that this metric in the evaluation. Specifically, the paper needs to provide a more rigorous justification for the IAS score's design and its correlation with human perception of interactive action quality. The current explanation lacks sufficient detail to establish its validity as a reliable evaluation metric. For example, it's unclear how the score handles different types of interactive actions, or how sensitive it is to minor variations in the generated images.

2. There is a lack of quantitative analysis for the ablation studies. (such as, preposition word ..) The absence of quantitative results for the ablation studies makes it difficult to assess the individual contributions of different components of the proposed method. For instance, the impact of specific preposition words on the generation quality is only evaluated qualitatively, which is insufficient to draw strong conclusions. A quantitative analysis, such as measuring the change in a relevant metric (e.g., image similarity, action accuracy) when specific prepositions are included or excluded, is needed to support the claims.

3. The authors released the code in the supplementary materials. Is it possible to view more samples of the dataset or generated results? The lack of a comprehensive dataset and generated sample visualization makes it difficult to fully understand the scope and limitations of the proposed method. The supplementary material should include a more extensive collection of examples, covering a wider range of interactive actions and scenarios, to allow for a more thorough evaluation of the method's performance.

4. I am curious about if SD-XL or other models were used instead of SD1.5. The choice of using SD1.5 as the base model raises questions about the method's generalizability to more advanced text-to-image models. The paper should explore the performance of the proposed approach with other models, such as SD-XL, to demonstrate its robustness and potential for further improvement.

### Questions
Please refer to the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper addresses the issue of text-to-image generation models struggling to accurately depict interactive actions (e.g., "a person picks up a cup"). To address this, the authors generate a synthetic dataset enriched with physical constraints using a graphics engine. They train the model through a teacher-student network with distillation learning, enhancing the model's ability to capture spatial and interactive relationships. The approach reduces alignment issues between subjects and objects, improving realism in generated images.

### Strengths
* The distillation-based method is a straightforward yet reasonable approach.
* The authors address a challenging task effectively.
* They propose a new metric for evaluation.

### Weaknesses
 * Limited Interaction Complexity: The paper focuses on single-object manipulation, which seems somewhat limited in scope.
* The qualitative results seem somewhat lacking. It seems this issue should be addressed through the proposed distillation method.

### Questions
* In the paper, they compare performance with ReVersion fine-tuned on their dataset, which is fair; however, the original ReVersion paper also demonstrates strong performance. For a more comprehensive comparison, the authors should include additional experimental results using the original (non-fine-tuned) ReVersion model.

* The ablation study shows that 'and' improves semantic understanding, while 'or' enhances visual representation. What is the reason for this conflict?

* Can the model perform in more complex interactions, such as multi-object manipulation or tool use (e.g., hammering a nail, tightening a screw with a screwdriver)?

### Soundness
1

### Presentation
1

### Contribution
2
