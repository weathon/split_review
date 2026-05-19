### Summary

This paper proposes a new method for zero-shot quantization, which uses proxy data to substitute for original data, thus reducing the cost of acquiring original data. The authors also propose a method for selecting proxy data. Experimental results show that the proposed method has a significant performance improvement.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The proposed method is simple and effective.
2. The paper is well-written and easy to follow.

### Weaknesses

#### Some Related Works

[1] Exploring the potential of proxy data for data-free knowledge distillation.
[2] Ds-quant: A data-free and scaling-friendly post-training quantization framework.

#### comment

1. The novelty of the proposed method is limited. The idea of using proxy data to substitute for original data is not new [1]. The proposed method is very similar to the method in [1], and the difference is that [1] uses the proxy data to guide the generation of synthetic data, while this paper uses the proxy data to directly participate in the quantization process. The core idea of leveraging a proxy dataset to mitigate the need for original data is already explored, and the current approach of directly incorporating proxy data into quantization, while different, does not introduce a fundamentally new concept. The method's reliance on a proxy dataset, even if not directly used for synthetic data generation, is a well-trodden path in data-free learning.
2. The paper lacks a comparison with existing data-free quantization methods. The paper should compare the proposed method with existing data-free quantization methods to demonstrate its effectiveness. The absence of a direct comparison with other data-free quantization techniques makes it difficult to assess the true contribution and performance of the proposed method. Without such a comparison, it's unclear if the gains are significant relative to other approaches that also aim to avoid the need for original data.
3. The experiments are insufficient. The experiments are not sufficient to demonstrate the effectiveness of the proposed method. The paper should include more experiments to validate the proposed method. The limited experimental scope raises concerns about the generalizability of the findings. More diverse datasets and model architectures should be considered to thoroughly validate the method's effectiveness.

### Suggestions

The paper needs to more clearly articulate the novelty of its approach in the context of existing work that utilizes proxy data. While the authors use the proxy data directly in the quantization process, the core idea of using a proxy dataset to mitigate the need for original data is not new. The paper should more clearly differentiate its approach from existing methods, such as the one mentioned in [1], and highlight the specific advantages of directly incorporating proxy data into quantization. A more detailed discussion of the differences in methodology and the specific benefits of the proposed approach is needed to establish its novelty. The authors should also consider exploring the theoretical underpinnings of why their approach works, which could further strengthen the contribution.

To address the lack of comparison with existing data-free quantization methods, the authors should include a comprehensive comparison with relevant baselines. This comparison should not only include performance metrics but also a detailed analysis of the computational cost and resource requirements of each method. The paper should clearly demonstrate how the proposed method compares to other data-free quantization techniques in terms of accuracy, efficiency, and robustness. This would provide a more complete picture of the method's strengths and weaknesses and allow for a more informed assessment of its contribution. The authors should also consider including a discussion of the limitations of their method and potential areas for future research.

Finally, the paper needs to include more extensive experiments to validate the effectiveness of the proposed method. The experiments should include a wider range of datasets, model architectures, and quantization settings. The authors should also consider including ablation studies to analyze the impact of different components of their method. For example, they could investigate the impact of different proxy datasets or different quantization parameters. This would provide a more thorough understanding of the method's behavior and allow for a more robust evaluation of its performance. The authors should also consider including a discussion of the limitations of their experimental setup and potential areas for future research.

### Questions

Please refer to the weakness part.

### Rating

5: marginally below the acceptance threshold

### Confidence

5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

**********
