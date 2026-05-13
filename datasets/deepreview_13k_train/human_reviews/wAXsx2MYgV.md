# Modeling dynamic social vision highlights gaps between deep learning and humans

- Decision: Accept
- Scores: 6, 8, 8, 6

## Abstract
Deep learning models trained on computer vision tasks are widely considered the most successful models of human vision to date. The majority of work that supports this idea evaluates how accurately these models predict behavior and brain responses to static images of objects and scenes. Real-world vision, however, is highly dynamic, and far less work has evaluated deep learning models on human responses to moving stimuli, especially those that involve more complicated, higher-order phenomena like social interactions. Here, we extend a dataset of natural videos depicting complex multi-agent interactions by collecting human-annotated sentence captions for each video, and we benchmark 350+ image, video, and language models on behavior and neural responses to the videos. As in prior work, we find that many vision models reach the noise ceiling in predicting visual scene features and responses along the ventral visual stream (often considered the primary neural substrate of object and scene recognition). In contrast, vision models poorly predict human action and social interaction ratings and neural responses in the lateral stream (a neural pathway theorized to specialize in dynamic, social vision), though video models show a striking advantage in predicting mid-level lateral stream regions. Language models (given human sentence captions of the videos) predict action and social ratings better than image and video models, but perform poorly at predicting neural responses in the lateral stream. Together, these results identify a major gap in AI's ability to match human social vision and provide insights to guide future model development for dynamic, natural contexts.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In this paper, the author extends a dataset of natural videos describing human action interactions by providing human-annotated sentences for each video and investigates the limitations of over 350+ models to predict human behavioral ratings and neural responses to dynamic social scenes. It concludes that language models predict action and social ratings better than image and video models but perform poorly at predicting neural responses in the lateral stream and provides insights into how well current AI systems replicate human social vision. More importantly, the author highlights the gap in current models' ability to understand dynamic social interactions and suggests potential directions.

### Strengths
•	The paper’s approach is innovative in building on the NeuroAI benchmarking with dynamic visual responses rather than using static scene responses, which are commonly evaluated by current image model. It’s the first investigation of benchmarking many models in response to naturalistic videos of human actions.

•	The paper gives a comprehensive model evaluation experiments conducting with this dataset. Spanning from video, language, image models over 350+, including a variety of architectures and objectives.

•	The paper is fully public with all data, code, model accessible. Further, it provides an interesting direction that Human-aligned DNNs may be a promising direction for dynamic social perception, and suggests that developing models that can handle relational and temporal elements essential for social scene understanding.

### Weaknesses
•	Limited Coverage or advanced video and language models: Although the dataset has been tested in 350+ models. The majority of them are obsoleted and cannot fully present the overall performance on the state-of-the-art image, video, and language models, like MViT, Co-DETR, DINO, GPT4o, LLAVA, Llama, etc. The most recent model on the paper’s list is up to 2021. This raises concerns about the generalizability of the findings to current models, particularly given the rapid advancements in the field. The lack of more recent models, especially those employing transformer architectures and large-scale pretraining, limits the conclusions that can be drawn about the current state of AI's ability to understand social interactions.

•	The author conducts experiments on a dataset, consisting of 250 3-sec videos, which is relatively small and less representative for training and evaluating deep learning models for making a significant claim on social action recognition. The data limitation might reduce the generalizability of getting conclusions when trading this complex multi-agent interactions task. The dataset's limited size and diversity may not capture the full range of human social interactions, potentially leading to biased or overly specific conclusions. The 3-second duration of the videos may also be insufficient to capture the temporal dynamics of more complex social interactions, further limiting the generalizability of the findings.

•	While the paper make a claim that language models are successful in predicting behavioral response but not in neural responses since providing language captions is insufficient for achieving neural alignment, it encourages the society to make a better connection between neural responses and models with a more well-designed approach. Instead, the conduct of experiments are insufficient in pinpointing precise architectural or training factors that contribute to performance differences by given task. The paper does not sufficiently explore the specific architectural or training factors that contribute to the observed performance differences between models. For example, the impact of different loss functions, regularization techniques, or pretraining strategies on the models' ability to predict human behavioral and neural responses is not investigated. This lack of detailed analysis limits the practical implications of the findings for model development.

### Questions
Questions are asked in the weakness section.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The primary contribution of this work is an analysis of 350 models over an existing dataset of social actions. The labels range from user ratings to fMRI images for brain regions engaged in the watching of videos of social action. The authors find that networks trained over images outperform language/video modalities.

### Strengths
1) Action datasets contain both physical and social actions, and are not focused on the exclusive modeling of either action. Exploring models trained over social actions exclusively provides very valuable insights on the difficulty of this domain of action.
2) The evaluation is very broad - 350 models is very impressive. The claims in the discussion are well supported.

### Weaknesses
1) The size of the dataset is very small (200 training videos), and the results are definitely impacted by this. Models trained over video datasets in particular must be large due to the variation over the time dimension. The models (and modalities) that perform well might largely be because of the size of the dataset.
2) Audio as a modality is missing, but I would argue is just as valuable as the sequence of images alone across many of the subjects (e.g. valence, arousal). Audio provides less benefit in action datasets focused on physical actions, but might be just as important as the visual modality w.r.t. social actions.
3) There is a lack of discussion around pre-training of the different models. This bears more importance than the model architecture (CNNs vs Transformers) especially due to the small size of the dataset. The video models may or may not be trained over datasets that include social actions (like Kinetics).

### Questions
1) I am unfamiliar with the usage of fMRIs in machine learning. But I imagine the variance from individual to individual must cause difficulties in predicting brain responses. Does it not make more sense to condition fMRI prediction on the baseline fMRI readings before the video viewing? Is the text or video input enough?
2) Figure 7 and Figure 8 mention image-language models being evaluated - but to my understanding, all models only take one modality. Are there models that take both images and language?
3) Action datasets deal with label subjectivity - is there any disagreement across annotators concerning the dataset being trained over? I imagine this is particularly a problem in the domain of social action.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
1. The authors benchmark hundreds of image, video and language models for behavior ratings and neural responses based on human social videos and their captions.
2. The authors compare these models based on their predictions of the behavior rating and neural responses.
3. The authors present several conclusion about the compared models and highlight gaps in their alignment.

### Strengths
1. The authors extend a human social video dataset with human annotated text descriptions.
2. The authors benchmark 350 image, video and language models for behavior rating and neural response prediction.
3. The authors highlight gaps in alignment of these models and compare their performance along different axes like architecture, training objective etc.

### Weaknesses
1. Just mentioning broad non-exhaustive categories like "self/category supervision, multi-modal and convolution vs transformer" is not a systematic approach to model selection. The authors should first select dimensions of model categorisation they want to compare like supervision type, generative or discriminative, model size, modality etc. and then choose models representing each type. The entire process needs to be detailed to make sure there is no bias in model selection that might affect conclusions downstream. The authors should provide their detailed model selection method.

2. While the authors benchmark several vision models, the vast majority of them are trained for image classification. Models trained with other objectives like object detection (only 2 used as far as I can tell), segmentation (none used as far as i can tell), masked reconstruction (none used as far as i can tell) etc. should also be benchmarked. More generally, vision based models should be categorised based on the different objectives used to train them and compared to provide insights into how different training objectives affect performance/alignment.

3.  While there are several generative language models benchmarked, the vision language models are primarily discriminative. Generative vision models like diffusion based (like stable diffusion), GAN based (like VQ-GAN) and VAE (like VQ-VAE) based models should also be benchmarked for insights into the performance gap between generative and discriminative representations for both language and vision models.

4. The comparisons between the benchmarked models need to be fair in terms of the number of parameters. It looks like the authors have compared the models regardless of the size. The authors should investigate and report whether there exists trends between prediction performance and model size for insights into how model size affects representation quality/alignment.

### Questions
see weaknesses

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
Unlike previous neuroscience AI studies that focus on deep learning models' responses to static images, this paper examines models' responses to human social interactions in dynamic videos. The authors create a small benchmark and evaluate an impressive number of models (over 350 image, video, and language models) on this dataset. These comprehensive experimental results could offer valuable insights for researchers in this field.

### Strengths
- The relationship between AI models and the human brain is an important area of study.
- This paper presents a highly comprehensive benchmark for examining how AI models—spanning image, video, and language models—respond to social interactions compared to human brain responses in similar scenarios.
- The limitations and discussions offer valuable insights that can inform and guide future research developments.

### Weaknesses
 - The technical contribution is limited. While I understand the overall effort and workload invested in this paper, it does not address the question of how to develop a human-like AI model. The paper primarily serves as a large-scale empirical study, lacking a novel algorithmic or theoretical contribution that advances the field of human-like AI. The analysis focuses on evaluating existing models rather than proposing new architectures or learning mechanisms that could lead to more human-aligned AI.
- Questions regarding the evaluation method: Why is a linear mapping applied between the extracted features and human data, such as fMRI responses? The rationale or assumptions behind this choice of linear mapping are not clear to me. Furthermore, is it appropriate to apply the same linear mapping approach across all models, despite their significant differences? The use of a linear mapping, while common, may not capture the complex, non-linear relationships that could exist between model representations and neural activity. Applying the same linear transformation across diverse models, from simple image classifiers to complex video and language models, could obscure important differences in how these models represent social interactions. If the evaluation method is not well-justified, the overall efforts should be reassessed carefully.

### Questions
- Please include additional details about the experiments.
- It seems to remain unclear whether developing a human-aligned model would enhance existing AI models, why not test some social behavior tasks used in the computer vision community, such as the social interaction tasks in [Ego4D [CVPR2022]](https://arxiv.org/abs/2110.07058) ? (not required to conduct such experiments)

Moreover, given my limited expertise in this specific topic, I recommend that the significance of this paper be assessed by reviewers with specialized knowledge in this area.

### Soundness
3

### Presentation
2

### Contribution
3
