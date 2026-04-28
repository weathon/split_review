# KBFormer: A Transformer-based Diffusion Model of Structured Entities with Heterogeneous Properties

- Decision: Reject
- Avg Score: 5.60
- Scores: 6, 5, 6, 5, 6

## Abstract
We present a generative attention-based architecture that models structured entities comprising different property types, such as numerical, categorical, string, and composite. This architecture handles such heterogeneous data through a mixed continuous-discrete diffusion process over the properties. This flexible framework is capable of modeling entities with arbitrary hierarchical properties, enabling applications to structured KB entities and tabular data. Experiments with a device KB and a nuclear physics dataset demonstrate the model's ability to learn representations useful for entity completion in diverse settings. This has many downstream use cases, including modeling numerical properties with high accuracy - critical for science applications. An additional benefit of the model is its inherent probabilistic nature, enabling predictions accompanied by uncertainties. These critical capabilities are leveraged in a nuclear physics dataset to make precise predictions on various properties of nuclei.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work proposes a diffusion model for generating and demasking structured entities. KBFormer uses a mixed continuous-discrete diffusion process to generate different data types, such as text, numerical, categorical, and ordinal, and a transformer module to model cross-property relations. The paper demonstrates that KBFormer can outperform large language models on entity completion tasks and provide uncertainty estimation.

### Strengths
- The proposed architecture with much smaller model parameters  can outperform LLMs which highlights the importance of modeling structure-aware inductive biases.

- It can perform entity completion tasks with high accuracy and provides uncertainty estimation which is very useful for science applications that require confidence and reliability

- It serves as an interpretable multi-modal foundation model for structured data and can augment LLMs with structure-aware inductive biases.

### Weaknesses
1) The paper does not discuss or compare with other methods that can handle discrete data with continuous state, such as [1].  Moreover, the paper only compares with LLaMA2 for the first experiment, but it would be interesting to see how the proposed model performs against other knowledge masking strategies, such as [2, 3].

2) The section on “Continuous Relaxation of Discrete State Diffusion” is not well explained. It is unclear what its objective is;  is the goal to learn bin centers, and how they are used in demasking? Is the discretization with 256 bins and learned bin centers similar to GMM with 256 mixtures? The paper also introduces some terms without proper definitions, such as “an infinite bin limit approximation” and “discretization with a large but finite bin density”. It would be helpful to provide more details and intuition behind these concepts.

3) The paper needs to improve its writing quality and clarity. Some specific issues are:
Proposition 1: The font of the proposition should be consistent and italicized. Is a proof provided  in the appendix?
Page 6: The phrase “… see Section 3.2.” should be enclosed in parentheses, as it is not part of the main sentence.

### Questions
1) Which type of encoder and decoder did you use for different property types: i)- conditioning on the property itself or ii) disjoint encoders for each property ?

2) In page 6, it is stated that “ ‘year’ has the same representation in different contexts …” but the RNN encoder outputs context-aware representation. Can you clarify?  

3) For experiments in section 5.2, what is the evaluation method? It is also worth comparing it with other models such as fine-tuned LLaMA2.  Also, for the evaluation of experiment in 5.1, please provide more clarification or examples for rotating each dictionary’s fields D times and predicting only the last value.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a diffusion-based generative model to study the structured entities, with various property types such as numerical, categorical, strings. This work should address an interesting topic. However, I am not an expert in this area, and I am getting quite confused about the whole procedure and mechanism after several rounds of reading. I have a quick look at the code and believe the author should implement correctly. Maybe the authors can provide more details about KBformer, and re-organize the presentation to make it easy for understanding.

### Strengths
**1** The problems that this work tries to address are interesting and important. Also, the performance is promising.

**1** The usage of diffusion process for entities is well-explored.

### Weaknesses
However, I hope the authors can improve the paper through the following aspects:

**1** the presentation of the paper is quite poor. For example, I hope the authors can make it comprehensive for Figure 5, many parts in this figure is unexplained. Maybe since I am not an expert in this topic, I find it quite confused and have many unclear parts for the KBFomer architecture.

### Questions
NA

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents KBFormer, an innovative transformer-based diffusion model adept at managing structured entities featuring heterogeneous characteristics. This versatile model excels in accommodating entities with complex hierarchical attributes, making it particularly suited for structured knowledge bases (KBs) and tabular data. KBFormer is designed to learn representations that are effective for entity completion across a range of contexts, and its probabilistic approach allows for predictions that incorporate measures of uncertainty. The authors detail the model's training methodology, introducing a novel loss modification that reimagines the problem as a continuous-time diffusion process over discrete states with an absorbing state. The paper culminates with an exploration of KBFormer's applicability in downstream tasks, highlighting its capacity to model numerical properties with remarkable precision and to generate accurate predictions in specialized domains, including nuclear physics.

### Strengths
- This work introduces KBFormer, a novel transformer-based diffusion model adept at managing structured entities with varied and complex properties.
- The paper demonstrates the model's practical applications, particularly in high-accuracy numerical property modeling and precise prediction-making in fields like nuclear physics, highlighting its value to researchers.
- The paper is well-placed in the literature, with the KBFormer framework being noted for its flexibility and extensiveness, marking a progression from previous models.
- The paper is clearly written and accessible, with lucid explanations of the model's architecture, training processes, and experimental results, catering to a broad audience.
- The submission includes supplementary materials for implementation, which enhances the paper's credibility and supports the reproducibility of the KBFormer model.

### Weaknesses
 - This paper lacks ablation studies. The paper does not include ablation studies to analyze the contribution of different components of the model to its overall performance. For example, it is mentioned in paragraph "Encoding" of section 4, that two alternatives for embedding numerical values, yet it lacks a quantitative performance comparison between these methods. Conducting such an analysis could shed light on the critical components of the model and direct future enhancements.
- There is no discussion in the paper about the limitations or potential failure modes of the KBFormer method. Including this could be crucial for fully understanding where the model may fall short in practical applications and where further research and development could be most beneficial.

### Questions
Besides the aspects mentioned in "Weakness", I have the following concerns:

- I would like to suggest the authors confirm whether the abbreviations used throughout the paper, such as “KB” in the abstract, are consistently defined upon first use? A uniform approach to abbreviation would aid reader comprehension.
- The introduction promises that the KBFormer model addresses several tasks: KB completion, entity linking, anomalous property detection, and enhancement of foundation models with learned representations. The experiments, however, seem to showcase a subset of these. Can the authors clarify the criteria for experiment selection and indicate if demonstrating the model's capabilities on the remaining tasks is within the scope of future work?
- Would the authors consider revising the reference list to ensure that all citations are consistent and reflect the most current research where applicable? This would help maintain the paper’s relevance and assist readers in locating the sources.

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a generative attention-based architecture that models structured entities comprising different property types, with applications on KB entities and tabular data. A hybrid diffusion training paradigm is proposed to handle the modeling of heterogeneous properties.

### Strengths
1. The paper is well-presented, with excellent visualizations and clear delivery of the model details and results.
2. KBTransformer enjoys superior performance against baselines in terms of prediction accuracies on two real data sets.

### Weaknesses
1. The paper's contribution seems to be a bit incremental, since the diffusion modeling over heterogeneous data in Section 3.2 follows the previous work [1]. It would be helpful if the authors could clarify the difference/contribution of the proposed method.
2. In the experiments, only the baseline that always predicts the marginal mode/mean is compared in terms of the prediction accuracy with different unmasked rates. Are there any other baselines with regression/autoregression that can be compared? Also it would be helpful if the authors could elaborate on Section 3.1 about why other traditional models with regression and masked modeling will have less optimal performance.

### Questions
Please see above.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a generative attention-based architecture, named KBFormer, for modeling structured entities consisting of different property types. The model is able to perform joint modeling of an entity's properties due to the hybrid diffusion training approach. The experimental results on a device KB and a nuclear physical dataset demonstrate the model's capability in representation learning for entity completion in diverse settings. The model is demonstrated to share information across properties and have various downstream uses for scientific applications. The inherent probabilistic nature of the model enables predictions accompanied by uncertainties.

### Strengths
Originality: The paper uniquely contributes to the field by proposing a generative attention-based architecture which can handle heterogenous data types through a mixed continuous-discrete diffusion process over the properties. Such a method stands out among the popular autoregressive models. 

Quality: The paper carefully designs the experiments to support the idea and improve their illustrations with helpful visualizations.

Clarity: The paper effectively communicates its ideas and findings with clarity. The paper is well-written, and the logic is coherent. Necessary mathematical deductions are presented for better understanding of the diffusion process. 

Significance: The model proposed in the paper successfully handles heterogeneous property types along with hierarchical encodings with semantic meaning for different property types, and demonstrates its potential in various downstream scientific tasks. Besides, the model has an edge over traditional autoregressive models due to its inherent probabilistic nature.

### Weaknesses
1. Although the authors make clear introductions to the hybrid diffusion training paradigm, the explanation for the model architecture is not clear enough (sometimes even confusing). In fact, the first of my two questions is because of not understanding the architecture here. I suggest the authors can modify Figure 5 and 6 to make the pipeline transparent to readers and include more details in the texts in an ordered way.

2. Although the inherent probabilistic nature of the model makes it suitable for prediction tasks for scientific scenario, I still believe that comparisons between the KBFormer and some regression model baselines should be included to demonstrate the effectiveness of the model. Besides, in order to illustrate the model's capability in scientific applications, more experiments on benchmarks from other disciplines like molecules, proteins, etc., are required.

### Questions
1. In terms of the model architecture, I suppose the output from the encoder is $(3, feature size)$ for the example shown in Figure 5. If that is true, I'm wondering why it is necessary to use a transformer model with such a short "sequence length".

2. Transformer encoders are used to encode text fields. However, if the text is simply a property value (e.g. "iPhone" in Figure 5), why not just use a pretrained word embedding?

3. The diffusion training strategy is a promising solution for probabilistic-based generative models. However, is the diffusion paradigm the optimal method to do this? Is there any other generative model (or even regressive model) that does not rely on the noise and denoise process?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
