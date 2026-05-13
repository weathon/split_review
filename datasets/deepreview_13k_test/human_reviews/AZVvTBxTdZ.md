# A Neural Architecture Dataset for Adversarial Robustness

- Decision: Reject
- Scores: 6, 5, 6, 5

## Abstract
Robustness to adversarial attacks is critical for practical deployments of deep neural networks. However, pursuing adversarial robustness from the network architecture perspective demands tremendous computational resources, thereby hampering progress in understanding and designing robust architectures. In this work, we aim to lower this barrier-to-entry for researchers without access to large-scale computation by introducing the first comprehensive neural architecture dataset under adversarial training, dubbed NARes, for adversarial robustness. NARes comprises 15,625 WRN-style unique architectures adversarially trained and evaluated against four adversarial attacks (including AutoAttack). With NARes, researchers can query the adversarial robustness of various models immediately, along with more detailed information, such as fine-grained training statistics, empirical Lipschitz constant, stable accuracy, etc. In addition, four checkpoints are provided for each architecture to facilitate further fine-tuning or analysis. For the first time, the dataset provides a high-resolution architecture landscape for adversarial robustness, enabling quick verifications of theoretical or empirical ideas. Through NARes, we offered some new insight and identified some contradictions in statements of prior studies. We believe NARes can serve as a valuable resource for the community to advance the understanding and design of robust neural architectures.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper spend tons of GPU resources to construct a huge benchmark on the relation between WRN architecture design and adversarial robustness. Specifically, the authors varied the depths and widths of WRN and used PGD-based adversarial training on CIFAR-10 dataset to get the adversarial robustness of the model architecture. 

Several interesting observations are found based on the benchmark results, which may benefit further research. I have concerns on whether those findings generalize to other model architectures beyond WRNs and CIFAR-10. 

The benchmark should be very welcomed by the NAS community, as a new benchmark for searching robust model architectures. I'm not sure how the benchmark could help wider communities, since the WRN + CIAFR-10 image classification + PGD adversarial training is only a very narrow scope in terms of robust machine learning. More advanced model architectures, larger-scale datasets, and tasks with better practical applications are missing in the current benchmark design.

### Strengths
1. Tons of GPU resources are generously spent to build the new benchmark. 

2. The observations from the benchmark results are all very interesting and may inspire future works. 

3. The benchmark should be very beneficial to the NAS community to design better search algorithms for robust model architectures.

### Weaknesses
My main concern is that the benchmark only covers a tiny scope in the field of robust machine learning. 
Specifically, the authors adopted the setting of WRN + CIAFR-10 image classification + PGD adversarial training, without very convincing justification. 
I'm aware that many previous adversarial training papers used similar settings. However, as a benchmark paper, it requires more attention, much more than papers proposing new algorithms, when it comes to designing the experiment settings, on which tons of resources will be spent. 
In my point of view, the WRN is not the best choice for image classification tasks, or as the backbone of detection and segmentation tasks, in year 2024. For applications running on cloud servers or where computation resources are not a constraint, large transformer-based models are dominant in terms of both clean accuracy and robustness under distributional shifts. For edge-device or other resource constrained devices, efficient vision transformers are dominant (e.g., [1]). Although these models are actually pure CNN models replacing the expensive multi-head self-attention with cheap token mixers like depth-wise convolution, their design of global architectures are very different with WRNs. They use the alternate token-mixer and channel-mixer design inspired by transformers. It is concerning if the conclusions from the benchmark do not generalize to these more advanced architectures. 
These transformer and efficient transformer models have also dominated applications such as object detection and segmentation, which have better practical applications than image classification, which leads to my second concern on the choice of the task in the benchmark. I'm fully aware that adversarial training papers typically adopt image classification as the primary benchmark task. But when it comes to real-world applications that requires high-level security, such as autonomous driving and security surveillance, detection and segmentation are more heavily used. As a benchmark paper, it would be good to focus not only on one single task, but on more tasks, especially those with more practical applications. My third concern is that the benchmark only adopts PGD-adversarial training (PGD-AT) as the defense method. It is not clear if the conclusions from PGD-AT generalizes to other defense methods (e.g. TRADE).

[1] FastViT: A Fast Hybrid Vision Transformer using Structural Reparameterization.

### Questions
Please see above.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper focuses on a valuable topic, namely, the robustness of the models. The main contribution of this paper lies on the proposed NARes dataset. This dataset is constructed for investigating the relationship between the model robustness and model architectures. NARes comprises 15,625 WRN-style architectures adversarially trained and evaluated against various adversarial attacks, such as AutoAttack. The authors provide extensive experimental results and meaningful observations.

### Strengths
1. The focused topic is valuable. Model robustness is of great significance in practical deep learning.
2. The scale of the proposed method is quite satisfactory. This paper constructs a large scale dataset that consists of 15,625 different model architectures and 62500 checkpoints in total.
3. The statement is clear and accurate. The organization and the writing of this paper is satisfactory that make the reader easily understand the core idea and meaningful conclusions.

### Weaknesses
My biggest concern to this work is its novelty. As far as I know, the RobustArt has not only investigated the relationship between the model architecture and robustness, but also investigated the features among model architectures, the training techniques, the adversarial noise robustness, the natural noise robustness, and the system noise robustness, which in fact takes the first step in this area. Compared with the RobustArt, the strengths of this study could only appear in the dataset scale and fine-grained factors, e.g., the width, depth. #MACs, and LIP of WRNs. I believe this study is meaningful and valuable, but it seems this study is more likely to be a star project in the open-source area. By the way, the statement about the RobustArt in section 2.3 appears to be misleading.

### Questions
(1) Plz carefully clarify the differences between this study and the RobustArt in the perspective of novelty.
(2) It could be more acceptable to provide some overall information, such like a leaderboard.
(3) This is quite a good work, but the open-source link is not provided.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors propose a new benchmark for architecture search of adversarially robust networks. They evaluate various depth and width settings in WideResNet. They also benchmark various architecture search algorithms on their benchmark.

### Strengths
-- This is a well-motivated paper as far as I can tell. Robustness to adversarial attacks is clearly an important problem, to which architecture search is an important component. 

-- I find the paper to be sound in terms of discussions of related work. Throughout the paper there is clear references both to the adversarial defense literature and the NAS literature. They also provide clear arguments for the distinctiveness of their method compared to prior NAS benchmarks.

-- The experimental setup appears to be sound and the benchmarking extensive. I find the experiments on the empirical Lipschitz constant to be interesting and against the convention that increasing depth would increase the Lipschitz constant. I believe the authors should consider discussing this connection more, especially in relation to the learning theory literature (for example, the Lipschitz constant can be related to the Frobenius norm of the weight matrices, and in turn related to generalization).

-- The connections between adversarial robustness and the Lipschitz constant are not surprising, but is an important empirical finding especially since the paper studies it systematically for the given architecture family in terms of depth, width. Similarly their findings on depth-width ratio are informative and will be of interest to the NAS community.

### Weaknesses
-- The focus on WRN-style architectures, while it makes sense practically, may limit the generalizability of findings to other architectures. For example, aspects like width and depth and their relationship to adversarial robustness may differ across architectures. Vision transformers are a very popular architecture, for example, and one could imagine that they may behave differently. 

-- Similarly, the empirical evaluation is only on CIFAR-10. While I understand ImageNet can be expensive (especially for adversarial training), there are several other datasets that are of similar training time e.g. CIFAR-100, TinyImageNet. For this reason and the one above I'm not sure if the benchmark would "catch on".

### Questions
-- How do you plan to keep the benchmark relevant as new architectures emerge?

-- What is the roadmap towards new architectures and datasets? Will it be open to the community or do you expect to run them yourselves? Why would someone from the community contribute to it? For example, in typical benchmarks you expect researchers with competing methods to be incentivized to contribute. Who would be incentivized to contribute these kind of extensive NAS comparisons?

Basically I want to know why you expect this benchmark will catch on.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper presents NARes, a novel dataset of 15,625 unique neural network architectures based on Wide Residual Networks (WRNs), designed to assess adversarial robustness. The dataset includes detailed adversarial training statistics and evaluations against four adversarial attacks, including AutoAttack. The authors claim that NARes offers new insights into adversarial robustness and identifies contradictions in previous studies.

### Strengths
1. The initiative to create a comprehensive dataset for adversarial robustness is laudable.
2. The dataset's focus on a wide range of architectures is a valuable contribution to the field.

### Weaknesses
1. The paper lacks clarity in explaining key terms and abbreviations, which is detrimental to the readability and accessibility of the research, such as MACs, PGD^20, and PGD-CW^40.
2. The absence of the code and dataset at the time of submission limits the ability of the community to engage with and validate the work.
3. There is a lack of detailed experimental procedures, which is essential for the reproducibility of the findings.
4. The paper would benefit from a clearer structure to better guide the reader through the research and its implications.
5. The establishment of a leaderboard for benchmarking could significantly enhance the utility of the dataset, which is currently missing.

### Questions
See weakness.

### Soundness
3

### Presentation
2

### Contribution
2
