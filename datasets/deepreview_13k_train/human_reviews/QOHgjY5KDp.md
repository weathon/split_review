# Aligning Human Motion Generation with Human Perceptions

- Decision: Accept
- Scores: 6, 8, 8, 6

## Abstract
\renewcommand{\thefootnote}{\fnsymbol{footnote}}
\setcounter{footnote}{3}

Human motion generation is a critical task with a wide range of applications. Achieving high realism in generated motions requires naturalness, smoothness, and plausibility. Despite rapid advancements in the field, current generation methods often fall short of these goals. Furthermore, existing evaluation metrics typically rely on ground-truth-based errors, simple heuristics, or distribution distances, which do not align well with human perceptions of motion quality.
In this work, we propose a data-driven approach to bridge this gap by introducing a large-scale human perceptual evaluation dataset, \dataset, and a human motion critic model, \model, that capture human perceptual preferences. Our critic model offers a more accurate metric for assessing motion quality and could be readily integrated into the motion generation pipeline to enhance generation quality. Extensive experiments demonstrate the effectiveness of our approach in both evaluating and improving the quality of generated human motions by aligning with human perceptions. Code and data are publicly available at \url{https://motioncritic.io/}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a data-driven approach to align human motion generation with human perceptions. It introduces a large-scale dataset MotionPercept and a human motion critic model MotionCritic. The main contributions include providing a more accurate metric for motion quality assessment and showing that the critic model can enhance motion generation quality.

### Strengths
（1） The use of a large-scale human-annotated dataset and a critic model for automatic evaluation to align motion generation quality with human perceptions is a significant step forward.
（2） The experimental design is comprehensive. It evaluates the MotionCritic model on different data distributions and shows its generalization ability. Also, it tests the model as a training supervision signal and analyzes its impact on motion generation quality.

### Weaknesses
The human preference annotation lacks consideration for the diversity of motion.

 The critic model is essentially just a discriminator. The statement that it ''Utilizes a critic model to fine-tune the motion generation model in a more flexible, unconstrained manner, which does not hurt multimodality '' is not convincing. This statement does not provide any meaningful insight.

Even though each text has only one preference annotation, the diversity in this paper is primarily maintained by the presence of many similar texts from a data-driven perspective. So, as long as there are many annotations, similar texts correspond to a variety of human-preferred motions.

### Questions
(1) Why not use the latest models, but MDM and FLAME released in 2022? 

(2)Since currently, another two paradigms Noise De-masking and GPT-like Auto-regressive model show their potentials for motion generation task, how could this method of motion generation with critic model supervision be general to these methods?

(3) Why the step sampling range set as [700,900] in Sec 5.1? Is there any experiment support this setting, because I think from 700 - 900 step to get x0 directly results in motion with more artifacts, it might be help for those motion with obvious errors, but if you want to improve the motion quality use critic supervision as post-training, maybe it doesn't make much sense. If I am wrong, please explain your thoughts with some proofs. 

BTW, I intially wanted to give 7 out of 10, but there is not this option. If authors can solve my concerns, I will raise the score.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This work introduces MotionPercept, a large-scale synthetic human motion dataset which contains human-ranked synthetic human motion generations, and MotionCritic, a model learned on MotionPercept. MotionCritic can be utilized to evaluate motion quality but also as an additional loss for motion quality. 
The authors show that MotionCritic follows human perception closer than existing evaluation metrics and can even be used to find outliers in existing human motion datasets.

### Strengths
This paper addresses a common problem in generative motion synthesis: how to evaluate the motion quality of a generated sequence? In contrast to the often utilized FID score MotionCrititic operates on a per-sequence base, which allows for a much more granular evaluation.

### Weaknesses
One major concern of the motion critic is its quality ceiling: MotionPercept is highly dependent on the generative models that produces the motion, so in turn MotionCritic is highly dependent on those generative models as well. That means that, for the model, the best possible motion is the best generative model of MotionPerecpt, potentially limiting the usefulness of the critic once generative models produce significantly better motion than has been produced for MotionPercept. Could the authors comment if there is a way to remedy this or if they have considered this a problem?

Another concern would be: how does MotionCritic behave when provided with unseen motion modalities? I.e. lets say MotionCritic was not trained with dancing motion but is now tasked to judge the motion quality of dancing: do the authors expect MotionCritic to continue being reliable or would retraining be required?

Why did the authors choose 2.3s sequence lengths (60 frames @24Hz)? This seems very short for complex motion, i.e. a person “sitting down”. Were complex motions discarded for the dataset generation? Otherwise, only the motion initiation would have been recorded.
Did the authors observe that the model tends to start from the same pose or position, i.e. a T-Pose? This might limit the application of MotionCiritic as it could favor motions and poses that are more similar to the “initialization” pose/motion.

How can MotionCritic be applied to sequences of different lengths, i.e. [A] How can MotionCritic deal with sequences shorter than 60 frames and how does it perform ?

How is the input motion to MotionCritic normalized? Is the first frame translation at the origin? How is the global rotation set up? Are the first frame rotations set to the same rotation for each generation?

[B] How can MotionCritic be applied to sequences far longer than 60 frames, i.e. 1000 frames?

Table 1: NDMS and NPSS are flipped.

The evaluation methods against which motion critic is compared should be discussed in the related work, and not just in Table 1.

The authors should describe in how they apply the other metrics that they compare against, i.e. how they normalize the data, what kind of data representation/hyperparameters they are using.

### Questions
-

### Soundness
2

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
4

### Summary
The paper introduces a novel evaluation metric for 3D human motion that aligns more closely with high-level human perception. A large-scale data annotation effort is conducted by asking users to select the highest quality motion from a set of samples. To capture human preferences, the paper proposes training a critic model that learns to assign a quality score to each motion sample. A comprehensive analysis compares the proposed critic model with commonly used evaluation metrics from prior work, revealing deficiencies in these established metrics for aligning with human perception, while the proposed critic model shows much higher alignment. Additionally, the paper presents a fine-tuning approach for improving the motion quality of pre-trained motion diffusion models by leveraging the proposed critic model.

### Strengths
The paper addresses a fundamental problem in human motion generation and is both well-written and well-motivated. I appreciate the authors' meticulous effort in their work.

Annotating a large sample set and training a critic model on this data is a clever idea. Additionally, the thorough analysis and comparisons effectively demonstrate the proposed method's impact. While the human motion modeling field has converged on a set of complementary metrics for quality assessment, these metrics still fall short of aligning with human perception, as shown in this paper. The proposed MotionCritic takes a more direct approach to addressing this issue. I believe this work is highly valuable for the community, contributing both to the research on evaluation and analysis of future human motion synthesis research. I also hope it will serve as an alternative to the counterintuitive FID score.

### Weaknesses
A sensitivity analysis could be included to assess the robustness and smoothness (e.g., Lipschitz continuity) of the critic model. For instance, how would the critic model respond if a pose is slightly perturbed, either randomly or in a structured way by rotating a joint beyond its limits?

By design, certain artifacts—such as foot-floor penetration, person-ground contact, etc.—might be missed, as the critic model lacks information needed to detect these issues (e.g., it only uses rotations and root translation as inputs). What are the authors' thoughts on this limitation?

Another potential concern is the reliance on a single model (e.g., MDM) for generating data used in the annotations. Although the paper presents results with an additional model (e.g., FLAME) to demonstrate generalization, it may be beneficial to curate an annotation set from various models and architectures to mitigate possible biases.

### Questions
1- This aligns with my comment on sensitivity analysis. The paper addresses only fine-tuning but does not consider an end-to-end training scenario. Theoretically, the critic model could also be used to train a motion model from scratch. I mention this because, even in the MDM fine-tuning experiment, the critic term is tightly controlled (with a low learning rate, low critic weight, and high KL-term weight). Is this due to difficulties in training with the critic term, possibly because of a non-smooth energy landscape?

2- Locomotion sequences with significant foot sliding receive high critic scores. Could this be due to a bias in the annotated samples, given that MDM generates many sequences with foot sliding? Have the authors considered training the critic with ground-truth samples as well? This should be straightforward, as ground-truth samples could always be preferred over synthetic ones.

3- Are the critic scores for two different samples comparable? I assume it isn’t a distance function. Could the authors comment on this?

4- This is minor but it would be great to have a comparison against a log-likelihood metric such as a normalizing flow.

### Soundness
3

### Presentation
4

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
This paper addresses the challenges in evaluating and improving human motion generation by proposing a human-aligned evaluation approach. The authors introduce MotionPercept, a large-scale dataset containing over 52,000 human preference annotations for generated motions, which provides a foundation for understanding motion quality from a human perspective. They also develop MotionCritic, a model trained on MotionPercept, which accurately predicts human-perceived motion quality and surpasses traditional metrics in alignment with human preferences. MotionCritic can be easily integrated into existing generation pipelines, where it functions as a supervision signal to improve motion quality with minimal fine-tuning.

### Strengths
A large amount of human preference annotation work has been done for text-to-motion, and a sizable dataset has been provided, which is beneficial to the community.

### Weaknesses
The human preference annotation lacks consideration for the diversity of motion.

### Questions
1. There is inherent diversity in the motion generated from text-to-motion. Regarding the fine-tuning comparisons in the supplementary materials, I observe that the generated motions generally align with semantic accuracy, and the physical accuracy appears to improve over time. Could it be that the critic score primarily reflects physical correctness? What I’d like to see is a visualization that compares multiple generated motions for a single text prompt, showing the distribution of critic scores (with five or more samples), as well as how motion diversity changes before and after fine-tuning. This result would better demonstrate the effectiveness of your proposed method and its balance in generating diverse outputs. 

2. When the text is simple, such as "run" or "punching," the corresponding motions should naturally be diverse. However, based on the annotation process provided in the HTML document, it seems that only the best out of four generated motions is selected, which shows no particular consideration for diversity. This raises the question of how Multimodality would improve after fine-tuning. [1] aligns motion generation with human preference. They only select the best result, which significantly reduces diversity (MModality, the diversity of motion generated for one text description). A discussion with [1] would also be beneficial.

3. The annotation of human preference in this paper for motion follows the same process as for images. I see that many useful insights (as metrics and supervision) also resemble those used in image-based tasks. Since motion data is a unique form of 3D data, differing greatly from 2D image data, are there any distinct insights here?

4. The annotation of human preference in this paper for motion follows the same process as for images. I also see that many insights (as metrics and supervision) also the same as image-based tasks [2,3]. Since motion data is a unique form of 3D data, differing greatly from 2D image data, are there any distinct insights here?

5. In Table 1, where MDM’s generated results are evaluated with different metrics, why does the metric with higher Acc is better?

Reference:

[1] HuTuMotion: Human-Tuned Latent Motion Diffusion Models with Minimal Feedback.   
[2] ImageReward: Learning and Evaluating Human Preferences for Text-to-Image Generation.  
[3] Better Aligning Text-to-Image Models with Human Preference.

### Soundness
2

### Presentation
2

### Contribution
2
