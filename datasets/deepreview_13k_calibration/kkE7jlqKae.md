# Real-Time Deepfake Detection in the Real World

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 6, 5

## Abstract
Recent improvements in generative AI made synthesizing fake images easy; as they can be used to cause harm, it is crucial to develop accurate techniques to identify them. This paper introduces "Locally Aware Deepfake Detection Algorithm" (\textit{LaDeDa}), that accepts a single $9 \times 9$ image patch and outputs its deepfake score. The image deepfake score is the pooled score of its patches. With merely patch-level information, LaDeDa significantly improves over the state-of-the-art, achieving around $99\%$ mAP on current benchmarks. Owing to the patch-level structure of LaDeDa, we hypothesize that the generation artifacts can be detected by a simple model. We therefore distill LaDeDa into Tiny-LaDeDa, a highly efficient model consisting of only $4$ convolutional layers. Remarkably, Tiny-LaDeDa has $375 \times$ fewer FLOPs and is $10\text{,}000 \times$ more parameter-efficient than LaDeDa, allowing it to run efficiently on edge devices with a minor decrease in accuracy. These almost-perfect scores raise the question: is the task of deepfake detection close to being solved?  Perhaps surprisingly, our investigation reveals that current training protocols prevent methods from generalizing to real-world deepfakes extracted from social media. To address this issue, we introduce \textit{WildRF}, a new deepfake detection dataset curated from several popular social networks. Our method achieves the top performance of $93.7\%$ mAP on WildRF, however the large gap from perfect accuracy shows that reliable real-world deepfake detection is still unsolved.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces a novel deepfake detection algorithm named Locally Aware Deepfake Detection Algorithm (LaDeDa), which processes individual 9x9 image patches to assign a deepfake score. LaDeDa significantly outperforms current benchmarks with approximately 99% mAP. The paper also presents a distilled version, Tiny-LaDeDa, which is highly efficient with reduced computational requirements, making it suitable for edge devices. The authors question whether the task of deepfake detection is nearing a solution but find that current training protocols fail to generalize to real-world deepfakes from social media. To address this, they introduce WildRF, a new dataset derived from social networks to better simulate real-world conditions.

### Strengths
1.Innovative patch-based detection method that leverages local features.

2.Development of Tiny-LaDeDa for efficient edge device operation.

3.Creation of WildRF dataset to better simulate real-world deepfake detection challenges.

### Weaknesses
1.According to the results, it seems that training on the datasets from the social media is better than the datasets from the simulated datasets, if training the detectors under more post-processing augmentations, does the performance will be better than training on the social media datasets?

2.Before the ensemble with CLIP, how do you train the CLIP model? All parameters are updated or just the linear classifier head?
3.In the sanity check, what kind of fake images are tested?

4.LaDeDa detects fake images through the extraction of local image patches. However, some deepfake techniques, such as face swapping only change the face region within the real images. Is the method still useful?

5.It is better to describe the details related to other gradient inductive biases in Fig.7(a).

TYPO: In the 772-th row, ‘teset’ should be ‘test’.

### Questions
Please see weakness above.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper introduces the 'Locally Aware Deepfake Detection Algorithm' (LaDeDa), which detects deepfakes using 9 × 9 image patches and outperforms the current method with nearly 99% mAP. The authors further distil LaDeDa into a lightweight model, Tiny-LaDeDa, which significantly reduces computational requirements and is suitable for edge devices. The authors further highlight limitations in current training protocols that hinder generalization to real-world deepfakes sourced from social media. To address this, they present a novel dataset named WildRF. Performance on WildRF, while leading at 93.7% mAP, indicates that reliable deepfake detection in real-world scenarios remains a challenge.

### Strengths
I believe the most significant contribution of this paper is the reconsideration of existing deepfake detection protocols. While current methods have reached their performance ceiling on standard benchmarks, the authors revealed shortcomings of existing deepfake detection algorithms when testing on images sourced from social media—the most popular distribution platform for deepfakes. I think this is an important issue that the community should pay attention to. Furthermore, the paper contributes a new deepfake detection method.

### Weaknesses
- Although the paper discusses the robustness of the method against JPEG compression and blur perturbation, I believe it would be beneficial to further evaluate the robustness of deepfake detection algorithms against adversarial perturbations, such as those proposed in [1] and basic L-p norm adversarial method like PGD and FGSM. 
- Moreover, the method's design relatively simple. Compared to PatchFor (the primary comparison method in this paper), it mainly improves the patch weighting strategy. It achieves nearly a 10% improvement on WildRF (the new benchmark proposed in this paper) without involving additional training techniques, which raises concerns about the fairness of this comparison. Could the authors further elaborate on the source of their method's effectiveness (either theoretically or through intuitive explanations)? Additionally, could authors provide the training setup, including both the baseline model and LaDeDa?

[1] Exploring Frequency Adversarial Attacks for Face Forgery Detection, CVPR2022

### Questions
Although deepfake detection is a relatively well-addressed problem, the new evaluation benchmark proposed in this paper warrants further attention from the community, and I hope the authors can address the aforementioned weaknesses. However, since I am not fully familiar with this field, my final rating will be based on the opinions of other reviewers.

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
5

### Summary
This paper addresses the pressing issue of deepfake detection by introducing "Locally Aware Deepfake Detection Algorithm", a  method that operates on 9×9 image patches to produce deepfake scores. The image-level deepfake score is obtained by pooling the scores of all patches. Building on the insight that generation artifacts can be detected through local features, the authors distill LaDeDa into "Tiny-LaDeDa," an efficient model consisting of only four convolutional layers. Tiny-LaDeDa maintains high accuracy while being computationally efficient enough for deployment on edge devices.
The authors also introduce WildRF, a new dataset of deepfake images curated from popular social media platforms. Through experiments, the paper demonstrates that while LaDeDa achieves top performance on WildRF (93.7% mAP), there remains a significant gap from perfect accuracy, highlighting that reliable real-world deepfake detection is still an unsolved challenge.

### Strengths
- Interesting Patch-Based Approach: LaDeDa focuses on small image patches (9×9 pixels). By limiting the receptive field, the model emphasizes local artifacts rather than global semantics.
- Tiny-LaDeDa: The distillation of LaDeDa into Tiny-LaDeDa is a valuable contribution. Tiny-LaDeDa maintains high accuracy while being highly efficient, with 375× fewer FLOPs and 10,000× fewer parameters. This makes it suitable for deployment on resource-constrained devices and real-time applications.
- Introduction of WildRF Dataset

### Weaknesses
-Limited Analysis of Failure Cases: The paper mentions that reliable real-world deepfake detection is still unsolved but provides limited analysis of why current methods fail on real-world data and what specific challenges need to be addressed.
-Ablation Studies Could Be Expanded: More extensive analyses of different components (e.g., impact of patch size, pooling methods, and model architecture choices) would strengthen the work.
-Comparison with More Recent Techniques: The paper primarily compares LaDeDa with somewhat classic existing methods but could benefit from including comparisons with the latest advancements in deepfake detection, especially methods that focus on real-world applicability.

### Questions
Can you explain how images were sourced, any filtering criteria applied, and how the balance between real and fake images was maintained?

What would be the most optimal patch sizes and why? 

Whare are some cases where LaDeDa and Tiny-LaDeDa fail to detect deepfakes in the real world? Or one fail and the other succeed?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a deepfake detection algorithm called LaDeDa, which accepts a single 9 × 9 image patch and outputs its deepfake score. 
The image deepfake score is the pooled score of its patches. 
With merely patch-level information, LaDeDa significantly improves over the state-of-the-art, achieving around 99\% mAP on current benchmarks. 
They then distill LaDeDa into Tiny-LaDeDa, a more efficient model consisting of only 4 convolutional layers.
The authors also introduce WildRF, a new deepfake detection dataset curated from several popular social networks and show that current training protocols prevent methods from generalizing to real-world deepfakes extracted from social media.

### Strengths
1. The paper is well-written and easy to follow.
2. The proposed method is feasible, using a patch-level structure to detect deepfakes is quite reasonable. Using a distillation method to obtain a more efficient model is also a good idea.
3. The experiments are comprehensive and the results are convincing.
4. The introduction of WildRF dataset is a valuable contribution to the community, which is the most attractive part of this paper.

### Weaknesses
1. The proposed method is not very innovative. The patch-level structure is not new, and the distillation method is also a common technique. The paper is not very appealing.
2. Since the authors claim that they can do patch-level detection, they should analyze and experiment on inpainted images, i.e., images with part real and part synthetic. Can the method detect deepfakes in this case?
3. The necessity of real-time detection is not fully demonstrated. Can the method be applied to detect deepfakes in generated or spliced videos?

### Questions
See Weakness.

### Soundness
3

### Presentation
3

### Contribution
3
