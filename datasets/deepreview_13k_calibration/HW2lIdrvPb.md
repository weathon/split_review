# Model Selection of Anomaly Detectors in the Absence of Labeled Validation Data

- Decision: Reject
- Avg Score: 5.67
- Scores: 6, 6, 5

## Abstract
Anomaly detection is the task of identifying abnormal samples in large unlabeled datasets. 
    While the advent of foundation models has produced powerful zero-shot anomaly detection methods, their deployment in practice is often hindered by the absence of labeled validation data---without it, their detection performance cannot be evaluated reliably.
    In this work, we propose SWSA (Selection With Synthetic Anomalies): a general-purpose framework to select image-based anomaly detectors without labeled validation data. Instead of collecting labeled validation data, we generate synthetic anomalies without any training or fine-tuning, using only a small support set of normal images. 
    Our synthetic anomalies are used to create detection tasks that compose a validation framework for model selection. 
    In an empirical study, we evaluate SWSA with three types of synthetic anomalies and on two selection tasks: model selection of image-based anomaly detectors and prompt selection for CLIP-based anomaly detection. 
    SWSA often selects models and prompts that match selections made with a ground-truth validation set, outperforming baseline selection strategies.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose to generate synthetic outlier data for outlier detection tasks. The method is based from mapping images into latents, then taking a mixture in latent space and mapping it back using a diffusion model.  
The evaluate the performance of one outlier detection method in multiple setups and 3 datasets. Furthermore they evaluate the suitability of the generated outliers for selecting prompts for the usage of CLIP as foundational model for zero-shot outlier detection.

### Strengths
They ask an important question, namely how reliable is synthetic outlier data for the evaluation of outlier detection setups.
The idea is clear and simple.

### Weaknesses
I think the question would need to be evaluated for more outlier detection methods, not just one distance based one.

Also the method to generate outliers is very simple. 
It is a simplified version of mixup in latent space. It offers no control over what kind of outliers are created. 
Calling it a style and content mixture is dubious, because the method seemingly has no attempted separation into content and style. it seemingly has only 1 latent space.
This would also benefit from a more thorough evaluation of creating outliers. e.g. stochastic mixup in latent space, or inpainting, and so on.

Also it is not clear to what extent the method learns to discriminate real image properties from synthetic ones - this is because the real images are never run through the encoding-decoding step.

This conclusion is not true:
In an extensive empirical study, ranging from natural images to industrial applications, we find that our synthetic validation framework selects the same models and hyper-parameters as selection with a ground-truth validation set.

yes in the simple class vs other classes on flowers and birds it holds, on the more realistic MVTec it does not hold, see their appendix.

It is not bad per se, if the proposed method does not work, but putting a questionable conclusion in the abstract is misleading.

The zero-shot task result is interesting scientifically. Practically it is unlikely that one would use that for serious outlier detection tasks.

### Questions
What are the five repetitions in Figure 3? Can they be compared against each other ?

How would the outlier detection perform for reconstruction based AD methods ? or maybe another class ?

Can experiments be run to ascertain the usefulness for smaller defects beyond MVTec ? What if the outliers are not on semantic level but more on imaging setting differences ?

Can an experiment be performed to understand to what extent the method classifies real vs diffusion generated images ?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In the paper "Model Selection of Anomaly Detectors in the Absence of Labeled Validation Data" the authors consider the task of anomaly detection in a semi-supervised setting where only normal data is given for training. For selecting a suitable anomaly detector, the authors propose to augment the validation data by anomalous data points that are created with the help of diffusion models. In their empirical study, the authors find the synthetically created anomalies to give rise to a good choice of anomaly detectors.

### Strengths
- Novel method and intriguing idea to create synthetic anomalies for images as an input.
- Strong empirical performance of the proposed method
- Thorough evaluation of the method and good set of baselines.
- The related literature is nicely reviewed and the overall presentation is excellent.

### Weaknesses
 - The authors could elaborate more on the limitations of the approach. For instance, one problem I see is that the synthetically generated anomalies do not necessarily resemble the ground truth distribution of anomalies. In particular, the question for the image classification datasets is indeed what would an actual anomaly look like? In particular, to me, it is questionable whether the generated images make sense at all as the observations would probably never be made in the real world. The method's reliance on diffusion models also introduces potential biases, as these models are trained on specific datasets and may not generalize well to all types of anomalies. Furthermore, the diversity of generated anomalies is not guaranteed, potentially leading to a narrow evaluation of anomaly detectors. It is also unclear how the method would perform when the normal data distribution is complex or multimodal, as the diffusion model might struggle to generate meaningful anomalies in such cases.
- Figure 3 needs more explanation what exactly is plotted. The legend is of the figure is also off, e.g., in Figure 3(a) there are squares which are not contained in the legend.

### Questions
- How are anomalies even defined in the image domain? Is it just out of distribution data? Unrealistic images? If the latter, why would one even expect to observe such images?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
To address the problem of sparse annotated data in existing detection tasks, the paper designed a framework that uses Diffusion Model interpolation to generate abnormal data, and then uses the synthesized data to perform model selection for anomaly detection. The paper conducted extensive experiments on both natural image data and industrial image data, demonstrating the effectiveness of this framework.

### Strengths
+ To address the problem of sparse annotated samples, the paper uses interpolation with Diffusion Model to transform normal images into abnormal images with certain semantic information, thus simulating some abnormal data well.
+ The paper validated the effectiveness of synthesized data through extensive experiments on different datasets and models.
+ The paper validated the effectiveness of synthesized data in selecting prompts for zero-shot detection using CLIP.

### Weaknesses
 + Although the paper's method has significant effects on the Flowers and CUB datasets, it does not perform well on the MVTec AD dataset. From Tables 1 and 2, it can be seen that the synthesized data is not helpful for the MVTec dataset. From Figure 2, it can also be seen that the interpolation synthesis has poor performance. For the CUB dataset, the anomalies are more significant, so the synthesized data is effective, but for the MVTec dataset, the anomalies are more subtle, so the synthesized data is not effective.
+ The paper's abnormal synthesis function is entirely based on DiffStyle, and it remains to be verified whether the method of interpolating abnormal images from different normal images is reasonable. Perhaps perturbing features in different dimensions in the latent space may have better results. The paper should consider different designs for high-level semantic anomalies and low-level semantic anomalies in this regard.

### Questions
+ It is unclear what considerations the authors had in comparing the Flowers, CUB, and MVTec datasets. There are significant differences between these datasets.
+ The paper's workload is significant, but the experimental character is too strong, and it is unclear whether the authors have any ideas for redesigning the Diffusion generation process based on the experimental results.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
