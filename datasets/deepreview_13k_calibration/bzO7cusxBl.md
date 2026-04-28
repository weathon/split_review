# Cross-domain Few-shot Classification via Maximization Optimized Kernel Dependence

- Decision: Reject
- Avg Score: 6.25
- Scores: 5, 6, 6, 8

## Abstract
In cross-domain few-shot classification, \emph{nearest centroid classifier} (NCC) aims to learn representations to construct a metric space where few-shot classification can be performed by measuring the similarities between samples and the prototype of each class. An intuition behind NCC is that each sample is pulled closer to the class centroid it belongs to while pushed away from other classes. However, in this paper, we find that there exist high similarities between NCC-learned representations of two samples from different classes. These undesirable high similarities may induce uncertainty and further result in incorrect classification of samples. In order to solve this problem, we propose a bi-level optimization framework, \emph{maximizing optimized kernel dependence} (MOKD), to learn better similarities (dependence) among samples so that similarities among samples belonging to the same class are maximized while similarities between samples from different classes are minimized. Specifically, MOKD first optimizes the kernel \emph{Hilbert-Schmidt Independence Criterion} (HSIC) by maximizing its test power to obtain a powerful kernel dependence measure, the optimized kernel HSIC (opt-HSIC). Then, an optimization problem w.r.t. the opt-HSIC is solved to maximize the similarities among samples belonging to the same class while minimizing the similarities among all samples simultaneously. Since kernel HSIC with large test power is sensitive to dependence, it can precisely measure the dependence among representations of samples. Extensive experiments on the popular benchmark Meta-Dataset show that MOKD can achieve \emph{state-of-the-art} generalization performance on unseen domains under most task settings and is able to learn better data clusters.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors propose a method called MOKD (Maximizing Optimized Kernel Dependence) which learns a set of class-specific representations by maximizing the dependence between feature representations and minimizing the dependence among all samples based on the optimized kernel dependence measures. To this end, they utilize Hilbert-Schmidt Independence Criterion (HSIC) which attempt to maximize optimized kernel dependence which is recently adopted in SSL-HSIC (Li et al., 2021b). The method can be seen as an extension of this method. I would not be surprised if the authors are same. The only difference is the utilization of test power in the revised method. The authors report better accuracies compared to SSL-HSIC.

### Strengths
Basic strengths of the paper can be summarized as follows:
i) The method is basically built on strong theoretical foundations whose efficacy is proved in the literature. The authors utilize the Hilbert-Schmidt Independence Criterion (HSIC) and kernel dependence maximization and efficacy of these concepts are already well demonstrated in the similar classification problems. 
ii) Demonstrating the ties between NCC and the proposed method is a plus. 
iii) Introducing test power concept seems novel. 
iv) The authors report better accuracies compared to the related methods including SSl-HSIC.

### Weaknesses
Main weaknesses of the paper can be summarized as follows:
i) There is a very similar method (SSL-HSIC) using the same concepts. As far as I understand the only difference is utilization of test power concept. Therefore, this method is revised version of another method, which limits the novelty.
ii) There are some wrong statements in the paper. The authors define k(z,c_c) as the kernel function given at the likelihood function used in Equation (1). I checked the paper again. The correct term must be exp(-d(z,c_c)) and d(z,c_c) is actually distance between z and c_c. Furthermore, the authors (Li et al., 2021a) use Mahalanobis distance not the cosine distance. Please note that the whole term, exp((-d(z,c_c)) looks like a Gaussian kernel function without a width term. They must be corrected. If the authors used this terminology in their proofs, they must be corrected as well.
iii) All the arguments given under Theorem 1 are not new, they are given in the main NCC paper. Similarly, the arguments given below Theorem also exist in (Li et al., 2021b).
iv) The optimization problem given at (5) is a constrained optimization problem and I wonder how the authors enforce these two constraints. For the first one, they convert it to selection of a width term if I understand correctly. What about the second constraint? Please give more information on optimization of the problem.
v) The authors compare their proposed method to URL, but I wonder why they do not compare against SSL-HSIC and NCC? Furthermore, the authors' use of cosine similarity within the likelihood function effectively reduces their method to a bias-less cross-entropy loss applied to normalized features. This formulation constrains the feature space to the outer shell of a hypersphere, which is problematic for open-set recognition scenarios and limits the general applicability of the method.

### Questions
1) The authors compare their proposed method to URL, but I wonder why they do not compare against SSL-HSIC and NCC? 
2) Please explain how the optimization problem is solved in more details (e.g., how the contraints are enforced?)

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a cross-domain few-shot classification method that is called maximizing optimized kernel dependence (MOKD). The proposed method consists in an optimization problem based on Hilbert-Schmidt Intendance Criterion (HSIC), in which the similarities among samples of the same class are minimized while the similarities among all samples are maximized. Experiments on standard benchmark of Meta-Dataset show that MOKD achieves better performance than the competing methods.

### Strengths
(1) Hilbert-Schmidt Intendance Criterion (HSIC) is a powerful kernel method for measuring dependence between two random variables. This measure is rarely used in few-shot learning (FSL) and this paper makes an interesting exploration by introducing it into FSL.

(2) The paper derives the objective of optimized kernel HSIC (opt-HSIC) based on Theorem 1, 3 and 4, clarifying its connection with the nearest centroid classifier (NCC).

### Weaknesses
The proposed MOKD method is very sensitive to parameter $\gamma$ (see figure 8 in appendix). This point is not raised especially in main paper: in section 5.2, only benefits of incorporating HSIC term is mentioned but not the sensibility of its contribution. It would interesting to elaborate more in the main paper on this point.

### Questions
1. Could you elaborate more on the senstivity to the $\gamma$ parameter? Especially how is is set for the various datasets.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes to replace the Nearest Centroid Classifier (NCC) loss with a loss based on Hilbert-Schmidt Independence Criterion (HSIC). The proposed loss called Maximizing Optimized Kernel Dependence (MOKD) is a bi-level optimization framework. MOKD first optimizes kernel parameters by test power maximization. Then, HSIC loss maximizes dependence between representations and labels and minimizes support among all samples based on optimized kernel dependence measure. Experiments on Meta-Dataset show the MOKD outperforms state-of-the-art methods on cross-domain few-shot classification methods and ablation studies.

### Strengths
-	The method of replacing NCC loss with HSIC loss is based on theoretical analysis (the upper bound analysis of NCC loss.)
-	The results on Meta-Dataset are better than state-of-the-art methods. 
-	MOKD could produce prototypes that are better clustered compared to NCC-based loss. 
-	Kernel parameter optimization by the Test Power Maximization (TPM) seems novel, and the ablation study confirms its effects. 
-	MOKD does not significantly increase the running time compared with the URL baseline.

### Weaknesses
-	This paper proposes to learn the Nearest Centroid Classifier (NCC) by HSIC. This point seems not directly related to the Cross-domain problem. 
-	The performance improvement by MOKD on the Trained on All Datasets setting is small.

### Questions
- Why would MOKD generalize unseen domains well? 
- How is the classification performed on the test dataset? Is it the same as NCC?  Does the TPM is also conducted on the test dataset?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In the realm of cross-domain few-shot classification, the nearest centroid classifier (NCC) endeavors to develop representations that craft a metric space, facilitating few-shot classification through the assessment of similarities between samples and the prototype of each respective class. A foundational idea behind NCC is the gravitational pull of each sample towards its respective class centroid while simultaneously being repelled from other classes. Nonetheless, the authors observed alarming similarities between NCC-derived representations of samples hailing from disparate classes. Such inadvertent similarities could sow seeds of doubt, potentially culminating in the misclassification of samples. Addressing this quandary, they put forth a dual-layer optimization framework coined as maximizing optimized kernel dependence (MOKD). MOKD aims to refine the perceived similarities (dependence) amongst samples, maximizing the likeness among samples of a shared class while simultaneously suppressing similarities between samples of distinct classes. In its initial phase, MOKD optimizes the kernel Hilbert-Schmidt Independence Criterion (HSIC), amplifying its test power to attain an influential kernel dependence measure known as optimized kernel HSIC (opt-HSIC). Subsequent to this, an optimization challenge concerning the opt-HSIC is undertaken to accentuate the similarities among samples from identical classes while concurrently minimizing similarities across the entire sample pool. Given the pronounced test power of kernel HSIC, which displays heightened sensitivity to dependence, it can adeptly gauge the dependence within the representations of samples. Rigorous tests carried out on the esteemed Meta-Dataset benchmark confirm that MOKD not only exhibits superior generalization prowess across uncharted domains in a multitude of task settings but also excels in crafting superior data clusters.

### Strengths
1 Cross-domain few-shot classification (CFC) is an important problem setting, where researchers want to find a good way to let a pre-trained model adapt to down stream tasks quickly with a few samples. The problem itself is even more important after many foundation models are proposed recently.

2 This paper focuses on the most important solution pipeline of CFC, and first identifies its issues via checking the similarity between same-label classes and different-label classes. Then, an optimized measure is proposed to solve this issue. The proposed solution is well-motivated by the experiments and the theory, making this paper make a solid contribution to the field.

3 Connecting HSIC to NCC (in a theoretical view) is very interesting, which provides another insight to understand NCC and finally motivates the proposed solution.

4. This paper conducted extensive experiments to verify the proposed solution, which is empirically solid as well. The improvement on unseen domain is impressive, verifying that the proposed solution can obtain better representations for down stream tasks.

### Weaknesses
 1 In Figure 1, we can observe that there are less noise in the MOKD case. However, it seems that the intra similarity is also smaller than (a). Can the authors explain this more?

2 What are implicit assumption this paper adopts to make few-shot learning be successful? Normally, we might have meta-distribution assumption or distribution-closeness assumption.

3 HSIC, as a valid statistic, can always be correct to evaluate the dependence among observed data. What is the exact function of maximizing test power in your method? What is the meaning of test power? It can be found that the opt-HSIC is indeed helpful. Thus, the reason is very interesting to be explained well.

4 How do you obtain the 95% confidence interval in all tables? Details might be needed here.

5 Figure 4 can be revised to avoid that the number 4.3 surpasses the figure.

### Questions
1 In Figure 1, we can observe that there are less noise in the MOKD case. However, it seems that the intra similarity is also smaller than (a). Can the authors explain this more?

2 What are implicit assumption this paper adopts to make few-shot learning be successful? Normally, we might have meta-distribution assumption or distribution-closeness assumption.

3 HSIC, as a valid statistic, can always be correct to evaluate the dependence among observed data. What is the exact function of maximizing test power in your method? What is the meaning of test power? It can be found that the opt-HSIC is indeed helpful. Thus, the reason is very interesting to be explained well.

4 How do you obtain the 95% confidence interval in all tables? Details might be needed here.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent
