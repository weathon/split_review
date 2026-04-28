# A Sanity Check for AI-generated Image Detection

- Decision: Accept
- Avg Score: 6.40
- Scores: 8, 6, 6, 6, 6

## Abstract
With the rapid development of generative models, discerning AI-generated content has evoked increasing attention from both industry and academia. In this paper, we conduct a sanity check on \textbf{\textit{``whether the task of AI-generated image detection has been solved''}}. 
To start with, we present \textbf{\texttt{Chameleon}} dataset, consisting of AI-generated images that are genuinely challenging for human perception. To quantify the generalization of existing methods, we evaluate 9 off-the-shelf AI-generated image detectors on \textbf{\texttt{Chameleon}} dataset. 
Upon analysis, almost all models misclassify AI-generated images as real ones. 
Later, we propose \textbf{AIDE}~(\textbf{A}I-generated \textbf{I}mage \textbf{DE}tector with Hybrid Features), 
which leverages multiple experts to simultaneously extract visual artifacts and noise patterns. 
Specifically, to capture the high-level semantics, we utilize CLIP to compute the visual embedding. 
This effectively enables the model to discern AI-generated images based on semantics and contextual information;
Secondly, we select the highest and lowest frequency patches in the image, and compute the low-level patchwise features, aiming to detect AI-generated images by low-level artifacts, for example, noise patterns, anti-aliasing, etc. 
While evaluating on existing benchmarks, for example, AIGCDetectBenchmark and GenImage, AIDE achieves \textbf{+3.5}\% and \textbf{+4.6}\% improvements to state-of-the-art methods, and on our proposed challenging \textbf{\texttt{Chameleon}} benchmarks, it also achieves the promising results, despite this problem for detecting AI-generated images is far from being solved.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a new dataset for AI-generated image detection named Chameleon. It also proposes a new model for AI image detection. Comprehensive evaluations are conducted.

### Strengths
1.A new datasets and evaluations to show the real status of AI-generated image detection are significant. This work shows that this task is far from solved.
2.The proposed Chameleon dataset is of high-quality and from real-world distributions/sources.
3.The proposed method is straightforward and effective. It combines both high-level semantic features and low-level pixel features.
4.The experiments show effectiveness of the method and the hardness of the new dataset.
5.This paper is easy to follow.

### Weaknesses
1.The experiments are mainly about the effectiveness of the proposed detection model. Some validation of the new dataset in its visual quality perspective will make the work stronger.  E.g., by human studies and comparisons between datasets.
2.In Table 6, it is better to also list the accuracy numbers under no perturbations for convenient comparison.
3.More recent related work can be compared or discussed.

### Questions
Mentioned in the weakness

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
This paper challenges the assumptions in AI-generated image detection by proposing new training and testing settings. It introduces a benchmark called Chameleon to test human perception and shows significant performance drops in nine evaluated models. The paper also presents AIDE, a detector that combines low-level and high-level features, achieving state-of-the-art results but still offering room for improvement.

### Strengths
This paper is relatively well-motivated as AI-generated image detection is a crucial issue. A new dataset named Chameleon is proposed for detecting AI-generated images.  I also find the evaluations thorough. The target issues of the paper are meaningful and worth exploring. The motivation is clear. The paper is easy to follow.

### Weaknesses
1.Over the past few years, a multitude of expansive and varied collections of AI-generated imagery have been crafted. Undertaking an in-depth analysis to contrast the newly introduced Chameleon dataset against its peers, considering factors like dataset size, utilized generation techniques, and the specific types of artifacts present, would serve to underscore its unique contributions. A more granular comparison, perhaps including a feature-by-feature analysis of image characteristics, would be beneficial.

2. It would be good if the authors collect fake images of fake news on the Internet and conduct experiments. This would add a crucial real-world dimension to the evaluation, as these images often have distinct characteristics compared to general AI-generated images, such as specific manipulation techniques and contextual biases.

### Questions
See Weaknesses.

### Soundness
3

### Presentation
2

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
This work aims to answer whether the AI-generated image detection problem has been solved. There are two main contributions in this submission, first, they propose a more challenging dataset, called Chameleon, to evaluate the generation ability of existing fake image detectors. Then, they propose a new detector with hybrid detection features, called AIDE (AI-generated Image DEtector with Hybrid Feature), that shows improved detection performance on this new challenging dataset, compared with the existing baseline detector.

### Strengths
This work's main contribution is that it has proposed a more challenging dataset with diverse categories, with which 9 AI-generated image detectors cannot handle the detection problem well. In the AIGC detection problem, I think it is important to create such a challenging baseline, particularly given the fact that the existing benchmark seems saturated.

Besides, a new detector with hybrid features (including frequency and semantics) is developed, and it shows improved performance on the AIGCDetectBenchmark, the GenImage benchmark, and Chameleon.

### Weaknesses
- This dataset only contains 4 categories, some of which only with hundreds of fake photos, this may not effectively cover the detection of a wide range of photos. The limited number of categories, specifically scene, object, animal, and human, raises concerns about the dataset's ability to generalize to the diverse real-world image distributions. The imbalance in the number of fake images per category, with some having only a few hundred, further exacerbates this issue. For example, the animal category's limited size may not adequately represent the variety of animal appearances and poses, potentially leading to biased detector performance.

- A recent work also adopts a mixture of expert architecture for fake image detection [1], which seems not be included as a baseline. It is supposed to discuss the major differences to AIDE, and serve as a possibly stronger baseline. The absence of a comparison to this specific mixture-of-experts approach is a significant oversight, as it represents a potentially state-of-the-art method in the field. Without this comparison, it's difficult to ascertain the true novelty and performance of the proposed AIDE detector.

- Regarding JPEG comparisons, only QF=95 and QF=90 are evaluated, more real-world compression such as QF=75, and even more severe but practical case e.g. QF=50 are supposed to be evaluated, too. The evaluation of JPEG compression robustness is incomplete, as it only considers high-quality factors. Real-world images often undergo more aggressive compression, and the detector's performance under QF=75 and QF=50 is crucial for practical applicability. The lack of evaluation at these lower quality factors leaves a gap in the assessment of the detector's robustness.

### Questions
- Regarding the dataset construction, this work provides 4 principles in p4, one of which is to cover a wide range of categories. I quite agree with the point. However, this dataset only contains 4 categories, scene, object, animal, and human, and in some categories, there may be only hundreds of photos (e.g. Animal fake images = 313). Then, given the limited number of samples and categories, how can the authors ensure whether the images are representative enough (or cover a wide range of images to be detected)? 

- Regarding the dataset construction, have the authors strictly obey to the 4 principles as presented in p4, or the generated images have been carefully selected and validated in 9 baseline methods beforehand in order to create such as challenging dataset?

- Experiments show 9 detectors cannot perform well on this dataset, this is good. However, I am eager to know the underlying reasons for their failure. Also, can the authors conduct a more fine-grained experiment that checks the accuracy of each of the 4 categories (scene, object, animal, and human), along with the overall category accuracy? I feel this might provide more insights. 

- Regarding the robustness evaluation of the proposed AIDE, if possible, please additionally evaluate JPEG compression with more realistic quality factors e.g. QF=75, QF=50 etc. Similarly, for Gaussian blur, please evaluate sigma=3 and 4.

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
4

### Summary
In this paper, the authors propose a new AI generated image dataset collected from the real-life scenarios, called Chameleon, in which the forgery images are genuinely challenging for human perception. Besides, this paper also provides a novel detection method, which exhibits better detection performance than previous SOTA methods.

### Strengths
•	This paper provides a challenging AI generated image dataset, which is collected from real-life scenarios, and indicates that the problem for detecting AI-generated images is far from being solved.
•	The authors provide a new detection method, achieving better performance than previous methods.
•	This paper is organized well.

### Weaknesses
•	The rationale behind how patches with the highest and lowest frequency highlight the distinctive characteristics of AI-generated images is unclear. The manuscript lacks a theoretical explanation for the proposed method.

•	In Table 2, comparing the entire dataset with subsets of the AIGCDetectBenchmark dataset seems unreasonable. A more appropriate comparison framework should be established. Specifically, the claim that "Chameleon offers greater magnitude" is not correct, as the proposed dataset is smaller than AIGCDetectBenchmark as a whole, and significantly smaller than datasets like GenImage. Thus, the magnitude of the proposed dataset is not a SOTA point.

•	Figure 4 does not provide sufficient evidence to support the claim that SFE (or PFE) can assist AIDE in focusing on specific semantic (or noise-related) clues. It may be beneficial to employ Grad-CAM to visualize the regions of interest when detecting forgery in images.

### Questions
•	The questions are as mentioned above.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces the Chameleon dataset and the AIDE detector for distinguishing between AI-generated and real images.

### Strengths
S1: Comprehensive Dataset: The Chameleon dataset offers a large-scale and diverse collection of AI-generated and real images, providing a robust foundation for training and evaluating detection models.

S2: Detailed Performance Evaluation: The paper provides thorough baseline comparisons and benchmarking, highlighting the strengths and weaknesses of the AIDE detector across various scenarios.

S3: Practical Applications: The focus on detecting AI-generated images is highly relevant in today's digital landscape, with the paper identifying practical areas for improvement.

### Weaknesses
W1: Method Innovation: The combination of patch-level features and global features proposed in this paper is not novel. The methods compared are mostly from the first half of 2023 and earlier, and some of the latest work is not included (such as LaRE^2, Forgery-aware Adaptive Transformer, etc.). The specific implementation of patch-level feature extraction, which appears to involve a block scoring mechanism to highlight high and low-frequency blocks, is not sufficiently differentiated from existing techniques. The use of such frequency-based analysis is a common practice in image processing and lacks a clear novel contribution in this context. The semantic feature embedding module, while conceptually sound, also does not present a substantially new approach, as capturing object co-occurrence and contextual relationships is a well-established technique in image analysis.

W2: Inference Speed: The inference throughput of the proposed method is not provided, nor is it compared with previous methods. The AIDE uses multiple SRMs, ResNet50, and CLIP/ConvNext models, which are much larger than existing work like Gendet that uses just ResNet-50 as the classifier. This raises questions about whether the performance increase claimed in the article is due to increased FLOPS/PARAMS or the AIDE itself. The lack of a detailed analysis of the computational cost and efficiency of the proposed method makes it difficult to assess its practical applicability.

W3: Dataset Comparison: The Chameleon dataset has not been comprehensively compared with existing datasets (such as CNNSpot, AIGCDetect, GenImage, WildFake, etc.) in terms of data size, data sources, semantic categories, generation models, image quality, and other relevant factors. Its novelty has not been sufficiently demonstrated. The paper does not provide a clear justification for why a new dataset is needed, given the existence of several other datasets for AI-generated image detection. A more detailed analysis of the limitations of existing datasets and how the Chameleon dataset addresses these limitations is needed.

### Questions
Q1: What is the cost of data collection, and is it feasible to annotate more data to scale up the dataset?

### Soundness
3

### Presentation
3

### Contribution
2
