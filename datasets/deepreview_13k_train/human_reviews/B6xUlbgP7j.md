# BRAIN: Behavioral Responses and Artificial Intelligence Neural-Modeling for Consumer Decision-Making

- Decision: Reject
- Scores: 1, 1, 3, 3

## Abstract
This research investigates consumer neuroscience and neuromarketing through a multivariate methodology, employing Principal Component Analysis (PCA) and deep learning neural networks to interpret consumer responses to functional products. EEG signals were collected, recorded, and analyzed from 16 individuals aged 20 to 29 to identify significant neuronal markers related to consumer choices. The pivotal factors influencing decision-making were identified as the low beta and low gamma frequency bands, as well as participants' attention and meditation levels. The findings validate the effectiveness of our approach, demonstrating its applicability across various fields requiring accurate and reliable classification. Additionally, it is recommended to explore the potential applications of this study in the food industry by creating personalized nutrition strategies based on individuals' brain activity patterns.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
The reviewer encountered significant challenges in understanding the manuscript due to the unclear writing style exhibited by the authors, despite her/his expertise as a practitioner in EEG and BCI. Analyzing the EEG time-series presented in Figure 2, it appears that the authors lack a fundamental understanding of EEG amplitudes and the distinction between samples and seconds as units. Furthermore, the authors attempt to integrate EEG data with facial and food product images into a singular machine learning model, employing a simplistic application of PCA. This amalgamation raises substantial questions regarding the model's intended function, particularly in relation to the handling of potential movement artifacts. Additionally, there seems to be a conflation of EEG and BCI terminology within the methodology section, indicating a limited comprehension of the subject matter. Regrettably, these issues lead to a recommendation for outright rejection of the submission.

### Strengths
Regrettably, the submission does not meet the rigorous standards expected of an academic publication.

### Weaknesses
The writing style of the manuscript presents significant challenges to comprehension. Specifically, it lacks adequate detail regarding the reproducibility of the research, particularly in terms of the specifications for the machine learning models employed, including differentiating between image data and time-series data, among other factors. The analysis of EEG data, particularly in Figure 2, demonstrates a lack of understanding of basic EEG principles, such as the interpretation of amplitude values and the distinction between samples and seconds. The authors' attempt to combine EEG time-series data with facial and food product images using a simplistic PCA approach raises serious concerns about the validity and interpretability of the resulting model. The manuscript also exhibits a conflation of EEG and BCI terminology, further indicating a lack of expertise in the subject matter. The absence of a more rigorous machine learning approach beyond naive PCA is a significant limitation, and the lack of clarity in the methodology makes it difficult to assess the validity of the results.

### Questions
Why did the authors solely focus on naive PCA? What rationale underlies their decision to refrain from evaluating more advanced machine learning methodologies? Furthermore, why was the manuscript not subjected to proofreading and peer review by colleagues who might have identified its challenging comprehensibility for individuals not directly involved in the project?

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
The study shows that EEG analysis can effectively assess taste preferences. This allows researchers to determine whether participants like or dislike certain food samples based on their brain activity. Key indicators of preference included low beta and gamma frequency bands as well as attention and meditation levels. A deep convolutional neural network (CNN) was used, which utilized four types of input including image data and EEG signals to classify participants' preferences.

### Strengths
The paper presents a new and promising idea. However, the chosen approach is quite simple and does not introduce new methods or models that advance existing research. The study would benefit from a more innovative methodological contribution to set it apart from previous work in the field.

### Weaknesses
The introduction lacks a comprehensive summary and does not adequately convey the motivation for the study. Instead, it reads more like a general document on the use of EEG in consumer choice analysis without clarifying the specific approach or objectives of the present work. Furthermore, the introduction consists of a single paragraph with little conceptual linkage between the topics covered. A clearer structure and a more coherent explanation of the purpose and methodology of the research are needed to explain in the introduction.

The study only considers the sensory or taste aspects of the product as the primary factor influencing consumer preferences, which is insufficient to provide valuable insights for the food industry in the context of product development. A more comprehensive assessment that includes additional factors such as texture, aroma, visual appeal and emotional response would provide a more complete understanding of consumer preferences and increase the relevance of the study to the industry.

Sections 2.2 to 2.3.4 of the paper primarily resemble tutorials on EEG signals and their acquisition processes rather than focused discussions relevant to the study's research questions.

There is no related work provided on the existing studies on the given topic.

Overall, this manuscript lacks the scholarly depth and clarity expected of a research paper. The presentation of ideas is often unclear and insufficient attention is paid to structure, coherence and technical detail necessary to effectively communicate the research objectives, methodology and results.

### Questions
I recommend that the authors refer to the weaknesses outlined earlier in the review.

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
The authors investigate brain activity and behavioral responses in relation to consumer neuroscience through exploring consumer decisions regarding food by analyzing 16 participants using EEG signals to classify preferences for functional food products with respect to different brain rhythms and facial expressions through the application of PCA and Deep Convolutional Neural Network. The beta and gamma frequency bands are emphasized for purposes of decision-making and form a possible pathway in the realms of neuromarketing and customized nutrition planning for the enhancement of healthy diets.

### Strengths
Interesting Application: Using EEG data in this research for consumer preference assessment of functional foods falls within the currently developing interests in personalized nutrition and neuromarketing.

Combining PCA and a DCNN in EEG data management is a good choice because this study focused on the decision-making analysis on the beta and gamma bands.

Practical implications: These findings are valuable pieces of information that could be very useful for direct marketing and product development directed toward consumers in the food industry, especially regarding healthier products.

### Weaknesses
Small Sample Size and Generalizability: The small sample size of 16 limits the generalizability of the findings. Testing a larger and more diverse population will provide a more robust base for the findings.
I'd say this study lacks comparative analysis with previous models or even traditional machine learning techniques since the outperformance of this proposed approach over simpler or alternative models is not clear.

Lack of Reproduction Instructions: Important parameters like PCA as well as the DCNN architecture used have not been described. An entire hyperparameter table along with data augmentation strategies would be useful in further increasing reproduction and clarity.

Overemphasis on Beta and Gamma Bands: Though beta and gamma rhythms are relevant to decision-making, excessive concentration may neglect other EEG components that could be significant for consumer preferences.

### Questions
What are the hyperparameters of the DCNN model selected? Are there any data augmentation strategies used during training?

Why restrict single-band analysis to the beta and gamma frequency bands? Were other bands, such as alpha or theta, considered and found irrelevant?

How is this different from existing neuromarketing models that work on EEG? A comparison would explain the advantages and disadvantages of your proposed method.

Do you ever validate the model on larger or different datasets? Because the participant pool is so small, these may provide further evidences about the generalizability and performance of your model in other contexts.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents a clear logic and well-structured model framework that integrates Principal Component Analysis (PCA) with deep learning neural networks (DCNNs) to analyze consumer preferences through EEG signals. However, it lacks a comparative analysis with existing methods, making it challenging to assess the robustness of its contributions. The overall framework appears simple, and the innovative aspects of the research are not clearly defined, raising questions about its uniqueness. While the results demonstrate solid applications, the absence of sufficient validation diminishes their impact. Additionally, the tables presented are distorted screenshots, affecting clarity. Key questions arise regarding the model’s comparative effectiveness and the specific innovations that enhance its applicability in the field of consumer neuroscience and neuromarketing.

### Strengths
The logic of the paper is clear, with a well-structured presentation of the model framework that effectively integrates PCA with DCNN framework. The strong performance metrics in application underscore the model’s capability to predict consumer preferences.

### Weaknesses
 - The paper lacks a comparative analysis, making it difficult to assess how the proposed method measures up against existing approaches.

- It is challenging to determine the solidity of the contribution, as the overall framework—comprising EEG acquisition followed by a deep convolutional neural network (DCNN)—appears relatively simple, and the innovative aspects of the research are not clearly articulated.

- While the application results are promising, the paper does not provide sufficient validation to validate the results of these findings.

- Additionally, the tables included in the paper appear to be screenshots, resulting in distortion that affects their readability and clarity.

In the captions of Figures 7, 8, and 9, the authors refer to the “Efficiency of BRAIN Architecture including $\bar{\beta}$ and $\bar{\gamma}$ brain rhythms in training, validation, and test phases.” However, they provide no context or explanation on how the data was split into training, validation, and testing. Additionally, the figures themselves only present confusion matrices and a single ROC curve, with no clear indication of how validation and testing were performed or represented.

### Questions
- Comparative Methods: How does the proposed framework utilizing EEG signals and DCNN compare to other existing methods in neuromarketing and consumer neuroscience, particularly regarding accuracy and interpretability? Are there specific benchmarks or studies the authors can reference to validate the effectiveness of their approach?

- Innovative Aspects: What are the key innovative elements of the proposed model that distinguish it from similar frameworks in the field? How do these innovations contribute to the understanding of consumer behavior and enhance the applicability of the findings in real-world scenarios, especially in developing personalized nutrition strategies?

### Soundness
2

### Presentation
2

### Contribution
1
