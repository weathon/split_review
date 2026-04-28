# DRL: Decomposed Representation Learning for Tabular Anomaly Detection

- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 5, 6, 6

## Abstract
Anomaly detection, indicating to identify the anomalies that significantly deviate from the majority normal instances of data, has been an important role in machine learning and related applications. Despite the significant success achieved in anomaly detection on image and text data, the accurate Tabular Anomaly Detection (TAD) has still been hindered due to the lack of clear prior semantic information in the tabular data. Most state-of-the-art TAD studies are along the line of reconstruction, which first reconstruct training data and then use reconstruction errors to decide anomalies; however, reconstruction on training data can still hardly distinguish anomalies due to the data entanglement in their representations. To address this problem, in this paper, we propose a novel approach Decomposed Representation Learning (DRL), to re-map data into a tailor-designed constrained space, in order to capture the underlying shared patterns of normal samples and differ anomalous patterns for TAD.
Specifically, we enforce the representation of each normal sample in the latent space to be decomposed into a weighted linear combination of randomly generated orthogonal basis vectors, where these basis vectors are both data-free and training-free.
Furthermore, we enhance the discriminative capability between normal and anomalous patterns in the latent space by introducing a novel constraint that amplifies the discrepancy between these two categories, supported by theoretical analysis. 
Finally, extensive experiments on 40 tabular datasets and 16 competing tabular anomaly detection algorithms show that our method achieves state-of-the-art performance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces Decomposed Representation Learning (DRL), a novel approach for addressing the entanglement issue in representation learning within reconstruction-based Tabular Anomaly Detection (TAD). DRL mitigates this problem by employing orthogonal bases in a training-free, data-free manner to remove latent space dependencies, implemented through the Gram-Schmidt process for Decomposition Loss. It also maximizes variance in the weights of normal latent bases, enhancing discrepancy with abnormal latents as supported by Proposition 1, and reconstructs the original input from latent representations to prevent task-irrelevant features. The paper validates DRL’s effectiveness with extensive experiments across 40 ADBench datasets and 15 baseline models, achieving state-of-the-art performance through detailed ablation studies and T-SNE visualizations.

### Strengths
1. The paper effectively addresses limitations in reconstruction-based methods by comparing DRL with recent state-of-the-art models such as NPT-AD and MCM, demonstrating its superior performance. This is a novel contribution to the field of tabular anomaly detection.
2. Theoretical support for the separation loss, specifically Proposition 1, provides a solid basis for the model's structure and validates its design choices.
3. Extensive experimentation across 40 ADBench datasets and 15 baseline models showcases the robustness and effectiveness of the DRL method, and ablation studies and T-SNE visualizations add valuable insights into its workings.

### Weaknesses
1. Lack of KNN Baseline Comparison: While the paper includes comparisons with several state-of-the-art methods, there is no performance comparison with KNN, a model often effective in tabular data tasks. Including KNN as a baseline would enhance the experimental section by providing insights into how DRL performs relative to a widely recognized tabular anomaly detection approach. I recommend the authors consider adding KNN results and explain how DRL’s design is particularly beneficial over KNN in anomaly detection.

2. Loose Bound in Separation Loss Calculation: In calculating the separation loss lower bound, the authors remove all terms involving squared expectations, which might lead to a relatively loose bound. It would be helpful if the authors could explore alternative derivations for this bound that might be tighter or justify the sufficiency of the current approach. Additionally, it would be useful to discuss how this looseness could potentially impact performance or theoretical guarantees of the DRL method.

3. Clarity in Section 2 and Lack of MCM Limitations: Some portions of the paper, particularly Section 2 (Preliminaries), could benefit from clearer explanations. For instance, a more detailed explanation of theta would aid readers in following the theoretical framework more easily. Additionally, while the authors discuss the disadvantages of NPT-AD, the limitations of MCM are not mentioned. Including a brief discussion on MCM's limitations would help balance the comparison and highlight DRL's unique advantages more clearly.

### Questions
1. What would happen if the basis vectors were set as unit vectors, for example, [1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1] ?
2. The paper states that cosine distance improves performance as L2 distance leads to optimization issues. Could the authors explore how performance might change with L1 distance, or clarify why cosine distance was chosen specifically over both L2 and L1?
3. Proposition 1 proposes that maximizing variance of weights attached to basis vectors in normal latents enhances separation from abnormal latents. Are there trade-offs in terms of model stability or convergence when applying this approach?
4. How sensitive is DRL’s performance to hyperparameter choices, such as the number of orthogonal basis vectors or weights in loss terms? Are there specific recommendations or guidelines for tuning these parameters across different types of tabular datasets?
5. What are the main limitations of DRL as identified by the authors?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a new method for tabular anomaly detection under the one-class setting via learning decomposed representations of normal samples. The key idea is to decompose normal representations into a weighted linear combination of data-free and training-free orthogonal basis vectors. Furthermore, a separation loss, supported by theoretical analysis, is designed to enhance model’s discriminative ability between normal and anomaly samples. Extensive experiments conducted on 40 datasets demonstrate the effectiveness of the proposed method.

### Strengths
1.	This paper is well-written and easy to read.
2.	The proposed decomposed representation learning method sounds reasonable for tabular anomaly detection.
3.	The authors provide a theoretical analysis to support the proposed separation loss.
4.	The comparative experiments conducted on 40 tabular datasets are quite extensive.

### Weaknesses
1.	I appreciate that this paper highlights the issue of normal and anomaly samples being entangled in raw space. However, the argument that normal and anomaly latent representations are entangled in reconstruction-based methods, leading to diminished discriminative power, seems somewhat unfounded. Since these models are biased towards reconstructing normal samples, it is expected that representations of the two classes would be entangled in latent space. Based on this, the motivation for learning decomposed normal representations is unclear to me. What are the specific advantages of learning decomposed representations for tabular anomaly detection? Specifically, how does this approach guarantee that the decomposed representations of normal data will be more separable from anomalies than the latent representations of reconstruction-based methods, given that the latter are already optimized to capture normal patterns?
2.	The visualized t-SNE results demonstrate that the proposed method can extract non-entangled normal and anomaly representations. However, the authors may need to explain the rationale for leveraging orthogonal basis vectors to learn such representations. Could vectors with other relational properties achieve the same effect? What are the specific advantages of using orthogonal basis vectors for decomposed representation learning? For example, would using non-orthogonal but linearly independent basis vectors lead to similar or different results, and why?
3.	I appreciate the authors’ efforts in conducting extensive ablation studies. However, what is the performance when using cosine distance for the decomposition loss? Additionally, how does the model perform if only alignment losses are used as anomaly scores during inference? It would be helpful to see a direct comparison of these alternatives.
4.	The sensitivity analysis of vector number is good. I wonder if the vector number is somehow related to the feature number of input data. Is there a principled way to determine the optimal number of basis vectors, or is it purely a hyperparameter tuning exercise?
5.	I appreciate the theoretical support for the separation loss. However, as the separation loss is applied between samples, is it sensitive to the batch size? Additionally, if the training normal samples are highly similar to each other, does this loss face convergence challenges? Could this lead to overfitting on a specific subset of normal samples?
6.	Can the proposed method be applied to other data types (e.g., image or time series data)? In other words, why is the proposed method specifically useful for tabular data. What inherent properties of tabular data make this approach particularly suitable, and how might it need to be adapted for other data modalities?
7.	This is a minor point, but the paper lacks a discussion on limitations and future work.

### Questions
see the weakness part.

### Soundness
2

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
This paper introduces Decomposed Representation Learning (DRL), a new framework for anomaly detection in tabular data. This approach aims to overcome the limitations of traditional reconstruction-based methods, which often struggle with data entanglement, especially in tabular settings where feature heterogeneity can obscure the separation between normal and anomalous samples. DRL remaps data into a latent space, enforcing each normal sample's representation as a linear combination of orthogonal basis vectors that are both data-free and training-free. Furthermore, DRL introduces a constraint to amplify discrepancies between normal and anomalous patterns in the latent space.

### Strengths
1. This paper is well-motivated, and the technical details are illustrated properly.
2. The proposed method is supported by a theoretical analysis of the constraint to maximize the discrepancy between normal and anomalous samples.
3. The authors conducted comprehensive experiments to demonstrate the effectiveness of the proposed DRL.

### Weaknesses
1. DRL relies on decomposing the representation of normal samples into linear combinations of orthogonal basis vectors, and this decomposition assumes that normal samples are well described by fixed orthogonal bases in the potential space. However, the true distribution of normal samples in complex, high-dimensional feature spaces may not be captured simply by a small number of basis vectors. The reviewer is concerned about whether the decomposition may not be sufficient to completely express the normal sample features if the distribution of high-dimensional data is complex or contains nonlinear feature associations, which in turn leads to inaccurate anomaly detection.

2.  The decomposition and separation constraints of this method require the computation of unique weight vectors for each sample, which may incur significant computational costs on high-dimensional data and large-scale datasets. Also, the introduction of the weight learner increases the model complexity, especially when the number of orthogonal basis vectors is large. The reviewer is concerned about the efficiency of the proposed method. Although authors have shown the runtime in A.5, more comparison with other baselines in terms of runtime will improve the persuasiveness of this aspect.

3. The reproducibility of this work is limited. The reviewer could not validate this work as the source code was not released.

### Questions
Please refer to weakness.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The authors present a Novel reconstruction-based outlier detection (R-OD) method for tabular data called DRL. DRL's novelty among other R-OD methods is that it focuses on representing the data $\mathbf{x} \in \mathbb{R}^d$ as a linear combination of a randomly selected basis $\mathcal{B}$ of $\mathbb{R}^D$, with $d>D$. To this end, the network learns an encoder $f_{\theta_f}$ from $\mathbb{R}^d$ to $\mathbb{R}^D$, a decoder $g_{\theta_g}$ and a weight learning function $\phi_{\theta_\phi}$ that is in charge of learning such weight representation. The authors also include a novel loss function to train DRL, focusing on 3 different aspects. (i) It learns an embedding function $f$ that agrees with a linear combination representation of the embedding $\phi$  in the $L_{decomposition}$ loss, (ii) it focuses on separating the normal samples between themselves in the $L_\text{separation}$ loss and (iii) it reconstructs the embedding by $f$ with $g$ in the $L_{aligment}$ loss. Furthermore, the authors include a theoretical result that motivates the use of $L_\text{separation}$, by proving that an increase in the total $L_2$ distances of the representations of inlier data during training, leads to a greater expected distance between an inlier and an outlier (Proposition 1). 

Additionally, the authors include an extensive list of real-world experiments in the main text, with 40 real-world datasets and 15 relevant competitors. In particular, the authors tested DRL's One-class classification (OCC) performance, provided an ablation study, and studied different types of distances and base selection strategies. The appendix includes further experiments with different types of synthetic outliers, sensibility to the parameters, robustness study and computational cost analysis among others.

### Strengths
1. The paper has a nice flow in the presentation.
2. The idea of using a linear combination of a projected random basis to represent the data is an interesting idea with big explainability potential.
3. The paper is well motivated, as the problem of OCC in tabular data is an important task in ML.
4. There is a large list of different experiments.
5. The authors use a statistical comparison test to provide a statistical significance analysis of the main experimental results.
6. The authors include the pseudo-code of the method in the appendix.

### Weaknesses
 There is not enough evidence to support the claims that the authors make in the paper, both theoretically and experimentally. 
Particularly:

### Theory
T.1. The authors claim that DRL " (...) assumes that the representation of each normal sample in the latent space can be effectively modeled as a mixture of fixed basis vectors with specific mixture proportions" (L160-161). This assumption is central to the method's idea, and it goes unsupported both in theory (no theoretical example of data behaving as such) and practice (no example proving that given such a theoretical example, one could extract exactly such representation). As an example, consider the manifold learning (ManL) literature. Assuming that data comes from a lower dimensional manifold $\mathcal{M}$ is a big assumption, however, there are examples of such data being generated by synthetic means, and also examples of ManL methods properly learning the representations ---see figure 5 in [Meila & Zhang]. 

T.2. The authors further claim that Proposition 1 proves that the outliers are going to be far away from the inliers (i.e., separated). While technically true on average, Proposition 1 does not "(...) amplify the discrepancy between the two (inlier and outlier) patterns" L224. What proposition 1 shows is that, if one increases the variance of the learned weights $w_i$, the process of measuring the distance between an inlier's representation and an outlier's representation will be, on average, higher. This, however, does not imply that, necessarily, you will increase the distance of the outliers with the total set of inliers. For example, one could obtain a representation that places a large set of outliers in the centroid of the inliers, with the remaining inliers being sparse around the centroid.

T.3. DRL's performance is not explained in the theoretical derivations. The authors focus on proving how the representation that they learn can "separate" outlier from inlier, but it is not clear how an increase in distance can affect the final scoring function (they use $L_\text{decomposition}$ as a final score). Particularly, it is not clear to me how it can affect the encoder $f$.


### Experiments
While this paper contains a large collection of experiments, they do not focus on verifying the theoretical claims of the method.

E.1. The authors include experiments to try to prove the claim mentioned in weakness number T.2 in Figure 1. However, out of the total list of datasets (40) and competitors (15), they only use 2 datasets and 1 competitor without any clear reason. This does not contain sufficient evidence that the outliers and the inliers can be separated by Proposition 1. 

E.2. Weakness T.1 addresses that the random basis reconstruction assumption has no example in theory. In practice, this assumption seems to not be properly explored. The authors include an ablation study in Table 2 where they compare different versions (including one employing only the basis reconstruction assumption) of DRL. However, they only included 7 out of the 40 datasets introduced earlier. 

Additionally, the authors include in Figure 5 a comparison between different variants of DRL. Particularly, variant B "applies the decomposition loss to observations, assuming that each normal sample can be decomposed into a set of orthogonal basis vectors (...)" L472-473. This variant ranked third to last among 8 different versions of the method. Furthermore, it is not possible to compare this performance to the other detectors as the authors do not say which methods they use, and only report an average PR-AUC. 

E.3. At the time of this review, there is no code available for DRL, making it not reproducible.

### Questions
I kindly ask the authors to address the following questions & concerns in order to improve the manuscript:

1. The performance of the method is not properly verified (see T.1,T.2,T.3). It will greatly improve the paper to address, particularly T.1 and T.2. For T.2, I suggest to prove that $\|w_a - \mu_{w_i} \|$ has a lower bound greater than the increase in $\|w_i\|$, where $\mu_{w_i}$ is the centroid of the inlier's representation in basis $\mathcal{B}$.

2. The authors should consider addressing concern E.1, to at least experimentally verify T.2. Is there any particular reason why not all datasets and competitors were considered (at the very least as an image in the appendix)?

3. The authors should consider rewriting section 5.2. It is unclear to me the difference between the ablation study presented in the section and the *Comparison of DRL and Variants in the Observation Space*. For instance, why are they separate sections if they seem to try to study the same thing? Why is there no reference to the datasets used in *Comparison of DRL and Variants in the Observation Space*, and why only the average PRAUC and not the full table of results? Why did the authors consider only 7 datasets out of the total 40 in the ablation study?

4. The author should strongly consider releasing the code for the method. Reproducibility is a crucial part of the scientific process, and without the code, this paper cannot be reproduced. Is there any strong reason as to why the code was not available at the time of the review?

I will consider changing my rating upon successfully addressing these questions during the rebuttal. 



### Additional remarks that did not influence the score
A couple of additional remarks that might improve the manuscript:

R1. P-values are not a scalar metric. This means that a difference between .20 to .90 is the same as a difference between .0501 and .0502 (when selecting a critical value of 0.05) [Lavine]. Thus, authors should consider removing Figure 4 for something more meaningful (see [Campos et al] results section).

R2. The Wilcoxon signed-rank test is a single-population comparison test. This means that it is strictly designed to work in single comparisons. The setting presented in the experiments is a multiple comparison setting, thus a multiple comparison test should be used in this regard (see, for example, the Conover-Iman test [Conover]). 


### References 

[Melia & Zhang] Meilă, M., & Zhang, H. (2023). Manifold learning: what, how, and why. https://arxiv.org/abs/2311.03757

[Lavine] M. Lavine, “Introduction to Statistical Thought” 

[Campos et al] Campos, G.O., Zimek, A., Sander, J. et al. On the evaluation of unsupervised outlier detection: measures, datasets, and an empirical study. Data Min Knowl Disc 30, 891–927 (2016). https://doi.org/10.1007/s10618-015-0444-8

[Conover] WJ Conover (1979), Multiple-Comparisons Procedures.



### Update

After the discussion with the authors, I have decided to increase my score from 3 to 6. See the comments below for more information.

### Soundness
3

### Presentation
3

### Contribution
2
