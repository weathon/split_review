# LAION-C: An out-of-distribution benchmark for web-scale vision models

- Decision: Reject
- Scores: 5, 5, 5, 6

## Abstract
Out-of-distribution (OOD) robustness is a desired property of computer vision models. Improving model robustness requires high-quality signals from robustness benchmarks to quantify progress. While various benchmark datasets such as ImageNet-C were proposed in the ImageNet era, most ImageNet-C corruption types are no longer OOD relative to today's large datasets scraped from the web, which already contain common corruptions such as blur or JPEG compression artifacts. Consequently, these standard benchmarks are no longer well-suited for evaluating OOD robustness in the era of web-scale datasets. Indeed, recent models show saturating scores on ImageNet-era OOD benchmarks, indicating that it is unclear whether models trained on web-scale datasets truly become better at OOD generalization or whether they have simply been exposed to the test distortions during training. To address this, we here introduce LAION-C as a benchmark alternative for ImageNet-C. LAION-C consists of six novel distortion types across five severity levels designed to be OOD, even for web-scale datasets such as LAION. In a comprehensive evaluation of state-of-the-art models, we find that the LAION-C dataset poses significant challenges to contemporary models. We additionally conducted a psychophysical experiment to evaluate the difficulty of our proposed corruptions for human observers, enabling a comparison of models to lab-quality human robustness data. We observe a paradigm shift in OOD generalization: from humans outperforming models to the best models now matching or outperforming the best human observers.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
During the ImageNet era, researchers developed numerous benchmarks to test how vision models perform on out-of-distribution data, with ImageNet-C emerging as one of the most widely used benchmakrs. ImageNet-C featured four types of corruptions: noise, blur, weather, and digital effects. However, the paper points out a key limitation: these corruptions are commonly found in web-scale training data, which makes them less effective for measuring true out-of-distribution robustness for web-scale models. To address this shortcoming, they've developed a new benchmark called LAION-C. This benchmark introduces six new, manually designed corruption types: Mosaic, Glitched, Vertical Lines, Stickers, Geometric Shapes, and Checkerboard patterns.

### Strengths
When it comes to benchmarking robust image classification, this paper presents a comprehensive and thorough set of experiments. The addition of psychophysics experiments is also valuable.

### Weaknesses
 - Why is there no evaluation of Vision-Language models?
- The paper, as it currently stands, doesn't adequately justify why we need another robustness benchmark for image classification, especially since it reaches similar conclusions to [1]. While the paper claims their benchmark is more challenging than ImageNet-C, this alone isn't particularly compelling. During the ImageNet era, ImageNet-C served as a good benchmark for testing out-of-distribution performance. However, now that we're in the age of Vision-Language foundation models, shouldn't we be going beyond simple image classification? Shouldn't we also be testing these models' ability to reason and explain their classification decisions for out-of-distribution samples?


### Questions
- What was your reasoning for selecting these 6 specific types of corruption?
- Some of the corruption levels, particularly at intensities 4 and 5, seem extremely severe. Looking at Figure 2, even a human would struggle to identify the images with Mosaic at intensities 4 and 5, Stickers at 3, 4, and 5, and Geometric Shapes at 3, 4, and 5. What's the rationale for including these extremely challenging cases? What meaningful insights can we gain from seeing models perform poorly on images that are essentially unrecognizable? If even humans can't identify these images, what value does testing models on them provide?

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
In this era of web scale vision models where distortion from ImageNet-C could be part of their training data, the improvements on ImageNet-C is not strongly correlated to model robustness. This paper proposes a new corruption benchmark to evaluate model’s robustness against distribution shifts. Authors carefully craft six synthetic new corruptions with five different severity levels that are visually different from ImageNet-C and real world data distribution. Authors evaluate different variety of models and also examine human performance on this benchmark. Results suggest that models struggle to perform on this benchmark when compared to ImageNet-C.

### Strengths
+ Presentation of problem formulation is clear. Figure 1 provide qualitative evidence that distortions of ImageNet-C are part of training data LAION 400M.

+ The proposed distortions are disjoint from ImageNet-C.

+ A wide range of vision models are evaluated against this benchmark to show its effectiveness.

+ Highly appreciate the experiments with human subjects to ensure comparability.

### Weaknesses
It is not clear on how to realize that improvement on the proposed distortions would translate to the improved generalization of the model. How do we know that these distortions would act as proxy to determine model generalization? Does improving on these distortions imply improving model performance on diverse unseen real world distribution shifts? To address this issue, it is important to establish that LAION-C correlates with generalization to real-world distribution shifts. Authors can evaluate different model performances on existing real-world OOD datasets and analyze their correlation with LAION-C performance.

As acknowledged by the authors, certain distortions disrupt the object features beyond visual recognition even at severity level 3 (e.g. Stickers and Geometric Shapes). It is not clear how the parameters for these severity levels are chosen. As some of the distortions mainly occlude the object of interest in the image, a ratio of occlusion of the object under these distortions would be helpful to understand the severity level. Besides, it would be informative to provide quantitative metrics of each severity level across all distortion types. For example, what is the average area of the geometric shapes at each severity level, or the average number of stickers and their sizes?

The argument that LAION-C is challenging but solved by finetuning is not convincing as the model improvements on the extreme severities could have been the result from learning spurious or shortcut features, and does not correspond to learning object features. Authors could examine this behaviour by analyzing model's attention patterns before and after fine-tuning, and test the fine-tuned model on other OOD datasets to assess genuine robustness improvements. Simply showing that fine-tuning improves performance on the corrupted dataset doesn't demonstrate that the model is learning robust features.

A prior work [a] introduced an alternative to ImageNet-C dataset called ImageNet-C-bar with distortions dissimilar to different augmentations used in the training, would these distortions eligible to become part of LAION-C?

### Questions
Please refer weakness section.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
LAION-C is a new benchmark dataset designed to evaluate the out-of-distribution (OOD) robustness of modern vision models trained on web-scale datasets. ​It includes six distortion types across five severity levels, intended to be OOD even for large datasets like LAION. ​
The paper argues that ImageNet-C is no longer effective for evaluating the robustness of models because many common corruptions in ImageNet-C, such as blur and JPEG compression artefacts, are already present in web-scale datasets. ​It includes a thorough evaluation of nearly 60 models as well as a comparison to human annotators.

### Strengths
Comprehensive Evaluation: The paper thoroughly evaluates 58 vision models on the LAION-C dataset, comparing their performance to human observers. This evaluation highlights the challenges posed by LAION-C and the variability in model robustness. ​

Human evaluation: The most insightful outcomes in the paper stem from the comparison to humans, which was done in a controlled setting. This is valuable as it allows good insights into the commonalities and differences between the algorithms and human perception.

### Weaknesses
## Performance Correlation with ImageNet-C
The paper motivates LAION-C mainly in comparison with ImageNet-C. As a pure OOD benchmark, it is unclear which advantage the new benchmark brings other than being harder and less saturated. Looking at Figure 3, there is an almost perfect alignment between ImageNet-C and LAION-C performance: models that perform better on ImageNet-C also perform better on LAION-C with only minimal changes between very similarly performing models. With this, the question is if the same study could have been performed using ImageNet-C instead?

## Nature of the distribution shifts
The paper proposes six new synthetic distortions. The motivation behind synthetic distortions is two-fold: on the one hand, they are easy to apply at a large scale. On the other hand, they are less likely to be contained in web-scale datasets. The experiments show what is intuitively clear: this data is further away from the training distribution of large models than ImageNet-C. The question, however, is whether these distribution shifts are _useful_.
Potentially useful shifts come in two types, which I will call A and B: 
* Type-A is the most straightforward: actual real-world distribution shifts that allow understanding of the model’s performance on in-the-wild data. 
* Type-B shifts are synthetic and might not appear in the real world, but they can be motivated by human/animal visual systems being robust in response to these changes. This allows for studying the differences between biological and artificial perception.

The shifts presented here are not of type A. It is difficult to imagine many real-world scenarios resulting in the proposed image corruption. They are also not of type B: for example, Figure 5 shows that humans are not very good at understanding these corruptions. 
What does the proposed OOD dataset tell us about the benchmarked models? It is not real-world performance, and it is also not how aligned they are with biological perception. What remains is the insight that the proposed distortions affect humans more than the models, which is somewhat interesting but not particularly useful.

### Questions
> 19 human subjects are briefly presented with a distorted image and are asked to classify it into one of 16 classes, reminiscent of how a DNN might be evaluated on a classification task.

How is this process reminiscent of the forward pass in a network? As a field, we are responsible for not overclaiming the “intelligence” or the relatedness of models to biological intelligence.

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
3

### Summary
This paper introduces LAION-C, a new out-of-distribution (OOD) dataset specifically designed for models trained on web-scale data, which can sometimes overlap with benchmarks like ImageNet-C. To mitigate this issue, the authors generated a dataset containing six types of image distortions, each across five severity levels. Experiments demonstrate the challenging OOD properties of LAION-C for existing models. Furthermore, the authors conducted psychophysical experiments to assess prediction consistency between human observers and models, revealing that current models can now match or even surpass the performance of the best human observers.

### Strengths
1. Clear structure and presentation: The paper is well-organized, with a logical structure and smooth flow that improves readability and comprehension.
2. Insightful motivation for OOD benchmarking: This dataset addresses the critical issue of data leakage in current benchmarks. This approach highlights the limitations of evaluating current models trained on web-scale data.
3. Interesting distortion design: The authors designed six distinct distortion types that minimize overlap with common real-world corruptions, reducing the likelihood of data leakage. This approach improves the dataset’s utility as a truly challenging OOD benchmark.

### Weaknesses
1. Limited novel insights in model ranking comparisons: Figure 4 shows minimal divergence in the ranking of model performance between ImageNet-C and LAION-C. Similarly, Figure 3 demonstrates a strong linear correlation between model performance on ImageNet-C and LAION-C. Since a benchmark dataset's purpose is to reveal different performance characteristics across models, more analysis is needed to clarify the unique insights LAION-C provides beyond what ImageNet-C already offers. The high correlation suggests that LAION-C may not be exposing fundamentally different failure modes in models compared to ImageNet-C. This raises questions about the necessity of introducing a new benchmark if it does not offer significantly different insights into model robustness.

2. Class disparity between datasets: ImageNet-C includes 1,000 classes, whereas LAION-C has only 16, potentially creating an imbalance in comparison. This difference in the number of classes could lead to skewed results, especially when comparing absolute performance metrics. The reduced number of classes in LAION-C might make it easier for models to achieve higher accuracy simply due to the smaller search space, rather than due to genuine robustness to the introduced distortions. This makes direct comparisons of absolute performance between the two datasets problematic, outside of the psychophysical experiments.

### Questions
1. Performance differences between CNNs and transformers: Given that LAION-C primarily features patch-based transformations, are there observed differences in how CNNs and transformers perform on these types of distortions?

2. Class disparity between datasets: ImageNet-C includes 1,000 classes, whereas LAION-C has only 16, potentially creating an imbalance in comparison. Excluding the psychophysical experiments, what methods or adjustments could be employed to address this disparity and ensure a fair evaluation between the datasets?

### Soundness
3

### Presentation
3

### Contribution
4
