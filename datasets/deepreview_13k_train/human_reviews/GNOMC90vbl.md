# Data-Driven Lipschitz Continuity: A Cost-Effective Approach to Improve Adversarial Robustness

- Decision: Reject
- Scores: 5, 5, 6, 5, 3

## Abstract
The security and robustness of deep neural networks (DNNs) have become increasingly concerning. This paper aims to provide both a theoretical foundation and a practical solution to ensure the reliability of DNNs. We explore the concept of Lipschitz continuity to certify the robustness of DNNs against adversarial attacks, which aim to mislead the network with adding imperceptible perturbations into inputs. We propose a novel algorithm that remaps the input domain into a constrained range, reducing the Lipschitz constant and potentially enhancing robustness. Unlike existing adversarially trained models, where robustness is enhanced by introducing additional examples from other datasets or generative models, our method is almost cost-free as it can be integrated with existing models without requiring re-training. Experimental results demonstrate the generalizability of our method, as it can be combined with various models and achieve enhancements in robustness. Furthermore, our method achieves the best robust accuracy for CIFAR10, CIFAR100, and ImageNet datasets on the RobustBench leaderboard.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work starts from Lipschitz continuity and enhances adversarial robustness by minimizing the empirical Lipschitz constant. Specifically, the authors propose a plug-in forged function that can be inserted before each convolutional layer and MLP layer to remap the input domain of each layer into a constrained set. The theoretical guarantee of this paper primarily demonstrates that the largest singular value of the parameter matrix can serve as a loose bound for the Lipschitz constant. Experimental results show that the forged layers can bring some improvement to existing adversarial training methods.

### Strengths
The logic flow of this work is coherent, and the writing is clear and easy to understand. The idea of optimizing the Lipschitz constant to achieve certified adversarial robustness is also a classic approach. The implementation is very straightforward, and the proposed forged function can serve as a plug-in module that integrates with any CNN or transformer-based model.

### Weaknesses
Theoretical side: The bound is somewhat too loose. This paper derives the final optimization objective through the Gershgorin Circle Theorem, but this bound lacks guarantees due to the multiple assumptions made. Specifically, while the Gershgorin Circle Theorem provides a bound on the eigenvalues, it does not guarantee that minimizing this bound will directly translate to a tighter Lipschitz constant for the overall network. The assumptions made to apply the theorem, such as the specific form of matrix A = W^T W, may not hold in all practical scenarios, especially when considering the non-linearities introduced by activation functions and the composition of multiple layers. The paper needs to more clearly address the limitations of this bound and provide a more rigorous justification for its use in the context of neural network Lipschitz constant estimation.

Empirical side: On one hand, from Tables 1 and 2, it seems that the forged function does not show significant improvements; in fact, when combined with other robust methods, the accuracy under AutoAttack even decreases. The performance gains are marginal at best, and the decrease in robustness when combined with other methods is concerning. This suggests that the forged function might not be compatible with all adversarial training techniques, or that it may interfere with the optimization process of these methods. On the other hand, the robustness of the forged function itself lacks experimental support, such as how much robustness it can provide without any robustness designs (including adversarial training). An important contribution of this paper is that it incurs lower costs compared to adversarial training, so a comparison of performance with adversarial training is necessary. The paper should include a baseline comparison of the forged function's performance against standard adversarial training methods, demonstrating its standalone robustness and cost-effectiveness.

### Questions
Please see weakness part.

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
This paper proposes a robustness enhancement method based on Lipschitz continuity, aiming to improve the security of deep neural networks (DNNs) under adversarial attacks. The authors introduce a forged function that constrains the input domain of the model to reduce its Lipschitz constant, potentially enhancing robustness. This method optimizes inference without retraining the model, thus reducing computational costs. Experiments on CIFAR10, CIFAR100, and ImageNet datasets tested various model architectures like WRN and Swin Transformer, evaluating performance under both white-box and black-box attacks.

### Strengths
The proposed forged function based on Lipschitz continuity is implemented during the inference phase, eliminating the need for retraining or model parameter adjustments. Compared to traditional adversarial training, this method offers a significant computational cost advantage, making it more efficient for applications with limited resources.

### Weaknesses
1. Please distinguish between the use of `\cite{}` and `\citep{}`.
2. The authors are encouraged to open-source their code.
3. In the "Related Work" section, the authors should mention the names of methods alongside author names to aid reader comprehension.
4. In Algorithm 1, Forged Function, please add a description of the hyperparameter $c^r$ in the `require` section.
5. AutoAttack is not the latest attack method; the authors are encouraged to use more advanced black-box attack methods, as referenced in [1].
6. Although the paper emphasizes low computational overhead during the inference phase, it is recommended that the authors provide specific experimental data or quantitative analysis to compare computational overhead.

### Questions
1. How effective is the proposed method in more complex tasks and models, such as object detection and multimodal tasks?
2. Although the authors validated against gradient obfuscation through AutoAttack, the forged function suppresses inputs below a threshold to zero, potentially introducing gradient obfuscation under untested attack methods. Are there further theoretical or experimental supports to ensure that this method does not introduce gradient obfuscation under various attack strategies?
3. How generalizable is this method? Is it applicable to non-vision tasks?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The author proposes a plug-play method to enhance the adversarial robustness of deep neural networks by focusing on Lipschitz continuity. This work reduces the Lipschitz constant by remapping the input domain to a constrained range, thus improving robustness without requiring retraining. This approach is almost cost-free, and experimental results combined with the previous work show the effectiveness of the proposed method.

### Strengths
1.	The method is highly cost-effective as it does not require model retraining or additional data. Moreover, due to its plug-and-play nature, the proposed method can be easily integrated with existing algorithms. 
2.	The authors provide detailed theoretical insights into the relationship between the Lipschitz constant and adversarial robustness. 
3.	The paper is well-organized and clearly presented, with extensive experiments across diverse datasets that validate the robustness of the proposed method.

### Weaknesses
1.	The experimental results, along with the authors' own analysis, indicate that the proposed method may reduce the classification accuracy on clean samples in some cases. While the authors discuss possible reasons, the paper could further analyze this trade-off and explore strategies to mitigate accuracy loss. Specifically, the paper should investigate the impact of the input remapping on the feature space of the network. It would be beneficial to analyze how the constrained input domain affects the distribution of activations in different layers and if this shift contributes to the observed accuracy drop. Furthermore, the authors should explore techniques to compensate for this accuracy loss, such as adaptive remapping strategies or fine-tuning methods that preserve the robustness gains while recovering the original accuracy.
2.	The choice of parameter $c^r$ is crucial to performance, but finding a single $c^r$ that performs well across all tasks is challenging based on the results presented. For example, $c^r=2^{-6}$ performs well on most tasks, while $c^r=2^{-7}$ works better for RST-AWP in Table 4. Adjusting this parameter for new tasks could be time-consuming. The paper lacks a systematic approach for selecting this parameter. The authors should investigate the relationship between the optimal $c^r$ and the specific characteristics of the dataset and model architecture. A more detailed analysis of how different values of $c^r$ affect the Lipschitz constant and the resulting robustness and accuracy trade-offs is needed. The paper should also consider developing an adaptive method for selecting $c^r$ based on the dataset or model, rather than relying on a manual search.

### Questions
1.	In the evaluation using $acc_{AA}$, are the adversarial examples generated using the original neural network architecture, or using the architecture with the proposed forged function?
2.	Can this method be extended to other tasks, such as NLP applications? Alternatively, could the proposed forged function improve the generalization ability of the model in standard training?
3.	Could the authors elaborate on the selection process of parameter $c^r$ and explore a broader range of $c^r$ values across additional datasets?
4.	The method is efficient for certain datasets, but for large datasets like the full ImageNet, it still be computationally expensive. Do the authors have any future plans to further reduce computational requirements?

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
4

### Summary
The paper proposes a model agnostic method for improving the robustness of the network. Essentially, the method prune the activation of small values of the pretrained models. The pruning threshold is determined by the data and a hyperparameter. The paper performs a series experiment on different kinds of adversarially-trained models and shows that the proposed method can improve the robust accuracy by about 0.5%-2% while keeping the accuracy on the natural images. The paper discuss the possibility of gradient masking. However, the experiments cannot fully eliminate such possibility.

### Strengths
1. The paper proposes a model agnostic method that can be easily applied to various robust models and improve the robustness of these method. Such methods have good potential for wide applications.

2. While the proposed method is simple, the pruning technique shows to improve the robust accuracy of various models. Considering the newly introduced hyperparameters are limited, the improvement is far above the margin of errors.

### Weaknesses
1. While the paper discuss the possibility of gradient masking, the experiment is not enough to completely rule out such possibilities. Specially, the paper uses forging function to cut specific activation. Therefore, attacking methods like BPDA should be combined into AutoAttack and the robust accuracy under such attacks should be reported.

2. The motivation of the paper is not fully elaborated in the experiment. For example, whether the empirical Lipschitz has truly been lowered by such method should be reported.

3. Despite the simplicity the method, the novelty of  the proposed method is limited.

### Questions
1. As $c^r$ is very small, I wonder the proportion of activation that be pruned in the experiment. 

2. As the proposed method change the activation even in the natural images, why the natural accuracy is improved in some cases?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This work aims to enhance the adversarial robustness of DNNs by reducing the Lipschitz constant. Unlike existing adversarially trained models, this method is a cost-free method to enhance adversarial robustness by introducing a forged function in the DNNs. Experimental results on CIFAR10, CIFAR100, and ImageNet datasets have demonstrated the proposed method outperforms the adversarial training method.

### Strengths
1. The idea of enhancing the adversarial robustness by reducing the Lipschitz constant is reasonable and straightforward.

2. This paper is well structured.

### Weaknesses
1. The concept of utilizing the Lipschitz constant to certify the adversarial robustness of DNNs has been explored in many previous works [1-3]. This Lipschitz constant is utilized to provide a provable adversarial robustness. However, this paper does not discuss the main differences and improvements from those provable adversarial defense methods. Specifically, the paper lacks a discussion on how the proposed method's performance compares to existing methods in terms of certified robustness bounds, which is a crucial aspect when using the Lipschitz constant for provable guarantees. It is unclear if the proposed method can achieve comparable or better certified robustness compared to existing methods.

2. The proposed forged function seems to be a variation of ReLU, just with a different threshold. Additionally, as illustrated in Figure 2, the Forged function is concatenated with ReLU. How does this differ from simply applying a shifted ReLU? The paper does not provide a clear explanation of the specific benefits of this concatenation or the added parameter $c^r$ beyond a simple shift. It is not clear if the added complexity of the forged function provides a significant advantage over a more straightforward shifted ReLU, especially considering the potential for increased computational overhead.

3. Given Equation (3), if the model becomes larger and more complex, would this increase the Lipschitz constant, potentially worsening the model's robustness? The paper does not address how the proposed method scales with increasing model complexity. It is important to analyze if the Lipschitz constant of the refined model is still non-increasing when the model architecture becomes deeper or wider. It is also unclear if the method is applicable to very large models, and if so, what are the potential limitations.

### Questions
See weakness.

### Soundness
2

### Presentation
2

### Contribution
2
