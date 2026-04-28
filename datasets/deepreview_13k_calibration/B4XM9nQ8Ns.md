# HyperSINDy: Deep Generative Modeling of Nonlinear Stochastic Governing Equations

- Decision: Reject
- Avg Score: 6.00
- Scores: 5, 5, 8, 6, 6, 6

## Abstract
The discovery of governing differential equations from data is an open frontier in machine learning. The {\em sparse identification of nonlinear dynamics} (SINDy) \citep{brunton_discovering_2016} framework enables data-driven discovery of interpretable models in the form of sparse, deterministic governing laws. Recent works have sought to adapt this approach to the stochastic setting, though these adaptations are severely hampered by the curse of dimensionality. On the other hand, Bayesian-inspired deep learning methods have achieved widespread success in high-dimensional probabilistic modeling via computationally efficient approximate inference techniques, suggesting the use of these techniques for efficient stochastic equation discovery. Here, we introduce {\em HyperSINDy}, a framework for modeling stochastic dynamics via a deep generative model of sparse governing equations whose parametric form is discovered from data. HyperSINDy employs a variational encoder to approximate the distribution of observed states and derivatives. A hypernetwork \citep{ha_hypernetworks_2016} transforms samples from this distribution into the coefficients of a differential equation whose sparse form is learned simultaneously using a trainable binary mask \citep{louizos_learning_2018}.
Once trained, HyperSINDy generates stochastic dynamics via a differential equation whose coefficients are driven by a Gaussian white noise.
In experiments, HyperSINDy accurately recovers ground truth stochastic governing equations, with learned stochasticity scaling to match that of the data.
Finally, HyperSINDy provides uncertainty quantification that scales to high-dimensional systems.
Taken together, HyperSINDy offers a promising framework for model discovery and uncertainty quantification in real-world systems, integrating sparse equation discovery methods with advances in statistical machine learning and deep generative modeling.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Authors introduce a framework called HyperSINDy for modeling stochastic dynamics using a deep generative model that discovers the parametric form of sparse governing equations from data. It employs an inference model and generative model to discover
an analytical representation of observed stochastic dynamics in the form of a random ODE (RODE). It is particularly useful for random coefficients.

### Strengths
Figure 1 shows the scheme of this method. It has three steps: inference mode, generative model and SINDy. It basically glue the Hypernetwork and SINDy together to tackle the random coefficient case.

### Weaknesses
1. It is a typical A+B type of paper. Each part is well studied and author glue them together and demonstrate it in several simple examples. I don't think there is enough novelty here.

2. All three examples are artificially made for this algorithm. All examples are corrected identified but I am not impressed unless authors are able to demonstrate some non-trivial RODE. The second example equation (11) is not even a valid example of stochastic  Lotka-Volterra. I don't know what is N(0,1) on the Right hand side means here. 

3. Authors have limited knowledge on RODE here in fact not all SDE can be transformed to RODE and vice versa. And in general RODE case, z is not independent with x.

### Questions
If x' is not available (e.g., after training), z is sampled from the prior z ∼ p_θ(z) to produce \Xi. I don't understand this part. Please elaborate more or give an example.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This work introduces HyperSINDy, a framework to model a family of special stochastic dynamics via a deep generative model of sparse, nonlinear governing equations whose parametric form is discovered from data.  HyperSINDy is built upon the combination of hypernetwork and SINDy and can learn a family of stochastic dynamics whose coefficients are driven by a Wiener process.

The main contributions of the HyperSINDy are summarized as follows: 
(1) This framework can efficiently and accurately model random differential equations (random ODEs), whose coefficients are parameterized by a Wiener process. Hence, it provides a generative modeling of stochastic dynamics when their random ODE forms are driven by white noises.

(2) HyperSINDy can discover the analytical form of a sparse governing equation without a-priori knowledge. Also, by using the sparse masks, the computational complexity of HyperSINDy is scalable.

### Strengths
(1) The authors represent a proof of concept for this architecture, the manuscript is well written. The numerical results are convincing.
(2) The authors of this work employ the random differential equations (random ODEs) as the library of candidate functions for SINDy. This approach is innovative and it enables the extension of SINDy from deterministic to stochastic dynamics.

### Weaknesses
 (1) Random differential equations are conjugate to stochastic differential equations. It is unclear how to convert a general SDEs into its random ODEs representations, for example, the Langevin type dynamics. The manuscript does not provide a clear, generalizable method for transforming a given SDE into its corresponding random ODE form, which limits the practical applicability of the proposed framework to a broader class of stochastic systems. Specifically, the lack of a systematic approach to handle different types of stochastic terms, such as multiplicative noise, raises concerns about the method's versatility.
(2) This manuscript lacks a comparison with other methods. The absence of a thorough comparison with existing methods for stochastic system identification makes it difficult to assess the relative performance and advantages of the proposed HyperSINDy framework. It is crucial to benchmark the method against established techniques to demonstrate its superiority or unique capabilities. For example, comparisons with methods that directly learn SDEs or other stochastic modeling techniques would be beneficial.
(3) Although the authors have commented in the manuscript, it is still unclear if this HyperSINDy framework can handle complex noise terms as well as the robustness of noises. The manuscript does not sufficiently address the limitations of the proposed method when dealing with non-Gaussian noise distributions or more complex noise structures. The performance of HyperSINDy under various noise conditions needs to be evaluated to assess its robustness and reliability in real-world applications, where noise is often non-ideal.

### Questions
(1) This manuscript could have been enhanced if it can provide examples of learning underdamped Langevin systems, for example, learn the harmonic oscillator under  thermal bath. 
(2) In particular, the manuscript could have been enhanced if it can provide an appendix discussion on how to construct a Random ODE representation for a general SDE.
(3) The manuscript could have been enhanced if it can provide numerical examples when different types of noises are added to the observation data.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work proposes HyperSINDy, a method for unsupervised discovery of governing differential equations from data in the stochastic setting. HyperSINDy combines variational Bayesian inference and hypernetworks (Ha et al., 2016) to build a generative model of the data. An L0 regularization scheme based on concrete random variables is used to ensure that the final differential equation learned is sparse and interpretable. HyperSINDy outperforms the previous state of the art in both random differential equation and stochastic differential equation settings.

### Strengths
- **The paper is very well written.** The presentation on the backgrounds (the SINDy framework, variational inference, L0 regularization) is very clear and the graphics help the readers better understand how the HyperSINDy framework works. There is also good discussion of the related works, i.e. ensembling methods and SDE-based approaches, which gives good motivation to the proposed method.
- **The proposed method is novel and achieves good improvements over existing methods.** It seems that the random differential equations (RDE) approach is a pretty novel perspective, and it is very natural to combine it with generative modeling. The HyperSINDy method also achieve uniformly better mean-squared error as well as uncertainty estimation than the best existing approach.

This paper seems like a solid advancement towards solving the very important problem of data-driven discovery of interpretable stochastic governing equations. This work will have wide applications in machine learning for science.

### Weaknesses
 - **Experimental results on higher dimensional datasets might be a bit lacking.** One of the important claims of the advantage of HyperSINDy is that it circumvents the curse of dimensionality which hinders the performance of other methods. However, only the HyperSINDy results for one 10D system is given. It might be better if the authors can clarify how the other methods perform on this system, and/or give other examples of high dimensional systems.


### Questions
- In section 3, in "$H$ implements the implicit distribution $p_\theta(\mathbf{\Xi}|\mathbf{z})$", why is it the "implicit distribution?" From my understanding, shouldn't $\Xi_z$ just be a delta distribution (deterministic) on $H(z)$?
- $p_\theta(z)$ is modeled to be a standard Gaussian with diagonal covariance. Would the independence between different $z_t$ allow sudden jumps in the parameters of the system? Would it be better to model it as something like a Gaussian process?
- Related to the last question: does the discretization step size influence the model learning result?
- I don't think what "E-SINDy" stands for is ever introduced in the paper.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes HyperSindy, which is a framework for modeling stochastic nonlinear dynamics. First a variational autoencoder is used to model the distribution of observed states and derivatives. Samples from the VAE are used with a hypernetwork to obtain the coefficients of the differential equations. These coefficients are combined with a function library to obtain the derivatives, allowing for the functional form of the equations to be learned. Experiments are conducted using simulated data, which show promising results.

### Strengths
The paper aims to learn both the parameters and the functional form of stochastic differential equations from data, which is a significant problem for scientific applications. The use of VAEs and hypernetworks for this problem is quite novel to my knowledge. The paper is well written and organized.

### Weaknesses
Experiments are conducted in simulated environments where the simulation parameters match to the modeling assumptions (mainly around Gaussianity). I would love to see more experiments confirming the applicability of the approach to broader problems, especially with real data.

As mentioned above, all the experiments are conducted using Gaussian distributions which match to the posterior distribution assumed for variational inference. Can authors comment on the limitations of these experiments?

The approach aims to learn both the functional form and parameters of the differential equations. Even though I agree that this might help with interpretability, I worry that the identifiability issues might be prominent. Do the authors expect any identifiability problems?

The promise of learning functional form is achieved through the function library. Are there any limitations of using such an approach?

What are the limitations of using a Gaussian prior with diagonal covariance for the generative model?

As mentioned by the authors, it is in general not straightforward to transform a SDE to a RODE. In fact, the transformation could be highly non-trivial and limits the application of the proposed scheme. See for example "The shifted ODE method for underdamped Langevin MCMC. by James Foster, Terry Lyons and Harald Oberhauser".

It is still not clear to me how to transform multiplicative noises.

### Questions
- As mentioned above, all the experiments are conducted using Gaussian distributions which match to the posterior distribution assumed for variational inference. Can authors comment on the limitations of these experiments?
- The approach aims to learn both the functional form and parameters of the differential equations. Even though I agree that this might help with interpretability, I worry that the identifiability issues might be prominent. Do the authors expect any identifiability problems?
- The promise of learning functional form is achieved through the function library. Are there any limitations of using such an approach?
- What are the limitations of using a Gaussian prior with diagonal covariance for the generative model?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a new framework HyperSINDy (Hyper sparse identification of nonlinear dynamics) to address the symbolic regression problems in high-dimensional, stochastic setting. Within a variational autoencoder, they use an encoder to learn the parameters $\mu, \sigma$ of the latent states $\mathbf{z}$, and a generative model to learn $p(\dot{\mathbf{x}}|\mathbf{x}, \mathbf{z})$ where $\mathbf{\dot{x}}$ is parameterized by $f_\mathbf{z}(\mathbf{x})$. With proper choice of $f_\mathbf{z}(\mathbf{x})$, they build the relationship between derivatives and coefficients for addressing the task of SINDy.

### Strengths
This paper is well written.

The idea of mapping a high-dimensional, stochastic data to a low dimensional latent space and learning the coefficients through a hyper network which takes low-dimensional latent variables are novel.

### Weaknesses
The capacity of $\Theta(\mathbf{x})$ still holds as a constraint for the performance, especially in the high-dimensional setup. It would be great if the authors could discuss the impact of the $\Theta(\mathbf{x})$. For example, what would the performance be if certain symbolic terms (shown up in the true equations) are missing in the dictionary in $\Theta(\mathbf{x})$.



### Questions
Q1. What is the column of ''STD'' in Figure 2 showing? Are they showing the standard deviation of the estimates? If that is the case, plugging in the standard deviation as the coefficients in the equations are confusing.

Q2. It would be great if the authors could provide more evaluation metrics for generated trajectories. Metrics like Lyapunov exponents would be helpful to see how good the performance is.

Q3. How robust the performance would be across different choice of the dimension of $\mathbf{z}$?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 6

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The author proposed HyperSINDy, a variant of SINDy for discovering stochastic dynamical systems. It employs a variational encoder and a sparsity promoting loss function to recover the underlying equation forms.

### Strengths
Originality: The author proposed a new learning framework by combining the auto-encoder and sparse-promoting loss functions for equation discovery tasks.

Quality: The result for the proposed method is comprehensive and includes various ODE cases. 

Clarity: The figure and equation are well formulated in general. The writing is self-contained to understand

Significance:  The proposed methods integrates sparse equation discovery methods deep generative modeling.

### Weaknesses
The problem setting is confusing and the baseline models are not adequate. Details see the questions part.

1. Problem setting about the stochastic system. As the author mentioned, they used an alternative definition of the stochastic dynamics, e.g random ODE. However, the reviewer is confused by the benefit of such definition compared to the deterministic setting. In result part 4.1, both the mean and the STD of the underlying system are shown. However, the STD form doesn't corresponds to any dynamics and the mean is close the the true mean of the system. In such circumstances, it seems only the mean estimation is important and the std cannot be leveraged to judge the performance of the proposed model. For part 4.2, the STD result is also confusing. It is compared with the diffusion terms but it is totally different from the true diffusion term. Therefore, the reviewer wants to ask why we need to include the STD and how it can help the proposed model.

2. The result needs to compare with more SOTA models and include more comprehensive metrics. There are several model combining learning based method and SINDy-like algorithm for the equation discovery tasks [1][2]. Also, by checking the Figure 2, we could find that the discovery form is different under different $\sigma$. For a equation discovery problem, it is important to get a consistent and correct form. Therefore the reviewer suggests adding more metrics on evaluating if the proposed model can get the correct form, e.g, precision and recall metrics.   
              
[1] Bayesian Spline Learning for Equation Discovery of Nonlinear Dynamics with Quantified Uncertainty. 
       
[2] Physics-informed learning of governing equations from scarce data
  
3. The high dimensional 10d lorenz 96 is not compared with any baselines. Moreover, the analytical form is not listed in the main manuscript. Figure 4's caption says check equation 9 but that's for lorenz 63. Lorenz 96 should like equation 12 but with the concrete forcing terms. Equation 12 indicates that all the coefficients except the forcing terms should be close to 1 or -1. However, the discovered coefficients for $x_i$ is not close to these values. Again, the reviewer doesn't understand what is the gain of reporting the STD form of the equation here.

4. The methodology part is confusing. Figures 2 says $\theta$ has 3 terms but page 8 says $\theta$ has 2 terms. Moreover, in the lower part of Figure 2, $z$ is firstly sampled from $p_{\theta}(z)$ then was fed into decoder $H$. However, the definition of $\theta$ has already included $H$, making the $H$ applied to $z$ 2 times. The term "inference model" is commonly used for test time, but the author use it to indicate training procedure. There are all the confusing parts need to be clarified.

### Questions
1. Problem setting about the stochastic system. As the author mentioned, they used an alternative definition of the stochastic dynamics, e.g random ODE. However, the reviewer is confused by the benefit of such definition compared to the deterministic setting. In result part 4.1, both the mean and the STD of the underlying system are shown. However, the STD form doesn't corresponds to any dynamics and the mean is close the the true mean of the system. In such circumstances, it seems only the mean estimation is important and the std cannot be leveraged to judge the performance of the proposed model. For part 4.2, the STD result is also confusing. It is compared with the diffusion terms but it is totally different from the true diffusion term. Therefore, the reviewer wants to ask why we need to include the STD and how it can help the proposed model. 

2. The result needs to compare with more SOTA models and include more comprehensive metrics. There are several model combining learning based method and SINDy-like algorithm for the equation discovery tasks [1][2]. Also, by checking the Figure 2, we could find that the discovery form is different under different $\sigma$. For a equation discovery problem, it is important to get a consistent and correct form. Therefore the reviewer suggests adding more metrics on evaluating if the proposed model can get the correct form, e.g, precision and recall metrics.   
              
[1] Bayesian Spline Learning for Equation Discovery of Nonlinear Dynamics with Quantified Uncertainty. 
       
[2] Physics-informed learning of governing equations from scarce data
  
3. The high dimensional 10d lorenz 96 is not compared with any baselines. Moreover, the analytical form is not listed in the main manuscript. Figure 4's caption says check equation 9 but that's for lorenz 63. Lorenz 96 should like equation 12 but with the concrete forcing terms. Equation 12 indicates that all the coefficients except the forcing terms should be close to 1 or -1. However, the discovered coefficients for $x_i$ is not close to these values. Again, the reviewer doesn't understand what is the gain of reporting the STD form of the equation here. 

4. The methodology part is confusing. Figures 2 says $\theta$ has 3 terms but page 8 says $\theta$ has 2 terms. Moreover, in the lower part of Figure 2, $z$ is firstly sampled from $p_{\theta}(z)$ then was fed into decoder $H$. However, the definition of $\theta$ has already included $H$, making the $H$ applied to $z$ 2 times. The term "inference model" is commonly used for test time, but the author use it to indicate training procedure. There are all the confusing parts need to be clarified.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
