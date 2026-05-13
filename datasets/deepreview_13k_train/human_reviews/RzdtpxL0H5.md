# DDAD: A Two-Pronged Adversarial Defense Based on Distributional Discrepancy

- Decision: Reject
- Scores: 6, 6, 8, 5, 6

## Abstract
Statistical adversarial data detection (SADD) detects whether an upcoming batch contains adversarial examples (AEs) by measuring the distributional discrepancies between clean examples (CEs) and AEs. In this paper, we reveal the potential strength of SADD-based methods by theoretically showing that minimizing distributional discrepancy can help reduce the expected loss on AEs. Nevertheless, despite these advantages, SADD-based methods have a potential limitation: they discard inputs detected as AEs, leading to the loss of clean information within those inputs. To address this limitation, we propose a two-pronged adversarial defense method, named Distributional-Discrepancy-based Adversarial Defense (DDAD). In the training phase, DDAD first optimizes the test power of the maximum mean discrepancy (MMD) to derive MMD-OPT, and then trains a denoiser by minimizing the MMD-OPT between CEs and AEs. In the inference phase, DDAD first leverages MMD-OPT to differentiate CEs and AEs, and then applies a two-pronged process: (1) directly feeding the detected CEs into the classifier, and (2) removing noise from the detected AEs by the distributional-discrepancy-based denoiser. Extensive experiments show that DDAD outperforms current state-of-the-art (SOTA) defense methods by notably improving clean and robust accuracy on CIFAR-10 and ImageNet-1K against adaptive white-box attacks. The code is available at: https://anonymous.4open.science/r/DDAD-DB60.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a two-pronged adversarial defending method called distributional-discrepancy-based adversarial defense, leveraging the maximum mean discrepancy. After training, the model could fist distinguishes between clean inputs and adversarial examples and then denoise the attacks before feeding them into the classifier. The paper conducts experiments on two datasets to demonstrate the effectiveness of the proposed method against attacks.

### Strengths
1.This paper is well-motivated and the idea of this paper is clearly explained.

2.The paper provides theoretical proofs and algorithms for the proposed idea.

3.The experiments are conducted across multiple datasets using various backbone architectures. The performance compared with the baseline methods demonstrates the effectiveness of the proposed method.

### Weaknesses
The following questions need more explanation:

1. The authors use Assumptions 1 and 2, along with Corollary 1, to establish that the ground truth labeling functions are equivalent for both the source and target domains. While it is true that clean examples and adversarial examples are actually using the same model, Assumption 1 needs further explanation. If $f_A$ represents a valid ground-truth labeling function specifically for the adversarial domain, why should it yield the same prediction for both adversarial examples $x+\epsilon'$ and clean examples $x$? Specifically, the assumption that a ground truth labeling function $f_A$ exists for the adversarial domain and that it is invariant to adversarial perturbations needs more rigorous justification. The paper should discuss the conditions under which this assumption holds, and acknowledge scenarios where it might not.

2. In the experiments, the threshold for MMD-OPT is set to 0.05. How was this threshold selected? The paper lacks a clear explanation of the process used to determine this value. It is unclear if this threshold is optimal or if it was chosen arbitrarily. A sensitivity analysis of the threshold on the performance of the proposed method should be included to justify the choice of this specific value. The impact of this threshold on both clean and robust accuracy needs to be explored.

3. The Evaluation Settings section in the paper lacks clarity. Are the baseline methods evaluated using AutoAttack, while the proposed method is evaluated with the adaptive white-box attack? Could you report the results under the same attack, for example, consider the entire process as a classifier and calculate the accuracy for defending adversarial examples from either AutoAttack or PGD+EOT. The current evaluation makes it difficult to compare the proposed method with existing approaches under identical conditions. The lack of a unified evaluation protocol raises concerns about the fairness of the comparison.

### Questions
Please see the weaknesses section. I will leave my rating for now and wait for the discussion.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The method proposed in this paper achieves significant improvements in both clean and robust accuracy compared to existing SOTA defense methods. It introduces a novel framework that enhances model robustness without the need to incorporate a large number of additional samples, which is particularly interesting.

### Strengths
The DDAD proposed in this article effectively avoids information loss.
Without relying on a large amount of additional data, DDAD has significantly improved its robustness on datasets such as CIFAR-10 and ImageNet-1K.
DDAD also has good scalability and can cope with unseen transfer attacks. Therefore, DDAD is able to defend against adversarial samples generated based on different models in a gray box environment, indicating that its defense capability can be generalized across models.

### Weaknesses
The paper has some limitations. 
First, it does not provide open-source code or detailed instructions to replicate the results, making it difficult for others to validate the findings. 
Second, the assumptions in Equation 4 are not fully extended to components like Batch Normalization layers, pooling layers, or transformer structures. Rather than simply showing added structures as in Figure 2, a more comprehensive explanation is needed to clarify how Equations 4,5, and 6 apply to these components.

### Questions
1. Could you provide more details or release code to help replicate the reported results?
2. How do the assumptions in Equation 4 extend to complex components like Batch Normalization (BN) layers, pooling layers, and transformer structures?
3. Given that DDAD performs well on CIFAR-10 and ImageNet-1K, how does it scale with even larger datasets or different image domains?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
Current Statistical adversarial data detection-based methods discard inputs that are detected as AEs, leading to the loss of clean information within those inputs. This paper, first theoretically establishes a relationship between adversarial risk and distributional discrepancy. Motivated by this, the paper proposes a two-stage defense method where during training they train a denoiser model to minimize the MMD-OPT between clean and adversarial examples. During inference, they first distinguish between the CE and AE, the clear examples are passed straight to the classifier, whereas the adversarial samples are passed through the denoiser first.

### Strengths
- The paper is well-written and has clear details.
- The authors conduct extensive experiments and provide theoretical motivations. 
- The proposed method, while relating to work in Certified Robustness, is novel to my understanding, and leads to significantly better results.

### Weaknesses
During inference, the authors assume access to a batch of clean validation data to serve as a reference for measuring distributional discrepancies. How are the constituents of this batch selected? For example, does it represent samples from each class uniformly, or does it follow the empirical distribution? Additionally, what would happen to performance if an attacker, for instance, supplied only samples from a single class along with one or two adversarial samples? Since detection is performed at the batch level, would the entire batch be classified as “clean samples”?

I am also concerned about the method's reliance on the composition of the reference batch. It is unclear how sensitive the method is to shifts in the input distribution. For example, if the reference batch is drawn from the training distribution, how would the method perform when presented with slightly out-of-distribution samples, such as those from CIFAR-10.2, CIFAR-C, or CIFAR-P? Would these samples be incorrectly flagged as adversarial, leading to unnecessary processing by the denoiser? This aspect needs further investigation to fully understand the practical limitations of the proposed approach.

Potentially missing related work?
	- Nayak et al. [1] also investigated using an MMD-based loss to train a denoiser for adversarial defense.

### Questions
- Please see the weaknesses.
- Potentially missing related work?
	- Nayak et al. [1] also investigated using an MMD-based loss to train a denoiser for adversarial defense. 

[1] Nayak, G. K., Rawal, R., & Chakraborty, A. (2023). DE-CROP: Data-efficient certified robustness for pretrained classifiers. In Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision (pp. 4622-4631).

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
Statistical adversarial data detection (SADD) methods generally detect whether an upcoming batch contains adversarial examples (AEs) by measuring the distributional discrepancies between clean examples (CEs) and AEs, and would discard such detected batches containing AEs. In this paper, the former action of the SADD methods is viewed as a potential strength, whereas the latter action of SADD is viewed as a potential limitation since it leads to the loss of clean CEs within those detected batches containing AEs and also potential under-utilization of AEs. Motivated to remove the limitation, the paper proposes a two-pronged adversarial defense method, named Distributional-Discrepancy-based Adversarial Defense (DDAD), which consists of two phases: a training phase and an inference phase. In the training phase, DDAD first  establishes a suitable measure called MMD-OPT to compute the maximum mean discrepancy (MMD) between a clean batch and an AE batch, and then trains a denoiser by minimizing the MMD-OPT between CEs and AEs and the cross entropy loss of an underlying DNN classifier over the denoised AE batch. In the inference phase, DDAD first detects whether an incoming batch is an AE batch based on the  MMD-OPT between the incoming batch and a reference clean batch, and then applies a two-pronged process: (1) directly feeding the incoming batch into the classifier if it is detected as a clean batch, and (2) adding Gaussian noise into the incoming batch and feeding the noise inserted incoming batch into the trained denoiser followed by the DNN classifier if the incoming batch is detected as an AE batch. Experiment results on CIFAR-10 and ImageNet-1K in terms of both clean and robust accuracy are reported and compared with some benchmark methods in the literature. 

Along the way, a theorem is established to upper bound the error probability of a classifier under the distribution of AEs by the sum of the error probability of the classifier under the distribution of CEs and the variation distance between the distribution of CEs and the distribution of AEs. No independent performance results are reported for the MMD-OPT based detector and the trained denoiser.

### Strengths
1. If the problem is formulated in a right manner, the idea of using a detector plus a denoiser (or adversarial perturbation diffuser) is interesting and worth to be further investigated.

2. Developing Theorem 1 and using it to provide some theoretic justification for the denoiser training is commended, although it is simple and  there is a discrepancy between the variance distance and MMD. 

3. The first three sections are generally well written.

### Weaknesses
1. The major issue in this paper and the line of work following SADD lies in the problem formulation itself. The word ``statistical'' in SADD implies that one has to deal a batch of samples with each sample serving as an input to an underlying DNN. The discrepancy between the batch requirement and the normal operation of the underlying DNN accepting a single sample as an input and making a prediction in response to the input makes the problem formulation impractical. The discussions in Section 7 can hardly justify the use of batches in the inference stage. The examples provided therein are not convincing and actually not applicable to the current problem. Depending on the underlying DNN in use, in those applications, the set of images fed into the DNN should be regarded as one input to help the DNN make a prediction. 

2. Even if we accept batch inference as a hypothetic working mode of DNNs, this will change the attack surface, and the robust problem will likely take a different form. However, in the current set up, an AE is defined traditionally to be a perturbed input which causes the underlying DNN to make an erroneous prediction when the DNN is working in a normal inference mode, accepting a single input and making a prediction in response to the input. By shifting the inference working mode to a different form, it does not really solve the original robustness problem.

3. Theorem 1 can be easily proved for the multi-label classification setting as well. Although it can motivate to minimize the distribution discrepancy between CE data and AE data, there is a gap between Theorem 1 and Figure 1 in terms of distribution distance used, which is the variation distance in Theorem, and MMD in Figure 1. Is there any mathematical or empirical relationship between these two distribution discrepancies? 

4. Figure 1 is not well explained to certain degree. (1) Are the two classifiers therein the same? (2) How are AEs generated? Are they generated specifically for the same classifier? (3) How are test data on the right side attacked? (4) For attached test data, what is the probability for MMD-OPT to classify them as clean?

### Questions
1. In the paper, DUNET (Liao et al., 2018) is as the denosing model. What is the impact of the denoising DNN on the performance of the trained denoiser? If a different DNN architecture is used in the denoiser training, how would it interact with MMD-OPT? Will the performance dramatically different?

2. With reference to Figure 1, are results in Table 1 produced under the conditions that (1) the classifier used in the training phase (left of Figure 1)  is the same as the classifier used in the inference phase (right of Figure 1), and (2) adversarial samples used in the training phase (left of Figure 1) are generated specifically for the same classifier?

3. Results in Table 3 are now clear. What do you mean by  "our method trained on WideResNet-28-10 against unseen transfer
attacks on CIFAR-10. Notably, attackers cannot access the parameters of WideResNet-28-10, and thus it is in a gray-box setting."? Please see my questions on Figure 1 above and explain your experiment results with reference to components in Figure 1. 

4. In Equation (5), where is m?  Do you assume that m=n in this case?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents a new adversarial defense mechanism called Distributional-Discrepancy-based Adversarial Defense (DDAD), which leverages statistical adversarial data detection (SADD). Unlike previous SADD-based methods that discard inputs detected as adversarial examples (AEs), DDAD employs a two-pronged process, in which clean examples (CEs) are sent directly to a classifier, and AEs are denoised before classification. The method is founded on the concept of Maximum Mean Discrepancy (MMD), which measures the distributional discrepancy between CEs and AEs. In the training phase, DDAD learns a denoiser and optimizes MMD-based statistics to distinguish between CEs and AEs. Extensive experiments show that the proposed DDAD method outperforms existing adversarial defense techniques in both clean and robust accuracy across CIFAR-10 and ImageNet-1K, including against unseen transfer attacks.

### Strengths
1. The paper provides a theoretical rationale behind the efficacy of minimizing distributional discrepancies for adversarial examples. The clear connection between adversarial risk and distributional discrepancy minimizes arbitrary choices for its design.
2. Combining statistical methods (MMD) with denoising brings a fresh perspective compared to standard approaches like adversarial training (AT) or adversarial purification (AP), demonstrating improved robustness and clean accuracy.
3. The DDAD effectively combines statistical detection (SADD) and denoising processes, which retains clean accuracy while defending against adversarial attacks using a straightforward and computationally less-intensive method compared to purely denoiser-based defenses.

### Weaknesses
1. Identifying discrepancies using MMD is highly reliant on batch-wise processing, which introduces practical limitations, especially in single-instance or real-time applications. Although this is discussed in the ablation studies and limitations, no immediate solutions are provided beyond recommending larger batch sizes. The reliance on batch processing for MMD calculation means that the method's latency will scale linearly with the batch size, making it unsuitable for low-latency applications unless batching is carefully managed. Furthermore, the method does not address how to handle cases where the batch size is smaller than the minimum required for reliable MMD estimation.
2. The method shows a drop in performance when batches contain a mixture of CEs and AEs. This could be problematic in domains where AEs are sparsely distributed, and include cases where the relative mixture is unknown beforehand. The performance degradation with mixed batches suggests that the MMD-based detection is not robust to variations in the proportion of adversarial examples. This is a significant limitation, as real-world scenarios often involve unpredictable mixtures of clean and adversarial data. The method needs to be more robust to these variations to be practically useful.
3.  The method is evaluated only on image classification tasks (CIFAR-10, ImageNet-1K). It would have been valuable to explore the effect of DDAD on more diverse datasets, such as medical imagery, autonomous driving, or natural language processing tasks, which may hinge on differently structured features. The lack of evaluation on diverse datasets limits the generalizability of the findings. Image classification tasks may not fully capture the complexities of adversarial attacks in other domains, and the method's performance may vary significantly with different data modalities.
4. While the method is holistic, it introduces a somewhat complex series of steps (MMD optimization, denoiser training, and dynamic thresholding). Both the denoiser and classifier need careful training and calibration, making reproducibility potentially challenging. The multiple training stages and hyperparameter tuning requirements increase the complexity of the method, potentially making it difficult to reproduce and deploy in practice. The sensitivity of the method to these parameters needs to be thoroughly investigated.

### Questions
1. You propose MMD as the core of your discrepancy measurement. How would alternative statistical measures (e.g., Wasserstein distance, energy distance) perform, and what drawbacks are there to switching from MMD?
2. The two-pronged method relies on a clearly defined distributional discrepancy threshold (t = 0.05). Could you provide more details regarding the sensitivity of the model to this hyperparameter? Would adaptive or learned thresholds enhance robustness?

### Soundness
3

### Presentation
3

### Contribution
3
