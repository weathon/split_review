# Boosting Ray Search Procedure of Hard-label Attacks with Transfer-based Priors

- Decision: Accept
- Scores: 8, 6, 8, 8

## Abstract
One of the most practical and challenging types of black-box adversarial attacks is the hard-label attack, where only top-1 predicted labels are available. One effective approach is to search for the optimal ray direction from the benign image that minimizes the $\ell_p$ norm distance to the adversarial region. The unique advantage of this approach is that it transforms the hard-label attack into a continuous optimization problem. The objective function value is the ray's radius and can be obtained through a binary search with high query cost. Existing methods use a "sign trick" in gradient estimation to reduce queries. In this paper, we theoretically analyze the quality of this gradient estimation, proposing a novel prior-guided approach to improve ray search efficiency, based on theoretical and experimental analysis. Specifically, we utilize the transfer-based priors from surrogate models, and our gradient estimators appropriately integrate them by approximating the projection of the true gradient onto the subspace spanned by these priors and some random directions, in a query-efficient way. We theoretically derive the expected cosine similarity between the obtained gradient estimators and the true gradient, and demonstrate the improvement brought by using priors. Extensive experiments on the ImageNet and CIFAR-10 datasets show that our approach significantly outperforms 11 state-of-the-art methods in query efficiency. Code will be released.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper addresses the problem of hard-label black-box adversarial attacks. The paper builds on an existing approach that seeks the optimal ray direction from a benign image to minimize the distance to the adversarial region. While this method has shown promise, its high query cost remains a major drawback. A variation of this method that uses ‘signed gradient’ suffers from gradient accuracy limitation. To address these issues, the authors propose incorporating a transfer-based prior to reduce the query burden and improve performance. Additionally, they provide theoretical analysis of the gradient estimation quality achieved through this transfer-based prior and provide insight into its effectiveness.

### Strengths
**Originality**: The concept of using transfer priors is not entirely new, as it was demonstrated in other works e.g., Dong et al. (2022). However, this paper's novelty lies in applying them to the more practical hard-label setting, where information is limited.

**Quality**: The methodology demonstrates technical soundness, particularly the idea of using transfer-based priors and then the approach to gradient approximation through closest projection on the subspace.  

**Clarity**: The writing could be further improved. Since the paper is based on previous work - Sign-OPT, it can be confusing for someone who is not well familiar with those works. The figures also make it hard to understand the key idea of the paper. In particular, the first figure is confusing as it has a lot of information which is unnecessary and does not motivate the problem or explain the idea well. 

**Significance**: The paper makes substantial contributions to adversarial machine learning by introducing a novel attack that leverages transfer-based priors in hard-label black-box setting. The paper demonstrates how this additional information from surrogate models can be effectively used.

### Weaknesses
1. The main contribution of the paper seems to have limited novelty. It essentially boils down to employing Eq (7), which is similar to the Sign-OPT method but with the addition of using gradients from surrogate classifiers.
2. It seems that the results don't clearly favor one approach over another. In some cases, Prior-Sign-OPT performs well, while in others, Prior-OPT outperforms it. Lines 319-321 mention that Prior-OPT outperforms Sign-OPT under certain conditions, but these conditions are not clearly explained, so the reasoning is unclear.
3. Another concern is the inconsistent performance in targeted attacks. For instance, in Figures 10(g) and 10(h), the proposed methods are not among the top three, throughout the plots. In other cases, other methods perform equally well (especially for smaller number of queries), yet no explanation is provided for these discrepancies.
4. The method underperforms when the number of queries is small. For example, in Table 1, for the ViT experiments, other methods achieve lower mean L2 norm distortions with fewer queries. Specifically, for targeted attacks up to 5k queries, other methods generate adversarial examples with smaller perturbations as compared to the proposed methods.

### Questions
1. **Lines 196-197**: The notation for qi (used for the transfer-based prior) and q (representing the total number of vectors) is confusing. It would help to revise the notation to make the distinction clearer and avoid confusion.

2. **Figure 1**: The figure is unclear and lacks proper labeling. Please add clear labels to define the regions and ensure the equations are more readable and understandable

3. **Figures 9 & 10, and Table 1**: These results highlight that using PGD (Projected Gradient Descent) significantly boosts performance. The question arises: How would the other methods perform if PGD were applied to them as well? Were there any experiments done to investigate that?

4. The results indicate that even adding a single transfer-based prior improves performance. However, it would be valuable to test an alternative where, instead of using random vectors, only prior vectors are used. Are there any experiments that investigate this scenario?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces two novel hard-label attack methods, Prior-Sign-OPT and Prior-OPT, which leverage transfer-based priors and random sampling vectors to enhance the query efficiency and success rate of black-box adversarial attacks. Theoretical analysis and experiments on ImageNet and CIFAR-10 datasets demonstrate that these methods significantly outperform 11 state-of-the-art techniques while reducing the number of queries needed.

### Strengths
1. This paper proposes a gradient estimation method to conduct hard-label attack and provides proof for it.

2. The paper is well-written.

### Weaknesses
1. The paper benefit from showing the time complexity.
2. This paper is a comprehensive study based on transfer and query, hence, I hope you could compare it with the results from the paper "Blackbox Attacks via Surrogate Ensemble Search. Neurips 2022."

### Questions
Please see the weakness

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a new method for hard-label attacks which uses transfer-based priors to estimate the gradient of the loss in hard-label attacks, which is quite query efficient.

### Strengths
1. This paper proposes a surrogate function to estimate compute the transfer-based priors, which can avoid the non-differentiable issue of using binary search to learn the prior.

2. The gradient of the loss in Eq. (3) can be estimated by the projection of the true gradient onto the subspace spanned by these transfer-based priors and some random directions.

### Weaknesses
An efficiency experiment is required to show how the proposed method improves the ray search efficiency.

### Questions
N/A

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
The paper addresses the challenge of hard-label adversarial attacks and enhances the efficiency of searching for the optimal ray direction by introducing a prior-guided approach that leverages transfer-based priors from surrogate models. Theoretical analysis is provided to validate the effectiveness of their gradient estimation technique, and extensive experiments on ImageNet and CIFAR-10 demonstrate significant improvements in query efficiency compared to 11 state-of-the-art methods.

### Strengths
1. The paper provides a solid theoretical foundation for the proposed gradient estimation technique.
2. Extensive experiments on multiple datasets demonstrate the practical effectiveness of the proposed method.
3. The focus on improving query efficiency is critical, as it addresses one of the major challenges in hard-label attacks, making the method more applicable in real-world scenarios.

### Weaknesses
1. The following work [1] also proposes to use a pre-trained model to reduce the query complexity of hard-label adversarial attacks. Please clarify the novelty based on this work.
2. The paper does not adequately address the scalability of the proposed method, particularly in scenarios involving larger models or more complex datasets.
3. The reliance on transfer-based priors from surrogate models raises concerns about overfitting and the applicability of the method to unseen models or datasets.

### Questions
See the weaknesses for details

### Soundness
3

### Presentation
3

### Contribution
3
