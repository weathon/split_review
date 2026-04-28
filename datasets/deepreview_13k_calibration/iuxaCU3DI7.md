# Recognize Any Surgical Object: Unleashing the Power of Weakly-Supervised Data

- Decision: Accept
- Avg Score: 7.50
- Scores: 8, 8, 8, 6

## Abstract
We present RASO, a foundation model designed to Recognize Any Surgical Object, offering robust open-set recognition capabilities across a broad range of surgical procedures and object classes, in both surgical images and videos. RASO leverages a novel weakly-supervised learning framework that generates tag-image-text pairs automatically from large-scale unannotated surgical lecture videos, significantly reducing the need for manual annotations. Our scalable data generation pipeline gatherers to 2,200 surgical procedures and produces 3.6 million tag annotations across 2,066 unique surgical tags. Our experiments show that RASO achieves improvements of 2.9 mAP, 4.5 mAP, 10.6 mAP, and 7.2 mAP on four standard surgical benchmarks respectively in zero-shot settings, and surpasses state-of-the-art models in supervised surgical action recognition tasks. We will open-source our code, model, and dataset to facilitate further research.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors introduced a foundation model aimed at recognizing surgical objects in closed and open set environments. It also adapts to learn from images and videos. They introduce a weakly supervised learning framework to generate tag-image-text pairs from surgical lecture videos. This allowed them to create an interesting dataset that could be helpful for researchers. Experimental results demonstrate that the proposed method outperforms other SOTA methods in zero-shot scenarios and in supervised surgical action recognition tasks.

### Strengths
- The paper is well presented and easy to follow.
- Although the technical contribution is limited, the efforts and contributions in the paper are great and are likely to help the research community in the field of surgical tool detection, segmentation and analysis. 
- The evaluation is good and ablation studies reflect how the method could work in different settings.

### Weaknesses
1- The main weakness of the paper from a technical perspective is the limited technical contribution. The methodology is heavily based on RAM (Zhang 2024) with an additional temporal attention layer.

2- It is not clear in Figure 2 how the embeddings from I and Vs are processed in the Tag Decoder. How does the network balance the importance of information coming from images or videos?

3- It was not clear why pre-training and fine-tuning were performed for a small number of epochs. Does the loss saturate when fine-tuning for 4 epochs only?

4- VLM automated annotation: it is not clear the effect of the ability of GPT-4o in generating accurate annotation. An assessment of this step is needed.

### Questions
To relate to the 4 points in the weakness section

1- Explain or confirm the main technical differences with RAM

2- Provide more details on how the network balances the importance of image and video embeddings

3- Answer point 3 in the weaknesses

4- Elaborate on 4 in the weaknesses

### Soundness
3

### Presentation
4

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
The paper introduces a recognize-any-object (RAM) foundation model for surgery. The work employs a weakly supervised approach by generating a weakly annotated dataset from web-surgical-like data sources. Data from surgical lectures is processed to generate captions that are further used to generate different levels of annotations, including actions and entities. From the methodological perspective, the model follows RAM-based architectures with an additional temporal attention fusion layer integrated to work on video information.

### Strengths
The paper incorporates weak annotations from multiple video sources and investigates the zero-shot generalizability of adapted recognize-anything models in the surgical environment. Generating annotations from surgical videos is a common limitation in the medical domain as it requires expert knowledge. Hence, an approach that allows leveraging this data is interesting from the surgical ML perspective.

### Weaknesses
The work presents a modification to a previous RAM model and a pipeline for data generation. Even though leveraging web-based data from unstructured medical sources can be relevant for medical machine-learning purposes, I am unsure about the significance of the contribution from the general machine-learning perspective.



### Questions
The work introduces a methodology to generate weak annotations, which can also make it possible to fine-tune existing foundation models with extensive surgical data. In this regard, what are the additional benefits of the introduced model compared with standard foundation models fine-tuned on the weakly annotated data?

It is interesting to see that in Table 4, average pooling performs better than temporal attention in the instrument recognition tasks. What would be the main insights regarding this result?

Figure 3 is written WshiperX, probably instead of WhisperX.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The Paper presents a data generation pipeline for weakly supervised training framework and a foundation model architecture RASO. RASO predicts an open set of tags for single frames while taking video context into account. The data generation pipeline extracts relevant tags from voiceovers of surgical lecture videos. RASO is evaluated in a zero-shot and a supervised setting.

### Strengths
- interesting approach which proposes novel architecture, pipeline and data
- Paper is well structured, easy to read and easy to follow the argumentation
- profound evaluation, RASO is compared against 4 SOTA architectures for the zero-shot setting on 4 datasets and 3 SOTA models for the supervised setting on the CholecT50
- Paper presents an ablation study for the pretraining and fine-tuning stages, as well as two different aggregation methods for the video context understanding 
- code, models and dataset will be open-sourced

### Weaknesses
 - missing details regarding the evaluation, e.g. why was the video aggregation not used in the first two experiments? which data was used for which configuration? ... (see questions)
- no link to code, data, and models in the paper

- Line 184ff: N and T both represent a number of features, the final embedding size is NxTxD, its unclear what the difference between N&T is and why there are two numbers of frames.
- Line 197 describes the text decoder to take visual features and predicted tags as input while figure 2 shows the encoder to take visual features and encoded tags but no prediction. Fig2 should be improved such that the prediction is taken into account by the text decoder.
- Line 235: The Paragraph heading “Discussion” doesn't really fit, as no results are discussed but rather advantages of the pipeline are listed
- Line 260: How are the generated tags split into the pretraining and fin-tuning set?
- Table1: EndoVis18 (RSS) is listed with 997 images. The dataset consists of 19 snippets with 300 frames each, why/how was it down sampled?
- Table2: why aren't the values of P & R highlighted? Esp. for P the text references the models superiority, this should be visualized in the table.
- Why is the Fbeta with beta=0.5 instead of the more common F1 score used?
- Table3: all values in the table should be given with the same amount of decimals
- Line 417ff: Figure2 introduces the RASO architecture to include a temporal-attention fusion, but the video recognition paragraph compares the video aggregation against a frame-wise approach? How does the frame-wise method work? Which features are aggregated?
- From the video recognition paragraph an Table3c it seems that the temporal-attention fusion was not used in the experiments of Table 1 and 2, as both configuration in Table3c differ from the earlier presented results (Table 1,2,3a&b). Why was the fusion not used as presented in Fig2?
- Table 3a and 3b are similar to the bottom two rows of Table 1 and 2 respectively. No new information is presented. I recommend to reference table 1 & 2 and use the space of Tables 3a&b to further explain the image-wise aggregation or the experimental setup to clarify why  temporal-attention fusion was not used in all experiments.
- Both configurations in Table 3c outperform the results of Table 3a&b. How does the ablation pretraining and fine-tuning change when applying any of the video aggregation methods?
- The paper cites many non-peer-reviewed publication on arXiv. Check if peer-reviewed versions are available (esp lines 539 & 545)
- Some references (lines 608, 623 & 630) are missing details on the journal / publisher

### Questions
- Line 33: Two Datasets are called EndoVis17 and EndoVis18. In both years EndoVis consisted of 4 challenges releasing datasets. I propose to use the challenge names robotic instrument segmentation (RIS) & robotic scene segmentation (RSS)
- Figure 1 is not referenced in the text.
- Every paragraph cites methods or models when firstly used, even if previously already used
- Line 184ff: N and T both represent a number of features, the final embedding size is NxTxD, its unclear what the difference between N&T is and why there are two numbers of frames.
- Line 197 describes the text decoder to take visual features and predicted tags as input while figure 2 shows the encoder to take visual features and encoded tags but no prediction. Fig2 should be improved such that the prediction is taken into account by the text decoder.
- Line 235: The Paragraph heading “Discussion” doesn't really fit, as no results are discussed but rather advantages of the pipeline are listed
- Line 260: How are the generated tags split into the pretraining and fin-tuning set?
- Table1: EndoVis18 (RSS) is listed with 997 images. The dataset consists of 19 snippets with 300 frames each, why/how was it down sampled?
- Table2: why aren't the values of P & R highlighted? Esp. for P the text references the models superiority, this should be visualized in the table.
- Why is the Fbeta with beta=0.5 instead of the more common F1 score used?
- Table3: all values in the table should be given with the same amount of decimals
- Line 417ff: Figure2 introduces the RASO architecture to include a temporal-attention fusion, but the video recognition paragraph compares the video aggregation against a frame-wise approach? How does the frame-wise method work? Which features are aggregated?
- From the video recognition paragraph an Table3c it seems that the temporal-attention fusion was not used in the experiments of Table 1 and 2, as both configuration in Table3c differ from the earlier presented results (Table 1,2,3a&b). Why was the fusion not used as presented in Fig2?
- Table 3a and 3b are similar to the bottom two rows of Table 1 and 2 respectively. No new information is presented. I recommend to reference table 1 & 2 and use the space of Tables 3a&b to further explain the image-wise aggregation or the experimental setup to clarify why  temporal-attention fusion was not used in all experiments.
- Both configurations in Table 3c outperform the results of Table 3a&b. How does the ablation pretraining and fine-tuning change when applying any of the video aggregation methods?
- The paper cites many non-peer-reviewed publication on arXiv. Check if peer-reviewed versions are available (esp lines 539 & 545)
- Some references (lines 608, 623 & 630) are missing details on the journal / publisher

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
The paper’s contributions include:

(1)RASO Model: A novel open-set recognition model tailored for recognizing diverse surgical objects in images and videos, incorporating temporal-attention fusion for video context. 

(2)Weakly-supervised Learning Framework: An efficient framework leveraging unannotated data, significantly reducing annotation reliance and supporting domains with limited annotated data.

(3)Data Generation Pipeline: A scalable, weakly-supervised pipeline that generates extensive tag-image-text data from over 2,200 surgical procedures, producing comprehensive surgical annotations.

(4)Experimental Results: RASO demonstrates substantial mAP improvements in zero-shot and supervised settings, outperforming current state-of-the-art models in surgical action recognition.

### Strengths
(1)The development of RASO introduces an attention-based temporal-fusion mechanism specifically for surgical videos, where temporal information is essential but often neglected in frame-based models. Additionally, the weakly-supervised learning framework and data generation pipeline are highly creative solutions to the prevalent problem of data scarcity, enabling the model to learn from unannotated surgical videos at scale.

(2)Extensive testing on four benchmark datasets, both in zero-shot and supervised settings, provides strong evidence of the model's effectiveness. 

(3)The article is well-structured, the motivation is clear, and the technical explanations are easy to understand

### Weaknesses
(1)The model heavily depends on a weakly-supervised dataset generated from surgical lecture videos, which, despite its scale, may introduce considerable noise due to the lack of domain-specific annotation quality control. The captions, while providing some context, are not guaranteed to accurately reflect the visual content of each frame, potentially leading to misalignments between the text and the surgical actions or objects present. A more detailed analysis of the caption quality and its correlation with the visual data is needed. Specifically, the distribution of entity keywords (tools or actions, etc.) in the captions should be analyzed to understand the dataset's biases and limitations, which could reveal if certain actions or tools are over or underrepresented, affecting the model's generalization capabilities.

(2)While the temporal-attention fusion layer is a key innovation intended to enhance video-based recognition, the paper lacks a rigorous justification for why this layer outperforms simpler alternatives, such as average pooling or recurrent networks. The paper should include a more detailed ablation study that compares the performance of the temporal-attention fusion layer with these alternatives across different surgical action recognition tasks, and also explore the impact of different attention mechanisms (e.g., self-attention, cross-attention) to understand the specific benefits of the chosen approach. Furthermore, the computational cost of the attention mechanism should be discussed, as it may be a limiting factor for real-time applications.

(3)This architecture includes a label decoder and a text decoder, where the text decoder aligns the visual content with the transcript during training. However, is there potential redundancy between the label decoder and text decoder modules? The paper should investigate the necessity of both decoders through an ablation study, evaluating the model's performance with only one decoder or with different combinations of decoders. This would help determine if both decoders are essential for the model's performance or if one is sufficient, potentially simplifying the architecture and reducing computational overhead.

### Questions
I'd like to ask how the frames were extracted. Were they keyframes, sampled at regular intervals, or something else?

### Soundness
3

### Presentation
3

### Contribution
2
