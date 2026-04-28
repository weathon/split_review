# An Effective Universal Polynomial Basis for Spectral Graph Neural Networks

- Decision: Reject
- Avg Score: 4.50
- Scores: 6, 3, 6, 3

## Abstract
\eat{They have been extensively explored in the spectral perspective, referred to as {\em graph filters}.}
Spectral Graph Neural Networks (GNNs), also referred to as {\em graph filters} have gained increasing prevalence for heterophily graphs. Optimal graph filters rely on Laplacian eigendecomposition for Fourier transform. In an attempt to avert the prohibitive computations, numerous polynomial filters by leveraging distinct polynomials have been proposed to approximate the desired graph filters. However, polynomials in the majority of polynomial filters are {\em predefined} and remain {\em fixed} across all graphs, failing to accommodate the diverse heterophily degrees across different graphs. To tackle this issue, we first investigate the correlation between polynomial bases of desired graph filters and the degrees of graph heterophily via a thorough theoretical analysis. Afterward, we develop an adaptive heterophily basis by incorporating graph heterophily degrees. Subsequently, we integrate this heterophily basis with the homophily basis, creating a universal polynomial basis {\em \newbasis}. In consequence, we devise a general polynomial filter {\em \ours}. Comprehensive experiments on both real-world and synthetic datasets with varying heterophily degrees significantly support the superiority of \ours, demonstrating the effectiveness and generality of \newbasis, as well as its promising capability as a new method for graph analysis.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Learning on heterophilous graphs comes with underlying obstacles since most GNN models and spectral filters are based on homophily assumption. This paper expects to address this problem by designing a new graph filter combining both traditional homophilous bases and the proposed heterophilous bases. Specifically, the authors explore the correlation between homophily ratio and Euclidean space angles in spectral space, based on which the homophilous ratio-related bases can be established. 

The experiments show the superiority of the proposed UniFilter on both homophilous datasets and heterophilous datasets. The analysis and ablation study strongly demonstrate the effectiveness of the proposed heterophilous bases which can adaptively capture useful heterophilous and homophilous information.

### Strengths
[Novelty] The main idea of designing homophilous-related bases is insightful and instructive. By investigating the correlation between homophily and bases, the well-designed heterophilous bases can adaptively and effectively address heterophilous graphs according to the homophilous ratio.
[Theoretical] The proposed UniFilter has strong theoretical support. It is partially guaranteed that the introduced heteraphilous filters can capture heterophilous information.
[Experiments] The  analysis of spectrum distribution of the learned frequencies clearly illustrated how the homophilous and heterophilous information is learned on different datasets.

### Weaknesses
1. [Related works] The paper loses investigations of the works also concentrating on heterophilous graphs [1-5]. The authors should compare these methods both experimentally as well conceptually, and explain the differences and relations. For example, [4] addresses heterophilous via combining different filters where each filter can be regarded as a basis, which is somehow similar to the proposed works. It is not sufficient to only compare with a subset of these methods; a comprehensive comparison is needed to fully contextualize the contribution.
2. [Completeness] This method will be effective under some assumptions, but the authors do not discuss the limitations. One example is as below.
3. [Theoretical] Theorem 3 shows the relationship between expectation and theta. However, the expectation is not accurate enough, especially when the distribution of spectra signal has a large variance, and at that time, constructing the basis according to theta would be invalid for capturing signals with extreme eigenvalue. The paper does not adequately address how the method performs when the spectral distribution deviates significantly from the assumptions made in the theoretical analysis. This is a critical limitation that needs further discussion.

### Questions
1. Please refer to weaknesses. especially weaknesses 3.

2. In Proof 3. authors claim that: "The negative value $\sum\frac{\lambda_i^{2k+1}(v_i^Tx_i)^2}{c1c2}$ decreases and the positive value $\sum\frac{\lambda_i^{2k+1}(v_i^Tx_i)^2}{c1c2}$" increases as the exponent k increases". How is this result derived? value range of $\lambda$ is $[-1,1]$, so the results should be the negative value decreases and the positive value decreases instead.

3. When connecting the bases with homophilous, the authors say "the basis spectrum is supposed to be aligned with homophily ratios" and "set $\theta:=\frac{\pi}{2}(1-h)$". I have two questions: 1) why does the basis spectrum need to align with homophily ratios? what is the advantage? and 2) why can it be aligned by setting $\theta:=\frac{\pi}{2}(1-h)$?

4. Could the proposed method mitigate the over-smoothing problem? Please include some experiments if possible.

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a new method called UniFilter for Spectral Graph Neural Networks (SGNNs) that addresses the issue of fixed polynomial filters in graph filters, accommodating the diverse heterophily degrees across different graphs. The core part of UniFilter is a vector basis called UniBasis, where the angle between each of two distinct basis vectors is $\theta=\frac{\pi}{2}(1-h)$.

The main flow that leads the authors to design UniBasis is as follows: First, the authors establish a theorem that depicts the correlation between homophily ratio $h$ and the frequency of a desired filtered vector signal. Next, the authors finds that on regular graphs, a signal's frequency is related to the its relative position towards the all-one vector.  This finding then leads the authors to build UniBasis.

In experiments, UniFilter show leading performances on real-world datasets compared with other state-of-the-art models.

### Strengths
- S1. The authors establish a theorem that depicts the correlation between homophily ratio $h$ and the frequency of the possibly desired output signal.    
- S2. UniBasis is able to control the angle between each of the two basis vectors. Higher the homophily ratio,  smaller the angle.

### Weaknesses
 - W1. The flow (as sketched in summary) lacks soundness.

  On regular graphs, the authors find that a signal's frequency is related to the its relative position towards the all-one vector. How does this observation leads to contraining the angles between basis vectors? The authors roughly write: "... it explicitly prompts us to the potential correlation between the vector angles (relative position) and the basis spectrum."

- W2. $h$ is used as a prior knowledge to adjust the angles among basis vectors. However, the direct calculation of $h$ relies on labels on test sets. This issue is important since it is related to label leakage. 

- W3. The claim "signals with **negative** weights are suppressed or eliminated as harmful information" lacks critical thinking. This assertion is related to the overall structure of the neural network, i.e., is there an neural layer after filtering?

### Questions
Please check weaknesses.

### Soundness
1 poor

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Spectral Graph Neural Networks (GNNs) have become increasingly prevalent due to their strong performance in handling heterophily in graph data. However, optimal graph filters rely on a complex process and, to bypass this complexity, numerous polynomial filters have been proposed. These polynomial filters are designed to approximate the desired graph filters. A significant challenge arises because these polynomial methods mainly focus on specific types of graph structures. They struggle to accommodate graphs that display a diverse range of homophily and heterophily degrees.The paper aims to address this challenge by understanding the relationship between polynomial bases of designed graph filters and the diverse homophily and heterophily degrees in graphs. After the analysis, an adaptive heterophily basis is developed. The paper then integrates this with a homophily basis, leading to the creation of a universal polynomial filter known as "UniFilter". 

Fundamentally, it seems that the adaptive basis ensures that the subsequent elements of the basis do not become too similar with higher k. The choice of this dissimilarity has been done in a very specific way, by computing signal specific basis vectors which are called heterophily basis in the paper. Unifilter is the combination of the standard polynomial basis with this heterophily basis. This combination is shown to give consistently good performance across varying range of homophily/heterophily datasets.

### Strengths
1. Interesting idea. 
2. The results are very encouraging

### Weaknesses
 1. The motivation for the choice of $\theta = \frac{\pi}{2}(1-h)$ from theorem 3, is not very straightforward and clear. The paper states that this choice is empirical, but there is very little given in terms of motivation for this exact form.
2. For this method, the knowledge of the homophily ratio seems to be important. In many practical scenarios, this may not be possible to be estimated accurately and even approximations could be difficult. No ablation study is presented showing the sensitivity of this model to the accurate knowledge of the homophily ratio.
3. The HetFilter seems to degrade rapidly past h=0.3 whereas OrtFilter is lot more graceful to the varying homophily ratio. It is unclear whether one would consider the presented fluctuations as inferior to the presented UniBasis. For UniBasis, in the region of h >= 0.3, the choice of tau should become extremely important (as is evident from Figure 4, where lower tau values can reduce performance on Cora by about 20 percentage points).

### Questions
Q1] Can you present a motivation for the choice of $\theta = \frac{\pi}{2}(1-h)$?
Q2] Imagine that we did not have the precise estimates of h, but we had approximate estimates of h with some variance. How much does the performance of the proposed approach change under this setting?
Q3] Since HetFilter can be expressed in terms of OrtFilter, There must be a w_k weights that should also work with OrtFilter. Then where is the gap in OrtFilter and HetFilter performance coming from?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper introduces UniBasis, a universal polynomial basis designed to align with varying degrees of graph heterophily. UniBasis is used to create UniFilter, a general graph filter. The authors demonstrate that UniFilter outperforms 18 baseline methods on real-world and synthetic datasets, confirming UniBasis's effectiveness and generality for graph analysis, particularly on graphs with varying levels of heterophily.

### Strengths
1) Taking into account the diverse degrees of heterophily when designing polynomial bases is an interesting idea that holds the potential to enhance filter learning.
2) The proposed heterophily bases demonstrate both theoretical and practical soundness, proving effective in somewhat.

### Weaknesses
1) The design of heterophilic bases relies on the dataset's homophily rate, denoted as $h$ in Algorithm 1. I am concerned this approach is impractical due to obtaining the exact homophily rate $h$ from the training data is not feasible. It appears that the authors have directly utilized the entire dataset, including the labels of the test set. There are also methods to learn the homophily rate $h$ during the training process,  but I think this process might affect the model's performance.
2) There are not enough datasets for heterophilic graphs, and previous work has highlighted some issues with the Chameleon and Squirrel datasets [1]. Therefore, I recommend conducting experiments using more extensive heterophilic graph datasets, such as the latest benchmarks available [1] and [2].

Minor Comments:
1) The writing in this paper requires further refinement. For example, the notations used are somewhat confusing, such as using bold uppercase letters $\mathbf{G}$ for a graph and calligraphic fonts $\mathcal{L}$ for the Laplacian matrix.

2) No available code for reproducing the results has been provided.

### Questions
1) Please refer to the aforementioned weaknesses.
2) I don't have any more concerns. My main concern is for the use of $h$, which brings some unfairness, and I would like to see a further response from the author.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
