# Prototype-based Optimal Transport for Out-of-Distribution Detection

- Decision: Reject
- Avg Score: 4.60
- Scores: 3, 8, 6, 3, 3

## Abstract
Detecting Out-of-Distribution (OOD) inputs is crucial for improving the reliability of deep neural networks in the real-world deployment. In this paper, inspired by the inherent distribution shift between ID and OOD data, we propose a novel method that leverages optimal transport to measure the distribution discrepancy between test inputs and ID prototypes. The resulting transport costs are used to quantify the individual contribution of each test input to the overall discrepancy, serving as a desirable measure for OOD detection. To address the issue that solely relying on the transport costs to ID prototypes is inadequate for identifying OOD inputs closer to ID data, we generate virtual outliers to approximate the OOD region via linear extrapolation. By combining the transport costs to ID prototypes with the costs to virtual outliers, the detection of OOD data near ID data is emphasized, thereby enhancing the distinction between ID and OOD inputs. Experiments demonstrate the superiority of our method over state-of-the-art methods.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
Summary:This paper proposes a new prototype-based optimal transfer (POT) method to detect out-of-distribution (OOD) data by measuring the optimal total transfer cost between the test sample and the ID prototype and the virtual outlier. In addition, this paper also proposes to obtain the virtual outlier of OOD by simple linear extrapolation, and demonstrates its effectiveness by comparing with the existing technology. The paper has a clear structure and rigorous logic, covering relevant background, methods, experimental evaluation and results analysis.

### Strengths
- This paper provides a new perspective on the OOD detection problem by combining the concepts of prototype and optimal transmission.
- The author conducted exhaustive experiments on multiple standard datasets, comparing the performance of POT with 21 existing technologies. The experiments are adequately designed and the results are clearly interpreted.

### Weaknesses
 - Formulas 2 and 3 in the paper mention that the calculation of the transmission plan and cost matrix comes from the ID prototype and test samples. The simple linear extrapolation to obtain the OOD area is also based on the test samples. This solution is not realistic under the task setting of OOD detection.
- The paper mentions that the OOD area is obtained by simple linear extrapolation, but based on the author's description and existing research, the difficulty of OOD samples lies in the approximate ID features in the feature space. The OOD area obtained by simple linear extrapolation may not be representative, and there is a lack of discussion on the interpretability of the process.
- The results of the paper method should also be compared with the results of some of the latest papers.

### Questions
- Are you skeptical about the effectiveness of obtaining OOD data areas through simple linear extrapolation?
- Is it realistic for OOD detection to use test data for linear extrapolation?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper focuses on detecting Out-of-Distribution (OOD) inputs, which is a crucial task for improving the reliability of deep neural networks. Since there exists an inherent distribution shift between ID and OOD data, the authors propose a novel method Prototype-based Optimal Transport (POT) which utilizes the prototype-based optimal transport to assess the discrepancy between test inputs and ID prototypes and use the obtaining transport costs for OOD detection. Since relying solely on the cost of ID prototypes is insufficient for discerning OOD data with smaller distribution shifts from ID data, they propose to generate virtual outliers to approximate the OOD region using representation linear representation extrapolation. Finally, experiments on several benchmark datasets are provided.

### Strengths
1. This paper addresses the OOD detection problem by measuring distribution discrepancy and proposes a novel approach using prototype-based optimal transport.
2. To identify OOD data with smaller distribution shifts from ID data, this paper proposes to generate virtual outliers to approximate the OOD region using representation linear representation extrapolation.
3. Comprehensive experimental results on various benchmark datasets demonstrate the effectiveness of the proposed detection method.

### Weaknesses
1. The experimental results and ablation studies require more explanation and discussion, rather than just describing the phenomena. For instance, the paper does not delve into why certain parameter choices lead to better performance, or why the proposed method performs better on some datasets compared to others. A more in-depth analysis of the score distributions, particularly in relation to the virtual outliers, is needed to understand the underlying mechanisms.
2. Although this paper reduces computational complexity by introducing the entropy regularization term and the Sinkhorn-Knopp algorithm, the optimal transport problem is still computationally intensive on large-scale datasets. The paper lacks a detailed analysis of the computational cost associated with the OT calculations, particularly in comparison to other OOD detection methods. This makes it difficult to assess the practical applicability of the proposed method in resource-constrained environments. The paper should provide a breakdown of the time spent on different components of the algorithm, such as feature extraction and OT computation.
3. Is the constraint w<0 in Eq. (8) necessary? Because there is no corresponding description in this paper, and this case was not considered in the parameter analysis. The paper should clarify the purpose of this constraint, and provide a justification for why it is needed. Furthermore, the parameter analysis should include a discussion of the impact of different values of w, including both positive and negative values, to provide a comprehensive understanding of its role in the proposed method.

### Questions
1.	Can the authors provide more discussions on the experimental results and ablation studies?
2.	Can the authors show the execute time of the proposed method compared with other methods?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The work considered the problem of OOD (Out-Of-Distribution) detection, and proposed a method based on optimal transport from test inputs to ID (in-distribution) prototypes. It first constructed the prototype of each class as the average representation for that class extracted from the feature encoder, then computed the optimal transport between the encoded feature of the test inputs and the class prototypes and used the sum of the transport costs from a test input to prototypes as an indication of the input's outlier-ness. It then noted that only using this is insufficient for detecting OOD data closer to ID, and proposed to generate virtual outliers by linear extrapolation between the prototypes and the mean of the test inputs, and finally used the difference between the transport cost to the ID prototypes and the cost to the virtual outliers as the final OOD score.

The work then performed extensive experiments. The results showed that the proposed method often outperforms the competitors and gets close-to-best performance otherwise. It can be used with different pretraining schemes without graceful performance degradation, and can use the network weights as the ID prototypes when training data are not available. Ablation study shows that the virtual outliers are important for the performance, and that the method is robust to hyperparameters: the extrapolation coefficient, the regularization coefficient, and the test batch size.

### Strengths
- The work addressed an important topic of OOD detection, and designed a pratical method.
- The proposed method used two key techniques: optimal transport and virtual outliers via linear extrapolation. The work illustrate the insights behind these techniques quite clearly.
- The experiments are quite extensive and the results are quite convincing, showing the strong performance and investigating important aspects of the method like robustness to hyperparameters.

### Weaknesses
 - The performance will depend on the feature encoder used. Is the method robust to the choice of the feature encoder? How large is the impact of the encoder?
- What if we use more than one class prototypes for each class? 
- What are the \mathcal{P} and \mathcal{M} in Line 241? Better to formally specify them.
- Eqn (9): the second "+" should be ":"?
- Table 1, Textures FPR95, NAC-UE result: should be underlined rather than boldfaced.
- Maybe also underline the second best results in Table 2, so as to show the performance margin and be consistent with Table 1.
- Figure 3 shows the ablation result on virtual outliers on Far-OOD datasets. What about ablation study on Near-OOD datasets?

### Questions
- The performance will depend on the feature encoder used. Is the method robust to the choice of the feature encoder? How large is the impact of the encoder? 
- What if we use more than one class prototypes for each class? 
- What are the \mathcal{P} and \mathcal{M} in Line 241? Better to formally specify them.
- Eqn (9): the second "+" should be ":"?
- Table 1, Textures FPR95, NAC-UE result: should be underlined rather than boldfaced.
- Maybe also underline the second best results in Table 2, so as to show the performance margin and be consistent with Table 1.
- Figure 3 shows the ablation result on virtual outliers on Far-OOD datasets. What about ablation study on Near-OOD datasets?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper addresses the inherent distributional differences between ID and OOD samples by proposing the use of optimal transport (OT) to measure the discrepancy between test inputs and ID prototypes, a method termed Prototype-based Optimal Transport (POT). The authors assess distances by calculating the transport cost from each test input to the ID prototypes. Additionally, they apply linear extrapolation to generate virtual outliers, effectively regularizing the decision boundary. By evaluating distributional differences between ID and OOD samples through optimal transport, this work introduces a novel perspective. Furthermore, the use of linear extrapolation enables optimal transport to function effectively within this framework.

### Strengths
1.	Explore a new OOD score by measuring the discrepancy between test images and ID prototypes from the perspective of optimal transport, which is well-supported theoretically.
2.	Use linear extrapolation to regularize the decision boundary, offering a successful perspective on applying optimal transport in OOD detection.

### Weaknesses
1.	In the use of OT, calculating ν for test samples in Equation (3) requires all test samples, which is impractical in real-world applications. Specifically, the computation of the marginal distribution ν, which involves summing over all test samples, necessitates access to the entire test set. This is a significant limitation as it prevents the method from being applied in online or streaming scenarios where test data arrives sequentially. The need to recompute ν with each new batch of test samples also introduces computational overhead and makes the method less scalable.
2.	When generating outliers via linear extrapolation, the method appears to rely on information from the test set, which is also impractical. The use of the empirical mean of the test set to generate virtual outliers introduces a dependency on the test data distribution. This is problematic because the method should ideally detect OOD samples without needing to know the characteristics of the test set in advance. The reliance on test set statistics for outlier generation compromises the method's ability to generalize to unseen OOD data.

### Questions
Why do you claim that your method measures differences directly in the latent space? It is clear that you are also using features obtained from the feature extractor. When comparing with DDE, you state that DDE measures differences in the representation space, which is influenced by the transformations of the DNN features, while POT measures differences in the latent space.

I will adjust the score based on your response.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces an approach to out-of-distribution (OOD) detection leveraging optimal transport (OT). The core idea is based on the observation that OOD inputs typically incur higher transport costs when mapped to the in-distribution (ID) in latent space. From this, they develop an OOD detection method by first compute the optimal transport plan from the test distribution to the ID distribution. OOD detection is then achieved by calculating the transport cost for each input and applying a threshold to determine whether the input is OOD. The author then benchmark their method with varied number of datasets.

### Strengths
- The comparison with other baseline methods appears comprehensive and thorough.

### Weaknesses
One of my concern is that  the paper lacks a deeper understanding for why OT would be better than other OOD detection methods. Standard approaches have increasingly focused on understanding geometric representations in neural networks, either through uncertainty estimation [1] or, more rigorously, likelihood estimation [2], sometimes aided by reconstruction autoencoders [3]. Given the connection between geometric representation and OT through the transport map, I would expect interpretative insights along this line rather than a direct application of OT for OOD detection. Without this, the current proposal, in my opinion, is incremental compared to the existing distance-based approaches.

The method presentation is not clear. I have some confusion in terms of how the OT plan is constructed using both in-distribution (ID) inputs and out-of-distribution (OOD) datasets. See question (1).

Finally, similar ideas of using optimal transport to characterize OOD error have been explored with more concrete theoretically properties, as in [4].

### Questions
(1) Can the author specify how the validation set is built in the OT formulation, especially the test batch size in Section 4.3? Specifically, my impression is that we only have 1 unique transport map from the validation set and we will use that for detecting OOD samples. As such, I'm not sure how varying the test batch size affect the result. Are we computing a distinct transport map for every test batch size? if so how do we decide the threshold for OOD samples for these test batch size? What if their statistic (portion between ID and OOD data) changes?

(2) How to apply this idea when the OOD set is small? How the validation set size affect the performance? 

(3) What is the fundamental idea that OT is better than other methods such as likelihood estimation?

### Soundness
1

### Presentation
2

### Contribution
2
