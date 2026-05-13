# ECLayr: Fast and Robust Topological Layer based on Differentiable Euler Characteristic Curve

- Decision: Reject
- Scores: 5, 5, 6, 5, 5

## Abstract
In the realm of Topological Data Analysis, persistent homology has traditionally served as a primary tool for extracting topological features. However, approaches relying on persistent homology often encounter practical challenges due to their high computational costs. To address this issue, we propose a computationally efficient novel topological layer tailored for general deep learning architectures, leveraging the Euler Characteristic Curve (ECC). Unlike methods based on persistent homology, ECC offers computational advantages by circumventing the need for persistent homology calculation, while still allowing access to crucial information about the underlying topological structure. The proposed layer can readily adapt to diverse data modalities by allowing appropriate filtration according to the user's preference, enabling its application across various learning problems without data preprocessing. We present a novel technique for stable backpropagation that effectively mitigates the vanishing gradient problems commonly encountered in existing methods, allowing for seamless integration of our layer into deep learning models. We go on to present stability analysis, showing that the proposed layer is robust against noise and outliers. We apply our method to topological autoencoders, showing that the standard loss function can effectively regularize topological structures of the latent space. Through classification experiments across various datasets, we illustrate the benefits of our approach in mitigating information loss under conditions of data scarcity or data contamination.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces ECLayr, a new topological layer for deep learning that uses the Euler Characteristic Curve (ECC) rather than traditional persistent homology. The key innovation is achieving efficient computation and stable backpropagation while still capturing useful topological features. The authors propose a new gradient approximation method that avoids the vanishing gradient issues found in previous approaches DECT using sigmoid approximations. They provide theoretical stability guarantees and demonstrate ECLayr's effectiveness through experiments on classification tasks with limited or noisy data, topological autoencoders, and high-dimensional medical imaging data.

### Strengths
- The computational efficiency gain compared to persistent homology approaches is significant - showing speed improvements of 10-30x while maintaining comparable performance. 
- The theoretical foundation is solid, with careful stability analysis and proofs regarding the gradient approximation method. 
- The empirical results are comprehensive, testing the method across different scenarios and comparing against relevant baselines.

### Weaknesses
 - The empirical results, while interesting, are somewhat preliminary - the authors acknowledge that their simple architecture couldn't fully capture the nested relationship in the data. 
- There could be more investigation into what topological features ECLayr is actually capturing and why they're useful for the specific tasks. The comparison to DECT could also be expanded, as it's the most similar existing approach. 
- The hyperparameter selection process (like choice of filtrations and beta for gradient control) could be better explained. Specifically, the choice of filtration seems crucial, yet the paper lacks a systematic way to select the most appropriate filtration for a given dataset. The method's sensitivity to the choice of grid points and intervals also needs further investigation.


### Questions
- How sensitive is the method to the choice of filtrations, the number of grid points and the intervals? Some ablation studies on these parameters would be informative.
- More insight into why ECLayr sometimes outperforms persistent homology-based methods despite capturing less topological information?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces a neural network layer based on Euler Characteristic Curve (ECC), which is computationally much more efficient than layers based on Persistent Homology (PH). Compared to earlier work in this direction, this technique is shown to mitigate the vanishing gradient problem (Section 4).

### Strengths
The paper includes both theoretical results that guarantee the stability of the ECC layer (Section 5), and experiments that demonstrate its good performance (Section 6). It is also well written and organized.

### Weaknesses
See questions below.

(Q1) Be mindful of the use of the word "topological" in the title, abstract and throughout the paper: Depending on the filtration, PH or ECC can capture geometric information too (which is e.g., the case for the Vietoris-Rips filtration too, that captures the size of the cycles). At least briefly comment on this.

(Q2) Somewhat related to (Q1) above, Turner et al. showed that ECC with respect to the height filtration from all directions describes the shape completely. Maybe this is relevant to mention too, and also comment why you don't opt for such an approach, as it is obviously more informative (more precisely, it provides complete information) than the limited aspects captured with ECC with respect to the filtrations you consider in your work?

(Q3) You write that the work most closely related to yours is by Kim and Röell. Why is PLLay more related to your approach than PersLay? What about ATOL [1]?

(Q4) When discussing related work, you write that the height filtration may be applicable to point clouds, yet with a compromise in connectivity information? Does this compromise need to happen? What if one uses non-vanilla Vietoris-Rips filtration with the height as the filtration function value on the vertices, and the geodesic/shortest-path distance as the filtration function on the edges? Also, does the work by Röell & Rieck not carry out experiments on MNIST and ModelNet point clouds?

(Q5) A (simplicial or) cubical complex is not a filtration (e.g. Section 3.1), we need a filtered cubical complex / filtration function value on each cube. I think you assume the filtration function to assign the greyscale pixel value, but this needs to be formulated more precisely. Other filtration functions are also reasonable, such as the DTM that you also use in this work, or height, density, dilation, erosion ..., see [2].

(Q6) More should be said about the choice of $T_{min}$ and $T_{max}$. For instance, for the example in Figure 1, choosing $T_{min} = 1$ and $T_{max} = 2$ would not give us any insights whatsoever? Can we not always take $T_{min}$ and $T_{max}$ to be respectively the minimum and maximum of the filtration function value across all simplices/cubes?

(Q7) Even more importantly, more can be said about the discretization of the interval $[T_{min}, T_{max}]$. The main advantage of PH is that one does not need to choose the filtration scale t that best captures the shape, rather, the shape is captured continuously across any value of t.  How do you know that there are no cycles that are both born and dead between some steps $t_i$ and $t_{i+1}$, and therefore not captured? This might be related to the assumptions of your crucial Proposition 5.1, but are never discussed. Also, if $\Delta t$ is very small (i.e., if one uses a very fine discretization to hopefully avoid the above issue), how useful is the very large constant on the right-hand side? This discussion is additionally important since you mention in Section 4.1 that the discretization is the problem for DECT by Röell, leading to gradient inconsistency.

(Q8) Can you visualize the different architectures (in the appendix)? Besides improved clarity, this might provide better insights on why ECC outperforms PH. Regarding this poor performance of PH in comparison to ECC, can you somewhat rely on Figure 5 (c) and (d), i.e., the behaviour of gradients, to provide some further intuition?

(Q9) Can you motivate the choice of the data sets in your experiments? Why not employ the data sets used in the paper that introduce your baselines such as PersLay, PLLay, DECT?

(Q10) In Section 6.1, you write that the time complexity is assessed by measuring the runtime for a complete iteration through the training data set. From Table 1, this means that PH is calculated for 60 000 28x28 images in only 33 seconds?

(Q11) Why do you say in Section 6.4 that the calculation of PH for Br35H 112 x 112 images is unfeasible, whereas it does work for the same data set, and even for 224 x 224 synthetic images in Section 6.1?

(Q12) Can you explain a bit better the "consequently" in the Discussion when you say that since ECC are topologically weaker invariants compared to PH, they exhibit less robustness? The latter is clear from the last paragraph of Section 5, but here you seem to imply that it is also expected? Intuitively, one would think that a signature is more stable if it captures less detailed information?

(Q13) Can you somewhat motivate the choice of hyperparameters? For instance, in Appendix H.4 you write that learning rates are 0.0001 and 0.01 respectively for ECLayr and ResNet?


Minor comments and typos:
- Explicitly mention that the proofs can be found in the Appendix (also to make it clearer that these results are not taken from the literature, but constitute the contribution of this paper).
- Stress more clearly the difference between C_X and E (ECC function and vector). For the sake of consistency, why not use E_X?
- A notation table (in appendix) could be helpful, especially when focusing on the main results, one needs to look through different parts of the paper to know what E, O, C are.
- Since you are comparing runtimes, I think it is useful to explicitly mention the size of the data sets and images in Section 6.
- References: Check the formatting, e.g., "Journal of Machine Learning Research" and "J. Mach. Learn. Res" are both used, the capitalization of journals is not consistent, "euler", etc.
- Appendix A: that is needed -> that are needed
- Appendix A, Footnote 1: reference is missing
- Appendix A: x. k -> x, k (2x)
- Appendix F title: Section -> Appendix. Also, should this Appendix not follow immediately after Appendix D, or at least after the two Appendices that contain the proofs for Section 4 and Section 5?
- Appendix 6: Proof of Proposition 5.2 -> Proof of Proposition 5.1

### Questions
(Q1) Be mindful of the use of the word "topological" in the title, abstract and throughout the paper: Depending on the filtration, PH or ECC can capture geometric information too (which is e.g., the case for the Vietoris-Rips filtration too, that captures the size of the cycles). At least briefly comment on this.

(Q2) Somewhat related to (Q1) above, Turner et al. showed that ECC with respect to the height filtration from all directions describes the shape completely. Maybe this is relevant to mention too, and also comment why you don't opt for such an approach, as it is obviously more informative (more precisely, it provides complete information) than the limited aspects captured with ECC with respect to the filtrations you consider in your work? 

(Q3) You write that the work most closely related to yours is by Kim and Röell. Why is PLLay more related to your approach than PersLay? What about ATOL [1]?

(Q4) When discussing related work, you write that the height filtration may be applicable to point clouds, yet with a compromise in connectivity information? Does this compromise need to happen? What if one uses non-vanilla Vietoris-Rips filtration with the height as the filtration function value on the vertices, and the geodesic/shortest-path distance as the filtration function on the edges? Also, does the work by Röell & Rieck not carry out experiments on MNIST and ModelNet point clouds?

(Q5) A (simplicial or) cubical complex is not a filtration (e.g. Section 3.1), we need a filtered cubical complex / filtration function value on each cube. I think you assume the filtration function to assign the greyscale pixel value, but this needs to be formulated more precisely. Other filtration functions are also reasonable, such as the DTM that you also use in this work, or height, density, dilation, erosion ..., see [2].

(Q6) More should be said about the choice of $T_{min}$ and $T_{max}$. For instance, for the example in Figure 1, choosing $T_{min} = 1$ and $T_{max} = 2$ would not give us any insights whatsoever? Can we not always take $T_{min}$ and $T_{max}$ to be respectively the minimum and maximum of the filtration function value across all simplices/cubes?

(Q7) Even more importantly, more can be said about the discretization of the interval $[T_{min}, T_{max}]$. The main advantage of PH is that one does not need to choose the filtration scale t that best captures the shape, rather, the shape is captured continuously across any value of t.  How do you know that there are no cycles that are both born and dead between some steps $t_i$ and $t_{i+1}$, and therefore not captured? This might be related to the assumptions of your crucial Proposition 5.1, but are never discussed. Also, if $\Delta t$ is very small (i.e., if one uses a very fine discretization to hopefully avoid the above issue), how useful is the very large constant on the right-hand side? This discussion is additionally important since you mention in Section 4.1 that the discretization is the problem for DECT by Röell, leading to gradient inconsistency.

(Q8) Can you visualize the different architectures (in the appendix)? Besides improved clarity, this might provide better insights on why ECC outperforms PH. Regarding this poor performance of PH in comparison to ECC, can you somewhat rely on Figure 5 (c) and (d), i.e., the behaviour of gradients, to provide some further intuition?

(Q9) Can you motivate the choice of the data sets in your experiments? Why not employ the data sets used in the paper that introduce your baselines such as PersLay, PLLay, DECT?

(Q10) In Section 6.1, you write that the time complexity is assessed by measuring the runtime for a complete iteration through the training data set. From Table 1, this means that PH is calculated for 60 000 28x28 images in only 33 seconds?

(Q11) Why do you say in Section 6.4 that the calculation of PH for Br35H 112 x 112 images is unfeasible, whereas it does work for the same data set, and even for 224 x 224 synthetic images in Section 6.1?

(Q12) Can you explain a bit better the "consequently" in the Discussion when you say that since ECC are topologically weaker invariants compared to PH, they exhibit less robustness? The latter is clear from the last paragraph of Section 5, but here you seem to imply that it is also expected? Intuitively, one would think that a signature is more stable if it captures less detailed information?

(Q13) Can you somewhat motivate the choice of hyperparameters? For instance, in Appendix H.4 you write that learning rates are 0.0001 and 0.01 respectively for ECLayr and ResNet?

[1] Royer, Martin, et al. "ATOL: Automatic topologically-oriented learning." arXiv preprint arXiv:1909.13472 (2019).

[2] Garin, Adélie, and Guillaume Tauzin. "A topological" reading" lesson: Classification of MNIST using TDA." 2019 18th IEEE International Conference On Machine Learning And Applications (ICMLA). IEEE, 2019. 

I will raise my score if the main questions above (in particular Q7-Q9) are properly addressed.


Minor comments and typos:
- Explicitly mention that the proofs can be found in the Appendix (also to make it clearer that these results are not taken from the literature, but constitute the contribution of this paper).
- Stress more clearly the difference between C_X and E (ECC function and vector). For the sake of consistency, why not use E_X?
- A notation table (in appendix) could be helpful, especially when focusing on the main results, one needs to look through different parts of the paper to know what E, O, C are.
- Since you are comparing runtimes, I think it is useful to explicitly mention the size of the data sets and images in Section 6.
- References: Check the formatting, e.g., "Journal of Machine Learning Research" and "J. Mach. Learn. Res" are both used, the capitalization of journals is not consistent, "euler", etc.
- Appendix A: that is needed -> that are needed
- Appendix A, Footnote 1: reference is missing
- Appendix A: x. k -> x, k (2x)
- Appendix F title: Section -> Appendix. Also, should this Appendix not follow immediately after Appendix D, or at least after the two Appendices that contain the proofs for Section 4 and Section 5?
- Appendix 6: Proof of Proposition 5.2 -> Proof of Proposition 5.1

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors propose a novel learnable topological layer based on Euler Characteristic Curve (ECC). They prove that ECC is differentiable and approximate the gradient using distributional derivatives to be used at the time of back propagation. They show experimental results on some synthetic dataset and MNIST dataset.

### Strengths
The paper is well-written and easy to follow.

The authors are solving one of the important problems in the TDA in ML community of integrating topological descriptors in a learnable manner into ML pipelines. 

The paper has a significant theoretical component.

### Weaknesses
Adding Table 4 and Table 5 from Appendix H.3 into the main text would help support the claim that though EC is not as expressive as PH, the performance is comparable.

However, I think that more extensive experimentation is required to understand the kind of data (graph data, point cloud data etc.) where trading off on the expressive power for computational efficiency does not result in a major decrease in performance. Specifically, the current experiments are limited to relatively simple synthetic datasets and MNIST, which might not fully reveal the limitations of using ECC instead of more expressive topological descriptors like persistence homology on complex data.

The paper would also benefit from ablation studies on choosing the hyper parameters $v, T_{min}, T_{max} $ because these seem quite important to capture the relevant parts of a filtration. The lack of such studies makes it difficult to assess the robustness and generalizability of the proposed method across different datasets and filtration strategies.

### Questions
Looking at Table 4, would it be a right statement to make that on MNIST dataset, EC is able to capture the topology and generalize well only by looking at, say 100 or 200 examples? As the size of the training set grows, the performance gains start reducing. In which case, do you think it would be better for topological methods to be used when training data available is very limited?

Perslay and PLlay have options for permutation invariant functions. Any specific reasons to use the choices that you have? I find it quite surprising that EC consistently performs better than PH.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces ECLayr, a computationally efficient topological layer for deep learning architectures, utilizing the Euler characteristic curve (ECC) rather than persistent homology (PH). ECLayr aims to overcome the computational limitations of PH while preserving essential topological insights. The layer is designed to integrate into various neural networks by providing stable backpropagation, addressing issues like vanishing gradients. ECLayr’s effectiveness is demonstrated through experiments in classification and topological autoencoders, highlighting its speed and robustness against data contamination.

### Strengths
- ECLayr presents an interesting approach to leveraging topological features by focusing on ECC instead of PH.
- The paper covers detailed theoretical evaluations of the proposed method.
- The paper is generally well-organized and explains complex concepts in topological data analysis clearly, although some explanations in the backpropagation section may benefit from further clarification.
- The proposed ECLayr layer has potential for broad application in scenarios where computational efficiency is crucial, such as high-dimensional data or real-time applications.

### Weaknesses
 - Although the paper introduces ECC in a deep learning context, ECC itself is not a new concept, limiting the work's novelty. The paper might benefit from comparisons with recent, alternative topological descriptors beyond PH to clarify its advantages.
- While experiments cover some datasets, they primarily test standard tasks and small datasets, which might not fully showcase the layer’s potential in more complex, large-scale applications. The experiments also lack a thorough exploration of hyperparameter sensitivity, particularly regarding the choice of filtration and discretization parameters, which could significantly impact performance.
- Although ECC-based methods are computationally efficient, they are also inherently less robust than PH due to dependence on small generators. Further testing with different noise levels or adversarial robustness could provide a clearer view of its resilience. The paper should include a more detailed analysis of the trade-offs between computational efficiency and robustness compared to PH-based methods, especially in the context of noisy or adversarial data.
- The stability and backpropagation advantages are discussed in some depth, but additional formal proofs or extended stability comparisons with PH-based methods would solidify the theoretical foundation. The current stability analysis focuses primarily on small perturbations, and it would be beneficial to see a more comprehensive analysis that includes larger perturbations and different types of noise.

### Questions
- The stability analysis primarily focuses on ECC robustness against small noise. Could the authors provide more comparative results showing how ECLayr performs under more significant noise compared to PH-based methods?
- Could you clarify the hyperparameters and initialization procedures in ECLayr's construction? Some details in the choice of differentiable filtrations seem crucial to replicating results.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces a topological data representation based on Euler characteristic curves (ECC). The representation is obtained via discritizing the ECC and then processing it with a parametrized, learnable map. To make the representation differentiable and avoid vanishing gradients, the authors approximate the derivative of the indicator function with a shifted Gaussian function. The paper highlights several advantages of this representation, including computational efficiency, mitigation of vanishing gradient issues, and stability under data perturbation. Numerical experiments are provided to demonstrate the representation’s effectiveness.

### Strengths
* The paper is well-structured and easy to follow. 
* The proposed representation is computationally efficient and applicable to general data and filtrations, allowing a convenient integration with deep learning models for diverse tasks.   
* The proposed representation mitigates the vanishing gradients issues. 
* The paper includes extensive experiments, covering various application scenarios and provides an adequate comparison with existing methods.

### Weaknesses
 * To avoid vanishing gradient, the authors approximate the (distributional) derivative of the indicator function with a Gaussian function and shift the Gaussian center to align with the filtration values. However, this approximation seems unnecessary, as the approach is equivalent to always setting $\partial \mathbb{I}(f_\sigma \leq t_i)/\partial f_\sigma$ as a fixed constant $\gamma$, where $f_\sigma \in [t_i, t_{i+1})$. This is also equivalent to approximating the indicator function $\mathbb{I}(f_\sigma \leq t_i)$ with a linear function $f_\sigma \mapsto \gamma (f_\sigma - t_i)$. It is then unclear how novel this technique is. 

* Another concern with the shifting is that, as the gradient is set to a constant independent of $f_\sigma$, the information about the filtration value is lost and all simplices with filtration values between $[t_i, t_{i+1})$ have a same gradient term $\partial \mathbb{I}(f_\sigma \leq t_i)/\partial f_\sigma=\gamma$. This leads to the topology information being distorted during back propagation. Specifically, the method effectively projects all filtration values within an interval $[t_i, t_{i+1})$ onto the single grid point $t_{i+1}$ during backpropagation, discarding the precise location of $f_\sigma$ within the interval. As a comparison, the sigmoid approximation [1] produces a gradient of the form $\lambda S^\prime(\lambda( f_\sigma -t_i))$, which contains information about $f_\sigma$. This gradient reflects the exact filtration value, allowing the representation to distinguish between different filtration values within the same interval, a capability lost in the proposed method.

* Regarding the stability result, Proposition 5.1 indicates the Lipschitz constant can be bounded by $2L/\Delta t$. This bound diverges with a rate $\Theta(\Delta t^{-1})$ as the grid size $\Delta t$ tends to zero. Hence, I question if it is useful, as a smaller $\Delta t$ corresponds to a better approximation of ECC during discretization. Note in the experiments described in H.2, $1/\Delta t = 1/(2/1000) = 500$; and in H.4, $1/\Delta t = 1/(.6/64)\approx 106$. As a comparison, persistence image, which is a PH-based representation and is also obtained with discretization, is stable with a grid-size-free Lipschitz constant [2]. 

Overall, while the proposed representation offers computational convenience, it is less informative than PH-based representation, especially with the discretization of ECC and the shifting techniques. I agree with the author that "understanding this tradeoff (between computational efficiency and expressiveness) is essential" and would have appreciated a more intuitive and theoretical discussion on this tradeoff. For example, how one can expect the proposed representation is better than a naive representation: a vector of the top-50 largest filtration values? This naive representation also does not require PH computations and is stable as long as the filtration function is. 

### Questions
* When computing the output of ECLayr from the discretized ECC, the paper mentions that "ECC may potentially contain some noise information. Thus, ... employ a differentiable parametrized map $g_\theta$ to project ECC to a learnable task-optimal representation". How should one expect this map to filter out noise information? 
* Just a reminder: the current heading in the paper is for last year’s conference.

### Soundness
2

### Presentation
3

### Contribution
2
