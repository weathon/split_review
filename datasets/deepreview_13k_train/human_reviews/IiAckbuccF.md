# Nonmyopic Bayesian Optimization in Dynamic Cost Settings

- Decision: Reject
- Scores: 3, 6, 5, 3

## Abstract
Bayesian optimization (BO) is a popular framework for optimizing black-box functions, leveraging probabilistic models such as Gaussian processes. However, conventional BO assumes static query costs, which limits its applicability to real-world problems with dynamic cost structures, such as geological surveys or biological sequence design, where query costs vary based on previous actions. To address this, we propose a cost-constrained nonmyopic BO algorithm that incorporates dynamic cost models. Our method employs a neural network policy for variational optimization over multi-step lookahead horizons to plan ahead in dynamic cost environments. Empirically, we benchmark our method on synthetic functions exhibiting a variety of dynamic cost structures. Furthermore, we apply our method to a real-world application in protein sequence design using a large language model-based policy, demonstrating its scalability and effectiveness in handling multi-step planning in a large and complex query space. Our nonmyopic BO algorithm consistently outperforms its myopic counterparts in both synthetic and real-world settings, achieving significant improvements in both efficiency and solution quality.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The classical Bayesian Optimization (BO) frameworks operate under the assumption of static query costs. However, in practical scenarios, dynamic cost structures often arise. Hence, query costs dynamically change with respect to the previous queries. To address this, the paper proposes a cost-constrained nonmyopic BO algorithm that incorporates dynamic cost models into the BO framework. The method employs pathwise Thompson sampling and variational optimization. Empirical evaluation on both synthetic and real-world problem domains shows the effectiveness and scalability of the proposed approach against myopic baselines.

### Strengths
- The proposed nonmyopic BO approach handles dynamic cost structures that are inherent to many real-world problem contexts.
- The empirical evaluation covers both synthetic and real-world problem domains, which demonstrates the applicability of the proposed approach in real-world problems.
- A complexity analysis for approximating the posterior predictive distribution via path-wise sampling is provided.
- The empirical analysis is presented considering different cost functions.
- Using an LLM as a variational network of the proposed approach and showcasing the application of the proposed method on the protein design process as a dialogue is interesting.

### Weaknesses
 - The empirical evaluation is not supportive enough to show the effectiveness of the proposed nonmyopic approach mainly due to the following reasons:
1. In Section 2, the paper cites many nonmyopic BO approaches from the literature, e.g. [1,2,3,4], including cost-aware and budget-constrained ones. However, in empirical analysis, these methods are not chosen as baselines, hence the empirical evidence is not strong enough to support contribution. It would have been supported better if the proposed method was compared against some of such approaches, which would clarify the contribution of using (pathwise Thompson sampling & variational network)-based proposed idea against existing lookahead ideas. Further, the method could have been empirically compared against those methods in terms of computational efficiency, since enhancing the computational efficiency of nonmyopic BO is one of the claims of the paper (line 120).

2. It is stated that the proposed approach can be more robust when the approximation of the reward function changes significantly between queries. However, it could have demonstrated the robustness of the approach better, if the behavior of the approach with respect to the approximate reward function throughout active learning queries was analyzed more thoroughly, for example by showing the error in the surrogate model's predictions over the course of optimization.

3. The paper concentrates on the HES acquisition function for the proposed approach. However, if the proposed approach is flexible and generalizable, then it could have shown its flexibility better if any other acquisition function is considered, such as knowledge gradient and expected improvement. It would also directly show the change in the performance among myopic and nonmyopic BO versions under the same acquisition function.

4. There are many missing important ablation analyses, which would have supported the effectiveness of the proposed approach better with respect to its individual parts, specifically:

- 5. The performance under different look ahead step sizes. How does the performance of the proposed approach change under a short look-ahead horizon (budget)? It would support the empirical performance with respect to different horizon lengths.

- 6. Regarding the initial surrogate model, an ablation on the quality of the initial surrogate GP with respect to (1) initial training set size (which is not stated in the paper?), and (2) kernel choice other than Matern would strengthen the empirical analysis. It is important to understand how sensitive the method is to the initial data and model choices.

- 7. Although a real-world problem (protein sequence design) is chosen as the second test bed, the analysis is not detailed and scalable considering the settings. That is, an ablation study regarding the different $T$ (number of edits) values would have shown the applicability of the proposed approach better. Because most protein sequences have a sequence search space >> 4096, such as a typical human protein is of length 200-300 which makes the search space enormous. There are many generative and BO-based approaches that can design considering all positions of the sequence efficiently, hence considering a very limited design setting does not support the applicability and scalability of the proposed approach well enough.

- 8. Similar to the above point, why only 2 amino acid types is considered for the design, among possible 20 choices? How does the empirical performance and computational efficiency of the method change with respect to increased search space?

- 9. Batched BO is a conventional method also demonstrated to be effective in biological sequence design problem. An ablation study on the increased batch size would help for a better analysis.

- 10. Lastly, an ablation analysis with respect to the variational network (e.g. using a variational network of different accuracy levels) on a problem domain would support the actual benefit of the proposed approach.

11. It would have been supported stronger if additional real-world problem domains e.g. from natural language processing were presented, since the paper states that the method is applicable across diverse domains (line 87).


12. [$\star$]How does the proposed approach differ compared to this recent work [5] which very similarly proposes a cost-aware multi-step look ahead acquisition function? I think clarifying the difference with respect to this work is crucial in evaluating the novelty and contribution of the paper.


**Minor:**

- A very minor, however, for the sake of consistency in writing, either nonmyopic or "non-myopic" should be used (e.g. line 94).
- The repetition of the "equation" in lines 244 and 254 should be corrected.

### Questions
1. How does the performance of the proposed method change against baselines under increased batch sizes?

2. How is the performance of the proposed approach against other nonmyopic BO methods given in the paper? (also see the weakness 1)

3. How do you evaluate the robustness of the proposed method with respect to the changes in reward function?

4. Is the proposed approach flexible and generalizable? Can it work under different acquisition functions?  

5. Are the baselines other than the multistep tree implemented with a lookahead horizon=1 (myopic), is that right?

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
3

### Summary
This paper proposes a nonmyopic Bayesian optimization method to tackle the black-box optimization problem where the evaluation cost is action-dependent. The authors propose to optimize recurrent neural networks to choose the next sample position, and use pathwise sampling to reduce the exponential complexity during multi-step planning. The experiment results demonstrate that the proposed nonmyopic method is capable of locate global optimal region in synthetic functions, and the real experiment results over protein design demonstrate the practicality of the proposed method.

### Strengths
1. I think the problem tackled by this paper is novel, which corresponds to many real-world applications where traditional BO cannot be directly applied in.

2. The overall algorithm design is intuitive and clear.

3. The experiment results of protein design is impressive.

### Weaknesses
1. There is only one real world experiment with discrete action space. It would be better if evaluating the proposed algorithm in real-world/simulation tasks with continuous space.

2. There is no comparison with the methods that tackle optimization problems with dynamic cost, as metioned in the related work.

### Questions
1. What is the $\lambda$ value assigned in the experiment? How to define this value in practice?

2. In protein design experiment, the optional actions are restricted to 2 amino acid in each edited position. Why not use all 4 amino acid as candidate actions?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
In this paper, the authors study nonmyopic Bayesian optimization in dynamic cost settings, where costs can exhibit both Markovian and non-Markovian properties. The authors propose to use recurrent neural networks for variational lookahead optimization which can greatly increase the lookahead horizon beyond existing works. Empirical evaluations on synthetic test functions and a protein design task demonstrate the effectiveness of the proposed method.

### Strengths
1. This paper systematically studies many classes of varying cost structures. This contribution is novel.

2. The proposal of using RNNs for lookahead optimization is novel and the effect of extending the lookahead horizon seems significant.

3. The experiment results seem promising in demonstrating the positive effect of having long lookahead horizons.

### Weaknesses
1. There is only one lookahead baseline in the empirical evaluation. The authors mentioned several others in the related works section [1, 2, 3]. Can the authors explain why they were not included in the comparison? There is also [4] which is related to the current work.

2. A major claimed contribution is that extending lookahead horizon improves optimization results. This makes intuitive sense but there is no ablation study to confirm this claim. It would be helpful to compare different lookahead horizons’s impact on the final optimization results.

### Questions
1. Around line 100, the authors mentioned the synthetic functions “requiring 10 to 20 planning steps to find the global optimum”. How does one determine this number for a function?

2. In the protein sequence experiment, how did the authors arrive at the specific form for $g(x)$ (line 459)?

3. Can the authors provide more details regarding using Llama-3.2 3B as the variational network (line 483)?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The work studies the problem of performing (global) optimization of a black-box function, where the cost between actions may vary. The work proposes to learn a neural network policy via variational optimization of a multi-step objective. The authors conduct experiments on a large number of synthetic test functions, as well as in a protein design task whose setting appears slightly different from the main work.

### Strengths
The paper aims to address the real problem of dynamic cost settings during black-box optimization.
The proposed algorithm appears to work across a range of tasks.

Moreover, the paper may provide preliminary supporting evidence that multi-step planning can improve performance over single-step algorithms.

The limitations and potential ethical impacts are well-discussed.

### Weaknesses
 * The paper in its current form does not make a comprehensive argument why multi-step planning may be preferable over single-step planning with optimism. Most single-step algorithms for BO such as the evaluated EI and UCB crucially rely on optimism to explore and prevent getting stuck at a local optimum. The evaluation of these baselines is limited (as I discuss in the following) and in its current form, is not fully convincing.

* While one of the key motivations behind this work, appears to be the practical importance of dynamic costs, the paper does not really address this in its evaluation.
While the proposed algorithm, balances performance and cost via the hyperparameter $\lambda$, while the employed performance measure (Bayesian cumulative regret) does not take into account cost at all. It is not clear how costs are evaluated within the experiments of Section 4.1. Furthermore, based on this, it also unclear how baselines take into account costs. The authors mention that the evaluate across multiple hand-designed costs, but how these costs are reflected in the experiment is not discussed.

Experiments on synthetic functions:

* In Figure 2, the various approaches are evaluated with *different* initial conditions. In my opinion, the initial conditions would have to be fixed across all methods for the results to be interpretable.

* A more general concern I have with the experiments is the evaluation of the baselines, in particular, the hyperparameter choices. It is well known that BO methods are sensetive to their hyperparameters to ensure sufficient levels of "optimism" not to get stuck in local optima (e.g., the $\beta$ in UCB). Moreover, the choice of kernel (*output scale & length scale*) critically influences whether methods will get "stuck" or find the global optimum. I did not find any details regarding this in the paper, nor any ablation studies. In my opinion, those are needed to be able to trust the results.

Experiments on protein design: I find the discussion of the experimental setup not very detailed (see my questions) and not related enough to preceding sections to interpret the results. Overall, the setting appears to depart significantly from the previously discussed setting and several details of the approach remain unclear.



More minor pointers:

* The key novelty the paper claims about the proposed algorithm is the application of variational optimization to non-myopic BO. The paper cites [1] as reference for variational optimization of designs (line 241), but should cite [2]. Moreover, [1] which is a follow-up to [2], proposes a non-myopic approach to experiment design. This present paper claims to be "more robust" than their approach (DAD), as far as I can see, without presenting empirical evidence.

* The paper discusses that computing the GP posterior has cubic complexity in the number of inducing points, but this can be reduced when using Bayesian linear regression with suitable features (e.g., random Fourier features, [3]) which can approximate the GP posterior to an arbitrary accuracy.

### Questions
* The paper discusses the idea of "pathwise sampling" in lines 276-. Can the authors clarify how this approach of sampling a function from the probabilistic model and then optimizing a sequence of steps over this (now fixed) function is different from trajectory sampling [1] used in PETS, with similar ideas being used in model-based RL with PILCO [2]?

* Why did the authors choose 64 restarts? Are the results meaningfully different with a different number of restarts? Requiring such a large number of restarts seems like a drawback of the proposed approach. Moreover, it would benefit the manuscript to explain what is meant by a "restart"; I assume it refers to starting the optimization process from multiple initial conditions.

* It is mentioned that the MSL method is not applicable to "real-world" tasks and referred to Section 4.2 (line 395), but I do not find any reference to MSL in the following.

Questions regarding experiments on protein design:

* Given that predictions of an LLM are used as the "ground-truth" fluorescence levels, could the protein sequence with large edit distance (Figure 4) be outliers / wrong predictions of the LLM? Otherwise, what are alternative explanations for the S-shaped curve in Figure 4?
* How are the hyperparameters chosen? Are they chosen on the validation set over which is also optimized?
* Why is the edit distance represented in the reward value (via $g$) and not only in the cost?
* How is $\lambda$ chosen?
* How does the regret reflect the cost of the chosen protein? That is, in what sense does the cost function $c$ affect the outcome of the empirical evaluation at all?
* It is not clear to me how the authors optimize the variational objective with the *non-Bayesian* LLM in this setting. Can the authors clarify in more detail how this is related to the algorithm proposed in the main text?
* It is mentioned that steps sometimes "fail" (line 494). Can the authors elaborate what is meant by this and clarify how often it fails for each of the discussed baselines?
* The paper provides no details on how the baselines are evaluated in this setting. Can the authors clarify this? In particular, can the authors clarify how "uncertainty" is measured in this context when we do not have a Bayesian model (as in the case of Llama-3.2). Or is a Bayesian linear regression uses, in which case I wonder how this can be compared to the Llama-3.2 policy network used in the proposed approach?

[1]: Chua et al. Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models.
[2]: Deisenroth et al. PILCO: A Model-Based and Data-Eﬃcient Approach to Policy Search.

### Soundness
2

### Presentation
2

### Contribution
2
