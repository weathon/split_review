# Universally Amplifying Randomized Smoothing for Certified Robustness with Anisotropic Noise

- Decision: Reject
- Scores: 3, 3, 3, 3

## Abstract
Randomized smoothing has achieved great success for certified adversarial robustness. However, existing methods (especially the theory for certification guarantee) rely on a fixed i.i.d. noise distribution for all dimensions of the data (e.g., all the pixels in an image), and may result in limited performance of certified robustness. To address this limitation, we propose UCAN: a novel technique that $\underline{U}$niversally amplifies randomized smoothing for $\underline{C}$ertified robustness with $\underline{A}$nisotropic $\underline{N}$oise. It can theoretically transform any randomized smoothing method with isotropic noise to ensure certified robustness based on different variants of anisotropic noise. The theories universally work for using different noise distributions against different $\ell_p$ perturbations. Furthermore, we also design a novel framework with three example noise parameter generators (NPGs) for customizing the anisotropic noise. Finally, experimental results demonstrate that UCAN significantly outperforms the state-of-the-art (SOTA) methods, e.g., the certified accuracy can be improved by up to $182.6$\% at large certified radii on MNIST, CIFAR10, and ImageNet datasets.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper aims at improving certified robustness by randomized smoothing with anisotropic noise. The universal theory for certification with anisotropic noise has been provided. The authors consider three kinds of customizing anisotropic noises, and provide corresponding noise generation methods. The authors conduct experiment to demonstrate that the proposed UCAN method achieve state-of-the-art performance compared to existing randomized smoothing-based methods for certified robustness.

### Strengths
1. The proposed method on smoothing with anisotropic noise is novel. It is interesting to see the expansion of RS-based methods from isotropic noises to anisotropic ones.
2. This paper provides the theoretical guarantee of certified robustness under anisotropic randomized smoothing, and comprehensive analyses to transform existing randomized smoothing methods to anisotropic cases.
3. Authors consider three different kinds of anisotropic noises, and provide a novel input-dependent one by optimizing $\mu(x)$ and $\sigma(x)$ by a multi-layer neural network.

### Weaknesses
1. My major concern of this paper is the potential unfairness in evaluation on UCAN and existing RS-based methods. The evaluation criterion seems to be based on scaled radius, which has different weight in each dimension. This is concerning because the reported results in Table 3 show an unusually high certified accuracy of over 70% on CIFAR-10 for an \(l_2\) radius of 1.75. This result appears inconsistent with the expected capabilities of \(l_\infty\) norm-based attacks with a budget of 8/255, which should have a maximum \(l_2\) norm of approximately \(\sqrt{3072 \times (\frac{8}{255})^2} \approx 1.74\). This suggests that the evaluation might not be based on a standard \(l_p\) norm, but rather on a scaled radius, which could be misleading. Scaled radius certification, while potentially useful in specific scenarios, might not be a fair criterion for general certified robustness. Different dimensions of an image can have varying sensitivity to adversarial perturbations. For instance, dimensions corresponding to the contour of an image might be more vulnerable than those representing the background. It is plausible that UCAN assigns smaller variances (\(\sigma\)) to these vulnerable dimensions, effectively gaining robustness in less critical dimensions. Therefore, a standard \(l_p\) norm evaluation is necessary to ensure a fair comparison with existing RS methods. If a scaled radius is used, a detailed explanation and justification for its use in this context are required.

2. In Theorem 3.2, the certification uses the p-norm of \(\frac{\delta_i}{\sigma_i}\), where \(\delta_i\) is the i-th dimension of the perturbation \(\delta\). This appears to be a one-dimensional scalar. Furthermore, Theorem 3.2 seems to be a direct corollary of Theorem 3.1, as the certification divides the variance \(\sigma_i\) for each \(\delta_i\), effectively making it isotropic. This raises questions about the novelty and necessity of Theorem 3.2.

3. There might be missing baselines for \(l_1\) and \(l_\infty\) certified robustness [1,2,3]. A comparison with existing certified \(l_1\) and \(l_\infty\) methods would strengthen the paper and provide a more comprehensive evaluation of UCAN's performance.

### Questions
1.	Why using 5-layers NN when generating universal/ input-dependent anisotropic noises? Is there some motivations or ablation studies for that?
2.	Could you provide more details on training of universal anisotropic noise? It seems that the variance loss is to optimize $\sigma$ and smoothing loss containing $\sigma$ when optimizing classifier $\theta_f$. I believe the two losses are optimized alternately but not simultaneously.
3.	The authors said that randomized smoothing achieved great success for certified adversarial robustness. Could RS really make classifier robust? Can you provide comparison of RS based model to the SOTA methods for achieving robustness?

### Soundness
2 fair

### Presentation
3 good

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
The authors interpret certified robustness from an anisotropic lens, with the aim of assessing how the performance of certification mechanisms within this context.

### Strengths
Well written, comprehensive experiments that match community expectations, nice visualisations that really break apart the differences between fixed pattern, universal, and input dependent noise. 

The input-dependent component of the noise is interesting.

### Weaknesses
My issues with this paper stem from two different directions, which I find to be significant hurdles to my ability to recommend this paper for publication.

The first is the fact that the contribution in constructing the anistropic noise measures (the core conceit of the paper) is essentially just a basic modification to extant techniques, with no other modifications being made. However, this is not in and of itself a reason for rejection - simple modifications can lead to impactful contributions. 

My primary concern relates to the alignment of the chosen area of investigation to the broader problem space. Specifically, I do not think that there is any framework (either in the literature or suggested in the framework) that would case about the area of the region of certification. From the certifiers perspective, what information about the security of a model is gained by knowledge of the Lebesgue measure of the noise region (or any other measure of the area of certification)? The primary measure of risk is the nearest extant adversarial example - this is well established in the literature as a measure of the adversarial risk (see Gilmer's "Motivating the Rules of the Game for Adversarial Example Research", 2018), because this measures the effort required for an adversary to identify an adversarial example. Any other risk measure would need to be well justified and well posed, and this is not the case within this work. The use of the Lebesgue measure, while mathematically sound, doesn't translate to a practically meaningful metric for assessing adversarial vulnerability in the context of certified robustness. The core issue is that a larger Lebesgue measure does not necessarily imply a more robust model, as adversarial examples may still exist at relatively small distances in certain directions, even if the overall 'area' of the certified region is large. This disconnect undermines the practical relevance of the proposed metric.

Given that the certified distances to the nearest possible adversarial example are unchanged by your work, I do not see how this leads to an improved understanding of adversarial risk. I would argue that rather than significantly improving upon SOTA, you're introducing a new metric to mask the fact that you do not appear to produce any level of outperformance. The paper fails to adequately justify why this new metric is a more relevant measure of robustness than the established certified radius, especially given that the certified radius is directly related to the minimum adversarial distance.

For a few minor issues:
-The use of lambda as the scale parameter, and $\sigma_i$ as the modification of the scale parameter. But $\lambda$ is typically proportional to the standard deviation, so using $\sigma_i$ as part of the notation is not as clear as it could be. 
- A secondary minor issue is that Table 1, I believe the Lee et. al PDF should be proportional to $||z||_{\infty}$, rather than $||z / \lambda||$.
- The idea of including a headline figure of an 182.6% improvement over SOTA - anyone reading this who was not familiar with this field would assume that this would be an apples-to-apples comparison, but it's not. There's no SOTA for certification that cares about area driven measures of certification, and so claiming a comparison to these prior techniques is not reasonable or well justified.

### Questions
Is there any justification for using the Lebesgue Measure as a proxy of adversarial risk?

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes to shift and re-scale the noise in randomized smoothing in order to generate anisotropic robustness guarantees. The approach is universal in the sense that any randomized smoothing-based method can be transformed into a model with such anisotropic guarantees. Experiments on benchmark image classification datasets demonstrate increased certified accuracy curves compared to past works.

### Strengths
1. The paper is very easy to read.
2. The approach is simple to understand, and the resulting theoretical guarantee follows from past robustness guarantees in a very straightforward manner. This simplicity should be considered a strength of the method, not a weakness of the paper.
3. The experiments are thorough, with comparisons to a wide range of prior methods and on high-dimensional image datasets (e.g., ImageNet).

### Weaknesses
1. The paper states that the theory is based on assumptions and the universality is relatively limited, but does not specify what these assumptions are or why they are stringent. This lack of clarity makes it difficult to assess the limitations of the proposed approach.
2. Definition 3.1 is presented as a definition, but it appears to be a restatement of certified radius theorems for general distributions and norms. This should be clarified and presented as a theorem rather than a definition to accurately reflect its nature.
3. The definition/review of alternative Lebesgue measure should be moved to Section 3.1, where Table 1 appears with Alt. Lebesgue Measure as a column. This would improve the flow and organization of the paper.
4. In Section 4.2, it is unclear whether the loss function is solely a function of the NPG parameters $\theta_g$. It would be beneficial to explicitly write $\mathcal{L}(\theta_g)$ to emphasize the optimization variable. Furthermore, it should be clarified if $\sigma$ and $\mu$ are functions of $\theta_g$, and if so, write $\sigma(\theta_g)$ and $\mu(\theta_g)$ in the smoothing loss expression for clarity.
5. The most significant issue is that the highest performing approach, which uses input-dependent anisotropic smoothing parameters optimized per-input, breaks the robustness certificates. Randomized smoothing certificates rely on using the same model for the nominal input $x$ and all perturbed versions $x+\delta$ within the certified ball. Optimizing $\mu$ and $\sigma$ at $x$ means the certificate only guarantees the same prediction at $x+\delta$ if the same $\mu$ and $\sigma$ are used. However, the scheme re-optimizes $\mu$ and $\sigma$ at $x+\delta$, effectively using a different model. This mathematical breakdown has been noted in prior work, such as Eiras et al. (2022), which uses a memory-based approach to address this issue. The paper should either fix this issue or remove the input-dependent part, as it significantly reduces the contribution of the paper.

### Questions
1. "However, its theory is based on assumptions and the universality is relatively limited." What assumptions? Please at least briefly mention them and why they are stringent.
2. Definition 3.1 does not really appear to be a "definition" in mathematical terms. It looks more like you are re-stating the certified radius theorems for general distributions and norms. So, this should probably be labeled as a "theorem".
3. Please move the definition/review of alternative Lebesgue measure to Section 3.1, where Table 1 appears with Alt. Lebesgue Measure as a column.
4. In Section 4.2, the loss function is solely a function of the NPG parameters $\theta_g$, correct? If so, it would be good to explicitly write $\mathcal{L}(\theta_g)$ to emphasize to the reader what you are optimizing over. Furthermore, $\sigma$ and $\mu$ would be functions of this parameter $\theta_g$, right? If so, it would also be good to write $\sigma(\theta_g)$ and $\mu(\theta_g)$ in the smoothing loss expression.
5. MOST IMPORTANT PROBLEM: Your highest performing approach, using input-dependent anisotropic smoothing parameters that are optimized per-input, breaks the robustness certificates. Namely, randomized smoothing robustness certificates intimately rely on the same model being used to predict at the nominal point $x$ and all perturbed versions $x+\delta$ in the certified ball around $x$. However, if you optimize $\mu,\sigma$ at $x$, then the smoothing-based certificate only says that $x+\delta$ will yield the same prediction if you also use the same parameters $\mu,\sigma$ to define the prediction at $x+\delta$. But, according to your scheme, you actually re-optimize $\mu,\sigma$ at the perturbed test input $x+\delta$ to generate the prediction at $x+\delta$, meaning you are using a different model than what smoothing certifies at $x$. This mathematical breakdown of certified robustness for input-dependent smoothing has been noted before in past works, and is the reason why works like Eiras et al. (2022) augment their input-dependent scheme with "memory." In order for your input-dependent smoothing scheme to work, you would also need to appeal to some "fix" like this memory method, which comes with its own issues (e.g., relating to dependency on input order, and increased memory overhead costs). Either you should fix this issue (and hopefully your certificates still provide substantial improvement over state-of-the-art), or you should remove this input-dependent part of the paper (which, in my opinion, would significantly reduce the contributions of the paper).

### Soundness
1 poor

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes an approach to Certified Robustness via Randomized Smoothing, in which the noise distribution for the different data dimensions is allowed to vary, i.e. is anisotropic. Three example noise parameter generators are proposed, and experimental results given on standard datasets against SOTA methods.

### Strengths
The paper is well presented, clearly structured and well written, with a reasonably comprehensive set of experiments performed.

### Weaknesses
My scoring reflects very much an issue raised in the Questions below. Clarification on that from the authors could substantially change my assessment.

The paper presents only an incremental improvement on SOTA methods, and in many ways the main Theorem (3.2) is really no more than a simple Corollary from prior work with a simple affine transformation on the variables (which would usually be done anyway in dealing with non-image data with very different means and scales in each data dimension).

The main issues, written in questions to the authors, concern (a) the presentation of the comparison with isotropic SOTA, and (b) the validity of the input-dependent noise (the method introduced in section 4.3). This latter is also used as the basis for the main results in section 5.3. Hence my rating for the paper could be improved significantly in light of any author response/clarification to my questions.

Some more minor comments here though:
- The binary case rather than multi-class is used for Cohen. This gives poorer results, of course. Not an issue, as it is done consistently for the proposed and SOTA methods. But it should be at least clarified as the statement of Theorem 3.2 suggests that the p_B value will be used, but then in Table 1 it is not (ie it is replaced by p_B = 1 – p_A)
- The definition of Acc in the Metrics section has it defined as a function of V’_S. And yet V’_S does not appear on the RHS!! (instead you have replaced it with the dth root of the product of the sigmas times R)
- At small radii, the SOTA methods are better (on the graphs) than the proposed method. Some discussion would be welcome on this.
- In section 5.1, it is mentioned that Cohen gives a tight radius. Again, as per above, this is really only in the non-binary form.

### Questions
In the experiments, it seems that the results vs {min \sigma_i} R should be presented (per Corollary 3.3) for a fair comparison, i.e. it is not clear to me that the proposed technique certifies a strictly larger L_p ball in the same conditions than SOTA (and what “same conditions” may mean is not clear e.g. it may mean isotropic sigma=1 and \product \sigma_i = 1 in anisotropic case). That said, the results in section 5.3 apparently include a certified accuracy wrt radius. It is not clear if this may be an answer to my query as it is not clear exactly what is being reported here.

Re section 4.3, I am a bit confused. This input-dependent proposal would give an x-dependent sigma, and hence an x-dependent classifier (ie x-dependent noise, over and above the obvious dependence on x). Theorem 3.2 holds assuming the noise is constant in the ball around x. This proposal in 4.3 violates that surely. Hence it is no longer true that Theorem 3.2 guarantees that the classifier gives an unchanged output in the region claimed, and so the proposed classifier is not certified robust in the claimed reghion around x. I may have misunderstood. Clarification/explanation is welcome.
Please see aeXiv paper 2110.05365 for an example of work done with input-dependent noise.

### Soundness
1 poor

### Presentation
3 good

### Contribution
2 fair
