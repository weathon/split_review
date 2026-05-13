# Debiased Deep Evidential Regression for Video Temporal Grounding

- Decision: Reject
- Scores: 5, 6, 5, 8

## Abstract
Existing Video Temporal Grounding (VTG) models perform well in accuracy but often fail to address open-world challenges posed by open-vocabulary queries and out-of-distribution (OOD) videos, which can lead to unreliable predictions. To address uncertainty, particularly with OOD data, we build a VTG baseline using Deep Evidential Regression (DER), which excels in capturing both aleatoric and epistemic uncertainty. Despite promising results, our baseline faces two key biases in multimodal tasks: (1) Modality imbalance, where uncertainty estimation is more sensitive to the visual modality than the text modality; (2) Counterintuitive uncertainty, resulting from excessive evidence suppression in regularization and uneven sample error distribution in conventional DER. To address these, we propose an RFF block for progressive modality alignment and a query reconstruction task to enhance sensitivity to text queries. Additionally, we introduce a Geom-regularizer to debias and calibrate uncertainty estimation. This marks the first extension of DER in VTG tasks. Extensive experiments demonstrate the effectiveness and robustness of our approach. Our code will be released soon.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
It presents DDM-VTG, a new model that integrates Deep Evidential Regression into Video Temporal Grounding to handle uncertainties in open-world scenarios. It addresses modality imbalance and counterintuitive uncertainty with a Reflective Flipped Fusion block and a Geom-regularizer, enhancing model robustness and effectiveness across benchmarks.

### Strengths
1. It introduces the first extension of Deep Evidential Regression (DER) to Video Temporal Grounding (VTG) tasks, aiming to address uncertainties in open-world scenarios. 
2. It proposes a Debiased DER Model (DDM-VTG) that tackles modality imbalance and counterintuitive uncertainty through a Reflective Flipped Fusion block and a Geom-regularizer, enhancing the model's sensitivity to text queries and calibrating uncertainty estimation.

### Weaknesses
1. The datasets used are not open-world.
2. The performance on the video summarization task is not advantageous enough.
3. Figure 2 shows 4 cases of the uncertainty. It is not clear how the method addresses (a)(b)(d) and how to evaluate if the methods can handle these scenarios.

### Questions
1. Since the datasets have annotations like a matched moment and text, how to evaluate the model's ability to learn uncertainty when processing an unreasonable text query? Like the example in Figure 1
2. In Geom-regularization, how to define accurate predictions? how to define less accurate predictions?

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
3

### Summary
The paper presents a novel approach to Video Temporal Grounding (VTG) by integrating Deep Evidential Regression (DER) to address uncertainties in open-world scenarios, such as out-of-distribution (OOD) data and open-vocabulary queries. The authors propose a Debiased DER Model for Video Temporal Grounding (DDM-VTG) that tackles modality imbalance and counterintuitive uncertainty through a Reflective Flipped Fusion (RFF) block, a query reconstruction task, and a Geom-regularizer. The model demonstrates effectiveness and robustness across multiple benchmarks.

### Strengths
1.	The proposed baseline model is innovative for its integration of Deep Evidential Regression (DER) with VTG tasks to address both aleatoric and epistemic uncertainties. 
2.	The paper not only identifies the existence of modal imbalance and structural flaws in regularization within the baseline model but also offers solutions to these issues.
3.	The authors have conducted extensive experiments across various benchmarks, which effectively demonstrate the efficacy of their approach.

### Weaknesses
1.	While the paper presents a novel approach to addressing uncertainties in VTG, it could benefit from a deeper analysis of the limitations of the proposed model, especially in handling highly ambiguous queries or extremely OOD data. Specifically, the paper lacks a discussion on how the model's uncertainty estimates behave when faced with queries that have multiple plausible temporal locations or when the input video content is significantly different from the training distribution. The paper should include an analysis of the model's performance on such challenging cases and how the uncertainty quantification reflects these difficulties.
2.	The paper could provide more insights into how the DDM-VTG model generalizes to other video-related tasks beyond the tested benchmarks. While the current benchmarks demonstrate the model's effectiveness in temporal grounding, it is unclear whether the proposed approach can be readily applied to tasks such as video action recognition or video captioning, which also involve temporal reasoning and uncertainty. The authors should discuss the potential challenges and modifications needed to extend the model to these tasks.
3.	When designing the baseline, whether DER provides positive assistance for the correct prediction of the model, the author needs to provide corresponding proof experiments. It is not clear if the inclusion of DER is actually beneficial to the model's predictive performance or if it is primarily serving to quantify uncertainty. The authors should provide ablation studies that compare the performance of the model with and without DER to demonstrate its contribution to the overall accuracy.
4.	When introducing the baseline, the author believes that it has a modal imbalance problem, and DDM-VTG effectively alleviates this imbalance, which requires corresponding experimental evidence. The paper needs to provide quantitative evidence, such as variance of the feature representations for each modality, to support the claim that the baseline model suffers from modality imbalance and that DDM-VTG effectively reduces this imbalance. Without such evidence, the claim remains unsubstantiated.
5.	The method proposed by the author showed out of distribution predictions on the qv height dataset, which to some extent indicates the generalization of DDM-VTG, but it is not clear and specific enough. The author needs to provide results on charades-CD. The paper should include a more comprehensive evaluation of the model's OOD generalization capabilities by testing it on additional datasets that have a significant domain shift from the training data. The current evaluation on the qv height dataset is not sufficient to fully demonstrate the model's robustness.

### Questions
Please see the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes Debiased DER Model for VTG, tackling open-vocabulary queries and out-of-distribution videos in video temporal grounding tasks. It extends the vanilla DER to VTG and establishes a baseline. To address two critical biases in the baseline—modality imbalance and counterintuitive uncertainty—the method incorporates a RFF block for progressively enhancing modal alignment, a query reconstruction task to ensure robust cross-modal alignment capabilities and a Geom-regularizer to calibrate uncertainty estimation. The proposed method has been evaluated on 4 datasets, demonstrating its effectiveness in Moment Retrieval, Highlight Detection and Video Summarization. The ablation studies also support the analysis.

### Strengths
- The basic idea is easy to follow and the main motivation is clear.
- The innovative integration of DER into VTG tasks is a novel approach that effectively addresses key issues like OOD videos.
- The proposed method achieves strong experiment results, both compared to its baseline and other SOTA methods.

### Weaknesses
 - In figure3, I can’t see the difference between the two distributions except for the color, which might be confusing as to why one is unreliable and the other is trustworthy.
- About the presentation. In 4.3, there is a significant disparity in the level of detail explained for different modules, perhaps the arrangement of content in the main text and appendix could be adjusted to make it clearer for readers.
- The experimental section only shows the comparison with SOTA methods on various metrics. In the appendix, only some cases of the QVHighlights dataset are shown, without visual results for the other datasets mentioned in the paper, and it also lacks displays of comparative results for the three sub-tasks. 
- It would be more complete to have a discussion of this increased cost if there are any, as well as techniques used to overcome it.
- (Minor) Minor typos/grammatical mistakes (e.g. 4.2 “VALLINA”)

### Questions
- In Figure 2, several challenges within VTG tasks are highlighted, but it appears that targeted comparative experiments were not conducted in the study. When compared with other works, can DDM-VTG perform better in addressing these challenges? Some discussions are expected.
- In the Query Reconstruction task, how can DDM-VTG ensure that the tokens predicted by the QR head are accurate when dealing with complex videos? What happens if the predictions are incorrect? Does it affect the accuracy of temporal localization of the whole video?
- In the case study, the average length of the videos is 150 seconds. How would the model perform with longer videos, and would the cost increase significantly?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper studies the issue of open-world challenges caused by open-vocabulary queries and out-of-distribution videos in video temporal grounding. The authors adopt the Deep Evidential Regression as baseline, and propose a Reflective Flipped Fusion block to realize modality alignment and query reconstruction. Meanwhile, a Geom-regularizer is proposed to debias and calibrate uncertainty estimation. Extensive experiments are conducted on the public dataset to validate the proposed method.

### Strengths
1. This paper extends the deep evidential regression to video temporal grounding for uncertainty estimation.
2. The authors propose a Geom-regularizer to solve the counterintuitive uncertainty and calibrate the estimation of uncertainty. 
3. The proposed method achieves comparable performance in the majority of benchmarks.

### Weaknesses
1. The evaluation of location bias is insufficient. There are no transfer experiments on the Charades-CD and ActivityNet-CD datasets to validate the model in OOD scenarios, as done by MomentDETR and MomentDiff. The absence of these experiments makes it difficult to assess the model's robustness to domain shifts, a critical aspect of open-world challenges. Specifically, the paper lacks analysis on how the proposed Geom-regularizer performs under distribution shift, which is crucial for uncertainty calibration in real-world scenarios.
2. The study of query reconstruction (QR) is not thorough. The authors only present performance across different QR epochs and learning rates. There is a lack of ablation studies on the impact of different masking strategies, such as masking verbs or adjectives, or varying the number of masked tokens. This limits the understanding of how different aspects of the query contribute to the model's performance and uncertainty estimation. The paper should explore the sensitivity of the model to different types of masked words and their impact on the final results.
3. Insufficient performance evaluation. Ego4D-NLQ is widely used in previous works, yet this study does not report results on this dataset. Additionally, the paper fails to compare with recent works, such as "R2-Tuning: Efficient Image-to-Video Transfer Learning for Video Temporal Grounding" from ECCV 2024. The lack of comparison with state-of-the-art methods and widely used benchmarks makes it difficult to assess the true contribution of the proposed method and its performance relative to existing approaches. The paper needs to provide a more comprehensive evaluation to establish its position in the field.

### Questions
1. Why does the model only mask and reconstruct one noun? Would masking more words help enhance text sensitivity?
2. In the conclusion, the authors claim that the model’s capabilities are limited by data quality and scale. ActivityNet-Captions and Ego4D-NLQ are large-scale datasets. Would the model perform well on these two datasets?

### Soundness
2

### Presentation
2

### Contribution
3
