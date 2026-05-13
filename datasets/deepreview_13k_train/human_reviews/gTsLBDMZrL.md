# A Prototype-oriented Fast Refinement Model for Few-shot Industrial Anomaly Detection

- Decision: Reject
- Scores: 5, 6, 6, 5

## Abstract
Industrial Anomaly Detection (IAD) in low data regime is crucial for automating industrial inspections in practice. Previous methods have primarily focused on obtaining robust prototypes using only a few normal images per product. However, these methods seldom account for transferring the characteristics of online query images to enhance the representativeness of the original prototypes in a systematic way. To address the pivot issue, we propose a fast prototype-oriented refinement model for few-shot IAD. Given online query images, we formulate prototype refinement as a nested optimization problem between transport probability for anomaly suppression and transform matrix for characteristic transfer. Then we present an Expectation Maximization (EM)-based algorithm to iteratively compute the transport probability and transform matrix. In the E-step, we use entropy-based optimal transport, known as the Sinkhorn algorithm, to learn the transport probability. In the M-step, the transform matrix is updated via gradient descent. Finally, we integrate our model with two popular and recently proposed few-shot IAD methods, PatchCore and WinCLIP. Comprehensive experiments on three widely used datasets including MVTec, ViSA, and MPDD verify the effectiveness and efficiency of our proposed model in few-shot IAD applications.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a prototype-oriented fast refinement model for few-shot industrial anomaly detection. It focuses on enhancing anomaly detection under few-shot condition by improving prototype representativeness with query image features. It formulates prototype refinement as a nested optimization problem, balancing anomaly suppression and characteristic transfer. The problem is solved iteratively with an EM-based algorithm. The model integrates with few-shot anomaly detection methods like PatchCore and WinCLIP, showing significant improvements in anomaly detection performance on datasets such as MVTec, ViSA, and MPDD

### Strengths
- Few-shot anomaly detection could have high impact in industrial anomay detection tasks. The proposed method improved the efficacy of few-shot industrial anomaly detection by combining with state-of-the-art methods.

- Extensive evaluations are carried out on three industrial anomaly detection datasets.

### Weaknesses
 - The optimization task in Eq. (3) is not well explained. The first term minimizes the distance between transformed prototypes, $WM_s$ and query features. While the optimal transport also measures the distance between prototypes and the query sample, subject to an optimal assignment. The two terms seem to overlap. A more thorough discussion on the difference and why the optimal transport regularization is necesssary is required.

- The prototype transformation acts more like a prototype selector. As shown in Eq (7), $W$ is first optimized to minimize the difference between query feature and selected prototypes. Moreover, the prototypes do not benefit from observing more testing/query samples. Therefore, the proposed step does not refine the prototype, but rather selects the most appropriate prototypes for the given query feature/sample.

- In the EM algorithm, I am wondering why gradient descent is adopted for update $W$. Since OT is independent of $W$, the optimization w.r.t. $W$ in Eq (7) is a simple linear regression problem. A closed-form solution exists and can be implemented in a more efficient way.

- Analysis to reveal why the prototype refinement, or prototype selector which might be more appropriate, works is missing. For example, the distribution of $W^*$ is not explcitly studied. If $W$ tends to be more one-hot, it validates the hypothesis that $W$ acts like a prototype selector.

- The proposed method requires solving the optimization problem in Eq (7) for every single query sample which introduces additional overhead.

### Questions
- More analysis and explanations on the optimal transport regularization is required.

- A thorough analysis into the prototype refinement is necessary. For example, the distribution of $W^*$ may reveal the true effectiveness of the ``prototype refinement'' module.

- Evaluate closed-form solution to $W$ in Eq (7).

### Soundness
3

### Presentation
2

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
To address the issue of prototypes not adequately representing the features of few-shot anomaly detection, the authors propose a prototype-oriented fast refinement model. They transform the problem of prototype refinement into a nested optimization problem and introduce an Expectation Maximization (EM)-based algorithm to iteratively compute the transport probability and transform matrix. The Sinkhorn algorithm is used to learn the transport probability. The effectiveness of the proposed method is demonstrated on PatchCore and WinCLIP, as well as on three anomaly detection datasets: MVTec, ViSA, and MPDD, under different shot settings.

### Strengths
1. The authors propose transforming the problem of prototype refinement into a nested optimization problem and solving it through optimal transport, which is a novel approach.

2. The authors achieve significant performance improvements on PatchCore and WinCLIP across different shot settings on the MVTec, ViSA, and MPDD anomaly detection datasets.

3. The authors demonstrate the efficiency of the method.

### Weaknesses
1. In Figure 3, it is recommended to simultaneously display the qualitative experimental results of PatchCore+ to enhance reliability.

2. It is suggested that the authors provide code or reliable PyTorch pseudocode.

3. Besides being extendable to PatchCore and WinCLIP, is the proposed structure applicable to other methods? The authors should provide explanations or experiments to demonstrate its extensibility and transferability.

4. The paper has some structural issues, notably the absence of a conclusion section.

### Questions
See Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposed an enhancenment module for feature similarity measurement based Anomaly Detection method and conducted experiments on Few-shot Anomaly Detection (AD) setting, a topic that has recently gained considerable attention and holds practical value in real-world scenarios. The authors' innovative use of optimal transport to optimize the process of feature distance measurement is commendable, as it not only introduces novelty but also demonstrates generality by being applicable to different methods. Additionally, the overall organization and writing of the article are well-executed, making it easy to follow and understand. However, the paper has some weaknesses. There is a notable lack of experimental comparisons; for instance, if the GraphCore method published in ICLR23 achieves significantly higher P-AUROC for MVTec 4-shot and I-AUROC for MPDD 4-shot compared to the best results of the paper's method, these results should be included in the comparison table (Table 1). The analysis of experimental results also needs to be strengthened, as there is significant variation in the improvement observed across different datasets. The proposed method shows a larger improvement on WinClip in MVTec but a larger improvement on PatchCore in VisA, and this inconsistency lacks theoretical analysis. The methods described in the article can be seen as a plugin for enhancing performance, and directly showing the increment in Table 1 would make it easier to read. Especially when the increment varies across different datasets, calculating the average improvement could better reflect the value of the method. Additionally, there is an inconsistency in the font used for "l" in Formula (1) on line 144, as well as lines 145 and 146, which can lead to confusion. Lastly, the relative changes in results on MPDD are quite noticeable, which could be attributed to the smaller size of the MPDD dataset (458 test images) and its inherent randomness. Conducting comparative experiments on larger datasets, such as the newly proposed Real-IAD dataset in CVPR2024, would provide a better reflection of the effectiveness of the methods.

### Strengths
1.Few-shot AD, which has gained considerable attention recently, also holds practical value in real-world scenarios.
2.Leveraging optimal transport to optimize the process of feature distance measurement is innovative and also exhibits generality in being grafted onto different methods.
3.The overall organization and writing of the article are well done.

### Weaknesses
1.There seems to be a lack of experimental comparisons. If the GraphCore method published in ICLR23 achieves significantly higher P-AUROC for MVTec 4-shot and I-AUROC for MPDD 4-shot compared to the best results of the paper's method, it should have been included in the comparison table (Table 1).

2.The analysis of experimental results needs to be strengthened. There is a significant variation in the improvement observed across different datasets. The proposed method shows a larger improvement on WinClip in MVTec, but a larger improvement on PatchCore in VisA. This inconsistency lacks theoretical analysis.

3. The methods described in the article can be seen as a plugin for enhancing performance. In the comparison with other methods in Table 1, directly showing the increment in the table makes it easier to read. Especially when the increment varies across different datasets, it may be better to calculate the average improvement to reflect the value of the method.

4.  inconsistency in the font used for "l" in Formula (1) on line 144, as well as lines 145 and 146. It can indeed lead to confusion.



### Questions
1. The relative changes in results on MPDD are quite noticeable, which could be attributed to the smaller size of the MPDD dataset (458 test images) and its inherent randomness. Conducting comparative experiments on larger datasets, such as the newly proposed Real-IAD dataset in CVPR2024, would provide a better reflection of the effectiveness of the methods.

Review information added after rebutal:
My concerns have been addressed, and the author will add the experiment results in the final version after acceptance.

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
5

### Summary
The paper addresses the challenge of industrial anomaly detection (IAD) in low data regimes. The authors argue that previous methods, while constructing normal prototypes from a few normal training images, do not adequately refine these prototypes using query images. Their proposed model leveraging an EM-based optimization algorithm to refine prototypes through iterations that suppress anomalies and transfer characteristics from query features.

### Strengths
1.	The paper presents a novel approach to few-shot IAD by formulating prototype refinement as a nested optimization problem, which is innovative in the field of industrial anomaly detection.

2.	The model is designed to integrate existing popular methods like PatchCore and WinCLIP, demonstrating its versatility and potential for widespread adoption.

### Weaknesses
1. The motivation of the work is not clear. It lacks necessary explanation on why OT is used, in the EM algorithm.

2. It is necessary to construct experiments to clarify "Point-to-point regularization does significantly limits the ability to transfer characteristics from query images to prototypes" (line 51-52) and “Previous methods may result in suboptimal prototype refinement ……” (line 81-86).

3. Some notations are confusing: $M\in R^{\alpha \times k\times h \times s}$, $s$ is not defined, line 149.

4. The presentation of the article needs to be improved as the current article is difficult to follow.

5. This paper is faithful to the idea of FastRecon, but the advantage of FastRecon is that it directly computes a closed solution for feature reconstruction, which speeds up inference. However, the method proposed by this paper is based on PatchCore, and the actual inference speed is not improved compared with Patchcore and FastRecon, so the term 'Fast' in the title is not justified.

6. Optimal transport is an effective method that can directly achieve significant performance gains, but the authors did not provide further experiments on OT.

### Questions
1. In Table 2, is the first setting (w/o W* , T*) naive WinCLIP? Why is the performance lower than the original (Table 1, 2-shot), especially Image-level AUROC?

2. Please provide some explanations on the limited performance improvement of WinCLIP+ over WinCLIP?

### Soundness
2

### Presentation
2

### Contribution
1
