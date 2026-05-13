# Say My Name: a Model's Bias Discovery Framework

- Decision: Reject
- Scores: 6, 5, 5, 5

## Abstract
In the last few years, due to the broad applicability of deep learning to downstream tasks and end-to-end training capabilities, increasingly more concerns about potential biases to specific, non-representative patterns have been raised. 
Many works focusing on unsupervised debiasing usually leverage the tendency of deep models to learn ``easier'' samples, for example by clustering the latent space to obtain bias pseudo-labels. However, the interpretation of such pseudo-labels is not trivial, especially for a non-expert end user, as it does not provide semantic information about the bias features.
To address this issue, we introduce ``Say My Name'' (SaMyNa), the first tool to identify biases within deep models semantically. Unlike existing methods, our approach focuses on biases learned by the model. Our text-based pipeline enhances explainability and supports debiasing efforts: applicable during either training or post-hoc validation, our method can disentangle task-related information and proposes itself as a tool to analyze biases. Evaluation on traditional benchmarks demonstrates its effectiveness in detecting biases and even disclaiming them, showcasing its broad applicability for model diagnosis.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors introduce a framework for detecting and captioning semantic biases of deep learning vision models. The authors propose a tool that identifies biases learned by models and assigns human-interpretable semantic labels to these biases for explainability and debiasing.
The method operates by sample subset selection, sample captioning via MLLM, keywords selections via text encoder, extracting learned class embedding, and keyword ranking.
The authors test the framework on popular benchmark datasets. The proposed method successfully identified biases. Also, this discovery can be used with bias mitigation methods, effectively debiasing models.

### Strengths
- The paper tackles an important problem in machine learning which is bias and spurious correlations, and propose an effective tool to analyse these biases from the endpoint of humans.

### Weaknesses
 - Experimental analysis on bias discovery is lackluster. I think correlation analyses between the proposed method and human annotations are needed.

- The efficacy of the method could depend heavily on the model type and alignment of the MLLM or text encoder. I believe there should be an experimental analysis to show the robustness of the method on this matter.

### Questions
- The proposed method does not use a validation set. How are the hyperparameters of its various components tuned?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper outlines a five-step process for identifying spurious bias of a model in natural language keywords. The steps are as follows: (1) sample selection, (2) captioning, (3) keyword selection, (4) classification embedding, and (5) keyword ranking. The experimental results showcase several sample outputs from this process. Furthermore, the evaluation highlights the utility of the identified keywords as pseudo-labels for groups, which can be leveraged by debiasing methods.

### Strengths
This paper addresses the critical issue of model bias discovery through an interesting approach that utilizes natural language keyword descriptions.

### Weaknesses
The proposed method lacks novelty since it shares many components with existing literature. For example, the iteration selection based on misclassification confidence outlined in Section 3.1 is a variant of the approach described by Nahon et al. (2023) [1], while the keyword extraction from natural language captions is similar to that found in Kim et al. (2024) [2]. Although these references are cited, the paper does not clearly delineate which aspects are novel, making it challenging to assess its originality. Specifically, the method's reliance on misclassification confidence for iterative selection, while effective, closely mirrors the core idea in [1], raising questions about the incremental contribution. Similarly, the use of natural language captions for keyword extraction, while a useful technique, is not a novel contribution in itself, given its prior use in [2]. The paper needs to more clearly articulate what specific innovations it introduces beyond these existing methods.

The authors claim contributions related to a text-based pipeline and the disentanglement of domain relevance and the usefulness of the extracted keywords in debiasing. However, only the latter contribution is substantiated by experimental results. The validity and utility of the first two claimed contributions remain unclear. The text-based pipeline, while presented as a novel aspect, lacks a clear demonstration of its unique advantages over existing approaches. The disentanglement of domain relevance also lacks concrete evidence, making it difficult to assess the practical impact of this claim. The paper would benefit from more rigorous experiments and analysis to support these claims.

Furthermore, there is room for improvement in the presentation of the paper. Here are some suggestions:
1. **Clarify Equations**: The presentation of the equations can be enhanced. For instance, in Equation 2, the denominator just represents the number of misclassifications, but uses complemented Dirac delta unnecessarily. Equation 3 calculates the average of the mean embeddings for both correctly classified and misclassified instances, but is presented as complicated double sum.
2. **Refine Citations**: A more judicious selection of parenthetical and in-text citations would enhance clarity and reduce unnecessary repetition throughout the text.

### Questions
1. Which portion is the most important contribution in the proposed pipeline?
2. Why is the model with the most confident misclassification useful in bias discovery? If the final model and the selected model are different by a lot, how would this selected model be useful in the final model bias discovery or mitigation?
3. The keywords are derived from the samples classified as the target class by the studied model. Although these keywords are correlated to the model classification, wouldn't this be not enough to indicate causation?
4. Is there any compounded bias effect since many off-the-shelf models participate in the pipeline? For example, captioning model may focus on specific aspect of image or text embedding model may be sensitive to specific keywords.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper tackles the identification of hidden dataset bias within training data, which prevents model from learning intrinsic features that generalizable across distributions. With existing text-based models, it extracts and ranks the bias-related keywords out of data, and leveraging this as the pseudo bias-labels for supervised learning to debias the model. It shows effectiveness in various dataset bias benchmarks in both synthetic and real-world setups.

### Strengths
This paper is well-written and addresses the critical research question of identifying unknown dataset bias (spurious correlation) within training. This would essentially enhance the explainability and reliability of models in real-world applications especially for safety critical purposes.

### Weaknesses
 **1. Lack of novelty and effectiveness**: Several key ideas of this paper already exist in previous paper [1]. These include 1) sampling keywords using pretrained captioning model, and 2) identifying bias key words. Despite of subtle technical difference, e.g., detecting bias keywords via contrasting true and false positives (this work) or true positive and false negative (Kim et al. [1]), but in overall this paper does not provide any scientific novelty for the same goal beyond the existing papers. Such resemblance in technical details is reflected in highly limited improvements in debiasing compared to Kim et al., as proposed in Table 1. Therefore, it would be helpful to further elaborate the novel contribution of this paper against existing baselines.

**2. Potential risk in identifying biased models**: Section 3.1 proposes to identify the biased models by looking at how confidently misclassify the training data. However, models might result in being overfitted to relatively small number of bias-conflicting data in training data, resulting in potential bias to be NOT detected in iteration $t^*$. Therefore, it is deemed required to further validate the effectiveness of utilizing train data for detecting bias against oracle, i.e., using held-out validation data.

### Questions
See weaknesses.

### Soundness
3

### Presentation
4

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors introduce the "Say My Name" pipeline, a method designed to identify and interpret biases learned by image classification models. The pipeline consists of five main steps:

1. Selection of Representative Subset: Selecting a subset of images that are representative of the biases learned by the model.
2. Captioning with Vision-Language Model: Using a vision-language model (VLM) to generate captions for the selected images.
3. Keyword Extraction: Selecting keywords that are common across captions within the same class.
4. Embedding Computation: Computing embeddings of the text descriptions for each class.
5. Keyword Ranking: Comparing the results from steps 3 and 4 to rank the top keywords associated with each class.

The authors apply their method to several datasets, including Waterbirds, CelebA, BAR, and ImageNet-A. They demonstrate that their approach can effectively identify meaningful textual descriptions of biases present in the models.

### Strengths
1. **Clarity and Readability:** The paper is well-written and easy to understand. The motivation behind the work is clearly explained.
2. **Methodological Breakdown:** In Section 3.2, the authors provide a detailed breakdown of the five-step pipeline, with clear links to each subsection. This organization enhances the readability and comprehension of the methodology.
3. **Practical Utility:** Interpreting biases in machine learning models is crucial. The proposed method appears straightforward to implement and could be readily applied to various image classification tasks.

### Weaknesses
1. **Lack of Novelty in Bias Identification:** The method for bias identification seems to be a straightforward application of existing techniques for extracting textual descriptors from images. Previous work has already explored the connection between classification errors and biases. The proposed pipeline essentially relies on using a vision-language model to caption images and then summarizing or ranking features. It's unclear how the authors' approach offers a significant technical contribution beyond existing methods or how it compares to simpler approaches, such as directly using a VLM followed by summarization with a large language model (LLM). Specifically, the novelty of the sample selection process is not clearly established. The paper does not provide a rigorous comparison against baseline methods that use a VLM and LLM directly, thus failing to demonstrate the necessity of the proposed multi-step pipeline. The keyword extraction method, while described, lacks a clear justification for its superiority over simpler alternatives, such as frequency-based keyword extraction from the VLM-generated captions.
2. **Interpretability and Quantification of Results:** The extracted rankings of keywords are difficult to quantify and interpret. For example, in Figure 4, the top features for different classes in the BAR dataset have scores ranging from 0.4 to 0.55, associating "climbing" with terms like "cliff," "rock," "rocks," and "steep." However, it's unclear whether these terms represent biases or causal features. There is a lack of empirical analysis to validate whether humans agree that these are indeed biases and how these scores should be interpreted or used in practice. The paper does not provide a clear methodology for distinguishing between spurious correlations and genuine causal features, and the interpretation of the scores remains subjective. The lack of a quantitative evaluation of the extracted biases makes it difficult to assess the effectiveness of the proposed method.
3. **Focus and Relevance of Bias Mitigation Study:** The inclusion of bias mitigation using the identified descriptors seems somewhat tangential to the main focus of the paper. Previous work has shown that, for datasets like CelebA and Waterbirds, extracting spurious attributes can improve performance. As such, the contribution in this area appears limited and may distract from the primary contributions of the paper. The bias mitigation section does not introduce any novel techniques and relies on standard GroupDRO, which further diminishes its contribution. The paper would be stronger if it focused on the bias identification method and provided a more thorough analysis of its results.

### Questions
Please see the weaknesses section for the main questions.

One missing reference (https://arxiv.org/abs/2204.13749), where the authors learned the unbiased-biased split directly from training.

### Soundness
2

### Presentation
3

### Contribution
2
