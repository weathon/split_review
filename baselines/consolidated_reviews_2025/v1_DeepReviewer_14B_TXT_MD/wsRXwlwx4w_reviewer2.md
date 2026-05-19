### Summary

This paper proposes a novel fine-tuning method called CoPrompt for vision-language models. The method enforces consistency constraints between the trainable and pre-trained models to prevent overfitting and improve generalization. The authors introduce two additional components to enhance the proposed consistency constraint: enforcing consistency on two perturbed inputs and combining prompting and adapter tuning. Experimental results show that CoPrompt outperforms existing methods on various evaluation suites.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The proposed method is well-motivated and reasonable.
2. The experiments are extensive and demonstrate the effectiveness of CoPrompt.
3. The ablation studies provide valuable insights into the contribution of each component in CoPrompt.

### Weaknesses

#### Some Related Works


#### comment

1. The authors claim that they are the first to combine prompting and adapter tuning, which is not true. The paper fails to cite or discuss previous works that have explored this combination, such as Parameter-Efficient Transfer Learning for NLP (PoCo) and Prompt-as-Adapter: Parameter-Efficient Transfer Learning for Vision-and-Language Few-Shot Learning (Prompt2Adapter). This oversight undermines the novelty of the proposed method.

2. The paper lacks a comparison with MaPLe using a similar number of parameters. MaPLe achieves comparable performance with only 3.55M learnable parameters, while CoPrompt uses 4.74M learnable parameters. A fair comparison should be made with methods having a similar parameter budget to accurately assess the effectiveness of the proposed method.

3. The paper does not provide a comparison of inference speed. While the authors mention that CoPrompt has around 2x FLOPs compared to MaPLe, a direct comparison of inference time is missing. This is a crucial aspect for practical applications and should be included.

4. The paper lacks a comparison with methods that use adapters only. It is important to understand the individual contributions of prompting and adapter tuning. A comparison with methods that use adapters only, such as CLIP-Adapter, would provide valuable insights.

5. The paper does not provide a comparison with methods that use prompting only. Similar to the previous point, a comparison with methods that use prompting only, such as CoOp, would provide valuable insights into the effectiveness of the proposed method.

6. The paper does not provide a comparison with methods that use prompting and adapters on both image and text branches. A comparison with methods like Prompt2Adapter would provide a more comprehensive evaluation of the proposed method.

7. The paper does not provide a comparison with methods that use prompting and adapters on only the text branch. A comparison with methods like CoCoOp would provide a more comprehensive evaluation of the proposed method.

### Suggestions

The paper needs to address the lack of comparison with existing methods that combine prompting and adapter tuning. Specifically, the authors should include a detailed comparison with Prompt2Adapter, which also combines prompting and adapter techniques for vision-and-language models. This comparison should not only focus on performance metrics but also on the number of learnable parameters, inference speed, and the specific implementation details of each method. Furthermore, the authors should clarify the novelty of their approach in light of these existing methods. A more thorough discussion of the related work is needed to accurately position the contribution of this paper.

To provide a fair evaluation of the proposed method, the authors should conduct experiments with a similar number of learnable parameters as MaPLe. This would involve adjusting the number of layers or the dimensionality of the adapters in CoPrompt to match the parameter count of MaPLe. This comparison would allow for a more accurate assessment of the effectiveness of the proposed consistency-guided training approach, independent of the number of parameters. Additionally, the authors should provide a detailed comparison of inference speed, including the time taken for a single forward pass, and the FLOPs required for both training and inference. This is crucial for understanding the practical applicability of the proposed method.

Finally, the authors should include comparisons with methods that use adapters only (e.g., CLIP-Adapter), prompting only (e.g., CoOp), and other combinations of prompting and adapters on both image and text branches (e.g., Prompt2Adapter) and only on the text branch (e.g., CoCoOp). These comparisons would provide a more comprehensive understanding of the individual contributions of each component and the overall effectiveness of the proposed method. The ablation study should also include a comparison with a version of CoPrompt that only uses prompting, and another version that only uses adapters, to isolate the effect of each component. This would help to understand whether the performance gains are due to the combination of prompting and adapters, or whether one of the components is more important than the other.

### Questions

Please see the weaknesses.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
