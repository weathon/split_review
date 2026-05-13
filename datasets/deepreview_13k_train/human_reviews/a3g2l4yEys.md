# Pangea: A Fully Open Multilingual Multimodal LLM for 39 Languages

- Decision: Accept
- Scores: 6, 8, 5, 8

## Abstract
Despite recent advances in multimodal large language models (MLLMs), their development has predominantly focused on English- and western-centric datasets and tasks, leaving most of the world's languages and diverse cultural contexts underrepresented.  
This paper introduces \model, a multilingual multimodal LLM trained on \traindata, a diverse 6M instruction dataset spanning 39 languages. \traindata features: 1) high-quality English instructions, 2) carefully machine-translated instructions, and 3) culturally relevant multimodal tasks to ensure cross-cultural coverage. 
To rigorously assess models' capabilities, we introduce \evaldata, a holistic evaluation suite encompassing 14 datasets covering 47 languages. 
Results show that \model significantly outperforms existing open-source models in multilingual settings and diverse cultural contexts. Ablation studies further reveal the importance of English data proportions, language popularity, and the number of multimodal training samples on overall performance.  We fully open-source our data, code, and trained checkpoints, to facilitate the development of inclusive and robust multilingual MLLMs, promoting equity and accessibility across a broader linguistic and cultural spectrum.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper describes PANGEA model and data, with a focus on multilingual multimodal settings. 	PANGEAINS is an instruction dataset that spans 39 languages that covers the different languages through translation and the culture references aspects of the data. PANGEABENCH is an evaluation suite consists of 14 datasets covering 47 languages. PANGEA, a model based on the LLaVA-Next architecture and trained on the PANGEAINS data, showed strong performance on several tasks comparing to strong baseline models.

### Strengths
1. This paper addressed an important research problem on multilingual multimodal learning, by providing a large instruction dataset and evaluation suite that covers multiple languages with the corresponding culture reference annotations. This data could be of interest to a broad audience in the research community. 
2. The paper is well written and easy to follow. The proposed PANGEAINS instruction data and the PANGEABENCH evaluation suite were described with good amount of details. The authors further provided examples of the data which is helpful in understanding the dataset proposed.
3. The authors conducted comprehensive experiments of the proposed model and data, by comparing it to several strong baseline models and evaluating on a diverse set of tasks. The performance of the model seems to be pretty strong from the evaluation results.

### Weaknesses
1. It could be helpful to a section to discuss related multilingual multimodal datasets (e.g. M3IT etc), and show how PANGEA compares to them. This could further illustrate the significance of the proposed data here.
2. Although the authors highlighted the introduction of PANGEA, the discussion on the modeling aspect of PANGEA is light. It seems to be a directly application of a LLaVA-Next based model trained using the new data proposed. It could help to further discuss the training specifics.
3. The proposed method (model and data) is only evaluated on one eval set, which is the proposed PANGEABENCH. It could be helpful to evaluate on additional evaluation suits to see how the improvement from training on PANGEAINS would generalize.

### Questions
1. Would the other open source models used as the baseline in this paper could also benefit from training on the PANGEAINS data?
2. How to validate if there is potential overfitting of training on the PANGEAINS and evaluating on PANGEABENCH?

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
4

### Summary
This paper introduces Pangea, a multilingual multi-modal LLM together with its multi-modal instruction fine-tuning dataset PangeaIns and a comprehensive benchmark PangeaBench:
- PangeaIns includes 6M examples from 39 languages and consists of (1) high-quality English instructions, (2) machine-translated instructions, (3) culturally relevant multimodal tasks
- PangeaBench, a multimodal evaluation suite consists of 14 diverse datasets covering 47 languages, including a human-curated multimodal chat benchmark xChat 

Pangea outperforms other open-source models by 7.3 points on English tasks and 18.0 points in multilingual tasks. Finally, the paper discusses the impact of English data, the necessity of language-specific datasets, and the limitations in multimodal chat and multilingual OCR.

### Strengths
A. This paper includes a very significant set of contributions which will be made public together with the code:
1. PangeaIns with 6M instructions from 39 languages that include (1) high-quality English instructions, (2) machine-translated instructions, (3) culturally relevant multimodal tasks
2. PangeaBench, a multimodal evaluation suite consists of 14 diverse datasets covering 47 languages
3. Pangea an MLLM covering 39 languages outperforms existing open-source models by 7.3 points on English tasks and 18.0 points in multilingual tasks.

B. The paper presents a detailed multilingual multi-modal data generation pipeline showcasing the limitation of open-source machine translation models, and the use of LLMs to enrich the multilingual data where the LLM score and filter images based on cultural informativeness. Then remaining data is enriched with re-generating descriptions and creating complex instructions. 

C. PangeaBench covering 47 languages in 14 datasets introduces a comprehensive evaluation for multilingual multimodal LLMs. Notably, the new evaluation dataset xChat is a human-curated benchmark where reference answers and scoring rubrics are annotated for each query. This enables a better use of LLM-as-a-judge for scoring other models' generations using a scale of 1-5 for each query.

### Weaknesses
There are only two minor weaknesses mainly focusing on the need for clarity and the presentation:

A. In Section 2.1, the paper mentions a post-processing pipeline for noisy translations, however, details are missing. This might be quite important for practitioners to build similar models. Therefore, I suggest authors to include more details there.

B. In Section 4.1, it has been mentioned that the model is based on Llava-Next architecture but this needs to be detailed. For example, does the training include multiple stages such as adapter alignment and SFT, or is only SFT has been used? If so what datasets are used in which stage?

### Questions
A. For text-only performance, how is the chat performance compared to the other models? Some evaluation benchmarks such as MTBench, ArenaHardAuto or AlphacaEval can be used for this comparison. 

B. Have you checked if there is any data leakage from the benchmarks that has been tested?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
PANGEAINS is a multilingual and multicultural dataset comprising 6 million samples across 39 languages, developed for instruction tuning. This dataset emphasizes linguistic and cultural diversity and implements strategies such as machine translation, cultural understanding guidelines, and high-quality image caption generation to address challenges in multilingual multimodal learning. By using machine translation, English instructions are extended into other languages, and culturally biased issues are resolved by curating images from the LAION-Multi dataset to capture cultural contexts.

PANGEABENCH is a comprehensive evaluation tool designed to assess PANGEA's performance across various languages and tasks. It includes diverse benchmarks that evaluate capabilities in cross-lingual and cross-cultural contexts. The multimodal tasks encompass natural conversation, image captioning, cultural understanding, multilingual visual question answering, and multi-subject reasoning, while text-only tasks are also included to examine the model's linguistic understanding.

Experimental results show that PANGEA-7B outperforms existing models in both English and multilingual tasks, particularly demonstrating significant improvements in cultural understanding tasks. The performance gap between English and multilingual tasks is small, indicating strong multilingual processing capabilities, although there remains a performance disparity compared to closed-source models. Additionally, PANGEA-7B exhibits the strongest performance in text-only tasks, with notable enhancements in handling complex multilingual reasoning and mathematical tasks attributed to the inclusion of math-related instructions.

The discussion explores the scaling effect of instruction quantity, the role of English data, the relationship between training sample proportions and performance, real-world applications of multimodal chat, and preliminary explorations of multilingual OCR. These insights aim to provide a comprehensive understanding of the model and outline future advancement directions. The development of PANGEAINS and PANGEABENCH is expected to significantly contribute to enhancing the performance of multilingual and multimodal models.

### Strengths
Originality
The paper presents approaches to multilingual and multimodal learning through the development of the PANGEAINS dataset and the PANGEABENCH evaluation framework. By focusing on both linguistic and cultural diversity, it addresses gaps in existing datasets that often overlook these critical aspects. The integration of machine translation and culturally relevant guidelines for data curation showcases an innovative methodology that enhances the relevance and applicability of the dataset. This originality is further emphasized by the emphasis on cultural understanding in multimodal tasks, which is a relatively underexplored area in the field.

Quality
The quality of the research is evident in the rigorous methodology employed for dataset creation and model evaluation. The paper provides a thorough explanation of the processes involved in curating the PANGEAINS dataset, including the use of high-quality image captioning and the implementation of robust evaluation metrics. The empirical results presented are well-supported, demonstrating PANGEA's superior performance in various tasks. Additionally, the use of established benchmarks and the careful selection of evaluation metrics contribute to the overall robustness of the findings.

Clarity
The paper is well-structured and clearly organized, making it accessible to readers across different backgrounds. Each section is logically connected, and the authors effectively communicate complex ideas through concise language and well-defined terminology. The inclusion of visual aids, such as figures and tables, enhances understanding by illustrating key concepts and results. Overall, the clarity of presentation allows for easy comprehension of the methodologies and findings.

Significance
The significance of the paper lies in its potential impact on the field of multilingual and multimodal learning. By providing a comprehensive dataset and a structured evaluation framework, the authors contribute valuable resources that can facilitate further research and development in this area. The focus on cultural diversity and understanding not only enriches the training of models but also promotes more inclusive and applicable AI systems. The findings underscore the importance of addressing cultural nuances in AI applications, which is essential for creating systems that are effective and relevant in a global context.

### Weaknesses
Limitations of the Dataset
The PANGEAINS dataset comprises samples from 39 languages; however, there exists a potential imbalance in both the quantity and quality of data for specific languages. This issue is particularly pronounced for low-resource languages that the authors do not explicitly address. The scarcity of data for these languages can lead to significant challenges in training models that are capable of performing effectively across diverse linguistic contexts. Insufficient representation may result in suboptimal performance, as the models may lack the necessary exposure to the varied linguistic structures and cultural nuances inherent in these languages.

Moreover, the quality of the data is as crucial as its quantity. If the available data for certain languages is of lower quality—whether due to inaccuracies in translation, lack of contextual relevance, or inadequate cultural representation—this can further exacerbate performance issues. Such disparities in data quality can hinder the model's ability to generalize effectively across languages, potentially leading to biased outputs and diminished reliability in multilingual applications.

Consequently, these imbalances may impede the overall generalization capabilities of multilingual processing, as the model’s performance may be skewed towards languages with richer datasets. Thus, it is imperative for future iterations of the dataset to ensure a more equitable distribution of data quality and quantity across all included languages, particularly for those that are underrepresented, in order to enhance the robustness and applicability of multilingual models.

-Depth of Cultural Context
In evaluating cultural understanding, the discussion regarding whether the PANGEAINS dataset adequately reflects diverse cultural backgrounds is somewhat lacking. Cultural differences are complex and nuanced, extending beyond mere linguistic expressions or visual representations to encompass social contexts, customs, values, and other interrelated elements. These factors shape the meanings within specific cultural contexts and are essential for multilingual multimodal models to accurately understand and process cultural nuances. However, the current dataset primarily focuses on the matching of images and captions, which may not sufficiently capture the depth of cultural context.

For instance, metaphorical expressions or symbolic meanings in one culture may be interpreted entirely differently in another. Capturing these subtle distinctions necessitates a more in-depth analysis that transcends simple dataset curation. It would be beneficial to incorporate expert consultations on cultural backgrounds and conduct comprehensive research on each culture to inform data collection efforts. Such an approach would enhance the model's ability to understand meanings across various cultural contexts and generate more nuanced responses.

- Limitations of Experimental Design
From the perspective of experimental design, there is a notable lack of in-depth analysis concerning specific tasks or languages. For example, in tasks such as multilingual visual question answering (VQA) or multi-subject reasoning, a detailed exploration of the factors influencing model performance is missing. Without such analysis, it becomes challenging to clearly understand the model's strengths and weaknesses, ultimately limiting the ability to establish future improvement directions.

Particularly, without a thorough examination of various determinants of performance—such as the characteristics of specific languages, dataset imbalances, or hyperparameter adjustments during training—understanding why a model excels or falters in certain tasks becomes difficult. Therefore, it is crucial that the experimental design explicitly defines the specific conditions and variables for each task, along with comparative analyses of performance across different environments. This approach would not only enhance model performance but also deepen the overall understanding of multilingual and multimodal systems.

### Questions
Data Representation: What strategies can be implemented to ensure a more balanced representation of low-resource languages within the PANGEAINS dataset?

Quality Assessment: How can we establish rigorous quality assessment protocols to evaluate the accuracy and relevance of data for each language in the dataset?

Cultural Context: What methodologies can be employed to enrich the dataset with culturally relevant examples and ensure that cultural nuances are adequately captured across all languages?

Data Augmentation: What role can data augmentation techniques play in enhancing the dataset, particularly for underrepresented languages, to improve model performance?


As a reviewer, I would like to provide detailed technical advice regarding the concerns particularly focusing on the potential imbalances in data quantity and quality across different languages, especially for low-resource languages. Perhaps I (not a robot) missed the methods described in your manuscript. Please let me know and provide additional information if possible.

1. Addressing Imbalances in Quantity and Quality
- Data Augmentation Techniques:

Synonym Replacement: Identify and replace words with their synonyms to generate paraphrased sentences that maintain the original meaning.
Back Translation: Translate sentences into another language and then back to the original language to create varied sentence structures while preserving semantic content.
Noise Injection: Introduce small amounts of noise (e.g., typos, grammatical variations) to simulate real-world language use and increase dataset diversity.

- Collaboration with Native Speakers:

Engage with native speakers or linguists proficient in low-resource languages to enhance the quality of your dataset. This could involve Crowdsourcing Platforms with native speakers for data validation and enrichment.

- Detailed Data Distribution Analysis:

Provide a comprehensive analysis of the data distribution across the 39 languages included in the dataset. This should include:
Quality Metrics: If applicable, include metrics that assess the quality of the data per language (e.g., linguistic diversity, error rates).

Visual Representations: Use graphs or charts to visually represent the distribution and highlight any significant imbalances.

2. Enhancing Quality of Cultural Representation

When collecting data, consider the cultural context of each language. This can be achieved by:
Ethnographic Research: Integrate ethnographic methods to understand cultural nuances that might not be reflected in traditional data collection.

Focus Groups: Conduct focus groups with speakers of the languages to gather insights on cultural expressions and values that should be represented in the dataset.

Examples of Cultural Representation: Provide specific examples of how the dataset captures cultural differences. Detail how various cultural elements (e.g., idioms, customs, social norms) are represented in the data. Case studies that illustrate the inclusion of culturally relevant examples. An analysis of how the dataset addresses or fails to address complex cultural concepts.



3. insufficient in-depth analysis related to specific tasks and languages, particularly in areas such as multilingual visual question answering (VQA) and multi-subject reasoning. 

Below are some actionable suggestions to enhance your analysis:

- Conducting Ablation Studies
Ablation Studies on Language Groups: Perform ablation studies to assess how different language groups affect model performance. This involves systematically removing specific languages or language features from the dataset to observe changes in performance metrics. Analyze which languages contribute the most to overall model effectiveness and identify any languages that may cause degradation in performance.

Ablation Studies on Task Types: Similarly, conduct ablation studies focusing on different task types (e.g., VQA versus multi-subject reasoning). By isolating the performance impacts of each task type, you can gain insights into which tasks are more challenging for your model and why.

Expert Collaboration: How can collaboration with linguistic and cultural experts be structured to inform the data collection process, ensuring a more comprehensive understanding of low-resource languages?

Evaluation Metrics: What specific evaluation metrics can be developed to assess the model's performance across different languages, particularly focusing on those with limited data?

Feedback Mechanisms: How can feedback mechanisms be incorporated into the dataset's development process to continuously improve data quality and representation based on model performance?

Cross-Linguistic Comparisons: What methods can be utilized to conduct cross-linguistic comparisons that identify specific challenges faced by the model when processing low-resource languages?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces PANGEA, a multilingual multimodal large language model (MLLM) addressing the limitations of English-centric data in existing models. The model was trained on a dataset called PANGEAINS, which includes 6 million instruction samples across 39 languages. PANGEINS combines high-quality English instructions, machine-translated content, and culturally relevant tasks. The authors also developed PANGEABENCH, an evaluation suite to assess the model’s multilingual and multimodal capabilities, including tasks like chat, image captioning, and visual question answering. PANGEA outperforms existing open-source models, especially in tasks requiring cross-cultural understanding, though it still lags behind proprietary models like GPT-4 in areas like complex reasoning. Fully open-sourced along with its dataset and evaluation suite, PANGEA aims to promote further research in inclusive multilingual LLMs, addressing challenges like data scarcity, cross-lingual transfer, and multilingual OCR.

### Strengths
1. This paper is well-written, offering comprehensive details on the curated instruction-tuning datasets, benchmarks, and evaluation results. The authors present their work with clarity and thoroughness.
2. The meticulously curated datasets for both training and evaluation are of significant practical value. They will undoubtedly make a substantial contribution to the multilingual research community, providing a robust foundation for future studies in this field.

### Weaknesses
1. The paper lacks some crucial details about the model and training process. Specifically, it would be beneficial to provide more information about the architecture, including the type of vision encoder used and the final total number of parameters. Additionally, details regarding the training infrastructure and duration are absent. 
2. Some evaluation setup details are missing, such as the number of shots for each dataset, which makes the results difficult to reproduce. For instance, the results for Qwen2-7B-instruct are significantly worse than those reported in the official release (https://qwenlm.github.io/blog/qwen2/#multilingual-capability-of-instruction-tuned-models). What is the reason?
3. Although the authors claim the model supports 39 languages, it's unclear which specific languages have shown improvement and to what extent compared to the backbone model. This is particularly uncertain for languages that comprise only a small portion of the PANGEAINS dataset.

### Questions
In Figure 7, the model's poor performance on English OCR is counterintuitive. What might explain this unexpected result?

### Soundness
4

### Presentation
3

### Contribution
4
