### Summary

This paper introduces a novel federated learning approach, Federated Dual Prompt Tuning (Fed-DPT), which utilizes a pre-trained vision-language model and applies both visual and textual prompt tuning to address domain shift challenges in a decentralized data setting. Extensive experiments demonstrate the effectiveness of Fed-DPT in domain-aware federated learning, significantly outperforming the original CLIP model.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow.

2. The proposed method is simple yet effective, surpassing various baselines on DomainNet.

### Weaknesses

#### Some Related Works

[1] Learning to prompt for vision-language models.
[2] A survey on visual prompt tuning.

#### comment

1. The scenario presented in the paper may be limited. The authors assume that each client corresponds to a specific domain with distinct statistical features. However, in real-world scenarios, federated learning often involves non-i.i.d. issues arising from various sources of data heterogeneity. For instance, data from different clients may vary in image styles, age, or gender distributions. The proposed method focuses solely on domain-specific text prompts for each client, which may not be applicable or effective in addressing the diverse non-i.i.d. challenges encountered in real-world federated learning settings. This raises concerns about the practical applicability and generalizability of the proposed method beyond the specific domain-centric scenario considered in the paper.

2. The authors propose visual and textual prompt tuning for federated learning, which has been extensively explored in previous works [1, 2]. Simultaneously, there are numerous works focusing on prompt tuning for federated learning. The authors should provide a more comprehensive discussion and comparison with these existing works to better position their contributions within the broader research landscape.

3. The paper lacks essential details regarding the implementation of visual and textual prompts. The authors should provide a thorough explanation of how these prompts are implemented in the context of CLIP. For instance, what is the specific form of the prompts? Are they learnable parameters or fixed templates? How are they incorporated into the input of the vision and language models? Providing these details would enhance the clarity and reproducibility of the proposed method.

4. The proposed method primarily addresses domain shift challenges in federated learning. However, it may not be suitable for other non-i.i.d. issues commonly encountered in real-world scenarios. For example, in medical imaging, data from different clients may vary in terms of image acquisition protocols, scanner manufacturers, or patient populations. These variations can introduce complex non-i.i.d. patterns that go beyond simple domain shifts. The authors should acknowledge these limitations and discuss the potential challenges and adaptations required to apply their method to such diverse and complex scenarios.

### Suggestions

The paper would benefit from a more thorough exploration of the non-i.i.d. challenges that arise in real-world federated learning scenarios. The current approach, which focuses on domain-specific text prompts, may not be sufficient to address the diverse heterogeneity present in practical applications. For instance, in a medical imaging context, variations in image acquisition protocols, scanner manufacturers, and patient populations can introduce complex non-i.i.d. patterns that go beyond simple domain shifts. The authors should consider how their method could be extended to handle such scenarios, potentially by incorporating techniques that can adapt to different types of data heterogeneity. This could involve exploring methods for learning client-specific visual prompts or incorporating mechanisms that can account for variations in data distributions beyond domain shifts. Furthermore, the authors should provide a more detailed analysis of the limitations of their approach and discuss potential future directions for addressing these challenges.

To strengthen the paper, the authors should provide a more comprehensive comparison with existing works on prompt tuning for federated learning. While the authors mention that their method is simple, they should also demonstrate a clear understanding of the existing landscape and highlight the unique contributions of their approach. This could involve a more detailed discussion of the similarities and differences between their method and other prompt-based federated learning techniques. For example, the authors could compare their approach to methods that use learnable prompts, fixed prompts, or combinations of both. They should also discuss the advantages and disadvantages of their approach compared to these existing methods, providing a more nuanced understanding of the trade-offs involved. A more thorough comparison would help to better position the contributions of this work within the broader research landscape.

Finally, the paper needs to provide more details regarding the implementation of visual and textual prompts. The authors should clearly explain how these prompts are incorporated into the CLIP model, including the specific form of the prompts, whether they are learnable parameters or fixed templates, and how they are integrated into the input of the vision and language models. For example, if the prompts are learnable parameters, the authors should describe how they are initialized and optimized during training. If they are fixed templates, the authors should explain how these templates are designed and how they are incorporated into the input. Providing these details would enhance the clarity and reproducibility of the proposed method, allowing other researchers to better understand and build upon this work. The authors should also consider including ablation studies to evaluate the impact of different prompt designs on the performance of their method.

### Questions

Please refer to the weakness section.

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
