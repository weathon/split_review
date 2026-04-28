# Learning a Compact, Parcel-independent Representation of the fMRI Functional Connectivity

- Decision: Reject
- Avg Score: 5.25
- Scores: 8, 5, 3, 5

## Abstract
Functional connectivity in functional magnetic resonance imaging (fMRI) data is often calculated at the level of area parcels. Given the data's low-dimensional nature, we posit a substantial degree of redundancy in these representations. Moreover, establishing correspondence across different individuals poses a significant challenge in that framework. We hypothesize that learning a compact representation of the functional connectivity data without losing the essential structure of the original data is possible. Our analysis, based on various performance benchmarks, indicates that the pre-computed mapping to low-dimensional latent space learned from the functional connectivity of one dataset generalizes well to another with both linear and non-linear autoencoder-based methods. Notably, the latent space learned using a variational autoencoder represents the data more effectively than linear methods at lower dimensions (2 dimensions). However, at higher dimensions (32 dimensions), the differences between linear and nonlinear dimensionality reduction methods diminish, rendering the performance comparable to the parcel space representation with 333 dimensions. Our findings highlight the potential of employing an established transformation to obtain a low-dimensional latent representation in future functional connectivity research, thereby solving the correspondence problem across parcel definitions, promoting reproducibility, and supporting open science objectives.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
In this work, the authors present an approach for learning a compact representation of functional connectivity data which generalize across different parcellations. The authors utilize a convolutional variational auto-encoder (VAE) and assess the quality of embeddings compared compact representations across multiple data sets.

### Strengths
The paper is well-written and fairly clear, and the approach seems novel as far as I have found.

Despite some missing pieces such as cross-validation results and error bars, the greatest strength of this work is in the extensive experimentation and results, which include multiple types of validation including reconstruction errors, distribution of canonical networks, and inter and intra-subject varaibility. The results in this study are quite convincing, and the method seems sound given its simplicity. The authors take pains to provide sufficient details for replicability in terms of model architecture and optimization, and a significant amount of work is included in the appendix which elaborates on the results and justifies hyper-parameter discussions. 

I want to take the simplicity of this approach as a strength rather than a weakness as well. I find that simple approaches are refreshing and if they outperform state of the art, should be widely adopted. That said, as I elaborate on in the weaknesses section, convolutional VAEs are a fairly old model and comparisons ought to be made with more novel methods such as Transformer-based architectures (such as Brain LM [1] perhaps), or generative adversarial networks (GANs) [2]. That said, the model convincingly outperforms the linear methods used as baselines in this work.

[1] Ortega Caro, Josue, et al. "BrainLM: A foundation model for brain activity recordings." bioRxiv (2023): 2023-09.

[2] Goodfellow, Ian, et al. "Generative adversarial networks." Communications of the ACM 63.11 (2020): 139-144.

### Weaknesses
While the simplicity of the model could be a strength, more work is needed to justify why a convolutional VAE would outperform other nonlinear reconstruction methods which exist in the literature. The most obvious omission is that the authors ought to compare against a traditional convolutional auto-encoder in order to justify why the variational model should be used in favor of a non-variational approach. As I've mentioned above, more novel reconstruction methods such as GANs and Transformer-based architecture ought also to be considered. The performance above linear reconstruction methods is convincing; however, multiple nonlinear reconstruction methods exist and have been applied to functional connectivity before [3,4,5]. This omission by itself puts this below the acceptance threshold for me, and unless the authors can provide a substantial rebuttal which includes comparisons, I would encourage them to resubmit this work at a later date given more substantive comparisons to modern architectures.

Furthermore, it seems the authors have not performed any cross-validation or multiple model training (across different random initializations) in order to reduce the variance from individual runs of the model. It is standard practice to perform a k-fold cross validation and provide error bars across folds in order to assure that model improvements do not amount to a particularly good subset of data or model initialization. This omission is more glaring than the previous one and puts it below a marginal reject to a full reject for me. If the authors can provide k-fold cross validation results in their revision, I will consider improving my score to a marginal reject; however, I think this work would benefit from a substantial revision and resubmission at a later date.

Finally, I think this work would benefit from training on a larger cohort of data, such as the UKBiobank [6] which contains several thousand participants. This alone does not lower the score for me; however, I will point out that the data sets in this study are quite small and finding a larger cohort of data would substantially improve the results here.

### Questions
1) how does the convolutional VAE compare with other nonlinear (deep-learning based) reconstruction methods? For example GANs or transformer-based architectures?

2) how does the performance of the model vary across folds in the data or across multiple model initializations?

### Soundness
3

### Presentation
4

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
The approach explores a beta-VAE for the compression of functional neuroimaging data by use of a spherical projection of the cortical surface evenly sampled to form an image that is used by a standard CNN based encoder-decoder variational autoencoder framework with a Gaussian prior as distribution of the variational bottleneck. The image used as input is derived from a seed map defining the Pearson correlation from the seed region to all other regions. The approach is contrasted toICA and PCA and performance quantified in terms of reconstruction ability from the compressed representation, silhouette index to quantify separation of networks in terms of predefined functional regions, as well as ratio of intra to intersubject variability as a proxy of reliability (i.e. measurements of same subject should have similar embeddings as opposed to the embeddings of different subjects) considering data from the human connectome project (HCP).

### Strengths
The paper is very well written and clear in its presentation.

The experimentation is carefully executed and includes quite a bit of additional investigations also in the supplementary. The evaluation criteria are sound (but could be strengthened, see weaknesses).

The use of seed based maps are interesting and can potentially have merits in general providing robust representations of functional neuroimaging data.

### Weaknesses
The approach is not contrasted any conventional modeling of the same data.

The approach is rather straightforward using a conventional \beta-VAE methodologically and the key contribution here is the use of seed maps rather than operating on the raw spatio-temporal data.

The approach is using qualitative evaluation approaches, i.e. quantitatively evaluating reconstruction, homogeneity by SI and same subject invariance when compared to different subjects are interesting metrics, but not necessarily of strong neuroscientific impact. I.e. a poor model focusing on noisy signals may have high subject consistency as noise/bias may be subject specific, produce high degree of homogeneity and lend itself well reconstructed as such noise confounders may be prominent as fMRI generally suffers from poor SNRs. As such, the methodology is not compared to ground truth information of neuroscientific interest such as recovery of task responses in task data, ability to predict properties of the individuals such as age, gender and cognitive capabilities etc (and why I deem the results qualitative). Such data is available from the HCP cohort and would strengthen the study to include and see what has been learned in regards to neuro- and cognitive-science relevant aspects.

The results are not so convincing. It seems simple methods such as ICA and PCA when applied with larger dimensions provide better reconstruction quality than the beta-VAE as indicated by the results of Figure 3. I find this somewhat surprising as I would expect the beta-VAE to be able through its non-linear modeling to efficiently compress the signal characteristics of the seed maps. This would be good to further elaborate upon as it then becomes unclear why to use advanced modeling approaches as opposed to very simple procedures such as ICA and PCA.

I understand that given the metrics and the uniqueness of considering seed-derived maps there are no natural alternative modeling procedures to consider. However, I would have liked to see conventional PCA and ICA compression on the time series and their reconstructions of seeds to further understand if this type of information cannot already be reproduced in such conventional neuroimaging analyses. 

Also, I think the paper would substantially improve to consider prediction of external information such as demography and cognitive abilities available in the HCP cohort to ground the methodology’s utility more quantitatively in terms of such ground truth information available for the individuals. It would in this context also be possible to understand and compare the proposed seed-based beta-VAE compressions utility when compared to standard neuroimaging compression methodologies operating directly on the spatio-temporal data for which there is a large literature using various approaches to predict aspects of the individuals of neuroscientific interest.

### Questions
How would PCA and ICA compare when applied to the spatio-temporal data as opposed to seed maps, i.e. filtering the data and reconstruction seed based maps from the filtered representations?

Why is \beta-VAE inferior in reconstructing the seed maps when using more dimensions when compared to ICA and PCA, and how would you generally tune for \beta in the \beta-VAE?

Why does ICA and PCA differ when they are reconstructing the same subspaces – this is unclear to me, please clarify, i.e. ICA is typically just a rotation of the corresponding PCA space – I believe I am missing an understanding on how these two approaches in this context become different.

Can you evaluate performance on information available at the subject level such as demography and cognitive capabilities in the HCP cohort based on the compressed representation?

- and how would such analysis compare to current SOTA supervised and representation learning approaches applied to fMRI in such tasks?

### Soundness
3

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
This paper is based on the hypothesis that ‘it is possible to learn a compact representation of functional connectivity data to enhance computational efficiency without compromising the essential structure of the original data’. This is achieved by projecting high-dimensional fMRI data onto a common low-dimensional latent space through a variational autoencoder, the study aims to reduce redundancy and improve cross-individual comparability, especially when different parcellation schemes are used. Using different performance metrics, the study explores how well key features in the original connectome are preserved across various dimensionality reduction methods and dimensions. The findings highlight that a variational autoencoder performs better than linear methods at lower dimensions and suggest that low-dimensional representations can enhance reproducibility and support open science.

### Strengths
1. The main motivation of this study was clearly explained. This study is based on the hypothesis that ‘it is possible to learn a compact representation of functional connectivity data to enhance computational efficiency without compromising the essential structure of the original data’. It is reasonable in the neuroscience field.
2. The proposed framework and geometric reformatting were clearly explained. The author applies the VAE framework to extract the low-dimensional representation of the reformatting image.

### Weaknesses
1. Although the proposed framework and geometric reformatting were clearly explained, however, this proposed framework lacks innovation, as the use of VAEs in neuroimaging is already well-established.
2. Dimensionality reduction and data compression to improve cross-individual comparability and computational efficiency are common strategies in many studies. 
3. From my point of view, the use of an autoencoder like VAE inherently involves a tradeoff between interpretability and data embedding. While the VAE effectively embeds high-dimensional data into a compact latent space, the representation in a new state space lacks intuitive interpretability. How about the comparison of other dimensional reduction methods, that directly extract the spatial or temporal modes in the original state space?

### Questions
1. What unique advantages does this framework offer in terms of cross-individual comparability and computational efficiency over other commonly used dimensionality reduction techniques, like PCA or ICA?
2. It is a tradeoff between interpretability and data compactness. In the past 2-6 years, it has been a popular topic in neuroscience that extracts harmonic modes/representations from structural networks or functional networks.
3. Typically, the estimation of functional connectivity might lose temporal information of neural data, how about the direct embedding of temporal signal in the proposed framework?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors train a variational autoencoder (VAE) to transform functional connectome seed maps into compressed latent representations that retain discriminatory power between individuals. Their hypothesis is that this approach improves on the standard practice of aggregating functional data into brain parcels which might leave room for further compression, while also collapsing meaningful vertex-level information. The authors conduct experiments that compute reconstruction accuracy,  and separation of subjects, comparing their VAE encoding to PCA, ICA, and a full parcellation encoding. They find that their approach separates subjects better than PCA and ICA, and clusters brain regions similarly to a established brain parcellations.

### Strengths
The goal of this work, dimensionality reduction and representation learning for functional connectomes, is a clear and a potentially impactful goal since functional surface maps are very high dimensional (tens of thousands of nodes). They also evaluate a variety of properties that would be desirable for feature learning including subject separation, agreement with existing parcellations, and reconstruction accuracy. Their method of latent feature embedding has an advantage over methods like t-SNE in that they can decode latent features into fMRI data. Their method is better than PCA and ICA at reconstruction accuracy and subject separation at 2 dimensions. The writing is generally clear and organized.

### Weaknesses
My largest concern is the significance of the contribution of this work. This paper cites a body of work by Kim et al. which also uses variational autoencoders to encode fMRI data with the same goals of reconstruction accuracy, and subject separation. In fact, figure 1 here is the same as Kim et al., 2021, just with a different seed map. Kim et al., 2021 also compares VAEs to PCA and ICA, further minimizing the novelty of this paper.

The authors cite computational complexity as a central motivation for the work. However, standard parcellations only use a couple hundred nodes, and datasets have around a hundred subjects. I am not convinced by their argument that computational complexity is a significant problem at this scale. After all, they cite a community detection algorithm which works on graphs over 1000x larger (Soman and Narang, 2011). While their method indeed is lower dimensional than parcellations with hundreds of areas, I would want to see complexity or runtime analysis if they claim that their method offers significant computational savings. 

Minor presentation comments on Figure 3:
- I think the colormap for correlations is a bit unclear since some similar colors are in fact far away from each other (e.g. light/dark blue, yellow and light green). I suggest considering alternative "diverging" color maps.
- Given that there isn't much discussion of matching subjects across method, I suggest not using line plots in panels B-D and instead using a Strip plot, or box-and-whisker plots, or bar plots. I think those do a better job depicting differences.

### Questions
- Does figure 3 only show results for the test set? 
- Are there other nonlinear feature learning methods that you can compare your method to? You rule-out t-SNE because the inverse mapping doesn't exist, but your comparisons (PCA, ICA) are both linear methods.

### Soundness
3

### Presentation
2

### Contribution
1
