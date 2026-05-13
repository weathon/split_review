# A Simple Interpretable Transformer for Fine-Grained Image Classification and Analysis

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
We present a novel usage of Transformers to make image classification interpretable.     
Unlike mainstream classifiers that wait until the last fully connected layer to incorporate class information to make predictions, we investigate a \emph{proactive} approach, asking each class to search for itself in an image. We realize this idea via a Transformer encoder-decoder inspired by DEtection TRansformer (DETR). We learn ``class-specific'' queries (one for each class) as input to the decoder, enabling each class to localize its patterns in an image via cross-attention. We name our approach INterpretable TRansformer (\Ours), which is fairly easy to implement and exhibits several compelling properties. We show that \Ours intrinsically encourages each class to attend distinctively; the cross-attention weights thus provide a faithful interpretation of the prediction. Interestingly, via ``multi-head'' cross-attention, \Ours could identify different ``attributes'' of a class, making it particularly suitable for fine-grained classification and analysis, which we demonstrate on eight datasets.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces Interpretable Transformer (INTR), a classifier that builds on the standard Transformer architecture. It leverages the cross-attention and a set of learnable class-specific queries to introduce by-design visual explanations for each class. The interpretability of INTR comes from the ability to track the cross-attention weights during inference, showing which parts of an image are being considered when making a prediction. The model proves to be effective in not only identifying parts of objects like bird heads but also in distinguishing between species by recognizing subtle attributes. The decrease in classification accuracy compared to ResNet is not a big deal but the evaluation that is mostly qualitative makes me question about its utility. Found details below.

### Strengths
- The presentation is clear and structure is easy-to-follow.
- I like the idea of manipulating distinctive features in Figure 5 and believe the authors could relates to Causal inference.
- I like the honesty in Table. 2 where the authors show the bad performance of INTR over different datasets.

### Weaknesses
 - As this paper’s evaluation contains mostly qualitative results (e.g. showing the visualizations and explanations of INTR), it would be great if they can show the real utility of the explanations for a human-related task [a]. In this case, the decreases in accuracy shown in Table. 2 can be completely negligible. Otherwise, I still see ResNet clearly better than INTR (although this is not a major point).
- The authors may also want to evaluate the explanations using proxy metrics in XAI.
- It has been unclear to me whether the bad performance of INTR stems from the capability of query vectors or not? It would be great if the authors have ablation studies for the query vectors (e.g. for classes with high inter-class variations, a simple vector could not be representative for the whole class). Also, how do they affect the explanations.
- The number of heads is equivalent to the number of concepts in ProtoPNet and its variants. For CUB, I believe the number of distinctive features is less than 8 (to my experience). Then I believe this number of heads should be adjusted according to the dataset.

### Questions
N/A

Post-rebuttal reviews:

I genuinely appreciate your great efforts put into this rebuttal!
# Real utility of the explanations.
Authors insisted that:

> In our current paper, the targeted real utility is indeed automatic attribute/trait identification and discovery for organisms.

and in Sect. G, they provided more context:

> These traits are grouped into four categories: 1) habitat and context, 2) size and
morphology, 3) color and pattern, and 4) behavior. Figure 1 shows that INTR can extract the first
three categories from the static images, while behavior typically requires videos.

However, looking at Fig.1, it is unclear how INTR extracts size and morphology information. For added context and background, simply highlighting background pixels provides only loose support for INTR's ability to extract habitat-related traits. There is a need for a systematic evaluation of INTR's efficiency in trait discovery. Currently, most of the claims about its utility are subjective and unconvincing..

# Evaluate the explanations using proxy metrics in XAI.

As authors also stated that: 
> For self-interpretable methods like ProtoPNet, ProtoPFormer, ProtoTree, and our INTR, which build specific classifiers, XAI metrics are seldom reported as they may not be fair across different methods.

The current evaluation using deletion and insertion as proxy metrics appears to be of limited significance. A more meaningful benchmark would involve comparing the explanations with other concept-based, self-interpretable classifiers, rather than relying on post-hoc explainers. 

# Performance of INTR.

Does increasing M to 2 equate to doubling the number of heads, in terms of the concepts to be learned? In Fig.20's bottom row, while increasing M can rectify misclassifications, the resultant explanations tend to be noisier. I hope authors will revise this for the next version.

# Overall

I again thank the authors for the incredible efforts in the rebuttal. Given that the authors partially addressed my concerns, I will increase the score from 5->6.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a method called feature accentuation. It is a new explainability method that it indicates which pixels in the image are relevant for the final decision of the model. As well as which kind of features activate relevant neurons.

### Strengths
A strength of this method is not needed auxiliary generative models and being seeded to images. 
Also, the release as an open-source library as part of Lucent will make it accessible to those who would like to use it for their applications or built on top of it.

To overcome some gaps from previous related research, this methods incorporates several techniques  to avoid that the modified image that accentuates some feature changes how it activates the neuron’s with respect to the original seed image as a regularisation term in the loss. There is an analysis on which layers play an important role to avoid undesired distortions, and it is reported that enforcing it in earlier layers yields better visualizations in early layers. An analysis in the impact of regularisation, parametrisation and augmentation techniques from the literature applied in this method is conducted, highlighting the right combination of those factors. Additionally, to improve relevance of the feature representations, a global normalisation is proposed

The experiments reported use circuit coherence assessment from another paper, which is a reasonable measure.

### Weaknesses
The other applications showcased are also of high importance, but the results become more difficult to assessed. How confirmation biased is overcomed with this method? It is still based on visualisations which need human assessment. The what is based on visual information that is difficult to parse for a human. How useful then it really is still an open question. This is already mentioned in limitations, but it is a strong self-critic that should be given more thought on how to overcome those. How to in corporate over tools for the interpretation is also not clear.



MINOR:
There is a reference missing with a question mark. There are a couple of blank space missing to segment words.

### Questions
Please refer to weakness points.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors present a method that uses Cross-Attention in a Transformer Encoder-Decoder setup to provide interpretable insights how classification results are obtained. By learning class-specific queries as input to the decoder paired with a shared class-agnostic weight vector, the method checks in an intuitive way whether each class can be located in an image, and which attributes within the image lead the ‘classifier’ to believe a certain class is present/dominant – providing a faithful way of interpreting how the decision was made (via visualization of the respective attention patterns).

### Strengths
### Quality:  
- Method is described in sufficient detail, including the intuitions underlying each component; Authors additionally do a good job in providing enough mathematical background to clearly follow the inner workings in a concise way;
- Conducted experiments clearly outline and support the intended contributions, mostly via illustrations of ‘qualitative’ results
- The level of detail provided in Section 3.4 is very helpful to further understand underlying motivations and inner workings of the method; 
### Clarity:  
- Very easy to read and follow, very well-structured manuscript; The author’s do an excellent job in posing questions that are then answered to clearly articulate their goals; Good use of illustrations to create compelling story line
### Originality & Significance: 
'Originality' is (as often) slightly tricky here: The underlying idea of using cross-attention between learnt queries that try to locate itself in the image is pretty much directly adopted from DETR – as the authors themselves correctly state.   
&#8594; The originality of this work hence mainly lies in the application to use this technique for better interpretability, which is paired with/supported by their way of performing classification to support faithfulness of the involved attention patterns;   
Considering these points, I do support the author’s claim of originality in this sense, especially thanks to the explicit consideration of the faithfulness aspect.

### Weaknesses
 **TLDR:** While one could potentially criticize the novelty in terms of methods, I do think this work clearly outlines a different and interesting perspective how CA can be used to increase interpretability in a (more) faithful way. Paired with the well-structured manner the manuscript is prepared, I lean towards recommending acceptance of this work — and am happy to further increase my score if the authors can address my questions & concern (mainly 1st weakness).

---
*Missing discussion of the encoder’s potential influence*:   
The (potential) influence of the encoder is not really discussed in this work; Standard DETR already employs a quite large CNN to ‘encode’ the information into embeddings, and one could argue that certain ‘decisions’ as to what is important are already made there. Note that the receptive field of each element of the feature map emitted by the encoder is substantial (potentially even global, esp. when ViT is used) and therefore could incorporate information of various locations throughout the actual input image.     
&#8594; Please correct me if I’m wrong, but the CA essentially shows us to which locations of the feature map the classifier is paying attention to – which does not necessarily have to directly correspond to the input image? I’d like to see some discussion/clarification of this point.

---
*Known and stated weaknesses/limitations, but still worth pointing out*: 
-  Self-attention in the Transformer Decoder quickly becomes prohibitive – as the authors correctly state. It however still worth noting that the complexity in memory and time grows quadratically with the number of classes due to the self-attention operation performed across the class-specific query tokens.  
  
    &#8594; I’d be curious to know whether the authors might have some suggestion whether all classes are required to be included as decoder input ‘all the time’, or whether some pre-selection could be performed to reduce the computational complexity, at least at inference time.


- Influence of pre-training: The authors state that they employ the DETR model pretrained on ImageNet and MSCOCO – which is a lot of data that importantly provides various different aspects of images (classification, as well as (multi-object) detection data);   
Note: The authors acknowledge this fact in the manuscript, but it is still worth pointing out since it is a potential point of concern that’s introducing some uncertainty as to how backbones that are trained on less data or ‘only ImageNet’ might perform when paired with INTR.

### Questions
**Main Questions connected to previously mentioned 'weaknesses'**: 

- Related to **Influence of Encoder**: As previously detailed, the CA shows to which locations of the feature map the classifier is paying attention to – which does not necessarily have to directly correspond to the input image, especially for architectures with global receptive fields. Do the authors agree with this? What are the (potential) implications of this towards the interpretability of the presented approach?

- Related to **Efficiency**: Do the authors see any possibility to improve efficiency of the method in terms of preventing quadratic growth w.r.t. the number of classes? (and thus increasing the ease of applicability towards datasets with more classes)

- Related to **Pre-training influence**: Did the authors experiment with training from scratch, e.g. on ImageNet, as well? (One alternative could also be using a (frozen) pre-trained backbone and train the 'remainder' of the architecture (Transformer decoder) on only ImageNet); Do the authors have any insight as to how much training on a detection task might help with focusing on detail, and whether this makes any difference to 'simple' classification pre-training? 


---
Some additional questions (mainly out of curiosity):

- I’d like to get some more insight regarding the importance of the shared ‘w’ vector to perform the classification; While I do understand the intuition, would the result of learning distinct representations differ if the representation itself was just averaged, i.e. ‘w’ would simply be 1/len(w)? 

- Simply out of interest: Did the authors encounter images with multiple objects during their experiments? If so, was their method able to actually locate these individually within the image if queries for the (multiple) ‘correct’ classes existed? If not, how would the authors expect the method to behave – ‘correctly’ finding e.g. 2 objects in an image, or do the authors expect that such use cases will cause issues? (Such a case could potentially be constructed by simply concatenating 2 partial images)

---
Comment:   
- It might be worth changing the way how HxW is described: The authors consistently describe ‘H’ and ‘W’ as the ‘number of grids’ – however, I’d strongly suggest to instead refer to the elements as “grid cells”, since at least I would see the entire image/matrix HxW as the grid, with H and W indexing the ‘grid cells/elements of the grid’


-----
**Post rebuttal update:**  
I'd like to genuinely thank the authors for their detailed answers and the effort invested into this rebuttal!  
My main concerns regarding the encoder's influence (receptive field) and pre-training have been partially addressed;  
I do however see some remaining challenges in the presented insights regarding reduced interpretability when using a different backbone: While I agree with the authors' statement that reuse of pretrained backbones is legitimate (and should be encouraged), the results show that using another (non-DETR) pretrained backbone (e.g. the presented ViTs in Fig.22) significantly hinders the efficacy of the presented INTR; This might be due to misalignment, but note that if the method should be useful, it must be applicable to a variety of backbones of interest, not just to one specific combination that has been optimized for DETR; Whether the method transfers well onto other architectures of choice still remains somewhat open/not entirely satisfyingly resolved.  
$\rightarrow$ That said, I do think the paper presents a novel and insightful take on interpretability. After reading the other reviews, I decided to stick with my initial rating.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper presents an interpretable learning framework using Detection Transformer (DETR) for fine-grained classification, namely INTR.

Specifically, learning "class-specific" queries, performing the cross-attention between the queries and the feature maps to obtain "class-specific" features, then a "class-agnostic" "presence" vector to determine where this query (class) is found in the image or not.

This paper also presents a mathematical explanation to unveil how the proposed framework learns.

This paper also presents a few ways to analyze the interpretable classification results, such as image manipulation to monitor changes in cross-attention & the classification score, and fine-grained attributes visualization analysis.

The experiments are mainly performed with fine-grained recognition datasets.

### Strengths
originality: While not novel (directly incorporating DETR), this paper rethinks the purpose of DETR and applies it to interpretable learning, also providing a valid mathematical explanation to show why and how the queries learn.

quality: This paper has presented experiments to show the benefit of the proposed interpretable framework. the method is straightforward and is easy to implement.

clarity: The paper is well written. The results are quite clear. But some presentations can be improved, for instance, in fig 5, the author can also show the changes in the attention map (like the one in fig 6). For Fig 4, I am not sure what to look at.

significance: Interpretability is a well-established problem but we still don't have a completely interpretable framework. I think this paper is somehow significant to affect the community. The idea of this paper is simple, this may inspire future works to improve upon this work.

### Weaknesses
- Lack of interpretability analysis. As mentioned by the author this paper is not about accuracy, hence I shall expect more quantitative/qualitative experiments to fully understand inner works. Since the author says INTR can detect the "attributes", the author can measure how precise the model can detect. What is the "accuracy" in detecting the attributes (e.g., Sec 4.2 of [1])? What are the captured attributes? Are these attributes shared or different among the different classes (e.g., it can detect the stripe of a bird, are they the same stripes or different in colors/patterns)? Why is that? I think all these results can be shown in the main paper.

- Comparison with other interpretable models. The only comparison I noticed is Fig 3. Are other models not able to identify attributes like INTR does? How do you quantitatively measure it? From what I see in this figure, ProtoPFormer is also able to locate local attributes, but there are not enough samples here.

- Image manipulation experiments seem not systematic enough, how do you measure the changes? E.g., after manipulating the "part", how many images changed the classification results? Are they still the correct or the wrong results? 

- The attention map now looks a bit not "clean" enough, when some attributes cannot be detected from the image, I suppose the attention should be empty instead of looking at the background, if it is looking at the background, does it mean it is a feature? or it is overfitting? The author did not further analyze it.

- the sentence "Fortunately, fine-grained classification usually focuses on a small set of visually similar classes; C is usually not large." may be not true, iNaturalist [2] has 10000 classes, and even the "bird" classes alone have 1478 classes.

### Questions
1. What is the "accuracy" in detecting the attributes (e.g., Sec 4.2 of [1])? What are the captured attributes? Are these attributes shared or different among the different classes (e.g., it can detect the stripe of a bird, are they the same stripes or different in colors/patterns)? Why is that?

2. Are other models not able to identify attributes like INTR does? How do you quantitatively measure it?

3. How do you systematically perform the image manipulation experiments? You should also measure the result quantitatively.

4. I understand that the attention map is not regularized by any loss functions so the attention maps may look weird. But how do you explain the attention focus on the background, but sometimes focus on the "attributes" (e.g. Fig 13)? How can we know what attributes will fire up which heads?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
2 fair
