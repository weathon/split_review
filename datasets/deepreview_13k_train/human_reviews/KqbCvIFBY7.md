# Particle Guidance: non-I.I.D. Diverse Sampling with Diffusion Models

- Decision: Accept
- Scores: 6, 8, 5, 5

## Abstract
In light of the widespread success of generative models, a significant amount of research has gone into speeding up their sampling time. However, generative models are often sampled multiple times to obtain a diverse set incurring a cost that is orthogonal to sampling time. We tackle the question of how to improve diversity and sample efficiency by moving beyond the common assumption of independent samples. We propose \textit{particle guidance}, an extension of diffusion-based generative sampling where a joint-particle time-evolving potential enforces diversity. We analyze theoretically the joint distribution that particle guidance generates, \rebut{how to learn a potential that achieves optimal diversity,} and the connections with methods in other disciplines. Empirically, we test the framework both in the setting of conditional image generation, where we are able to increase diversity without affecting quality, and molecular conformer generation, where we reduce the state-of-the-art median error by 13\% on average.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The aim of the methodology developed in this paper is to promote sample diversity when sampling I.I.D. from a diffusion model. Indeed, when drawing a $M$ i.i.d. samples from a multimodal density with $M$ modes, it is unlikely to get a sample on each one of the modes, even when all the modes have the same weight. To promote sample diversity when sampling from a diffusion model, the authors propose to modify the backward process by adding a repulsion term ensuring that samples drawn at each step of the diffusion process are as dissimilar as possible.

### Strengths
1- The problem that this paper tries to solve is quite original.  
2- The paper is well written and the idea in itself is interesting. It is also quite nice that authors managed to give an explicit formula for the the joint density targeted by their modified backward process. The connection with other works that make use of a repulsion term is also a nice addition.  
3- The experiments are well explained and sound.

### Weaknesses
1- While Theorem 1 is interesting, the expression derived for the joint density is not very interpretable and so one does not get a good grasp of what the modified backward process is targeting. It is quite unsatisying that the authors did not add a toy experiment where they explicitely compare the law of the samples obtained from particle guidance with the initial law that is targeted. I believe that the authors should consider an experiment in which the modes do not have the same weights and then show what is actually the law that they are sampling from. I would expect this law to not have the correct statistical weights, which could be quite unconvenient. 

2- Failure cases of the proposed method are not discussed. Furthermore, as far as I can tell there is no real discussion on the choice of the potential and its parameters (besides in the toy example). How did the authors choose the potential in the other examples? Can a badly chosen potential perform worse than the original diffusion model?

### Questions
Why did the authors choose such a small variance for the Gaussian mixture experiment?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a method to sample from a joint distribution of a diffusion model combined with some potential function, with a specific focus on potentials that encourage diversity. This is done by attaching an additional "guidance" term to the diffusion SDE that moves the generation towards high-potential region, which shares the similar idea of prior works on guidance, e.g. classifier guidance. The paper analyzes the theoretical properties of the implied joint distribution, and connections to related works. Empirically, the paper demonstrates the superiority of the proposed method in Gaussian synthetic example, text-to-image generation and molecular conformation generation. In these examples, the proposed method has scored better in diversity and other downstream metrics compared to the standard IID samping.

### Strengths
- The paper is very well-written and easy to follow.

- The motivation of this paper is very clear and seems to be important. 

- The proposed method presents simple and effective way to overcome the limitation of IID sampling, which is the inefficiency in exploring all possible modes. 

- The empirical comparison is comprehensive and convincing.

### Weaknesses
 - While the angle of this paper (to promote efficiency and diversity) is novel, I found the methodology itself, namely equation 1, does not have too much _technical_ novelty, and seems to be following the line of "guidance" works, e.g. classifier guidance, reconstruction guidance [1], DPS[2], Pseudo-inverse diffusion sampler [3], universal guidance [4], etc. The core idea of adding a gradient term to the diffusion SDE to steer the sampling process is well-established, and the specific form used here, while effective, does not introduce a significant departure from existing techniques. The novelty is primarily in the application of this guidance to a set of particles rather than a single sample, and the analysis of the resulting joint distribution, but the underlying mechanism is not fundamentally new.

- One potential weakness is the memory constraint invoked by simulating multiple particles (and getting their gradients) at the same time. The authors should provide a more detailed analysis of the computational cost, especially for high-dimensional data and large numbers of particles. The memory requirements for storing intermediate states and gradients for multiple particles could become prohibitive, limiting the scalability of the method. Additionally, the communication overhead between GPUs or other processing units might become a bottleneck.

- Another missing discussion is on the choice of $n$, the number of particles used in practice. How does one determine $N$, and what is its implication on the joint distribution? For example, I hypothesize that for $n_1>n_2$, marginalizing out the last $n1-n2$ particles in the joint distribution of $n1$ does not recover the joint distribution of $n_2$. And when $n$ is much larger than the number of modes in the diffusion model that we are interested in, what would happen by running the proposed method (especially when using a large guidance weight). Would that result in generating particles that have very low density under the diffusion model? The authors should explore the sensitivity of the method to the number of particles used, and provide some guidance on how to choose this parameter in practice.

- This point is regarding clarify. Similar to the above "marginalization" argument, I think there is a missing discussion on whether such joint sampling of $x_1, \cdots, x_n$ would recover marginally exact samples from a diffusion model, and I assume not (correct me if I'm wrong). But somehow I found the paper can be misleading in suggesting "yes", e.g. on page 3 "Intuitively, this will push our different samples to be dissimilar from one another while at the same time matching our distribution, improving sample efficiency." The paper needs to explicitly acknowledge that the marginal distribution of individual samples is altered by the particle guidance, and that the method does not produce samples that are marginally distributed according to the original diffusion model. This distinction is crucial for understanding the limitations of the approach.

### Questions
1. In abstract, can you explain which part of the paper discusses "its implications on the choice of potential"? 

2. The "finite-sampling" property of diffusion models does not seem to be accurate. Apparently, sampling from the diffusion SDE (in a discrete manner, and without running infinite Langevin steps) will also accumulate error. It seems like the authors were referring this property to getting to every "mode" of the distribution in finite steps. If this is the case, I wonder the authors can be more clear about this point, and provide evidence or reference to support this claim?

3. Can you further explain why "Hence the density p0ˆ can be understood as a reweighting of the random variable Z" (the sentence under equation 5 on page 4)? Furthermore, can you provide intuition on what the random variable $Z$ encode?

4. Maybe I missed this part, but for all experiments, what are the $n$, number of particles you used, and how do you determine them?

5. In the preamble part of section 5, the reference to the text-to-image experiment is missing.

6. In Figure 3, how is "varying guidance scale from 6 to 10" reflected/used in the figure and this experiment?

7. Table 1 seems to miss the reference and descriptions of competing methods. Furthermore, I wonder why the authors didn't experiment the proposed method on geodiff model. Is that possible? 

8. Section 6 seems really interesting! I wonder if there is any practical challenge in instantiating that paradigm?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The work investigates how to increase the diversity of one batch of samples for diffusion models. Specifically, the authors introduce a method named particle guidance, which is based on the gradient of a crafted time-varying potential field. The authors conduct various experiments to demonstrate the effectiveness of the method and provide an interesting analysis of the proposed method. However, some statements need to be clarified and more details about the experiments are needed.

### Strengths
- The topic, increasing diversity of generated samples, is important and crucial.
- The theoretical analysis conducted in the main paper and appendix are non-trivial and interesting.
- Experiments presented in the paper look good and show visual improvements.

### Weaknesses
Will the marginal distribution of Eq-1 be the same as that of the original diffusion model? It appears that the proposed method alters the marginal distribution. I am concerned that this shift in distribution may not be desirable in many applications. Specifically, if the goal is to generate samples that accurately reflect the underlying data distribution, altering the marginal could lead to a biased representation. This is a significant concern, especially if the method is intended for use in downstream tasks that rely on the fidelity of the generated samples to the true distribution. 

It seems that most experiments conducted in this work focus on small batch sizes. I am interested in the authors' discussion regarding the scalability and effectiveness of the proposed method for large batch size. The computational cost of calculating the potential field, especially with pairwise kernels, could become prohibitive as batch sizes increase. Furthermore, the memory requirements for storing and processing the gradients for a large number of samples could also limit the practical applicability of the method. It's unclear how the method would perform with batch sizes of 64, 128, or more, which are commonly used in large-scale diffusion model training and inference.

There doesn't seem to be a principled approach to designing the proposed potential field besides the method present in Sec 6, which demands non-trivial training. The lack of a clear strategy for designing the potential field, outside of learning it, is a limitation. Without a more systematic way to define these potentials, it is difficult to understand how the choice of potential affects the diversity and quality of the generated samples. This makes the method less generalizable and harder to apply to new problem settings or datasets. 

The illustrated plots in Figure 1 are a bit misleading to me. Why are the initial points concentrated in one mode? In a high-dimensional setting, the chance of sampling close-by Gaussian points is low. The figure gives the impression that the initial samples are tightly clustered in a single mode, which is not typical for high-dimensional Gaussian noise. This representation could lead to an oversimplified understanding of the method's behavior. A more realistic depiction of the initial sample distribution would be beneficial.

Why were different guidance weights chosen for the IID and particle guidance experiments?

For fair evaluation purposes, could the authors post un-cherry-picked images on an anonymous website, for example, the first 50 text prompts of MS COCO or PartiPrompts? This should be done with the same hyper-parameters and random seed.

### Questions
See above

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes the use of particle guidance for sampling in diffusion-based models, emphasizing that particle guidance increases diversity without reducing quality.

### Strengths
Diversity is a crucial property in generative modeling and sampling. Whether for multi-modal sampling or the regeneration of real data, we aim to cover each mode. The problem studied in this paper is significant.

The paper's approach is succinct and clear, making it easy to follow.

### Weaknesses
Despite the author's belief that diffusion models may suffer from mode collapse, previous experience suggests that mode collapse in diffusion models is not particularly severe [1]. If mode collapse is not a leading factor in most cases, it might affect the significance of this study. When the number of modes far exceeds the number of samples, it's evident that iid sampling and sampling with repulsion are similar, which seems to be the case for most data. For instance, in Figure 4 (a), diversity does not appear to be a severe issue. The main problem in Figure 4 (d) seems to be overfitting to the training data (an artificial setting). I think the authors should emphasize scenarios where the number of samples is close to the number of modes to highlight the setting's effectiveness. Molecular conformer might be an example, but since I am not an expert in that area, the authors could further explain.

The paper's theoretical foundation is weak and does not directly explain why particle guidance can increase diversity.

### Questions
The authors are encouraged to further elucidate in what practical situations iid might fail (e.g., when the number of modes is close to the number of samples).

Has the paper investigated the impact of the number of particles on the final generation outcome?

Is there theoretical proof that particle guidance is better to some extent (even though this aligns with intuition)?

The paper uses an ODE solver. Would there be any changes if an SDE solver is used?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
