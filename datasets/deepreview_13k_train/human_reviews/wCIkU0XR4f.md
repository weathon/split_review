# How Does Data Diversity Shape The Weight Landscape of Neural Networks?

- Decision: Reject
- Scores: 3, 3, 5, 6

## Abstract
To enhance the generalization of machine learning models to unseen data, techniques such as dropout, weight decay ($L_2$ regularization), and noise augmentation are commonly employed. While regularization methods (i.e., dropout and weight decay) are geared toward adjusting model parameters to prevent overfitting, data augmentation increases the diversity of the input training set, a method purported to improve accuracy and calibration error. In this paper, we investigate the impact of each of these techniques on the parameter space of neural networks, with the goal of understanding how they alter the weight landscape in transfer learning scenarios. To accomplish this, we employ Random Matrix Theory to analyze the eigenvalue distributions of pre-trained models, fine-tuned using these techniques but using different levels of data diversity, for the same downstream tasks. We observe that diverse data influences the weight landscape in a similar fashion as dropout. Additionally, we compare commonly used data augmentation methods with synthetic data created by generative models. We conclude that synthetic data can bring more diversity into real input data, resulting in a better performance on out-of-distribution test instances.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This submission examines how data diversity shapes the weight landscape of neural networks. To investigate this, the study explores how techniques such as dataset augmentation and regularization methods impact the parameter space of neural networks, focusing on transfer learning scenarios. Random Matrix Theory is applied to analyze the eigenvalue distributions of pre-trained models, fine-tuned using these techniques with varying levels of data diversity for the same downstream tasks. The main observation is that diverse data influences the weight landscape in a similar way to dropout. Additionally, synthetic data created by generative models can increase diversity and improve out-of-distribution generalization.

### Strengths
+ Studying the impact of data augmentation on the landscape of weight parameters is interesting, and the use of Random Matrix Theory is straightforward.
+ The observation that “dropout and data augmentation exhibit similarities in how they affect the weight space of neural networks” is also intriguing. This observation seems expected and reasonable.

+ The final disucssion part is good. Serveral good points are made in disucussing the impact of regularization methods and data augmentation

### Weaknesses
 - **The main concern is that the analysis methodology is not convincing**. This submission states, “since the heavy-tailed nature of pre-trained models… we focus on the trend of how regularization and diverse data influence the weight spectrum.” This statement is unclear. The weight differences observed are between a pre-trained model and a fine-tuned model, which are expected to be naturally different due to the use of different training data and objectives. It’s unclear why this difference is a valid measure of the effect of each technique. Specifically, the paper does not adequately explain why comparing the weight differences (ΔM) between a pre-trained and fine-tuned model, across different fine-tuning methods, provides a meaningful measure of the effect of each technique. The claim that techniques falling in the same quadrant of the visualization analysis have the same effect on the weight space is not sufficiently justified. The paper needs to clarify how this quadrant analysis isolates the effect of each technique from the inherent differences between pre-trained and fine-tuned models. 

Second, the Vendi Score (VS) is used to measure the intensity of diversity, which is acceptable. However, using different spaces—specifically, the raw pixel space versus the feature space—yields different observations, as shown in Figure 1. How should this difference be interpreted? The paper states that VS was not used to measure diversity in the feature space, but it was used to evaluate the diversity introduced by various data augmentation and synthetic data methods. This distinction is not clear in the paper. The paper needs to clarify how the VS score is calculated in both pixel and feature space and why these two measures are not directly comparable. Additionally, why is CLIP used instead of Inception? Also, the definition of VS(K) is unclear. What does K represent?

- **The analysis lacks clarity.** The ESD is used to illustrate the effect of each technique in Figure 3, but what is the main point? It’s challenging to draw clear observations from this figure. The paper needs to provide more specific explanations of what features of the ESD are being analyzed and how they relate to the effects of different techniques. For example, are they looking at the spread, the tail, or some other property of the distribution? Figure 4 raises the same question. Additionally, what is the purpose of reporting Table 2, which merely lists numbers without providing a clear takeaway? The paper needs to explain what these numbers represent and how they support the claims being made. Moreover, The order of classes in Figure1 will have impact, but this submission does not consider this. The paper needs to demonstrate that the class order does not affect the conclusions drawn from the Vendi Score analysis.

### Questions
Please clarify and improve the analysis methodology. Additionally, the results lack clarity and do not consistently demonstrate a clear observation. While the discussion section is interesting, the analysis does not effectively support the main points.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The submission makes use of perspectives about how spectral analysis of weight matrices in neural networks relate to its regularization properties developed in “Traditional and heavy-tailed self regularization in neural network models”, Martin and Mahoney, 2019.  The key assumption is that similar deviations in the eigenspectrum from that predicted by random matrix theory signify equivalent generalization properties.

Under this assumption, the submission explores the spectral effect data diversity has on the weight matrices of a transformer-based neural network being fine-tuned with different levels and varieties of data diversity, relating the changes to those induced by traditional regularization techniques such as dropout and weight decay. 

Experiments are performed by fine-tuning a CLIP vision encoder on CIFAR 10 and 100. Results suggest that data augmentations and some amount of synthetic data inclusion have similar effects on the empirical eigenspectrum as dropout while differing in some aspects from weight decay.

### Strengths
Originality: While the method for analysis is borrowed, the particular application in the context of comparing data augmentation approaches with other regularizers is new, to my knowledge. 

Clarity: The submission is easy to read, and the presentation is well-organized. 

Quality and significance: The analysis is intriguing, and suggestive of further explorations.

### Weaknesses
The submission’s goal of using mathematical tools to inspect similarities between data augmentations and model-parameter based regularization strategies is intriguing. However, this goal is not adequately explored for the results to be considered informative enough to be interesting or actionable. Only one base model is used, and the choice of two small-scale image datasets is somewhat narrow. The analysis would benefit from exploring a wider range of model architectures and datasets to establish the generality of the observed spectral patterns. For instance, the behavior of convolutional layers in ResNet architectures could be compared to the transformer layers in the CLIP model. Furthermore, the datasets used, CIFAR-10 and CIFAR-100, are relatively small and might not fully capture the complexities of real-world data distributions, limiting the conclusions that can be drawn about the effectiveness of data augmentation techniques in more realistic scenarios. 

The synthetic data experiments seem a little out of place, it was not clear to me why they fit in this paper, and what the connection is to the analytic method that seemed to be the central focus of the submission. In my opinion, these two aspects can be separate drafts, with considerably more thorough experimentation in order to make compelling cases for both. The paper does not clearly articulate how the spectral analysis of the weight matrices directly relates to the synthetic data generation process. The connection between the observed spectral changes and the specific characteristics of the synthetic data (e.g., diversity, realism) is not well-established, making it difficult to interpret the results in a meaningful way. The inclusion of synthetic data feels disconnected from the core analysis of weight matrix spectra and regularization.

Some typos:

L203: “Since the…” —> “Due to the…”?

L210-211: “properties of the spectral” —> “properties of the spectrum” or “spectral properties of the weight matrices”?

### Questions
1. Is CIFAR a good choice for fine-tuning experiments on a pre-trained CLIP B/32 model? Aren’t these models typically trained on higher resolution images?

2. L151 says that “We also observe that pixel-wise diversity scores do not always match embedding-wise scores after applying data augmentation.” Is the base model trained with some of these data augmentations already, thus learning to be invariant to them?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper explores the effects of various regularization and augmentation techniques on the parameter space of neural networks, with a particular focus on the weight landscape in transfer learning contexts. Specifically, it employs Random Matrix Theory to examine the distribution of eigenvalues between pretrained and finetuned models that utilize these techniques. Additionally, the paper conducts comparative experiments across diverse datasets to further investigate these effects.

### Strengths
This paper leverages Random Matrix Theory to analyze the impact of augmentation and regularization techniques, providing a valuable perspective for examining more complex methods.
The paper puts forward several arguments, notably that diverse data can enhance model performance.
The study includes multiple experiments designed to investigate the effects of various regularization and augmentation strategies.

### Weaknesses
While this paper effectively explores the impact of various regularization techniques and provides some explanations, it primarily resembles an experimental report. I am curious whether the findings from these experiments could be utilized to optimize the application of regularization or data augmentation techniques.
Moreover, the focus of the paper is predominantly on experimental validation, and the use of mainly the CIFAR dataset might not be sufficiently representative. It would be beneficial to include additional datasets to strengthen the validity of the results.
Regarding the explanations provided for the findings, could the authors offer some theoretical analysis to elucidate why these phenomena occur? This would enhance the depth of the paper and provide a stronger theoretical foundation for the observed effects.

### Questions
Please refer to weakness

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper provides a new insight into data diversity shape and its relationship with the weight landscape of neural networks. Furthermore, it investigates how data diversity can influence the weight matrices of neural networks. It focuses on comparing the impact of traditional regularization (dropout, weight decay) and data augmentation on neural networks. The authors used the Vendi Score, which measures the diversity in datasets, to quantify how diverse datasets, including synthetic data from generative models, affect model generalization. It finds that synthetic data can enhance model performance when combined with real data but can also cause model collapse when overused.

### Strengths
In general, the topic is interesting, and the paper is well-written. It provides good insights into the impact of diversity and synthetic data for better generalization with respect to the neural network landscape. Furthermore, the diversity per class for different augmentation strategies is motivating.

### Weaknesses
The work seems good, but it lacks more baselines and more motivation about its importance. Data diversity and generalization is a hot topic, as we can see in new works such as Hemmat, Reyhane Askari, et al. "Improving Geo-diversity of Generated Images with Contextualized Vendi Score Guidance." arXiv preprint arXiv:2406.04551 (2024). So, having a deep analysis of it is important. Furthermore, the work says that synthetic data can hurt the generalization data, but I didn't see any in-depth analysis of it, such as a graphic describing the amount of synthetic data vs. performance or diversity of the final model.

1 - For instance, the title of the work is "How does data diversity shape the weight landscape of neural networks?" but the experiments are done only with the CLIP VIT model; if possible, it would be good to have additional experiments with other models/backbone and also another dataset such as ImageNet (if not possible due to hardware constraints, consider using subsets of it such as imagenette), this would make the work more robust and grounded in better-evaluating settings.

2 - Figure 1 only brings cifar10, but this analysis is nice to have for other datasets as well (if not on the main paper, you can add it to the supplementary material).

3 - There is no visualization of the loss landscape; I think this is an important opportunity to show the behavior of data augmentation or synthetic data in the loss landscape.

4 - Other baselines such as Fine-tuning with Very Large Dropout (Zhang, Jianyu, and Léon Bottou), Dropout+Weight Decay (a combination of the two baselines of Fig. 3) would be interesting to have.

### Questions
For me the authors can work on the Weaknesses list described. I think the work has its merits, but the authors need to address some of the points mentioned in the Weaknesses section.

Some important points for the authors: 

1. Does the pre-train zero-shot model affect the diversity or data augmentation used? Or can the landscape change if you start from a model from scratch? This can be a good analysis with a small model such as resnet18 or resnet34 (I am not saying to test it with CLIP, but this could be an interesting point). Additionally, why only choose CLIP VIT specifically, and do you believe that your findings would generalize to other architectures? How the pre-training model could interact with data diversity effects, and do you expect different results for models trained from scratch versus fine-tuned models.

2. Do you think that loss landscape visualization would complement your current analysis?

3. "Therefore, a careful balance between real and synthetic data is still necessary to prevent model collapse and prevent overfitting." Could we use a diversity metric inside the training to guide the augmentation needed or even to balance the amount of synthetic vs. real data? If so, do you think that the model would collapse or overfit the synthetic data? Discuss the potential challenges and benefits of incorporating a diversity metric into the training process,

The above questions can be used to improve some insights and analysis of the work. Furthermore, I didn't see anything about open-source code or reproducibility, which can be important for the scientific community. 

I am happy to see the rebuttal phase and hope that the authors can do a good job of improving the points mentioned.

### Soundness
3

### Presentation
3

### Contribution
3
