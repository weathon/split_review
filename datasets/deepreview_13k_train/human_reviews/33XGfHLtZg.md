# Conformal Risk Control

- Decision: Accept
- Scores: 6, 6, 8, 8, 6, 8

## Abstract
We extend conformal prediction to control the expected value of any monotone loss function.
    The algorithm generalizes split conformal prediction together with its coverage guarantee.
    Like conformal prediction, the conformal risk control procedure is tight up to an $\mathcal{O}(1/n)$ factor.
    We also introduce extensions of the idea to distribution shift, quantile risk control, multiple and adversarial risk control, and expectations of U-statistics.
    Worked examples from computer vision and natural language processing demonstrate the usage of our algorithm to bound the false negative rate, graph distance, and token-level F1-score.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper extends CP coverage guarantees to risk upper bounds. Under the assumption that the risk function is monotone, the authors derive a finite-sample and distribution-free bound on the risk expectation. Extensions and applications of the idea are also provided.

### Strengths
Extending the finite-sample and distribution-free coverage guarantees of CP to more general risk minimization problems may have a great practical impact. The experiments section contains a nice series of practical applications. I appreciate the authors included a full proof in the main text.

### Weaknesses
The relevance and novelty of the theoretical parts may be stated better in the introduction. The authors should 
- clarify why obtaining expectation-based bounds is more challenging than applying existing risk-control algorithms, e.g. the
hypothesis testing strategy of [1], and 
- specify what is different and what is taken from other works, e.g. some of the definitions are similar to [1], where the setup is slightly different.

Under the monotonicity assumption, Theorem 1 seems to be a straightforward reformulation of the standard validity proof for CP prediction intervals. Indeed, Section 4.2 outlines a much simpler formulation of the proposed algorithm. The authors may consider moving and discussing that section before Theorem 1 and adding a practical example where Theorem 1 is needed.

- The algorithm's main parameter, $\lambda$, is introduced in an example. It would be better to have a formal definition of it.
- A motivation is mentioned at the end of page 2: "it is generally impossible to recast risk control as coverage control". The statement is not proven or supported by examples. 
- Why does $R_n$ carrry an index? Are $R_1, ..., R_{n-1}$ used anywehere? This seems similar to [1], where the index refers to a specific value of $\lambda$.
- Can $R(\lambda)$ be interpreted as a parameterized conformity score and $\lambda$ as the quantile of the corresponding empirical distribution?
- [1] addresses the case of non-monotonic risks. How is this compatible with Proposition 2?
- Does the method apply to the outputs of a regression model?
- Are the extensions of Section 4 straightforward consequences of Theorem 1 and existing CP theory?

### Questions
- The algorithm's main parameter, $\lambda$, is introduced in an example. It would be better to have a formal definition of it.
- A motivation is mentioned at the end of page 2: "it is generally impossible to recast risk control as coverage control". The statement is not proven or supported by examples. 
- Why does $R_n$ carrry an index? Are $R_1, ..., R_{n-1}$ used anywehere? This seems similar to [1], where the index refers to a specific value of $\lambda$.
- Can $R(\lambda)$ be interpreted as a parameterized conformity score and $\lambda$ as the quantile of the corresponding empirical distribution?
- [1] addresses the case of non-monotonic risks. How is this compatible with Proposition 2?
- Does the method apply to the outputs of a regression model?
- Are the extensions of Section 4 straightforward consequences of Theorem 1 and existing CP theory? 

[1]
"Learn then Test: Calibrating predictive algorithms to achieve risk control".

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper extends conformal prediction to conformal risk control for any monotone loss function, which can be applied to different tasks more generally, such as token-level F1 scores. They also consider distribution shifts quantified by TV distribution distance and provide evaluations to validate the results.

### Strengths
1. The research question is important for many perspectives, such as trustworthiness ML.
2. The paper is comprehensive and includes multiple perspectives besides the main result, including distribution shifts and discussions of different types of losses.

### Weaknesses
1. I suggest adding detailed discussions of differences to related work [1,2].

[1] Learn then test: Calibrating predictive algorithms to achieve risk control. arXiv preprint arXiv:2110.01052, 2021

[2]  Distribution-free, risk-controlling prediction sets. Journal of the ACM (JACM), 68(6):1–34, 2021

2. The preview (sec 1.1) is clear, but theorem 1 is not well presented. $\lambda_{\text{max}}$ and $L_i$ are not defined or referred to in the context.

3. It is interesting to discuss whether we can have inverse relations of theorem 1? Specifically, given a parameter $\lambda$, can we inversely compute $\alpha$ to control the risk of $\lambda$?

### Questions
Please refer to the weakness part.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work generalizes the conformal prediction guarantees for coverage to controlling the risk of general monotone (or near monotone) losses, validating the proposed method on various real-life examples.

### Strengths
I think this is an exciting work with many strengths
- Method: generalize the CP method to arbitrary monotone loss functions, with extensions & modifications in distributional shift, controlling risk of multiple tasks, adversarial risks, etc.
- Theory: provide the guarantee for the proposed method, and demonstrating the need for monotone functions (Proposition 2) and how to monotonie loss functions (Corollary 1) for the same guarantee
- Experiment: provide extensive and useful illustration of the method in various tasks.

### Weaknesses
I think the only weaknesses lie in the experimental comparison.
1. In all examples presented in section 3, the authors only show the satisfactory performance of the proposed method. No comparison against other baselines is provided. If this is due to a lack of existing methods for similar tasks, it would be helpful to highlight this, explain why this is the case, and include doing so as future directions.
2. For tasks mentioned in the extensions, it would be helpful to also illustrate the effectiveness of the proposed method on a subset of them.

### Questions
What are limitations and future directions? It would be helpful to discuss these in the conclusion as well.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper offers a generalization of split conformal prediction, from its standard coverage-type guarantees to producing (threshold-based) set-valued predictions which bound, in expectation, arbitrary monotonic (in the threshold selected) loss functions (i.e. risks). The guarantees are very similar to conformal prediction (up to knowing an upper bound on the risk function), and the method flexibly generalizes some other important extensions of conformal prediction, such as e.g. the distribution shift conformal modeling of Tibshirani et al.

### Strengths
The paper considers a productive generalization of conformal prediction, and easily extends the same proof technique as in vanilla conformal to handle relevant monotonic risks that are not coverage indicators. This leads to a host of both worked-out, and potential, applications to provably bounding useful risks (such as e.g. the running example of FNR) in various settings.

The useful extensions, to quantile control, multiple risks, and covariate shift among others, are also quite easy to derive from this generalized framework.

The experiments are (for the most part) cleanly formulated and executed, confirming that relevant risks are easily bounded in practice as predicted from the theory. 

The paper is overall pleasantly written, and surveys all its contributions in a transparent manner.

As a result, I believe this paper would be a nice contribution to the conference, for both its theoretical soundness and simplicity as well as for its potential to be used in applications as diverse as split conformal prediction itself.

### Weaknesses
1. A relatively significant point is that, while theoretical bounds here are given in expectation, as compared to existing PAC-type guarantees on general risks developed in other recent related papers, but in practice it would still make a lot of sense to establish good empirical performance of conformal risk prediction relative to those --- and in particular, to Learn-then-Test, which appears both very tractable just as the proposed framework here, but also handles arbitrary losses, not just ones that are monotonic, and thus seems to offer better flexibility in practical settings (without having to resort to discussions of near-monotonicity like the present manuscript does). Since the displayed metrics about the conformal risk control method are agnostic to whether in-expectation or PAC-style guarantees are given, it should be easy to make this comparison quite direct, from a practical standpoint.

2. As a very minor point, the experiment on F1 score control in open-domain question answering, in contrast to other experiments in this paper, seems less useful and set up in a somewhat stylized way that doesn't seem to aim to capture any of the linguistic difficulties in tackling open domain question-answering --- which makes the plotted performance graph seem not very interesting. The F1 score is computed over a rather simplistic bag-of-tokens similarity between predictions and answers, and is not justified by the authors as the risk measure of choice here; moreover, a shift to alpha = 0.3 happens with the scant explanation that this is the best empirical choice such that almost all answers are typically correct. Recognizing that this is just a toy example to support the validity of the proposed method, I would still have liked to see a somewhat deeper discussion of what monotonic risks one could/should use when dealing with natural language; this would be very useful in the context of recent developments in LLMs.

### Questions
As stated above, I would like to see an experimental comparison to other methods offering guarantees on generalized risks; in particular Learn-then-Test.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper extends conformal prediction to control the expected value of any monotone loss function. This type of guarantee called conformal risk control can be seen as a generalization of CP and includes CP as a particular case. Authors prove that for bounded loss, the conformal risk procedure provides a bound for any given $\alpha$ and this bound is tight up to a $\mathcal{O}(1/n)$ factor. The paper also explores different settings/problems such as distribution shift, quantile risk control, adversarial risk control, and expectations of U-statistics. Finally, experiments highlight the soundness of their proposals.

### Strengths
This is a clever and promising idea to generalize conformal prediction guarantees.

This problem is of particular interest to the conformal prediction community.

The paper is very well written and easy to follow. This is a real pleasure to read it.

### Weaknesses
It seems to me that the paper is more a collection of lots of theoretical results (c.f. Section 4. "Extensions": distribution shift, quantile risk, adversarial risk..)  than a real important contribution to a particular problem. This somewhat blurs the main contribution of the paper, which might have benefited from presenting only the risk control in a standard setting, but with a much more in-depth theoretical analysis. The current structure makes it difficult to fully grasp the core implications of the proposed conformal risk control method, as the extensions, while interesting, dilute the focus on the fundamental results.

The experimental results are not analyzed at all. In addition, the extensions in section 4 have not been the subject of any experiments. The lack of analysis makes it hard to assess the practical value of the proposed method. For example, it is unclear how the performance of the conformal risk control compares to standard conformal prediction in practical settings. Furthermore, the absence of experiments for the extensions makes it difficult to ascertain their real-world applicability and limitations.

No limits are indicated in the conclusion. In my opinion, comments on the limitations of the proposed approach are lacking. Without a discussion of the limitations, it is difficult to understand the scope and applicability of the proposed method. For instance, it would be useful to know under which conditions the method might fail or perform poorly. 

Minor:

The proof of Theorem 1 should be in the appendix with all the other proofs.

"In this case, conformal risk control finds...the expected value is..." , hat on $\lambda$ is missing in the right part of the equality.

Typos: Examining (??),

### Questions
Under the distribution shift setting, the weights need to be estimated. How this can be done? and what is the impact on the control of the risk when $w$ is replaced by an estimate?

Is there a link between quantile risk control and training-conditional guarantee in standard conformal prediction?

Can you give a real situation where we want to control risks defined by adversarial perturbations?

The assumption that $P(J(L_i, \lambda) > 0) = 0$ appears to be the CP equivalent of the continuous score assumption. Is this true?

It is said in the paper that in "monotonizing" a loss will only be powerful if the loss is near-monotone. Although this seems intuitive, do you have any numerical evidence for this? (or/and a basic example).

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 6

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper generalizes the tools of the Conformal Prediction framework to achieve prediction sets satisfying general criteria, including the traditional coverage criteria. They provide an adaptation to Split Conformal Prediction that achieves this new "risk" metric. They demonstrate empirically that such a method indeed holds similar risk guarantees to the known coverage guarantee over a host of real datasets.

### Strengths
1. The intuition of the paper is strong. Developing a method to generalize Conformal Prediction to different loss functions is a clear improvement on existing literature, and the contribution is clear.
2. The experiments are very well done. The experiments over several loss functions are clear and convincing. 
3. The paper's motivation is clear, and the impact of such work is immediately evident. 
4. The extensions are strong and of good breadth. This framework is evidently useful for providing guarantees under different risk settings, not just the initial canonical setting of risk presented first. 

Overall, I vote for acceptance of this paper. I have several questions on computability and the writing, but these can be fixed and explained for the camera-ready version.

### Weaknesses
1. Some motivating examples of cases where such conformal risk control would be desirable over the traditional coverage guarantee are missing. While the paper mentions F1-score, it would be beneficial to elaborate on specific scenarios where optimizing for F1-score, or other metrics, is more appropriate than coverage. For instance, in imbalanced datasets, a high coverage might still result in poor performance on the minority class, making F1-score a more relevant metric. Concrete examples in the introduction would strengthen the motivation for this generalization.
2. The assumption of a bounded loss function requires further justification. While coverage naturally satisfies this, the paper should provide more examples of loss functions that either satisfy or violate this condition, beyond the brief mention of clipped losses. For example, what about losses that grow polynomially or exponentially? A discussion of the implications of this boundedness assumption on the applicability of the method would be helpful.
3. The definition and usage of the \(\Lambda\) operator are unclear. The paper states that \(L_i\) is a map from \(\Lambda\) to another set, but \(\Lambda\) itself is not explicitly defined. It is also stated that \(\sup \Lambda \in \Lambda\), which is confusing if \(\Lambda\) is the set of possible \(\lambda\) values, as it would imply that the supremum of the set of possible thresholds is itself a possible threshold. This needs clarification.
4. The intuitive explanation of the method in Section 1.1 is lacking, particularly in explaining why the proposed approach works. Conformal prediction's popularity stems from its intuitiveness, which is not adequately captured here. The definitions and claims lack a clear intuitive explanation, making it difficult to understand the underlying mechanism. More explanation is needed to clarify the meaning of the constants and claims.
5. The computability of \(\hat{\lambda}\) is a major concern. The paper does not provide sufficient details on how this value is calculated, and it seems non-trivial. This is a critical aspect of the method, and the paper should address whether this formalization makes computation easier compared to other conformal risk control methods. The computational complexity and practical feasibility of finding \(\hat{\lambda}\) should be discussed.
6. The guarantee of \(\alpha - \frac{2B}{n+1}\) in Section 1.1 is concerning. Standard Split Conformal Prediction has a guarantee of \(\geq \alpha\), which is only loose by \(\frac{1}{n+1}\). The paper should clarify if this method recovers the tightest guarantees of Split Conformal Prediction when the loss function is set to miscoverage, and why the guarantee is weaker.
7. The related works section needs more clarity on the differences between existing and current work. The paper mentions that the guarantee is in expectation, but it is unclear why this is better than existing works. Do existing works provide worst-case or high-probability guarantees? The technical similarity between different methods is not a sufficient justification for the contribution. The paper should elaborate on what existing conformal risk works do, and whether they directly generalize conformal predictions or are less tight. More details are needed to differentiate this work from existing approaches.
8. The theoretical section, particularly Section 2.1, lacks intuitive explanations. The proof steps should be explained in more detail, and the meaning of each step should be clarified. The notation in the proof of Theorem 1 is difficult to follow, and the use of \(\hat{\lambda}'\) and \(\hat{\lambda}\) is confusing. A cleanup of the proof and notation is needed.
9. The assumption in Theorem 2, \(\mathbb{P}(J(L_i, \lambda) > 0) = 0\), is presented without sufficient explanation. The paper should clarify which loss functions satisfy this condition and which do not, and why. This analysis is crucial for understanding the scope and applicability of Theorem 2.

### Questions
Please see above.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent
