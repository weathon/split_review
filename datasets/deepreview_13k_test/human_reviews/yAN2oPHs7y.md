# Neuro-Symbolic Rule Lists

- Decision: Reject
- Scores: 6, 5, 3, 6

## Abstract
Machine learning models deployed in sensitive areas such as healthcare must be interpretable to ensure accountability and fairness.
Rule lists (\textbf{if} $\texttt{Age} < 35 \,\land\,  \texttt{Priors}  > 0$ \textbf{then} $\texttt{Recidivism} = \texttt{True}$, \textbf{else if} Next Condition \dots)
offer full transparency, making them well-suited for high-stakes decisions.
However, learning such rule lists presents significant challenges.
Existing methods based on combinatorial optimization require feature pre-discretization and impose restrictions on rule size. 
Neuro-symbolic methods use more scalable continuous optimization yet place similar pre-discretization constraints and suffer from unstable optimization.
To address the existing limitations, we introduce \ourmethod, an end-to-end trainable model that unifies discretization, rule learning, and rule order into a 
single differentiable framework. 
We formulate a continuous relaxation of the rule list learning problem that converges to a strict rule list through temperature annealing.
\ourmethod learns both the discretizations of individual features, as well as their combination into conjunctive rules without any pre-processing or restrictions.
Extensive experiments demonstrate that \ourmethod consistently outperforms both combinatorial and neuro-symbolic methods,
effectively learning simple and complex rules, as well as their order, across a wide range of datasets.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces Neuro-Symbolic Rule Lists (NyRules), an upgrade to standard rule
lists -- a well known class of white-box classifiers -- that in addition to learning
rules also learn how to discretize continuous input features automatically.  (This
is where the "neuro-symbolic" moniker comes form.)  This feat is achieved by
introducing a continuous relaxation of rule list learning, which is combinatorial
in nature.  NyRules is similar in spirit to existing differentiable rule learning
approaches, except it focuses specifically on rule lists and reuses/improves upon some
key techniques: 1) differentiable thresholding functions from Yang et al.,
used as-is; 2) the differentiable conjunction-of-a-subset operation from Xu et al., improved
to avoid vanishing gradients; 3) linear relaxation + annealing to enable end-to-end learning of
the rule list.  NyRules are evaluated on several data sets against several
competitors.

**Post-rebuttal**: I bumped the score to 6 based on the author's additional experiments and clarifications.

### Strengths
**Originality**:  NyRules combines existing ideas and improves on them.  The level of novelty is acceptable.

**Quality**: All technical contributions appear to be good.  The experiments are carried out on several "real-world" data sets as well as on synthetic data, and the results are 5-fold cross-validated (which is refreshing; however: why 5 and not 10+?). The choice of competitors is also sensible.  Performance improvement on "real-world" data is rather robust, although not dramatic in most cases (see also Weaknesses).

**Clarity**: The text is generally well written, and figures/plots are altogether clean and useful.  However, parts of the manuscript feel a bit rushed: I was puzzled by a few equations (which are not always entirely formal) and statements, see below.

**Significance**: NyRules contributes to research on differentiable rule learning, well motivated by explainability requirements.  The contribution is neither niche nor exceedingly significant.

### Weaknesses
**Quality**: 

- There is a pretty big issue with Table 1, which I wish sorted out:  in many situations, XGBoost performs *much* better than any of the competitors,   yet it is never marked in bold in Table 1.  This is the case also for the rings dataset.  This choice is not explained in the text (I may have missed it!) and risks conveying a twisted perception of performance improvement.

  I understand that boosted trees can be less interpretable than rule lists, and that -- since the paper does not attempt to evaluate interpretability of learned models at all -- this cannot be demonstrated.  But as a result, the results hyperfocus on prediction accuracy, where NyRules does *not* have an edge over XGBoost (to the best of my understanding).

  **Suggestion**: the authors should explicitly explain in the paper why XGBoost results are not bolded, even when they outperform other methods, and clarify that the focus is on comparing interpretable rule-based methods, with XGBoost included as a non-interpretable benchmark. Adding this explanation would provide important context and avoid potential misinterpretation of the results.

- A key issue is that there is not specific study of the impact of the threshold learning step, which is a big selling point of the proposed method.  I am left wondering whether it is indeed important for performance and interpretability.

  **Suggestion**:  the authors could conduct an ablation specifically focused on the threshold learning component by, e.g., comparing NyRules with a version that uses pre-discretized features, to directly demonstrate the impact of learned thresholds on performance and potentially on interpretability.

- The authors equate rule length with interpretability, but this is not exactly exact.

  **Suggestion**: the authors should acknowledge this limitation in the Limitations section discussing that while rule length is used as a proxy for interpretability, a more comprehensive evaluation of interpretability, ideally including user studies, would provide a more accurate assessment.

**Clarity**:

- NeSy is **neuro**-symbolic because the perceptual component -- responsible for encoding low-level inputs such as images into high-level symbolic variables -- is implemented using neural networks.  In this paper the perception component is minimal: it corresponds to the thresholding step.  I honestly feel calling the proposed method "neuro-symbolic" is a stretch, and could be interpreted as disrespectful of what people in NeSy AI aim to do.  I am not going to penalize the paper based on this, but I wanted to make it clear that I did not appreciate this choice.

- Some equations are repeated unnecessarily (the definition of r(.) and eq. 2).

- p2: Last equation: $\alpha \le x_i \le \beta$ is not a function, it is a condition; please add an indicator function.  This also applies to line 184.

- Eq 1: rl(.) is undefined.

- Eq 1: the "s.t." does not make much sense, because this is neither a satisfiability nor an optimization problem.  It should be replaced with an if-and-only-if.  In short, I'd write:
$$
  rl(x) = c_j \qquad \Leftrightarrow \qquad \exists j s.t. (a_j(x) = 1) \land \forall i . p_i > p_j . (a_i(x) = 0).
$$
Since priorities are unique, the condition $i \ne j$ is unnecessary.  Actually, in its current form the equation seems incorrect, as it requires lower-priority conditions not to fire (i \ne j, p_i < p_j), which to the best of my understanding is not needed.  Or did I get this wrong?

- line 188: mangled sentence.

- line 262: what does the argmax_l act on?  The argument is c.

- line 278: same.

- I cannot follow the comment at line 280: what is the point of talking about boosted rule sets at this point?  This is the only place in the paper where they are mentioned.

I am willing to increase my score provided the authors address the main issues I raised.

### Questions
- Feel free to discuss any of the main weaknesses I listed above.

- line 204: "In the end, we seek to obtain strict logical rules for use in a rule list."  If I understand correctly, once the temperature is low enough, the learned predicates will already be "almost" discrete.  At this stage, couldn't you just replace them with their hard counterparts, and obtain a hard rule list classifier?  The lower the temperature, the closer the original soft RL classifier and the corresponding hard RL classifier will behave in terms of predictions and loss, meaning there's little to be gained, performance-wise, from using the soft version, and much to be gained (for the few inputs that fall in the affected region of input space), interpretability-wise, by using the hard version.  So why not do that?  Have you evaluated empirically what happens if you follow this route?

- Appendix C: what split did you use for evaluating performance during grid search?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper paper proposes a novel end-to-end differentiable model to learn rule lists called NyRules and addresses limitations from existing work.
The method takes into account the discretisation of continuous features into predicates, the learning of conjunctions & rules as well as the ordering of the rules into rule lists.
NyRules performances were validated on both synthetic and real world datasets and compared to existing methods.

### Strengths
The paper is clearly written and of great quality.
The solution proposed to solve the vanishing gradients for the chosen computation of the conjunction is well formulated and the efficiency of the relaxation proven with the ablation study.
Supplementary material (with code) is provided for reproducibility.

### Weaknesses
Major comments:
- Discretization on the fly has already be done in existing works (for example: _Kusters, Remy, Yusik Kim, Marine Collery, Christian de Sainte Marie, and Shubham Gupta. "Differentiable Rule Induction with Learned Relational Features." In International Workshop on Neural-Symbolic Learning and Reasoning. 2022_). However, the thresholding layer presented in this paper is still very relevant and different from _Kusters et al_ approach for instance.
The paper's contributions need to be put into perspective. Also a comparison between the two different thresholding layers would strengthen the quality of the paper.
- The improvements provided by the rule ordering are not proven. An additional ablation study would be required in order to differentiate the impact of the predicate layer and the active priority. Especially for comparison with RLNet which is also a neural-based approach to learn rule lists.
- The final else (with no predicates) in the rule list is not described nor explained.
- The fact that $l=2$ (binary classification) in the entire paper should be mentioned from start explicitly. It is indirectly mentioned only in 3.4 where the BCE loss is specified, in 5.1 where only datasets for binary classification are used and in future works (6.2). The reader is told this method is applicable for multi-classification with parameter $l$.
- The interpretation of $c_j$ in the rules is not explicit. "if $a_j$ then $c_j$" is then converted in Figure 1 into "if [...] then P(Disease) = 94%" for example. Where is that value coming from ? softmax of $c_j$ ? I believe it needs to be explicit.

Other comments:
- Related work is lacking contributions from different fields. For instance, fuzzy logics with studies like _van Krieken, Emile, Erman Acar, and Frank van Harmelen. "Analyzing differentiable fuzzy logic operators." Artificial Intelligence 302 (2022): 103602._ which analysed different differentiable logical conjunctions.
- The description of the temperature annealing schedule seems to be missing.
- In 3.3 the number of rules $k$ and the number of classes $l$ _are_ (typo?) fixed beforehand. 
- Figure 3.c, X1=1 and X2=1 = 0 ?
- References to datasets sources are missing
- Pre-processing of the datasets is not described. How are the datasets continuous feature discretised for other methods ?
- The distribution of the features types in the datasets could be provided to highlight the relevance of the predicate layer of NyRules.

### Questions
- Answers / changes following the major comments listed above will address most of the limitations of this current version of the paper.

Additional questions:
- The relevance of the predicate layer is highlighted for the Ring dataset that has exclusively continuous features. Did you observe a drop in performance compared to other methods for datasets with no continuous features ? 
- Have you tried other differentiable logical conjunction layers ?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper presents a rule learning system for numerical data, that integrates discretization and learning. This is, by itself, not a novel contribution. Classic rule learning algorithms such as Ripper can do that as well. It also optimizes the rule order of the resulting list, which is a somewhat debatable contribution, because rules in a decision list are not independent of the order. This is also a problem for interpretability, BTW. Results are presented in F1-scores, which is somewhat unconventional for work in this area, and makes a comparison harder. I also miss a comparison to the (still) standard benchmark Ripper, in the Java implementation available, e.g., in Weka (this is important, the Python implementation Wittgenstein is considerably worse, and unfortunately many of the published claims of superiority over Ripper are based on that implementation). As a result, I find it hard to assess the value of this work. I do think that the paper (although generally well written) could be much stronger and more credible with respect to the experimental evaluation.

### Strengths
- nice formal presentation of the work

### Weaknesses
- experimental results are somewhat non-standard, in particular the use of F1. Why do you think F1 is a good measure for evaluating classification problems? It is quite adequate for information retrieval, because there is an asymmetry between the positive and negative class, so that it is o.k. that unretrieved irrelevant documents do not influence the result, but I don't see why ignoring true negatives should be a good idea in any of the problems studied here.

- The results also seem to be flawed at times. For example, results of CORELS at 0.33 or 0.27 when other algorithms are above 0.9 (similar for SBRL) indicate for me that the algorithms have not been adequately used. Possible explanations could be that they did not learn any rules, or learned for the wrong class, or similar. In my view, no algorithm can be as bad as 0.16 for Titanic. I guess you could invert its predictions and would get a better result (this would be clearer if accuracy had been used as an evaluation metric).

- The authors seem to assume that decision lists are just an ordering of rules. Of course, an ordered rule set is a decision list, but the opposite is not true. This affects optimality and interpretability. Consider, for example the decision list
IF A then +
ELSIF B then -
ELSIF C then +
ELSE -
Note that each rule is only valid in context. It is, e.g., not true that all C's are positive, only if they are not B.
If you simply reorder the rules in the decision list (e.g., by swapping the two positive rules) this may drastically change the semantics. This is why classical rule learning algorithms like Ripper always learn a decision list in Sequence (Ripper does optimize it later on). 

On the other hand, you could also rewrite the decision list as a rule set as follows:
IF A then +
IF B and NOT A then -
IF C and NOT B and NOT A then +
In that case, you could reorder the rules as you wish. If rules like this are learned, they would be longer (which would be consistent with what the authors observed on their algorithm), but, on the other hand, the ordering is practically irrelevant.

So probably, the authors learn a mixture of both (optimizing both the order and the rule bodies at the same time), but this should be discussed deeper.

- The ordering also has an effect on interpretability, of course. A long decision list cannot be easily interpreted, because the rules cannot be interpreted independently, you always have to interpret them in context of all previous rules. So the claim already posed in the introduction that decision lists are interpretable is debatable, in particular for long lists. It does hold if rules can be interpreted independently, but in that case the order would be irrelevant (see above). The authors should more clearly discuss the trade-off between ordered rules and interpretability.

UPDATE: Based on the authors' response, I have downgraded my evaluation. They provide results for Ripper, but they seem to be flawed or at least not reproducible with the provided information. See my reply for details.

### Questions
Is there a reference for GREEDY? What implementations of the algorithms did you use?

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
4

### Summary
This paper proposes a new framework for learning rule lists by gradient descent, named NyRules. First, the authors introduce a differentiable representation of a rule list using some existing techniques, such as the Gumbel-Softmax. Then, they formulate the task of learning a rule list that minimizes the empirical risk and the constraints on the support as a continuous optimization problem. One of the advantages of the proposed method is that it does not require pre-processing steps such as discretization and rule mining, which are required by most existing methods and often incur additional computational costs. Experimental results demonstrated that the proposed method achieved good accuracy compared to the baselines across all the datasets.

### Strengths
Overall, I like this paper, and I think the authors make solid contributions to the community on interpretable machine learning. 
- S1. This paper is well-written, well-organized, and easy to follow. 
- S2. The authors introduce a differentiable representation of rule lists, which is a novel approach to the best of my knowledge. While the proposed representation mainly consists of existing methods, including [Yang et al. 2018], [Xu et al. 2024], and [Jang et al. 2017], it also includes some unique techniques, such as relaxed formulation for alleviating the vanishing gradients issues. In addition, I think the illustrative demonstration of each continuous relaxation (Figures 3 and 4) helps readers understand the effectiveness of the proposed approach well. 
- S3. The experimental results demonstrated that the proposed method often achieved better accuracy than the existing methods. The proposed method also attained comparable accuracy to XGBoost, which was surprising to me.

### Weaknesses
While I think this is a good paper, I believe the following concerns should be addressed to improve the quality of this paper: 
- W1. One of my major concerns is the computational cost of the proposed method. I could not find the experimental results on the running times of the proposed method and baselines, even in the appendix. To claim that the proposed method overcomes the scalability issue of the existing methods, I think the running time of the proposed method should be compared with the existing methods. Although I agree that it is a desirable advantage that the proposed method does not require discretization and rule mining as pre-processing, I am worried about the scalability of the proposed method because its average running time was not reported in the paper. 
- W2. This paper looks to be missing descriptions of some important information. For example, this paper seems to assume a binary classification task implicitly. I think it should be explicitly mentioned at, for example, the beginning of Section 2. In addition, as mentioned above, this paper seems to lack the experimental results on the computational times of the proposed method and baselines. I think such information should be reported because scalability is one of the important factors for practitioners when deciding which algorithm they should use for their task.

### Questions
- Q1. Could you show the experimental results on the average running times of the proposed method to the baselines? 
- Q2 (optional). From the objective function in Section 3.4, the proposed method does not explicitly impose constraints on the sparsity of predicates in each rule. However, from Figure 5(b), the experimental results suggest that the proposed method tends to obtain sparse rules, which was surprising to me. Did you carry out any post-processing for it? In addition, I guess that the required length of each rule to maintain sufficient accuracy may vary depending on the dataset. Does the trend in Figure 5(b) differ depending on the dataset?
- Q3 (optional). In the learning problem of the proposed method, the constraints on minimum and maximum supports are relaxed as soft constraints (i.e., regularizer). In the experiments, how often did the learned rule lists violate the constraints on minimum and maximum supports? Also, while the learned rule lists may not violate this constraint if we set $\lambda$ to be a sufficiently large value, how does it affect the accuracy or computational cost of the proposed method?
- Q4 (optional). If I understand correctly, the proposed learning algorithm gradually decreases the annealing temperatures $t_{\pi}$ and $t_{rl}$. Could you show the pseudo-code of a procedure for determining the values of $t_{\pi}$ and $t_{rl}$ in each step during training?

### Soundness
3

### Presentation
3

### Contribution
3
