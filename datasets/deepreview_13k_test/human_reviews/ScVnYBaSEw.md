# UNSURE: Unknown Noise level Stein's Unbiased Risk Estimator

- Decision: Accept
- Scores: 5, 8, 8, 3

## Abstract
Recently, many self-supervised learning methods for image reconstruction have been proposed that can learn from noisy data alone, bypassing the need for ground-truth references.  Most existing methods cluster around two classes: i) Noise2Self and similar cross-validation methods that require very mild knowledge about the noise distribution, and ii) Stein's Unbiased Risk Estimator (SURE) and similar approaches that assume full knowledge of the distribution. The first class of methods is often suboptimal compared to supervised learning, and the second class \corr{tends to be} impractical, as the noise level is \corr{often} unknown in real-world applications.
In this paper, we provide a theoretical framework that characterizes this expressivity-robustness trade-off and propose a new approach based on SURE, but unlike the standard SURE, does not require knowledge about the noise level.}.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents a theoretical framework aimed at addressing the limitations of existing self-supervised learning (SSL) methods for image reconstruction. However, several critical issues undermine its contributions and overall validity.
The proposed estimator builds on Stein’s Unbiased Risk Estimator (SURE) without offering significant advancements beyond existing methodologies. While the authors claim their approach allows for learning in scenarios with unknown noise structures, similar claims have been made in prior works without the need for extensive computational resources. This redundancy raises questions about the paper's originality and its contribution to the field.
The theoretical framework lacks clarity, making it difficult for readers to grasp the practical implications of the proposed methods. The authors introduce constrained self-supervised losses with Lagrange multipliers, but fail to provide sufficient detail on how these constraints improve learning outcomes compared to traditional methods. This omission hampers reproducibility and understanding, which are essential in scientific discourse.
Although the authors present evaluations claiming near state-of-the-art results, they do not adequately benchmark against a comprehensive set of competitive methods. Their focus on a narrow range of tasks, particularly in MRI reconstruction, limits the generalizability of their findings. The evidence provided does not convincingly demonstrate that their method consistently outperforms other self-supervised techniques across diverse applications.
The paper acknowledges that the proposed method requires more computational resources than existing approaches. This raises practical concerns regarding its applicability in real-world scenarios, especially considering that many researchers and practitioners may not have access to such resources. The trade-off between computational efficiency and performance is inadequately addressed, leaving potential users with unresolved questions about feasibility.
While the authors assert that their method generalizes well to complex tasks like MRI reconstruction, they provide insufficient evidence to substantiate these claims. Generalization is a critical aspect of any learning framework; without robust validation across varied datasets and tasks, such assertions remain speculative at best.
In summary, while the paper attempts to tackle relevant issues in self-supervised learning for image reconstruction, it ultimately falls short due to a lack of novelty, clarity, empirical validation, and robust generalization evidence. These shortcomings warrant rejection as they detract from the potential impact and applicability of the research within the broader field of machine learning and computer vision.

### Strengths
1)	The paper presents, a novel family of self-supervised estimators that effectively addresses the challenges of unknown noise levels, extending the capabilities of existing methods like SURE, and well-written.
2)	It offers a clear theoretical framework that elucidates the robustness-expressivity trade-off in self-supervised learning, enhancing the understanding of estimator dynamics.
3)	The paper includes thorough experiments on established datasets, providing solid empirical evidence for the effectiveness of their method compared to other self-supervised methods and showing its applicability across diverse imaging problems.

### Weaknesses
1) Computational complexity was already mentioned by the authors. Proposed method requires additional evaluations during training, leading to increased computational costs and potential implementation challenges.
2) The proposed ZED estimator struggles with high-entropy noise distributions, and the method's effectiveness may vary depending on optimizer settings and hyperparameter tuning. It would be better to provide possible strategies to remedy this 
3) While the experiments demonstrate strong performance in specific tasks, there is limited exploration of diverse imaging applications and noise scenarios, which may affect generalizability. 
4) The related work section can be summarized to better discuss the actual contribution of the current work.

### Questions
1)	In case of correlated Gaussian noise, the construction in (14) assumes that the set of s-dimensional covariance matrices includes the true covariance, i.e., the plausible covariance matrices. This intrinsically assumes a low dimensional structure, but this was not mentioned in the text. Also in practice, this assumption might not hold, and as such it would only do a low-dimensional projection of the true covariance onto s-dimensional space? The consequences and possible solutions of this case is not discussed.
2)	Table 1 results claim that the proposed method perform close (≈ 1dB) to the SURE with known noise model. However, 1dB in PSNR is a distinct difference, and claiming that performing close to the SURE is misleading.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper addresses recent advances in self-supervised learning methods for image reconstruction that learn directly from noisy data, eliminating the need for ground-truth data. The authors introduce a theoretical framework that examines the trade-off between expressivity and robustness in noise-handling techniques.

### Strengths
-  The authors introduce a theoretical framework that examines the trade-off between expressivity and robustness in noise-handling techniques.

- The method does not require knowledge about the noise level to denoise images.

- Numerical validation is presented to verify the ability of the proposed methodology to estimate the noise level.

### Weaknesses
- A primary limitation of this paper is that the denoising experiments are carried out on synthetic scenarios i.e. a clean image is corrupted by noise.  Could the authors consider testing their denoising method and noise level estimation in a more realistic scenario? For instance Noise2Noise (method the authors claim to outperform) has been tested in experimental cryo-em images (see link below). Testing the proposed method in such a scenario would provide valuable insights into its practical applicability, particularly in terms of noise level estimation and the quality of the denoised output.
		
https://github.com/tbepler/topaz/blob/master/tutorial/04_denoising.ipynb

- The image dataset studied in this paper are relatively of low level of details (mostly low frequency images), raising an important question about robustness. How well would the algorithm perform when trained on images with higher levels of detail? Using the cryo-em images would be interesting scenario since resolution it is the most important factor to determine the performance of any denoising method.

**Minor Comment**

- I suggest the authors to change the notation of matrices in capital boldface to be consistent with the current notation of vectors.

### Questions
- On top of my previous comment, the authors did not discuss if the estimation of noise level has limitations in extreme cases? Could the authors discuss whether the noise level estimator is still accurate in low SNR cases which are also common in imaging applications?

- For the case of General inverse problems, it is interesting the proposed method is able to adapt to the range of $A^{T}$. However, it posses the question, could the authors discuss the stability of the proposed method where the dimension of the range is small? What is the limit in terms of range dimension so the propose method is able to accurately estimate the noise level?

- Based on my previous comments some discussion is needed on the performance of the proposed method when the estimation of noise level is performed in extreme cases, and low dimension range of $A^{T}$.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces a novel framework that bridges this gap by proposing a SURE-inspired method that can effectively learn from noisy data without explicit noise-level information. The authors provide theoretical analysis of their proposed method and through experiments, the authors demonstrate good performance compared to existing self-supervised methods on various imaging inverse problems.

### Strengths
This manuscript presents a well-structured and comprehensive review of existing denoising techniques. The clear and logical organization of the content enhances readability.

### Weaknesses
While the contribution of this manuscript may not be groundbreaking, it offers a valuable insight into denoising techniques. Regarding the title, a more descriptive title such as "Unknown Noise Level Estimation via Self-supervised Stein's Unbiased Risk Estimator" would provide a clearer indication of the paper's focus. Additionally, minor punctuation errors are present throughout the manuscript, which could be addressed in a future revision.

### Questions
(n/a)

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper deals with the problem of designing an image/signal denoising algorithm given a sample of noisy images/signals $y_1,\ldots,y_N$ from $\mathbb R^n$. It is assumed that each $y_i$ satisfies the relation $y_i = x_i + \sigma\epsilon_i$, $i=1,\ldots,N+1$, where $\epsilon_i$ is independent of $x_i$ and is drawn from the Gaussian distribution $\mathcal N(0,\mathbf I)$. The proposed method is solve with respect to $f$ and $\eta\in\mathbb R$ 
the optimization problem
$$
\min_f \max_{\eta} \frac1N \sum_{i=1}^N \Big(|f(y_i) - y_i|^2 + 2\eta \ \textrm{div} f(y_i)\Big),
$$
where $f$ is chosen from a parametric class of functions, such as neural networks with a given architecture and varying weights. 

Extensions to the setting of a noise covariance matrix of a more general form are also considered. In particular, if $y_i = x_i + \Sigma^{1/2}\epsilon_i$ with $\Sigma = \sum_{j=1}^s \eta_j \Psi_j$, where $\Psi_1,\ldots,\Psi_s$ are some known matrices and $\eta\in\mathbb R^s$ is an unknown vector, the proposal is to solve the saddle point problem
$$
\min_f \max_{\eta\in\mathbb R^s} \frac1N \sum_{i=1}^N \Big(|f(y_i) - y_i|^2 + 2\sum_{j=1}^s \eta_j \ \textrm{Tr} [\Psi_jf(y_i)]\Big).
$$
(There is a mistake in this formula as it is written in the paper, the correct form should be
$$
\min_f \max_{\eta\in\mathbb R^s} \frac1N \sum_{i=1}^N \Big(|f(y_i) - y_i|^2 + 2\sum_{j=1}^s \eta_j \ \textrm{Tr} \big[\Psi_j \ Df(y_i)\big]\Big)
$$
where $Df$ is the Jacobian matrix of $f$. 

The main mathematical result of the paper, stated in Theorem 3, provides the explicit form of the minimizer of the problem above.

### Strengths
The paper is pleasant to read. The proposed method is based on a simple idea and the experiments show that it improves on some methods that have been recently proposed in the literature (such as Noise2Void, Neighbor2Neighbor).

### Weaknesses
1. Mathematical analysis of the proposed methodology is very light. In particular, neither the properties of the proposed estimator nor the convergence of the optimization algorithm are studied.  

2. The framework for the learning problem is not clearly defined. The abstract and introduction reference supervised and self-supervised settings multiple times, but how these settings are interpreted in image reconstruction remains unclear. This only becomes explicit at the bottom of page 7, where it is clarified that the available data consist of $y_1, \ldots, y_N$. I recommend moving this clarification to the beginning of Section 2.

3. In Sections 2 and 3, the term estimator is repeatedly used to describe objects that cannot be computed directly from the data, as they rely on knowledge of the distribution of $y$. To avoid this misuse of terminology, it would be preferable to use a more accurate term.

4. Minor comments and typos:
- In the second paragraph of Section 1 on page 1, the two items starting with "i) SURE" and "ii) Noise2Self" are presented in a different order than in the abstract. For the sake of consistency throughout the paper, it would be beneficial to align their order.
- Page 3, the two lines just above Eq. (5): I guess $\mathbb R^m$ should be replaced with $\mathbb R^n$.
- Page 3, Eq. (4): This formula is easy to obtain, but it might be useful to provide a reference for non-experts. 
- Page 4, Eq. (UNSURE): I suggest putting parentheses around the expression within the expectation, to underline that the divergence is also under the expectation. 
- Something wrong with formula (14). The gradient of $f$ should appear in the second term.
- Page 6: "are more flexible" -> "are more flexible than"
- Page 6: "we can considering" -> "we can consider"

5. The setting under consideration closely resembles what is commonly known as the empirical Bayes framework. A discussion of the relevant literature on empirical Bayes methods would be a valuable addition.

6. The title of the paper appears somewhat misleading. It suggests that the paper will propose an unbiased estimator of the risk of an estimator $f(y)$ in the case where $\sigma$ is unknown, implying that the unbiased risk estimator would not depend on $\sigma$. However, the paper instead restricts attention to estimators $f$ for which the Stein unbiased risk estimate (SURE) happens to be independent of $\sigma$.

### Questions
An important argument in the proof of Theorem 3 is the use of strong duality. The authors refer to (Luenberger, 1969, Chapter 8). I believe they are referencing Theorem 1 on page 224. (If this is indeed the case, it would be helpful to highlight it in the paper.) I have a question related to the application of this theorem. Assuming that the constraint is of the form $G(x) \leqslant \theta$, the theorem requires the existence of $x_1$ such that the strict inequality $G(x_1) < \theta$ holds. My impression is that this condition cannot be satisfied in the setting under consideration. However, I may have overlooked something. Could the authors please clarify this?

### Soundness
3

### Presentation
2

### Contribution
2
