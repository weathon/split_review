# On the Relation Between Linear Diffusion and Power Iteration

- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 3, 6

## Abstract
Recently, diffusion models have gained popularity due to their impressive generative abilities. These models learn the implicit distribution given by the training dataset, and sample new data by transforming random noise through the reverse process, which can be thought of as gradual denoising. In this work, we examine the generation process as a ``correlation machine'', where random noise is repeatedly enhanced in correlation with the implicit given distribution. 
To this end, we explore the linear case, where the optimal denoiser in the MSE sense is known to be the PCA projection. This enables us to connect the theory of diffusion models to the spiked covariance model, where the dependence of the denoiser on the noise level and the amount of training data can be expressed analytically, in the rank-1 case.
In a series of numerical experiments, we extend this result to general low rank data, and show that low frequencies emerge earlier in the generation process, where the denoising basis vectors are more aligned to the true data with a rate depending on their eigenvalues. This model allows us to show that the linear diffusion model converges in mean to the leading eigenvector of the underlying data, similarly to the prevalent power iteration method. 
Finally, we empirically demonstrate the applicability of our findings beyond the linear case, in the Jacobians of a deep, non-linear denoiser, used in general image generation tasks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper studies the generation process of diffusion models. Focusing on linear models where the diffusion process is similar to performing noisy PCA, the authors show that the generation process of the linear diffusion model is similar to the power iteration method in that it converges to the leading eigenvector of the underlying data distribution.

### Strengths
The authors aim to provide an analysis of the diffusion process, an important question for diffusion models. This is achieved using a simple model.

Overall, the writing is easy to follow.

### Weaknesses
Providing theoretical studies for complex problems in deep learning and deep generative models is often very challenging. Thus, it is common practice to study a simpler problem that can shed light on the underlying mechanisms of more complex ones. While this work falls into this category, I found that the results for the linear diffusion model diverge significantly from the phenomena observed in real cases.

(1) Theorem 4.3 shows that the diffusion process only converges to the dominant eigenvector (the one corresponding to the largest eigenvalue). Thus, it gives a bad estimation for the true distribution with a dimension larger than 1. While eq. (25) also provides a formulation when noise is injected in the intermediate steps, (i) it does not provide an estimation guarantee for the entire spectrum, (ii) many recent diffusion models such as DDIMDMP-solver do not require the injection of noise in the intermediate steps.

(2) The results in Section 5 (e.g, Figure 7) on real cases only demonstrate the convergence to the entire spectrum, not the dominant eigenvector. This also supports the gap between the analysis in Theorem 4.3 and the phenomenon observed in real cases. 

(3) Initially, I thought Section 5 was intended to support the argument that the diffusion process converges to the "true distribution" as in Theorem 4.3. However, this is not the case, as Figure 7 plots the convergence of the network Jacobian evaluated at $x_t$. Thus, even at $t= 0$, it depends on the learned network and does not represent the true distribution of the data; the convergence probably holds as long as the network is Lipschitz. In other words, the convergence does not indicate the quality of the diffusion process. For example, a network that outputs all zeros would also exhibit fast convergence. I may be misinterpreting the results; if so, I'd appreciate clarification.

### Questions
(1) what are $x_j$ and $n$ in eq. (26)? 
(2) where $v_j$ right after eq. (26) should be $u_j$.
(3) line 487: what is $J$ in $sin(\theta_J)$? is it $i$?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper explore diffusion reverse sampling process by analyzing a linear diffusion model. The main result is that the reverse sampling process leads to samples that concentrate on the first eigenvector of the covariance matrix of the underlying data.

### Strengths
The paper has a clear structure and is easy to read. The topic is also interesting since studying the evolution of the denoisers along diffusion trajectory is important but less well explored in the literature.

### Weaknesses
I have doubt on both the theoretical and practical aspects of this work. The theoretical results do not seem correct (correct me if I am wrong) and the connection to practice is weak. I list my questions as below:

*Major questions:

(i) Can the author explain how do they conclude Theorem 4.3 ? The author claimed that the final projection operator is a diagonal matrix with a spectrum concentrate around the first eigenvalue (line 409-412) and they supported this claim qualitatively in Figure 5. However, I cannot find a close-form expression for this projection matrix as in the limit of $\tau\rightarrow \infty$. From (24) I would assume 
\begin{align}
\mathbb{E}\mathcal{P_{\tau}}=U_0 c_0^\tau\text{diag}[1, (\frac{c_1}{c_0})^\tau,...] U_0^T,
\end{align}
, which do not really hold since equation (20) only holds for small t. If we assume this expression holds, we have 
\begin{align}
\mathbb{E}x_gx_g^T=(U_0c_0^{2\tau}\text{diag}[1, (\frac{c_1}{c_0})^{\tau},...])(\mathbb{E}[\epsilon_T\epsilon_T^T])(\text{diag}[1, (\frac{c_1}{c_0})^{\tau},...]U_0^T).
\end{align}

By the assumption that diffusion stepsize is $\frac{1}{T}$ and there are $T$ steps in total (line 360-361), we have $\epsilon_T\sim\mathcal{N}(0,\frac{1}{T})$. Therefore $\mathbb{E}x_gx_g^T=U_0\text{diag}[c_0^{2\tau}/T, c_1^{2\tau}/T,...]U_0^T$. Then how does this term equal to $u_0u_0^T$ as in equation (17)? Shouldn't all eigenvectors go to zero as $T\rightarrow \infty$ ? 


(ii) In section 5 the author claims that correlation of the low indices (lower frequencies) withstands higher noise levels. However, it is shown in Figure 7 that many of the dark curves remain flat during a wide range of time steps and only drop when t approaches 0, which is very different from linear case (Figure 3) that show a gradual evolution of the sine angles. Therefore I disagree with that the decaying behavior of the nonlinear model  is similar to that in the linear case.

*Minor questions:
(i) The Figure 7 is very difficult to read since all the useful information is concentrated near $t=0$. I suggest the authors to redraw the plot using log scale.

(ii) The paper could benefit from putting more details on the theoretical results in an appendix. Not sure whether authors are allowed to add one.

### Questions
I'd like to summarize my final assessment of this paper here:

1. First of all, the authors argue a linear diffusion models generate samples that concentrate on the first eigenvector of the covariance matrix. However, the diffusion models considered are not trained with the standard denoising score matching loss, rather, it is trained with a sequential denoising loss that is very different from the standard diffusion model. Besides the training loss, the reverse diffusion process considered in this paper is also not the standard reverse diffusion process. Due to this differences between the model considered in the paper and the standard diffusion model (which is not clearly explained in the paper), the conclusion in this paper can be misleading to the general public. The theorem states the linear diffusion models can only generate images that concentrate on the first eigenvector, thus of limiting diversity. However, as I've shown in my comment, the optimal linear diffusion models trained with standard diffusion denoising score matching loss are equivalent to the score function of noisy Gaussian distributions. Therefore, standard reverse sampling using the optimal linear diffusion models is equivalent to sampling from a Gaussian distribution, which can generate samples with great diversity. I urge the author to carefully take care of this discrepancy between standard diffusion and the model they considered, to avoid any misleading. 

2. Second, in the section 5 of the paper the authors investigate the Jacobian and state the linear diffusion model is similar to the nonlinear diffusion model. However, while there indeed is certain similarity between case and nonlinear case, a significant amount of dissimilarity also exists but is ignored by the authors without any discussion. The implication of this section is also unclear. I expect the authors to discuss the property of the final generated samples from the nonlinear diffusion models with some mathematical formulation. Please notice that for linear model, the Jacobian fully explains the network behavior since Jacobian is the linear weight itself. However, for nonlinear models, the Jacobian $\nabla f(x_t)$only captures how the network's output change w.r.t. to input $x_t$ at a local region. However, to investigate the property of the final samples, we need to study the property of $f(x_t)$ itself. 

3. Third, some assumptions made in this paper is not valid. For example, the author cannot assume $\sigma_t=\frac{1}{T}$ (line 354), which implies $\epsilon_t\sim N(0,\frac{1}{T})$. Under this assumption, more sampling steps result in smaller amount of noise at the end stage of diffusion forward process. However, the noise level at the end of the forward diffusion should be sufficiently large so that the noisy distribution at time step is approximately a Gaussian distribution with zero mean. If this is violated, the reverse sampling process starting from a random Gaussian noise can not recover the clean distribution. Though the authors in the comment argue they use valid schedule in the numerical experiment, I do believe they should derive their theorem from valid schedule as well. Unfortunately since the theorem derived in the paper explicitly depends on $T\rightarrow \infty$, the $\epsilon_t$ will be extremely small, directly contradict the basic assumption of diffusion model, therefore the theorem is less meaningful.

In conclusion, I suggest rejection for the paper and I believe major revision should be made before the next submission.

### Soundness
1

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
The explores the relationship between the power iteration method and diffusion models with a linear denoiser, that can be modeled as a PCA projection, enabling analysis via the spiked covariance model. The authors demonstrate that, in the reverse process, high eigen-value components emerge earlier, and leading eigenvectors align with the data distribution.

### Strengths
The paper provides a novel perspective on diffusion models for understanding the generation process by drawing parallels with power iteration. The work opens up new research directions for improving the interpretability and performance of generative models by highlighting the eigenvector alignment properties in diffusion models. The paper is well-written with most claims justified theoretically and backed by empirical evidence.

### Weaknesses
The paper does a good job at conveying the idea and intuition from the simulations, however, the proof of the main result (Theorem 4.3), could be refined more. Particularly, I can not fully understand the proof in the high noise regime i.e., $\tau \leq t \leq T$. A more explicit explanation for the following statement would enhance the rigor: how exactly does Assumption 4.2 guarantee that $U_\tau^\top U_{\tau+1}$ is diagonal just enough not to spoil the diagonality of the next partial operator $\mathbb E \mathcal P_{\tau+1}$? Can the authors justify this mathematically? 

- Most experiments for linear case are done on MNIST- could the authors clarify to what extent the assumptions made in the spiked covariance model apply to real-world datasets? For example, in cases where the low-dimensional subspace assumption does not hold.
- Moreover, since power iteration is such a major theme of the paper, a small discussion of the power iteration method in the introduction would help enhance readability.
- The term $u_i^t$, has never been defined. Moreover, a consistent notation of keeping time in the superscript and index in the subscript  (or vice-versa) for both vectors and matrices will help avoid confusion.

### Questions
- Most experiments for linear case are done on MNIST- could the authors clarify to what extent the assumptions made in the spiked covariance model apply to real-world datasets? For example, in cases where the low-dimensional subspace assumption does not hold.
- Moreover, since power iteration is such a major theme of the paper, a small discussion of the power iteration method in the introduction would help enhance readability.
- The term $u_i^t$, has never been defined. Moreover, a consistent notation of keeping time in the superscript and index in the subscript  (or vice-versa) for both vectors and matrices will help avoid confusion.

### Soundness
3

### Presentation
3

### Contribution
3
