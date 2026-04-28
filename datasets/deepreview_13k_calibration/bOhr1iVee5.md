# Spiking GS: Towards High-Accuracy and Low-Cost Surface Reconstruction via Spiking Neuron-based Gaussian Splatting

- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 5, 5, 5

## Abstract
3D Gaussian Splatting is capable of reconstructing 3D scenes in minutes. Despite recent advances in improving surface reconstruction accuracy, the reconstructed results still exhibit bias and suffer from inefficiency in storage and training. This paper provides a different observation on the cause of the inefficiency and the reconstruction bias, which is attributed to the integration of the low-opacity parts (LOPs) of 3D Gaussians. We identify the source of LOPs and propose Spiking GS to reduce two types of LOPs by integrating spiking neurons into the Gaussian Splatting pipeline. Specifically, we introduce global and local full-precision integrate-and-fire spiking neurons to the opacity and representation function of flattened 3D Gaussians, respectively. Furthermore, we enhance the density control strategy with spiking neurons' thresholds and a new cloning criterion. Our method can represent more accurate reconstructed surfaces at a lower cost.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work innovatively integrates spiking neurons into 3D Gaussian Splatting, effectively addressing issues related to low-opacity parts. The paper presents solid experimental validation, demonstrating advantages in both efficiency and effectiveness.

### Strengths
1. They provide insightful analysis of the low-opacity parts (LOPs) problem, categorizing it into LOGs and LOTs, and propose global and local FIF neurons as solutions, representing an innovative approach.
2. The proposed method demonstrates effectiveness across several benchmarks, achieving state-of-the-art performance while significantly reducing computational overhead.
3. The writing is clear and accessible, with coherent logical progression throughout, and supported by comprehensive experimental validation.

### Weaknesses
1. Insufficient theoretical explanation for the effectiveness of spiking neurons in addressing LOPs.
2. Limited discussion on the impact of parameter selection on performance in section 4.2.

### Questions
I would appreciate a more detailed explanation of the precise mechanisms through which the global and local FIF neurons address LOGs and LOTs, respectively. The specific interaction between these components and their respective roles in mitigating opacity-related challenges merits further elaboration.

### Soundness
3

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
This article proposes a 3DGS method based on pulse activation for scene reconstruction. Especially, the analysis of LOPS, LOGS, and LOTS in this article is very exciting and clear, which will help future researchers to carry out further work. Some innovative narratives that are too simplistic can easily lead to ambiguity. However, the author emphasizes that this article focuses on large-scale scene reconstruction and has not been experienced in experiments.I think this article still needs to enrich and modify the narrative logic, and improve the experimental part.

### Strengths
This article provides a detailed analysis of the crucial opacity issue in the 3DGS reconstruction series. The analysis of the impact of LOPS, LOGS, and LOTS is very thorough, which assists the subsequent description and experimental development. The article has clear logic and combines the latest third-generation pulse neurons and 3DGS to achieve a new efficient reconstruction architecture.

### Weaknesses
There are some issues with this article: (1) Based on the description in the article that the FIF neuron seems to be a creative work in other works, this article adds global and local limitations. Moreover, the author did not provide a detailed explanation of the differences from the original FIF neurons in the article. Based on the author's brief description, I believe this tends to be a simple call to FIF neurons rather than an innovation. (2) In addition, the author did not clearly state the specific details of the scale based clone, which appears to be very lacking in innovation. The experimental part also did not verify this cloning method. (3) The experimental section lacks visualization of large-scale scenes and does not focus on the rendering effect of new views. (4) Verification of missing loss components. The author emphasizes in the introduction that this article did not use geometric constraints, but the loss definition contains a large amount of prior supervision, which is contradictory. Meanwhile, the impact of adding these losses on performance has not been verified.

### Questions
(1) Please describe the essential differences between FIF neurons used in Spiking GS and FIF neurons;
(2) Please describe the guidance of global FIF and local FIF on the convergence process of GS;
(3) Please describe the role of mixing multiple geometric priors for supervision;
(4) The description of Scale based Clone is too brief. Please add it;
(5) Please explain the design logic of the experimental section;
(6) The visualization section shows that there is not much difference between Spike GS and GOF. Please provide more comprehensive comparison results for reference.

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
The authors propose a 3D Gaussian splatting method based on spiking neurons to address inefficiency and reconstruction bias in traditional 3D Gaussian splatting. They claim that the bias is largely due to the integration of low-opacity parts (LOPs) in the generated Gaussians. To counter this, they introduce global and local full-precision IF spiking neurons to manage the opacity and representation function of flattened 3D Gaussians, respectively. Additionally, they enhance the density control strategy by leveraging spiking neuron thresholds and implementing a new criterion based on Gaussian scales.

### Strengths
* The paper provides a theoretical analysis of the LOPs issue in 3D Gaussian splatting, accompanied by well-executed visualizations. 

* The approach balances the presence of LOPs by employing global and local FIF spiking neurons, which effectively suppress the integration of LOPs during view rendering. 

* Optimized training strategies are introduced, including a scale-based cloning technique and various regularization losses, aimed at enhancing reconstruction accuracy. 

* This method achieves high-quality 3D reconstruction with a reduced parameter count, making it both efficient and effective.

### Weaknesses
 * From Equations (7) and (8), the described FIF method seems to follow a spiking neuron approach where activation occurs only when a threshold is exceeded, maintaining traditional 3D Gaussian splatting in other cases. If this interpretation is correct, could this approach be seen as using spiking neuron properties to perform a type of "pruning" operation, thereby reducing parameter count? The mechanism by which the learnable threshold is optimized and how it impacts the overall training dynamics requires further clarification. Specifically, the interaction between the threshold learning and the Gaussian parameter optimization needs to be elaborated for a better understanding of the method’s effectiveness.

* In terms of reconstruction results, the proposed method appears to produce smoother outputs than traditional 3D Gaussian splatting, potentially at the cost of high-frequency details. The claim that details are preserved despite the smoother surfaces needs more rigorous justification, perhaps through quantitative analysis of high-frequency components in the reconstructed outputs. It is important to understand if the smoothing effect is a direct consequence of the spiking neuron’s thresholding mechanism or other aspects of the training process, and whether this effect is consistent across different datasets and scene complexities.

* The comparative results presented so far are limited, making it difficult to fully assess the advantages of this method. The ablation study should be expanded to include more variations of the proposed method to isolate the contribution of each component. Furthermore, the comparison with state-of-the-art methods should be more extensive, including a wider range of datasets and evaluation metrics to demonstrate the robustness and generalizability of the approach.

* Should the symbols in Equations (4) and (5) represent vectors? It may be helpful for the authors to review these expressions. Additionally, if the equations involve integration, the meaning of the ⋅\cdot⋅ symbol needs further clarification, as it currently does not seem fully aligned with the integrate-and-fire concept of spiking neurons. The lack of clarity in these equations makes it difficult to understand the mathematical foundation of the method.

* While the illustrations are visually appealing, the font size is rather small, and the detailed content in each image can be challenging to discern.

### Questions
* Certain terms lack clear definitions, such as the meaning of "full-precision" in line 84. Additionally, in the acronym LOGs, what does the "G" stand for? 

* To my knowledge, there are already many methods combining neuromorphic cameras with 3D Gaussian splatting, where the cameras generate spike/event data. Could the spiking neuron approach in this paper be readily adapted for use with such spike/event data? 

* Why was color reconstruction not used? 3D Gaussian splatting has been widely applied for RGB data reconstruction, so it seems feasible to directly compare colored 3D reconstructions, especially with results across multiple views.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper points out that low opacity parts (LOPs) in 3D Gaussian Splatting negatively affect the performance and efficiency of the reconstruction, and introduces global and local full-precision IF spiking neurons to reduce the LOPs and thus improve the performance and efficiency. In addition, the authors propose scale-based clone to further improve the reconstruction quality. Experiments on several datasets show that the proposed method has better performance and efficiency than the existing methods.

### Strengths
1. This paper points out that LOPs in 3D Gaussian splicing can negatively affect the performance and efficiency of reconstruction, and further decomposes them into LOGs and LOTs.
2. The paper introduces global and local full-precision IF spiking neurons to reduce LOPs, thereby improving performance and efficiency.
3. The authors further optimize the proposed method including threshold loss, scale loss, and scale-based clone to improve the reconstruction quality.
4. The authors experimentally demonstrated the effectiveness and performance advantages of the proposed method.

### Weaknesses
1. The full-precision IF neurons used by the authors (Eqs. 7 and 8) appear to contain only step functions with learnable thresholds, which is significantly different from typical spiking neurons with multiple time steps. This contributed to the limited innovation of this paper.
2. The paper lacks ablation studies for comparison with baseline, making it difficult to adequately understand the effects of each module. For example, the comparison of the proposed method with w/o glb and w/o loc is shown in Table 1~3, but it does not show how much of the improvement over the baseline is achieved by using only glb and loc.
3. It is recommended that the authors reorganize the structure of the paper, e.g., more detailed ablation studies such as loss functions should be placed in the paper rather than in the Supplementary Material to help understand these contributions.

### Questions
Please see weakness.

### Soundness
2

### Presentation
2

### Contribution
2
