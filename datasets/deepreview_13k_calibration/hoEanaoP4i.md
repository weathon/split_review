# MD-LSM: An Efficient Tool for Real-time Monitoring Linear Separability of Hidden-layer Outputs of Deep Networks

- Decision: Reject
- Avg Score: 6.00
- Scores: 6, 8, 8, 5, 3

## Abstract
Many studies have shown that evaluating the linear separability of hidden-layer outputs plays a key role in understanding the working mechanism of deep networks. However, it is still challenging to develop the linear separability measure (LSM) that satisfies all of the following requirements: 1) it should be an absolute measure; 2) it should be insensitive to the outliers; and 3) its computational cost should be low for real-time monitoring the behavior of each hidden layer. In this paper, we propose the Minkowski difference-based linear separability measures (MD-LSMs) that just meet the first two requirements. Moreover, we also introduce an approximate calculation method to significantly decrease their computation costs with only a slight precision sacrifice. As an application example, we conduct the experiments on the real-time monitoring for the hidden-layer behaviors of several popular deep networks, and show that the outputs of the hidden layers adjacent to the output layer have higher linear separability degrees. We also observe that the change of linear separability degree of hidden layers (especially the ones are adjacent to the output layers) are in sync with the change of the training accuracy of the entire network. It implies that the linear separability of some important hidden layers can be treated as a performance criterion to characterize the network's training behavior. The relevant theoretical discussion also validates this finding.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The newly introduced Minkowski Difference-based Linear Separability Measure (MD-LSM) is a tool designed to evaluate and understand the mechanisms of hidden layers in deep neural networks. This measure assesses the ability of a neural network to linearly separate two sets of data by analyzing their distribution through a hyperplane. Using the Minkowski difference, MD-LSM calculates the spatial relationship between data points from different classes, essentially determining if they can be linearly divided at a certain layer. By examining this separability, MD-LSM provides insights into how well the network’s hidden layers contribute to distinguishing between different classes, helping researchers and practitioners analyze the effectiveness of these layers in complex models. MD-LSM achieves this by solving two key factors: maintaining an absolute measure and being insensitive to outliers.

### Strengths
The strength of this paper lies in maintaining the efficiency and absoluteness in the linear separability of the hidden layers through the proposed method, MD-LSM. The measures LS*, LS0, and LS1 achieve efficiency scores, indicating that the model classifies all examples with straightforward accuracy, leaving no ambiguity regarding which points belong to which group. By emphasizing this exact efficiency, the paper enhances our understanding of how deep neural networks operate and underscores the effectiveness of these measures in quantifying linear separability.

### Weaknesses
1. High computational cost may make it difficult to use MD-LSM in large-scale or real-time applications, which could prevent it from being widely adopted for evaluating linear separability in deep neural networks.

2. In Table 2, high variance in results among LS*, LS0, and LS1, especially LS0's poor performance, shows that these models lack reliability and effectiveness in handling highly overlapping data in classification tasks. The high variability of LS2 within the MD-LSM values demonstrates its sensitivity to the analyzed data. This sensitivity can result in instability, complicating the interpretation of results across different scenarios. Furthermore, the LS2 model is prone to overfitting, which can lead to biased outcomes when applied to new data.

3. The evaluation of the proposed theory is incomplete, as factors such as increasing network size and utilizing state-of-the-art activation functions must be considered during the assessment of linear separability in hidden layers; an evaluation with a single dataset is insufficient, and larger datasets like ImageNet should be included for a more comprehensive analysis.

### Questions
see above in weakness section

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
Large neural networks are difficult to analyze directly. Instead, the authors analyze the measure of linear separability of hidden layers. In the paper, a new measure for estimating linear separability is proposed, which satisfies two of the three requirements described by the authors. After that, the paper proposes an approximate extension that satisfies all the properties. The authors demonstrate the effectiveness of the proposed separability measures for classification problems in the image domain. The authors conduct an experiment on a wide class of image classification models. Also, the paper provides a deep mathematical analysis and comparison with other linear separability measures.

### Strengths
As the authors claim, the proposed measure and its extension can really improve monitoring of deep model training. Separately, I would like to note that the work presents a good mathematical justification for all conclusions, which allows for a much better analysis of the applicability limits of the proposed ideas, their limitations and greatly increases the significance of the work. Also, the authors provide experiments on a wide class of models, which demonstrates and emphasizes the universality of the proposed ideas. In general, the work has excellent quality and clarity of the formulated ideas and high originality of the proposed ideas and mathematical calculations, which have high theoretical value and have potentially good practical value.

### Weaknesses
Despite the large number of advantages voiced above. I would like to highlight some points that I would like to see in the work on this topic.

The experiments show monitoring of linear separability for a pair of classes from the CIFAR-10 dataset. In conclusion, the authors point out that experiments on other datasets were not conducted citing limitations on the volume of text and high computational costs. Nevertheless, I would like to see, albeit small, but experiments on data closer to real industry tasks. Also, the proposed measure is positioned as quite universal. However, if in the limitations the authors indicate that the work focuses only on the classification problem, then no discussions about the applicability of the proposed measure to other classification problems, for example, texts or graphs, are indicated in the article.

### Questions
Perhaps I missed the description of the restriction of the proposed ideas to the domain of images in text. How will the proposed measure behave for text classification problems, graph classification problems, and other classification problems?

### Soundness
4

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
4

### Summary
The paper submits a measure to understand the linear separability of hidden layers in deep neural network.

### Strengths
A measure for detecting the linear separability of hidden layer outputs.
The measure makes sense and is solidly done, with theoretical intuition and depth.
Good and detailed experimental sections.
Good Theoretical results.

### Weaknesses
While the paper is solidly written, I would suggest certaint improvements.

Please detail the notion of major side and minor. These two ideas later become really important in defining your metric. So, we need more intuition below Definition 2.4

prior to going to an approximate calculation of MD-LSM, I would suggest dicsussing the implications/intuition when a linear network of one layer is not used. In practice we use, a multi layer network, an intuition on how the ideas for one layer linear network would translate to this case are important and necessary.

I really think, that the discussion on the synchronicity phenomenon should be indicated somewhere in the front of the paper. Because, I went most of the paper trying to understand, why do I need to care about linear separability of hidden layers.

The notion of multi-point sets, how is this translated to a data set in a standard ML literature.

Most ML methods involve a nonlinear function in the middle. how does the measure (relative or absolute) deal with that, what is the notion of separability in these contexts?

### Questions
The notion of multi-point sets, how is this translated to a data set in a standard ML literature.

Most ML methods involve a nonlinear function in the middle. how does the measure (relative or absolute) deal with that, what is the notion of separability in these contexts?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The primary goal of the paper is to develop a computationally efficient method to measure the linear separability of each hidden-layer output in deep networks. The MD-LSM is specifically designed to be an absolute measure, robust, computationally inexpensive, insensitive to outliers and able to perform real-time monitoring.
Comparison with SoTA such as GDV, GRQ, Structural manner (Hidden classification layer) (Table 1); Proposed method provides a potential for improving model interpretability; Formal definitions and theorem-based explanations; Adaptibility to different network structures (VGG-16, GoogleNet Inception V1, ViT); Detailed algorithmic flows and extensive experimental report.
the authors have relied on simple activation functions and less number of layers. It will also be extremely interesting to work on a generalized solution that can address the non linear transformations as well. The paper is well-written and introduces an intriguing theoretical concept supported by rigorous proofs. However, additional experimentation is necessary to validate the findings further. Lines 489 to 498 highlight some of the identified limitations, and the authors plan to address these in future work, which will enhance the overall completeness of the paper.

### Strengths
The paper is well written with a precise structure. It forms a theoretical foundation for the proposed Minkowski distance based linear separability measure. The supplementary material is comprehensive, containing rigorous mathematical proofs and detailed experimental reporting, with implementations across various deep network architectures.

### Weaknesses
However, the work lacks a thorough experimental analysis, particularly in addressing practical implementation challenges. A notable limitation is the absence of discussion on real-time monitoring difficulties in large networks, with no proposed solutions including techniques such as scaling or dimensionality reduction.
The choice of Minkowski difference, while computationally advantageous for calculating linear separability, lacks clear theoretical justification in the paper. This approach focuses on pairwise differences and may overlook global distributional features. Other approaches may involve using kernel-based methods (making it effective for both linear and nonlinear separability), Wasserstein distance, contrastive loss-based measures, etc. which cater to a larger problem. The paper's Theorem 2.2 makes the questionable assumption that linear separability can always be represented by a hyperplane through the Minkowski difference, failing to account for scenarios with overlapping class boundaries or even multiple hyperplanes. Furthermore, the strict emphasis on linear separability neglects the possibility of non-linear relationships in complex data distributions, which are prevalent in most real-world datasets. This limitation becomes particularly apparent when dealing with specialized data types like point cloud data, where higher dimensional patterns can be easily missed, highlighting the method's constraints in handling more complex data structures.
The theoretical framework presented here aims at establishing an absolute measure yet shifts towards an approximation of MD-LSM in practical implementations, effectively making it a relative metric. This inconsistency between the theoretical foundation and the practical application raises questions over the fundamental purpose of the measure. While the paper explores this relative approach, it overlooks well-established methods like KL divergence (Kullback and Leibler, 1951), which has demonstrated significant success in tracking distributional shifts over time and has proven particularly valuable for real-time model monitoring applications. Additionally, despite the approximations introduced in practical implementations, the computational burden remains substantial, suggesting that the proposed method may not offer significant advantages over existing approaches in terms of computational efficiency.
The comparative analysis between the original MD-LSM and its approximation is only provided with respect to the dataset distribution and not with respect to changing model architectures. It is not feasible to be used in large scale models as Line 135 states that the approximation values slightly differ from original ones, and this error could massively increase with increasing layers as in the case of complicated classification tasks, that include composition of multiple hidden layers (Line 148-150). The experimental scope is notably restricted, with ViT being the only architecture incorporating attention mechanisms. This limited testing raises questions about the method's applicability to more complex and commonly used models, particularly in NLP tasks where heavier attention-based architectures are standard practice. The absence of experiments with these contemporary, computationally intensive models leaves a critical gap in understanding the method's scalability and reliability across the full spectrum of modern deep learning applications.
The paper's claim regarding outlier insensitivity lacks experimental validation, presenting it as an apparent fact without proper empirical support. A detailed experimental analysis on anomalous and imbalanced datasets will help create a clear picture. Furthermore, the MD-LSM implementation uses the one-vs-rest strategy to handle multi-class classification tasks which also has many drawbacks. This approach is likely to miss significant inter-class relations and may also lead to interpretation issues, especially when dealing with multi class problems.
Empirical analysis of proofs in supplementary section is missing. Assumptions such as 𝑀.𝑀𝑇 = 𝐼, vastly reduce the generalizability of the methods, as it does not hold for data with high correlation or redundancy. There is also a lack of statistical analysis to clearly understand the robustness and consistency of MD-LSM across different network architectures and layers.
There is a synchronicity between training accuracy and MD-LSM, which is ironic as training accuracy is a relative measure. A model may exhibit high training accuracy, but poor generalization as seen in the case of overfitting. Therefore, if such synchronicity exists, an elaborate experimental discussion along with the extensive report will be interesting and may further lead to a better perspective. Understanding this relationship could lead to:
1. Better model evaluation techniques
2. More effective training monitoring
3. Improved early stopping criteria
4. More reliable model selection methods
The analysis may also include dropping / freezing layers to observe overall changes. (Line 151-155).
Line 223, “Since the computation of LS∗(A, B) is difficult, we consider its variant”, line 229 “Unfortunately, it is still difficult to solve LS0”: Contradicting statements. No proper justification for introducing LS0, as the sign function only reduces one logic step, in comparison to LS∗. Line 235-238, “If all points of MD(A, B) locate in one side of ωTm = 0, i.e., the two sets A, B are linearly separable, it holds that LS1(A, B) = 1. In contrast, if the value of LS1(A, B) is close to zero, the convex hulls of the two sets A, B overlap heavily. Because of the existence of absolute value operation, the solution of LS1 is difficult as well.” The problem of heavy overlap is introduced but not addressed. The low absolute and relative scores in Table 2, again bring out this issue.
Lastly, there is a writing error in line 261, “We achieves”.

### Questions
Posed in the Weakness section...

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper presents a novel approach to analyzing the linear separability of the latent representation of hidden layers in deep neural networks. It introduces the Minkowski difference and analyzes the maximum linearly separable subsets induced by it. The method is validated on multiple architectures on the CIFAR10 dataset.

### Strengths
- the background work is clearly reported and explained, with a clear overview of previous works with their pros and cons
 - the proposed method is theoretically grounded, and the explanation in Sec 2.1 is very clear
 - the paper is accompanied by clear and nice plots, showing the different aspects of the approach

### Weaknesses
 - the paper presents a method that should address the efficiency of the problem, which the authors state is a weak point of all other methods. However, no performance statistic nor computational complexity analysis is carried out. Thus, such “efficiency” cannot be assessed. Furthermore, the choice of not comparing against linear probing, which is the most relevant competitor, is not justified.
 - The method proposes a sound approach for evaluating the linear separability of latent representation learned by neural networks. However, such a sound approach has to be drastically simplified to make it computationally feasible and (supposedly) inexpensive. However, the only analysis carried out to analyse how drastic this approximation is, it’s on low-dimensional, synthetic datasets. Moreover, the results presented in Table 7 and Table 8 show that the approximated $LS_i$ metrics are not consistent across different layers, further questioning the validity of the approximation.
 - at the end of Sec3.2, it is stated that for real-world networks, only a subset of the data is used for computational reasons (only using a batch of 500). This is evidence that the proposed method is not as efficient as promised. Furthermore, a linear probe on 500 samples is almost instant to train using simple and lightweight optimizers like L-BFGS.
 - no supplementary material is provided, limiting reproducibility and independent evaluation of the results.
- remark 2.6 states that the approximate evaluation of the metrics is carried out using $\hat{\omega}$ as maximizer. However, the separating hyperplane obtained from this vector seems to simply be the one connecting the centroids of the two groups. If this is indeed the case, the authors should justify how the method proposed differs from previous literature.

Other concerns:
 - From section 2.2, the math becomes more cumbersome than the previous part. In particular, $|MD(A,B)| = |A \times B| = |A| \cdot |B|$, which is clearer (referring to the last part of page 4).
 - Eq.2 is overly complicated: if you search over any $w \in R^N$, then you don’t need the inner-max since $1(w^Tm<0) = 1(-w^Tm>0)$. Therefore, the $w$ that maximizes the inner equation can just have the opposite sign. In other words, you just need $LS_*(A,B) = max_{w \in R^N} \frac{\sum 1(w^Tm > 0)}{|A| \cdot |B|}$, which is most likely easier to understand.
 - Eq.4 has the same “problem” as Eq.2, meaning that the search over all $w$s already includes the other sign.
 - in Sec 2.3, you go on at approximating the original Eq.2 multiple times, and at the end, you end up with a very heavy simplification, $\hat{w}$, which is still $O(|A|x|B|)$. How is this more “efficient” than linear probing, which has computational complexity $O(np^2+p^2)$ (n samples p features) for regression, or using lbfgs for logistic regression? This is even worse for multi-class, where the OvR approach requires S calculations.
 - in Sec 2.4, “Their largest relative error is less than 3%. This finding supports the effectiveness of the approximate manner” is arguably opinable since this statistic is drawn from a single dataset, which is furthermore synthetic, so it cannot be taken at all as a general statistic of the proposed method approximation error. The same holds for the subsequent comparison.

### Questions
Overall, I am open to reconsideration, if new comparison are added from the computation perspective, mainly showing how this method is either better than probing given the same time budget, or that given equally good results, it takes less time, otherwise it seems that the contribution on the “efficiency” (which is the main difference to probing) cannot be assessed.

### Soundness
2

### Presentation
3

### Contribution
1
