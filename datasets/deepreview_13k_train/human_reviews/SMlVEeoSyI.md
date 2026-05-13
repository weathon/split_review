# StretchySnake: Flexible VideoMamba for Short and Long-Form Action Recognition

- Decision: Reject
- Scores: 3, 6, 6

## Abstract
State space models (SSMs) have very recently been introduced as an alternative deep architecture to transformers, exhibiting competitive or superior performance across various language and vision tasks. However, both SSMs and transformers share certain limitations in the vision domain, namely spatio-temporal inflexibility. Traditionally, deep video models are trained on a fixed resolution and number of frames, often arbitrarily chosen as a trade-off between performance and computational cost. Changing the resolution and/or number of frames a model can ingest usually requires retraining the model, while avoiding re-training by variably changing the weights of a trained model leads to significantly reduced test accuracy. In this paper, we introduce a spatio-temporal flexible training method that encourages a single set of learned weights to adapt well to any input resolution or video length. We achieve this by simply randomly changing the spatial and temporal resolutions of a video during training, and dynamically interpolating the model's weights accordingly. This single change in training not only allows for one model to be applied to both short and long video understanding tasks alike, but also allows for user-specific tailoring of computational cost. We propose and evaluate $5$ different spatio-temporal flexible training methods to find the optimal type for training a video SSM. We then evaluate our best flexibly-trained SSM, which we call StretchySnake, across a variety of short- and long-form action recognition evaluation protocols, such as video retrieval, fine-tuning, and linear probing, and massively outperform the same vanilla video SSM trained in a standard fashion by up to $28$% in some cases. Therefore, our training method can be used as a simple drop-in training technique for any SSM-based video models to strongly improve performance and instill spatio-temporal and compute flexibility.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
To develop spatio-temporal feature representations that are robust across varying video lengths, the paper exposes pretrained VideoMamba models to random spatio-temporal input resolutions via resizing operations. The proposed method is evaluated on the UCF101, HMDB51, Breakfast, and COIN datasets. Ablation studies are conducted for different spatio-temporal resolutions, and visual analysis for video retrieval is also provided.

### Strengths
- The implementation details are sufficiently thorough, enhancing the reproducibility and reliability of this work
- The visual analysis provided is clear and convincing.

### Weaknesses
 - The intended purpose of Figure 2 is unclear. For instance, the spatial positional embeddings are obscured by other elements, and the temporal positional embedding, defined as $\textbf{ξ}^t$ with shape $1 \times S \times D$ on line 207, is illustrated as having only shape $D$.  On line 194, $S=H \times W \ (p \times p)$, but $S = 128/16=8$, which is very confused. 

- There is a mismatch between Fig.(2) and its caption, where the figure merely depicts a standard tokenization process for videos, while the caption emphasizes 'flexibility,' which is not effectively conveyed in this diagram. 

- The paper uses mathematical symbols inappropriately and inconsistently with established conventions, making it challenging for readers to fully understand the paper.

- There is a lack of comparisons with state-of-the-art (SOTA) methods on action recognition tasks. Additionally, StretchySnake’s performance is surpassed by SOTA methods, such as VideoMAE, which achieves 99.6% top-1 accuracy on UCF101, significantly higher than StretchySnake’s 96.5%.

- The four datasets used in the paper are small-scale. No results on larger scale datasets, such as Kinetics400/600 and Something-Something are provided in this paper.

- Overall, the concept of "st-flexibility" amounts to a straightforward spatio-temporal interpolation of the input, limiting the novelty of the idea and offering minimal contribution to the community.

### Questions
Please refer to the Weaknesses.

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces StretchySnake, a training method for video state space models (SSMs) that enhances spatio-temporal flexibility. The approach involves randomly varying the spatial and temporal resolutions of videos during training, allowing a single model to adapt to different input sizes without retraining. The authors evaluate five different spatio-temporal flexible training methods and find that "static tokens" perform optimally. StretchySnake, their best-performing model, significantly outperforms the standard VideoMamba across various action recognition datasets,

### Strengths
In general, the proposed method is somehow simple yet effective. The proposed method explores different settings of making the fixed resolution VideoMamba flexible to dynamic spatial and temporal resolution. Also, the proposed method performs extensive experiments on both short and long action recognition datasets to verify the effectiveness of the proposed method. Various visualization also makes the results more convincing.

### Weaknesses
Besides the strengths part, I still have some concerns about the paper:

1. The author starts to fine-tune the model from a self-supervised trained VideoMamba model. Then the author claimed that the static tokens perform best at flexible training, i.e., different time scales and different spatial resolutions. Will the self-supervised training (VideoMAE with token masking) dominate the downstream pattern and performance? I think solely fine-tuning and line-probing a pre-trained fixed-resolution model is less convincing than flexible training a model from scratch and then applying it in the downstream tasks. The author could perform a from-scratch pipeline, even in a smaller dataset to verify the effectiveness of the proposed method to make the result more convincing.

2. The author could have more datasets to convince the model. For example, the author chooses two appearance-based action recognition dataset like UCF101 and HMDB51, and 2 multi-label datasets like BreakFast and COIN. What if the proposed method are tested on some temporal sensitive datasets like Sth-Sth V2? If the author could verify that, I think the proposed paper can be more convincing.

3. For FLOPs calculation, the author could compare more with test time augmentations (i.e.), with fixed resolution models, but performing more inferences. Applying dynamic resolution to a fixed-resolution model is sometimes unfair here.

### Questions
Based on the weaknesses mentioned above, I have the following questions:

1. Is the static token pattern dominated by the upstream self-supervised learning tasks?

2. Will the static-token pattern also performs better on temporal related datasets like Sth-Sth V2?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper aims to train a flexible VideoMamba architecture, which can handle short and long-term video understanding by adapting different video resolution and temporal sampling rate. Accordingly, the paper proposes a simple yet effective stragety based on dynamically interpolating model weights. The authors conduct experiments on four short or long-term video datasets, namely UCF101, HMDB51, COIN and Breakfast, and the results demonstrate that the proposed training method can improve VideoMamba effectively.

### Strengths
1. The authors propose a simple yet effective method to adapt different video inputs, which seems to generalize to other domains. 
2. The proposed model can handle both short-term and long-term videos, which advances the applications of VideoMamba.

### Weaknesses
1. The authors conduct experiments on UCF101, HMDB51, COIN and Breakfast datasets, which are relatively small datasets. Can you provide results on relative larger datasets, e.g., Kinetics400, something-something-v2. The provided results on K400 are for video retrieval, not action recognition, which is the primary task for video architectures. While retrieval is a useful proxy, it does not fully validate the model's action recognition capabilities, especially given the different optimization objectives and evaluation metrics. Action recognition results on K400 and SSv2 are necessary to fully assess the model's performance.
2. As stated in Line 299~300, the authors verify the effectiveness of the proposed model mainly based on transfer learning experiments. How about the performance in vanilla fully-supervised setting? The paper lacks a thorough investigation of the model's performance when trained from scratch on a large-scale dataset, which is crucial for understanding its generalization ability and potential for real-world applications. The transfer learning results are promising, but they do not fully address the model's intrinsic learning capacity.
3. Can the proposed training recipe benefits downstream video understanding tasks, e.g., weakly-supervised action localization? The paper does not explore the potential benefits of the proposed training method for downstream tasks beyond action recognition, such as weakly-supervised action localization or video captioning. This limits the scope of the evaluation and leaves open questions about the broader applicability of the method.

### Questions
1. In Line 347~348, the authors conclude that the best type of st-flexibility modeling is static-tokens, according to the empirical analysis. Can you explain the reason in model design or learning? I think any insights you provide will benefit the society. 
2. As stated in Line 316~317, on Kinetics-400, you flexibly train the proposed model for 12 epochs, while train the vanilla VideoMamba for 50 epochs. Why? Is it not fair? How do the two models perform on Kinetics-400?

### Soundness
3

### Presentation
3

### Contribution
3
