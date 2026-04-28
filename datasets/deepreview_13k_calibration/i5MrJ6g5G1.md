# Simple and Controllable Uniform Discrete Diffusion Language Models

- Decision: Accept
- Avg Score: 5.25
- Scores: 6, 6, 6, 3

## Abstract
Diffusion models for continuous data gained widespread adoption owing to their high quality generation and control mechanisms. However, controllable diffusion on discrete data faces challenges: continuous diffusion guidance methods are not applicable and recent discrete diffusion models are not well-suited to control or exhibit a quality gap. Here, we provide a straightforward derivation of classifier-free and classifier-based guidance for discrete diffusion, as well as a new class of diffusion models that leverage uniform noise and thus can continuously edit their outputs. We improve the quality of these models with a novel continuous-time variational lower bound that yields state-of-the-art performance, in settings with small vocabularies. Empirically, we demonstrate the effectiveness of our guidance mechanisms relative to autoregressive and diffusion baselines, especially in conjunction with uniform noise diffusion, on several discrete data domains, including genomic sequences, small molecule design, and discretized image generation.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents several advances in discrete diffusion models, specifically focusing on uniform noise diffusion and guidance mechanisms. The authors make three main contributions:

-  developing classifier-based and classifier-free guidance for discrete diffusion models,

-  introducing Uniform Diffusion Language Models (UDLM) with an improved variational bound

-  demonstrating superior controlled generation compared to autoregressive baselines across multiple domains.

### Strengths
-  Theoretical foundation with clear derivations of the continuous-time variational bound

- Practical guidance mechanisms that are easy to implement

- Thorough ablation studies and hyperparameter analysis

### Weaknesses
The primary limitation is the scope of improvements being mainly restricted to multinomial diffusion with small vocabulary settings, with a persistent performance gap in larger vocabulary NLP tasks. The paper lacks computational complexity analysis and detailed runtime comparisons. Some hyperparameter choices, particularly sampling steps T, would benefit from more thorough justification. The theoretical analysis of guidance mechanisms could be more extensive, and more exploration of failure cases would strengthen the work.

### Questions
- What are the primary factors limiting performance on larger vocabularies, and how might these be addressed?

- How to understand equation 9, does it have any connection with the loss in Lou 2023?

- How does the choice of sampling steps T affect the trade-off between generation quality and computational cost? Is there a systematic way to choose optimal T?

- Have the authors explored potential failure modes of their guidance mechanisms, especially in cases where the guidance strength $\gamma$ is high?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a discrete diffusion model and guidance mechanism that is effective at controllable generation. The paper uses discrete classifier-based and classifier-free guidance, and introduces uniform noise diffusion language models that can continuously edit discrete data.

### Strengths
1. Adapting diffusion model to discrete data is an important task as it can be utilized to a few data generation tasks, such as molecule and text generation.

3. The experiments demonstrate the effectiveness of guidance with discrete diffusion models on several domains, and show that UDLM can achieve state-of-the-art performance on small vocabulary datasets.

### Weaknesses
 1. In Introduction, "D-CBG" is introduced before being explained.

2. I would recommend the paper to explain the logic, why the proposed UDLM can make the guidance easier? To me I think the only difference is to reset the $\pi$ value in the proposed method. How can we understand the motivation for this setting and what's the intuition?

3. In the first paragraph of Section 3.2, the paper mentions that the proposed method yields a simple expression for ELBO, but I didnt see ELBO below. Also, I would suggest the paper use a table to compare the new and the old ELBO to make the improvement more clear.

### Questions
See weakness above.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In this paper, the authors derive classifier-free and classifier-based guidance for discrete diffusion-model controllable generation.  The proposed guidance techniques build upon discrete diffusion techniques that interpolate between clean data and a noisy prior.   Empirically,   the proposed method outperforms Autoregressive models and several diffusion-model baselines on genomic sequences, small molecule design and CIFAR-10.

### Strengths
1.  The paper is well-written and well-organized. 

2. The proposed method is simple and easy to follow. 

3. It seems the proposed method outperforms baselines on several discrete tasks.

### Weaknesses
1.  The description of the contribution is not clear enough.  Some parts may be overclaimed.

I am not sure whether the claimed contribution is classifier-free and classifier-based guidance for a discrete diffusion-model controllable generation or if it further includes the interpolating discrete diffusion model parts.  In Line 58 on page 2, the authors claim they introduce "a class of discrete diffusion models particularly amenable to guidance."  This part may be overclaimed because the key technique involved is the simplified discrete diffusion process with the transition probabilities as the interpolation between the current state and a prior distribution. This technique may not be new. See the following point two.

2. Very similar discrete diffusion works are not discussed and compared.

In both [1] and [2],  similar simplified discrete diffusion processes with the transition probabilities as the interpolation between the current state and a prior are employed,  which is very related to the proposed method. However,  discussion and comparison with these works are missing.   As a result, the claimed SOTA performance is unconvincing. Specifically, the lack of comparison makes it difficult to assess whether the performance gains are due to the proposed guidance methods or the specific choice of the underlying diffusion process, which is similar to existing methods.

3. What is the key advantage of the proposed method over other discrete diffusion methods is not clearly discussed. 

What is the key advantage of the proposed method compared with other discrete diffusion methods? Why does the proposed method perform better than other discrete diffusion methods? The paper lacks a detailed analysis of the specific properties of their method that lead to improved performance, such as convergence rates, stability, or computational efficiency compared to alternatives.

4.   The equitation in Line 181 on page 4 may not be correct. 

Why does the log(p) term equal the inner product term?

### Questions
1. Please clarify the contribution of this paper as the point one listed in the above weakness part. 

2. What is the relationship and difference between the proposed discrete diffusion method and the one in [1] and [2] listed above?

3. What is the key advantage of the proposed method compared with other discrete diffusion methods? Why does the proposed method perform better than other discrete diffusion methods?

4. Please explain about the equitation in Line 181 on page 4.  Why does the log(p) term equal the inner product term?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes to introduce uniform noising paths for discrete diffusion models. The paper derives an explicit formulation for the variational lower bound under a uniform prior. The paper further introduces methods to perform classifier-free and classifier-based guidance in this discrete diffusion setting. Experiments are conducted in regular text, images, genome, and molecular settings.

### Strengths
The paper is generally well written with the development of ideas following a logical narrative. The experimental settings considered are also diverse in terms of various discrete domains. Beyond this, it is difficult to pinpoint further clear strengths.

### Weaknesses
I appreciate the authors for trying to crisply write their simple uniform diffusion model framework but I have several critical concerns regarding various aspects of this paper that I will outline below.

**Novelty**

I very respectfully disagree with the author's contributions. The uniform prior and the corresponding are widely known and exist in the literature. In fact, I challenge the authors to demonstrate how their formulation differs from Discrete Flow Matching (Gat et. al 2024), and Dirichlet Flow/Diffusion (Stark et. al). There are other papers as well, but very explicitly your objective function in your variational lower bound can be shown $\mathbb{E}[-\log p(x_0 | x_t)]$ where $x_t \sim p_t(x)$ is the uniform path. This analysis is a direct application of the MDLM setup for the uniform path. I am open to being wrong here, but I do not see anything novel here despite equation 10 suggesting there is more going on than there is. Also, I believe the first-order Taylor approximation to guidance was already introduced in 
(Nisonoff et. al 2024) and the adaptation in this paper is very respectfully a minor change.


**Technical Limitations**

Regarding the new classifier/classifier-free guidance formulation the fact that we need to compute the normalization constant means that this cannot be extended to actual larger-scale systems where we would want to apply discrete diffusion models as opposed to autoregressive ones. I have severe concerns regarding the usefulness of the claim that the proposed method works well on small vocabularies, this to me is a sign that this approach is fundamentally limited. Note that Dirichlet Flow Matching (Stark et. al 2024) point out this exact issue with a uniform prior paths, and hence suggest their Dirichlet paths.

**Experimental Concerns**

Regarding the experimental setup I have a few concerns regarding the results presented. I find the omission of MDLM for the LM1B table 3 to be awkward. Looking at Table 1 in the MDLM paper we notice that their test perplexity upper bound is 27.04 which is better than the UDLM. In fact, I really do not understand the need to report Table 1 and 3 for the same dataset, it feels contrived to change the vocabulary size. It is clear that uniform doesn't work in this setting and I bet playing with noise schedules and other small details would close the gap for MDLM and UDLM in the smaller scientific settings. I also found it surprising the Generative Perplexity under GPT-2 was not reported as MDLM does. Finally, there are no textual generated samples as done for even CIFAR 10. This is a strange omission, we should be able to visually inspect the difference in suspected performance.

### Questions
N/A

### Soundness
2

### Presentation
3

### Contribution
1
