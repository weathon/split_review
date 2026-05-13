# Characterizing the Training Dynamics of Private Fine-tuning with Langevin Diffusion

- Decision: Reject
- Scores: 5, 6, 8

## Abstract
We show that differentially private full fine-tuning (DP-FFT) can distort pre-trained backbone features based on both theoretical and empirical results. We identify the cause of the distortion as the misalignment between the pre-trained backbone and the randomly initialized linear head. We prove that a sequential fine-tuning strategy can mitigate the feature distortion: first-linear-probing-then-fine-tuning (DP-LP-FFT). A new approximation scheme allows us to derive approximate upper and lower bounds on the training loss of DP-LP and DP-FFT, in a simple but canonical setting of 2-layer neural networks with ReLU activation. Experiments on real-world datasets and architectures are consistent with our theoretical insights.   We also derive new upper bounds for 2-layer linear networks without the approximation. Moreover, our theory suggests a trade-off of privacy budget allocation in multi-phase fine-tuning methods like DP-LP-FFT.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper addresses the challenge of differentially private fine-tuning of deep learning models. The authors highlight that naïve full-parameter fine-tuning leads to misalignment between the pre-trained features and the last layer. They propose a hybrid strategy that combines linear probing with fine-tuning, demonstrating theoretically and empirically that this approach mitigates feature distortion. The theoretical framework is based on a simplified Langevin diffusion and a two-layer ReLU neural network. The paper’s theoretical insights are further supported by experimental evaluations on various vision tasks and models.

### Strengths
**S1.** The importance and relevance of the problem tackled — differentially private deep learning — is highlighted well, given the challenge posed by the high dimensionality of typical models.

**S2.** The concept of splitting the privacy budget between full parameter tuning (or Full Fine-Tuning, FFT) and Linear Probing (LP: tuning only the last layer) appears intriguing and potentially valuable for practical applications.

**S3.** The attempt to provide rigorous theoretical analysis addresses a gap in the current literature.

**S4.** The paper includes multiple experiments across diverse datasets and models, supporting the benefits of the proposed hybrid approach.

### Weaknesses
 **W1.** The idea of combining FFT and LP is not entirely novel, as similar approaches were introduced and experimentally tested by Tang et al. (2023). A more detailed discussion of how this paper builds on or extends prior work is needed. Specifically, the paper should clarify the novelty of their approach compared to existing methods, especially regarding the specific combination of linear probing and full fine-tuning under differential privacy, and whether the theoretical analysis provides new insights beyond what is already known.

**W2.** The theoretical model appears oversimplified. Using a 2-layer neural network with ReLU activations while enabling a decoupling of feature learning and classification seems far removed from the practical settings under consideration. It is unclear how this model aligns with realistic applications, particularly since results in Section 4.1.1 suggest exponential convergence, implying that the underlying problem is no harder than strongly convex optimization (or that PL conditions hold for the loss). The analysis also uses a simplified Langevin diffusion instead of DP-SGD, raising concerns about the relevance of the theoretical results to practical DP training. The authors apply a zeroth-order asymptotic expansion, which seems to remove the Brownian motion representing Gaussian noise, a core component of DP training. This simplification makes the method equivalent to simple gradient flow, ignoring the crucial per-sample clipping operation that is essential for DP deep learning. The claim that the modeling preserves the noisy behavior of DP-SGD needs further justification, especially given the removal of the noise term and clipping.

**W3.** Assumptions 3.1 and 3.2 are unconventional and strongly restrictive. Only one previous work referenced these assumptions, making it difficult to accept them as standard or practical in the context of simple binary classification. The assumptions require a specific geometric structure of the data and pre-trained features, which may not hold in real-world scenarios, limiting the applicability of the theoretical results.

**W4.** The experimental setup lacks details on the clipping threshold, a key parameter influencing DP-SGD performance and necessary for reproducibility. Without specifying the clipping threshold, it is difficult to assess the validity and generalizability of the experimental results. The paper should also include a sensitivity analysis of the clipping threshold to show how it affects the performance of the proposed method.

**W5.** The paper’s theoretical results and mathematical proofs in the Appendix are difficult to follow, partly due to unclear notation and insufficient explanation. Specific issues and questions include:

- The notation $\sim$ in line 214 is ambiguous.

- The choice of zero-mean Gaussian initialization for the linear head is restrictive and not well-motivated.

- The meaning of *“optimality”* of $w_j$ in line 232 is unclear.

- After a quick look at the work of Ganesh et al. (2023b), I did not find the exact statement of Theorem 4.1. Could the authors please point me to the exact place in the original paper?

- Theorems 4.2 and 4.3 are hard to comprehend and presented without almost any commentary or explanation. The interpretation of the constants and the implications of the limit behavior need to be clarified.

- It is unclear to me why the authors say that
> According to Theorem 5.1, a greater proportion of the privacy budget should be allocated to DP-LP
when the total privacy budget is smaller.

- Moreover, I would like to ask what is parameter $\rho$. It seems like it can make $r$ arbitrarily large.

- Section 5.2 relies on assumptions from the Appendix, which are also very strong (like E.7). Such an approach makes it hard to access the theoretical contributions of the paper adequately. The connection between these assumptions and real-world data is not clear.

- What does variable $D$ denote on line 442? How big can $t_{lp}$ be in practice for realistic parameter values? It is unclear how Corollary 5.3 is obtained for the main paper text.

- The steps of Theorem 3.3 proof are unclear. For instance, how is formula (28) obtained? Why the probability on line 958 equals $1-2^{-h}$?

### Questions
Most of my concerns are mentioned in the Weaknesses part.

**Q1.** Is there a reason why Langevin diffusion is defined differently from Ganesh et al. (2023b)?

**Q2.** How realistic are Assumptions 3.1 and 3.2? Were they experimentally validated?

**Q3.** Public pre-training and private fine-tuning approach has been seriously questioned recently. I would appreciate the author's thoughts on the recent position paper by Tramèr et al. (2024).

___

Tramèr, F., Kamath, G., & Carlini, N. (2024). Position: Considerations for Differentially Private Learning with Large-Scale Public Pretraining. Proceedings of the 41st International Conference on Machine Learning.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper examines differentially private (DP) fine-tuning (FT) methods, showing through theoretical and empirical analysis that DP full FT can distort pretrained backbone features due to misalignment between the pretrained backbone and the randomly initialized linear head. To address this, the authors propose DP-LP_FFT, which first performs linear probing and then fine-tunes. Additionally, the paper provides convergence rates for the proposed methods using two-layer neural networks.

### Strengths
- The paper investigates an interesting phenomenon in fine-tuning methods, where non-private fine-tuning distorts pretrained features and leads to degraded OOD performance. A similar empirical effect is observed in private settings, as shown in Figure 3.

- The proposed DP-LP running before DP-FFT can theoretically reduce feature distortion. It would be beneficial to provide experimental results to compare with Figure 3.

- The proposed LP mechanism in private fine-tuning is effective, as demonstrated in Tables 1 and 2.

### Weaknesses
There is a lack of comparison of feature distortion with DP-LP. Specifically, while the paper argues that DP full fine-tuning (FFT) distorts features, it does not provide a direct empirical comparison of the feature representations learned by DP-FFT versus DP-LP. It would be beneficial to visualize or quantify the differences in feature space, perhaps using techniques like t-SNE or calculating the cosine similarity between feature vectors. This would provide more concrete evidence for the claim that DP-LP avoids the feature distortion observed in DP-FFT. Without this comparison, the argument relies more on the theoretical claim that freezing the backbone prevents distortion, rather than direct empirical observation of the learned representations. The paper would benefit from an analysis that shows the extent to which features are preserved or altered by each method.

### Questions
In line 199 , why are subspaces separated by $\mathbb{I}\_{\boldsymbol{x}\_i^{\top} z>0}=\mathbb{I}\_{y_i=-1}$ or $\mathbb{I}\_{\boldsymbol{x}\_i^{\top} z>0}=\mathbb{I}\_{y_i=1}$ ?

### Soundness
3

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
This work studies the training dynamics of DP fine-tuning using a Langevin diffusion approximation of DP-SGD, and provides theoretical understandings of how fune-tuning techniques (such as DP-LP, DP-FFT, or a hybrid) affect the out-of-distribution performance of a 2-layer ReLU network.
Using a zeroth-order approximation, the authors provide a theoretical explanation of an empirical phenomenon that randomly initialized linear heads distort pre-trained backbone features in the early stages of DP-FFT.
To mitigate or even avoid the feature distortion, they propose a hybrid method that combines DP-LP and DP-FFT, and further examine the privacy budget allocation across DP-LP and DP-FFT. 
Extensive numerical experiments support theoretical findings and demonstrate the effectiveness of the proposed hybrid method.
Overall, this work deepens our understanding of DP fine-tuning by providing a solid theoretical explanation. 
I found this work interesting and thus recommend an Accept.

### Strengths
1. Use Langevin diffusion as an approximation of DP-SGD to study the dynamics of DP tuning. While obtained from an approximation model, findings are very interesting and align with empirical observatons. 
2. The proposed hybrid tuning method is supported by theoretical guaranteens and evidence from extensive experiments. 
3. Insights into privacy budget allocation are of practical interest.

### Weaknesses
In practice, trainings are usually done in a discrete manner (say t=1,2,...), but Lagenvin diffusion is a continuous approximation for t>0. This gap may hamper the generality of this work's findings. For example, if $\Delta t$ in Theorem 3.3 belongs to [0,1], then feature distortion might not be an issue, because we start from $t=1$. Therefore, it would be helpful if authors could provide a short discussion of the value of $\Delta t$, or name some driving factors that may significantly affect the value of $\Delta t$.

### Questions
1. theorem 3.4 says after $\Delta t$, DP-FFT does not distort the pre-trained features. But the Eq (10) is stated for $\forall t\in(0, \Delta t)$. Is there a typo in the range of $t$? I guess it should be $∀t\in(\Delta t, \infty)$?
2. typos around line 1148

### Soundness
3

### Presentation
3

### Contribution
3
