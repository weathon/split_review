# Algorithm for Concept Extrapolation: Diverse Generalization via Selective Disagreement

- Decision: Reject
- Scores: 5, 6, 6, 5

## Abstract
Standard deep learning approaches often struggle to handle out-of-distribution data, especially when the distributional shift breaks spurious correlations. While some approaches to handling spurious correlations under distributional shift aim to separate causal and spurious features without access to target distribution data, they rely on labeled data from different domains or contingent assumptions about the nature of neural representations. Existing methods that do make use of unlabeled target data make strict assumptions about the target data distribution. To overcome these limitations, we present the Algorithm for Concept Extrapolation (ACE). Using an exponentially-weighted disagreement loss to maximize disagreement on target instances \textit{that break spurious correlations}, ACE achieves state of the art performance on spurious complete correlation benchmarks. We also show ACE is robust to unlabeled target distributions where spurious and ground truth features are not statistically independent. Finally, we demonstrate the applicability of ACE for handling goal-misgeneralization in deep reinforcement learning, with our ``ACE agent'' achieving a 16% higher level completion rate in the CoinRun goal misgeneralisation problem when the coin is randomly placed in the level.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This study proposes a novel method, termed ACE, to address the issue of pseudo-correlation under distribution shifts, which is a challenging problem in the field of machine learning.

------

Thank the authors for their response and the additional experiments! I still believe that the paper should be further enhanced regarding clarity, especially in terms of the presentation of the algorithm's practicality and complexity. Additionally, the paper could benefit from more comparative baselines.

### Strengths
1. The performance improvements of the ACE algorithm compared to existing techniques are demonstrated across multiple benchmark tests.
2. The paper highlights the robustness of the ACE algorithm to variations in target distribution mixture rates, which is an important characteristic.

### Weaknesses
1.	Based solely on the descriptions provided in the paper, there remains some confusion regarding the application of this method. The paper should include an algorithm or pseudocode to clarify how to utilize this algorithm to address practical problems.
2.	The lack of experiments conducted on datasets other than images, especially text classification datasets, imposes certain limitations on the applicability of this method. In fact, there are many datasets in the text domain that exhibit spurious correlations, such as the CivilComments dataset. Furthermore, even within image datasets, additional datasets, such as CelebA and IN9, should be explored.
3.	The paper does not discuss the computational complexity of this algorithm, which is an important consideration for its scalability in practical applications.
4.	Although the experimental results demonstrate effectiveness, the paper does not provide sufficient theoretical support to explain why the ACE algorithm is effective, particularly regarding the choice of the exponential weighting scheme.
5.	The paper lacks a detailed introduction to the comparative baselines. To my knowledge, many methods included in the comparison, such as CORAL, IRM, ERM, and GroupDRO, were developed prior to 2020. Additionally, more advanced methods, such as LISA (2022) and Fish (2022), should also be included in the comparisons.

### Questions
See weaknesses.

### Soundness
2

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
4

### Summary
The authors introduce the Algorithm for Concept Extrapolation (ACE), which aims to learn multiple classifiers that maintain high accuracy on source distribution data while strategically disagreeing on target distribution instances that violate spurious correlations. The key idea is an exponentially-weighted disagreement loss that encourages classifier disagreement primarily on instances likely to break correlations, combined with an approach to batch size selection based on expected "mix rates" (the frequency of correlation-breaking instances). The authors provide theoretical motivation through a feature interpolation model and argue that access to unlabeled target data makes the problem more tractable than trying to learn all possible generalizations from source data alone.

The paper validates ACE through a battery of experiments showing superior performance to prior methods across multiple benchmarks. On standard spurious correlation tasks (WaterbirdsCC, CIFAR-MNIST), ACE achieves state-of-the-art results. More impressively, on the challenging Spawrious M2M-Hard dataset involving multiple interacting spurious correlations, ACE achieves 92.47% accuracy compared to the previous best of 68.93%. The authors also demonstrate ACE's robustness to varying mix rates through experiments on a custom HappyFaces dataset, showing it outperforms DivDis across all mix rates tested.

### Strengths
- The paper offers a clear motivation for why access to unlabeled target data makes the problem more tractable than trying to learn all possible generalizations. It then goes on to clearly formulate how spurious correlations manifest in target distributions through "mix rates". The authors also offer a thoughtful analysis of why previous approaches (like DivDis) might fail when their distributional assumptions are violated, situating the paper well in literature.
- The exponentially-weighted disagreement loss is a clever way to focus on likely correlation-breaking instances. The batch size analysis further provides practical guidance for implementation.
- The method is evaluated across a variety of tasks and compared with multiple baselines. Strong experimental results bolster the validitiy of the method on both classification and RL tasks. Results suggest clear improvement over baselines across different mix rates. The authors also offer careful ablation of mix rate effects with different batch sizes.

### Weaknesses
 - The strong experimental results come with important caveats: the method requires target validation data for hyperparameter tuning, uses different backbone networks than baselines, and requires careful batch size selection based on expected mix rates that may be difficult to estimate in practice. The authors also claim broader relevance to AI alignment problems like reward tampering and sycophancy, though these applications remain largely theoretical.
- There are some methodological concerns as well. For instance, there is no statistical significance testing or error bars reported. There is a heavy reliance on artificially constructed datasets (HappyFaces) rather than real-world data and it appears to me that HappyFaces dataset was created using facial expression detection that likely has its own biases.
- The paper could benefit from more extensive ablation studies isolating impact of different components.

### Questions
See Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a new method for handling out-of-distribution generalization in deep learning, particularly when spurious correlations in training data are not present in a new evaluation domain. The core idea is that disagreement on testing data between models that solve the training data might be a good proxy for when an example is ``hard’’ because the correlations in training break down. They leverage this signal to train a classifier on a loss that encourages disagreement on examples where correlations in training break down, but agreement on other test examples. This method achieves better performance on out of domain generalization evaluations, including a goal misgeneralization benchmark task.

My understanding is that maximizing disagreement on test examples is not new and that is the core idea of the baseline disdiv. The new idea is that disagreement should only be maximized on examples that are correlation breaking, and the disagreement of many trained classifiers could be a signal for when correlation breaking occurs. 

This is not my domain of expertise, so I am not confident about whether they evaluated all relevant baselines, chose good benchmarks to evaluate on, or made good assumptions.

Use /citep and not /cite when, all of these citations are formatted incorrectly. 

I think there are some typos in the math notation and I think another pass or two is necessary to get this up to make sure the rigor is uniform. In particular, try to be clear what the difference between a feature and a classifier is in the set up-- my understanding is that features and classifiers have the same type signature, i.e., something that maps from X to Y. Also consider trying to factor out a layer of superscript/subscript in the notation, I know that’s hard, but some of the terms are rough. That being said, the core ideas are communicated and I can see that the set up and method sections aim for a high level of rigor, which I appreciate. 





Typo in formulation, the definition of similarity between f and g is missing an f line 100

Like 107, a lone * should by f*

The definition of the ground truth feature and spurious features suddenly becomes much less rigorous and technical. I think you should maintain the level or rigor here. What is a feature, what is correlated to what?

Line 288 four key claims, only three claims stated though

### Strengths
See review

### Weaknesses
This paper introduces a new method for handling out-of-distribution generalization in deep learning, particularly when spurious correlations in training data are not present in a new evaluation domain. The core idea is that disagreement on testing data between models that solve the training data might be a good proxy for when an example is ``hard’’ because the correlations in training break down. They leverage this signal to train a classifier on a loss that encourages disagreement on examples where correlations in training break down, but agreement on other test examples. This method achieves better performance on out of domain generalization evaluations, including a goal misgeneralization benchmark task.

My understanding is that maximizing disagreement on test examples is not new and that is the core idea of the baseline disdiv. The new idea is that disagreement should only be maximized on examples that are correlation breaking, and the disagreement of many trained classifiers could be a signal for when correlation breaking occurs. 

This is not my domain of expertise, so I am not confident about whether they evaluated all relevant baselines, chose good benchmarks to evaluate on, or made good assumptions.

I think there are some typos in the math notation and I think another pass or two is necessary to get this up to make sure the rigor is uniform. In particular, try to be clear what the difference between a feature and a classifier is in the set up-- my understanding is that features and classifiers have the same type signature, i.e., something that maps from X to Y. Also consider trying to factor out a layer of superscript/subscript in the notation, I know that’s hard, but some of the terms are rough. That being said, the core ideas are communicated and I can see that the set up and method sections aim for a high level of rigor, which I appreciate.



Typo in formulation, the definition of similarity between f and g is missing an f line 100

Like 107, a lone * should by f*

The definition of the ground truth feature and spurious features suddenly becomes much less rigorous and technical. I think you should maintain the level or rigor here. What is a feature, what is correlated to what?

Line 288 four key claims, only three claims stated though

### Questions
see review

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents ACE, algorithm for concept extrapolation, which uses unlabeled data from the target distribution to learn more robust models. The key idea is to learn to diverse classifiers on the source distribution which disagree on the correlation-breaking instances from the target distribution. Empricailly, ACE performs well on two datasets containing spurious correlations and also in an RL setting with goal-misgeneralization. Importantly, ACE works well even with a low amount of spurious correlation breaking instances in the target distribution, unlike prior work.

### Strengths
1. The proposed method is principled and the paper makes interesting arguments (although more conceptual / intuition based) on: (a) why it makes more sense to focus on predictive diversity compared to representational diversity (sec 2.2) ; (b) why focusing only on correlation-breaking instances from the target dataset makes more sense than using all unlabeled examples from the target distribution.

2. The proposed method is reasonably simple, where only an additional regularization term based on disagreement is added.

3. The paper shows that the proposed method, ACE has a particular advantage over existing methods at low target mix rate.

4. The paper also shows connections between spurious correlations and goal misgeneralization/reward hacking which is interesting, and the proposed method also shows initial promise for it (Figure 3)

### Weaknesses
1. The baselines in the main tables (1 and 2) are hard to interpret since they use a different backbone model than the proposed method ACE. (ResNet vs ClipVIT). Given that, it’s not clear if the improvements are just due to a better backbone model or due to the proposed method.

2. Missing Ablations — one of the main claims in the paper and the main difference from prior work (DAT-B) is to only focus on correlation breaking instances in the target dataset instead of using all unlabeled examples. It would be useful to have this ablation to empirically show this.

3. The paper only focuses on the setting of complete spurious correlations i.e. the spurious and ground true feature both always agree on the source dataset. While that is fine to use for controlled setting, the paper would be much stronger if it also showed results on a realistic setting with non-zero source rate. 

    a. Realistically, the true feature should perfectly explain the source dataset (up to some noise) whereas the spurious feature should not. 

    b. Additionally, the paper could be much stronger if it evaluated on more naturally occurring spurious correlations rather than artificially created as in CIFAR-MNIST or M2M (e.g. MultiNLI or CivilComments-WILDS as used in https://arxiv.org/pdf/2107.09044) 

4. (minor) Missing baselines — given that DivDis is a very similar method and already used in Table 1, it’s unclear why that baseline is not reported for other results such as in Table 2.

### Questions
1. Line 104 — does this mean the no. of classifiers required is exponential?

2. Line 100 – missing f?

3. Line 106 – missing f in f*?

4. Line 190: the the learned classifiers → the learned classifiers

5. Line 229 – missing “)” 

6. Line 288 – mentions ‘four key claims’ but there seem to be only three.

7. Line 429 — ‘where the coin in placed’ → ‘where the coin is placed’

8. \citet{} vs \citep{} — in a lot of places the citation should not be in text i.e. in bracket using \citep{}. 

9. Overall the paper could benefit from proofreading once more!

### Soundness
3

### Presentation
2

### Contribution
2
