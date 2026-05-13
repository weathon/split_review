# Generalized Group Data Attribution

- Decision: Reject
- Scores: 3, 3, 5, 5

## Abstract
Data Attribution (DA) methods quantify the influence of individual training data points on model outputs and have broad applications such as explainability, data selection, and noisy label identification. However, existing DA methods are often computationally intensive, limiting their applicability to large-scale machine learning models. 
To address this challenge, we introduce the Generalized Group Data Attribution (GGDA) framework, which computationally simplifies DA by attributing to groups of training points instead of individual ones. GGDA is a general framework that subsumes existing attribution methods and can be applied to new DA techniques as they emerge. It allows users to optimize the trade-off between efficiency and fidelity based on their needs. Our empirical results demonstrate that GGDA applied to popular DA methods such as Influence Functions, TracIn, and TRAK results in upto \textbf{10x-50x} speedups over standard DA methods while gracefully trading off attribution fidelity. For downstream applications such as dataset pruning and noisy label identification, 
we demonstrate that GGDA significantly improves computational efficiency and maintains effectiveness, enabling practical applications in large-scale machine learning scenarios that were previously infeasible.%\footnote{Code is available in the supplementary material}

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes Generalized Group Data Attribution - a method for combining individual data attribution (scores indicating the influence of single training points for single test predictions) into group data attributions (scores indicating the influence of groups of training points for model properties). The resulting attributions are faster to estimate and enable a variety of downstream applications.

### Strengths
The paper is clearly written and addresses an important problem, namely the resource-intensive nature of many data attribution methods. The proposed solution is clearly explained, and the writing is clear and concise.

### Weaknesses
In my opinion, the main weakness of this paper is the novelty and depth of the investigation. As far as I can tell, the paper proposes turning a point-to-point data attribution method into a group-to-group data attribution method by effectively summing the corresponding individual attributions. This does not seem so fundamental a contribution---e.g., the fact that this reduces sample complexity from O(# points) to O(# groups) seems to follow directly by construction, as without loss of generality one can just call each group a "datapoint." 

I think that a more in-depth investigation of the mechanism by which individual attributions are combined could strengthen the paper---for example, are there weighting schemes that improve performance? Are robust estimators (e.g., the median) qualitatively different than taking the average? I also think that the application section could be more fleshed out - the dataset pruning results are the most interesting to me: further investigation into the source of success of GGDA (variance reduction? Soft thresholding? Etc.) would have improved the analysis.

### Questions
See weaknesses above. Also - is there any intuition for why grad-k-means works so well as a clustering method?

### Soundness
4

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper addresses data attribution estimation, which assesses the contribution of a training sample to a model’s generalization according to a downstream performance metric. While data attribution is beneficial for tasks like data pruning and correcting mislabeled samples, it is often computationally impractical, as its demands scale linearly with the number of training samples. To tackle this, the authors propose Generalized Group Data Attribution (GGDA), which shifts attribution from individual samples to groups of samples. They demonstrate that K-means clustering on activation gradients is an effective heuristic for forming these groups. The authors reframe traditional attribution metrics, including the Leave-One-Out and gradient-based metrics, and apply GGDA to dataset pruning and noisy-label identification in small-scale experiments on MNIST, CIFAR-10, HELOC, and TRAC.

## Claims
1.	GGDA can be applied to any sample-based data attribution method.
2.	It trades attribution fidelity for computational efficiency.
3.	GGDA significantly speeds up data attribution.
4.	It is effective for noisy-label identification and data pruning.
5.	GGDA enables practical applications for large-scale machine learning.

### Strengths
The paper is well-written, clearly defining introduced concepts, and is well-motivated, as improving computational efficiency in data attribution is valuable for large-scale machine learning. The authors investigate a generally applicable approach to enhance the computational efficiency of data attribution methods, as claimed. The use a variety of data (tabular, image, text) modalities to validate their approach in downstream supervised learning tasks.

### Weaknesses
Weaknesses

1.	The experimental datasets (e.g., MNIST, CIFAR-10) are relatively small, calling into question GGDA’s scalability claims for large-scale ML. Can the method be tested on a larger dataset like ImageNet? Does it maintain an effective compute-fidelity tradeoff as sample size increases? Specifically, the paper lacks a clear analysis of how the computational cost of group formation (e.g., K-means clustering) scales with the number of training samples and the number of groups. It is unclear if the speedups observed on small datasets will translate to larger datasets where the cost of clustering may become a bottleneck.
2.	In Section 4, line 272, the authors claim computational advantages for group data attribution. However, in line 265, they note that “a single batched gradient computation is roughly equivalent in runtime to individual per-sample gradients.” Do the results in Tables 1, 2, and 3 use the best available per-sample data attribution methods? Are implementation of individual per-sample gradient-based methods batched, for example via vmap functionals? The paper should clarify whether the per-sample gradient computations are optimized using techniques like vectorization or if they are implemented in a naive, iterative manner. This is crucial for a fair comparison of computational efficiency.
3.	Tables lack clarity regarding ± symbols. Do these indicate multiple trials with different seeds? Are groups recomputed for each trial? Why are the values ±0.0 in Table 1? It is unclear if the reported standard deviations are across different random initializations of the model, different data splits, or different group assignments. The paper needs to explicitly state the experimental procedure used to generate the reported statistics.
4.	Tables 1 and 2 do not include baselines for no data removal. This makes it difficult to assess the absolute performance of GGDA in data pruning. Without a baseline, it is unclear if the reported results are better than simply not removing any data.
5.	The rationale for clustering by activation gradient, rather than activations alone, is unclear. Aren’t gradients inherently dependent on activations? Could further intuition be provided? The paper should provide a more detailed explanation of why gradients are a better feature for clustering than activations, especially since gradients are computed with respect to a loss function and may be more sensitive to the specific training process.

### Questions
1.	It is a bit surprising that group data attribution improves the data selection fidelity. How does GGDA achieve that, and could this improvement be due to the group selection heuristic rather than the method itself?

### Soundness
1

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
The paper “Generalized Group Data Attribution” introduces the GGDA framework, designed to enhance data attribution efficiency by grouping training data points. GGDA aggregates training data into groups instead of handling individual points, significantly improving computational efficiency while maintaining comparable accuracy. It extends popular attribution methods like Influence Functions, TracIn, and TRAK to group-based settings, making them suitable for large-scale datasets.

Extensive experiments on various datasets and models validate GGDA’s performance in tasks like dataset pruning and noisy label detection, demonstrating its effectiveness and scalability. However, the paper could benefit from more experiments on real-world large-scale datasets, as well as a deeper theoretical analysis of the K-Means grouping strategy, which plays a critical role in enhancing attribution efficiency yet lacks detailed discussion in the theoretical framework.

Overall, GGDA shows promise for data attribution, but needs further validation for large-scale dataset use and a deeper theoretical analysis of the K-Means grouping strategy.

### Strengths
The paper's experimental section introduces K-Means clustering in gradient space as part of the grouping strategy. This innovative design improves attribution accuracy. The approach demonstrates significant advantages in different attribution tasks, such as dataset pruning and noisy label detection, validating its applicability across various scenarios.

### Weaknesses
1.  **Absence of Large-Scale Dataset Experiments**: The experiments primarily focus on small to medium-scale datasets, leaving out truly large-scale datasets (e.g., billion-level data). To better demonstrate GGDA’s scalability, future work should incorporate experiments on large-scale datasets and report both computational efficiency and attribution performance in such scenarios. The current experiments do not adequately demonstrate the method's ability to handle the complexities of real-world data distributions and high dimensionality often encountered in large-scale settings. This limitation makes it difficult to assess the practical applicability of the proposed method in industrial or large research contexts.
2.  **Lack of K-Means Analysis**: K-Means plays a vital role in the proposed method's effectiveness, but the paper lacks theoretical analysis and runtime details for this component. This omission limits the evaluation of its feasibility and efficiency. Providing more detailed descriptions in the appendix or code repository would enhance reproducibility for researchers. Specifically, the paper should address the sensitivity of the K-Means clustering to initialization, the convergence properties within the gradient space, and the impact of different distance metrics used in the clustering process. Furthermore, the computational cost of K-Means, especially in high-dimensional gradient spaces, needs to be thoroughly analyzed and reported.

### Questions
1. Do the authors plan to conduct experiments on large-scale datasets (e.g., billion-level data) in future work to further validate the scalability and attribution performance of GGDA?
2. The paper lacks details on K-Means runtime and theoretical analysis. The authors could add these implementation details in the appendix to facilitate reproducibility, especially considering that K-Means in the gradient space can be time-consuming when the gradient space is large.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes to generalize the traditional data attribution method to consider attributing to (1) groups of data points instead of individual data points, and (2) the property function that captures model behavior beyond the test loss.

### Strengths
Overall
1. The motivation is clear.
2. The definitions and the problem formulation are consistent throughout.
3. The experimental results are presented cleanly.

### Weaknesses
The main weaknesses are the novelty and soundness of both proposals:
1. The second proposal, "property function," is already known in the literature as "target function." For example, see [1] in statistics, and [2] in data attribution.
2. The first proposal, considering groups of data points, doesn't seem to have the claimed computational gain by looking at the analysis for the Influence Function.
    - From Section 4, the analysis is true obviously since there are no conceptual differences from the influence function (together with the target function concept mentioned above). While I'm not sure about the computational complexity advantage claimed in the paper (batch gradient computation $\approx$ per gradient computation), from my understanding, for whatever algorithm is used to approximate the iHVP (inverse-Hessian vector product) computation, constructing $H_{\theta} = \sum_{i=1}^{n} \nabla_\theta^2 \ell(x_i)$ will inevitably scale with $n$. Hence, the claimed computational advantage is not there at least until Line 266. 
    - It's better to bring the idea of batched $H_{\theta}$ as in the TRAK paragraph for $\hat{F}_{\theta}^{\text{batched}}$ to the Influence Function analysis to demonstrate the claimed advantage.

       However, even with the batched approximation of $H_{\theta}$, some theoretical justification is lacking. Whether this will be a good approximation is unclear to me. Additionally, as described in Line 319, some clustering algorithms are needed in order to obtain a small approximation error on $\nabla_{\theta}\ell(x_i)$, which I suppose will make the algorithm scale with $n$ again.

Overall, the second proposal (*property function*) already exists in the literature, while for the first proposal (*grouped data points*), I'm not convinced by the claimed computational efficiency gain for the Influence function and TRAK when Hessian or (empirical) FIM are involved. Without a justification for an efficient and good approximation of the Hessian (and its inverse with iHVP computation), such an extension is trivial from the linearity of IF, TRAK, and related influence-function-based methods.

### Questions
See Weaknesses. Additionally:
1. In Section 4, the definition of TracIn is not standard, at least deviating from the original paper and even ignoring the scaling. It only sums over batches that contain a particular training sample $x_i$, not over all iterations unless we're considering full-batch training. I think this should be mentioned.
2. The *Gradient K-Means* grouping method in the experiment suffers from the issue I raise above (2), where when we need to consider individual gradients, the claimed computational efficiency goes away.

Some minor suggestions in writing:
1. Line 120, replace $\mathcal{D} = \\{(x_0, y_0), (x_1, y_1), \\ldots (x_n y_n)\\}$ by $\\mathcal{D} = \\{(x_0, y_0), (x_1, y_1), \\ldots , (x_n, y_n)\\}$ (two "," are missing).
2. Line 217 and 266, replace $k << n$ by $k \\ll n$.
3. Line 232, replace - with --- without spaces at the beginning (before TRAK) and the ending (after TracIn).
4. Line 252, replace `\citep{}` with `\citet{}`.
5. Line 276~288, tracein should all be TracIn?

### Soundness
3

### Presentation
3

### Contribution
2
