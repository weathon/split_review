# DensBO: Dynamic Ensembling of Surrogate Models for Hyperparameter Optimisation

- Decision: Reject
- Scores: 5, 3, 3, 6

## Abstract
Hyperparameter optimisation (HPO) of machine learning models is crucial for achieving optimal performance for different tasks. Surrogate-based optimisation techniques, such as Bayesian optimisation (BO), have been successfully applied to tackle this problem. BO is subject to different design choices of its components. In particular, depending on the nature and the size of the search space, the choice of the surrogate model has a substantial impact on the overall performance of BO. Surrogate models in BO approximate the function to optimise and guide the search towards promising regions by predicting the function value for different solution candidates. Combining different machine learning (ML) models is known to lead to performance gains, e.g., in different prediction tasks. To this end, we propose a novel dynamic approach to ensemble surrogate models in the BO pipeline, leveraging the complementary powers of different surrogate models at different stages of the optimisation process. We empirically evaluate our method on numerous benchmarks and demonstrate its advantage compared to state-of-the-art single-surrogate BO baselines. We highlight the usefulness of our approach in finding good hyperparameter configurations in mixed (numerical and categorical) search spaces for a wide range of problems.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
DensBO offers a novel and dynamic approach to ensemble surrogate models in Bayesian optimization. While some transfer knowledge between tasks have been used in the past, this method uses the dynamic ensemble on the same task. This allows the use of different surrogate models at different stages of the optimization. This might also be useful to deal with numerical and categorical search spaces.
The method trains all surrogate models and creates a weighted ensemble, where the weights are updated using an exponential moving average between the previous and the new weights. At each time step, the surrogate model that has the lowest MSE error on the new sampled points, gets the weight of 1 and zero for the rest.
The paper evaluates the method on YAHPO Gym and JAHS-Bench-201 making use of a total of 859 available instances. The results show that the proposed method outperforms using individual models in Bayesian optimization. While the method comes at the cost of an additional hyperparameter, the paper convincingly demonstrates that the method is very robust as long as the hyperparameter is set to a high value.
Overall, the paper proposes an interesting addition to the Bayesian optimization methodology, that is of general interest to the ICLR, but has one major weakness (see below) due to which I have to rate this paper borderline reject.

### Strengths
The paper is easy to read and understand.
* The paper explains the choices of the surrogate model by DensBO at the different stages of the optimization. Although gradient boosting (GB) is not competitive as a single surrogate model, the authors show that their model can pick random forest (RF)in the beginning of the optimization (few observations) and then dynamically chooses GB when they have a higher number of evaluations.
*  They also show results on different budgets, which is very interesting to point out when the DensBO is not working well. In a small budget Gaussian processes outperform DensBO. In fact, ensembling requires training and querying more than one surrogate model, which means that it increases the overhead of BO, and should thus not be used in very low budget settings.
* Finally, the explanation of the fraction budget used as a hyper parameter. The authors test and explain its effect on the behavior of DensBO.

### Weaknesses
The experimental setup is uncommon for Bayesian optimization and might introduce unwanted bias into the evaluation. Concretely, the models are only updated every eight iterations (see line 819), and references the HEBO documentation and SMAC. However, I cannot find a clear recommendation to do so in the HEBO documentation, and also no trace of this in the SMAC paper [1]. This batch update strategy, while potentially beneficial for parallel computation, deviates from the standard sequential Bayesian optimization paradigm, which could significantly impact the observed performance and generalization of the proposed method. The paper does not adequately justify this choice, nor does it explore the sensitivity of the method to this parameter. Furthermore, the paper does not clearly state that the results are only valid for the parallel setting, which is a major oversight.

Related work does not discuss meta-learning in Bayesian optimization, see for example the work by Martin Wistuba and Nicolas Schilling between 2015 and 2018. These are probably not helpful for solving the problem at hand, but at least should be mentioned. The omission of these relevant meta-learning approaches in BO, which explore transferring knowledge across tasks or using prior information to guide the optimization process, leaves a gap in the contextualization of the proposed method. This is especially important given that the proposed method dynamically selects surrogate models, a concept that shares some similarities with meta-learning strategies.

Additional solutions to the 2021 NeurIPS BBO challenge besides HEBO that ensemble different BO methods are not discussed. In particular, the 2nd place, and the winner of the warm start leaderboard, used extensive ensembling of different BO methods (2nd place) and surrogates (winner of the warm start leaderboard, see also [2]). These omissions limit the paper's ability to position itself within the broader landscape of Bayesian optimization techniques, particularly those that have demonstrated strong empirical performance in challenging benchmarks.

### Questions
* The fact that GPs do not work well on dimensions above 20 has been disputed recently [1, 2]. Also, the provided references about BO with GPs not working for a higher number of dimensions are 7 years old or older. Can you still make this claim using up-to-date-literature?
* Scikit-learn’s implementation of random forests and extremely randomized trees does not handle categorical features - how do you deal with this in practice? (The same might hold for gradient boosting, depending on the scikit-learn class used)
* How is the uncertainty for gradient boosting computed?

References:
1. https://arxiv.org/abs/2402.02229
2. https://arxiv.org/abs/2402.02746

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The authors propose a new surrogate model for Bayesian optimization. They use a weighted ensemble of 4 different surrogates which are weighted best on their prediction performance in the past. This new surrogate is compared to each individual surrogate on several benchmarks with respect to rank.

### Strengths
The paper is well-written and the idea clearly communicated. The paper uses sufficiently many benchmarks. The idea to dynamically choose the most suitable surrogate model during optimization is interesting.

### Weaknesses
The evaluation metric is not a suitable choice for this setup for two main reasons:

1. We have clusters of surrogates: there are 5 variants of ENS, 3 variants of tree-based methods and 1 GP method. Why is this a problem? Let's assume we want to compare GP to ENS on 2 benchmarks. If ENS is better than the GP on one benchmark and the GP better on the other, both would get a rank of 1.5. If we had 5 variants of ENS (where these variants also have a clear ranking among each other), then ENS-best would get a rank of 1 on the problem where ENS does better than GP and a rank of 2 where the GP does better. However, the GP gets a rank of 6 where the ENS variants do better. Thus, the GP overall gets a rank of 3.5 and ENS-best 1.5. Only adding more variants of ENS make the GP look much worse than it is. In my opinion, we should compare 1 ENS variant with a GP and RF (no other tree-based methods).
2. We don't see absolute differences: we see the GP doing initially very well for "cheap" benchmarks. The authors claim to eventually do better. However, differences towards the end of the optimization process might be completely meaningless (small absolute gains).

The approach to set the ensemble weights is not well motivated and not ablated (see "Questions" for ideas what to ablate). I do not understand why this depends on the answer to "which model would have been best in evaluating the current point?" if we continue choosing points somewhere else in the space.

Adding the state-of-the-art for the respective benchmarks would be useful to give a useful baseline for the benchmarks.

Missing baseline: use GP if the problem instance contains only continuous hyperparameters, otherwise use RF

**After review:** I wish the authors had added the missing baseline mentioned above. The authors said that this is computationally infeasible during the short time while they in fact have results for GP and RF on all problems. Therefore, it is not clear to me why a posthoc analysis isn't possible and this appears to be a red flag to me.

### Questions
How important is the initialization of w? What happens if we init all with equal weights?

How well does ENS with oracle w? This means that we choose only the surrogate among the available candidates that did best on the respective benchmark.

What is the motivation for using 3 tree-based models? How would ENS change if there was only RF (best tree-based model) and GP?

How important is it to choose weights based on fit to last observe point rather than general fit?

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors present DensBO, a method which dynamically uses a weighted ensemble of different surrogate models when optimizing the acquisition function.

### Strengths
- The paper is well-written and the method is clearly presented. 
- The ablation with the smoothing factor $\alpha$ is interesting and provides insight into how much the prior performance should impact the ensemble. Furthermore, the promising performance of $\alpha=1.0$ alleviates some of the overhead cost of using an ensemble surrogate model. 
- The authors conduct an extensive empirical evaluation on over 800 optimization problems and demonstrate that their ensemble method consistently outperforms the single models as well as the static ensemble. Furthermore, the ensemble is more effective than individual models when controlling for the total budget as well as controlling for the number of evaluations.
- The experiments are described in detail and the results seem fully replicable.

### Weaknesses
 - This paper does not provide enough evidence that ensembles, and the additional costs associated with fitting multiple models, outperform careful initial model selection across the many different objectives. It would be interesting to see another baseline for “performance of best single-surrogate model for problem”, which would allow us to compare the impact of ideal model selection compared to ensembling. For a more realistic setting, we could also include another baseline of “performance of best single-surrogate model as determined by best MSE on initial points.” If this baseline performs well, this indicates that the overhead cost of ensembles are unnecessary. 
- Furthermore, there is no comparison between DensBO vs other static ensembling methods which carefully select the ensemble model weights (rather than using a naive equal weighting). It is unclear how much of the improved performance originates from the dynamic ensembling proposed from the paper or from ensembling in general.
- While I believe DensBO is the first to use a dynamic ensemble of GP and trees fit to the same BO optimization trajectory, there has been previous work which utilizes dynamic ensembling for BO which are weighted based on model fit [1, 2, 3]. If the claim is that the specific MSE weighting scheme is desirable, it would be helpful to see comparisons with other weighting schemes.

### Questions
- Have you tried running experiments with a different number of starting points? Due to the varying scaling properties of the individual surrogate models, the number of initial points may impact the performance of the methods given a fixed budget. Furthermore, considering your hypothesis about why GB works poorly in line 462, it may be helpful to understand the performance gap.

### Soundness
2

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
&nbsp;

The authors introduce a dynamic ensembling approach for Bayesian optimization considering both continuous and mixed continuous/discrete parameter spaces. A key finding of the authors' work appears to be that model selection (the limiting case of the authors' approach when the exponential moving average weighting parameter alpha is set to 1) outperforms weighted ensembling across the majority of experiments. The empirical findings of the paper are informative and rigorous and as such, I am leaning towards accepting the paper. I do, however, have some major concerns with the baselining of prior work in model selection for Bayesian optimization, namely the approach taken in [6] that I believe should be incorporated. Additionally, the work would be further strengthened if a thorough ablation on the components of HEBO could be performed. Most notably if the model ensembling inherent to HEBO could be decoupled from the ensembling approach the authors' introduce. I will upgrade my score if these concerns can be addressed during the rebuttal phase, albeit I understand it will require extensive work on the part of the authors.

&nbsp;

### Strengths
&nbsp;

1. The empirical evaluation of the authors' method is extensive and offers conclusive evidence that dynamic model selection outperforms a single surrogate model and a static ensemble across a suite of continuous and mixed continuous/discrete hyperparameter optimization tasks.

2. The authors codebase is well-documented and I am led to believe that the results are fully reproducible.

3. The paper is written in a clear and objective fashion.

4. The finding that model selection outperforms a weighted ensemble in the majority of experiments is a very interesting finding for the Bayesian optimization community.

&nbsp;

### Weaknesses
 
**MAJOR POINTS**

 
1. In Equation 6, the authors take the average of the individual model standard deviations to compute the ensemble standard deviation. In Equation 9 of [10], the authors provide an expression for the predictive uncertainty of the ensemble that decomposes uncertainty into aleatoric and epistemic uncertainty. As far as I can tell, Equation 6 is only computing the aleatoric uncertainty and is missing the term for epistemic uncertainty (disagreement between models). What was the authors' justification for omitting the epistemic uncertainty component of the predictive uncertainty? Furthermore, does the omission of epistemic uncertainty affect the experimental results, and if so, how?

2. It would be worth adding the work from [6] as an additional baseline method since the parameter setting of alpha=1 i.e. model selection appears to perform best in experiments. This method, which uses Bayesian optimization in an inner loop to select the best model at each iteration of BO would be applicable to experiments over continuous hyperparameter spaces. It would be informative to see how model selection using the MSE compares against model selection using the marginal likelihood as in [6].

3. For the empirical results in the appendix it may be worth plotting the log regret in place of the regret of each method. This may provide a clearer picture of the performance deltas to be expected between the methods.

4. In Section 6, the baseline single GP implementation is presumably implemented using HEBO? If so, it makes some sense that the single GP variant of HEBO is performant in the low sample regime as early in the optimization trace, the treatment of the GP hyperparameters is fully Bayesian and hence there is an inherent notion of model ensembling. It would be interesting to run an ablation with the robust acquisition formulation (fully Bayesian treatment of hyperparameters) turned off. This could be achieved by using only the input/output warping and MACE components of HEBO. This would also decouple the inherent model ensembling within HEBO from the ensembling introduced by the authors.

5. It would be worth emphasizing in the introduction as well as the overall narrative of the paper, the result that alpha=1 i.e. model selection outperforms ensembling in the experiments. This seems to be a key finding of the paper.

 
**MINOR POINTS**

 
1. There are some missing capitalizations in the references e.g. "Bayesian" in place of "bayesian".

2. When citing Bayesian optimization on line 47, it may be worth referencing some of the originating papers [2, 3] as discussed in [4].

3. On line 84, the statement that Gaussian processes are performant in settings where the dimension is lower than 20 should potentially be moderated in light of recent work such as [5] which shows that Bayesian optimization can be performant in problems with 100s of dimensions if the lengthscale prior is scaled with the dimensionality. 

4. In light of the major points above, the sentence, "We present, for the first time, a dynamic ensembling approach for surrogate models in the context of HPO" may need to be moderated in light of [6] which introduces an ensemble of GP models (cf. Equation 8 in [6]) for Bayesian optimization and reports experimental results for hyperparameter tuning (neural networks and SVMs) of models fit on UCI datasets.

5. In the codebase it may be beneficial to rename the HEBO directory since I initially assumed this was directly copied from the HEBO codebase whereas in fact it contains code relevant for the method introduced in this paper.

6. On line 134, why is the loss function "estimated"?

7.  Line 139, see point 2 above.

8. On line 142, a set notation with curly braces may be more appropriate than parentheses.

9. On line. 154, is there a typo with the bolding of lambda in the correlation vector?

10. When citing the expected improvement acquisition function [9] should be cited as discussed in [4].

11. On line 217, in terms of the claim that this work introduces dynamic model ensembling for hyperparameter optimization see again the major points above, namely the reference to [6].

12. Line 230, extraneous colon.

13. Missing full stop at the end of Equation 16.

14. Figure 9, extraneous bracket around panel d. It may be worth additionally explaining the black dotted line in the figure as the distance to the closest variance bound.

15. In line 3 of Algorithm 1 it would be worth specifying how the model weights are initialized.

16. The notation in line 5 of Algorithm 1 is a little confusing. For example mu and sigma should be vector quantities and the notation suggests the models are fit on lambda alone and not the associated costs.

17. On line 7, it may be better if lambda_t is defined as a vector. Similarly on line 8.

18. On line 307, "heteroscedasticity and non-stationarity respectively" may be a better phrasing given that the Box-Cox and Yeo-Johnson transforms in HEBO address heteroscedasticity specifically whereas the Kumaraswamy transform addresses non-stationarity specifically. The authors indeed emphasize this in Appendix C.

19. In Section 4, in the description of the aspects of HEBO that yield performance gains, there are two additional components worthy of mention. The first, is the fact that HEBO uses the Multi-objective ACquisition Ensemble (MACE) method of [11] which ensembles the EI, PI, and UCB acquisition functions. The second, is that HEBO uses a robust acquisition function formulation which is equivalent to a fully Bayesian approach to the GP hyperparameters early in the optimization trace. In the HEBO paper, all 4 components were shown to improve performance independently of each other in an ablation study.

20. It would be worth citing the MACE paper [11] as the source work for the approach taken in HEBO. Out of interest, does the reference by Forrester also include such an acquisition function ensemble?

21. In the caption of Figure 2, it would be worth adding the number of random trials the errorbars are computed over.

22. Missing full stop at the end of Equation 9.

23. On line 784, I believe noise may still be heteroscedastic, yet adhere to a Gaussian noise model, save for the fact that the parameters of the Gaussian distribution will vary depending on the position in the input space? Willing to discuss this point further!

24. Equation 10 may be more clearly defined as a piecewise function?

25. It would be worth citing the Adam optimizer [12] given that it is used.

26. In line 845, the Q-function (state-action value function) holds the predicted discounted future return (discounted cumulative reward) rather than the expected simple reward.

27. For the significance test in Section I of the Appendix it would be good to formally state the null hypothesis and report the p-value of the permutation test.

 


### Questions
&nbsp;

1. In the introduction could the authors explain why the citation to "Language Models are few-shot learners" is an appropriate citation for the point that evaluating a single hyperparameter configuration of a model can be very expensive?

2. What is the motivation for assessing MSE only on the newly sampled points and not on the entire dataset collected so far in the trace? Do the authors have any intuition for how behavior would change if the MSE was defined on the full dataset? The motivation is outlined partially in Section C.2 of the Appendix.

&nbsp;

### Soundness
4

### Presentation
4

### Contribution
3
