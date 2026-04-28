# Monty Hall and Optimized Conformal Prediction to Improve Decision-Making with LLMs

- Decision: Reject
- Scores: 8, 6, 5, 3

## Abstract
Large language models (LLMs) are empowering decision-making in open-world agents in several applications, including tool or API usage and answering multiple choice questions (MCQs). However, they often make overconfident, incorrect predictions, which can be risky in high-stakes settings like healthcare and finance. To mitigate these risks, recent works have used conformal prediction (CP), a model-agnostic framework for distribution-free uncertainty quantification. CP transforms a \emph{score function} into prediction sets that contain the true answer with high probability. While CP provides this coverage guarantee for arbitrary scores, the score quality significantly impacts prediction set sizes. Prior works have relied on LLM logits or other heuristic scores, lacking quality guarantees. We address this limitation by introducing CP-OPT, an optimization framework to learn scores that minimize set sizes while maintaining coverage. Furthermore, inspired by the Monty Hall problem, we extend CP's utility beyond uncertainty quantification to improve accuracy. We propose a method called \emph{conformal revision of questions} (CROQ) to revise the problem by narrowing down the available choices to those in the prediction set. The coverage guarantee of CP ensures that the correct choice is in the revised question prompt with high probability, while the smaller number of choices increases the LLM's chances of answering it correctly. Experiments on the MMLU,  ToolAlpaca, and TruthfulQA datasets with Llama-3 and Phi-3 models show that optimized CP scores reduce set sizes while maintaining coverage guarantee, and CROQ shows significant improvement in accuracy over the standard inference procedure.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents a method where conformal prediction can be used to quantify and reduce output uncertainty for decision-making problems using LLMs.
Authors show that using standard LLM softmax logits in the case of MCQ can be improved more using their proposed conformal prediction scoring under coverage constraint CP-OPT in cases when LLM logits are not as highly informative. Further they propose CROQ (which is reprompting the LM with the previous conformal set produced) which are shown to increase accuracy further.  

Empirically the proposed method seems to be promising when LLM softmax logits lacks information and the utilisation of CROQ

### Strengths
The paper is well written the problem is well motivated and presented well.
Overall the intuition behind using conformal prediction in the context of MCQ answer using LLMs is well appreciated.

Extensive experiments performed across 3 different MCQ datasets for different configurations for testing the utility of proposed conformal prediction set scoring framework CP-OPT (e.g. Fig 4. Table 1 , Fig 3).
 
Explaination of Hypothesis w.r.t empirical evidence for 4.2 is well presented.

### Weaknesses
- Limited baseline model coverage. It would have been good to see a couple more open source models, to test the gaps across further models with respect to Logits procedure.
- The design principles for learning CP-OPT seems limited as to using a 3-layer neural network. Some more additional details will be useful.

### Questions
Section 3.1.2 - cardinality of $\mathcal{D}_{train}$ is $n_t$ but in equation it shows $n$. 

Fig 3: MMLU-10 and MMLU-15 for LLama, is there any specific reason as to there is a continued diminishing effect to revision as coverage parameter is increased as compared to other cases where the spike is less spread.
Although this is not the focus of the paper, any discussion on how this can be in some sense extrapolated to open ended question generation settings as well.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper considers the setting where LLMs are used to answer MCQ-style problems. The authors consider the use of conformal prediction in this setting and make two methodological contributions:
1. Firstly, the authors propose a method of optimising score function which leads to smaller confromal sets on average. 
2. Secondly, the authors investigate what happens if the LLMs are provided revised questions where the options are restricted to the conformal sets.

### Strengths
1. The paper is well-written
2. The methodology is clearly explained
3. The paper includes extensive experiments to empirically investigate the methodology proposed.

### Weaknesses
1. The paper considers the MCQ-setting, which could be somewhat restrictive. Is it possible to extend these ideas to settings where the model is not provided with options?
2. My main concerns regarding this paper are two fold: 

i. Firstly, the methodologies proposed are somewhat orthogonal. The CP-OPT is a general methodology for optimising the score function which could be applicable to any CP problem (and is not specific to LLMs). In comparison, the CROQ methodology simply re-queries the model using the conformal sets. These methodologies are completely independent of each other and therefore I think the main contribution of the paper is not very coherent.

ii. Secondly, the methodologies proposed themselves are not very novel. For example, Cherian et al., 2024 (which the authors cite) seem to propose a very similar methodology of optimising the score functions as that proposed in this paper. Can the authors please elaborate on how their methodology is different? Similarly, the idea of re-querying the model does not seem very novel either. 

3. In Figure 3, please also add the uncertainty in the accuracies for all methods. In most cases, its unclear whether CP-OPT produces a better accuracy than logits. 

4. While it can be seen that CP-OPT leads to smaller sets on average, it is not convincing from the empirical results that the accuracy of revised questions is strictly better when using CP-OPT as opposed to just logits. Can the authors explain why CP-OPT does not seem to do better than logits at CROQ? 

5. Can the authors explain why for MMLU there is no difference in Figure 4 between CP-OPT and logit methods whereas for Truthful QA, CPT-OPT leads to fewer deferrals and higher accuracy?

### Questions
See weaknesses section above.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes two techniques related to conformal prediction. For the first technique, the paper proposes a method for minimizing the size of the set of outputs in order to meet the coverage objective of the conformal predictor. As the objectives are non-differentiable, the paper proposes a differentiable approximation based on using the sigmoid to approximate the indicator function. For the second technique, the paper proposes a two stage method for improving the preformance of MCQ prediction. The method first use the conformal predictor to reduce the number of options to consider in the MCQ question, then predicts again with the remaining option.

### Strengths
The proposed method for reducing the size of the set of outputs is natural and relatively simple, which is good. The experimental results for the proposed two stage method for improving performance in MCQ questions are good.

### Weaknesses
The experimental results for reducing the size of the set of outputs did not show much improvement for the proposed method. In most of the cases considered (except 3 cases), the size is smaller but the coverage is also correspondingly smaller, so the improvement is not convincing. The reason for improvement in the two stage MCQ method is not clear and not much insights is provided in the paper on it. The analogy to Monty Hall is not convincing and is actually misleading as the mechanism for the improved performance in the two stage prediction method in Monty Hall is not present here. Note that no additional information is provided unlike in the Monty Hall case and if the correct posterior probability for each option is provided by the predictor, the optimal action is to predict the option with the highest probability, a one stage method.

### Questions
If possible, some insights on why improvement is small for the first technique would be useful. Similarly, insights of why the two stage method is helpful would be useful, if possible. Given that two stages is helpful, would even more stages be even more helpful?

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
The authors present two orthogonal methods related to conformal prediction: The first part of the manuscript introduces CP-OPT, an optimization framework to learn scores
that minimize set sizes. The second part introduces *conformal revision of questions
(CROQ)*, a method that improves model predictions by removing low-quality answers (the ones that are not part of the conformal prediction set) and querying the model again on the remaining high-quality examples. The methods are empirically assessed on three multiple-choice question answering tasks.

### Strengths
1. The ideas of the work are very interesting. In particular I find the second part of the manuscript about conformal revision of questions (CROQ) interesting.

2. The proposed methods are simple, orthogonal to the choice of underlying model architecture and easy to understand. The manuscript is accessible to readers with diverse backgrounds. I appreciate that the authors withstand the trend of overcomplicating their ideas.

3. I find it surprising that CROQ works. It shows that large language models are able to bootstrap in the sense that they can incrementally guide themselves to the correct answer, similar to the idea called *chain-of-thought reasoning* [1].

[1] Wei, Jason, et al. *Chain-of-thought prompting elicits reasoning in large language models.*. Advances in neural information processing systems 35 (2022): 24824-24837.

### Weaknesses
1. The manuscript is divided into two rather unrelated parts. Unfortunately, this division comes at the cost that both ideas are treated somewhat superficially. I would advise the authors to go for either one of two options: 1) Create a coherent and convincing story that unifies both parts or 2) Remove one of the two parts from the manuscript and extend the other part (I recommend option 2).

2. The writing of the manuscript can be improved. There exist a number of inconsistencies (see Questions section) and unclear/confusing notation (the latter point is likely subjective).

3. I am not convinced that CROQ works due to conformal prediction, as the $1 - \alpha$ coverage guarantee does not seem relevant for the method to work. For a downstream purpose, conformal prediction just yields an arbitrary threshold to remove low-quality answers. But it does not matter whether this prediction set achieves $1 - \alpha$ coverage, because this $\alpha$ has no particular meaning. Instead, the essential (and interesting) point seems to be that the model can improve its own predictions simply by removing answers that have low quality, where the quality threshold must be tuned. I hypothesize that it would be more efficient to tune this quality threshold directly rather than tuning the $\alpha$ parameter (which is subject to variance from the calibration set), which indirectly predicts a quality threshold. I would ask the authors to provide a convincing answer why the coverage guarantee at a given level $1 - \alpha$ is relevant for the method and why they cannot just tune the quality threshold directly.

### Questions
line 1: I am not sure whether the association with the Monty Hall Problem for CROQ is reasonable. There exists an essential difference: For CROQ, the agent (LLM) solves the answer entirely based on its own predictions (and data), whereas there exists an external entity in the Monty Hall Problem (the host) who opens a door. I suggest modifying the narrative.

line 38: *complete a task. (Qu et al., 2024;* The dot after *task* should be removed.

line 42: Figure 1 shows a large language model that makes a wrong prediction, but reveals little about what to expect when reading the manuscript. I would advise combining Figure 1 and Figure 2 or replacing Figure 1 by Figure 2 and omitting Figure 1 entirely (I recommend the latter).

line 46: In spite of the title, the work by [1] does not use conformal prediction, but a multiple hypothesis testing method called *learn then test* [2]. You may consider moving this reference somewhere else, removing the reference, or rewriting the sentence to broaden the scope.

line 53: *any scoring function* For the sake of consistency, I advise the authors to call this function *score function* everywhere.

line 175: Is *conformity score function* the same as *score function*, which is the same as *scoring function*? If yes, please replace all variants by *score function*.

line 178: I find the notation $C(\tilde{x} \, | \, g, \hat{\tau})$ a bit misleading. It may create the impression that the score function $g$ is a random variable. I would advise replacing this notation with something like $C(\tilde{x} ; g, \hat{\tau})$ or $C_{g, \hat{\tau}}(\tilde{x})$.

line 206: This notation seems quite unusual. I recommend just writing $ \mathbb{E}_{x} $ or e.g. $ \mathbb{E}_{x \sim P} $ (in the latter case,  $P$ must then also be introduced).

line 214: I am surprised to find that the optimal threshold $\tau$ is part of the definition. I believe that $\tau^*$ is just a deterministic function of $g^*$.

line 221: Replace the period with a colon: "*distribution.*" should be "*distribution:*".

line 229: Replace "*higher*" with "*larger*": "*higher $\beta$*" should be "*larger $\beta$*".

line 237: Specify what the arrow $\rightarrow$ means, e.g., *convergence in probability*.

line 240: What is this *flexible space of functions* $\mathcal{G}$? 

line 245: Similarly as to my comment for line 214, I believe we only need to optimize for $g$, because $\tau$ is just a function of $g$.

line 245: The equation has $\lambda$ and $\lambda_2$. I suggest renaming $\lambda$ to $\lambda_1$ for sake of consistency.

line 245: Clarify what $|| g ||_2$ means. Is it the squared norm over parameters of $g$? Or is it $\int |g(x, y)| dxdy$?

line 245: Why is the penalty formulation used to solve a constrained optimization problem? Would it be possible to solve the problem using the augmented Lagrangian method, which leads to a more accurate solution?

line 289: Unlike the authors, I am surprised that this works: In contrast to the Monty Hall Problem, the door with the goat is not opened by an external entity, but by the model itself (which makes a great difference).

line 420: I believe that the *discussion* section should rather be called *results*. 

line 479: [1] is a suitable reference in the more general context of risk control, but as mentioned in an earlier comment, [1] does not employ conformal prediction. I would therefore suggest removing the reference or rewriting the text accordingly.

line 484: As far as [1] is concerned, there seems to be another misunderstanding: [1] also aims at reducing prediction set size, unlike claimed. I would suggest removing this sentence.


[1] Quach, Victor, et al. *Conformal language modeling*. International Conference on Learning Representations, 2023.

[2] Angelopoulos, Anastasios N., et al. *Learn then test: Calibrating predictive algorithms to achieve risk control.* arXiv preprint arXiv:2110.01052, 2021.

### Soundness
2

### Presentation
2

### Contribution
2
