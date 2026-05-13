# Learning Robust EEG Representations with a Large Spatiotemporal Transformer as a Foundation Model

- Decision: Reject
- Scores: 3, 6, 6, 6, 6

## Abstract
Electroencephalography (EEG)-based brain-computer interfaces (BCIs) serve many control paradigms by relying on a variety in active brain regions and EEG features. Developing a universal EEG foundation model has been challenging due to the large variety in recording setups and experimental tasks. Additionally, researchers often contend with limited labeled data, making it difficult to utilize large deep-learning models effectively. While there have been successful attempts to develop EEG foundation models, few studies have systematically evaluated their adaptability across diverse BCI control paradigms. To address this gap, we propose a novel, yet simple spatiotemporal EEG transformer (ST-EEGFormer) that projects segments (“patches”) of raw EEG data into an embedding space enriched with a spatial and temporal embedding, allowing the model to effectively handle EEG data exhibiting various channel set-ups and time lengths. To improve data efficiency, we first employed a masked autoencoder (MAE) task to pre-train the ST-EEGFormer in a self-supervised learning manner on a dataset combining six different motor imagery (MI) datasets, a P300 dataset, and a steady-state visual evoked potential (SSVEP) dataset, all of which are public. Next, we benchmarked the pre-trained model, after fine-tuning, on diverse downstream classification tasks. To evaluate the generalization capability, we conducted additional experiments on two public datasets, not used for pre-training: a seizure classification dataset and an online MI BCI dataset. We compared the performance against a simple linear model, EEGNet (a classic CNN-based benchmark model), the state-of-the-art supervised EEG Conformer model, and two foundation models, BIOT and Large Brain Model (LaBraM). The pre-trained ST-EEGFormers could learn robust EEG representations, achieving higher classification accuracies than the benchmarked models across all eight pre-training datasets and exhibiting strong generalization on new datasets with limited training data. Finally, we report several visualizations of the model including the features on which the results are based.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper proposes a spatio-temporal EEG transformer to build an EEG foundation model. The model is pretrained using a masked autoencoder (MAE) on various public datasets and demonstrates strong generalization on new datasets, outperforming existing work such as EEGNet and EEG Conformer in various classification tasks.

### Strengths
1. The authors conducted model pretraining using very large amounts of data from 8 EEG datasets with various tasks. 
2. The proposed network effectively captures both temporal and spatial information from EEG data.
3. The method achieves state-of-the-art performance across multiple datasets.

### Weaknesses
Overall, it is difficult to evaluate the contribution of this work due to (1) limited novelty and (2) missing comparison with recently published work. The proposed architecture is similar or a simple version of LaBraM [2] Please see details as follows:   

1. Questionable Contribution Claims: The authors make several problematic claims regarding the novelty and contributions of the proposed ST-EEGFormer. For example, in line 134-135, '...However, since their encoder module works with patches of EEG signals in fixed channels and time length, transferring between datasets remains unrealistic and challenging', this statement on current methods not being able to adapt to different datasets due to their reliance on fixed channels and time lengths is NOT true. The authors fail to mention recent published work, such as BIOT [1] (NeurIPS' 23) and LaBraM [2] (ICLR' 24), which were explicitly designed to handle diverse EEG datasets with varying channels and lengths. Therefore, the contribution claim 'This paper presents, for the first time, a large transformer-based ST-EEGFormer model that is channel-aware, flexible, and applicable across various datasets and tasks' (line 079-080) is inaccurate and misleading.

2. Inappropriate Statements in Contribution Section: In line 086, ' Upon acceptance of this paper, the code and pretrained model weights will be made open-source', this statement should NOT be in the Contribution section, as these resources are not currently available to  the EEG community or to reviewers who are evaluating the work. Similarly, in line 087-089, the authors claim 'We believe that the demonstrated effectiveness of the proposed ST-EEGFormer model can serve as a pioneering effort, encouraging further studies on developing better end-to-end EEG-BCI foundation models to accelerate BCI development and neuroscience research.' , which would be better suited to the discussion section rather than contributions.

3. Lack of Comparison with Closly-related Recent Work: This manuscript fails to conduct comparisons with recently published work, including BIOT [1] (NeurIPS' 23) and LaBraM [2] (ICLR' 24), which have made their code and pretrained weights publicy available, making direct implementation and evaluation easy. Please see the pretrained weights here: 
BIOT [1] pretrained weights: https://github.com/ycq091044/BIOT/tree/main/pretrained-models
LaBraM [2] pretrained weights: https://github.com/935963004/LaBraM/tree/main/checkpoints

### Questions
The authors should provide more details on the pretraining setup, including GPU usage and time used for pretraining.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents ST-EEGFormer, a large transformer-based model designed for learning representations from EEG data.  The model is channel-aware and flexible, capable of handling diverse datasets and tasks through self-supervised pretraining using the masked autoencoder approach.

### Strengths
1. Foundation models for EEG (and time series data in general) are not inherently designed to handle varying numbers of channels. The paper solves this issue by using both temporal and spatial positional encodings for each token, which enables the model to work with a variety of different datasets and tasks.
2. Existing foundation models for EEG such as Neuro-GPT [1] and BENDR [2] pre-trained on a single large dataset (TUH) whereas the current paper utilizes a variety of different datasets for pre-training of their model because of its ability to handle varying numbers of channels.

### Weaknesses
1. The novelty is not entirely clear. The authors claim that the novelty lies in their model’s ability to project segments of raw EEG data into an embedding space enriched with spatial and temporal embeddings. However, this appears to merge two existing and increasingly popular techniques in time-series research: (1) The paper by Xie et al. [3] published in 2022 uses a very similar method to encode both spatial and temporal position in a single transformer model. (2) Papers such as PatchTST [4] and Neuro-GPT [1] have performed chunking along the temporal axis.

2. While EEG-Conformer is a relevant model to compare with, It would be beneficial to the paper to conduct qualitative and quantitive comparisons with other papers that share the same spirit of foundation models for EEG such as Neuro-GPT [1], BENDR [2], and EEGFormer [5]. The lack of comparison with these models makes it difficult to assess the true contribution of the proposed method.

3. A major expectation from a foundation model is the ability to generalize on data it hasn’t seen before, i.e. data that it wasn’t pretrained on. The authors have evaluated the model on only two such datasets. It would be helpful to expand this evaluation to include more datasets that are not part of the training corpus, preferably alongside comparisons with other large EEG-models mentioned earlier. The current evaluation is insufficient to demonstrate the generalization capabilities of the model.

Minor issues:
1. On line 149 of the text, it’s not very clear what the authors mean by “samll patches consist of all channels”. Perhaps, it is “small patches consisting of all channels”.
2. From 426-428, the following sentence is repeated: “However, differences were observed when additional clusters were introduced”.
3. In Table 2, it would be better to have the second-best accuracy underlined instead of bold for better distinction.

### Questions
1. Referring to point 1 in Weaknesses, could the authors please elaborate on the novelty of their work?

2. The original EEG Conformer paper reports an accuracy of 78.66% for the BCI Competition IV Dataset 2a, while the current paper reports EEG-conformer’s accuracy for the same dataset as 56%. For BCI Competition IV Dataset 2a, the reported accuracies in both the original (84.63%) and current paper (83.10%) are more or less the same. Can the authors kindly explain the significant difference in the reported accuracy for EEG Conformer on the BCI Competition IV Dataset 2a?

References:
1. Cui, Wenhui, et al. "Neuro-GPT: developing a foundation model for EEG." arXiv preprint arXiv:2311.03764 (2023).
2. Kostas, Demetres, Stephane Aroca-Ouellette, and Frank Rudzicz. "BENDR: Using transformers and a contrastive self-supervised learning task to learn from massive amounts of EEG data." Frontiers in Human Neuroscience 15 (2021): 653659.
3. Xie J, Zhang J, Sun J, Ma Z, Qin L, Li G, Zhou H, Zhan Y. A Transformer-Based Approach Combining Deep Learning Network and Spatial-Temporal Information for Raw EEG Classification. IEEE Trans Neural Syst Rehabil Eng. 2022
4. Nie, Yuqi, et al. "A time series is worth 64 words: Long-term forecasting with transformers." arXiv preprint arXiv:2211.14730 (2022).
5. Chen, Yuqi, et al. "EEGFormer: Towards transferable and interpretable large-scale EEG foundation model." arXiv preprint arXiv:2401.10278 (2024).

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
4

### Summary
This paper explores the difficulties associated with creating a universal EEG-based brain-computer interface (BCI) by presenting a new spatiotemporal EEG transformer (ST-EEGFormer). The authors aim to enhance current BCI applications while tackling the issue of scarce labeled data in EEG studies. Their model is designed to effectively manage a range of EEG recording configurations and tasks using self-supervised learning, thereby aiming to boost data efficiency and classification accuracy. The research also highlights the ST-EEGFormer’s ability to generalize across different datasets, underscoring its significant potential for advancing EEG research and BCI technology. Ultimately, this work offers both a practical approach to existing challenges and a theoretical insight into EEG data representation.

### Strengths
A key strength of this research is the ability of the pretrained ST-EEGFormer to develop robust EEG representations that yield superior classification accuracies compared to benchmark models across various pretraining datasets. This highlights not only the model’s effectiveness but also its adaptability, as it demonstrates strong generalization on new datasets, even with limited training data. Furthermore, the incorporation of visualizations of model features improves the interpretability of the results, shedding light on the model's functioning. By making the pretrained model weights and code publicly accessible, the study promotes transparency and encourages further exploration in the field, thereby enhancing its overall impact.

### Weaknesses
Although the ST-EEGFormer demonstrates strong performance, its effectiveness may be constrained when encountering entirely new or atypical datasets that significantly differ from those used in pretraining. Specifically, the model's reliance on pretraining on a limited set of datasets may not capture the full spectrum of EEG signal variability, potentially leading to reduced performance on datasets with different recording parameters, subject populations, or task paradigms. Moreover, the model's complexity could lead to higher computational demands, presenting practical challenges for real-time BCI applications, particularly in resource-constrained environments. The computational overhead associated with the transformer architecture, including the attention mechanism, could limit its applicability in scenarios requiring low-latency processing. 
One potential limitation of this study is its reliance on self-supervised learning, which might not fully tackle the challenges arising from the variability of EEG data across different tasks and recording conditions. While self-supervised learning is effective for capturing general features, it may not be optimal for tasks requiring fine-grained discrimination or for datasets with unique characteristics. Lastly, while the paper highlights improved classification accuracies, a more thorough examination of the model's interpretability and any potential biases in its learning process would enhance the reliability of the results across various populations and contexts. The lack of detailed analysis regarding the model's decision-making process and potential biases could limit its practical applicability, especially in sensitive domains where fairness and transparency are crucial.

### Questions
In the related work section, I recommend expanding the discussion on recent developments in attention-based transformer models that have influenced BCI researchers. Specifically, incorporating citations from key foundational papers in this field would strengthen your analysis.

Including a discussion section is much more beneficial than simply reporting the results. You can put limitations and suggest future directions for research within the same context.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper addresses the challenges of developing a universal EEG-based brain-computer interface (BCI) by introducing a novel spatiotemporal EEG transformer (ST-EEGFormer). This work combines the objectives of enhancing existing applications in BCI technology and addressing the problem of limited labeled data in EEG research. By proposing a model that effectively handles diverse EEG recording setups and tasks through self-supervised learning, the authors aim to improve data efficiency and classification performance. Additionally, the study emphasizes the generalization capabilities of the ST-EEGFormer across various datasets, thus highlighting its potential impact on the field of EEG research and BCI applications. Overall, the paper seeks to provide both a practical solution for known challenges and a theoretical contribution to the understanding of EEG data representation.

### Strengths
A strong point of this work is the demonstrated capability of the pretrained ST-EEGFormer to learn robust EEG representations that achieve higher classification accuracies compared to benchmark models across various pretraining datasets. This indicates not only the effectiveness of the model but also its adaptability, as it exhibits strong generalization on new datasets, even when limited training data is available. Additionally, the inclusion of visualizations of model features enhances the interpretability of the results, providing insights into how the model operates. The commitment to making the pretrained model weights and code publicly available further promotes transparency and encourages further research in the field, enhancing the overall impact of the study.

### Weaknesses
One potential weakness of the study is the reliance on self-supervised learning, which may not fully address the challenges posed by the variability in EEG data across different tasks and recording setups. While the ST-EEGFormer shows strong performance, the model's effectiveness could be limited when faced with completely novel or atypical datasets that diverge significantly from those used in pretraining. Additionally, the complexity of the model may result in increased computational requirements, which could pose practical challenges for real-time BCI applications. Finally, while the paper reports improved classification accuracies, it may benefit from a more detailed analysis of the model's interpretability and potential biases in its learning process, ensuring that the results are not only accurate but also reliable across diverse populations and scenarios.

### Questions
1- The introduction provides a comprehensive overview of EEG and its applications in BCIs, effectively contextualizing the research. However, there are a few areas that could be improved: First, while it outlines various EEG paradigms and traditional methods, it could benefit from a clearer statement of the specific gap or problem the proposed ST-EEGFormer addresses more explicitly. This would help readers understand the motivation behind the research. Furthermore, the transition between discussing existing methods and introducing the new model feels somewhat abrupt; a smoother connection would enhance the flow of the narrative.

Ican see huge gap here: Consequently, small models that typically rely on convolutional neural networks (CNNs) impose
restrictions on input shape (e.g., the number of EEG channels, and the number of samples), further
complicating the use of different datasets as they usually exhibit different data formats.
Contributions: This paper presents, for the first time, a large transformer-based ST-EEGFormer
model that is channel-aware, flexible, and applicable across various datasets and tasks. 

2- In the related work section, I suggest enhancing the discussion on recent advances in attention-based transformer models that have inspired BCI researchers. Specifically, you could include citations from foundational papers in this area, such as:

"A transformer-based approach combining deep learning networks and spatial-temporal information for raw EEG classification" (IEEE Transactions on Neural Systems and Rehabilitation Engineering, 2022, 30, pp. 2126-2136).
"An end-to-end CNN with attentional mechanism applied to raw EEG in a BCI classification task" (Journal of Neural Engineering, 2021, 18(4), p. 0460e3).
Including these earlier works would provide valuable context, allowing you to discuss how they relate to or differ from the current studies. Additionally, a brief exploration of the evolution of transformer-based approaches in EEG classification would enrich the narrative and demonstrate the progression in this research area. This could help clarify the significance of the EEG Conformer model in relation to previous methodologies.

3-It may be beneficial to consider both non-overlapping and overlapping segments during the tokenization process. Non-overlapping segments simplify the model's input structure, potentially enhancing processing efficiency. However, overlapping segments can capture greater temporal context and variations within the data, which may lead to richer feature representations. By incorporating both approaches, the model could leverage the strengths of each method, thereby improving its ability to generalize across different EEG tasks and enhancing overall performance. This dual strategy would also provide more flexibility in handling EEG data, accommodating various recording setups and experimental conditions. I recommend discussing the potential trade-offs between these approaches and comparing their performance specifically in the context of the ST-EEGFormer model.

4- I encourage the authors to include a discussion section in this paper to address the results in depth. This section should explore the implications of the findings, highlight any limitations, and suggest directions for future research. Including these elements will enhance the overall impact of the paper and provide valuable insights for readers.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposes a universal spatiotemporal EEG transformer model, which is pretrained on segments of various EEG-based BCI experiment datasets (motor imagery, P300 speller, SSVEP). Pretraining is performed via a standard masked autoencoder (MAE) approach. The model is also shown to generalize well on a diverse set of downstream classification tasks, which were not used in pretraining (e.g., seizure classification).

### Strengths
- This work is unique in its collection of a wide range of pretraining datasets on diverse tasks (i.e., both including motor imagery, P300 speller, or SSVEP datasets), without being constrained to the number of EEG sensors.
- The success of generalization experiments on alternative datasets on other tasks (seizure classification, online MI) is a strong point.

### Weaknesses
 - Methodologically, the work is solely based on the well-known MAE approach, and the main contribution appears to be only empirical.
- Some of the experimental results necessitate further details/clarifications (see questions).



### Questions
- It appears like the ST-EEGFormer-large model is often necessary to achieve state-of-the-art performance, in comparison to existing models. To justify and validate this comparison, one should also include the total computational overhead and the training costs of obtaining each of these models (small, base, large) for final use.

- Finger MI classification experiments (Large-MI-5F) demonstrate quite strong results. It would be interesting to see how much of model generalization could be performed on this dataset, if it was not part of the pretraining corpus (i.e., pretraining without Large-MI-5F at all and only testing on this dataset for downstream classification).

- The MAE pretraining strategy should be discussed a bit more in the main manuscript to be self-contained.

- The paper only considers EEGNet and EEG Conformer models as state-of-the-art model examples. However, there has been a wide range of attempts to improve generalization performance in EEG-based BCIs along this line, and the authors should discuss (if not empirically compare against) these relevant pieces of work.

[1] "Learning invariant representations from EEG via adversarial inference."

[2] "Contrastive learning of subject-invariant EEG representations for cross-subject emotion recognition."

[3] "BENDR: Using transformers and a contrastive self-supervised learning task to learn from massive amounts of EEG data."

[4] "SPD domain-specific batch normalization to crack interpretable unsupervised domain adaptation in EEG."

### Soundness
3

### Presentation
3

### Contribution
2
