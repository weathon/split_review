# Zero-shot Concept Bottleneck Models via Sparse Regression of Retrieved Concepts

- Decision: Reject
- Scores: 5, 6, 5, 5, 3, 5

## Abstract
Concept bottleneck models (CBMs) are inherently interpretable neural network models, which explain their final label prediction by high-level semantic \textit{concepts} predicted in the intermediate layers. Previous works of CBMs have succeeded in achieving high-accuracy concept/label predictions without manually collected concept labels by incorporating large language models (LLMs) and vision-language models (VLMs). However, they still require training on the target dataset to learn input-to-concept and concept-to-label correspondences, incurring target dataset collections and training resource requirements. In this paper, we present \textit{zero-shot concept bottleneck models} (Z-CBMs), which are interpretable models predicting labels and concepts in a fully zero-shot manner without training neural networks. Z-CBMs utilize a large-scale concept bank, which is composed of millions of noun phrases extracted from caption datasets, to describe arbitrary input in various domains. To infer the input-to-concept correspondence, we introduce \textit{concept retrieval}, which dynamically searches input-related concepts from the concept bank on the multi-modal feature space of pre-trained VLMs. This enables Z-CBMs to handle the millions of concepts and extract appropriate concepts for each input image. In the concept-to-label inference stage, we apply \textit{concept regression} to select important concepts from the retrieved concept candidates containing noisy concepts related to each other. To this end, concept regression estimates the importance weight of concepts with sparse linear regression approximating the input image feature vectors by the weighted sum of concept feature vectors. Through extensive experiments, we confirm that our Z-CBMs achieve both high target task performance and interpretability without any additional training.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper addresses zero-shot scenario for concept bottleneck models (CBMs). Previous methods successfully eliminate a dependency of manually annotated concept labels via large language models (LLMs) and vision-language models (VLMs). However, they still require training the models on target dataset and not applicable to the zero-shot scenarios. Zero-shot CBMs (Z-CBMs) constructs large-scale concept bank using caption datasets and noun parser, retrievals concept candidates following input images, and predicts final labels using the retrieved concepts. The experiments demonstrate the effectiveness of the proposed method on target task performance and interpretability.

### Strengths
- The paper is well-written and easy-to-follow.
- The main idea is straightforward and intuitive.
- Target task performance is competitive. Table 1 shows that the proposed method even outperforms the performance of the original CLIP, and Table 2 shows that a simple trainable variant of the proposed method outperforms the previous method in the same setting.

### Weaknesses
 - The reason for performance improvement compared to the original CLIP is unclear. The paper argues that it is due to a reduced modality gap in the concept-to-label mapping. However, this claim is not fair since the modality gap still exists in the input-to-concept mapping. Furthermore, since CLIP is trained on image-to-text matching, the claim that performance improves due to a reduced modality gap in text-to-text matching also requires sufficient references.

- I'm not entirely clear on the advantages of this approach over the most basic interpretable approach based on CLIP. Specifically, one could retain the standard CLIP classification process and simply retrieve concepts from a concept bank using visual features for interpretability. While this baseline is hard to address concept intervention, it doesn't seem to offer significant differences in terms of interpretability.

- The performance difference between linear regression and lasso in Table 6 is unclear. Linear regression should estimate the original visual features ($f_V(x)$) more accurately, so why does linear regression perform so poorly here?

### Questions
- Why was linear regression used instead of lasso in L426-427?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper proposes a “zero-shot” concept bottleneck model (CBM). The original idea in CBM is to first represent a given image in the concept space, ie. as a weighted combination of existing concepts and then classifying the image using these concept-weights based image representation. The original works rely supervised training to build image→concept and concept→class predicts. More recent works reduce labelling efforts by leveraging the prior knowledge available in vision-language models (VLMs) and LLMs, e.g. “Label-Free Concept Bottleneck” and others.

The recent works on avoiding supervised concept predictor training however still require a training dataset to train concept→class predictor. This paper basically aims to avoid supervision altogether. The proposed method semi-automatically builds a large concept vocabulary (over existing image caption datasets) , selects the most relevant concepts specifically for a given image according to the image-text representations of a pretrained VLM (eg CLIP) and learns an image-specific concept-text-embeddings to image-embeddings mapping based on reconstruction loss. The resulting concept-embedding based approximation to image’s representation is used to classify the image based on cosine similarity to the textual embeddings of target class labels.


# Post-discussion update
I would like to thank the authors and the fellow reviewers for the fruitful discussions. I’ve read the discussions (including the final responses of the authors), and here is a summary of my opinion:

- I expressed my concerns about the possibly misleading results in Table 1, and the random matrix experiment confirms these concerns. The revised paper, however, mitigates this issue by providing a more cautious discussion and supporting it with additional results. I believe the random matrix experiment should also go into any published version of the paper.
- I found the CLIP-Scores misleading and authors agreed on that. They proposed to address this concern by separating the CLIP model used within the method from the one used in evaluation. While the authors' proposal to separate the CLIP model used in evaluation reduces some bias, it is likely that CLIP models, despite low-level differences, behave in correlated ways. This limitation makes it challenging to establish CLIP-Score as a fully reliable metric.
- I’m “happy” about the hyper-parameter tuning response of the authors, thanks.
- Literature discussion is improved but here I do share the concerns of Reviewer mgBg: the arguments remain too strong in many places, like claiming the model as free of from additional training or data. The fact that somebody else trained CLIP on a gigantic dataset doesn’t alter the dependencies of the proposed approach. The paper shares elements with prior works built on pre-trained classifiers and visual attributes more than what the current text reflects, even after the updates.
- Domain dependence: this is still an open concern, but perhaps not a red flag on its own.

Overall, I remain inclined towards a ‘weak reject’ due to the concerns outlined above. However, in recognition of the thoughtful improvements addressing some of these concerns, I am raising my score to 6.

### Strengths
- The paper’s work is an interesting addition to the research on CBMs. It addresses the missing supervision problem that seems to remain unaddressed in prior CBM work and tackles it in a relatively meaningful manner.
- The XAI-performance results in Table 3 look impressively good.
- The method is simple and easy to understand.

### Weaknesses
 - The paper’s results in Table 1 are not impressive , and this is very much expected as the learned CBM-based representation is afterall an image-specific approximation to the image’s visual representation. It is “normal” that it performs very similar to the CLIP baseline, and I am not sure if the improved performance implies any significant achievement, as the paper lacks any substantial analysis on it (despite commenting that it might be thanks to the reduced representation gap). The core issue is that the method constructs an image-specific dictionary of concept embeddings, and if this dictionary is sufficiently large and diverse, the resulting representation can closely approximate the original CLIP embedding, regardless of the semantic meaningfulness of the concepts. The random matrix experiment, where performance approaches the baseline with increasing K, further supports this concern. The method's ability to approximate the original image embedding does not inherently validate the claim of improved explainability through meaningful concepts.
- It seems to me that the paper’s results in Table 2 (CLIP-Score) can be misleading because it seems to be measuring the average correlation between the image’s CLIP-image representation and the obtained CBM representation. As the CBM representation of this paper is a direct reconstruction of CLIP-image representation, it seems again “normal” (not interesting) to observe high scores. (Please correct me if I’m missing something here.) The concept weights are selected to maximize correlation with the CLIP feature, so it is not surprising that the top-weighted concepts achieve high CLIP-Scores. This raises questions about the informativeness of this metric for evaluating the quality of the learned concept representations.
- How were the hyper-parameters like lambda tuned? Is lambda (and other hyper-parameters, if exists) all the same across all experiments and all datasets? What methodology was used? ie. if one wants to reproduce the exact results from scratch, how should he/she tune the hyper-parameter(s) to reach the same value(s).
- The paper seems to be missing one relevant paper from the zero-shot learning domain: “Attributes2Classname: A discriminative model for attribute-based unsupervised zero-shot learning”. Similar to the proposed work, this paper learns to represent images in terms of a linear transformation of relevant concepts’ (predicted attributes’) textual embeddings, with and without labelled image dataset. It seems to share many motivations like reducing modality gap via representing images in terms of a combination of concept (attribute) textual embeddings and avoiding image supervision, and therefore can/should be discussed within the paper.
- The method heavily relies on the prior knowledge of pre-trained VLM (CLIP), and therefore, cannot be used in incompatible domains; unlike (more) supervised CBMs. In that sense, as this paper already relies on a huge training set that the VLM pre-training requires, it is not clear if any real achievement is made in terms of building human-understandable concept-based image representations with reduced supervision, from a philosophical point of view.

### Questions
- Can you provide more detailed comparisons to prior work by directly using their concept sets? I am a bit lost in understanding how much the comparisons to prior work are directly one-to-one comparable and what elements make a (positive/negative) difference?
- How does the hyper-parameters like lambda for linear regression and lasso affect the results in terms of Table 1, 2, 3 results?
- In regards to the performance gains over CLIP image embedding: how well the method performs if you were to use a random matrix as $F_{C_x}$ in Eq 3 & 4, instead of true concept embeddings, for various K values?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors propose a variant of concept bottleneck models (CBM) which uses sparse linear regression on a databank of concepts to approximate the visual feature of each image. The resulting CBM can achieve reasonable zero-shot accuracy and CLIP-score without additional training. The proposed framework does not require additional data.

### Strengths
(1) The method is simple.

(2) The results are good. The authors show that their ZS-CBM achieves SoTA accuracy among prior CBMs. They also demonstrate the quality (relevance) of the selected concepts using CLIP-score results.

### Weaknesses
I can't find anything wrong with this paper except perhaps the lack of technical innovation. There is abundant literature on concept bottleneck models. Sparse regression on concept features is very widely used. Using retrieval to find relevant concepts is not technically interesting. In my opinion, this work does not add much value to the existing CBM literature.

### Questions
None.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper utilizes a large-scale concept bank and a dynamic concept retrieval method to make high-accuracy predictions without requiring additional training on a target dataset. By employing sparse regression to identify and weigh the importance of relevant concepts from the bank, Z-CBMs achieve effective concept-to-label mappings while ensuring model interpretability, addressing the limitations of previous concept bottleneck models that relied on extensive manual data collection and training.

### Strengths
1. To the best of my knowledge, this paper is the first to propose a zero-shot Concept Bottleneck Model (CBM), marking a significant contribution to the field of CBMs. Furthermore, the proposed zero-shot CBM method exhibits predictive capabilities comparable to those of CLIP, while its architecture enhances the model's interpretability.

2. The experiments presented in this paper are comprehensive and well-executed, encompassing 12 datasets. Despite the absence of suitable benchmarks, the authors have effectively compared their method with zero-shot CLIP and other training head approaches.

3. This paper introduces the concept of a "concept bank" and employs an efficient concept retrieval method for label prediction based on this foundation. The concept bank is constructed through the analysis of extensive datasets. In Section 4.6.2 and Table 1, the authors provide a detailed comparison of zero-shot performance across different sizes of concept banks, demonstrating that expanding the concept bank enhances the expressive capacity of the CBM, thereby improving its zero-shot performance.

### Weaknesses
1. While this article provides a valuable comparison of various methods related to the concept bank, it appears that the testing results for a specific approach—constructing a concept bank using a question-and-answer method similar to the label-free CBM [1]—are not included. Including this method, particularly in the context of designing a smaller, domain-specific concept bank, could enhance the comprehensiveness of the analysis. I encourage the authors to include a comparison with a concept bank generated using the question-and-answer approach from the label-free CBM, as this would provide a deeper understanding of the different concept bank construction approaches.

2. The paper mentions that the regular term in sparse regression can help reduce conceptual redundancy; however, it lacks specific visual results to illustrate this effect. Additionally, the advantages of using sparse regression in comparison to other distance metrics in feature space for weight determination are not clearly established. To strengthen the paper, I suggest that the authors provide visual examples comparing the concepts selected by sparse regression versus other methods, demonstrating how redundancy is reduced. Furthermore, including a quantitative comparison of sparse regression against other weighting methods would enhance the clarity and convincing nature of the proposed method.

### Questions
1. This article compares various methods related to the concept bank. However, I may have overlooked the testing results for a specific approach: constructing a concept bank using a question-and-answer method similar to the label-free CBM [1]. This involves designing a smaller concept bank tailored to the problem domain.

2. In this paper, it is mentioned that the regular term in sparse regression can help reduce conceptual redundancy. Could you please provide some specific visual results to illustrate this effect? Additionally, I’m curious about the advantages of sparse regression compared to using distance or other metrics in feature space to determine weights. If there are any experimental results that demonstrate this comparison, it would certainly enhance the persuasiveness of the method presented in your paper. 

3. I noticed the inference time presented in Figure 6. Could the authors clarify whether this represents the total time for the entire zero-shot inference process? As the scale of the concept bank expands, it is important to understand how embedding and concept retrieval times may increase. I would appreciate it if the authors could provide a breakdown of the reported times, detailing the components of the inference process (e.g., embedding, concept retrieval, regression) and how these times are affected as the concept bank size increases.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
In this paper zero-shot concept bottleneck models are discussed as a means of obtaining explainable (in terms of concepts) zero-shot classifiers (as in classes without explicit training data). The idea is to use a concept bottleneck model to translate an image into a set of visual concepts, and then use these concepts to classify the image into one of the target classes of the benchmark dataset. Since the train/test data of the benchmark data is not explicitly used, this is a form of zero-shot classification. In the proposed method, the concept bank consists of about 5M concepts obtained from image captioning datasets (including e.g. Flickr-30K and the YFCC-15M dataset). The image and all the concepts are encoded in the CLIP embedding space, and then the top K most similar ones are used. From this set of concepts a sparsely weighted CLIP feature vector is constructed, which is then used to find the nearest target class y. This model is evaluated on 12 classification tasks and performs similar to zero-shot CLIP.

### Strengths
The ideas presented in this paper make a lot of sense, and the manuscript is clearly written. The relevance becomes clear from the amount of related research in this direction of ‘attribute-based’ or ‘concept-based’ zero-shot classification, which dates back at least to 2010s. However, this is also the largest weak point of the paper, the novelty compared to papers and ideas presented back then is not clearly stated, nor is the paper compared to any other zero-shot method besides retrieving in the CLIP space. Of course some techniques / methods did not exist back then (eg the CLIP embedding space), that does not make this paper substantially different.

### Weaknesses
## Major weakness
The major weakness of this submission is the novelty with respect to previous work (likely of a previous generation, before deep learning took off). The idea of zero-shot classification in a visual-semantical space based on a joint embedding is not novel. A good example is [**ConSe 2014**], where imagenet classifiers are used together with a Word2Vec space to compose a Word2Vec embedding for an image (based on the classifier outputs and the word embeddings of the class names], which is then used for zero-shot classification in text space. This is extremely similar to the posed idea, except that now a CLIP space is used. Also the idea of using a (sparse) regression of the concepts has been explored before [**Write 2013, Costa 2014, Objects2Actions 2015**]. None of these papers uses an explicit attribute/concept-to-class mapping as the seminal work of Lampert et al. [**AwA 2013**], they all used a discovered attribute-to-class mapping based on an embedding space [**ConSe 2014, Objects2Actions 2015**] or based on co-occurrence statistics or web search [**Costa 2014**], including co-occurences from the YFCC dataset, also used in this work.

The *only* difference I see with respect to these works, is that the concept bank used in this paper is much larger and that a CLIP embedding is used. Based on the previous works, the following questions are interesting, but not explored in this submission:
- The weighting of concepts is now based on the input image, it could also be done based on the target classes (ie, each class selects the top-K concepts which are most similar, or find the most co-occurring concepts in the captioning datasets)
- The weights of a concept in the linear regression model can be negative, this is unlikely to be beneficial given that the used concepts are the top-K most relevant for this particular image. Would it make sense to restrict W to be positive? 
- What is the influence of lambda on the performance? And on the sparsity? Is the optimal lambda dataset specific? It seems that the current value (1x10-5) is extremely small, compared to the size of W (which has K weights, with K ~1000). 
- Using proper negative concepts for a class is likely to be beneficial, given that knowing what is not related to the target class is a strong signal, could that be explored as well?
- What similarity function is used in the clip space? Is it cosine similarity? Is Fcx W normalized?
- The similarity between a concept and the image is now an indicator function only (concept in top-K concepts for this image). While, the similarity value might contain a strong signal of relevance. It could make sense to use the similarity value between the image and the concepts also in constructing the concept clip embedding of the image.

## Secondary weaknesses / suggestions
1. The second step, the final label prediction (Eq 4) is a purely textual reasoning problem. In the light of the enormous reasoning power of the LLMs, it could be explored if LLMs would be able to reason about the final class provided the top-K concepts from the previous stage.

2. A suggestion for an additional exploration. In this submission, the CLIP space is searched in a cross-modal setting, from an input image to a target/output text. While in [**ReCo 2024**] it has been shown that uni-modal search works much better (image-image) and then use cross-modal fusion (use the textual description of that image). This could be exploited (e.g.) by using (image, caption) pairs from the image datasets. It would be interesting to study if different search strategies improve the zero-shot classification performance.

### Minor/Nitpicks
- In table 1: the bold facing of performance should include the zero-shot/linear-probe CLIP.
- It is unclear why the zero-shot CLIP model should be considered as the upper bound of the proposed method. The proposed method uses the (implicit) knowledge of millions of additional (image, text) pairs.

### Questions
1. The main question is how is this work different from [**ConSe 2014**] (and other similar works), and then beyond that they use an ImageNet classifier to transform images to text, and here a CLIP space has been used. So, please clarify what novel contributions the method makes beyond using a CLIP embedding space instead of Word2Vec + ImageNet classes? 

2. Please clarify: (a) the used CLIP similarity function, (b) Fcx W being normalized, (c) the influence of lambda.

3. Please discuss the open directions (taken from previous research): weighing based on target classes, restricting W to positive weights only, using negative concepts in a proper manner, using similarity value.

3. From Figure 3 it becomes clear that some concepts are negated, for example `NOT macro rope` (bottom row, right). How is this defined? Is the `not` a part of the concept, and hence used encoded in `f_T(concept)` vector, or is the `not` a result of the linear regression, for these concepts with a negative weight in W? Please elaborate whether it is conceptually desired that concepts in the top K most related concepts for an image could be negative weighed for the image-text embedding.

### Soundness
4

### Presentation
3

### Contribution
1

---

## Human Reviewer 6

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposed a novel approach for achieving zero-shot image classification based on explainable Concept Bottlenecks. Compared with existing Concept Bottleneck Models, the authors proposed approach gets rid of the requirement of labelled training data for learning the mapping network from concepts to categories by fitting the image representation with concept features. The experimental results verified the effectiveness of this approach.

### Strengths
This paper provides a novel interpretable zero-shot image classification method.

Compared with existing Concept Bottleneck Models, the proposed method eliminates the requirement of labeled training data.

This paper provides a tool for researchers to understand the semantics of CLIP-extracted visual features.

### Weaknesses
The inference cost is significantly increased due to the extremely large concept bank and the test-time learning process.

This paper lacks discussion of other training-free concept bottleneck approaches, e.g., “Visual Classification via Description from Large Language Models”.

The interpretability of the candidate concepts is questionable. Concepts such as “Not maltese dog terrier” do not provide clear, human-understandable information for identifying categories, and the paper does not adequately address the issue of concept granularity or negative concepts.

### Questions
The authors may consider comparing the inference speed between the proposed approach and existing CBMs.

I’m wondering whether the visual and textual features are in the same space as shown in Fig 2 (a) for fitting image features with textual features of candidate concepts, considering that they are from two modalities and in the pre-training stage, the text features and visual features are aligned by cross-entropy loss rather than strictly calibrated by L2 Loss. The authors may consider showing a t-SNE figure to clarify this.

The authors may consider evaluating the interpretability of the candidate concepts. In my opinion, concepts such as “Not maltese dog terrier” cannot provide interpretable information for identifying categories.

### Soundness
3

### Presentation
3

### Contribution
3
