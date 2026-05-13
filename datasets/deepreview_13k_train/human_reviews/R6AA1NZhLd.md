# Topoformer: brain-like topographic organization in Transformer language models through spatial querying and reweighting

- Decision: Reject
- Scores: 5, 6, 5, 8, 6

## Abstract
Spatial functional organization is a hallmark of biological brains: neurons are arranged topographically according to their response properties at different scales. In contrast, representations within most machine learning models lack spatial biases, and instead manifest as disorganized vector spaces that are difficult to visualize and interpret. Here, we propose a novel form of self-attention that turn Transformers into "Topoformers" with topographic organization. Our primary contribution is Spatial Querying, where keys and queries are arranged on 2D grids, and local pools of queries are associated with a given key. Our secondary contribution is Spatial Reweighting, where we convert the standard fully connected layer of self-attention into a locally connected layer. We first demonstrate the feasibility of our approach using by training a 1-layer Topoformer on a sentiment classification task. We show that training with Spatial Querying results in corresponding topographic organization between queries and keys, and Spatial Reweighting results in corresponding topographic organization between values and self-attention outputs. This emergent organization is \textit{semantically interpretable}: the internal activation magnitudes show spatial biases for sentences with positive and negative sentiment. Moreover, generic topographic organization is seen in the low dimensional structure of activations revealed through principal component analysis. After establishing that we can indeed obtain interpretable topography, we apply the Topoformer motifs at scale. We train the widely used BERT architecture on larger corpora with a masked language modeling objective. We find that the topographic variant of this model performs on par with a non-topographic control architecture on downstream NLP benchmarks. Finally, we analyze an fMRI dataset of human brain responses to a large set of naturalistic sentences, demonstrating that the Topoformer yields similar forms of topographic organization for linguistic information as that present in the language network of individual subjects. Scaling up Topoformers holds promise for greater interpretability in NLP research, and for more accurate models of the organization of linguistic and semantic information in the human brain.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Biological brains feature spatial organization in neuron arrangement. However, the representations of current machine learning models lack such organization, pose challenges in interpretation. This study introduces a novel approach called Spatial Querying, and Spatial Reweighting, which results in interpretable topographic organization. The primary contributions can be summarized as follows: Introduced a Topoformer with topographic organization and demonstrated this organization through a 1-layer Topoformer in sentiment analysis task. Subsequently, scaling this proposed method to BERT, achieving competitive results in NLP benchmarks. Further experimental studies reveal that Topoformers exhibit similar linguistic organization while analyzing human brain activity.

### Strengths
1.	Addressed the architectural disparity between current Transformer models and the biological brain by inducing a topographic organization of features within the Transformer.
2.	The topographic organization of the Topoformer yields competitive performance compared to the Vanilla Transformer model in small-scale sentiment analysis and benchmark GLUE tasks.
3.	The proposed method is scalable for both small and larger-scale datasets.
4.	The alignment between the way information is organized in the Topoformer and the human language network is clearly shown using brain dataset.

### Weaknesses
1.	Although the novelty of the paper is interesting, but it lacks specific experimental details.
	o	How to choose the optimal number of tokens in local spatial querying? The paper does not clarify whether spatial querying operates on token embeddings or feature maps derived from them. It is crucial to specify the exact input to the spatial querying mechanism. Furthermore, the method for determining the receptive field (RF) size for spatial querying and reweighting is not described, making it difficult to reproduce the results.
	o	Additionally, with the introduction of local pooling of spatial queries, the parameter differences between Topoformer and Vanilla BERT is not provided. The paper should explicitly state whether the spatial querying and reweighting operations introduce additional learnable parameters, and if so, how many.
	o	How did the authors generate Fig 4? What does "Stat Value" refer to? The statistical measure used to quantify the topographic organization is not clearly defined. It is unclear how this "Stat Value" is computed across different layers and for different components (queries, keys, values, and fc_out). The methodology for generating the topographic maps needs to be detailed.
	o	What does fc_out refer to? It is not defined or referenced anywhere in the entire paper except in Fig 4. The absence of a clear definition for 'fc_out' makes it difficult to understand the data presented in Figure 4. The paper needs to define all abbreviations and terms used.
	o	Typically, a BERT-base model comprises 12 encoder layers. However, in Fig 4, there are 15 layers depicted. Could the authors provide an explanation as to why there are 15 layers in this context? The discrepancy in the number of layers between a standard BERT-base model and the model used in the experiments raises concerns about the consistency of the implementation.
2.	The validation of the proposed Topographic Transformer model appears insufficient. Similar to BERTology studies, has the proposed Topoformer been assessed for its ability to capture the hierarchy of linguistic structure (such as early layers capturing surface features, intermediate layers capturing syntax, and later layers representing semantics)? The paper lacks analysis to determine if the topographic organization is related to linguistic hierarchies.
3.	Why does the Topoformer with a single head result in better accuracy scores on the GLUE benchmark compared to the multihead attention? The paper does not provide any explanation or analysis of this counter-intuitive result, which needs further investigation.
4.	What is the complexity of self-attention in Topoformer after introducing the local spatial querying mechanism? Did the authors maintain the same local spatial querying across layers, or did they increase the local pool size with the depth of the layer? The paper does not discuss the computational complexity of the proposed method and how the local spatial querying affects the overall complexity of the model. The choice of the receptive field size and whether it varies across layers is also not addressed.
5.	the clarity can be improved:
6.	several typos: In Fig4: fc_out, rest of the paper: fc-out, FC-Out

### Questions
1. What is the representational similarity between Topoformer and Vanilla BERT across layers? During fine-tuning of Topoformer, similar to fine-tuned BERT, are the last layers significantly affected?
2. Please check weaknesses for the remaining questions.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces the Topoformer, a transformer model, here applied to language, that imposes spatial structure on the latent dimensions involved in the attention process. It uses a binary matrix encoding spatial proximity that is placed between the K and Q matrices that create the attention matrix. Further, local connectivity is used after the application of the V matrix.

This transformer is trained first using a 1-layer version on Imdb, later a large BERT version.

Transformer activations are inspected and found to have spatial structure.

A relationship is drawn between this spatial structure and that found in and fMRI language experiment.

### Strengths
This paper introduces the idea of spatial structure in the attention mechanism of a transformer, devises a method to achieve it, and shows that the spatial structure indeed appears.

### Weaknesses
This paper is unfortunately quite badly written, but thankfully many aspects can be improved straightforwardly.

1. The abstract and intro contain falsehoods and non sequiturs and would largely benefit from being made more concise.
Example of falsehood: Abstract, sentence 2. Convnets exhibit and exploit spatial structure
Example of non sequitur: Intro, paragraph 3. "Despite the success of these LMs, the fact that their architecture is
not compatible with spatial constraints of the biological cortex is a fundamental limitation for the
growing research enterprise that uses LMs as models of human intelligence" the one simply does not follow from the other, on any level, especially without concrete evidence.

The paper would largely benefit from having such problematic statements removed, since they contribute to the impression that the authors might want to pull the wool over the reader's eyes.

2. Variables used in formulas are not introduced and formulas are hard to find and not explained. See, e.g. the first math items in 2.1. Further, see reference to a non-existent "Equation 4" (which may correspond to Eq4 found in the appendix, but the reader can't know this, because it is possible that enumeration restarts. On top of this, the equation from the appendix is stated without any context or description of what is what).

3. The link to brain organization is highly suggested or strongly stated along the paper but is unfortunately very tenuous. Examples are Fig 1, where learned spatial attention structure is juxtaposed with some brain flatmaps and the term "brain-like" is used. There are so many possible reasons for smooth variation of brain data - for starters there is the smoothing employed in the pre-processing, the mapping to MNI space and the subsequent mapping to the cortical surface. Functional brain regions do exist, but absent individual localizers it is even unclear whether the cropped regions are correct. It would be good to give a map showing any form of predictive power of any language model on the selected voxels. As an aside, it would have been great to have an idea on a global surface or a 3D brain of where this region actually lies. Also the figure caption says "Brain responses are visualized", while the diagram mentions PCs, which are not brain responses, but summaries of them.


Related to both 1 and 3, the statement "Because we have already shown the spatial smoothness of these components, if we see smoothness in the correlation of these components with voxels/units in the target space, we can infer that there is a
correspondence between the two topographies." is incorrect. One would see patterns, and smoothness in the correlation of the topoformer pixels with many things, possibly even certain noise vectors (though with lower correlation values), but very likely with brain data from other regions. The latter would be a good test. It would be very useful to see the correlation drop when using e.g. data from a visual area or a motor area.
The currently important thing to read from the diagram is the relatively high correlation value which shows that there is a correspondence between the transformer activations in brain activity. However, this is also true for unstructured transformers.

All in all, it would be very helpful if the authors backed their statements up better with actual analyses and put sharp and concise statements along with proof if not an established fact.

It is worth considering removing the brain analysis part and focusing on more detailed interpretability of the transformer model. E.g. why is the focus on the final layer of the topoformer model? What do the other ones look like? Even if they exhibit the spatial property less, this would be interesting. A comprehensive study would have been more helpful instead of a link to brain activity that does not strongly corroborate similar topological information, but that only shows what several papers have already shown - a correspondence of these models to brain activity.

### Questions
Why is locality enforced using a matrix M that forces averaging of the adjacent keys and queries? This a priori does not actually have to enforce similarity between the points that are connected, but it does seem that it is enough pressure to make the locations become similar to their average.
A different approach would be to simply constrain each location to only be able to use information from a neighborhood. Was this approach considered at all?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Paper 2 proposes a novel approach to training Transformer language models with topographic organization, called Topoformer. The key idea of Topoformer is to arrange the keys and queries of the self-attention mechanism on a 2D grid, and to associate local pools of queries with a given key. This allows Topoformer to learn topographic representations of language, which are more interpretable and efficient than the unstructured representations learned by traditional Transformer models.

### Strengths
The proposed method, Topoformer, is a novel approach to training Transformer language models with topographic organization.
Topoformer has been shown to be feasible on a 1-layer sentiment classification task and to perform on par with a non-topographic control architecture on downstream NLP benchmarks.
Topoformer has also been shown to yield similar forms of topographic organization for linguistic information as that present in the language network of individual subjects.

### Weaknesses
The paper does not provide any concrete examples of how Topoformers can be used to improve the interpretability of NLP models. Specifically, while the 2D grid structure is presented as a means for topographic organization, the paper lacks a clear demonstration of how this organization translates to interpretable features or representations. For example, it is not clear how specific regions of the grid respond to different linguistic features or concepts, and how this could be visualized or analyzed. The paper also does not evaluate Topoformer on a variety of different NLP tasks. While the sentiment classification task and GLUE benchmark are useful, the paper would benefit from a more thorough evaluation on tasks that probe different aspects of language understanding, such as question answering, text summarization, or natural language inference. This would help to establish the generalizability of the proposed approach and its potential for real-world applications.

### Questions
How can Topoformers be used to improve the interpretability of NLP models?
Will this Topoformer increase the performance of the donw-steam task?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors introduce a method for integrating topographic organization into the keys, queries, values, and outputs of the self attention mechanism of a transformer. They validate that this indeed yields topographic organization on the simple IMDB task. When their method is applied to language modeling (BERT) the authors identify topographic organization with respect to semantic clusters of topics (music / sport). They then measure the topographic organization of human subjects (through FMRI) with respect to language, and compare these results to the topographic organization of their Topoformer-BERT model through correlation analysis. They show that there is indeed strong spatial correlation between their model and the human FMRI data, indicating some similarity of topographic maps. Finally, they show that this topographic organization does not significantly hurt the performance of their Topoformers compared to non-topographic baselines.

-----

### Post Rebuttal
We thank the authors for their extensive response to our review. We have looked at the updated PDF and find it to be a significant improvement over the original version and therefore maintain our recommendation that this is a good paper that should be accepted.

### Strengths
- Novelty — this is the first model which integrate topographic organization into a transformer (to the best of my knowledge) and furthermore one of the first to do so for language. 
- The comparison with human FMRI data adds a important degree of grounding to the paper which only adds to it’s impact.
- The quality of the writing in the paper is very high in general, and specifically the introduction is very succinctly written and elegantly describes topographic models.
- The use of a topographic metric to quantify topographic organization across multiple layers in an easily digestible way is a welcome finding in the field. 
- Topographic organization in artificial neural networks is an important but understudied topic, and I believe this paper will draw important attention to in the future. Furthermore, I believe this paper has the potential to become a foundational paper in the field given it’s application to transformers and language modeling at this crucial point in time.

### Weaknesses
 - The appendix is poorly formatted and appears almost incomplete. There are equations (such as (4)) which are important to the text but are left with undefined symbols. Furthermore, some figures (such as the Brain-PC correlation with a non-topographic control) appear to be missing (or is this Figure 9?).
- No baseline for IMDB accuracy performance without topographic organization.
- Only a single attention head is used on all experiments, limited the comparison with most state of the art transformer architectures. (To be clear, I think the Topoformer-BERT also only uses a single head but could not find this in the text).
- Too many important aspects are relegated to the Appendix making the text challenging to read. The authors should improve the formatting of the appendix (ensure headings for sub-sections are in the correct location) and potentially move some figures (such as Figure 9, and equation 4) to the main text. 
- Given the authors mention that they compared many spatial receptive field sizes, it would be nice (and make sense) if they included these results in the appendix. Furthermore, it would be helpful to understand how the authors ultimately settled on their final choices of RF sizes as this is not described in the text.
- The topographic organization for the values and fc_out appears quite weak (despite the topographic metric). This makes one either question the topographic metric, or question the usefulness of this model for organizing the actual output of self-attention. It would be helpful if the authors could comment on this. (To be clear, despite this weak organization of values, I still think there is significant value in the strong organization of keys and queries and therefore do not think this should be held strongly against the quality of this paper). 
- It would be helpful if the authors included additional controls comparing non-topographic models with brain PCs for the correlation plots of Section 3.3. Without these, the strengths of the conclusions drawn from this correlation analysis are significantly lowered.

### Questions
- Is there any intuition why in Figure 1, you see that the Keys and Queries show strong selectivity for negative sentiment but not positive? While the values appear to show only very strong selectivity (very little intermediary), but for both classes? Is this somehow a result of the different mechanisms used to induce topographic organization? (Bilinear vs. Matrix-vector product?). Similarly, is there a reason why these components appear to have patchier organization in the BERT setting as welll? 
- In the appendix you say SQR was less stable and required larger batch size, do you have intuition for why this might be? 
- Would it be possible to again compute the topography metric (Equation 4) on the correlation maps between the model and Brain PCs? Would this make sense as another quantative metric of the alignment of the two representations?
- Do the PCs found for the human participants correspond to any semantic categories of the text?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors propose to include topographic constraints to the Transformer model by using spatial querying and spatial reweighting. This resulted in “Topoformers” The authors demonstrate their methods both in simple examples and in BERT architecture on large language corpora.  They found that the Topoformers performed slightly worse than the standard Transformers, but they allowed better interpretability. Furthermore, the authors compared the emerging topographic organization of the language areas obtained from the fMRI experiments with that from the model, and they reported similarity between the two. Overall, I find the ideas to be interesting and I enjoy reading the paper. However, the explanation and quantification of the fMRI results are not clear. It was difficult for me to judge the strength of the results. I will explain in more details below.

### Strengths
Most parts of the paper were very well written. The motivation and the computational approaches were nicely explained.

The idea of incorporating “connectivity constraints” to transformer language models seems to be novel, despite recent work on including such constraints to deep network models in vision. 

The ideas behind  the modeling approach are well explained and the results are promising.

The paper combines modeling and empirical studies based on fMRI experiments.

### Weaknesses
The main weakness I see is that the approach to link the topological structure of the fMRI data to that of the Topoformer model was not well explained and is questionable. These include Section 3.3, Fig 1B, and Fig 6. Also see my questions below.

Specifically, the visualization in Figure 1B lacks clarity; the different colors and their relation to the underlying data are not sufficiently explained. This makes it difficult to assess the validity of the topographic representation. Similarly, Figure 6 suffers from the same issue, making it hard to interpret the spatial correspondence between model and brain. The description of how the weights are visualized on the cortical MNI surface (Section 3.3) is vague, and it is unclear what these 'weights' represent in the context of the model's principal components. The authors state that spatial smoothness in the correlation between model components and brain voxels implies a correspondence between topographies, but this argument needs further justification. The method for quantifying the strength of this correspondence is also missing, making it difficult to evaluate the claims. Finally, the control analysis in Appendix A 6.1, which aims to show a lack of topographic correspondence in a control model, is not convincing. The control model's analysis does not directly compare the Brain-PC correlation map, as shown in Figure 5, making it an inappropriate control.

### Questions
— What does Fig 1b plot exactly? What does the different colors represent?The description in the caption was insufficient for understanding what’s really going on.  Same questions apply for Fig 6. 

— How to interpret the statistics in Fig 4? The calculation of the Typograph statistic is based on Equation 4, but there is a lack of explanation regarding how to interpret it and why this is a good statistics to use. 

— In section 3.3., the authors stated “we then visualized the weights in the cortical MNI surface space (Gao et al., 2015a)”. What doe the “weights” mean here?

— when connecting the data with the model, the authors say “Because we have already shown the spatial smoothness of these components, if we see smoothness in the correlation of these components with voxels/units in the target space, we can infer that there is a correspondence between the two topographies.” This is not obvious to me. I would appreciate if the authors could unpack the arguments. Furthermore, how to quantify the strength of the correspondence?

— The authors performed a control analysis in Appendix A 6.1, i.e. “We sanity-checked that a control model did not show any topographic correspondence with the brain organization (see Appendix A.6.1). ” But I don’t understand why this is the appropriate control because Fig 9 is not about the mapping between the PCs and single units for the control model & brain response. I’d think that one would need a figure analogous to Fig 5, i.e., to show the Brain-PC correlation map under the control model.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
