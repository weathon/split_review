# $\mathbb{X}$-Sample Contrastive Loss: Improving Contrastive Learning with Sample Similarity Graphs

- Decision: Accept
- Scores: 5, 5, 8, 6

## Abstract
Learning good representations involves capturing the diverse ways in which data samples relate. Contrastive loss—an objective matching related samples—underlies methods from self-supervised to multimodal learning. Contrastive losses, however, can be viewed more broadly as modifying a similarity graph to indicate how samples should relate in the embedding space.  This view reveals a shortcoming in contrastive learning: the similarity graph is binary, as only one sample is the related positive sample. Crucially, similarities \textit{across} samples are ignored. 
Based on this observation, we revise the standard contrastive loss to explicitly encode how a sample relates to others. We experiment with this new objective, called $\mathbb{X}$-Sample Contrastive, to train vision models based on similarities in class or text caption descriptions.
Our study spans three scales: ImageNet-1k with 1 million, CC3M with 3 million, and CC12M with 12 million samples. The representations learned via our objective outperform both contrastive self-supervised and vision-language models trained on the same data across a range of tasks. When training on CC12M, we outperform CLIP by $0.6\%$ on both ImageNet and ImageNet Real. Our objective appears to work particularly well in lower-data regimes, with gains over CLIP of $17.2\%$ on ImageNet and $18.0\%$ on ImageNet Real when training with CC3M. Finally, our objective seems to encourage the model to learn representations that separate objects from their attributes and backgrounds, with gains of $3.3$-$5.6$\% over CLIP on ImageNet9. We hope the proposed solution takes a small step towards developing richer learning objectives for understanding sample relations in foundation models.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work presents X-CLR, a contrastive loss objective that replaces the usual binary positive/negative samples in contrastive learning with soft labels that can vary inside [0,1]. The resulting loss function requires pairwise similarity labels, which the authors suggest can come in the form of metadata or via text embeddings of captions generated from class labels. A comprehensive set of experiments on ImageNet and CC3M/CC12M show improvement in performance of X-CLR relative to existing contrastive learning baselines on classification tasks.

### Strengths
1) The proposed method and its advantages are intuitive and easy to understand, and there is a comparison with existing vision-based contrastive loss functions.

2) The suite of experimental results is comprehensive, and considers many useful ablations. I particularly appreciated the practical experiments about finetuning and refining existing vision backbones, and the explorations of high-quality vs noisy similarity data.

### Weaknesses
1) There is limited novelty to the proposed contrastive learning loss function, which is a relatively simple swapping of binary positive/negative sample labels in existing contrastive learning losses with a soft label.

2) Pursuant to the first point, there not much detailed analysis of how this method related to existing ones beyond a comparison of the binary vs. soft label graph.

3) The presentation of the paper is inconsistent - there are some very concise and informative figures, like Figure 1, but for example, there are many wording issues throughout, and there are other places where more detail is needed (this is particularly true for table captions).

4) Some weaknesses in experimental results - there is only one network architecture tested, though I accept the given justification to some extent.

### Questions
1) Some of the results you get for competing methods are far below what those methods report in their papers. Just as an example, in Table 1, ImageNet accuracy from your experiment with SimCLR is 63.4% vs. the 69.3% reported in their paper, and SupCon is 74.3% in your table vs. 78.7% reported in their paper. This is a very significant difference, since in the case of SupCon, their reported result outperforms X-CLR. Did you look into the large differences here? Can you explain them?

2) Please add some more detail to the table captions. The captions right now generally tell me what the takeaway should be, but they don't tell me the specifics of what I'm looking at: things like what the numbers actually represent (accuracy), what the columns mean (i.e., for Table 1, "Accuracy of networks pretrained on ImageNet with various contrastive learning algorithms, and evaluated on a set of..."), etc. Also, I think it is a stretch to call Theorem 1 a theorem - this is an re-expression of these losses in matrix form, and the cited paper doesn't even offer a proof. I think these can simply be stated.

3) I found the CLIP experiments section confusing. In your CLIP baseline, are you actually training a vision encoder and language encoder jointly with a CLIP loss, or are you taking a pretrained CLIP model and performing training with X-CLR loss? Also, in general I thought a deeper analysis with CLIP was missing from Section 3, particularly in the case of generating similarities with captions + a CLIP text encoder. Is X-CLR equivalent to CLIP training with a frozen / pre-trained text encoder in this case? If not, how is it different? I think this comparison is important to contextualize your method.

4) In the case of ImageNet, you use class labels to generate text captions, and then embed these to get text embeddings, which ultimately determine the connection strengths in the graph. This creates a similarity matrix that has some particular properties, i.e., images within the same class have a similarity of 1, as in the Supervised graph in Figure 1, along with other nonzero entries based on the similarities of two different images' classes. Does this end up being the same as SupCon? There are some similarities with supervised learning here, but there is no analysis of this similarity.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes a new contrastive objective that uses a target similarity graph based on additional information or models. The modification is applied to contrastive losses in both multi-modal learning (image-text CLIP training) as well as self-supervised learning (images). The proposed modification is called “X-Sample Contrastive Loss” or X-CLR, where the model assumes access to an external source of metadata and possibly pretrained models that can define a graph of similarity between inputs. The goal is to replace the 0-1 hard similarity graph used in contrastive methods with soft similarity graphs based on some ground-truth information.

### Strengths
- Unifying SSL, multi-modal contrastive learning, and distillation methods in one formulation is helpful in defining generalized training methods.
- The ablation on the similarity sources in Table 2 is interesting as it shows strong text encoders are not helpful for X-CLR loss than more simple sentence transformer.

### Weaknesses
 - The paper should clearly separate the SSL methods on images from image-text methods such as CLIP and clearly define X-CLR modification for both setups. There is a clear difference between contrastive losses for the two setups, one relies on image augmentations to define contrastive pairs while the other relies on paired image-text datasets. Figure 1.b presents a pseudocode for the X-CLR loss that is valid only when paired image-text data is available. In fact, the only reason this loss does not collapse to a trivial and all equal solution is that the `text_emb` is detached from the computation graph.
- The tables and comparisons should specify which models have access to additional data and/or additional pretrained models. For example, Table 1 compares X-CLR to SimCLR while X-CLR not only has access to the labels, but also access to pretrained text models. The comparison to methods that do not have the advantages of X-CLR is not fair. Specifically, when the method using the labels in ImageNet to define the loss, it can no longer be fairly compared with SSL methods that do not have access to labels. For example, the analysis in section 4.5 that compares the overhead of X-CLR to SimCLR needs to account for the training time of the text encoder as well.
- On line 354, the paper claims that “X-CLR is more general than model distillation methods as the similarities can come from any source” and cites the TinyCLIP [1]. Are the authors claiming X-CLR can be better than CLIP distillation methods? If so, the paper should compare to state-of-the-art CLIP distillation methods such TinyCLIP [1] and MobileCLIP [2]. That being said, I did not find a clear definition of X-CLR for image-text loss that allows for training both image/text towers even if it uses pretrained image and/or text pretrained models. Specifically, the loss should have image2text and text2image terms or show that it can learn a comparable representation without these terms.

### Questions
- Are both Tables 1,3,4 using pretrained frozen sentence transformers as the text encoder?

### Soundness
2

### Presentation
2

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
This paper introduces a new objective, called $\mathbb{X}$-Sample Contrastive Learning, where the binary designations in standard contrastive learning are replaced by a soft target based on similarities between samples. These similarities can be obtained through any preferred method, with this paper mainly using frozen text encoders for the experiments. Moreover, the method can be applied fairly easily to any contrastive objective, with this paper focusing on the InfoNCE objective.

The proposed method is trained on ImageNet, CC3M and CC12M and compared against one supervised learning method and various SSL methodologies. It is shown that $\mathbb{X}$-CLR leads to consistent improvements for classification and background decomposition compared to the baselines, with minimal increase in computation.

### Strengths
This paper recognizes an important problem, which is that commonly used contrastive objectives assume binary similarity scores, which in many settings do not make much sense. The proposed method is an intuitive way of generalizing contrastive learning to non-binary similarity scores, effectively dealing with this problem. $\mathbb{X}$-CLR is tested through a comprehensive suite of experiments, showcasing its effectiveness and highlighting some of the important design choices that should be taken into account when using this objective.

The paper is well written with a clear explanation of the problem of existing contrastive learning methods, followed by a great presentation of the proposed method. Moreover, the experiment descriptions are both clear and concise, effectively highlighting the strengths and weaknesses of the method. Finally, the paper is well structured overall, making it enjoyable to read.

### Weaknesses
In my opinion, there are no significant weaknesses in the paper. The only thing I was wondering regarding the experiments is how fair the comparison between $\mathbb{X}$-CLR and the SSL methods in Table 1 is. It seems to me that $\mathbb{X}$-CLR is a supervised method in this setting. If the authors agree with me, then it might be nice to explicitly mention this in the text to avoid any possible confusion. That being said, I do think including the comparison is important to showcase the effect of proper similarity scoring, so this is a minor remark.

Aside from that, I have some small notes regarding the presentation, which I will list below:
  - It may be useful to shortly mention what $f_\theta$ and $K$ are after equation (1) in line 202 if space is not a concern. It is reasonably clear from the context, but being explicit rarely hurts.
  - In the data  scarcity setting (figure 3a), SupCon appears to be better than $\mathbb{X}$-CLR, while the text mentions that $\mathbb{X}$-CLR improves over SupCon.
  - The coloring of SupCon and SimCLR in figures 3a and 3b is flipped, which is a bit confusing at first glance.
  - The paragraph related to table 4 does not mention training on CC3M, which might be useful to mention for clarity.

### Questions
As mentioned before, I think the given experiments paint a clear picture of the method. So the questions listed here are mostly out of interest and not things that I necessarily think make sense to include in the paper. That being said, I was wondering a few things about the method:
  - What happens in imbalanced settings? I imagine that the similarities for an instance with rare caption/label/meta data would be much lower than for instances with more common caption/label/meta data. Do you think this would have a strong effect on the method? Have you tried experimenting with for example ImageNet-LT?
  - An annoying problem of contrastive learning is its sensitivity to the batch size ($B$), which stems from its effect on the ratio of positives to negatives across the training set ($B^{-1}$). I imagine that $\mathbb{X}$-CLR partially solves this problem, especially for larger batch sizes, given that the similarities $\mathbf{G}_{ij}^{(\text{soft})}$ approximately follow $\mathbb{P}\_X(\text{sim}(X\_i, X))$, where $\mathbb{P}\_X$ denotes the population distribution on inputs $X$. The only bias being the small effect of the true positive $\mathbf{G}\_{ii}^{(\text{soft})} = 1$. Is this something you looked into? If yes, how sensitive is $\mathbb{X}$-CLR to changes in the batch size? Furthermore, does the application of the softmax to obtain the distribution $s$ have any negative effects for larger batch sizes (since $s_i \rightarrow 0$ when $B \rightarrow \infty$)?
  - Do the similarities for ImageNet (shown in figure 5a) come from the way the text encoder input is constructed (so from the fixed template part)? If this is the case, do the similarities not give a false view of how strongly related images are? I expected there to be at least some very low similarities for each image, although I might be misunderstanding something here.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper argue for revising the standard contrastive cross-entropy loss from binary targets of a sparse augmentation graph to a soft target graph where the target values can be between [0, 1]. The new method is called X-CLR. The authors suggest to use extra metadata associated with the dataset to find the soft target distribution, and in this work mostly use the pairwise similarities from a pretrained text encoder on text captions/descriptions to encode this distribution. Although the authors note that the framework is general, "the similarities can come from any source including any metadata". Conduct experiments to train vision models with text captions/descriptions. The study spans different datasets and the results show improvements over contrastive baselines.

### Strengths
1. The paper is well-written and easy to read.
2. Experiment study spans different datasets and comparisons to contrastive baselines.
3. The authors test with different similarity graphs (random graph, graph inferred from metadata, augmentation graph, true class graph), and find that a soft graph can improve over the binary graph of existing contrastive approaches.

### Weaknesses
1. Relying on extra metadata and a pretrained model limits the applicability compared to the contrastive baselines. I also think this is a simple solution. Specifically, the requirement for a pretrained text encoder to generate pairwise similarities introduces a significant dependency. This dependency not only increases computational overhead but also restricts the method's use in scenarios where such encoders are unavailable or unsuitable. Furthermore, the method's reliance on metadata, which may not always be readily available or reliable, further limits its practical applicability. The simplicity of using a pretrained model to generate similarities, while effective, does not offer substantial methodological novelty.
2. The idea of soft-targets for cross-entropy based contrastive loss is very general. It also lack some novelty to the paper's related work on soft-targets. While the authors frame their approach as introducing similarities, the core mechanism of using soft targets in a contrastive loss is not new. The novelty is further diminished by the fact that the paper does not explore the theoretical implications of using soft targets in contrastive learning, such as convergence properties or the impact on the learned representation space. The lack of a theoretical analysis makes it difficult to assess the generalizability of the proposed method beyond the specific datasets used in the experiments.

### Questions
Suggestion: Finding a soft target graph without extra metadata or pretrained model with self-supervised techniques would give better applicability.

### Soundness
3

### Presentation
3

### Contribution
2
