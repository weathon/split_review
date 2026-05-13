# Efficient Adaptive Filtering for Deformable Image registration

- Decision: Reject
- Scores: 5, 6, 3, 6

## Abstract
In medical image registration, where targets exhibit piecewise smooth structures, a carefully designed low-resolution data structure can effectively approximate full-resolution deformation fields with minimal accuracy loss. 
Although this physical prior has proven effective in traditional registration algorithms, it remains underexplored in current learning-based registration literature.
In this paper, we propose AdaWarp, a novel neural network module that leverages this prior for efficient and accurate medical image registration. 
AdaWarp comprises an encoder, a guidance map generator, and a differentiable bilateral grid, enabling an edge-preserving low-frequency approximation of the deformation field. 
This design reduces computational complexity with low-resolution feature maps while increasing the effective receptive field, achieving a balanced trade-off between registration accuracy and efficiency.
Experiments on two registration datasets covering different modalities and input constraints demonstrate that AdaWarp outperforms existing methods in accuracy-efficiency and accuracy-smoothness tradeoffs.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper leverages prior knowledge observed in medical images to introduce the Piece-wise Smooth (P-S) Assumption as a basis for addressing medical image registration tasks. Specifically, the authors propose AdaWarp, a warping method that utilizes learnable adaptive filtering to register medical scans in line with the P-S assumption. By employing a low-resolution latent representation along with a differentiable bilateral grid, the method achieves a better balance between accuracy and efficiency. Experiments conducted on two registration datasets validate the effectiveness of the proposed approach.

### Strengths
1. The motivation behind this paper is reasonable. By analyzing daily CT and MRI scans in the cardiac and abdominal regions, the authors observed two consistent patterns across certain subjects, leading to the formulation of the Piece-wise Smooth (P-S) Assumption. This assumption leverages physical priors from observed medical image patterns, which is both innovative and plausible, enhancing neural network-based registration tasks by grounding them in realistic assumptions about medical image structures.
2. The paper provides thorough comparative experiments. The authors test AdaWarp on two registration datasets spanning different modalities and input constraints, which demonstrates robustness and broad applicability.

### Weaknesses
1. The novelty of this paper does not seem particularly strong. While the method leverages an encoder to extract a latent representation that approximates the deformation field at a low resolution, this approach mainly contributes to the model's efficiency but is not unique. The use of latent feature representations for similar tasks has already become common in the field.
2.  The core of AdaWarp is a differentiable bilateral grid,  which naturally incorporates the P-S prior.  In implementation, the guidance map aids in processes like splatting, blurring, and slicing. This incremental modification lacks sufficient novelty.

### Questions
See the above strengths and weaknesses.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a learning framework that improves the accuracy-efficiency trade-off in medical image registration by leveraging the piece-wise smooth prior. The proposed method was evaluated on two medical image datasets involving cardiac MRI and abdomen CT images. This method transforms the deformable registration problem into a keypoint detection task and shows potential for segmentation tasks.

### Strengths
The proposed method bridges the gap in the existing literature focusing on the balance between registration accuracy and computational efficiency, which is capable of enforcing global smoothness while respecting local discontinuities. This paper was well-written with very clear description on methodology.

### Weaknesses
1. The major concern is the research focus of this study, which might not be of sufficient significance in the field of medical image registration. After the introduction of deep learning-based registration methods, e.g., VoxelMorph, existing methods have become very fast, allowing real-time registration using GPUs. Under this situation, only a few studies have specifically focused on improving efficiency, which suggests that this topic might not be the most pressing problem in the community. The paper does not adequately justify the need for further efficiency gains, especially given the already high speeds achieved by existing methods.

2. Another concern is the generalizability of the piece-wise smooth (P-S) assumption. In the study, this assumption was exemplified and evaluated with cardiac MRI and abdomen CT images, where there are relatively fewer complex anatomical structures and local deformations. It’s important to evaluate the proposed method on the well-benchmarked brain MRI registration tasks, in which the P-S assumption may fail, particularly in regions with highly convoluted structures or significant anatomical variability. The current evaluation does not sufficiently demonstrate the robustness of the method across diverse anatomical contexts.

### Questions
1. In Figure 4 and Figure 5, why not include VoxelMorph into comparison? VoxelMorph is the most widely-benchmarked method and has high efficiency with low number of parameters.  
2. There is a recent registration study in CVPR (CorrMLP, Meng et al. 2024), which is based on a totally conflicting motivation against this paper. CorrMLP attempted to capture long-range dependency among full-resolution image details in an efficient approach (using MLPs), while this paper suggests that only low-resolution features are sufficient. So, it’s interesting to compare with the CorrMLP: did the proposed method achieve similar registration accuracy while reducing much computational complexity?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a novel method to utilise prior knowledge (piece-wise smooth assumption) to enhance learning based registration striking a balance between computational complexity and accuracy. The performance is evaluated on a cardiac and an abdominal dataset.

### Strengths
The paper presents AdaWarp, a novel method that integrates the piece-wise smoothness assumption enforcing global smoothness while respecting local discontinuities in a learning framework striking a balance between complexity and accuracy. 

Moreover, it demonstrates connections of the adaptive filtering approach with the self attention.

The experimentation on two challenging registration tasks cardiac and inter-subject abdominal registration demonstrate that AdaWarp outperforms existing methods in accuracy-efficiency and accuracy-smoothness tradeoffs.

### Weaknesses
Although I believe that the paper attempts to bridge a gap in the literature by incorporating a differentiable bilateral grid within a learning-based registration framework, I would like to point out several weaknesses and raise some questions regarding the experiments.

[A] I would like to invite the authors to elaborate on this statement regarding iterative optimization-based methods: “As a result, these approaches tend to be time-consuming and lack the ability to incorporate contextual information effectively.” Specifically, it is unclear what type of contextual information is being referenced, as iterative methods can incorporate multi-channel information, such as segmentation maps, alongside the images themselves. Furthermore, the statement regarding time-consumption needs clarification, as discrete optimization methods can converge in fewer iterations than continuous methods, especially for large deformations, though they may have higher memory requirements.

[B] “While high-dimensional filtering can project signals onto arbitrary spaces, we focus on extending by one additional dimension to account for the object boundary.”

What is the intuition behind this approach? Is only one additional dimension sufficient? I would like to invite the authors to further elaborate and explain their choice. It is not clear why a single additional dimension is sufficient to capture the complex relationships that may exist within the data, especially when considering that the bilateral grid could potentially benefit from capturing contextual differences beyond simple intensity variations.

[C] The role of the guidance map generator component is unclear. Could the authors please explain why this component is used or needed? It is not clear why the raw image intensities cannot be used directly as the additional coordinate in the bilateral grid, and what advantage the trainable guidance map provides.

[D] Could the authors clarify whether the same lambda values are used for all methods or if different values are applied? How were these values tuned? Were they also tuned for the baselines?

[E] The proposed method utilizes a diffeomorphic transformation model; however, it is not clear whether the baselines follow the same principle. Could the authors provide a table that explicitly lists the hyperparameters used by each of the baselines along with the transformation model?

[F] The authors chose different baselines for the two datasets, which is puzzling. What is the intuition behind this decision? Is there a reason why this approach was chosen?

[G] The paper presents t-tests for DICE scores but not for other metrics. Is there a reason for this choice? Could the authors extend their t-tests to cover HD95 as well?

[H] “Learning-based methods generally outperform traditional ones in registration accuracy, though with slightly higher SDlogJ.”

Do the authors have any intuition as to why this is the case? Normally, I would expect that iterative optimization methods achieve higher accuracy [1].

[I] For the abdominal dataset, the proposed method uses Convex Adam’s framework with the same segmentation model as a feature extractor. Is there any reason for this choice? Could the model be trained from scratch? Could the authors elaborate on the design choices, including why the architecture differs depending on the dataset?

[J] The code is not available. Are the authors planning to make their code publicly accessible?

[K] Due to the lack of ground truth, registration is evaluated quantitatively with surrogate measures. However, to ensure the registration’s success, it is common practice to inspect the resulting transformed images qualitatively as well. I would like to invite the authors to provide qualitative results for both datasets, as this would substantially strengthen their claims.

### Questions
I encourage the authors to consider addressing as many of the points highlighted in the weaknesses section as possible. Additionally, while the paper presents an intriguing and novel approach, the clarity and quality of the presentation could benefit from further refinement.

### Soundness
2

### Presentation
2

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
The paper presents AdaWarp, a novel architecture in medical image registration. The model introduces a piece-wise smooth (P-S) assumption, which exploits the smoothness of intensity variations within anatomical regions while preserving sharp boundaries between organs. This assumption is incorporated into the network through a differentiable bilateral grid, which allows for efficient edge-preserving filtering and reduces computational complexity.

### Strengths
1. The integration of the differentiable bilateral grid into the deep learning framework for image registration is highly innovative. It effectively addresses the limitations of traditional smoothness constraints, enabling the model to better handle complex and localized deformations.

2. The paper is well-structured, offering a clear explanation of the proposed methods. It provides detailed descriptions of the differentiable bilateral grid, encoder architecture, and adaptive filtering process. Visual aids, such as Figures 4 and 5, are particularly useful in clarifying complex comparisons.

3. This method presents a promising alternative for resolving the conflict between global smoothness and local deformations, potentially offering improved solutions in certain applications.

### Weaknesses
The weaknesses of the paper are primarily in the literature review and experimental sections, which lack sufficient references and baseline comparisons, as well as visual results. These limitations are why I rated the paper as "fair" in terms of Presentation and Soundness.


1. The paper needs more references in the literature review. The current review only discusses works that do not address the conflict between global smoothness and local deformations. However, this is not the first paper to tackle this problem. Research such as multi-scale registration and patch-wise registration also offers relevant solutions. While these methods may not explicitly incorporate the piece-wise smooth prior, they still manage local deformations while maintaining overall smoothness. The authors should include these references in the background and select baselines from this body of work to show that the proposed method offers a superior solution to the problem.

2. The experiments do not adequately support the claimed advantages of the proposed method. While the paper argues that the model can generate sharp boundaries between organs by incorporating the P-S assumption, it fails to provide visual results to substantiate this key contribution. Relying solely on numerical metrics like Dice, HD95, and SDlogJ does not clearly demonstrate that the model’s output preserves sharp boundaries.

3. The writing in the experiments section is somewhat disorganized. The authors employ significantly different model structures and training strategies, including both unsupervised and semi-supervised approaches (which require further clarification), depending on the dataset. This inconsistency raises concerns about the generalizability of the model across different tasks. Additionally, the experiments lack ablation studies, which are necessary to demonstrate the effectiveness of each component in the proposed methods.

### Questions
1. Why were different model structures used for different datasets? What would be the result of using Ada-Res on the Abdomen CT dataset and Ada-Cost on the ACDC dataset? A comparison of these model structures across datasets could help demonstrate their generalizability and clarify why different architectures were chosen for each.

2. In the Abdomen CT dataset, Ada-Cost uses “the same segmentation model for feature extraction.” Was this segmentation model pre-trained? If so, this would make Ada-Cost a semi-supervised registration model. Comparing it with other unsupervised deep learning-based methods would be unfair. Additionally, how exactly was the segmentation model integrated into your model’s structure? Does it replace the "guidance map generator," or is it incorporated elsewhere in the architecture?

3. More references, more baselines and visual evaluations of warped images and warped segmentation masks would be highly valuable. Providing such visual results would help demonstrate the effectiveness of your method in producing sharp boundaries, which cannot be fully illustrated through numerical metrics alone.

4. I would greatly appreciate it if the paper could provide information on the inference and training time of the proposed method. This data would offer more valuable insights into the computational efficiency of the model.

5. Another concern is that the authors selected "interpretability and explainable AI" as Primary Area. I’m not sure if this is appropriate since there is no work about interpretability of proposed method.

### Soundness
3

### Presentation
2

### Contribution
3
