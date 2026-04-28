# Pseudo Physics-Informed Neural Operators

- Decision: Reject
- Avg Score: 4.33
- Scores: 3, 6, 3, 5, 6, 3

## Abstract
Recent advancements in operator learning are transforming the landscape of computational physics and engineering, especially alongside the rapidly evolving field of physics-informed machine learning. The convergence of these areas offers
exciting opportunities for innovative research and applications. However, merging
these two realms often demands deep expertise and explicit knowledge of physical systems, which may be challenging or even impractical in relatively complex applications. To address this limitation, we propose a novel framework: Pseudo
Physics-Informed Neural Operator (PPI-NO). In this framework, we construct a
surrogate physics system for the target system using partial differential equations
(PDEs) derived from simple, rudimentary physics knowledge, such as basic differential operators. We then couple the surrogate system with the neural operator model, utilizing an alternating update and learning process to iteratively enhance
the model’s predictive power. While the physics derived via PPI-NO may not mirror the ground-truth underlying physical laws — hence the term “pseudo physics” — this approach significantly enhances the accuracy of current operator learning
models, particularly in data scarce scenarios. Through extensive evaluations across
five benchmark operator learning tasks and an application in fatigue modeling,
PPI-NO consistently outperforms competing methods by a significant margin. The
success of PPI-NO may introduce a new paradigm in physics-informed machine
learning, one that requires minimal physics knowledge and opens the door to
broader applications in data-driven physics learning and simulations.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This work attempts to provide regularization to deep operator network training by adding a "pseudo-physics" component when there is no knowledge of the PDE to inform training. A comprehensive experimental study with ablation is provided.

### Strengths
This is a method that attempts to provide physics regularization to the training of deep operator networks, which are usually trained only from data.

A comprehensive ablation study is provided.

### Weaknesses
This is a bootstrapping approach where one attempts to learn the physics and then use it to improve training of the operator network over a data-drive baseline. It is not clear how the pseudo-physics constraint helps achieve a better solution. This could happen simply by additional training of the operator network. There is no firm rationale for how this should work.

No comparison is made with the physics-informed neural operator using the correct physics. The authors' method should give a solution with accuracy between the data-driven and the physics-informed cases, but we do not know how much improvement is made unless we can see what the accuracy of the fully physics-informed operator network is.

There is some incorrect terminology (see Questions) and incorrect technical statements. For example, in Section 3.1, the authors state that the PDE solution can be obtained through integration of Green's function, but this is only true for linear PDEs.

The authors assess the additional number of parameters in their model, which is small, but nothing is said about the additional training and inference time incurred. The latter is important because there is a lot of iterative training and refinement in the proposed method.

### Questions
The approach to learn the physics resembles that in Section IV-B of Zhang et al. "Deep Learning and Symbolic Regression for
Discovering Parametric Equations". The authors should give that reference and compare their approach to theirs.

Why do the authors use the acronym "DONet" for "DeepONet"? The latter is the term widely used in the literature.

On page 2, the discretized versions of u and f aren't "collocation points". That refers to points where a PDE residual is minimized.

Still page 2, the efficiency of FNO does not reside in performing the convolution in the frequency domain, per se, but in learning the parameters in the frequency domain.

On page 3, it's not clear what the authors mean by having more data by decomposing the 128x128 input in 16,384 points. This is still the same amount of data.

On page 4, the authors say that the convolution layer is used to compensate for errors in the discretization of the derivatives. How?

### Soundness
2

### Presentation
3

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
Paper introduces pseudo physics-informed Neural operators tailored for complex scenarios where physics is not fully known and data is sparse. It presents a new data-efficient approach to train neural operators via incorporating a pseudo physics-informed module which maps the solution u and its derivative to the source function f using a limited (u, f) pairs. The learned mapping is then used iteratively as part of training a data-driven neural operator. The paper tested the performance of the proposed model against two baselines, namely, FNO and DeepONet across a range of benchmarks and a real-world application. The method is shown to enhance the accuracy of neural operators particularly with limited data.

### Strengths
Paper is systematically written and easy to read. The idea presented is quite interesting, novel and an important one given the issue of lack of data and partially known physics one often encounters in real world applications. 

The proposed model seems to notably improve the baseline models performance in limited data regimes despite marginally increasing the training time. The results presented sufficiently support the claims made by the authors. 

The effectiveness of the proposed model was assessed in a real-world context scenario in fatigue modeling where no comprehensive PDE exists to fully describe the system. With the use of the pseduo-PI approach and sparse data, the proposed model is able to achieve accurate performance.

The author have ensured to highlight the limitations of the proposed models (e.g., being opaque and non-interpretable, and not applicable to input functions) which is appreciated.

### Weaknesses
The framework cannot be used for learning the mapping from the initial condition to the solution and the examples provided are mainly limited to mapping the source function to the solution. 

It will help if the training procedure is described step by step, with one of the examples used in the results. 

Citing and differentiating your work from this paper is recommended - https://www.sciencedirect.com/science/article/abs/pii/S0021999120307166

### Questions
Is it possible to use other operators (apart from differentiation) in the initial physics learning? For example, introducing operators such as sines, cosines or other complex ones? How about utilizing some concepts from this paper - https://arxiv.org/abs/2207.06240?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors propose the Pseudo Physics-Informed Neural Operator (PPI-NO), which couples the existing concepts of physics discovery and neural operator learning. In particular, a surrogate partial differential equation (PDE) representation is learned from data using a neural network. Afterwards, the neural-network-PDE model is used as a regularizer to refine the training of the neural operator. The authors claim that the coupling helps the neural operator learn effectively in the low data limit.

### Strengths
The paper is written clearly and has appropriate results to support the authors' claim. Further, the paper proposes the integration of the non-trivial concepts of physics discovery and neural operator learning, which is an important problem.

### Weaknesses
1.The idea of coupling physics discovery with NN has been explored earlier. For e.g., see PINN-SR [1].

2. The basic idea of the manuscript is problematic. The discovered "pseudo" physics is not exact and hence is of much lower-fidelity (and is unlikely to generalize). The data available is of higher fidelity. Therefore a composite loss function where one term is of higher fidelity and the other is of lower fidelity will, in theory, stop the model from generalization. This fact has been previously pointed on in [2] and as a remedy transfer learning was proposed. The lower-fidelity physics, learned from limited data, may introduce biases that hinder the model's ability to learn the true underlying physics from the high-fidelity data, especially in regions where the pseudo-physics is inaccurate.

3. Even by incorporating rudimentary physics information, a significant decrease in error is not observed in Table 1 (which is not totally unexpected given the point above). In the results of the DONet-Darcy flow, DONet-Diffusion, and all Poisson and advection equations, the reduction in error is minimal, which makes the contribution of the discovered physics marginal. The error reduction is inconsistent across different training data sizes, further suggesting that the learned pseudo-physics may not be robust or beneficial in all scenarios.

4. Like any other basis function-based physics-discovery algorithms, this framework also requires careful selection of the derivatives, which limits the proposed framework's applicability. It is evident in Table 1. Even when the training data is increased, the relative error increases instead of decreasing in some cases. This may be due to faulty physics identification. I will also add that since the exact terms are not known, using a L2 loss in generally not preferred (as with L2 error, even those terms that are supposed to be absent will have non-zero weights). This contributes to the error in equation discovery and hence, the accuracy of the overall method. The lack of a systematic approach for selecting the derivatives and the use of L2 loss for equation discovery are significant limitations.

5. Important aspects like the effect of incorporating physics on the zero-shot prediction on super- and sub-resolutions, as well as generalization to out-of-distribution input, have not been studied. These are required to gauge the strength of the proposed framework correctly. The absence of these analyses makes it difficult to assess the true generalization capabilities of the proposed method.

### Questions
1. l083. You define f(x) as the source function. I believe neural operators go beyond simply source functions to solution mapping.
2. l087. \mathbb{F} and \mathbb{U} are not defined.
3. l147. How order of derivatives should be chosen?
4. Eq. (5). Why generate N' samples in the second term? Instead, why can we not use the available N samples from the first term?
5. In section 4, important literature in this area are missing. For example, SNO [1], CNO [2], LNO [3], and PIWNO [4] are not reviewed.
6. l301. Why are the same derivatives not used across all the examples? How are they chosen?
7. l302. For the SIF example, why are polynomials of the derivatives not used? 
8. l311. What do the iterations denote?
9. l317. For the SIF example, 400-600 training samples are used. Obtaining such a training set using high-fidelity crack simulations is very costly. This completely defeats the purpose of the proposed framework.
10. Table 1. Why does the error in DONet-Darcy, DONet-Poisson, and DONet-Advection examples increase with the increase in training data?
11. In Table 2. The decrease in error in the case of PPI-NO is very marginal. This indicates that the incorporation of rudimentary physics is ineffective in complex problems like the SIF prediction. 
12. l413. Should the baseline comparison be moved to an ablation study in the given setup? Otherwise, the comparison for physics accuracy should be made with dedicated physics discovery algorithms like PINN-SR [5].


[1] Fanaskov, Vladimir Sergeevich, and Ivan V. Oseledets. "Spectral neural operators." Doklady Mathematics. Vol. 108. No. Suppl 2. Moscow: Pleiades Publishing, 2023.

[2] Raonic, Bogdan, et al. "Convolutional neural operators for robust and accurate learning of PDEs." Advances in Neural Information Processing Systems 36 (2024).

[3] Cao, Qianying, Somdatta Goswami, and George Em Karniadakis. "Laplace neural operator for solving differential equations." Nature Machine Intelligence 6.6 (2024): 631-640.

[4] Navaneeth, N., Tapas Tripura, and Souvik Chakraborty. "Physics informed WNO." Computer Methods in Applied Mechanics and Engineering 418 (2024): 116546.

[5] Chen, Zhao, Yang Liu, and Hao Sun. "Physics-informed learning of governing equations from scarce data." Nature communications 12.1 (2021): 6136.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In complex systems with minimal information of the underlying physics, it is difficult to model physics based losses. To overcome this issue, the authors propose a surrogate model that learns the inverse mapping between the solution at discrete points, its derivatives and the source term at the corresponding discrete points. This model effectively serves as the “teacher model” for a neural operator framework that learns the solution from the source term. The derivatives of the solution are computed based on numerical differences. It is pseudo physics informed because the operator is trained using the surrogate model rather than loss functions and residuals defined over the actual PDE.

### Strengths
Originality: The use of the inverse model as the ground truth in cases where the data is sparse and the governing PDE is unknown is quite promising because in a lot of applied settings, it is not always the case that a governing PDE is known. 

Quality: The intuition of the paper is quite clear. There are thorough experiments on standard benchmark datasets. The authors perform several ablations to substantiate their claims. The figures clearly indicate the message the authors are trying to convey. 

Significance: This is a novel idea that builds upon the Physics-informed ML literature, combining inverse-PDE estimates into the learning pipeline as an alternative to physics based residuals and losses.

### Weaknesses
They use the neighborhood information captured within the convolution layers as a way to compensate for errors in numerical differences. A graph neural operator would be both discretization agnostic and would be better for capturing neighborhood information. 

The training dataset seems quite low. It is not clear whether 5 examples indicate 5 instances of the same PDE with different co-efficients or whether it’s 5 different sparse representations, with the same co-efficients. 

The property of neural operator is that it’s discretization agnostic. The authors don’t mention what discretizations they tested. 128x128 grid is not indicative of the discretization, but rather the resolution. By this I mean that this setting could be a set of densely located 128x128 points in a very small area within a large mesh or a set of 128x128 sparse points spread over the entire mesh. 

While comparing against data driven FNO models is a good baseline, the authors propose this architecture as a substitute for Physics informed ML. Therefore, it would be appropriate to show how this scales against PINNs and PINOs. 

In the FNO paper, the models were trained on training sets with 1000 instances. However, the authors here use a significantly smaller training dataset. Could it be possible that the failure scenarios shown in Figure 3. are because the FNO models require a larger training set to converge? Perhaps a more fair comparison would be to train both the FNO model and the PPI-FNO model on the larger dataset. 
It seems unreasonable to think that a system is so sparse that the training dataset only has 5 instances. Moreover, it is not clear whether sparsity refers to the size of the training dataset or the number of points within the mesh (sparse discretization).

Based on the responses provided by the authors, I'm not convinced that the experiments performed substantiate the theoretical claims. While I find the paper interesting and the authors have conducted thorough experiments, I think the experiments may have used inadequate settings. Furthermore, I find the authors' answers to questions by the other reviewers unconvincing. I will not change my score. 

I would like to provide actionable feedback regarding the experiments section:

1. Prove that the model outperforms FNO, GNOT, DINo, IPOT etc. in all reasonable settings - This backs the theoretical claims in the earlier sections
2. Prove that the model generalizes well to sparse training data - This provides evidence of improved efficiency compared to SOTA models. (The authors have already attempted to do this in the paper, but it would help to include newer SOTA models)

### Questions
1.	When the source terms and the boundary conditions are known, the PDEs can be estimated using Monte-Carlo Walk-on-Spheres (WOS). Neural Walk-on-spheres trains neural networks based on WOS estimates. How does the error rate of the Surrogate model compare against random-walks that accumulate the source term over the green function? 

2.	What is the justification for using convolution neural networks as the surrogate model, to capture neighborhood information? A radius based graph neural network is discretization agnostic and works especially well in sparse settings. 

3.	The surrogate model is not discretization agnostic. The functions sampled would have to be the same discretization as it was trained on. Which would mean that the neural operator model can predict any sparse distribution of points, but the second loss term (i.e. the surrogate model) has to be a fixed discretization. This seems like a bottleneck. Were there reasons for not making the second model a neural operator. Perhaps using [1] would be a good way to ensure operator learning through the entire pipeline. 

[1] Wang, Tian, and Chuang Wang. "Latent Neural Operator for Solving Forward and Inverse PDE Problems." arXiv preprint arXiv:2406.03923 (2024).

### Soundness
3

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
4

### Summary
The paper adapts physics-informed neural operators to settings without knowledge of the underlying PDE by approximating while learning the neural operator. This is then shown to improve the performance of neural operators in the case of scarce data.

### Strengths
- The approach is interesting, novel, and well-reasoned.
- The ablation studies for different components are appreciated.
- Thorough evaluations show the effectiveness of the method.
- Clear presentation, easy to follow

### Weaknesses
 - The presented approach can only learn the operator mapping the source function to the solution function. That this is not the standard operator learning problem setting (as for example discussed in the FNO paper) is only mentioned in the limitations section at the end of the appendix. It would be helpful to mention the focus during the problem formulation already and put the limitation section in the main paper.
- The training set sizes seem random and sometimes do not cover a broad range. This is the most significant for the SIF dataset. It would have been interesting to see different experiments with dataset sizes covering a broader range like 10, 100, 1000 
- Timing: It would be interesting to have an actual time comparison between the methods. Furthermore, since the idea is that this idea saves time as less data has to be generated, a comparison to the time it takes to compute more data would be interesting.

Minor Notes:
- You often write feedforward layer/network, when I think you mean fully-connected layer/network. A convolutional layer is, for example, also a feedforward layer.
- p.4: You state that you use "numerical difference" to compute the derivatives. Do you mean finite differences?
- Eq. 4: p(f) is not defined
- Figure 2 seems to be too early
- p. 10, l.521: "the best choice [of $\lambda$] is often in between" In between what? This seems to be a very vague statement

### Questions
- The experiments in Table 3 and and Table 4a seem very similar. Can you explain the main difference (apart from including FNO) is?
- While I understand that it is not the idea to use PPI-FNO when the PDE is known, it would be interesting to see a comparison between PPI-NO und PI-NO, to learn about the loss by approximating the PDE instead of using the correct one. Can you run some experiments with PI-NO for a comparison?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 6

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper proposes a way to train a solution operator for partial differential equations applicable when only few data points are available. For this, they first apply a system identification technique to approximate the underlying partial differential equation and then use this equation for physics-informed training of their solution operator. They evaluate their method on 5 non-trivial partial differential equations.

System identification is a well-studied field and physics-informed training of neural operators has been done before, as the authors correctly describe. The novelty lies in their combination to train a solution operator with only few data points. To my knowledge, this has indeed not been done before. The idea is simple and makes sense.

I think the biggest weakness is that the straight-forward way to train a solution operator with few data is not discussed and therefore, also not part of their experiments: After the PDE is approximated, one could use this to generate new data and train the solution operator in a supervised setting with many data points. I would expect this to work better than the author’s method since neural networks are easier to optimize with data sets than with a physics-informed loss. Their only baseline is supervised training with few data points. As I expect training on few data points to require much less time than physics-informed training, I don't consider this a fair comparison. A convincing benchmark would require reporting the actual time spent on training and then further spent the same amount of time on a decent baseline, for instance, the one outlined above. For example, half of the time for the generation of further solution-source terms, and the other half for training the solution operator. 

Another issue is that the author's method is basically using two other techniques from two different subfields in sequence rather than coupling the underlying principles into an improved method. While this is not inherently negative, it raises the expectation for a more generalized argumentation. For instance, including more than one specific technique for each of the subfields, such as another technique for system identification. Or making a theoretical argument about how the individual errors of the PDE approximation in the first step and the solution operator approximation add up to the total error. 

Some minor points: 
- I think many details on the experiments (convolutional kernel size, activation functions, frameworks used,...) should be moved to the appendix
- Equation 2 indicates that the first neural network (denoted by phi in the paper) acts on quantities at a specific spatial point while Figure 1 indicates phi acts on entire fields on the spatial domain. This should be clarified. 
- The related work section should mention some works on system identification.

### Strengths
See above.

### Weaknesses
I think the biggest weakness is that the straight-forward way to train a solution operator with few data is not discussed and therefore, also not part of their experiments: After the PDE is approximated, one could use this to generate new data and train the solution operator in a supervised setting with many data points. I would expect this to work better than the author’s method since neural networks are easier to optimize with data sets than with a physics-informed loss. Their only baseline is supervised training with few data points. As I expect training on few data points to require much less time than physics-informed training, I don't consider this a fair comparison. A convincing benchmark would require reporting the actual time spent on training and then further spent the same amount of time on a decent baseline, for instance, the one outlined above. For example, half of the time for the generation of further solution-source terms, and the other half for training the solution operator. 

Another issue is that the author's method is basically using two other techniques from two different subfields in sequence rather than coupling the underlying principles into an improved method. While this is not inherently negative, it raises the expectation for a more generalized argumentation. For instance, including more than one specific technique for each of the subfields, such as another technique for system identification. Or making a theoretical argument about how the individual errors of the PDE approximation in the first step and the solution operator approximation add up to the total error. 

Some minor points: 
- I think many details on the experiments (convolutional kernel size, activation functions, frameworks used,...) should be moved to the appendix
- Equation 2 indicates that the first neural network (denoted by phi in the paper) acts on quantities at a specific spatial point while Figure 1 indicates phi acts on entire fields on the spatial domain. This should be clarified. 
- The related work section should mention some works on system identification.

### Questions
- The abstract states that the method ‘enhances the accuracy of current operator learning
models, particularly in data scarce scenarios’.  As I understand the paper, the presented method is  suited only for data-scarce scenarios.
- Why are physics-informed losses introduced as a regularization technique? (in the introduction)

### Soundness
2

### Presentation
2

### Contribution
2
