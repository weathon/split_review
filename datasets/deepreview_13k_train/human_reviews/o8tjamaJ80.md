# Adversarial AutoMixup

- Decision: Accept
- Scores: 8, 6, 8

## Abstract
Data mixing augmentation has been widely applied to improve the generalization ability of deep neural networks. Recently, offline data mixing augmentation, \textit{e.g.} handcrafted and saliency information-based mixup, has been gradually replaced by automatic mixing approaches. Through minimizing two sub-tasks, namely, mixed sample generation and mixup classification in an end-to-end way, AutoMix significantly improves accuracy on image classification tasks. However, as the optimization objective is consistent for the two sub-tasks, this approach is prone to generating consistent instead of diverse mixed samples, which results in overfitting for target task training. In this paper, we propose AdAutomixup, an adversarial automatic mixup augmentation approach that generates challenging samples to train a robust classifier for image classification, by alternatively optimizing the classifier and the mixup sample generator. AdAutomixup comprises two modules, a mixed example generator, and a target classifier. The mixed sample generator aims to produce hard mixed examples to challenge the target classifier, while the target classifier's aim is to learn robust features from hard mixed examples to improve generalization. To prevent the collapse of the inherent meanings of images, we further introduce an exponential moving average (EMA) teacher and cosine similarity to train AdAutomixup in an end-to-end way. Extensive experiments on seven image benchmarks consistently prove that our approach outperforms the state of the art in various classification scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
Mixup data augmentations are widely used and usually require well-designed sample mixing strategies, e.g., AutoMix optimized in an end-to-end manner. However, using the same mixup classification loss as the learning objective for both the mixed sample generation and classification tasks might cause consistent and unitary samples, which lack diversity. Based on AutoMix, this paper proposes AdAutomixup, an adversarial automatic mixup augmentation approach that generates challenging samples to train a robust vein classifier for palm-vein identification by alternatively optimizing the classifier and the mixup sample generator. Meanwhile, the authors introduce an EMA teacher with cosine similarity to train AdAutomixup preventing the collapse of the inherent meanings of images. Extensive experiments on five mixup classification benchmarks demonstrate the effectiveness of the proposed methods.

### Strengths
* (**S1**) This paper provides an interesting view of improving mixed sample qualities through adversarial training in the close-loop optimized mixup augmentation framework. The overall presentation of the manuscript is easy to follow, and the proposed methods are well-motivated.

* (**S2**) Extensive experiments on mixup benchmarks verify the performance gains of the proposed AdAutoMix compared to existing mixup methods. Popular Transformer architectures are included in experiments.

### Weaknesses
 * (**W1**) More empirical analysis of the proposed methods can be added. Despite the authors visualizing the mixed samples and CAM maps of various mixup methods, it can only reflect the overall performances and characteristics of different methods. I suggest the authors provide a fine-grained analysis of each proposed module to demonstrate its effectiveness, e.g., plotting the classification accuracy of using adversarial training or not. Specifically, it would be beneficial to see ablation studies that isolate the impact of the adversarial training component on the overall performance. For instance, the contribution of the adversarial loss could be evaluated by comparing the performance of the model trained with and without this loss, while keeping all other components constant. Furthermore, analyzing the sensitivity of the adversarial training parameters, such as the learning rate and the strength of the adversarial perturbation, would provide a more comprehensive understanding of the method's behavior. This would help in identifying the optimal configuration for different datasets and tasks.

* (**W2**) Small-scale experiments. The authors only provide comparison results on CIFAR-10/100, Tiny-ImageNet, and fine-grained classification datasets. More experiments on ImageNet-1K or other large-scale datasets are required. Meanwhile, the evaluation tasks or metrics can be more diverse, such as more robustness evaluations with adversarial attacks and transfer experiments to downstream tasks. The current evaluation lacks a comprehensive assessment of the model's robustness and generalization capabilities. It is crucial to evaluate the model's performance under various perturbations, such as adversarial attacks, noise, and occlusions. Additionally, transfer learning experiments to different datasets or tasks would demonstrate the generalizability of the proposed method. For example, evaluating the model's performance on object detection or semantic segmentation tasks would provide more insights into its versatility.

* (**W3**) Some minor drawbacks in writing formats, and I suggest the authors take more time to polish the writing. As for Section 3, the arrangement of Sec. 3.1 and Sec. 3.2 can be reversed. Or the authors can provide a Preliminary section to introduce the background knowledge (e.g., mixup classification problem). As for equations, the text subscripts (e.g., $argmin_{\theta}$, $L_{amce}$) should be in bold format, i.e., using `\mathrm{}` as $\mathrm{argmin}_{\theta}$. As for tables and figures, there are some untidy arrangements, like Table 3, 4, and 5, and Figure 5 and 6. The author might zoom in on Figure 1 to show the detailed improvement of AdAutoMix.

### Questions
* (**Q1**) Do the authors provide the hyper-parameter settings of AdAutoMix (e.g., the mixing ratio $\lambda$, the mixed sample number $N$, and $\beta$ in Eq. (12)? The authors might provide a sensitivity analysis of the hyper-parameters in the Appendix.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes an adversarial data augmentation strategy that builds on top of AutoMix. The framework alternates between training a mixed example generator and a target classifier. The mixed sample generator aims to produce hard examples and the target tries to improve generalization by learning robust features. With automatic mixup approaches (based on saliency or otherwise) the combination is deterministically selected, and there is no sample diversification. To mitigate this, the method proposes an adversarial generator instead. 
To prevent a collapse from the generator, an EMA teacher and a weighted cosine similarity term between the mixed sample and individual samples is used for end-to-end learning.

### Strengths
Results are consistently better than AutoMixup and the evaluation (Table 1) is thorough.



--------
Post-rebuttal:

The authors have adequately addressed the concerns in the review. Useful experiments and ablations have been added as well. I'm still a little skeptical about the actual impact of the paper, from the methods and corresponding evaluation numbers in the paper I believe that we're at the point of diminishing returns. 

I've therefore increased my score to a 6.

### Weaknesses
There is no evaluation compared to Adversarial data augmentation approaches [1, 2, 3, 4]. At least an introduction or related works section should be added as relevant approaches to the problem.

The term “cross attention module” (CAM) should not be used as it can be confused with “class activation mapping” (CAM) which is generally used in saliency-based data augmentation methods.

Some notation is confusing - the encoder weight is updated with an EMA of the weights of the classifier - $\hat{\phi} = \xi \hat{\phi} + (1-\xi) W$. Is it unclear if the encoder refers to the generator or the classifier. Later near Equation 12, $\psi$ is referred to as a target classifier with weights $W$. 

Equation 7 and 8 refer to the same value of $y$ used in cross entropy. It is better to keep the form of the loss consistent, since $y_{mix} = \sum_i y_i \lambda_i$, implies 

$\sum_i L_{ce}(\psi(x_{mix}), y_i) \lambda_i = \sum_i -\lambda_i y_i \log(\psi(x_{mix})) = \log(\psi(x_{mix})) \sum_i -\lambda_i y_i = -\log(\psi(x_{mix})) y_{mix} = L_{ce}((\psi(x_{mix}), y_{mix}))$


Equations 10 through 15 are badly formatted and hard to read. It is also unclear what the individual contribution of the four cross-entropy terms are, and a suitable way to choose $\alpha$ and $\beta$. 

Section 4.2 mentions the proposed method has the lowest calibration error, but there is no table showing the ECE of other baselines. Fig.4. shows the ECE of only the proposed method.


Typos and minor mistakes:
“to facility representation”
Mxiup → mixup
bad formatting  in eq 5
notation in eq 6, 7 is unclear. is the $*$ scalar multiplication?
what is meant by “inherent meaning of images” - this sounds slightly unscientific, this should be explained in a bit more detail 

Currently, I think the paper needs a lot of work - both in terms of coherence and motivation for the method. There are too many elements all over the place and it is unclear what the improvement actually comes from. The evaluation criteria is not standard (see Questions) and needs more justification. Therefore, I recommend an initial reject.

### Questions
The method compares the median of the top-1 test accuracy in the last 10 training epochs. Since adversarial methods are generally brittle and have unstable training dynamics, does the mean test accuracy fluctuate a lot? Also, it seems that there is no validation set used to choose the best checkpoint. This evaluation criteria is not justified in the paper.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a new augmentation technique. First it proposes hard samples to train and secondly a robustification of the classifier. The method is evaluated on 4 datasets

### Strengths
The idea to augment with hard examples is interesting. Furthermore, to iterate between augmentation and classifier is also interesting.
Showed results are strong.

### Weaknesses
I do not see any significant weakness. The method is harder to implement and it requires more resources that other augmentation techniques, but given the timeline of augmentation, it is expected

### Questions
None. I see this paper as a clear contribution.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent
