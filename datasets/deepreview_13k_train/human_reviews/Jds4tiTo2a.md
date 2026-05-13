# Diff-In: Data Influence Estimation with Differential Approximation

- Decision: Reject
- Scores: 6, 6, 6, 6

## Abstract
In this paper, we introduce a new formulation to approximate a sample's influence by accumulating the differences in influence between consecutive learning steps, which we term Diff-In. Specifically, we formulate the sample-wise influence as the cumulative sum of its changes/differences across successive training iterations. 
By employing second-order approximations, we approximate these difference terms with high accuracy while eliminating the need for model convexity required by existing methods.
Despite being a second-order method, Diff-In maintains computational complexity comparable to that of first-order methods and remains scalable. This efficiency is achieved by computing the product of the Hessian and gradient, which can be efficiently approximated using finite differences of first-order gradients. 
We assess the approximation accuracy of Diff-In both theoretically and empirically. Our theoretical analysis demonstrates that Diff-In achieves significantly lower approximation error compared to existing influence estimators. Extensive experiments further confirm its superior performance across multiple benchmark datasets in three data-centric tasks: data cleaning, data deletion, and coreset selection. 
Notably, our experiments on data pruning for large-scale vision-language pre-training show that Diff-In can scale to millions of data points and outperforms strong baselines.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes Diff-In to estimate the data influence by accumulating differences between consecutive training steps. Diff-In approximates data influence as temporal differences with second-order methods. However, its computational cost is comparable with a first-order method.

I am not an expert in data influence. I feel my assessment of the paper's novelty may not be accurate. However, I acknowledge the theoretical and empirical results presented in the paper, and think that this is a solid paper.

### Strengths
1. Novel Theoretical Framework: Provides rigorous mathematical formulation with error bounds for influence estimation without requiring model convexity.

2. Computational Efficiency: Achieves complexity comparable to first-order methods despite using second-order approximations through efficient Hessian-gradient product calculations.

3. Strong Empirical Results: Demonstrates consistent superior performance across data cleaning (9% improvement), data deletion (2% improvement), and coreset selection tasks on multiple datasets.

### Weaknesses
1. Checkpoint Dependency: Implementation relies heavily on saved checkpoints during training, with unclear guidelines on optimal checkpoint selection.

2. Limited Generalizability: Currently focused on sample-level influence, lacking broader application to model hyperparameters.

3. Theoretical Assumptions: Analysis assumes Lipschitz continuous gradients and bounded gradient norms, with limited discussion of assumption violations.

### Questions
Please refer to the weaknesses.

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
4

### Summary
The paper proposes a new formulation for influence estimation by accumulating differences in influence computation over iterative training timesteps, using second order approximations for the difference terms. The authors also conduct experiments in 3 task settings (data cleaning, data deletion, and coreset selection) and report performance alongside other influence computation methods and baselines.

### Strengths
- The approach to estimate influence by a second order approximation of the finite difference terms is novel.
- The results showcase that Diff-In can improve performance compared to the other methods considered in the paper.

### Weaknesses
Overall, I like the direction of the work, but find that it possesses certain issues, such as the (random) selection of checkpoints, missing experimental analysis and comparisons with other relevant influence methods, that would allow me to recommend acceptance. I am happy to engage more on the points listed below:

1. **Selecting Checkpoints (i.e. choosing $m$)**: I find the (hyperparameter) step of selecting checkpoints to be one of the major drawbacks with the approach as this is implicitly assumed by the method. While the authors conduct experiments on CIFAR-10 and ResNet-18 in Section 5.4 (and in Figure 2 on sampling strategies), these recommendations cannot generalize to new datasets and ideally this step will need to be carried out prior to utilizing Diff-In. That is, the appropriate value of $m$ might be different for other datasets and models, and it essentially becomes a hyperparameter in need of optimization. This step can be prohibitively expensive to undertake for models with a large number of parameters (e.g. LLMs). Furthermore, the authors recommend using random sampling to select the relevant set of checkpoints $\mathcal{T}_m$ which introduces another potential issue. It is possible, especially with small $m$ (i.e. $m=5$) that all the checkpoints chosen can lead to inaccurate estimation. That is, for the same setting of $m=5$, a practitioner utilizing Diff-In could obtain very different results, and it is not clear to me how this randomness in performance can be mitigated. Ideally, ablations on other datasets and models need to be undertaken to showcase if indeed the value of $m$ is general across datasets/models, which seems unlikely. 
2. **Missing Experimental Analysis**: First, I find that the paper is lacking more extensive comparison with other relevant influence based approaches. To truly assess the benefits of Diff-In, the authors should compare with recent influence approaches designed for larger models (such as EK-FAC [1], TRAK [2], and/or Arnoldi iteration [3]) and better Hessian-free methods (for instance, IP [4] and outlier gradient influence [5] seem to be very relevant for the data cleaning task). I think it is especially important to consider methods that circumvent the convexity assumption as we are dealing with larger models-- for e.g. EK-FAC estimates PBRF instead of LOO by using the Gauss-Newton Hessian instead of the standard Hessian. Second, I believe that for the data cleaning experiments of Section 5.1 the authors should consider standard influence estimation alongside self-influence as in prior work [5,6]. What are the results when the influence is computed on a clean validation set? Is Diff-In still the top performer? Third, since the paper claims that Diff-In remains scalable across larger models, I believe it is necessary to have more comprehensive analysis of running time especially with larger models and other methods. Specifically, running time analysis should be conducted on other datasets/models (preferably larger models) where both performance and running time should be provided for comparison. I also feel that the time taken to select the ideal number of checkpoints $m$ (if not fixed as 5) should be factored in as well. 
3. **Data Deletion and Machine Unlearning**: The data deletion setting seems to me to be conceptually equivalent to undertaking machine unlearning [7] and as the unlearning community has studied this problem extensively, it would be useful to utilize some recent and popular approaches (refer to [7]) for fair comparison (and not just 2 influence approaches). I would also suggest that the authors reframe this subsection and task to reflect that it is conceptually just unlearning (or otherwise list out the key differences). Data deletion in past work [5,6] has usually allowed one model retraining, and so that readers are not confused I think this should be made clear both in name and through better descriptions by referring to it as unlearning.
4. **Adding to Related Works**: Despite a comprehensive related works in the appendix, I think there are a number of papers that should also be discussed that are currently missing. Alongside a few of the papers mentioned above (for experimental comparison), it would also be beneficial to include descriptions on methods such as Datamodels [8], LoGra [9], tree estimation [10], HyDRA [11], data reweighing [12], among other relevant work in this space [13,14].
5. **Typos**: There are some typos in the paper that can be revised. For instance on line 84 (page 2), "TraceIn" -> "TracIn", and the section heading for Section 3 should read "Appromati" -> "Approximation". There are also repeated references: for instance, the paper "On second-order group influence functions for black-box predictions" by Basu et al appears twice in the bibliography.

### Questions
Each of the weaknesses listed above can be considered as a question.

### Soundness
3

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
This paper introduces Diff-In, a novel approach for estimating the influence of training samples across multiple learning steps. The core innovation of Diff-In lies in approximating the second-order Hessian-gradient product using only first-order computations. This approach enables Diff-In to achieve the high accuracy typical of second-order methods while maintaining the computational efficiency of first-order techniques.  Theoretical analysis and extensive experiments support Diff-In's effectiveness.

### Strengths
- The paper is well-written and clearly structured, making the methodology easy to follow.
- The formulation is intuitive, and the theoretical analysis appears generally sound.
- Experimental results show Diff-In's effectiveness.

### Weaknesses
 - Diff-In closely follows TraceIn’s approach of accumulating influence over successive training steps. The main technical advancement appears to be an extension of TraceIn’s formulation (Eq. 3) to Eq. 5, limiting its novelty.
- The baseline choices are somewhat outdated, and the authors should include comparisons with more recent state-of-the-art methods, such as [1-2]. Specifically, the absence of comparisons with methods that leverage second-order information more directly, such as those based on Hessian approximations, is a notable gap.
- Additionally, speed comparisons with these newer approaches are missing, which would provide a more comprehensive evaluation. Furthermore, the computational cost of the proposed method, particularly in terms of memory usage for storing intermediate gradients and Hessian approximations, needs to be more thoroughly analyzed, especially for large-scale models and datasets.

### Questions
- The authors evaluate Diff-In through downstream applications but do not consider counterfactual-type metrics, such as the Linear Data Modeling Score (LDS) introduced in [2]. Would such metrics provide further insight into Diff-In's performance?
- While Figure 3 demonstrates that Diff-In incurs minimal computational overhead compared to TracIn, this may be limited to smaller models. Could the authors provide similar speed comparisons for large-scale models?

### Soundness
3

### Presentation
3

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
This paper introduces a novel method called Diff-In for estimating the influence of data points during model training. Unlike existing methods that rely on convexity assumptions or first-order approximations, Diff-In calculates the cumulative differences in influence between consecutive training steps. By using second-order approximations of the Hessian-gradient product, it achieves higher accuracy without increasing computational complexity. The approach is scalable and can be applied to large datasets. Extensive experiments demonstrate that Diff-In outperforms previous methods in data-centric tasks like data cleaning, data deletion, and coreset selection, particularly excelling in large-scale vision-language pretraining tasks.

### Strengths
- Innovative Approach: Diff-In offers a fresh perspective by focusing on the temporal differences in influence, which significantly improves accuracy without relying on model convexity. Moreover, Diff-In achieves second-order estimation accuracy with computational complexity similar to first-order methods, combining high accuracy with efficiency.
- Scalability: The method is computationally efficient and scalable to large datasets, making it suitable for modern machine learning applications. 
- Comprehensive Evaluation: The paper presents extensive experiments on various tasks, demonstrating Diff-In’s superior performance over existing methods across several benchmarks.

### Weaknesses
 - Polynomial growth of estimation error: The theoretical upper limit of the Diff-In estimation error grows polynomially with the number of training steps. This growth, while better than exponential, may still limit the scalability of the method, particularly in scenarios involving very long training times or complex models where the parameter space is vast and the optimization landscape is highly non-convex. The paper should explore the practical implications of this polynomial error growth more thoroughly, perhaps by examining how the error scales with the number of training steps in different model architectures and datasets. A more detailed analysis of the trade-off between training steps T and error would be beneficial for understanding the method's limitations.
- Matching between data quality and model capabilities: Using influence scores directly for data management does not seem to take into account the matching of data quality and model capabilities. For example, when performing core set selection, can only considering the influence score alone really select a high-quality data subset or a subset that is most helpful for downstream tasks? The influence score, as currently used, might prioritize data points that are influential in the training process but not necessarily those that are most informative or representative of the underlying data distribution. This could lead to a coreset that is not optimal for generalization or for specific downstream tasks. The method should consider incorporating a mechanism to assess the quality of the selected data points in relation to the model's learning capacity and downstream task requirements.

### Questions
None

### Soundness
4

### Presentation
4

### Contribution
4
