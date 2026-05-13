# Interpreting CLIP's Image Representation via Text-Based Decomposition

- Decision: Accept
- Scores: 8, 8, 8, 8

## Abstract
\vspace{-.5em}
   We investigate the CLIP image encoder by analyzing how individual model components affect the final representation. 
    We decompose the image representation as a sum across individual image patches, model layers, and attention heads, and use CLIP's text representation to interpret the summands.
    Interpreting the attention heads, we characterize each head's role by automatically finding text representations that span its output space, which reveals property-specific roles for many heads (e.g.~location or shape). Next, interpreting the image patches, we uncover an emergent spatial localization within CLIP. Finally, we use this understanding to remove spurious features from CLIP and to create a strong zero-shot image segmenter. Our results indicate that a scalable understanding of transformer models is attainable and can be used to repair and improve models.\footnote{Project page and code: \url{https://yossigandelsman.io/clip_decomposition/}}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper delves deep into the famous CLIP vision-langauge model for understanding its image-encoder components with the help of text representation. This includes understanding the role of attention heads, self-attention layers, MLP layers as well as the effect of each layer on the final representation in terms of downstream task performance. As the image backbone is completely aligned with text embedding representations, this work makes advantage of this property to interpret the image encoder components. 
Interestingly, each head role is associated with capturing specific attributes and properties, which leads to several downstream applications including, image retrieval with specific properties defined by head and removing spurious features by neglecting the heads which focuses such features.
The analysis is performed on CLIP models with various scales, which shows the generality of this study.

### Strengths
1) This paper presents important timely study to understand the inner working of image backbones of the large scale vision-language models like CLIP which has become a very popular paradigm. This will help to improve the next generation of such models in terms of architecture and training.
2) The use of text to interpret the image backbone components is motivating by the fact that CLIP backbone understands text representations. 
3) Extensive analysis shows the main performance drivers of the image backbone of CLIP, and could help in rejecting the redundant modules present in such vision-language architectures.
4) The proposed TextBase algorithm to associate specific roles per head using text is fairly motivated and its effectiveness is shown via downstream retrieval experiments.
5) This analysis unlocks several improvements for downstream tasks including reducing known spurious cues and zero-shot segmentation.
5) Finally the paper is well written and easy to understand.

### Weaknesses
I could not think much about any significant weaknesses in this work. I have some questions as follows:

1) How the zero-shot results compare against from methods like MaskCLIP [1]?
2) It has been shown that the zero-shot accuracy of the embeddings from only late attention layers is very competitive to the original performance. Will this also hold true where the representations are used for downstream tasks which require adaption? For example, it will be good to see the linear probe performance of the filtered embeddings on imagenet or other datasets like CIFAR100, Caltech101.

### Questions
Please refer to the weaknesses section! Thank you.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper delves into the analysis of the CLIP image encoder, breaking down the image representation by considering individual image patches, model layers, and attention heads. Using CLIP's text representation, the authors interpret these components, discovering specific roles for many attention heads, such as identifying location or shape. They also identify an emergent spatial localization within CLIP by interpreting the image patches. Leveraging this understanding, they enhance CLIP by eliminating unnecessary features and developing a potent zero-shot image segmenter. The research showcases that a comprehensive understanding of transformer models can lead to their improvement and rectification. Furthermore, the authors demonstrate two applications: reducing spurious correlations in datasets and using head representations for image retrieval based on properties like color and texture.

### Strengths
Strength:
1. Paper is well-organized
2. The proposed analysis (importance of different attention layers) and two use cases (removal of spurious correlations and head-based image retrieval) are interesting.

### Weaknesses
Weakness:
No ablation studies on the impact of the pool size (M) and the basis size (m) on the performance of the decomposition.



### Questions
Questions:
1. “all layers but the last 4 attention layers has only a small effect on CLIP’s zero-shot classification accuracy” maybe just because the early layers’ feature are not semantically distinctive? But they should be still important to extract low-level features.
2. Is it possible to achieve the “dual” aspect of the text encoder of the CLIP: 1) find layer-wise importance of the text encoder; 2) find and remove redundant heads to reduce spurious correlations; 3) perform head-based text retrieval based on query images.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper ’Interpreting CLIPs Image Representation via Text-based Decomposition’ studies the internal representation of CLIP by decomposing the final [CLS] image representation as a sum across different layers, heads and tokens. Using direct effect to ablate certain layers, the authors first understand that the late attention layers are important for the image representation. Furthermore, the authors further study the attention heads and token decompositions in the later layers to come up with two applications: (i) Annotating attention heads with image-specific properties which was leveraged to primarily reduce spurious cues; (ii) Decomposition into image tokens enabled zero-shot segmentation.

### Strengths
- This paper is one of the well executed papers in understanding the internal representations of CLIP. The writing is excellent and clear! 
- The text-decomposition based TextBase is technically simple, sound and a good tool to annotate internal components of CLIP with text. - This tool can infact be extended to study other non-CLIP vision-language models too.
- Strong (potential) applications in removing spurious correlation, image retrieval or zero-shot segmentation.

### Weaknesses
Cons / Questions:
- While the authors perform the direct effect in the paper, can the authors comment on how indirect effects can be leveraged to understand the internal representations? I think this is an important distinction to understand if understanding the internal representations in more detail can unlock further downstream capabilities. If affirmative, what downstream capabilities will be feasible?
- I am not sure if the current way to create the initial set of descriptions is diverse enough to capture “general” image properties or attributes. I believe the corpus of 3.4k sentences is too small for this analysis. While this set is a good starting point, can the authors comment on how this set can be extended to make it more diverse?
- Did the authors analyse the OpenAI CLIP variants using this framework? The OpenCLIP and OpenAI variants are trained on different pre-training corpus, so a good ablation is to understand if these properties are somehow dependent on the pre-training data distribution. 
- Can the authors comment on how the images set in Sec. 4.1 is chosen? This is not very clear from the text. Is this set a generic image set that you use to obtain m text-descriptions per head from a bigger set of text-descriptions?

### Questions
Check Cons / Questions;

Overall, the paper is an interesting take on understanding the internal representations of CLIP with the additional benefit of showing applications on image retrieval and reducing spurious correlations.  I am leaning towards acceptance and happy to increase my score if the authors adequately respond to the questions.

### Soundness
3 good

### Presentation
4 excellent

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
The research dissects the CLIP image encoder, identifying specialized roles of its internal components, and reveals an inherent spatial awareness in its processing by using the CLIP’s text representation. Insights gained from this analysis facilitate the removal of extraneous data and the enhancement of the model, notably demonstrated through the creation of an effective zero-shot image segmenter. This underscores the potential for in-depth, scalable understanding and improvement of transformer models.

### Strengths
1. Well written text
2. Excellent figure to explain the pipeline. (Fig 1)
3. Tested on various backbone and datasets
4. Carefully designed ablation study to show why we should focus on MSA blocks instead MLP blocks. This also provides nice reasoning for the decomposition algorithm design. 

5. An excellent way to provide explanations to researchers to understand the trained models. Instead of providing an enormous amount of random feature number to explain the model, the proposed method is able to align the reasoning to text. This could serve as a nice tool to collaborate with human researchers. 
6. Smart way to utilize ChatGPT 3.5 to provide text prompts

### Weaknesses
1. Seems like human users are still required to provide some sort of heuristic to decide the role of a head. I would like to know how hard it is from the user point of view. 
2. Seems like most of the experiments have been done on general image datasets. I am curious about the results on some fine grained tasks or datasets for example human face recognition.

### Questions
1. Human AI teaming. 
- I am thinking about the task from a human-AI taming point of view. How hard is it for the human to identify the role of each head? Is it possible to introduce some humans during inference time to prune/select which head to use for final prediction?
2. “Note everything has a direct role” 
- Does it mean there exists complicated features that we need to leave it as a black box, or we can ignore them as redundant feature points?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent
