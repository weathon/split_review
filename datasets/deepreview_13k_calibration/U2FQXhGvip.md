# Improving Distribution Matching via Score-Based Priors and Structural Regularization

- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 3, 3, 6, 5

## Abstract
Distribution matching (DM) can be applied to multiple tasks including fair classification, domain adaptation and domain translation.
However, traditional variational DM methods such as VAE-based methods unnecessarily bias the latent distributions towards simple priors or fail to preserve semantic structure leading to suboptimal latent representations.
To address these limitations, we propose novel VAE-based DM approach which incorporates a flexible score-based prior and a semantic structure preserving regularization.
For score-based priors, the key challenge is that computing the likelihood is expensive.
Yet, our key insight is that computing the likelihood is unnecessary for updating the encoder and thus we prove that the necessary gradients can be computed using only one score function evaluation.
Additionally, we adapted the structure preserving regularization inspired by the Gromov-Wasserstein distance, which explicitly encourages the retention of geometric structure in the latent space, even when the latent space has fewer dimensions than the observed space. 
Our framework further allows the integration of semantically meaningful structure from pretrained or foundation models into the latent space, ensuring that the representations preserve semantic structure that is informative and relevant to downstream tasks.
We empirically demonstrate that our DM approach leads to better latent representations compared to similar methods for fair classification, domain adaptation, and domain translation tasks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The following paper proposes score-based priors for VAEs in combination with Gromov-Wasserstein distance regularization for the domain adaptation problem.

### Strengths
The combination of score-based priors for VAEs with Gromov-Wasserstein distance seems to be a novel approach.

### Weaknesses
The contribution of the paper is unclear, making it difficult to follow. The authors frequently shift between topics in introduction section. Initially stating that they are addressing the distribution matching problem. However, they then build their motivation around fairness, robustness, causality, and explainability concepts, before ultimately changing the narrative, and  focus on the domain adaptation problem.

In addition, the evaluation provided is very poor, the central claims of the paper about "flexibility" are not supported. The evaluation is limited to domain adaptation, and the datasets used for comparison are simple. In addition, the paper proposes the use of structural regularization based on the Gromov-Wasserstein (GW) distance, but fails to provide any evaluation showing that this structural regularization is beneficial. Furthermore, the paper does not consider any datasets where the importance of structural regularization would be relevant.

Finally, the presentation can be improved. More examples and comparison on the face translation task, improved fonts on MNIST figure, comparison on at least, classic domain adaptation tasks as MNIST->SVHN, MNITS-MNIST-M. GW abbreviation is defined a few times in each section.

### Questions
1) Why are "flexible" representations important for trustworthiness, and what is your contribution? How do you demonstrate this flexibility? 

2) Why are score-based priors useful for domain adaptation? 

3) In the introduction, the authors criticize optimal transport methods with Euclidean cost functions. But the comparison with these methods in the domain adaptation task is missing, see papers (1,2,3).

4) Experimental settings in section 5.1 are unclear, why did the authors consider this dataset and not the more popular Celeb-A benchmark? 

5) Why is it important to use structural regularization for the MNIST to USPS dataset? it would be more valuable to consider a typical dataset where Gromov-Wassesrstein regularization is applied. It is important to show how the method performs compared to other domain adaptation methods based on GW (4,5).

**References:**
1) https://openaccess.thecvf.com/content_CVPR_2020/papers/Li_Enhanced_Transport_Distance_for_Unsupervised_Domain_Adaptation_CVPR_2020_paper.pdf
2) http://proceedings.mlr.press/v139/fatras21a/fatras21a.pdf
3) https://proceedings.neurips.cc/paper_files/paper/2020/file/9719a00ed0c5709d80dfef33795dcef3-Paper.pdf
4) https://arxiv.org/pdf/2205.10738
5) https://arxiv.org/pdf/2303.05978

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a distribution matching approach using score-based priors and leverages a distance-preserving distortion loss inspired by Gromov-Wasserstein. The authors present a Score Function Substitution (SFS) trick for efficient training of their score-based prior and evaluate their method on domain adaptation, fairness, and domain translation tasks.

While the paper presents an interesting approach to distribution matching with some promising empirical results, the lack of proper acknowledgment of prior work on Gromov-Wasserstein losses in autoencoders significantly diminishes the claimed novelty. The experimental evaluation would benefit from clearer ablation studies, additional quantitative results for domain translation, and comparisons to relevant competing methods with flexible priors. These additions would help better position the work's contributions relative to the existing literature. Thus, currently the paper does not reach the bar for acceptance.

### Strengths
- Novel technical contribution with the Score Function Substitution (SFS) trick
- Empirical evaluation across multiple tasks
- Demonstrates improvements over standard Gaussian prior baselines

### Weaknesses
 - Missing discussion & contextualization of related work:
	- Employing a Gromov-Wasserstein-inspired loss in an Autoencoder setting has previously been proposed in [1,2,3]. The authors propose to use a distance-preserving distortion loss. This has first been proposed in [1], and then extended in [2,3]. Thus, the method and contribution part of the paper needs to be significantly adapted as the proposed term is not a novel loss but an incorporation of previous existing methods.
- Experimental section:
	- It is unclear whether, in Sections 5.1 and 5.2, the structure-preserving loss was used for all experiments.
	- Comparison to other competing methods. The authors compare their score-based prior to a Gaussian prior. However, competing methods have also proposed to learn a flexible prior, e.g. [1,4,5]. A comparison to other methods leveraging a trainable prior would significantly strengthen the experimental section of the paper.
	- For section 5.4, no quantitative results are reported. Adding quantitative results would validate this section of the experiments as sole qualitative results are hard to judge.

- Minor:
	- Notation: After Eq. 1 it is unclear what d is and what the exact problem setup is here. This is only explained after Eq. 9. I think it would be beneficial to move this to the beginning of Section 2, including a more detailed introduction of the problem statement.
	- State-of-the-art Unpaired Domain Translation methods are not discussed in the related work section [6,7,8,9].

### Questions
- In Sections 5.1 and 5.2, is the structure-preserving loss used for all experiments? What would be the effect of removing/applying it?
- How important is the structure-preserving loss for the domain translation experiments in Section 5.4?
- How does the work compare to existing trainable prior approaches?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper proposes a VAE-based distribution matching approach using a score-based prior. The authors introduce the Score Function Substitution (SFS) trick that facilitates efficient VAE training.
Additionally, they combine the VAE objective with a GW regularizer to ensure that the latent space retains the structural/semantic properties of the data space. The authors validate their approach across several applications, including fair classification, domain adaptation and domain translation.

### Strengths
**S1 |** Score Function Substitution (SFS) is a simple and interesting modification of the LSGM approach.

**S2 |** The experiments in Sections 5.1 and 5.2 support the proposed method.

### Weaknesses
 **W1 |** It would be beneficial to provide more clarification and motivation regarding the VAUB formulation and the associated challenges. I can see that VAUB is simply a domain/class-conditioned VAE with a shared learnable prior. If so, proposing score-based priors for this formulation is a marginal contribution compared to LSGM[1].

**W2 |** The Score Function Substitution (SFS) appears very similar, if not identical, to score distillation sampling (SDS) [2]. This idea has been widely explored for text-to-3D generation [2,3] and diffusion distillation [4,5,6,7]. The proposed method can be interpreted as a direct SDS application to LSGM[1]. It is important to discuss these works and their connection to the proposed method thoroughly. 

**W3 |** The use of the GW metric for VAE does not seem novel either [9,10]. The connection to this line of work also needs to be carefully discussed. For example, GWAE[9] shares similar ideas and motivation. 

**W4 |** The experimental setups lack important details, making it difficult to understand how the proposed method is exactly applied to various tasks. For example, what are the model inputs and targets for the source and target domains across all tasks?

**W5 |** I do not think that domain adaptation and translation between USPS and MNIST are appropriate tasks, as the domains appear too similar. Also, why were CLIP embeddings chosen for MNIST? Could the authors consider exploring other tasks for this problem, such as those suggested in [8]?

**W6 |** I can hardly agree that the domain translation results are informative. While it is evident that the method preserves the original content better than VAUB, it struggles with effective translation in most cases.

**W7 |** If I understand correctly, the usefulness of the GW regularizer is demonstrated only for the domain adaptation task. Could the authors investigate the effect of this regularizer on other tasks when it is applicable? Could the authors provide insights into which cases the regularizer is more effective? 

**W8 |** Given that the SFS modification approximates the objective in LSGM [1], it would be interesting to compare these two approaches directly.

**Minor**

* $d$ is undefined in Section 2. 

### Questions
Please address the questions and concerns in Weaknesses.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This manuscript introduces a novel VAE structure that leverages score-based priors instead of the Gaussian ones, which might overcome some limitations of conventional VAEs by allowing the model to learn more complex patterns in the latent space without needing explicit likelihood calculations. Moreover, the authors incorporate a structure-preserving regularization based on the Gromov-Wasserstein distance, which maintains the geometric relationships among data. The authors demonstrate the effectiveness of the proposed methods on various tasks, including fair classification, domain adaptation, and domain translation. By combining theoretical insights with practical applications, this work could take a step forward in distribution matching.

######################################### Post Rebuttal ######################################### 

None author response found. I will keep my score.

######################################### Post Rebuttal #########################################

### Strengths
1. The manuscript is well-written and clearly motivated, with the step-by-step derivations and sufficient literature to understand each proposed component.

2. Using score-based priors instead of the Gaussian priors in variational inference methods like VAEs is interesting and promising, which might help the model identify more complex hidden patterns in the input data. Moreover, using the score function to evaluate the encoder gradients might associate how the model learns its parameters with changes in the data’s probability density. 

3. Using the Gromov-Wasserstein distance as the regularization term to make sure that the latent space maintains the semantic structure of the data is interesting.

### Weaknesses
1. Although using score-based priors is interesting, however, score-based priors are inherently more computationally intensive than simple Gaussian priors, potentially leading to longer training times. I would suggest an ablation study to compare the runtime complexity (e.g., training time per epoch, total training time until convergence, and inference time) of the proposed score-based priors with those of VAEs using the Gaussian priors. The evaluation metric could be the time in seconds, along with an indicator specifying the type of GPU platform used for these experiments.

2. From Equation (13) to Equation (14), it seems like noisy versions of the latent samples are introduced to develop a denoising score matching objective for the proposed method. If that is the case, based on my understanding, it seems the method still uses a Gaussian prior in variational inference but with more constrained regularization. I suggest the authors provide more details on how to implement Equation (14) for a specific task (e.g., domain adaptation or fair classification). It remains unclear how the score-based prior is used during the inference stage for downstream tasks, especially if the method relies on sampling from the learned latent space.

### Questions
1. Could the authors elaborate more on why other optimal transport methods can only compare points from spaces with the same number of dimensions?

2. Equation (14) shows the final derivation of the proposed method, which, to me, appears similar to denoising score matching in the latent space. Could the authors explain how the proposed method differs from denoising score matching?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper considered the distribution matching approach through the scoring matching framework. By overcoming the limitations on both adversarial training and variational inference, the proposed scoring matching method incorporated Gromow-Wasserstein (GW). Experiences on fairness, domain adaptation and domain translation have been done.

### Strengths
1. This paper naturally extended the previous work Gong (2024) by improving certain limitations in variational inference. 
2. The paper is seemingly technically sound. 
3. The experiments are conducted in diverse domains and applications, thereby a clear improvement.

### Weaknesses
Unfortunately, I think this paper clearly falls short for acceptance.

My most important concerns lies in a significant lack of **clear, concrete and convincing** supporting evidence within the paper. The overall feeling is full of self-claim but very limited justification and support. Most arguments are simply presented without clear and concrete support. The following are notable concerns.

- I could not understand which parts constitute the most significant contributions. If we check the claimed contribution in the paper.

> Introduction of Score-Based Priors for Flexible Representation: We propose score based priors, enhancing flexibility and preserving complex data structures without requiring sampling or likelihood estimation.

The paper claimed many benefits of proposed methods. However, this reviewer did not understand why they are beneficial or what’s the point in the context of distribution matching. For example, *flexibility and preserving complex data structures without requiring sampling or likelihood estimation*. I could not understand why likelihood estimation is a bad thing. In complex data structures, how complex is it? From the paper, the actual contribution in data structure is about the cluster assumption. Does cluster information is equivalent to complex data structure? I believe there is a significant gap here. How to justify the flexibility, can you give concrete evidence such as improving the efficiency?

From the analysis and paper, I did not clearly identify the concrete and convincing evidences for the claim.

> Structure-Preserving Constraints Inspired by Gromov-Wasserstein Distance: We introduce a Gromov-Wasserstein-based constraint to preserve geometric relationships, ensuring robust, task-relevant latent representations across transformations.

Again there are several questions regarding this claim. How GW distance explicitly preserves the geometric relationships, why not other relevant techniques such as hierarchical generative models could not? There is a lack of clear rationale and throughout comparison without others.

This contribution is also claimed by robust, task-relevant latent representations across transformations. However, this reviewer could find very limited **concrete** supporting evidence about robust, task-relevant latent representations.

> Empirical Validation: Our experiments demonstrate improved downstream task performance in fairness learning, domain adaptation, and domain translation using score-based priors and structural preservation.

I found this to be the most concerning point. Indeed, what does it mean by improved downstream tasks in Digit dataset or tabular Adult dataset? Do we need downstream tasks in these datasets? Why do we need to learn a representation in these datasets? The representation learning, back to the original sense, aims to learn meaningful information from very high-dimensional and complex datasets. I could not understand how the proposed experiments are associated with real-world representation learning in this sense.

*Using score-based priors and structural preservation.* Again, I could not think of this as an advantage, this paper simply compared some old baselines and the most relevant paper (Gong, 24). But the fact is that there is a rich literature in generative models that incorporate score-based or structural level information. There is a clear lack of comparison.


- There are many awkward claims within the paper. I will list several in the introduction.

> (List 33-35) Unfortunately, simply collecting more data or building bigger models is unlikely to solve these problems, as they require imposing additional constraints on the learning process.

What is the supporting evidence by saying *more data or bigger models is unlikely to ….*. There are many papers that indeed support more diverse datasets or bigger models could solve this issue, such as scaling law papers. This essentially reveals the larger, more data is indeed better.

*they require imposing additional constraints on the learning process*, again what is the supporting evidence to say additional constraints? Can you provide concrete evidence by justifying it?


> (Line 43) One of the most used distribution matching methods is adversarial models,

This claim is not necessarily true. Indeed, most generative models can be broadly viewed as distribution matching between data distribution and generative distribution such as VAE (though KL divergence), score matching (via Fisher divergence).
> (Line 51-53) While this simplifies the optimization process and
ensures tractability during generative tasks, it biases the latent space, often leading to a loss of critical structure in the data during transformation.

This is not always true. For example, the high-dimensional gaussian distribution is indeed expressive. Considering the experimental datasets such as Adult and Digits, I think this is sufficient.


> (Line 65) For instance, domain adaptation tasks require not only distribution alignment but also the preservation of clusters or other semantic features.

My question is that if we have a perfect distribution alignment, that should imply the cluster or other semantic feature will also be well-aligned, right?

> (Line 75) Unlike Gaussian priors, score-based models do not bias the latent representations towards a fixed distribution, enabling
the model to capture richer and more nuanced patterns.

General form is richer but also enhances the risk of overfitting, right?

> (Line 85) Our framework can also integrates semantic information from pretrained models, such as CLIP(Radford et al., 2021),

Unfortunately there is no concrete supporting evidence for this.


> (Line 11-12) Distribution matching (DM) can be applied to multiple tasks including fair classification,

Can you differentiate fair classification and fair representation learning **in your paper**? What are the key differences in your context? What are the exact downstreaming applications in your paper if we consider fair representation learning?

### Questions
See the weakness section. Overall, In the rebuttal or future revision I would strongly suggest authors 

- For each statement or argument, please provide concrete evidence such as citation from well-established literature, your own experimental results or throughout analysis. 
- Precisely and accurately express all the notations and terminologies.

### Soundness
3

### Presentation
1

### Contribution
1
