# Decompose the model: mechanistic interpretability in image models with generalized integrated gradients (GIG)

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 3, 6, 6

## Abstract
In the field of eXplainable AI (XAI) in language models, the progression from local explanations of individual decisions to global explanations with high-level concepts has laid the groundwork for mechanistic interpretability, which aims to decode the exact operations. %, particularly in language models. 
However, this paradigm has not been adequately explored in image models, where existing methods have primarily focused on class-specific interpretations.
This paper introduces a novel approach to systematically trace the entire pathway from input through all intermediate layers to the final output within the whole dataset.
We utilize Pointwise Feature Vectors (PFVs) and Effective Receptive Fields (ERFs) to decompose model embeddings into interpretable Concept Vectors.
Then, we calculate the relevance between concept vectors with our Generalized Integrated Gradients (GIG), enabling a comprehensive, dataset-wide analysis of model behavior.
We validate our method of concept extraction and concept attribution in both qualitative and quantitative evaluations.
Our approach advances the understanding of semantic significance within image models, offering a holistic view of their operational mechanics.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The author proposed an architecture that can trace the pathway from the input to the output across the dataset. Specifically, the author first uses pointwise feature vectors (PFVs) and instance-specific effective receptive fields (iERFs) to generate concept vectors (CVs). Then the author introduces a new method called Generalized Integrated Gradients (GIG) to capture the contribution of a specific concept vector in a layer to both the final output and concept vectors of subsequent layers. Moreover, the author provides extensive experiment results to validate the effectiveness of the proposed method.

### Strengths
1. The paper is well-organized and easy to follow.
2. The author provides extensive experiments that can validate the effectiveness of the proposed method.

### Weaknesses
1. In Figure 3, the author demonstrates that concept 3 represents the 'rounded cone'. It is better to provide more diverse examples. The current examples are mostly noses which are not sufficient to prove that concept 3 represents the 'rounded cone'. It is better to provide more non-animal cone-shaped examples.

2. For the PFV decomposition, it is better to normalize the total contribution to 1, which can not only help to compare the contribution for each concept but also provide more information when a concept is an inter-class concept. It can provide a better comparison for the inter-class concept. Currently, I cannot fully understand why the decomposition has a result like 39.4 $\times$ concept 1 in the top left of Figure 7, how to understand 39.4 in this example while the concept that contributes most to the result in the bottom left of the example that in layer 4.2 block is only 7?

3. In the Figure 5 Insertion experiment, for the result of layer 3.5 to layer 4, there is a huge drop when inserting the final 5%. However, for the previous layers, there is no such phenomenon. Is there any explanation for this phenomenon?

### Questions
N/A

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a approach for achieving mechanistic interpretability in image models by systematically tracing data flow through all intermediate layers to the final output across an entire dataset, which borrow from ideas from the language models. The authors propose the use of Pointwise Feature Vectors (PFVs) and Effective Receptive Fields (ERFs) to break down model embeddings into interpretable Concept Vectors. The relevance between these Concept Vectors is quantified using a new technique called Generalized Integrated Gradients (GIG). This methodology provides some analysis of model behavior, moving beyond class-specific explanations and offering a holistic, dataset-wide view of model interpretability. Experiments on ResNet50 demonstrate the effectiveness of this method in both qualitative and quantitative evaluations.

### Strengths
1. The introduction of PFVs, ERFs, and the GIG technique represents a viable approach in the field of interpretability for image models. This methodology offers a step towards deeper understanding by focusing on dataset-wide explanations rather than individual class explanations.
2. The authors provide a visualization GUI to help me clearly understand the effectiveness of GIG.

### Weaknesses
1. The novelty of this paper is uncertain. It appears to be a straightforward adaptation of mechanistic interpretability analysis from the field of large models, with only minor modifications, such as the introduction of GIG. I recommend that the authors provide a theoretical justification to demonstrate how GIG delivers more accurate and robust interpretability for each concept. By the way, such idea is quite similar to LRP.
2. The paper lacks a clear definition of concept, which is essential for understanding the methodology. Additionally, the definitions of PFV and ERF are somewhat ambiguous, as it is questionable whether DNNs make decisions based solely on individual pixels. In certain models, such as ViTs, decisions may also be patch-based. Clarification on these definitions and their applicability is needed.
3. While the proposed approach seems effective, it may face scalability challenges when applied to large models or datasets due to the computational expense of calculating PFVs and performing clustering. The paper does not adequately address the computational implications of this approach, especially for larger architectures.
4. The paper provides a single example using the ResNet-50 model, which is relatively shallow compared to current large models. To more thoroughly validate the proposed method, additional results using deeper models, such as ViT or CLIP, would be beneficial. Expanding the evaluation to these models could further support the approach’s robustness and generalizability.
5. Minor: most of the figures are not scalable vector graphics.

### Questions
1. What is the sensitivity of the method to hyperparameters like the number of clusters in bisecting k-means? It would be helpful to understand how robust the method is to changes in these parameters, as well as any guidelines for selecting optimal values.
2. How does GIG compare in computational performance with other attribution methods? Given the additional complexity introduced by GIG, a comparison of computational efficiency with methods like integrated gradients or SHAP could help users assess the trade-offs of this approach.

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
4

### Summary
The paper presents a novel approach to mechanistic interpretability in image models, utilizing Pointwise Feature Vectors (PFVs) and instance-specific Effective Receptive Fields (iERFs) to decompose features into concept vectors, followed by Generalized Integrated Gradients (GIG) for inter-layer concept attribution. The authors focus on dataset-wide analysis in ResNet50, aiming to uncover “shared concepts” that transcend individual classes.

### Strengths
+ The combined use of PFVs, iERFs, and GIG offers a comprehensive pathway for analyzing inter-layer relationships in image models.

+ By moving beyond class-specific interpretations, this method identifies cross-class shared concepts, broadening its utility in analyzing dataset-wide patterns.

### Weaknesses
 - Defining “concepts” as features across channels is ambiguous and possibly arbitrary. The choice of clustering method and number of clusters affects concept formation, raising concerns about consistency and potential cherry-picking. Specifically, the method does not provide a clear justification for why features across channels should be grouped together to form a concept, rather than considering individual feature maps or combinations of feature maps within a channel. The lack of a principled basis for this grouping introduces a degree of arbitrariness that could lead to inconsistent or unstable concept representations. Furthermore, the sensitivity of the results to the clustering algorithm and the number of clusters chosen is a significant concern, as it implies that the identified concepts are not inherent properties of the model but rather artifacts of the analysis process.

- The clustering and inter-layer attribution processes, especially GIG, are computationally intensive, limiting the approach’s scalability to larger models and datasets. The computational burden of clustering Pointwise Feature Vectors (PFVs) and subsequently applying Generalized Integrated Gradients (GIG) for inter-layer attribution is substantial. This computational cost makes it difficult to apply the method to larger models with more parameters or to analyze datasets with a large number of images. The practical applicability of the method is therefore limited by its computational demands.

- The study primarily focuses on the ResNet50 model, which is convolutional and has a relatively straightforward layer structure. The approach may not directly extend to transformer-based models or architectures with more complex connectivity patterns, limiting its general applicability to other modern architectures. The reliance on PFVs and iERFs, which are defined in the context of convolutional layers, makes it unclear how these concepts would translate to transformer architectures, which operate on attention mechanisms and token embeddings. The method's applicability to models with skip connections or other complex connectivity patterns is also not addressed, raising concerns about its generalizability.

- Clustering PFVs to form concepts may lead to a loss of granularity in capturing finer details, as individual nuances in features could be overshadowed when grouped into larger concepts. This limitation could make the approach less effective for tasks requiring detailed feature analysis, such as fine-grained object recognition. The aggregation of features into clusters could obscure subtle but important variations in feature activations, potentially leading to a loss of information that is critical for tasks requiring high precision.

- Concept extraction and the interpretability of these concepts can be subjective. Evaluating whether the extracted concepts are meaningful or correctly represent features within the model’s decision-making process is challenging, as human evaluators may have differing opinions on the quality and relevance of these concepts. The reliance on human judgment for evaluating the extracted concepts introduces a degree of subjectivity that makes it difficult to objectively assess the validity of the method. The lack of a clear, objective metric for evaluating the quality of the extracted concepts is a significant limitation.

- The method does not include robustness testing for the identified concepts, such as how stable they are under input perturbations or across different initializations of the same model. This lack of robustness testing limits the reliability of the concepts for understanding model behavior across varying conditions. The stability of the extracted concepts under adversarial attacks or other input perturbations is not evaluated, which raises concerns about their reliability for understanding model behavior under varying conditions. The lack of testing across different initializations of the same model also limits the generalizability of the findings.

### Questions
see Weaknesses

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
5

### Summary
This paper proposes an XAI method that first identifies $K$ essential features in each layer, along with their visual cues, using a small image dataset. It then determines the impact of these features on subsequent layers and on the final classification output. This method is model-agnostic and can be applied to both CNNs and ViTs. Rather than providing class-specific explanations, it offers dataset-wide explanations.

### Strengths
- They propose a method to analyze the model's features across an entire dataset.
- They provide effective visualizations to convey their insights.
- They use instance-specific Effective Receptive Fields (iERF) to label each identified feature.
- They propose a method to trace a path from input to output, rather than in the reverse direction.
- Their model does not require any additional training.

### Weaknesses
 - Even with iERF, there is no guarantee of finding a meaningful representation (a human-understandable part across multiple images) for each concept. The method relies on the assumption that the identified features will correspond to semantically coherent concepts, which is not always the case. The iERF might highlight a spatially localized region, but this region may not have a consistent interpretation across different images or even within the same image under varying contexts.
- Using ImageNet validation to identify concepts may be limiting, as this dataset may not contain all the features the model has learned during training. The ImageNet dataset, while extensive, is still a finite collection of images and might not represent the full spectrum of features that a model learns, especially if the model was trained on a different or larger dataset. This could lead to a biased or incomplete understanding of the model's internal representations.
- Some parts of the paper are unclear and difficult to understand, such as the last two sentences of the first paragraph in Section 3.2.1. The description of how Pointwise Feature Vectors (PFVs) are sampled is not sufficiently clear, making it difficult to understand the exact procedure and its implications. The probabilistic sampling based on contribution to output logits needs more detailed explanation.
- When clustering to find concepts, some may be over-segmented while others may not be segmented at all. The use of k-means clustering, while common, is sensitive to the choice of k and can lead to inconsistent segmentation results. Some concepts might be split into multiple clusters, while others might be grouped together, obscuring the true underlying structure of the feature space.
- In Section 4.2.1, you state: "However, as seen in the bottom part of Fig. 4, while the concepts from ‘Ours’ are human-interpretable, those from SAE seem ambiguous and even irrelevant to the class." However, your method may also detect non-meaningful features in some cases. The claim of superior interpretability compared to other methods is not fully justified, as the method itself is susceptible to identifying non-meaningful or spurious features.
- Not all identified concepts are meaningful, as seen in Figure 9, where the first row of concepts in the top-left example lacks interpretability. The qualitative results show that some of the identified concepts do not correspond to easily understandable visual features, raising concerns about the overall reliability of the method.

### Questions
- In Section 3.2.1, why did you choose 1 PFV per image-layer? Why not choose 2? What happens to the discovered concepts if this number varies?
- How do you determine the number of clusters? As you know, this has a strong correlation with the dataset being used.
- Why is the claim made in the last paragraph of Section 3.2.2 correct? How do you justify it? What if the discovered concepts are interdependent and unable to span the space where PFVs exist?
- Do the values represented for $l_0$ (ratio) in Table 1 indicate that most of the coefficients are zero and that PFVs are represented by only a few concept vectors?
- In Figure 5, under Deletion, from Layer 2.3 to Layer 3.0, why does the blue line rise at the end?

### Soundness
3

### Presentation
2

### Contribution
3
