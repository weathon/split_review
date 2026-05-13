# Enhancing Cognition and Explainability of Multimodal Foundation Models with Self-Synthesized Data

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Large multimodal models (LMMs) have shown impressive capabilities in a wide range of visual tasks. However, they often struggle with identifying domain-specific objectives and fail to explain their predictions reasonably. To address the above challenge, we propose a novel iterative visual fine-tuning framework to improve the effectiveness and explainability of LMMs using self-synthesized data. Specifically, visual fine-tuning requires images, queries, and target answers. Our approach begins by synthesizing interpretable answers that include human-verifiable visual features. These features are based on expert-defined concepts, carefully selected based on their alignment with the image content. After each round of fine-tuning, we apply a reward model-free filtering mechanism to select the highest-quality interpretable answers for the next round of tuning. This iterative process of data synthesis and fine-tuning progressively improves the model's ability to generate accurate and reasonable explanations. Experimental results demonstrate the effectiveness of our method in improving both the accuracy and explainability of specialized visual classification tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper propose a new framework to improve LMMs in domain-specific visual classification by enhancing cognition and explainability through iterative finetuning and the Information Bottleneck principle. This approach boosts accuracy and interpretability without extensive annotations, making LMMs more applicable in specialized fields. Future work may explore more complex tasks and scalability improvements.

### Strengths
* The writing of the paper is logically clear and easy to follow.
* An interesting and effective self-improving approach, which enhances the model's performance in fine-grained classification tasks.

### Weaknesses
 * need evaluate on more general benchmarks, e.g. MMVet, MMStar, and SEED-Bench2...
* it is better to report experimental runtime.
* missing important ablation study: to validate the effectiveness of the two data selection strategies, results using unfiltered data for training should be provided as a comparison baseline.
* minor: In Table 1, highlighting the best results would improve readability.

### Questions
* is the choice of text encoder significantly impact the results of data selection?
* is there any qualitative example that demonstrate the effectiveness of the data selection strategy?

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
In this paper, the authors argue that the limited domain-specific knowledge in the current the LMMs. The main challenge for such limited parametric knowledge is on lack of data to further fine-tune the models. Accordingly the authors propose a new synthetic data generation pipelines from the model themselves and fine-tune the models with the generated data to enhance domain-specific cognitive capabilities.

### Strengths
The main challenge for data generation synthesis is on how to assure the self-generated data quality and its reliability. The authors cleverly employ information bottleneck theory to extract intersect knowledge from exterior knowledge (such as from expert or gpt-like models) and the visual contents. In addition, by introducing a doubly robust rejection sampling strategy improves both the accuracy and interpretability of the model prediction.

### Weaknesses
Evaluation is somewhat limited due to the main results are mainly conducted on classification task. Therefore, during the fine-tuning stage with the synthesized data, it can potentially negatively impact the general model QA capabilities.

### Questions
1. What are the trainable parameters during the fine-tuning stage? The text-aligned vision encoder such as CLIP lacks detailed visual perception due to the training nature (focusing on contrastive learning with paired text supervision). The reviewer wonders where the performance gain is obtained from. If fine-tuning is only applied to the parametric knowledge of the LLM side, does this adequately address the encoder’s deficiencies in processing complex visual data?

2. Continually, the reviewer wonders whether there are any negative effects of using synthesized data for fine-tuning. Could this potentially harm the model's general QA capabilities? Can the authors compare the general benchmark results before and after the finetuing?

### Soundness
3

### Presentation
3

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
This paper proposes a novel framework to improve the explainability of large multimodal models (LMMs) in visual classification tasks. The authors address the challenge of LMMs struggling to identify domain-specific objectives and explain their predictions. Their approach involves fine-tuning LMMs using self-synthesized data, which includes interpretable answers containing human-verifiable visual features. The framework iteratively generates high-quality training data by leveraging the model's captioning abilities and filtering synthesized outputs using a reward model-free mechanism. This method enhances the model's ability to generate accurate and justifiable explanations for its classifications, without relying on extensive manual annotations. The paper presents experimental results demonstrating the effectiveness of the proposed framework across various datasets and discusses the theoretical foundations behind it.

### Strengths
*   **Clear Problem Identification and Justification:** The authors successfully identify the challenge of LMMs struggling with domain-specific visual classification and explainability. They pinpoint insufficient domain-specific alignment as the root cause, highlighting that LMMs often fail to link key visual features with correct labels and provide justifiable explanations for predictions. 
*   **Significant Accuracy Improvement:** The paper demonstrates a substantial increase in classification accuracy through its proposed method compared to training with labels alone. The authors showcase this improvement across multiple iterations, highlighting the efficacy of their approach in achieving more robust classification.
*   **Novel Framework and Theoretical Grounding:** The authors introduce a novel framework for enhancing LMMs' domain-specific cognition and explainability using self-synthesized interpretable answers. The framework's two key steps, image-level visual concept selection and reward model-free rejection sampling, are thoroughly described and grounded in information theory. 
*   **Multifaceted Evaluation of Explanation Quality:** The authors address the difficulty of assessing explanation quality without ground truth annotations by employing a multi-faceted evaluation approach. This involves metrics like Explanation Existence (EE), Cognition Score (CS), and Fluency Score (FS), each offering insights into different aspects of the generated explanations. 
*   **Clear Writing and Presentation:** The paper is commended for its clear writing, making it easy to understand the presented concepts and methods. The use of illustrative figures and tables further enhances the clarity and impact of the research.

### Weaknesses
 *   **Generalization to Unseen Categories:** The paper doesn't explicitly address the model's ability to generalize to unseen categories. While the method shows promise in fine-grained classification within specific datasets, it remains unclear whether the model can effectively transfer its learned knowledge to classify entirely new object categories. Further investigation is needed to determine if the performance gains are limited to the fine-tuned categories or if the model truly unlocks a broader understanding of visual concepts that can extend to novel classes. The paper should include experiments on datasets with completely disjoint categories to assess this generalization capability.

*   **Dependence on Base LMM and Lack of Ablation Studies:** The proposed method relies heavily on the capabilities of the chosen base LMM (LLaVA-1.5). The paper doesn't provide ablation studies exploring the impact of different base LMMs or their pre-training data on the final performance. It is possible that the performance is still bounded by the limitations of LLaVA-1.5. To strengthen the paper's claims, investigations into the sensitivity of the method to different base LMMs, particularly those with different architectures or pre-training objectives, would be beneficial. This would help determine if the method's effectiveness is consistent across various LMM architectures.

*   **Label Generation and Testing Set Validity:** The paper doesn't fully explain how to create a valid testing set when the labels used for training are generated by the model itself. This raises concerns about potential biases and circularity in the evaluation process. Further clarification is needed on how to ensure the independence and representativeness of the testing set to provide a more reliable assessment of the model's true performance. Specifically, the paper needs to clarify whether the test set labels are also generated by the model or if they are from the original dataset, and if the latter, how the model avoids overfitting to the training set's generated explanations.

*   **Acquisition of Label-Level Concepts:** The process of obtaining the Label-level concepts (Z) is not explicitly outlined in the paper. While the paper mentions expert-defined concepts, it is unclear whether this implies manual annotation by human experts or if these concepts can be acquired automatically. If human expert annotation is still required, it would introduce a significant bottleneck in the scalability of the approach. Further details on the origin and acquisition of these concepts, including the specific prompts used to elicit these concepts from experts or LLMs, would be helpful. The paper should also discuss the potential for bias introduced by the choice of experts or LLMs.

*   **Potential Overfitting to Explanation Format:** The paper focuses on generating explanations in a specific format. It is possible that the model overfits to this format, limiting its ability to generalize to other explanation styles or answer formats. Exploring the model's performance with different explanation formats or encouraging the model to generate more diverse responses would strengthen the paper's conclusions regarding the general explainability of the fine-tuned model. The paper should include experiments that evaluate the model's performance when the explanation format is varied, such as by asking for explanations in different styles or with varying levels of detail.

*   **Limited Comparison with External Works:** The experimental evaluation in Table 1 primarily compares the proposed method against self-created baselines (NL and L+GE). While these baselines offer a useful reference point, including comparisons with other external works in explainable visual classification would provide a more comprehensive assessment of the method's strengths and limitations. Additionally, comparing the performance with methods that use manually annotated labels as an upper bound would be valuable for contextualizing the achieved results. The paper should include a more thorough comparison with existing state-of-the-art methods in explainable AI and visual classification, including methods that use different approaches to generating explanations.

### Questions
If the authors can well address the questions in the weakness section, I will consider increase the rating.

### Soundness
3

### Presentation
3

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
This paper proposes to improve LLMs’ capabilities in fine-grained image classification. In particular, it focuses on an iterative approach that derives synthetic explanations by identifying discriminative properties of the stimuli, and leveraging them for fine-tuning. The key properties are selected by measuring their cosine similarity with a pool of expert annotations, where the properties for each stimulus are determined by prompting a pretrained vision-language model. Experimental results on multiple datasets demonstrate the usefulness of the approach in enhancing the model performance and generating detailed explanations for the answers.

### Strengths
(1) Improving the interpretability of LLMs is an important problem, and the focus on challenging classification problems is a reasonable direction.

(2) The paper proposes a general framework for automatically constructing explanations for fine-grained classification, which shows promise in simultaneously enhancing the performance and interpretability of LLMs.

(3) The paper takes into account various automatic evaluation metrics and also conducts user studies for model validation, providing a comprehensive view of the effectiveness of the proposed method.

### Weaknesses
(1) It is not surprising that off-the-shelf LLMs can fail to provide reasonable explanations for fine-grained classification, as their aim for general applications does not align with the requirement for expert-level knowledge for specific tasks. My general concern for the paper is that, how much of the improvement comes from the shift of domain caused by fine-tuning, and whether or not such changes will harm the generalizability of LLMs. As shown in Table 1, despite the advantage of the proposed method,  a general model actually has equivalent performance among many metrics. 

(2) Related to the previous comment. I believe the comparison in Table 1 is missing some important baselines. In particular, the compared methods either are not trained on fine-grained classification (Base), or do not take into account explanations with reasonable quality (i.e., NL does not use any explanation and thus is expected to fail at interpretation, while L+GE only has access to explanations derived from the class labels alone). On the other hand, the proposed method has full access to both visual and language data, enabling it to perform a more thorough domain shift. For a fair comparison, it would be reasonable to include another baseline that is trained with explanations derived by prompting a vision-language model on each image. This experiment can also be used to validate the effectiveness of the proposed sampling method, i.e., how well its filtered properties outperform unfiltered ones. 

(3) Furthermore, I would encourage the authors to additionally consider evaluations on both the fine-grained and general classification (e.g., via zero-shot setting). This will enable us to explore additional research questions, e.g., whether fine-tuning on expert-level explanations leads to stronger general reasoning capabilities, or whether the challenge behind LLM explainability is rooted in the conflict between general and specific domains.

(4) The paper emphasizes an iterative approach for selecting key features for explanations. Nevertheless, other than reporting the model accuracy for each iteration, there is no analysis regarding how it affects the quality of explanations.

### Questions
(1) Please justify the effects of domain shift over improvement in reasoning capabilities and explanability. 

(2) After fine-tuning on the specific tasks, do the LLMs still perform well in general reasoning? 

(3) Does learning on one dataset benefit fine-grained classification in general? For instance, does training on CUB-200 lead to improvement in Stanford dogs?

(4) Please consider including additional baselines for comparison, as noted in the Weaknesses section.

(5) How does the iterative process benefit the derivation of discriminative concepts? A quantitative analysis would be reasonable.

### Soundness
2

### Presentation
3

### Contribution
3
