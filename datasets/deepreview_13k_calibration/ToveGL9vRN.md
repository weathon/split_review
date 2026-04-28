# Since Faithfulness Fails: The Performance Limits of Neural Causal Discovery

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 5, 6

## Abstract
Neural causal discovery methods have recently improved in terms of scalability and computational efficiency.
However, there are still opportunities for improving their accuracy in uncovering causal structures.
We argue that the key obstacle in unlocking this potential is the faithfulness assumption, commonly used by contemporary neural approaches. We show that this assumption, which is often not satisfied in real-world or synthetic datasets, limits the effectiveness of existing methods. We evaluate
the impact of
faithfulness violations both qualitatively and quantitatively and provide a unified evaluation framework to facilitate further research.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper posits that the primary obstacle in neural causal discovery is the faithfulness assumption frequently used by modern neural approaches. It examines the impact of violations of this assumption both qualitatively and quantitatively, and provides a unified evaluation framework to facilitate further research.

### Strengths
- The main claim of this work is that progress in causal discovery requires moving beyond the faithfulness assumption, which is a reasonable standpoint. The key experimental findings are:
 >- despite advancements in causal discovery over the past few years, $ESHD_{CPDAG}$ and $F1-Score_{CPDAG}$ metrics do not improve significantly. 
>-  structure discovery accuracy does not scale with the amount of data. 
>-  variations in MLP architecture have minimal impact on performance.

-  develop techniques to measure how faithfulness violations degrade performance (Figure 4 is particularly interesting) and set an
upper bound for current benchmarks.

-  The paper is well-written.

### Weaknesses
 - Line 71 : $U_{i}$ is assumed to be 1-dimensional.  Justify.
- Please justify the additive noise assumption. 
- > Faithfulness assumption can be violated, for example, in a situation when paths cancel each other effects out, leading to statistical independence despite an existing causal relationship. 

**Give concrete example**
 - Expected SHD between CPDAGs has been discussed; there is no discussion about $F1-Score_{CPDAG}$
 -  Why do Table 1 and Section 3.2  miss the result on ER(5, 1)? 
 - why do you exclude *DIFFUSION MODELS FOR CAUSAL DISCOVERY
VIA TOPOLOGICAL ORDERING* in your analysis? 

- > To provide a comprehensive evaluation, we explored architectures with 1, 2, and 3 layers, configured
with 4, 8, and 16 hidden units.

**why do you think this is sufficient to conclude *variations in MLP architecture have minimal impact on performance* ?**

- The faithfulness metric, denoted DeFaith needs more detailed discussion. For example, 
>  To address this, we introduce a degree of faithfulness metric, denoted DeFaith, to measure how well statistical dependencies correspond to the true graph’s d-separation properties. Inspired by Zhang & Spirtes (2003), we use Spearman’s rank correlation coefficient to quantify the conditional dependencies in the dataset. We define a predictor of d-separation based on the coefficient.

**Please clearly state what is the predictor here.**
**More discussion is needed around the quality of this predictor itself**.

- The paper does not address how to design neural causal discovery methods without the faithfulness assumption.

### Questions
Please see Weaknesses

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
3

### Summary
This paper experimentally demonstrates that violating the faithfulness assumption is the key obstacle in improving the performance of existing neural causal discovery methods. In this paper, the authors introduce a metric to measure the degree of faithfulness violation, and also proposed a method to compute an experimental bound on the causal discovery performance.

### Strengths
- I totally agree with the authors on the assertion that faithfulness violations might be the key reason why the performance within the current causal discovery paradigm is limited to a large extent. I am happy to see the experimental support presented in this work.
    
- The proposed metric of faithfulness violations also makes sense
    
- The paper is well organized in a logical manner, and is easy to follow.

### Weaknesses
 - The analyses presented in the paper are only experimental, lacking a theoretical foundation. Although they provide some insights, it might be not convincing enough to generalize to other scenarios.
    
- The proposed method to compute experimental upper bound is highly unlikely to scale up.

### Questions
- Why assuming additive noise SCMs in the paper?
    
- How general is the proposed faithfulness metric? At what conditions does it work?
    
- Why not choosing NOTEARS or its variants as baselines? I think NOTEARS might be one of the most well-known neural causal discovery methods?
    
- Since MLPs have universally strong fitting abilities, the loss easily converges to zero or a very small value when training a network for each parent set. In this case, it is possible that the log-likelihood losses of many DAGs lead to zero or a very small value or have very similar value. If so, how to identify the true DAG?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper has claimed that progress in causal discovery requires moving beyond the faithfulness assumption. The experiments shows that the violation of faithfulness would degrade performance. To clearly quantify this phenomenon, a metric called DeFaith has been proposed. Also, as the increase of sample size, the performance of different methods, including DCDI, BayseDAG, DiBS, SCCD, don’t show improvement or even show degraded performance. To investigate the limits of different socre-based neural causal discovery methods, an algorithm called NN-opt has been proposed which consists two step. Through NN-opt, the upper bound of the neural method could be estimated.

### Strengths
1. This paper touches some important theoretical aspects of neural causal discovery.
2. Several ordinary causal approaches are compared.

### Weaknesses
1. The theoretical analysis can be built more in depth to justify the arguements of the paper.



### Questions
Q1:In the structure evaluation, Expected SHD between CPDAGs and Expected F1-Score between CPDAGs have been defined. Compared to other metrics such as SHD and SID, is there any strength or reason to use them?

Q2:DeFaith is proposed to evaluated the faithfulness, but could this metric accurately describe the change of the faithfulness? Could you give more theoretical analysis about the reality between the faithfulness and DeFaith? It is better if this quantification can be justified to be more theoretically "close" to the faithfulness.

Q3:As mentioned before, NN-opt could compute the upper bound of specific methods. In step 2, which is exhaustive graph search, it is not feasible in practice. Is there any way to improve the method to make it practiced?

Q4:In this paper, several methods have been evaluated to search the upper bound of these methods using different sample size and neural structures. From the aspect of experiments, the methods evaluated in the paper may only include some typical ones among all methods and it’s more persuasive to compare more socre-based neural causal discovery methods. Could you give some reason of the selection of the four methods?

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
4

### Summary
The paper presents the idea that the ''faithfulness assumption" is holding back the improvements in the neural causal discovery research. The work starts with empirically demonstrating the strenghts and limitations of neural causal discovery. To this end, a benchmark is proposed where several of the discovery algorithms are evaluated.  Then a degree of faithfulness metric is proposed that is helpful to estimate to what degree does faithfulness effect the discovery algorithms.

### Strengths
1. The premise is really interesting. Identifying the faithfulness assumption as the main culprit is an important hypothesis that can have wide ranging impact.

2. The paper is relatively well written.

### Weaknesses
There are several issues with the paper that forces me to go with a lower rating.

1. Although the premise is interesting, the overall work does not justify the premise. For example, using a AUC-ROC curve to measure faithfulness is not very well justified. Also quantifying the conditional dependecies by a correlation coefficient is not very innovative/interesting.

2. The works talks about why such assumptions are a problem for real world datasets, but the experimental evaluations are on synthetic data sets. This kind of defeats the message.

3. The NN-opt method seems to pretty expensive since all possible DAG's are being evaluated.

4. In Fig 2, SDCD and Bayes DAF do show a downward trend so maybe more evaluations are required before claiming that there is no improvement in the ESHD metric.

5. Spell check required. Eg: Masuring -> Measuring in heading of Section 4.

### Questions
Please look at the weaknesses section. Furthermore,

1. Were there any ablation studies conducted for the neural networks as functional aprroximators?

2. I do not see the point of Fig 1 to be honest. It gives no specific information.

### Soundness
2

### Presentation
3

### Contribution
2
