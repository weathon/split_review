# Formalizing Spuriousness of Biased Datasets using Partial Information Decomposition

- Decision: Reject
- Scores: 3, 5, 6, 5, 8

## Abstract
Spurious patterns refer to a mathematical association between two or more variables in a dataset that are not causally related. However, this notion of spuriousness, which is usually introduced due to sampling biases in the dataset, has classically lacked a formal definition. To address this gap, this work presents the first information-theoretic formalization of spuriousness in a dataset (given a split of spurious and core features) using a mathematical framework called Partial Information Decomposition (PID). Specifically, we disentangle the joint information content that the spurious and core features share about another target variable (e.g., the prediction label) into distinct components, namely \emph{unique, redundant, and synergistic information}. We propose the use of unique information, with roots in Blackwell Sufficiency, as a novel metric to formally quantify dataset spuriousness and derive its desirable properties. We empirically demonstrate how higher unique information in the spurious features in a dataset could lead a model into choosing the spurious features over the core features for inference, often having low worst-group-accuracy. We also propose a novel autoencoder-based estimator for computing unique information that is able to handle high-dimensional image data. Finally, we also show how this unique information in the spurious feature is reduced across several dataset-based spurious-pattern-mitigation techniques such as data reweighting and varying levels of background mixing, demonstrating a novel tradeoff between unique information (spuriousness) and worst-group-accuracy.
\let\thefootnote\relax\footnotetext{Accepted at ICML 2024 Workshop on Data-centric Machine Learning Research (DMLR): Datasets for Foundation Models.  \\
\\Correspondence to: Barproda Halder $<$bhalder@umd.edu$>$.
}

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents a novel framework to quantify dataset spuriousness, addressing a gap in formalizing how spurious correlations between non-causal features and the label affect model generalization. The measure is calculated based on unique information and synergistic information values obtained from partial information decomposition. Experiments show negative correlation between the values of this measure and generalization metrics under distribution shift.

### Strengths
1)The problem is important and relevant to OOD Generalization.

2)The proposed measure is novel.

3)The experiments consider a range of datasets and somewhat empirically support the claims of the paper.

### Weaknesses
1)The measure relies on the assumption that causal and spurious features can be separated in the image as foreground and background. However, this assumption may not hold universally or even in most of the cases; for instance, spurious features like rotation or color affect all pixels rather than specific regions. In fact, disentangling causal and spurious features in a major challenge for many OOD tasks.

2)In the experiments, standard deviations or error bars are not provided, making it difficult to assess the scientific significance of the results. Furthermore, error bars are needed not just for the final performance metrics but also for the proposed measure itself, as well as any intermediate calculations involving dimensionality reduction and clustering, since these steps introduce randomness.

3)There is no theoretical proof for why a higher value of the proposed measure would correspond to worse OOD performance. The paper proposes two candidate measures which are demonstrated to be unsuitable in some cases, but it is not clear why the final proposed measure is suitable in all cases. The lack of theoretical justification is a significant weakness.

4)Related to above, this paper lacks novel theoretical contribution. The theory presented is straightforward from partial information decomposition theory. Methodologically too, the main contribution comes from Bertschinger et al., (2014) which is used to calculate PID. The discretization of high-dimensional data, while necessary for PID calculation, also introduces a significant loss of information, which is not adequately addressed.

### Questions
1)During dimensionality reduction, how are the number of clusters chosen? Why do we need to approximate the distribution in a discrete way and what do we lose by doing so?

2)Why are other measures like I(Y;B) etc. not clearly reported in the results? This would help us compare the proposed measure with other measures.

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
In this paper, the authors propose a novel measure of spuriousness by utilizing Partial Information Decomposition (PID) and an explainability framework consisting of segmentation, dimensionality reduction, and estimation modules to specifically handle high dimensional image data efficiently. In general, the proposed measure of spuriousness is interesting.

### Strengths
The proposed methods are novel and the experiments are extensive.

### Weaknesses
The writing in some places is a bit unclear and some implementation details are lacking.

In the proposed autoencoder-based explainability framework, it seems that we need to select a non-negative constant $\gamma$ in dimensionality reduction phase, the readers may want to know how to select the value of $\gamma$. It will be helpful if the authors can give some guidance about the selection of $\gamma$.

In this paper, the authors propose a novel metric of spuriousness, then how can we identify one feature as a spurious one? It seems that we need the threshold?

It seems that there is a typo in "a the" in line 266.

In line 182, what is "Z_3 \bigoplus N$?

### Questions
1, In the proposed autoencoder-based explainability framework, it seems that we need to select a non-negative constant $\gamma$ in dimensionality reduction phase, the readers may want to know how to select the value of $\gamma$. It will be helpful if the authors can give some guidance about the selection of $\gamma$.

2, In this paper, the authors propose a novel metric of spuriousness, then how can we identify one feature as a spurious one? It seems that we need the threshold?

3, It seems that there is a typo in "a the" in line 266.

4, In line 182, what is "Z_3 \bigoplus N$?

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
1

### Summary
The framework builds on a foundation in information theory known as Partial Information Decomposition (PID) to break down the total information about the target variable into four distinct, non-negative components: unique information (within both core and spurious features), redundant information, and synergistic information. Using this decomposition, we introduce a novel metric for assessing the spuriousness of a dataset, guiding models to prioritize spurious features over core features.

### Strengths
this paper is based on a sound foundation: abstract / line 96 - line 125
the provided experimental evaluation doesn't include the statistical ratios (mean + std)

### Weaknesses
poor writing quality

this paper is based on a sound foundation: abstract / line 96 - line 125
the provided experimental evaluation doesn't include the statistical ratios (mean + std)

### Questions
-

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
4

### Summary
This work focuses on the problem of spurious correlation in the data-driven models. It leverages the partial information decomposition (PID) to decompose the total information into four quantities such as the unique information of core and spurious features, the redundant information that is shared by two features, and the synergistic information that arises due to the collaboration of the two features. Based on this decomposition, the authors propose a framework called Spurious Disentangler to empirically evaluate the “spuriousness” of image data.

### Strengths
1. The paper focuses on an important task that evaluates the degree of “spuriousness” of a dataset.
2. The idea of decomposing the total information into the aforementioned four values to study the spurious correlation problem is very interesting.
3. The paper is well-written and easy to follow.

### Weaknesses
1. My main concern is the contribution and practicality of the proposed method. Although the idea of using information theory to quantify spuriousness is interesting, the actual use case of the proposed framework is limited and not properly discussed. Most results only show that the framework “is consistent with existing knowledge” (e.g. Theorem 1, experimental observations).

2. The proposed framework, “spuriousness disentangler”, relies heavily on segmentations. This greatly reduces its application scenarios. Datasets where spurious and core features can be explicitly separated as object & background are limited.

3. The requirement of the existence of a pre-trained semantic segmentation model is problematic. This is equivalent to requiring a much larger and more general dataset or a much more powerful model where the spurious correlation problems are already mitigated to a good extent. Such a “Deus Ex Machina” approach is questionable in practice.

4. The experiment section lacks insights and does not highlight the contribution of the proposed method.
    - The experiments are repeated on four datasets. However, the observations are all descriptive yet the contribution and the superiority of the proposed method are limited. For example, in L427-L429, the authors conclude from Fig. 7 that $M_{sp}$ is a good measure because it is consistent with worst-group accuracy. This claim treats worst-group accuracy as the standard for evaluating “spuriousness”. The contribution of PID is completely missing here. 
    - The qualitative visualization of Figure 8 is only one sample. In L430, it is concluded from Figure 8 that “when the dataset is balanced or mixed background, the model emphasizes \textbf{more} on the core features (the red regions)”. This justification is insufficient. To justify that the model focuses “more” on the core feature. A score such as the IoU should be computed over the entire dataset to support this claim.


[Minor]:

1. L76, L78: “We first” appears twice.
2. L82-L83: The meaning of $A$ is not specified in $\mathrm{Syn}(Y:A,B)$. Is it supposed to be $F$? The definitions of $A$ and $F$ overlap throughout the manuscript and create unnecessary difficulty for the audience. The authors may consider unifying them for a clearer presentation.
3. In L147-148, $\mathcal{X}$ isn’t defined above.
4. In Figure 5, the location of the text “Encoder”, and “Decoder” and the curly brackets are misplaced.
5. The spacing after Figure 8 is completely missing.
6. It’s better to add captions for the subfigures in Figure 8 to indicate the five variants.

### Questions
1. Regarding the main concern, can the authors elaborate more on the use case of the framework where it is a better choice than existing measures such as worst-group accuracy?
2. In L53, the authors mentioned, “this notion of spuriousness in any given dataset has classically lacked a formal definition. To address this gap,…”. There are similar works discussing the quantification of spuriousness. e.g. [1,2]. Can the authors elaborate more on how the contribution of this work differs from this existing work? 
3. Is it possible to generalize the proposed “spuriousness disentangler” framework to datasets where the segmentation of two features is infeasible? For example, in tabular data, the spurious features can be sensitive attributes such as gender, race, etc. These features cannot be segmented. 
4. In counterexample 1, the authors refer to canonical example 1 and claim that this scenario should be considered as having “no spuriousness”. However, in canonical example 1, since $B = Y+N_B$, $F = Y+N_F$ with i.i.d. noise $N_B, N_F$, the spurious feature $B$ is equally connected to the label $Y$ compared with the core feature. Shouldn’t this be the “most spurious” scenario?


[Reference]

[1] Ye, H., Zou, J., & Zhang, L. (2023, April). Freeze then train: Towards provable representation learning under spurious correlations and feature noise. In *International Conference on Artificial Intelligence and Statistics* (pp. 8968-8990). PMLR.

[2] Wang, Y., & Wang, X. (2024, April). On the Effect of Key Factors in Spurious Correlation: A theoretical Perspective. In *International Conference on Artificial Intelligence and Statistics* (pp. 3745-3753). PMLR.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper introduces a novel framework called spurious disentangler that uses Partial Information Decomposition (PID) to analyze and quantify spurious correlations in datasets. The authors propose a new measure $M_{sp}$ that assesses how likely a dataset will lead models to rely on spurious features over core features, implementing this through a three-module system of segmentation, dimensionality reduction, and PID estimation. Through experiments on multiple datasets, they demonstrate a consistent negative correlation between their spuriousness measure and model generalization metrics.

### Strengths
1. This paper clearly explains why simpler measures are insufficient and develops a novel spuriousness measure through examples and counterexamples. 

2. This paper proposes a novel and complete framework called spuriousness disentangler for handling high-dimensional image data.

3. This paper provides extensive experimental results. It tests on multiple benchmark datasets, examines different types of sampling biases, and provides Grad-CAM visualizations. The experimental results well support their claims.

4. I think this research is of great significance. It can help identify problematic datasets before expensive model training.

### Weaknesses
1. This works requires manual identification of core and spurious features, which significantly limits its applicability since this might requires human-expert knowledge.

2. This paper focuses on the image classification task, it might be better if the authors can validate their framework on some NLP tasks.

### Questions
N/A

### Soundness
3

### Presentation
3

### Contribution
3
