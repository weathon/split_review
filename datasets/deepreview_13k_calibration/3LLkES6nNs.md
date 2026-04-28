# Infinitely Deep Residual Networks: Unveiling Wide Neural ODEs as Gaussian Processes

- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 5, 3, 6

## Abstract
While Neural Ordinary Differential Equations (Neural ODEs) have demonstrated practical numerical success, our theoretical understanding of them remains limited. Notably, we still lack convergence results and prediction performance estimates for Neural ODEs trained using gradient-based methods. Inspired by numerical analysis, one might investigate Neural ODEs by studying the limiting behavior of Residual Networks (ResNets) as depth $\ell$ approaches to infinity. However, a significant challenge arises due to the prevalent use of shared parameters in Neural ODEs. Consequently, the corresponding ResNets possess \textit{infinite depth} and \textit{shared weights} across all layers. This characteristic prevents the direct application of methods relying on Stochastic Differential Equations (SDEs) to ResNets.

In this paper, we analyze Neural ODEs using an infinitely deep ResNet with shared weights. Our analysis is rooted in asymptotic analysis from random matrix theory (RMT). Consequently, we establish the Neural Network and Gaussian Process (NNGP) correspondence for Neural ODEs, regardless of whether the parameters are shared. Remarkably, the resulting Gaussian processes (GPs) exhibit distinct behaviors depending on the use of parameter sharing, setting them apart from other neural network architectures such as feed-forward, convolutional, and recurrent networks. Moreover, we prove that, in the presence of these divergent GPs, NNGP kernels are strictly positive definite when non-polynomial activation functions are applied. These findings lay the foundation for exploring the training and generalization of Neural ODEs, paving the way for future research in this domain. Additionally, we furnish an efficient dynamic programming algorithm for calculating the covariance matrix for given input data. Finally, we conduct a series of numerical experiments to support our theoretical findings.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper analyzes infinite-depth residual models (NeuralODEs) and shows that as width converges to infinity, they converge to a Gaussian Process.

### Strengths
The topic of understanding and analyzing infinite-depth and infinite-width models is interesting and timely. The authors analyze NeuralODE, an infinite-depth-limit of a ResNet, and show its relationship, in the infinite-width limit, to a Gaussian Process, with a  difference in the resulting process depending on whether weight matrices are shared across layers or not.

### Weaknesses
The manuscript presents an analysis of infinite-depth residual models (NeuralODEs) and demonstrates their convergence to a Gaussian Process in the infinite-width limit. While the topic is relevant, the work appears to be an incremental addition to a recent analysis of Deep Equilibrium Models (DEQs). The core investigation follows a similar outline, with adjustments to account for residual connections in NeuralODEs (e.g., the summation term $\sum_{i=1}^l z^i$ in Thm. 3.2 eq (8) versus $z^l$ for DEQs) and the possibility of differing weights. The analysis does not offer sufficiently novel insights into infinite-depth models, particularly given the existing literature. The primary distinction highlighted, the difference in the resulting Gaussian process based on whether weight matrices are shared across layers, while technically correct, does not represent a significant conceptual leap beyond what is already understood about the behavior of such models. The conclusions, while mathematically sound, do not provide substantial new understanding of the behavior of infinite-depth models.

### Questions
See Weaknesses section.

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies signal propagation in neural ODEs and their discretizations at initialization. The authors consider both temporally constant weights and temporally independent weights and derive convergence rates for the preactivations for the case where weights are temporally constant. They also derive recursions for the limiting covariance kernels for the two cases of weight tying. These recursions can be solved with a dynamic programming method by simply storing results for previously computed kernels for earlier layers and looking them up to compute later layer correlations. The authors show that temporally shared weights give rise to different kernels than temporally independent weights.

### Strengths
This paper studies an interesting topic of infinite depth residual networks, which has recently begun to receive more attention from theorists. The results appear correct and sensible, especially to someone who is familiar with NNGP/NTK type results for non-residual architectures. The proof techniques appear valid, though I am not an expert in this area of random matrix theory. Further, the authors provide some numerical simulations, demonstrating Gaussianity of preactivations and convergence of covariance kernels to their limit.

### Weaknesses
The primary weakness of this work is that (as far as I can tell) the main result is not as novel as claimed. The ODE model with temporally constant weights focused on in this paper is not a new architecture but is really just a randomly connected recurrent RNN, which has been analyzed by physicists and theoretical neuroscientists for decades. In particular, this is exactly the Cristanti and Sompolinsky model of a RNN (https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.61.259, https://journals.aps.org/pre/abstract/10.1103/PhysRevE.98.062120) without a leak term. Techniques like dynamical mean field theory (DMFT) can be used to calculate the large width limit of these dynamics and would recover identical dynamics for the covariances as the authors provide. Some other relevant papers are Helias & Dahmen book (https://arxiv.org/abs/1901.10416).  There are also prior works which solve the equations without non-stationary assumptions (https://proceedings.neurips.cc/paper_files/paper/2022/file/e6f29fb27bb400f89f5584c175005679-Paper-Conference.pdf).

The authors should make contact with this literature and discuss a comparison with their derived limit and the limit for DMFT for random RNNs.

1. In equation 3, is it clear that beta is always O(1/L) ? I would expect it needs to scale as O(1/sqrt{L}) if the weights are independent across times. If so, this should be stated clearly somewhere. I think this is important because the scaling of beta with T should determine whether one gets the Log-Gaussian result of Li et al (beta ~ O(1) and L ~ N) or the SDE type limit Hayou and Yang beta ~ 1/sqrt{L}. Further the convergence result for preactivations should only hold in the shared weights case with U fixed and for a fixed realization of the weights W.   
2. What is going on in eq 4? Not clear at all how this relates or what assumptions on A make this equation hold.
3. Figure 2: why are the shared weight networks converge to their limit, but the non-shared networks do not converge to their limit? Is there any analysis of finite size error that would predict this? 
4. Figure 3: It is unclear to me if the smallest eigenvalue is the proper metric. Numerical stability of algorithms usually depends on some kind of normalized metric of smallest eigenvalue like condition number which compares largest to smallest eigenvalue. I am wondering if the shared weights has better condition number rather than just larger minimum eigenvalues. 
5. Why do the authors refer to this model as a Neural ODE rather than a RNN? My impression was that weight sharing across layers is what distinguished RNNs from standard feedforward networks.

### Questions
1. In equation 3, is it clear that beta is always O(1/L) ? I would expect it needs to scale as O(1/sqrt{L}) if the weights are independent across times. If so, this should be stated clearly somewhere. I think this is important because the scaling of beta with T should determine whether one gets the Log-Gaussian result of Li et al (beta ~ O(1) and L ~ N) or the SDE type limit Hayou and Yang beta ~ 1/sqrt{L}. Further the convergence result for preactivations should only hold in the shared weights case with U fixed and for a fixed realization of the weights W.   
2. What is going on in eq 4? Not clear at all how this relates or what assumptions on A make this equation hold.
3. Figure 2: why are the shared weight networks converge to their limit, but the non-shared networks do not converge to their limit? Is there any analysis of finite size error that would predict this? 
4. Figure 3: It is unclear to me if the smallest eigenvalue is the proper metric. Numerical stability of algorithms usually depends on some kind of normalized metric of smallest eigenvalue like condition number which compares largest to smallest eigenvalue. I am wondering if the shared weights has better condition number rather than just larger minimum eigenvalues. 
5. Why do the authors refer to this model as a Neural ODE rather than a RNN? My impression was that weight sharing across layers is what distinguished RNNs from standard feedforward networks. 


If the authors could answer these questions and address the discuss the connection to random RNN models, I would consider raising my score.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper uses infinite ResNet to analyze the convergence and prediction performance of wide neural ODEs, where it thinks the Neural ODEs can be regarded as an infinite ResNet.

### Strengths
1. This paper regards the NODE as the infinite deep ResNet, which is interesting.
2. The motivation is meaningful to understand the neural network with the help of the relationship of the ODE and the NN.

### Weaknesses
1. Poor format and logic. e.g."width is infinity.."; in Fig.1, "Distribution of one output neuron: Neural ODE and ResNet w/wo shared weights" does not correspond to its legend "Neural ODE, Shared ResNet, Indep. ResNet".
2. Contribution is poor and is not well supported.


### Questions
1. As I know, not every layer of the standard ResNet has the same number of parameters/channels, so how do we achieve the shared parameter? If you are using a simplified version of ResNet, it should be clarified. 
2. In the first sentence of the second paragraph of the introduction, missing some references to support your presentation. Can you give me some references？
3."we are faced with infinite-depth residual neural networks with shared weights..." Although intuitively, I think this may be right, there still is not enough evidence to support it.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors develop a connection between Gaussian process and autonomous and nonautonomous neural ODE based on random matrix theory. They also show that the kernel of the Gaussian process is strictly positive definite if the input is restricted to the unit sphere. Furthermore, they provide an algorithm for computing th covariance matrix.

### Strengths
The authors analyze neural ODE from the perspective of Gaussian process. They provide the covariace matrix of the Gaussian process. The analysis is benefitial for better understandings of Neural ODE.

### Weaknesses
The paper is sometimes hard to follow. Some assumptions are not clearly stated, for example,
- For Eq. (4), do we need some assumptions regarding $A$? I don't think any square matrix satisfies Eq. (4). Specifically, the equation implies that the expectation of the outer product of $A$ with itself is the identity matrix, which is a strong condition. It is not clear if this is a standard assumption for random matrices in this context, and if not, it needs to be explicitly stated and justified. Furthermore, it is not clear what distribution is assumed for the entries of $A$, and how this distribution affects the validity of the results.
- After Propostion 3.1., the authors say "our ResNet $f_{\theta}^L$ approximates the Neural ODE $f_{\theta}$ effectively in the limit as L approaches infinity". In my understanding, that happens if $T$ is fixed. In that case, as the step size goes to 0, $L$ goes to infinity. If that is correct, please clarify that. The connection between the discrete ResNet and the continuous Neural ODE is not fully clear. The authors should explicitly state the relationship between the number of layers $L$, the time horizon $T$, and the step size $\beta$. The conditions under which the discrete approximation converges to the continuous one should be made more precise.
- In my understanding, to prove Theorem 3.2, we need Lemmas C.1 and C.2, which involves the controllability of the function. The authors say "The convergence is achived under the assumption of a controllable activation function." before Definition 3.1. However, in Theorem 3.2, they do not mention the controllability. Should we assume the activation functions are controllable throughout the paper? In that case, please clarify that. The role of the controllability assumption in the overall argument needs to be clarified. It is not clear if this assumption is necessary for all the results, or only for specific theorems. The authors should clearly state where this assumption is needed and why.

### Questions
Minor comments:
- Equations should be referred with parenthesis (e.g. equation (1)). Use \eqref instead of \ref.
- Some references should also be cited with parenthesis. Use \citep if you need the parenthesis.
- In Lemma C.2, there is an unknown label for an equation.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
