# On the Recoverability of Causal Relations from Temporally Aggregated I.I.D Data

- Decision: Reject
- Scores: 5, 6, 6, 6, 6

## Abstract
We consider the effect of temporal aggregation on instantaneous (non-temporal) causal discovery in general setting. 
This is motivated by the observation that the true causal time lag is often considerably shorter than the observational interval. This discrepancy  leads to high aggregation, causing time-delay causality to vanish and instantaneous dependence to manifest. Although we expect such instantaneous dependence has consistency with the true causal relation in certain sense to make the discovery results meaningful, it remains unclear what type of consistency we need and when will such consistency be satisfied. We proposed functional consistency and conditional independence consistency in formal way correspond functional causal model-based methods and conditional independence-based methods respectively and provide the conditions under which these consistencies will hold. We show theoretically and experimentally that causal discovery results may be seriously distorted by aggregation especially in complete nonlinear case and we also find causal relationship still recoverable from aggregated data if we have partial linearity or appropriate prior.
Our findings suggest community should take a cautious and meticulous approach when interpreting causal discovery results from such data and show why and when aggregation will distort the performance of causal discovery methods.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper addresses an interesting problem of whether Granger-type causality is consistent with the instantaneous Graphical causal model even after temporal aggregation.
 
The authors seem to discuss some kind of invariance properties under temporal aggregation, assuming a few typical temporal causal structures, such as the chain and fork.

### Strengths
Addresses a fundamental problem of whether different definitions of causality are consistent or not.

### Weaknesses
 - Many concepts are poorly defined.
- The description is often qualitative and vague. It is hard to follow the line of thought of the authors.
 
Unfortunately, this paper is not clearly written. Here are instances of vagueness taken from Section 3.1 alone.
 
- VAR (1) is typically accepted as a linear model. It is not clear if f() covers another model. The terminology seems inconsistent to the notation.
- The number of variables seems to be s but not clearly defined.
- What "k is large" means is not clear.
- $g(k)$ is defined as "any normalization function like g(k)=1". Then, how do you guarantee that $(X_1 -X_{k+1})/g(k)$ vanishes?
- Definition 1 uses undefined terms such as "imply," "compatible," and "some degree of inconsistency." Their definition is not very clear.

### Questions
$g(k)$ is defined as "any normalization function like g(k)=1". Then, how do you guarantee that $(X_1 -X_{k+1})/g(k)$ vanishes?

### Soundness
2 fair

### Presentation
1 poor

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
In a lot of real world cases, data are actually generated from time-delayed causal relationships, but are reported by aggregating the data by some means. This paper analyses when this aggregation can be a problem for causal discovery algorithms. The authors investigate assumptions on the time-delayed causal relationships which may no longer hold on the aggregated data. As functional and constraint based methods work conditioned on these assumptions, this analysis provides insight into when these methods can fail. These results are corroborated with experiments.

### Strengths
- The paper deals with an interesting, important and understudied issue when it comes to causal discovery. This work raises important points for causal discovery with real world data.
- The paper is mostly clear in its exposition, although some sections can be strenghtened.

### Weaknesses
 - Section 3 is confusing, mainly due to the fact that some terms are a bit vague. While "functional consistency" is defined, it uses words like "compatible" and "degree of consistency" that are vague and confuse the definition. For example, does compatible seems to mean that the aggregated data is a function of the aggregated data and a noise term?  Furthermore, does $\hat{f}$ having some degree of consistency with underlying $f$ mean that they are the same function? As a result of this vagueness, the rest of this section is unclear. A clearer connection to why this consistency is needed would also help the reader a lot. Specifically, the definition of functional consistency does not explicitly state that the condition must hold for all possible values of X, which is a critical requirement for the definition to be meaningful. The current wording allows for the possibility that the condition holds only for some specific values of X, which would not be sufficient for the intended analysis.
 - I would have liked to see more experiments with various models. For example, only the LiNGAM algorithm is tested, what about ANM? Does the performance degrade for methods that do not make any functional assumptions (e.g. kernel based methods like KCDC [1])?
 - Theorem 1 is confusing to read as its not grammatically correct.
- Why does the infinite K only consider the linear model? Is this due to the previous section? This is not clear.
- Is there a way to validate the assumptions in Theorem 2?

### Questions
- Theorem 1 is confusing to read as its not grammatically correct.
- Why does the infinite K only consider the linear model? Is this due to the previous section? This is not clear.
- Is there a way to validate the assumptions in Theorem 2?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors provide theoretical conditions that are necessary to ensure the consistency of causal discovery results, including functional consistency and conditional independence consistency when analyzing temporally aggregated i.i.d. data.

### Strengths
1. The problem the authors seek to address is an interesting question that holds significance in the field of causal discovery. The authors discussed conditions needed to recover true causal relations from temporally aggregated data.
2. The authors conduct simulation experiments to support their claims.

### Weaknesses
1. I doubt that there is a technical flaw in the proof of Theorem 3, which is described in the Questions section.
2. The credibility of Corollary 1 is also in question, as it follows Theorem 3. This is mentioned in the Questions section.
3. While the name of Theorem 3 is "Necessary and Sufficient Condition for Conditional Independence Consistency," the content of "Theorem 3" only presents three equivalent statements that appear to just utilize the marginalization of the joint distribution. Please briefly explain how the three equivalent statements are necessary and sufficient conditions for conditional independence consistency if I misunderstand the point.
4. As mentioned in the limitation section, the paper discussed the impact of temporal aggregation but did not offer any resolution. Consequently, it is challenging to assess the significance of this paper's contribution.
5. Given Fig.2 and the discussion between 4.2 and Remark 1, the experimental results appear to illustrate that discussion rather than provide evidence for any significant claims in the main paper.

### Questions
1. Referencing specific equations is challenging as there is no index for the equations in the appendix.
2. In the proof of Theorem 3, the derivation from the third equation and the fourth equation below the sentence "On the left hand side (LHS):" is in question. The denominator of the third equation is $p_{S_Y, S_X}(S_Y, S_X)$ and $S_Y$ is a function of $Y_1,\cdots, Y_k$. Given this, it appears inappropriate to directly insert $p_{S_Y, S_X}(S_Y, S_X)$ into the integrand, as it is a function dependent on the integrated variables.
3. Even after ignoring the doubts in the proof of Theorem 3, Corollary 1 is questionable. Given Fig.2, how can $S_X$ independent with $Y_{1:k}$ given $S_Y$? In what situation does the "if" statement hold?
4. Could you state the necessary and sufficient conditions for conditional independence consistency in words, given the three equivalent statements in Theorem 3?
5. What does the $n$ mean in Theorem 1? Should it be $k$?
6. In definition 1, it said that "Moreover, the function $\hat{f}$ has some degree of consistency with the underlying causal function $f$." The phrase "some degree of consistency" is ambiguous; could it be explained more precisely?
7. Could you explain how to get the equation $f(X, e_1) + f(0, e_2) = f(0, e_1) + f(X, e_2)$ in the appendix?
8. Can you provide an explanation of how the second equality in $f(X_1,e_1)+f(X_2,e_2) = f_1(X_1)+f_1(X_2)+f_2(e_1)+f_2(e_2) = f_1(X_1 +X_2)+f_2(e_1)+f_2(e_2),$ is derived in the appendix?
9. There is no $\hat{f}$ appearing in the proof of Theorem 1; is it unrelated?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors focus on the problem of temporal aggregation.  In many real-world problems, data is aggregated at a very high scale, which may lead highly-dependent data to become i.i.d.  If we're interested in effects at the de-aggregated level, performing causal discovery at the aggregate level can lead to errors.  The authors define conditions for functional and conditional independence consistency under temporal aggregation.  They then provide some simulation experiments to demonstrate the dangers of aggregation.

### Strengths
The authors address a very important problem - they are correct that temporal aggregation is rampant and, if done carelessly, can result in problems such as the introduction of spurious effects.  For the most part, the authors motivate this well.  The division into functional consistency and CI consistency is logical and well-presented and, for the most part, the notation is clear.  The experiments that are there do a good job at providing an initial assessment of the soundness of their findings.

### Weaknesses
I think much of this paper is poorly explained, leading to some issues with understandability.  There are a few sentences, that occur at unfortunately important parts, that I had a hard time following.  I especially noted this in the description of the intuition behind Definition 1 and Theorem 1.
- For the paragraph after Definition 1, that first sentence is a run-on ("Intuitively, functional consistency might suggest X=f(X,e), here we introduce a different function f, which allows for the possibility"), and the sentence after that sounds very strange ("This is because actually existing such f is difficult for nonlinear case").
- Theorem 1 feels impossible to follow grammatically. "f has the form ___ is necessary for the functional equation ____ holds for some f and some e that is only related to e with ______"
Theorem 2 could also benefit from some discussion around intuition.  My understanding is that Theorems 1 and 2 are the main results of this paper (as the conditions for consistency for functional and CI-based methods).  However, Theorem 1 suffers from the grammatical lac of clarity I described above, and Theorem 2 introduces a whole new set of variables (alpha, beta, and gamma) that don't appear to ever be defined (though please let me know if I just missed them and they are defined somewhere).  Some intuitive discussion of these theorems, as well as an editing pass to increase clarity, would improve this paper significantly.

In Section 3.1, after equation 1, you suggest that g(k) can be any normalizing function, such as g(k)=1 or g(k)=k.  However, later in that section, you say that, as k becomes large, g(k) approaches 0, allowing you to remove that term under large k.  However, I'm not sure how that works in general when you say that g(k)=1 is a valid normalizing function (which will not tend to 0).  And g(k)=k will only tend to 0 with very large k, but no discussion (that I noticed) is ever had about how large k needs to be for the results of this paper to hold.  Especially since in the experiments, the largest k I see is 50, which doesn't feel large enough to assume that g(k) -> 0.

While the authors discuss the dangers of temporal aggregation at a high level in the intro, the only example actually provided in the intro (the effect of temperature on ice cream sales, aggregated daily) is actually one where temporal aggregation doesn't seem to pose a problem.  While the effects become instantaneous at the aggregate level, it's an effect that's consistent with the dynamics at the de-aggregated level and one that seems reasonable for causal discovery methods to detect.  With the focus on dangers of potentially spurious instantaneous relationships from aggregation, an example where such relationships can arise would be helpful for motivation.

The experiments are quite weak.  The authors present two sets of experiments: a simulation with a single, two-variable model that shows how Direct LiNGAM has issues as k increases (due to the non-Gaussianity assumpton?) and experiments with a three variable model with either a chain, fork, or collider structure, showing how CI tests perform poorly if no linearity is present.  If I'm understanding correctly, the second set of experiments doesn't actually contain any aggregation (it takes place over two time steps) and doesn't actually employ a specific causal discovery algorithm, focusing instead of the performance of CI tests.  These are reasonable first-step tests, but the lack of any remotely realistic data, data with more than 2-3 variables or across more than 2 time steps, and structures with any amount of complexity leaves the evaluation feeling very weak.

### Questions
In Section 4, why are only chain-like, fork-like, and collider-like models considered?  Given that the focus is on temporal aggregation, cycle structures are quite likely (e.g., X{t-1} -> Y{t}, Y{t-1} -> Z{t}, Z{t-1} -> X{t}).  Obviously, this causes problems upon aggregation if we don't have a way for our model to learn or reason about cyclic models, but this seems like the type of case that is especially relevant in a discussion about temporal aggregation.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the problem of Causal Discovery for Time-Series Data with IID samples. This problem is relevant for a variety of applications, such as healthcare, bioinformatics, economics and finance. In this submission, the author(s) study if causal discovery results obtained from IID time series data is consistent with the true causal process. To this end, the author(s) provide various theoretical results and experiments. The author(s) conclude that functional consistency is difficult to achieve in non-linear situations, and that even in linear non-Gaussian situations, the instantaneous model generated by temporal aggregation is still unidentifiable as the number the number of data points from the underlying causal process that are combined to form each observation goes to infinity.

### Strengths
In my opinion, this paper has the following strengths: (i) The problem is overall very relevant; (ii) the paper is well-written and easy to follow; (iii) the theoretical results are interesting. Overall, I believe that a discussion on identifiability and functional consistency of time-series data is needed.

### Weaknesses
Although this paper is mostly of theoretical interest, it would have been good to have more experiments. In the main text, the author(s) only consider simulated experiments on conditional independence tests and LiNGAM.



### Questions
In your submission, you discuss the relationship with faithfulness and conditional independence consistency. However, it can be argued that faithfulness is generally an unrealistic assumption in practice. Have you consider weaker assumptions, such as Causal Minimality (see i.e. Assumption 3 in [1])?

[1] https://arxiv.org/abs/2210.14706

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
