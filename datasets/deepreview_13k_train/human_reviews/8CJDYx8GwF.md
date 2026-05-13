# Gradient Flow Provably Learns Robust Classifiers for Data from Orthonormal Clusters

- Decision: Reject
- Scores: 5, 6, 6, 8

## Abstract
Deep learning-based classifiers are known to be vulnerable to adversarial attacks. Existing methods for defending against such attacks require adding a defense mechanism or modifying the learning procedure (e.g., by adding adversarial examples). This paper shows that for certain data distribution one can learn a provably robust classifier using standard learning methods and without adding a defense mechanism. More specifically, this paper addresses the problem of finding a robust classifier for a binary classification problem in which the data comes from a mixture of Gaussian clusters with orthonormal cluster centers. First, we characterize the largest $\ell_2$-attack any classifier can defend against while maintaining high accuracy, and show the existence of optimal robust classifiers achieving this maximum $\ell_2$-robustness. Next, we show that given data sampled from the orthonormal cluster model, gradient flow on a two-layer network with a polynomial ReLU activation and without adversarial examples provably finds an optimal robust classifier.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper studies the binary classification problem in which the data comes from a mixture of Gaussian clusters with orthonormal cluster centers. The paper first shows that an attack with unlimited budget is not defendable and establishes a maximum budget for a plausible attack. Then, it shows that some classifier can achieve this robustness while maintaining accuracy. Finaly, the paper shows that a neural network with a single hidden layer and polynomial ReLU activation can be trained using gradient descent to approximate this optimal classifier when the initialization of the network parameters is favorable.

### Strengths
- Originality:

The paper is original in its focus on GMM distributed data.

- Quality:

The paper is rigorous in its presentation.

- Clarity:

The paper is clear for the most part.

- Significance:

The issue of finding plausible classification problems that are amenable to analysis is important considering the current stage in understanding adversarial examples phenomenon.

---------Edited-----------

I increase my original score of 3 to 5 since the overall quality of the paper is very good.

### Weaknesses
I believe that the paper is not ready for publication based on four key observations.

First, the assumptions of the analysis are very restrictive, the orthonormality condition on the cluster centers for example exclude even the simplest classification problems such as XOR. The assumption that data is generated from a mixture of Gaussians with orthonormal centers severely limits the applicability of the results. This constraint implies that the data effectively lies on a simplex, which is a highly specific and unrealistic scenario for most real-world datasets. Such a rigid structure prevents the analysis from generalizing to more complex and practical classification problems, where data distributions are rarely so neatly structured.

Second, the paper makes no attempt to show that the analysis bears any relevance in real-world scenarios. The theoretical results, while mathematically sound within the confines of the imposed assumptions, lack empirical validation on datasets that exhibit more realistic characteristics. Without such validation, it remains unclear whether the insights gained from this analysis can be translated into practical improvements in the training of robust classifiers.

Third, the analysis does not connect or explain any issue that the analysis is revealing with regards to the current paradigm of training robust ANNs. While the main theorem asserts that the degree of polynomial ReLUs should be at least 3, it does not explain what makes the first degree ReLUs unsuitable. Furthermore, while the paper claims training robust classifiers are possible with simple gradient decent, it does not explain why is it that we observe a trade-off between accuracy and robustness in practice. The analysis fails to address the practical challenges of training robust networks, such as the observed trade-off between accuracy and robustness, and the limitations of ReLU activation functions. The paper should delve deeper into the reasons behind these phenomena, providing a more comprehensive understanding of the issues at hand.

Last but not least, some of the claims of the paper are obvious and has no significance. For example, we don't need a mathematical analysis to figure out the reason behind the fact that attacks with unlimited budget are not defendable. Moreover, we don't need a reason to believe that robust classifier exists since every optimal Bayes classifier is accurate and robust by definition.

### Questions
See the Weaknesses section.

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper addresses the vulnerability of deep learning-based classifiers to adversarial attacks, which typically require defense mechanisms or modified learning procedures, such as adding adversarial examples. The authors demonstrate that for certain data distributions, it is possible to train a provably robust classifier using standard learning methods without any additional defenses. Focusing on a binary classification problem where the data is generated from a mixture of Gaussian clusters with orthonormal centers, the paper first characterizes the largest $\ell_2$-attack that a classifier can defend against while maintaining high accuracy. It then proves the existence of optimal robust classifiers achieving this maximum $\ell_2$-robustness. Furthermore, the authors show that for data sampled from the orthonormal cluster model, gradient flow on a two-layer network with a polynomial ReLU activation, even without adversarial examples, can provably yield an optimal robust classifier.

### Strengths
1. This paper provides solid theoretical analysis, proving that under the multi-cluster data assumption, a two-layer pReLU neural network with certain initialization conditions can converge to a robust solution.

2. The paper mainly utilizes the techniques from [1] and offers a two-phase training dynamics analysis based on early stopping.

3. Overall, the paper is written quite smoothly.

**Reference**

[1] Boursier, E., Pillaud-Vivien, L., & Flammarion, N. (2022). Gradient flow dynamics of shallow relu networks for square loss and orthogonal inputs. Advances in Neural Information Processing Systems, 35, 20105-20118.

### Weaknesses
1. The Non-degenerate initialization shape assumption used in the paper seems overly strong, as it requires that each Voronoi region contains at least one initialized weight, which may not be natural. Specifically, when considering a random initialization setup, if the dimension $ D $ is much larger than the number of clusters $ K $, the randomly initialized weights should be approximately orthogonal to the $ K $-dimensional subspace formed by the cluster features with high probability. This appears to suggest that the non-degeneracy gap might be very small, potentially requiring an impractically large number of neurons to satisfy the assumption. Furthermore, the paper does not provide a clear analysis on how the non-degeneracy gap scales with the dimension $D$ and the number of clusters $K$, making it difficult to assess the practical applicability of this assumption.

2. The paper considers a setup with sufficiently small data variance $ \alpha $. However, the empirical phenomena observed in [2] seem to be independent of the variance. Thus, the paper only partially addresses the conjecture in [2] by resolving a special case for finite orthogonal data. The limitation to small variance $ \alpha $ significantly restricts the scope of the theoretical results, as it is unclear how the derived robustness guarantees would hold for larger, more realistic data variances. The analysis does not explore the transition from small to large variance regimes, which could reveal important insights into the robustness properties of the model.

3. The paper lacks effective experimental validation of its theoretical analysis and conclusions, such as numerical simulations on synthetic data and observations on real image classification datasets. While the theoretical analysis is rigorous, the absence of empirical results makes it difficult to assess the practical relevance of the findings. Specifically, it is unclear whether the theoretical robustness guarantees translate into tangible improvements in real-world scenarios. The paper would benefit from experiments that demonstrate the behavior of the proposed method on both synthetic and real-world datasets, and compare its performance against existing adversarial training techniques.

### Questions
1. Could the authors provide an analysis and verification of whether their proposed non-degeneracy gap assumption holds for general small random initialization?

2. The main text does not seem to clearly explain why the small quantities in the conclusions are related to the variance $ \alpha $. Could the authors offer a more intuitive explanation?

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
4

### Summary
This paper study the problem 'what is the maximum adversarial perturbation a neural network can tolerate?' within the theory. The article contains three main theorems. Theorem 1 shows that for the Orthonormal cluster data, any Lebesgue measurable function can not keep robustness under budget $L_2$ norm 1 on such distribution with a probability. Theorem 2 gives the analysis of the robustness for Bayes optimal classifier. Theorem 3 shows that with some assumptions, a pRelu two-layer network can converges to optimal robust classifier after training.

### Strengths
1, In my opinion, the conclusion is new and reasonable. 
2, Motivation is reasonable.
3, The article has a good writing.

### Weaknesses
1, The proof is a bit long, I didn't take a closer look. I hope the author can write the proof of the theorem more concisely.

2, This paper mainly focus on the orthonormal clusters data, and to make sure that $<\mu_i,\mu_j>=I(i=j)$, there are at most D(dim of $x$) clusters in the data distribution, this type of data appears to be a combination of several normal distributions that are relatively far apart. So may I ask why considering this type of data? What are the practical applications of this kind of data in reality?

3, Theorem 1 said that: 'Given a sample $(x,y)∼D_{X,Y}$', we have equation (3), but I think the probability in (3) should be about $(x,y)\sim D_{X,Y}$? So it should not be written 'Given a sample $(x,y)∼D_{X,Y}$' here. The same for Theorem 2.

4, For the network structure, author do not choose Relu network due to  'Relu is non-differentiable' as said in note 1. But in my opinion,  this is not important. Relu is almost differentiable everywhere, which seems sufficient, and so many work have done on Relu network. Moreover, Relu is frequently used in real world. So, what would happen we take p=1? Is the author's main conclusion (converges to optimal robust classifier) still correct?

5, Why there is an upper bound of the amount of data in theorem 3? It should be more data lead to the better the training, why does the author need an upper bound for the data here?

6,  In Theorem 3, I think $\theta(t)$ represent the parameters obtained after t steps training, is it right?  And what is the learning rate?

7, Accoding  to the real world experience, normal training makes the network non-robust. In the paper, as said in equation (7) and definition (6) of dataset, author also does not consider the robustness training, but according to theorem 3, training lead to optimal robust classifier. Is there a contradiction in between?

### Questions
1, This paper mainly focus on the orthonormal clusters data, and to make sure that $<\mu_i,\mu_j>=I(i=j)$, there are at most D(dim of $x$) clusters in the data distribution, this type of data appears to be a combination of several normal distributions that are relatively far apart. So may I ask why considering this type of data? What are the practical applications of this kind of data in reality?

2, Theorem 1 said that: 'Given a sample $(x,y)∼D_{X,Y}$, we have equation (3)', but I think the probability in (3) should be about $(x,y)\sim D_{X,Y}$? So it should not be written 'Given a sample $(x,y)∼D_{X,Y}$' here. The same for Theorem 2.

3, For the network structure, author do not choose Relu network due to  'Relu is non-differentiable' as said in note 1. But in my opinion,  this is not important. Relu is almost differentiable everywhere, which seems sufficient, and so many work have done on Relu network. Moreover, Relu is frequently used in real world. So, what would happen we take p=1? Is the author's main conclusion (converges to optimal robust classifier) still correct? 

4, Why there is an upper bound of the amount of data in theorem 3? It should be more data lead to the better the training, why does the author need an upper bound for the data here?

5,  In Theorem 3, I think $\theta(t)$ represent the parameters obtained after t steps training, is it right?  And what is the learning rate?

6, Accoding  to the real world experience, normal training makes the network non-robust. In the paper, as said in equation (7) and definition (6) of dataset, author also does not consider the robustness training, but according to theorem 3, training lead to optimal robust classifier. Is there a contradiction in between?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper analyses the robustness of networks in a very fine-grained way. Specifically, it assumes the data distribution obeys mixture K-Gaussian clusters, and the cluster centers is orthonormal. In this way, the paper proves that the optimal robust classifier under this distribution is approaching to $\sqrt{2}/2$ if the dimension is sufficient large or the intra-class variance is small. Furthermore, beyond the existence, this paper uses gradient flows to prove that with some assumptions on initial points, pReLU networks can converge to a nearly optimal robust classifier if the intra-cluster variance is small.

### Strengths
This paper is well-written and easy-to-follow. I appreciate author’s effort to make a strongly technical paper easy for folks to read, that will be beneficial for the community. For examples, authors introduce many intuitions for the assumptions or the results of the theorem, and bring detailed proof sketch for readers to grasp.

This paper develops a full convergence analysis for gradient flow, demonstrating the conjecture on (Min & Vidal 2024), bring the significant contribution.

The technical contribution is solid. Although I do not check each stuff of the whole proofs, I believe they are correct after reading the proof sketch and some important part of the proof in the appendix.

The authors have discussed their limitations concretely, that will help readers understand their work comprehensively.

### Weaknesses
The assumption of the data distribution seems too strong. The awesome results may be unable to instruct learning for real-world scenarios. Specifically, the assumption of orthonormal cluster centers and a variance of $1/D$ within each cluster is highly restrictive and unlikely to hold in practice. This limits the applicability of the theoretical findings. For example, real-world data often exhibits complex, non-Gaussian cluster structures with varying degrees of overlap and non-uniform variances. The assumption of equal variance across all clusters is also a simplification that does not reflect real-world data distributions. Furthermore, the assumption of orthonormal cluster centers is a strong constraint that is unlikely to be satisfied in practical scenarios. 

Typo: In Line 061 it should be “orthonormal”.

### Questions
Is your assumption reasonable for real-world datasets? For instance, the $1/D$ variance assumption?

(Min & Vidal 2024) has proved the (almost) $\sqrt{2}/2$ robustness for $F^{(p)}$ classifier, and your Theorem 2 proves the similar result for Bayes optimal classifier. Is this a progress? I think the Bayes optimal classifier probably should be more robust than $F^{(p)}$. Maybe “optimal” does not means “robust optimal” in some cases. Can you provide more discussions on that?

### Soundness
4

### Presentation
4

### Contribution
3
