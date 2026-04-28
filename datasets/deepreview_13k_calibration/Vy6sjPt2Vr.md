# A Spitting Image: Superpixel Transformers

- Decision: Reject
- Avg Score: 5.50
- Scores: 3, 5, 8, 6

## Abstract
Vision Transformer (ViT) architectures treat tokenization as an inflexible, monolithic process with regular grid partitions. 
In this work, we propose a generalized superpixel transformer (SPiT) framework that decouples tokenization from feature extraction; a significant shift from contemporary approaches, where these are treated as an undifferentiated whole. 
Using on-line superpixel tokenization and scale- and shape-invariant feature extraction, we perform experiments and ablations that contrast our approach with canonical tokenization and randomized partitions as baselines. 
We find that modular superpixel-based tokenization provides significantly improved interpretability using state-of-the-art metrics for faithfulness while maintaining competitive classification performance, providing a space of semantically-rich models that can generalize across different vision tasks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper suggests using superpixels instead of patches as the input for vision transformers. It generates superpixels using a previous method with a different regularization term. Experiments show that superpixels have better interpretability than patches.

### Strengths
This paper has an interesting motivation to use superpixels instead of grids as the input for vision transformers. It also provides better interpretability by visualizing the attention maps. The paper gives the formulation of the proposed method and proves that the conventional ViT is a special case of it.

### Weaknesses
This paper has limited novelty, as previous works [1,2] have already explored the combination of superpixels and Transformers. The superpixels are created using only low-level and predefined features in the first layer, which may cause permanent errors. Specifically, the reliance on initial, handcrafted features for superpixel generation could lead to suboptimal tokenization that persists throughout the network, as these features may not adequately capture the complexities of the input data. This is a potential concern because the quality of the superpixels directly impacts the information available to subsequent layers. In contrast, [1,2] use the features learned by the network, which are dynamically updated during training and can therefore adapt to the specific characteristics of the dataset. This may explain why the performance on image classification is worse than the baseline, as shown in Table 1, where the proposed method consistently underperforms, particularly on datasets with high intra-class variability.

### Questions
Do you use a differentiable online tokenization process?

How does your method compare with conventional superpixel methods like SLIC, since you also use manually defined features?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a method that replaces the square patch tokenization by superpixel tokenization in vision transformers. The authors implemented a GPU-based superpixel method to serve as the tokens. The authors investigates the ViT using superpixel tokens for image classification tasks, and find that the proposed method is useful in some cases.

### Strengths
- The idea of replacing square tokens with superpixel tokens is straightforward and reasonable.
- Extensive experiments to analyze the proposed method. 
- The proposed method has better explainability then vanilla square patch tokens.

### Weaknesses
 - The experimental results are not very convincing. As stated in the paper "although we insist that the results are not significant enough to warrant any clear benefit for any framework in particular on classification tasks". It is not clear how useful is the proposed method in image classification and other tasks.
- Some sentences are not complete, e.g., "We hope that our work inspires more research into the" in page 9.

- The runtime analysis is missing. It is unclear how the computational overhead of generating superpixel tokens compares to the standard patch-based tokenization, especially during training. The paper only briefly touches on inference runtime, but a comprehensive analysis including training time is essential.
- It is not clear if the superpixel tokens are static throughout the network or if they are dynamically adjusted or merged across layers. This is a crucial detail for understanding the hierarchical feature representation, and it is not adequately addressed in the paper.

### Questions
The runtime analysis is missing. Would replacing the square patches with superpixels for tokens requires much extra runtime?
Do the superpixel tokens remain the same in each layer or are hierarchically grouped together?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces an innovative approach to improving tokenization strategies in vision transformers. In contrast to traditional regular grid partitioning methods, they propose a superpixel transformer approach capable of irregular tokenization. By employing state-of-the-art metrics, this method can flexibly divide irregular patches, thereby enhancing the ability of subsequent transformer modules to extract higher-quality features and significantly improving model interpretability. Furthermore, the authors conducted an extensive series of experiments to rigorously validate the effectiveness of their method.

### Strengths
This paper demonstrates a highly promising starting point by introducing the use of superpixel partitioning for irregular patch division, which seeks to address the inherent limitations of traditional grid-based partitioning methods in transformers. As highlighted by the authors, this approach has the potential to significantly enhance the interpretability of attention mechanisms in Vision Transformer (ViT) and facilitate the extraction of high-quality features, marking its potential impact on pioneering applications of transformers. The paper maintains a clear and informative structure. In summary, this work demonstrates a high degree of originality and holds substantial potential for further research and applications in the field.

### Weaknesses
1、In the experimental section, the authors have provided thorough validation and analysis of the enhancement in feature extraction achieved by superpixel tokens in subsequent transformer modules. However, the paper lacks a rigorous analysis of SPiT's computational efficiency. While Table 4 indicates that the superpixel algorithm used in this study performs comparably to state-of-the-art algorithms with substantially lower inference time, it is essential to explore the computational overhead introduced by integrating superpixel tokens with subsequent transformer modules. Specifically, the paper should analyze the inference time of the entire pipeline, not just the superpixel generation, and compare it against standard ViT and RViT models. This should include a breakdown of the time spent in the superpixel tokenization step versus the transformer layers, to understand where the bottlenecks lie. A detailed analysis of FLOPs and memory usage would also be beneficial to fully assess the practical applicability of the proposed method.

2、The determination of hierarchical levels T is not clearly explained, and the impact of this parameter on model performance is not sufficiently explored. The paper lacks a clear rationale for choosing a specific value for T, and it is unclear how different values of T affect the granularity of the superpixel tokens and, consequently, the performance of the model. To provide a more comprehensive understanding, the authors should include an additional set of ablation experiments to explore the relationship between T settings, the resulting number of tokens, and model performance. These experiments should investigate a range of T values and analyze the trade-offs between computational cost and accuracy. This analysis should also consider the variance in the number of tokens generated across different images, and how this variability affects the overall efficiency and stability of the model.

3、The paper's summary of related work is relatively limited. The authors should consider expanding the discussion of strategies for improving tokenization methods in the related work section, such as [1] [2]. This would contribute to a more thorough understanding of the research landscape and enhance the paper's contributions. Specifically, the related work should discuss how other methods address the limitations of regular grid partitioning, and how the proposed superpixel approach compares to these alternatives in terms of computational cost, feature quality, and interpretability. A more detailed comparison with methods that use adaptive or learned tokenization strategies would also be beneficial.

### Questions
Have you considered conducting a comparative analysis between your superpixel tokenization method and mixed-scale tokenization approaches [1] [2]? Mixed-scale tokenization can also alleviate the limitations of regular grid partitioning methods to some extent, reducing information loss without introducing excessive computational overhead. What advantages do you offer in comparison to them?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes to revisit the standard uniform square tokenization in vision transformers, and instead replace it with **superpixel-based tokenization**. The superpixel partition follows the methodology of "SuperPixel Hierarchy" (Wei et al, Transactions on Image Processing 2018) with an additional regularization term for self-loop edges. Based on this criterion, pixels are grouped hierarchically to form superpixels, and the number of hierarchy levels is chosen to obtain a comparable number of tokens to `ViT-B/16`.
Once the superpixels are defined, several sets of features are extract for each of them to form the input token representations:
  * **positional encodings** are computed as a histogram over the spatial positions present in the superpixel
  * **texture features** are extracted using gradient operators
  * **color features** are computed by interpolating the light intensity information present in the suerpixel

Once the superpixel and corresponding features are defined, the rest of the model is defined as a standard transformer architectures. In practice, the paper uses **ViT (Small and Base)** as backbone. The proposed method is evaluated on the task of image classification, as well as through various explainability metrics. It is compared to the backbone (ViT), as well to a method employing random Voronoi cells as tokens. The results show that the proposed method can match classification accuracy of the standard ViT backbone while yielding more interpretable feature attribution maps.

### Strengths
- **Clear writing and motivation**: The paper is clearly written and fully describes the proposed tokenization as well as feature extraction methods. The core motivation of departing from "uniform square patches" tokenization is very meaningful and superpixels appear like a well established tool to tackle this problem.

- **Clear reproducibility details**: The paper clearly describes the training details and hyperparameters in the appendix to reproduce the results.

- **Interpretability results**: The paper report interpretability experiments results using multiple metrics/frameworks to evaluate the faithfulness of feature attributions.

### Weaknesses
 - **Practicality of superpixels**: One advantage of square tokenization is that it is highly practical:, it's a simple patching operation, and the position encodings can easily be transferred across scales using interpolation (see for instance "*FlexiViT: One Model for All Patch Sizes, Beyer et al, CVPR 2023*"). In contrast, the proposed method requires the extra step of generating superpixels for each input image, which is not discussed in the paper. The computational overhead of this superpixel generation, including its impact on both training and inference time, is not sufficiently addressed. While the paper mentions that the number of tokens is comparable to ViT-B/16, it does not provide a detailed analysis of the computational cost associated with generating these superpixels, nor does it discuss the implications of having a variable number of tokens per image on batched execution.

- **Limited baselines:** The paper primarly evaluates three methods: `ViT-{S,B}/16` (the base model), `SPiT-{S, B}/16` (the proposed model) and `RViT-{S,B}/16`, which, from my understanding, is a baseline introduced in this paper using random Voronoi cells as tokens. I understand that improving classification accuracy is not the main goal of the paper hence the choice of baselines, but I do still think the paper would benefit from comparing to baselines which have a similar goal (i.e. either methods that propose more flexible tokenization, or more interpretable attention maps). The absence of comparisons with methods that also aim for more flexible tokenization or improved interpretability limits the assessment of the proposed method's unique contributions. For example, methods that employ dynamic tokenization or token merging could provide a more relevant comparison.

- **Missing related work:** In general, the discussion of related work in the paper is very short and does not seem to contextualize the paper enough. For instance, some points which may be interesting to discuss:
  * On the aspect of interpretability, models such as `DINO` trained with finer-grained tokens (*Emerging Properties in Self-Supervised Vision Transformers, Caron et al, CVPR 2021*) would be a stronger baseline than ViT trained with coarser patch size
  * *Vision Transformer with Super Token Sampling, Huang et al, CVPR 2023* is another method that uses superpixel in Vision transformers. The related work section explains that this method build super-pixel by gradually merging square patches, unlike the current work which uses super-pixels from the start; However, it is not clear to me why this is preferable, and how these two approaches compare in practice.
  * In addition, there has been many works investigating more flexible tokenization than the standard ViT "uniform square" assumption, which is not reflected in the introduction. For instance:
    * **Token merging** approaches (e.g. "*`ToME`: Your ViT but faster, Bolya et al, ICLR 2023*") also alleviate the issues that [quote] *" complexity and memory scales quadratically with the number of tokens in self-attention"*
    * Other works on **dynamic tokenization** (e.g. "*Vision Transformers with Mixed-Resolution Tokenization, Ronen et al, 2023*" or "*MSViT: Dynamic Mixed-Scale Tokenization for Vision Transformers, Havtorn et al, 2023*") also propose to incorporate mixed-resolution information directly at the input tokens stage and also show that ViT "can be succesfully trained under irregular tokenization"
    * `Swin` transformers and other **multi-scale works** gradually build multi-scale tokens, hence they do not have the issue that [quote] *"the scale of the partitions are rigidly linked to the model architecture by a fixed patch size"*

**Overall summary:** My main concern is that it is not clear to me why using superpixels as tokens is advantageous with respect to other methods implementing some form of input-dependent tokenization, either in terms of performance or computational cost. The main gain seems to be in obtaining more fine-grained interpretability maps, but these are also only compared to the standard ViT-backbone (and the random voronoi cell baseline)

### Questions
- **Notion of equivalence in Propositions 1 and 2**: What does it mean for the two operators to be equivalent ? the proof of proposition 1 only seems to show that both operators have the same input and output dimensions. Generally, I am not sure what the conclusion of Section 2.4 is and how significant it is.

- **Number of tokens and batched executions:** In Section 2.2, it is said that "*We empirically verify that setting T = 4 produces comparable numbers of tokens to a ViT-B16*"; Does this mean that each image has a different number of tokens in practice, and how does this impact batched execution during training/inference ?


- **Evaluation on segmentation:** The choice of super-pixels seem particularly relevant for more dense tasks such as segmentation: This might be a more favorable task to evaluate on than image classification.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
