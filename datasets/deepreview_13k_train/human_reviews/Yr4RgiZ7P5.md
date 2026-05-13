# Does resistance to style-transfer equal Shape Bias? Evaluating shape bias by distorted shape

- Decision: Reject
- Scores: 6, 3, 6, 6

## Abstract
Deep learning models are known to exhibit a strong texture bias, while human tends to rely heavily on global shape for object recognition.  The current benchmark for evaluating a model's shape bias is a set of style-transferred images with the assumption that resistance to the attack of style transfer is related to the development of shape sensitivity in the model. In this work, we show that networks trained with style-transfer images indeed learn to ignore style, but its shape bias arises primarily from local shapes. We provide a $\textbf{Distorted Shape Testbench(DiST)}$ as an alternative measurement of global shape sensitivity. Our test includes 2400 original images from ImageNet-1K, each of which is accompanied by two images with the global shapes of the original image distorted while preserving its texture via the texture synthesis program. We found that (1) models that performed well on the previous shape bias evaluation do not fare well in the proposed DiST; (2)  the widely adopted ViT models do not show significant advantages over Convolutional Neural Networks (CNNs) on this benchmark despite that ViTs rank higher on the previous shape bias tests. (3) training with DiST images bridges the significant gap between human and existing  SOTA models' performance while preserving the model's accuracy on standard image classification tasks; training with DiST images and style-transferred images are complementary, and can be combined to train network together to enhance both the global and local shape sensitivity of the network. Our code will be host in the anonymous github: \url{https://anonymous.4open.science/r/ICLR2024-DiST/}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a new benchmark to measure how well models can handle distorted shapes. They show that removing texture alone is not sufficient to make models robust to shape distortions. They also suggest that combining their method with Stylized Aug training can improve the models’ robustness to both style and shape variations.

### Strengths
This paper is clear and well-structured. The authors share their code, which facilitates the replication of the experiments. The benchmark they propose is original, as it focuses on shape distortions rather than style variations. They also provide a human baseline for comparison.

### Weaknesses
I have some doubts about the need for models to be robust to shape distortions. The examples in Fig. 2(a) seem very challenging even for humans. Are there any real-world applications that require such ability? The distorted shapes do not seem to have any physical meaning.

And what is the benefit of using global shape features if the model can already classify the image based on local shape features?

I also noticed that DiSTinguish itself worsens the performance on SIN-1K, as shown in Table 3. Can you explain why this happens?

### Questions
Please check weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper is centralled concerned with robustness of recognition to shape distortion. The question asked in "does resistance to style transfer equal shape bias?" By which the authors seem to mean that recogntion algorithms that have been extended to be decently robust to texture change in objects are not robust to shape changes.

The paper introduces a data set dseigned for the problem, and a distance they call DiST.

### Strengths
I like the odd-one-out test, which I think is a sound way to measure subjective distances.

### Weaknesses
It is clear from simple observation that texture and shape can both change, and that neural nets are currently configured to rely primarily on texture. So the paper is not saying too much in that regard.

The dataset introduced comprises an unconvincing collection of images. These include images that have been assumbled from sub-images of the object at different scales and points of view, peeled fruit (and peeled footballs). The reason this is not convncing is that the shape changes within a class will rarely if ever be expressed in such a way. Far more common would be simple geometric distortions. As an example, a "man" could be distorted into a "strong man" by increasing body and muscle size compared to the head. A second reason is that in some cases at least shapes can change in very unexpected ways but still be reognisable. Dali's melting watches are an example.

The fact that current models do not perform so well on the new dataset is not surprising. It is not so hard to contruct such a dataset. And the conclusion that humans out perform machines is equally unsurprising.

### Questions
Why not use some kind of warping to resist changes in shape? (Inter-class warps should be distinct from intra-class warps).

What is your justification for using images made of pieces of photos of an object? (These are not shape distorted, they are mosaics of regualarly shaped parts)

People can draw things - say a face - in all sorts of shapes. Eyes can be round, lines, crosses, diamonds and many more shapes.
Why not include such examples in your dataset (these examples are real and common in art)

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper propose a benchmark dataset, DiST, to measure the global shape sensitivity of models. The images in this dataset is constructed by applying global shape distortion to natural images. Specifically, it follows Gatys et al. (2015), but optimize the intermediate layers' feature but keep the gram matrix not changes. Therefore, the texture information is kept but the shape information lost. Based on this newly constructed dataset, this paper have several interesting observations.

### Strengths
This paper is studying an interesting problem, and figured out the missing pieces from the previous studies.

The proposed image construction methods simple but makes sense.

The experimental results further illustrate the value of the proposed dataset.

### Weaknesses
The scale of this dataset is too small (less than 10k images IIUC). It would be good to use the proposed method to construct an ImageNet-level dataset.

It would be good to show some well generated images while show some bad images as well, which can help people better understand the pros and cons of the proposed method.

It would be good to benchmark more models. For example, the shape-biased and the texture-biased model from [a].

### Questions
See weakness. My main concern is the scale of the dataset on both number of images and number of tested models. This paper is very interesting, but potential can explore more.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
For visual recognition, human rely more on shape while Neural Network rely more on textures, and previous methods trained style transfer augmentation failed to extract global shape information. This paper propose Distorted Shape Testbench as a measurement for global shape sensitivity, and a corresponding training method to improve Visual recognition networks' ability to extract global shape. Qualitative and quantitative experiments have been conducted to show the method's superiority.

### Strengths
1. The choice of research topic is insightful, both interesting and practical. 
2. The proposed method and benchmark are likely to be helpful helpful to many relevant research fields.
3. The results are promising and the experiments are convincing

### Weaknesses
1. In the experiment section, the authors only compared Resnet and ViT, the limited number of network architectures may make the conclusion less persuasive
2. The proposed DiST benchmark is only tested on classification task, while there are many tasks influenced by global shape information. Experiments on different tasks may be needed to show the Versatility of DiST.

### Questions
1. The proposed ways of generating shape distortion is based on Neural Style Transfer, does the specific ways of style transfer algorithm used matter? Or could other style transfer/shape distortion methods achieve the same performance?
2. The distorted images have similar textures but different global shape with the originally images. Would contrastive learning help improve the performance in this situation>

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
