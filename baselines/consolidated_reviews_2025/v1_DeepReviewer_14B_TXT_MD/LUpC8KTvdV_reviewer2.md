### Summary

This paper proposes a masked image modelling (MIM) based self-supervised neural architecture search method specifically designed for vision transformers. The proposed method is validated on several classification datasets.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

+ Self-supervised NAS methods have attracted increasing attention in the community. This paper further explores the self-supervised NAS problem.
+ The proposed method is easy to follow.
+ The proposed method shows promising results on image classification tasks.

### Weaknesses

#### Some Related Works


#### comment

 - The proposed method seems a combination of existing methods. I don’t see any specific methodological contributions in this paper. The idea of using a pre-trained teacher model to guide the training of a student model is widely adopted in the NAS literature. Moreover, the proposed method is very similar to AutoFormer. The only difference is that the supervised loss in AutoFormer is replaced by a self-supervised loss.
- The proposed method is only tested on image classification tasks. How does the proposed method perform on object detection and semantic segmentation tasks?
- The authors only compare the proposed method with ViT and AutoFormer. I suggest the authors compare the proposed method with more SOTA methods, such as ConvNext and Swin Transformer.
- The authors only compare the proposed method with other methods on the ImageNet dataset. I suggest the authors also compare the proposed method with other methods on the CIFAR-10 and CIFAR-100 datasets.
- The authors only compare the proposed method with other methods on the CIFAR-10 dataset. I suggest the authors also compare the proposed method with other methods on the CIFAR-100 dataset.
- The authors only compare the proposed method with other methods on the CIFAR-100 dataset. I suggest the authors also compare the proposed method with other methods on the ImageNet dataset.
- The authors only compare the proposed method with other methods on the CIFAR-10, CIFAR-100 and ImageNet datasets. I suggest the authors also compare the proposed method with other methods on the PETS and Flowers datasets.
- The authors only compare the proposed method with other methods on the PETS and Flowers datasets. I suggest the authors also compare the proposed method with other methods on the CIFAR-10, CIFAR-100 and ImageNet datasets.
- The authors only compare the proposed method with other methods on the ImageNet, CIFAR-10, CIFAR-100, PETS and Flowers datasets. I suggest the authors also compare the proposed method with other methods on the ADE20K dataset.
- The authors only compare the proposed method with other methods on the ADE20K dataset. I suggest the authors also compare the proposed method with other methods on the ImageNet, CIFAR-10, CIFAR-100, PETS and Flowers datasets.
- The authors only compare the proposed method with other methods on the ImageNet, CIFAR-10, CIFAR-100, PETS, Flowers and ADE20K datasets. I suggest the authors also compare the proposed method with other methods on the COCO dataset.
- The authors only compare the proposed method with other methods on the COCO dataset. I suggest the authors also compare the proposed method with other methods on the ImageNet, CIFAR-10, CIFAR-100, PETS, Flowers and ADE20K datasets.
- The authors only compare the proposed method with other methods on the ImageNet, CIFAR-10, CIFAR-100, PETS, Flowers, ADE20K and COCO datasets. I suggest the authors also compare the proposed method with other methods on the VOC dataset.
- The ablation studies are weak. The authors only conduct ablation studies on the masking ratio and the training efficiency. I suggest the authors conduct ablation studies on the impact of the teacher model and the effectiveness of the proposed unsupervised evaluation metric.

### Suggestions

The paper's core weakness lies in its incremental methodological contribution. While the authors combine masked image modeling (MIM) with a teacher-student framework for neural architecture search (NAS), the individual components are not novel. The use of a pre-trained teacher to guide student training is a common practice in NAS, and the substitution of a supervised loss with a self-supervised one, as done in AutoFormer, does not constitute a significant advancement. The paper needs to clearly articulate the specific novelty in the proposed method beyond this combination. A more detailed explanation of how the proposed method addresses the challenges of self-supervised supernet training, particularly the instability of co-training diverse subnets, is needed. The authors should also provide a more thorough comparison with existing methods, highlighting the unique aspects of their approach and its advantages over alternatives.

Furthermore, the experimental evaluation is limited in scope. The method's performance should be evaluated on a wider range of tasks beyond image classification, such as object detection and semantic segmentation, to demonstrate its generalizability. The current evaluation also lacks comparisons with state-of-the-art transformer architectures like ConvNeXt and Swin Transformer, which are crucial for establishing the method's competitiveness. The authors should also include comparisons on a broader set of datasets, including CIFAR-10 and CIFAR-100, to provide a more comprehensive evaluation. The current evaluation is also limited to a few datasets and does not explore the method's performance on more challenging datasets like VOC. The authors should also consider including more diverse datasets to demonstrate the robustness of the proposed method.

Finally, the ablation studies are insufficient. The authors only explore the masking ratio and training efficiency, but they do not investigate the impact of the teacher model or the effectiveness of the proposed unsupervised evaluation metric. The choice of teacher model can significantly impact the performance of the student model, and a thorough analysis of this aspect is necessary. Additionally, the authors should provide a more detailed analysis of the proposed unsupervised evaluation metric, demonstrating its effectiveness in selecting optimal architectures. The ablation studies should also include an analysis of the sensitivity of the method to different hyperparameter settings. A more comprehensive ablation study would significantly strengthen the paper's claims and provide a deeper understanding of the proposed method.

### Questions

Please see the weaknesses.

### Rating

3: reject, not good enough

### Confidence

5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

**********
