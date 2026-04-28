# Meta-Learning Nonlinear Dynamical Systems with Deep Kernels

- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 3, 5, 5

## Abstract
Scientific processes are often modelled by sets of differential equations. As datasets grow, individually fitting these models and quantifying their uncertainties becomes a computationally challenging task. In this paper, we focus on improving the scalability of a particular class of stochastic dynamical model, called latent force models. These offer a balance between data-driven and mechanistic inference in dynamical systems, achieved by deriving a kernel function over a low-dimensional latent force. However, exact computation of posterior kernel terms is rarely tractable, requiring approximations for complex scenarios such as nonlinear dynamics. We overcome this issue by posing the problem as meta-learning the class of latent force models corresponding to a set of differential equations. By employing a deep kernel along with a sensible function embedding, we demonstrate the ability to extrapolate from simulations to real experimental datasets. Finally, we show how our model scales compared with other approximations.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper considers the problem of fitting the models of scientific processes (given by sets of differential equations) and quantifying their uncertainty. It is a challenging task, when the datasets are becoming larger. The authors focus particularly on improving the scalability of the less-known class of stochastic dynamical models - latent force models, which operates on kernel functions over a low-dimensional latent force. To overcome the challenging issue of exact computation of a posterior kernel, the paper proposes to rewrite this task into a problem of meta-learning the class of latent force models corresponding to a set of  differential equations. The main idea here is using the known Deep Kernels approach.

### Strengths
The paper has a few significant strengths, which I will outline below:
1. The paper considers the challenging and important problem of modeling complex scientific scenarios given a nonlinear dynamics. This is important not only from the deep learning by also other sciences perspectives.
2. The idea of improving the improving the scalability of the latent force models by incorporating the Deep Kernels approach is reasonable, especially, because the Deep Kernels and GPs enforce strong Bayesian structure.
3. The presented method seems to be faster than the other consider methods.
4. The flow of the manuscript is well-organized.

### Weaknesses
However, despite the strengths, the paper has a few major weaknesses. I will focus especially on the Experiments and Related Works sections.

**Major weaknesses:**

1. The authors place their work within the Meta-Learning field, but they do not compare the proposed model with any other Meta-Learning method. Moreover, the lack of even mentioning the Meta-Learning approaches within the Related Works section. Unfortunately, it is an important issue, because the Meta-Learning field is known from considering many GP-based approaches. To mention just a few: [1], [2], [3], [4], and [5]. I strongly suggest to compare the proposed method with other Meta-Learning approaches. It could also be a good source of new ideas for the future work.
2. If I understand correctly, the authors for each experiments used the same kernel - RBF. However, in the Deep Kernel setting, we can utilize any kernel function we would like - even the scalar product in an embedding space is able to imitate many other kernels. From my perspective, the lack of comparison across various kernels (e.g., family of Matern kernels, spectral or cosine kernel) is another important issue. Even if the RBF kernel would be the best for all of the presented experiments, I would like to see any justification or ablation study proving that.
3. The DKLFM method is compared with only two other methods: DeepLFM and Alfi, from which one is providing the exact solutions. However, taking into consideration the Results in Table 2, we can see that even the DeepLFM is significantly better than DKLFM. I would like to see incorporated DeepLFM into similar comparison as presented in Figure 6.

**Minor weaknesses:**

1. I am not particularly sure if the MSE is the best metric to compare between the solutions. The interesting will be to see how it looks like in different measures, like NLL/ELBO, since it should be available in the GP setting.
2. I am not certain if I understand correctly the comparison between Alfi, DeepLFM and DKLFM. What is the size of datasets on which each result in those tables are computed? If I understand it looks like this: the results for Alfi and DeepLFM are from the set of 20 examples and the results for DKLFM is from the set of 256 examples? Moreover, regarding the computation times if they are averaged across all examples? Please if you could elaborate more on this? If the results for 2 methods are from the smaller set of examples than for the last method, it will not be a fair comparison.

### Questions
I would like to see especially the following experiments and improvements:
1. Comparing with other Meta-Learning methods and placing the DKLFM in a right place in this field (adding needed related works).
2. Please if you could follow the experiment being an ablation study across different kernels for the Deep GPs?
3. Please, compare the DeepLFM with DKLFM in a similar regime to the one presented in Figure 6.
4. Elaborating more on the comparison between Alfi, DeepLFM and DKLFM since the experiment section is not crystal clear.


**Questions:**
1. It will be really helpful if you will be able to add the comparison on other metric like NLL or ELBO.
2. I have a question if in more complex examples the incorporation of the GPs is a good idea? I mean that the GPs are really powerful method, but it has the strong assumptions regarding the Normal distribution, which might reduce the model flexibility in a more complex (e.g., non-gaussian) distributions. It could be a good idea to incorporate the flow-based approaches which are able to map one distribution into another. Or just use the neural ODE. Out of the topic is the question what Alfi use as a particular ODE solver? Maybe it will be able to rewrite this setting into neural ODE.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a method for improving scalability of a particular class of stochastic dynamical model, called latent force models. To this end, the paper proposes a method, deep kernel learning of latent force models, which embeds a data instance into an instance-specific representation, which is later used to infer a hidden representation, on which a Gaussian process operates on. With the GP machinery, hidden representations of unseen input mesh can be inferred and, consequently, output can be inferred. The proposed method is tested on two classes of benchmark problems, ordinary differential equations and partial differential equations.

### Strengths
- The motivation is clear. 

- The mathematical description of the paper is clear. 

- The experimental results seem to provide the proposed model’s efficiency (or presumably the scalability) over the compared baselines.

### Weaknesses
 - The use of terms such as “multi-task modeling” and “meta-learning” may require some careful considerations. The task in the manuscript is defined as each data instance. For example, in the dynamics modeling context, a single task here corresponds to learning a dynamics function (or inferring a parameter as in system identification) from a set of measurement, which is collected from simulating a set of ODEs with a specific parameter. This way of defining “task” may be considered as a non-standard way in “multi-task learning” and, thus, a proper definition would be needed. Relatedly, the use of the terminology “meta-learning”  also seems to require proper justification. Without these, the current method can be seen as a single framework, which is a mixture of parametric and non-parametric ML algorithms, where the parametric part of the framework is being trained on multiple input instances (which are denoted as tasks in the paper) via likelihood maximization with a regular gradient descent algorithm (without specifically learning meta-learned model parameters). 

- The assumption on the availability of the latent force seems to be less practical. As shown in one of the benchmarks (the ODE benchmark), it does seem that latent force needs to be inferred from another software package (Alfi). The paper does not provide much information on how reliable this process is or if there are other alternatives for collecting latent forces (if they are not readily available). Based on this limited information, it is less convincing if the proposed method is practical. A side note is that the software, Alfi, seems to be based on the algorithm, appeared in a preprint, which has not been published; this makes it ever harder to assess the practicality of the proposed method.  

- The description of the experimental section is not very clear. There seem to be two separate ODEs, mRNA and LV. But the descriptions on those two ODEs are mixed together and it’s unclear how the tasks are defined and how the actual experiments have been performed. Moreover, it is unclear if the authors provide all sufficient information on their experiments. 

- An empirical side of the paper is weak. The proposed method has been tested on  relatively simple sets of benchmark problems, which does not seem to provide much insight on the effectiveness of the method or the scalability of the method. It does not seem that there is no place where the scalability of the method is discussed. Finally, the output MSE of the method on the second benchmark problem seems to be very poor.

### Questions
- There are several questions on the weaknesses section.

- In addition to the ones already asked, here are additional questions.

  - The paper discusses the choices of the embedder. Would there be any comparisons between different choices of embedder? What are the specifications of deep kernels that are used in the experiments? Has the authors considered set encoders as well for their purpose? 

  - Can the authors provide more details on the experiments? How the dataset has been created, e.g., uniform sample in the temporal domain, what integrator was used for the mRNA ODE, etc?  

  - How is the latent MSE defined?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Exact Gaussian processes inference has been well known for its heavy computation. This is especially an obstacle to practical use to large data set for latent force models which the latent force is modeled by GPs. This work aims to overcome this issue. The authors proposes latent force models with deep GP kernels and its fast inference algorithm. In meta-learning framework, the task representation vector is concatenated to the input vector as the input of kernel. The proposed method is tested on synthetic dynamical systems and real experimental data.

### Strengths
The proposed method has been shown fast and scalable to large datasets comparing to other methods, which makes more practical use of LFMs. The introduction of task representation vector is to generalize LFM to new tasks. The deep GP kernels grants the model more expressive power.

### Weaknesses
The model formulation needs clarification.
- Missing observation (output) $\mathbf{y}$ likelihood.
- Latent force $\mathbf{f}_n$ and $f$ (likelihood) are the same or not? 
- Better use symbols consistently. The same symbols in GP preliminaries and model formulation with different meanings are confusing.

The figures captions lack description. 

It is unclear how this is and should be in framework of meta-learning. What meta knowledge is learned and used, the task representation? The encoder for task representation is undermotivated.

### Questions
- Why are the latent force observable?
- Why do the observations not exist for test in Fig 4b?
- What do the colors represent in the figures?
- What kind of error bars are used?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper tackles the computational challenges of fitting latent force models to large datasets. These models bridge data-driven and mechanistic inferences but are computationally demanding, especially in nonlinear dynamics. The authors introduce a meta-learning approach using a deep kernel and functional embedding, enabling better extrapolation from simulations to real data. The proposed method's scalability is compared favorably against other approximation techniques.

### Strengths
The method is technically sound, and the problem is theoretically interesting. The use of task representation in meta-learning scheme here is interesting, and the method is novel in providing a numerical solver free approach for dynamical system solving.
The papers popularizes another point of view of dimensionality reduction method that is specific for physical models and makes use of this method to do meta-learning.

### Weaknesses
The paper mainly compares with [1], which is a single task approach, and is slow for using ODE/PDE solvers. The main argument made here is that the proposed approach uses inference to get rid of the numerical solvers, and uses task encoding to broaden to multi-task setting, and so when applied to many tasks at the same time (about 200 as reported in Figure 6), the proposed method will achieve both a quick inference and an accurate one. However, training the proposed model requires an expensive generation of training datasets, which is not required in [1]. I understand that the approach is trying to show task representation is useful in generalizing to fast multi-task setting, but some information on the training cost of the proposed approach compared to that of [1] would be appreciated. 

Besides, the empirical results are mostly focused on very low-dimensional tasks, and are not showcasing the power of LFMs. It would be great to see some high-dimensional experiments.

[1] Jacob D Moss, Felix L Opolka, Bianca Dumitrascu, and Pietro Lio. Approximate latent force model inference. arXiv preprint arXiv:2109.11851, 2021.

### Questions
N/A

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
