# A Large-scale Dataset with Behavior, Attributes, and Content of Mobile Short-video Platform

- Decision: Reject
- Avg Score: 4.50
- Scores: 6, 6, 5, 1

## Abstract
Short-video platforms show an increasing impact on people’s daily life nowadays, with billions of active users spending plenty of time each day. The interactions between users and online platforms give rise to many scientific problems across computational social science and artificial intelligence. However, despite the rapid development of short-video platforms, currently there are serious shortcomings in existing relevant datasets on three aspects: inadequate user-video feedback, limited user attributes and lack of video content. To address these problems, we provide a large-scale dataset with rich user behavior, attributes and video content from a real mobile short-video platform. This dataset covers 10,000 voluntary users and 153,561 videos, and we conduct three-fold technical validations of the dataset. First, we verify the richness of the behavior data including interaction frequency and feedback distribution. Second, we validate the wide coverage of user-side and video-side attribute data. Third, we confirm the representing ability of the content features. We believe the dataset could support the broad research community, including user modeling, social science, human behavior understanding, etc. Our dataset is available at this anonymous link: http://101.6.70.16:8080/.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this paper, a large-scale dataset with behavior, attributes, and content of mobile short-video platform is proposed. The proposed dataset includes 10,000 voluntary users and 153,561 videos. The authors perform three-fold technical validations of the dataset, focusing on the richness of behavior data (such as interaction frequency and feedback distribution), the extensive coverage of both user-side and video-side attribute data, and the representational capacity of the content features. This dataset aims to support a wide range of research areas, including but not limited to user modeling, social sciences, and understanding human behavior.

### Strengths
1. The paper is well organized and presented, which is easy to follow. 
2. The scale of the dataset is large, which can support the training of large models and promote the development of applications in different fields. It is good for the community. 
3. The paper provides a detailed introduction of the dataset, including the specific compositions of behavior data, attribute data and content data. 
4. The authors conduct statistical analysis of data distributions, interaction numbers, as well as the associations between behaviors and preferences.

### Weaknesses
1. The dataset proposed in the paper lacks testing in tasks of different research areas (such as user modeling, social sciences, and understanding human behavior) mentioned in the paper, which results in insufficient clarity regarding its practicality and applicability.
2. Different tasks and methods have not been tested on this dataset, resulting in an incomplete benchmark. This may lead to confusion regarding the use of the dataset due to the absence of reference benchmark results.
3. Visual examples of different data such as video, images, text, and audio of behavior, attribute, and content data should be given. Both the paper and the supplementary material do not provide sufficient visual instances. It is not good for readers.
4. There are some minor grammar errors and typos.

### Questions
See weakness.

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
The paper presents a new collected dataset for user's interaction with the social media platform, TikTok. The dataset contains data about the videos (raw pixels), video's metadata, user's metadata, and multiple user's explicit and implicit interactions with each of the videos. The data is mostly (if not entirely) covering Chinese users from multiple demographics (data which is also provided). 
This dataset is the first one to release all these information along with raw video (audio, frames, ASR) data, which can be useful for multiple applications. The value of the data lies on the fact that will be made publicly available, providing a step forward democratizing the study of recommendations algorithms and their implications.

### Strengths
The paper's main contribution is the data. The richness of the data collection and the fact that the authors have consent to use and distribute this data to the research community is a very valuable contribution for future studies on recommendation algorithms, biases in them and the potential societal impact that these might have. 

The authors provide several initial insights on the data that give an overview of the potential of it. 

The collection pipeline is also very valuable as it can serve for future datasets to follow the same protocol to enrich the data further to more diverse demographics.

### Weaknesses
 The paper has two main weaknesses that I would like the authors to discuss carefully:
1. Every dataset has biases. However, this one in particular has a very critical one which is the population that it focused on. In Figure 5d, it's clear that the users that appear in the dataset are mostly from China, which makes the dataset tailored to a single demographic population. Although, the data is still valuable, conclusions that will be made in the future using this data can be only applied to the Chinese population. I would like to know what to the authors and other reviewers think about this critical point.

2. Most of the data provided by the data is simply collected by how the users interact with the platform. However, there are a couple of design choices that were unclear to me:

     - There is no explanation on how the video categories I,II, and III were chosen. The authors mention that they are hierarchical, which sounds like a good idea. However, the is no explanation on how the hierarchies were chosen and how were the classes picked from the tags, titles, and content of the videos. How was this discretization of classes done for I? How was then the hierarchical structure form to have II and III?

    - It was not clear to me what is the "effective view" label, what does it try to convey and why is the threshold of 3 seconds picked?


Others:
although not a weakness I have a few recommendations to improve the presentation of the paper.

1. Whenever not sure about the gender of the referring person, it's better to use THEY as pronoun instead of saying he/she all the time. It also easier to read this way.
2. Figure 4 x axis should number of like**s** in plural.
3. Figure 4 caption can be further improved by stating that the data presented is per user not per video, it can be confusing if one reads the figure before reaching the paragraph in which it is mentioned.
4. Figure can be moves so they are closer to the place they are mentioned. Right now Figures 3 and 4, are like 2 to 3 pages away from the paragraph they are mentioned in. It would be better if authors manage to arrange them in a way that they are closer to the sections they belong to.

### Questions
1. What are the implications on the fact that most of the users from the dataset come from a single country? What are the benefits from it? What are the downsides of having so little diversity in terms of country of origin? Could the conclusions made with this data be extrapolated to other places? If not, what could be the solution for this?

2. What was the criteria to pick the classes for Category I?

3. What was then the Criteria to make the hierarchies from I to II and III?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a large-scale dataset derived from a mobile short-video platform. Compared to previous datasets, it expands the scope of user behavior data (including both explicit and implicit feedback), user attributes (covering demographics, geographic, and device-related information), and video content (including raw video files, visual features, and ASR transcripts). The paper provides a technical validation of the dataset, confirming the comprehensive nature of its behavioral data, broad attribute coverage, and representational strength of its content features.

### Strengths
1. The dataset includes raw videos, which is valuable as many video datasets lack this component today.
2. The dataset captures user actions and attributes from multiple perspectives, offering new insights into the relationship between user behavior and video content.

### Weaknesses
1. The dataset includes raw videos, which is valuable as many video datasets lack this component today.
2. The dataset captures user actions and attributes from multiple perspectives, offering new insights into the relationship between user behavior and video content.

1.  The link to the dataset seems to be broken, possibly due to a network issue on my end. Could you provide guidance on accessing it? I may consider raising the score if access is successful.
2. From a data perspective:Since the data originates from a single social media platform, user behavior is influenced by the platform’s 
    * recommendation algorithm. This introduces significant bias due to these recommendation effects.
    * The visual features were extracted using a 2016 image model, while more advanced models are now available that can extract features from video encodings. Thus, the extracted visual features may be insufficient.
3. From a validation perspective:
    * The conclusions presented in Section 3.1.2 lack depth and seem self-evident.
    * The paper lacks proof-of-concept experiments to demonstrate the dataset’s value in the proposed research areas, which somewhat diminishes the paper’s impact.
    * Most validations rely on statistical analyses, rather than truly testing the representational ability of the video data. Statistical data alone is insufficient to prove the dataset’s research value.
4. Overall, while the dataset provides fresh data and unique insights into user actions, the paper lacks experimental results demonstrating the dataset’s applicability across the various domains it proposes.

### Questions
see weakness

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
This paper introduces a rich dataset collected from a real mobile short-video platform, filling important gaps in data on user behavior, demographics, and video content. With information from 10,000 users and over 153,000 videos, it’s a valuable resource for researchers in social science and AI.

- The dataset captures over a million user interactions, covering both passive behaviors (like viewing time) and active actions (likes, comments, follows, shares, saves, and dislikes), which enables a deeper look into user interests and behaviors.
- It includes detailed demographic information, such as age, gender, city, city size, community type, and device price, allowing researchers to explore how different user groups engage with the platform.
- For video content, the dataset includes raw video files, visual features, and transcripts generated through speech-to-text, organized into primary, secondary, and tertiary categories for easy content analysis.
- Extensive validation ensures that the dataset accurately represents various user behaviors and demographics. Video content quality is confirmed through visual clustering techniques, which show clear distinctions among video types.
- This dataset stands out for its scale and depth, surpassing similar datasets like Kuaishou, REASONER, and MicroVideo-1.7M, and is ideal for studies on user modeling, recommendation systems, and topics like filter bubbles and user addiction.
- Designed to support diverse research areas, the dataset can be used to improve personalized recommendations, study fairness in algorithms, understand user engagement, and examine how recommendation systems influence information diversity and polarization.
- It’s publicly available and ethically compliant, with user and video identifiers anonymized, and all sensitive data handled carefully to protect privacy.

### Strengths
- The dataset integrates detailed user behavior logs, diverse user and video attributes, and raw video content, offering a comprehensive foundation for research across various fields. This thorough approach addresses gaps found in other datasets, making it a valuable resource for studies in computational social science, artificial intelligence, and algorithmic fairness.

- With the inclusion of raw video files alongside processed visual features and automatic speech recognition (ASR) text, the dataset enables deep video understanding and multimodal research, expanding analytical capabilities beyond what many other datasets support.

- Containing over one million interactions from 10,000 users across 153,000 videos, the dataset is robust, dependable, and well-suited for various analytical tasks. It provides in-depth demographic, geographical, and device-related data that supports research in recommendation systems, social science, and algorithmic fairness, while minimizing statistical biases.

- The dataset is structured with clarity, including detailed tables and figures to enhance accessibility and usability. Ethical considerations, such as informed consent, anonymized data, and opt-out options, uphold high privacy standards, making the dataset a trustworthy resource for the research community.

- Designed for versatility, this dataset supports a wide range of studies, including user modeling, AI fairness, filter bubbles, polarization, and user addiction, making it a valuable asset across multiple research domains.

### Weaknesses
 - The paper does not compare model performance trained on this new dataset with previous benchmarks in the literature, making it challenging to assess the dataset’s practical utility. This absence of baseline comparisons limits our ability to measure performance gaps and evaluate how well (or poorly) this dataset performs relative to established standards. For me, this is the most critical aspect, as such a comparison is essential to determine the dataset's true impact and value in advancing the field.

- The selection criteria for users and videos are not explicitly detailed, raising concerns about the dataset's representativeness and potential sampling biases. The paper does not  also sufficiently analyze or acknowledge potential biases, such as volunteer self-selection bias, geographic concentration, or device type distribution, which could affect the dataset's generalizability.

- Apart from qualitative t-SNE visualizations, the study lacks a quantitative evaluation, such as clustering metrics or downstream task performance, to effectively validate the quality of the extracted video features.

- The review of existing datasets and related work is not exhaustive, potentially overlooking relevant studies and resources that could contextualize the dataset's contributions.

### Questions
- Could you provide baseline experiments demonstrating the dataset's applicability and effectiveness for common tasks such as recommendation, user modeling, or video classification?

- Expand the literature review to encompass the latest publicly available short-video datasets. Provide a comparative table highlighting key features, such as the number of users, videos, interaction types, and content richness, to clearly demonstrate how your dataset stands out.

- Please adjust Figure 4, as the text appears too close together. Changing the format would improve its readability.

- It would be helpful to enlarge the legends in Figures 3, 4, and 5, as they are currently quite small. Also, please consider using a color palette that is accessible to colorblind viewers, including in Figure 6.

- Include case studies or illustrative experiments that showcase the dataset's application in areas such as user modeling, fairness analysis, or studying filter bubbles. Presenting preliminary results or hypothetical scenarios can help researchers envision practical uses and inspire innovative applications.

- Describe the handling of multilingual content within the dataset. Specify the languages supported by the ASR system and outline any post-processing steps taken to enhance transcription accuracy. Provide statistics on the accuracy rates or error rates of the ASR results, if available.

- How do the potential biases affect the dataset's generalizability, and what steps have been taken to mitigate them?

- Add a dedicated section to discuss the dataset's limitations, covering potential biases, data sparsity in specific interaction types, and gaps in demographic coverage. Transparently addressing these issues helps researchers to consider them in their analyses and supports trust in the dataset's integrity.

### Soundness
3

### Presentation
3

### Contribution
1
