# An Investigation of Representation and Allocation Harms in Contrastive Learning

- Decision: Accept
- Scores: 5, 6, 8

## Abstract
The effect of underrepresentation on the performance of minority groups is known to be a serious problem in supervised learning settings; however, it has been underexplored so far in the context of self-supervised learning (SSL). In this paper, we demonstrate that contrastive learning (CL), a popular variant of SSL, tends to collapse representations of minority groups with certain majority groups. We refer to this phenomenon as representation harm and demonstrate it on image and text datasets using the corresponding popular CL methods. Furthermore, our causal mediation analysis of allocation harm on a downstream classification task reveals that representation harm is partly responsible for it, thus emphasizing the importance of studying and mitigating representation harm. Finally, we provide a theoretical explanation for representation harm using a stochastic block model that leads to a representational neural collapse in a contrastive learning setting.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The study presented in this paper concentrates on examining how contrastive learning (CL) can cause representation harm, particularly when certain groups are not adequately represented in the training data. The researchers demonstrate that these underrepresented groups often merge into other semantically similar groups that are better represented. Further, through a theoretical analysis involving graphs, it is shown that increased connectivity between two groups of nodes leads to their convergence. Lastly, a causal analysis reveals that the detrimental effects on representation caused by CL are irreparable for subsequent tasks, even when a probe is trained using the CL representations.

### Strengths
1.	The composition of the paper is clear and comprehensive, discussing results in depth and highlighting representational harm. The paper offers practical insights to diminish the adverse effects of CL techniques.
2.	Section 4 presents an intriguing analysis, exploring how representational biases can lead to allocation disparities.
3.	The paper's empirical research is commendable, and its theoretical framework provides a robust underpinning for the empirical observations. The outcomes from both empirical and theoretical perspectives appear promising.

### Weaknesses
1.	The text in the figures is too small for easy readability and needs enlargement for better clarity.
2.	A more thorough justification is needed for the chosen metric of representation harm, given its critical importance to the paper's analysis.
3.	The necessity for different data setups in Sections 5 and 6, particularly the choice of causal mediation analysis for Section 6, lacks proper motivation and explanation.
4.	The paper's primary limitation is the absence of a comprehensive large-scale study, especially in the realm of self-supervised learning (SSL).

### Questions
See weaknesses above

### Soundness
2 fair

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the effect of under-representation on the performance of minority groups in the context of self-supervised learning (SSL), specifically contrastive learning (CL). They show that CL tends to collapse representations of minority groups with certain majority groups, leading to representation harms and downstream allocation harms even when labeled data is balanced. Theory and experiments are presented to support their results.

### Strengths
1. This is a well written paper that discusses an important topic that is well motivated. This rigorous analysis is likely of interest to practitioners and useful to mitigate the potential harm from CL methods.
2. The empirical study is good and the theoretical study adds a solid foundation to the empirical results. Both empirical and theoretical findings are promising.
3. Section 4 is also quite interesting, showing how representation harms can cause allocation harms.

### Weaknesses
1. There needs to be an intuitive definition of allocative harms and representation harms when they are first mentioned in the intro, which matches the precise definition in section 2.
2. Figure text is generally too small to see clearly.
3. Why does this metric for representation harm make sense? It seems like an important decision critical for the rest of the paper, so needs better justification. Specifically, the use of cosine similarity for image embeddings and a different metric for text embeddings needs a clearer rationale. The choice of metric impacts the interpretation of results and should be rigorously defended.
4. The examples used in section 2 are not very useful - sure automobiles and trucks could collapse but is it the worst thing - are there more compelling real-world examples to illustrate these problems? The current example does not highlight the potential for real-world harm.
5. Why are the metrics for representation harm in 2.1.2 and 2.2.2 different? This seems weird. Even if the exact distance (eg cosine vs l2 for image or word embeddings) are different - why are the metrics different? The difference in metrics makes it difficult to compare the results across different datasets and scenarios, and the rationale for this difference is not clear.
6. Why do sections 5 and 6 require a different data setup? Specifically, why is causal mediation analysis the right framework to study section 6 - this was not motivated. It is not clear why a causal framework is necessary, and what other frameworks could be considered. The motivation for using causal mediation analysis is not strong enough and the reasons for not using other frameworks are not discussed.
7. The empirical analysis is conducted only on CIFAR10 and BIASBIOS datasets - I would have liked to see more to further strengthen the results in the paper, such as including celebA which is quite standard for studying biases in vision models, or perhaps even with results on a CLIP model for results on image-text models.

### Questions
see weaknesses above

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper focuses on studying the issue of representation harm in contrastive learning (CL) that arises when some groups are underrepresented in the training corpora. In this case, the authors show that the underrepresented groups tend to collapse into semantically similar groups (that are not underrepresented). In a follow up theoretical analysis on graphs, the authors show that two groups of nodes tend to collapse as their connectivity increases. Finally, through a causal analysis, the authors show that the representation harms caused by CL cannot be mitigated for downstream tasks when training a probe on top of the CL representations.

### Strengths
1. The paper studies an important problem in self-supervised learning through contrastive objectives (that of representation collapse of groups that are underrepresented in the training data)
2. It does so in a sound and systematic way, by providing evidence on controlled images (CIFAR10), imbalanced text (BiasBios) and a theoretical analysis with artificial graphs.
3. The paper is well written, with a thorough discussion of results and potential insufficiencies of an existing class of algorithms in overcoming representation harm, showing how more work is needed in the area of CL to result in algorithms that are robust to underrepresentation of certain groups (which can be hard to identify at scale to begin with).

### Weaknesses
The main weakness I can find from this paper is the lack of a large-scale study. SSL, and CL in particular, are most effective when used on large amounts of data. The controlled studies in this paper allow us to analyze the existing representation harms. However, it can be seen that these values are generally much lower for BiasBios than for CIFAR10. On the other hand, this could be due to the different domain (text). A study on ImageNet (larger number of both samples and classes) could potentially disentangle this confound. In particular, it would be interesting to know whether having more diversity in the data alleviates learning spurious features (e.g. collapsing classes with similar background colors), and reduces collapse of underrepresented groups. Furthermore, the use of a fixed 75%/25% split of the test set for training and evaluating the linear probe, respectively, is not standard practice. A more robust approach would involve using a separate validation set, or employing cross-validation techniques to ensure the reliability of the probe's performance and avoid potential overfitting to a specific subset of the test data.

### Questions
1. Typo “a” at the end of line 6 in page 2
2. You could use diverging palettes (with a neutral color at 1.0) in the heatmaps, to clearly distinguish HR<1. Having a colorbar next to each heatmap figure would also improve readability.
3. In Figure 2, do you have any idea why there’s such a large difference (10%) between deer and horse collapsing?
4. In line 4 of Sec 2.1.2, you can add “of classes” after “a pair” to help the reader understand better 
5. In Sec 2.2.2, when you define the GRH metric, I would have found it useful to have a sketch of a plane with boundaries that show what each region means. It’s something you could consider adding when you get an extra page
6. In Sec 4.2, why do you train on 75% of the Test set?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
