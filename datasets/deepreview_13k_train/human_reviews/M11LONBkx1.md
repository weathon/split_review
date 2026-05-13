# Diffusion with Synthetic Features: Feature Imputation for Graphs with Partially Observed Features

- Decision: Reject
- Scores: 6, 5, 6, 6

## Abstract
In this paper, we tackle learning tasks on graphs with missing features, improving the applicability of graph neural networks to real-world graph-structured data. Previous diffusion-based imputation methods overlook the presence of channels with low-variance features, and these channels contribute very little to the performance in graph learning tasks. To overcome this issue, we propose a new diffusion-based imputation scheme using synthetic features in addition to observed features. The proposed scheme first identifies channels with low-variance features via pre-diffusion and generates a synthetic feature for a randomly chosen node in each low-variance channel. Then, our diffusion process spreads the synthetic features widely while considering observed features simultaneously. Extensive experiments on graphs with various rates of missing features demonstrate the effectiveness of our scheme, achieving state-of-the-art performance in both semi-supervised node classification and link prediction.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper tackles the missing feature problem in graphs through the lens of low-variance channels. To address this, FISF first pre-diffuses the known features to unknown features and generates a synthetic feature on a specific low-variance channel. Finally, it diffuses the synthetic feature widely, treating it as a known feature throughout the graph. Performance across various missing rates demonstrates the efficacy of FISF.

### Strengths
1. The problem of the low-variance channel is interesting and provides a new perspective on the missing feature issue in the graph community.
  
2. The use of generating synthetic features seems to be a straightforward remedy for the low-variance channel.
  
3. The paper is well-written and easy to follow.

### Weaknesses
1. Although the authors demonstrated the existence of a low-variance channel after current diffusion-based methods, FP and PCFI, the link explaining how these low-variance channels act as a bottleneck for overall performance is not comprehensively provided. For example, the performance of node classification could be provided after excluding some portions of low-variance channels. Additionally, I am curious whether the original variance of the dataset, without any missing features, shows low variance as depicted in Figure 1. In this context, the authors should explain why a low-variance channel is especially burdensome in scenarios with missing features.
  
2. I wonder if the low-variance problem is due to zero-initialization. In cases of severe missing data and zero-initialization is equipped, the majority of the feature matrix would consist of zeros, so the output matrix would naturally contain many zeros (i.e., biases, if adding biases is enabled), especially considering that most graph datasets use one-hot encoding via bag-of-words for feature matrices. If the initialization for the missing feature were from random sampling, such as a uniform or normal distribution, the low variance problem might be easily addressed.
  
3. Although diffusion via synthetic features can enhance the distinctiveness across features, it might undermine the GNN's key inductive bias, which is the smoothness across connected nodes. A more in-depth discussion of the trade-off between feature distinctiveness and the smoothness of connected features should be provided.
  
4. While the authors proposed the use of synthetic features, excluding this module, the pre-diffusion and diffusion with synthetic features are exactly aligned with the existing work, PCFI. This raises concerns about the overall novelty of this paper.
  
5. The complexity of FISF compared to existing works is not comprehensively addressed. Given that the adjacency matrix is created for each feature dimension, the complexity would be exceedingly high, potentially limiting the practical application of FISF.
  
6. The proposed missing rates of 0.995 and 0.999 seem unrealistic. Furthermore, edge information can also be missing in real-world scenarios, a factor that should be considered.

### Questions
See the Weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a method for missing value imputation on top of pseudo-confidence-based feature imputation (PCFI) by manipulating the features with low variance, whose were left behind by PCFI. The idea is to insert another random feature for each low variance.

### Strengths
I think the original idea is fair that the paper try to amplify low variance features.

### Weaknesses
The direction of amplifying low variance features can be a good idea and if it is done right, there might be an optimal point that maximize performance on top of its baseline.
However, the paper shows the algorithm, how to manipulate the synthetically generated random features without a clue why it has to be done that way, for what purpose. Overall, the paper really proposes a "new method" without actually showing what is the problem it is solving and how the method help achieving the goal. The core issue is that while the method introduces synthetic random features to increase variance in low-variance channels, it lacks a clear justification for why this specific manipulation leads to improved performance in downstream tasks. The paper does not explain why simply adding variance, without considering the underlying data distribution or task-specific relevance, should be beneficial. It's not clear how the random features interact with the existing features or how they contribute to the learning process of the downstream task. The method seems to be based on an assumption that more variance is always better, which is not necessarily true. The paper also does not provide any theoretical or empirical evidence to support the claim that this specific method of variance injection is optimal or even effective in general. The lack of a clear rationale makes the proposed method seem arbitrary and difficult to justify.

### Questions
What is the idea of a synthetic random feature and how it help improving performance?

### Soundness
1 poor

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper claims that existing methods output low variance channels within imputed features and then presents a method called FISF, which performs diffusion with randomly injected synthetic features on low variance channels discovered from pre-diffusion process.

### Strengths
- This paper empirically shows that existing diffusion-based methods causes many low variance channels within imputed features, while proposed method FISF can solve those problem (Figure 1).
- The paper is well-written and easy to follow.

### Weaknesses
 - This paper does not clearly justify why alleviating the low variance channel problem of the existing diffusion methods is significant for graph learning tasks, even though it is a key motivation of this paper. Without additional evidences, it is hard to agree with this paper’s argument that low variance channels contribute very little to performance.
- This paper lacks justification of using naïve random synthetic features. Authors claim that more distinctive representations are crucial for classification tasks, but I have concern that randomly injected synthetic features can lead to lower intra-class node representation similarity thus can be harmful on downstream tasks. In my opinion, discussion on aforementioned concern is required.
- It is required to include the time complexity of presented method. Since V_{k}^{(a)} differs by channel ‘a’ as synthetic feature-injected node differs by channels, diffusion process should be done by channels. Moreover, as presented method further requires pre-diffusion process, presented FISF seems to have much higher time complexity compared to existing methods, especially FP.
- As presented in the Table 5 in the Appendix, hyperparameters have been tuned with respect to each feature missing rate r_m. Regarding complexity of setting optimal hyperparameters, there is some concern about practical usage of FISF. 
- Lastly, considering the similarity of Label Propagation (LP) and FP, and the argument about low variance channels (in respect of very high missing feature rates), I think this paper shares similar motivation with Poisson Learning [1], which mitigates very low label rate problem in LP. Poisson Learning points out that LP outputs almost constant pseudo-labels for most of unlabeled samples, while this paper points out existing diffusion-based methods including FP causes “low variance channels”, i.e. almost constant features (or an exact constant when there is only one observed feature value, as presented in this paper). Regarding aforementioned similarity, further discussion with Poisson Learning might be beneficial.

### Questions
-	Can you provide the feature variance distribution (Figure 1) in more realistic missing feature settings (I.e. r_m <= 0.9)? In my opinion, authors have to show that existing diffusion-based methods still suffer from the problem of making low variance channels in various missing feature settings, especially in more realistic scenarios.
-	Can you provide further theoretical or empirical evidences that can explain why random synthetic feature works well? (to resolve concern in W2)
-	What happens if pre-diffusion method is replaced to FP from PCFI? (Why this paper have chosen PCFI as a pre-diffusion method?)

[1] Jeff Calder, Brendan Cook, Matthew Thorpe and Dejan Slepcev. Poisson Learning: Graph Based Semi-Supervised Learning At Very Low Label Rates. In International Conference on Machine Learning, pp. 1306-1316. PMLR, 2020.

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
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper addresses the task of learning on graphs with missing features, specifically focusing on improving the application of graph neural networks (GNNs) to real-world graph-structured data. The paper introduces a novel diffusion-based imputation scheme called Feature Imputation with Synthetic Features (FISF).

(1) It generates synthetic features via pre-diffusion for randomly chosen nodes in these channels.

(2) The diffusion process spreads these synthetic features while also considering observed features simultaneously.

(3) The proposed scheme has been empirically tested, showing promising results, especially in scenarios with a high rate of missing 
features. It shows robust performance in both semi-supervised node classification and link prediction tasks.

### Strengths
1. The paper addresses a significant and practical problem in the domain of graph learning.

2. The proposed FISF method is novel, focusing on low-variance channels that were overlooked by previous approaches.

3. The paper seems to provide extensive experiments on graphs with varying rates of missing features, demonstrating the robustness of the proposed method.

### Weaknesses
1. From the provided content, it's unclear how the proposed method scales with large real-world graphs or its computational efficiency.

2. The abstract and introduction don't mention how generalizable the method is across diverse types of graph-structured data or different

### Questions
See weakness

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
