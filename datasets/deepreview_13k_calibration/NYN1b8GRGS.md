# GIM: Learning Generalizable Image Matcher From Internet Videos

- Decision: Accept
- Avg Score: 5.75
- Scores: 8, 1, 8, 6

## Abstract
Image matching is a fundamental computer vision problem. While learning-based methods achieve state-of-the-art performance on existing benchmarks, they generalize poorly to in-the-wild images. Such methods typically need to train separate models for different scene types (\eg, indoor vs. outdoor) and are impractical when the scene type is unknown in advance. One of the underlying problems is the limited scalability of existing data construction pipelines, which limits the diversity of standard image matching datasets. To address this problem, we propose GIM, a self-training framework for learning a \emph{single generalizable} model based on any image matching architecture using internet videos, an abundant and diverse data source. Given an architecture, GIM first trains it on standard domain-specific datasets and then combines it with complementary matching methods to create dense labels on nearby frames of novel videos. These labels are filtered by robust fitting, and then enhanced by propagating them to distant frames. The final model is trained on propagated data with strong augmentations. Not relying on complex 3D reconstruction makes GIM much more efficient and less likely to fail than standard SfM-and-MVS based frameworks. We also propose ZEB, the first zero-shot evaluation benchmark for image matching. By mixing data from diverse domains, ZEB can thoroughly assess the cross-domain generalization performance of different methods. Experiments demonstrate the effectiveness and generality of GIM. Applying GIM consistently improves the zero-shot performance of 3 state-of-the-art image matching architectures as the number of downloaded videos increases (Fig.~\ref{fig:Teaser} (a)); with 50 hours of YouTube videos, the relative zero-shot performance improves by $8.4\%-18.1\%$. GIM also enables generalization to extreme cross-domain data such as Bird Eye View (BEV) images of projected 3D point clouds (Fig.~\ref{fig:Teaser} (c)). More importantly, our single zero-shot model consistently outperforms domain-specific baselines when evaluated on downstream tasks inherent to their respective domains. The source code, a demo, and the benchmark are available at \href{https://xuelunshen.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a self-supervised method for image correspondence learning from easily accessible internet videos. The proposed method first trains an image-matching network on a standard dataset with GT supervision and then combines it with complementary image-matching methods to generate candidate correspondences between nearby frames of internet videos. Then, robust fitting is applied to remove outliers in the generated candidate correspondences. The remaining correspondences are used to re-train the image-matching network. By using this self-supervised training scheme, the performance improvement on existing image-matching models is impressive.

### Strengths
Many of the current deep networks suffer from poor generalization ability to unknown data distributions when the amount and diversity of training data are limited. Fine-tuning the model on the target data distribution with a small amount of data from the target domain with GT supervision is a natural way. However, obtaining GT information of the data from the target domain might not always be easy, especially in correspondence matching, pose estimation, 3D reconstruction, etc. 

To address this challenge, this paper introduces a self-supervision strategy for image matchers using readily available internet videos. There is no need to run an SfM or COMAP pipeline, which is usually computationally expensive and un-robust to in-the-wild images, to obtain the GT correspondences. The performance improvement on three standard image-matching networks, diverse evaluation images, and various downstream tasks is impressive.

### Weaknesses
My comments below are more like questions instead of weaknesses.

(1) The proposed method combines a baseline image-matching network (e.g., SuperGlue, LoFTR, DKM) trained on a standard dataset and complementary image-matching methods to generate candidate correspondences. From the experiments section, the complementary image matching methods perform inferiorly than the baseline network. I have two questions here.
     a. Since the performance is inferior, why are they needed? Will this increase the number of estimated correspondences between two images and thus improve the performance?
     b. The introduction says "multiple" complementary image matching methods are used. While in the experiments section, it seems that only one complementary image matching method is used for each baseline method (SuperGlue, LoFTR & DKM). Will the number of complementary methods affect the performance?

(2) Does batch size affect the self-supervision performance? From the implementation details, the GIM label generation on 50 hours of YouTube videos takes 4 days on 16 A100 GPUs. How long will it take to re-train a baseline network using the generated labels (and on which type and how many GPUs)? Will the proposed method still work on an RTX 3090, which is commonly used in universities?

### Questions
Please refer to the weakness section above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposed a Generalizable Image Matcher. It generalizes across training sets, view points, it works with BEV and even point cloud.

They also proposed ZEB, the first zero-shot evaluation benchmark for image matching. The claim it mixes data from diverse domains,
by using it one can assess the cross-domain generalization performance.

Extensive experiments on state-of-the-art baselines are compared.

### Strengths
The overview image in page.1 is impressive already. The method works on three strongest baseline (DKM, SuperGlue, and LoFTR) and improves them further more. It surprises me the method works with such huge view point differences and it also works with BEV pointcloud.

The training is using internet videos which prevents the COLMAP (SfM + MVS) bias for a single scene.

The proposed GIM is essentially a point matching ground-truth reinvention by using the label propagation through video with strong augmentation. However, it's so effective on every method by using the same training according to section 3.1.

I consider the simplicity not a weakness, but as a strength. If the proposed method is reproducable, I believe it would be the new standard of image matching.

The reconstruction results in Fig.3,4,5 are very impressive especially when you know it's training on sequence video instead of SfM alike scenario.

### Weaknesses
This paper is very impressive, I think the only thing left is just some implementation details becuase the self-training part is very short and only about the ground-truth instead of the training itself. 

The only thing left is just open-sourcing the proposed code of the label propagation and training data to verify it's accuracy.

### Questions
Please share more about the training details. By domain specific training is it just swapping the GT or there are more details that's not being covered in the paper?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Observing that existing datasets for learning image-matching algorithm lacks diversity, the authors propose to learn image matchers from diverse tourism videos available on the internet. To obtain (pseudo-)labels for training, the authors propose to aggregate predictions from multiple matchers trained on small datasets and use a label propagation algorithm to propagate labels beyond nearby frames. Training on the pseudo-labeled data, existing image matching techniques demonstrate strong generalizability to unseen image domains, significantly outperforming image matchers trained on traditional datasets. In addition, the authors demonstrated that the proposed self-training framework showed strong scaling behavior, promising stronger image matchers for future work.

### Strengths
1. Simple and scalable framework: The proposed self-training framework is simple and scalable. 
2. Strong zero-shot generalizability: Compared to image matchers trained on the traditional datasets, image matchers trained using self-training demonstrated stronger zero-shot generalizability, yielding more robust and performant image matchers. 
3. Comprehensive experiments: Experiments include large collections of datasets and downstream tasks, showing the superiority of self-trained image matchers.

### Weaknesses
1. Lacking real indoor datasets in the benchmark: This is a nitpick but it would be great to have more real indoor datasets in the benchmark. Right now, most of the real datasets are driving-related and the indoor dataset only covers basements and corridors.

### Questions
Questions:
1. Will the performance continue to improve if the self-training is repeated multiple times or do the authors expect the models to start degrading due to noisy pseudo-labels?
2. Current work focuses on tourism videos. Would the approach work for other types of videos such as egocentric videos?


Suggestions:
1. (Related Work) Image Matching Datasets: MegaDepth is outdoor and ScanNet is indoor?
2. Section 3.1: “Multi-method Matching” was a little confusing. Would it make sense to use “Pseudo-matches Generation through Multi-method Matching”?
3. Table 1 KIT: GIM_LoFTR is slightly worse that LoFTR (out). 
4. Table 2 w/o video: The reviewer assumes this is DKM (IN). It would be nice to specify this in the table. 


Pre-rebuttal Rating: Overall, this is a good paper that presents an alternative to learning strong image matcher. The zero-shot investigation is insightful, and the framework’s strong zero-shot performance is encouraging despite its simplicity. The reviewer recommends accepting the paper prior to the rebuttal stage.

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces the GIM framework, aiming to address the challenge of generalizing image matching to diverse real-world scenarios. Taking cues from established computer vision models, GIM adopts a zero-shot generalization approach, leveraging the vast and varied nature of internet videos. The methodology involves a two-step training process: initial training on domain-specific datasets followed by an integration with several image matching techniques. This combined model seeks to identify potential correspondences in close video frames, with outlier detection mechanisms ensuring data quality. Notably, while traditional methods such as SfM and MVS have exhibited limitations in handling in-the-wild videos, GIM claims to efficiently provide reliable supervision signals for these scenarios, thereby promising to push the boundaries of current state-of-the-art models.

### Strengths
+ The introduction of the GIM framework is a significant advancement, marking the first attempt to leverage internet videos in training a universally applicable image matcher. This initiative promises to address generalization challenges across multiple real-world contexts.

+ The formulation of the ZEB benchmark is a noteworthy achievement. As a pioneering zero-shot evaluation benchmark integrating real-world and simulated data, ZEB is poised to become an instrumental tool in gauging the generalization capacities of existing models.

### Weaknesses
 - The heavy reliance on internet videos for training might introduce biases or noise. The generalization capability of GIM, when trained on other diverse datasets, remains an unanswered question.

- With the consistent performance improvement with increased video data, there might be concerns about potential overfitting. Addressing this, perhaps with regularization techniques or other measures, would be crucial.

- Internet videos can be noisy, and their quality can vary. How resistant is GIM to such noise, and how does it handle low-quality data?

### Questions
-  While the use of internet videos is innovative, how did you ensure that the videos used for training represent a diverse range of scenarios, especially given the potential for internet content to have biases?

- How does the GIM model handle noise and varying quality within internet videos? Were any preprocessing steps or filters applied to ensure data quality?

- How did you address concerns of overfitting, especially with the consistent improvement seen with increasing video data?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
