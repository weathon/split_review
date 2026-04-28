# Accelerating Neural ODEs: A Variational Formulation-based Approach

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 8, 6, 6

## Abstract
Neural Ordinary Differential Equations (Neural ODEs or NODEs) excel at modeling continuous dynamical systems from observational data, especially when the data is irregularly sampled. However, existing training methods predominantly rely on numerical ODE solvers, which are time-consuming and prone to accumulating numerical errors over time due to autoregression. In this work, we propose the VF-NODE, a novel approach based on the variational formulation (VF) to accelerate the training of NODEs. Unlike existing training methods, the proposed VF-NODEs implement a series of global integrals, thus evaluating Deep Neural Network (DNN)--based vector fields only at specific observed data points. This strategy drastically reduces the number of function evaluations (NFEs). Moreover, our method eliminates the use of autoregression, thereby reducing error accumulations for modeling dynamical systems. Nevertheless, the VF loss introduces oscillatory terms into the integrals when using the Fourier basis. We incorporate Filon's method to address this issue. To further enhance the performance for noisy and incomplete data, we employ the natural cubic spline regression to estimate a closed-form approximation. We provide a fundamental analysis of how our approach minimizes computational costs. Extensive experiments demonstrate that our approach accelerates NODE training by 10 to 1000 times compared to existing NODE-based methods, while achieving higher or comparable accuracy in dynamical systems. The source code will be publicly available upon publication.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors present a new method for training Neural ODEs (NODEs) based on a variational formulation of an ODE loss. The resulting method used spline regression and to interpolate noisy data which allows for a computation of a variational loss. The advantage of the method is many few function evaluations during training.

### Strengths
The strengths of the paper are:
- the proposed method introduces a reasonable approach to training a NODE based on a variational formulation of the loss
- The training method requires many fewer function evaluations, allowing for much faster training than existing methods.
- The method maintains or at times outperms competing methods in terms of accuracy.

### Weaknesses
The weaknesses of the paper are:
- Many of the examples seem somewhat toy. It is unclear how the method might extend to much noisier / less structured ODEs with more complex dynamics. In particular one would expect the  spline regression / interpolation to eventually fail on very long, non-smooth or noisy trajectories. From the paper it is difficult to get a sense of how much these attributes are present in the given benchmarks.
- Implementation of the method is not straightforward from a practitioner's point of view.
- The method introduces a number of hyper parameters required for accurate interpolation which must be chosen/tuned.
- The benefit of reduced training, while convenient, is not broadly important for many of the problems considered.

### Questions
In the COVID-19 dataset example is the data gathered from real world observations? Or is the data generated from some parametric model of COVID-19 spread?

Do the authors have a sense of the limits of the spline regression / interpolation? On what sorts of trajectories it might fail? 

It would be very helpful if the authors could provide plots of training trajectories the ODEs in consideration so the reader could assess the noise levels / complexity of the trajectories.

### Soundness
3

### Presentation
3

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
This paper proposes a new way to train NeuralODEs that is faster than current approaches. Current training strategies require numerically solving the differential equation which is very computationally expensive due to the high number of function evaluations at each time step. The approach introduced here relies on the variational formulation as a surrogate objective. However, the variational formulation still requires the value of the vector field and underlying time series at each time step, so the authors approximate this with cubic splines. To compute oscillatory integrals, the authors incorporate the Filon method. Finally, the authors demonstrate the performance of their method and show impressive computational time gains. Some prediction performance gains are also observed, due to the non-accumulation of errors in their training approach.

### Strengths
Speeding up the training of neural ODE methods is a very important challenge with potentially high impact. 

The method proposed shows clear computational time improvements as well as some prediction performance gains. 

The method makes sense, and the paper is well written and easy to read.

### Weaknesses
One significant weakness that I see with this approach is that it requires defining the trajectories of the time series a priori (here with cubic splines). As such, the model with learn a vector field that agrees with the cubic spline interpolation and will not figure out alternative dynamics. If this is correct, this is a signicant limitation as one important application of NeuralODEs is for data imputation. I would like the authors to discuss that limitation more clearly in the paper and/or to argue against the reasoning above. 

Given that you use cubic splines to interpolate the dynamics (and vector field), another baseline can now be considered. That is, you can now use the same cubic spline acceleration to directly integrate Equation 1 and compute the MSE at the observation points. Is such an approach reasonable ? This should be considered as an additional baseline, that doesn't use the variational approach but the cubic spline interpolation.

4.2 Step 4, the fact of interpolating the vector field using the values only at the observation points seems strange to me as the interpolation will not coincide between observations. That is, between observations, with $\hat{f}$ the interpolation of the vector field:
$ \hat{f}(t) \neq f(\hat{x}(t))$. Can the authors give more details about this discrepancy and motivate why it makes sense ? 

During training, your method requires computing cubic splines coefficients for each time series every time (at least for the $b$ coefficients). Can the author elaborate on the compuational cost of such a procedure ? I would also like the authors to explain how the gradient with respect to $\theta$ can still flow from the computation of the $b$ coefficients - how is this end-to-end differentiable ?

### Questions
As stated above, I would like the authors to discuss the limitations of using an explicit interpolation of the dynamics before training.

4.2 Step 4, the fact of interpolating the vector field using the values only at the observation points seems strange to me as the interpolation will not coincide between observations. That is, between observations, with $\hat{f}$ the interpolation of the vector field:
$ \hat{f}(t) \neq f(\hat{x}(t))$. Can the authors give more details about this discrepancy and motivate why it makes sense ? 

During training, your method requires computing cubic splines coefficients for each time series every time (at least for the $b$ coefficients). Can the author elaborate on the compuational cost of such a procedure ? I would also like the authors to explain how the gradient with respect to $\theta$ can still flow from the computation of the $b$ coefficients - how is this end-to-end differentiable ?

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
3

### Summary
This paper introduces VF-NODE, a new method for accelerating the training of Neural ODEs by using a variational formulation that evaluates vector fields only at observed data points, reducing function evaluations (NFEs) and eliminating autoregression, thereby minimizing error accumulation. The approach integrates Filon’s method to handle oscillations in the loss function and uses natural cubic spline regression to manage noisy or incomplete data. Experiments show VF-NODE is 10x to 1000x faster than traditional methods while maintaining or improving accuracy.

### Strengths
This paper introduces a novel approach using variational formulation (VF) to greatly accelerate Neural ODE training, reducing function evaluations and improving accuracy. By integrating Filon's method with cubic spline regression for handling oscillatory integrals, the method achieves 10x to 1000x faster training across various dynamical systems with higher or competitive accuracy, demonstrating originality, technical rigor, and real-world applicability.

### Weaknesses
The author accelerates the training of the original NODEs method by adopting the VF-NODEs approach. However, the necessity and rationality of transforming the training problem into the optimization problem of Equation 6 still require further elaboration.  See Questions for details.

### Questions
1. The author utilized natural spline interpolation to fit the orbit **$x$** as well as the vector field $f_\theta$ in this process. Then, why not directly adopt the strategy of gradient flow matching for training (see literature [1]). This approach seems more straightforward and bypasses the high computational costs associated with traditional numerical integration.

2. As the author did not present the trajectory plots in experiments, I am concerned about the performance boundaries of this method in handling time series data. Is this method only effective on data with simple behaviors, or can it still outperform traditional NODE methods for more complex systems (such as chaotic systems) ?

3. When using natural spline interpolation, is there an overfitting issue, such as the Runge phenomenon?

4. This method directly inputs the data from the original system, thus it cannot train through modeling latent variables (like latent ODE method), which may result in a loss of the method's flexibility.

[1] Li X, Zhang J, Zhu Q, et al. From Fourier to Neural ODEs: Flow matching for modeling complex systems[J]. arXiv preprint arXiv:2405.11542, 2024.

If the authors can answer the above questions well, I would be happy to consider raising the score.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
**Edit:** I have increased my score and confidence following the author responses.


This paper proposes a new method for speeding up the training of Neural ODEs. The method removes the need for an ODE solve during the forward and backward pass of a Neural ODE.

The theory behind the approach is to rewrite integration by parts:

$\int_0^T x\dot{\phi} dt = [x\phi]_{0}^{T} - \int_0^T \dot{x}\phi dt$ 

If $\phi(0)=0$ and $\phi(T)=0$, then $\int_0^T x\dot{\phi} dt + \int_0^T \dot{x}\phi dt = 0$.

The aim is to approximate $\dot{x}$ using a neural network $f_\theta(x, t)$. And so rather than solving the ODE for $f_\theta$ and applying MSE on the observations, the method attempts to minimise $\int_0^T x\dot{\phi_l} dt + \int_0^T f_\theta \phi_l dt$, for a set of orthonormal basis function $\phi_l$ that are zero at the boundaries of the solve.

A fourier basis is used as a natural choice for $\phi_l$, and cubic splines are used to approximate $x(t)$ in the integrals to give them analytical solutions.

Experiments demonstrate good performance measured by MSE, and a speed up in training time.

### Strengths
- The writing is strong
- The solution is novel and interesting, it's particularly interesting to see an approach which does not solve the ODE in the forward pass
- The theory behind the method is strong
- The experiments demonstrate good MSE
- The ablations on the basis functions demonstrate using a Fourier basis is a good choice

### Weaknesses
 - I found the evaluation confusing. As far as I can tell the only place where any wall clock timing is carried out is in Figure 2, on one dataset, the glycolytic model. All other tables seem to be about MSE. However, the main claims and messages of the paper are about accelerating neural ODEs. If the main claim is that this approach speeds up training then this should be shown more across all datasets. Are these numbers available, have I missed them?
- Figure 2 shows no uncertainties on the time taken to train.
- There is an error in line 137-138. If there is regularisation applied during training, the training time can also be reduced, since later iterations are made faster after regularisation is applied in earlier iterations of training.
- Following on from this, the experiments would be made more convincing by testing some of these regularisation methods. For example minimising higher order derivatives. Currently the main baselines for speed are discretise-then-optimise, optimise-then-discretise and Seminorms, of which only Seminorms claim to speed up Neural ODEs. This point would not be as relevant if the main claims of the paper are about MSE rather than time to train.
- It is not clear what ODE solver is used in the experiments, if adaptive solvers are used it is harder to make the argument that the forward solve is slow. The proposed method is linear in the number of observed points (to do cubic interpolation), however if there are many observed points this method will be slower compared to an adaptive solver if the trajectories are quite smooth. Have adaptive solvers been tested? The reverse is also true, if the dynamics are complex an adaptive solver can take smaller steps whereas the proposed method might suffer from accuracy issues as identified in the paper.

### Questions
- Is it possible to include two papers in the related work: 1) STEER: Simple Temporal Regularization For Neural
ODEs and 2) Interpolation Technique to Speed Up Gradients Propagation in Neural ODEs?

### Soundness
3

### Presentation
4

### Contribution
3
