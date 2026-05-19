### Summary

This paper proposes a recurrent video enhancement network (ReBotNet) for real-time video enhancement. The authors introduce a dual-branch architecture that processes spatio-temporal features and image tokens separately, along with a recurrent training approach that leverages the previous prediction as an additional input. The authors also curated two new datasets, PortraitVideo and FullVideo, which emulate real-world video enhancement scenarios. Experimental results show that ReBotNet outperforms existing methods in terms of computational cost and inference time.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple and easy to understand.
3. The experiments are comprehensive, including both quantitative and qualitative results.

### Weaknesses

#### Some Related Works

[1] Diverse video frame interpolation with transformer.
[2] Video restoration transformer.

#### comment

1. The authors claim that the proposed method is lightweight and fast, but the authors did not compare it with other lightweight models. The authors should compare it with other lightweight models to demonstrate its advantages. Specifically, the paper lacks a comparison with methods that explicitly focus on reducing computational cost, such as those employing efficient attention mechanisms or lightweight convolutional architectures. Without such comparisons, it is difficult to assess the true efficiency of the proposed method relative to the state-of-the-art in lightweight video processing.
2. The authors should compare the proposed method with more recent video restoration methods, such as [1, 2]. The current comparison is limited to older methods, and the field of video restoration has seen significant advancements in recent years. The absence of comparisons with these more recent methods makes it difficult to ascertain the true performance of the proposed method in the context of the current state-of-the-art.
3. The authors should compare the proposed method with other video restoration methods in terms of computational cost. The paper only compares the proposed method with a few older methods, and it does not provide a comprehensive analysis of the computational cost compared to other recent video restoration methods. This makes it difficult to understand the trade-offs between performance and computational resources.
4. The authors should provide more details about the datasets used in the experiments. The paper lacks sufficient information about the datasets, including the size, diversity, and characteristics of the data. This makes it difficult to assess the generalizability of the proposed method and to compare it with other methods that may have been evaluated on different datasets.

### Suggestions

The paper would benefit significantly from a more thorough evaluation of the proposed method's efficiency. Specifically, the authors should include comparisons with other lightweight video processing models, such as those employing efficient attention mechanisms or lightweight convolutional architectures. This would provide a more comprehensive understanding of the trade-offs between performance and computational cost. For example, the authors could compare their method against models that use depthwise separable convolutions or other parameter-efficient techniques. Furthermore, the authors should provide a detailed analysis of the computational cost of their method, including the number of parameters, FLOPs, and memory usage. This analysis should be compared with other recent video restoration methods to demonstrate the efficiency of the proposed method.

To address the lack of comparison with recent video restoration methods, the authors should include a more comprehensive evaluation against state-of-the-art techniques. This should include methods that use transformer architectures, as well as other recent approaches in video restoration. The authors should also consider comparing their method against methods that are specifically designed for real-time video enhancement, as this would provide a more relevant comparison. The evaluation should include both quantitative metrics, such as PSNR and SSIM, and qualitative assessments of the visual quality of the enhanced videos. This would provide a more complete picture of the performance of the proposed method in the context of the current state-of-the-art.

Finally, the authors should provide more details about the datasets used in the experiments. This should include the size, diversity, and characteristics of the data, as well as any preprocessing steps that were applied. The authors should also consider providing a more detailed description of the evaluation protocol, including the specific metrics that were used and the criteria for determining the quality of the enhanced videos. This would make it easier for other researchers to reproduce the results and to compare their methods with the proposed approach. Furthermore, the authors should consider evaluating their method on a wider range of datasets to demonstrate its generalizability.

### Questions

1. The authors should compare the proposed method with other lightweight models.
2. The authors should compare the proposed method with more recent video restoration methods.
3. The authors should compare the proposed method with other video restoration methods in terms of computational cost.
4. The authors should provide more details about the datasets used in the experiments.

### Rating

5

### Confidence

5

**********
