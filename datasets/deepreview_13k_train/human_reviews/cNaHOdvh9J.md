# Adversarial Latent Feature Augmentation for Fairness

- Decision: Accept
- Scores: 6, 8, 6, 6

## Abstract
Achieving fairness in machine learning remains a critical challenge, especially due to the opaque effects of data augmentation on input spaces within nonlinear neural networks. Nevertheless, current approaches that emphasize augmenting latent features, rather than input spaces, offer limited insights into their ability to detect and mitigate bias. In response, we introduce the concept of the "unfair region" in the latent space, a subspace that highlights areas where misclassification rates for certain demographic groups are disproportionately high, leading to unfair prediction results. To address this, we propose Adversarial Latent Feature Augmentation (ALFA), a method that leverages adversarial fairness attacks to perturb latent space features, which are then used as data augmentation for fine-tuning. ALFA intentionally shifts latent features into unfair regions, and the last layer of the network is fine-tuned with these perturbed features, leading to a corrected decision boundary that enhances fairness in classification in a cost-effective manner. We present a theoretical framework demonstrating that our adversarial fairness objective reliably generates biased feature perturbations, and that fine-tuning on samples from these unfair regions ensures fairness improvements. Extensive experiments across diverse datasets, modalities, and backbone networks validate that training with these adversarial features significantly enhances fairness while maintaining predictive accuracy in classification tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper solves unfairness issues in classification tasks, which is caused by data imbalance. They proposed adversarial latent feature augmentation method which identifies the possible unfair region in latent space and fine-tune the model to mitigate such unfair decisions. The experiments demonstrated that ALFA achieves better group fairness without compromising accuracy.

### Strengths
1. This paper presents an interesting perspective that biased model can be fine-tuned in an adversarial learning fashion. The key of the proposed method is to identify the unfair features in latent space, which is based on Zafar 2017's work with covariance formulation. Eq. 4 uses L_fair as an reference which help calculate the desired perturbation.
2. The concept of unfair region looks like an interesting idea for promoting fairness. This concept is an extension for adversarial learning in the context of fairness learning.
3. Algorithm 1 shows the overall procedure for fairness tuning, which is convincing and also easy to follow.

### Weaknesses
1. I realised the unfair region concept is defined by misclassification rate but the used fairness metric, i.e., EOd, is only for positive predictions. This misalignment has raised a big concern for the proposed method.
2. From my understanding, given any biased training set, the unfair region should be not only produced by the observed data and pre-trained model ,but also captured by the perturbation, i.e., augmented data. Is this the correct way to understand Fig.1?
3. It is widely believed that adversarial perturbation improves the robustness with the sacrifice of hurting the model performance on benign data. In the context of fairness learning, the performance drops for data samples which fall in the fair region will be affected. I understand during the tuning phase, i.e., Eq. 5, the benign data is also retrained to mitigate this issue. But any other strategies can be used?
4. The theoretical framework is highlighted in abstract while it is not clearly presented in the main body of the paper. Am I missing it?

### Questions
Please refer to the weaknesses.

My further questions are: (1) Adversarial learning idea is also used for learning sensitive invariant representation. I think the authors should discuss the connection with this branch of works. (2) Regarding the misclassification, should fairness metric like group utility difference, i.e., Rawlsian fairness, be used for the paper?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors propose a method to perturb latent space features, to augment the learning by highlighting areas where the performance within certain subgroups is sub-optimal. They support the methodology with theoretical analysis and thorough experiments, demonstrating the effectiveness of the method in reducing the bias, without compromising on the accuracy. The paper is extremely well written, presenting a novel approach, with strong motivation, solid backing for the methodology both empirically and theoretically and detailed discussions and code.

### Strengths
- [S1] Well motivated paper, particularly from the point of view of understanding how to use the latent space better to reduce biases in neural networks. Lot of the literature as the authors mention is quite superficial with respect to justifying the methodology with intuition or analysis for why it works for any random latent space.
- [S2] Objective $\mathscr{L}_{fair}$ seems well defined and linked to Equalized Odds in the appendix. Proof overview looks fine.
- [S3] The use of Sinkhorn over Wasserstein is a clever experimental choice, which sidesteps a lot of computational issues associated with such algorithms.
- [S4] Inclusion of clean and well written code is a big plus towards implementation of the proposed method.
- [S5] The plotting of Pareto curves as opposed to simply singleton points in Figure 4 and Figure 5 is a pleasant sight to understand the patterns across different fairness-accuracy tradeoffs.

### Weaknesses
 - [W1] Visualization of the latent space of real world datasets (say via PCA), for smaller ones at least perhaps akin to the figures for synthetic datasets, would help understand the unfair regions a bit better.
- [W2] I am slightly concerned about the practicality of the proposed approach in high dimensional latent spaces, do the authors have thoughts or any experiments about how the method scales with (keeping everything else constant) a) Input Feature Dimensions b) Latent Space Dimension

### Questions
- [Q1] With regards to [S3], is there a comparison available for usage of Wasserstein over Sinkhorn, in terms of possible gain in performance at the cost of some computational overhead? Could it be feasible for smaller datasets like German/COMPAS? An additional analysis in Appendix Section D would prove insightful to support this choice.
- [Q2] Is there analysis for how the covariance of the label and sensitive attribute affect the effectiveness of the method? I like the table in Section E of the Appendix, but I would be curious to know under what regimes is the method particularly effective? Also what if the covariates shift from train to test? Is the Table E for only the train data? Would be nice to see some more discussion along these lines as I think it could shed some light on the practical scenarios in which the proposed method would be most effective.

### Soundness
4

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
4

### Summary
This paper introduces ALFA (Adversarial Latent Feature Augmentation), an approach to enforce Equalized Odds fairness in binary classification through adversarial data augmentation. The method generates adversarial perturbations in the latent space by maximizing the covariance between sensitive attributes and logits of the predicted probability. The approach operates in two phases: first creating biased latent features through fairness attacks, then fine-tuning on both original and perturbed features using a dual cross-entropy loss to balance fairness and accuracy. Comprehensive experiments across multiple datasets (Adult, COMPAS, German, Drug, Wikipedia and CelebA) demonstrate ALFA's effectiveness in improving Equalized Odds while maintaining competitive predictive performance.

### Strengths
- The paper presents a novel integration of adversarial perturbations and data augmentation in latent space to address fairness constraints.
- The proposed method achieves competitive results

### Weaknesses
1) **Problem Formulation and Distribution Mismatch:**
The fairness enforcement is performed on artificially balanced demographic data (n00 = n01 = n10 = n11), while the test distribution could be imbalanced. This fundamental distribution mismatch is not adequately addressed.
The method achieves Demographic Parity proportional to Equalized Odds on this really specific case, which contradicts the known incompatibility between these metrics and loses the essential dependence between Y and A.

2) **Incomplete Baseline Comparisons:**
The experimental comparisons raise concerns about completeness and fair representation of SOTA methods:
On standard datasets (German/Adult and Wikipedia - Figure 6), the method achieves EO violations no better than 0.1, while existing approaches [1] show that Zafar et al. (2013) using covariance loss, typically achieve EO violations close to 0.03 under the same test conditions on adult uci(20% test split).
This performance gap suggests the experimental evaluation may not fully represent the capabilities of existing state-of-the-art methods

3) **Technical Gaps:**
The methodology lacks sufficient technical explanations and critical implementation details are missing, particularly regarding the generation of δ

### Questions
The authors' responses have addressed most of my concerns. Based on the current revision, I have updated my rating to 6.

##################################


Upsampling Strategy and Distribution Mismatch:

1) How is the upsampling implemented - are instances repeated multiple times to achieve Np = 4 · max(n00, n01, n10, n11)?
2) My main concern is regarding that the fairness improvement by reducing ∆EOd (i.e., ∆EOd(θp) ≤ ∆EOd(θ)) is demonstrated on this upsampled distribution rather than the original dataset. For a test set (20% of the original data) that maintains its original unbalanced distribution, how does your method guarantee fairness on the test data, particularly with highly unbalanced combinations of A and Y?  Being fair on the upsampled training data does not necessarily imply fairness on the original distribution present in your test set.

Training Procedure:

3) Why does the method use a single pass of the two-step process, unlike traditional adversarial learning approaches where the adversary and model are iteratively updated multiple times? 

Technical Details of δ Implementation:

4) How exactly is δ maximized? Is it implemented as a neural network trained via gradient descent?
5) Does the maximization of δ take $X_p$ as input?
6) What mathematical constraints ensure proximity in latent space? Are there Lipschitz constraints on δ maximization?

Loss Function Balance:

7) Equation 5 uses equal weighting between the balanced and unbalanced distributions, which shifts half the focus to the upsampled distribution. Without a hyperparameter to control this split, how can the model maintain proper task accuracy? Even when fairness enforcement is not needed (i.e., when α approaches infinity), the attention remains partially shifted to the balanced distribution $D(X_p,Y_p,A_p)$, which could differs from the test distribution.

8) Could this equal weighting explain why your method shows lower accuracy than SOTA in the unfair regions of Figure 4? Additionally, the blue curve is largely absent in unfair regions (high α values) except for Adult UCI dataset. Did other datasets also show poor performance in these regions with higher values of α?"

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a novel bias mitigation approach that leverages adversarial attacks on model fairness to augment samples in the latent space region where the model makes the most mistakes. The last layer of the model is then retrained with augmented latent features to correct the decision boundary for better, fairer predictions. The proposed method is evaluated on several benchmarks, showing the improvement over the baseline methods considered. Theoretical insights also back the proposed method.

### Strengths
1. The paper is well-written, well-organized, and relatively easy to follow. 
2. The counterintuitive idea of using fairness attacks on a pretrained model to mitigate bias is interesting and novel. 
3. The experiments are thorough and spanned across different types of datasets and model classes.
The proposed method is flexible and can be adapted to different types of fair constraints. 
4. The results demonstrate the effectiveness of the adversarial data augmentation method in mitigating bias, and the theoretical results are intuitive.

### Weaknesses
1. While Figure 1 provides an intuitive comparison with related work, the related work section can be improved to amplify the paper's position. In particular, using adversarial learning to identify regions where the model makes the most mistakes is not novel and has been studied before by `Lahoti, Preethi, et al.` [1].  I recommend the authors discuss this work and consider it as a baseline for comparison. The authors should clarify how their method addresses imbalanced demographic distributions, as methods like ARL are designed to handle such scenarios. Specifically, it's unclear how a small demographic group with a high false positive rate would contribute minimally to the overall loss, and why ALFA would not face the same issue, given that the fairness attack relies on the pre-trained model's decision boundary. Furthermore, the claim that ALFA is more computationally efficient than ARL needs further justification, especially since ARL can also be applied to latent representations with a linear adversary, similar to the last-layer fine-tuning in ALFA. The authors should also acknowledge that ARL operates without demographic information, making it applicable in broader settings, and discuss how ALFA can reduce its reliance on demographic data.
2. The proof of theorem 3.2 seems to rely on the assumption that samples from high error regions mostly influence the gradient updates. This seems to depend on the success rate of the fairness attack, and the authors did not demonstrate that the attack can fully construct `R_unfair`.  I suggest to clarify the assumptions used in theorem 3.2. The authors should clarify the relationship between $d_i$ and $\hat{y}_{i}$ in measuring the corresponding fairness metrics, particularly how $d_i$ is restricted to positive outcomes as measured in $\Delta DP$. Additionally, the assumption of a piecewise linear function should be discussed in the context of real-world data, and the interpretation of the constants ($C, C_0, C_1$) in the upper bounds, which measure the difference in the number of samples in each group within each segment, should be clarified.
3. It is suggested the author could perform additional experiments to show the success rate of the fairness attack on real datasets, i.e., the unfair region is actually the region targeted by the fairness attack. This will support the assumption that the attack can effectively identify `R_unfair` and oversample data points from that region. For example, predicting the accuracy of a sensitive attribute classifier in these regions and comparing it with the ground truth `R_unfair`. These experiments showing that the fairness attack effectively augments data points in the ground truth `R_unfair` would support the inherent assumption made in theorem 3.2.  
4. Some parts of the paper can be improved for clarity; for example, in Figure 4-6, some baseline methods have fewer tradeoff points than others; the number of parameters controlling the tradeoff between $\Delta_{EOD}$ and Acc. should be provided. In Fig. 2(a), providing the decision boundary for different perturbation levels $\delta$ might provide better insight into the magnitude of the fairness attack over the corrected boundary. Furthermore, the authors should clarify why the corrected model has better fairness for $\alpha=1$ than for $\alpha=0$ in the newly added Figure 8, and what happens for intermediate values of $\alpha$ (e.g., $\alpha=0.5$). The role of $\alpha$ in controlling fairness in the corrected model needs further explanation, as it is counterintuitive that a less pronounced fairness attack results in better fairness.
5. Throughout the paper (e.g., Line 137), it’s stated that the method improves group fairness _without compromising accuracy_; as the results show the tradeoff between fairness and accuracy, the statement should be updated to reflect this fact. For example, the authors formulate the statement as "_improves group fairness while maintaining accuracy_ (as much as possible)". This would highlight the fact that there is a potential tradeoff. The method also fails to efficiently control the trade-off between fairness and accuracy, which is a critical issue for practitioners. The authors should address this limitation and provide actionable tools for satisfying specific fairness levels.

### Questions
Please see the above Weaknesses section.

### Soundness
3

### Presentation
3

### Contribution
3
