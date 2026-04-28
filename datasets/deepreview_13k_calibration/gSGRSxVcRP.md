# Detecting and Approximating Redundant Computational Blocks in Neural Networks

- Decision: Reject
- Avg Score: 4.25
- Scores: 5, 6, 3, 3

## Abstract
Deep neural networks often learn similar internal representations, both across different models and within their own layers. While inter-network similarities have enabled techniques such as model stitching and merging, intra-network similarities present new opportunities for designing more efficient architectures. 
In this paper, we investigate the emergence of these internal similarities across different layers in diverse neural architectures, showing that similarity patterns emerge independently of the datataset used.
We introduce a simple metric, Block Redundancy, to detect redundant blocks, providing a foundation for future architectural optimization methods. Building on this, we propose Redundant Blocks Approximation (RBA), a general framework that identifies and approximates one or more redundant computational blocks using simpler transformations.
We show that the transformation $\mathcal{T}$ between two representations can be efficiently computed in closed-form, and it is enough to replace the redundant blocks from the network.
RBA reduces model parameters and time complexity while maintaining good performance. We validate our method on classification tasks in the vision domain, using a variety of pretrained foundational models and datasets.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper investigates the similarities across different layers in diverse neural architectures and assesses the redundancy of blocks in vision transformer based on the similarities of outputs between two blocks. Ultimately, redundant blocks are replaced with simple linear layers to achieve lightweight models. Experiments on multiple datasets and models demonstrate that the proposed method appears to be effective.

### Strengths
1. Code is released.
2. The paper is well-presented and easy to follow.
3. The experimental results and ablation study show the effectiveness.

### Weaknesses
1. In Equation 1, when $b=1$, what does $\bf{h} ^ {(0)} (x)$ represent?
2. In Line 147 on Page 3, the authors state that a higher BR indicates a potential redundancy in block $b$. Why is block $b-1$ not considered to be a redundant block? Similarly, in Line 158, why not skip $b _ i$ while retaining any layer or several layers from $b _ {i+1}$ to $b _ {i+n}$?
3. In Table 2, is the retraining step conducted under the 'skip' mode? If not, the accuracy after retraining should be reported.
4. This paper lacks the comparison with other model compression methods, such as pruning techniques.
5. The results on more complex datasets, such as ImageNet, should be reported. Also, can the proposed method be used to other tasks, such as object detection?

### Questions
Please see the weaknesses.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Based on the observation that multiple blocks in neural networks produce similar representations, the paper identifies these similar blocks (basically a vit encoder layer) and approximate the later blocks from previous blocks with similar representations. The paper uses the inverse of MSE between [CLS] tokens of transformers to identify redundant blocks. The redundant blocks are estimated using a linear transformation. The experiments showed that there is a increase in accuracy when approximating the redundant blocks in some cases but, in some cases accuracy decreases as well.

### Strengths
The paper studied an important problem of removing redundant blocks from a vision transformer. The study approximated all intermediate redundant blocks which can remove multiple maybe less redundant layers that still ultimately leads to a similar representation as the preceding layers. The paper perform experiments to measure accuracy on removing different redundant blocks. The writing is written in simple grammar making it easy to understand. The observation that redundant blocks are model specific and not data specific is important as it allows building an architecture that is inherently faster than the base model with similar capabilities. The paper provides detailed reproducibility statement in its appendix.

### Weaknesses
1. Novelty of Block Redundancy: Block redundancy is just the negative MSE of block i and block i+n outputs, cant an MSE just do the same job albeit a lower mse meaning more redundancy?
2. Tables 1,2 and 3 show that the best architecture needs to be searched and there is no singular dataset agnostic architecture that consistently maintain or improve the performance as shown in figures 2 and 6, although the change in accuracy is less, in cases where the drop in accuracy is important, the complexity of finding the optimal architecture increases.  This could be because of two reasons, a.)The BR is too simple that it isnt a suitable metric to rank redundant blocks. b.) The linear approximation performed might not be optimal.

3. This paper is not the first to try replacing redundant parts of a vision transformer. Venkataramanan et al [1] does linear approximation of redundant attention layers. While both papers are different as replacement learning focuses on replacing complete encoder blocks, the linear approximation and redundancy metric [1] can easily be extended to block level replacement. How does the BR and linear approximation compare to Venkataraman et al's approach when performing block approximation? basically we need to compare the accuracy and throughput (if significant).

4. No results on downstream tasks like segmentation and object detection. This is important to understand the effectiveness of replacement of redundant blocks for tasks other than classification. The paper could apply the technique on Uformer on ADE20K dataset for Segmentation like in [1] and DETR on Pascal VOC / COCO for object detection. Feel free to use any other models or benchmarks other than specified.

Nitpick: In figure 6 in the row of DeiT-S there is are hidden column names behind the image, that could be cleared in case of preparing camera ready.

### Questions
I would improve my score if the following questions are answered:
1.  The need for BR and not simply using MSE? I suggest that the paper removes the contribution of BR and just stick with MSE or negative MSE.
2. Some results on segmentation and object detection? Whats important is whether we can get a dataset agnostic architecture of modern transformers with lesser parameters. If time does not permit both segmentation and object detection results performing only segmentation is also acceptable, but, it is important to compare the results with [1].
3. Can you provide ablations on BR and Linear Approximation with [1]? This is important to justify the design choices made in this paper.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper is interested in finding redundancy within deep neural network models and approximating redundant blocks using a linear transformation. The paper first introduces the Block Redundancy (BR) metric, that computes the MSE between representations of two consecutive blocks on a subset of training data, to evaluate changes in the internal representation of the models. Then, it proposes to approximate highly redundant blocks by finding a good linear transformation between the redundant representations. The linear transformation is found by solving a least square problem between the inputs and outputs of the redundant blocks. Finally, experiments show that using the approximated transformation on redundant blocks preserves performance while reducing number of parameters.

### Strengths
- **Significance**: The motivation and research questions of the paper can lead practical impacts. Finding redundancies and approximations for large pretrained models can reduce the number of parameters and make them lighter and more efficient at inference. To this end, the paper shows that we can find such simple approximations while preserving downstream performances.  
- **Quality**: The paper presents experiments on multiple pretrained Transformer models and multiple image datasets.   
- **Clarity**: The organization of the paper and the writing are clear. I appreciate the "Takeaway" part after each experimental subsection.

### Weaknesses
 **Originality**: 
  - The first part of the paper, regarding the similarities between inner representations of pretrained foundation models, echoes previous studies on the same topic such as Nguyen et al. (2020), as mentioned in the paper. The main difference in this first part, is that the study is done on larger transformer-based foundation models as opposed to convolutional architectures, but the same insights are found, so this is a small contribution in my opinion.
  - It is not clear to what aim the paper introduces this "BR" metric. Why not consider other established similarity metrics such as CKA (Kornblith et al., 2019), or directly the cosine similarity of consecutive representations, for instance ? Why should we use the BR metric instead of other metrics ? In other words, what is measured by BR that is not measured by other metrics ? Furthermore, the similarities between blocks are shown with pairwise cosine similarities in Figure 2 and Section 4.1. Why not use the BR metric in that case ? 
 
**Quality**:
  - There are two weaknesses with the BR metric that are not discussed in the paper: i) it can only be computed between representations of same dimensions, this is usually the case in transformer-based architectures, but not for different kind of architectures, such as CNNs for instance ; ii) the metric is sensitive to different scaling for the representations. That means, for instance, that if the transformation between the two representations is only a linear rescaling by a matrix $A$, such as $h^{(b)}(x) = A h^{(b-1)}(x)$, then $BR(b) = -\frac{||A - I||_2}{|D_{sub}|} \sum_{x \in D_{sub}} ||h^{(b-1)}(x)||_2$ which can be very low, even though the overall transformation can be easily approximated linearly. So I'm not sure the BR metric is a good proxy metric to evaluate if the blocks can be linearly approximated or not.
  - The link between the BR metric and the RBA approach is actually not that clear in the paper. Do we observe that redundant blocks found by BR are actually the ones we can "remove" by RBA ? In experiments in Table 1, results when applying RBA to a lot of different blocks are shown, but I don't see a link with actual values of BR for these blocks.

**Significance**:
  - The experiments are only conducted on small scale datasets, the study would be more meaningful and significant with bigger datasets like ImageNet, at least, to evaluate scalability.
  - While the idea of approximating whole blocks to reduce number of parameters is conceptually interesting, is it better than pruning ? Do we achieve a better reduction of number of parameters while preserving performance ? 
  - If I understand correctly, the RBA are computed in closed form using 3000 training samples of the *corresponding* dataset the model is then evaluated on. To what extent these approximations transfer from one dataset to another ? If we use 3000 images from cifar10 to approximate some layers, do we preserve performance on ImageNet ?

- The method has the inherent weakness of being only applicable to transformer architectures.
- The question of sensitivity to rescaling is a problem. I'm not convinced that MSE is the best metric to estimate if a layer can be approximated by a linear representation because of that.
- I'm not convinced by the discussion regarding comparison with pruning methods.   First, I do not agree that all pruning methods require fine-tuning or training. From a quick search, Singh & Alistarh (2020) [A] presents results in "one-shot pruning" without re-training the pruned network. Therefore, it is a setting considered in pruning, which could serve as a ground for comparison with the proposed method. Second, while I agree that the method has the advantages of computing linear approximations in closed form without retraining the model, and that comparisons should be fair, it is currently very difficult to evaluate the effectiveness and the significance of the "reduction in trainable parameters shown in Table 1" in a vacuum, without a comparison.

Furthermore, I also agree with the weakness raised by reviewer tZQp about the method requiring a NAS. There is currently no obvious way to find the good set of layers to approximate, thus requiring to compute a lot (maybe all) of possible combinations. This can be seen in Figure 6, with ViT-S on ImageNet. Approximating 4-> 5 gives lower performance thant 2->3, even though BR is better for 4->5.

### Questions
I've written specific questions in the Weaknesses part, please refer to that. I've tried to compile some of the questions below:
- Why not consider the BR metric in the pairwise similarity matrices shown in Figure 2 ?
- Is there a link between BR and the preservation of performance after RBA in Table 1 ?
- If we compute RBA with data from one dataset, does it transfer to a different dataset ?
- Are the values shown for "Params" in Table 1 including the RBA parameters of the approximated block(s) ?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a framework to optimize deep neural networks by detecting and approximating redundant computational blocks, aiming to reduce computational complexity without sacrificing performance. The authors propose a metric called Block Redundancy (BR), which identifies components that do not contribute significantly to the network’s final output.  Using this metric, they develop Redundant Blocks Approximation (RBA), a method that approximates these redundant blocks through simple transformations.

### Strengths
- The paper is clearly written and easy to follow. 
- The idea of BR and RBA approach is simple and intuitive

### Weaknesses
 - The paper aims to develop an algorithm for training-free compression of visual transformers. However, the related work appears to be lacking. Several methods such as [1, 2] that achieve compression with minimal training are missing.

- Comparison with state-of-the-art methods is missing. Benchmarking against established compression techniques is essential for positioning RBA’s efficacy relative to existing approaches. 

- The experimental evaluation is limited to small datasets, making it difficult to assess RBA’s robustness for larger, more complex datasets such as ImageNet. Demonstrating generalization on larger datasets would strengthen the claim of RBA’s scalability and efficiency.

### Questions
Please refer to Weaknesses

### Soundness
2

### Presentation
3

### Contribution
2
