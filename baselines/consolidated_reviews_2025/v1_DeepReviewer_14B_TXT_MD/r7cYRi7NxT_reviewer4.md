### Summary

This paper introduces Hierarchical Side-Tuning (HST), a parameter-efficient transfer learning method designed to adapt large vision Transformer backbones to diverse downstream tasks. The tuning framework incorporates a trainable hierarchical side network that leverages the intermediate features of the pre-trained model and generates multi-scale features for making predictions. Extensive experiments illustrate that HST consistently outperforms previous state-of-the-art methods on diverse benchmarks, significantly reducing the performance disparity between PETL methods and full fine-tuning in dense prediction tasks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The proposed method is novel and effective. It leverages the intermediate features of the pre-trained model and generates multi-scale features for making predictions. 

2. The experimental results are strong. The proposed method consistently outperforms previous state-of-the-art methods on diverse benchmarks, significantly reducing the performance disparity between PETL methods and full fine-tuning in dense prediction tasks.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method seems to be a combination of several existing methods, such as Side-Tuning and LST. The novelty of the proposed method is not clear.

2. The proposed method is not the most parameter-efficient one, compared with methods like LoRA, SSF, and Bias.

3. The proposed method is not the most efficient one, compared with methods like LoRA, SSF, and Bias.

4. The proposed method does not perform well on some datasets, such as EuroSAT, Clevr/Distance, and SmallNORB/Ele.

### Suggestions

The paper introduces Hierarchical Side-Tuning (HST), a parameter-efficient transfer learning method for adapting large vision transformer backbones. While the method shows promising results, several aspects warrant further investigation. First, the novelty of HST needs to be more clearly articulated. The paper should explicitly highlight the differences between HST and existing methods like Side-Tuning and LST, focusing on the specific architectural choices and their impact on performance. A detailed ablation study could help to isolate the contributions of each component of HST, demonstrating how the hierarchical side network and the use of intermediate features lead to performance gains. Furthermore, the paper should provide a more in-depth analysis of the computational cost and memory footprint of HST compared to other parameter-efficient methods. This analysis should include a breakdown of the FLOPs and memory requirements for each component of the proposed method, as well as a comparison with LoRA, SSF, and Bias. This would help to clarify the trade-offs between performance and efficiency, and provide a more comprehensive understanding of the practical implications of using HST.

Second, the paper should address the performance limitations of HST on specific datasets. The authors should investigate the reasons behind the lower performance on datasets like EuroSAT, Clevr/Distance, and SmallNORB/Ele. This could involve analyzing the characteristics of these datasets and identifying the specific challenges they pose for HST. For example, it would be beneficial to explore whether the performance drop is due to the limited number of training samples, the complexity of the data, or the specific nature of the tasks. Based on this analysis, the authors could propose potential solutions to improve the robustness of HST across different datasets. This could involve incorporating data augmentation techniques, adjusting the architecture of the side network, or exploring different training strategies. Additionally, the paper should include a more detailed discussion of the limitations of HST and suggest potential directions for future research.

Finally, the paper should provide a more thorough comparison with other parameter-efficient methods. While the paper compares HST with LoRA, SSF, and Bias, it would be beneficial to include a comparison with other state-of-the-art methods, such as AdaptFormer and NOAH. This would provide a more comprehensive evaluation of the proposed method and help to establish its position in the field. The comparison should include not only performance metrics but also computational cost and memory requirements. Furthermore, the paper should discuss the potential advantages and disadvantages of HST compared to other methods, highlighting the specific scenarios where HST is most effective. This would help to provide a more balanced and nuanced view of the proposed method and its potential impact on the field.

### Questions

Please see the weaknesses.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
