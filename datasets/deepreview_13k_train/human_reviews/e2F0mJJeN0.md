# Geometric Median (GM) Matching for Robust Data Pruning

- Decision: Reject
- Scores: 3, 3, 3

## Abstract
Data pruning, the combinatorial task of selecting a small and informative subset from a large dataset, is crucial for mitigating the enormous computational costs associated with training data-hungry modern deep learning models at scale. Since large-scale data collections are invariably noisy, developing data pruning strategies that remain robust even in the presence of corruption is critical in practice. Unfortunately, the existing heuristics for (robust) data pruning lack theoretical coherence and rely on heroic assumptions, that are, often unattainable, by the very nature of the problem setting. Moreover, these strategies often yield sub-optimal neural scaling laws even compared to random sampling, especially in scenarios involving strong corruption and aggressive pruning rates -- making provably robust data pruning an open challenge. In response, in this work, we propose Geometric Median ($\gm$) Matching -- a herding~\citep{welling2009herding} style greedy algorithm -- that yields a $k$-subset such that the mean of the subset approximates the geometric median of the (potentially) noisy dataset. Theoretically, we show that $\gm$ Matching enjoys an improved $\gO(1/k)$ scaling over $\gO(1/\sqrt{k})$ scaling of uniform sampling; while achieving the optimal breakdown point of 1/2 even under arbitrary corruption. Extensive experiments across popular deep learning benchmarks indicate that $\gm$ Matching consistently outperforms prior state-of-the-art; the gains become more profound at high rates of corruption and aggressive pruning rates; making $\gm$ Matching a strong baseline for future research in robust data pruning.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposed a data pruning method based on geometric median-guided sampling. Moreover, the author presents a solver with a relatively fast convergence rate. The experimental results, to some extent, demonstrate the effectiveness of this method.

### Strengths
See the summarization part.

### Weaknesses
1. It is rather difficult for me to identify the innovative points of the proposed scheme in this paper compared to previous methods. For instance, the Moderate based on Geometric Median is also available in other approaches [1,2]. In the context of research progress, innovation is the key driving force. Without clear differentiating factors, it becomes challenging to justify the novelty and significance of this new scheme within the existing body of knowledge. There should be a distinct advantage or a novel application aspect that sets it apart from what has been done before.

2. The experiments in this paper are highly insufficient. They are still centered around CIFAR and Tiny-ImageNet. I don't believe these experimental scenarios are adequate to prove the effectiveness of the Pruning algorithm, nor can they easily reflect the application value of the algorithm. The real scenarios where data pruning plays a significant role should be in the learning process of VLM and LLM. In the field of data-driven research, the choice of experimental datasets directly impacts the reliability and generalizability of the results. Restricting these relatively small-scale and specific datasets fails to capture the complexity and diversity of real-world applications. To truly evaluate the potential of a Pruning algorithm, it is essential to test it in more relevant and challenging environments such as those encountered in the training of large-scale language and vision models.

3. I have some doubts regarding the theoretical analysis in this paper. Firstly, there is a lack of theoretical analysis of the generalization performance of the Coreset results. Moreover, as far as I know, there isn't necessarily a connection between the so-called **neighborhood of the true mean** targeted by Theorem 1 and the actual final performance. Theorem 1 also lacks some intuitive explanations and valuable inferences. Theoretical analysis provides the foundation for understanding the behavior and potential of an algorithm. The absence of these key elements in the theoretical part raises concerns about the overall validity of the proposed approach.

### Questions
See the weakness part.

### Soundness
3

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
This paper presents an efficient and simple algorithm for data pruning in the presence of noise, along with a theoretical guarantee on the estimation error.

### Strengths
The paper is well written and easy to follow.

### Weaknesses
1. Some important references and comparisons are missing, e.g. [1] Robust Data Pruning under Label Noise via Maximizing Re-labeling Accuracy.(NeurIPs 2023), [2] Feature Distribution Matching by Optimal Transport for Effective and Robust Coreset Selection.(AAAI 2024). The reported performance is not SOTA.
2. The main idea of the paper is to utilize the Geometric Median instead of the empirical mean objective in moment matching. However, as mentioned, both Geometric Median and Moment Matching have been extensively studied in the literature. The novelty is quite limited.
3. Some expressions and notation could be more precise.
   - In Eq. 2 and Eq. 3, are the dimensions of $ x $ and $ \theta_t $ consistent? Is $ x \in \mathbb{R}^d $? Additionally, what does $ x_t $ represent, and is $ x_t \in D_S $?
   - In Eq. 6, what is $ S $? Is it equivalent to $ D_S $?

### Questions
1. How does the proposed method distinguish between hard samples and noise samples? For instance, in Figure 1, if there are currently no perturbed data points (i.e., the data forms a bimodal distribution with both the red and blue regions representing clean data), GM Matching might only cover the blue region and fail to encompass the red region. The authors claim that existing methods tend to select simpler samples, which can make them susceptible to outliers. However, it seems that GM Matching may not guarantee that the selected data points cover the entire data distribution and could misclassify clean samples (or hard samples) as noise samples, potentially resulting in a biased subset. It might be beneficial for the authors to consider how the method could better address the practical performance of data pruning alongside robustness guarantees.
2. What does "breakdown point" refer to? Is there a formal definition? Additionally, how is the optimal breakdown point of 1/2 achieved? It's better to provide further explanation or mathematical proof .
3. How are the convergence rates $ O(1/k) $ and $ O(1/\sqrt{k}) $ defined and estimated in the paper? I am unsure if these refer to convergence rates, scaling, or some other asymptotic metric. Furthermore, the proposed method is said to have better convergence rates compared to random sampling. Given that $ \mu_\epsilon^{GM} $ needs to be approximated rather than computed directly, shouldn't of the calculation of convergence rates consider the computational process involved in estimating $ \mu_\epsilon^{GM} $?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes a data pruning method for noisy labeled datasets, which uses geimetric median matching to find the coreset. This paper first describes the moment matching and then describes the geometric median matching. Experiments are conducted on three datasets CIFAR10, CIFAR100 and Tiny-ImageNet.

### Strengths
1. It is very meaningful to solve the problem of data pruning in the noisy label scene.

### Weaknesses
1. The coverage of related work is not enough, which is not consistent with contribution point one. Many existing works study the robust data pruning in noisy scenarios (e.g. [1]Prune4R4L, [2]FDMat). The performance of these methods is much higher than that of the proposed GM matching.
2. The motivation of the paper is unclear and the difference from baseline (Moderate) is not described. The contribution of the paper is unclear. The baseline (Moderate) appears to perform a similar function, selecting a coreset based on distances to class centers. However, the paper does not adequately explain how the proposed geometric median matching approach differs fundamentally from this baseline, particularly in the context of noisy datasets. Without a clear distinction, the novelty and significance of the proposed method are difficult to ascertain.
3. The paper is poorly written. The description of the formulas lacks rigor, with **nearly all formulas** containing undefined symbols and incorrect descriptions. These issues hinder the overall understanding of the paper.

    For example,
    in Eq. 1, (1) ${x_{i}}$  is not distinguished (${x_{i}\in D}$ and ${x_{i}\in D_{S}}$); (2)What does ${X_{i}}$ mean ? Is ${X_{i}}$ a feature or a sample ?

    in Eq.2, what does $<,>$ mean? Why does ${x_{i}\in D}$ become ${x \in D}$ ?

    in Eq.3, what does $\theta_{t}$ mean? and what does $\theta_{T}$ mean ?

    in Eq.4, what does $z$ mean ?

    in Eq.5, what does $\mu^{GM}_{\epsilon}$ mean ?

    in Eq.6,  Why does ${x_{i}\in D}$ become ${x_{i} \in S}$ ? What is ${S}$ ?

     **There are various errors in all the following formulas.**

### Questions
1. The description of the paper is so poor that it seriously affects understanding.
2. The performance presented in the paper is not state-of-the-art, and there is a lack of comparison with the latest methods (e.g. [1-3]).

### Soundness
1

### Presentation
1

### Contribution
1
