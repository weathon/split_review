# Motion PointNet: Solving Dynamic Capture in Point Cloud Video Human Action

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 6, 3

## Abstract
Motion representation plays a pivotal role in understanding video data, thereby elevating the dynamic capture to the forefront of action recognition tasks based on point cloud video. Previous works mainly compute the motion information in an unguided way, e.g. aggregate the spatial variations on adjacent point cloud frames using 4D convolutions or capture a point trajectory with kinematic computation like scene flow. However, the former fails to explicitly consider motion representation in corresponding frames, and the latter's reliance on tracking point trajectories becomes impractical in real-life applications due to the potential inter-frame migration of points. In this paper, we tackle the dynamic capture in point cloud video action by formulating it as solvable partial differential equations (PDEs) in feature space. Based on this intuitive design, we propose Motion PointNet, a novel method that improves the dynamic capture in point cloud video human action by constructing clear guidance for network learning. Motion PointNet is composed of a lightweight yet effective PointNet-like encoder and a PDEs-solving module for dynamic capture. Remarkably, our Motion PointNet, with merely 0.72 M parameters and 0.82 G FLOPs, achieves an impressive accuracy of 97.52 % on the MSRAction-3D dataset, surpassing the current state-of-the-art in all aspects. The code and the trained models will be released for reproduction.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a method that extends PointNet++ for point cloud video processing. To tackle the motion information in point cloud videos, a partial differential equation (PDE) method is proposed. Experiments on the MSRAction-3D and NTU RGB+D datasets show the effectiveness of the proposed method.

### Strengths
1. The method is effective and efficient. 
2. Using PDE to solve point cloud video problems looks novel.

### Weaknesses
1. It is not that clear what the most important part in the PDEs-solving module. To my understanding, it is basically a variant of Transformer. More comparision with vanilla Transformer is encouraged.

2. It cloud be better to provide more details of PDEs and explain more the reason to use  the PDE method.

### Questions
The PDEs-solving module seems independent of point clouds. I wonder whether  the proposed module can be used for traditional video understanding.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a new method called Motion PointNet for dynamic capture in point cloud video human action recognition. The key contributions are:

- They propose to view the dynamic capture process as solving partial differential equations (PDEs) in the feature space. This provides a new perspective to model the temporal dynamics.

- They design a lightweight PointNet-like encoder to generate spatio-temporal features from point cloud sequences. 

- They introduce a PDEs-solving module to reconstruct the spatial features from the temporal features. This establishes a temporal-to-spatial mapping and enhances dynamic modeling. 

- The proposed method achieves state-of-the-art results on MSRAction-3D, NTU RGB+D, and UTD-MHAD datasets, with high efficiency in terms of parameters and FLOPs.

- Ablation studies demonstrate the effectiveness of the PDEs-solving module in improving dynamic capture.

### Strengths
This paper presents a highly original approach for point cloud video action recognition by formulating the dynamic modeling as a PDEs-solving problem. Here are the key strengths:

**Originality**: The perspective of using PDEs-solving for point cloud video modeling is novel and has not been explored before. Converting the dynamic capture to a PDEs problem with a temporal-to-spatial mapping provides a new way to establish temporal guidance.

**Quality**: The proposed method achieves state-of-the-art results on multiple benchmarks with high efficiency, demonstrating its effectiveness. The comparisons to previous works are comprehensive. The ablation studies verify the contribution of each component.

**Clarity**: The method is clearly explained with sufficient details and illustrations. The problem formulation of PDEs-solving for dynamic modeling is intuitive. The network architecture and training process are well elaborated. 

**Significance**: This work opens up a new direction of using PDEs-solving techniques for point cloud sequence modeling. The concept of converting dynamic modeling to a PDEs problem can inspire more future work. The high performance and efficiency also make the method attractive for real-world applications.

In summary, it proposes a novel perspective for dynamic point cloud modeling, achieves strong results, and clearly explains the key ideas. The PDEs-solving concept introduces new possibilities for point cloud video analysis.

### Weaknesses
While the paper presents a novel and effective approach, here are some weaknesses that could be improved:

- The formulation and explanation of the PDEs-solving could be more rigorous mathematically. Some key equations lack details on the formulations, specifically regarding the choice of basis functions and the specific form of the differential operators used. The paper would benefit from a more detailed derivation of the PDEs, including a discussion of the assumptions made and the limitations of the chosen formulation.

- The design space of the PDEs-solving module could be explored more thoroughly. For example, how are the basis operators and reconstruction loss function chosen? The paper does not provide sufficient justification for the specific choices made, such as the use of a particular spectral method or the selection of the loss function. A more detailed analysis of alternative designs and their impact on performance would be valuable.

- The comparisons to some recent works like PointMapNet are missing. This could help better demonstrate advantages over other lightweight models. The paper should include a more comprehensive comparison with other state-of-the-art methods, particularly those that focus on efficient point cloud processing, to better contextualize the performance of the proposed approach.

- The evaluations are limited to action recognition. It remains unclear how the dynamic modeling capability would transfer to other tasks like segmentation or detection. The paper should explore the generalizability of the proposed method to other tasks beyond action recognition, such as point cloud segmentation or object detection, to demonstrate its broader applicability.

- There lacks ablation and analysis on different encoder architectures. Can other lightweight encoders also benefit from the PDEs-solving? The paper should include ablation studies with different encoder architectures to demonstrate the robustness of the PDEs-solving module and its potential to improve the performance of other point cloud processing networks.

- The computational complexity and efficiency analysis is incomplete. Actual runtime comparisons could better demonstrate the speed. The paper should provide a more detailed analysis of the computational complexity of the proposed method, including actual runtime measurements on different hardware platforms, to better demonstrate its efficiency.

- The model interpretability is limited. Visualizations or analyses connecting the PDEs-solving to improved dynamics are lacking. The paper should include visualizations or other analyses to provide insights into how the PDEs-solving module contributes to improved dynamic modeling and to enhance the interpretability of the proposed approach.

### Questions
Please see the weaknesses above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces Motion PointNet for point cloud video action recognition. The Motion PointNet builds on PointNet++ encoder and a PDEs-solving module to capture input dynamics. The author adopts two state training to train the model. In first stage, the model is trained under the spatial feature reconstruction objective from the temporal features. In second stage, the model is fine-tuned for action recognition. The method outperforms previous approaches across different benchmarks, while the model is also lightweight compared with others.

### Strengths
- **Strong recognition performance**. The proposed Motion PointNet outperforms previous approaches on 3 public datasets in action recognition. 

 - **Light model**.  While the performance is strong, the model is quite light in model size and computation. 

- **Rich comparison**. The paper makes a thorough comparison with state-of-the-art methods.

### Weaknesses
 - **Understanding reconstruction objective** The loss function in (15) is not fully make sense. Given the model is trained from scratch, the 
GT $F_s$ used as supervision is also random features at the beginning, how would the contrastive objective leads the model towards the correct direction as it is the only loss used in pre-training stage?


- **Motivation of PDE is not clear**. After reading the paper, I still do not quite understand why we need a PDE to build the mapping from temporal features to spatial features. What will be changed if we replace the spectral model with some MLP or transformer like networks as   long as we make a nonlinear mapping between two spaces. The justification for using PDEs, especially given that point cloud video dynamics are primarily deformations rather than fluid-like motions, remains unclear. The paper does not adequately explain why a PDE-based approach is more suitable than other nonlinear mapping techniques, such as those used in transformer networks, particularly since transformers have shown strong performance in various complex tasks.

- **Why 2 stage training**. Could we jointly train a classification head along with the contrastive objective? What will the performance like.  The paper does not provide a strong justification for the two-stage training process. It is unclear why a joint training approach, which could potentially allow for end-to-end optimization, is not considered. The current approach of pre-training with a contrastive objective and then fine-tuning for classification may not be the most efficient way to learn task-specific features.

- **Missing simple baselines**. There are some simple baselines the method should compare with. 1, train a model with the same encoder and classification head using the same number of iterations of two stage training. 2, only fine-tune the classification head while freeze the encoder to evaluate the pre-trained presentation. The lack of these baselines makes it difficult to isolate the contribution of the proposed PDE module and the two-stage training strategy. Without these comparisons, it's hard to determine if the performance gains are due to the specific design choices or simply the result of a more complex training procedure.

### Questions
- **Feature response in figure 3**. How does those orange points are being selected? It seems like binary selection (I expect to see more colors represent the strongness of different points instead of the binary setting) What is the response from other methods (like PointNet ++) , this visualization comparison could tell the model indeed capture those dynamics. In second row of Side Kick, it seems the binary response still contain many irrelevant points based on locality instead of temporal features. 


- **Does the pre-trained features generalizable**. It seems in first stage training there is no labels required, so it is fully unsupervised. I wonder if the learned representation could be generalized or quickly adapted to other domains like what visual representation work did (i.e. MAE).

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
