# Towards scientific discovery with dictionary learning: Extracting biological concepts from microscopy foundation models

- Decision: Reject
- Avg Score: 5.60
- Scores: 8, 5, 5, 5, 5

## Abstract
Dictionary learning (DL) has emerged as a powerful interpretability tool for large language models. By extracting known concepts (e.g., Golden-Gate Bridge) from human-interpretable data (e.g., text), sparse DL can elucidate a model's inner workings. In this work, we ask if DL can also be used to discover *unknown* concepts from less human-interpretable scientific data (e.g., cell images), ultimately enabling modern approaches to scientific discovery. As a first step, we use DL algorithms to study microscopy foundation models trained on multi-cell image data, where little prior knowledge exists regarding which high-level concepts  should arise. We show that sparse dictionaries indeed extract biologically-meaningful concepts such as cell type and genetic perturbation type. We also propose a new DL algorithm, Iterative Codebook Feature Learning (ICFL), and combine it with a pre-processing step which uses PCA whitening from a control dataset. In our experiments, we demonstrate that both ICFL and PCA improve the selectivity or "monosemanticity" of extracted features compared to TopK sparse autoencoders.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors propose a Dictionary Learning method to discover unknown concepts from Foundation Models that have been pre-trained on image-based phenotypic screening data.  Specifically, the goal is to learn a new, sparse feature representation, such that individual features align with interpretable biological concepts.  To this end, they propose a new method called Iterative Codebook Feature Learning (ICFL) and benchmark it against a competitive approach: TopK Sparse Autoencoders (Topk SAE).  Their proposed method is closely related to orthogonal matching pursuit algorithm, and they demonstrate that it reduces the number of dead/unused features relative to TopK SAE on their dataset.

Using this method, the authors demonstrate that sparse dictionaries can extract biologically meaningful concepts such as cell type and functional genetic perturbations, and that ICFL features demonstrate higher selectivity for these concepts than TopK SAE.  They also demonstrate that PCA whitening has a significant impact on the selectivity of the learned features.  In addition, the paper shows qualitative examples of images that correspond to specific concepts, and provides possible interpretations by way of heat maps highlighting local correlation between the token map and feature direction.

### Strengths
The authors address a challenging and important problem in drug discovery, namely the lack of interpretability of learned features from large-scale phenotypic screens.  This is a particularly challenging problem, because it involves interpreting "black box" deep learning models in a domain where there are not clear examples of known concepts to draw upon.  By contrast, in natural images, objects such as cars and animals provide numerous intuitive visual concepts.  To address this challenge, the authors leverage 5 classification tasks with qualitatively different labels: (1) cell type, (2) experimental batch, and (3-5) genetic perturbations.  By evaluating the performance (eg, via linear probing) of their learned features on these tasks, they can ascribe some biological significance to the learned concepts.  Of particular relevance are features that align with the functional genetic perturbation labels.

The paper then proposes a novel method called Iterative Codebook Feature Learning (ICFL) to improve upon existing Dictionary Learning methods which often learn imbalanced features, where some features are unused (so called "dead latents"), and other features are over-used.  Based on the 5 tasks listed above, the paper evaluates the performance of ICFL and TopK SAE on linear probing.  In addition, they evaluate the selectivity of features learned from these two methods, demonstrating that ICFL both retains more information and has more selective features than TopK SAE.  They also observe that PCA whitening has a significant effect on the quality of learned features.  

Based on the above framework, the authors provide an analysis of the number of features that have selectivity above a threshold (0.1, 0.2 and 0.5) for their 5 different task labels.  Interestingly, while a large fraction of features have high selectivity for cell type (23 labels), very few features have selectivity for functional gene group (39 labels).  This highlights the remaining challenge of learning concepts that are specific to subtle genetic perturbations.

Overall, the application of dictionary learning to image-based phenotypic screening is a promising direction, and the paper includes multiple insightful analyses.  While there remains significant progress to be made towards extracting meaningful concepts from images of cells under genetic perturbation, the paper represents a significant and original contribution to this topic.

### Weaknesses
The paper proposes a new method for Dictionary Learning, called Iterative Codebook Feature Learning, specifically to address the challenge of inadvertently learning "dead latents" by existing methods.  Their method appears to very effectively achieve this goal (Table 1); however, this contribution would be more significant if the authors included an evaluation on additional datasets, such as those used in Gao et al.

In Figure 1, the authors provide multiple examples of images ranked by their alignment with different learned concepts.  However, it's difficult to conclude how distinct the learned concepts are.  For example, Features A, B and C (and potentially numerous other features) could all be influenced by the total cell count in the images.  In addition, Figure 2 d-f suggest that numerous different features have a similar correlation with labels such as Cell Type, Perturbation ID, and Functional Gene Group.

The authors provide a qualitative analysis of their method's ability to identify novel biological concepts in Figures 4 and 5.  For example, in Figure 4, they investigate a feature that is strongly correlated with gene knock outs from the adherens junctions pathway.  By visualizing  heat map of the inner product of individual tokens with the learned feature, they conclude that specific cells within each image have escaped the perturbation, exhibiting normal phenotypes, and correspondingly are not highlighted in the heat maps.  However, this qualitative analysis could inadvertently suffer from confirmation bias.  I suggest a more rigorous analysis, such as having a blinded expert identify cells that are not exhibiting an expected phenotype for a genetic perturbation.  This would produce a cell-level annotation of outlier cells, amongst other cells that are exhibiting the intended phenotype.  Based on this, it would be interesting to evaluate the correspondence of token-level heat maps with this annotation.

The clarity of Figure 2 could be improved.  Here are some suggestions:

1) In Fig 2a, tasks are listed by number ((1)-(5)); however this isn't clearly described in the figure caption.  I suggest either naming the tasks explicitly in Fig 2a, or including a reference in the figure caption.

2) There appears to be a typo in the legend for Fig 2a-c.  The dashed line is listed as "w/o pcaw" and there is a missing line for "w pca".


Additional minor edits:

1) Section 6.2: "...image taken form a subset of the public..." -> "...image taken from a subset of the public..."

### Questions
I was confused by the histograms in Figure 3 a-d.  In particular, for some genetic relationships (a,c) the result of paired genetic perturbations was to reduce the mean cosine similarity, yielding a negative value.  Is this expected for these specific gene pairs?  It would be helpful to include additional discussion on the expected cosine-similarity for each pairs of perturbations.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper presents a study of interpretability using sparse dictionary learning for large foundation models of microscopy images. An algorithm is proposed for iterative codebook feature learning (ICFL), which is used to learn a sparse feature space where individual features are presumably more interpretable. Similar methodologies have been used for exploring interpretation of language models, and the presented methodology is an extension for cellular images. The paper presents a quantitative evaluation of how certain known biological and experimental aspects of the images can be identified with the sparse representation, and them compares against manually engineered features. Finally, the paper presents a qualitative evaluation of what the meaning of certain features may be by selecting some which activate with genetic perturbations and channel specific activity.

### Strengths
* The presentation of a novel algorithm for learning sparse encodings of token representations. The algorithm could be used for other models and data modalities.
* A quantitative and qualitative evaluation of performance.
* A unique analysis for the specialized domain of cellular images and genetic perturbations.

### Weaknesses
1) Are the sparse features really interpretable? Sparse autoencoders emerged as a minimal transformation strategy for interpreting the activations of transformers, which are not directly associated with any semantic meaning. However, this paper does not present strong evidence that the sparse features can be more interpretable than the regular transformer activations for this application domain. There are two reasons for this A) the approach presented in the paper depends on additional token transformations, which makes the reader believe that the interpretation is not really associated to what the model encodes. B) The interpretability scores presented in the quantitative evaluation are based only on a few known labels. Are those labels all that can be interpreted in the models?
2) Aggregated token representations and weak supervision. There are several transformations applied to the tokens before dictionary learning, which obscures the claims made in the paper about interpreting the inner workings of the models. The fundamental question for interpretability is what is the model doing and how we can use that information to keep it under control? Discovering biases and understanding how they are encoded in the model is at the heart of these approaches, but in this paper, the model outputs are first aggregated and decorrelated with PCA whitening using labeled data to proceed with dictionary learning. This contradiction between the claims / motivation of the paper and the actual procedure followed for interpretation is confusing. This also suggests that the interpretation is performed at the level of one downstream task rather than at the level of model activations and inner workings.
3) Monsemanticity? The paper also claims that their approach finds directions that are monosemantic, but the results do not support such claims. The quantitative evaluation is focused on making sure that the learned sparse features capture as much signal as the original features. Monosemantic features would be able to classify these concepts with a single dimension, which is not what the evaluation presents. The results in Fig. 3 seem to indicate that there is still considerable entanglement between features.
4) Not reproducible research. As far as this reviewer can tell, the models and data to reproduce this research are not publicly available. The machine learning community strives for openness and reproducibility, exemplified by the open source, open review, and open access practices. It is a significant downside of this manuscript that the presented results cannot be independently verified.

### Questions
* What does it mean to have interpretable features? The paper makes the conclusion that the original token activations are not interpretable, and therefore additional feature transformations are needed. Is this an effect of the lack of a more generic interpretability score for this domain? What is the original model capturing that prevents interpretation without interventions?
* The qualitative evaluation depends on manual interpretation by experts. What would be a more scalable way to make interpretations of morphological variations of cells without having to resort to human annotations?
* To address point 1) and 2) above, how can the authors demonstrate that original features are not as interpretable as the sparse features? This is particularly important before and after the aggregations and transformations used to learn the sparse features. Is it the case that aggregated features after PCA are as interpretable as the sparse codes? What are we gaining in interpretability if these transformations disentangle their meaning from other variation? Please compare feature specificity and other metrics of the original and transformed token features to understand the utility of the proposed algorithm.
* To address point 1) above, what other information can be used to interpret features beyond classification tasks? Something more scalable that requires less manual intervention?
* To address point 3) above, are there any individual features that classify any of the concepts more accurately than random? What percent of the concepts and what percent of the sparse features can be connected in this way? This would clarify if the learned codes are really monosemantic or not. A comparison with original and transformed tokens would be necessary too.
* To address point 4) above, how can others reproduce the results of this research and use them as applications in future work? This research could be conducted entirely with publicly available data by training a community model, for instance. If the research reported in this paper cannot be verified, perhaps this is not scientific progress, but rather a commercial application, in which case other venues are more appropriate for dissemination than ICLR.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper focuses on sparse dictionary learning for unsupervised learning of concepts from microscopy images. The target vectors are embeddings from microscopy foundation models and the dictionary is overcomplete, intended for sparse combination of latent concepts to reconstruct the target embeddings. The proposed method ICFL closely resembles OMP for L0 sparse recovery. The authors perform in-depth analyses to demonstrate the strengths of their approach for microscopic images.

### Strengths
This is an interesting study where the authors combine classical signal processing idea of dictionary learning (from 2006 when K-SVD was first proposed) and recent foundation models for microscopy images. This shows that classical ideas can feed off from the latest advancements in deep learning to promote the interpretability of the results, which deep learning (despite all the recent saliency methods) clearly lacks. The authors perform several in-depth ablations, both quantitatively and qualitatively, to demonstrate that the learned latent concepts 1) do not lose the "downstream" performance, such as cell type classification and 2) also enable interpretability analysis of each learned concept.

### Weaknesses
While I believe the study is thorough as explained above, there are few concerns that I think are holding back the paper.

1. **Presentation** I think the authors are presenting the paper in very verbose manner, which made it confusing to get main messages from the paper. For instance, I am not sure if the "Superposition hypothesis" and "disentanglement and causal representation literature" were necessary to lay out the logic for the paper - The authors could have simply dived in to why dictionary learning is desirable. 

Also for explaining results, I sometimes found myself lost in why each of the experiment is important and how it ties to the central message of ICFL (e.g., Fig.2b, Fig.2C, Fig.3f, Fig.3g). Also the authors in the results section switch between different tasks (among the five tasks and experiments) without sufficiently explaining, and this made it hard to follow the paper. I would like the authors to really work on the clarify of the paper.

2. **Technical novelty** At the end of the day, ICFL is a variation of Orthogonal Matching Pursuit and also restricted to L0 recovery methods, which has been around since early 1990s. The added novelty could be that the target is an embedding vector, but this wouldn't really considered a technical novelty typically required for ICLR submissions. For ICFL to really be a great contribution, I think the algorithm should also be able to handle more-widely used L1 recovery methods, given plethora of works in this space (both in classical signal processing sense and more recent neural network sense, through unrolled networks for sparse recovery)

I also think for this to be considered as a robust concept recovery method, additional experiments are required for other variations of microscopy FMs as well. The authors restrict the analyses on MAE-pretrained ViTs, whereas if the authors also perform similar analyses on other types of SSL-pretrained ViTs for this domain, I think that would strengthen the argument that ICFL is robust.

3. **Lack of takeaway messages & Baselines** The authors largely compare ICFL against two major baselines. Top-K SAE and CellProfiler. It is great that it is performing better than Top-K SAE, which I consider a lower bound, but this doesn't seem to tell you much about the performance one would hope to reach for actual downstream tasks & Biomarker discovery research. The reason is that ICFL lags behind on almost all metrics behind the original embedding baseline and CellProfiler-derived baselines - As a reader/possible user of the algorithm, I find it less convincing to use ICFL, if it is always performing worse than simpler and older approaches.

I think the authors try to counterbalance by devoting lots of effort in to qualitative analysis part, but due to the presentation issues outline above, I found it less convincing. As an example of lack of takeaway messages, in Table 3, it's good that for lower threshold you get some degree of features with good selectivity, but what does that really mean in terms of using it for actual research? What does Cell Type 928 feature count with Threshold 0.1 mean in this context? How should a scientist interpret this?

4. **Minor points**
- Figure 3 caption. No description of (e), (f), (g) - I think b) c) were intended for that. 
- I am not sure what Pearson correlation of 0.71 is supposed to mean for CP and ICFL features. Doesn't this mean certain labels are just more likely to be activated than other labels? Not necessarily that ICFL is capable of identifying the features similar to CP.
- I think the authors need to experiment with different size of dictionary. Why 8,192 only?

### Questions
- In line 319, why use center crop, instead of the whole image?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a method for dictionary learning on microscopy images to extract concepts from the image data in an unsupervised fashion.  The proposed method, Iterative Codebook Feature Learning, is an alternative to TopK sparse auto-encoder, that uses an orthogonal matching pursuit approach, resulting in fewer unused/"dead" features.  Experimental results confirm that the learned representations with ICFL have fewer dead features relative to TopK, and improved selectivity with respect to labels from several classification tasks.  Some qualitative analysis is given of the learned features.

### Strengths
+ The paper studies an interesting and important domain, where the question of whether meaningful concepts can be extracted automatically from data has significance to biological science.

+ Empirical results are generally well-organized and support the claimed benefits of using ICFL over TopK, specifically with respect to improved selectivity scores and reconstruction quality.  Results also highlight the importance of PCA whitening as a pre-processing step.  Comparison is also given with handcrafted features, and the paper is clear on limitations/areas where current methods fall short of desired performance.

### Weaknesses
 - With respect to machine learning methodology, the technical novelty of the paper is somewhat limited.  The overall problem and approach follows TopK, except rather than optimizing the specific TopK formulation, an orthogonal matching pursuit approach is used instead. The core algorithmic contribution is essentially a substitution of optimization strategy, which raises questions about the fundamental advancement in representation learning.

- ICFL was shown to be superior to TopK on some quantitative measures, but these measures are proxies and not an end goal in themselves.  Qualitative results were only given for ICFL.  Was any qualitative analysis done on the TopK learned features?  Was it the case that those features were clearly sub-optimal to ICFL from a qualitative perspective?  Or were they also able to capture any concepts like the morphologies shown in Figure 1?

- The qualitative analysis gives a discussion and intuition for a small number of the learned features.  Was it the case that many of the learned features had this kind of interpretability as human-understandable concepts?  Or was this only true for the small subset shown?

- More generally, how do you see the results of this method being used in biological research?  Is the desired goal that by looking through the learned features, a researcher might find a single concept that captures something complex and unexpected, warranting further study?  I ask this in regard to the overall positioning and motivation of the paper as discussed in the related work.  For instance, from the perspective of biological research and understanding, why not instead take a CRL approach that directly tries to learn interpretable features/representation?  Or if certain tasks are of key importance, why not focus on learning concept vectors with respect to that task/class-labeled data.  It would be interesting to compare the proposed method with class-based concepts using something like Ghorbani et al Automatic Concept-based Explanations, for instance using the specific tasks already being considered in the paper.

### Questions
- ICFL was shown to be superior to TopK on some quantitative measures, but these measures are proxies and not an end goal in themselves.  Qualitative results were only given for ICFL.  Was any qualitative analysis done on the TopK learned features?  Was it the case that those features were clearly sub-optimal to ICFL from a qualitative perspective?  Or were they also able to capture any concepts like the morphologies shown in Figure 1?

- The qualitative analysis gives a discussion and intuition for a small number of the learned features.  Was it the case that many of the learned features had this kind of interpretability as human-understandable concepts?  Or was this only true for the small subset shown?

- More generally, how do you see the results of this method being used in biological research?  Is the desired goal that by looking through the learned features, a researcher might find a single concept that captures something complex and unexpected, warranting further study?  I ask this in regard to the overall positioning and motivation of the paper as discussed in the related work.  For instance, from the perspective of biological research and understanding, why not instead take a CRL approach that directly tries to learn interpretable features/representation?  Or if certain tasks are of key importance, why not focus on learning concept vectors with respect to that task/class-labeled data.  It would be interesting to compare the proposed method with class-based concepts using something like Ghorbani et al Automatic Concept-based Explanations, for instance using the specific tasks already being considered in the paper.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces an algorithm called Iterative Codebook Feature Learning (ICFL). The algorithm consists of a simple linear generator with an l2 reconstruction (as in standard l1 sparse coding) with sparsity being enforced with a topK  (instead of the typical l1) condition on the projections of the data to the decoding matrix columns. The optimal decoding weight matrix is identified with SGD. Once the optimal dictionary is identified the process is iterated with the residual of the image reconstruction for a fixed number of iterations (presumably sufficient to capture the entire structure of the data and set the residual to 0). The ICFL algoirthm is compared against a top-K sparse autoencoder from a recent publication. The comparison looks at the quality of reconstruction and the utility of the full range of dictionary elements suggesting that the ICFL  method yields improved performance. The algorithm is then applied to intermediate level representations from a large masked autoencoder that has been trained on microscopy images, it is described as a foundation model. The authors claim that this enables them to learn sparse features that have physical meaning from foundation models, enabling a new form of scientific discovery.

The sparse coding algorithm seems interesting. However, it seems to me that having a fixed number of iterations would lead to a lot of redundant computation, it would be interesting to see look at the decay of the norm of the residual after ever ICFL iteration. A termination condition based on the norm would seem more sensible to me.
Another interesting direction would be to look at multiresolution features, which are relevant to image structure, usually the iterative algorithms such as those proposed by Mallat & Zhang (1993) lead to features that lie in different parts of the frequency domain and using convolutional operators with dilations to capture structure at different iterations might lead to improved performance of the ICFL algorithm.
While the ICFL demonstrates an interesting approach I am not convinced that studying the internal representation of foundation model can lead to anything particularly meaningful. Why didn’t you work with the original data instead? How can you tell that your result is not a product of some odd averaging (or other form of merging/separation) of features?
I am not a microscopy expert so it is difficult to evaluate that aspect of the paper but I admit that the results seem convincing.
Overall the contribution seems novel and non-trivial, however, its future scientific significance appears to be vague to me at this point.

### Strengths
It is a non-trivial technical contribution. The paper appears to combine expertise from multiple areas including at least foundation models in microscopy, cellular microscopy, and sparse coding. There is a novel method of analysis of foundation models that might lead to a significant contribution to cellular microscopy.

### Weaknesses
The sparse coding algorithm seems interesting. However, it seems to me that having a fixed number of iterations would lead to a lot of redundant computation, it would be interesting to see look at the decay of the norm of the residual after ever ICFL iteration. A termination condition based on the norm would seem more sensible to me.
Another interesting direction would be to look at multiresolution features, which are relevant to image structure, usually the iterative algorithms such as those proposed by Mallat & Zhang (1993) lead to features that lie in different parts of the frequency domain and using convolutional operators with dilations to capture structure at different iterations might lead to improved performance of the ICFL algorithm.
While the ICFL demonstrates an interesting approach I am not convinced that studying the internal representation of foundation model can lead to anything particularly meaningful. Why didn’t you work with the original data instead? How can you tell that your result is not a product of some odd averaging (or other form of merging/separation) of features?
I am not a microscopy expert so it is difficult to evaluate that aspect of the paper but I admit that the results seem convincing.
Overall the contribution seems novel and non-trivial, however, its future scientific significance appears to be vague to me at this point.

### Questions
What features do you get when you apply ICFL directly on cellular microscopy images?
Can you provide a plot that demonstrates the decay of the norm of the image residual after successive ICFL iteration?
Can you elaborate on the significance of the obtained features? 
Why did the token heatmap specialise on the missing actin (line 426)?
Can you give more details on the foundation model (e.g. input, output)? 
What do you think your model can learn from a foundation model, something related to its input or its output, or both?

### Soundness
3

### Presentation
4

### Contribution
3
