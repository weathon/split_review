# MULTIMODAL GENERATIVE AI FOR STORY POINT ESTIMATION

- Decision: Reject
- Scores: 3, 5, 3, 3

## Abstract
This research explores the application of Multimodal Generative AI to enhance story point estimation in Agile software development. By integrating text, image, and categorical data using advanced models like BERT, CNN, and XGBoost, our approach surpasses the limitations of traditional single-modal estimation methods. The results demonstrate good accuracy for simpler story points, while also highlighting challenges in more complex categories due to data imbalance. This study further explores the impact of categorical data, particularly severity, on the estimation process, emphasizing its influence on model performance. Our findings emphasize the transformative potential of multimodal data integration in refining AI-driven project management, paving the way for more precise, adaptable, and domain-specific AI capabilities. Additionally, this work outlines future directions for addressing data variability and enhancing the robustness of AI in Agile methodologies.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper presents approach to estimating story points in Agile development using generative AI.  The authors extracted/curated data from Bugzilla and developed a modeling approach that involved extracting BERT text embeddings, CNN image features and other categorical features.  They use XGBoost to learn to estimate story points.

### Strengths
Machine learning can be very beneficial in software development as has been seen with code generation tools.  This paper presents a relevant task and approaches it in a multimodal fashion, both of which I’d like to highlight as positives.  The paper was interesting, but hard to read and has a number of major flaws that mean I have to evaluate it as not being ready for publication.

### Weaknesses
I would suggest the authors thoroughly revise the content and prepare it for another venue.  There would be a significant amount of work necessary to get this paper to an ICLR publication standard, but the basis for a potentially interesting piece of research is there.

The most significant issue with the work is the lack of detail and precision in the writing which mean it would be impossible to replication to event approximate the solution.  There are many areas where this needs to be improved and too many to list individually here.  The dataset used seems very small and is quite difficult for a user to actually picture.  The authors only curate 113 examples, yet they present Bugzilla as a VAST source of user stories - so why only use a very small number of stories?  Why not show clearer examples of the data?  Table 1 has screenshots which are impossible to read.  I don’t see the point of showing those thumbnails - if they are so small for privacy reasons then they could be excluded altogether.  If not, then make them larger.

The second issue is there presentation of the work, there are several areas of the manuscript, such as Table 2, that offer very little to the reader.  Is one supposed to interpret the numbers in the first two columns?  What is the point of showing this type of data?

There are plots that are almost unreadable (e.g., Fig.3 - font is too small) and tables that have basic formatting issues that are at best distracting and raise questions about the attention of detail paid to other aspects of the work.  I like confusion matrices but Fig. 1 takes up half a page and contains 9 numbers.  This could be condensed to a single sentence and contain as much information.  

Tables such as Table 5 take up almost half a page and contain very little addition insight for the reader. If necessary these could be put in the supplement and the space used to add much more detail about the methods.

The methods the authors choose has very little technical novelty (BERT, CNN, XGboost).  The tools are not even state of the art. I imagine some of these choices were a result of the small dataset but even with these tools I find it almost impossible to see how they could create a convincing argument for generalization based on the amount of stories they actually have.

### Questions
Why use such a small dataset?

Why present the results in the way they are shown in the paper?  There would seem to be much more efficient ways of showing the results.

Why the choice of tools (CNN, Bert, XGBoost) that were used? Specifically, what other methods were tried.

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In summary, the manuscript introduces a compelling approach to story point estimation using multimodal AI. Addressing some points regarding answering some key questions and presntations would strengthen the work by enhancing clarity, rigor, and practical applicability.

### Strengths
The manuscript presents an application of multimodal AI for story point (SP) estimation, combining text, image, and categorical data. This integration addresses limitations of traditional methods that often rely on single-modal data as the author claimed. The methodology includes advanced models (BERT, CNN, and XGBoost) that are well-suited to their respective data types, enabling a holistic approach to SP estimation (as per author claimed). Study also provides quantitative insights, showing improvement in simpler SP categories & highlighting the effects of removing severity data on performance. The paper also suggests specific improvements, like incorporating models such as ViLBERT and CLIP, to address limitations in the current approach, as well as techniques to balance the dataset and refine image processing.

### Weaknesses
Terms like "good accuracy" lack precision; including concrete metrics would improve clarity and impact. The introduction does not fully explain why image data is essential for SP estimation in Agile, especially for readers unfamiliar with how visual elements relate to user stories. The unexpected finding that excluding severity data improves model performance warrants a deeper analysis, potentially with additional literature to support or clarify the impact. While BERT and CNN are used for text and image embeddings, the paper could benefit from justifying these choices over other state-of-the-art options, especially as BERT is no longer the most advanced model for text. The study acknowledges data imbalance but does not explore or implement balancing techniques like SMOTE, which could improve model performance in complex SP categories. The reliance on Bugzilla data may narrow the applicability of the model across other Agile frameworks, given that the data could be biased toward specific story types and domain-specific language. Although severity data is included as a categorical feature, the rationale for why it might critically impact SP estimation is not fully developed, leaving room for further exploration of feature significance.

### Questions
1. Abstract:
In abstract authors concisely outlines the aim of the study to enhance SP estimation through multimodal AI.

Some points they may add:
* Stating the dataset source -Bugzilla to enhance clarity.
* Terms like "good accuracy" seem vague. Quantitative results/specific metrics would strengthen the abstract.
* Mention of challenges due to data imbalance is relevant but could briefly explain how it impacts the model.

2. Introduction

* Intro references planning poker & traditional methods but don’t clearly explain the need for an automated solution to readers unfamiliar with Agile.
* It’s not clear why image data, specifically, is vital to SP estimation (for me at least). An explanation of how visual data relates to Agile requirements probably would enhance understanding.
* A deeper look into gen AI’s distinct benefits (e.g., context-awareness, adaptability) for Agile workflows would/might solidify the argument.
 3. Related Work

* While this section highlights the limitations of single-modal data, it doesn’t provide examples OR metrics from prior studies for contrast. (optional todo)
* While a gap in Agile applications of multimodal AI is noted, discussing how multimodal models have succeeded in similar domains (e.g., sentiment analysis) would add depth. (optional todo) 
4. Approach and Methodology

* Rationale for selecting Bugzilla could be elaborated. 
* Does Bugzilla provide comprehensive and unbiased data for SP estimation?
    * The choice of Fibonacci sequencing for story points seems novel. 
    * However, further justification for this selection would help—why not use a regression model instead of Fibonacci classes?
    * It’s unclear why specific embeddings were chosen for text and images (e.g., BERT and CNN as BERT is not a SOTA anymore !). Adding an explanation of alternative options considered and their pros and cons would enrich this section.
* Short comparative analysis on why XGBoost performs better than other ensemble models could justify this choice.
* This section lacks a clear explanation of its impact. How was severity expected to influence story point estimation, and why was it hypothesized to be a critical feature? 
5. Results and Discussion

* The manuscript could use more detailed metrics (e.g., confusion matrices for all categories, especially complex SPs). 
* It’s crucial to see how each story point level performed, including precise PR (recision-recall) data.
* Model showed improvement w/o severity data, raising questions about the feature’s importance. Was this result surprising, or did it align with initial expectations? A short discussion on the reasoning behind severity’s impact, potentially with related literature support, would strengthen the analysis.
* Misclassification trends are insightful but would benefit from a breakdown of the challenges in each category.
* Mentioning possible approaches (e.g., SMOTE for synthetic sampling) to address the data imbalance would offer actionable insight for future readers. 
6. Limitations and Challenges

* Limitations inherent to Bugzilla, such as domain-specific language or bias toward particular story types, might restrict generalizability. A discussion on this could be helpful.
* The quality and relevance of images were acknowledged as variable, which introduces noise. Elaborating on specific image characteristics that were particularly challenging could clarify this point.
* The process of integrating text, image, and categorical data has inherent challenges. Were there issues in aligning these modalities, and how were they addressed? 
7. Future Work

* Mentioning multimodal models like ViLBERT and CLIP was insightful, but discussing why these models might perform better for this task (e.g., handling of domain-specific data) would be beneficial.
* Using synthetic data to balance categories would be a valuable experiment. An elaboration on which techniques might best suit this data would provide actionable direction.
* While the idea of fine-tuning BERT on a domain-specific corpus was mentioned, further detail on where to source or create this corpus would provide clear next steps. 
8. Conclusion
* Manuscript could include how the proposed model might directly benefit Agile teams in practice.
* Ending with a statement on the transformative potential of multimodal AI in project management would provide a strong conclusion.
 Writing and Presentation

* Terms such as "severity data," "multimodal integration," and "story points" may not be universally understood by all readers, particularly those outside Agile contexts. Including brief definitions or explanations would improve readability.
* Figures could use more detailed captions, especially the confusion matrices, to guide readers through the results more effectively.
 Additional Observations
* Bugzilla data may be limited to certain Agile frameworks or specific team practices. If so, this could limit applicability across broader Agile methodologies.
* There is no mention of whether performance differences were statistically significant, which could validate or refute the observed improvement without severity data.
 In summary, the manuscript introduces a compelling approach to story point estimation using multimodal AI. Addressing these points would strengthen the work by enhancing clarity, rigor, and practical applicability.

### Soundness
2

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
The paper introduces a framework for enhancing story point estimation in Agile software development using multimodal generative AI. By integrating textual data through BERT embeddings, image data via CNN features, and categorical data such as severity levels using ordinal encoding, the authors aim to improve estimation accuracy. They utilize data from Bugzilla, an open-source bug tracking system, comprising user stories, images, and historical comments. The proposed model employs XGBoost for classification, predicting story points based on the Fibonacci sequence commonly used in Agile methodologies. Experiments compare models trained with and without severity data, revealing that excluding severity data leads to better overall accuracy. The paper acknowledges limitations like the small and imbalanced dataset and suggests future work to address these challenges.

### Strengths
- The paper tackles the practical problem of story point estimation in Agile software development, which has direct implications for project management and efficiency.
- By incorporating text, images, and categorical data, the approach recognizes the multifaceted nature of user stories and attempts to model them more comprehensively.
- Leveraging BERT for text embeddings and CNNs for image features is appropriate and aligns with current best practices in handling such data types.

### Weaknesses
 - The methodology relies on standard machine learning models and does not introduce any novel techniques or approaches. The use of pre-trained BERT and CNN models for feature extraction without fine-tuning or customization for the problem at hand limits the contribution. Specifically, the paper does not explore techniques such as domain adaptation or contrastive learning, which could potentially improve the model's performance on this specific task. Furthermore, the choice of XGBoost as a classifier, while effective, is not justified against other potentially more suitable models for multimodal data.
- With only 113 observations, the dataset is too small for training a robust machine learning model, especially one intended for practical application. The severe imbalance in story point categories further hampers the model's ability to generalize. The paper does not detail the class distribution, making it difficult to assess the severity of the imbalance and its potential impact on model performance. The lack of a clear strategy for handling this imbalance, such as oversampling or undersampling techniques, is a significant oversight.
- The paper does not employ robust validation techniques suitable for small datasets, such as cross-validation or bootstrapping, which raises concerns about the reliability of the reported results. Furthermore, lack of simple baselines such as human-expert estimation, or multi-modal LLMs such as GPT-4o or LLaVA, making it difficult to assess its effectiveness. The absence of a clear evaluation protocol, including metrics beyond overall accuracy, such as precision, recall, and F1-score for each story point category, further limits the interpretability of the results.
- Grammatical errors, awkward phrasing, and inconsistent use of figures and tables detract from the clarity and professionalism of the paper.

### Questions
- Given the small dataset, did the authors perform any statistical significance tests to ensure that the observed improvements are not due to random chance?
- How did the authors assess the quality and relevance of the image data? Were any measures taken to exclude irrelevant or low-quality images that could introduce noise?

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
In this paper, the authors explored Multimodal Generative AI to improve story point estimation in Agile software development. They proposed a novel framework that combines multiple types of data, including text data and images like UI/UX mockups and screenshots, and categorical data. By collecting data from Bugzilla's open-source bug tracking system, they proposed a model with XGBoost for story point classification. They further evaluate the performance with and without severity data as part of the inputs. The experiments show promising results for leveraging multimodal approaches in Agile software development.

### Strengths
- The paper proposed a novel approach for combining diverse data modalities in Agil story point estimation. The multimodal approach improves the understanding of user stories compared with existing estimation techniques that typically only rely on single modality. 
- The discussion on the impact of severity for model performance is insightful. Through the empirical analysis, the fact that removing severity data improved performance challenges the intuitive assumption that more features lead to better performance.

### Weaknesses
 - The paper could benefit significantly from clearer writing and better organization. The readability could be improved significantly by presenting the experimental results more clearly, and by addressing several grammatical issues throughout the text. The motivation could be more thoroughly explained to improve the overall justification. The writing gives the impression of being kinda rushed for the submission deadline. 
- The paper lacks several important technical details, such as the specific model of CNN used for image processing, and the BERT model used for text processing. There is no information on the hyperparameter settings for each model, the training process, or any preprocessing steps applied to the data before feeding it into the models. These missing details make it difficult to fully evaluate the replicability of the experiments. Additionally, much of the experimental results are under-explained for example in Tab. 2, the first and second columns listed feature information which is very hard to understand their purpose. It is also unclear why nearly a page in Appendix Sec. A is dedicated to basic explanations of BERT, CNN, and XGBoost, which seems somewhat redundant for an ICLR audience familiar with these concepts.

### Questions
- How scalable is this approach for larger datasets with higher complexity, and what adjustments would be required to achieve good performance?
- What measures were taken to mitigate potential biases introduced by the imbalance in story point categories, especially given the limited data for complex story points?

### Soundness
2

### Presentation
1

### Contribution
2
