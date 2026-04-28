# Representational Similarity via Interpretable Visual Concepts

- Decision: Accept
- Avg Score: 6.80
- Scores: 6, 8, 6, 8, 6

## Abstract
How do two deep neural networks differ in how they arrive at a decision? Measuring deep network similarity has been a long-standing open question. Most existing metrics provide a single number to measure the similarity of two networks at a given layer, but give no insight into what makes them similar or dissimilar. We introduce an interpretable representational similarity method (RSVC) to compare two networks. We use RSVC to discover shared and unique visual concepts between two models. We show that some aspects of model differences can be attributed to unique concepts discovered by one model that are not well represented in the other. Finally, we conduct extensive evaluations across different vision model architectures and training protocols to demonstrate its effectiveness.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies the representational similarity between different vision networks. The main novelty is to provide insight into not just _how_ similar are two networks but in _what_ ways are they similar. This is achieved through a dictionary learning method that approximates the activations at some layer of a network as a nonnegative combination of "visual concepts", which are just a set of activation vectors.  Then the similarity between two networks is measured as the similarity of the visual concepts they each represent, either through a correlation-based metric or via regression from one set of concepts onto the other. The paper finds that there is some degree of similarity between the visual concepts in different networks, that there are some important concepts that differ between different networks, and that layers near the input or near the output of the network are most alike, while middle layers differ.

### Strengths
I like the motivation of this paper. It is convincing that 1) understanding _what_ differs between different neural representations is important,  and 2) prior work has mostly overlooked this question (although a few papers that were not cited do address this question; see weaknesses).

Other strengths include:
* The writing is mostly clear.
* The methods appear to be reasonable and I don't see obvious errors.
* The paper delivers a tool that could increase interpretability of representational differences, because the differences can be visualized. 
* Several of the findings are interesting; I was especially intrigued by 1) the method can identify low similarity, high importance concepts, 2) middle layers show the greatest differences between different networks.

### Weaknesses
The main premise of this paper is to go beyond prior work on representational similarity, which only gave summary numerical scores, and instead show "_what_ visual concepts make two models similar or dissimilar." This is a great question, but the paper falls short of fully delivering on it.

There is only one figure, Fig 2, in the main paper that directly addresses this central question, comparing two models and showing how they differ in terms of the visual concepts they learn. The appendix has more results along these lines but I'm still not sure what insights to take away from these results. The visual concepts themselves are not clearly defined or easily interpretable, making it difficult to understand the nature of the differences. For example, in Fig 2, it's unclear why certain patches are grouped together and what specific visual features they represent. The lack of clear semantic meaning for the discovered concepts limits the interpretability of the results.

I take it to be that the contribution is not to *show* what is different between different nets but rather to provide a *tool* that is in principle capable of showing what is different. This is a valid contribution but I think the paper would nonetheless be stronger if the tool were used to provide new insights into the model differences.

The other results (Figs 3, 4, and 5) are interesting but fall back into the category of summary statistics that don't go deep into what makes two models similar or dissimilar. Instead we only learn that 1) there are important differences (intriguing! but what are they), and 2) the differences live primarily on the middle layers of networks (although from Fig 5 it looks like the increase in similarity at the deepest layers is quite minor indeed). While these results are interesting, they don't provide a detailed understanding of the specific visual concepts that differ between the models. The paper does not demonstrate how the tool can be used to gain actionable insights into model behavior or performance.

If this paper is indeed meant to just introduce a tool, rather than a discovery, then the reader needs to be convinced that the tool is valuable. I'm mostly convinced that the tool is valid and in some ways new. But I'm not sure what to do with it, nor if the community would be able to use this tool to make new discoveries. This isn't an absolutely critical weakness -- time can tell if it is useful -- but I would rather have seen more validation of the usefulness of the tool in this paper. It would be wonderful if the paper could use the tool to tell us something about neural representations we didn't know before, like, say, that resnets focus more on background elements than transformers, or, ideally, something deeper than that. To make this super compelling, I would like a demonstration that this new way of identifying differences has advantages over other ways of identifying representational differences, in a head to head comparison. But I'm not sure how to do that.

There are also a few overlooked prior works I think are worth discussing (or, ideally, comparing to):

1. "Rosetta Neurons: Mining the Common Units in a Model Zoo," Amil Dravid, Yossi Gandelsman, Alexei A. Efros, Assaf Shocher, ICCV 2023

-- This paper also identifies visual concepts that are shared between different models. In their case, the concepts are coded by neurons, across different models, that are correlated in terms of their responses to the same set of image patches.

2. "Understanding the Role of Individual Units in a Deep Neural Network," David Bau, Jun-Yan Zhu, Hendrik Strobelt, Agata Lapedrizad, Bolei Zhouf, and Antonio Torralba, PNAS 2020

-- This paper also provides a tool for identifying which visual concepts are encoded by different networks, and compares two networks in this way.

3. "Exploring Neural Networks with Activation Atlases," Shan Carter, Zan Armstrong, Ludwig Schubert, Ian Johnson, Chris Olah, Distill, 2019

-- This paper introduces "activation atlases", which are yet another way of identifying visual concepts learned by different networks. This work does not use these atlases to compare different models, which differs from the current paper's goals.

There is also a recent line of work on interpretability via sparse autoencoders that may be worth looking into, e.g., https://transformer-circuits.pub/2024/scaling-monosemanticity/

### Questions
1. I didn't fully understand why use image patches rather than whole images. This could be motivated more clearly, or justified with an experiment comparing using patches vs whole images.
2. I would appreciate if the authors can address the missing reference I mentioned above. Why should a reader prefer your proposed method over these prior methods? What are the advantages and disadvantages of each approach, or are they not comparable?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces Representational Similarity via Visual Concepts (RSVC), a method to compare representations between neural networks by analyzing shared and unique visual concepts instead in pairs of pretrained models, with the goal of providing a better comparative breakdown of pairwise model similarities.
Conceptually, RSVC extends work by Fel et al. 2023a, b on a dictionary-based formulation of concept-based XAI, and introduces different mechanisms to study similarities between concept explanations of two different networks: (1) A correlational analysis of concept coefficients, and a (2) regression-based approach, in which a linear model is trained to predict concept assignments between models. These two concept similarity methods are then used in conjunction with a concept importance estimator and a concept-performance-dependence study to broadly understand the existence and prevalence of unique and shared concept pairs between models.
Experiments are conducted for RN18, RN50, ViT-S, ViT-L, MAE & DINO pretrained on ImageNet to showcase concept similarities between different model architectures and training paradigms.

### Strengths
In general, I find this paper to be sufficiently well written and structured; with the presentation and detailed image visualization and captions to be commendable: Figures and their captions can be read standalone and still convey key contributions; which significantly enhances readability. Moreover, the proposed method is described and visualized in a way that makes it much easier to grasp all relevant key aspects.

At the same time, the extension of works by Fel et al. seems sensible, and to the best of my knowledge, the use of a dictionary-based concept attribution method for __model similarity__ studies is novel.

Moreover, I very much appreciate the experimental breadth the authors followed to test the different potential usecases of RSVC.

### Weaknesses
Unfortunately, I currently have some more pressing issues and questions which stop me from recommending acceptance at this stage. Ordered by importance, these are:

---

__Lack of sanity checks and proof of concepts__.
Interpretability methods are strongly reliant on sanity checks (Adebayo et al. 2018, https://arxiv.org/abs/1810.03292, Boehle et al. 2022, https://arxiv.org/abs/2205.10268). The authors unfortunately directly apply their proposed methods on arbitrary model pairings, without first firmly establishing the validity of the proposed approach. To do so, I believe that at the very least, the following steps need to be included:

(1) Establishing a baseline. This means that using two models for which concept similarities are highly likely or even guaranteed, and applying both MMCS and RSVC (regression-based) to understand how visualizations in Fig. 3 changes. As it is now, it is much more difficult to relate computed values and their respective significance. A baseline could e.g include the same model architecture trained on the same data ordering, but with small changes in the initialization; or a fixed initialization but changes in the data ordering.
(2) Studying variations away from the baseline above. By structurally varying the baseline (e.g. going to different augmentations, different data subsets, ...) understand how the proposed metric changes.
(3) More clearly establish what extracted concepts actually look like. The example in Fig. 1 with bird tail and sky background seems quite convincing, but then when looking at actual examples in Fig. 2, these become much less convincing: The net appears consistently in all scenarios (alongside arms and hands), and I find it difficult to see any consistency here.

Without establishing such baselines and sanity checks, it is very difficult to assign actual meanings to extract values.

---

__Conceptual / Architectural Inconsistencies__.
There are some elements in the proposed approach that currently do not make much sense to me, particularly:

* L171: "Each concept proposal is resized to the model’s input resolution and passed through the network." >>> Learned features are generally resolution-dependent unless speficially trained not to be. As such, the resulting extract concepts (from the resized image patches) hold much less meaning with respect to the actual network, no? I may not understand the setup sufficiently here, but resizing patches and using thereby derived U_i, W_i for concept comparisons does not make much sense to me. Why not just store the full activation output and break it down corresponding to the patch formulation?


* As the authors correctly state for the correlational setup described in 3.2.1, MCS does not accout for any confounding elements. But it is not completely clear to me how RSVC avoid the issue of confounders? If I have a confounding element in e.g. M2 which would produce similar concept coefficient than the actual extracted concept would, this would still be an issue even when using the learned linear map, right?

* For the replacement tests: What are the guarantees that U_2-1 operates in the same basis as U_1, such that a direct replacement is well defined? The learned maps in Eq. 4 are trained without any guarantees that the bases between both models overlap, no?

---

__Some less important notes that are not majorly impacting my decision, but are useful to address:__

* L133-135: "While our work also aims to compare two models in an interpretable manner, our approach does not make use of surrogate models and instead uses the activations of the original model itself." But isn't the projection matrix another learned linear model? I.e. isn't RSVC also using surrogate models?

* The use of a linear predictor (or one with directly assignable importance values) to test matching up to permutation, scale and shift has been studied in-depth in disentangled representation learning, e.g. in Locatello et al. 2018 (https://arxiv.org/abs/1811.12359), Eastwood et al. 2018 (https://openreview.net/forum?id=By-7dz-AZ), Locatello et al. 2019 (https://jmlr.org/papers/volume21/19-976/19-976.pdf), Eastwood et al. 2022 (https://arxiv.org/abs/2210.00364) or Roth et al. 2023 (https://openreview.net/pdf/f1f46edad3b1c36e9c46c00c16e8592cfd1e4df6.pdf). These may provide a useful resource for experimental ablation studies, and should be discussed to augment the short reference to disentangled representation learning in the related works section.

* Section 3.3 is fairly redundant, and should either be excluded entirely, or in my eyes more crucially, described in much more detail, as the use of concept importance is quite prevalent throughout the paper.

### Questions
See weaknesses. I'm happy to raise my score if the authors can address my first two points, and during the rebuttal can provide baseline studies and sanity checks; as I believe the paper to be an overall meaningful contribution if these points can be incorporated.

### Soundness
2

### Presentation
4

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
The paper presents an approach for measuring the similarity between representations of two models using "concepts". It quantifies the similarity between the internal concepts of the models, extracted with a concept-based xAI method.

### Strengths
1. The paper is well-written, easy to follow, and defines well the different stages of the method and the evaluation.

2. The idea of the paper is novel - instead of comparing functional similarity or direct similarity in representations, it uses a decomposition into "concepts" and compares the similarity between concepts. Instead of providing one similarity measure, this paper also demonstrates visually what are the concepts that make two models similar or dissimilar. 

3. The paper provides a comprehensive study of the relations between concept similarity and concept importance to address the main possible limitation of using concepts - their non-straight-forward connection to the computation in the model.

### Weaknesses
1. This approach might be sensitive to the concept extraction method. The extraction of $U_i$ and $W_i$ provide very different results for different concept dictionary sizes $k$ and if some L1 sparsity regularization is applied. Specifically, the choice of $k$ impacts the granularity of the concepts, with larger $k$ potentially leading to more fragmented and less interpretable concepts, while smaller $k$ might miss important distinctions. Furthermore, the L1 regularization strength directly controls the sparsity of the concept vectors, which can affect the similarity scores. A more thorough investigation is needed to understand how these parameters affect the resulting concept similarity measures. A comparison of different approaches for concept extraction and ablation of their hyper-parameters can provide better insights into the approach sensitivity.

2. Computational cost - this process requires computing representations on many images, extracting representations from each layer, training linear models, and comparing correlations. The computational cost of this process is not discussed, and the trade-offs between the number of images that are needed for each of the steps are also missing. For instance, the number of images needed to reliably extract concepts and train the linear mapping should be investigated, as this will directly impact the computational burden and the quality of the results. The paper should also discuss the scaling of the method with respect to model size and dataset size.

3. Usability - The current approach for coming up with meaningful observations about the representations requires a human in the loop, who goes over all the concepts and investigates the similar and dissimilar concepts (as shown in Figure 2). This manual inspection is time-consuming and subjective, making it difficult to scale the method to larger models or datasets. The paper should explore methods to automate or semi-automate the interpretation of the concept similarity results. Can it be automated somehow?

4. Missing related work:

Dravid et al., Rosetta neurons: Mining the common units in a model zoo, ICCV 2023

Rombach et al., Network-to-network translation with conditional invertible neural networks, NeurIPS 2020

Typo in 250: We use it *to* compute...

### Questions
Why does the approach use per-class concepts? Different classes of images can have shared computation and shared intermediate concepts? Using per-class concepts might result in missing shared concepts, and functional similarity.  

The current model assumes implicitly that the models $M_1$ and $M_2$ are classifiers (the matching is applied per class). What modifications are needed to make it work on other types of models (e.g. representation learners/segmenters)? 

What data is used to compute the linear mapping in line 282? Is it part of $I^c$?

### Soundness
2

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
The paper presents a method for comparing the representations of two neural networks using visual concepts. Concepts are extracted by factorising the matrix of activations corresponding to a set of images. The authors present two methods for the comparison of visual concepts, one based on correlations between the coefficient matrices, and another using regression, using one set of concept coefficients to predict the other and vice-versa. Also proposed is a method for measuring the dissimilarity of representations, where one network can contain a concept deemed important to classification, which is not present in the other network. These methods are evaluated on a variety of networks, investigating the relationship between concept importance and concept similarity.

### Strengths
- The topic is of great interest. Providing interpretable model comparisons that go beyond model performance will be useful to practitioners.
- The method goes beyond just measuring similarity, but provides interpretation for both similar and dissimilar concepts, something that is often overlooked in model comparison.
- The example in Figure 2 is very convincing.
- The proposed method for measuring similarity and dissimilarity is very intuitive.

### Weaknesses
 - Some implementation details are missing (clarified in the questions section)
- Brainscore does link representation similarity scores to functional differences; models are evaluated using similarity in representations but also comparisons in the output. In places it is described as comparing representations between two neural networks, which is not true. It is between the activations in a network and  macaque brain activations.
- Colour bars in Figure 3 and 4 would make the figure slightly clearer.
- In Eq. 5, mentioning why L1 regularisation is used would make it clear to the reader.
- The introduction is quite brief, and fails to motivate the problem addressed. It could benefit from a small discussion on why interpretability is important and why concepts are more useful than say saliency maps or superpixels (LIME).

### Questions
-  How many images are used to construct  $\mathcal{I}_{1,2}^c$, and is it a requirement for the models to overlap slightly so that $\mathcal{I}^c$ has enough samples? How consistent are the concepts extracted with less samples? The images used to measure similarity seem very important for the ability to interpret results, as the images need to represent the concepts important for classification.
- Does the size of the patch effect the concepts found? And what patch size was used in the paper.
- Along the same lines, what is the split of $\mathcal{I}^c$ between test and train for the regression task?
- Do the authors have any intuition for using this method to compare models that do not necessary predict the same number of classes?
- In Figure 2, could you look at the regression weights learned, and see that the concept for the RN50 would be predicted by two separate concepts in the RN18? This would substantiate the claim in line 465, that possible the RN18 contains separate concepts for hands and net, as these concepts would have large contribution when predicting the 'hands/arms near a volleyball/net' concept in RN50.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
### Post rebuttal

---------------

The rebuttal clarifies most of my concerns. I think this work may provide some direction on how to compare models in terms of model explanations.

For the final version, I urge the authors to:

1. Point to some of the GPT based model explanations to Fig 2 and Section 3.4.
2. Clean the plots in Fig 3 and Fig 4 to remove the majority of less important points to make the trends more visible.
3. Add to the main paper, that they used a separate validation set to tune lambda from Eq. 4

---------

This work aims to analyze similarity between two trained networks in terms of what visual concepts they encode. It builds on top of prior work (Fel et al 2023) which provides a formulation to extract “concepts” from learned network. Namely, the activations of a network $A  \in R^{N \times D} $ are decomposed to form $U \in R^{N \times k}$ (concept coefficient matrix)  and $W  \in R^{k \times D}$ (concept basis). Given $U_1$, $R_1$, $U_2$ and $R_2$ of two different models, they propose “correlation” and “regression” to measure concept similarity. Correlation (MMCS) (loosely) measures the correlation between $U_1$ and $U_2$, while regression (CMCS) measures how well $U_2$ can be decoded from $U_1$ using a linear model (and vice versa).

The paper performs three experiments: comparing concept importance vs CMCS, how changes in concept similarity affect final outputs and layer-wise conceptual similarity using MMCS.

### Strengths
The paper explores a new area which is representational similarity using visual concepts. Finding interpretable ways on how different networks are similar may offer valuable insights to the community.

### Weaknesses
On reading the title, I was expecting insights that show what sort of visual concepts are learned by a model, and what is different as scale, data and architecture is varied. But I found these insights not present in the paper. The paper performs three sets of experiments but its a bit unclear why these are interesting to study. For example:

* In Figure 5, the authors investigate their proposed metrics layer-wise across various models. However, what additional insights does this offer over (Raghu et al 2021)?
* In Figure 4, high importance features show high correlation between L2 and pearson coefficients, But this is also a bit obvious.

I also found the presentation sometimes difficult to follow. See below for detailed feedback.

* The abstract says that this work presents a practical tool to discover the cause of model failures but this discussion is missing in the main text.
* L167 - L169. Next, as visual features are highly correlated, patches from each image are sampled to form a set X c 1 of “concept proposal” images. More detail is required on how these patches are extracted from the image? Are they just randomly sampled, if yes then how many? And is each patch resized independently to the original image resolution?
* L202 - L203. It’s unclear why there is a tradeoff between computational cost and error between these two techniques.
* L201 - 211. $R^{\rho}$ and $R^{S}$ are mentioned, so which one does R employ?
* L214: Eq 2) takes the max across all columns for each row and vice-versa. IIUC, this is because there is no direct correspondence between the columns in U1 and the columns in U2. That is the first concept of U1 may represent something completely different from the first column U2. So to measure similarity, one matches each column of U1 to the column that has maximum correlation in U2. Even though this may be obvious to the authors, it will be nice if some discussion is added.
* L297: Eq1) How is $\lambda$ tuned?
* L348 - L349 For our exploration with DINO and MAE, we fine-tune the models on NABirds (Van Horn et al., 2015). Why do this?
* Fig 2) plots the correlation plots between $U_1 \in R ^{N \times K}$ and $U_{1\rightarrow 2}$. Are both matrices flattened to 1D to plot the correlation plot. What is the value of n and k?
* Fig 2) In both orange and light blue grids, there are grid-like textures and hand and arms at net. So, I find the descriptions and explanation unconvincing 
* Fig 3). The paper introduces low, medium CI and concept similarities without any precise definitions. One could for example precisely define the top 5% percentile of concept importance as high and so on.
* Fig 3) How many points are in each subplot of Fig 3. Some amount of detail atleast for one subplot may be required.
* Fig 3) The paper says that “model differences are largely driven by medium similarity, medium importance concepts”. I found this conclusion hard to believe for the y-axis, the center of each heatmap seems to be close to 0.0 For the x-axis, it is indeed centered at medium importance.
* Fig 4) The presentation will be clearer if separate plots are presented for high importance and low importance plots.
* So as $\Delta$Pearson becomes closer to zero, the cross-model concepts are more similar to same-model concepts. This implies that the L2-distance (and KL should reduce) when $\Delta$Pearson becomes closer to zero. However, this trend is not esadily deducible from Fig.4. Can the authors please add more clarification?

### Questions
* The abstract says that this work presents a practical tool to discover the cause of model failures but this discussion is missing in the main text.
* L167 - L169. Next, as visual features are highly correlated, patches from each image are sampled to form a set X c 1 of “concept proposal” images. More detail is required on how these patches are extracted from the image? Are they just randomly sampled, if yes then how many? And is each patch resized independently to the original image resolution?
* L202 - L203. It’s unclear why there is a tradeoff between computational cost and error between these two techniques.
* L201 - 211. $R^{\rho}$ and $R^{S}$ are mentioned, so which one does R employ?
* L214: Eq 2) takes the max across all columns for each row and vice-versa. IIUC, this is because there is no direct correspondence between the columns in U1 and the columns in U2. That is the first concept of U1 may represent something completely different from the first column U2. So to measure similarity, one matches each column of U1 to the column that has maximum correlation in U2. Even though this may be obvious to the authors, it will be nice if some discussion is added.
* L297: Eq1) How is $\lambda$ tuned?
* L348 - L349 For our exploration with DINO and MAE, we fine-tune the models on NABirds (Van Horn et al., 2015). Why do this?
* Fig 2) plots the correlation plots between $U_1 \in R ^{N \times K}$ and $U_{1\rightarrow 2}$. Are both matrices flattened to 1D to plot the correlation plot. What is the value of n and k?
* Fig 2) In both orange and light blue grids, there are grid-like textures and hand and arms at net. So, I find the descriptions and explanation unconvincing 
* Fig 3). The paper introduces low, medium CI and concept similarities without any precise definitions. One could for example precisely define the top 5% percentile of concept importance as high and so on.
* Fig 3) How many points are in each subplot of Fig 3. Some amount of detail atleast for one subplot may be required.
* Fig 3) The paper says that “model differences are largely driven by medium similarity, medium importance concepts”. I found this conclusion hard to believe for the y-axis, the center of each heatmap seems to be close to 0.0 For the x-axis, it is indeed centered at medium importance.
* Fig 4) The presentation will be clearer if separate plots are presented for high importance and low importance plots.

### Soundness
2

### Presentation
2

### Contribution
2
