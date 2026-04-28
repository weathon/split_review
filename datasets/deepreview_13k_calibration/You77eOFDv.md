# RefConv: Re-parameterized Refocusing Convolution for Powerful ConvNets

- Decision: Reject
- Avg Score: 6.00
- Scores: 5, 5, 8

## Abstract
We propose Re-parameterized Refocusing Convolution (RefConv) as a replacement for regular convolutional layers, which is a plug-and-play module to improve the performance without any inference costs. Specifically, given a pre-trained model, RefConv applies a trainable Refocusing Transformation to the basis kernels inherited from the pre-trained model to establish connections among the parameters. For example, a depth-wise RefConv can relate the parameters of a specific channel of convolution kernel to the parameters of the other kernel, i.e., make them refocus on the other parts of the model they have never attended to, rather than focus on the input features only. From another perspective, RefConv augments the priors of existing model structures by utilizing the representations encoded in the pre-trained parameters as the priors and refocusing on them to learn novel representations, thus further enhancing the representational capacity of the pre-trained model. 
Experimental results validated that RefConv can improve multiple CNN-based models by a clear margin on image classification (up to 1.47\% higher top-1 accuracy on ImageNet), object detection and semantic segmentation without introducing any extra inference costs or altering the original model structure. 
Further studies demonstrated that RefConv can reduce the redundancy of channels and smooth the loss landscape, which explains its effectiveness.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
In this paper, the authors propose a technique called Re-parameterized Refocusing Convolution, which is based on the idea of structural re-parameterization, i.e., incorporating more learnable parameters into the model during training and training them for better performance. These parameters are merged into the original model's parameters during inference to achieve the goal of not introducing additional inference costs.

### Strengths
The approach in this paper can be viewed as "convolution B of convolution A", where A is the convolution parameter trained by the pre-training process and kept frozen once trained.B is the convolution parameter that continues to be trained.

The method in this paper has a slight advantage over several other structural reparameterization and weight reparameterization methods in terms of results.

I think the conclusion of the final analysis, "Re-parameterized refocusing reduces redundancy between channels", demonstrates well the changes that the methods in this paper can make to a pre-trained convolutional model.

The experiments included a variety of convolutional models.

### Weaknesses
Observe that the ImageNet experimental results have about 1% performance improvement on many models, but also a lot more Params.

The network architectures that come into play are generally early CNN models such as ResNet, DenseNet, MobileNet family, etc. For modern convolutional architectures such as SlaK, RepLKNet, HorNet, etc., the effect is currently unknown.

### Questions
1	The refocusing technique seems to be one that can be iterated. Can the refocusing technique in this paper continue to be iterative? I.e., after doing one refocusing exercise, then the next one. Will the results continue to improve?

2	For the base weight W_b, one of the points claimed by the refocusing technique is the possibility of establishing links between its individual channels. Why is this necessary? Each channel of the base weight kernel has its own role, so to link them?

3	During refocus training, the result after convolution of the base weight W_b with its previous features can be seen as a new "feature". The transform weight W_t can be seen as trainable to process this new "feature". This process is equivalent to fine-tuning the convolution after "injecting" new parameters. I would like to ask if any experiments with other models (e.g. new convolutional networks) have found that this degrades performance?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper introduces a novel approach to neural network training, specifically by bifurcating the weight training process into two distinct stages. However, I believe the validation of the method's effectiveness is not adequately comprehensive. Given the current state of the paper, my recommendation would be to not accept it in its present form.

### Strengths
The concept presented in the paper captures the interest.


Figure 1 is exceptionally clear and effectively conveys the central concept of the method proposed in the paper.


Because the parameters are seamlessly integrated, the proposed method does not incur additional costs during the inference phase.


The paper employs techniques such as visualization to offer numerous valuable insights.

### Weaknesses
The proposed method incurs a higher training cost compared to the original approach. My concern does not lie with the cost itself; rather, I am questioning the accuracy and reliability of the validation process employed.

The authors believe that their method can indirectly connect information from different channels of the input, which is clearly a mistake. Let x = [x1, x2, ..., xc]; y = [y1, y2, ..., yc]. It is obvious that y1 does not contain the content from x2 to xc. If there is any, please prove it using the notation I provided.


I am quite familiar with ImageNet, and I have concerns about the data presented in Table 1. I would like the authors to refer to the data from timm. The authors might argue that their values are lower than the standard libraries in timm because they only trained for 100 epochs, but I consider this a drawback. If the standard training procedure from timm was used, perhaps the authors' method would not show any gain. It is conceivable that the authors' method is essentially equivalent to providing more extensive training to an originally under-trained model, albeit with a longer training time. If a model is adequately and standardly trained, the authors' method should be unnecessary.


In the first experiment of Section 4.4, the authors should train all models to full convergence (for instance, more than 500 epochs) before making comparisons. Stepping back, when the authors retrain this model, do they use twice the training epochs?


The second experiment in Section 4.4 is incorrect. The authors should not simply use a small learning rate to fine-tune; instead, they should follow timm’s practice of training from scratch for 500 epochs until convergence.

### Questions
See #Weakness.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposed a novel re-parameterization method named Re-parameterized Refocusing, which can establish connections across the channels of the learned conv kernel.
Experiments show that the proposed method can improve the performance of many convnets in various tasks, such as image classification and segmentation, without introducing any computation cost in inference phase.

### Strengths
1. The proposed method is novel and effective.
2. The experiments are solid.

### Weaknesses
None

### Questions
None

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good
