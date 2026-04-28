# GAMformer: In-Context Learning for Generalized Additive Models

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 6, 5, 3

## Abstract
Generalized Additive Models (GAMs) are widely recognized for their ability to create fully interpretable machine learning models for tabular data. Traditionally, training GAMs involves iterative learning algorithms, such as splines, boosted trees, or neural networks, which refine the additive components through repeated error reduction. In this paper, we introduce \textit{GAMformer}, the first method to leverage in-context learning to estimate shape functions of a GAM in a single forward pass, representing a significant departure from the conventional iterative approaches to GAM fitting. Building on previous research applying in-context learning to tabular data, we exclusively use complex, synthetic data to train GAMformer, yet find it extrapolates well to real-world data. Our experiments show that GAMformer performs on par with other leading GAMs across various classification benchmarks while generating highly interpretable shape functions.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents GAMformer, a novel model for fitting Generalized Additive Models (GAMs) using in-context learning (ICL) within a transformer-based framework. Unlike traditional GAMs that rely on iterative methods such as splines or gradient boosting, GAMformer uses a single forward pass to estimate shape functions for each feature, eliminating the need for hyperparameter tuning and iterative optimization. This approach is trained exclusively on synthetic data but performs competitively with existing GAMs on real-world tasks. GAMformer’s non-parametric, binned approach to shape function estimation enables high interpretability of feature impacts. Experimental results show that GAMformer matches or surpasses other interpretable machine learning methods on both synthetic and real-world tabular datasets, including clinical applications on the MIMIC dataset for ICU mortality prediction. Additionally, the model’s adaptability to real-world data demonstrates its potential for scalable, interpretable applications without extensive tuning.

### Strengths
GAMformer is a contribution to GAMs, leveraging ICL and transformer models to eliminate iterative optimization, thereby simplifying the modeling process and reducing the computational overhead associated with traditional GAMs.

The model maintains high interpretability—crucial for critical fields like healthcare—while matching the performance of established methods like Explainable Boosting Machines (EBMs).

GAMformer’s training on synthetic data enables it to generalize to real-world data effectively, a challenging task for many models, especially in interpretability-driven applications.

The use of a non-parametric, binned representation for shape functions allows for flexibility, particularly for capturing discontinuities or sudden shifts in feature impacts.

The model was rigorously tested across various benchmark datasets, and a case study on ICU mortality in the MIMIC-II dataset demonstrated its clinical interpretability potential, which is well-aligned with the paper’s goals.

### Weaknesses
GAMformer currently only supports main effects and second-order feature interactions, limiting its applicability for datasets where higher-order interactions are significant. 

The Transformer architecture in GAMformer scales quadratically with the number of data points, leading to potential performance bottlenecks for very large datasets. Exploring scalable attention mechanisms, as the authors suggest, would strengthen the model’s practical use.

While the clinical case study is insightful, further empirical evaluations across diverse fields (e.g., finance, manufacturing) would provide a clearer picture of GAMformer’s interpretability and performance across different domains.

There is a lack of quantitative results tables comparing the model with recent baselines.

### Questions
Please see the weaknesses section.

### Soundness
3

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
The paper proposes an in-context learning approach for learning generalized additive models for tabular data building on prior work (PFN and TabPFN) for tabular classification.
The training procedure executes on synthetic data by sampling a random causal graph and generating data from an initial random sample. The data is split into training and test datasets to simulate inference. 
A transformer model applies attention across the data points and features and handles tabular data of varying sizes. A single forward pass of the transformer estimates the shape functions for the given in-context training data which are then applied to the test example. The shape functions themselves are represented as discrete functions which apply to discretized and binned features. The method is demonstrated experimentally on synthetic and real data including a mortality risk case study where the shape functions are used to interpret model predictions.

### Strengths
The method appears to be a novel approach for learning generalized additive models.

The paper is well-written, ideas and goals are clearly stated, background work is acknowledged and limitations are addressed.

Experiments are done on synthetic and real examples with an extensive public health case study interpreting the learned shape functions and their implications. 

The paper discusses the limitations of the model which are 1) lack of accounting of higher-order interactions 2) lack of improvement over datasets larger than seen during training and 3) quadratic complexity of the transformer.

Also propose an extension to model higher-order effects by concatenating data and high-order effects.

### Weaknesses
The approach appears to be limited to discrete target values. Shape functions are learned as discretized functions over discretized features which could be limiting.



### Questions
Do you only consider discrete target variables in the experiments? Given that the features are binned and discretized, could the method be applied for regression with continuous variables?

### Soundness
3

### Presentation
4

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
The paper addresses the problem of supervised learning for tabular data and proposes a solution based on generalized additive models. A key feature is the use of an attention-based neural network (Transformer) to process the training data and provide a prior over the parameters of the non-linear predictive functions. The learning process involves splitting the training data into a training set and a holdout set. A predictive likelihood over the holdout set is used to learn the prior based on the training set. Experiments on synthetic data and OpenML datasets are conducted to compare the proposed solution with explainable boosted machines, demonstrating its ability to achieve comparable predictive performance

### Strengths
1. The paper is clear and well-written **Clarity**
2. The paper addresses an important and relevant problem, specifically how to leverage deep learning to learn a prior for predictive tasks on tabular data. **Relevance**
3. The code is available, and a Jupyter Notebook is provided to demonstrate how the proposed model and explainable boosted machines generate the predictive functions **Code Availability**. However, no checks have been performed to verify the reproducibility of the experiments.

### Weaknesses
1. The novelty of the paper is limited and incremental. **Novelty**. The main ideas have already appeared in two previous works [1,2], and the primary difference seems to be the use of a different classifier/regressor. In other words, instead of considering Bayesian neural networks or structural causal models like in [1,2], the authors focus on generalised additive models. In essence, the work can be seen as an application of existing ideas within the context of generalised additive models.
2. There are several vague and overstated claims that are not properly supported. For instance, the abstract mentions that the proposed solution generates highly interpretable predictive functions. **Soundness** However, this is also true for the competitors, and it is unclear what the real advantage of the proposed solution is over existing generalised additive models and other interpretable models (such as XGBoost). In the experiments (e.g., lines 304-305), it is stated that the proposed solution outperforms explainable boosted machines (EBMs), but these claims seem exaggerated. Firstly, in the low-data regime (32 samples) with a larger number of features (64), the proposed solution clearly underperforms compared to EBMs by 14 points, suggesting a possible blind spot and indicating that sufficient data is required for the proposed solution to perform on par. Secondly, it is unclear whether the differences in the results are statistically significant, as no standard deviation is provided. Similarly, for Figures 2 and 3, it is claimed that the proposed solution clearly learns smoother predictive functions. However, this is subjective and not consistently true (only the 1st and 3rd plots in Figure 2 support the authors' claim).
3. The experimental analysis lacks a consistent comparison across datasets and tasks with other interpretable models. Additionally, the analysis focuses on the case where the ground truth classifier lies within the hypothesis space. What about the agnostic case? **Quality**
4. The experiments are conducted on small datasets, reflecting the poor scalability of the approach. While the idea of synthesizing data may be reasonable for small datasets, it may not be tractable or feasible for higher-dimensional data, given the potential for combinatorial explosion. Scalability and feasibility are currently overlooked, which is a significant limitation of the proposed solution. As a result, it is unclear why one should prefer this approach over existing interpretable models that are more scalable. **Quality/Significance**

### Questions
Please, refer to the main weaknesses.

### Soundness
2

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
4

### Summary
The authors use prior fitted networks to train a large transform-type architecture that can then learn the shape functions of additive models in a single forward pass. The resulting model is competitive to other approaches with similar interpretability and capacity.

### Strengths
- **Originality**: The idea of learning shape functions in-context is novel and interesting. 
- **Numerical Experiments** The comparisons cover a variety of models from different classes, thus giving a bigger picture of GAMformer's capabilities.

### Weaknesses
## Major

### Contributions

- **[C1]** The claim that "experimental results demonstrate GAMformer's capacity to match the accuracy of leading GAMs" might be accurate regarding performance, but the interpretability has not been sufficiently scrutinized. See comments on Experiments below. The shape functions presented are visually similar to those of EBMs and NAMs, but a more rigorous analysis of their interpretability is needed, such as a user study or a quantitative measure of how well they align with domain knowledge.
- **[C2]** In light of GAMs requiring no tuning (at least in the `mgcv` package, which uses methods like AIC for smoothing parameter selection), the claim "... to form shape functions ... eliminating the need for ... iterative learning and hyperparameter tuning" does not seem particularly significant. The automatic smoothing parameter selection in `mgcv` is a key feature that the authors seem to overlook.
- **[C3]** The contribution claiming the model was applied to the MIMIC-II dataset lacks significance. This dataset has been analyzed previously. The current study does not add any new insights. The dataset itself is also not particularly challenging, yet the modeling approach seems to have missed a key property of the dataset (see **E3** below).

### Technical soundness/correctness

- **[T1]** The introduction to GAMs is missing a distributional assumption (a GAM consists of both structural and distributional assumptions; see Wood, 2017). The authors should explicitly state the assumed distribution of the response variable, as this is a crucial part of the GAM definition.
- **[T2]** The simulated functions are not GAMs but deterministic functions. As correctly noted by the authors, a GAM is defined by a link function, yet they use a simple indicator function without induced noise or distributional assumptions for the simulation, which does not correspond to the data-generating process of a GAM. The code uses `sigmoid`, but there is no distribution involved (same for the regression task). This makes it difficult to assess if the method can actually recover the underlying structure of a true GAM.
- **[T3]** "Allocating bins based on the quantiles of the feature in the training dataset" → This approach is likely inferior to equidistant binning, as quantile-based binning alters the data distribution of the feature (see Li and Wood, 2017). While quantile binning is used in some tree-based methods, it is not necessarily optimal for all models, and the authors should justify this choice.
- **[T4]** The comparisons with `mgcv::gam` appear incomplete (see below). The authors should provide more details on the `mgcv` implementation, including the specific formula used and the smoothing parameter selection method. The fact that logistic regression outperforms `mgcv::gam` suggests a potential issue with the experimental setup or the `mgcv` implementation.

### Significance

- **[S1]** The computational costs of:  
    + fitting a GAM are $O(N_{train} \cdot (K \cdot p)^2)$ (see Wood, 2020), where $p$ is the number of features and $K$ the number of basis functions (in `mgcv`, often set to 10). For the data used by the authors, this would amount to 50-800 parameters;  
    + predicting with a fitted GAM is $O(N_{test} \cdot K \cdot p)$.

  In contrast, ICL requires millions of parameters, if I understand Sec. 3.2 correctly, and even with fast inference, it is slow compared to GAMs, where typically $N > p$ and hence the quadratic scaling of $N$ in the transformer is still the bottleneck. Moreover, the authors report that the model required 25 days on a high-performance GPU, whereas all the analyzed datasets could be fit within seconds using GAMs. GAMs can also be applied to datasets of size $10^8$ using `mgcv::bam` (see Wood et al., 2017).
  
- **[S2]** The method does not seem to outperform other models in prediction accuracy and appears to be inferior to TabPFN. TabPFN itself could also be analyzed using SHAP after computing the predictions, raising the question if a specific architecture is even necessary. The authors should clarify why a specific architecture is needed when post-hoc interpretability methods can be applied to other models.
- **[S3]** I could not identify any other significant insights of theoretical nature or similar that could be derived from a GAMformer. In particular, I would assume that the SCMs in TabPFN likely already cover GAM-type models (related to **S2**). This raises the question of what additional benefit is gained by making them explicit, as done here. The authors should explain the specific advantages of explicitly modeling GAMs compared to using a more general model with post-hoc interpretability.

### Experiments

- **[E1]** The experiments do not show the shape functions of the GAM method, which would be particularly useful for illustrative examples. Showing the shape functions of the GAM method would allow for a direct visual comparison and help assess whether the GAMformer is learning similar functions.
- **[E2]** Simulations should be designed to correspond to an actual GAM to see whether the GAMformer can actually recover those (see **T2**). The authors should simulate data from a GAM with a specified link function and error distribution to properly evaluate the method's ability to recover the true underlying model.
- **[E2/T4]** The `mgcv::gam` should not be inferior to logistic regression if used correctly (see Figure 6). The authors need to provide more details on how `mgcv::gam` was used, including the formula, basis functions, and smoothing parameter selection method, to understand why it performed poorly.
- **[E3]** Isn't there censoring in the MIMIC datasets? A time-to-event model might be more appropriate in this case then. The authors should justify the use of a standard classification model on the MIMIC data, given the presence of censoring, and consider using a time-to-event model if appropriate.
- **[E4]** In the Appendix experiments, the authors switch to `pyGAM`, which is known to be inferior to `mgcv::gam`, and do not report the latter's performance. The authors should include the performance of `mgcv::gam` in the Appendix experiments for a fair comparison.

### Reproducibility

- **[R1]** The code does not provide competitor models. The authors should provide the code for all competitor models to ensure reproducibility.

### Writing

- **[W1]** There is some redundancy between Sections 1 and 2, which disrupts the flow of reading. The authors should merge or reorganize these sections to improve the flow and avoid repetition.
- **[W2]** The notation $j_{x_i}$ is somewhat confusing, as $j$ is an index in the bins and $x_i$ represents the $i$th feature in $x$. The authors should clarify this notation or use a more intuitive one.

## Minor / Technical soundness

- **[M1]** The $f$ functions are typically referred to as *smooth terms* or *smooth functions* in the GAM literature, not *shape functions* (a term seemingly invented by the NAM community). They are also not *partial dependence plots* (as these are plots, not functions; in GAM literature, they are referred to as *partial effects*).
- **[M2]** The $g$ function typically does not map to $\mathbb{R}$ but to a subspace ($\mathcal{Y}$, or more specifically, e.g., (0,1) for the logistic function).
- **[M3]** What is $q_\theta$ in equation (2)?
- **[M4]** "Spline-based GAMs use the backfitting algorithm" $\rightarrow$ Backfitting was proposed by Hastie and Tibshirani. More recent approaches, like those from Wood, use PIRLS or alternatives like INLA (see Wood, 2017).
- **[M5]** The citation in footnote 3 (and for the `mgcv` package in general) seems incorrect.
- **[M6]** No "shape functions" for pairwise smooth interactions are shown.

### Questions
- **Q1**: I would be very happy if the authors could address the weaknesses I have mentioned above
- **Q2**: Are there any insights of GAMformers that I might have missed?
- **Q3**: Have the authors thought about analyzing the smoothness of GAMformers and whether this could provide more interpretable functions compared to the jagged functions of NAMs / EBMs?
- **Q4**: Have the authors thought about extending the class of GAMs? I would assume that this model could also learn a combination of GAMs, trees, NODEs, etc., and still remain interpretable.

### Soundness
2

### Presentation
2

### Contribution
1
