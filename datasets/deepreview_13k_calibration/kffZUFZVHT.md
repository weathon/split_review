# Mouse Lockbox Dataset: Behavior Recognition of Mice Solving Mechanical Puzzles

- Decision: Reject
- Avg Score: 5.60
- Scores: 5, 5, 6, 6, 6

## Abstract
Machine learning and computer vision have a major impact on the study of natural animal behavior, as they enable automated action classification of large bodies of videos. Mice are the standard mammalian model system in many fields of research, but the open datasets that are currently available to refine machine learning methods mostly focus on either simple or social behaviors. In this work, we present a large video dataset of individual mice solving complex mechanical puzzles, so-called lockboxes. The dataset consists of a total of well over 110 hours of animal behavior, recorded with three cameras from different perspectives. As a benchmark for frame-level action classification methods, we provide human-annotated labels for all videos of two different mice, that equal 13% of our dataset. The used keypoint (pose) tracking-based action classification framework illustrates the challenges of automated labeling of fine-grained behaviors, such as the manipulation of objects. We hope that our work will help accelerate the advancement of automated action and behavior classification in the computational neuroscience community. An anonymized preview of our dataset is available for the reviewers of this manuscript at https://www.dropbox.com/scl/fo/h7nkai8574h23qfq9m1b2/AP4gNZOpDJJ7z0yGtbWQiOc?rlkey=w36jzxqjkghg0j0xva5zsxy2v&st=5r9msqjw&dl=0

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors present a new, large dataset of lab mice solving mechanical lockbox puzzles. Unlike existing animal behavior datasets, their lockboxes capture more cognitive / learning / problem solving abilities of the animals. In the future, this dataset, or the use of the lockboxes morie generally, could be used to better understand motor and cognitive learning and complex neural computations and processes. At the moment, the dataset's benchmark includes recognizing a set of actions or action.puzzle states.

### Strengths
The author present an interesting and novel new dataset of mice solving puzzles. It is not 100% clear to me the extent of the research questions one could use such a dataset for, and I encourage the reviewers to expound on this in their revision.

### Weaknesses
As a dataset paper, the authors should be providing additional technical details, data quality metrics, and an expanded set of methods for benchmarking. I've left specific comments on these points in the questions section.

A few things in the introduction that would be good to clarify in the text.

L55 -- you say that it is a disadvantage that poses are low dimensional. But there are many scenarios where this is advantage.
L58 -- I don't understand what you mean when you write, "It impedes mapping of keypoint locations from different perspectives into a common coordinate system."
L59-60 -- there is actually an ideal set of keypoint locations -- skeletal joints 
L107 -- "the more recent works" are actually older than some of the ones you cite in the previous sentence

Relatedly, you spend a lot of the intro saying how bad it is to use keypoints for behavioral analysis, but then go on to use keypoints for your benchmark action recognition results. What am I missing?

Please provide a clear breakdown of how much of your dataset video time is the animals engaged with the puzzle. What is your definition of "playtime"? I would prefer if these data were in the table and not in a ring/pie chart that is harder to read. 

How precise is your keypoint tracking (3D error in mm)? How many keypoints were tracked exactly? What tracking method did you use? What method/model did you use to go from keypoints to frame labels in your benchmarking? There is a lot of missing detail that is required of a datasets / benchmarks paper that the authors must provide for the work to be useful to others.

Similarly, as a dataset/benchmark paper, it is standard to show results from several different methods, or at least some internal comparisons over different model configurations/hyperparamters.

The authors have had the opportunity to address reviewer TrHr’s well-articulated follow-up response regarding the need for additional experiments (a concern I also share), but have not done so. Also, simple suggestions made by TrHr to clean up Table 1 appear to have been ignored.
The authors stated that Appendix A.2 contained 2D tracking performance metrics, but these measures are not there.
As the authors are using 3D keypoints for their analyses, their error metrics should really be in 3D, not in 2D.
The authors highlight multiple times that they provide 33% more video than any existing public mouse dataset. But this is only because they multiply their hours by the number of camera perspectives, which seems contrived. Taken to an extreme, what if someone used 1000 cameras and recorded only 10 minutes of behavior total. Is it meaningful to say this would be the largest dataset of mouse behavior? To me, the more important metric is the amount of animal behavior recorded (independent of perspective count). If anything, the social datasets should get another multiplier x2 to make it total mouse hours in the datasets (which would then make CalMS21 and CRIM13 larger than lockbox).
‘Intelligent’ behavior is a loaded and controversial term. Social interactions certainly require intelligence, and they also involve interactions with other entities in the environment.
Social datasets also have interaction behavior labels, and they introduce techniques for identifying behaviors that involve interactions with their environment. So I disagree with the statement that existing methods for behavioral identification “extract behavioral primitives of a mouse in isolation, rather than interactions with its environment as we do here.”

### Questions
A few things in the introduction that would be good to clarify in the text.

L55 -- you say that it is a disadvantage that poses are low dimensional. But there are many scenarios where this is advantage.
L58 -- I don't understand what you mean when you write, "It impedes mapping of keypoint locations from different perspectives into a common coordinate system."
L59-60 -- there is actually an ideal set of keypoint locations -- skeletal joints 
L107 -- "the more recent works" are actually older than some of the ones you cite in the previous sentence

Relatedly, you spend a lot of the intro saying how bad it is to use keypoints for behavioral analysis, but then go on to use keypoints for your benchmark action recognition results. What am I missing?

Please provide a clear breakdown of how much of your dataset video time is the animals engaged with the puzzle. What is your definition of "playtime"? I would prefer if these data were in the table and not in a ring/pie chart that is harder to read. 

How precise is your keypoint tracking (3D error in mm)? How many keypoints were tracked exactly? What tracking method did you use? What method/model did you use to go from keypoints to frame labels in your benchmarking? There is a lot of missing detail that is required of a datasets / benchmarks paper that the authors must provide for the work to be useful to others.

Similarly, as a dataset/benchmark paper, it is standard to show results from several different methods, or at least some internal comparisons over different model configurations/hyperparamters.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors propose a novel dataset, the _Mouse Lockbox Dataset_, which includes videos of individual mice dealing with mechanical puzzles named lockboxes. While existing datasets mainly target mice's social or common behaviors, the aim of the proposed dataset is to provide a useful resource for studying single-agent intelligent behaviors.
The paper describes with great detail both the setup used by the authors to record it and the procedure they established to annotate the (13% of the) dataset. The human-annotated labels are also compared with a benchmark automatic method, which relies on the poses of the mice as extracted with DeepLabCut. In particular, the authors compare the human-human agreement on the labels with the one obtained by comparing the human annotator and the automatic method performance.

### Strengths
1. The paper is clear and well-written, reporting several important details on the dataset generation process. 
2. The dataset represents an interesting source for computational ethology to study the mice's behavior in controlled environments when dealing with mechanical problem-solving.
3. The ~13% of the dataset is annotated with several features that can be leveraged to effectively delve into the mice's behavior.
4. The related work section clearly reports and compares the proposed dataset with the most important datasets in rodent computational ethology literature.

### Weaknesses
1. While the proposed dataset represents a novel source for studying mice behavior, the authors lack a proper experiment to showcase the relevance of their contribution. Benchmarking an automatic method against the human annotators reinforces the idea of a high-quality dataset but does not deliver to a non-ethologist reader the idea of how to use the  _Mouse Lockbox Dataset_.
2. To complete section 2, the authors could report a table comparing their proposed dataset with the available literature described therein.
3. The method used for benchmarking is not reported in the paper, although it is cited in the introduction. To help the reader understand the importance of this baseline, the authors should introduce it in its dedicated section, reporting at least some high-level details about the structure of this baseline.
4. The introduction is fragmented (with several paragraphs) and does not focus enough on the paper's contributions. In particular, the section describes recent advancements and methods in computational ethology well, but only the last two paragraphs describe the content of the proposed paper.
5. In general, the paper would greatly benefit from introducing and evaluating some methods that can be used on the _Mouse Lockbox Dataset_ to provide a reference for future users and encourage research with it.

### Questions
1. Will the key-point tracking results be released with the _Mouse Lockbox Dataset_? In the conclusive section, the authors claim, "(...) we are convinced that approaches beyond keypoint (pose) tracking, e.g., representations learnt without any or under self-supervision, are crucial to future advancements in neuroscience.", however when dealing with metric tasks, e.g., estimating the distance of the mouse from the lockbox, keypoint data represent an important piece of information. Also, to qualitatively assess the baseline performance, adding an image of the key points extracted by the baseline would be interesting.

### Soundness
3

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
The paper introduces a novel video dataset of individual mice interacting with complex mechanical lockbox puzzles, labeled as the "Mouse Lockbox Dataset." It provides a significant contribution to computational neuroethology, presenting over 110 hours of video data capturing intricate, non-social behaviors. The dataset uniquely includes multi-perspective recordings, human-annotated action labels for a subset of videos, and benchmark results utilizing a keypoint-based action classification method. This work aims to support machine learning advancements in behavioral action classification, particularly in fine-grained tasks such as object manipulation.

### Strengths
1. This dataset addresses a crucial gap in animal behavior research by focusing on complex, single-agent interactions in mice—particularly rare for capturing intricate, non-social behaviors.
2. Its scale and detail are impressive, with over 110 hours of footage from multiple angles. The multi-perspective setup and extensive annotations make it a highly valuable resource for training and evaluating behavior recognition models.
3. The inclusion of a keypoint-based action classification benchmark is a well-considered addition. It establishes a standard for future comparisons and highlights the strengths of current methods (e.g., proximity detection) as well as their limitations (e.g., recognizing fine-grained actions).
4. The authors provide a detailed methodology for creating the dataset, which supports reproducibility and helps ensure the reliability of the process.

### Weaknesses
1. Although this dataset is a valuable resource for behavior recognition, the paper lacks clear examples of specific use cases and potential research problems it could address. The absence of concrete applications or suggested research directions may limit its utility as an inspiration for future work. Providing examples of problems or experimental scenarios where this dataset could be useful would strengthen its research impact and relevance. For instance, the paper could elaborate on how the dataset could be used to study the learning curves of mice as they interact with the lockboxes, or how the fine-grained action labels could be used to analyze the strategies employed by different mice. The current presentation leaves the reader to imagine these applications, which weakens the impact of the work.
2. The pseudo-synchronization of the multi-camera setup presents a minor challenge for users needing precise 3D reconstructions. While the misalignment is slight, it may still affect analyses requiring high precision. Specifically, the temporal offset of 1.39 ± 1.5 frames could introduce significant errors when attempting to triangulate the position of the mouse or its limbs across multiple views, especially during rapid movements. This limitation should be more thoroughly discussed, perhaps with an analysis of the potential impact on 3D pose estimation accuracy.
3. Certain actions, such as biting, have lower annotator agreement, indicating challenges in reliably annotating these behaviors. This suggests that alternative or more standardized annotation methods may be necessary to improve reliability. The paper should explore the reasons for this lower agreement, such as the subtlety of the action or the potential for occlusion, and suggest ways to mitigate these issues in future annotation efforts. For example, using a frame-by-frame annotation approach with slow-motion review might improve the consistency of labeling biting actions.

### Questions
1. Could you clarify whether alternative pose-tracking methods were considered, particularly to improve the accuracy of detecting fine-grained actions like biting?
2. Is there a plan to expand the dataset with additional annotated videos, or are any tools being developed to help automate or verify annotation accuracy for challenging actions?
3. Given the temporal desynchronization in the multi-perspective recordings, have you considered any post-processing or alignment correction methods to reduce this effect?

### Soundness
3

### Presentation
2

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
The paper introduces a new dataset in the field of computational ethology. It focuses on creating various scenarios where mouse behaviour and actions are recorded while it tries to solve complex mechanical lockbox opening problems in return for treats. The novelty of the paper lies with the fact that existing datasets in this topic focuses only on problems which are not sufficiently complex or are concerned with studying social behaviour of animals.

### Strengths
•	The dataset has over 117 hours of videos of mice behaviour doing complex tasks. This multi-perspective video data is novel and crucial to enable the development of advance methods in the field of neuroscience. 
•	Action based labelling is very detailed, providing annotations at sub-second intervals.
•	The authors are very transparent in how they gathered the data and in compliance of local laws regarding to animal research. 
•	Human annotation is provided by the authors with special care taken to ensure that there is no leakage between the labelled and unlabelled set by keeping the mouses separate for labelled set. 
•	The human annotators followed a specific set of ethograms which makes the process objective in nature and lowers the possibility of disagreement.
•	The authors provide detailed statistics of their dataset

### Weaknesses
•	Labelled data provided is very limited and represents only 13% of the total available data. More annotated data, particularly across a wider range of behavioral interactions, would significantly enhance the dataset's utility for supervised learning tasks. The current amount may restrict the ability to train robust models capable of generalizing to unseen behaviors.
•	The dataset focuses exclusively on female mice, and the reasoning behind this is not explained, nor do the authors cite any papers which justify this choice. This lack of diversity in the subjects could introduce a significant bias, limiting the generalizability of any models trained on this data to the broader population of mice, which includes both sexes. The absence of male subjects prevents the study of potential sex-specific behavioral differences.
•	There is an uneven distribution between playtime action labels. This imbalance could lead to models that are biased towards the more frequent actions, while underperforming on less common but potentially important behaviors. If this cannot be made closer to each other, the authors should mention why it is so and provide a detailed analysis of the potential impact of this imbalance on model training and evaluation.
•	The dataset is provided in grayscale. While this is not a major weakness, the conversion to grayscale discards potentially valuable color information that could be relevant for certain analyses. RGB images could provide additional cues, such as subtle changes in skin tone or fur color, which might correlate with specific behaviors or physiological states.
•	The authors do not provide camera homography information of the cameras involved. This omission makes it difficult to perform accurate 3D reconstruction of the mouse's movements and interactions with the environment, limiting the potential for detailed spatial analysis.

### Questions
•	It would be great if the authors provided a baseline method on a task with their dataset.
•	A data dictionary of the labels as well as a getting started notebook was not provided. These would greatly increase the ease of use of the dataset.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper collected a multi-perspective video dataset of individual mice solving complex mechanical puzzles. This paper also provided the human-annotated labels, i.e., the proximity between a mouse and a mechanism. The authors give detailed statistics of playtime shares per lockbox.

### Strengths
1. This paper collected a large-scale video dataset of individual mice solving complex mechanical puzzles. 
2. This paper is well-organized and easy to read.
3. This paper provides a comprehensive review of relevant work.

### Weaknesses
1. This paper only collected a new dataset and ignored benchmark methods for recognizing mouse actions.
2. The comparison between the dataset collected in this paper and previous datasets is unclear. The author can provide a summary table to illustrate the differences from previous work.
3. There is no baseline or proposed method regarding the behavior recognition of mice.

### Questions
1. What pose keypoint definitions were used in this work? Will different key point definitions affect recognition?
2. Are all the mice in the dataset presented in this paper under normal light conditions?
3. Does the hunger state of mice affect their ability to solve mechanical puzzles?

### Soundness
2

### Presentation
2

### Contribution
2
