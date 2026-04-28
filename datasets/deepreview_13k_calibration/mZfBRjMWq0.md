# G2D2: Gradient-guided Discrete Diffusion for image inverse problem solving

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 6, 6, 5

## Abstract
Recent literature has effectively leveraged diffusion models trained on continuous variables as priors for solving inverse problems. Notably, discrete diffusion models with discrete latent codes have shown strong performance, particularly in modalities suited for discrete compressed representations, such as image and motion generation. However, their discrete and non-differentiable nature has limited their application to inverse problems formulated in continuous spaces. This paper presents a novel method for addressing linear inverse problems by leveraging image-generation models based on discrete diffusion as priors. We overcome these limitations by approximating the true posterior distribution with a variational distribution constructed from categorical distributions and continuous relaxation techniques. Furthermore, we employ a star-shaped noise process to mitigate the drawbacks of traditional discrete diffusion models with absorbing states, demonstrating that our method performs comparably to continuous diffusion techniques. To the best of our knowledge, this is the first approach to use discrete diffusion model-based priors for solving image inverse problems.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors propose a method for solving inverse problems using discrete diffusion models with gradient guidance. They utilize the Gumbel trick to relax the categorical distribution, allowing for gradient computation. Additionally, they introduce star-shaped diffusion models to address the limitations of conventional discrete diffusion models. This approach increases the probability of transitioning to the absorbing state, enabling correction of erroneous codes. In experiments, the proposed method outperforms previous continuous pixel/latent domain diffusion model-based inverse solvers in super-resolution and deblurring tasks. They also apply it to a path-following task using a generative masked motion model.

### Strengths
The authors propose novel methods to address challenges arising when adapting previous approaches to the new task of discrete inverse problems.

### Weaknesses
The motivation for using a discrete diffusion model in the image domain is lacking. Given the availability of options to reduce computational burden, such as low-precision floating points or lighter models, the necessity of a discrete representation is not clearly justified. It would be more convincing if the proposed method demonstrated its advantages in areas where discrete representations are essential, such as language or molecular modeling. To strengthen the paper, consider the following suggestions:
- Compare the discrete approach directly with continuous models that use low-precision or lightweight architectures.
- Include experiments in domains where discrete representations are inherently suitable, such as text generation or molecular modeling.
- Discuss any potential advantages of discrete representations in image domains that may not be immediately clear from the current results.

- How does the discrete star-shaped diffusion process compare with its continuous counterparts in terms of similarities and differences? Could you discuss the specific challenges the authors faced when adapting star-shaped diffusion to discrete spaces and the strategies used to address them? Additionally, please elaborate on any unexpected advantages or limitations of the discrete version compared to the continuous model.
- Could discrete star-shaped diffusion models be integrated with diffusion model-based solvers like DDRM or DDNM?
- The proposed method outperforms even continuous-domain algorithms in image tasks. Were the experiments conducted under computational constraints? If so, please specify these restrictions and provide evaluations under unrestricted conditions as well.

Possible Errors
- Proof of Lemma B.3: The proof appears incorrect. In Lines 975 to 980, the claim that the reverse transition inverts the forward process and leads to equality with $\delta_{z_0, z_0{\prime}}$ should be revised. While the lemma’s conclusion is unaffected, replace exact equalities with equality in distribution where appropriate.
- Line 265: $z_t \to z_{t-1}$.

### Questions
- How does the discrete star-shaped diffusion process compare with its continuous counterparts in terms of similarities and differences? Could you discuss the specific challenges the authors faced when adapting star-shaped diffusion to discrete spaces and the strategies used to address them? Additionally, please elaborate on any unexpected advantages or limitations of the discrete version compared to the continuous model.
- Could discrete star-shaped diffusion models be integrated with diffusion model-based solvers like DDRM or DDNM?
- The proposed method outperforms even continuous-domain algorithms in image tasks. Were the experiments conducted under computational constraints? If so, please specify these restrictions and provide evaluations under unrestricted conditions as well.

Possible Errors
- Proof of Lemma B.3: The proof appears incorrect. In Lines 975 to 980, the claim that the reverse transition inverts the forward process and leads to equality with $\delta_{z_0, z_0{\prime}}$ should be revised. While the lemma’s conclusion is unaffected, replace exact equalities with equality in distribution where appropriate.
- Line 265: $z_t \to z_{t-1}$.

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Authors propose Gradient-guided Discrete Diffusion (G2D2), a novel method for solving linear inverse problems using discrete diffusion as priors. Limitations of discrete diffusion priors are overcame by approximating posterior with variational distribution constructed from categorical distributions and continuous relaxation techniques. Authors demonstrate their method on super-resolution and Gaussian deblurring tasks on ImageNet and FFHQ datasets. G2D2 is compared against popular baselines such as DPS, DDRM, PSLD and ReSample and found to be competitive against continuous diffusion models.

### Strengths
* The paper is written very well.
* Using discrete diffusion priors for solving inverse problems is a novel direction that is not well explored.
* Usage of star-shaped noise process is motivated well with big gain in downstream performance compared to the standard Markov noise process.

### Weaknesses
 * While I appreciate the novelty of using discrete diffusion models in the context of inverse problems, the advantages of using them against continuous counterparts are not motivated well.
* See the questions below.
 * Line 436: "For the image inverse problem experiments, we used text prompts for the VQ-Diffusion model...", do the authors use similar text conditioning for competing methods? If not would it give unfair advantage to G2D2?
* In the limitations section, it is mentioned that "G2D2 does not significantly surpass its continuous counterparts in terms of computational speed or performance". Is there a clear advantage of using discrete diffusions?
* In the appendix, authors provide the hyperparameters used for competing methods (DPS, DDRM, etc.). Are those values taken directly from the corresponding papers or a hyperparemeter search was conducted to find them?
	* If taken directly, I would recommend tuning them separately since in my experience these values are not robust against small changes in the problem setup (some papers add noise to the image in the range [-1,1] some in [0,1] etc.).
	* If the latter one, it would be good to describe which range was searched over how many validation samples.

### Questions
* Line 436: "For the image inverse problem experiments, we used text prompts for the VQ-Diffusion model...", do the authors use similar text conditioning for competing methods? If not would it give unfair advantage to G2D2?
* In the limitations section, it is mentioned that "G2D2 does not significantly surpass its continuous counterparts in terms of computational speed or performance". Is there a clear advantage of using discrete diffusions? 
* In the appendix, authors provide the hyperparameters used for competing methods (DPS, DDRM, etc.). Are those values taken directly from the corresponding papers or a hyperparemeter search was conducted to find them? 
	* If taken directly, I would recommend tuning them separately since in my experience these values are not robust against small changes in the problem setup (some papers add noise to the image in the range [-1,1] some in [0,1] etc.).
	* If the latter one, it would be good to describe which range was searched over how many validation samples.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The authors propose G2D2, a diffusion model-based inverse problem solver (DIS) that uses a discrete diffusion model. To the best of my knowledge, this is the first work to demonstrate that this is possible. Since using the usual mask-observing Markov process of discrete diffusion models makes it hard to correct for the errors arising in the earlier stages of the sampling, the authors propose to use a star-shaped diffusion, where similar to DDIM, $z_t$s are conditionally independent given $z_0$. During inference, the parameters $\alpha$ of the variational reverse categorical distribution are optimized by balancing the prior and the likelihood, which is grounded by sound theory. Experiments are conducted on a standard FFHQ/ImageNet settings.

### Strengths
1. To the best of my knowledge, this is the first work to target using discrete diffusion models for solving inverse problems. G2D2 will open up new opportunities for testing out different discrete diffusion priors.

2. The theory is sound, and the resulting algorithm is straightforward to understand and implement. This resembles how most of the current DIS is implemented in practice, where the predicted $x_0$ is used to compute the likelihood loss, and the sampling to $x_{t-1}$ is conducted with a DDIM sampling step.

### Weaknesses
1. The results are weak. This is somewhat understandable given that the pre-trained diffusion prior is suboptimal, and latent diffusion models (whether continuous or discrete) tend to be inferior to pixel-based methods due to the existence of decoders. Specifically, the paper does not provide a detailed analysis of the limitations of the VQ-VAE decoder, which is known to introduce artifacts and information loss. A more thorough investigation into how the decoder impacts the performance of the inverse problem solver is needed, including a comparison with pixel-based diffusion models.

2. The presentation could be improved. Using a star-shaped noise process is one of the crucial contributions of the work, but this is first introduced in 3.1. A brief review of this before the main section would be beneficial for better understanding. The current introduction does not adequately motivate the need for a star-shaped diffusion process, leaving the reader to wonder why the standard Markov chain approach is insufficient. A clearer explanation of the limitations of the standard approach and how the star-shaped diffusion addresses them is necessary.

3. Many readers interested in the work will already be familiar with the family of continuous diffusion-based methods, and in many points, G2D2 resembles them. It would be beneficial for the authors to draw links to the continuous counterpart, especially in the construction of the sampling. The paper lacks a detailed comparison of the sampling procedures between G2D2 and continuous diffusion models, particularly in terms of how the optimization of the variational reverse categorical distribution relates to the denoising process in continuous methods. A more in-depth discussion of the theoretical and practical differences is needed.

4. Motion inverse problem solving is demonstrated without any comparison. The paper only presents qualitative results for motion inverse problem solving, without any quantitative evaluation or comparison to existing methods. This makes it difficult to assess the effectiveness of G2D2 for this task. A quantitative comparison with state-of-the-art motion synthesis methods is needed to validate the claims.

5. It is discussed that G2D2 can be used with MaskGIT, which is one of the main strength of the work. However, MaskGIT is only used for motion inverse problem solving, which only consists of a small proportion of the experiments. The paper does not explore the potential of using MaskGIT for image inverse problems, which is a significant missed opportunity. Given that MaskGIT is a powerful prior, it would be valuable to see how it performs in comparison to VQ-diffusion for image tasks.

### Questions
Did the authors try using MaskGIT prior to image inverse problems? It is a better prior than VQ-diffusion, and it would be surprising if the results did not improve by simply switching the pre-trained model.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper solves inverse problems in image processing by leveraging discrete diffusion models. Unlike prior approaches using continuous diffusion models, G2D2 introduces a star-shaped noise process and variational relaxation to enable the use of discrete diffusion models in continuous image reconstruction tasks, such as super-resolution and Gaussian deblurring.

### Strengths
1. G2D2 is original in its use of discrete diffusion models for solving inverse problems, which were previously limited to continuous domains. The introduction of the star-shaped noise process and continuous relaxation techniques shows a creative solution to a challenging problem of applying discrete models to continuous tasks.

### Weaknesses
1. While G2D2 introduces innovative techniques, the computational complexity of the variational optimization and continuous relaxation might be higher than other methods. The paper could benefit from more detailed discussions on the computational trade-offs, specifically regarding the number of optimization steps per time step and the potential for adaptive scheduling of these steps, to make the approach more efficient. The current analysis lacks a rigorous comparison of the computational cost with other methods, particularly in terms of wall-clock time and memory usage, which is crucial for practical applications.


2. The paper focuses primarily on image processing tasks such as super-resolution and deblurring, with limited exploration of other possible applications. Extending the method to more diverse and complex inverse problems, such as in other imaging modalities or higher-dimensional data (e.g., 3D medical imaging), would improve the robustness and generalizability of G2D2. The current scope limits the impact of the proposed method, and a more thorough investigation into its applicability to different data types and problem settings is needed.


3. Although G2D2 is compared with several continuous diffusion models, a more thorough comparison with the latest emerging techniques, such as latent diffusion models or score-based generative models, would strengthen the evaluation. The current comparisons do not fully capture the state-of-the-art, and a more comprehensive benchmark is necessary to fully assess the performance of G2D2 relative to other leading methods.


4. The paper emphasizes that the star-shaped noise process can correct early-stage errors, but it does not explore the limitations of this mechanism in depth. There could be scenarios where certain types of errors are less tractable, and a discussion on the failure modes of G2D2 is needed. Specifically, the paper should analyze how the method performs when the initial estimate is far from the true solution, and whether the star-shaped noise process can effectively recover from such situations.


5. More related work should be cited such as "Diffusion modeling with domain-conditioned prior guidance for accelerated mri and qmri reconstruction".

### Questions
1. How does the star-shaped noise process enable the "re-masking" operation, and why is this beneficial for solving inverse problems?

2. What are the advantages of using a star-shaped noise process over a standard Markov process for sampling in discrete diffusion models?

3. What does the term "conditionally independent" imply about the relationship between the noisy discrete latents z1, z2,...,zT given z0 in the star-shaped noise process?

4. What does Property 2 suggest about the relationship between the marginal distributions of the joint distribution q_sampling and the star-shaped noise process graphical model?

5. How does the mean-field structure of both q(zt - 1 | z0) and p_\alpha (z0|zt,y) impact the marginalization process in the G2D2 method?

6. In the algorithm, What challenges might arise if the optimization process does not incorporate the values from the previous time step during initialization?

### Soundness
3

### Presentation
2

### Contribution
2
