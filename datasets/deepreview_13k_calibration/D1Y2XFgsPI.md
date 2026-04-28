# Imputation for prediction: beware of diminishing returns.

- Decision: Accept
- Avg Score: 6.60
- Scores: 3, 8, 8, 6, 8

## Abstract
Missing values are prevalent across various fields, posing challenges for training and deploying predictive models. In this context, imputation is a common practice, driven by the hope that accurate imputations will enhance predictions. However, recent theoretical and empirical studies indicate that simple constant imputation can be consistent and competitive. This empirical study aims at clarifying \emph{if} and \emph{when} investing in advanced imputation methods yields significantly better predictions. Relating imputation and predictive accuracies across combinations of imputation and predictive models on 20 datasets, we show that imputation accuracy matters less i) when using expressive models, ii) when incorporating missingness indicators as complementary inputs, iii) matters much more for generated linear outcomes than for real-data outcomes. Interestingly, we also show that the use of the missingness indicator is beneficial to the prediction performance, \emph{even in MCAR scenarios}. Overall, on real-data with powerful models, improving imputation only has a minor effect on prediction performance. Thus, investing in better imputations for improved predictions often offers limited benefits.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper empirically studies the effects of various missing value imputation methods, in particular whether better imputation accuracy yields higher prediction performance. The authors conduct experiments on nineteen benchmark datasets using four imputation methods, three different models, as well as variations such as missingness indicators and semi-synthetic linear labels. They conclude that imputation accuracy does affect prediction performance, although the gains are quite small, and the effect is further reduced if the model is more expressive, missing value indicators are used, or the target variable has a non-linear relationship to the covariates.

### Strengths
The paper presents an empirical study that can help us better understand the effect of various imputation techniques for different model/problem scenarios, which is an important question as missing values are ubiquitous and often handled by imputation. The paper specifically considers the link between imputation accuracy and prediction performance, which have been studied theoretically in some scenarios but not empirically for real-world problems.

The experimental setup is clearly described in detail for reproducibility, and the authors mention that code will also be available upon publication. The experiments are also thorough in terms of datasets, models, and imputation methods.

Related work discussion is clear, including both theoretical and empirical studies about missing value imputation methods.

### Weaknesses
Many claims/conclusions in the paper are based on small differences in average values with overlapping confidence intervals, and there are no statistical tests for significance. For example, the authors claim that the imputation techniques considered in the experiments show diverse imputation performance (Figure 2), but apart from mean imputation being worse than others, there doesn’t seem to be a definitive difference in quality by the other three imputers. 

In addition, the claim about correlation of imputation accuracy and prediction performance is made based on the small but positive slope of the regression line (Figure 4). However, the slope seems very small in most cases to suggest this, especially in the 20% missing case, and the correlation may still be very weak (small correlation coefficient). On the other hand, the authors suggest that good imputations matter more in the linear response case (semi-simulated data), based on the slightly higher correlation (Fig 5), but the slope seems still very small (Fig 11).

In about a third of the benchmark datasets, the dimension is small such that 20% missing means just one missing feature. I would expect the difference between simple and more complex imputation techniques to be pretty small in such cases. It would be helpful to see a breakdown of results by dataset dimensionality to understand this effect. The authors should also clarify whether the missingness is applied per sample or per feature, as this significantly impacts the interpretation of the results.

The experiment in MNAR scenario (Section 4.4) didn’t feel very connected to the rest of the paper. As the authors also noted, it is well known that most imputation methods (without considering causal structures) are not valid under MNAR. The results in this section are not particularly surprising or insightful, and it's unclear what the main takeaway is.

### Questions
The observation about good imputations having less effect when using missingness indicators was very interesting. To test the intuition mentioned in Section 4.5, I think it would be interesting to use explainability techniques on these models trained with missingness indicators to see if the importance/weights of features drop when they are missing (i.e. inputs with the corresponding missingness indicator on).

Does the correlation of prediction performance and imputation accuracy (e.g, Figures 3 and 4) also show any difference by imputation method?

Would larger missingness rates show more significant correlations?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors use an empirical approach to investigate whether advanced imputation techniques significantly improve predictive accuracy in models with missing data. The study finds that while sophisticated imputation can enhance prediction in certain contexts, the benefits are modest, especially when more expressive models and/or missingness indicators are used. They conclude with the assertion that resources might be better allocated to models that inherently handle missing data rather than focusing extensively on imputation improvements.

### Strengths
The value of this paper arises from its significance, not its originality. What I mean by this is that the paper effectively reports a "null" result: something that *doesn't* work. This kind of work is valuable because it saves the community time by not re-inventing square wheels. We need to know what doesn't work. 

If you count papers that provide evidence that a method doesn't work (I do) as original, then yes this paper is original. This definition of originality fits under the notion of originality as "a new definition or problem formulation," because the authors are recommending that the data imputation research solves the wrong problem if the goal is improved prediction.

The quality of the work was adequate, they performed a comprehensive study using several different models and many different datasets to arrive at a convincing analysis of model performance.

### Weaknesses
I did not mention clarity in the Strengths section because the paper needs a lot of stylistic work. The authors would benefit from reading Strunk & White's "Elements of Style" as well as Steven Pinker's "A Sense of Style." There were many redundant sentences, unnecessary adverbs ("really", "interestingly", etc), unnecessary metadiscourse (e.g., let me tell you what I'm going to tell you) and acronyms that were defined not on their first occurrence (or never at all). Missingness indicators, which are a prominent concept in the paper, should be defined in one sentence in the introduction. In addition, different paragraphs seemed to have different authors, where at least one author appears to not have an adequate grasp of English. I'm not judging that (I don't speak any other language, hats of to them if that is the case) but there are resources to help non-native English speakers (even ChatGPT now does a reasonably decent job: write a paragraph, input it along with "improve:" and then see how the output paragraph is written- I find this helpful for succinctness but it can also help with sentence structure/word choices). All of these weaknesses combined to make reading the paper feel arduous.



### Questions
Please eliminate redundant sentences, remove unnecessary adverbs ("really", "interestingly", etc), remove unnecessary metadiscourse (e.g., let me tell you what I'm going to tell you- the end of section 1 ) and acronyms that were defined not on their first occurrence (or never at all). Missingness indicators, which are a prominent concept in the paper, should be defined in one sentence in the introduction. Also, the quality and clarity of the writing varies greatly from paragraph to paragraph - can you make it more consistent? 

Line 140: what do you mean by a "universally consistent" algorithm?

Why is the 'semi-synthetic' data (top of page 5) 'semi'? Can you elaborate on that?

Line 341 uses the word "nuanced" in a strange way - so strange I couldn't figure out what the sentence in which it appears actually means.

You say 'comparing imputers is not our main objective' (twice), but it is an important set of results, right? Clearly, it is a salient result that a mean imputer does worse than other methods for both 20% and 50% missingness rates, and you could envision people citing this paper for that result. Perhaps these results should not be downplayed? 

Please re-read and consider linearizing the order/structure of your sentences. For example, line 456 reads "For prediction, imputation matters but marginally." You will minimize the amount of cognitive bandwidth / patience of your readers if you linearize the sentence structure, e.g.: 'Imputation matters marginally for prediction." If that is too much of a change of meaning, then consider 'Imputation matters for prediction, but only marginally.' These kinds of reverse-order sentences occur throughout the manuscript and, in aggregate, bog down the reader.

### Soundness
3

### Presentation
1

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper explores the link between imputation quality and downstream performance. Through multiple experiments, the paper demonstrates that under MCAR patterns, the quality of reconstruction error is not always linked with performance, depending upon modelling strategies.

### Strengths
The paper is well written and easy to read, presenting novel results even under the simple MCAR setting.

### Weaknesses
The critical insight that adding missing indicators can be beneficial, even under MCAR, needs more justification (with a potential theoretical justification). Intuitively, I suggest exploring the correlation between reconstruction error and gain from adding the indicator. I believe the correlation should be strong as the model is able to 'discard' badly imputed data. Additionally, an experiment with a random mask appended would demonstrate that this result is not just a product of a larger number of parameters in the model or some regularisation.

Other works have explored this relation. I would recommend comparing the results with work such as Bertsimas 2024, where the authors conclude, "While common sense suggests that a 'good' imputation method produces datasets that are plausible, we show, on the contrary, that, as far as prediction is concerned, crude can be good."

Bertsimas D, Delarue A, Pauphilet J. Simple Imputation Rules for Prediction with Missing Data: Theoretical Guarantees vs. Empirical Performance. Transactions on Machine Learning Research. 2024 Jun 5.

### Questions
None

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper investigates the empirical importance of accurate imputation in tabular, continuous data with MCAR missingness. It compares four common imputation techniques and three model architectures (2x NN, 1x tree-based) across 19 real-world, medium-sized (<50,000 samples), fully-observed datasets augmented with simulated missingness.

The authors conclude that good imputation yields marginal improvements in terms of prediction performance and that missingness indicators may be beneficial even in MCAR scenarios.

### Strengths
The study performs an extensive experiment across a variety of imputation methods, prediction models, and datasets.

### Weaknesses
The authors conclude that both better imputations and missingness indicators improve prediction performance. Neither of these findings is particularly surprising if we consider the optimal prediction with MCAR data:

$\mathbb{E}[Y \mid X_o, M] = \int_{X_m} f^\star(X_m, X_o)p(X_m \mid X_o)dX_m,$

where, in line with Le Morvan et al. (2021), $Y$ is the outcome, $X_o$ and $X_m$ are the observed respectively missing covariates, and $f^\star$ is the underlying full-data function. For the type of conditional mean imputation used in this work, we do not target $p(X_m \mid X_o)$ but instead estimate $\mathbb{E}[X_m \mid X_o]$. In the extreme, we have perfect knowledge of this expectation through an oracle, and Le Morvan et al. (2021) in their Figure 4 already demonstrated that the performance of such an oracle > imputation via chained equations > mean impute. In the same figure, they also show that missing indicators are beneficial even in MCAR settings. The authors must be aware of this work, since they cite it as their main reference in their section "4.5 WHY IS THE INDICATOR BENEFICIAL, EVEN WITH MCAR DATA?", where they exclusively lean on Le Morvan et al. (2021) to explain why missingness indicators, even if they contain no information about the outcome, may still aid learning an often discontinuous optimal predictor.

The empirical findings regarding the limited benefit of improved imputation are also not novel. Several existing benchmarks have shown that simple imputation methods often perform competitively with more complex ones, and that the performance gains from more accurate imputation are often marginal. This is consistent with the theoretical result that almost all imputations lead asymptotically to the optimal prediction, whatever the missingness mechanism. The authors should have discussed these existing benchmarks, which include Paterakis (2024), Shadbahr (2023), Perez-Lebel (2022), Jäger (2021), and Woznica (2020). The authors also do not sufficiently acknowledge that the benefit of missingness indicators in MCAR scenarios has been demonstrated both theoretically and empirically in previous work [1]. The authors' conclusion that better imputations and missingness indicators improve prediction performance is therefore not novel, and the paper lacks a clear justification for why these well-established findings need to be revisited.

### Questions
Given that both key findings are consistent with established theory and have been described before empirically, what are the novel contributions that would justify acceptance of the paper?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This study quantifies the relationship between imputation accuracy and prediction performance across various datasets, showing that improvements in prediction are typically only 10% or less of the gains in imputation \(R^2\). It finds that advanced imputation methods are less beneficial with more flexible models (e.g., XGBoost) and when using missingness indicators, which improve predictions even in MCAR scenarios. The authors highlight that in MNAR settings, the impact of better imputation is likely even smaller.

### Strengths
The paper effectively bridges theoretical work on the minimal impact of imputation in asymptotic settings with empirical studies of the "impute-then-predict" pipeline in supervised learning, offering a rigorous evaluation of when imputation accuracy affects prediction. The authors position their work within the existing literature by addressing both empirical evaluations of imputation methods and theoretical frameworks. The evaluation spans 19 datasets, multiple imputation methods, and prediction models across MCAR and MNAR settings, with detailed analysis of relative prediction performance and imputation time. The use of critical difference plots establishes upper bounds on the benefits of imputation, particularly in best-case MCAR scenarios.

### Weaknesses
 - When drawing conclusions from Figs. 1 and 2 (last paragraph of Sec. 4.1), the authors could address the conditions under which advanced imputers do provide a benefit. For example, while XGBoost might not benefit much from MissForest, other less flexible models like MLP show greater improvements when paired with more advanced imputations. 

    The authors might also explore non-linear or hierarchical relationships within the datasets where advanced imputations could outperform simpler methods more consistently. In cases where feature interactions are complex, MissForest could have greater effects. Specifically, the analysis could benefit from examining datasets with varying degrees of non-linearity and feature interaction complexity, rather than relying solely on the 19 datasets used, which may not fully capture the nuances of when advanced imputation methods are most beneficial. For instance, datasets with strong interaction effects between features might show a more pronounced benefit from methods like MissForest, which can capture these relationships better than simpler methods.

- Regarding “Good imputations matter less when the response is non-linear” (pgs. 7-8), the authors could strengthen the argument about non-linearities disrupting the relationship between imputation quality and prediction performance by incorporating insights from Le Morvan et al. (2021), which shows that *even with high-quality imputation*, non-linear functions can introduce discontinuities, making them harder to learn optimally. They could further illustrate how the *non-continuous nature of the regression function* after conditional imputation (as discussed in the paper) increases the complexity of the learning process in non-linear settings, which explains why non-linearities amplify the noise in the imputation-prediction relationship. The authors could provide a more detailed explanation of how the conditional imputation process, which involves imputing missing values based on observed values, can lead to discontinuities in the regression function, particularly when the underlying relationships are non-linear. This could be further illustrated with a simple example, such as a dataset where the true relationship between features and the target is a quadratic function, and demonstrate how the imputation process can introduce local discontinuities that hinder the learning process.

- On the question of whether the missingness indicator is the optimal way to represent missingness (pg. 9),  the authors could discuss specific limitations of the indicator in more detail, such as potential over-reliance on the indicator or the risk of introducing additional noise into the model. The authors cite the polar encoding paper of Lenz et. al. 2024, but could  suggest additional methods to represent missingness more effectively, such as embedding missingness directly within the model architecture or using neural architectures like NeuMiss that incorporate missing patterns in a more structured way (Le Morvan et al., 2021). Specifically, the authors could discuss how the missingness indicator might be treated as a feature with equal importance as other features, even though it does not carry the same semantic meaning. This could lead to the model overfitting to the missingness pattern rather than learning the underlying relationships between the features and the target. Furthermore, the authors could explore the potential of using more sophisticated missingness representations, such as learning a separate embedding for each missingness pattern, which could allow the model to capture more nuanced information about the missing data.

### Questions
- Pg. 2., line 70: The MNAR definition could be clarified by stating that missingness is related to the unobserved values themselves, making it informative. In this case, the probability of missing data is related to the actual values that are missing. Also, the MAR and MNAR abbreviations should be spelled out in the first instance. 

- Pg. 2, line 103: the sentence could be clarified, e.g., Woźnica & Biecek (2020) trained imputers separately for the training and test datasets, which led to an 'imputation shift'—a situation where the imputation patterns between the two datasets differ, causing inconsistencies in the data used for model training versus model evaluation.

- Pg. 5, it may be informative to state in the “Computational resources” section or in the Appendix the computational hardware (e.g,. number of CPUs) used to conduct the experiments. 

**Typos/grammar**:
- Pg. 1, line 52: missing parentheses
- Pg. 2, line 85: “mportant”
- Pg. 5, line 223: It’s been previously stated that for XGBoost and the MLP, hyperparameters are optimized using Optuna (Akiba et al., 2019)
- Pg. 7, line 348: proper casing for figures (“fig. 2”)
- Pg. 8, line 415: citation for Pereira 2024 not included in the reference list

### Soundness
4

### Presentation
3

### Contribution
3
