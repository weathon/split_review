# Temporal Source Recovery for Time-Series Source-Free Unsupervised Domain Adaptation

- Decision: Reject
- Avg Score: 4.67
- Scores: 6, 3, 5

## Abstract
Source-Free Unsupervised Domain Adaptation (SFUDA) has gained popularity for its ability to adapt pretrained models to target domains without accessing source domains, ensuring source data privacy. While SFUDA is well-developed in visual tasks, its application to Time-Series SFUDA (TS-SFUDA) remains limited due to the challenge of transferring crucial temporal dependencies across domains. Although a few researchers begin to explore this area, they rely on specific source domain designs, which are impractical as source data owners cannot be expected to follow particular pretraining protocols. To solve this, we propose Temporal Source Recovery (TemSR), a framework that transfers temporal dependencies for effective TS-SFUDA without requiring source-specific designs. TemSR features a recovery process that leverages masking, recovery, and optimization to generate a source-like distribution with recovered source temporal dependencies. To ensure effective recovery, we further design segment-based regularization to restore local dependencies and anchor-based recovery diversity maximization to enhance the diversity of the source-like distribution. The source-like distribution is then adapted to the target domain using traditional UDA techniques. Extensive experiments across multiple TS tasks demonstrate the effectiveness of TemSR, even surpassing existing TS-SFUDA method that requires source domain designs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses the time-series source-free domain adaptation problem. It proposes a source recovery method that recovers target data to a source-like distribution and introduces anchor-based recovery diversity maximization to enhance the diversity of the source-like distribution.

### Strengths
1. The overall idea of source distribution recovery is reasonable.
2. The method section is detailed and clearly presented.

### Weaknesses
1. The ablation study could be more comprehensive, as there are additional specific designs with intuitive explanations mentioned in the method section beyond the three variants in Table 4, such as the consistent segment entropy loss and different components in the ARDM loss.
2. The two key requirements stated at the beginning of Section 3.3 are intuitive. More explanation or support from the literature would be beneficial.

### Questions
In Section 4.5, could the authors explain why minimizing the domain discrepancy between the source-like and target domains is required for domain adaptation? This point does not appear to be discussed in previous sections.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
In this paper, the authors present a temporal source recovery (TemSR) framework for source-free unsupervised domain adaptation. Specifically, a source-like distribution is generated with the source temporal dependencies recovered. A segment-based regularization and an anchor-based recovery diversity maximization are developed to enhance the source recovery. Experiments on three datasets are done to verify the proposed TemSR.

### Strengths
1. The paper proposes to deal with a practical and meaningful adaptation scenario, that is source-free unsupervised domain adaptation.
2. The paper presents a temporal source recovery (TemSR) framework for source-free unsupervised domain adaptation.
3. The paper conduct experiments on three practical datasets, and demonstrate the effectiveness of the proposed TemSR  compared with given baselines.

### Weaknesses
 1. One of my major concerns of the work is on the technical novelty. Using mask and then recovery has been shown the adaptation and transfer capability in generation tasks, e.g., masked autoencoder and videoMAE. The application of such an idea to source-free UDA setting makes the technical significance limited although it may not be explicitly done before.
 2. The paper misses some important video-based UDA related works. Video is a popular time-series data, and there are quite a lot of video-based UDA research. The reviewer suggests the authors to discuss them in related work section. 
 3. For time-series data as stated in the setting with N channels and L time points, existing UDA works usually handle both the spatial and temporal divergence, e.g., [ref1,2]. However, the paper seems to overlook the spatial divergence and only focus on the temporal one.
 4. The experimental studies are not very convincing. The author may refer to my detailed comments on the below questions.

### Questions
1. Figure 2 is not very informative. It is inadequate to use two ellipses to represent complex temporal and spatial divergence across TS data. Moreover, what does “target distribution” mean here? Are you trying to explain why using masked target data? 
2. Regarding the recovery component, is a reconstruction loss included? Or using a pretrained reconstruction model as backbone? If not, is it better to initialize the recovery model by a reconstruction model pretrained on the target unsupervised data? 
3. Regarding the segment regularization line 248-250, low entropy difference between segments does not indicate the smooth dependencies among segments. The authors may need to present ablation studies on this term (Eq. (2)) to show its effectiveness. Moreover, what does {C,E,L,R} mean? As in Eq. (2), (k, s) belongs to {C,E,L,R}, is it trying to minimize the entropy difference between arbitrary segment pairs? 
4. Can you elaborate more on the test flow? Are you using the pretrained source classifier for final prediction?
5. Regarding the experiments parts: (1) more complex video benchmark datasets are encouraged to be tested; (2) why using the same CNN backbone? For different tasks, different backbones should be used. For instance, for action recognition tasks, there are more advanced backbones, e.g., I3D, videomae; (3) Model details should be presented in the main contents. Please elaborate more on the recovery model as it is the main contribution. Are you using LSTM or Bi-LSTM? Why not considering Transformer structure? (4) The results are not very convincing to show the performance superiority of TemSR as TemSR is the winner in 2 of 5, 1 of 5, and 3 of 5 tasks in the three datasets. (5) Sensitivity analysis shows that the optimal hyper-parameter value varies across tasks. It is not convincing to conclude the best value range is 1 to 10 by only using 3 datasets. The hyper-parameter generalization ability of the proposed TemSR is also an issue when facing new tasks or datasets. Moreover, what is “EEG” in figures 4,5,6?

[ref1] Contrast and mix: Temporal contrastive video domain adaptation with background mixing

[ref2] Unsupervised video domain adaptation for action recognition: A disentanglement perspective

### Soundness
2

### Presentation
3

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
The paper a noval framework, TemSR, for Time-Series Source-Free Unsupervised Domain Adaptation (TS-SFUDA), designed to recover and transfer temporal dependencies without access to source data. TemSR employs a masking, recovery, and optimization process to generate a source-like distribution with restored temporal dependencies. To improve the recovery process, segment-based regularization is introduced to capture local dependencies and maximize anchor-based recovery diversity to ensure diversity in the recovered distribution. Extensive experiments across various time-series tasks demonstrate the effectiveness of TemSR, surpassing existing methods that rely on source-specific pretraining designs while maintaining source data privacy.

### Strengths
1. The proposed task ensures source data privacy by performing domain adaptation without needing the source data.
2. The paper is logically structured, with a smooth connection between the motivation and the proposed method. Mathematical proofs are provided.
3. The introduction of the anchor-based recovery diversity maximization helps generate more diverse and realistic source-like distributions, improving adaptation performance.
4. 3 Benchmark datasets have been applied for evaluations.

### Weaknesses
1. The notation in Figure 1 is inconsistent with the notation in the text. Specifically, is the **L_sse** in Figure 1 the same as **L_seg** mentioned in line 259?
2. The non-source-free baseline models used are outdated, with CoDATS being published four years ago. It would be beneficial to include more recent baseline models from 2023, such as CLUDA ("Contrastive Learning in Unsupervised Domain Adaptation for Semantic Segmentation", Neurips 2023) and RainCoat ("Domain Adaptation for Time Series Under Feature and Label Shifts", ICML 2023).
3. Although using three benchmark datasets is sufficient, most previous MTS-UDA tasks typically select 7-10 source-target pairs (as the source-pair combination for HAR and SSC datasets can be hundreds) and report the average and standard deviation for comparisons, which provides a more balanced and fair evaluation. Moreover, the standard deviation across all pairs can demonstrate the model's robustness by highlighting its performance consistency across different cases. Having only five pairs per dataset is insufficient for a fair comparison.

### Questions
Methodologies:
1. In Section 3.3 on Recovery-initialization, could you further explain which parts are initialized in Figure.1 framework? Furthermore, could you provide further clarification on why initializing with the target distribution satisfies the first requirement:  "The initialized distribution should be close to the source distribution; otherwise, obtaining an effective source-like distribution is difficult". If possible, could you add an ablation study by initializing randomly? Could you further explain why GAN does not meet the two requirement?
2. Targeting to the "masking", as there is no "dimension related" information provided, could you give more details on the masking strategy? Will the masked parts be replaced with 0 or some noise? Or, you apply a similar masking strategy as MAE (Masked Autoencoders Are Scalable Vision Learners)?

Experiments:
1. In Section 4.1 (Datasets and Settings), you state that you followed the "identical training configurations as Ragab et al. (2023b)," referring to the paper titled "Source-Free Domain Adaptation with Temporal Imputation for Time Series Data. (MAPU)" However, after reviewing both the cited paper and the appendix of your work, I noticed that the datasets were split into training and testing sets only, with no mention of a validation set. If the best model is selected based on the test dataset, this could lead to biased evaluations, which raises concerns about the fairness of the evaluation process. In addition, For reproducibility, could you please include a table in the appendix listing key hyperparameters (e.g. learning rates, batch sizes, number of epochs) for all models, including baselines, to ensure fair comparison which could be easier for reading?
2. In the L_seg, four masking positions are utilized under the assumption that they can effectively capture local dependencies. Could you conduct some ablation study experiments to demonstrate that all four types of masking positions are significant, or how does each position affects the overall performance?
3. Could you add a computational complexity analysis with the proposed model and the baseline models?

### Soundness
2

### Presentation
3

### Contribution
3
