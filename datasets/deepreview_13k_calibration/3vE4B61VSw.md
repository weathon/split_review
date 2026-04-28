# Accurate Split Learning on Noisy Signals

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 6, 3

## Abstract
Noise injection is applied in Split Learning to address privacy concerns about data leakage. Previous works protect Split Learning by adding noise to the intermediate results during the forward pass. Unfortunately, noisy signals significantly degrade the accuracy of Split Learning training. This paper focuses on improving the training accuracy of Split Learning over noisy signals while protecting training data from reconstruction attacks. We propose two denoising techniques, namely scaling and random masking. Our theoretical results show that both of our denoising techniques accurately estimate the intermediate variables during the forward pass of Split Learning. Moreover, our experiments with deep neural networks demonstrate that the proposed denoising approaches allow Split Learning to tolerate high noise levels while achieving almost the same accuracy as the noise-free baseline. Interestingly, we show that after applying our denoising techniques, the resultant network is more resilient against a state-of-the-art attack compared to the simple noise injection approach.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduces two denoising techniques—scaling and random masking—for Differential Privacy (DP) within the Split Learning framework. These methods aim to preserve security guarantees while maintaining model accuracy. The authors focus on theoretical contributions supported by extensive simulation and empirical studies, demonstrating that the proposed techniques enhance the accuracy of split neural network classification under DP. Additionally, the paper shows that the resulting deep neural networks are resilient to state-of-the-art hijacking attacks.

### Strengths
1. The paper provides a theoretical proof explaining how the proposed denoising methods reduce MSE under certain conditions, effectively denoising while preserving privacy guarantees. The paper covers both a simple identity layer and a more complex linear layer with non-linear activation, with implications for both classification and broader applications.
2. It discusses how the two denoising methods approximate DP-SGD and contribute to privacy.
3. Simulations are conducted for both linear and non-linear cases. Results indicate that the denoising methods exhibit different characteristics at varying noise scales, validating the theoretical claims and offering guidance on the application of each method.
4. The authors conduct practical experiments across five datasets and various ML tasks, including image classification, recommendation, and language modeling. The results show significant improvements, with accuracy close to the clean model performance.
5. The paper examines how hyperparameter settings (e.g., learning rate, weight decay, and optimizer choice) impact denoising performance in practical CIFAR-10/100 image classification tasks.
6. Empirical studies indicate that the proposed method, combined with noise injection, effectively mitigates FSHA.
7. Code is available for review and extensive discussion & extra experiments are available in appendix

### Weaknesses
1. The theorem and its proof are limited to L-1 layers, which restricts the scope. The analysis does not extend to arbitrary layers within the network, which limits the practical applicability of the theoretical results. A more general theoretical framework would be beneficial.
2. While simulation largely supports the theoretical findings, discrepancies are observed between simulation and practical results. For example, scaling outperforms masking in simulation, though this does not hold consistently in practice. The inconsistency between simulation and practical results raises questions about the robustness of the proposed methods in real-world scenarios. The paper should address these discrepancies more thoroughly.
3. Performance degradation occurs when the cut layer is set below L-1. The paper does not provide sufficient analysis of why this degradation occurs, nor does it explore methods to mitigate this issue. This limits the flexibility of the proposed approach.
4. The paper does not explore hybrid applications of the two denoising methods. Combining scaling and masking could potentially lead to better performance, and the lack of investigation in this direction is a missed opportunity.
5. The empirical study tests only a limited set of noise-injection parameters (e.g., noise scale = 0.7). Exploring denoising limitations would be informative. The study should include a wider range of noise scales to fully understand the limitations of the proposed methods.
6. The empirical study also uses a limited range of cut-layer settings. The study should explore a broader range of cut-layer positions to provide a more comprehensive evaluation of the proposed methods.
7. The paper evaluates only a limited range of attack types. While FSHA is considered, other relevant attacks should be included to provide a more robust evaluation of the security of the proposed approach.
8. The techniques are demonstrated only in a two-party split learning setup, despite their potential applicability to Split Federated Learning, which has broader real-world use. The paper should discuss the potential and challenges of applying the proposed methods in a federated setting.

### Questions
1. The denoising mechanism requires the addition of a tanh function. Could this cause performance degradation? Is it always applicable to general ML tasks?
2. There are no empirical results for cut layers below L-2. Exploring these results could help elucidate the proposed methods' limitations.
3. Could the authors provide more insight into why scaling does not mitigate FSHA effectively?
4. Could the authors discuss the limited performance improvement of the denoising mechanism on Laplacian noise?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper presents innovative denoising techniques for Split Learning to enhance training accuracy while preserving data privacy against reconstruction attacks. The authors propose scaling and random masking methods, demonstrating their efficacy through theoretical and experimental results.

### Strengths
1) The paper addresses a critical issue in Split Learning regarding data privacy and accuracy, which is highly relevant in today’s data-driven environment.
2) It introduces two novel denoising techniques—scaling and random masking—that show significant promise in improving training performance under noisy conditions.
3) The theoretical analysis is well-supported by experimental results, enhancing the validity of the proposed methods.
The clarity of the writing and organization of the content facilitate understanding, making complex ideas accessible to a broader audience.

### Weaknesses
1) The experimental validation may lack diversity in the datasets used, potentially limiting generalizability.
2) Comparisons with existing methods could be more robust to highlight the advantages of the proposed techniques.
3) The paper could benefit from clearer explanations of the denoising algorithms for readers unfamiliar with the underlying concepts.

### Questions
1) The literature review could be expanded to include more recent studies, providing a broader context for the proposed techniques.
2) Additional details on the experimental setup would enhance reproducibility and transparency, allowing other researchers to validate the findings.
3) The paper could benefit from more comprehensive discussions on the limitations of the proposed methods and potential future work.
4) A more detailed analysis of the impact of varying noise levels on training accuracy could provide deeper insights into the practical applications of the proposed techniques.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper discusses the use of scaling and random masking as a denoising method for noise-injected networks in the context of split learning. The authors present both theoretical and empirical evidence showing that applying these denoising techniques during the training phase improves testing accuracy. Additionally, the study demonstrates that the proposed denoising methods enhance the network’s resilience against feature space hijacking attacks.

### Strengths
The authors aim to demonstrate that the proposed denoising methods (scaling and random masking) improve test accuracy through both theoretical analysis and empirical evaluation.

### Weaknesses
I believe the focus of the paper is misaligned with the target. First, I think the motivation was made clear: to protect models against reconstruction attacks, noise is often added to intermediate representations (IRs), which leads to a drop in accuracy. This creates a privacy-accuracy or robustness-accuracy trade-off. The primary goal of the paper should be to demonstrate that the proposed methods (scaling and random masking) improve this trade-off, but unfortunately discussions about this trade-off is completely missing.

The authors dedicate substantial space to showing that the denoising methods preserve accuracy when noise is injected. However, this seems unnecessary. It is intuitive that denoising in noise-injected networks would help maintain accuracy—a rather trivial observation. Variance scales as the square of the variable scaling, so scaling down naturally reduces variance. Similarly, adding random masking during training makes the network more robust to noise. This is intuitive and easy to understand. 

What the authors really want to show is that the proposed methods also helps in improve network privacy (or at least no degrade on it) so that a better trade-off become possible. This is critical but unfortunately, the authors spend so less effort on it.  I expected to see quantitative measurements against multiple types of attacks, but only the feature space hijacking attack is covered, while other attacks mentioned in the introduction are ignored. Additionally, quantitative results are lacking. 

As such, I feel authors fail to demonstrate a better accuracy-privacy trade-off, leading to their contribution unjustified.

Additionally, they are also minor issues in both theoretical and empirical study. In my understanding, the denoising methods are applied during the training, so with and without this it will lead to different weights. I don't think it is reflected in theoretical analysis. In the empirical analysis part, I don't think it is the best choice to show graphs of accuracy by training epoch as it takes a lot of space. Instead, I would expect to see much richer results from using different parameter settings.

### Questions
1. Is there any conclusion on the choice of parameters (i.e. \lambda, p). Authors mostly use \lambda=0.1 or 0.2, p = 0.1 or 0.2. How did author choose on this setting? Does the theoretical analysis provide guidance on how we should choose \lambda and p?

### Soundness
2

### Presentation
1

### Contribution
2
