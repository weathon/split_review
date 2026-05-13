# One Hundred Neural Networks and Brains Watching Videos: Lessons from Alignment

- Decision: Accept
- Scores: 8, 6, 8, 6

## Abstract
What can we learn from comparing video models to human brains, arguably the most efficient and effective video processing systems in existence? Our work takes a step towards answering this question by performing the first large-scale benchmarking of deep video models on representational alignment to the human brain, using publicly available models and a recently released video brain imaging (fMRI) dataset. We disentangle four factors of variation in the models (temporal modeling, classification task, architecture, and training dataset) that affect alignment to the brain, which we measure by conducting Representational Similarity Analysis across multiple brain regions and model layers. We show that temporal modeling is key for alignment to brain regions involved in early visual processing, while a relevant classification task is key for alignment to higher-level regions. Moreover, we identify clear differences between the brain scoring patterns across layers of CNNs and Transformers, and reveal how training dataset biases transfer to alignment with functionally selective brain areas. Additionally, we uncover a negative correlation of computational complexity to brain alignment. Measuring a total of 99 neural networks and 10 human brains watching videos, we aim to forge a path that widens our understanding of temporal and semantic video representations in brains and machines, ideally leading towards more efficient video models and more mechanistic explanations of processing in the human brain.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
1

### Summary
This paper investigates the roles of temporal modeling and action recognition optimization in aligning video models with brain activity patterns during video observation. The findings show that early visual processing regions in the brain benefit from temporal modeling, aligning with neuroscience literature that these areas are sensitive to short-term changes, whereas late areas are more semantically oriented and responsive to action categories. Comparisons between CNNs and Transformers reveal that Transformers align with early brain regions at shallower layers due to their global attention mechanism, suggesting a different spatial processing approach than CNNs, which makes sense when compared with our intuitions about the models. The study also finds that computationally efficient models align better with high-level brain regions, implying that achieving human-like abstract semantics does not require high computational resources. Limitations include reliance on indirect brain measurements, fMRI's low temporal resolution, and a limited set of available video models.

### Strengths
- Interesting paper, great exploration, well written. 
- The study provides a nuanced understanding of how temporal modeling and action recognition optimization affect alignment with different stages of brain processing, offering valuable insights for both neuroscience and machine learning.
- By comparing CNNs and Transformers, the paper highlights unique alignment patterns, suggesting that global attention mechanisms in Transformers may capture early brain processing more effectively than CNNs.
- The finding that computationally efficient models align better with high-level brain areas supports the development of optimized models that achieve human-like abstract representations without excessive computational costs.
- The research bridges machine learning and neuroscience, potentially guiding the design of video models that better align with human brain activity (particularly in applications involving temporal and semantic processing).

### Weaknesses
 - One significant limitation is the narrow focus on visual regions, neglecting other brain networks that are also engaged during video watching. Motion and imagery cues in videos can activate regions beyond visual areas, including those related to emotion, memory, and multisensory integration. This raises the question of why the study did not analyze the entire brain, as doing so could potentially yield more comprehensive insights and improve alignment accuracy by leveraging richer information from other relevant brain networks.
- The study only benchmarks models available in a specific library, limiting comparisons across diverse training paradigms (e.g., supervised, contrastive, self-supervised). This restricts the generalizability of findings and leaves open questions about whether models trained with different methods would exhibit distinct alignment patterns.

### Questions
- Why limit the analysis to visual regions only? Motion and imagery cues in videos can activate brain networks beyond the visual cortex. 
- There are several recent visual/neural decoding papers (such as MindEye, MindVis, etc.). How do they compare numerically with what is presented in this paper?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper aims to address an important question, which is the correlation between human brain activations to complex stimuli - video-watching - recorded with fMRI and extracted features from various deep learning models. The authors compared about 100 different deep learning models (image-based, video-based) for ten different subjects. They used different criteria to evaluate the correlation between brain and deep learning models' activations: 1. temporal modelling (image-based vs video-based) 2. classification tasks (image vs video classification); 3. type of architecture (CNN vs Transformer-based models) 4. training datasets 5. computational complexity of the models. The study identifies various trends, such as the correlation between models' activations and early or high-level regions from the visual cortex, as well as differences between architectures (CNN vs Transformers) and a negative global correlation with models' complexity.

### Strengths
- The paper discusses a very interesting and relevant topic. Such a large-scale benchmark, which compares very different and high-performing CNNs and Transformer architectures, is of high value for investigating how image and video models compare with brain feature extraction and hierarchical modelling of visual information.  

- The methodology is relatively well-thought-out, with many differentiating criteria to evaluate the impact of important properties of computer vision models, which should process visual information differently: image-based and video-based modelling, different training datasets, transformers vs. CNNs, etc. There are all relevant, and the paper does a good job at analysing the results. 

- Statistical tests are carefully run to validate the relevance of the results, which is a great plus to support the validity of the results for such a large-scale study. 

- The discussion underlines important points about the role of different layers (in terms of depth), and about the difference in modelling visual features with self-attention (transformer) and convolutions (CNNs)

### Weaknesses
 - The abstract and introduction lack clarity and could benefit from better writing. For instance, the concepts of "brain representational alignment" and "model-brain alignment" in the abstract are unclear and can be confusing. The second bullet point int= the contributions is not very clear.

- Although the question addressed is highly important/interesting, the reason for conducting such research is not sufficiently well-motivated. Particularly, it is difficult to clearly understand the neuroscience motivations for comparing brain activations to features extracted from deep learning models and how the study would benefit both the development of neuroscience and deep learning architectures in the future.

- One of the main weaknesses is the lack of description of the data acquisition and data preprocessing, which are crucial for a paper of that scale. More extensive (even in the appendix) information about the fMRI acquisition (TR, resolutions, etc.), the preprocessing strategies, and the anatomical/functional registration strategies would be required to fully evaluate how brain signals could be reliably used for comparison. Otherwise, this would undermine the quality of the results and conclusions that can be drawn (see questions below)

- Some points of the methodology could benefit from more clarity (see questions below)

- Some limitations of the study could be better discussed: choice of the fMRI dataset, and the limitations of using the Brain Representational Alignment to model brain alignment.

### Questions
**Questions about the limitations of the study**:

- The paper discusses alternatives in the literature to study brain alignment via projecting feature space into voxel space. Still, it should be compared with more recent approaches than those cited in the paper and notably very successful methods that correlated brain activations and language modelling (speech/text), such as [1,2,3]. Is there any reason why those methods are performing in NLP, but maybe are not in image-based/video-based models?

**Methods/Results**:

- I understand the complexity of using high-res feature dimensionality, but it would have been nice to know/see if PCA impact the prediction accuracy (line 188) and the following results. 

- How is the feature extraction achieved for the transformer-based architectures (line 270)? This is not clear at the moment.

- Line 275: "Image models trained on action recognition expect the input all at once according to their preprocessing function similar to video models." The temporal modelling for the image-based models on video datasets is not clear. Could you please clarify?

- Could you confirm that the points drawn in Figure 2.a and similar correspond to the maximum activation across layers for any given model? Would it be interesting to study the variance of correlation across layers for each model? Are there any models where layers are completely decorrelated to brain activations or is the correlation generally homogenous across layers? I am not sure this information is currently provided in the current graphs. 

- From the graphs in Appendix B, notably Figure 7, it seems that the layers the most responsive to V1/V2 are the mid-layer forms of most of the architectures; what is the rationale, as we know that low-level visual features are extracted by early layers in CNNs based architectures?

- Given that many results indicate that the highest correlation is for the classification layer, would it be interesting to use an unsupervised algorithm? how would you expect the results to differ? 

- From Figure 7, it seems that the early visual cortices v1, v2, and v3 have very similar patterns, although one would expect hierarchical modelling in these particular layers. Is this the case? Is there any rational behind? 

**Data**

- A thorough description of the dataset used is clearly missing. In particular, what is the voxel resolution, the MRI acquisition parameters, the TR of fMRI?

- Is the brain solely anatomically aligned or functionally aligned? One would expect the brains to be functionally aligned, e.g. using MSM registration [4], as the study compares brain functional activation between different subjects, and anatomical registration might not be sufficient to compare brain activations at the voxel level. 

- Are the brains aligned across repetition of the same stimuli? It is not clear if this occurs during the same session or in different sessions. As voxels are averaged across subjects, this seems important. 

- Information is missing about whether the study takes into account the temporal lag between brain activation and stimuli to compare brain activation and features. Also, the limitations of using BOLD signals to model brain processing should be mentioned. 

- Are the ROIs defined subject-wise or using a template? This should greatly impact the correspondence of functional regions between subjects.
 
- There is no discussion on the limit of using voxel-wise modelling compared to surface-based modelling. However, surface-based modelling has been shown to be a better predictor of brain function [5,6].


[1] Toward a realistic model of speech processing in the brain with self-supervised learning, J.Millet et al, Neurips 2022

[2] Natural speech reveals the semantic maps that tile human cerebral cortex, AG Huth et al, Nature 2016

[3] Semantic reconstruction of continuous language from non-invasive brain recordings, J Tang et al, Nature Neuroscience 2023

[4] Multimodal surface matching with higher-order smoothness constraints, EC Robinson et al, Neuroimage 2016

[5] A multi-modal parcellation of human cerebral cortex, MF Glasser et al, Nature 2016

[6] The impact of traditional neuroimaging methods on the spatial localization of cortical areas, T Coalson et al, PNAS 2018

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper investigates representation alignment between the human visual system and task-driven deep learning models in viewing dynamic natural stimuli, measured in representational similarity across brain regions and model layers. The authors conducted a large-scale ablation on a range of vision models and training conditions, including static vs dynamic models, training data composition, and model architectures and sizes. They showed that dynamic models are more aligned with human early visual areas, moreover, convolution-based models exhibit the hierarchical structure of the biological visual system more so than Transformer-based models.

### Strengths
- The question of how similar the biological visual system and the machine learning counterpart process visual information, especially in dynamic settings, is of high interest to both the machine learning and computational neuroscience communities.
- Overall the paper is well written. In particular, the Related Work section succinctly defines where/how this work complements existing literature. 
- The choice of models and experiments conducted are thorough, and the analysis of representation similarities between model layers and brain regions is more detailed than previous in this area. The findings on CNN-based models appear to exhibit the hierarchical structure while Transformer-based models have similar representation across depth, aligning with previous work in comparing CNN vs ViT internal representation [1]. These results can potentially guide the visual response modeling community on the choice of model architecture for different regions in the visual system.

[1] Raghu, Maithra, et al. "Do vision transformers see like convolutional neural networks?." Advances in neural information processing systems 34 (2021): 12116-12128.

### Weaknesses
I don’t have any major concerns with the paper but have some minor questions and suggestions, please see below.

- Figure 2a shows that image models trained on object classification are (slightly) more aligned to the early and intermediate (V3ab and hV4) visual areas than image models that are trained on action recognition, but are worse in later visual areas. I wonder if the authors have any suggestions as to why this is the case.
- The brackets and asterisk above the box plots in Figure 2a need some spacing between pairs of boxplots. Right now they are all on the same line and it is difficult to read which pair is which. 
- The authors reported a negative correlation between models’ FLOPs (computational complexity) and alignment to higher visual areas. Does the same trend hold if we compare the model performance, maybe the validation or test accuracy (or whatever metric that was used) of the model in their respective datasets? e.g. Do more performant models in their specific task lead to worsened alignment?
- The results show that CNNs exhibit a better hierarchy overall, while Transformers are more aligned to early visual areas. I know that ConViT is already part of the model zoo but have the authors examined architectures that use both convolution and self-attention? Such as CvT [2].

### Questions
- Figure 2a shows that image models trained on object classification are (slightly) more aligned to the early and intermediate (V3ab and hV4) visual areas than image models that are trained on action recognition, but are worse in later visual areas. I wonder if the authors have any suggestions as to why this is the case.
- The brackets and asterisk above the box plots in Figure 2a need some spacing between pairs of boxplots. Right now they are all on the same line and it is difficult to read which pair is which. 
- The authors reported a negative correlation between models’ FLOPs (computational complexity) and alignment to higher visual areas. Does the same trend hold if we compare the model performance, maybe the validation or test accuracy (or whatever metric that was used) of the model in their respective datasets? e.g. Do more performant models in their specific task lead to worsened alignment?
- The results show that CNNs exhibit a better hierarchy overall, while Transformers are more aligned to early visual areas. I know that ConViT is already part of the model zoo but have the authors examined architectures that use both convolution and self-attention? Such as CvT [2].

[2] Wu, Haiping, et al. "Cvt: Introducing convolutions to vision transformers." Proceedings of the IEEE/CVF international conference on computer vision. 2021.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a comprehensive benchmarking study that compares deep video models with human brain responses to natural video stimuli. The authors utilize a video-fMRI dataset to investigate how various factors, such as temporal modeling, classification tasks, architecture, and training datasets, influence the alignment between neural network representations and human visual processing. The study reveals some insights into the mechanisms of video processing in both artificial and biological systems.

### Strengths
The paper addresses a novel and important question regarding the alignment of neural network representations with human brain activity in the context of video processing. The approach of systematically benchmarking a large number of models is innovative and contributes to the understanding of how different architectures and training datasets affect representational alignment.

The paper is clearly written and well-organized, making complex concepts accessible to readers. The figures and tables effectively illustrate the findings, aiding in the communication of key results.

### Weaknesses
The temporal resolution of the fMRI dataset. As mentioned by the authors, the low temporal resolution of fMRI is insufficient for representing the brain's processing of temporal information. It is recommended to consider using brain imaging data with higher temporal resolution, such as MEG, for this comparative study.

The diversity of video stimuli data is lacking. Although the entire video database contains 1102 samples, the authors only used 102 for analysis. Why not use all of them? Since each video clip is only 3 seconds long and scene transitions are very limited, using only 102 samples makes it difficult to draw universally applicable conclusions.

As mentioned by the authors, similar studies comparing brain responses to model representations on the natural scenes have been published in previous work. Although this paper tests a richer set of models, the novelty of its method and conclusions are relatively limited.

The authors mention that this work can inspire us to design more efficient video processing models. How exactly do these comparisons motivate the design of more efficient video processing models? Based on the experimental results, it would be meaningful if the authors could give some reasonable suggestions for designing more efficient video models.

Is there any project code (such as a GitHub link) to ensure the reproducibility of the experiments?

### Questions
The diversity of video stimuli data is lacking. Although the entire video database contains 1102 samples, the authors only used 102 for analysis. Why not use all of them? Since each video clip is only 3 seconds long and scene transitions are very limited, using only 102 samples makes it difficult to draw universally applicable conclusions.

How exactly do these comparisons motivate the design of more efficient video processing models? Based on the experimental results, it would be meaningful if the authors could give some reasonable suggestions for designing more efficient video models.

Is there any project code (such as a GitHub link) to ensure the reproducibility of the experiments?

### Soundness
3

### Presentation
3

### Contribution
3
