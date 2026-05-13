# Boosting Document Layout Analysis with Graphic Multi-modal Data Fusion and Spatial Geometric Transformation

- Decision: Reject
- Scores: 6, 5, 5, 6

## Abstract
Document layout analysis is essential for Document Intelligence, playing a pivotal role in automated understanding and processing of document content. Most existing approaches within this domain are predicated on computer vision techniques that concentrate on image modality, despite documents containing both rich visual and textual information. While recent advances in multi-modal approaches begin to incorporate word embeddings to enhance recognition capabilities, they also incur a substantial computational burden.  Moreover,  the diversity of document structures demands models with great robustness, especially during the document editing process.  In this paper, we introduce pluggable and efficient data pre-processing strategies to boost the layout analysis performance. Firstly, we discover that element categories depend on relative relationships and propose a Graphical Multi-modal Data Fusion technique, which constructs a graph to establish connections between disparate textual segments. Secondly, in terms of structural diversity of documents, we devise a Spatial Geometric Transformation strategy to improve model robustness against layout alterations. Our methods operate during the pre-processing phase, which facilitates straightforward integration with existing models to achieve significant accuracy increase with negligible extra computations. Experimental results show that our strategies illustrate State-Of-The-Art performance across multiple document layout analysis datasets. We will make the code publicly available shortly.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents an architecture for learning a representation of document images. The presented model is addressed to improve the efficiency of Document Layout Analysis systems. It is presented as a pre-processing strategy that can be plugged in baseline methods for semantic segmentation. The paper taxonomizes existing methods for DLA as Vision-based and Multi-modal models. The proposed contributions are: First, the Graphic Multi-modal Data Fusion model uses Graph Attention Networks to generate image features at pixel level that combine word, sentence embeddings with attention scores between them as a structural representation. The second proposal is the  Spatial Geometric Transformation, that consists in several document operations that allow to augment the data used for training, boosting the layout features. Both strategies are integrated in pre-processing steps in the experimental setup consisting in FasterRCNN and CascadeRCNN as baselines.

### Strengths
A multimodal system is presented, that combines visual information, semantic embeddings from words and senteces, and an attention mechanism capturing the relative relationships between text elements.

The Spatial Geometric Transformation is a simple but effective method consisting in basic operations that allow to augment the original data with plausible document new instances.

The proposed representation is experimentally shown as an improvement when it is used as a pre-processing step in classical baselines.

### Weaknesses
The use of structural information, in particular graph-based representations is not novel. There are several works that combine visual, textual and structural features. In particular, the attention mechanism that is proposed is the classical implementation of the Graph Attention Networks (GAT).

In a layout, there are other components than just text. The strategy of modeling relationship between elements is baed on text words and sentences, but not considering other elements like figures, images, tables... The method seems to be highly sensitive to the detection of text words and lines, disregarding a more macroscopic representation.

### Questions
How does your method differ from a classical Tranformer model, that actually captures the attention between words of a text? The attention mechanism implemented between sentences resembles a Graph Transformer architecture.

It is not clear to me how sentences are obtained. Are they "meaningful" sentences obtained by the BERT model? or just word lines? 

The extraction of edges in eq (3) is based in the 4 nearest sentences, in terms of their position. Have you considered other strategies, like a visibility graph?

======================== AFTER THE REBUTTAL

After interacting with the authors, and looking at the other reviewers' revisions, I will keep the score of the first review. I thank the authors for their clarifying responses, and the effort to consider the comments. The authors have solved most of my concerns. However, I consider that the proposed method and contribution still has room for improvement in a more solid work, and it prevents me to raise the score.

### Soundness
3

### Presentation
3

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
The paper describes a simple method for image pre-processing specially designed to obtain a better image representation for document layout analysis. Two different pre-processing strategies are proposed: on one hand, enriching image information with semantic information obtained through word embedding and the relations between words and sentences in the document. On the other hand, a data augmentation strategy specific for document layout analysis. The proposed strategies can be integrated with several existing DLA methods with a very reduced extra computation cost. Experimental results analyze the contribution of the two proposed pre-processing strategies and compare the performance with current SoA on standard benchmarks, showing SoA performance.

### Strengths
- The proposed method is simple, efficient and can be integrated into several DLA methods. 
- Experimental results show that the Graphical Multi-modal Data Fusion module improves the results of Faster-RCNN and Cascade-RCNN, obtaining SoA results on the standard benchmarks.

### Weaknesses
 - Although the experiments show an improvement in the performance when the pre-processing step is applied, it is not clear to me which is the reason that brings that improvement, since the proposed fusion approach does not seem very intutitive to me. It is just the result of summing raw pixel values with some very highly compressed semantic word and sentence information, which can be very unrelated values. It would be valuable if you could explain the rationale behind the fusion of raw pixel values with semantic information. Moreover, semantic word embedding undergoes an aggressive projection from 768 dimensions to only 3, with the risk of high informaton loss. It is difficult to me to visualize which enriched information is added to the original image in eq. (8). Some discussion on this would be useful.
- The ablation analysis is incomplete. The contribtuion of the two strategies is evaluated but the multimodal fusion module should be analyzed with a deeper detail. It should be analyzed the contribution of word and sentence graphs (i.e, what are the results using only the word graph or the sentence graph?). The contribution of the attention on the graph should also be analyzed (comparing results using the sentence/word features with and without attention on the graph) since one of the starting hypothesis is that the relations among elemetns in the document are relevant for DLA. 
- The contribution of the SGT is a bit marginal

### Questions
- The fusion strategy only modifies the original image where there is text. What about non-text elements, such as tables or figures? What is the impact of the method on those regions? 
- In equation (8), is the token embedding w_m the result of attention on word graph? Or is it just the original token embedding without attention?

### Soundness
2

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
The manuscript proposes two methods in the pre-processing stage of a document layout analysis (DLA) task. The proposed models fall under the category of multi-modal methods, as they combine semantic information (e.g. word embeddings) along with the vision-based information (e.g. spatial positions). While a few multi-modal methods exist, the primary contribution of the paper is on computational cost savings, while still achieving a better mAP score.

The first method is a Graphic Multi-modal data fusion (GMDF) stage, which constructs a graph from spatial and semantic relationships. The original document image is parsed through an OCR, and tokenized. The word embeddings are used to from word and sentence graphs. The fusion of the spatial and semantic graph in then fed to the backbone of the network.

The second method is a data augmentation technique. Various augmentations are produced based on sentence remixing, paragraph perturbation and crops are used to improve the generalization of the model.

The approach is evaluated on 4 DLA datasets (DocLayNet, D4LA, PubLayNet and Docbank), and against 2 detectors: FasterRCNN and CascadeRCNN. Compared to VGT (previous SOTA), the average mAP score goes up by 1.0 while reducing the FLOPS to half.

### Strengths
The paper's has a few strengths in significance: computational cost, pluggable pre-processing step and a multi-modal approach to gather both semantic and spatial information. The proposed GMDF + SGT stages are able to perform as good as SOTA VGT method with nearly half the FLOPs. The proposed approaches are a pre-processing step, whose output is fed to the backbone of any DLA network. This makes the method applicable to a lot more use-cases. Lastly, using both textual and spatial information usually outweighs vision-only approach, and this method proves this again. 

In terms of experiments, ablation studies are performed, along with comparisons with both vision and multi-modal approaches. The comparison with VGT method is clear in terms of mAP and FLOPs.

### Weaknesses
The primary weaknesses of the paper are insufficient experiments, reasoning of success, and originality.

Originality: It is unclear how a text and spatial graph is novel. The paper itself talks about SOTA approaches that have done the same, but is not able to clarify what makes the GMDF stage novel. Creating a word graph, and constructing a sentence graph from it has been a known and well studied work. As graph-based methods have known scaling challenges, it is unclear why the given approach will flare better? The second stage SGT is a well-known data augmentation technique. It does leave open questions like -
- What is the effect of scaling on OCR parsing?
- Why augment here instead of abstracting it away from the architecture, and pulling it in training procedures

Reasoning of Success: On the lines of novelty, it is unclear why does the approach perform better? What are the areas it fails and why?

Experiments: Lastly, while the mAP scores are compared against a gamut of SOTA approaches, VGT is picked as the only one from the list for FLOPs comparison. How does the proposed approach compares to other SOTA techniques with similar mAP scores: Hybrid (V+BERT-3L), Hybrid (V+BERT-12L), GLAM+YOLOv5x6?
- How does the approach generalize to non-standard documents with unstructured layouts?
- How does it get affected by a bad OCR result? Do the semantic information start to hurt more than help then?
The data augmentations are also limited to scaling, translating and cropping. It does not seem to capture the real world issues like skewing, font changes, noise artifacts etc.

### Questions
- As graph-based methods have known scaling challenges, it is unclear why the given approach will flare better? The second stage SGT is a well-known data augmentation technique. It does leave open questions like -
- What is the effect of scaling on OCR parsing?
- Why augment here instead of abstracting it away from the architecture, and pulling it in training procedures
- why does the approach perform better? What are the areas it fails and why?
- How does the proposed approach compares to other SOTA techniques with similar mAP scores: Hybrid (V+BERT-3L), Hybrid (V+BERT-12L), GLAM+YOLOv5x6?
- How does the approach generalize to non-standard documents with unstructured layouts?
- How does it get affected by a bad OCR result? Do the semantic information start to hurt more than help then?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Current document layout analysis methods are mainly divided into two categories: one is based on computer vision technology, which focuses on image modality but ignores the textual modality in documents; the second is based on multimodal technology, integrating word embeddings to improve recognition accuracy, but inevitably increasing the computational burden after introducing textual modality. The authors found that the relative relationships among elements in the document affect the element categories, thus proposing Graphical Multi-modal Data Fusion technique, which is an image preprocessing module. Its main purpose is to construct a graph to establish connections between different disparate textual segments. At the same time, to enhance the robustness of the model, the authors designed Spatial Geometric Transformation strategy, which enhances the diversity of document structure in three dimensions: sentence, paragraph, and page. This strategy is also used in the image preprocessing stage. The authors skillfully leveraged "multimodal" information to improve accuracy without incurring much additional computation through their proposed strategies. Experimental results show that the authors' strategies have demonstrated state-of-the-art performance on multiple document layout analysis datasets.

### Strengths
Graphical Multi-modal Data Fusion technique proposed by the authors effectively integrates multimodal information, combining image modality and textual modality into a Fusion Image that is input into the model. This clever use of "multimodal" information significantly enhances the model's accuracy without substantially increasing its computational load. In addition to this, Spatial Geometric Transformation strategy put forward by the authors introduces variations at the sentence, paragraph, and page levels to enhance the diversity of document structures. This not only improves the model's robustness but also further increases its accuracy.

### Weaknesses
1. The authors claim that the proposed method not only facilitates integration with existing models but also achieves significant accuracy improvements with negligible extra computations. However, the author does not discuss why such methods can "negligible extra computations"; They only conducted ablation experiments to prove that their methods do not bring additional burdens.

2. There is a lack of experiments on other commonly used layout analysis datasets, such as PubLayNet and M6Doc. Furthermore, there is no comparison with the latest methods, such as M2Doc. Whether the proposed method can be applied to or integrated with the most recent approaches, such as M2Doc. Additionally, the performance comparisons and ablation studies are only conducted on DocLayNet, which is not convincing.

### Questions
In the paper, it would be advantageous to highlight the performance improvements achieved with minimal additional computational cost, along with an analysis that explains the underlying reasons for these gains. This approach would not only more effectively underscore the key contributions of the work but also pave the way for future research in this area. Furthermore, for aesthetic purposes, it is suggested to shift the 'Parser / OCR' label in Figure 2(a) slightly to the left. To strengthen the credibility of the proposed method, it is advisable to conduct a comparative analysis against previous methods on more benchmarks, as well as to include ablation studies on additional datasets.

### Soundness
3

### Presentation
3

### Contribution
3
