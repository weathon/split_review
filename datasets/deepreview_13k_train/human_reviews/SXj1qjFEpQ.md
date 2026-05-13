# Generalizing to New Dynamical Systems via Frequency Domain Adaptation

- Decision: Reject
- Scores: 6, 5, 6, 6

## Abstract
Learning the underlying dynamics from data with deep neural networks has shown remarkable potential in modeling various complex physical dynamics. However, current approaches are constrained in their ability to make reliable predictions in a specific domain and struggle with generalizing to unseen systems that are governed by the same general dynamics but differ in environmental characteristics. In this work, we formulate a parameter-efficient method, FNSDA, that can readily generalize to new dynamics via adaptation in Fourier space. Specifically, FNSDA identifies the shareable dynamics based on the known environments using an automatic partition in Fourier modes and learns to adjust the modes specific for each new environment by conditioning on low-dimensional latent systematic parameters for efficient generalization. We experimentally evaluate FNSDA on representative families of nonlinear dynamics. The results show that FNSDA can achieve superior or competitive generalization performance compared to existing methods with a significantly reduced parameter cost.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work proposes an adaptation to the traditional Fourier neural operator (FNO) to learn on trajectories that follow the same differential equations (with parameters that might change. Trajectories from a single set of parameters is referred to as an environment). 

The core idea is that frequencies define the trajectory observed in an environment.  In that sense, the authors propose to model the relevant frequencies as an additive combination of “common frequencies” and “specific frequencies”. In line with this remark, the authors then propose an environment specific combination of the fourier modes. This provides the authors with a simple framework to test their method on a variety of DE for both in domain prediction and out of domain adaptation. 

The overall algorithm is learned to minimize the prediction error on several time steps and additional penalty on the environment specific variable $c_e$ that conditions the env-specific FNO layer.

### Strengths
Overall, the paper is fairly well written and relevant baselines are selected in the experimental section (which is fairly well conducted). 

It builds up upon FNO paper and  (Kirchmeyer et al). Note that the proposition is conceptually close to the latter, adapting the model in the frequency domain whereas (Kirchmeyer et al) proposes an adaptation directly in the neural network parameters domain.

### Weaknesses
1.  I would have enjoy at least experimental considerations showing the discrepancies in terms of Fourier frequencies in a dynamical when initial conditions or PDE coefficient vary.

2. Note that i believe that this can also be done more theoretically analysing the Fourier modes of some simple equations such as the wave equation. Such a work could be a nice motivation for the proposed approach  

3. What are the main limitation of the work ? Do you know about systems that behave "no continuously" in the frequency domain, e.g. that do not conserve frequencies when varying some condition ?

4. I find Fig.4 difficult to read.

### Questions
Questions:

1. Should not $K$ (eq.5) depend on the environment itself ? Indeed, it seems natural that the splitting in the frequency domain depends on the environment ? 
2. Can the authors provide an intuitive explanation for $W_e$ and $W_s$ ? 
3. Can the authors detail the meaning of penalizing $c_e$ ? What is the influence of the value of $\lambda$ on training ?
4. It would have been nice to compare the data intensiveness of the proposed algorithm. For instance comparing the prediction/adaptation error for selected models with the number of trajectories available during training.

### Soundness
3 good

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
This paper presents a method to improve the generalization of trained DNN model for dynamic systems. The method is based on FNO. The paper presents the network design, theory, and some empirical validation of the proposed method.

### Strengths
The motivation of the proposed method is sound, and the research efforts in this direction can represent significant advancement of DL for dynamic system behavior modeling. The idea presented in the manuscript is novel, but intuitively makes sense. The paper does a good job explaining the ideas. The experimental results do provide some validation on the effectiveness of the proposed method.

### Weaknesses
The narrative of the paper can be further improved. The experimental results also can be further improved by more comprehensive test cases. See the questions section for more details.

My biggest question is the meaning of `environment` in the context. For an ODE, one would need the model coefficients and the initial conditions (IC). For a PDE, one would have to add the boundary conditions (BC). Since the method is built on FNO, which should be effective to cover different ICs. The main text didn't explain this part well. Based on my reading of the supplemental material, seems by `environment`, the authors mean model coefficients of different values.

Following up to the previous point, a better narrative is to use uncertainties: `aleatoric` and `epistemic`.

Two of the experiments are ODEs, which are not the strong points of FNOs. I would like to see more experiments on various types of PDEs

From supplemental materials, the `deviations` from the model coefficients used for training and to adaptation seem to nicely covered. One example is the Glycolitic oscilators, the training $k_1 \in \{100, 90, 80\}$, and the evaluation of $k_1$ is bracket value of $85$ and $95$.  What happens when $k_1$ values chosen far away from the training interval, e.g., $125$. Some ablation study to show when the method will fail can actually give the readers a better understanding of the proposed method. 

For NS example, what are the equivalent Reynolds number in different training and evaluation settings?

### Questions
1. My biggest question is the meaning of `environment` in the context. For an ODE, one would need the model coefficients and the initial conditions (IC). For a PDE, one would have to add the boundary conditions (BC). Since the method is built on FNO, which should be effective to cover different ICs. The main text didn't explain this part well. Based on my reading of the supplemental material, seems by `environment`, the authors mean model coefficients of different values. 

2. Following up to the previous point, a better narrative is to use uncertainties: `aleatoric` and `epistemic`. 

3. Two of the experiments are ODEs, which are not the strong points of FNOs. I would like to see more experiments on various types of PDEs

4. From supplemental materials, the `deviations` from the model coefficients used for training and to adaptation seem to nicely covered. One example is the Glycolitic oscilators, the training $k_1 \in \{100, 90, 80\}$, and the evaluation of $k_1$ is bracket value of $85$ and $95$.  What happens when $k_1$ values chosen far away from the training interval, e.g., $125$. Some ablation study to show when the method will fail can actually give the readers a better understanding of the proposed method. 

5. For NS example, what are the equivalent Reynolds number in different training and evaluation settings?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper tackles the generalization to new physical systems of DL architectures. The architecture consists of a modified version of a Fourier Neural Operator (FNO). Adaptation is performed in the frequency domain with a parameter $c_e$ and in the projected space with the parameter $\beta_e$ of the Swish activation function, which changes for each layer. In the frequency domain, frequencies are decomposed into two components that are added, a constant one across environments and an environment-specific one. The constant component consists of the multiplication of the Fourier transform with two learned matrices, $R_s^{(l)}$ and $(1-K)$ and the environment-specific one consists of the same multiplication with two matrices, $W_{env}^{(l)} c_e$ and $K$. The filter $K$ then acts as a selection of the different frequencies that are split into the two groups. The loss is an integral of a MSE over the temporal domain, thus needing numerical solvers to compute it. Adaptation is performed by updating only $c_e$ and $(\beta_e^{(l)})_l$ once the model is trained. The architecture is then tested on two settings, a one-shot adaptation and an unseen future prediction, using four different datasets.

### Strengths
- Interesting to perform adaptation mostly in the frequency domain.
- The method seems to be well-trained and details on the influence of the different training improvements are presented.
- Quantitative results are promising.

### Weaknesses
 - The modification of the original FNO architecture is not very important.
- There is no qualitative results presented (except Figure 1 which is not really commented). This is then hard to really capture if the model is able to generalize well.
- It would be interesting to see the adaptation of the method with an increasing number of trajectories to adapt from. Currently, only-one shot adaptation is performed.
- Adaptation is performed by updating $c_e$, it would be important to have an ablation study on the influence of the dimension of $c_e$ on the performances.
- An interesting ablation study would be to make the $\beta_e$ of the Swish activation function a constant. Indeed, in the current architecture, the adaptation is not completely done in the frequency domain, thus it is hard to understand the influence of this adaptation. A follow-up minor concern would be that only updating $\beta_e$ at adaptation would lead to similar results to the current architecture.
- This is minor but the ordinate of Figure 4 c) and d) should be in log-scale, it is impossible to distinguish the middle and end of the training curve.

### Questions
- Have you studied the influence of the number of modes of the architecture for the different datasets? 
- Why did you chose Euler solver to compute the loss for the NS dataset and RK4 for the other datasets?
- How did you chose $T_{ad}$ and $T$ for the extra-trajectory adaptation? It seems to depend on the discretization which is coherent, but I wonder how would changing $T_{ad}$ and $T$ would change the results. Have you tried with different values?
- Have you compared the adaptation times of the different methods?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper addresses the generalization of neural surrogates of physics systems in forecasting heterogeneous dynamics. A novel method is proposed that 1) features on the frequency domain are used to generalize to unseen dynamics and 2) strategies such as separating commonalities and discrepancies among environments and swish activation are used in training the model. Empirical results show improved forecasting performance.

### Strengths
- The problem of adapting neural forecasting models on heterogeneous dynamics is important.
- Empirical results are obtained by comparison with benchmarks and tested on the chosen datasets.

### Weaknesses
 - In Section 1 the author mentioned the limitations of meta-learning that they require updating a large number of parameters. This is true in optimization-based meta-learning, but not always true in other settings such as feed-forward-based meta-learning and metric-based meta-learning.
- The methodology is confusing. First, although the related work demonstrates the benefit of the Fourier transform in computation, the benefit of Fourier transform vs traditional methods such as recurrent neural networks and neural ODE-based methods in adaptation is missing. Second, the inconsistency of notations in paragraphs and figures makes it difficult to understand. 
- The details of comparison baseline models need to be provided. No visual comparison of the prediction and the ground truths in experiments and ablation studies. The ablation study could be more complete.

### Questions
- The methodology is incremental based on CoDA (weights separated into environment-specific and environment-invariant parts) and using frequency domain features. The experimental results also show that CoDA has compatible performance with the proposed method on some of the datasets in both inter- and extra-trajectory adaptation. It would be more convincing if the authors add an ablation study on either using the frequency domain on CoDA or using features on temporal domains in the proposed method.
- Could the author address the comparison with feed-forward-based meta-learning? Feed-forward-based meta-learning does not require optimizing a large number of parameters and extra adaptation steps on test environments. It would be nice to mention this type of work, such as https://openreview.net/pdf?id=7C9aRX2nBf2, as related work.
- There is confusion in Fig 2 and Eq 4: if z^{(l)} is a time instant u(t) as described in Fig 2, what is the benefit of using the Fourier transform and inverse Fourier transform in comparison with traditional convolutional neural networks?
- Could the author explain the notations in methodology? For instance, what is F_e? What is the dimension of z^{(l)}? What are the dimension of W_{env}^{(l)}, f^e in Eq 8?
- Why is the ERM-adp worse than ERM in both settings? How is the adaptation performed on the model? Could the author provide more details of training the baseline models?
- The improvement by partition seems not significant compared to using all Fourier modes as shown in Fig 3. Is it specific to the dataset or a universal phenomenon among all datasets?
- The swish activation with the cosine annealing scheduler contributed significantly to the improvement of the performance. It would be fair to compare the results if all other baseline models were trained with the same activation function and scheduler.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
