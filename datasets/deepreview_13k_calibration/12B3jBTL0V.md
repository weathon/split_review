# Modeling the Human Visual System: Comparative Insights from Response-Optimized and Task-Optimized Vision Models, Language Models, and different Readout Mechanisms

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 3, 5, 6

## Abstract
Over the past decade, predictive modeling of neural responses in the primate visual system has advanced significantly, largely driven by various deep neural network approaches. These include models optimized directly for visual recognition, cross-modal alignment through contrastive objectives, neural response prediction from scratch, and large language model embeddings. Likewise, different readout mechanisms—ranging from fully linear to spatial-feature factorized methods—have been explored for mapping network activations to neural responses. Despite the diversity of these approaches, it remains unclear which method performs best across different visual regions. In this study, we systematically compare these approaches for modeling the human visual system and investigate alternative strategies to improve response predictions. Our findings reveal that for early to mid-level visual areas, response-optimized models with visual inputs offer superior prediction accuracy, while for higher visual regions, embeddings from Large Language Models (LLMs) based on detailed contextual descriptions of images and task-optimized models pretrained on large vision datasets provide the best fit. Through comparative analysis of these modeling approaches, we identified three distinct regions in the visual cortex: one sensitive primarily to perceptual features of the input that are not captured by linguistic descriptions, another attuned to fine-grained visual details representing semantic information, and a third responsive to abstract, global meanings aligned with linguistic content. We also highlight the critical role of readout mechanisms, proposing a novel scheme that modulates receptive fields and feature maps based on semantic content, resulting in an accuracy boost of 3-23\% over existing SOTAs for all models and brain regions. Together, these findings offer key insights into building more precise models of the visual system.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this work, the authors present a comprehensive suite of analyses comparing vision / language DNN models to human fMRI data. Using a novel “readout” mechanism designed explicitly to account for space in the mapping of DNN embeddings to brain activity, the authors report localizing 3 sub-regions in the human visual cortex that respond differentially to spatial and semantic information.

### Strengths
The use of deep neural network models to predict and understand the structure of representation in the biological visual system is a practice rife with heretofore unanswered, but deeply foundational questions as to how it should be done. Bucking a trend that far too often recycles canonical, but relatively unscrutinized methods to new models or new brain data, this submission is impressive not just for the fact that it tackles these questions head-on, but tackles so many of them simultaneously -- and does so (mostly) without losing the forest for the trees. For this alone, I applaud the authors and can recommend that this paper be accepted.

### Weaknesses
My major concern here (and one that I admit is not fully within the authors control, but which clarifying updates or different narrative focus could nonetheless address) is the lingering doubt as to whether even these newer, more expertly designed methods actually do give us any meaningful new “insights” about the biological system they’re nominally designed to give us insights about. An overly reductionist summary of the “findings” of this analysis with respect to the human visual brain could well be that they simply provide more evidence for what is already a amply established gradient of increasingly “abstract” visual information from early (more view-dependent) areas (where smaller, localized receptive fields and retinotopy are the dominant representational motifs) to later (less view-dependent) visual areas (where -- depending on which side of the ventral / dorsal divide those areas are closer to -- you begin to get “representations” that evoke “object categories”, “navigational affordances”, or “conceptual semantics”). And while much debate does remain as to many of the details here, it seems (to me at least) that the existence of this gradient is more or less a common consensus. The core issue is that the reported results, while technically sound, seem to largely recapitulate known properties of the visual system without providing a deeper mechanistic understanding. The localization of differential responses to spatial and semantic information in the visual cortex, while interesting, does not necessarily explain *how* these representations are formed or processed. The study could benefit from a more focused investigation into the specific transformations occurring within these regions, rather than simply demonstrating their differential sensitivity to different types of information. The current analysis risks being descriptive rather than explanatory.

### Questions
My primary suggestion for strengthening this paper is more or less solely for the authors to lean further into its greatest strength -- and to further explicate or justify the expert methods that differentiate this work from so many others attempting to tackle similar questions. Needless to say, perhaps, there are a number of ways the authors could do this. Below are a few different “options” that (I hope) seem reasonable given the constraints of the current review. The authors should feel free to choose however many / whichever of these seems most feasible or intuitive. For me, at least, almost any movement along these vectors is movement that would increase the value of this work for the target audience it seems intended for:
- “Beyond accuracy”: The primary justification of the authors’ “novel readout mechanism” is the general increase in accuracy it provides over other methods. But the emphasis on accuracy as the primary advantage rings a bit hollow if a major part of the goal here is to gain insight into the structure of  representation in biological cortex. There are many alternative ways (e.g. data augmentation, denoising, nonlinearities) -- even “hacky” ones (e.g. smaller cross-validation splits) that one could use to increase the predictive accuracy of model readout mechanisms. What demonstrable advantage does the “semantic spatial transformer” readout have over readout methods with respect to the theoretical questions at play here? (An example answer: “ordinal least squares or regularized regression-style readouts do not preserve spatial information -- therefore making certain areas of the brain appear to be more transform-invariant than they likely are in reality. Here’s a metric that operationalizes the probability of transform-invariance in the fMRI data without models. And here is a side-by-side comparison of the transform-invariance we estimate with ridge regression and our STN readout, respectively.”)
- “Semantics” without language model confounds: There are a number of issues (again, beyond the scope of this paper, but nonetheless relevant) with the use of language models as predictive models of visual fMRI data -- including the fact the inputs to these models (tokenized words) are already proto-symbolic at the time of their initial injection into the candidate representational models that embed them (and are thus more abstract by default than the pixels injected into vision models); and also, an increasing “convergence” between vision and language models [1] that suggests a sort of “default” alignment between these systems attributable (most likely, it seems) to biases in their training data. How to get at questions of “semantics” without over-interpreting language models? One way, perhaps, is to reconsider the brain data itself: It has been suggested by [2] that certain kinds of transformations on the underlying brain data to be modeled (e.g. aggregating across multiple neurons in the case of electrophysiology) can instantiate properties like linearly-separable category boundaries not otherwise apparent without those transformations. If something like this is done on the features of vision models (e.g. averaging across multiple images of the same visual concept), do vision models begin to look more “semantic”? Perhaps the semantic spatial transformer could be used to unveil precisely the kinds of feature transformations that occur along the gradient from early to late visual cortex.
- “densifying” the “single” captions: The authors claim that the localized semantic descriptions inherent to their “dense” captioning method unveil a noticeable midpoint between early, more spatiotopic representations and later, “globally” abstract representations. But is this really about the local tagging of an image’s subparts? Providing more comprehensive “single captions” of the full image that includes more extensive specification of details might close the gap between the dense captioning method and the global captioning -- but in a way that obviates the need to manually subdivide the image. In short, adding further detail (with and without explicitly spatial language) seems like an important control for downstream interpretation of this result.

[1] Huh, M., Cheung, B., Wang, T., & Isola, P. (2024). The platonic representation hypothesis. arXiv preprint arXiv:2405.07987.
[2] Vinken, K., Prince, J. S., Konkle, T., & Livingstone, M. S. (2023). The neural code for “face cells” is not face-specific. Science Advances, 9(35), eadg1736.

### Soundness
3

### Presentation
2

### Contribution
4

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
Using fMRI data from the Natural Scenes Dataset, the authors investigate how different encoder backbones and readout mechanisms predict neural responses in the human visual system. 

They compare a range of models, including those optimized for visual recognition (e.g., AlexNet, ResNet), neural response prediction, and language or vision-language tasks (e.g., CLIP, MPNET). Furthermore, they explore various readout mechanisms to map model activations to fMRI signals, introducing a novel approach (in the context of fMRI encoders) called the Semantic Spatial Transformer readout.

They find that:

1. Response-optimized models perform best in early visual areas (V1-V4): This suggests that these areas prioritize perceptual features not readily captured by linguistic descriptions or task-specific training.

2. Task-optimized and language models do better in higher visual areas: This indicates a shift towards semantic processing in these regions. Large language model embeddings, particularly those using detailed contextual descriptions, prove highly effective.

3. Semantic Spatial Transformer readout improves performance: This novel readout consistently outperforms existing methods like linear, Gaussian, and factorized readouts, boosting accuracy by 3-23%. This improvement stems from its ability to learn stimulus-specific modulations of receptive fields and feature maps.

### Strengths
I think overall, the authors' thorough experimentation is the greatest strength of this paper:

* **Systematic Comparison:** They do a reasonably systematic comparison, comparing a diverse range of models and readout mechanisms, which offers valuable insights.
* **Novel Readout Mechanism:** They propose (in the context of fMRI encoders) a novel readout mechanism—the using the previously proposed spatial transformer with differentiable bilinear sampling —and show that it indeed improves prediction accuracy.  This is a significant contribution in the context of fMRI encoders.
* **Identification of Cortical Regions:** They identify three cortical regions, largely aligned with prior hypotheses about visual cortical functionality. This further strengthens existing theories.
* **Good Discussion of Prior Work:** The authors do a reasonably good job in discussing prior fMRI encoder literature, effectively contextualizing their research.  This demonstrates a solid understanding of the field.

### Weaknesses
The presentation of this paper could be *significantly* improved. I think the presentation quality of this paper does not match the quality of other ICLR papers I am currently reviewing or have reviewed in past years, or ICLR papers that have been accepted in prior years.

The figures are unclear and lack consistent formatting, notation often unexplained, and significant wasted space.

My specific concerns are below:
1. Figure 1 -> This figure is very cluttered and very confusing. Why are the subfigure legends (A, and B) placed so randomly?
2. Figure 1 -> What is the 'What' weight matrix, where does it come from? It is obvious if you are familiar with fMRI encoder literature, but describing the interaction between the weight matrix and green using a tensor product $\otimes$ seems very misleading. This tensor product is also used in the upper part as well, which is deeply misleading, and instead should be expressed as a transposed matrix product. These symbols have a meaning and without redefinition this is pretty confusing.
3. Figure 1 -> Why is the task optimized framework placed together with the response optimized framework without any clarification of which is which? 
4. Figure 1 -> Why is the dense captioning output also part of the response optimized framework with a rotation equivariant network?
5. Where are the dense captions coming from? `Line 210` says `An image of size 424 ∗ 424 is divided into grids of size 53 ∗ 53`, but does not otherwise clarify the origin of the captions anywhere in the paper. What model is used here?
6. `Line 224` please avoid vector matrix products. This assumes row vectors which is not standard.
7. `Line 237` what are the shapes of the output of function $V_c(x,y)$? Could you describe this sampling in more detail?
8. Spatial transformer section, `Line 269` it is unclear what $\theta_2$ is. This is a really important part of the paper and a key claimed contribution. Could the authors mathematically clarify how $\theta_2$ plays a role?
9. `Line 286`, what is `AT`?
10. `Line 297` are the models not voxel wise models?
11. Figure 2A, the bottom descriptions of the models is very confusing. How is the "Language Encoder" being used with "Semantic Spatial Transformer Readouts"? 
12. Figure 2B, please use a proper categorical color map for discrete data.
13. Minor -- Figure 3B, extra space before optimized
14. Figure 3, how are you defining "better predicted by Task Optimized"? Is this the best of ResNet50 or AlexNet? Why use these models when CLIP has been shown to be the best model of visual responses?
15. All flatmaps have significant wasted space.
16. Lack of analysis of the spatial transformer networks. While the paper claims STNs as a significant contribution, there is no visualization of the affine parameters for each voxel. Do the affine parameters focus on population receptive fields that are provided in NSD?

### Questions
Please see weaknesses section for the questions.

### Soundness
3

### Presentation
1

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
This paper compares task-optimized vision and language models to brain response-optimized networks on the natural scenes fMRI dataset (NSD), and introduce a new readout mechanism for model-brain mapping based on spatial receptive field and semantic content. They find that response-optimized networks provide the best match to early visual regions, while task optimized vision-language models better match high-level visual regions. They also find their readout mechanism using spatial transformers improves model to brain mapping (though only marginally).

The comparison between response and task optimized models is interesting, but overall the results provide only a marginal advance in our understanding and computational models of visual cortex. The spatial transformer network readout is novel, but it is not entirely clear what the value of this contribution is. It provides slightly better performance over other methods, but is much more complex (involves integrating an additional Resnet-50 module to weight the channels of each model) and provides only minimal quantitative gains over much simpler methods.

### Strengths
-	Compare response optimized and task optimized models directly
-	Compared many different model-brain mapping functions
-       Present a new metric for model-brain mapping

### Weaknesses
 - The models tested varied along many factors making it difficult to draw strong conclusions about the role of response vs. task-optimization or vision vs. language in model’s performance. For response vs. task, these points could have been made more compelling by training the same architecture on both task and neural responses
- The biggest issue is that the major findings of this paper have been shown previously (also on the same dataset). Prior work with vision and language models (e.g., Doerig et al.) that showed semantic content is more important for high than low-level visual regions, and Khosla & Wehbe which introduced the response optimized model used here and already showed it predicted NSD responses.
- The utility of the STN was not well motivated. Figure 2 suggests that the different readout mechanisms provide largely similar results with only minor quantitative differences. This slight boost is unsurprising given how much more complex the spatial transformer network is compared to other readouts.

### Questions
-	Why are the models in Figure 2b shown on a continuous color bar?
-	Why were only a subset of the NSD subjects used?

### Soundness
2

### Presentation
3

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
The authors aim to evaluate the extent to which LLMs (based on single or dense image captions) predict activity in high-level visual cortex relative to ImageNet-pretrained vision models or neural-response optimized vision models. They introduce a novel readout method that shows higher performance in predicting neural responses relative to linear regression and two other readout methods. They find three distinct regions of visual cortex that are better predicted by vision models, LLMs based on dense captioned images, or LLMs for single image captions.

### Strengths
Literature review is comprehensive, and overall, the paper is clearly written. 

The paper is not highly original building on prior readout methods, and recent work conducting large-scale benchmarking of AI models against the brain. However, the addition of dense image captions to extract representations from the language models is a nice contribution to the literature on LM alignment with visual cortex. I have some reservations mentioned below that are impacting my score, but if addressed, I think the paper may constitute a meaningful contribution to the literature.

### Weaknesses
The paper needs to better justify why a different readout method is necessary. The authors state that the predominant readout method is linear ridge regression, which has high computational and memory demands, but representational similarity analysis (RSA) is nearly as commonly used in the human literature and is less computationally intensive (Kriegeskorte et al, 2008). More importantly, however, the reason that the NeuroAI field tends to rely on linear regression as a readout is based on the logic that we are interested in evaluating the similarity of the representations up to a linear transformation (in representation space) without introducing non-linearities in the readout method. The authors should provide better justification for why a novel readout method is needed within that framework.

The Semantic Spatial Transformer has greater improvement relative to Ridge regression for the vision model than the language model (Figure 2), and vision models are found to better predict more voxels in high-level visual cortex using the Semantic Spatial Transformer readout (Figure 4) than when using Ridge regression (Figure 5). To me, it is a problem that the readout method does not provide uniform improvements across models. This suggests to me that the readout method is introducing a bias in the conclusions. The authors should address this potential bias more thoroughly. The fact that the Semantic Spatial Transformer (SST) readout benefits more from the higher spatial resolution of vision model feature maps, as opposed to the lower resolution feature maps of language models, is a critical concern. This suggests that the SST readout is not a neutral measure of brain alignment, but rather is sensitive to the spatial properties of the input feature maps. This sensitivity could lead to spurious conclusions about the relative alignment of different models with the brain.

Figure 4D shows three regions that respond more to vision model, single captions language model, or dense caption language model, but this is binarizing the difference between each pair of models. However, the claims of these three distinct regions would be strengthened by showing that high-level visual voxels, for example, have additional explained variance by the single caption language model after accounting for the variance explained by vision and dense caption models.

### Questions
Why did the authors only use 4 of the 8 participants from NSD? 

Figure 1A is confusing. I don’t follow how each of the different readout methods are shown here. Better labels would be very helpful.

### Soundness
3

### Presentation
3

### Contribution
3
