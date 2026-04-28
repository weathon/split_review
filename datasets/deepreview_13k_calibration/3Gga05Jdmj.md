# CtrLoRA: An Extensible and Efficient Framework for Controllable Image Generation

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
\vspace{-1.5ex}
Recently, large-scale diffusion models have made impressive progress in text-to-image (T2I) generation.
To further equip these T2I models with fine-grained spatial control, approaches like ControlNet introduce an extra network that learns to follow a condition image.
However, for every single condition type, ControlNet requires independent training on millions of data pairs with hundreds of GPU hours, which is quite expensive and makes it challenging for ordinary users to explore and develop new types of conditions.
To address this problem, we propose the CtrLoRA framework, which trains a \textit{Base ControlNet} to learn the common knowledge of image-to-image generation from multiple base conditions, along with \textit{condition-specific LoRAs} to capture distinct characteristics of each condition.
Utilizing our pretrained Base ControlNet, users can easily adapt it to new conditions, requiring as few as 1,000 data pairs and less than one hour of single-GPU training to obtain satisfactory results in most scenarios.
Moreover, our CtrLoRA reduces the learnable parameters by 90\% compared to ControlNet, significantly lowering the threshold to distribute and deploy the model weights.
Extensive experiments on various types of conditions demonstrate the efficiency and effectiveness of our method.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes CtrLoRA for better controllability of the conditional image generation. This framework trains a Base ControlNet for the general image-to-image generation and then uses the LoRA fine-tuning for specific user instructions. Experiments show the effectiveness of the proposed method.

### Strengths
- The paper is well-organized and easy to follow.
- The authors conduct sufficient ablation studies to evaluate the proposed modules.
- The experiments demonstrate the training efficiency of the proposed method and its capability to unify various visual conditions for generation.

### Weaknesses
 - The authors train a base ControlNet for the subsequent LoRA fine-tuning. However, why not directly fine-tune a pre-trained ControlNet or Uni-ControlNet? It is unclear why training a new base ControlNet is necessary, especially given the computational cost. The paper should provide a more thorough justification for this design choice, including a comparison of training times and resource usage.

- Lack of comparison to: ControlNet++[1]. The absence of this comparison makes it difficult to assess the relative performance of the proposed method against a strong baseline. The paper should include quantitative results and a qualitative analysis of the differences between the two methods.

- The paper does not explore whether this method can be generalized to other diffusion models such as SDXL and Pixart. This limits the impact of the work, as the current trend is towards larger and more powerful models. The paper should at least discuss the potential challenges and opportunities of extending the method to these models.

### Questions
Please refer to the weakness.

### Soundness
3

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
This paper proposes CtrlLoRA, a two-stage parameter-efficient fine-tuning pipeline, to ease the original ControlNet's computation burden in terms of different conditions. The authors evaluate CtrlLoRA through extensive experiments by both the quality and the computation efficiency.

### Strengths
1. This paper focus on an important problem, extending ControlNet to a lightweight manner.
2. Experimental results are impressive, especially the convergence experiment.

### Weaknesses
1. In line 70, the authors state that ControlNet with Canny edges requires 3 million images over 600 GPU hours for one condition. In contrast, line 244 indicates that Base ControlNet necessitates millions of images for 6000 GPU hours for 9 conditions. Although it is not fair enough, but it implies that the proposed method does not significantly reduce the computational burden.

2. In line 239, the mechanism of training with 9 conditions is not clear enough. As different conditions have different levels of sparse information of input images, why they have equal training iterations? And continuous shifting between different conditions may make the training hard.

3. the motivation why the new conditions are not trained as the Base ControlNet by a shifting mechanism is not clear enough.

4. Most results are from "Base CN + CtrlLoRA'', and results from "Community Model + CtrlLoRA" in Figure 11a are rare, not enough to convince that CtrlLoRA is effective when transferring to other community models.

5. pretrained-VAE seems to be only an interesting trick.

6. putting all the prompts in the appendix makes reading inconvenient.

### Questions
1. The results in Figure11b demonstrate that the different conditions are effectively disentangled, with a direct summation module according to Figure 3c. Could you clarify why this module is effective, such as presenting the results of two elements both separately and after sum-up.

2. A detail, why not presenting all 9 base-condition results comparison to UniControl in Table 2?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper draws on the idea of combining a base model with PEFT (Parameter-Efficient Fine-Tuning) for controllable generation. It trains a Base ControlNet obtained through several condition-specific training processes, and then fine-tunes it with a small amount of data for newly introduced conditions to obtain different condition-specific LoRAs. This approach improves the efficiency of training new condition generators at a lower cost.

### Strengths
- To address the high cost of separately training different models for conditional generation tasks, this paper proposes a training method that transitions from a base controlnet model to a lightly fine-tuned lora model. This approach ensures generation quality while achieving a faster convergence rate.

- The paper shows many analyses of the proposed method and presents the results generated for a total of more than a dozen conditions.

- The paper is well structured and easy to follow.

### Weaknesses
 - The paper primarily aims to improve the training efficiency of all kinds of conditional models, hence it employs a series of LoRAs to train the newly introduced conditions based on the "Base ControlNet". However, there is relatively little comparison and discussion of existing methods that efficiently train ControlNet, such as T2I-Adapter, ControlLoRA, and SCEdit. Specifically, the paper lacks a detailed analysis of how its method compares to these alternatives in terms of training time, resource consumption, and performance on a variety of conditional generation tasks. A more thorough comparison would strengthen the paper's claims of improved efficiency.

- There currently exists a viable **controlnet-union** model, which can handle different conditions using a single model. This may be a higher-level representation of the training of the "Base ControlNet" model discussed in the paper. On the other hand, the use of LoRA for fine-tuning is relatively straightforward and has been implemented in previous community works, such as ControlLoRA. In comparison, the overall innovativeness of the paper is limited. The paper does not clearly articulate the specific advantages of its approach over these existing methods, particularly in scenarios where a single model for multiple conditions is desired. The incremental benefit of using a base model plus LoRA over direct LoRA fine-tuning is not sufficiently justified.

- The paper does not discuss how many conditions to use or how to select conditions for training the "Base ControlNet" to achieve optimal knowledge transfer effects. This lack of guidance makes it difficult to assess the general applicability of the proposed method. The paper should explore the impact of different base condition sets on the performance of new conditions, and provide recommendations for selecting base conditions to maximize knowledge transfer.

### Questions
- Regarding the discussion of "Adaptation to new conditions," while training a comparison method from scratch with a small amount of data may indeed result in slow convergence, what would be the results if we used a pre-trained conditional model (analogous to possessing a Base ControlNet) for fine-tuning?

- I'm curious about the performance between a pre-trained controlnet model available in the community and a model trained using proposed "Base + LoRA" with same conditions.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
In this paper, the authors propose a CtrloRA framework. This framework starts by training a basic ControlNet that handles various image conditions efficiently. With this trained network, one can quickly fine-tune it to adapt to new conditions using a task-specific LoRA—specifically, fine-tuning requires only 1,000 paired images and less than an hour on a single GPU. The experimental results confirm that this method greatly speeds up the training process for new image conditions. Based on these impressive findings, I recommend a weak acceptance. However, there are some unclear points and missing experiments in the paper (see the Question section), and my final decision will depend on the authors' responses to these issues.

### Strengths
The CtrloRA framework introduced in this paper allows users to quickly and efficiently fine-tune the ControlNet to new image conditions, with minimal resource consumption. The experimental results validate the effectiveness of this method. Additionally, the paper is well-structured and clearly written.

### Weaknesses
There are some unclear points and missing experiments in the paper (see the Question section), and my final decision will depend on the authors' responses to these issues.

### Questions
1. Consider specifying 1-2 new image conditions and key metrics (e.g., adaptation speed, data efficiency, performance) for comparing UniControl [1] fine-tuning to CtrLoRA. This would provide a clear, focused comparison.
2. Additional baselines are required for each base image condition. Comparisons should be made with a fully trained ControlNet, which has been trained exclusively under a single image condition, to establish a more comprehensive benchmark.
3. Similarly, for the new condition, it is essential to compare the performance of CtrLora against ControlNet when ControlNet has been fully trained on a single modality. This will provide a clearer understanding of their relative efficiencies.
4. It would be beneficial to explore how the number of image conditions used during the training of the base ControlNet affects its ability to learn new conditions. Insights into the scalability and adaptability of the base network could prove crucial for future applications.
5. I have noted that CtrloRA can perform low-level image enhancement tasks, such as low-light image enhancement. Could the authors demonstrate how CtrloRA performs in comparison to other diffusion models for low-light image enhancement? This could highlight potential advantages or unique features of CtrloRA in practical applications.

[1] UniControl: A Unified Diffusion Model for Controllable Visual Generation In the Wild.

### Soundness
3

### Presentation
3

### Contribution
3
