# Unlocking Point Processes through Point Set Diffusion

- Decision: Accept
- Scores: 6, 8, 8, 6

## Abstract
Point processes model the distribution of random point sets in mathematical spaces, such as spatial and temporal domains, with applications in fields like seismology, neuroscience, and economics.
Existing statistical and machine learning models for point processes are predominantly constrained by their reliance on the characteristic intensity function, introducing an inherent trade-off between efficiency and flexibility.
In this paper, we introduce \textsc{Point Set Diffusion}, a diffusion-based latent variable model that can represent arbitrary point processes on general metric spaces without relying on the intensity function.
By directly learning to stochastically interpolate between noise and data point sets, our approach enables efficient, parallel sampling and flexible generation for complex conditional tasks defined on the metric space.
Experiments on synthetic and real-world datasets demonstrate that \textsc{Point Set Diffusion} achieves state-of-the-art performance in unconditional and conditional generation of spatial and spatiotemporal point processes while providing up to orders of magnitude faster sampling than autoregressive baselines.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposes a novel modeling approach to point processes via diffusion on point sets (discrete events), addressing the reliance on the intensity function when establishing or learning the model. It can capture the distribution of point processes and generate a series of events based on noise point sets. Meanwhile, the sampling efficiency of point set diffusion is superior. The overall presentations of both the methodology and experiments are excellent.

### Strengths
The idea of using the diffusion-style model to characterize point processes is super interesting. The content is clear and well-written, making the methodology and the results accessible to the reader. The paper also covers unconditional and conditional sampling methods, which have the potential to correspond to two important questions in the point process modeling (first-order and second-order modeling). The authors also provide thorough experimentation to validate the effectiveness of the proposed model.

### Weaknesses
In my opinion, the main weakness, or the most improvement-needed part of the paper, lies in the modeling and experiments of ordered point processes:

1. An important characteristic of the ordered point processes (TPPs or STPPs) is the dependence between future events and past events, which is not considered in the model. The proposed method seems to only consider the first-order statistics of the data (the event intensity/density), and treat these statistics at certain times or locations as fixed values to be learned by the model. For example, if the training data set contains multiple event trajectories sampled over the horizon of $[0, T]$, then the model will assume $p(T/2)$ (the event density at $T/2$) is fixed and to be learned. However, in TPPs, the $p(T/2)$ depends on the history (observation before $T/2$), and is different in each realization of the event trajectory, which violates the assumption of the diffusion model.

2. Although a conditional sampling method is proposed in the paper (Algorithm 3.1), I am wondering about its effectiveness in practice. First, what the $q(X_{t-1}|X_{0}^{c})$ is (line 287) remains unknown. Meanwhile, the (technical/practical) reason for using this conditioning is not shown. The results in Figure 7 are not convincing enough. To me, even though the authors claim that they are solving conditioning tasks and are visualizing the predicted densities for events from different trajectories (panels at the bottom), these density plots would look similar if we overlap them with each other. In other words, I think the model only predicts an averaged event intensity over space, and it has little connection with the conditioned samples.

3. An alternative to prove the effectiveness of conditional generation is to show the predicted intensity/density of events at different times, given a trajectory from the pinwheel dataset. This is the same idea as Figure 5 in [1]. The difference between density functions at different times is more significant and would help validate the conditional sampling method.

4. The conditional sampling task is only experimented with in the spatial domain. An example of showing the evolution of the predicted conditional density of a pinwheel trajectory can support the claim of effective conditional sampling in an ordered (temporal) domain.

5. I am also concerned that there is no log-likelihood metric reported in the paper. The metrics used in the paper are about the first-order characteristics of the data, on which I believe the proposed Point Set Diffusion can perform well. However, they cannot fully reflect the model's fit to the data when second-order data dependencies are involved (e.g., in ordered point processes). On the other hand, the log-likliehood is still the golden standard to suggest the model's goodness-of-fit to the data when it comes to conditional models or tasks [2][3]. Other point process studies that use the diffusion model will also report the data log-likelihood when evaluating the model [4][5]. I am curious about the proposed model's performance on the log-likelihood metric.

Again, I acknowledge and respect the authors' contribution to the proposed method, and I hope the above questions can be properly answered or addressed.

### Questions
1. In Figure 5, can the authors show the predicted density of different trajectories in the same masked area?

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes a Point Set Diffusion model for conditioned and unconditioned generations of point processes (spatial, temporal, and spacial-temporal) without intensity functions. The model treats the latent space of the point process as a whole and applies diffusion to learn how to generate point processes from noise (unconditioned) and conditioning masks (conditioned). At the training phase, the point process is passed through a forward process that gradually thins the original points and adds points from a noise point process. Then, a parameterized model is trained for the backward process that gradually predicts the points in the last timestep conditioned on the current timestep and thins the noise points in the current point process. After training, both conditioned and unconditioned sampling procedures are provided. Numerical experiments illustrate that the proposed Point Set Diffusion model achieves much faster sampling speed than intensity-based autoregressive models. Moreover, it outperforms several baseline autoregressive models on various SPP and STPP tasks, especially density estimation tasks.

### Strengths
1. The paper is overall well-written and easy to follow. The basic concepts are introduced clearly with consistent notations. The forward process, backward process, and final sampling algorithms are well explained. Illustrations (Figure 1-3) are very clear for readers to follow the workflow of the proposed Point Set Diffusion model. The datasets and metrics are also clear in the experiment section. 

2. The idea of leveraging diffusion models to generate the whole point process is intriguing, and it is quite different from the common approaches that use autoregressive models with parameterized intensity functions that suffer from sampling speed and are restricted to forecasting tasks. Numerical results are very promising to support the efficacy of the proposed model.

### Weaknesses
1. Currently there are very few baseline algorithms, e.g., for SPP conditional generation there is only one baseline, and for STPP forecasting there are only two. It would be more convincing to compare with more baseline models, or to provide more evidence that the current baselines are already SOTA (which I believe they are).

### Questions
1. The sampling time and quality of the diffusion model are directly related to the number of forward/backward steps, which I could not find in the paper. Could the authors provide some ablation study on the number of steps, e.g., how the sampling time and quality grow with it?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a diffusion-based latent variable model for general point processes on metric spaces. By learning stochastic interpolations between data and noise point sets, the model enables efficient, parallel sampling and flexible generation for complex tasks on the metric space. Experiments on synthetic and real-world datasets show that the proposed model achieves state-of-the-art results in unconditional and conditional tasks for spatial and spatio-temporal point processes.

### Strengths
1. This paper generalizes the Add-Thin model to define a model for point processes on general metric spaces, enhancing the model's applicability and promising future prospects.
2. The idea is sound and well-founded. The paper is overall well-written and easy to follow.
3. Experiments show that the proposed model achieves state-of-the-art results on both conditional and unconditional tasks while enabling faster sampling.

### Weaknesses
1. It would be helpful to discuss the connections between the proposed model and the Add-Thin model when modeling univariate temporal point processes. Specifically, a more detailed comparison of the underlying assumptions and mechanisms of each model when applied to the same data would be beneficial. This should include a discussion on how the disentanglement of superposition and thinning in the proposed model affects the learning process compared to the coupled approach in Add-Thin.
2. In the conditional sampling, the definition of $q(X_{t-1} | X_{0}^c)$ in line 287 was not provided. It is unclear how the conditioning mask is applied and how the noise is added to the conditional set. A more detailed explanation of the process, including the specific mathematical operations, is needed to ensure reproducibility and understanding of the conditional sampling mechanism.

Typo: $X_{t+1}^{\text{thin}}$ and $X_{t}^{\text{thin}}$ in Eq.(9) should be $X_{t+1}^{\varepsilon}$ and $X_{t}^{\varepsilon}$.

### Questions
1. In the experiments, how are $\alpha_t$, $\beta_t$, and $T$ set?

2. The proposed model generalizes the Add-Thin model to general metric spaces. When modeling univariate TPPs, how does the performance of the proposed model compare to Add-Thin in both unconditional and conditional sampling scenarios?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a novel diffusion-based approach to model point processes without relying on traditional intensity functions. This model is characterized by its ability to efficiently and flexibly generate point sets through stochastic interpolation between data and noise sets. Experiments on synthetic and real-world datasets demonstrate that the model achieves state-of-the-art performance in generating spatial and spatiotemporal point processes, significantly outperforming existing methods in terms of speed and accuracy of sample generation.

### Strengths
- The approach of modeling point processes using the diffusion model is interesting.
- Efficient sampling is achieved by making effective use of thinning.
- The effectiveness of the proposed method is evaluated on artificial and real data.
- The manuscript is well-written.

### Weaknesses
 - There is not enough discussion about computational complexity. Specifically, the manuscript lacks a detailed analysis of how the runtime scales with the number of points in a set and the dimensionality of the space. The use of attention mechanisms in the encoder could lead to quadratic complexity, which should be addressed.
- Not very clear on how to set hyperparameters. The paper does not provide sufficient guidance on selecting the number of diffusion steps, the noise schedule, or other crucial parameters. The lack of a systematic approach to hyperparameter tuning makes it difficult to reproduce the results or apply the method to new datasets.
- No mention of the effectiveness of the method with respect to the amount of data. The paper does not discuss how the performance of the model is affected by the size of the training dataset. It is unclear whether the model is robust to small datasets or if it requires a large amount of data to achieve good performance. This is a critical aspect for practical applications.
- No discussion of limitation. The paper does not adequately address the limitations of the proposed method. For example, the interpretability of the model is not discussed, and it is unclear how the method compares to parametric approaches in terms of understanding the underlying point process.

### Questions
- Can you add a discussion on learning time? How does the computational complexity increase, especially with more data points?
- How can hyperparameters (e.g. number of diffusion steps T or noise scheduling) be determined?
- Please tell me more about the limitation of the proposed method. For example, how robust is the proposed method in situations where there is little data? Also, will the interpretability of the proposed method be lower than parametric methods (e.g., DNN-based Hawkes processes), or will the number of sensitive hyperparameters increase by using diffusion models as a base?

### Soundness
3

### Presentation
3

### Contribution
3
