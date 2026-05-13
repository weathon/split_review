# Text Descriptions are Compressive and Invariant Representations for Visual Learning

- Decision: Reject
- Scores: 5, 3, 6, 5

## Abstract
Modern image classification is based upon directly predicting classes via large discriminative networks, which do not directly contain information about the intuitive visual features that may constitute a classification decision. 
Recently, work in vision-language models (VLM) such as CLIP has provided ways to specify natural language descriptions of image classes, but typically focuses on providing single descriptions for each class. In this work, we demonstrate that an alternative approach, in line with humans' understanding of multiple visual features per class, can also provide compelling performance in the robust few-shot learning setting. 
In particular, we introduce a novel method, \textit{SLR-AVD (Sparse Logistic Regression using Augmented Visual Descriptors)}. This method first automatically generates multiple visual descriptions of each class via a large language model (LLM), then uses a VLM to translate these descriptions to a set of visual feature embeddings of each image, and finally uses sparse logistic regression to select a relevant subset of these features to classify each image.
Core to our approach is the fact that, information-theoretically, these descriptive features are more invariant to domain shift than traditional image embeddings, even though the VLM training process is not explicitly designed for invariant representation learning. These invariant descriptive features also compose a better input compression scheme. When combined with finetuning, we show that SLR-AVD is able to outperform existing state-of-the-art finetuning approaches on both in-distribution and out-of-distribution performance.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a model SLR-AVD which first automatically generates visual descriptions of each class via a LLM, then use a VLM to translate these descriptions to a set of viaul feature embeddings of each image. The features are proved to be more invariant to domain shift than traditional image embeddings with information-theory. The SLR-AVD is validated on both in-distribution and out-of-distribution classification.

### Strengths
The proposed model is novel, which extracts multiple potential visual features of each class, and then uses L1-regularized logistic regression to fit a sparse linear classifier on top of these visual descriptions. The generated descriptive features are proved to retain substantial information about the true labels, making them good invariant representations.

### Weaknesses
The paper writing and the experiments need improvement.

1. The training and inference process is not clear.
- What is the loss function used to train the model?
- The three W matrices W_{vd}, W_{cp}, and W_{avd} are used as zero-shot classifiers. However, the inference process of the zero-shot classifier is not clearly explained.
- In Section 3.2 paragraph 2, it would be better to mathematically specify how to regularize W_{avd}, and how to pick three features for each class with the largest coefficients.
2. The experiments show limited performance gain in zero-shot classification.
- the results in Table 1 indicate that ZS-VD performs worse than ZS. ZS-AVD only provides marginal improvement over ZS, i.e., 0.74 (IN), 0.74 (IN-V2), 0.13 (IN-R), 0.23 (IN-A), 0.27 (ObjectNet).
3. In Figure 3, it would be interesting to show the performance of the ZS-VD model.
4. In section 4.2, which dataset is the OOD test set?

### Questions
Figure 4 is unclear and the sub-caption in the bottom-right corner is blocked.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a method to produce better zero-shot classifiers for vision-language models, more specifically CLIP.
To do so, the set of standard class prompts used to construct zero-shot classifiers is enhanced using GPT-3 with extra textual descriptions.
Moreover, $\ell_1$ regularized logistic regression classifier is trained to select certain textual descriptions for each class.
This way, slightly better performance is achieved on ImageNet datasets compared to the standard prompts.

### Strengths
One of the strengths of this paper is the idea of sparse selection of automatically generated prompts for classes (for which we want to learn a zero-shot classifier).
There are several prompt templates, which are provided as input to GPT-3 to retrieve textual descriptions for classes.
Then $\ell_1$-regularized logistic regression is trained to select the most discriminative prompts for each class.
This strategy brings slight performance boost over manually constructing only a few (if not one) class prompts.

### Weaknesses
There are two main concerns that I would like to raise.

1) The benefit of automatically generating prompts for obtaining zero-shot classifiers is not very clear and significant. Table-1 compares the proposed method of generating textual desciptions from GPT-3 (ZS-AVD) against using only manually defined class prompts (ZS), and we see marginal improvements (max a few decimal points). It would be nice to see the impact of the number and diversity of generated prompts into performance. Section 4.1 mentions that "...class names are probably one of the strongest prompts... One can certainly try to improve ZS-VD results by more carefully prompting GPT-3, or gathering descriptors from different data sources/search engines." this contradicts with the motivation of the paper, no?

2) The benefit of using $\ell_1$-regularized logistic regression technique is not very clear either. It would be nice to see if simple $\ell_2$ regularization performs the same, or what kind of prompts selected for certain classes using different regularization criterons. Also, a simple k-NN based approach can also be applied as a baseline both with soft or hard assignment. On the other hand, similar logistic regression can be trained also for ZS (where there can be multiple manually defined class prompts). Maybe the impact is only due to learning weights ($W$) which connect the two modalities (image and text) using some regularization technique.
Section-5 mentions that "Applying sparse logistic regression then successfully selects the important features, which turn out to be intuitive" but we don't see any evidence, right?

Minor comments:
- 1st sentence of Introduction: "Self-supervised vision-language models (VLMs) like CLIP..." is there any reference claiming CLIP to be self-supervised?
- 2nd sentence of Section-2: "WLOG..." what is WLOG?
- Missing closing paranthesis in Figure-1
- 4th paragraph of Section-3.1 ("Denote M ...") is very confusing. It would be nice to explain all $U$ and $W$ in a diagram/visualization.
- Figure-3 caption "the x-axis represents..." (not y)
- Figure-3 what is the label for y-axis?

### Questions
I would like the authors to address the concerns I listed in the weaknesses part.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a method for obtaining more robust CLIP models. First, multiple visual descriptions are generated by an LLM and then used by the CLIP model alongside encodings of the class names. The visual representation is projected into the class + descriptors space and then a sparse logistic regression is trained on this representation.  As shown by experiments estimating mutual information, projecting on the class embeddings and visual descriptions minimizes the mutual-info with the domain, while selecting sparse features follows the bottleneck principle. Experimentally, the method is shown to produce better results than good baselines and can be combined with existing methods.

### Strengths
* S1. The method is well-motivated.

* S2. The method is sound. Both the visual descriptions and sparsity are good ways to improve robustness.

### Weaknesses
 * W1. The paper already compares against a few methods, but some additional baselines and ablations would also help. First, the full method but with logistic regression instead of sparse logistic regression (this will show if the sparsity is really important). The same method without using the video descriptions (partially shown in Table 1). Second, an MLP with a similar number of parameters as SLR-AVD, with different levels of weight decay. Third, use random projections / learnable matrices instead of the U projections (this will also induce a bottleneck). 

* W2. It will be good to have an overall comparison with different methods and an ablation study of the proposed method. I am thinking mainly of using the same base model (e.g. ViT- B/16), maybe just some standard few-shot k (e.g. k=16). A table with all datasets as columns and different methods (ZS, LP, MLP probing, FullFinetunning, CoOp, Wise) and ablations (ZS-AVD, SLR-AVD etc.).

* W3. It will be good to see the performance of *all* models presenting using different number of shots: 1,2,4,8,16, 32. At the moment some ablations contain only up to 4 or 16 shots.

* W4. The paper focuses on few-shot learning and this is an important area. To see the tradeoffs of the proposed method and the baselines, it will be interesting to also see the performance using larger training sets. For example, use k from 64, 256, 1024, etc. This way we can see at which scale of training samples is the proposed method more beneficial.


* W5. Comparison with CoOP does not seem to be fair. “Since CoOp injects “classname” to the prompt during inference directly, this enforces a very strong prior. For a fair comparison, we also inject a strong prior by interpolating our learned linear head”. It is not clear what this means, and why a direct comparison is not fair. Why is the “classname” injection a strong prior for CoOP? Isn’t SLR-AVD also using the same classname to produce the class prompts (CP)? Combining the proposed method with Wise and comparing to plain CoOp seems unfair.

* W5.2. The comparison with CoOP is made using Resnet-50, which gives poorer performance for CLIP. Comparison using the ViT models should also be made.

* W6. It is not clear how hyperparameter selection is done. Hyperparameter and model selection are crucial for domain generalization, thus this should be made more clear. For Wise models, alpha seems to be selected optimally, using validation OOD data.

* W7. In Figure 4 top, it seems like WISE-FT+LP, which finetunes only the last linear layer, is compared against WISE-FT+SLR-AVD, which finetunes the entire model. Is this correct, or is WISE-FT+SLR-AVD finetunning only the linear classifier? Both should either update the linear layer or full-finetuning. Also, what is the difference between WISE-FT+LP and WISE-SLR?


* W8. The paper will benefit from a better presentation. There are multiple acronyms, and sometimes the difference between them is not clear. The section in the appendix explaining the acronyms should be expanded with more details and should contain all acronyms and combinations used (e.g. WISE-FT+SLR-AVD, WISE-FT+SLR-AVD). 
* W8.2 Minor: Figure 4 should be improved, e.g. use consistent symbols, especially for start and end points. Show the optimal checkpoint in the figure.

### Questions
Q: What is the number of learnable parameters of SLR-AVD, how does it compare to linear probing?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper is in line with a recent trend of augmenting CLIP's classification templates with class-specific descriptions generated from LLMs   (eg, GPT-3). The major technical contribution of this work is to concatenate the descriptions of all classes of interest, learn weights to aggregate these descriptions' text features and form new classifiers for each class. The weights are regularized with l1-norm to encourage sparsity. Experiments show that tuning with this classifier outperforms methods that work directly on top of vision features (without texts). Besides, information-theoretical analysis is also provided to show the improved invariance of text features (in CLIP's joint VL space) over raw vision features (output of the vision tower prior to linear projection).

### Strengths
*Originality*: The technical contribution is relatively limited, which still fits in the scope of description selection. Its combination with other schemes like LP-FT is somehow instrumental. Yet the theoretical analysis is relatively novel and inspiring.

*Clarity*: The paper is overall clearly written. Yet the organization could be improved, and more details could be provided to help understand details of the proposed method.

*Significance*: This paper fits in the scope of visual representation learning under text supervision, and provides analysis on feature invariance and compression, which is helpful for the community.

### Weaknesses
I put the minor concerns in the section above (which did not harm my rating much), and list the major concerns here:

1) The theoretical analysis is not well-aligned with the proposed method:
- The major conclusion that could be derived from sec 3.3 is that features from CLIP's joint VL space are more compressed and invariant to visual variations (compared with vision features).
- This is good and helps us understand CLIP itself, but does not explain why using descriptions (no matter w/ or w/o selection) is better than using other texts (eg, the default templates), which is the foundation of the proposed method.
- From fig. 2 I find $I(H_{avd}; A)$ is almost identical to $I(H_{cp}; A)$, indicating descriptions do not introduce more invariance than template ensemble, which raises concern on why descriptions are needed in this work. $I(H_{avd}; Y)$ is higher than $I(H_{cp}; Y)$, which should indicate better predictions, yet in tab. 1 the gain of ZS-AVD over ZS is just marginal.

2)  The experiments also do not support this work (description selection)'s superiority over other template designs:
- In tab. 2 & 3, SLR's superiority over FT & LP under the few-shot setting is expected, since both WISE-FT's $W_\text{learned}$ and LP's classifier are trained from scratch given only very few samples, thus could not match the performance of classifiers derived from CLIP's text encoder.
- Yet this does not help understand SLR's strength over other classifiers. For instance, a) what if we drop the selection process and just follow Menon & Vondric's average ensemble, b) what about WaffleCLIP [1]'s random descriptors, c) how much is SLR's improvement over CLIP's default templates, and d) how do k-NN classifiers (use average pooling of the labeled few-shot samples to form classifiers, try both vision features and VL features) perform?

3) No ablation study is provided to understand the proposed method (relatively minor)

### Questions
One possible cause of ZS-VD's much inferior performance than ZS in tab.1 is the use of class templates. If the templates of ZS are also applied to ZS-VD, the difference in their performance should be marginal (refer to WaffleCLIP). I suggest the authors give it a try.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
