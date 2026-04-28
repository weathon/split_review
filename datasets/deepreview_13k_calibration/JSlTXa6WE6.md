# Efficient Certification of Physics-Informed Neural Networks

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 6, 6, 5

## Abstract
Recent work provides promising evidence that Physics-Informed Neural Networks (PINN) can efficiently solve partial differential equations (PDE). However, previous works have failed to provide guarantees on the \textit{worst-case} residual error of a PINN across the spatio-temporal domain -- a measure akin to the tolerance of numerical solvers -- focusing instead on point-wise comparisons between their solution and the ones obtained by a solver on a set of inputs. In real-world applications, one cannot consider tests on a finite set of points to be sufficient grounds for deployment, as the performance could be substantially worse on a different set.
To alleviate this issue, we establish guaranteed error-based conditions for PINNs over their \textit{continuous} applicability domain. To verify the extent to which they hold, we introduce \partialcrown: a general, efficient and scalable post-training framework to bound PINN residual errors. We demonstrate its effectiveness in obtaining tight certificates by applying it to two classically studied PINNs -- Burgers' and \schrodinger's equations --, and two more challenging ones with real-world applications -- the Allan-Cahn and Diffusion-Sorption equations.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes to solve the question of “efficient certification” of PINNs which – as the authors state – is the question of trying to quickly estimate bounds on the supremum (over domain points) error made by the neural surrogate for the residuals. The authors give experiments to suggest that their methods give upperbounds almost as good as the estimations made via random sampling of domain points.

### Strengths
The claims that have been proven in this paper do indeed seem a bit surprising – that upto second order of derivatives for the neural net, these functions can be linearly bounded bothways.

### Weaknesses
Prima facie the paper is very badly written – to the point of being very much devoid of motivations. Till one gets to the experiments, it's entirely unclear what is the “certification” question that is even being solved. In fact even after reading everything in the main paper, it's not clear at all as to why the random point sampling way is not enough to implement a check of the inequalities as required in Definition 1. What exactly is being gained by this method (as demonstrated in the third column of Table 1) as opposed to the results in the first two columns?  

Even the run-time reported to obtain some of these numbers in the third column of Table 1 seems to be in millions of seconds. 
That is more than a day! So this method isn't hinged on an argument of speed either.  

Secondly, I am not able to ascertain from the given descriptions if the presence of these linear two-way bounds is a special case for the first two derivatives of a neural net or does this happen for all derivatives. Is the method $\partial-$CROWN hinged on the validity of these linear bounds? In that case, why is the method of interest to the general PINN formalism where arbitrarily high orders of derivatives can potentially occur.  

Thirdly, the theorems are very badly stated. It's not clear from their statements as to whether or not there is an explicit expression for these linear bounds and if yes (which it seems to be from the appendix!) then what information is required to be able to compute them.  

Fourthly, the choice of the PDE examples for testing are very skewed. If one is doing experiments on multiple PDEs then it would have been better to include PDEs that have more than 2 variables. It does not help to have all the examples be stuck to two variable PDEs!  

Also, the Schrodinger PDE example looks a bit strange. Which natural Hamiltonian function even leads to this? This seems to be coming from a system with a potential energy which is “$-|u|^2$” - and that is never a natural setting – to the best of my knowledge of quantum theory!

### Questions
It would be great if the authors can give a precise answer to the first two weaknesses pointed out above.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper tries to establish correctness certification for PINN models via the proposed $\partial-$CROWN post-training framework. Under several assumptions, the authors prove two theorems showing that the upper and lower bound of the solution can be computed in $\mathcal O(L)$ time. The authors experimentally demonstrate the tightness of their bound via a few small PDE examples, showing that they can achieve excellent approximation (compared with MC samples) much more efficiently.

### Strengths
- Undoubtedly, bounding the error of ML solutions *globally*, as the authors try to tackle, is important and necessary for ML methods to be practically applicable. I am happy to see theoretical and empirical research on this avenue.
- The improved Greedy Input Branching intuitively makes sense to me, although its direction comparison with the non-optimized algorithm seems to be lacking.
- This paper is well-written, and the organization and flow are clear. I also pretty much appreciate the combination of theoretical proof and empirical demonstration.

### Weaknesses
While I like this paper, there are several non-negligible problems that have to be addressed before the paper reaches the bar of acceptance.

- First of all, I am not sure why the authors naturally assume that the ground truth can be represented by a FNN. For instance, even a single electron wave function decays exponentially, which an FNN cannot represent. Since the goal here is to bound the global error, I do not think the gap between the best FNN versus the actual ground truth can be ignored. Similarly, assumption 1 limits the applicability of your theorems - what happens if I add some exponential layers, or what if I use other architecture? The justification for using only FNNs based on their universal approximation property is not entirely convincing. While FNNs are universal approximators in the infinite width limit, in practice, other architectures like CNNs and Transformers often perform better for specific tasks (e.g., images and language, respectively). The paper needs to address why the proposed method is limited to FNNs and what challenges prevent its application to other architectures. Is it due to the specific mathematical techniques, such as the convex relaxations and bound propagation used, which may only be easily applied to linear or piecewise linear models?  A more detailed explanation of the limitations of the method is crucial.
- Your theorems only prove the existence of bounds, while your algorithm is still greedy. If I understand correctly, this actually means that: the approximation error (say the numbers in Table 1) is not *guaranteed* to be an upper bound of the global error, right? If so, despite the acceleration you achieve, how can you demonstrate that in a large system, your error approximation is *accurate*?
- I do think the paper should include more complex tasks, as PINN is known to be less accurate in large systems (or long simulation time intervals). Current experiments, while sufficient as a proof of concept, are insufficient to demonstrate the proposed algorithm can indeed provide a better approximation. For instance, you can try multi-body Schrodinger equations, like [1], or HJB equations [2]. These are of large scales and non-linear, making it challenging (IMO) to your method.

### Questions
- From my understanding, speed is one of your strengths. Can you more comprehensively compare with previous methods to demonstrate how fast your method is? A table or figure will be ideal.
- I think the paper could be benefited by including more takeaways, especially for the theorems. I can sort of imagine how this theorem is proved, but it would be great if the authors could give a proof sketch and discuss how each assumption and condition works.
- notation layer $k$: try to use $l$ since the total layer number is $L$.

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
The paper provides a definition of global correctness conditions for PINNs that produces the solutions of PINNs. The authors propose CROWN based certification framework to bound first and second derivatives $\mu_\theta$ as well as the $f_\theta$. 

While CROWN provides a theoretical bound, given the approximations used throughout the bounding process, such bound is still less tight to bound the actual $h$. The authors utilize a similar idea to BaB, and apply greedy input branching algorithm to the bounding process.

The authors have provided experiments to verify that (1) $\partial$- CROWN are more tight compared to empirical errors computed with a large number of samples (2) residual-based certificates and the commonly reported solution errors are highly correlated. They have also provided an ablation study to check the importance of the branching algorithm.

### Strengths
(1) The paper provides a good contribution to the research community. The authors are building the correctness conditions for PINNs over the input domain, which can improve the robustness and trustworthiness of PINN when applying it to the scientific domains.

(2) While CROWN is not new, the authors make novel contributions to apply CROWN to solving PINN's correctness conditions. 

(3) In Section 5, the authors have provided detailed theoretical foundations for how to bound the correctness conditions. The proofs in appendix are long but easy to read.  The authors have also provided a theoretical analysis of the running time for $\partial$-CROWM algorithm.

(4) The authors have provided an improved version with greedy input branching, similar to the idea of original branch-and-bound (BaB) process.

### Weaknesses
 (1) The major concern that reviewer has is that the certification procedure is the on PINN residual error, $f$, but not on the estimation to the true PDE solution. While the authors have provided Exp 2 and Appendix C to demonstrate that there is a strong relationship between the residual error and the PDE solution, it is only conducted on PDEs with a clear PDE solution. More experiments should be conducted with various PDE equations (with multiple solutions, with trivial solutions, etc.) to find out how bounding $f$ is effective. Especially for the recent papers that discuss the failure modes of PINN[1], how would bounding the residual errors help, both theoretically and empirically? The paper needs to address the fundamental issue that a small residual error does not guarantee an accurate solution, particularly in cases where PINNs might converge to a trivial or incorrect solution. This is a critical limitation that needs more rigorous investigation, and the current experiments do not sufficiently address this concern.

(2) Figure 2 looks meaningless. The Figure 2(a)-2(d) only shows the visualization of the time evolution of $u$, versus the residual
errors for three different PDE equations. However, it is hard to observe any clear patterns of the residual errors, and the authors only briefly mention the residual errors without explaining any scientific insights from the Figure. The reviewer thinks it is better to put the Figure into Appendix, and instead briefly mention Appendix A and B in the main text.

(3) Table 1 shows that  $\partial$-CROWN approaches the empirical bounds obtained using Monte Carlo sampling while providing the guarantee that no point within the domain breaks those bounds. The reviewer think it will be nice to document some time it takes for MC sampling versus the $\partial$-CROWN (at least for residual error), to demonstrate its efficiency.

(4) Figure 1 is occupying too much spaces while the words on the upper right corner are hard to read. Maybe the authors should consider providing a more concise illustration that occupies less space.

(5) In Section 6.3, the authors should consider also including the ablation study on $N_b$ into the main text.

(6) In Section 5.3, the authors mention that "exploring the areas... via sampling (SAMPLE, line 3)", is there a typo and should be line 5 instead of line 3?

### Questions
(1) In the appendix A, the authors have mentioned to use Physics-informed Adversarial Training to reduce the errors of PINN and demonstrate that $\partial$- CROWN can also bound the residual errors of PIAT. However, there are been various ways of reduce the errors of PINN, for example, scheduled training [1] or building a more complex architecture with transformer [2]. The reviewer is wondering if the $\partial$-CROWN can adapt to NN training that involves more complex loss functions, or more complex architectures?

(2) Similar to Question 1 in Weakness, how could $\partial$-CROWN be used in solving the failures of PINN? If the residual error is large (or being stagnant for a long time), does that imply the PINN is failing to provide a good solution?

(3) Have the authors study the relation between $\partial$-CROWN's time complexity to the size of the PINN's neural network?

(4) How does $\partial$-CROWn behave when the amount of training data is low? Intuitively, the reviewer believes that the amount of training data needs to be evenly spreading across the domain to allow greedy input branching algorithm to work. But what happens when the amount of training data is not evenly spreading?

 
[1]: Krishnapriyan, Aditi S., Amir Gholami, Shandian Zhe, Robert M. Kirby, and Michael W. Mahoney. 2021. "Characterizing possible failure modes in physics-informed neural networks." arXiv preprint arXiv:2109.01050.

[2]: Zhao, Zhiyuan, Xueying Ding, and B. Aditya Prakash. 2023. "PINNsFormer: A Transformer-Based Framework For Physics-Informed Neural Networks." arXiv preprint arXiv:2307.11833.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Propose certification for PINN, i.e., guarantees on the worst-case residual error of a PINN, which can be used for prediction of PINN's performance for trustworthy PINN.

### Strengths
The paper is well-motivated as the theoretical guarantee is always a huge concern for PINN whose theory is not transparent, making it less practical than traditional finite element methods.

The theory is clearly proved together with supporting experiments.

### Weaknesses
The authors only provide theory for 1st and 2nd order derivates in PDEs. However, high-order PDEs are common, such as KdV, Kuramoto-Sivashinsky, and Boussinesq-Burger PDEs.

I don't think the extension to general high-order PDEs is simple, although I noticed the author thought it was trivial, because the expression of high-order derivative is extremely complex, which may affect the tightness of the certification. How does the PDE order affect the tightness of your certification?

Is this framework still valid when PINN encounters propagation failure? See https://arxiv.org/abs/2203.07404 Figure 2. The losses are very small but the error is huge.

To be more specific, there exists a case where PINN converges to a low residual loss but with a huge relative test l2 error, due to the propagation failure, or we can regard it as PINN converges to some spurious local minima corresponding to the trivial solution. In that case, the PINN model will be smooth and low loss. How can your theory deal with this case?

Besides, although the author shows by a figure that the residual loss correlates with the test l2 relative error well, I would like to emphasize that residual loss only provides a loose upper bound for the test l2 relative error. In other words, low residual loss cannot guarantee low test error.

Thus, I suggest the author test their theoretical framework in some tough cases where PINN encounters propagation failure.

### Questions
Can this theoretical framework be extended to high-order nonlinear PDEs? High-order PDEs are common, such as KdV, Kuramoto-Sivashinsky, and Boussinesq-Burger PDEs. How does PDE order affect the tightness of your certification?

Is this framework still valid when PINN encounters propagation failure? See https://arxiv.org/abs/2203.07404 Figure 2. The losses are very small but the error is huge.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
