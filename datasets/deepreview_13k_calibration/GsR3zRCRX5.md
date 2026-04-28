# Robust Simulation-Based Inference under Missing Data

- Decision: Accept
- Avg Score: 6.17
- Scores: 8, 8, 6, 6, 6, 3

## Abstract
Simulation-based inference (SBI) methods typically require fully observed data to infer parameters of models with intractable likelihood functions. However, datasets often contain missing values due to incomplete observations, data corruptions (common in astrophysics), or instrument limitations (e.g., in high-energy physics applications). In such scenarios, missing data must be imputed before applying any SBI method. This work formalizes the problem of missing data in SBI and demonstrates that naive imputation methods can introduce bias into the SBI posterior. We introduce a novel method that addresses this issue by jointly learning the imputation model and the inference network within a neural posterior estimation (NPE) framework. Extensive empirical results on SBI benchmarks show that our approach provides robust inference outcomes compared to baselines, for varying levels of missing data, while being amortized.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper introduces a method for addressing the issue of missing data in the context of
simulation-based inference (SBI). The approach uses neural processes to learn an
imputation model from simulated data and then combines the learned imputation model
with standard neural posterior estimation (NPE) to perform SBI. The authors first show
how previous approaches for addressing missing data with zero- or mean-value imputation
can lead to biased SBI posteriors. They then evaluate their approach on a set of
tractable SBI benchmarking tasks and two intractable tasks. Additionally, they perform
ablation studies and show how their method can be extended to generalize over different
levels of missingness in the data.

### Strengths
The paper is well-written and clearly structured. The figures are visually appealing,
and the results are reported over a reasonable number of repetitions and with error
bars. The introduction and background section are concise and easy to follow, except
maybe for section 3.3, for which additional background is given in the appendix.

### Originality

The paper addresses a known problem that has been tackled in the field of SBI before.
However, it shows that previous approaches had limited success. It then proposes a new
method that combines techniques from existing research on learning imputation. Thus,
overall, using neural processes for learning imputation models for neural SBI is not a
strong technical contribution in itself, but can still be a valuable contribution to the
field of SBI. However, while most of the related work on missing data in SBI is cited
accurately, it seems that the work by Gloeckler et al. is actually very similar to the
approach proposed here. See below for details.

### Quality

The derivations for combining imputation models with NPE appear technically sound. The
experimental results support the initial claims that the proposed method is more robust
to missing data than the baselines. However, the choice of performance metrics and the
comparison to previous methods should be improved (see below).

### Clarity

As mentioned above, I believe the paper is presented quite clearly. What I am missing is
a discussion of the potential limitations of the presented method, see below.

### Significance

The paper addresses an important problem in the field of SBI, as actual SBI applications
usually deal with real-world observations that often have missing data. This problem has
gained only little attention in the literature so far. If the concerns on the evaluation
listed below are addressed and the method turns out to perform better than previous
approaches, it will be a valuable addition to the field.

### Weaknesses
### Missing discussion of previous work

- There is one early SBI paper that addressed imputation in SBI that is missing and
  should be discussed: Lueckmann et al. 2017 automatically learn imputation values for
  NPE using an MDN embedding network, actually on the same Hodgkin-Huxley benchmark as
  used here. A discussion of this paper and a comparison to their proposed method would be
  appropriate. In particular, in section 3.3 and figure 4, they use an imputation model in the last layer of the MDN, to which you could 
  compare. A comparison to this approach could be straightforward as your NPE-NN baseline approach seems quite similar to their 
  approach. Ideally, you can show how your approach leads to more accurate imputation values on the benchmarking or the HH task, as 
  they actually observed that their learned imputation values tend to be close to the sample mean of the feature. 

- The discussion of the work by Gloeckler et al. is not accurate. The Simformer actually
  learns the imputation of the missing data as well. In that sense, it is actually very
  similar to the approach proposed here. Relating to the example given in the paper:

  > However, this method estimates the partial posterior distribution p(θ | x1, x3)
  > given x = [x1, x2, x3, x4, x5], where x1 & x3 are the only observed variables,
  > without considering the mechanisms that lead to missing data.

  This is not correct. The SIMFORMER can perform *arbitrary* conditioning and
  evaluation. Thus, when given only x1 & x3, it can actually predict p(θ, x2, x4, x5 |
  x1, x3), which then serves as an imputation model for the missing data points (e.g.,
  just sampling from p(θ, x2, x4, x5 | x1, x3) and ignoring x2, x4, x5 would amount to
  obtain an approximation to p(θ | x2, x4, x5, x1, x3)).  A more detailed and more
  accurate discussion of this work would be essential here. The code for applying the
  Simformer is available at https://github.com/mackelab/simformer and appears to be
  well-documented. Ideally, it would possible to show on one of the benchmarking tasks how RISE leads to better imputation by being able to explicitly model different types of missingness, which seems to be the distinctive feature compared to the Simformer. 

### Choice of performance metrics

The choice of MMD and RMSE is not ideal. MMD can be misleading depending on the choice
of kernel bandwidth (Lueckmann et al. 2021) and RMSE seems to measure accurate parameter
discovery, although posteriors do not have to be centered on the true parameters at all.
I suggest the following
- In addition to MMD, calculate **C2ST** as well as it gives an absolut and interpretable and not just a relative comparison to reference posteriors. 
- instead of RMSE, calculate the the **nominal log posterior probability**, i.e., obtaining the NPE posterior for each x in the test set,
and then averaging in the log probs of the corresponding thetas (as done in Papamakarios
et al. 2019, Greenberg et al. 2019, and discussed in detail in Lueckmann et al. 2021). The log nominal density, when averaged over many test data points, is a relative comparison metric of posterior accuracy. This would be more appropriate than using RMSE because it measures posterior accuracy and not just parameter discovery accuracy. 

Additionally, it would be good to also evaluate the calibration properties of the
inferred posteriors, e.g., by calculating the SBC or expected coverage, at least on the
four benchmarking tasks. This will show how well-calibrated the different methods are.

### Discussion of data and computational requirements

It would be essential to give more details on how the training data set for RISE is
constructed. Given the large number of additional NN parameters required for training
the imputation model, I would expect that RISE needs more simulations for training
compared to naive imputation or NPE-NN. Concretely, how many simulations where used for training RISE, or more generally, what are the simulation budgets used for the different benchmark tasks and methods?

Same for the computational resources. How much more effort in terms of data and
resources does the user have to put in in order to use RISE? It would be good for the reader to see comparisons of training time and memory usage of the different methods.

### Questions
What are the simulation budgets used for the different benchmarks and methods?

### Soundness
3

### Presentation
3

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
The paper emphasizes the problem of missing data in simulation-based inference (SBI) and proposes to learn a latent variable model of the predictive imputation distribution . This problem has a long-standing tradition in statistics and probabilistic modeling and extends way beyond SBI. However, it has received relatively little attention in the SBI literature, one reason being that simple data augmentation approaches are sufficient in most cases. The main value of the paper lies in the generality of the proposed method, which is clearly justified and well motivated.

### Strengths
- The paper is clearly written and easy to follow; it can be appreciated by both readers familiar with SBI and newcomers to the field. It addresses an important practical problem and is of interest to the community.

- The joint training of a posterior surrogate and latent variable missing data model is original, quite general, and useful for SBI applications where the simulator is cheap to run.

- The evaluation features a variety of different models (even though the selected four SBI benchmarks are rather uninteresting and not specifically designed to assess the impact of missingness).

### Weaknesses
 *Major points*

- The first contribution, namely, the “formalization” of the problem in SBI, is a bit of a stretch, as it is simply the standard missing data setting (i.e., equations 2–3 are not specific to approximate posteriors obtained via SBI). Propositions 1 and 2 are straightforward, and there is some notational confusion which may lead one to think that $x_{obs}$ is the real (non-simulated) data, while it is just a partition of the simulated data. Why not simply write the expectation as running over the augmented joint model $p(x_{miss}, x_{obs},\theta)$ in Proposition 2? The current presentation obscures the fact that the core challenge is handling the missing data component within the simulation output, which is a well-trodden path in statistics.

- The method is somewhat of an overkill for simple data, such as the 1D Ricker model used to pitch it, where the bias can easily be eliminated via data augmentation and a missingness mask provided as an additional input to the network. The demonstration in Figure 1 is simply bad practice and an example of model misspecification, as the networks have never seen imputed values during training. The work by Wang et al. (2024) is also somewhat misrepresented in the current paper, as they do not simply impute the data with constant values but use data augmentation and a mask indicator, which can be a much more efficient, albeit less sophisticated, approach for simpler cases (e.g., MCAR / MAR) [see also point on potential difficulties in learning the imputation model]. The paper should more clearly acknowledge the limitations of the proposed method for low-dimensional data with simple missingness patterns.

- The paper lacks key ablation studies demonstrating the impact of a bad $p(x_{miss}∣x_{obs})$ model. I assume such a model will lead to unreasonable variance inflation of the posterior and hence miscalibration (see next point). The authors themselves acknowledge that “learning the imputation model correctly is central to RISE’s performance,” so it seems paramount to quantify the impact of approximation error in $p(x_{miss}∣x_{obs})$. Specifically, the paper should investigate how the quality of the learned imputation model affects the accuracy and uncertainty quantification of the final posterior.

- It is important to add calibration error as an additional, practically relevant coverage metric to all experiments, besides simply looking at MMD and Bayes RMSE. I suspect—and am open to being proven wrong—that difficulties in learning $p(x_{miss}∣x_{obs})$ will result in rather poor calibration, which can easily go undetected by RMSE or MMD (values are heavily kernel-dependent). The paper should include metrics such as expected coverage or probability calibration error to assess the reliability of the posterior estimates.

*Minor points*

- The notation needs some polishing, e.g., bold font is used for data vectors, but parameter vectors are not bold. On a related note, I believe it would be informative to introduce precise notation for sequences of vectors vs. vectors and focus the discussion on sequences, since, e.g., missing points in set-based data can be trivially handled by summarizing the reduced set, whereas missing points in temporal or spatiotemporal data present a real challenge. The paper should clarify the scope of the method with respect to different data structures and missingness patterns.

- Some citations have inaccuracies, e.g., Gloeckler et al. is not an arxiv paper but an ICML paper, Radev et al. (2022) should be Radev et al. (2020), and so on.

- It would be nice for **Algorithm 1** to illustrate that the method results in an ensemble of posteriors (i.e., one for each sample from the imputation model) and that this ensemble uncertainty is integrated out for inference.

- I could not find any details on simulation budgets for the experiments. It would be nice to quantify performance as a function of simulation budget in at least one of the experiments.

### Questions
- What are the benefits of learning a latent variable model for the predictive missing data distribution instead of directly parameterizing it using another flexible generative network (e.g., a diffusion model)?

- What is M in equation 7?

- What are the error bars computed over in Figures 3 and 5?

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
4

### Summary
This paper addresses the problem of missing data in simulation-based inference (SBI). The authors formalize how missing data can introduce bias into SBI posterior estimates when naive imputation methods are used. They propose RISE (Robust Inference under imputed SimulatEd data) to tackle this issue. This novel method jointly learns an imputation model and an inference network within a neural posterior estimation (NPE) framework. The imputation model is based on neural processes, allowing RISE to handle different missingness mechanisms (MCAR, MAR, MNAR). The method is amortized and can be generalized across varying levels of missingness. Extensive experiments on SBI benchmarks demonstrate that RISE outperforms baseline methods in inference and imputation tasks.

### Strengths
- **Contribution**: The paper tackles a significant and underexplored problem in SBI—handling missing data—and provides a novel solution by jointly learning imputation and inference models.

- **Theoretical foundation**: The authors provide a formal analysis showing how naive imputation leads to biased posterior estimates, strengthening the motivation for their method. The cases for MNAR, MAR, and MCAR have been nicely formalized. The simplification of $\mathcal{L}\_{RISE}$ by $\mathcal{L}\_{NPE}$ in Proposition 2 is particularly convenient.

- **Amortization**: The method can generalize across varying levels of missing data (RISE-Meta), making it practical for real-world applications.

### Weaknesses
 - **Clarity of presentation**: Some parts, particularly the mathematical formulations and explanations of the method, could be clearer. For instance, in Section 1 (Introduction), the authors refer to Figure 1, which has the axes $\theta_{1}$ and $\theta_{2}$ but only in Section 2 (Preliminaries) define what $\theta$ is.

- **Literature for handling missing values is limited**: While the literature review mentions prominent methods for handling missing values from the deep learning literature, such as GAIN [1], more traditional and frequently used techniques have been excluded. For example, the authors could have compared their methods or, at the very least, acknowledged imputation techniques such as expectation-maximization (EM) found even in the deep learning literature [2] and other traditional approaches such as MICE [3].

- **Computational efficiency**: The paper does not provide a detailed analysis of the computational cost of RISE. This is especially true because the paper uses normalizing flows, which can be computationally expensive. Given the added complexity of jointly learning the imputation model and the inference network, it would be useful to understand the trade-offs.

- **Some important limitations, such as the Gaussian assumption, have not been highlighted**: Even though the authors mention in line 255 that the Gaussian assumption does not limit the expressivity, this is still a limitation that has to be clearly highlighted. The argument for infinite mixtures may be valid theoretically but computationally infeasible. This is especially true as the authors mention in line 476 that the credibility of the posterior estimates needs to be further examined, which is directly impacted by the normality assumption.

- **Source code for reproduction**: It would have been good to have the source code available for a more careful examination and reproduction of the results.

### Questions
- **Confusion in the contributions**: As mentioned above, in line 84, the most important contribution of the paper is that the proposed method is 'robust' to shift in the posterior distributions, but at the same time, the authors mention that the credibility of the posterior estimate after imputation remains an area for exploration. This seems contradictory. Can the authors clarify this point?

- **Discussion of possible alternatives**: Why not use the EM algorithm?

- **Extension to multiple observations**: I didn't quite understand if RISE can be extended to handle multiple observed data points per parameter setting. If so, what modifications would be necessary?

- **Small remark on the structure of Section 5**: I initially missed the referred datasets. Is it because you once showed the SBI benchmarks and the other datasets (Adrenergic and Kinase)? Section 5 was structured confusingly; I recommend restructuring it or adding a small paragraph before *performance metrics*  to more clearly explain the section structure for the datasets.

- **Sensitivity to neural process architecture**: How sensitive is the performance of RISE to the choice of neural process architecture and hyperparameters? Have the authors conducted ablation studies on this aspect?

- **Computational efficiency**: Can the authors provide insights into the computational complexity of RISE compared to baseline methods? How does training time scale with data dimensionality and missingness levels?

- **Handling model misspecification**: While the paper assumes a well-specified simulator, how would RISE perform under model misspecification? Can the method be adapted to account for this?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper explores the challenge of SBI under conditions of missing data and introduces a novel method named RISE. By integrating Neural Posterior Estimation (NPE) with neural processes, RISE effectively tackles the problem of missing data. Experimental results show that RISE offers a more robust posterior estimation than other imputation methods across varying levels of missingness.

### Strengths
This work presents the RISE method, which innovatively combines data imputation and neural posterior estimation to address the issue of missing data in SBI. This combination is novel within the SBI domain. The authors have validated the effectiveness of the method using multiple benchmark models and real-world datasets under various experimental settings. The paper is well-organized and the figures are easy for readers to understand.

### Weaknesses
1. Reporting of Benchmark Metrics:

The authors report only MMD and RMSE as performance metrics. However, additional metrics commonly used in SBI literature or benchmarks [1] would provide a more comprehensive evaluation. For example, metrics like the negative log probability of true parameters (to assess the density of true parameters $\theta$ within the approximate posterior), median distances (to evaluate the distance between samples generated from $\theta$ under the approximate posterior and observations), and Classifier 2-Sample Tests (C2ST, to measure the closeness between approximate and true posteriors) are not included in this paper. C2ST is sensitive to subtle differences between distributions in high-dimensional spaces, potentially revealing nuances that MMD may miss due to kernel dependence [2]. Specifically, the lack of metrics that directly assess the quality of the posterior samples, such as the probability of the true parameters under the learned posterior, makes it difficult to assess the calibration of the method. The median distance, which measures the discrepancy between the simulated data from the posterior and the observed data, is also crucial for evaluating the practical utility of the inferred parameters.

To enhance the robustness and comprehensiveness of the evaluation, I recommend the authors include C2ST as an additional metric, and also include metrics such as the negative log probability of the true parameters and median distances.

2. Comparisons to NPE-Zero and NPE-Mean:

The RISE method is compared with NPE-Zero and NPE-Mean methods, which fill missing inputs using zeros or sample means (Line 48, 323). These two imputation strategies are overly simplistic and introduce significant bias (as seen in Figure 1.(c)), resulting in biased posterior distributions. While these baselines are easy to implement, they do not represent the state-of-the-art in handling missing data. For a more rigorous comparison, it may be helpful to add a baseline such as Gloeckler et al. (2024) under the MCAR cases (Line 289). This would provide a more meaningful comparison against a method designed for missing data scenarios, rather than just simple imputation techniques.

3. Choice of Conditional Density Estimator:

For the conditional density estimator, the authors do not use the Neural Spline Flows (NSFs) structure [3] employed in the SBI library. The NSFs is more performant and flexible than MAFs and has been widely used for SBI tasks in recent works [1, 4, 5, 6]. The choice of MAFs over NSFs is not justified, and it is unclear if this choice impacts the overall performance of RISE. It would be helpful if the authors provided a rationale for selecting MAFs over NSFs or included an ablation study comparing RISE performance using MAFs and NSFs. The use of NSFs could potentially lead to better posterior approximations, and this should be explored.

### Questions
1. The RISE loss function (Eq. (5)) includes two parts: $\hat{p_\varphi} $ to generate $x_{mis}$ given $x_{obs}$, and $q_\phi$ to generate $\theta$ given $x_{obs}$ and $x_{mis}$. Can these two parts be trained separately? Alternatively, is it possible to train a flow directly from $x_{obs}$ or $(x_{obs}, c_{obs})$ to $\theta$?

2. (For Weaknesses 2): In Line 289, the authors mention that the method proposed by Gloeckler et al. (2024) is unequipped to handle MAR and MNAR cases. Why not compare this method with RISE under MCAR cases?

3. (For Weaknesses 2): Could the authors include additional illustrations to show how the summary statistics produced by their data imputation method deviate from the true statistics, similar to what is shown in Figure 1.(c)? I believe this would help clarify why the RISE method reduces posterior bias.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes an approach to deal with missing data in the simulation-based inference (SBI) setting. In SBI, parameters are to be inferred for a model with an intractable likelihood function. The authors propose an imputation approach utilising latent neural processes, in which parameters of the neural process and the posterior estimator are jointly optimised. The resulting method (RISE) is compared against alternative approaches on a number of problems showing good performance in terms of MMD and RSME.

### Strengths
- The paper addresses are timely, relevant topic.
- Motivation and approach are clearly laid out.
- The evaluation spans statistical problems and real world data sets.
- RISE outperforms baselines on problems considered.

### Weaknesses
 - Some comparisons are missing, see questions for details.
- HH example would benefit from quantitative evaluation.
- Previous literature could be cited more accurately, some examples:
  - L46: See also Lueckmann et al. (2017) where NN-based imputation for SBI was used.
  - L50: Citing Radev et al. (2022) for NPE seems out of place, consider crediting NPE to Papamakarios and Murray (2016) and subsequent work based on it.
  - L206: The VAE paper was published in 2013, not 2022.

### Questions
- Have you considered running simulation-based calibration to check posteriors after imputation? This would allow going beyond the qualitative analysis on the HH example.
- How does NPE-NN perform on the HH example?
- What are meta-learning results for the remaining statistical problems (Ricker, OUP)?
- How does RISE compare against the method by Gloeckner et al. for MCAR cases?
- Are posterior distributions for all statistical examples unimodal?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 6

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
The authors provide a method that aims to simultaneously learn an imputation model, alongside a posterior approximation, under an assumed missing data distribution. They fit both models by minimizing the forward KL divergence using samples generated from the assumed models joint distribution (including both missingness and the simulator component). A neural process model is used for imputation, and a masked autoregressive flow for the inference component.

### Strengths
This paper addresses handling missing data simulation-based inference , which is common problem in fields like astrophysics. The experiments include reasonable examples and the results seem to be good. The method is well motivated by including a probabilistic model over the missingness. Overall the paper is clear and well structured.

### Weaknesses
There were a few substantial issues which I feel would need to be addressed.

- From the onset, the paper should make it clear that we are interested in either the case where we have multiple observations, or expect multiple observations, so wish to maintain an amortized estimator. Otherwise, we can simply remove the missing indices from the simulated output, training the posterior estimate only on the observed sites. The examples unfortunately also focus on the single observation setting. The paper does not adequately address the trivial solution of simply removing missing indices in the single observation case, which is a significant oversight given the focus on single observation examples.

- The review of previous work is not sufficiently thorough. For example, the authors state "the latter problem of missing data in SBI has received little to no attention. The only exception is the work of Wang et al. (2024)". A quick search pointed me some other examples https://arxiv.org/abs/2211.03747, https://iopscience.iop.org/article/10.3847/2041-8213/ace361/meta. The summary of Wang et al. (2024) is further very poor, and perhaps should at least mention the use of training the NPE model using augmented simulations with artificially missing values, alongside a missing indicator variable. It is not clearly justified why this approach is a bad idea, especially for flexible neural network conditioning models used in normalizing flows. The related work section fails to mention relevant methods that use kernel density estimation or nearest-neighbor imputation, which are important baselines for handling missing data in simulation-based inference. The discussion of Wang et al. (2024) is also inadequate, failing to highlight the key aspect of using a binary mask indicator during training.

- In my opinion, the notation with $x_{obs}$ is likely to confuse some readers, e.g. as it is used to refer to the subset of simulated data which is not missing in the observed data, not the observed data itself.

- The title itself I would argue is too broad, closer to describing an area of research, rather than being informative to the presented method.

- At least from the objective described in equation 5, I can see no reason to think joint training provides any benefits. The expectation is taken over a fixed distribution, and each model (inference/imputation model) has disjoint parameter sets. From my understanding you could separate the objective into two independent objectives, and expect very similar results, if not identical results, depending on the optimizer. The paper does not provide a clear justification for the joint training procedure. The objective function appears separable into two independent optimization problems, one for the imputation model and one for the inference model, and the paper does not explain why joint training is necessary or beneficial.

- No code has been provided to the reviewers.

### Questions
Does NPE-Mean and NPE-Zero refer to imputing only after training the NPE model? If so, I think it would be better to compare to methods  listed in Wang et al. (2024), which ensure the inference model learns to approximate the posterior using missing data during training. Otherwise, we are simply relying on neural networks to generalize to possibly out of distribution points, which is in my opinion not a fair comparison.

Why might the "joint" training procedure be useful? Have I missinterpreted the fact the objective could be partitioned into two independent objectives?

### Soundness
2

### Presentation
3

### Contribution
2
