# Autoregressive Transformers are Zero-Shot Video Imitators

- Decision: Accept
- Scores: 8, 6, 8, 6

## Abstract
People interact with the real-world largely dependent on visual signal, which are ubiquitous and illustrate detailed demonstrations. In this paper, we explore utilizing visual signals as a new interface for models to interact with the environment. Specifically, we choose videos as a representative visual signal. And by training autoregressive Transformers on video datasets in a self-supervised objective, we find that the model emerges a zero-shot capability to infer the semantics from a demonstration video, and imitate the semantics to an unseen scenario. This allows the models to perform unseen tasks by watching the demonstration video in an in-context manner, without further fine-tuning. To validate the imitation capacity, we design various evaluation metrics including both objective and subjective measures. The results show that our models can generate high-quality video clips that accurately align with the semantic guidance provided by the demonstration videos, and we also show that the imitation capacity follows the scaling law.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a video generation based on autoregressive transformers trained with the objective of imitating a set of seed videos. In experiments, the authors show that the model is able to imitate tasks presented to it in an in-context manner. In addition, the learned representations coming from the model are also useful for classification tasks.

### Strengths
Originality:
The idea of performing in-context autoregressive video generation is interesting and I have not seen it being done before. Autoregressive video generation without text is very difficult, and this approach seems to address some of the difficulties.

Quality / Clarity:
The paper is clear and easy to read. The proposed idea is simple and I believe easy to replicate from the descriptions.

Significance:
I believe that even though this paper is not producing mind blowing results such as Sora, Kling, Veo and others. The ideas proposed here can be useful for the scientific community to continue exploring the problem of video generation

### Weaknesses
Weaknesses / Questions:

Missing baselines:
* Not sure if I missed this from reading the Baselines paragraph in the manuscript, but did the authors include a simple next frame prediction baseline?

### Questions
See weaknesses.

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
The authors proposed to train an autoregressive model for video imitation. The model training is performed in a self-supervised manner using a continuous video. Then, in the inference stage, given a demonstration and query video, the model could generate subsequent video frames of the query video that imitate the same semantics or actions conveyed by the demonstration video. The model shows zero-shot capacity when generating the imitation video frames.

### Strengths
- The topic of video imitation is valuable and would attract sufficient attention in the community, especially for embodied AI, since the approach could be applied to generate a large number of unseen training data, which is costly to obtain manually in the real world.
- It is interesting that the autoregressive model trained without using demonstration videos can generalise to the imitation inference stage when the demonstration is provided.
- The proposed framework is flexible and can be extended to imitate videos conditioned on text, which might be easier to acquire than demonstration videos and practically applicable.

### Weaknesses
 - On the technical side, the novelty of the proposed method is limited. The combination of VQ-VAE and Transformer is commonly adopted for image generation. Specifically, the use of a VQ-VAE for discrete latent representation of video frames, followed by a Transformer for autoregressive generation, is a well-established pipeline. The paper does not sufficiently articulate any novel modifications or architectural innovations beyond this standard combination.
- There is a lack of detailed explanation about why self-supervised training without acquiring demonstrations during training will generalise to video imitations given demonstrations. The paper does not provide a clear theoretical or mechanistic explanation for this generalization capability. It is unclear how the model learns to disentangle the semantics of actions from the specific visual context during training, and how this disentanglement enables imitation of novel actions from a demonstration video.
- The visual quality of the generated imitation video is limited as shown in Table 1. The V-Acc and P-Acc scores are quite low, suggesting that the generated video's content might differ from the expected one. The low V-Acc and P-Acc scores, which are based on a pre-trained video classifier, indicate a significant discrepancy between the generated and ground truth videos. This raises concerns about the practical applicability of the proposed method. Failure cases would help readers understand the method's limitations. I suggest the authors provide a detailed analysis accordingly. It would be beneficial to see examples where the model fails to capture the nuances of the demonstration video or generates semantically inconsistent content.
- The evaluation of using text as conditions is very limited. The paper only provides a brief demonstration of text conditioning, without a thorough analysis of its capabilities and limitations. The experiments do not explore the model's ability to handle complex or ambiguous textual descriptions, or to generate videos that accurately reflect the semantic content of the text. The lack of quantitative metrics for text-conditioned video generation makes it difficult to assess the effectiveness of this aspect of the model.
- The quality of writing could be further improved by providing more details regarding task definition and technical details. For example, it would be better to list all the types of demonstration videos. Currently, it is unclear if any more tasks are involved other than object manipulation and camera movement (and their detailed types). The training objectives could be clarified (currently missing) for those unfamiliar with VQ-VAE/VQ-GAN for better reproducibility. Specifically, the paper lacks a clear description of the loss function used for training the autoregressive model, and how it interacts with the VQ-VAE component.

### Questions
- It is confusing to define a contrast action. What is the discipline? It might be better to provide a detailed list of all the situations that are considered.
- Is it possible to provide the V-acc and LPIPS scores in Table 2? In my view, V-acc and LPIPS are more faithful and direct measurements of the visual content of the generated videos.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces Video Imitator (VidIT), an autoregressive transformer model trained for zero-shot video imitation, enabling it to imitate the semantics of a given demonstration video and generate coherent video clips without requiring further fine-tuning. VidIT uses a next-token prediction objective to learn from video datasets, allowing it to generate video sequences that are semantically aligned with demonstrations. The model is evaluated on visual quality and semantic accuracy using both automatic metrics and human assessment.

### Strengths
1. Zero-shot Capability: VidIT achieves a zero-shot imitation capacity, enabling it to generalize from video demonstrations without further training.

2. Versatile Applications: The model can be applied to multiple downstream tasks, including robotic simulation, video planning, and segmentation.

3. Comprehensive Evaluation Benchmark: Both objective metrics and subjective human evaluations validate the quality and semantic coherence of generated videos.

4. Scalable Model: The model demonstrates improved performance when scaled up, providing strong semantic control in video generation.

### Weaknesses
1. Limited Sequence Length: Because now the mainstream video generation solutions have reached more than 5 seconds, the evaluation is primarily on short sequences; the performance on longer sequences remains untested.

2. Gap Between the Training Web Videos and Evaluation Metrics: In the benchmark constructed in this article, the domains of the evaluation metric are mostly in indoor scenes (SSv2), which is relatively limited. This is likely why adding more web videos to the training data did not make the model perform better. To get more accurate conclusions, evaluation metrics should be developed for more open scenarios and diverse tasks mentioned in the appendix, such as task imitator.

### Questions
How well does the model generalize to longer video sequences compared to the current evaluations on short clips?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper trains autoregressive Transformers on video datasets in a self-supervised manner, enabling the model to infer and imitate semantics from a demonstration video in a zero-shot way, allowing it to perform unseen tasks without fine-tuning.

### Strengths
1. This paper trained a transformer model called VidIT, which can learn motion information from a reference video and apply this motion to the prediction of a target video.

2. The method is effective, as extensive experiments demonstrate significant improvements in metrics, and the visual results further prove that the method effectively learns motion information.

3. This approach is based on an interesting discovery, which the authors define as "zero-shot video imitators." This finding could inspire future work in the transformer series.

4. The method can be applied to various tasks, such as unconditional video prediction, proving its strong generalization ability.

### Weaknesses
1. However, the main contributions of this paper are not entirely clear to me. I believe there might be two key contributions:
a) The development of a video imitator model capable of mimicking actions from a reference video.
b) The demonstration that transformers possess zero-shot capabilities without needing specific training for tasks involving action imitation.

If the primary contribution is the first point, then the task of "imitating actions from a reference video" has been addressed in several previous works [1, 2]. Moreover, achieving the results shown in this paper could also be done using some existing open-source video editing models. Additionally, similar effects can be achieved by controlling camera angles [3].

If the primary contribution is the second point, then readers of this paper would be highly interested in understanding why transformers possess this zero-shot ability. However, the paper only demonstrates through experiments that task-specific training and the zero-shot approach yield similar performance. In my opinion, this is insufficient to explain the transformer's zero-shot capabilities. I recommend providing evidence through analyses of feature maps or attention scores to support this claim.

2. In Section 4.1, the paper introduces four settings but ultimately selects two. It is recommended that the names of these settings remain consistent throughout the paper to avoid confusing the readers. Also, ensure that these names are consistent with the names used in the experiments in Section 5.

3. Additionally, I suggest including more details about the training process, such as the hardware used and the approximate training time.

### Questions
1. However, the main contributions of this paper are not entirely clear to me. I believe there might be two key contributions:
a) The development of a video imitator model capable of mimicking actions from a reference video.
b) The demonstration that transformers possess zero-shot capabilities without needing specific training for tasks involving action imitation.

If the primary contribution is the first point, then the task of "imitating actions from a reference video" has been addressed in several previous works [1, 2]. Moreover, achieving the results shown in this paper could also be done using some existing open-source video editing models. Additionally, similar effects can be achieved by controlling camera angles [3].

If the primary contribution is the second point, then readers of this paper would be highly interested in understanding why transformers possess this zero-shot ability. However, the paper only demonstrates through experiments that task-specific training and the zero-shot approach yield similar performance. In my opinion, this is insufficient to explain the transformer's zero-shot capabilities. I recommend providing evidence through analyses of feature maps or attention scores to support this claim.

2. In Section 4.1, the paper introduces four settings but ultimately selects two. It is recommended that the names of these settings remain consistent throughout the paper to avoid confusing the readers. Also, ensure that these names are consistent with the names used in the experiments in Section 5.

3. Additionally, I suggest including more details about the training process, such as the hardware used and the approximate training time.

### Soundness
3

### Presentation
3

### Contribution
2
