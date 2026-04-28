# LATABLE: TOWARDS LARGE TABULAR MODELS

- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 5, 3, 3

## Abstract
Tabular data is one of the most ubiquitous modalities, yet the literature on tabular generative foundation models is lagging far behind its text and vision counterparts. Creating such a model is hard, due to the heterogeneous feature spaces of different tabular datasets, tabular metadata (e.g. dataset description and feature headers), and tables lacking prior knowledge (e.g. feature order). In this work we propose LaTable: a novel tabular diffusion model that addresses these challenges and can be trained across different datasets. Through extensive experiments we find that LaTable outperforms baselines on in-distribution generation, and that finetuning LaTable can generate out-of-distribution datasets better with fewer samples. On the other hand, we explore the poor zero-shot performance of LaTable, and what it may teach us about building generative tabular foundation models with better zero- and few-shot generation capabilities.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper introduces LaTable, a diffusion-based generative model for table generation. LaTable is designed to support flexible generation with varying numbers and types of features, utilizes additional context like dataset descriptions and feature information, and demonstrates equivariance with respect to column order. The authors conducted experiments showing that model performance scales with both model and table sizes, and that LaTable outperforms several baselines. Results also indicate that training across multiple datasets, incorporating textual context, and exposing the model to more data samples (e.g., table rows) or increasing the model size enhance its performance.

### Strengths
- The authors provide a clear motivation for the need for tabular generative models and present a model designed to meet the specific requirements of tabular data generation. The related works section is well-written, highlighting why LLM-based approaches are not optimal compared to their diffusion-based approach.
- The authors conducted comprehensive experiments, examining critical factors beyond general model performance, such as scalability, cross-dataset training procedures, and the impact of including textual context.

### Weaknesses
 - The evaluation setup is unclear. The authors mention Cardio, URL, WiDS, Insurance, and Heloc as test datasets, citing Stoian et al. However, only URL, WiDS, and Heloc are covered in that paper; details on Cardio and Insurance datasets are not disclosed, and relevant citations for these datasets are missing. Additionally, the authors do not provide clear references to the baselines (e.g., it is unclear which papers CTGAN, TVAE, ARF, DDPM, and GREAT correspond to in L343).
- The authors state that all methods are fine-tuned on the test dataset (L348) but then fit a CatBoost model on the generated data from models fine-tuned on the test set (L346) to predict table elements from the test set itself (L347). Is this interpretation correct? If so, the metrics’ significance is unclear. For instance, a model that generates only the exact data it was fine-tuned on would make the generated synthetic training set overlap with the test set, which would improve CatBoost performance, but the metrics would not indicate the model’s ability to generate novel synthetic data instead of memorized training data. The fine-tuning procedure on the test set, followed by training a classifier on the generated data, raises concerns about data leakage and the validity of the evaluation. The evaluation protocol does not clearly isolate the generative capabilities of the model from its capacity to memorize and reproduce training data.
- The paper's presentation is poor and requires improvement. References are incorrectly formatted (e.g., missing parentheses), figures exceed boundary limits (e.g., Figure 2), and the phrase “scaling law” is mentioned 14 times without citing a single scaling law paper.
- No results are provided for multiclass classification or regression tasks. Although some discussion is included in L467, quantitative comparisons on other tasks between the authors’ method and other baselines are necessary to showcase the general capability and utility of LaTable. The absence of these results limits the assessment of the model's versatility and applicability to a broader range of tabular data problems.

### Questions
Can the authors clarify what WhereIsAI/UAE-Large-V1 refers to in L171?

### Soundness
1

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The work introduces a generative model LaTable designed specifically for tabular data generation. Recognizing the ubiquity and challenges of tabular data, the authors focus on managing heterogeneous tabular data features, such as categorical and numerical variables, across various datasets. LaTable leverages metadata to improve the generation process and is built upon an encoder-only transformer. The model is evaluated through few-shot learning scenarios to validate its cross-dataset generalization capabilities. Additionally, LaTable shows early signs of scaling laws, commonly observed in foundation models in other domains.

### Strengths
The paper clearly outlines four primary design goals—cross-dataset generation, handling of categorical and numerical features, use of textual context, and column order equivariance—and effectively aligns these with specific model design choices. Additionally, it identifies scaling laws unique to tabular data, which is valuable given that this area has not been thoroughly explored within the scope of tabular foundation models.

### Weaknesses
1. LaTable shows limited robustness on non-binary classification tasks, such as multi-class classification and regression, suggesting constrained generalization across different task types.
2. The descriptions of datasets and baseline models are brief and lack detail.
3. The evaluation metrics are limited, primarily focusing on downstream performance.
4. Figure 2 is oversized.
5. Although the paper acknowledges issues of data bias and fairness, it does not explore practical approaches to detecting or mitigating these biases in real-world applications.

### Questions
1. Will you consider including additional metrics beyond downstream performance, such as low-order and high-order statistics [1]?
2. Will you consider adding more recent baselines, such as TABSYN [1] and TabDDPM [2]?
3. Figure 2 illustrates the effects of training set size and model parameters but does not address the impact of the number of categories and numerical features. Will you consider investigating this aspect?
4. Do you plan to release the codes?

[1] Zhang, Hengrui, et al. "Mixed-type tabular data synthesis with score-based diffusion in latent space." arXiv preprint arXiv:2310.09656 (2023).
[2] Kotelnikov, Akim, et al. "Tabddpm: Modelling tabular data with diffusion models." International Conference on Machine Learning. PMLR, 2023.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
The paper introduces "LaTable," a novel generative model for tabular data based on diffusion techniques, specifically aimed at large-scale tabular data generation. LaTable displays early signs of "scaling laws" observed in foundation models. The authors empirically demonstrate that their model outperforms existing generative models in ood settings.

### Strengths
- The paper addresses the underexplored domain of large-scale tabular data modeling, a departure from traditional focus areas in foundation models such as text and vision.
- The model meets several carefully formulated desiderata: cross-dataset generation, mixed-type handling, use of textual metadata, and equivariance to column order. The authors thoroughly answer each desiderata in their model design.
- LaTable represents an important step toward creating generative models that can be applied to diverse tabular datasets.

### Weaknesses
I mostly found it hard to understand the architecture of the model and the training objectives you used on it. I am from outside the tabular data community so this may be the reason, but I think that it should be clear to people outside the community as well. It is clear that you very carefully designed the architecture to meet all your requirements but I wasn't sure in the end what is the input/output, how you train everything end-to-end. A more higher level description is required instead of diving in directly to satisfying desiderata.

### Questions
None

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
3

### Summary
This work proposes LaTable, a Diffusion model for tabular data generation that can be pretrained on large collections of tabular datasets and used for unconditional and conditional generation on unseen datasets in a few-shot manner. The model is evaluated in a few-shot generation setup where it performs comparably against other techniques.

### Strengths
Strengths:

* The present work is one of the first works that trains a generative transformer model across several dataset. The collection of datasets used to train the model presented is bigger than of any other works I am aware of, thereby making a reasonable step towards scaling up tabular models.

* Evaluation through ablation studies : I like the evaluation done through several ablation studies, showing the usefulness of the individual components. The results support the respective design choices.

* The Limitation and Discussion Section is honest and insightful.

### Weaknesses
Weaknesses
* The write-up is quite hard to understand and the notation seems overwhelming at some points. I know the basics of denoising diffusion models, but I was not quite able to follow in what space the diffusion happens and how exactly it is mapped back and forth into the tabular representation. Figure 1 doesn’t help much to gain a better understanding. In particular, I would have appreciated a section which would detail the generation procedure. I do not understand where in Figure 1 noise is input to generate synthetic samples and in diffusion models there are different generation paradigms as well, such as latent diffusion etc. I do not think the write-up is very accessible in its current form.
* Related Work. This is not the first attempt to build a tabular foundation models trained on multiple datasets. Notable approaches include TabPFN (Hollmann et al., 2023). I also wonder how LaTable compares to other approaches (although mainly focused on classification), such as Yak et al. (2023) or Zhu et al. (2023). It is unfortunate, that these competing approaches are neither discussed nor compared in the evaluation. 
* Conditional Generation / Classification is not evaluated. The authors describe how conditional generation can be implemented with LaTable, but do not test is as far as I see. This also trivally allows to use LaTable for the classification task (by conditioning on all tabular features and letting the model generate the label). Here, it would be insightful to compare LaTable’s performance to models such as TabPFN, XTab, or GREAT. Also in addition, zero-shot and fine-tuning with the entire dataset should be considered for a comprehensive evaluation.
* The evaluation only uses ML Efficiency (Train Synth., Test Real, TSTR). For a comprehensive picture, the performance of a model trained on the real data should be included as an upper baseline to assess the data quality gap in the TSTR table. In addition, there could be further data quality metrics, including metrics such as the Discriminator metric (e.g. used in Borisov et al., 2023) where a model is trained to differentiate between original and synthetic data and its performance is reported. Also some quantitative results could complement the evaluation.

The overall impression of the submission suggests that not much care was taken to prepare the current manuscript for submission and several important things have been neglected:
* The citation format is incorrect, citep is not used properly
* The Appendix and Supplementary materials are missing
* There are several formatting issues, e.g., Figure 2
* Text in formulas should be wrapped in \text, e.g. \text{softmax} (eqn. 1, 2)
* There is no code available.

While these points may be fixed, I think for submission at a respected venue such as ICLR more care should be taken.

**Summary.** Overall, the submission seems to be rushed and I think a thorough revision is needed. This should include a more accessible write-up, studying classification performance and additional data quality metrics, and comparing with other attempts for building large tabular models.


Typos: 
* Please check if “e.g.” should be followed by a comma.
* l. 237: transformer‘s
* l. 207 mathbb{R}  instead of normal R
* Caption of Figure 2: Capitalization of LaTable

### Questions
Can you explain the generation procedure? Where is the noise inserted?

Can you differentiate LaTable from other large tabular models, e.g. TabPFN? How does it compare?

### Soundness
2

### Presentation
1

### Contribution
3
