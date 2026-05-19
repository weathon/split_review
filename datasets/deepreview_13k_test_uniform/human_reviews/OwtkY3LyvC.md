# Bridging The Gap Between Training and Testing for Certified Robustness

- Decision: Reject
- Scores: 3, 5, 1, 5, 3

## Abstract
Certified robustness provides a theoretical lower bound for adversarial robustness and arouses widespread interests and discussions from the research community. With theoretical support to improve the certified robustness on the training set, practitioners endeavor to train a more certified robust model during inference on the test set. However, the experimental neglect on the training set and the theoretical ignorance during inference on the test set induce a gap between training and testing for certified robustness. By establishing an equivalence between the convergence of training loss and the improvement of certified robustness, we recognize there is a trade-off between expressive power and generalization (assuming a well-conditioned optimization) for certified robustness, which is similar to the underfitting and overfitting discussed in machine learning. To investigate this trade-off, we design a new orthogonal convolution-Controllable Orthogonal Convolution Kernel (COCK) which provides a wider range of expressive power than existing orthogonal convolutions. Empirically, there is a power-driven shift from vanilla classification accuracy to certified robustness in the sense of the optimal trade-off between expressive power and generalization. The experimental results suggest that by carefully improving the expressive power from the optimal trade-off for vanilla classification performance, the model will be more certified robust.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper presents an analysis on certified robustness on Convolutional Netural Networks (CNNs). The authors first show an equivalence between the convergence of training loss and improvement of certified robustness. After that, a new orthogonal convolution-Controllable Orthogonal Convolution Kernel (COCK) is proposed to mitigate the trade-off between expressive power and generalization. Through experiments on CIFAR10 dataset, the authors show that COCK achieves improvement on vallina accuracy and certified accuracy compared to existing baselines.

### Strengths
The proposed method performs better than the baseline on most cases.

### Weaknesses
I believe the current paper is not in a publishable quality for the following reasonings:
1. Preliminary is not clear. In Section 3, the definition of cerfified robustness is missing. It's also not well-explained how it's connected to orthogonal convolution and Lipschitz-contrainted models.
2. Definition is not clear, notation is not consistent. For example, in the beginning of Section 3, $x^{(i)}$ denotes the $i$-th example in the training set, while in Equation (10), $x^{(ij)}$ denotes the $j$-th example that belongs to class $i$. The definitions of Convolition (3.3.1), margin loss (4.2.1) and certified robust accuracy (4.2.3 and 4.2.4) are also not clear.
3. Theorem 4.1.1 is not clear. I don't think it trivial that "minimizing training loss is equivalent to maximizing the output margin $m_k^{(ij)}$". It's also not clear how equivalent it is between the derease of training loss and the improvement of certified robustness. One should give a mathematical description to support the argument. 
4. The proposed algorithm COCK is not well explained. How it it's related to Proposition 5.1.1 (and Fourier Transform)？What does COCK actually do? There is not adequate explanation on section 5.
5. How COCK is related to r-RELU? Also, Figure 1 is not well captioned.
6. The experiments are limited to CIFAR10 dataset and LipConvNet. Also, the citation of baselines (SOC, BCOP and Cayley) are missing.

### Questions
Please refer to the "Weakness" above.

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper aims to understand the differences in certified robustness observed during training and testing phases, especially focusing on how the expressive power of models impacts certified robustness on the test set.

The authors identify a trade-off between expressive power and generalization for certified robustness, drawing an analogy to the overfitting and underfitting dynamics in traditional machine learning. To explore this, they introduce a new model component, the Controllable Orthogonal Convolution Kernel (COCK), which allows for greater flexibility and a broader range of expressive power than existing orthogonal convolution methods.

### Strengths
1. This paper provides a fresh perspective by drawing a parallel between the traditional machine learning concepts of underfitting and overfitting and the balance between expressive power and generalization in certified robustness. This analogy sheds light on an often-overlooked aspect in the field, emphasizing that certified robustness exhibits similar trade-offs as seen in conventional learning. This insight could potentially open new avenues for the research community to deepen their understanding of certified robustness.

2. The authors introduce the Controllable Orthogonal Convolution Kernel (COCK), a module specifically designed to adjust the expressive power of neural networks. By enabling more nuanced control over the model’s expressive capacity, COCK serves to bridge the gap between training and test robustness.

### Weaknesses
1. The central finding of the paper—that there exists a trade-off between expressive power and generalization for certified robustness— is not surprising and may be considered common knowledge in this field. While the paper empirically validates this trade-off, it lacks both theoretical understanding and empirical analysis of this trade-off.

2. Although the paper introduces new definitions and theorems, these contributions primarily reinterpret existing ideas rather than advancing theoretical understanding. For instance, Proposition 5.1.1 on COCK appears to be more of an application or extension of existing techniques rather than a novel theoretical innovation. Thus, the paper’s contributions seem limited.

### Questions
See the Weaknesses. 

Overall, I think this paper raises an interesting phenomenon, but the theoretical research or experimental analysis of this phenomenon is not deep enough and needs further improvement.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
This paper designs a new certified robustness method named COCK that is claimed to enjoy a better robustness-utility trade-off (but I don't understand what is the intuition behind the design of COCK). Experiments are conducted on CIFAR-10, CIFAR-100, and Tiny-ImageNet to evaluate the proposed COCK method (which shows that COCK is significantly worse than most recent certified robustness methods).

### Strengths
None.

### Weaknesses
1. The certified robustness performance of the proposed COCK method is significantly weaker than recent certified robustness methods such as [r1] and [r2]. Specifically, for example, according to Table 1, when the $l\_2$-perturbation radius is $\frac{108}{255}$, the best certified robust accuracy COCK achieved on CIFAR-10 dataset is $60.79\\%$. However, with a higher perturbation radius $\rho = 0.5 > \frac{108}{255}$, on the CIFAR-10 dataset, [r1] and [r2] achieved certified robust accuracies of $65.5\\%$ and $70.7\\%$ respectively, which both are significantly higher than the result of COCK. Similar things also happen for the other dataset (CIFAR-100) and other perturbation radii. Furthermore, [r1] and [r2] can work on the ImageNet dataset, while COCK is only analyzed on the Tiny-ImageNet dataset. So if the proposed COCK method is so weak, why the community needs to waste time on it?

2. Algorithm 1 (i.e., COCK) seems to be very time-consuming, which may significantly limit the practicality of the proposed COCK method. There are two main calculation challenges: (1) Line#681 needs to conduct $3t$ times of matrix multiplication (i.e., calculate the term $B^3\_{\tau-1} S$ for $t$ times), and (2) Line#688 needs to perform inverse-FFT for $i*j$ times. So I suggest the authors analyze the theoretical and empirical time complexity of COCK. Also please note that [r1] and [r2] can even work without additional model training.

3. The authors claim that one of their contributions is that they discover "a trade-off between expressive power and generalization for certified robustness" (For example, see Line#078-079). Unfortunately, they are not the first to find the trade-off and such an observation is now very trivial. Specifically, the trade-off between model robustness and utility has been widely accepted by the ML S&P community and has also been well studied in many existing works such as [r3], [r4], [r5], and [r6].

4. I still do not understand what is the motivation for designing COCK? How can it make COCK enjoys certified robustness better than existing certified robustness approaches (although it actually cannot)? Please comment.

5. Experiments could be significantly improved. Firstly, I suggest including experiments on the (vanilla) ImageNet dataset. Secondly, I think the authors should cite more recent certified robustness baselines and compare them with your proposed COCK. It is worth noting that the most recent paper that the authors cited in this work is from 2022, which is still a too-old paper (in the field of certified robustness).

**References:**

[r1] Carlini N. et al. "(Certified!!) Adversarial Robustness for Free!" arXiv 2206.10550 / ICLR 2023.

[r2] Chen H. et al. "Diffusion Models are Certifiably Robust Classifiers." arXiv 2402.02316 / NeurIPS 2024.

[r3] Raghunathan A. et al. "Understanding and Mitigating the Tradeoff between Robustness and Accuracy." ICML 2020.

[r4] Donhauser K et al. "Interpolation can hurt robust generalization even when there is no noise." NeurIPS 2021.

[r5] Rice L. et al. "Overfitting in adversarially robust deep learning." ICML 2020.

[r6] Fu S. et al. "Theoretical Analysis of Robust Overfitting for Wide DNNs: An NTK Approach." ICLR 2024.

### Questions
See **Weaknesses** for details.

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This manuscript introduces the controllable orthogonal convolutional kernel (COCK), which uses a more flexible parameterization of convolution operation while controlling its Lipschitz constants. In this context, COCK demonstrates better flexibility while ensuring certified robustness.

### Strengths
1. The gap of certified robustness between the training and the test set is a key issue in provably robustness while underexplored. The proposed method is theoretically guaranteed.

2. The experiment is comprehensive.

3. The manuscript is generally well-written and easy to follow.

### Weaknesses
1. My major concern is the logic of the motivation and the proposed method. As Section 5 demonstrates, the proposed COCK is more flexible than vanilla orthogonal convolution, why doesn't it suffer more from overfitting? The last paragraph in Section 4.1 points out that there is a trade-off between expressive power (related to parameterization flexibility) and generalization.

2. Theorem 5.2.1 may need more explanation. I agree COCK demonstrates no-inferior performance in the experiment, but I am suspicious about the proof of this theorem. In the proof, especially Equation (35), the authors seem to assume that the margins of COCK and the baseline are the same, while it may not be the case. In addition, when using COCK for parameterization, there may exist no-inferior points compared with the baseline, but we cannot guarantee the optimization in training and lead the parameter to converge to such cases. In this regard, the conclusion of Theorem 5.2.1 looks too strong, the authors may need more assumptions or explanations to make this part more rigorous.

3. Although the experiment is comprehensive, the $\rho$ that we achieve good certified robustness is small, limiting the practical use of the method. Actually, in the empirical study of adversarial training, the $\epsilon$ value in the $l_2$ cases is usually set as $0.5$ or $2$, much larger than the values used in the experiment (e.g. Table 1) of this manuscript.

### Questions
The major questions are pointed out in the "weakness" part, the authors need to answer those questions to address my concerns.

Two minor issues:

1. In Definition 4.2.2, the difference between $\epsilon$ and $\epsilon_2$ seems unclear.

2. In Figure 1, the authors should distinguish the difference between the original input and the post-transformation features. In the current figure, it looks like there are $8$ points in total.

From my point of view, the current version of the manuscript is not ready for publication. I welcome the authors to address my concerns in the rebuttal.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper studies the gap between training and test certified accuracy and identifies a questionable trade-off between expressive power and generalization. Following this, the paper proposes a new orthogonal convolution named Controllable Orthogonal Convolution Kernel (COCK) which improves the certified robustness.

### Strengths
1. The paper studies an important problem of certifying robustness in neural networks.
2. The new convolution COCK learns parameters in the frequency domain which is novel and seems to improve the certified robustness.

### Weaknesses
The argument for the trade-off between training and test certified robustness raises some fundamental issues that are not discussed in the work (see Questions).

### Questions
### The fundamental questions I have are the following:
1. The trade-off between expressive power and generalization for certified robustness is questionable. It is primarily established based on the argument that "expressive power brings high generalization error to classification performance during inference (overfitting) and is certain to degrade the certified robustness on the test set" (lines 245-247). But, this doesn't hold for commonly used overparameterized neural networks, as they exhibit double descent phenomenon, that is, increasing the expressive power (near 0 training error) decreases the generalization error (test error) [P1]. 
2. Why the theoretical results established on the training set cannot extend to the test set from the same data distribution? The argument made by the authors for expecting a gap between the training and test certified robustness is "experimental neglect on the training set and the theoretical ignorance during inference on the test set" -- but, statistically when training and test sets are from the same distribution, the theory established on large training data would translate to the test set as well. 

### Questions on COCK:
1. In Algorithm 1 (line 670), is the inverse Fourier transform in line 688 new compared to the existing orthogonal convolutions? 
2. Line 295: it is not clear why $h=w=n$ and what is $n$? 
3. Line 324: how does COCK provide data scaling? Please clarify it.
4. Line 330: in the toy example case, why is the comparison made against a diagonal matrix? Would COCK result in a diagonal matrix in any of the settings?
5. The toy example visualization is unclear. What exactly is visualized? Are the points in data space, or are they layer wise feature space? The feature space dimension is also not mentioned. 

### Questions on experiments:
1. How COCK is different from SOC, BCOP, and Cayley, the orthogonal convolutions used in experiments? Please add citations for the other algorithms and briefly compare and contrast them. 
2. The closest algorithm to COCK is layer-wise orthogonal training (LOT), as mentioned in line 116. However, a direct comparison is *not* made experimentally. Are the orthogonal convolutions used (SOC, BCOP, Cayley) do layer-wise orthogonalization? 
3. what is max-min activation mentioned in line 383?
4. Line 393: $\rho$ is used for l2 norm perturbation. I think it is the same as $\epsilon$ used in sections before. Is it? If so, please follow the same notation for clarity.

Overall, I think the new convolution is novel and interesting that it improves the certified robustness compared to the other orthogonal convolutions. But, the premise of the trade-off analysis is not convincing. 

[P1] Belkin et al. "Reconciling modern machine-learning practice and the classical bias–variance trade-off." PNAS 2019

### Soundness
2

### Presentation
2

### Contribution
2
