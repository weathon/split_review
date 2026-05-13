# Masked Temporal Interpolation Diffusion for Procedure Planning in Instructional Videos

- Decision: Accept
- Scores: 6, 8, 6

## Abstract
In this paper, we study the problem of procedure planning in instructional videos, which involves making goal-directed plans based on current visual observations in unstructured, real-life videos. Prior research leverages different forms of supervision to bridge the gap between observed states and unobserved actions. Building on this foundation, we propose an innovative approach by introducing a latent space temporal logical interpolation module within the diffusion model framework. This module enables the intermediate supervision of temporal logical relationships that were previously nonexistent. In terms of details, we employ an interpolator to guide the intermediate process within the diffusion model, using the start and end observation features as inputs. This involves extracting latent features through an encoder and applying an interpolation strategy with transformer encoder blocks to derive the latent features. Furthermore, to ensure the accuracy of actions in the outputs, we implement a masking strategy to constrain the scope of predictions and a task-adaptive masked proximity loss for the training process. Results across these three datasets of varying scales demonstrate that our MTID model achieves state-of-the-art performance on the overwhelming majority of key metrics. The code is available at https://anonymous.4open.science/r/MTID-E2E3/README.md.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposed a diffusion-based method, i.e. Masked Temporal Interpolation Diffusion (MTID) model for procedure planning. The diffusion model part is based on PDPP which takes the start and goal visual feature, action sequence and task class as input. The author proposed a Latent Space Temporal Logical Interpolation Module to generate the intermediate visual features given the start and goal visual features. Additionally, the authors proposed a masked projection and a task-adaptive masked proximity loss. the masked projection excludes the actions that do not belong to the tasks. The task-adaptive masked proximity loss puts more weight on the actions closer to the start and end actions and puts more penalties on the excluded actions. The experiments were performed on Crosstask, Coin, and NIV datasets, and SOTA results were achieved on most metrics of Crosstask and Coin datasets.

### Strengths
- This paper addresses the limitation of the previous diffusion model approach, i.e. the temporal dependencies of actions, by using generated intermediate visual supervision.
- The Latent Space Temporal Logical Interpolation Module seems to be helpful as the intermediate visual supervision.
- The task-adaptive masked proximity loss seems to contribute to the increase of performance.

### Weaknesses
 - The Latent Space Temporal Logical Interpolation module does not have anything to do with 'logic'. It only has temporal dependencies between actions. Linear interpolation between start and goal visual observations with weights is not logic. The term 'logical' implies the use of formal logic or reasoning, which is not present in the proposed interpolation method. The module simply generates intermediate features based on temporal proximity, lacking any logical inference capabilities.

 - The experiment setting needs to be specified clearly in the main manuscript. The results on Coin and NIV datasets are misleading. This paper follows the setting of PDPP, however the results of baseline models (KEPP, SCHEMA) follow a different experiment setting. This needs to be clarified. Furthermore, the NIV dataset misses the results of PDPP, the proposed method does not outperform PDPP on all metrics for both time horizons. The lack of consistent experimental settings makes it difficult to compare the proposed method fairly with existing approaches. Specifically, the use of different window sizes for defining states in PDPP versus KEPP introduces a significant confounding factor.

 - Although the proposed ideas are interesting, it is not clear how the Latent Space Temporal Logical Interpolation module and the task-adaptive masked proximity loss contribute to the improvement on performance as they are built on top of PDPP. It will be beneficial to see the ablation studies of different combinations of model components on all datasets, i.e. diffusion + Latent Space Temporal Logical Interpolation, diffusion + masked project + task-adaptive masked proximity loss. The absence of detailed ablation studies makes it difficult to isolate the contribution of each component. For example, it is unclear whether the performance gains are primarily due to the interpolation module, the masked projection, or the task-adaptive loss, or a combination thereof.

 - The presentation of the work has ambiguities and needs to be clarified. For details see comments below.

### Questions
In the paragraph starting from line 81, the authors need to clarify which parts in MTID are from PDPP (e.g. using predicted task class in the input matrix for the diffusion model, mask intermediate visual features, etc.)

- In equation 1, why introduce M? v1:M should just be v2:T-1, i.e. the number of intermediate steps.

- The notations for actions are inconsistent. Sometimes \hat{a_t} is the ground truth action, sometimes \bar{a_t} is (e.g. Eq 10), and sometimes a_t is (e.g. Figure 2). Please make them consistent throughout the full text.

- The caption of Figure 2 needs to be elaborated. And the part to exclude actions that do not belong to a class is not shown. The fonts are too small to read.

- The caption of Figure 3 needs to be elaborated. The fonts are too small to read.

- Line 316, PDPP weights both start and end actions.

- Put What does the dagger symbol mean in the caption of Table 1 too.

- Line 359, Crosstask has 105 action classes.

- Merge Table 13 in the appendix to Table 3 in the main manuscript to show results on all metrics on Coin and NIV.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces the Masked Temporal Interpolation Diffusion model to improve procedure planning in instructional videos. MTID integrates a latent space temporal logical interpolation module into a diffusion framework, generating richer visual supervision for intermediate states. The model is evaluated across benchmarking datasets and has been shown to achieve promising results.

### Strengths
The proposed MTID model is a novel application of diffusion models for procedural planning, introducing an innovative interpolation mechanism to enrich visual supervision, which is rarely addressed in the field.

The paper provides strong experimental evidence demonstrating that MTID outperforms existing models on multiple benchmark datasets. The results on CrossTask, COIN, and NIV datasets suggest significant improvements in most evaluation metrics. Plus the ablation studies are detailed and informative.

### Weaknesses
The model's architecture, especially the use of latent space interpolation combined with diffusion processes, may be difficult for readers to grasp fully. More intuitive visualizations or a simplified explanation could aid in better understanding.

The classification results in NIV datasets seems to be way better than that of the COIN dataset. However, as shown in Table 3, the procedure planning results in terms of success rate and mAcc do not show then same trend. It seems like your model perform slightly better or generally the same on COIN rather than on NIV. How can you explain this discrepancy?

### Questions
Does the task-adaptive masked proximity loss sufficiently balance intermediate state supervision with endpoint accuracy, or are there alternative loss functions that could enhance performance?

The classification results in NIV datasets seems to be way better than that of the COIN dataset. However, as shown in Table 3, the procedure planning results in terms of success rate and mAcc do not show then same trend. It seems like your model perform slightly better or generally the same on COIN rather than on NIV. How can you explain this discrepancy?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposes a Masked Temporal Interpolation Diffusion model to tackle the problem of procedure planning in instructional videos, including a latent space temporal logical interpolation module. The interpolated mid-state visual feature is used to guide the intermediate process within the diffusion model. The MTID achieves SOTA performance on several datasets.

### Strengths
1. Based on previous works, this paper additionally uses the interpolated mid-state latent visual feature to supervise the model.
2. The proposed MTID model achieves SOTA performance on several datasets.

### Weaknesses
1. The core concept is using the interpolated visual feature to provide visual-level mid-state supervision. However, the motivation of this operation is unclear. Using linear interpolation to interpolate the mid-state visual feature based on the start and goal visual feature is challenging. Additionally, an experiment that directly uses the visual features of mid-state for supervision (like previous works DDN) should be added, which can be seen as an upper bound.   
2. In this paper, the task classifier uses a transformer, howerer,  in previous papers (EGPP, PDPP), a MLP is enough for this simple classification task.
3. The masked projection introduces too much prior (i.e., the action space of each task).
4. More analysis should be provided about the Task-Adaptive Masked Proximity Loss ablation, (MSE+GW achieves 15.1, while MSE+W+GW+M achieves 15.26). What's the weighted gradient loss, the authors should give more detail in the Method part. 
5. The novelty of the proposed method is limited compared with previous work PDPP.

### Questions
Refer to the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2
