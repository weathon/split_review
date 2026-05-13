# The BabyView dataset: High-resolution egocentric videos of infants’ and young children’s everyday experiences

- Decision: Reject
- Scores: 6, 3, 8, 5, 5

## Abstract
Human children far exceed modern machine learning algorithms in their sample efficiency, achieving high performance in key domains with much less data than current models. 
This ``data gap'' is a key challenge both for building intelligent artificial systems and for understanding human development.
Egocentric video capturing children's experience -- their ``training data'' -- is a key ingredient for comparison of humans and models and for the development of algorithmic innovations to bridge this gap.
Yet there are few such datasets available, and extant data are low-resolution, have limited metadata, and importantly, represent only a small set of children's experiences.
Here, we provide the first release of the largest developmental egocentric video dataset to date -- the BabyView dataset -- recorded using a high-resolution camera with a large vertical field-of-view and gyroscope/accelerometer data.
This 493 hour dataset includes egocentric videos from children spanning 6 months -- 5 years of age in both longitudinal, at-home contexts and in a preschool environment.
We provide gold-standard annotations for the evaluation of speech transcription, speaker diarization, and human pose estimation, and evaluate models in each of these domains. 
We train self-supervised language and vision models and evaluate their transfer to out-of-distribution tasks including syntactic structure learning, object recognition, depth estimation, and image segmentation. 
Although performance in each scales with dataset size, overall performance is relatively lower than when models are trained on curated datasets, especially in the visual domain. 
Our dataset stands as an open challenge for robust, human-like AI systems: how can such systems achieve human-levels of success on the same scale and distribution of training data as humans?

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents a large-scale developmental video dataset (the Babyview dataset), recorded using wearable cameras worn by young children. Babyview comes with video and IMU data, as well as automatically generated speech transcription, speaker diarization, and human pose data. Leveraging this dataset, the authors conducted a series of benchmarks on visual and language representation learning, leading to some interesting results and findings.

### Strengths
The Babyview dataset presents one of the largest developmental egocentric video datasets capturing children’s visual experience. This dataset offers the opportunity to address key research questions in developmental physiology and machine learning, e.g., the gap in learning efficiency between machines and humans.

The dataset, which represents a considerable investment of effort, will be accessible to authorized research teams, serving as a valuable resource to facilitate future research.

While the annotations are automatically derived from data, a comparison to human annotations was considered to quantify the annotation quality.  

The paper is fairly well written and easy to follow. Technical details are well described. 

The benchmarks are interesting, though many of their results are not very surprising.

### Weaknesses
I am not entirely convinced by the recording setup. The camera has a large vertical field of view, but a rather narrow horizontal field of view that seems to be much smaller than human vision system. While it is true that we do not have high resolution peripheral vision, ignoring some major portion of the field of view seems problematic for capturing the children's visual experience. 

The experiment design and the presentation of the results could use some work. 
* For example, Figure 2 included a "logistic fit" to extrapolate the trend of models trained on developmental data. There is little justification or explanation about this fit. Similarly, Figure 3 considered a log-linear extrapolation of the vision results. It is not clear if this extrapolation is reasonable. 
* Another example is Table 4. The performance gap between models pretrained on egocentric videos and those trained on Internet images may stem from the domain shift between the two types of data. One possible approach to address this is to evaluate models pretrained on developmental egocentric videos using other egocentric video datasets.

### Questions
It would be a good idea to include some details about the camera, e.g., the field of view of the camera, resolution of the video, to make the paper self-contained.

The authors are encouraged to further elaborate how the dataset can be used by the machine learning community at large.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors propose a large-scale, high-resoultion dataset for visual learning for infants. The dataset contains large field-of-view, accelerometer data, and annotations including speech transcription, speaker diarization, and human pose estimation. Using this dataset, the authors investigated self-supervised models in both language and visual domain, and found inferior performance compared to models trained on curated datasets.

### Strengths
[+] The proposed dataset aims to provide data for a very interesting and important research question - How can biological vision learn so efficiently and effectively with limited amount of data (experience) and supervision.

[+] The authors provide detailed description of dataset preparation, including data capture, access, and annotations.

[+] It is interesting to see investigation into both the linguistic and vision representation learning jointly stemmed from a single dataset.

### Weaknesses
[-] My main concern is that the contribution and usefulness of the proposed dataset is not exactly clear. Although large-scale and high-resolution, the dataset does not contain any control or interaction motivated by the observer (infant).
- It is my belief that a large component of visual learning is from interacting with our environments and paying attention to things that surprise us. 
- This feedback is absent in the datasets of this format. I am curious what the authors' position on the significance of the lack of observer-driven controls, and whether it is feasible for such a dataset to produce model that can match human performance.
- By simply observing the visual world from an infant perspective, I am leaning towards the results from the Kitten Carosel experiment (Held And Hein, 1963).
- This perspective is further confirmed by the reported inferior quantitative results, both in language and visual domain.
- Although this dataset looks promising, I could not find sufficient evidence in the current version of the manuscript to support its usefulness. Further investigations in how this dataset can be useful for certain tasks / insights would greatly improve the paper in my opinion.

[-] Regarding the investigation in self-supervised vision models, the authors considered DINOv2 and MoCov3, which both assume a diverse set of images as input. I don't believe that they would take the full advantage of the video data in this dataset. Lines of work including [B-D] would be more appropriate here.

### Questions
Please refer to weaknesses.

### Soundness
1

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents the babyview dataset, a developmental dataset with egocentric videos taken from the child’s perspective. Alongside, language and human pose annotations are provided. Furthermore, the authors benchmark language and visual self-supervised learning on this dataset, providing insightful discussions on the results.

### Strengths
+ The BabyView dataset is a valuable addition to the limited pool of egocentric developmental datasets and is well-positioned to enable further analysis in this domain.

+ The benchmark results in Section 5 and the general discussion in Section 6 are particularly engaging. They highlight the challenges in visual self-supervised learning from egocentric videos in particular, which lag behind language representation learning. 

+ It is good to have the data scaling experiments (Figure 2 & 3). They provide an estimation of the data amount needed for machines to achieve human-level performance, offering insights for future research.

### Weaknesses
The paper notes the greater difficulty of visual self-supervised learning on egocentric videos compared to language representation learning. While this observation is generally accurate, additional discussion could clarify the role of domain gap in downstream tasks. Namely, language evaluation is less impacted by domain shift, unlike visual tasks, where the evaluation tasks (object detection, depth estimation, semantic segmentation) are essentially from third-person viewpoints. This disparity impacts the performance of models trained on egocentric data. On the other hand, several egocentric tasks in EPIC-Kitchens and Ego4D, such as egocentric action recognition, could also serve as evaluation tasks. These may show different trends, as they do not face the ego-exo viewpoint gap. It would be helpful if the authors could expand on these distinctions and their implications.

+ Including EgoExo4D (https://arxiv.org/abs/2311.18259) in related works and Table 1 for comparison could be helpful, as it’s a recently introduced foundational benchmark for egocentric research. Additionally, could the authors clarify what the "Long?" and "N" columns in Table 1 signify? 

+ Section 4.2, are the pose annotations specifically for adults recorded in the videos? An example figure of pose annotations in the main paper could enhance clarity. Likewise, it would also be good to include a language annotation example in the main paper.

+ L356-358, Could the authors explain the rationale for extracting Ego4D at 1 FPS versus BV-Home and SAYCam at 5 FPS?

### Questions
+ Including EgoExo4D (https://arxiv.org/abs/2311.18259) in related works and Table 1 for comparison could be helpful, as it’s a recently introduced foundational benchmark for egocentric research. Additionally, could the authors clarify what the "Long?" and "N" columns in Table 1 signify? 

+ Section 4.2, are the pose annotations specifically for adults recorded in the videos? An example figure of pose annotations in the main paper could enhance clarity. Likewise, it would also be good to include a language annotation example in the main paper.

+ L356-358, Could the authors explain the rationale for extracting Ego4D at 1 FPS versus BV-Home and SAYCam at 5 FPS?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents the BabyView dataset, a novel dataset of egocentric videos from infants aged 6 months - 5 years captured over their developmental years. It includes 430 hours of high-resolution videos captured from a GoPro Hero Bones camera mounted on a safety helmet designed for infants (100 x 75 degrees FoV) and gyroscope/accelerometer data. Furthermore, there are annotations for evaluating speech transcriptions, speaker diarization and human pose estimation. The authors perform language learning and visual task learning experiments to assess the quality of the data when compared to other egocentric datasets and internet-style curated datasets. The findings suggest that current self-supervised approaches are more successful when trained on curated datasets than on egocentric datasets. Overall, this dataset presents a challenge for developing human-like AI systems that can learn efficiently with sensory information captured from the developmental stages of infants.

### Strengths
I like the motivation behind the paper and feel it has some key strengths.
* The dataset contains diverse egocentric videos captured through the developmental stages of infants. It will be a valuable resource to the community for developing biologically-motivated learning algorithms. 
* The large-scale nature and diversity are useful for splicing the dataset along different axes (e.g., data from a particular age group, data for a single infant through several years of development, etc.). Moreover, the dataset is not split into train/val/test splits. Different communities can split the data as appropriate for their settings. 
* The authors have promised to share the data while maintaining the privacy of participants. This is missing in prior developmental datasets that can have restrictions, barring large parts of the research community from using them openly.

### Weaknesses
IMO, the paper has three main weaknesses.

# 1. Objective measures of the dataset's value

* The authors claim that this is a great dataset, but the objective value of the dataset is not quantified properly.

* First, none of the existing learning algorithms benefit from BV-Home (for language in Figure 2 and vision in Table 4). All ego datasets fall short of curated datasets. But more importantly, BV-Home does not distinguish itself from Ego4D / SayCam / CHILDES in any way. All the analyses presented could have been equivalently performed on other datasets (e.g., SayCam), and similar conclusions would have been reached.

* L431 "our results suggest that current self-supervised ... are dependent on large, curated datasets .." -- this suggests that the failure of current methods to do well with BabyView is attributed to the method design and not the dataset design. While this is partly true, it remains to be seen whether more developmentally accurate learning algorithms (whatever they may be) would do well with the BabyView dataset. As acknowledged by the authors in L450 - 458, there are inherent selection biases and diversity restrictions associated with the dataset that could prevent developmentally accurate learning algorithms from working well.

* As the authors state in L445, developmentally appropriate benchmarks may be needed to quantify the value of the BabyView dataset. Since these do not exist yet, I feel it is up to the authors to demonstrate the utility of the proposed dataset. This is missing.

Overall, the benefit of BabyView dataset over existing datasets has not been demonstrated experimentally. If standard vision and text benchmarks are not appropriate, then the onus is on the authors to identify/design better benchmarks or alternative metrics to bring out the value of developmental ego video datasets.


# 2. Annotation quality and utility are not clear
* The results in Table 2 suggest that the WER (%) is low (which is good), but the diarization precision and recall are poor for "gold-standard annotations". The quality of the pose annotations is also not quantified. 
* Moreover, the utility of these annotations is not clear. For example, the annotations in Ego4D were explicitly used to define benchmarks for the community to make progress on. The application in Ego4D was for head-worn AR/VR devices, which are a practical use case for the benchmarks. In BabyView, the annotations are stand-alone, and their utility is unclear and unquantified.

# 3. Tools to access the dataset 
* As a quality-of-life measure for users who want to utilize this dataset, it is not clear how access to such a large-scale dataset will be facilitated and simplified. Will there be tooling developed to easily download and visualize the videos and annotations? Will there be tooling for users to download meaningful subsets of the dataset (e.g., data for infants from ages 1 - 2)?

### Questions
1. What is the objective measure of the dataset's value?
2. Is the annotation quality truly "gold-standard"? The vision community has a high bar for human annotation quality.
3. How do users navigate this large-scale dataset? Will appropriate tooling be developed around the dataset?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this paper, 2 new datasets are proposed consisting of recordings from children growing up between 6 months and 3 years representing a huge effort from collection. This specialised egocentric viewpoint represents a rare collection. The babyview dataset includes over 430 hours from multiple children and a separate 47 hour dataset which consists of one participant is also released (named Ego-SingleChild). Experiments showcase the interest in the data collected for self supervised models, and evaluating on language understanding tasks as well as vision tasks such as human pose estimation and object recognition.

### Strengths
* The data collected is interesting, will be released to the research community, and represent new video data that can be used for both computer vision and other disciplines (such as psychology).
* The effort for the data collection is huge representing long-term, real world data collection totalling over 400 hours of recorded video.
* The data could be of great use for further self-supervised research and model/algorithmic improvements.

### Weaknesses
# Weaknesses

* Table 1: EPIC-Kitchens and part of Ego4D should have Accelerometer data from the recordings depending on the devices that are used from the papers of both datasets. Additionally, what does the long category mean in this context? What's the threshold for a dataset to be considered long? It is unclear what the specific criteria are for a dataset to be classified as 'long' in this context, and how this impacts the analysis or the suitability of the dataset for different tasks. The lack of a clear definition makes it difficult to compare the datasets effectively.
* Line 129 describes the work as the first release of the dataset. This phrase makes me question as a reviewer whether the dataset can be considered finished, is the work complete enough to make use of for the proposed tasks or should the community wait for more data? This statement feels premature, especially given the experimental results which seem to indicate that more data would be beneficial for the tasks explored. The implications of releasing a dataset that is still under active collection should be addressed more clearly.
* Line 152, what does 0;5-3;1 years mean in the context of the ages? The notation used for the age range of the participants is not standard and requires clarification. It is not immediately obvious what the semicolon represents, and this could cause confusion for readers unfamiliar with this specific notation. A more explicit definition should be provided.
* Table 3 AP and AR are not defined (this is only defined in the context of the appendix however there is a lot of space within the main paper for more definitions such as these. The lack of definitions for AP and AR within the main body of the paper makes it difficult to understand the reported results. While the definitions are present in the appendix, they should be included in the main text for ease of understanding and to avoid forcing the reader to constantly refer to the appendix.
* The experiments showcase interesting results, but they feel a bit unfocused as a section, it's not clear what the main tasks are for this dataset, beyond what is discussed within the paper, but then in the discussion section speech recognition and pose recognition perform well on the data from the dataset. The experimental section lacks a clear narrative and the connection between the experiments and the intended use of the dataset is not well-defined. The experiments seem to be a collection of exploratory tasks rather than a focused evaluation of the dataset's capabilities.
* Line 425 I'm not sure I agree with the statement of providing improved data, and not sure where this is coming from for the results. The claim that the dataset provides improved data is not sufficiently supported by the results presented. It is unclear what specific metrics or comparisons are being used to justify this statement, and more evidence is needed to support this claim.
* Line 733: Some of the demographics seem very skewed towards certain demographics. This is not a failing of the dataset as it represents initial work and findings, but to have some discussion/experiments regarding this lack of variance would be good to see. Of particular note is the family income. The demographic skew in the dataset, particularly regarding family income, raises concerns about the generalizability of the findings. While this is acknowledged, a more thorough discussion of the potential impact of this skew on the results and the limitations it imposes would be beneficial.
* Line 802: The speaker labels imply that only mothers were captured during the dataset, is this true? The speaker labels suggest a potential bias in the dataset towards mothers, and it is unclear if other caregivers were also included. This potential bias needs to be addressed, and the reasons for the exclusion of other caregivers should be explained.
* It would be interesting to see whether there is a large domain shift between the babyview dataset and the Ego-SingleChild, as well as the other egocentric datasets that have been compared to in the paper. The potential for domain shift between the different datasets, especially between BabyView and Ego-SingleChild, is a significant concern that needs to be addressed. The impact of this domain shift on the performance of models trained on one dataset and evaluated on another should be investigated.

### Questions
1. I would like to see some clarification regarding what the authors envisage for the future of the dataset and any specific tasks that they have in mind. Maybe it is because of the current structure of the paper, but this wasn't clear to me over my multiple read-throughs. The experiments consist of a mix of potential tasks and exploratory experiments for the reader to get a sense of the dataset. This is only mentioned within the discussion, but it's hard to refer to which experimental results refer to which part of the discussion.
2. Why is the current version of the dataset being released now, if data is continued to be collected, why not wait until a larger dataset can be released? There are some experiments within the paper that showcase the amount of data required, i.e. Figures 2 and 3, imply that more data is needed, but then the discussion implies that more data wouldn't help.
3. Have experiments/more investigation gone into the potentially skewed demographics that have been collected? It would be good to see some discussion regarding these.
4. Were only mothers and children collected within the dataset? Was there a reason as to why fathers were not included?
5. Have any experiments/investigation regarding the difference in domains between the different cameras from the two datasets as well as other egocentric datasets such as Ego4D or EPIC-Kitchens?

### Soundness
2

### Presentation
3

### Contribution
4
