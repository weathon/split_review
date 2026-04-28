# Rethinking Language-Alignment in Human Visual Cortex with Syntax Manipulation and Word Models

- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 5, 6, 6

## Abstract
Recent success predicting human ventral visual system responses to images from large language model (LLM) representations of image captions has sparked renewed interest in the possibility that high-level visual representations are aligned to language. Here, we further explore this possibility using image-caption pairs from the Natural Scenes fMRI Dataset, examining how well language-only representations of image captions predict image-evoked human visual cortical responses, compared to predictions based on vision model responses to the images themselves. As in recent work, we find that unimodal language models predict brain responses in human visual cortex as well as unimodal vision models. However, we find that the predictive power of large language models rests almost entirely on their ability to capture information about the nouns present in image descriptions, with little to no role for syntactic structure or semantic compositionality in predicting neural responses to static natural scenes. We propose that the convergence between language-model and vision-model representations and those of high-level visual cortex arises not from direct interaction between vision and language, but instead from common reference to real-world entities, and the prediction of brain data whose principal variance is defined by common objects in common, non-compositional contexts.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper studies how language-only representations of image captions can predict image-evoked human visual cortical responses, both occipitotemporal cortex (OTC) and early visual cortex (EVC). The paper includes three studies that argue that pure visual learning and pure language learning may be converging on representations that are equally predictive and that the nouns account for the performance of language models; specifically, they act like bag-of-word models.

### Strengths
The paper is well-structured and clearly written. The methodology, results, and discussions are interesting and easy to follow. The authors not only provide empirical findings on the effectiveness of the language and vision representations but also take a closer look at what actually contributes to the observations.

### Weaknesses
See Questions

- I wonder why the authors choose only one model (SBERT-MiniLM-6) as the only representation of the LLMs in the experiment in Section 2.2 while the results from Figure 2 and the discussion in Section 2.1 argue that this is the standout, which could be an outlier and doesn't fully represent the language-only model. Have the authors seen similar results when experimenting with different LLMs?
- There is a discussion on how a vision-language model like CLIP performs like a bag of words [1, 2, 3]. If I understand correctly, not enforcing differentiation between the correct caption and shuffled caption can cause a loss of the capability of compositional reasoning, which the authors discussed in Section 3. It would be great if you could experiment by substituting with improved models like NegCLIP in [1] for text embedding.

### Questions
- I wonder why the authors choose only one model (SBERT-MiniLM-6) as the only representation of the LLMs in the experiment in Section 2.2 while the results from Figure 2 and the discussion in Section 2.1 argue that this is the standout, which could be an outlier and doesn't fully represent the language-only model. Have the authors seen similar results when experimenting with different LLMs?
- There is a discussion on how a vision-language model like CLIP performs like a bag of words [1, 2, 3]. If I understand correctly, not enforcing differentiation between the correct caption and shuffled caption can cause a loss of the capability of compositional reasoning, which the authors discussed in Section 3. It would be great if you could experiment by substituting with improved models like NegCLIP in [1] for text embedding.

[1] When and why vision-language models behave like bags-of-words, and what to do about it? Yuksekgonul et al., ICLR 2022
[2] SUGARCREPE: Fixing Hackable Benchmarks for Vision-Language Compositionality, Hsieh et al., NeurIPS 2023
[3] TripletCLIP : Improving Compositional Reasoning of CLIP via Synthetic Vision-Language Negatives, Patel et al., NeurIPS 2024

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper looks at the alignment between visual cortex activity and vision/language models, and investigate the idea that high-level visual representations are language-aligned. Using fMRI data from the Natural Scenes Dataset (NSD -- specifically a 1000 images subset), they compare the ability of vision-only, language-only, and multimodal (vision-language) models to predict brain responses in early visual cortex (EVC) and occipitotemporal cortex (OTC).

They find that unimodal language models predicted OTC activity as well as unimodal vision models, but this predictive power stemmed primarily from capturing information about nouns in image captions, rather than syntactic structure or semantic compositionality. A simplified “handcrafted” word model based on just 62 nouns and adjectives, using CLIP embeddings, performed comparably to the full CLIP image embeddings in predicting OTC activity. This suggests that the success of language models in predicting high-level visual cortex activity may be due to capturing grounded information from co-occurrence statistics rather than true language alignment.

Language models performed significantly worse than vision models in predicting EVC activity, highlighting their inability to capture lower-level visual features.

### Strengths
Broadly I do think the authors did a good job designing the experiments, and the problem is of concrete scientific interest (rather than of only engineering interest like many image decoding works that rely on NSD). The authors go to a great extent in ensuring the soundness of their experiments.

The question that authors pose in the paper (to what extent do linguistic features of image descriptors predict OTC activations) is very interesting, especially in context of prior work that has been suggestive of linguistic integration at the edge of what are traditional "visual areas" in the brain.

### Weaknesses
I have two primary concerns:
* The first is regarding the breadth and scope of the claims, and if the current experiments are really sufficient to substantiate the claims.
* The second is regarding the third experiment which utilized CLIP

Regarding the former -- "scope of claims". For example the abstract ends with `prediction of brain data whose principal variance is defined by common objects in common, non-compositional contexts` and the introduction from `Line 046` to `Line 067`. My primary concern is that it is unclear if:
1. Perhaps it is a limitation of current language models, and they simply do not capture spatial relationships or complex (negation or adjective) relationships. Is it not possible, that one day there may exist some language-only model that captures these compositional relationships well? [1, 2, 3]
2. It is unclear if the claims are due to limitations in the fMRI modality, which primarily reflects slow temporal signals. Would the claims necessarily still hold up under electrophysiology or calcium imaging? I think this is at least worth discussing.

[1] Locating and Editing Factual Associations in GPT (specifically this paper identifies auto-regressive language models as having directional fact attributions, which clearly breaks the compositionality assumption)

[2] Evaluating Spatial Understanding of Large Language Models

[3] What's "up" with vision-language models? Investigating their struggle with spatial reasoning

Regarding the latter concern (third experiment):
* It is well known that the text encoder from CLIP and other vision-language contrastive models behave like a bag-of-words model and rarely perform above chance on compositional or spatial reasoning tasks, and this is likely due to the dataset used to train these models [4, 5, 6, 7, 8]. These issues are widely known, and it is concerning to me that the authors were seemingly unaware of this issue. I believe this experiment is primarily showing this failure of current vision-language models, and it is difficult to use this experiment to make claims about representations in the brain.

[4] When and Why Vision-Language Models Behave like Bags-Of-Words, and What to Do About It? 

[5] Winoground: Probing Vision and Language Models for Visio-Linguistic Compositionality

[6] Breaking Common Sense: WHOOPS! A Vision-and-Language Benchmark of Synthetic and Compositional Images

[7] Why is winoground hard? investigating failures in visuolinguistic compositionality

[8] When are Lemons Purple? The Concept Association Bias of Vision-Language Models

Another minor concern is the extent of the machine learning contribution. While this paper was submitted under the primary area "applications to neuroscience & cognitive science", I do not think this paper makes any claims regarding new machine learning techniques. However I do want to emphasize that this is a minor concern.

Other very minor issues:
1. Text format of the paper does not match other ICLR papers (font choice/thickness, spacing)
2. Wrong paper template (Does not show "Under review as a conference paper at ICLR 2025")

### Questions
1. Why were 1,000 images chosen? Was this because these 1,000 images were seen by all four subjects?
2. Table 1, what is the model used in "Vision-only" or "Language-only"? Is this one model? Or is this the average of multiple models?
3. For Line 151, is that the noise ceiling averaged over all OTC voxels? 
4. What token are you using for the next token or masked language models as input to the encoder?
5. For Figure 2, when you discuss multimodal vision models, are you using the image component or the text component?
6. For Figure 2, can you clarify what is the "semiopaque fill" and "translucent fill"? To me they look the same.
7. How are the count models used? Do you have every potential word initialized to 0, and then set the corresponding lookup to the number of occurrences for each word?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper surveyed whether high-level visual representations in the human brain are aligned with language by investigating how well the language-only model can predict neural responses to images compared with that of a vision-only model. Using the Natural Scenes fMRI Dataset, they find that while language models predict brain responses and vision models, the predictive power of language models reflects their ability to capture information about nouns present in image descriptions rather than syntactic structure or semantic compositionality. The authors imply that such convergence between the language and vision representations in the high-level visual cortex is due to a common reference to real-world entities rather than by direct interaction of vision and language.

### Strengths
- Novel analysis with "anchor point embeddings" for illustrating simple word-based predictions
- Comprehensive experimental design comparing multiple model types (vision-only, language-only, hybrid)
- Good empirical evidence supporting their main claims

### Weaknesses
 - Without testing on more diverse datasets (apart from NSD), how are we making sure that there's no bias in the analysis
- Captions, like those in the COCO dataset, are designed to describe static scenes and thus yield a dataset that is inherently biased toward simple object-focused descriptions. This kind of language may correspond well with visual cortex responses to simple image recognition tasks but does not allow for an understanding of how the brain integrates language in more complex or conceptual ways
- RSA can overgeneralize the degree of alignment, masking differences that might appear in a voxel-wise or layer-specific type of analysis.

### Questions
- What are the author's thoughts on extending the analysis to include dynamic stimuli or temporal sequences?
- How do you you think the results might/might not change with more abstract or conceptual visual stimuli that require linguistic knowledge for interpretation?

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
3

### Summary
Inspired by recent successes of multimodal vision-language models in predicting visual cortical activity, the authors conduct a finer-grained analysis involving three sets of experiments on the Natural Scenes fMRI dataset. In the first experiment, the authors show that representations from vision-only self-supervised models are similarly predictive to representations from language-only models (trained via autoregressive and masked-language modeling losses). The second and third experiments probe how language-only representations can be predictive of occipitotemporal cortex activity, finding that token-based representations without explicit representation of syntax, be it from GLOVE embeddings or CLIP text embeddings for a base set of 62 hand crafted words, can achieve similar predictive results as normal language-based representations. From this, the authors argue that the similarity in predictive power of vision-only and language-only representations comes not from the influence of language on the high-level visual cortex but from them representing the same units in the world.

### Strengths
1) The experiments comparing GLOVE representations (with the whole sentence or a bag-of-words perturbation) against representations from language models make a convincing argument that at least for the Natural Scenes dataset, the variation can be explained by nouns and adjectives without requiring further syntactic structure. The following experiment with CLIP representation lends more support to this claim.

2) The authors present a strong discussion section highlighting various limitations of their methodology, most importantly the simplicity of the scenes in the Natural Scenes fMRI dataset not allowing for linguistically interesting captions that can be used to more convincingly validate the influence of language on the high-level visual cortex (or lack thereof). 

3) The strength of the discussion makes it such that even if the results are not generalizable due to the limitations of the dataset, they point towards a limitation in the current datasets used in predicting brain representations from model representations and can catalyze future work curating datasets with richer scenes and captions.

### Weaknesses
1) While the authors note the chosen dataset and brain regions as limitations, they should also include the flaws of the model representations themselves as an obstacle in arriving at a clearer conclusion. CLIP representations have been shown to inadequately represent compositional structure, with CLIP language embeddings not being robust to changes in word order [1, 2] or minimal, meaning-altering edits to words [3, 4]. Given this, there is the alternative possibility that multi-modal representations do not improve over vision-only representations, not because the high-level visual cortex is not influenced by language, but because the representations do not adequately model additional syntactic structure. This limitation extends beyond just CLIP, as the bag-of-words perturbation analysis shows that even models like BERT and GPT-2, which are capable of modeling syntax, do not show a significant difference in predictive power when syntactic structure is removed. This suggests that the models may not be leveraging syntactic information even when it is present, potentially due to the simplicity of the captions in the Natural Scenes dataset or the models' inherent biases towards surface-level semantics rather than deeper syntactic understanding.


### Questions
The feature extraction procedure section in the appendix would benefit from more details. For instance, for BERT-based models, is the CLS token used as is convention or is some separate aggregation procedure applied on hidden representations associated with each token? Likewise for GPT-2, is the embedding of the final token used as a representation of the caption?

### Soundness
3

### Presentation
3

### Contribution
3
