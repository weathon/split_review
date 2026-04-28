# On progressive sharpening, flat minima and generalisation

- Decision: Reject
- Avg Score: 5.00
- Scores: 3, 3, 6, 8

## Abstract
We present a new approach to understanding the relationship between loss curvature and input-output model behaviour in deep learning.  Specifically, we use existing empirical analyses of the spectrum of deep network loss Hessians to ground an ansatz tying together the loss Hessian and the input-output Jacobian over training samples during the training of deep neural networks. We then prove a series of theoretical results which quantify the degree to which the input-output Jacobian of a model approximates its Lipschitz norm over a data distribution, and deduce a novel generalisation bound in terms of the empirical Jacobian. We use our ansatz, together with our theoretical results, to give a new account of the recently observed progressive sharpening phenomenon, as well as the generalisation properties of flat minima. Experimental evidence is provided to validate our claims.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper explores the relationship between the loss Hessian and the input-output Jacobian via an ansatz, motivated largely based on intuition, by decomposing the Gauss-Newton part of the Hessian into constituting matrices that are also contained in the Jacobian. Some theoretical results are derived as to the extent the maximum input-output Jacobian norm captures the Lipschitz norm of the function as well as its behaviour during training and a simple link to generalization. Overall, these are used to explain the cause of progressive sharpening (related to the edge of stability) as well as some inconsistencies in the flat minima hypothesis.

### Strengths
- The paper provides an interesting perspective on how the loss Hessian and input-output Jacobian are closely connected. 
- There are some interesting but preliminary results on the behaviour of Hessian maximum eigenvalue (referred to as sharpness) and Jacobian norm in different scenarios, with varying kinds of regularization strategies. It gives an impression that when the low value of sharpness arises due to smaller contributions from the Jacobian, then a lower generalization is implied. 
- Understanding when and to what extent the flat minima hypothesis exactly holds is an important research direction. So this work might help towards this end.

### Weaknesses
 - **The Ansatz is pretty crude and the overall narrative overly simplistic:** The authors' ansatz, which decomposes the Gauss-Newton part of the Hessian, lacks rigorous justification and relies heavily on intuition. The paper does not provide a quantitative analysis of how the individual terms of the decomposition interact, instead opting to show their behavior in isolation. This makes it difficult to assess the validity of the ansatz and its ability to explain the observed phenomena. The lack of a detailed quantitative attribution of the Hessian's behavior to the Jacobian's components is a significant weakness, limiting the explanatory power of the proposed framework. The authors' assignment of unexplained behavior to non-Jacobian terms is also done without sufficient justification, further weakening the overall argument.

&nbsp;

- **Theoretical results are fairly simple and lack any evaluation:** The theoretical results presented are not particularly novel and largely consist of manipulations of existing inequalities. The bounds derived, such as in Theorem 5.1 and 6.1, are difficult to evaluate numerically, raising concerns about their practical utility. The paper makes claims about empirical observations based on these theoretical results, but the bounds are often one-sided and insufficient to explain complex phenomena like progressive sharpening. The connection between the theoretical results and the empirical observations is often speculative, and the paper does not provide a clear methodology for validating these theoretical findings.

&nbsp;

- **Unconvincing empirical results**: The presented experiments, while interesting, do not provide strong support for the paper's claims.

   - (a) The relationship between the Jacobian norm and Hessian sharpness shown in Figure 1 is not consistent over the entire training process, as demonstrated in Figure 29. The initial correlation is also not very clean, as seen in Figures 8-12, and the scales of the Jacobian norm and Hessian sharpness diverge significantly for non-zero label smoothing. This casts doubt on the robustness of the proposed relationship.

    - (b) The generalization gap curves in Figures 2 and 5 do not consistently support the claims made about the relationship between sharpness, Jacobian norm, and generalization. The comparison across different learning rates in Figure 2 does not show a clear trend, and the increase in Jacobian norm midway through training in Figure 5 is not well-explained. The correlation between these quantities seems weak, and the paper does not provide quantitative measures of correlation to support its claims. The results are not convincing, especially for the higher learning rates, which contradicts the paper's claim about the generalization benefits of initially large learning rates.

   - (c) The batch size experiments, conducted for a fixed number of epochs, may be confounded by the different number of updates performed. A comparison based on the number of updates, rather than epochs, would be more informative. Additionally, while the training loss is shown, comparing the gradient norm of the loss would provide a more direct measure of convergence.

&nbsp;

- **Literature on Jacobian norm:** The paper does not adequately distinguish its contributions from those of Gamba et al 2023. The discussion of Jacobian norms in (Khromov & Singh, 2023; https://arxiv.org/pdf/2302.10886.pdf), their relation to generalization, and the bound on the variance via the Lipschitz constant, overlaps with some of the material presented here, but this is not properly acknowledged.

### Questions
^^

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper studies the impact of loss curvature broadly on generalization through the lens of input output Jacobian.

### Strengths
On an empirical note, the paper has interesting experiments linking the Jacobian norm and the performance of the models.  The paper is well written and makes clear arguments.

### Weaknesses
a) The result of theorem 6.1 suffers terribly from the curse of dimensionality. The authors comment that the data is intrinsically low dimension, however it is not trivial to identify this low-dimensional support and therein lies the challenge to understand generalization in deep learning challenging. Specifically, the bound involves a term that grows exponentially with the intrinsic dimension, making it practically useless for high-dimensional data, which is the typical setting in deep learning. While the authors mention the possibility of using generative models to approximate the low-dimensional support, this introduces additional complexities and approximations that are not addressed in the current work. The practical applicability of this theorem is therefore severely limited by this dimensionality issue.

b) The result of theorem 5.1 is also very hard to parse and it is not clear how it is linked to progressive sharpening? Yes, in order to estimate a $f_*$ and starting from low curvature or low Jacobian norm the network has to increase sharpness during training.  The surprising aspect of progressive sharpening is that the sharpness increases despite presence of many minima which are flat. I do not think the theorem can capture multiple minima hence cannot explain progressive sharpness. The theorem provides a lower bound on the Lipschitz constant based on the loss, but it doesn't explain why the network converges to sharper minima rather than flat ones. The connection to progressive sharpening is not clearly established, as the theorem does not account for the dynamics of training or the presence of multiple minima with varying sharpness.

### Questions
a) Does if always hold that the term in right side of inequality of Eq. (9) in the statement of Theorem 5.1 is always positive. 

minor:

It would be helpful to reformulate the statement of ansatz 3.1 in technical terms.

### Soundness
3 good

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper expands on previous work exploring the relationship between the curvature of the loss landscape (the Hessian eigenvalues) and the sensitivity of the input-output mapping of the neural network (the singular values of the input-output Jacobian). The key claim is that these two properties vary together in certain circumstances (Ansatz 3.1), and this assertion is then leveraged to study mechanisms underlying progressive sharpening and the relationship between flat minima and generalization.

### Strengths
I appreciate the work done by the paper to characterize mitigating factors for when Ansatz 3.1 will not hold (listed at the end of Section 3) and then discussing which of these mitigating factors is at play in certain results.  The results of the experiments are generally clear and cover a wide range of approaches to improve generalization/bias training methods towards flat minima.  Sections 4 and 6 were overall easy to follow. 

Note that my lower confidence score is to indicate that I am not as familiar with recent work in this area and that I hope my fellow reviewers can provide additional context on the novelty of this work.

### Weaknesses
 **Section 5:** I found the logic of this section challenging to follow.  The paper states "Theorem 4.3 tells us that any training procedure that reduces the loss over all data points will also increase the sample-maximum Jacobian norm from a low starting point."  Where does the loss on all data points come into Theorem 4.3?

The results have a number of restrictions (which are mostly acknowledged by the paper) that limit the applicability of the contributions:
* The conditions under which Ansatz 3.1 holds are not rigorously proven. Specifically, the relationship between the input-output Jacobian and the Gauss-Newton conjugate, as described in Equation 4, is not explicitly derived, making the core claim of the paper an assumption rather than a proven result. This lack of rigorous proof significantly weakens the theoretical foundation of the work.
* The results only hold for simple distributions discussed in Definition 4.1 and 4.2.  The paper gives the example of a GAN with a latent distribution on a hypercube or sphere as an example of a setup where the theory holds, but in most situations this distributional assumption does not hold. This severely limits the practical implications of the theoretical findings, as real-world data rarely conforms to such idealized distributions. The paper should address how deviations from these distributions might affect the conclusions.
* The experiments are only on CIFAR-10 and CIFAR-100.  Larger scale vision or language tasks are not considered. This narrow experimental scope makes it difficult to assess the generalizability of the findings to more complex and practically relevant scenarios. The paper needs to provide a stronger justification for why these datasets are sufficient to validate the claims, or include experiments on more diverse datasets.

Minor Notes:
* Figure 2: I would not use $\lambda$ to denote the weight decay when much of your paper is discussing eigenvalues of the Hessian.  You could just title the $x$-axis weight decay.
* A recent paper to add to the background section on "Flatness, Jacobians, and Generalization." The work does an empirical analysis about the claims on many of the cited papers in larger-scale settings: Maksym Andriushchenko, Francesco Croce, Maximilian Müller, Matthias Hein, Nicolas Flammarion. "A Modern Look at the Relationship between Sharpness and Generalization." https://arxiv.org/abs/2302.07011

### Questions
* Would you say that your work essentially points to the sensitivity of the input-output Jacobian being the more fundamental quantity (vs. the sharpness of the loss landscape) when thinking about progressive sharpening and generalization?  Or would you summarize your work a different way?  

* Does your work result in any new suggestions for practitioners on what training techniques should be used to best improve generalization. Or put another way, what would you say we gain from the understanding presented in this paper?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors consider a decomposition of the Hessian of a convex loss for neural networks that yields the Gauss-Newton matrix as one of its terms which in turn can be decomposed as a sum over composites of individual input-output Jacobians of the neural network layers. The authors argue that, based on empirical evidence, the large (outlying) eigenvalues of the Gauss-Newton matrix determine those of the Hessian (curvature) and the spectrum of the Gauss-Newton matrix is in turn determined by the extreme singular values of the input-output Jacobians. So to understand the progressive sharpening phenomenon and better generalization with flat curvature it makes sense to analyze the input-output Jacobian norm. The authors’ theoretical contributions explain progressive sharpening, the connection between the Lipschitz norm of a neural network, its input-output Jacobian, and its generalization gap for the given input distribution assumptions. Through numerical experiments the authors also demonstrate how the Jacobian norm is correlated to sharpness and the generalization gap in practice and how different regularization approaches such as label smoothing, weight decay, sharpness aware minimization, data augmentation, learning rate changes etc. impact generalization gap, Jacobian norm and sharpness. The theoretical approach in the paper is compatible with the view that loss flatness does not generally imply generalization because of possible reparameterization (the Dinh et al reference).

### Strengths
- The theory in this paper is driven by empirical observations and explains effects that intuitively make sense and that have been observed by practitioners in a way that contributes to a deeper understanding about generalization.
- The empirical results in the paper are well chosen to demonstrate the various effects discussed and cover a large part of relevant regularization and hyperparameter dimensions

### Weaknesses
 - The authors argue that their generalization bound (Theorem 6) is superior compared to other generalization bounds in the literature because it involves data complexity over hypothesis complexity. As a reason, the authors cite that datasets in standard deep learning are intrinsically low dimensional and hence the rate of their bound can be nontrivial in practice. But it does not become clear from the paper how the intrinsic dimensionality is estimated in practice and whether that means that it's possible to tightly estimate actual generalization gaps in practice based on their rate in practice (even for simple examples). Specifically, the paper does not provide any concrete method for estimating the intrinsic dimensionality of the data manifold, which is crucial for the practical applicability of their bound. Without a clear procedure to estimate this dimensionality, it's difficult to assess the tightness of the bound and its usefulness in real-world scenarios. The claim of superiority over other bounds is therefore not fully substantiated.


### Questions
- The main claims / contributions about progressive sharpening (Theorem 5.1) and generalization (Theorem 6.1) could be summarized or more clearly highlighted already in the abstract / introduction.
- For the paper to be more self-contained iIt would be helpful to clearly list and explain the empirical phenomena explained by the theory. E.g. the implicit regularization through higher initial learning rate / edge of stability phenomenon may not be familiar to all readers.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
