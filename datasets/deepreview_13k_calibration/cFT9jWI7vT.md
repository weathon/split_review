# Towards Architecture-Insensitive Untrained Network Priors for Accelerated MRI

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 6, 3, 6

## Abstract
Untrained neural networks pioneered by Deep Image Prior have recently enabled MRI reconstruction without requiring fully-sampled measurements for training. Their success is widely attributed to the implicit regularization induced by suitable network architectures. However, the lack of understanding of such architectural priors results in superfluous design choices and sub-optimal outcomes. This work aims to simplify the architectural design decisions for DIP-MRI to facilitate its practical deployment. We observe that certain architectural components are more prone to causing overfitting regardless of the number of parameters, incurring severe reconstruction artifacts by hindering accurate extrapolation on the un-acquired measurements. We interpret this phenomenon from a frequency perspective and find that the architectural characteristics favoring low frequencies, i.e., deep and narrow with unlearnt upsampling, can lead to enhanced generalization and hence better reconstruction. Building on this insight, we propose two architecture-agnostic remedies: one to constrain the frequency range of the white-noise input and the other to penalize the Lipschitz constants of the network. We demonstrate that even with just one extra line of code on the input, the performance gap between the ill-designed models and the high-performing ones can be closed. These results signify that for the first time, architectural biases on untrained MRI reconstruction can be mitigated without architectural modifications.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This study investigates the performance of untrained neural networks for MRI reconstruction tasks. To address the unclear architecture design choice for achieving good reconstruction quality, the author come up with two observations:
1. The noise input with low frequency constraint helps to improve the reconstruction quality.
2. The introduction of a collection of learnable Lipschitz constant can fix the performance gap among different model architectures.

On the two MRI datasets, the paper shows that proposed approaches can stablize the reconstruction performance across models with different kind of hyper-parameters.

### Strengths
1. Investigating the untrained neural networks (Deep Image Prior) on MRI reconstructions is new and interesting.

2. The proposed approaches are simple and can be easily reproduced assume the baseline codes are accessible.

3. With such minor modifications, the new method outperforms the baseline DIP method.

### Weaknesses
1. Thought the idea of applying DIP to MRI reconstruction sounds interesting, I am worried about the potential impact this study can reach.
Considering the unclear trade-off between the additional optimization time per each image VS the one-time training budget, I don't think this idea is well motivated for medical image application. To address this, the authors could either present the table of estimated optimization runtime. Or the authors could show DIP-related methods clearly outperform the standard supervised methods.   


2. It seems to me that the model hyper-parameter insights are derived from the baseline CNN model, it would really enhance the paper if the architecture study could have included detailed transformer or nas experiments, other than a short discussion presented in the introduction.

### Questions
Please see the above weakness section.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper focuses on improving the reconstruction of Magnetic Resonance Imaging (MRI) data from under-sampled measurements. It introduces untrained networks inspired by the "deep image prior" concept, which relies on architecture rather than paired measurements. The study systematically analyzes the impact of architectural components on MRI reconstruction quality, leading to the identification of influential factors. The paper proposes architecture-agnostic remedies to mitigate overfitting in underperforming networks, enhancing reconstruction efficiency and robustness.

### Strengths
1) The paper conducts a systematic and comprehensive analysis of the architectural influences of "deep image prior" like methods on MRI reconstruction. It identifies key components that affect reconstruction quality, providing valuable insights for researchers and practitioners. To my knowledge, this has not been investigated before in the way that the paper does.
2) Motivated by their investigation, the authors propose architecture-agnostic remedies to mitigate overfitting in underperforming networks are practical and computationally efficient, offering a solution to enhance reconstruction efficiency without extensive architectural modifications.
3) The paper supports its findings with extensive experiments, demonstrating the effectiveness of the proposed methods.
4) The paper is well-structured and effectively communicates its methodology, findings, and contributions, making it accessible to a broad audience.

### Weaknesses
1) The study primarily focuses on MRI reconstruction, which is a specific application in medical imaging. "deep image prior" like methods are generic and I wonder what modifications, if any, are required to make the proposed solutions work for other domains. It's unclear if the architectural insights gained here would directly translate to tasks like natural image denoising or super-resolution without significant adjustments. The paper should address the generalizability of its findings beyond the specific context of MRI.
2) The paper heavily emphasizes the architectural aspects of the problem, but it does not explore other potential factors that might affect MRI reconstruction quality, such as data acquisition protocols. Do the authors observe any different conclusions when the data undersampling factor is changed? It's important to understand if the identified architectural remedies remain effective under varying undersampling rates, or if different strategies are needed for more aggressive undersampling. The lack of exploration of data acquisition parameters limits the scope of the study.
3) There is limited discussion on how the hyperparameters were selected? Are there any practical recommendations on how to select hyperparameters such as sigma of Gaussian blur etc.? Will it depend on the degree of under sampling in the data? The paper would benefit from a more detailed analysis of the hyperparameter selection process, including a discussion on how these parameters interact with the degree of undersampling and the network architecture. Without clear guidelines, the practical applicability of the proposed methods is diminished.

### Questions
Please see weaknesses above

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
This paper introduces an enhanced version of the deep image prior for MRI reconstruction. The contributions include the proposal of an optimized architecture (specifying width, kernel size, etc.) tailored for a specific experimental setup. Notably, the approach incorporates input coordinates instead of relying solely on white Gaussian noises and integrates Lipschitz Regularization into the training loss. The experimental validation is conducted on the fastMRI dataset, focusing on a 4x acceleration factor scenario.

### Strengths
- Comprehensive investigation on the architecture of deep image prior.
- This paper is in general easy to follow (though with some unclear parts, see weakness below).

### Weaknesses
 - Overclaim: The author claims that the proposed architecture demonstrates optimal performance, a claim primarily based on observations from a specific data setup. Such a conclusion lacks merit without theoretical justification or validation across diverse data setups. It remains unclear if the proposed architecture would yield similar results in other scenarios. Notably, the comparison against a fully-sampled ground truth, while foundational, is impractical in real-world applications.

- Lack of Novelty: The realm of MRI reconstruction networks has reached a saturation point in performance (see also the results shown on the fastMRI leaderboard). Therefore, any new approach must offer a distinct advantage absent in existing methods. While incorporating input coordinates and applying Lipschitz regularization might be novel in the context of DIP for MRI, these contributions might not significantly impact the broader MRI reconstruction community.

- Performance: The fastMRI 4x acceleration challenge is widely acknowledged as non-challenging for deep learning models. Reference to Table 12 in the fastMRI dataset paper (https://arxiv.org/pdf/1811.08839.pdf) indicates that classical TV methods, despite being non-learning-based, yield comparable results to those presented in this paper (both in terms of PSNR and SSIM). Furthermore, the UNet results outperform the proposed method by a significant margin.

- The authors' conclusions are based on a limited exploration of architectures within a specific dataset (fastMRI) and problem (4x MRI reconstruction). The observed patterns, such as the importance of low-pass filtering, are derived from this narrow context. It is questionable whether these heuristic observations can be generalized to different datasets or reconstruction problems. A more robust approach would involve either theoretical justification for the observed patterns or validation across diverse datasets and tasks.

- The paper compares against Self-Validation (Yaman et al., 2021), but the reported performance is significantly worse than what was originally reported in that work. This discrepancy raises concerns about the implementation or experimental setup. The authors should address this discrepancy and explain why the Self-Validation baseline performs so poorly in their experiments, especially considering that it utilizes a deep unfolding architecture which should be more robust than the standard DIP network.

### Questions
- Why does the author not compare against with end-to-end learning method, such as Unet or some deep unfolding baseline like VarNet?
- The Brain setup in Table 6 seems never been mentioned in this paper.

### Soundness
1 poor

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper tackles the overfitting issue of untrained networks from the perspective of non-architectural interventions. Specifically, the authors propose to (1) low-pass filter the network input, and/or (2) penalize the Lipschitz constant of the network to encourage more smoothness in the output and to prevent the network from overfitting.

### Strengths
The paper is overall well-written with a smooth flow.

The paper is filled with interesting and valuable experiments. The most prominent examples are Fig. 4, Fig. 6, and Tab. 4.

The idea of low-pass filtering the input noise with the goal of regularizing the smoothness-artifact trade-off in the output reconstruction is impressive. Likewise its effectiveness in lifting up the performance of under-performing models.

### Weaknesses
The problem has a rich literature, some of which are already cited by the authors. What is missing is comparison to those baselines. e.g., self-validation based early stopping is also a non-architectural (and popular) regularization to avoid overfitting. Thus, it’s essential to compare against that baseline (and potentially a few more). The authors have confined themselves to a mere disadvantages summary of such important baselines in the introduction.

Section 4 is presented as the first systematic study on architectural dependencies of untrained networks. However, it is redundant with the investigations already done in the literature. e.g., [1] Appendix B already discusses such design choices conclusively.
[1]Darestani, M.Z. and Heckel, R., 2021. Accelerated MRI with un-trained neural networks.  IEEE Transactions on Computational Imaging,  7, pp.724-733.

A very interesting case to explore would be investigating architectures that still incur overfitting after applying the proposed regularizations; something not explored in the paper. Specifically, it would be valuable to see if the proposed method can completely eliminate overfitting for some architectures or if it only mitigates it. This would provide a better understanding of the limitations of the proposed approach.

Minor

The space before “(“ is often omitted. e.g., many cases in  paragraphs 2&4 of page 3.

Since section 4.1 is also and experimental section in its nature, it’d be useful to have the dataset setup here (similar to section 4.2 or 6). This is because untrained networks require different architectures for each anatomy.

### Questions
- Fig. 3 claims deeper and narrower networks are less prone to overfitting. However, the metric to draw this conclusion isn’t fair. Instead of measuring the absolute masked SSIM curves, one should measure the slope of the fall and the convergence value since it isn’t surprising to see deeper networks overfitting at later stages during the course of optimization.

Furthermore, the claim tries to partly deliver the point that #parameters isn’t the primary factor in overfitting; however, the 2-layer 256-channel network has indeed 4x more parameters compared to the 8-layer 64-channel network according to Tab. 3, and therefore more prone to overfitting because of its #parameters?
Finally, is Fig. 3 averaged over multiple examples or only the results of one sample? If it’s just one sample, it’d be hard to draw such bold conclusions.

- What are the authors’ thoughts on using their method for 8x? The reviewer fully understands that given the limited rebuttal time, it’s not reasonable to ask for conclusive 8x experiments. But given the fact that the difference between untrained and trained networks enlarges by going from 4x to 8x acceleration, would it be possible to claim that the proposed regularization schemes may help reducing that gap?

Minor

- Isn’t there a better way to design Tab. 2? Because currently, the labels Depth, Width, Kernel size, and Skip connections are placed in a very confusing way.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
