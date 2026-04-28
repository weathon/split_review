# RelCon: Relative Contrastive Learning for a Motion Foundation Model for Wearable Data

- Decision: Accept
- Avg Score: 6.75
- Scores: 8, 5, 8, 6

## Abstract
We present RelCon, a novel self-supervised \textit{Rel}ative \textit{Con}trastive learning approach that uses a learnable distance measure in combination with a softened contrastive loss for training an motion foundation model from wearable sensors. The learnable distance measure captures motif similarity and domain-specific semantic information such as rotation invariance. The learned distance provides a measurement of semantic similarity between a pair of accelerometer time-series segments, which is used to measure the distance between an anchor and various other sampled candidate segments. The self-supervised model is trained on 1 billion segments from  87,376 participants from a large wearables dataset. The model achieves strong performance across multiple downstream tasks, encompassing both classification and regression. To our knowledge, we are the first to show the generalizability of a self-supervised learning model with motion data from wearables across distinct evaluation tasks.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents RelCon, a contrastive learning approach that leverages relative similarity between different accel signal segments (motifs) as a softened discriminative loss in contrastive learning. Authors use the proposed contrastive learning setup to pre-train a 1-D ResNet-34 backbone on 2.56 s long 100 Hz accel signal segments. The resulting pre-trained model generated a 256-dimensional embedding representing the accel signal segment. This pre-trained model was kept frozen and a linear layer was trained for downstream tasks, such as activity classification and gait metrics regression. 

Authors show the effectiveness of their method via rigorous comparisons with SSL works (REBAR, AugPred, SimCLR) as well as supervised training approaches on the downstream classification tasks.

### Strengths
* The paper is very well-written. The authors clearly explain their approach, what parts are similar to the past work, and where they have improved over the past work. 

* This paper has strong empirical results. I think, the approach is most similar to REBAR (which used motif-based similarity in contrastive loss) and AugPred (which pre-trained another accel-based foundation model). However, authors show that RelCon achieves much better empirical results compared to both REBAR and AugPred.

### Weaknesses
I think, the only weakness of the proposed method is that it can be seen as a somewhat straightforward extension of REBAR by i) using the relative distance as a soft metric instead of hard similarity labels, and ii) a few additional enhancements that were also proposed independently by others earlier (sec 3.1). However, authors clearly quantify the benefits of RelCon over earlier works via rigorous empirical evaluations where it outperforms AugPred, SimCLR, and REBAR in most cases.

### Questions
* Why is REBAR not included as a baseline in Table 4?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The current paper presents a foundation model for acceleration data on wrist wearables applied to human activity recognition. In this case, focus on the classification of a broad set of human activities (e.g, walking, stair-climbing, swimming,..).
The main contribution is an approach to include augmented data for enhancing the learning of similar samples systematically distorted. And a new formulation for a relative contrastive loss that encodes relative order relationships into the standard cross entropy loss.
The results of the foundational model proposed trained on 1 Billion segments of data of wrist acceleration (equivalent to 82 years of data from 87k participants).

### Strengths
1. A foundational model trained on a large data sample over 82 years of data from 87k participants
2. An interesting approach for training through self-supervised learning data augmentation.
3. Introducing a loss function (relative contrastive loss) that accounts for augmented points distance to the anchor for improving training, thus making it resistant to false positives.
4. Comparative analysis with similar approaches
5. Performance proved on the classification of motion tasks as well as regression of 2 metrics in walking.

### Weaknesses
1. The learning approach is only tested on only 2 datasets of a single sensor, thus the idea of an acceleration foundational model is not proven as a generalization is still questionable. Others such as: PAMAP2, USC-HAD, MHealth. 
2. One suggestion would be to evaluate other acceleration-based HAR with multiple signals in benchmarks of HAR that go beyond single sensor-based. 
3. Improvements to previous work seem marginal +0.01 AUC and 2.17 F1-score improvement for classification tasks on the AHMS dataset. 
*3. It would be ideal to conduct statistical significance tests on these improvements and discuss the practical implications of these improvements. Also, please highlight the meaning of your improvement in some specific classes (does it improve greatly in one class?). Rather than relying only on F1 scores.
4. Results comparing to wrist acceleration models across the literature were limited to SimCLR and REBAR. And the analysis compared to supervised learning was minimally addressed. 
*4 * I would recommend comparing the performance in some of the SOTA best-trained models for activity classification: e.g, F1-scores on PAMAP2 0.86 (Essa & Abdelmaksoud, 2023), MHealth: 0.94(Suh et al., 2023), 0.83 USC-HAD (Essa & Abdelmaksoud, 2023), and so.

### Questions
1. What is your definition of a Motif,?
2. How could it be proven in this work that distance measures actually reflect similarities in motifs?
3. Why is the title "motion Foundation Model for wearable data" → your current work although extensive data was trained comprises "Wrist acceleration data" not any other modality even from IMU, thus it reads incorrectly.	(2,56 s segments of 100 Hz x,y,z accelerations) 
4. In Figure 1 is there strict proof of all the characteristics listed here? I would like to see each of them analyzed more clearly in the conclusions.
5. What is the size of the dataset and classes used for evaluation on HHAR, and PAMAP2?
6. What is the distribution of data on each of these datasets? Balance on classes?
Is PAMAP2 wrist or ankle data used? There is a discrepancy between Table 3 and the description in the text.
7. What is the inference time, and computational complexity of the proposed approach RelCon? Is there any advantage over REBAR or SimCLR?
8.1 On Fig. 2, why is it concluded that the representation is clearer? I fail to see a difference compared with REBAR.
8.2. On the t-SNE, what perplexity was used? Are the results consistent at all levels?

### Soundness
2

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
4

### Summary
This paper presents a relative contrastive learning framework with motion time series data from wearables. Contrastive learning is a common technique for developing pre-trained models for motion time series data. A major component of contrastive learning for motion time series is to construct pair and negative pairs of samples to obtain some representation, which isn’t trivial for motion time series. 

The main challenge is the difficulty of generating augmented views of the same time series segment without introducing artifacts. This paper builds upon an existing contrastive framework that makes use of the fact that many short segments of human activities are repeated in nature which can be used as positive pairs e.g. repeated walking, hand-shaking behaviors. The paper improved on a learnable distance metric used to select the positive pairs and introduced a soft contrastive loss so that not all the negative pairs are considered the same.

The experiments presented showed competitive performance against other pre-trained models and other self-supervised methods.

### Strengths
1. This paper nicely incorporated characterises of motion time series into the design of the contrastive learning framework which is commendable. 
2. The empirical performance is promising.
3. A wide range of benchmarks are included

### Weaknesses
1. Neither the code nor the model is open source, preventing future reuse. I believe at least pseudo code should be provided somewhere. 
2. The Apple Heart and Movement Study used to retrain the model was collected using consumer-grade devices in a free-living environment. Often, data coming from consumer-grade devices have limited data quality, including noise and missing data. More descriptives on the study participants, data processing pipeline, and an exploratory analysis of the IMU data will help to understand what data goes into pre-training.
3. I believe the results shown in Table 3 when comparing the proposed model and another pre-trained model is biased for several reasons. The benchmark datasets used Opportunity and PAMAP2 are small, it is very easy to overfit ofthese two datasets. The authors are quoting performance in the high 90 of their proposed model which is a sign of overfitting already. Can the authors at least share their code during the review process so that we know how the evaluation was implemented?
4. Another reason the benchmark is overfitted (Table 3) is that the metric difference between a pre-trained model and a non-pre-trained model is a mere 5%. Whereas the performance difference for Yuan et al is about 10%+. Furthermore, Yuan et al, 2024 was pre-trained on the UKB which is 10x the size of the Apple Heart & Movement Study, it is hard to believe the reported performance from this work is about 100% better in some cases.

### Questions
1. In text citations have not be been correctly phrased throughout the manuscript
2. The selection of 2.56 second as the window length requires justification. If the proposed work were to be a foundation model, it should be designed to cater for common window lengths used 1s, 5s, 10s etc.
3. Can you share your code at least during the review process as again there are questions around your evaluation procedure which is likely due to overfitting?
4. How are your workout labels obtained, self-reported or via some objective alternative modality?
5. What are the population characteristics of the pre-training population?
6. How did you process your IMU data, filtering, downsampling, non-wear detection? 
7. In table 3, can you include a statement to indicate the results from Yuan et al are quoted as you didn't implement their evaluations to avoid confusion.

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
5

### Summary
This paper introduces a self-supervised learning approach, RelCon, that uses a relative contrastive learning method to train a motion foundation model for wearable sensor data. The model is pretrained on a large-scale dataset AHMS comprising 1B accelerometer segments from over 87,000 participants. RelCon integrates a learnable distance measure and a softened contrastive loss, which enables the proposed model to capture motif similarity and domain-specific semantic information. The evaluation demonstrates good performance of the proposed method across multiple downstream tasks, including gait metric regression and human activity recognition, compared to existing state-of-the-art approaches.

### Strengths
+ This paper presents an extensive dataset for pretraining the model. The dataset scale is substantial, and training on over a billion segments could significantly contribute to wearable motion data analysis.
+ The proposed SSL approach with a learnable distance measure and softened contrastive loss is interesting and looks novel.

### Weaknesses
 - The authors compared their ReCon foundation model trained on their AHMS dataset using ResNet-34 with Yuan et al. (2024) trained on UkBioBank Dataset using ResNet-18. Even though they argued that ResNet-34 is "smaller and deeper" and performs better than ResNet-18, this is not a fair comparison to show the superiority of their AHMS dataset and method. A fair evaluation should employ the same architecture (e.g., ResNet-18 for both methods) to isolate the effect of the SSL method, rather than introducing variability due to architecture differences. Specifically, the claim that ResNet-34 is 'smaller' is misleading, as it has a higher parameter count and computational cost, making it a more powerful model. This difference in model capacity could be a confounding factor in the comparison, potentially inflating the performance of the proposed method.
- The authors do not conduct an adequate benchmarking study on an established dataset for SSL in accelerometer data. For instance, they could evaluate their method by pretraining on the AHMS and Capture-24 datasets, allowing for a more consistent comparison to other SSL methods. The absence of a direct comparison on a common dataset makes it difficult to assess the true contribution of the proposed method relative to existing self-supervised learning techniques. Furthermore, the lack of evaluation on a standardized benchmark limits the generalizability of the findings and makes it difficult for other researchers to reproduce and build upon this work.

### Questions
- Please provide a fair comparison evaluation with Yuan et al. (2024) using the same network architecture.
- Is it possible to evaluate the proposed SSL method with other SSL approaches pretraining on the same dataset like Capture-24?

### Soundness
3

### Presentation
3

### Contribution
3
