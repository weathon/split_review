# LR0.FM: LOW-RESOLUTION ZERO-SHOT CLASSIFICATION BENCHMARK FOR FOUNDATION MODELS

- Decision: Accept
- Scores: 8, 6, 6, 8

## Abstract
Visual-language foundation Models (FMs) exhibit remarkable zero-shot generalization across diverse tasks, largely attributed to extensive pre-training on largescale datasets. However, their robustness on low-resolution/pixelated (LR) images, a common challenge in real-world scenarios, remains underexplored. We introduce LR0.FM, a comprehensive benchmark evaluating the impact of low resolution on the zero-shot classification performance of 10 FM(s) across 66 backbones and 15 datasets. We propose a novel metric, Weighted Aggregated Robustness, to address the limitations of existing metrics and better evaluate model performance across resolutions and datasets. Our key findings show that: (i) model size positively correlates with robustness to resolution degradation, (ii) pre-training dataset quality is more important than its size, and (iii) fine-tuned and higher resolution models are less robust against LR. Our analysis further reveals that model makes semantically reasonable predictions at LR, and the lack of fine-grained details in input adversely impacts the model’s initial layers more than the deeper layers. We use these insights and introduce a simple strategy, LRTK0, to enhance robustness of models without compromising their pre-trained weights. We demonstrate the effectiveness of LR-TK0 for robustness against lowresolution across several datasets and its generalization capability across backbones and other approaches. Code will be publicly released.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper tackles the problem of low-resolution zero-shot classification with vision-language foundation models. The authors observe that zero-shot classification accuracy drops when the resolution of input images decreases. First, they identified limitations in the existing evaluation metrics. They propose an improved relative robustness measure, which avoids misleading high scores when the model behaves closely to random predictions. Additionally, they propose weighted aggregated robustness (WAR) instead of simply averaging scores over datasets, in order to fairly reflect all the datasets. Second, they benchmark 10 foundation models (spanning 66 backbones) using 15 datasets on low-resolution zero-shot classification. Analysis on the dimensions of pretraining data and pretrained model reveals different observations: 1- Robustness to low-resolution correlates positively with pretraining data quality and model size, 2- models with higher resolution input data are less robust to low-resolution, 3- Initial layers are specifically affected when resolution changes. Finally, the authors propose generating high-resolution data using a diffusion model and learning tokens appended to frozen model weight in a teacher-student framework, where the teacher sees high resolution and the student sees both high and low resolutions. Extensive experiments and ablations show the effectiveness of the proposed framework in improving zero-shot classification accuracy, specifically in extreme low-resolution scenarios (e.g., 16x16, 32x32).

### Strengths
The paper starts with a good introduction motivating the study of low-resolution (LR) zero-shot classification from a practical angle. The contributions (benchmarking, adjusted metrics, method to improve LR image classification) are clearly conveyed. The potential viability of a solution for LR mispredictions is nicely motivated by Figure 2 in the introduction, showing that the mispredictions in LR case are still semantically decent.

The proposed improvement of the relative robustness score [1] which makes it close to 0 when the predictions are close to random predictions is sound and interesting. Moreover, the proposed weighted aggregated robustness score is well-motivated and shown to better reflect each dataset fairly. 

For the benchmarking part, the paper is rich in figures and results showing the problem (degraded LR classification) and insights about correlated factors (model size and pretraining data quality). These results being observed on a wide variety of backbones are interesting and each dimension (for example the pretraining data quality) could be investigated in a specific line of future research. Additionally, pretraining research can benefit from these observations to better account for factors that are expected to improve LR downstream performance. 

Finally, proposing a solution based on freezing model weights and appending tokens that are learned in a teacher-student framework is sound and practical. Generating data with a diffusion model to train these tokens is straightforward and shown experimentally to be effective. 

[1] Schiappa et al., Robustness Analysis on Foundational Segmentation Models. CVPRW 2024

### Weaknesses
The authors mention that low-resolution images are simulated by downsampling high-resolution images using bicubic interpolation. I'm wondering whether using "real" low-resolution images can lead to different observations in all the experimental results. Would the degradation in zero-shot classification accuracy in that case start to be significant from 64x64 or from a higher resolution? Would all the correlations with model size, pretraining dataset size and quality, resolution of pretraining images ...  be the same in this case? Same question for the proposed token learning process.

The phenomenon shown in Figure 2 is interesting: misclassified low-resolution images are still assigned reasonable semantic predictions. Only few examples are shown in this figure. How often does this happen when measured on a full dataset? Is it resulting from the downsampling of the images instead of using images directly captured at low-resolution (relating to first point)?

The LR-TK0 framework is shown in Table 2 to be effective for 16x16 and 32x32. However, for higher resolutions, the metrics (WAR and SAR) and classification accuracy are still on par or lower than the original model. Isn't this compromising the initial model for ''intermediate'' resolutions?

### Questions
I am not sure to have understood how results in Figure 7 (right) affect the choice of LR tokens position. Additionally, in Figure 15, what does the x-axis mean? For instance, does [5] mean that LR tokens are introduced starting from the 5th block?

Potential typos:
* Figure 3 (right): $f_{c1}$ $\rightarrow$ $f_{c2}$, $f_{c3}$.
* Figure 4 caption: tradational $\rightarrow$ traditional. 
* Figure 5 caption: Pertaining $\rightarrow$ pretraining.
* Line 476: Table 3 $\rightarrow$ Table 4.

.................................................................................................................................................................................................................

Post-rebuttal

.................................................................................................................................................................................................................

I would like to thank the authors for addressing my concerns. I vote with a score of 8 for the paper being the first to benchmark a variety of VLM backbones on low-resolution (LR) images, providing extensive experiments offering insights about the influence of factors like model size and pretraining data quality on the robustness to LR. The identified flaws in existing robustness score and SAR (which measures robustness of a model across datasets) are clear and the proposed solutions are sound (improved relative robustness and WAR, respectively). On the other hand, LR-TK0 as a framework for learning  tokens using pairs of HR-LR images (generated with a diffusion model) is sound and effective especially for extremely low-resolution. 
Reading other reviewers' concerns (whom i would like to thank for bringing out some points that helped removing ambiguity in figure captions and details about the proposed metrics), and the corresponding authors' replies, I believe there is no critical weakness in the paper and therefore increase my score.

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
4

### Summary
This paper has explored the zero-shot ability of the visual-langrage foundation model on low-resolution images. The first contribution is that a new robust metric is proposed, named weighted aggregated robustness, which takes into account the cues of the order of the datasets and the gap between the best and random performance on the individual dataset. With abundant experiments considering different kinds of foundation models, backbones, and datasets, the paper reveals that the model is more robust with a larger size and better training data quality. Based on these analyses, a new strategy is designed to improve the zero-shot performance of the foundation model on low-resolution images by adding low-resolution tokens. 
This research work is interesting and the paper gives abundant experiments and analyses. However, the illustration and description of the figures, the structure of the paper, and the clarity of some core concepts make the paper hard to follow.

### Strengths
1. The new robustness metric is reasonable.
2. The experiment analysis is sufficient.
3. The effectiveness of the proposed LR-TK0 is verified. 
4. The viewpoint of this paper is interesting.

### Weaknesses
1. The "misleading high robustness" of SAR is clear. The "SAR overlooks dataset" is hard to understand as: 1) What does the ordering of the model mean? 2) What is the object function to optimize the model weight? 3) From the middle subfigure of Fig 4, the difference between SAR and WAR is small. how does the figure prove the SAR overlooks datasets? 4) From the last sentence of page 5, both SAR and WAR are used. SAR is for the individual dataset and WAR is used across the datasets. Does it mean that it does matter that SAR has  "misleading high robustness" problem? 5) How to choose the hyperparameter alpha in Eq. 1?
2. The figures are hard to read as:1) Too many factors are shown with the area of the circle (Fig. 5), the length of the bar (Fig. 7), the color of the text (Fig. 3), etc. 2) The subfigures has no relation in some figure, such as Fig. 3 to Fig. 5.
3. The paper claims that 66 backbones are used. What are they?
4. The LR-TK0 technique is not clear on page 7 as 1) it lacks the introduction of LR token, 2) What's "Path generation" in Fig. 10? 3)How to compute the contrastive loss as there are three numbers in Fig. 10?
5. The experiment analyses of Table 2 and Table 3 are not clear. What's the experimental setting when the SR method is used in Table 2? It lacks a summary of Table 3.
6. Some minor typos: 1)The caption of Table 2. 2)The format of the figure references is not consistent. 3) "The naming convention ..." in Line 178 is hard to understand. 4) There's an extra period after "Problem B) SAR overlooks datasets".

### Questions
My main concern is the weakness 1 and 4 in the weaknesses part. I think it could not be clearly solved due to the page limitation. I suggest the authors choose the core and important parts, then make them clearly introduced and put them in the main body.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a benchmark LR0.FM for foundation models on LR. The authors propose the metric WAR-n to measure the robustness of foundation models. Additionally, the authors propose a method LR-TK0 to enhance performance on LR.

### Strengths
1. I believe this benchmark for LR is important.

2. Extensive benchmark experiments analyses about LR0.FM.

### Weaknesses
1. In Problem B) SAR overlooks datasets, it is unclear what Spearman Rank correlation and AX optimization are, as well as how to obtain weights through AX optimization, making it difficult to understand why WAR is proposed.

2. In Table 2, Ours has performance improvement over EVA-B/16, which should be attributed to fine-tuning using the synthetic images&LR images and it certainly improves the performance. Therefore, the experiments comparison are not fair and please explain what the appealing novelty is. Additionally, in Table 3, ours performs better than the SR method, but it is unclear what the differences are between ours and SR methods and why ours is more effective.

3. In the introduction, for "We observe that existing robustness metrics have some limitations", you should introduce what the existing metrics are.

4. In Figure 1, it's not clear what the y-axis is.

5. In section 3, in "The naming convention would represent the publicly available backbone pretrained weight names. Pre-training Sizes are indicated like CLIP-ViT H(400M), where M denotes million image-text pretraining.", "CLIP-ViT H" is not the weight names and it should be clear that M is the size of dataset.

6. In evaluation metrics, in $\gamma_n^D$, only 224 or each HR is used? May be $\gamma_n^D = 1 - \left(\frac{A_{m} - A_n^D}{A_{m}}\right), m=224,256,378...$ is better.

7. There are some wrong details. Here, only the obvious mistakes are pointed out: In figure 10, "Fire (& ice) icons represent trainable (& frozen) parameters." is not a suitable caption and there are no (a) and (b) in the figure

8. In table 5, what is the difference between Baseline row and the next below row?

9. In Grad-CAM results, it's not clear what the vanilla model is.

10. The figure caption should explain the figure content rather than the meaning of the axes. Several figures have this issue, such as Figure 13 and Figure 14.

11. In some figures, it's not needed to use arrow, like in figure 4 and figure 5.

### Questions
Please respond to the questions in the weakness.


____________________
post-rebuttal message:

The authors have promised the suggested revisions, which may facilitate the readers' understanding.

Therefore I have raised my rating from 3 to 6, accordingly.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes a low-resolution benchmark named LR0.FM and a simple training method, LR-TK0, can improve low-resolution performance. The paper measures the low-resolution performance of vision-language foundation models using LR0.FM and presents valuable findings based on performance analysis. LR-TK0 suggests adding a visual prompt to each spatial token of every layer to enhance the low-resolution performance of VL models. Experiments exhibit the effect of LR-TK0.

### Strengths
- LR0.FM benchmark includes diverse VL foundation models on various datasets. I believe the low-resolution reports on 10 foundation models across 66 backbones for 15 datasets might be helpful to a lot of researchers in VL foundation models.
- The paper includes meaningful revision on evaluation metrics, i.e., `improved relative robustness` and `weighted aggregation for resolution.` Even though these metrics are not perfect, I think raising issues on metrics and trying to solve them can provide positive guidance for the benchmark field.
- The paper provides various aspects of benchmark results in Figures 5 - 7, which are more impressive and insightful than simple ranking.

### Weaknesses
- Although I agree with the efficiency of the low-resolution benchmark, I'm not sure of the value of low-resolution performance in the vision-language model domain. Generally, images in `16x16` or `32x32` are not the main target of VL models, which limits the contribution and impacts of LR0.FM benchmark.

- There is no comparison with other benchmark results. It would be more informative if the paper provided whether the low-resolution robustness aligns with other robustness benchmarks or has a unique pattern.

- LR-TK0 is a valid way to improve low-resolution performance. But, the connection between LR0.FM and LR-TK0 is not strong. It feels like reading two related papers rather than enhancing the contribution of LR0.FM.

### Questions
- Is the low-resolution performance important for vision-language models? Do you have any practical use case on it?

- Compared to another robustness benchmark in VL models, does low-resolution robustness show a different pattern, or is it similar to others?

- Problem A and Problem B seem to be practical issues for benchmarking. But I'm not sure how significant these problems are. Could you provide a quantitative report on the significance of this problem?

- In Section 4, the description points to Figure 5 (right, (a)) and (right (b)). But, only (i) and (ii) exist in Figure 5 (right).

### Soundness
3

### Presentation
3

### Contribution
3
