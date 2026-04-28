# Finding Shared Decodable Concepts and their Negations in the Brain

- Decision: Accept
- Avg Score: 6.75
- Scores: 5, 6, 8, 8

## Abstract
Prior work has offered evidence for functional localization in the brain; different anatomical regions preferentially activate for certain types of visual input. For example, the fusiform face area preferentially activates for visual stimuli that include a face. However, the spectrum of visual semantics is extensive, and only a few semantically-tuned patches of cortex have so far been identified in the human brain. Using a multimodal (natural language and image) neural network architecture (CLIP, \cite{CLIP}, we train a highly accurate contrastive model that maps brain responses during naturalistic image viewing to CLIP embeddings. We then use a novel adaptation of the DBSCAN clustering algorithm to cluster the parameters of these participant-specific contrastive models. This reveals what we call Shared Decodable Concepts (SDCs): clusters in CLIP space that are decodable from common sets of voxels across multiple participants.

Examining the images most and least associated with each SDC cluster gives us additional insight into the semantic properties of each SDC.  We note SDCs for previously reported visual features (e.g. orientation tuning in early visual cortex) as well as visual semantic concepts such as faces, places and bodies. In cases where our method finds multiple clusters for a visuo-semantic concept, the least associated images allow us to dissociate between confounding factors.  For example, we discovered two clusters of food images, one driven by color, the other by shape. We also uncover previously unreported areas with visuo-semantic sensitivity such as regions of extrastriate body area (EBA) tuned for legs/hands and sensitivity to numerosity in right intraparietal sulcus, sensitivity associated with visual perspective (close/far) and more. Thus, our contrastive-learning methodology better characterizes new and existing visuo-semantic representations in the brain by leveraging multimodal neural network representations and a novel adaptation of clustering algorithms.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This study aims to identify brain areas that respond to specific visual concepts, aiming to expand our understanding of functional localization beyond known areas like the fusiform face area. Using a model based on CLIP embeddings, the authors map brain responses to clusters of shared visual concepts, called "Shared Decodable Concepts" (SDCs), across multiple participants. By applying a modified DBSCAN clustering algorithm, they reveal consistent brain regions linked to both previously known (e.g., faces, places) and novel visual concepts (e.g., specific body parts, numerosity, perspective). This method particularly allows data analysis within each participant’s unique brain structure, avoiding issues with traditional alignment methods.

### Strengths
- The discovered novel selectivities observed in the study are quite interesting and potentially good hypotheses for future brain imaging studies 
- The perspective that both active and suppressed neural responses are useful for identifying brain regions tied to distinct visual concepts is somewhat unique and not something I've seen in prior studies 
- This method circumvents the need to align subjects data, while still being able to extract shared representational structure across participants

### Weaknesses
 - More methodological details are needed. More motivation behind why DBSCAN clustering used over other clustering algorithms? How do the authors select the epsilon which ultimately determines the number of clusters? Specifically, what range of epsilon values were explored, and what criteria were used to determine the 'reasonable' range? The lack of a principled approach to selecting epsilon is a significant concern.
- The authors should acknowledge that there is a lot of human bias involved in interpreting the concepts based on the activated images. For e.g. in 4.1, the authors interpret the negative representative images to indicate images that lack clearly visible faces. However, many other interpretations are also consistent with these sets of images (e.g. they all contain scenes). Similarly Cluster 2 in Fig. 5 could mean something other than bodies too (implied motion?). The subjectivity involved in interpreting the clusters makes me less enthusiastic about the study. Automating this interpretability analyses in future work could be interesting. The authors should also acknowledge that the interpretability is limited by the resolution of the CLIP embeddings themselves; the concepts discovered are constrained by what CLIP can represent.
- To better understand the strengths of the proposed methodology, it would also be helpful to compare it against natural candidates for understanding shared representational structure across participants, like Canonical Correlation analysis. The authors should provide a more thorough justification for why clustering in the CLIP embedding space is the most appropriate method, especially given the availability of other established methods for cross-subject analysis.

### Questions
The authors frame their study in the context of previous work on identifying functionally localized brain regions. However, it is unclear how their methodology would specifically highlight concepts confined to a few visual areas versus those spread across the brain. Instead, the approach appears to identify concepts that are easily decodable from brain signals across participants, regardless of whether decoding relies on signals from a small localized area or broader, distributed regions.

### Soundness
2

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors propose an approach for detecting "Shared Decodable Concepts" in human visual fMRI data: clusters in CLIP space that are decodable from common sets of voxels across multiple participants. These clusters are identified using a modified implementation of the DBSCAN clustering algorithm, which identifies clusters in high-dim spaces. In particular, the algorithm operates over vectors of linear decoding weights that map between voxels and CLIP latents. Each weight vector is treated as a brain-decodable concept for a given voxel, such that cosine distance between the weight vectors corresponding to different voxels from different subjects can be used to index the similarity of the concepts encoded therein. After clustering, the authors interpret the SDCs by inspecting a set of "positive" representative images (and words) that are associated with the centroid of each one, and by further identifying groups of "negative" images (and words) that are represented in a maximally different manner. These analyses enable the authors to identify many well-studied aspects of visual cortical organization, such as areas that are tuned to face, body, scene, and word content, and to identify some less-well-studied features such as crowds and lighting. These observations may form the basis for future hypothesis-driven studies that seek to further probe the nuances of the representations of these visual concepts.

### Strengths
- The idea of clustering different subjects' parameter/weight vectors as a means of studying what is common (or different) across individuals' brains is a promising direction that merits more attention and exploration in the field. It's a clever way to overcome the challenges of aligning different brains, while respecting the nuances of individuals' representational signatures. 
- Beyond the well-studied forms of category selectivity that pop out in the SDC analysis, some of the observations are new and interesting (e.g. a "softness" cluster). Identifying these signatures was only possible because of the sophisticated overall methodological approach applied to a rich dataset. These provide provocative directions for future research, to be sure they are actually replicable signatures across datasets rather than clusters that are biased by the specifics of NSD and/or the use of CLIP. 
- The authors make use of the richest possible data (NSD) available, and I appreciate the careful treatment of noise ceiling-related issues in the paper. It's also important that the authors ran a control comparing CLIP decoding to ridge regression. 
- It's useful that this work provides further empirical perspective on the hotly debated topic of whether food selectivity is separable from color representation in the ventral stream. 
- It's powerful to provide clear visual intuition of both the positive and negative examples that correspond to each cluster, as a way to bolster both the interpretability and the hypothesis space that each SDC provides. 
- I deeply appreciate that the authors discussed the possibility of bias in the conclusion, which might arise from the use of NSD stimuli, and which might arise from the use of CLIP.

### Weaknesses
 - In general the paper does a poor job citing other relevant literature, missing some critical papers on category selectivity in the visual system, as well as on recent efforts to use CLIP models for data-driven interpretability of visual feature tuning. Given the topic of the paper, the fact that it has only 20 citations total is insufficient to cover recent work in this area. For example, the authors should connect their observations of body-related selectivity to other works such as: [1,2], and perhaps others. Citing few works beyond the "original" papers identifying FFA/PPA etc makes it hard to understand how many of the findings are novel versus replicates of other studies. I was also surprised that the authors did not cite/discuss [3] and any other works that use NSD and CLIP to propose new kinds of representational distinctions and signatures in the visual system. Furthermore, Stan Dehaene has relevant work on numerosity representations in the brain that should be cited/discussed. The discussion of food/color representations is missing a key citation from [4]... and so forth. I'd also recommend discussing existing methods of functional / representational alignment that do not required projecting individuals into a shared anatomical space, such as hyperalignment and shared response modeling. Why would simpler methods like these be insufficient for this problem of revealing shared dimensions and visualizing the images that project strongly/weakly onto them? I believe that there's extra "juice" to be gained from the CLIP-based approach, it would just help if this historical context were touched on somewhere in the paper. 

- There are many ways to achieve high distance from a given cluster centroid in high dimensional space. I understand the reason for looking at the most- and least-associated images with each SDC cluster, but it's not clear that being atypical in a clustering sense implies that those images would actually have a suppressive impact on the voxels' or regions' response profiles. The authors should clarify the relationship between below-baseline activation and the images identified as maximally different from the cluster centroid. The results here provide clear testable hypotheses, but the impact of the work is limited without further data collection to validate/falsify the positive-negative axes the authors propose.

- The introduction should convey why combining data across participants is a necessary step to discover new forms of category selectivity - this is not obvious. Would a straightforward clustering algorithm applied to the voxel tuning within individual subjects reveal many of these same clusters? The authors do not present analyses that clearly show that cross-subject analysis is necessary to uncover particular forms of interpretable latent dimensions. 

- The clarity could have been improved by streamlining the extensive methods description that occurs before any main results are presented, leaving the nitty-gritty details for the supplement. Sections 2 and 3 place a high working memory burden on the reader - reducing this could help a lot with readability. 

- This might seem like a minor/pedantic point, but the authors' use of the word "semantic" to describe feature tuning in high-level visual cortex is a bit fraught - even if different regions have selectivities that seam meaningful to the human eye, that does not mean that the neurons themselves necessarily compute semantically interpretable features. (Furthermore, language fMRI researchers likely also have a very different conception of what "semantically tuned patches of cortex" means, compared to vision researchers.) I would recommend that the authors reconsider wordings such as "semantic concepts that drive activity" or "semantically-tuned patches" throughout the paper, in favor of language that describes forms of "visual feature tuning" that may be semantically interpretable, post-hoc, without implying that the underlying cells themselves "know" what semantics are.

### Questions
- One main question I am left with is: how many of these proposed clusters contain novel interpretable forms of feature tuning? It is difficult to know without a much more systematic attempt to cite relevant literature on visual category selectivity. 
- It remains unclear to me whether cross-subject analysis is required to derive these forms of insight, as discussed above. 
- Another key question relates to the issue of bias mentioned above. It would be straightforward to attempt to replicate some of these analyses using BOLD5000, THINGS, or other large datasets to address the possibility of bias that arises from the NSD stimuli. Another critical issue is whether relying on the CLIP feature space unavoidably biases the outcomes of analyses toward semantically interpretable outcomes. In other words, does the use of CLIP cause us to "overfit our understanding" of these brain areas to a feature space that was constrained to be language-aligned? I am not positive how I would go about addressing this issue, but at minimum I would appreciate if the authors attempted to discuss it. 
- Given that orientation tuning is a hallmark of V1 representations, why did V1 not show up in the corresponding cluster(s), only V2/V3?

Overall, given the extent of concerns listed above, I am unable to rate the paper higher than a 3 currently. In principle, I am willing to raise my review score if the authors are able to better situate this work in the context of other literature, and more clearly pinpoint the specific novel findings/predictions that differentiate it from other work that has used CLIP to try to understand NSD.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a new method to discover semantically interpretable fine-grained functional organization of fMRI responses that are consistent across participants. It then applies this method to the NSD data form Allen et al, reporting both established functional responses (FFA etc and responses claimed to be novel (e.g. for particular body parts, numerosity, etc).

I recommend acceptance of the paper because the method proposed is useful, the writeup is clear, and the analyses appear solid.

### Strengths
Strengths of the paper are that it tackles an important problem, applies it to a beautiful data set, and reports interpretable results that either serve to establish the validity of the method (via replication of established findings) or report intriguing new results. Another strength is the emphasis on the lowest responses of functional clusters, something that is widely appreciated in the field but rarely if ever explicitly discussed. A third strength is the care that was taken to re-calculate the per-voxel noise ceiling estimates on training data only, a small but important point.

### Weaknesses
The main weaknesses of the paper concern the failure to situate the paper in the context of relevant prior work. Some of the results are described as novel without reference to related findings published previously, For example, the claim of selectivity for different aspects of the body should acknowledge a large prior literature on this topic, e.g.: 
Orlov, T., Makin, T. R., & Zohary, E. (2010). Topographic representation of the human body in the occipitotemporal cortex. Neuron, 68(3), 586-600.
Weiner, K. S., & Grill-Spector, K. (2011). Not one extrastriate body area: using anatomical landmarks, hMT+, and visual field maps to parcellate limb-selective activations in human lateral occipitotemporal cortex. Neuroimage, 56(4), 2183-2199.
Bracci, S., Caramazza, A., & Peelen, M. V. (2015). Representational similarity of body parts in human occipitotemporal cortex. Journal of Neuroscience, 35(38), 12977-12985.
Bracci, S., Ietswaart, M., Peelen, M. V., & Cavina-Pratesi, C. (2010). Dissociable neural responses to hands and non-hand body parts in human left extrastriate visual cortex. Journal of neurophysiology, 103(6), 3389-3397.
big-small close/far this is the ref:
Konkle, T., & Oliva, A. (2012). A real-world size organization of object responses in occipitotemporal cortex. Neuron, 74(6), 1114-1124.
And concerning the proposed method, data-driven analyses of fMRI data especially using clustering have been reported for at least 15 years, and this should be at least acknowledged, e.g.:
Golland, Y., Golland, P., Bentin, S., & Malach, R. (2008). Data-driven clustering reveals a fundamental subdivision of the human cortex into two global systems. Neuropsychologia, 46(2), 540-553.
Lashkari, D., Vul, E., Kanwisher, N., & Golland, P. (2010). Discovering structure in the space of fMRI selectivity profiles. Neuroimage, 50(3), 1085-1098.
Yeo, B. T., Krienen, F. M., Sepulcre, J., Sabuncu, M. R., Lashkari, D., Hollinshead, M., ... & Buckner, R. L. (2011). The organization of the human cerebral cortex estimated by intrinsic functional connectivity. Journal of neurophysiology.
and contrasted with alternative data-driven methods using ICA, NMF, etc, e.g.:
Norman-Haignere, S., Kanwisher, N. G., & McDermott, J. H. (2015). Distinct cortical pathways for music and speech revealed by hypothesis-free voxel decomposition. Neuron, 88(6), 1281-1296.
Khosla, M., Murty, N. A. R., & Kanwisher, N. (2022). A highly selective response to food in human visual cortex revealed by hypothesis-free voxel decomposition. Current Biology, 32(19), 4159-4171.

### Questions
Recommendations to improve the paper:

1. At least cite some of the relevant prior literature as discussed above.
2. It would be useful if the authors could clarify whether the "suppressed" responses are simply lower than those to other stimuli, or whether they are actually lower than a minimal baseline (e.g. the response when no stimulus is presented). In this reviewer's opinion "suppression" should refer to a response below the no-stimulus baseline, and it is not clear that is the case here.
3. The claim that food-related voxel clusters " span bilateral FFA, V4, and PPA." doesn't make sense given the usual definition of FFA and PPA as face and place selective. Presumably what is mean here is that food-related voxels are found near the FFA and PPA.
4. The authors should show how well the brain data reproduces CLIP embeddings (and how this changes over training). That is, show how similar Y_hat is to Y_CLIP. 
5. How does using the CLIP dimension (w_i) improve on just using the neural response values (x_i) in this method? 
6. Perhaps comment on whether these results tell us more about the brain or about CLIP.

### Soundness
4

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
4

### Summary
This paper presents a novel technique for discovering and interpreting functionally specialized clusters in the brain. Using the Natural Scenes Dataset, the authors train linear decoders to map single voxel activities onto CLIP embedding vectors for the respective images seen in the neuroimaging experiment. Then, the authors leverage the similarity of voxel->CLIP prediction weights to perform clustering. Specifically, the authors develop a variant of the DBSCAN algorithm that leverages across-subject consistency in order to find the most consistent and semantically meaningful components. The authors present the results for several components, showing the spatial topography as well as the most strongly and weakly activating images. The authors interpret the components in light of both their spatial topography, and the content that appears present in the strong and weak activating images.

### Strengths
- Interesting method
- The use of a contrastive loss in the fitting of clip latents from voxel activities is particularly interesting
- The modification of DBSCAN is elegant, and provides an intriguing way of aggregating information across subjects
- Good figures

### Weaknesses
 - The early vision components (horizontal and straight lines) activate parts of V1-V3 that represent the periphery (if the authors are unaware: on the flat map, the center of the strips of V1-V3 corresponds to foveal bias, and moving outward corresponds to increasing peripheral eccentricity). This isn't discussed but seems important. The lack of foveal activation in these components is particularly striking given the high density of foveal representation in early visual cortex. It would be important to understand why the method does not identify foveal representations of these features.

- The results are very qualitative. The paper could be strengthened by making some objective quantifications of the content of different components, rather than just "reading the tea leaves". For example, the authors could compute the CLIP similarity between the images and the cluster's concept vector, or use a classifier to predict the presence of different concepts in the images. This would provide a more rigorous and quantitative assessment of the clusters' semantic content.

- This paper joins with a serious of related papers exploring visual components (e.g. Khosla et. al 2022; BrainDIVE, Luo et. al 2023 NeurIPS; BrainSCUBA, Luo et. al 2024 ICLR), to name a few. I'm not sure if there is any single result here that is particularly novel. This makes the paper less compelling. Additionally, the method is not compared to other methods, so it is unclear whether it holds any advantages. The authors should more clearly articulate the unique contributions of their approach and provide a more thorough comparison to existing methods.

- The paper is very light on references. In my opinion, having 20 references for a paper on such a popular topic is a bit of a disservice to the field. There are many relevant papers on visual encoding, functional clustering, and the use of deep learning models in neuroscience that should be cited.

- This sentence is confusing: "We emphasize that there is no constraint that voxels within a shared visual semantic cluster be spatially adjacent in the brain, yet during visualization we consistently find contiguous patches both within and across participants". Please explain how this can be. The algorithm appears spatial, in that core points are defined as having at least minNeighbors points within their epsilon (spatial) neighborhood. Additionally, the epsilon expansion appears to be highly spatial in nature. If it is truly the case that there is no spatial constraint, it would be a mistake to simply call the algorithm a DBSCAN variant -- it would be better to say that it is inspired by DBSCAN, then give it a new name to avoid confusion. Actually, this is probably a good idea regardless.

### Questions
- Can you explain this sentence: "We emphasize that there is no constraint that voxels within a shared visual semantic cluster be spatially adjacent in the brain". 

- How does this paper go above and beyond the findings of other recent works exploring functional selectivity using the Natural Scenes Dataset?


- Can you provide some intuition for why the contrastive fitting of voxel -> clip latents outperforms ridge regression?

### Soundness
3

### Presentation
3

### Contribution
3
