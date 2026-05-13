# A Brain-Inspired Regularizer for Adversarial Robustness

- Decision: Reject
- Scores: 3, 3, 3

## Abstract
Convolutional Neural Networks (CNNs) excel in many visual tasks, but they tend to be sensitive to slight input perturbations that are imperceptible to the human eye, often resulting in task failures. Recent studies indicate that training CNNs with regularizers that promote brain-like representations, using neural recordings, can improve model robustness. However, the requirement to use neural data severely restricts the utility of these methods. Is it possible to develop regularizers that mimic the computational function of neural regularizers without the need for neural recordings, thereby expanding the usability and effectiveness of these techniques? In this work, we inspect a neural regularizer introduced in Li et al. to extract its underlying strength. The regularizer uses neural representational similarities, which we find also correlate with pixel similarities. Motivated by this finding, we introduce a new regularizer that retains the essence of the original but is computed using image pixel similarities, eliminating the need for neural recordings.  We show that our regularization method 1) significantly increases model robustness against a variety of black box attacks, 2) relies only on original, unaugmented datasets and 3) is computationally inexpensive. Our work explores how biologically motivated loss functions can be used to drive the performance of artificial neural networks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper inspects an existing neural regularizer to establish that the idea can be used for image pixel similarities without the use of actual neural recordings. Based on this observation, the authors propose a new regularization method based on two hyperparameters and eliminating the need for neural recordings. It is evaluated for different adversarial attacks and grayscale and colored datasets. Based on the selected threshold value, the target similarity matrix is calculated. The method is tested against transferable FGSM and Boundary attack as well as common image corruptions.

### Strengths
- The proposed method eliminates the need for neural recordings, which are generally expensive.
- Well-motivated, intuitive, and simple method to eliminate the actual neural recordings. 
- Computationally light method.

### Weaknesses
 - The authors mention, "our aim is not to come up with the best adversarial defence ..." on lines 519-521, which contradicts the title and the paper content that gives an impression the proposed method is to improve the adversarial robustness of the existing networks. 
- The authors should discuss the preliminary details/definitions they use frequently from the baseline paper. For example, what are the classification and regularization datasets? 
- While the improvement on the common corruptions is good, the evaluation of adversarial robustness is incomplete. The method is only tested against transferable FGSM and Boundary attacks. More robust evaluation with stronger white-box [1, 2] and black-box attacks [3] should be done to claim adversarial robustness. Specifically, the evaluation lacks adaptive attacks, which are crucial for assessing the true robustness of a defense mechanism. The current evaluation is limited to simple transfer-based attacks, which are not sufficient to demonstrate the effectiveness of the proposed method against a determined adversary.
- Evaluation is only limited to one CNN architecture - ResNet18. More evaluation of diverse architectures and models like WideResNet will provide additional evidence for the claims. The performance of the proposed method might be highly dependent on the specific architecture, and thus, testing on a wider range of architectures is necessary to generalize the findings. Furthermore, the depth and width of the network can significantly impact the effectiveness of regularization techniques, and this aspect is not explored.
- In Section 2, the adversarial attacks mentioned are very old. The newer, more effective, and stronger attacks are not included. Similar observations are made for the adversarial defense subsection in Section 2.   
- Minor typos - "imageNet" instead of "ImageNet" on line 389, every equation is referred as "eq. equation " instead of "Eq. " or "Equation ",  

### Questions
My main concern is the contradictory claims in the paper. Please refer to the weakness section for more questions and details.

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
3

### Summary
Inspired by the work of Li et al. (2019) and guided by the observation that pixel similarities in the original image exhibit a pattern similar to neural recordings, the authors propose a new regularization method to improve neural network robustness with a significant reduction in computational requirements. As claimed by the authors, the proposed method also applies to colour datasets and has been tested on ResNet18 using CIFAR10, CIFAR100, and ImageNet with Gaussian noise and some black-box attacks.

### Strengths
1. The idea presented in the paper is interesting.
2. Lots of experiments have been conducted to support the conclusions.
3. The paper considers various aspects of robustness, including both *adversarial robustness* and *common corruptions*.

### Weaknesses
1. There are lots of obvious grammar, abbreviation, and citation errors in the paper. Aside from the grammar mistakes, such as in line 12 of the Abstract where it says "... but they tend to sensitive ..." which should be "... they tend to be sensitive...", nearly all equation references are incorrectly formatted. It should be "Equation" or "Eq." instead of "eq.equation." Additionally, please check the references you've used. For instance, on lines 83-84 of page 2, you incorrectly cite Szegedy et al. (2013) ... Madry et al. (2017) without proper formatting. A parenthesis is likely needed here; please refer to the formatting instructions in section 4.1. You should review the paper at least once before submission.
    
2. The writing and organization of the paper are very vague and confusing. In the Introduction section on page 2, you list six contributions of your work. However, some of these contributions are too trivial to be included as a separate item. For example, in the fourth contribution, you state: 'We assess the robustness of the regularized models to common corruptions using the CIFAR-10-C dataset (Hendrycks & Dietterich, 2019a).' I do not believe this alone is substantial enough to be listed as a contribution. Some contributions could be combined. In the last contribution, you mention: 'We show that our regularization method primarily protects against high-frequency perturbations…,' which explains the mechanism behind your proposed method but does not stand alone as a contribution. Instead, the sentence on lines 74-75 serves more as a contribution but is not included in the contributions list.
 
3. Outdated related works. In the related works section, the most recent work you mention on adversarial attacks is from 2017, which was published seven years ago. You should include at least one recent study. Additionally, the most recent work across all of your related works is Kireev et al. (2022), which is only mentioned once. I suggest incorporating a broader scope of more up-to-date works.

4. Some concepts are not clearly explained. On page 3, lines 137-138, you mention S_{i,j}^{target} as the target's pairwise cosine similarity, but it is unclear what 'target' refers to. The explanation of this term is insufficient, and the reader is left to guess the meaning of this crucial component of the proposed method.

5. Some of your claims need clearer evidence. On page 4, lines 162-166, you mention a similarity in the pattern of correlation between neural representational similarity and image pixel similarity, but the only evidence provided is Fig. 2, which is not convincing on its own. Additionally, your explanation of Fig. 2 is quite vague. For example, in the leftmost figure of Fig. 2, I see r=0.83, but there is no explanation provided for this value. The correlation value alone is not sufficient to justify the claim of similarity, and the lack of explanation for the correlation coefficient further weakens the argument.

### Questions
1. As stated in your second contribution, 'We show that our regularizer drives the network to be more robust to a wide range of black-box attacks,' and since all your experiments are based on ResNet18, I am curious whether this method would work for different architectures, such as MLPs.

2. Since FGSM is $L_infty$ based and considered one of the weakest attack methods, I am curious whether your proposed method would still be effective against more advanced transfer attacks.  

3. In Section 4.6, you attempt to demonstrate that your method is computationally inexpensive, but it is quite confusing to understand why this is the case from Fig. 8. Could you provide any plots related to computational complexity or time to support your argument?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper introduces a new, brain-inspired regularizer for CNNs that enhances robustness against adversarial attacks without needing neural data. By using pixel-based similarity measures instead of neural recordings, the proposed method simplifies implementation and makes the regularization process computationally efficient. Tests across several datasets and adversarial attacks (e.g., Gaussian noise, FGSM, and Boundary Attacks) show that this approach achieves significant robustness. Though it doesn’t outperform the latest adversarial defenses on all fronts, it holds promise for practical applications requiring efficient and accessible methods for adversarial robustness. The findings highlight how neuroscience-inspired regularizers can improve machine learning models without heavy data dependencies.

### Strengths
The strengths of this paper include an accessible regularizer that enhances robustness without neural data and computational efficiency by avoiding data augmentations.
I find the brain-inspired motivation of the paper also worthwhile.

### Weaknesses
There are many weaknesses.
The authors only tested on CIFAR. I could not see any tests comparing with the large amount of defenses available today.
The paper is heavily based on the paper from Li 2019.
I find the presentation to be lacking. There are no figures explaining the bioinspiration or the motivation behind the method,  or even how does this differs from the work from Li 2019.
The improvement from regularization looks very similar to the ones achieved by simple adversarial training.
The choice of attacks could. have been more diverse. L0 and Linfty attacks with both white and black box types are the standard for evaluation.

### Questions
How does the method presented compare with current defenses?

### Soundness
3

### Presentation
2

### Contribution
1
