# Fast training and sampling of Restricted Boltzmann Machines

- Decision: Accept
- Avg Score: 4.25
- Scores: 3, 6, 5, 3

## Abstract
Restricted Boltzmann Machines (RBMs) are effective tools for modeling complex systems and deriving insights from data. However, training these models with highly structured data presents significant challenges due to the slow mixing characteristics of Markov Chain Monte Carlo (MCMC) processes. In this study, we build upon recent theoretical advancements in RBM training, focusing on the gradual encoding of data patterns into singular vectors of the coupling matrix, to significantly reduce the computational cost of training (in very clustered datasets) and evaluating and sampling in RBMs in general.  The learning process is analogous to thermodynamic continuous phase transitions observed in ferromagnetic models, where new modes in the probability measure emerge in a continuous manner. Such continuous transitions are associated with the critical slowdown effect, which adversely affects the accuracy of gradient estimates, particularly during the initial stages of training with clustered data. To mitigate this issue, we propose a pre-training phase that encodes the principal components into a low-rank RBM through a convex optimization process. This approach facilitates efficient static Monte Carlo sampling and accurate computation of the partition function. Furthermore, we exploit the continuous and smooth nature of the parameter annealing trajectory to achieve reliable and computationally efficient log-likelihood estimations, enabling online assessment during the training process, and proposing a novel sampling strategy termed parallel trajectory tempering that outperforms previously optimized MCMC methods.
Our results demonstrate that this innovative training strategy enables RBMs to effectively address highly structured datasets that conventional methods struggle with. Additionally, we provide evidence that our log-likelihood estimation is more accurate than traditional, more computationally intensive approaches in controlled scenarios. Moreover, the parallel trajectory tempering algorithm significantly accelerates MCMC processes compared to existing and conventional methods.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper discusses approximations to train a restricted Boltzmann machine (RBM). The first is to pre-train the RBM by fitting a constrained (low-rank) form of the RBM to the low-dimensional PCA space of the data. This can help with finding a good initial solution. After this various MCMC approaches are considered to continue training.

### Strengths
RBMs are an important model and finding appropriate ways to train them is a topic of significant interest. The paper highlights the phenomenon of critical slowing down and how pre-training the model with a low-rank approximation of the parameter matrix can help the model overcome some of the slowing down effects.

### Weaknesses
The paper suffers from a lack of clarity of presentation and lack of clarity of novelty.

The paper mentions that the idea of a low-rank approach has already been used by others and it's unclear to me what novelty there is in any of the sampling approaches used after the pre-training phase.

In terms of presentation, there are notational inconsistencies and a general lack of clarity in terms of the main ideas. Fundamentally the approach of fitting a constrained model seems straightforward and indeed I believe there is a simple way to compute the projected distribution in the PCA space (using the Fourier integral representation of the Dirac delta function) which the authors do not discuss.

*** introduction

Whilst the RBM is well known, it would be helpful I feel for a reader to have the definition of the model earlier in the text. It currently isn't defined until near the end of page 4. Please introduce the RBM formally earlier in the text.

Notation: inconsistent use of $N_v$ and $N_{\text{v}}$ throughout, similarly for $N_h$.

Equation 1: it might be better to write W_{i\alpha}, rather than w_{i\alpha} since w is used later for the "singular values".

*** page 2

Figure 1 isn't very easy to parse. For example the panel on race is placed more in the Mickey column than the human genome column.

*** page 5

Please clarify the difference between "model averages" and "observable averages" and the difference between using N_s independent MCMC processes and R parallel chains.

Please clarify for the reader the meaning of <v_ih_a>_D

Section 4: It is not correct that it is possible to train "exactly" an RBM with a reduced number of modes. Approximations are required, as explained in the supplementary material.

Please state what the free parameters to learn are in equation 3. If u and \bar{u} are the singular directions, then the free parameters would be w_\alpha? 

In general I found the description of the low-rank approach unclear and this important section needs work to make it simpler and more clear to the reader.

For figure 14 it would be useful to show the distribution of the PCA projected data to see how well the RBM matches the projected data distribution.

It's unclear to me what contribution the authors are claiming to make. They state that the learning of the low rank parameterisation of W has been done before. Please clarify what the contributions of the paper are.


*** Section 5

I find it hard to follow why the authors are considering different sampling schemes and therefore what the aim of this section is. I presume this is considering alternative sampling approaches after the low-rank pre-training has been applied. However, I struggle to follow a clear recommendation or conclusion as to which method might be more suitable.

*** Section 6

In the conclusion the authors claim to have introduced a method that enables "precise computation of log-likelihood". I cannot see anything in the main text that relates to this. There is no experiment I can see that measures the quality of the log-likelihood approximation. Please give some evidence to support this assertion.


*** Supplementary material

The use of the term "mode" isn't very clear. The phrasing suggests that the first d modes of the maximum likelihood trained RBM should correspond to the d "modes" of the PCA solution. I'm not sure I know what this means. What are modes of a PCA solution?

The notation \hat{u} is confused with \bar{u}.

Why use $w$ here whereas $W$ is used in the main text?

The derivation is quite confusing. For example the dependence on \bar{u} in equation 7 disappears without explanation. Indeed \bar{u} seems to be never properly defined.

Please state clearly what are the parameters of the model that are being learned.

Section A.2. The claim as before of exact training is incorrectly made here.

The notation in equation 20 is confusing, such as w_{\alpha,a}=\sum_i w_{ia}u_{i\alpha} -- are arabic and latin indices meant to indicate referencing a different entity, even though both objects are labelled w?

In general I find the supplementary material confusing. I believe it is trying to fit an RBM projected to the d-dimensional subspace defined by PCA of the data to the empirical data distribution in that same subspace. However, approximations are clearly required in order to compute the projected RBM distribution. Given that, for a very low dimension d then one can easily discretise the model and carry out a simple maximum likelihood fit. If that is what is being done, it is not well explained and rather misleading (since this requires approximations itself).

An alternative (and standard) way to compute the marginal p(m) is to use the integral (Fourier) representation of the Dirac delta function. This means that the summation over v can be then carried out exactly, leaving only a d-dimensional integral to exactly compute p(m). This can also be carried out using discretisation for small d. The authors are (as I can understand) also using discretised integrals, so I'm unclear why they don't employ the standard Fourier Delta representation approach to compute p(m) -- this would seem to involve less approximations that the approach the authors consider.

### Questions
*** introduction

Whilst the RBM is well known, it would be helpful I feel for a reader to have the definition of the model earlier in the text. It currently isn't defined until near the end of page 4. Please introduce the RBM formally earlier in the text.

Notation: inconsistent use of $N_v$ and $N_{\text{v}}$ throughout, similarly for $N_h$.

Equation 1: it might be better to write W_{i\alpha}, rather than w_{i\alpha} since w is used later for the "singular values".

*** page 2

Figure 1 isn't very easy to parse. For example the panel on race is placed more in the Mickey column than the human genome column.

*** page 5

Please clarify the difference between "model averages" and "observable averages" and the difference between using N_s independent MCMC processes and R parallel chains.

Please clarify for the reader the meaning of <v_ih_a>_D

Section 4: It is not correct that it is possible to train "exactly" an RBM with a reduced number of modes. Approximations are required, as explained in the supplementary material.

Please state what the free parameters to learn are in equation 3. If u and \bar{u} are the singular directions, then the free parameters would be w_\alpha? 

In general I found the description of the low-rank approach unclear and this important section needs work to make it simpler and more clear to the reader.

For figure 14 it would be useful to show the distribution of the PCA projected data to see how well the RBM matches the projected data distribution.

It's unclear to me what contribution the authors are claiming to make. They state that the learning of the low rank parameterisation of W has been done before. Please clarify what the contributions of the paper are.


*** Section 5

I find it hard to follow why the authors are considering different sampling schemes and therefore what the aim of this section is. I presume this is considering alternative sampling approaches after the low-rank pre-training has been applied. However, I struggle to follow a clear recommendation or conclusion as to which method might be more suitable.

*** Section 6

In the conclusion the authors claim to have introduced a method that enables "precise computation of log-likelihood". I cannot see anything in the main text that relates to this. There is no experiment I can see that measures the quality of the log-likelihood approximation. Please give some evidence to support this assertion.


*** Supplementary material

The use of the term "mode" isn't very clear. The phrasing suggests that the first d modes of the maximum likelihood trained RBM should correspond to the d "modes" of the PCA solution. I'm not sure I know what this means. What are modes of a PCA solution?

The notation \hat{u} is confused with \bar{u}.

Why use $w$ here whereas $W$ is used in the main text?

The derivation is quite confusing. For example the dependence on \bar{u} in equation 7 disappears without explanation. Indeed \bar{u} seems to be never properly defined.

Please state clearly what are the parameters of the model that are being learned.

Section A.2. The claim as before of exact training is incorrectly made here.

The notation in equation 20 is confusing, such as w_{\alpha,a}=\sum_i w_{ia}u_{i\alpha} -- are arabic and latin indices meant to indicate referencing a different entity, even though both objects are labelled w?

In general I find the supplementary material confusing. I believe it is trying to fit an RBM projected to the d-dimensional subspace defined by PCA of the data to the empirical data distribution in that same subspace. However, approximations are clearly required in order to compute the projected RBM distribution. Given that, for a very low dimension d then one can easily discretise the model and carry out a simple maximum likelihood fit. If that is what is being done, it is not well explained and rather misleading (since this requires approximations itself).

An alternative (and standard) way to compute the marginal p(m) is to use the integral (Fourier) representation of the Dirac delta function. This means that the summation over v can be then carried out exactly, leaving only a d-dimensional integral to exactly compute p(m). This can also be carried out using discretisation for small d. The authors are (as I can understand) also using discretised integrals, so I'm unclear why they don't employ the standard Fourier Delta representation approach to compute p(m) -- this would seem to involve less approximations that the approach the authors consider.

### Soundness
2

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
4

### Summary
The claimed novelties of this work are twofold. 
First, this paper proposes low-ranking training of RBMs by directly encoding the principal components throughout a convex-optimization process. This pre-training component proves to be very efficient when data are particularly clustered. In such cases, target densities are highly multimodal, and the model struggles to "discover"all the modes from scratch during training without the pre-training phase. This autonomous discovery of new modes is often associated with second-order phase transitions, similar to systems from statistical mechanics, where critical slowing down prevents the discovery of all modes in finite time efficiently. 

As a second contribution, the paper also investigates how to use a variation of parallel tempering (PT) algorithms, termed parallel trajectory tempering, to sample more efficiently and obtain log-likelihoods estimates. In simple terms, parallel trajectory tempering (PTT) essentially relies on the same idea of parallel tempering of swapping between models at different temperatures using the Metropolis rule (and therefore retaining detailed balance). However, differently from PT, PTT swaps a full set of parameters $\Theta^t$ instead of the temperature $\beta$ only. In that sense, it can be thought of as a generalization of PT. 

Numerical experiments in Fig. 2 prove the pre-trained low-rank RBM to be more capable of identifying all modes in highly clustered data, while Figs. 3-4 show that PTT allows more accurate loglikelihood estimation and faster yet more efficient sampling from all modes of distribution compared to standard alternate Gibbs sampling (AGS).

### Strengths
- The paper is well-written and easy to follow. 
- It represents a pleasant read that is accessible to a broad audience. 
- The literature review and related work section read well and are exhaustive.
- The idea of pre-training the RBM to encode the principal components is simple yet very effective. 
- Leveraging the analogy between critical slowing down and the struggle of RBM during training to be ergodic and discovering all modes of the distributions is elegant and intuitive (though I suppose this is not a novelty of this paper, it is very nicely pictured in the introduction). 
- The numerical experiments look solid and aligned with the theoretical insights given in the main text. 
- I have not thoroughly checked the mathematical details in the appendix, but at first glance, they look good.

### Weaknesses
 - I find it a bit challenging to identify the two main contributions in the paper as those are totally disentangled in their presentation between Sec. 4 and Sec. 5.2. I strongly recommend adding a list of bullet points at the end of section 1 to clearly list the contributions of work and crossref to the corresponding point in the paper. This would substantially help navigate the paper.  
- I find that the structure of sections 5.2 and 5.2.1 can be improved. In particular, I find it confusing that Parallel Trajectory Tempering is introduced in section 5.2, and Parallel Tempering approaches are discussed in section 5.2.1. I find this logically inefficient as I believe that a more natural yet easier-to-follow flow would be to first introduce Parallel Tempering approaches and then explain what makes PTT different compared to existing approaches from the literature. As this is one fundamental contribution of this work I believe it is crucial to rework these sections such that the actual novelty emerges more clearly from the discussion. 
- The discussion around eq. (4) is rather crucial for the paper as it represents one of the main contributions of this work. Currently, the novelty with respect to Decelle and Furtlehner (2021a) is not very clear to me, and I would appreciate it if the authors could elaborate more on this. Moreover, what's the intuition behind the "magnetizations" along each of the singular vectors? Is there any correspondence with the magnetization as a physical observable? As far as I understand, those should be the projections along the unitary vectors of the visible variable. Is that correct? If all my understanding is correct, then the new contribution of this work is to use a bias initialization along a direction $\boldsymbol{u}_0$, which augments the dimensionality of the system by one in the bias direction. If all above is still all correct, I wonder the following:
    - How beneficial is to have such an augmented direction for the bias compared to the naive approach proposed in Decelle and Furtlehner (2021a)?
    - Have the authors conducted any ablation studies to compare the differences in performances between Decelle and Furtlehner (2021a) and their new approach from an empirical standpoint?

This latter point is crucial in assessing the effective novelty of this work. At the moment the reason for the lower score is primarily due to my perception of limited novelty. I am more than happy to discuss this with the authors during the rebuttal and revisit my score upon clarification of my concerns above (and below, see, e.g., the first bullet point in the **Questions** cell).

### Questions
## Questions, Small comments and typos
- Would it be possible for the authors to provide a sketch and pseudocode for their PTT algorithm as a standalone and in comparison to PT? This would be very helpful to get a better understanding of the contribution of this work. 
- Is there any intuition behind the bump observed in Figure 3 at around $10^3$ gradient updates (left and middle plot).
- Layout: there's a problem with Figure 2. The x-axis is sometimes completely or partly cut. I strongly recommend carefully checking this, aligning the plots, and making sure such problems are removed. 
- In general the authors often refer to the Appendix as SI (I assume Supplement Information). I guess this acronym has not been defined anywhere. I identify its first occurrence in line 96. Perhaps the authors can define what SI is or, alternatively just all it appendix. 
- Line 235: I'd recommend adding a reference for critical slowing down. This comment applies to earlier occurrences of this concept.
- Line 459: grew -> grey
- Line 512: Banos et al. (2010) might need to be wrapped in parenthesis \cite -> \citep

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This research proposes an efficient training approach for structured data in RBMs by employing pre-training based on simple convex optimization, which significantly facilitates learning for structured datasets. Furthermore, the study introduces a novel sampling and log-likelihood evaluation method that leverages the model's learning process, differing from conventional Parallel Tempering.

### Strengths
- The paper offers a novel contribution by proposing a pre-training technique and a new sampling approach for RBMs inspired by their thermodynamic properties. This builds on the existing theoretical analyses of RBMs.
- To my knowledge, extending replica Monte Carlo methods to a learning trajectory is original and intriguing.
- Including a specialized physics background in the Appendix makes the paper accessible even to readers without a physics background.

### Weaknesses
The distinction between theoretical claims and empirical findings is not clear. It would be beneficial for the authors to clarify which parts of the study are based on theoretical analysis and which are supported by numerical experiments, particularly in the context of related work. For instance, the first- and second-order phase transition claims pertain to equilibrium properties. However, it is unclear how these phase transitions are justified when updating parameters with limited samples.

- In Section 4, the paper introduces pre-training for low-rank RBMs with singular value decomposition (SVD)--based weights, aiming to avoid continuous phase transitions (second-order transitions) as structural patterns gradually emerge. It is further claimed that training can proceed quickly using the PCD method after post-pre-training. Could the authors provide a more detailed explanation for this intuition? Even if second-order transitions are avoided, if there are multiple stable clustered states, capturing multiple modes with the PCD method may be challenging and could introduce bias in the estimation. However, the paper claims, "Once the main directions are incorporated, training can efficiently continue with standard algorithms like PCD, as the mixing times of pre-trained machines tend to be much shorter than at the transitions." I believe that simulating clustered models with simple PCD often results in impractically long mixing times. Indeed, in Section 5.2, it is argued that mixing is very slow for AGS in clustered data.

- The statement "It’s also often ineffective with highly clustered data due to first-order phase transitions in EBMs, where modes disappear abruptly at certain temperatures, as discussed by Decelle & Furtlehner (2021a)" suggests that using PT becomes challenging because the learned RBM exhibits a first-order transition at specific temperatures. However, does the existence of a first-order transition in the learned RBM typically occur regardless of the statistical model being learned? For example, if learning a model without a first-order transition, such as the Ising model without a local field, does a first-order transition still arise in the learned RBM? This seems somewhat nontrivial.

- In the phase diagram of A. Decelle’s Thermodynamics of Restricted Boltzmann Machine and Related Learning Dynamics does not appear to be a first-order transition, and the AT line may suggests continuous phase transitions dominated by Full-step RSB. Thus, the claim regarding first-order transitions requires further elaboration. If a first-order transition is present, it would be essential to validate this by examining the free energy from the equilibrium state of the learned model, which could likely be accomplished by evaluating the partition function using the proposed method.
- If a first-order transition does exist, then the exchange probability in PT would approach zero near the transition. Has this phenomenon been observed? Additionally, it would be helpful to evaluate the round-trip rate of PT and PTT.
- While it is argued that preparing models at different temperatures is challenging for PT, it should be noted that the proposed approach also requires storing models during the learning process.
- The CelebA data in Figure 2 appears to be truncated.

### Questions
- Does critical slowing down occur in the energy-based model when the hidden variables are traced out, or does it occur in the joint distribution that includes the hidden variables? If the phase transition occurs in the joint measure, does the traced-out distribution also exhibit a phase transition?
- What is the definition of $\bar{u}$?
- Could the authors provide a detailed derivation of Equation (4)? The terms $\bar{u}_{a}$ and $\eta_{a}$ are currently undefined.
- The phrase "a direction $\bar{u}_0$ is used for the magnetization $m_0$ that is only present in the bias term" is unclear. Could you explain this in more detail?
- Is it possible to learn DBM without pre-training using the pre-training with weights introduced by [1] ?

[1] Yuma Ichikawa and Koji Hukushima, Statistical-mechanical Study of Deep Boltzmann Machine Given Weight Parameters after Training by Singular Value Decomposition.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper studies algorithms for the training of Restricted Boltzmann Machines (RBMs).  It argues that "highly structured" data require different algorithms than those that have been successful for, e.g., image datasets.  There are three algorithmic ideas that are discussed: 1) Pre-training an RBM using an "exact" procedure that produces low-rank weight matrices; 2) Estimating log-likelihoods using annealed importance sampling across steps of a training run; and 3) Using parallel tempering for sampling, again using different steps of training. Evidence for the efficacy of these procedures is provided in the form of curves from training runs on a few small datasets.

### Strengths
1. The idea of low-rank pre-training is interesting and seems like it could be useful if it scaled up.

2. The idea of doing AIS across the training run is creative and clever.

3. Parallel tempering across training steps seems new.

### Weaknesses
1. I think this paper has a somewhat limited audience.  It mostly builds upon work from a small group of authors, using language most familiar to that community.  (For example, one person's work is cited thirteen times in the references.)  A significant amount of jargon is used that keeps this from being a readable stand-alone paper.  This is coupled with heuristic explanations for things that appear to rely on sharing the particular statistical mechanical point of view of this subcommunity.

2. Much of the motivation for the work centers on "highly structured" data, which is not defined clearly.  The authors indicate that this corresponds to the existence of clusters.  The paper does not show examples of the methods succeeding or failing in the presence of this structure.  For example, the Celeb-A dataset is given as an example of a dataset in which there are not clusters and so it is not "highly structured".  However, Figure 2 does not seem to show us that this matters for the pre-training procedure.  Figure 15 is
similar.  Why does one conclude that the bottom row of Fig 2 and Fig 15 are significantly different from what we see in the top row of Fig 2?  The lack of a clear definition of "highly structured" makes it difficult to assess the scope of the proposed methods.  A more rigorous characterization, perhaps using measures of cluster separation or mixing times of Markov chains, would be beneficial.

3. The main text is highly verbose, with most of the actual concrete content being in the appendices.  I don't think anything novel is introduced until page six. The core algorithmic contributions should be presented earlier and more concisely in the main text, with the appendices reserved for supporting details.

4. I find it difficult to appreciate precisely what the contribution of Section 4 is.  As I understand it, the insight is "do Decelle & Furtlehner (2021a) before you do PCD".  This is useful information, but between this section and Appendix A, I'm not sure where the boundary is between this and D&F (2021a). The specific modifications or extensions to the D&F (2021a) method should be clearly delineated, highlighting the novel aspects of the current work. It is unclear what specific practical challenges are overcome by the changes.

5. While the ideas of section 5 are interesting and Figure 3 is intriguing, the empirical results are at the level of "preliminary findings" on a single small problem.  Even with the vastly smaller compute resources of 15 years ago, RBM researchers were studying larger problems. The lack of experiments on larger datasets or more complex problems limits the impact of this section. The paper should demonstrate the scalability of the proposed methods.

6. The title is too broad relative to what the paper delivers.

Typos:
 - L161-162: "two slow"
 - L478: "exchanges parameters" but I think you mean "exchanges configuration".
 - L775-776: \bar{u} vs \hat{u}.
 - L836-837: "gradient is convex" -- surely you mean the training objective is convex in the parameters.

### Questions
1. Why didn't you apply this to larger problems?

2. What are situations where the pre-training fails?

3. Is PTT useful for generating samples during training, using only earlier parts of the training run?

### Soundness
2

### Presentation
2

### Contribution
2
