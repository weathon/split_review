# Social Reward: Evaluating and Enhancing Generative AI through Million-User Feedback from an Online Creative Community

- Decision: Accept
- Scores: 6, 8, 8, 5

## Abstract
\vspace{-0.3em}
Social reward as a form of community recognition provides a strong source of motivation for users of online platforms to engage and contribute with content. The recent progress of text-conditioned image synthesis has ushered in a collaborative era where AI empowers users to craft original visual artworks seeking community validation. Nevertheless, assessing these models in the context of collective community preference introduces distinct challenges. Existing evaluation methods predominantly center on limited size user studies guided by image quality and prompt alignment. This work pioneers a paradigm shift, unveiling \textbf{Social Reward} - an innovative reward modeling framework that leverages implicit feedback from social network users engaged in creative editing of generated images. We embark on an extensive journey of dataset curation and refinement, drawing from Picsart: an online visual creation and editing platform, yielding a \textbf{first million-user-scale} dataset of implicit human preferences for user-generated visual art named \textbf{Picsart Image-Social}. Our analysis exposes the shortcomings of current metrics in modeling community creative preference of text-to-image models' outputs, compelling us to introduce a novel predictive model explicitly tailored to address these limitations. Rigorous quantitative experiments and user study show that our Social Reward model aligns better with social popularity than existing metrics. Furthermore, we utilize Social Reward to fine-tune text-to-image models, yielding images that are more favored by not only Social Reward, but also other established metrics. These findings highlight the relevance and effectiveness of Social Reward in assessing community appreciation for AI-generated artworks, establishing a closer alignment with users' creative goals: creating popular visual art.
\vspace{-0.5em}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a groundbreaking approach by introducing the concept of utilizing social rewards within a reward modeling framework to assess and enhance generative AI systems. The authors collected data from Platform A and employed the frequency with which an image is reused for editing by other users as a performance metric. Notably, they have constructed a colossal dataset, known as the "PA Image-Social dataset", which collects feedback on the relationships between images and prompts, offering a valuable resource for the analysis of positive and unpopular image-prompts associations.

The study also includes a comprehensive evaluation of the Social Reward model, demonstrating its superiority over existing models in capturing community-level creative preferences. Furthermore, the authors conducted an evaluation showcasing the effectiveness of fine-tuning AI models with Social Reward, revealing performance improvements across multiple performance metrics. This innovative paper brings forth a promising avenue for the assessment and enhancement of generative AI, backed by meticulous research and empirical evidence.

### Strengths
Thanks for your interests in ICLR! Overall, this is an interesting paper on a topic which is of interest to ICLR Conference. It introduces an innovative set of metrics designed to gauge the intricate interplay between prompts and images, accompanied by the construction of an unprecedented million-user-scale dataset, offering invaluable insights into human preferences for user-generated visual art. The metrics, composed of five distinct factors, provide a robust framework for evaluating performance.

Additionally, the authors furnish a robust evaluation of the Social Reward model, including comprehensive comparisons with existing models and metrics. Their meticulous analysis strengthens the paper's standing in the field and underscores its potential to advance our understanding of generative AI.

### Weaknesses
The paper offers a comprehensive introduction to the metrics and evaluation methods; however, I am very curious about the PA Image-Social dataset and want to learn more about its details.

### Questions
I am curious about the data distribution within the collected dataset. It would be highly informative if the authors could provide insights into key aspects such as the percentage of popular images, the presence of influential users, and the overall engagement levels of individual users.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper advocates the importance of social rewards as a motivating factor for user engagement and content contribution on online platforms. It focuses on the co-creative process in text-conditioned image synthesis within online social networks, emphasizing the challenges of assessing models in the context of collective community preferences. The paper introduces a novel framework called "Social Reward" that leverages implicit feedback from users engaged in creative editing of generated images. This approach is supported by an extensive dataset and demonstrates improved alignment with social popularity compared to existing metrics.

### Strengths
The main strengths and innovations of this paper are:

(1)	The introduction of Social Reward, a novel reward modeling framework that leverages implicit feedback from social network users engaged in creative editing of generated images, to assess community appreciation of AI-generated artworks. To put their contributions in context, the authors discussed recent endeavors that propose modeling human preference by learning scoring functions from datasets consisting of human-annotated prompts paired with synthetic images.

(2)	The curation of a million-user-scale dataset of implicit human preferences for user-generated visuals by drawing from an anonymous online visual creation and editing platform, perpetually invigorated by a vibrant user community, where the feedback is drawn from individuals who actively engage with the images on the platform for editing purposes. It is used to demonstrate the distinctiveness of the Social Reward in comparison to those employed by existing solutions and to highlight the limitations of these solutions. 

(3)	The paper contributed to the field of T2I synthesis by introducing a new paradigm for evaluating the quality of AI-generated artworks that is more closely aligned with users' creative goals.  The rigorous quantitative experiments and user studies that show that the Social Reward model aligns better with social popularity than existing metrics. Social Reward can be used to fine-tune generative models to better align with creative preferences of the community.

Overall, this paper represents a nice contribution to the field of generative AI art and has the potential to improve the quality of AI-generated artworks by better aligning them with users' creative goals.

### Weaknesses
-	I failed to follow what the authors meant by referring to Pick-a-Pic as “relatively small scale of collected user preferences along with absence of ‘collective feedback’”. Please explain why.

-	In Figure 7, it is hard to tell why Social Reward fine-tuning actually improves, as the examples might just be cherry picked and observing them doesn’t give me the intuition what Social Reward essentially improves or corrects any pattern consistently. Table 6 numbers are also marginally close to each other. Could the authors elaborate some critical win cases or “take home points”, that can be consistently observed after using Social Reward fine-tuning?

-	The study relies entirely on self-report survey measures. Self-report can be subject to biases like social desirability bias where participants answer in a way they feel is more socially acceptable rather than reflecting their true thoughts and behaviors. How the authors think their data curation was/was not affected by the social bias?

-	(Minor) For robust user study, as a cross-sectional study collecting data at only one time point, it cannot determine causation or the direction of effects. A longitudinal design collecting multiple waves of data over time would allow for stronger conclusions about how the variables influence each other over time.

### Questions
Please check the weakness part. The first three points are more crucial for me.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a novel reward modeling framework, called Social Reward, for assessing community appreciation of AI-generated artworks. The framework leverages implicit feedback from social network users engaged in creative editing of generated images, rather than relying on limited size user studies guided by image quality and alignment with prompts. 

The authors curate a million-user-scale dataset of implicit human preferences for user-generated visuals by drawing from an anonymous online visual creation and editing platform. Rigorous quantitative experiments and user studies show that the Social Reward model aligns better with social popularity than existing metrics.

### Strengths
The paper starts with an interesting insight. Social reward is a form of community recognition that provides a strong source of motivation for users of online platforms to actively engage and contribute with content to accumulate peers' approval. Positive social feedback are essential for maintaining social cohesion and individual well-being. On online social platforms, users seek satisfaction via accumulation of their network’s peers engagement with shared content in the form of likes, views, etc. Therefore, social reward can motivate users to engage with online platforms by providing them with a sense of validation and recognition from their peers.

The authors’ analysis exposes the shortcomings of current metrics in modeling community creative preference of text-to-image models’ outputs. Many quantitative experiments and user study show that Social Reward model aligns better with social popularity than existing metrics.

The dataset curation process for the million-user-scale dataset of implicit human preferences for user-generated visuals involved drawing from an anonymous online visual creation and editing platform. The dataset was curated by leveraging collective feedback, which implies multiple users’ editing choices for the given content item, as a cleaning mechanism of organic implicit user behavior. A number of other data collection techniques had been utilized for addressing such biases as caption bias, content exposure time, and user follower base biases. Each positive and negative instance within the PA Image-Social dataset is a product of collective, independent, implicit voting by user community. I think this dataset would be valuable for many follow-up analyses.

### Weaknesses
As one limitation, this paper does not aim to introduce a specific new RLHF algorithm as a primary focus. Instead, its main emphasis lies on exploring a novel aspect of data-centric reward modeling, which has previously received little attention. The paper introduces a comprehensive end-to-end solution, and it's important to acknowledge that each component of this solution builds upon prior ideas and engineering techniques. However, it's worth noting that the integration of these components into a cohesive whole represents a significant and commendable achievement.



### Questions
How was user data right and privacy protected in your data curation process? That was not mentioned anywhere in paper.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes to create a new dataset of implicit human creative preferences for user-generated visual art. The dataset is created based on an online visual creation and editing platform and millions of user feedback from the online social community are collected to evaluate the quality of generated images. Due to the uniqueness of this dataset in modeling content creativity, the authors also proposed a new social reward metric to evaluate image quality. The social reward metric is further used to fine-turn the text-to-image generation model.

### Strengths
1.	Previous text-to-image generation human preference datasets mainly focus on general fidelity and text-image alignment, ignoring content creativity. This paper created a new dataset to fill this gap. 
2.	To evaluate the creativity of the image, the authors utilize the number of times an image has been reused for editing purposes by other users, which is reasonable and more aligned with real users. The number of collected feedbacks is also in the million scale.
3.	The authors also demonstrate the proposed social reward metric's effectiveness in fine-turning the text-to-image generation model.

### Weaknesses
1.	In the proposed social reward metric, the authors mainly focus on the creation-related metric such as the number of times an image has been reused for editing purposes by other users. However, user comments, views or likes are also important dimensions. It’s better to show whether a higher value of the proposed metric in this paper will induce a lower or higher value of the traditional metrics.
2.	The social reward metric in this paper is optimized using the triplet loss. As a dataset and benchmark paper, it’s recommended to compare with other existing contrastive learning methods such as NCE or infoNCE.
3.	The constructed dataset consists of prompt, positive image, and negative image. It’s unclear what’s the specific threshold to decide the positive and negative image.

### Questions
See the Weaknesses for questions.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
