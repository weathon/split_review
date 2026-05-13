# CosPGD: an efficient white-box adversarial attack for pixel-wise prediction tasks

- Decision: Reject
- Scores: 8, 5, 5, 5

## Abstract
While neural networks allow highly accurate predictions in many tasks, their lack of robustness towards even slight input perturbations often hampers their deployment.
Adversarial attacks such as the seminal \emph{projected gradient descent} (PGD) offer an effective means to evaluate a model's robustness and dedicated solutions have been proposed for attacks on semantic segmentation or optical flow estimation. While they attempt to increase the attack's efficiency, a further objective is to balance its effect, so that it acts on the entire image domain instead of isolated point-wise predictions. This often comes at the cost of optimization stability and thus efficiency.  
Here, we propose CosPGD, an attack that encourages more balanced errors over the entire image domain while increasing the attack's overall efficiency.
To this end, CosPGD leverages a simple alignment score computed from any pixel-wise prediction and its target to scale the loss in a smooth and fully differentiable way. 
It leads to efficient evaluations of a model's robustness for semantic segmentation as well as regression models (such as optical flow, disparity estimation, or image restoration), and it allows it to outperform the previous SotA attack on semantic segmentation.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper concentrates on adversarial attacks tailored for pixel-wise prediction tasks such as semantic segmentation, optical flow prediction, and image restoration. 
It uncovers that PGD, a method commonly used in image classification, is not efficient for pixel-wise prediction tasks, and SegPGD, a method designed for semantic segmentation, is not applicable to other pixel-wise tasks. 
The paper introduces CosPGD, an efficient white-box adversarial attack specifically designed for pixel-wise prediction tasks. It utilizes cosine similarity between prediction distributions and ground truth (or target, in the case of targeted attacks) to weight the loss value of each pixel, enabling more effective and nuanced attacks. 
Experimental results across various datasets and settings demonstrate CosPGD's superiority and versatility in assessing the robustness of models for pixel-wise prediction tasks.

### Strengths
1. The proposed CosPGD is a relatively simple modification of SegPGD, yet it significantly enhances effectiveness across multiple datasets. While SegPGD differentiates between pixels that are predicted correctly and those predicted incorrectly during the generation of adversarial examples, assigning different pre-defined weights to the loss terms of correctly and incorrectly predicted pixels, CosPGD replaces these pre-defined weights with cosine similarities between the predictions and ground truth at each pixel. Experimental results demonstrate that this modification results in a more effective attack.

2. CosPGD is applicable to a variety of pixel-wise prediction tasks, including semantic segmentation, optical flow prediction, and image restoration. Unlike SegPGD, which is limited to pixel-wise classification tasks, CosPGD can be readily extended to both pixel-wise classification and regression tasks. Experimental results confirm the effectiveness of CosPGD on several pixel-wise prediction tasks.

3. There are abundant ablation experiments regarding hyper-parameters such as perturbation bounds, step sizes, and iteration steps, all of which verify the effectiveness of CosPGD compared to previous methods like PGD and SegPGD.

### Weaknesses
1. The paper does not provide sufficient comparisons and discussions related to recent works in pixel-wise prediction tasks, such as Qu et al. [1], and other applicable attacks in image classification, like C&W [2], and MI-FGSM [3]. Specifically, the lack of a comparative analysis against these methods, which have demonstrated strong performance in related domains, leaves a gap in understanding the relative effectiveness of the proposed CosPGD. For instance, a comparison with the certified radius-guided attack framework in [1] would be crucial to assess the robustness guarantees offered by CosPGD. Similarly, the absence of comparisons with C&W [2] and MI-FGSM [3], which are known to be effective adversarial attacks, makes it difficult to place CosPGD within the broader landscape of adversarial attack methods.

2. Why does using cosine similarity as a weight (in CosPGD) outperform predefined weights (in SegPGD)? Is there a detailed explanation? The paper lacks a rigorous analysis of why the cosine similarity weighting is superior to the fixed weights used in SegPGD. A more in-depth discussion of the mathematical properties and the underlying mechanisms that lead to this performance difference is needed. For example, does the cosine similarity provide a more nuanced gradient signal for optimization, or does it better capture the semantic structure of the prediction space?

3. Why does the paper adopt different settings for the three tasks: non-targeted attacks for semantic segmentation and image restoration, and targeted attacks for optical flow prediction? What about the performance of targeted attacks for semantic segmentation and image restoration? The rationale for using different attack settings across the three tasks is not sufficiently justified. The paper should provide a more detailed explanation for why targeted attacks are more suitable for optical flow while non-targeted attacks are used for semantic segmentation and image restoration. Furthermore, the absence of results for targeted attacks on semantic segmentation and image restoration limits the scope of the evaluation and raises questions about the generalizability of the findings.

4. The experimental results presented in Figures 14 and 15 make it challenging to discern the numerical values. Presenting the data in a tabular form would be more beneficial. The visual presentation of the results in Figures 14 and 15 lacks precision, making it difficult to accurately compare the performance of different methods. The use of tables would allow for a more precise and quantitative analysis of the results.

5.There is a lack of a detailed definition for $L$ in equations (1), (5), and (6). The paper does not clearly define the loss function $L$ used in equations (1), (5), and (6). This lack of clarity makes it difficult to understand the exact implementation of the proposed method and raises concerns about the reproducibility of the results.

### Questions
See in weakness

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes CosPGD, a unified white-box adversarial attack aiming to any pixel-wise prediction task based on the cosine similarity between the distributions over the predictions and ground truth. The effectiveness of the method is demonstrated through a series of experiments across multiple tasks including semantic segmentation, optical flow and image denoising.

### Strengths
First and foremost, in comparison to the recently introduced SegPGD, CosPGD demonstrates a considerably more pronounced adversarial attack impact in semantic segmentation tasks. Notably, what sets CosPGD apart is its applicability beyond segmentation-specific tasks when compared to SegPGD. CosPGD serves as a versatile attack method applicable to any pixel-wise prediction task, boasting efficient deployment capabilities and superior efficacy in contrast to the general PGD method.

### Weaknesses
Section 4.3's content warrants appropriate adjustment. This section primarily showcases the superior degradation effect of CosPGD on NAFNet in comparison to PGD and SegPGD (particularly at low attack iterations). However, this evidence alone may not adequately support the assertion that "CosPGD can efficiently enhance a new model's robustness." To convincingly substantiate this claim, the authors should present more compelling evidence within the main body of the paper, rather than relegating it to the appendix. It is particularly essential to include results from the denoising task (as presented in Appendix D2). The current presentation focuses heavily on the attack's effectiveness in degrading performance, but lacks sufficient evidence to support claims about its utility in enhancing model robustness. The paper needs to clarify how the observed degradation translates into a practical method for improving model training, especially within the main body of the paper. The claim that CosPGD can efficiently enhance robustness needs more direct experimental validation, such as showing improved performance after adversarial training with CosPGD, rather than just showing degradation under attack. This is especially important since the method is presented as a general improvement for pixel-wise classification tasks.

### Questions
1. Although CosPGD exhibits substantial improvements over SegPGD in terms of attack efficacy and generality, it is worth noting that SegPGD also contributes significantly to enhancing model robustness through adversarial training. The absence of corresponding experiments makes it challenging to completely establish the effectiveness of this aspect.

2. An inquiry arises regarding the rationale behind the author's choice of an optical flow experiment to evaluate the versatility of CosPGD. The choice of optical flow as a benchmark should be substantiated by explaining how the characteristics of this task effectively highlight the advantages of CosPGD. Furthermore, additional experiments should be incorporated to showcase CosPGD's performance in various image restoration tasks, such as single image deraining, to bolster its claims further.

3. It seems like the authors need to reorganize the contribution of the paper, since the core of the paper is actually a general improvement on adversarial training for pixelwise classification tasks.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposed a white-box adversarial attack method CosPGD that considers the cosine similarity between predictions and targets for each pixel.  The authors claimed that CosPGD can be used for various pixel-wise prediction tasks, outperforming existing attacks on semantic segmentation and providing insights into model performance. It is similar to SegPGD and the experiments are insufficient to validate the advantage of the proposed method.

### Strengths
1) The authors introduce the principle and method of CosPGD clearly in **Sec.3**.

2) The universal design for loss function of CosPGD make it be applicable to a wide range of pixel-wise prediction tasks.

### Weaknesses
1) Take the non-targeted attack as an example, the proposed loss function in Eq.(5) $L_{\mathrm{cos}}=\frac{1}{H \times W} \sum_{H \times W} \cos (\overrightarrow{\text { pred }}, \overrightarrow{\text { target }}) \cdot L\left(f_{\text {net }}\left(\boldsymbol{X}^{\text {adv } v}\right), \boldsymbol{Y}\right),$ 
   is very similar with the loss function of SegPGD[1]  $L_{SegPGD} = \frac{1}{{H}\times{W}} \sum_{j\in P^T} L_j + \frac{1}{{H}\times{W}} \sum_{k\in P^F} L_k$. The core difference lies in the pixel-wise scaling factor. While CosPGD uses cosine similarity, SegPGD employs a binary classification of pixels into correctly and incorrectly classified sets, with a tunable parameter to balance the two. This difference, while present, does not appear to be a significant leap in novelty, as both methods essentially perform pixel-wise loss scaling based on prediction accuracy. The use of cosine similarity, while a continuous measure, is not a fundamentally new concept in this context.

2) Although it claims that CosPGD can be used for various pixel-wise prediction tasks, the experimental results do not consistently demonstrate a significant improvement compared to SegPGD[1]. Specifically, in the image restoration task as shown in **Fig.7**, the performance of CosPGD is only marginally better than SegPGD, especially when considering the 20 iterations. This raises concerns about the practical advantage of CosPGD in scenarios beyond semantic segmentation, where SegPGD might be adapted with similar performance.

3） In **Sec.4.2** the paper identifies their method's performance in the optical flow task, but it only presents experiments compared with PGD[2] in **Fig.5**. It is unclear how SegPGD[1] performs in the optical flow task, and whether the proposed method offers any advantage over a modified SegPGD for this task. The lack of a direct comparison with SegPGD in this context makes it difficult to assess the true contribution of CosPGD.

4） In **Sec4.3** the authors state that "We observe that at low number of attack iterations (3 attack iterations) it performs significantly worse than PGD, thus demonstrating its limitation on this task." However, SegPGD[1] requires adjusting a balance factor during the attack iteration, and white-box attacks are not typically compared at such low iteration counts. Therefore, the comparison at 3 iterations is not a fair evaluation of the method's capabilities relative to SegPGD, which may require more iterations to show its effectiveness. This comparison seems to highlight a limitation of CosPGD rather than a genuine advantage of SegPGD.

### Questions
Please see the weakness.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a white-box adversarial attack CosPGD for dense predictions tasks such as semantic segmentation, optical flow and image restoration. CosPGD adopts the cossine similarity to weight the basic PGD attack, which has better interpretability compared to the weight adjustment based on the number of iterations used in SegPGD. Experimental results show CosPGD is strong attack performance in multi tasks.

### Strengths
1. The authors discuss the differences and advantages of PGD and SegPGD.
2. Compared to SegPGD, CosPGD has a broader generality, which can be applied not only to pixel classification tasks but also to pixel regression tasks.

### Weaknesses
1. The core of the proposed method is very similar to SegPGD, as both aim to focus on the pixels where the attack has not been successful yet (e.g. pixels with large cosine similarity weight). Therefore, the novelty is limited. The use of cosine similarity, while interpretable, does not fundamentally alter the underlying iterative attack strategy of focusing on pixels that are not yet adversarial. The core idea of re-weighting the loss based on a measure of prediction correctness is shared with SegPGD, making the contribution incremental rather than transformative. The mathematical formulation, while using cosine similarity, still operates within the same framework of iteratively adjusting pixel-wise gradients based on a measure of error, which is also present in SegPGD.
2. Ablation experiments lacking other metrics like cosine distance. The ablation study should include a more comprehensive analysis of the impact of different distance metrics. Specifically, it is unclear why cosine similarity is the optimal choice, and the lack of experiments with other metrics such as KL divergence or JS divergence leaves a gap in the analysis. The paper should provide a justification for the choice of cosine similarity by comparing its performance against other common distribution distance metrics.
3. Lack of performance comparison experiments with state-of-the-art methods [1] for semantic segmentation tasks. The paper lacks a comparison with recent state-of-the-art adversarial attack methods for semantic segmentation. The absence of such a comparison makes it difficult to assess the relative performance of the proposed method. Specifically, the paper should compare against methods that are specifically designed for semantic segmentation, not just general adversarial attacks.

### Questions
See Weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
