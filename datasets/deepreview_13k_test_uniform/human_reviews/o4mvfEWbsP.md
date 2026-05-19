# Sparse Hyperspectral Band Selection Based on Expectation Maximization

- Decision: Reject
- Scores: 5, 3, 3, 5

## Abstract
Band selection is crucial in spectral imaging, as it involves choosing the most relevant bands from large hyperspectral datasets to retain essential information while reducing the burden of data transmission and analysis. Addressing this need, we introduce a novel method for band selection that utilizes an Expectation Maximization algorithm to facilitate selection through the sparsification of spectral band importance. Our method enhances sparsity effects and effectively delineates the relationships between spectral bands during the sparsification process. Supported by thorough theoretical analysis and experimental validation on public datasets, our approach has proven to be both robust and practical. Compared to other sparsification methods, it not only excels in achieving significant sparsity effects but also demonstrates marked advantages in illustrating inter-band relationships. Our method delivers outstanding performance in band selection tasks and holds potential for broader applications in other sparsity-oriented contexts in the future.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a novel hyperspectral band selection method that leverages sparse importance representation and Expectation Maximization. The method is applicable to both supervised and unsupervised tasks, achieving state-of-the-art performance on several real hyperspectral datasets. Overall, the paper offers valuable insights into feature selection; however, several issues need to be addressed.

### Strengths
1. The paper presents a novel band selection method specifically designed for hyperspectral images. This method leverages the Expectation-Maximization algorithm and sparse representation, distinguishing it from existing band selection approaches.
2. The paper offers a solid theoretical foundation and introduces an effective optimization strategy for the proposed method.
3. The proposed method is versatile and can be applied to a variety of downstream tasks, including both supervised and unsupervised classification.
4. The experimental results on three hyperspectral datasets demonstrate a promising improvement over existing methods.

### Weaknesses
1. Due to the hyperspectral imaging mechanism, spectral bands are not independent, particularly among adjacent bands. This is a significant distinction between band selection and traditional feature selection. However, the proposed method does not account for this issue, which diminishes its applicability to hyperspectral images. 
2. The proposed method combines Expectation-Maximization with a sparsification process, alternating the selected bands into a deep learning model. However, it is unclear why this approach is superior to inputting all bands directly into the deep learning model for feature learning. Furthermore, the distinction between band selection and channel attention is ambiguous; the latter can be trained in an end-to-end manner. What is the true advantage of the proposed method?
3. Sparse representation techniques have been widely utilized for feature selection or band selection. How does the introduced sparsification process differ from classical sparse representation learning? 
4. The optimization of the importance weight $c$ during training is not clearly explained. Further clarification is needed.
5. In Table 3, the bands selected by the proposed method on the KSC dataset include adjacent bands, such as 24-26 and 30-32. Intuitively, this appears inappropriate for hyperspectral images. How do the authors justify this selection and the better classification accuracy?

### Questions
See the Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents a novel method for band selection based on expectation maximization algorithm, which facilitates the selection process via the sparsification of spectral band importance. The presentation is clear and extensive experiments demonstrate the effectiveness of the design.

### Strengths
1.	The authors integrate band selection and post-tasks within a unified framework. For the first time, the EM algorithm is adopted for band selection, facilitating the sparsity of band importance.
2.	The authors provide a theoretical analysis of the model. Extensive experiments are conducted to demonstrate the effectiveness of the design.

### Weaknesses
1.	The literature review on band selection is limited in the section of related work. A number of new relevant methods are not mentioned.
2.	The problem formulation and motivation of this paper are not precise. Some statements lack evidence and are not convincing. For instance: in line 46, “.These approaches are problematic because the assigned importance is not always precise and overlooks the interplay between bands”. There are many band selection methods that leverage the band correlations. Moreover, in line 52: “Existing methods of imposing sparsity, such as L1 and L2 losses, do not consistently yield table sparsity effects;” This sentence is vague and is difficult to understand. The claimed second challenge in line 52 is not convincing.
3.	The comparison is unfair. The proposed method is supervised, which introduced the post-task related loss. However, the compared methods are task-independent. For this reason, the results are not convincing.

### Questions
1.	Since the compared methods are task-independent, the improvements of the proposed method can be mainly attributed to the task-related loss. The authors need to provide fair comparisons.
2.	How to set the number of bands in real applications? How does the number of bands influence the performance?
3.	The authors claim “a novel deep-learning band selection method” in the conclusion. In which part, deep neural network is utilized. 
4.	In the abstract, the authors claim that the proposed method is robust. In which aspect, it is robust. How to support this claim?

### Soundness
2

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
4

### Summary
This method leverages an Expectation Maximization (EM) algorithm to sparsely represent the importance of spectral bands, thereby enhancing selection efficiency and reducing data processing complexity. The paper asserts that this approach not only achieves significant sparsity but also excels in illustrating the inter-band relationships, offering a potential solution for spectral band selection tasks. The authors provide a comprehensive theoretical analysis and experimental validation using public datasets, demonstrating the method's superiority over other sparsification techniques.

### Strengths
Neither the questions raised nor the methods used in the paper are new.

### Weaknesses
EM algorithm is out of date in the area of hyperspectral image band selection.

### Questions
1.Band selection refers to selecting important bands from hyperspectral images rather than selecting bands with high correlation from hyperspectral datasets.
2.The author points out that existing methods are not always accurate in assigning band importance. How can we prove whether this problem exists? How can you prove that your method can effectively solve this problem?
3.The loss of L1 and L2 cannot produce stable sparse effects, and this issue should be illustrated with a diagram to help readers better understand.
4.Why use the EM algorithm to design the band selection method? How does your method solve the problem of unstable sparsity of L1 and L2, as well as the difficulty in describing the band relationships during the sparsity process? All of these need to be logically explained in the introduction.
5.The method lacks a framework diagram, which should allow readers to clearly understand the steps of the method without reading the entire text.
6.Why is the name of the method used instead of the author in the experimental table? My suggestion is to modify it to the method name and year.
7.In the field of band selection, SVM is a commonly used evaluation method, and you should add relevant experiments on SVM.

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a novel method for band selection in hyperspectral images, by integrating sparsity within an EM algorithm.

### Strengths
The method is interesting, with some nice theoretical properties. The paper is well written.

### Weaknesses
The authors present their method as being the first to implement a sparsity representation method based on the EM algorithm. However, this is not correct, as the authors are missing many related methods that integrate sparsity within an EM algorithm. Some of the missing related methods are:
- Bouveyron, C., & Brunet-Saumard, C. (2014). Discriminative variable selection for clustering with the sparse Fisher-EM algorithm. Computational Statistics, 29, 489-513.
- Ghosh, A. K., & Chakraborty, A. (2017). Use of EM algorithm for data reduction under sparsity assumption. Computational Statistics, 32, 387-407.
- Wang, Z., Gu, Q., Ning, Y., & Liu, H. (2015). High dimensional em algorithm: Statistical optimization and asymptotic normality. Advances in neural information processing systems, 28.
- Latouche, P., Mattei, P. A., Bouveyron, C., & Chiquet, J. (2016). Combining a relaxed EM algorithm with Occam’s razor for Bayesian variable selection in high-dimensional regression. Journal of Multivariate Analysis, 146, 177-190.
- Ročková, V. (2018). Particle EM for variable selection. Journal of the American Statistical Association, 113(524), 1684-1697.
- Ročková, V., & George, E. I. (2014). EMVS: The EM approach to Bayesian variable selection. Journal of the American Statistical Association, 109(506), 828-846.
- Wang, J., Liang, F., & Ji, Y. (2016). An ensemble EM algorithm for Bayesian variable selection. arXiv preprint arXiv:1603.04360.

As a result, the contributions of the submitted work are clearly positioned in such literature. Moreover, the comparative experiments are missing such related work.

### Questions
Positioning within the literature, including the above cited work.

### Soundness
3

### Presentation
3

### Contribution
3
