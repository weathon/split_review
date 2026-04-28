# RDT-1B: a Diffusion Foundation Model for Bimanual Manipulation

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 6, 8, 6

## Abstract
Bimanual manipulation is essential in robotics, yet developing foundation models is extremely challenging due to the inherent complexity of coordinating two robot arms (leading to multi-modal action distributions) and the scarcity of training data. In this paper, we present the Robotics Diffusion Transformer (RDT), a pioneering diffusion foundation model for bimanual manipulation. RDT builds on diffusion models to effectively represent multi-modality, with innovative designs of a scalable Transformer to deal with the heterogeneity of multi-modal inputs and to capture the nonlinearity and high frequency of robotic data. To address data scarcity, we further introduce a Physically Interpretable Unified Action Space, which can unify the action representations of various robots while preserving the physical meanings of original actions, facilitating learning transferrable physical knowledge. With these designs, we managed to pre-train RDT on the largest collection of multi-robot datasets to date and scaled it up to $1.2$B parameters, which is the largest diffusion-based foundation model for robotic manipulation. We finally fine-tuned RDT on a self-created multi-task bimanual dataset with over $6$K+ episodes to refine its manipulation capabilities. Experiments on real robots demonstrate that RDT significantly outperforms existing methods. It exhibits zero-shot generalization to unseen objects and scenes, understands and follows language instructions, learns new skills with just 1$\sim$5 demonstrations, and effectively handles complex, dexterous tasks.
We refer to the \href{https://rdt-robotics.io/rdt-robotics/}{project page} for the code and videos.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper develops a 1.2B-parameter robotics foundation model that is trained and evaluated on real robot data for bimanual manipulation. The model is trained with imitation learning: (i) pretrained on 1M trajectories combining available datatsets collected for different robots, and (ii) fine-tuned on a self-collected dataset with 6k demonstrations for a Mobile Aloha robot. The model adopts a diffusion transformer (DiT) architecture that takes multi-modal inputs (images, language, etc.) and generate action chunks with multimodal distribution. 

The model is evaluated on 7 real robot tasks against mainstream baselines. The comparison shows that the model can: (i) generalize zero-shot to novel objects, scenes and language, (ii) learn new skills with few data, (iii) accomplish dexterous tasks. Ablation studies show that larger model and pretraining with large data significantly boost the performance.

### Strengths
The paper presents a complete and remarkable research work that pushes forward the boundary of large-scale robot learning. 
- The model is developed on top of the diffusion transformer with a unified action space, which allows large-scale pretraining on heterogeneous robot data to boost the performance
- The authors collect the largest robot dataset for bimanual manipulation with comprehensive task coverage for fine-tuning the model
- The experiments show that the advantage of the model from a foundation model aspect: generalization, few-shot learning, and scaling behavior

### Weaknesses
 - While the paper demonstrates that the foundation model is allows zero-shot and few-shot generalization, and can achieve dexterous manipulation, each of these characteristics is only validated on ~one task and may be insufficient. Evaluations on more tasks and existing benchmark tasks will complete the results.
- It seems that the baselines are not trained on the complete fine-tuning dataset. This doesn't form an apple-to-apple comparison.
- The writing of the paper has room for improvement. Some of the sentences are too long, which prevent reading of the paper smoothly.
- Mistakes in citing papers. For example, it seems that "Xie et al. 2020" is wrongly used as the reference of DiT in line 83 and 319.

### Questions
- The model uses frozen vision encoders. Does it mean existing pretrained visual representation is sufficient for robot manipulation? I wonder if the authors spot any cases where pretrained visual encoder is insufficient and lead to unsatisfactory performance.
- In pretraining on heterogeneous data with varied control frequency, the model takes control frequency as conditioning. I wonder how this strategy works in practice - does the model learns policy prior corresponding to different control frequency?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents an effort toward building a foundation model for bimanual manipulation. It proposes techniques to unify the action space, enabling training on a very large robot dataset. The authors also scale up the model to 1.2B parameters, making it the largest diffusion transformer model for robotics. In this process, the authors identify several key elements to improve training stability and performance. The resulting model achieves good zero-shot generalization performance on unseen and complex tasks.

### Strengths
This paper demonstrates strong performance in scaling up robotics models. It presents several interesting components that improve training stability and performance.

The unified action space, and especially the padding technique, is interesting.

The paper shows capabilities on several challenging real-world bimanual manipulation tasks.

### Weaknesses
Several claims are not very precise and not very clear. For example, the authors mention the nonlinearity and high frequency of robotic data. While it is true that the data is nonlinear, how does the proposed method tackle this challenge? The authors argue that changing the last linear layer to an MLP block solves this problem and brings significant performance improvements. While the performance is impressive, I think this requires more careful ablation experiments. Firstly, the entire diffusion transformer is already highly nonlinear due to stacking multiple layers, so why does adding more layers help in this case? Specifically, the transformer's attention mechanism and feed-forward networks already introduce substantial non-linearities; it is unclear why an additional MLP at the output would be so crucial. Secondly, in the original UNet diffusion policy, the last layer is a Conv1dBlock; have the authors compared with that? Lastly, why is it only evaluated on the dexterity task?

It is also unclear how the model design choices address the “high frequency of robotic data.” Given that these two claims are highlighted in the abstract as the main challenges, I believe they require more careful analysis and discussion. The authors should provide a more detailed explanation of how their specific architectural choices, such as the MLP decoder or the normalization layers, are designed to capture and process high-frequency components in the robotic data. Without this, the claims remain unsubstantiated.

As the unified action representation is a major contribution of this paper, there should also be more analysis of this aspect. For example, what are the performance gains from using all the data because of the unified action space, compared to previous methods that use “robots with similar action spaces (Yang et al., 2023; Ghosh et al., 2023; Kim et al., 2024) or retain only a subset of inputs sharing the same structure (Collaboration et al., 2023; Yang et al., 2024)”? Additionally, what is the performance gain of the proposed padding strategy compared with padding with all zeros? The paper lacks a direct comparison showing the impact of the unified action space and the specific padding strategy, making it difficult to assess their individual contributions.

The authors argue the necessity of using RMSNorm and QKNorm, but they only show the loss without them (Figure 4(a)), which provides very little information on how effective the proposed approach is and whether it addresses the instability issue. It also does not mention how to integrate these normalization layers within the transformer. The paper should include a more detailed analysis of the normalization layers, including how they are integrated into the transformer architecture and how they specifically address training instability. Simply showing a loss curve without these layers does not provide sufficient evidence.

Scaling up the models and data is certainly attractive, and the paper shows impressive results. However, most of the analysis are “binary”, which means the results are either with or without. Showing more datapoints (model with different size, using different percentage of the dataset) will present more insights to the reader.

### Questions
My questions are mainly also discussed in the weakness. Here is an summary:
1. Given that the diffusion transformer already contains multiple nonlinear layers, why does adding an additional layer improve performance? Have you conducted ablation studies to support this choice?
2. In the original UNet diffusion policy, the last layer is a Conv1dBlock. Have you compared the performance of your MLP block with this alternative?
3. What is the the MLP block performance gains on other tasks?
4. Can you provide more insight into how the model design specifically addresses high frequency change?
5. What are the performance gains from using all data through this unified action space compared to previous methods that only use robots with similar action spaces or retain subsets of inputs with a common structure?
6. How does the proposed padding strategy improve performance compared to zero padding? Could you provide comparative results?
7. How do these normalization layers integrate into the transformer architecture, and how do they address instability? Have you tested different configurations of these layers?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents the Robotics Diffusion Transformer (RDT), a large-scale diffusion-based model for bimanual robotics. RDT introduces a Physically Interpretable Unified Action Space to standardize actions across robots, enhancing generalization, and uses diffusion models to handle complex, continuous action distributions. Pre-trained on the largest multi-robot dataset and fine-tuned on a custom bimanual dataset, RDT demonstrates strong zero-shot and few-shot generalization, outperforming existing methods in dexterous, real-world tasks.

### Strengths
- The paper introduces a novel application of diffusion models to bimanual manipulation, addressing the high-dimensional, multi-modal action space through a Physically Interpretable Unified Action Space. This approach is a creative extension of diffusion models in robotics, particularly for dual-arm coordination, a challenging domain with limited prior work.

- The model is rigorously tested, with comprehensive experiments demonstrating superior performance over existing baselines. The use of the largest multi-robot dataset and a specialized bimanual dataset for fine-tuning enhances the validity of results and supports the model's effectiveness.

- This work contributes substantially to the field by advancing foundation models for robotic manipulation. RDT’s capabilities for zero-shot generalization, few-shot learning, and instruction following mark a significant step towards adaptable and scalable robotic models, with promising implications for real-world applications.

### Weaknesses
 - The paper introduces a Physically Interpretable Unified Action Space for handling data heterogeneity, but additional details on potential limitations or failure cases during training with highly diverse data would be beneficial. This could include examples where action standardization might lead to loss of unique features across robots, such as when robots have significantly different kinematic structures or when tasks require very specific, non-standardized motions. The paper should discuss how the unified action space might affect the model's ability to learn fine-grained control or adapt to unusual robot configurations.

- Although the experiments show impressive results, expanding the evaluation to more varied and complex real-world tasks (beyond the 6,000-episode dataset) and more hardwares(beyond ALOHA) could further validate RDT's robustness. The current evaluation, while comprehensive, might not fully capture the challenges of more intricate manipulation scenarios or the variability encountered with different robot platforms. It would be beneficial to see results on tasks that require more complex reasoning or involve a wider range of object properties and environmental conditions.

- The paper proposes several innovative multi-modal encodings (e.g., masking, cross-attention) but lacks ablation studies on these design choices. Showing how each component contributes to performance could clarify their impact on handling visual and language-conditioned tasks effectively. For example, it's unclear how much performance gain comes from the masking strategy versus the cross-attention mechanism, and whether these components are equally important for different types of tasks. A more detailed analysis of these design choices would strengthen the paper.

- There's a typo at L76, it should be "data" instead of "date" .

### Questions
- Could the authors elaborate on why diffusion models were specifically chosen over other generative methods like VAEs or GANs for this task? While diffusion models show high expressiveness, a comparison or rationale would clarify their unique benefits in bimanual manipulation.

- The Physically Interpretable Unified Action Space is innovative, but how does it handle robots with vastly different kinematics or action constraints?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a unified action representation to align different robots, facilitating pre-training on diverse robot datasets for bimanual manipulation. Additionally, it introduces a diffusion transformer-based architecture with several modifications for enhancing policy learning, and scaling up with large datasets.

### Strengths
A foundational model for bimanual manipulation is absent in the current community, which is an important direction; aligning different robot embodiments is also a crucial question for pre-training on large-scale datasets. The proposed action representation is simple yet effective for pre-training on diverse robot datasets.

### Weaknesses
Compared to the robot datasets used for pre-training the baseline, such as OpenVLA, this paper appears to use a more diverse set of datasets, including additional bimanual manipulation datasets like ALOHA and Mobile ALOHA, contributing nearly 10% of the total datasets. Fine-tuning a baseline pre-trained on single-arm datasets for a bimanual manipulation setting may result in poor performance on bimanual tasks, making it difficult to demonstrate that using the diffusion transformer architecture is superior to using a large language model as the pre-training backbone.

Furthermore, the comparison with the baseline is not entirely fair. The baseline is not pre-trained from scratch on the exact same dataset but is first pre-trained on a single-arm dataset, followed by modifications to the input and output for bimanual tasks, and then further pre-training. This multi-stage process could significantly impact the baseline's performance, making it challenging to isolate the effect of the proposed diffusion transformer architecture. The paper does not provide sufficient details on how the baseline models are adapted to bimanual tasks, particularly regarding the input and output modifications, and the extent of further pre-training on bimanual data. This lack of clarity makes it difficult to assess the validity of the comparison.

### Questions
1. "Does the RDT-1B fine-tuning use the entire self-collected dataset, and is it not fine-tuned separately for each task in the evaluation?"
2. "Regarding the computation of success rate for the 'wash cup' task with 'seen cup1': the success rate (SR) for 'get water' is 50, for 'pour water' is 87.5, and for 'place back cup' is also 87.5, yet the overall SR is listed as 50. Since the 'get water' subtask has an SR of 50, and the following subtasks have SRs below 100, how is the total SR calculated as 50?"

### Soundness
2

### Presentation
3

### Contribution
2
