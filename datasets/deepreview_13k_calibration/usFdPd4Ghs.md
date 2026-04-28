# Deep Kernel Posterior Learning under Infinite Variance Prior Weights

- Decision: Accept
- Avg Score: 6.80
- Scores: 5, 8, 5, 8, 8

## Abstract
\citet{RadfordNeal1996} proved that infinitely wide shallow Bayesian neural networks (BNN) converge to Gaussian processes (GP), when the network weights have bounded prior variance. \citet{ChoSaul2009} provided a useful recursive formula for deep kernel processes for relating the covariance kernel of each layer to the layer immediately below. Moreover, they worked out the form of the layer-wise covariance kernel in an explicit manner for several common activation functions. Recent works, including \citet{aitchison2021deep}, have highlighted that the covariance kernels obtained in this manner are deterministic and hence, precludes any possibility of representation learning, which amounts to learning a non-degenerate posterior of a random kernel given the data. To address this, they propose adding artificial noise to the kernel to retain stochasticity, and develop deep kernel inverse Wishart processes. Nonetheless, this artificial noise injection could be critiqued in that it would not naturally emerge in a classic BNN architecture under an infinite-width limit. To address this, we show that a Bayesian deep neural network, where each layer width approaches infinity, and all network weights are elliptically distributed with infinite variance, converges to a process with $\alpha$-stable marginals in each layer that has a conditionally Gaussian representation. These conditional random covariance kernels could be recursively linked in the manner of \citet{ChoSaul2009}, even though marginally the process exhibits stable behavior, and hence covariances are not even necessarily defined. We also provide useful generalizations of the recent results of \citet{LoriaBhadra} on shallow networks to multi-layer networks, and remedy the computational burden of their approach. The computational and statistical benefits over competing approaches stand out in simulations and in demonstrations on benchmark data sets.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The authors consider Bayesian neural networks in the infinite-width limit under infinite variance priors on the weights. They show that the resulting covariance kernel becomes a random process that depends on the given data, in contrast to the finite variance prior case, where the kernel is deterministic. Additionally, they demonstrate that the representation in each layer is Gaussian when conditioned on the associated covariance realization. In the experiments, they show that the data-dependent stochastic covariance enables feature learning, and that the resulting predictive Gaussian process achieves improved performance on benchmarks.

### Strengths
- The technical aspects of the paper appear solid, although I have not checked the results in detail.
- The experiments seem to effectively support the theoretical claims.

### Weaknesses
 - The paper is somewhat challenging to approach, given its niche topic and highly technical content. It also feels quite text-heavy.


### Questions
Q1. Can we summarize the key points as follows: Under a specific infinite variance prior, the covariance kernel becomes a stochastic process at each layer. Even if the marginal does not exist, sequential sampling is still possible. Furthermore, conditioning on a covariance sample at a given layer yields a Gaussian representation, while marginalizing over the covariance leads the representation to follow a heavy-tailed distribution centered at 0.

Q2. You could perhaps include a 1-dimensional regression example to illustrate the model’s behavior for varying $\alpha$. Additionally, it might be helpful to show the covariance matrix to demonstrate its properties and the correlation among input data.

Q3. Could you clarify the technical differences between the current paper and Loria & Bhadra (2024), which makes the approach feasible?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
**Summary**
Neal's infinite width neural networks, even when extended to the deep setting, do not account for representation learning. That is, they result in a GP with a fixed covariance function. This is unlike typical but intractable Bayesian neural networks, which are capable of representation learning. The authors consider heavy tailed priors, elliptically distributed with infinite variance, and show that the network converges to a process with $\alpha$-stable marginals. Each layer is conditionally Gaussian, even though the covariances are not necessarily even defined.  The main technical tool is the CLT for alpha-stable RVs (Theorem 4 from another paper, with alpha=2 being the classical CLT), and a (conditionally Gaussian) Gaussian mixture representation of the characteristic function of the alpha-stable RV (equation (1)). Furthermore, a computationally viable MCMC method for doing inference is also provided. The derived method is demonstrated on some UCI benchmarks, showing better prediction than other methods, and being faster than a previous heavy-tailed method.

### Strengths
**Strengths:**
- The proposed model is capable of representation learning. Specifically, Proposition 3 nicely shows that the feature at layer l depends on the data X, y observed in training, which is unlike many finite width models. It is nice to have this notion of representation learning formalised in this simple way.
- The idea of the paper is relatively straightforward: everything is conditionally Gaussian given this scale parameter, which induces the heavy-tailed behaviour. I see this simplicity as a strength, as it doesn't require complicated constructs to convey a nice and useful result.
- The method is demonstrated, firstly on some artifical but enlightening discontinuous functions (where it either almost matches the shallow stable process or is able to compute a posterior where the shallow stable process fails), and also on some UCI benchmarks, where it usually outperforms other methods and the previous shallow stable process is intractable. There are also some nice graphics comparing the posterior predictives of other models in 1D and a QQ plot showing non-Gaussian behaviour of the features. More extreme non-Gaussian behaviour is shown in the appendix (in particular, Figure 10 - I am wondering why the authors did not choose to include this as their main non-Gaussian demonstration in the main paper?)
- Appendix B and D, which contain the proofs, appear to not have any major technical errors.

### Weaknesses
 **Weaknesses:**
- Unless I am mistaken, "The key finding is that the conditional mutual information decays at a slower rate for smaller α" should be "The key finding is that the mutual information [which itself is computed via MCMC as an expected conditional mutual information] decays at a slower rate for smaller α." Figure 1 shows a mutual information, not conditional mutual information.


**Minor:**
- Theorem 1. $J_\delta(\theta)$ can be computed explicitly, and this is obvious to people familiar with the result of Cho & Saul (as mentioned in the following paragraph). But some readers might find it alarming to see $J_\delta(\theta)$ before it is defined. Perhaps the result of Cho & Saul could be made more explicit before theorem 1 (i.e. move $J$ up in the page)
- Figure 1 and 2 labels are too small. Sans-serif font clashes with the text in the main paper.
- last sentence of first paragraph of section 4.2 seems to have odd grammar.

### Questions
**Questions:**
- I don't understand this sentence, could you please clarify? "The third limitation is one noted by Neal (1996), that in the case of multiple outputs, GPs cannot learn the covariance structure, as the covariance is always zero under a Gaussian limit." Are you saying that for a vector-valued neural network output, any two outputs are independent? This would be false, even in the finite variance setting, as long as one considers non-isotropic Gaussian weights (which is relatively straight-forward). E.g. see weights W in section 1 of "Avoiding Kernel Fixed Points: Computing with ELU and GELU infinite networks, AAAI 2021".
- Another related work might be "Richer priors for infinitely wide multi-layer perceptrons". In particular, Theorem 1 and Proposition 2 seem to show that the resulting posterior predictive distribution also marginalises out an $\alpha$-stable distributed scale matrix in the covariance matrix. This seems similar to equation (19), where a scale and a location parameter are integrated out in the posterior predictive, and the resulting model is a kind of infinite mixture of GPs. Although I think the motivation for considering such infinite mixtures is different: this paper focusses on heavy tailed whereas the other one focusses on exchangeability, and considers more "mild" mixing. Still, it could be nice to motivate the current approach both from the perspective of heavy-tailed priors and from the perspective of exchangeability in the hidden layers.
- Is it possible to construct deep $\alpha$-stable processes for gradient flow (extending NTK), rather than BNNs?
- As far as I can tell from the proof of Theorem 1 in Appendix B, rectified monomial activations are not strictly required for the proof to work. All that is required is that a recursive equation for the conditional covariance is available, which is true beyond this activation for other activations (see e.g. the works I mentioned above). It might be nice to extend the theoretical statement to more broad activation functions.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The article presents a deep kernel process with infinite variance priors including a recursive formula and experiments illustrating dependence on the inputs and behavior for discontinuous targets.

### Strengths
The article 
* provides a discussion of references, theoretical results, and experiments. 
* discusses potential benefits in prediction and uncertainty quantification. 
* suggests feature learning that is not possible under a Gaussian process.

### Weaknesses
1. My main concern with the article is the writing and presentation, which I think need to be improved. 
The abstract gives a long discussion of prior works but ideally it should instead give a crisp description of the main points in the article. The lengthy discussion in the introduction comments on prior works and perceived limitations, but does not provide a sufficiently concise and clear description of the objective, motivation, and contributions of the present work. Terminology could be introduced more clearly in preliminaries, rather than in prior works. The writing is in parts repetitive and the thread is not sufficiently clear.  


Suggestions proposed by the ICLR Associate Program Chair: 
    1. Revise the abstract to focus on succinctly stating the key contributions and results of the paper, rather than discussing prior work.
    2. Restructure the introduction to clearly state the objectives, motivation and main contributions upfront before discussing related work.
    3. Add a preliminaries section to introduce key terminology and concepts.
    4. Review the paper to remove repetition and improve the logical flow of ideas between sections.  


2. My second concern is the motivation and innovations, which I do not find sufficiently clearly articulated in the article. 
For Theorem 1 it is mentioned that the result permits characterization of the deep kernel process in an infinite variance setting and for Proposition 3 that it results in a posterior distribution of the features that depends on the observations. I can see that there are differences to prior works and that feature learning is an interesting topic, but in my opinion it is not sufficiently clearly explained what the motivation is for formulating this particular deep kernel process. Another point that is not described in sufficient clarity is what the concrete and significant conceptual and technical innovations are that go into obtaining the proofs and how they could be useful for obtaining further relevant advances.  


Suggestions proposed by the ICLR Associate Program Chair: 
    1. Provide a clearer explanation of why an infinite variance setting is important or beneficial for deep kernel processes.
    2. Discuss more explicitly how the ability to learn features from observations addresses limitations of previous approaches.
    3. Highlight the key technical challenges in proving Theorem 1 and Proposition 3, and how overcoming these challenges advances the field.
    4. Explain potential applications or extensions of their technical innovations beyond this specific model.
    5. Provide a clearer explanation of why this particular deep kernel process formulation was chosen and what advantages it offers.  


3. Description of the experiments. 
In my opinion the motivation and description of the experiments are not sufficiently clearly presented.  


Suggestions proposed by the ICLR Associate Program Chair: 
    1. Provide clearer motivation for each experiment, explaining how it relates to the theoretical results.
    2. Improve the description of experimental setups, including details on datasets, baselines, and evaluation metrics.
    3. Discuss the implications of the experimental results in more depth, relating them back to the theoretical contributions.

### Questions
* Could the authors please offer more comments on the motivation for considering this particular model? 
* Could the authors please offer comments on what the concrete and significant technical advances are?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
Although deep kernel processes allow for more flexibility than standard GPs, they still assume smoothness and finite variance, which is unsuitable for modelling data with heavy tails or discontinuities. This is particularly relevant to representation learning, where deterministic covariance kernels limit the ability to learn non-degenerate, data-dependent representations. In contrast, $\alpha$-stable distributions are well-suited to problems were large fluctuations or discontinuities can be expected. Taking inspiration from these strengths, in this paper the authors assign $\alpha$-stable distributions with infinite variance to the weights in each layer of a BNN, such that the BNN now converges to a deep $\alpha$-stable kernel process rather than GP in the infinite-width limit.

They also develop conditional Gaussian representations of $\alpha$-stable processes that allow for recursive computation of the stochastic kernels at each layer. Through a combination of numerical experiments on synthetic discontinuous functions and evaluations on widely-used datasets from the UCI repository, the authors demonstrate that the deep $\alpha$-stable kernel process outperforms competing approaches when modelling discontinuous or heavy-tailed data. However, simpler models or GPs with traditional Gaussian priors might be preferable for smoother data due to their lower computational cost.

### Strengths
- Due to my limited familiarity with α-stable processes, I didn’t review all of the theoretical details. However, the paper reads as well-structured and complete, and the writing clearly highlights the contributions in the context of prior work with a solid mix of theoretical grounding, ablation studies, and performance benchmarks on public datasets.
- The problem statement is otherwise well-described, and I think this work should be of interest to future work on BNNs by addressing core limitations of smoothness and finite variance in existing models. I also wonder whether the non-Gaussian priors explored in this work could also be considered in other deep models?
- I appreciated the extensive numerical experiments that showcased the model’s performance in controlled settings that properly validate it meets the intended criteria of modelling non-Gaussian behaviours. I do wish the section real-world datasets was more compelling however.

**Post-rebuttal update**

Raised score from 6 to 8.

### Weaknesses
Although the paper is well-written overall, the dense presentation of different concepts makes it challenging to intuitively grasp without visual aids or simplified examples. I would recommend the inclusion of more figures illustrating how the α-stable kernel process differs from traditional GPs, ideally showing its behavior on simple synthetic data to highlight the flexibility and stochasticity introduced by their method. Some detail can likely also be moved to the appendix instead. The lack of visual aids makes it difficult to understand the practical implications of using α-stable distributions, especially how the tail behavior impacts the learned kernels. For example, a visualization of the kernel's shape under different α values would be beneficial. Furthermore, while the real-world datasets are at par with other GP literature, the analysis could be more compelling by including a wider range of datasets with varying degrees of discontinuity or heavy-tailed noise to better demonstrate the model's strengths and limitations. The current selection of datasets does not fully showcase the unique advantages of the proposed approach over standard Gaussian process models.

### Questions
N/A

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper considers an infinite-width Bayesian neural network, with infinite-variance weights.  Interestingly, in this setting, representations/kernels do not become deterministic as usual in infinite-width limits, but remain stochastic, and hence learnable.

### Strengths
The theoretical contributions are extremely strong.  They consider an extremely interesting regime, and the question of how to avoid deterministic kernels in infinite-width networks is a critical one for Bayesian neural networks.

They have an extensive and excellent Appendix.

### Weaknesses
The experiments are weaker, but this can be expected in a paper with a mainly theoretical focus and contribution, such as this one.

### Questions
N/A

### Soundness
3

### Presentation
3

### Contribution
3
