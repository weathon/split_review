# Towards Simple and Provable Parameter-Free Adaptive Gradient Methods

- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 3, 6

## Abstract
Optimization algorithms such as AdaGrad and Adam have significantly advanced the training of deep models by dynamically adjusting the learning rate during the optimization process. However, adhoc tuning of learning rates poses a challenge, leading to inefficiencies in practice. To address this issue, recent research has focused on developing "learning-rate-free" or "parameter-free" algorithms that operate effectively without the need for learning rate tuning. This paper presents AdaGrad++ and Adam++, novel parameter-free variants of AdaGrad and Adam with convergence guarantees. We prove that AdaGrad++ achieves comparable convergence rates to AdaGrad in convex optimization without predefined learning rate assumptions. Similarly, Adam++ matches the convergence rate of Adam without relying on any conditions on the learning rates. Experimental results across various deep learning tasks validate the competitive performance of AdaGrad++ and Adam++

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes two simple parameter-free variants of AdaGrad and Adam, called AdaGrad++ and Adam++. The authors also prove that the proposed algorithms including AdaGrad++ and Adam++ can achieve comparable convergence rates to their counterparts, AdaGrad and Adam. Some experimental results are reported.

### Strengths
The paper is complete in format.

### Weaknesses
As shown in Algorithm 1, the main differences between AdaGrad++ and Adam are from (Ivgi et al., 2023). Therefore, the novelty of this paper is limited. The experimental results are not convincing. The comparisons with recent algorithms are missing. The paper lacks a thorough discussion on the practical implications of the proposed parameter-free methods, especially in scenarios where computational overhead is a concern. The theoretical convergence analysis, while present, does not sufficiently explore the tightness of the bounds or compare them against the known rates of other parameter-free adaptive methods.

### Questions
1.	What’s the difference between the parameter-free techniques used in the proposed algorithm and existing ones?
2.	The detailed discussions about the convergence rates of the proposed algorithms and recently proposed algorithms are missing.
3.	The authors should compare the proposed algorithms with more recently proposed algorithms.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes a learning-rate-tuning-free method. Compared with the previous method DoG [1], this work introduces the parameter dimension $d$ into the Learning Rate (LR) and proposes AdaGrad++ and Adam++ by incorporating the new formula of LR into vanilla AdaGrad and Adam. 

Besides, following the previous settings and proof framework of DoG, this work provides the convergence guarantee of the proposed methods, specifically, Theorem 4.2 and Theorem 5.2, under strong assumptions, i.e.,  convex, bounded stochastic gradient.  Regarding the evaluation, this work conducted image classification tasks - ResNet18, ResNet50, and VGG16 under CIFAR10 dataset, and language tasks - GPT-2 under OpenWebText dataset.

[1] Ivgi, Maor, Oliver Hinder, and Yair Carmon. "Dog is sgd’s best friend: A parameter-free dynamic step size schedule." International Conference on Machine Learning. PMLR, 2023.

### Strengths
The parameter-free methods have gained attention recently.  Achieving optimal convergence guarantees without the knowledge of specific problem-dependent properties is beneficial theoretically and practically.  And this paper tries to tackle this challenge practically and shows some evidence.

### Weaknesses
$	extbf{Weakness in techniques:}$

(1) Both Corollary 4.4 and Corollary 5.2 (and Theorem 4.2 and Theorem 5.1) state that the number of iterations requires $T \propto \mathcal{O}(d)$ to converge, where $d$ is the parameter dimension. Thus, this result is less useful or enlightening to demonstrate the practical performance of the proposed method since the $T<<d$ in practical practice. Besides, $T$ is independent of $d$ in previous work such as Corollary 1 of [1] and Theorem 1 of [2]. The linear dependence on the parameter dimension $d$ in the convergence rate is a significant limitation, as it implies that the number of iterations needed for convergence scales directly with the dimensionality of the problem. This is not practical for high-dimensional problems common in deep learning, where $d$ can be in the millions or billions, and it is unclear how this theoretical result translates to practical performance where $T$ is typically much smaller than $d$.

(2) Corollary 4.4 and Corollary 5.2 state similar convergence rates for AdaGrad++ and Adam++. However, as mentioned by the author “AdaGrad++ as we found it consistently underperforms compared to Adam and Adam++”. The theoretical analysis fails to capture the practical performance differences between AdaGrad++ and Adam++, which suggests that the theoretical bounds are not tight enough to be informative. The convergence rates are similar, yet the empirical performance differs significantly, highlighting a disconnect between theory and practice.

(3) The first discrepancy between theorem proof and practical algorithm. Theorem 5.1 (Corollary 5.2) requires $\lambda \in (0,1)$, which actually disables the momentum update of Adam very quickly, seeing line-6 and line-7. However, I believe the success of Adam and the proposed method in fact counts on the momentum update, as mentioned by the Author that “Adam++ with $\lambda$ = 1 can achieve highly competitive performance under various practical settings”. The theoretical requirement of $\lambda \in (0,1)$ for the momentum term in Adam++ is problematic, as it effectively diminishes the momentum update over time. This contradicts the practical use of Adam, where momentum is crucial for performance, and the authors themselves acknowledge that setting $\lambda = 1$ yields better results.

(4) The second discrepancy between theorem proof and practical algorithm. “Case 2” operation in Algorithm 2 requires the max operation over $v_{t}$ to comfort the convergence proof, however, the practical algorithm needs to eliminate it, as mentioned by the author “experiments have demonstrated that the simplified version $s_{t} = \sqrt{ (t + 1)  v_{t}}$ works better in practice”. The max operation over $v_t$ in the theoretical algorithm is not used in the practical implementation, which raises questions about the validity of the theoretical analysis. The practical algorithm uses a simplified version that performs better, indicating that the theoretical analysis does not align with the practical algorithm's success.

Overall, the technical proofs and results are less connected with the practical performance.

$	extbf{Weakness in evaluation:}$

(1) Considering a parameter-free (or learning-rate-free) optimizer, it is expected to perform well on a spectrum of optimization tasks across different datasets, network architectures, and training parameters such as batch size, number of epochs, etc.  I recognize that it is hard to comprehensively verify the method and lacks a uniform criterion of comparison. But universal adaptivity matters for LR-tuning-free methods.

However, the conducted experiments in this work are insufficient to demonstrate the adaptivity compared with previous work. For example, in terms of the image classification tasks, Table 5 of [1] employed 5 diverse network architectures and 12 different datasets, while this work employed 2 diverse network architectures (ResNet* and VGG) and 1 dataset. Same for the language tasks, seeing Table 4 of [1]. The small-scale experiment cannot support the adaptivity of the proposed methods. The experimental evaluation is limited in scope, failing to demonstrate the claimed adaptivity of the proposed method. The image classification experiments use only two architectures and one dataset, while the language tasks use a single model and dataset. This is insufficient to establish the method's robustness across diverse tasks.

(2) I believe a golden choice of training settings is: Adam+LR(1e-3)+Cosine LR decay, which could be used as the baseline instead of a constant learning rate, since decreasing LR w.r.t. Iterations is well supported by many theoretical results. Table 1 in this paper demonstrates that the default choice of training method, Adam+LR(1e-3)+Cosine LR decay, outperforms the proposed methods. The choice of a constant learning rate as a baseline is not ideal, as it does not reflect common practices in deep learning. A more appropriate baseline would be Adam with a cosine learning rate decay, which is widely used and has theoretical support. The fact that the proposed method is outperformed by this baseline further questions its practical value.


$	extbf{Weakness in method novelty or enlightenment:}$

(1) The main modification compared with the previous method is introducing $\sqrt{d}$ into the learning rate, however, this modification is not well supported intuitively or theoretically. The introduction of $\sqrt{d}$ into the learning rate lacks a clear theoretical or intuitive justification. It is not clear why this specific modification is necessary or how it contributes to the performance of the proposed method.

### Questions
(1) how to explain $T\propto d$? and how to connect the theoretical results with the performance improvements?

(2) Regarding the image classification task, Adam++ is employed, however, AdamW++ (Case 2) is employed for language tasks. Do you have any particular reasons for the switching&tuning operations?  I also noticed two missing settings, i.e., AdamW++ (Case 1) and constant learning rate, in language tasks.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors extend the idea of the DoG framework to Adam and AdaGrad to create parameter-free optimizers with adaptive learning rates. They also propose theorems for the convergence guarantees of their methods.

### Strengths
The paper is well-written, clear, and easy to follow. The authors extend the idea of the DoG framework to Adam and AdaGrad. They also propose theorems for the convergence guarantees of their methods; however, the math was not carefully checked by the reviewer.

### Weaknesses
-    The novel update rule of the learning rate requires storing in memory the original weights of the model, in addition to the weights of the current model and the first and second moments (in Adam’s case). This results in a memory overhead, approximately 33% larger than that of Adam. Furthermore, the update rules require the computation of an additional L2 norm, which can slowdown wallclock time for larger models. These memory and computational overheads are never mentioned or measured explicitly.

-    When comparing optimizers, wall-clock time is important; however, the paper does not mention how the proposed method compares with others in terms of computational time.

-    The minimal performance gains may not justify the added memory and computational overheads.

-    The plotted figures are so small that it is difficult to discern the details.

-    AdaGrad++ is introduced, but the authors state that it underperforms Adam and it is never actually plotted or shown in image classification or language modeling tasks. This raises the question of why it is included in the paper. A comparison with the standard AdaGrad version would have been appropriate since it was introduced.

-    Sophia is mentioned yet never compared against; the authors even state that they use NanoGPT from Sophia’s codebase, which is concerning. In fact, looking at Sophia’s results, it seems to the reviewer that it outperforms Adam++ on the GPT-2 language modeling tasks at 50K steps.

-    In image classification, standard Adam achieves the highest test accuracy in most cases.

-    CIFAR-10 is arguably an outdated task for image classification. It would be beneficial to test at least CIFAR-100, Tiny-ImageNet, and possibly full ImageNet. Additionally, testing transformer-based backbones like the ViT would be more appropriate than VGG16.

### Questions
-    What are the memory and computational overhead required for AdaGrad++ and Adam++? 
-    How does Adam++ compare in wall-clock time with respect to classic Adam?
-    CIFAR-10 is a small dataset for today's standard, how does Adam++ perform on larger image classification datasets and on ViT backbones?

### Soundness
3

### Presentation
3

### Contribution
2
