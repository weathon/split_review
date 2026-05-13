# NN-ResDMD: Learning Koopman Representations for Complex Dynamics with Spectral Residuals

- Decision: Reject
- Scores: 5, 5, 5, 6

## Abstract
Analyzing long-term behaviors in high-dimensional nonlinear dynamical systems remains a significant challenge. The Koopman operator framework has emerged as a powerful tool to address this issue by providing a globally linear perspective on nonlinear dynamics. However, existing methods for approximating the Koopman operator and its spectral components, particularly in large-scale systems, often lack robust theoretical guarantees.
Residual Dynamic Mode Decomposition (ResDMD) introduces a spectral residual measure to assess the convergence of the estimated Koopman spectrum, which helps filter out spurious spectral components. 
Nevertheless, it depends on pre-computed spectra, thereby inheriting their inaccuracies. 
To overcome its limitations, we introduce the Neural Network-ResDMD (NN-ResDMD), a method that directly estimates Koopman spectral components by minimizing the spectral residual. By leveraging neural networks, NN-ResDMD automatically identifies the optimal basis functions of the Koopman invariant subspace, eliminating the need for manual selection and improving the reliability of the analysis.
Experiments on physical and biological systems demonstrate that NN-ResDMD significantly improves both accuracy and scalability, making it an effective tool for analyzing complex dynamical systems.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
A method for computing the Koopman spectra of dynamical systems is proposed. It stands on two main ingredients: 1) the use of spectral residual as a loss function, and 2) the use of NNs for constructing observables. Its applications to a pendulum, turbulence, and neural dynamics are presented, and the proposed method is shown to be successful in extracting the Koopman spectra and analyzing the data.

### Strengths
- The method is technically reasonable.
- The idea is somewhat new. To my knowledge, using the resDMD objective with neural observables is quite natural but has not been exactly practiced yet.
- The experiments nicely demonstrate the utility of the method.

### Weaknesses
(1) Although the work is solid, I do not think the technical contribution is so significant to be included in the ICLR proceedings. The use of neural observables has been known and practiced well in these 8 years or so, and ResDMD has been already well known and discussed recently. The technical contribution of this work inevitably looks incremental.

(2) The rich literature on the use of NNs as DMD observables, other than Li et al. (2017), seems to be overlooked. For example, even restricting the scope to the mere use of NNs for DMD-based analysis (i.e., excluding more applied perspectives such as control), the following papers (and probably more) should be relevant:

- N. Takeishi, Y. Kawahara, T. Yairi: Learning Koopman invariant subspaces for dynamic mode decomposition, Advances in Neural Information Processing Systems 30, 2017, pp. 1130–1140
- B. Lusch, J. N. Kutz, S. L. Brunton: Deep learning for universal linear embeddings of nonlinear dynamics, Nature Communications, vol. 9, no. 1, p. 4950, 2018
- A. Mardt, L. Pasquali, H. Wu, F. Noé: VAMPnetsfor deep learning of molecular kinetics, Nature Communications, vol. 9, no. 1, p. 5, 2018.
- E. Yeung, S. Kundu, N. Hodas: Learning deep neural network representations for Koopman operators of nonlinear dynamical systems, Proceedings of the 2019 American Control Conference, 2019, pp. 4832–4839
- S. E. Otto, C. W. Rowley: Linearly recurrent autoencoder networks for learning dynamics, SIAM Journal on Applied Dynamical Systems, vol. 18, no. 1, pp. 558–593, 2019
- O. Azencot, N. B. Erichson, V. Lin, M. W. Mahoney: Forecasting sequential data using consistent Koopman autoencoders, Proceedings of the 37th International Conference on Machine Learning, 2020, pp. 475–485
- H. Wu, F. Noé: Variational approach for learning Markov processes from time series data, Journal of Nonlinear Science, vol. 30, no. 1, pp.23–66, 2020
- D. J. Alford-Lago, C. W. Curtis, A. T. Ihler, O. Issan: Deep learning enhanced dynamic mode decomposition, Chaos: An Interdisciplinary Journal of Nonlinear Science, vol. 32, no. 3, p. 033116, 2022
- T. Iwata, Y. Kawahara: Neural dynamic mode decomposition for end-to-end modeling of nonlinear dynamics, Journal of Computational Dynamics, vol. 10, no. 2, pp. 268–280, 2023

I do not think all of them should be included in the reference with detail, but at least the existence of such a rich literature should be mentioned to help readers to better understand the context of the research.

Below are relatively minor technical points that I found unclear.

(3) The authors emphasize the "lack of theoretical guarantee of convergence" of EDMD for several times. In what sense is this "lack" supposed? For example, the work by Korda & Mezić:

- M. Korda & I. Mezić: On convergence of extended dynamic mode decomposition to the Koopman operator, Journal of Nonlinear Science, vol. 28, pp. 687–710, 2018

discusses the convergence in some sense.

(4) The proposed method alternates between the gradient-based update of $\theta$ and the least squares solution to get $K$. Is there any insight of this choice? I am asking this because it is also possible to include the least squares within the gradient computation, as done in Takeishi et al. (2017); Otto & Rowley (2019) listed above for example.

(5) In the experiment, does EDMD-DL follow the exactly same configuration as NN-ResDMD except for the loss function? (it should.) Please elaborate on this more clearly to make it easier to assess the benefit particular to the proposed method.

### Questions
Although there is no specific question that will surely affect my evaluation, some comments if any on the points listed in the Weaknesses section would be highly helpful.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors propose NN-ResDMD, a deep learning-based approach that directly estimates Koopman spectral components by minimizing a spectral residual. This method aims to improve the reliability of approximating Koopman spectra in nonlinear dynamical systems by automatically identifying optimal basis functions for the Koopman invariant subspace. The paper presents experiments on physical and biological systems, demonstrating the method's scalability and accuracy for complex dynamics.

My main comment on this paper is that it lacks sufficient innovation or fails to effectively demonstrate its unique contributions. The use of deep learning to estimate Koopman operators has been explored extensively in prior research. For example:

[1] Lusch, B., Kutz, J. N., & Brunton, S. L. (2018). Deep learning for universal linear embeddings of nonlinear dynamics. Nature Communications, 9, Article 4950.
[2] Mardt, A., Pasquali, L., Wu, H., & Noé, F. (2018). VAMPnets for deep learning of molecular kinetics. Nature Communications, 9, Article 5.
[3] Mardt, A., Pasquali, L., Wu, H., & Noé, F. (2020). Deep learning Markov and Koopman models with physical constraints. Proceedings of Machine Learning Research, 107, 451-475.

The squared relative residual proposed in this paper has similarities to the VAMP-E score explored by Wu and Noé in their work on VAMP [4]. The VAMP score framework has served as a basis for many deep learning models, including VAMPnets [2], state-free reversible VAMPnets and GraphVAMPnets. It would be beneficial for the authors to position their spectral residual measure within this established framework, providing a comparative analysis or highlighting any differences in formulation or performance.

[4] Wu, H., & Noé, F. (2020). Variational approach for learning Markov processes from time series data. Journal of Nonlinear Science, 30, 23-66.

### Strengths
The proposed NN-ResDMD method offers a deep neural network based approach for estimating Koopman spectral components

### Weaknesses
My main comment on this paper is that it lacks sufficient innovation or fails to effectively demonstrate its unique contributions. The use of deep learning to estimate Koopman operators has been explored extensively in prior research. For example:

[1] Lusch, B., Kutz, J. N., & Brunton, S. L. (2018). Deep learning for universal linear embeddings of nonlinear dynamics. Nature Communications, 9, Article 4950.
[2] Mardt, A., Pasquali, L., Wu, H., & Noé, F. (2018). VAMPnets for deep learning of molecular kinetics. Nature Communications, 9, Article 5.
[3] Mardt, A., Pasquali, L., Wu, H., & Noé, F. (2020). Deep learning Markov and Koopman models with physical constraints. Proceedings of Machine Learning Research, 107, 451-475.

The squared relative residual proposed in this paper has similarities to the VAMP-E score explored by Wu and Noé in their work on VAMP [4]. The VAMP score framework has served as a basis for many deep learning models, including VAMPnets [2], state-free reversible VAMPnets and GraphVAMPnets. It would be beneficial for the authors to position their spectral residual measure within this established framework, providing a comparative analysis or highlighting any differences in formulation or performance.

[4] Wu, H., & Noé, F. (2020). Variational approach for learning Markov processes from time series data. Journal of Nonlinear Science, 30, 23-66.

### Questions
(1) How does this method differ from existing deep learning approaches for Koopman operator estimation, and what substantial improvements does it offer in terms of robustness, accuracy, or efficiency?

(2) What are the differences and connections between the proposed loss function in this paper and existing evaluation functions like the VAMP score?

### Soundness
4

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a new method, NN-ResDMD, to estimate the spectral components of Koopman operators. It builds upon Residual Dynamic Mode Decomposition (ResDMD) and uses a neural network to identify basis functions instead of manually selecting them.

### Strengths
- The description and clarity of the proposed approach is good overall.
- The proposed approach is theoretically justified by the guarantees of the ResDMD method it is built upon.
- The clustering results on the neural dynamics experiment are promising.
- The code for the experiments is already available online.

### Weaknesses
 **I do not think this paper makes a sufficiently strong contribution**. My understanding is that the proposed approach is simply ResDMD where the basis functions are parametrized by a neural network instead of specified manually, and then iteratively optimized. In my opinion this paper is better suited as a workshop paper in its current form.

The authors use feedforward neural network but the details of the architecture of the feedforward neural network are not provided. The authors **did not investigate the use and choice of other typically better-performing neural network architectures**. I don't think this should be left as future work but should already have been investigated. Similarly, exploring the direction of integrating the proposed approach with PINNs/PINOs would have made the contribution of the paper stronger, instead of leaving it as future work.

There is **no discussion of the computational cost** of the approach, which could be a big drawback of the proposed approach. As far as I understand it, the single evaluation (or few evaluations) of the eigenpairs in ResDMD is replaced by an iterative process where each iteration requires the evaluation of the eigenpairs in NN-ResDMD. This is an expensive part of the algorithm and there are no guarantees for the number of iterations required, so the running time there could be many times larger than for the classical ResDMD. In addition, there is also the cost of the additional optimization steps which can be very large if the neural networks are also large. Overall, the proposed algorithm seems significantly slower than existing approaches, so a trade-off between accuracy and computational time needs to be very carefully discussed theoretically and empirically.

More generally, the **limitations of the algorithm are not discussed**.

**The results of the experiments are not clear**
- The results of the pendulum experiment are not clear. Need to specify more precisely and explicitly what the ground truth is to understand if these are good/bad results. Why are the results of the NN-ResDMD approach shaded areas while all the other methods are displayed using points? The shaded area also has a large radius, so maybe the results are not as good as stated compared to Hankel-DMD for instance for which the points remain close to the unit circle.
- The results of the turbulence experiments are not clear, since there is no ground truth provided. I am not familiar with that experiment so I do not know what the results are supposed to look like. It is unclear to me why the NN-ResDMD results in Figure 5 are considered good, while those in Figure 7 for Hankel-DMD are considered bad.
- The results of the neural dynamics experiments could be made clearer. Why do you choose a different number of eigenfunctions for the different approaches? Is this a fair comparison? Figure 6.a., 9.a. and 10.a. show the decomposed eigenfunctions for the different approaches. There is no ground truth provided, so it is not clear to me what we learn from these plots.

Given that the proposed approach is compared to Hankel-DMD in all the numerical experiments, it would be worth detailing what that approach actually does compared to the other DMD approaches discussed in the paper. Maybe that was the original aim of Appendix A.5 which has been left empty.

The diagram in Figure 1 needs to be cleaner and more "professional"

Make sure to specify the variables over which the optimization is performed in equations (3.4) and (3.5)

### Questions
A collection of questions and suggestions have been made in the Weaknesses section.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors propose Neural Network-ResDMD (NN-ResDMD), where the dictionary functions are automatically selected by neural networks. The network is trained by minimizeing the loss function that is related to the residual of the eigenvalue problem of the Koopman operator. Numerical results are also illustrated to confirm the behavior of the proposed method.

### Strengths
ResDMD is a powerful tool to observe the spectra of Koopman operators. The authors combine neural networks and ResDMD to make ResDMD more flexible method. The topic is interesting and relevent to the community. The paper is well-organized and easy to follow.

### Weaknesses
The authors insist their proposed method automatically select basis functions, eliminating the need for manual intervention. I understand that in practice, applying neural networks to find proper basis functions is more flexible. However, theoretically, advantages of applying neural networks to estimating Koopman operators and their eigenvalues are not clear for me. They assume there is a basis function $\psi_i$ and construct a neural network that can sufficiently approximate $\psi_i$. Could you clarify what is $\psi_i$? And, what impact on estimating Koopman operators and their eigenvalues is induced by the error of the approximation of $\psi_i$ by using the neural network? Furthermore, while the use of neural networks as universal approximators is well-established, the specific implications for the convergence and stability of the Koopman operator approximation in this context are not rigorously addressed. It's not clear how the approximation error of the neural network translates to the error in the estimated Koopman operator's spectrum, especially in the presence of noisy or limited data. The paper lacks a discussion on the potential for overfitting when using neural networks to learn basis functions, and how this might affect the generalization capability of the learned Koopman operator. The method's sensitivity to the neural network architecture and hyperparameters also remains unclear, which could limit its practical applicability.

### Questions
In Fig. 4, the spectrum of the estiated Koopman operator by NN-ResDMD is distributed on the unit circle. On the other hand, the spectra of the estimated Koopman operators by other methods are distributed also inside the unit circle. Is the dynamical system measure preserving, or did you only focus on the spectra on the unit circle?

Minor comment:  
In line 208, do you mean $(G+\sigma I)^{-1}$ instead of $\dagger$ since $G$ is positive-semi definite?

### Soundness
3

### Presentation
3

### Contribution
2
