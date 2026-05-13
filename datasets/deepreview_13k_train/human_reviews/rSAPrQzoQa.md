# Subject Clustering by an Improved IF-PCA Algorithm

- Decision: Reject
- Scores: 3, 5, 6, 6

## Abstract
Subject (e.g., cell or patient) clustering is an important problem in genetics and genomics.  Influential features PCA (IF-PCA) is a recent idea for clustering, where we first select a small fraction of measured features and then cluster subjects (e.g., cells or patient) into different groups using the classical PCA clustering approach. A challenge the method faces is that, we may have complex signal and noise structures across features or across subjects or both, which may make the IF-PCA less effective. 
To deal with such a challenge, we propose a new approach, IFPCA+, where  we combine IF-PCA with the recent idea of manifold fitting. The latter was shown to better support class separation. We compare our approach with the most popular subject clustering approaches, including but not limited to  DESC, SC3 and Seurat, using 10 gene microarray data sets and 8 single-cell data sets.  We show that with the new method,  we have a significant improvement in feature selection accuracy,  and that on average,  our method outperforms several of the most competitive algorithms nowadays (including IF-PCA, DESC, Seurat) in terms of clustering accuracy and ARI. We also shed light on the insight underlying such improvements.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes a novel strategy to cluster high-dimensional datasets, and applies it to number of important benchmark datasets, including both scRNA and micro-arrays.

### Strengths
- Clustering high-dimensional data is an important and unsolved problem
- Methods that work well on scRNA data are important
- Section 2.3 explains the IFPCA+ method well.  
- The improvement of DMF over IF in Table 5 is impressive.

### Weaknesses
 - I found the description of the method difficult to follow.  I do not need to know the history of developments of related methods.

- My summary of the work is that is it essentially a way of pre-processing the data to let IF-PCA run better (with slight modifications to the parameters of IF-PCA).  To the extent that it works, that is useful.  However, there is no theory suggesting when it would work.  The simulations are limited, in that I do not see comparison to the other methods in the simulation, nor do I know precisely which metrics are computed in the simulation.  It seems this work is more suitable for a venue like KDD.  To be appropriate for this venue, more theory would be appropriate. 

- In the end, the method takes longer, improves a little in terms of some metrics of interest, but does not provide any more insight into the data.

### Questions
1. What is 'subject clustering', as opposed to 'clustering'?

2. Manifold fitting, both sample-wise and feature-wise, are new to me.  Is manifold fitting just another name for manifold learning? Please explain these concepts prior to using them. 

3. What is a 'nonlinear dataset' (line 98 and elsewhere)

4. Some of the references are incorrect, please correct.

5. Please put all the background material in a background section.  The methods can then simply describe your method, highlighting the differences with previous work.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper proposes an enhanced version of the Influential Features PCA (IF-PCA) method, referred to as IF-PCA+. The authors identify several limitations of the traditional IF-PCA, particularly its assumptions regarding sample independence, feature selection that overlooks correlations, and its ineffectiveness in handling high dropout noise commonly found in single-cell RNA sequencing (scRNA-seq) data. To address these challenges, the authors integrate a novel manifold fitting component, DMF (Data Manifold Fitting), with the modified IF-PCA. This combination aims to improve the robustness and accuracy of clustering in high-dimensional data. The paper reports that IF-PCA+ achieves competitive performance compared to modern clustering algorithms, demonstrating high accuracy in various datasets, including the Grun dataset and others where traditional IF-PCA struggles.

### Strengths
Originality: The paper presents a novel approach by integrating manifold fitting into the IF-PCA framework, resulting in the new method IF-PCA+. This proposal addresses several limitations of traditional IF-PCA, particularly in handling high-dimensional data with complex noise structures. The introduction of Diffusion-based Manifold Fitting (DMF) improves robustness against noise, leading to a significant advancement over clustering methodologies.

Significance: By improving clustering accuracy and feature selection in high-dimensional datasets, IF-PCA+ can facilitate better insights into biological processes and disease mechanisms. The findings could have broad applications in various domains, including cancer research and personalized medicine, making this work highly relevant and impactful.

### Weaknesses
The clarity of presentation of this paper needs to be improved. There are a lot of English mistakes, subject-verb disagreement, singular/plural noun errors, incorrect use of or missing articles (the/a/an), incorrect prepositions, verb form/conjugation errors, etc. Additionally, there are some typos in the mathematical formulas. These should be carefully addressed prior to the publication of this paper.

Examples:

ABSTRACT：
The phrase 'including IF-PCA, DESC, Seurat' is missing the conjunction 'and' before 'Seurat'.
Please define the acronym 'ARI' the first time it is used in the text.

1 INTRODUCTION
line 035: Change 'n subject' to 'n subjects'.
line 041: Change 'other feature are' to 'other features are'.
line 058: Change 'which poses' to 'posing'.
line 059: Change 'Last but not the least' to 'Last but not least'.
line 067: Change 'recover' to 'recovers' and 'by address' to 'by addressing'.
line 071: Change 'proves' to 'proves to be'.
line 073: Change 'feature' to 'features'.
line 078: Change 'neighborhoods' to 'neighboring'.
line 083: Add 'the' before 'empirical evidence'.
line 085: Change 'eliminated' to 'eliminating' and 'replaced' to 'replacing'.
line 087: Change 'resulting' to 'result' and 'utlize' to 'utilizes'.
line 092: Change 'with' to 'against'.
line 095: Change 'perform' to 'performs'.
line 096: Change 'Comparing to' to 'Compared to'.
line 097: Change 'perform' to 'performs' and 'achieve' to 'achieves'.
line 098: Change 'does not do well' to 'does not perform well'.
line 107: Change 'section' to 'Section' (to maintain consistency in capitalization).

2 METHODS
line 122: Change 'correlation based' to 'correlation-based'.
line 127: Change 'places' to 'room'.
line 133: Change 'an manifold' to 'a manifold'.
line 127: Correct the typo 'bandwith' to 'bandwidth'.
line 135: Change 'a n by Kdiff' to 'an n by Kdiff'.
line 155: Change 'Comparing to' to 'Compared to'
line 165: Change 'curse of dimensionality' to 'the curse of dimensionality' and 'when compared to' to 'compared to'.
line 169: Change 'stabilizing' to 'stabilize'.
line 177: Remove the redundant 'the' in 'the the benchmark'.
line 178: Change 'This support' to 'This supports'.
line 186: Change 'an improvement to' to 'an improvement over'.
lines 198, 200 and 202: Remove the redundant word 'many'.
line 213: Change 'x_i' in the subscript 'x_i \leq t' to 'x_j(i)', for notational consistency and clarity.
line 214: Change '\bar{x}(j)' to '\bar{x}_j' and '\hat{\sigma}(j)' to '\hat{\sigma}_j' , for notational consistency and clarity.
line 228: Change the subindex '-1' to 'K_0'.
line 233: Change 'for manifold fitting algorithms' to 'as a manifold fitting algorithm' or 'for manifold fitting'.
line 247: Add 'the' before 'diffusion map'.
line 252: Correct the typo 'tunning' to 'tuning'.
line 267: Change 'a n by p' to 'an n by p'.
line 313: Change 'matlab' to 'MATLAB' and 'same with' to 'the same as'.
lines 321 and 322: Change 'can be find' (which occurred twice) to 'can be found.

3 RESULTS
line 338: Change 'Table 2, and 3' to 'Tables 2 and 3'.
line 358: Add 'the' before 'gene filter'.

### Questions
In line 270, how to select the tuning parameters n_0, knn_f and knn_s?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents IF-PCA+, an enhanced version of the influential feature principal component analysis (IF-PCA) algorithm, designed for high-dimensional subject clustering. IF-PCA+ incorporates diffusion-based manifold fitting (DMF) to improve feature selection, denoising, and class separation by leveraging both sample-wise and feature-wise manifold structures. The combined IF-PCA+ algorithm is designed to handle nonlinear relationships, correlations between features and samples, and robust noise handling. Experimental results show that IF-PCA+ outperforms several SOTA clustering methods on single-cell datasets and is competitive on microarray datasets.

### Strengths
1. The paper systematically identifies and addresses limitations in existing algorithms, progressively enhancing IF-PCA+ through the integration of DMF and an adaptive K-means clustering approach.
2. Experiments show that IF-PCA+ achieves the best average rank and regret across single-cell RNA-seq datasets, consistently outperforming other competitive methods.

### Weaknesses
1. The Methods section lacks a comprehensive description of prior work (e.g., ysl23, yao2, IF-PCA), making it difficult to follow. Specifically, the paper assumes a strong familiarity with these methods, which is not always the case, and does not adequately explain their core mechanisms or limitations that IF-PCA+ aims to address. Some abbreviations (e.g., KS on line 209) are undefined, and citing experimental results (lines 174-185, 288-289) within the algorithm description seems unprofessional and unnecessary, disrupting the logical flow of the methodology. The inclusion of these results within the method description blurs the line between methodology and validation, making it harder to assess the novelty of the approach.
2. Comparisons use different languages (Python vs. R), leading to biased runtime results; theoretical complexity analysis would be fairer. The reported runtimes are not comparable due to the use of different implementations and environments, making it difficult to draw meaningful conclusions about the efficiency of the proposed method. Additionally, runtime results (lines 316-321) belong in the results section, ideally in a table for clarity, as they are part of the experimental validation rather than the method description itself.
3. Some abbreviations of comparative algorithms (Xs) are unclear and are only explained in the appendix. These explanations should be moved to the main text to improve readability and make the content flow more smoothly. The lack of immediate clarity regarding these abbreviations hinders the reader's ability to understand the comparative analysis and the relative performance of IF-PCA+.
4. The parameters tuning part remains challenging. The paper does not provide sufficient guidance on how to select appropriate parameters for IF-PCA+, which is a critical aspect for practical application. The lack of clear guidelines makes it difficult to reproduce the results and apply the method to new datasets.

### Questions
1. Table 4 shows a large regret gap between IF-PCA+ and IF-PCA, which needs further discussion.
2. Table 5’s IF-sf results reach 1.0 in settings A and B without a clear explanation, raising questions about robustness.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Clustering is an important problem in practice. In this paper, the authors consider subject clustering. They want to improve upon a previously proposed method, IF-PCA, which is to select features first, and then perform clustering of subjects using classical PCA clustering approach on the selected features. The authors argue that IF-PCA may not work well for problems with complex signal and noise structures. As a result, they proposed an improved version, IFPCA+ by combining manifold learning with IF-PCA. They show the performance using many real datasets.

### Strengths
The proposed IFPCA+ intends to overcome a few limitations of IF-PCA. Specifically, IF-PCA assumes samples are independent. Such an assumption doesn’t hold for problems such as single cell data. Furthermore, the feature selection step of IF-PCA doesn’t incorporate correlations among features, and IF-PCA only handles the data linearly. IFPCA+ aims to address these limitations through the use of manifold fitting with the diffusion-based manifold fitting (DMF) algorithm and its integration with IF-PCA. The authors have done comprehensive numerical comparisons with a number of alternative methods.

### Weaknesses
Although IFPCA+ is well motivated as an extension of IF-PCA, the method relies on the key step of manifold fitting. If such a low dimensional nonlinear structure exists, IFPCA+ has the great potential to handle data more effectively. However, it is not clear how to examine such an assumption for a practical problem. Specifically, while the authors suggest using methods like Scree plots or spectral embedding, these are not always definitive, especially in high-dimensional noisy data. Furthermore, there are several tuning parameters to tune, including those within the diffusion map and k-means steps. How should one select them in practice without any knowledge about the potential number of clusters etc.? More discussion on the guideline will be helpful. 

The authors mentioned a number of variants of the IFPCA+ on Page 6. It will be useful to give a clear recommendation on which one to use for a particular problem. For example, what are the trade-offs between the different variants in terms of computational cost and accuracy? A more detailed comparison would be beneficial.

Please provide some discussion on the data size that the proposed method can handle in terms of n and p since in many genomic data, p can be in millions. The current discussion lacks specific details on the computational complexity of each step, making it difficult to assess the method's scalability. It is also unclear how the method would perform with extremely large datasets, where memory limitations might become a significant issue.

### Questions
1.	Single cell data often have zero-inflation. How does that affect the proposed clustering methods? Perhaps add some numerical simulation illustrates the effects of increasing proportions of zeros. The authors seem to suggest that the manifold fitting step helps to handle zero inflation. It is not clear to this reviewer why that is the case. More discussions on this would be needed.
2.	What are the numbers in Table 1? Please explain these numbers and how they were obtained for real data.
3.	For the PCA clustering step, the authors use max(4,K) top left singular vectors to run k-means. Why use 4 instead of a higher number?
4.	Does IF-PCA+ only work for non-negative data since log transformation was used for step 1 on Page 5? I saw a version of nolog-IFPCA+ mentioned later. It will be helpful to provide clear recommendations on which version to use for different applications.
5.	The writing needs to be improved for more clear presentation. For example, for the modified IF-PCA on Pages 4, 5, what does KS mean for the KS step? Are you referring to Kolmogorov-Smirnov test? On page 5, line 252, “tunning” should be “tuning”

### Soundness
3

### Presentation
3

### Contribution
2
