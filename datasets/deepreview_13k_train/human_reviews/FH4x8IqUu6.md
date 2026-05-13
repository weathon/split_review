# What Time Tells Us? Time-Aware Representation Learning from Static Images

- Decision: Reject
- Scores: 5, 5, 3

## Abstract
Time becomes visible through changes in what we see, as daylight fades and shadows grow. Inspired by this, in this paper we explore the potential to learn time-aware representations from static images, trying to answer: *what time tells us?* To this end, we first introduce a Time-Oriented Collection (TOC) dataset, which contains 130,906 images with reliable timestamps. Leveraging this dataset, we propose a Time-Image Contrastive Learning (TICL) approach to jointly model timestamp and related visual representations through cross-modal contrastive learning. We found that the proposed TICL, 1) not only achieve state-of-the-art performance on the timestamp estimation task, over various benchmark metrics, 2) but also, interestingly, though only seeing static images, the representations learned by TICL show strong capability in several time-aware downstream tasks such as time-based image retrieval, video scene classification, and time-aware image editing. Our findings confirm that time-aware visual representations are learnable from static images and beneficial for various vision tasks, laying a foundation for future research on understanding time-related visual context.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper addresses the problem of predicting the hour from a given image, leveraging a contrastive loss framework similar to CLIP to align visual space (image) with time representation. It also proposes a data cleanup method and introduces the TOC dataset for hour prediction. The effectiveness of its learned representations is evaluated across multiple downstream tasks, including retrieval, scene classification, and time-aware image editing.

### Strengths
- The paper offers solid motivation with clear writing and well-designed diagrams, facilitating comprehension. Additionally, the visualizations effectively illustrate the method's potential.

- Baseline comparisons are well-chosen, including standard regression methods and varied model architectures such as CLIP, DINOv2, and ConvNext, providing a extensive evaluation.

- The paper presents a broad range of applications, including generative tasks. The choice of diverse experiments is commendable.

### Weaknesses
 - **W1**: A key limitation of the proposed method is its limited technical contribution. The approach employs a simple MLP to project hour-based one-hot encodings into the representation space without advancing time representation in a meaningful way. For instance, while GeoCLIP introduces Random Fourier Features (RFF) to encode geolocation effectively, this work lacks a specific contribution in time representation, appearing more as a direct adaptation of GeoCLIP for time embeddings.
- - **W1.1**: Specifically, the method encodes the floating-point hour value into a one-hot representation of discrete classes (Appendix A.3). This approach underutilizes the ground-truth data, reducing precise time information into approximate class categories. An improved approach might represent time in a hierarchical manner—for instance, with a top-level division for the quarter of the day, followed by classifiers for each hour and even down to minute level—thus preserving the granularity of the original data.

- **W2**: Another major concern is the limited scope of the proposed method. Since it addresses only hour information, it does not account for other factors that significantly affect visual similarity. For example, the time of year (season) can substantially alter a location's appearance, making the problem ill-defined without considering month information. Another influencing factor could be the geographic location, which also impacts visual appearance.

- **W3**: The details provided about the TOC dataset in the Appendix (particularly Fig. 9) reveal a clear skew towards countries in the Western and Northern hemispheres. This imbalance is undesirable for the proposed hour-prediction problem, as geolocation significantly impacts appearance-based similarity in relation to time representation.

- **W4**: On closer examination of the time-based editing results (Fig. 28), it’s apparent that the generated edits fails to retain original image information. For instance, in Fig. 28(b), second row, the building structure noticeably changes. It may not be clear at the low-resolution results provided in the paper. Although this is an observation not central to my evaluation, such shifts may defeat the intended purpose of the editing application.

- **W5**: The video scene classification task raises two questions:

- - How does this task contribute to evaluating time-aware representations? Scene classification should ideally be time-invariant.

- - The proposed scene classification pipeline does not look intuitive. For zero-shot classification, it would be intuitive to use only the candidate model (e.g., CLIP) features. The introduction of VideoMAE here is unexpected, and it would be helpful for the authors to clarify this choice in the rebuttal.

### Questions
Please refer to the limitations section for further details.

Q1: The choice of partitioned classes for representing time is unclear. Could the authors provide a justification for this design choice over other choices like using RFF or using an hierarchical representation? (See Weakness W1.)

Q2: How is video scene classification a relevant downstream application for evaluating hour-aware representations?

Q3: What is the reason behind appending VideoMAE features? Could the authors provide results, such as those in Table 3, without the inclusion of VideoMAE features?

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper presents a dataset (TOC: Time-Oriented Collection) and method (TICL: Time-Image Contrastive Learning) for hour prediction. The TOC dataset is a filtered subset of the Flickr images from the CVT dataset. Filtering is done by removing irrelevant images, like memes/text and images with incorrect timestamps. TICL is a method that aligns CLIP image embeddings after an adapter layer with the embeddings from a time encoder using a CLIP-like contrastive loss. The experimental results show state-of-the-art performance on hour prediction compared to other methods, as well as applications of the time-aware image embeddings on retrieval, editing, and video scene classification.

### Strengths
TICL achieves SoTA performance on hour prediction compared to other methods, such as Zhai et al. (2019) and Salem et al. (2022). 

The authors conduct ablations using different image backbones, clearly showing that CLIP is the best option. Furthermore, the authors show that using the time encoder module and time adapter performs better on most metrics. 

The paper has an interesting analysis explaining why regression methods don’t work well, even when trained with a circular MSE loss. 

Cleaning the images from CVT makes sense, given that some of them do not contain any time information (for example, memes), and training with them would probably hurt the model performance. 

The time-based image retrieval application with TICL shows significant improvement over other methods.

### Weaknesses
Method and results 

TICL is only able to predict the hour of the day, while previous SoTA methods are able to predict multiple things besides hours. The method proposed by [1] predicts the hour, month, and geographical location of the images, while [2] predicts the hour, week and month. Comparing TICL with these other methods is not completely fair, given that they need to allocate capacity to other tasks as well. 

Other recent methods, such as [3] are also able to predict hours and months indirectly and are trained with similar datasets, but the authors didn’t include it in their evaluation. The code and model weights for [3] are publicly available and the authors should include it as a baseline. Please include this model as a baseline. 

The method itself is not very novel. It is largely based on GeoCLIP with simplified components, such as replacing the Random Fourier Features (RFF) Encoder with an MLP and removing the dynamic queue. 

The authors should conduct ablations with different time representations and encoder architectures. There should be a table comparing their time encoder with the RFFs encoder from GeoCLIP and with Time2Vec [4].  

It’s not clear why the hours are converted into one-hot encoded vectors before passing them to the time encoder. A more straightforward approach would be to pass the hour directly as an integer/float and project it to a high-dimensional vector with a linear layer. Another option would be to decompose the hour into sine and cosine components, similar to [5]. Please conduct further ablations using this time representations. 

It would be interesting to see a more in-depth analysis of the time prediction errors. The confusion matrices are a good start, but quantitatively, what is the accuracy at different moments of the day? In other words, how does the error during the morning, noon, afternoon, and night compare against each other? For example, it seems like in the AMOS test set a lot of images in the morning are being confused by images in the afternoon.  

Also, one hour can look very different in the same location but different months, or in the same month but different locations. How does the time prediction error close to the Equator compare against a location at high latitudes? Or how does the time error in a location close to the tropics change during the summer and winter seasons. These questions are interesting but left unexplored. 

Dataset 

The AMOS subset from CVT has ~100k images. Since this dataset is from outdoor cameras across the whole day and year, around half of them are captured at night. In some cameras, these images look too dark to get any meaningful time information. However, this leaves around 50k daytime images, most of which have good weather and there is no reason to exclude them from the test set. If the authors only train on TOC, why are they testing the model only on 3556 AMOS images?  

Cleaning the Flickr subset of CVT makes sense, but the authors should’ve conducted experiments training the model with the original “noisy” dataset and the clean dataset to show how this step is crucial for good time prediction. 

Applications 

The retrieval and editing applications are interesting, but it’s not clear why a time-aware time embedding would help in the video scene classification task. First of all, why would a time-aware embedding help in scene classification? Intuitively, a model for scene classification should be invariant to time, so why is TICL helping? 

By looking at figure 5, it seems that TICL embeddings form better clusters than the vanilla CLIP embeddings for the different scene classes. However, most of the scene classes are indoors (bedroom, car, hotel, kitchen, etc.). The images from CVT are mostly from outdoor scenes, so how can the model help predict indoor scenes if it has seen very few indoor images? During training Also, the gap between VideoMAE+CLIP and VideoMAE+TICL seems unreasonably large compared to the other datasets, where gains are modest, why is that the case? 

The time editing tasks seems to work well, but it would be interesting to see if it produces realistic shadows or color hues given the time of day. For example, a simple test would be to take a picture of an object with known height, let’s say at 10 AM and 4 PM, and measure the shadow lengths. Then, pass the 10 AM image to the editing model and change the time to 4 PM to see if the angle and length of the shadow in the generated image matches the real image.

### Questions
Questions 

Please refer to the weaknesses section. Here are some additional questions: 

Are all previous methods shown in table 1 retrained with the TOC train set? 

During the dataset filtering process, the authors remove images that appear during daytime but are captured at 12 AM. Do they do the same for other typical night hours, such as 11 PM, 1 AM, etc.? Also, there might be some edge cases where 12 AM has sunlight, like in locations with high latitudes. Did the authors consider such cases? 

What is the accuracy of the DBSCAN method in removing unnatural or uncalibrated images? If accuracy is not a good metric, how are the authors validating that the filtering method is working correctly?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper demonstrates that learning time-of-day classifier on top of a frozen CLIP backbone does better than learning it on top of other feature representations (e.g. DINO) as well as better than previous works that learned such models end-to-end (e.g. with a ResNet). To present a more faithful evaluation, the authors combine exiting datasets and manually filtering them to remove unnatural samples and samples with incorrect timestamps. In addition, the authors demonstrate that the resulting projection of the CLIP features can be useful for some other tasks that can benefit from time-of-day understanding (e.g. video scene classification).

### Strengths
The paper is relatively well written and easy to parse.

The conclusion that CLIP features are useful for time-of-day classification due to their strong semantic understanding capabilities is reasonable. 

The proposed approach outperforms prior work by a large margin by capitalizing on CLIP features. That said, there are questions to the experimental setup (see below).

Cleaning up the annotations in existing time-of-day classification datasets is a useful effort.

### Weaknesses
Virtually no implementation and experimental setup details are reported in the paper, making it impossible to judge the significance of the reported results. Most importantly, it’s unclear if other methods were also trained on the clean training set collected by the authors or if the authors just evaluated the publicly available checkpoints. It is also unclear what the backbones used in ablation in Table 2 were pre-trained on (except for DINO-v2). It is also unclear why for some models ViT-Base variant is used, but for others (e.g. the CLIP backbone) ViT-Large is reported.

Same goes for the downstream task evaluations in section 5.3. For example, the proposed CLIP projection results in a major performance improvement on the Hollywood2-Scene dataset (26.8 accuracy points over the second-best variant) which is not explained by the authors and is probably an artifact of the (unreported) hyper-parameters used when learning a linear classifier on this dataset.

Overall, all the downstream evaluations in the paper are designed by the authors and the details are not reported so it’s impossible to trust the results.

The contribution is significantly overclaimed. The authors talk about "representation learning" but training a projection module on top of a frozen CLIP encoder is not representation learning. The only (somewhat) convincing results are reported on the task of time-of-day classification for which the projection module was trained. 

To sum up, the focus of this paper is extremely narrow, the novelty is minimal, and the experimental evaluation is flawed/unconvincing.

### Questions
Please report:

The exact training dataset used for each compared method.
Pre-training details for all backbones used in ablations.
Rationale for using different model sizes (ViT-Base vs ViT-Large) across ablation experiments.
A detailed description of each downstream task evaluation setup.
Potential reasons for such a large performance improvement gap between Hollywood2-Scene and other video scene classification datasets. Conduct additional experiments or analysis to verify that the improvement is not due to some artifact of the setup.

Please revise the claims to more accurately reflect the scope of the work.

### Soundness
2

### Presentation
3

### Contribution
1
