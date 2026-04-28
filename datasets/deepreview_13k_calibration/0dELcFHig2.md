# Multi-modal brain encoding models for multi-modal stimuli

- Decision: Accept
- Avg Score: 6.67
- Scores: 8, 6, 6

## Abstract
Despite participants engaging in unimodal stimuli, such as watching images or silent videos, recent work has demonstrated that multi-modal Transformer models can predict visual brain activity impressively well, even with incongruent modality representations. This raises the question of how accurately these multi-modal models can predict brain activity when participants are engaged in multi-modal stimuli. As these models grow increasingly popular, their use in studying neural activity provides insights into how our brains respond to such multi-modal naturalistic stimuli, i.e., where it separates and integrates information across modalities through a hierarchy of early sensory regions to higher cognition (language regions). We investigate this question by using multiple unimodal and two types of multi-modal models—cross-modal and jointly pretrained—to determine which type of models is more relevant to fMRI brain activity when participants are engaged in watching movies (videos with audio). We observe that both types of multi-modal models show improved alignment in several language and visual regions. This study also helps in identifying which brain regions process unimodal versus multi-modal information. We further investigate the contribution of each modality to multi-modal alignment by carefully removing unimodal features one by one from multi-modal representations, and find that there is additional information beyond the unimodal embeddings that is processed in the visual and language regions. Based on this investigation, we find that while for cross-modal models, their brain alignment is partially attributed to the video modality; for jointly pretrained models, it is partially attributed to both the video and audio modalities. These findings serve as strong motivation for the neuro-science community to investigate the interpretability of these models for deepening our understanding of multi-modal information processing in brain.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
- Existing work uses unimodal models to identify language and vision processing pathways in the brain. This paper studies multimodal processing in the brain. Multimodal networks are aligned to the brain, and regions with better alignment are identified as the sites of multimodal processing. To verify that the alignment is actually due to multimodality, unimodal influence is removed from multimodal representations by subtracting out the multimodal target, as predicted by the unimodal input, from the multimodal features.

### Strengths
- This work is novel in that it is the first to use fMRI. But other works also take similar approaches to identifying multimodal processing (see weaknesses).
- Findings of the difference between cross-modal and jointly-trained models with respect to regions is novel
- These findings have neuroscientific significance
- Appropriate random baselines are used to give context to alignment numbers is given

### Weaknesses
 - Relationship with previous work [1] and similar concurrent work [2,3] that uses multimodal models to probe for multimodal processing in the brain should be discussed. [1] studies cross-modal and jointly trained networks and uses a naturalistic multi-modal stimuli.
- The random baseline described in 6.1 is good to make sure that the trained model weights matter. To better get a sense of whether the alignment actually reflects processing in the brain, another good sanity check would be to run a permutation test in which you keep the trained weights, but give the movie stimulus inputs to the model in scrambled order. This would give a floor for the scale of alignments that we see in subsequent results.

## Small things
- Line 276 typo: wmploy -> employ

### Questions
- For the procedure described in the Figure 1b caption on removing unimodal influence: why subtract out the unimodal contribution? Why not learn a regression directly from the unimodal contribution itself, i.e., the predictions of $r$?
- Can it be said that the IB-audio and IB-video unimodal representations described on lines 223-224 are not truly unimodal, since they are extracted from a model that was trained with multimodal inputs? Then, they reflect correspondences between language and vision.
- Figure 3 second row, middle two columns: Why does the green bar not have $\wedge *$ for SV? It seems significantly higher than both light green bars. Why does the green bar have $\wedge *$ for MT? It only seems significantly higher than on light green bar.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper compares different multimodal AI models to human brain responses while participants view audiovisual movies. They compare two different multimodal models, one cross-modal model that learns separate visual/audio embeddings and projects them into a shared representational space, and one jointly pretrained multimodal model, and three unimodal (vision or speech) models. The results show that in most brain regions multimodal training improves encoding model performance of voxel activity, particularly compared to unimodal speech models. The authors do additional residual analysis to understand the unique contribution of multimodal models (over unimodal models) to brain predictivity.

Overall, this is an interesting approach and the paper has many strengths. The link between results and overall conclusions was not always clear. In particular, the small number of highly varied models makes it difficult to draw strong conclusions about parallels between multimodal processing in the models and brains. Finally, there were several clarification/presentation questions.

### Strengths
There are many interesting and novel aspects to this paper. First, while there have been extensive encoding model studies on visual or audio stimuli, few have looked at model comparison to multimodal movies. The comparison of audiovisual models to this data is particularly novel. Further the comparison of different types of multimodal models is interesting (though it is difficult to draw strong conclusions about what their comparison tells you about multimodal processing in the brain, see below), and particularly the attempts to quantify what additional explanatory power a multimodal model has over unimodal models. The encoding analyses were also robust, particularly the cross-movie train/test splits.

### Weaknesses
The biggest issues stem from the comparison of the performance of a relatively small number of models that differ along many factors. This limitation makes it difficult to attribute any model differences to multimodality or different cross-modal training schemes, as the model architecture and training sets vary from model to model. Specifically, the models vary in terms of their input modalities (some are unimodal, some are multimodal), their architectures (e.g., joint vs. cross-modal), and their training objectives and datasets. This makes it challenging to isolate the specific contribution of multimodality to the observed brain encoding performance. For instance, a jointly trained model might perform better not because of its joint training, but because of a more effective architecture or a larger training dataset.

The fMRI dataset uses a small-n, data-rich design, which is good, but given this, it would help to see the results at the individual subjects’ level (in the appendix). On bar plots, it would be nice to plot each of the six subjects as a point overlaid on the average bar (rather than error bars which can obscure differences across the small number of subjects).

The residual analyses and results are somewhat confusing. The residual correlation with unimodal features was 0.56, which is still quite high. Given this, it is not clear that unimodal information was removed from multimodal models. Alternatively, the authors could do the residual analysis on the brain instead of the models (i.e., fit a model with both unimodal and cross modal and predict with just cross modal). Relatedly they could calculate the product measure or unique variance explained by multimodal models above unimodal models from this joint model.

Overall, the language and visual region responses look largely the same in most analyses. There are some quantitative/statistical differences, but the pattern is extremely similar. The authors should address this.

Perhaps related to the above point, all regions of interest are defined anatomically, but there is a fair amount of subject-wise variability in the anatomy of high-level functional regions, such as language. The authors should address this limitation.

Acronyms and plots were difficult to follow. Would help to spell out throughout vision versus lang regions for example, and clarify the legend in figure 4 (e.g., it was not clear on first read that “-“ indicates “minus”).

Figure 5 is difficult to read and interpret. In terms of clarification, the authors should specify hemispheres/views (it looks like a lateral view on top, medial on bottom, but I’m not certain). The results look extremely noisy and seem to show random patterns, with as much red as blue. Blue are areas the unimodal models perform better? How should that be interpreted? The legend says the colorbar indicates “percentage increase/decrease. Does this mean 0.5% or 50%? If the former, these are very tiny differences, which perhaps explains the above confusion, but I believe makes it difficult to draw any strong conclusions about these results.

I had questions about two of the conclusions listed in the discussion. I was unsure what the second part of conclusion 2 (“This variance can be partially attributed to the removal of video features alone, rather than auditory features.”) meant. I am also unconvinced of conclusion #4 given the overall similarity between language and visual brain regions described above.

Typos:
- Line 224: “audo” --> “audio”
- Line 276: “wmploy” --> “employ”

### Questions
It would help to have additional methodological details in some sections:
-	Was cross-subject prediction generated by using all of the predictor subjects voxels, to predict the target subject’s voxel-wise responses?
-	What are the six different modalities in the image-bind modality? I thought it was an audio-visual model (which I would consider two modalities)
-	The layer-wise predictions for models are shown in the appendix, but do the main text figures use all layers or best layer? If the latter, how is this layer selected.
-	Are the whole brain results averaged across all cortical voxels? Or only those with above-threshold cross-subject prediction? Or some other criteria?

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
4

### Summary
The authors aim to address whether there is a difference in brain-alignment based on whether multimodal models had cross-modality pretraining (separate encoders for two modalities) or joint pretraining (shared encoder across modalities). They compare one model of each type to video and speech models and evaluate the prediction in a large-scale open access movie dataset. Using residual analyses, they investigate whether there are multi-modal representations in visual and language regions of the brain.

### Strengths
For the most part, the authors use standard and well validated methods to answer their question. I particularly like the approach of evaluating the performance on entire held-out videos and using the residual analysis to investing multi-modal effects above and beyond unimodal effects.

### Weaknesses
The authors only evaluate two multi-modal models and a small number of unimodal models. However, the chosen models differ on many factors (e.g. architecture, training data) in addition to the input modality and as a result, it is premature to draw conclusions about semantic representations in the brain that may be attributable to any of these factors. To my mind, there are two ways to mitigate this concern: 1) controlled model training and evaluation so that only one factor varies at a time, or 2) testing many different models of a given class such that even across significant model variations there is a robust effect of modality regardless of particular model factors. I think that this is a serious concern because not  all prior work has found that multi-modal models are more brain aligned. In controlled comparisons between visual models with the same architecture and training data, there was no performance increase as a result of contrastive image-language training (Conwell et al., 2023). These authors suggest that the higher alignment of CLIP relative to unimodal models in other work may be training set size.

A minor weakness of the paper is that the authors use custom, non-standard acronyms and names for brain regions (e.g., scene visual area, SV, and object visual processing region, OV). It is confusing as a reader, but more critically, it difficult to understand what has been found for particular regions across the field, making the status of the literature more tenuous. I would suggest that the authors adopt standard acronyms throughout (e.g., PPA instead of SV).

Although the paper overall is fairly clear, section 6.3 and the corresponding figures (4, 9, and 10) are difficult to follow. I welcome clarification because, outside of a few lines in the discussion, I am having a hard time understanding which regions do show a multi-modal effect. Additionally, I think that the authors should emphasize whether they uncover expected unimodal effects in primary sensory cortices. In particular, we would expect that EVC would be predicted by visual models with no additional multi-modal contribution and similarly in AC but for auditory models. I am having trouble determining whether that is the case from the figures, but if it is not the case, it would lend more weight to my major concern about differences between models beyond modality.

### Questions
Why did the authors choose to use parametric statistics? To my knowledge non-parametric statistics are more common in NeuroAI to estimate a baseline performance rather than assuming one. 

Are the brains on the bottom in Figure 5 the medial view? It is difficult to see why there are four brains in each box. Outside of labeling, showing the sulci on the inflated brains would help to orient the reader to what is being shown.

### Soundness
3

### Presentation
3

### Contribution
3
