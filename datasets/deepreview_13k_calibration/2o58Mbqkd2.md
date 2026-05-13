# The Superposition of Diffusion Models

- Decision: Accept
- Avg Score: 7.33
- Scores: 6, 6, 10

## Abstract
The Cambrian explosion of easily accessible pre-trained diffusion models suggests a demand for methods that combine multiple different pre-trained diffusion models without incurring the significant computational burden of re-training a larger combined model. In this paper, we cast the problem of combining multiple pre-trained diffusion models at the generation stage under a novel proposed framework termed superposition. Theoretically, we derive superposition from rigorous first principles stemming from the celebrated continuity equation and design two novel algorithms tailor-made for combining diffusion models in SuperDiff.  We demonstrate that SuperDiff is scalable to large pre-trained diffusion models as superposition is performed *solely through composition during inference*, and also enjoys painless implementation as it combines different pre-trained vector fields through an automated re-weighting scheme. Notably, we show that SuperDiff is efficient during inference time, and mimics traditional composition operators such as the logical $\texttt{OR}$ and the logical $\texttt{AND}$. We empirically demonstrate the utility of using SuperDiff for generating more diverse images on CIFAR-10, more faithful prompt conditioned image editing using Stable Diffusion, and improved unconditional *de novo* structure design of proteins.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors propose the method to combine the multiple pre-trained diffusion models at the inference time without retraining the models. They come up with the theoretical principles using the continuity equation to show how diffusion models can be viewed in the superposition of elementary vector fields. Here, they implement two algorithms to combine pre-trained diffusion models. One is a mixture of densities (sampling from one model OR another), and the other is equal densities(samples that are likely to belong to one model AND another). They also overcome the challenges with existing diffusion models, such as (1. Differences of Marginal super-positional vector field between different models) and (2. Divergence operation’s time complexity) by introducing their density estimator. They apply their approach in various ways, such as combining models trained on disjoint datasets, concept interpolation in image generation, and improving the structure of protein design.

### Strengths
1. The paper is well-written and easy to understand. There are almost no grammatical errors. By developing the idea of superposition and using theoretical principles, the authors prove the idea's potential and present a reasonable result.
2. They apply their work to two individual tasks, which could be divisive among readers, but I found it interesting.
3. Also, it is interesting that the authors discover their model follows traditional operators such as logical OR and logical AND, making it intuitive. Similarly, the background of explaining how the superposition emerged from the diffusion models by using the vector fields and propositions is interesting.
4. They use nine propositions, two theorems, and one lemma to support their idea, which helps readers understand why their algorithms work.

### Weaknesses
**(Main) Qualitative Results and the Quantitative Results with figures**
1. Figure 1 is weak to verify the novelty of the model. I also think the generated images in the appendix, as well as the qualitative results, are mediocre. The visual quality of the generated images lacks sharpness and detail, making it difficult to assess the true capabilities of the proposed method. The concept combinations often appear blurry or distorted, failing to convincingly demonstrate the superposition of features. This is especially concerning given the claim of combining pre-trained models without retraining.
2. The author only uses the AND operation (sampling equal densities) for qualitative results, and OR operation for the quantitative results. I believe that including the results for the OR operation in qualitative results and the AND operation in quantitative results would strengthen the paper. This would provide a more comprehensive view of the statement on line 104 on page 2: "improvements in designability and novelty generation". The absence of a direct comparison between the visual outputs of both operations makes it difficult to validate the claims of both novelty and designability improvements. The lack of visual examples for the OR operation leaves a gap in understanding its practical implications for image generation.
3. Figure 2 does not show how the generated images are actually arranged. It is necessary to verify if the same results occur when directly arranging the generated images with the trained datasets. The figure lacks clarity in how the generated samples are spatially organized, making it hard to understand if the method truly captures the underlying data distribution. It is crucial to show if the generated samples maintain the same spatial relationship as the original training data, which is not evident from the current figure.

**Evaluation metrics and ablation study**
1. The comparative group for the paper's qualitative results is insufficient. Comparisons with other recent models that produce dual images, such as factorization diffusion or visual anagram (Geng et al.,2024), could be added. Since it is clear that the latent diffusion result for just adding the prompt 'that looks like' would indeed be worse than the proposed method. The absence of comparisons with state-of-the-art methods limits the assessment of the proposed method's novelty and performance. A direct comparison with models that explicitly address dual image generation is necessary to establish the superiority of the proposed approach.
2. Similarly, in the process of making baselines for concept interpolation, I wonder if the value of the ablation study would have increased if the direction of A->B and B->A was changed and the comparison group was chosen by using the better result. The current ablation study lacks a systematic exploration of the interpolation direction, which might lead to biased results. A more comprehensive ablation study should consider both A->B and B->A directions and select the better result for comparison to ensure the robustness of the findings.
3. The execution times for the experiments were not provided. The authors claim to have solved the computational expense issue, but no results support this claim. The lack of computational cost analysis undermines the claim of improved efficiency. Providing the execution times for the proposed method and comparing them with baseline methods is crucial to validate the computational benefits.

**Clarity of the paper**
1. Proposition 8 appears to be quite important but confusing because it was cut off the page. Listing the individual terms of $Aκ = b + o(Δt)$ on the same page would improve comprehension. The presentation of Proposition 8 is unclear due to the page break, making it difficult to grasp the full context and implications of the equation. A complete presentation of the equation on a single page is essential for better understanding.
2. The related work section comes out almost at the end of page 10, and I think this part should come out more front. It comes out so out of the blue that it somewhat interferes with understanding. The late introduction of the related work section disrupts the logical flow of the paper and makes it harder to place the proposed method in the context of existing research. Moving the related work section to an earlier position would improve the overall coherence of the paper.
3. The protein generation part is not clearly introduced. The authors compare Designability, Novelty, and Diversity, and there is no separate explanation of how this part is meaningful in protein generation. I didn't feel that logic was connected smoothly. The lack of explanation of the metrics used for protein generation makes it difficult to understand the significance of the results. A clear explanation of how designability, novelty, and diversity relate to protein generation is necessary to establish the relevance of the findings.

### Questions
**Major Questions**
1. I am curious why text-based evaluation metrics such as Clip Score were not used. It seems like an obvious choice to do.
2. In section 2.1, how were the mixing coefficients $wj$ actually set? Is the model capable of adjusting the weights for mixing? I am also curious about how $N$ for the individual forward process was actually set.
3. The method overview on page 5 mentions that pre-trained diffusion models can be used, but I am curious if the only one actually used is CIFAR-10, as shown in Table 1. (The experiment by providing the models with CIFAR-10 with two sets of labels divided into five and five) I think if the authors provide the results using the output of various datasets, the paper will be stronger.

**Minor Questions**
1. I think there should be punctuation after *"...a superposition of elementary vector fields"* on page 3, lines 140 and 141.
2. I think the introduction of the abstract is too long. This could be reduced since the intro occupies 1/3 of the entire amount.
3. It would have been interesting if there was a comparison according to the distance of the disjoint set.

### Soundness
2

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
3

### Summary
This paper proposes a novel algorithm for combining multiple pre-trained diffusion models at inference time, by the principle of superposition of vector fields. The method demonstrates more diverse generation results, better prompt following on image data, and improved structure design of proteins as well.

### Strengths
* The theoretical framework is solid.
* The method is well-motivated and supported by the theory.
* The method is training-free, and could be applied to diffusion models with different architectures.
* The results of protein generation outperform other baselines.

### Weaknesses
 * The practical implications of AND, and OR operators are not explained clearly in both image and protein generation settings. What effect will the OR operator create on images, compared to the AND operator? Specifically, it's unclear how the OR operator's mixture of densities translates to concrete visual differences compared to the AND operator's interpolation of concepts. The paper needs to clarify if the OR operator is simply selecting between concepts or creating a more complex combination, and how this differs from a simple averaging of outputs.
* Lacks quantitative results on SD. Could have used metrics such as TIFA Score [1]  and Image Reward [2]. I wonder if there is any reason that no such metric was used. The absence of these metrics makes it difficult to assess the quality and faithfulness of the generated images, especially when comparing the proposed method against existing techniques. The paper should also clarify if the chosen metrics are appropriate for evaluating the specific type of image generation performed by the proposed method.
* Lacks comparison against other relevant methods [3-6]. In particular, [3,4,6] are all inference-time methods that sample from some sort of mixture of scores and demonstrate multiple practical uses, such as composing objects, styles, scenes, or improving text-image alignment. Need more discussions on the capabilities of the proposed method versus others: besides the different theoretical perspectives, how SUPERDIFF performs differently, the strengths and weaknesses of SUPERDIFF than the other methods. If experiments are not possible, please include a more detailed discussion. The comparison could help readers understand the proposed method in a broader context. The paper should clarify the specific advantages and disadvantages of the proposed method compared to these existing methods, especially in terms of computational cost, generation quality, and the ability to handle complex prompts.

### Questions
* Why are there no quantitative results on SD, and detailed discussion of other very relevant methods as referenced earlier?
* FID statistics on CIFAR-10 are computed on the whole dataset. Is it fair to evaluate models trained on a partial dataset using such statistics, especially when the two partitions are generated by splitting the classes?
* What are the practical implications of the OR operator, especially in the field of image generation?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
10

### Rating Number
10

### Confidence
5

### Summary
This paper introduces a novel, principled, and efficient way to combine diffusion models trained on different datasets (or conditioned on different prompts) to generate images from the mixture and the "intersection" of the corresponding distributions. It is based on a clever way to evaluate the densities $\log p^i_t(x_t)$ of the current iterate $x_t$ under each (noisy) distribution $q^i_t$ during synthesis.

### Strengths
The main strength of the paper is the important observation that the probability density function of generated images can be efficiently evaluated without the need for computing the divergence of the score. It is leveraged to sample from mixtures of densities, where the weights can be defined implicitly and adaptively (in the case of the logical AND operator as defined here). The experimental results convincingly demonstrate the effectiveness of the resulting approach.

### Weaknesses
In my opinion, the main weakness of the paper is in the clarity of the presentation of the central theoretical result (culminating in Proposition 7) and the motivation for the approach. I believe it can be significantly improved, which could enhance the impact of the paper.
- I found section 2.1 to be unnecessary complicated and rather irrelevant for the rest of the exposition. To my understanding, the main ideas are (1) that SDEs define linear equations on the densities, so that a mixture of clean distributions $\sum w_i p^i$ leads to a mixture of noisy distributions $\sum w_i p_t^i$ and (2) the relationship $\nabla \log (\sum w_i p^i_t) = \sum w_i p^i_t \nabla \log p^i_t / \sum w_i p^i_t$. These motivate the need for evaluating $p^i_t$ to combine scores in the correct way to sample from mixtures.
- The equations are obscured by the use of general schedules with arbitrary $\alpha_t$ and $\sigma^2_t$. I encourage the authors to state the results in the main text with e.g. $\alpha_t = 1$ and $\sigma_2^t$ (known as the variance exploding SDE) to simplify the exposition and relegate the general case to the appendix. The use of general schedules makes it difficult to grasp the core mechanics of the method, and obscures the connection to simpler, more intuitive formulations.
- Some results are also less intuitive (in my opinion) due to the choice to work in discrete time. For example, Proposition 6 and Theorem 1 are nothing but approximating the kernels $k_{\Delta t}$ and $r_{\Delta t}$ with Euler-Maruyama discretizations of the corresponding forward or backward SDEs (and analyzing the discretization error in Theorem 2). Similarly, Proposition 7 can be obtained in continuous time first (and then discretized) by applying Itô's formula to $\log q_t(x_t)$ where $x_t$ is a solution of the backward SDE (and using the fact that $q_t$ solves a Fokker-Planck equation). As an example, in the variance-exploding case, one obtains that $\mathrm{d} \log q_t(x_t) = \frac{\mathrm{d}t}2 ||\nabla \log q_t(x_t)||^2 + \langle \mathrm{d}x_t, \nabla \log q_t(x_t)\rangle$, which is the $\Delta t \to 0$ limit of Proposition 7 with $\alpha_t = 1$ and $\sigma^2_t = t$. I believe this result to be of independent interest, and would thus benefit from being highlighted and stated as simply as possible.

Another issue I have is regarding the logical OR and AND operators as defined in this paper.
- The logical OR operator corresponds to a fixed-weight mixture of distributions, and it is thus trivial to sample from. One can simply select one diffusion model with probability corresponding to the mixture weight, and then use exclusively the score of the chosen diffusion model during generation. Using SuperDiff should be equivalent to this algorithm. So either the improved results in section 4 can also be achieved with this simple baseline, in which case the theoretical results are not needed, or the baseline underperforms, in which case the improvements come from unknown implementation choices which are completely orthogonal from the theoretical analysis. In both cases, this raises questions.
- The real strength of the approach, I think, is when the mixture weights are adaptive (i.e., they are allowed to depend on the current iterate $x_t$). In that case, however, it is not clear what density we are ultimately sampling from. If I understand correctly, here the logical AND operator is defined implicitly, and produces samples $x$ such that $q^1(x) = q^2(x)$. A perhaps more usual definition is that one would aim to sample from the normalized product $q^1(x)q^2(x)/Z$ (or geometric mean $\sqrt{q^1(x)q^2(x)}/Z$), but this seems difficult to achieve with the formalism of this paper. It could be beneficial to include a short discussion of this matter in the paper.

Finally, I could not see where the parameters $\omega$ and $T$ in Table 2 were explained.

### Questions
- How do the authors explain the source of their numerical improvements using SuperDiff OR?
- What density is being sampled from when using SuperDiff AND?

### Soundness
3

### Presentation
2

### Contribution
4
