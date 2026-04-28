# Latent-EnSF: A Latent Ensemble Score Filter for High-Dimensional Data Assimilation with Sparse Observation Data

- Decision: Accept
- Avg Score: 6.17
- Scores: 5, 6, 6, 8, 6, 6

## Abstract
Accurate modeling and prediction of complex physical systems often rely on data assimilation techniques to correct errors inherent in model simulations. Traditional methods like the Ensemble Kalman Filter (EnKF) and its variants as well as the recently developed Ensemble Score Filters (EnSF) face significant challenges when dealing with high-dimensional and nonlinear Bayesian filtering problems with sparse observations, which are ubiquitous in real-world applications. In this paper, we propose a novel data assimilation method, Latent-EnSF, which leverages EnSF with efficient and consistent latent representations of the full states and sparse observations to address the joint challenges of high dimensionlity in states and high sparsity in observations for nonlinear Bayesian filtering. We introduce a coupled 
Variational Autoencoder (VAE) with two encoders to encode the full states and sparse observations in a consistent way guaranteed by a latent distribution matching and regularization as well as a consistent state reconstruction. With comparison to several methods, we demonstrate the higher accuracy, faster convergence, and higher efficiency of Latent-EnSF for two challenging applications with complex models in shallow water wave propagation and medium-range weather forecasting, for highly sparse observations in both space and time.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The Ensemble Kalman Filter (EnKF) enables data assimilation for Nonlinear State-Space Models, but it encounters the problem of vanishing gradients in tasks where observations are sparse in high-dimensional state spaces. This paper proposes a solution to this issue by proposing the Latent Ensemble Score Filter (Latent-EnSF), which embeds states and observations into a latent space via a Variational Autoencoder (VAE). The proposed method claims to be effective for various data assimilation tasks with sparse observations in high-dimensional state spaces.

### Strengths
This paper's strength lies in demonstrating that data assimilation in the latent space can effectively solve the problem of vanishing gradients.

### Weaknesses
One issue with this paper is that it unfairly compares the LETKF under unfavorable conditions. The Ensemble Kalman Filter does not inherently suffer from the vanishing gradient problem, so embedding into the latent space is not necessarily required. If the goal is to propose a good method for data assimilation in high-dimensional nonlinear state spaces, it should be directly compared with the Localized Ensemble Transform Kalman Filter (LETKF) but not with Latent-LETKF. However, this comparison is not provided.

Moreover, physical laws are often described by differential equations with spatially local interactions, leading to strong local correlations. The LETKF leverages this locality to scale to data assimilation problems with large state spaces by performing local computations in parallel. Comparing the computation speed without considering this parallelization is also misleading. The authors should provide a more detailed analysis of the computational cost, including the overhead of the VAE and the potential for parallelization in their proposed method. A comparison of the computational time with a parallelized LETKF implementation would be more informative.

Regarding Equations (11)-(13), it is mentioned that the VAE's loss function minimizes the empirical loss function, but isn't the state ( $x_t$ ) unobserved? It is not clearly stated how learning is performed when the state ( $x_t$ ) is unobserved. The paper needs to clarify how the VAE is trained when the true state is not available during the training phase, and how the latent space is learned without direct access to the true state. The current explanation is insufficient and raises concerns about the validity of the training process.

Additionally, it implicitly assumes the state can be estimated from observations at a single time point as shown in Equation (11) ($x_t$ can be recovered either from $D(z_t)$ or $D(z_t^{obs})$). Thus, it is unclear whether this method applies to nonlinear observations. The paper should explicitly discuss the limitations of the proposed method with respect to nonlinear observation operators and provide a more detailed analysis of the applicability of the method to various types of observation models. It is also unclear how the method would perform with noisy or incomplete observations, which are common in real-world scenarios.

# LETKF is included in the experiments thanks to the authors' feedback. However, how much the initial conditions affect the performance is still unclear.

### Questions
What initial state distributions are used for the experiments? It should be explicitly given.
Regarding the perturbed trajectory, how is the perturbation applied? It should also be explicitly given.

### Soundness
2

### Presentation
2

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
The paper presents a novel data assimilation method called Latent-EnSF aimed at improving accuracy and efficiency in modeling high-dimensional and nonlinear systems with sparse observations. The authors propose using a coupled VAE with two encoders, one for the full state and another for sparse observations. This ensures consistent encoding of both types into a shared latent space, allowing efficient assimilation with fewer dimensions. Overall, the research topic is of interest in the community of data assimilation. However, from a methodology point of view, the novelty of the proposed approach might be limited to the combination of existing ENSF and latent data assimilation algorithm.

### Strengths
The Latent-EnSF method presented in this paper addresses key challenges in data assimilation for high-dimensional systems with sparse observations by leveraging a coupled VAE to compress both state and observation data into a shared latent space (However this idea is not new). This approach not only reduces computational complexity but also enhances the robustness of data assimilation when observation data is sparse, avoiding the gradient vanishing issues that hinder ENSF. Experimental results demonstrate Latent-EnSF's superior accuracy, faster convergence, and computational efficiency compared to existing methods.

### Weaknesses
The Latent-EnSF builds upon EnSF by integrating latent representations that avoid the computational challenges of sparse data. While the idea is sound and logical, performing data assimilation in the latent space is a well-established approach (see, for example, Peyron et al., 2021, 'Latent Space Data Assimilation Using Deep Learning'). Additionally, conducting data assimilation with a shared latent space for both the state vector and observations is also a known concept (see, for example, Cheng et al., 2024, 'Multi-domain Encoder–Decoder Neural Networks for Latent Data Assimilation in Dynamical Systems'). Therefore, from the reviewer’s perspective, the novelty of this paper primarily lies in combining existing latent data assimilation techniques with ENSF.

As the authors mentioned, since the state and observation vectors are encoded into a common latent space, the transformation function is restricted to an identity mapping. However, this may pose a problem regarding the specification of the observation error covariance matrix in the latent space; specifically, how to transform uncertainties from the full physical space to the latent space remains an important question. In the numerical experiments, the authors should also include noisy observations and demonstrate how latent-ENSF could account for observation uncertainty.

### Questions
A lot of latent data assimilation algorithms make use of the variational DA framework instead of enkf, for ex, Peyron et al., 2021 and Melinc et al, 2023. The authors should also compare 4d-var based latent DA approaches against latent-ENSF.

 Instead of only sparse observations, it would also be interesting to compare latent-ensf against existing methods for partial and irregular observations.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper identified a shortcoming in the recently developed Ensemble Score Filtering method, which is that observations at sparse sites lead to a collapse in the model gradient, by introducing a low-dimensional latent variable encoding, which recovers improved inference in this sparse setting.

### Strengths
This problem is high value, and the approach unifies several interesting ideas.

Empirical results are impressive.

### Weaknesses
Minor cosmetic and presentational issues. These are not crucial, but I will attempt to note when I see them

More crucially, theoretical explanation for the empirical success does not seem complete, and details are missing which might allow the reader to deduce this for themselves.

Firstly, there are a number of small errors and typos, e.g. equation 14 introduces the KL "Divergence" as  function of the parameters of the Gaussian distribution $\operatorname{KLD}(\mu,\Sigma)$ .That is not a divergence. It looks like it is maybe the conventional KL between a given diagonal Gaussian and a standard diagonal Gaussian? There are also some in the section 4.1.1, which I will address in the Questions. There are a couple more I noticed but did not note down; I'll leave these cosmetic issues aside for the moment so we can get to the substantive weakness and return if there is time.

The paper's argument on an important assertion, that sparse observations are problematic EnSF updates (l202). However, this part of the argument is not made sufficiently clearly for such a central part of the paper. The first supporting evidence  (figure 8 in appendix b) is confusing - AFAICT it simply shows what a sparse sampling grid looks like, which... doesn't really show anything. That is just a graphic depiction of the form of the observation operator $H$, I think. Section 4.1.1 does heavier lifting, which is that attempts to show that empirically, as the updates get sparser in the sense of sampling a coarse spatial grid, the quality of the EnSF estimates degrades. However, I am not convinced it does show that; It is unclear to me if this is because the experimental evidence itself is lacking; it could be the labeling in the figures. See questions for clarifications on that point.

The explanation for what problem is being solved here and why the solution works seems incorrect or at least incomplete.
If the baseline is EnSF, which uses (up to some discretization error and ensemble approximation etc) the "true" model $M$ and the "true" observation operator $H$, then it should in principle recover the "best" estimate of the system dynamics. the proposed method Latent-EnSF claims to get superior performance by introducing a further layer of approximation, mapping the observations and dynamics into a VAE. Since we have introduces a further approximation then we must assume that all else being equal, the VAE-based method should be worse in accuracy (it might be faster at inference time or something like that).

As such, if Latent-EnSF  it is doing better in accuracy terms than EnSF, it seems that it should be because it gets to exploit more information at inference time than does EnSF. Presumably this "extra" information is in the form of better spatial smoothing encoded in the encoder/decoder networks of the VAE, which can presumably learn the which spatial fields are in the training data. If so, we expect that the information enters the method via the training losses (11,12,13) and also by the training data set. The paper does not seem to interrogate the training losses and also I cannot easily work out what the actual training procedure is for the neural nets, so it is not clear to the reader what smoothing the neural nets are actually learning.

### Questions
## What is the actual deficiency of EnSF?

The empirical results are great.
What is actually happening here theoretically? Since Latent-EnSF and EnSF are both targeting the same likelihood, and the VAE-based Latent-EnSF is making a looser approximation to the posterior than the original model, then it is not sufficient IMO to claim it is simply addressing a problem of missing gradient; Latent-EnSF needs to be jsutified in terms of how it draws better inference from the same information.
I've expanded on this question in the _weaknesses_ section, but I invite you to answer it here.

As part of that I also suggest it will be good to clarify which data (training data, inference time observation) informs the final prediction. Questions about that in the next section. 

## What is the training distribution?

What is the training process used for the NN? What distribution of states is in that dataset? Does an encoder trained for (however many trajectories are in this dataset) generalize badly to data assimilation problems drawn from a different dataset (say, different initial conditions) in a way that EnSF does not? That would be evidence that this method learns a good spatial smoothing, and would also suggest a deficiency in the original EnSF, if it has difficulty in spatial smoothing

## Section 4.1.1
I'm confused about both figures and the explanation. Can you answer for me the following?

1. Figure 2: I'm not sure what $\eta$ is. Is it the reconstructed state? If so, in the 4x sparse row we see that the reconstructed solution has a banded structure. Why? I know that the _observations_ updates are sparse, but when we propagate from those back through our diffusion steps, should we not recover a densely sampled field at whatever resolution our simulator $M$ runs?
2. Figure 3:  

   1. it's not clear what "perturbed" means here. From cross checking I think this is the error that a simulator would accrue from failing  to update at all. Why is it constant? For interesting models (e.g. with lyapunov exponent ) I would expect this to grow over time. This leads me to wonder if the systems that are being modeled here are not very interesting, or maybe that RMSE is a bad measure, or that the duaration over which we observe the system is simply not interesting. For the kind of challenging systems mentioned in the paper (e.g. the high dimensional lorenz) I would expect diverging loss metrics under perturbation
   2. I'm not even sure which model is being plotted in these figures. It looks like a fluid PDE?
  3. There are no error bars here. I would expect for such a central plot that we would make some attempt to plot error bars under random perturbations and ideally also random initial conditions.

## What sparsity patterns are allowed?

The proposed method appears to have a curious limitation, which is that the spatially-sparse observations must occur at fixed sites $S$ for all timesteps. This is not required in the EnKF and, although i know it less well, should not be required in the EnSF. Is it required for this model also, or can that be relaxed?

## section 4.1

>However, though the Latent-LETKF beats the Latent-
>EnKF benchmark, especially with higher latent dimensions, our approach is still much better in
>terms of assimilation speed, accuracy, and efficiency (see Table 1) for all cases.

Some confusing phrasing. *Is* that table 1 shows? It seems to me that it shows on two benchmarks, Latent-EnSF is the fastest in terms of wall-clock inference time. (Side point: it's ok in my opinion to use minimal wall clock time for operations with a deterministic number of FLOPs, means and standard deviations are not ideal for timing execution which is an asymmetric right-skewed distribution who randomness is mostly due to external factors) However the graph shows that on (I think on some different model?) that Latent-EnSF is more accurate than Latent-LETKF.
Moreover, some of these methods (the VAE-based ones) require us to train a neural network, and others (EnKF) do not. How much does the NN training time add to these? When I've trained my encoder networks, does that generalise to unseen initial conditions, or do I need to train a new encoder? When do I need to train a new encoder? How costly is that? 
These is not to say that I think anything is incorrect, but rather that the statements and supporting evidence are messy, and comparisons do not appear to be "apples-to-apples". Can you make the statements more precise? or the example more strictly comparable?

Why LETKF? I'm not advocating an exhaustive pairwise comparison between every possible model in this domain, but if the primary comparison is with LETKF then that method might need to be introduced more. note also that EnKF can handle this case as well, so would have been a logical method to include on the Figrues 4 and 5. If you are not going to do that (and I am sympathetic we we all get asked to do too many comparisons in these conference submissions) then can you make the justification explicit for which comparisons you wish to make?

Figure 8: The paper talks about $\nabla_x \log P(y|x)$ and yet graph shows $\nabla_x P(y|x)$. Why?

Figure 8, figure 2: There is not color bar on the plots ot help us interpret the field values. I assume white means zero valued and the colors are bipolar? If so, I have a further question: The plots show the score function evaluated at sparse spatial locations by showing fewer pixels non-zero with values in a grid of fixed size, implying that gradient of the score function at these locations is also zero. To my mind, would be more correct to say that the score is not sampled at that location and has no value, rather than being zero. We would more conventionally show that by displaying a lower-resolution grid, i.e. with fewer, larger pixels. Moreover, we could imagine in-filling the grid, now? $\nabla_x \log P(y_2|x_1)$ will still convey influence, and thus a gradient between the sampling sites of  $x_1$ and $y_2$ if they are spatially near each other. Or: Am I missing something? Do I not understand the conditioning operation correctly in the score function?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper aims to address the problem of assimilating sparse observation data effectively using the ensemble score filter framework for data assimilation. Their method proceeds by encoding both state and observations to a latent space of the same dimension before applying the score-based ensemble filter. This allows one to avoid the issue of having mismatched size of the observation and state dimensions, preventing vanishing gradient of the likelihood. Experimental results demonstrate the efficacy of the approach showing further promise of score-based methods for data assimilation.

### Strengths
The paper addresses a critical issue with many of the score-based filters being proposed recently, namely, that the observations being assimilated are too idealistic. The methodology proposed in this work brings it closer to more realistic scenarios, where observations are sparsely distributed. Results in the experiments are encouraging, showing that the latent EnSF can significantly outperform standard EnSF or LETKF in latent space. The writing is generally clear and sufficient details are provided to implement the proposed model.

### Weaknesses
One key weakness of this work is that baseline comparisons against traditional DA methods are missing. For example, how does it compare to standard ensemble Kalman filter (LETKF) or 4DVar in physical space? The authors consider LETKF in latent space but this approach is not actually used in practice. If we want to really demonstrate efficacy of the approach, a comparison with these traditional method should be provided. These methods are likely to perform quite well on the presented examples so it will help us see how much extra benefit we can gain by replacing them with the proposed latent EnSF framework. Furthermore, some details of the algorithm were unclear to me, which you can find below in __Questions__. Finally, plots to show the sparse observations can be improved by increasing the marker size. At the moment, it is impossible to see where the observations are without zooming in significantly.

### Questions
- The authors should clarify that the Kullback-Leibler divergence in (14) is taken with respect to the standard normal measure. When talking about statistical divergences, one should specify which two measures the divergence are taken with respect to and in which order.
- Is the loss in (11)-(13) correct? The reconstruction term should be marginalised over the latent variable $z_t$ if this were to be trained like a VAE.
- Related to the above question, can the loss (11)-(13) be derived from first principles via variational Bayes? Or is the loss more just "VAE-inspired"?
- Do we train for the encoder/decoder at every timestep $t$? Do the authors take into account its training cost if so? It seems quite expensive to achieve in practice.
- At the moment, it seems like the method only works in the case where the observations are placed on a regular grid. Is there a way to extend this to a more realistic scenario where the observations are less regularly sampled?
- Could the authors please elaborate more on how they compute the latent observation noise $\hat{\gamma}_t$? The authors only give a passing remark but this does not seem so obvious to me.
- How do the results in the experiments compare to more traditional data assimilation methods like the EnKF or 4DVar? Does the latent EnSF still outperform these in the sparse observation setting?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper develops the recently proposed Ensemble Score Filters (EnSF) by incorporating Variational Autoencoder (VAE) to define EnKS in the latent space derived by VAE. The resulted algorithm, hence named latent-EnSF, inherits the effectiveness of EnSF in high-dimensional data assimilation, but also solves the issued of EnSF when dealing with the sparse observations. Despite some possible typos, the proposed method is clearly explained, supported with thorough comparison with various alternative algorithms including vanilla EnSF, latent-EnKF, latent LETKF, FourCastNet using two models in water wave propagation and medium-range weather forecasting.

### Strengths
Most of the implementation in the latent space of EnSF is straightforward. The added benefit of handling sparse observations by running EnSF in the latent space is impressive and has potential impact in data assimilation in high dimensions with sparse observations. I certainly appreciate the thorough comparison offered in this paper.

### Weaknesses
1. EnSF has already achieved great results in high-dimensional data assimilation problems. VAE is used as a dimension reduction method. The mysterious capability of handling sparse observations by combining them remains largely un-explained. Though there is some on line 323, the paper may benefit in clarity from more elaboration in this aspect. Specifically, the paper does not clearly articulate why the latent space representation enables the method to overcome the limitations of EnSF with sparse observations. The explanation should delve into the specific properties of the latent space that facilitate this, such as how the VAE's learned representation might regularize the problem or provide a more informative gradient for the assimilation process, especially when the observation operator is highly ill-conditioned due to sparsity.

2. The most difficult part to understand is the latent matching term (13) on line 244. Two encoders, the state encoder and the data encoder, compress two different things. Why do they need to match the codes (mean and variance) in the latent space? I see the authors report segregated latent representations without such term, but I still find it unnatural and lack some explanation on its contribution to the capability of handling sparse observations. The paper should provide a more detailed justification for why aligning the latent representations of the state and observations is necessary. It is not clear why the means and variances of these two different encodings should be forced to match, especially given that the state and observations have different dimensionalities and information content. A more thorough explanation of the theoretical underpinnings of this matching, and its impact on the overall performance, is needed.

3. The precision of solutions to inverse problems naturally depends on the data information available. While I am impressed by the comparison between EnSF and latent-EnSF in terms of handling the sparse observations, some comments on the limitation of the proposed latent-EnSF is also appreciated. The paper should discuss the limitations of the proposed method, especially in scenarios where the observation data is extremely sparse or noisy. It is important to understand the boundaries of the method's applicability and how it might degrade under challenging conditions. For example, how does the method perform when the observation data is so sparse that it provides very little information about the true state, and how does it compare to other methods under such conditions?

### Questions
* Line 222: What do you mean by "the output as a full-dimensional observation in the latent space"? Is it "in the full space"?

* Equation (14), KL divergence is defined between two distributions. What are they in your equation (14)? Did you mean to say $KL(N(\mu_t, \Sigma_t)|| N(\mu_t^\text{obs}, \Sigma_t^\text{obs}) )? Then pay attention to the signs.

* Line 314: can you comment on the computational cost of this step because equation (16) involves both encoder and decoder.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 6

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces Latent-EnSF, a data assimilation method designed to address the challenges of high-dimensional state spaces and sparse observations in nonlinear Bayesian filtering problems. By extending the Ensemble Score Filter (EnSF) with a latent space representation using coupled variational autoencoders (VAEs), the method transforms both full states and sparse observations into a shared encoded latent space. Then, it leverages EnSF, a score-based filtering method, to filter in the encoded latent space.  The paper claims that leveraging the proposed method can effectively overcome the limitations posed by sparse observations. The numerical results show the improved accuracy, faster convergence, and enhanced computational efficiency in high-dimensional nonlinear systems, with applications in shallow water wave propagation and medium-range weather forecasting.

### Strengths
The paper presents a clear and well-motivated rationale for addressing high-dimensional data assimilation with sparse observations in EnSF. The proposed method is intuitively and logically structured, and the experimental results validate its effectiveness and improvements over some of the existing approaches.

### Weaknesses
A potential weakness of this paper is the absence of certain important details regarding the developed method, which are noted in the discussion section.

1. The primary question I have regarding this paper is about the training of the VAE. Specifically, it is unclear whether the encoders and decoder are trained at each time step $t$ or if they are pre-trained. Based on Equations (11–13) and Figure 1, it appears that the input data $ x_t$ for the encoder is derived iteratively during the data assimilation process (from predictive distribution), suggesting that the VAE might need to be retrained at each step. If so, this would significantly slow down the filtering process, raising questions about the efficiency claims presented in the experimental results. Additional clarification on the training procedure of the VAE is necessary to understand how the reported computational efficiency is achieved.

2. The presentation of Section 3.2 is somewhat confusing, and a few points could use further clarification:

   - Could you please elaborate on the need for introducing $ \xi_t $ and $ \zeta_t $? Are these variables different from the $ z_t $ and $ z_t^{\text{obs}} $ used in Section 3.1, and if so, how?
   - In lines 320–321 on page 6 and in Algorithm 1, why is the reparameterization trick needed again to sample the latent variable $ z_t $? My understanding is that after solving the reverse-time SDE in Equation 6, you already have the ensemble of latent states as samples. Could you clarify this step?

3. Minor Issues:

 - Consider moving Figure 1 to Section 3, as it would better illustrate the proposed method in context.

 - In Section 3.1, certain notations are unclear, such as $ \Sigma_t $ and $ \sigma_t $. Clearer definitions would improve readability.

 - On page 5, you note that the GLA proposed by Cheng et al. (2023) can face computational issues when the latent space is high-dimensional. While I agree, typically, as shown in this paper, the latent dimension $ 2r \ll d $, so GLA’s efficiency may not necessarily be compromised in this case. Did you consider including a comparison with GLA in the experiments? 

 - While the method is based on the EnSF, it seems that the discussion on the existing data assimilation methods for high-dimensional state spaces and sparse observations is missing e.g. (and more),

      - Chen Y, Sanz-Alonso D, Willett R. "Reduced-order Autodifferentiable Ensemble Kalman Filters," *Inverse Problems*, 2023; 39(12):124001.

     I believe including the discussion of more related work could make the proposed method's positioning more comprehensive.

### Questions
1. The primary question I have regarding this paper is about the training of the VAE. Specifically, it is unclear whether the encoders and decoder are trained at each time step $t$ or if they are pre-trained. Based on Equations (11–13) and Figure 1, it appears that the input data $ x_t$ for the encoder is derived iteratively during the data assimilation process (from predictive distribution), suggesting that the VAE might need to be retrained at each step. If so, this would significantly slow down the filtering process, raising questions about the efficiency claims presented in the experimental results. Additional clarification on the training procedure of the VAE is necessary to understand how the reported computational efficiency is achieved.

2. The presentation of Section 3.2 is somewhat confusing, and a few points could use further clarification:

   - Could you please elaborate on the need for introducing $ \xi_t $ and $ \zeta_t $? Are these variables different from the $ z_t $ and $ z_t^{\text{obs}} $ used in Section 3.1, and if so, how?
   - In lines 320–321 on page 6 and in Algorithm 1, why is the reparameterization trick needed again to sample the latent variable $ z_t $? My understanding is that after solving the reverse-time SDE in Equation 6, you already have the ensemble of latent states as samples. Could you clarify this step?

3. Minor Issues:

 - Consider moving Figure 1 to Section 3, as it would better illustrate the proposed method in context.

 - In Section 3.1, certain notations are unclear, such as $ \Sigma_t $ and $ \sigma_t $. Clearer definitions would improve readability.

 - On page 5, you note that the GLA proposed by Cheng et al. (2023) can face computational issues when the latent space is high-dimensional. While I agree, typically, as shown in this paper, the latent dimension $ 2r \ll d $, so GLA’s efficiency may not necessarily be compromised in this case. Did you consider including a comparison with GLA in the experiments? 

 - While the method is based on the EnSF, it seems that the discussion on the existing data assimilation methods for high-dimensional state spaces and sparse observations is missing e.g. (and more),

      - Chen Y, Sanz-Alonso D, Willett R. "Reduced-order Autodifferentiable Ensemble Kalman Filters," *Inverse Problems*, 2023; 39(12):124001.

     I believe including the discussion of more related work could make the proposed method's positioning more comprehensive.

### Soundness
2

### Presentation
2

### Contribution
2
