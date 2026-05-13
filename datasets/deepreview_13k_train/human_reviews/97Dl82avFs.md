# Alt-Text with Context: Improving Accessibility for Images on Twitter

- Decision: Accept
- Scores: 8, 6, 5

## Abstract
In this work we present an approach for generating alternative text (or alt-text) descriptions for images shared on social media, specifically Twitter.
More than just a special case of image captioning, alt-text is both more literally descriptive and context-specific.
Also critically, images posted to Twitter are often accompanied by user-written text that despite not necessarily describing the image may provide useful context that if properly leveraged can be informative.
We address this task with a multimodal model that conditions on both textual information from the associated social media post as well as visual signal from the image, and demonstrate that the utility of these two information sources stacks.
We put forward a new dataset of 371k images paired with alt-text and tweets scraped from Twitter and evaluate on it across a variety of automated metrics as well as human evaluation.
We show that our approach of conditioning on both tweet text and visual information significantly outperforms prior work, by more than 2x on BLEU@4.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies on an important problem: how to generate Alt-text to help improve the accessibility of social media images. More specifically, the authors collected and cleaned a large dataset of images incorporated with the alt-text labeled by users. With this large dataset, they are able to evaluate the proposed method and some baselines. Overall the proposed solution is not novel for the Machine Learning Community. But the research problem is interesting and meaningful. Also, the collected dataset is important for the community of HCI and Social Media Analysis.

### Strengths
1. The collected dataset is important and useful. The data preprocess ensure its usability.

2. The research problem raised in this paper is important.

### Weaknesses
1. The novelty of the proposed method is really limited excpet the tweet-text-based reranking.

2. The experiment is somewhat not extensive. For example, from Table 1, it seems that the tweet-based reranking is the most important component. But the authors did not tried to incorporate the reranking with the baselines, which is not fair.

### Questions
1. Will the tweet-based reranking improve the baselines like BLIP-2 and ClipCap?

2. Is there some other reranking strategies that you tried? Such as comparing the Clip-based similarity in the representation space?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a method for generating "alt-text" for social media images. In this paper, "alt-text" is explained as a more detailed description and context-specific than a generic image caption.
The proposed method takes an image and the social media text that accompanies the image and outputs the alt-text of the image. The input image is encoded by CLIP and combined with the encoded text. The combined information is then input to GPT-2 to generate the alt-text.
The author has collected tweets and their corresponding images with alt-text to create a dataset for alt-text generation research. The evaluation shows the results of using this dataset to compare the proposed method with several baseline methods.

### Strengths
The author points out that in social media, images are often posted in addition to textual information, but there is little information describing the images, and in such situations, information about the images is not conveyed by text-to-speech software for the visually impaired, for example. I agree with this point and understand its importance as a study.

As for the proposed method, its basic structure consists of encoding images using CLIP and generating text using GPT-2. This structure itself is not unique, as it is a concept that has been used in existing research. I believe that the originality lies in the extended part of the basic configuration, where not only the image but also the text to which the image is attached is input.

The fact that an original data set was constructed for this study is commendable. It is also commendable that in the evaluation using this data set, comparisons with various methods were made to show the characteristics of this task.

### Weaknesses
As mentioned in the "Strengths" section, the focus on "alt-text" is highly evaluated, but there is room for improvement in that "alt-text" is not clearly defined in the paper.

In the evaluation dataset, the "alt-text" entered by twitter users is used as the correct answer, but it is written as "alt-text captions on Twitter are written by untrained users, they can be noisy, inconsistent in form and specificity, and occasionally do not even describe the image contents" in the paper, and it seems that the authors are discussing the generation method without knowing what "alt-text" is.

Although the difficulty is understandable, I think that the discussion should start with clarifying what "alt-text" is, and then discussing the generation method.

### Questions
I wondered if the "alt-text" would be written differently for different people, even for the same image. Is it possible for the proposed method to learn well in such a case?

In addition, although the paper uses crowdsourcing for evaluation, I think it is possible that the evaluation by the viewer of the "akt-text" may also differ from person to person. How did the evaluation go this time?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents a method to generate accessibility captions for images shared on Twitter. The proposed approach combines CLIP embeddings for the images, as well as additional context that is included in the tweet’s text to create an embedding that is then fed to GPT-2 to generate the accessibility description. The paper’s evaluation demonstrates that the proposed approach can outperform naive and neural-based approaches like ClipCap and BLIP-2.

### Strengths
First of all, I would like to applaud the authors for working on this important and timely problem. I believe that this research is very important and can have the potential to improve the lives and online experience of many people with visual impairments. Overall, I believe that this research focuses on an important problem, and there is potential for a big impact. Second, the paper collects a large-scale dataset of images and user-generated accessibility captions from Twitter; this dataset is far bigger than previous research efforts focusing on similar research problems. Third, I believe that the paper’s approach is a simple, creative, and effective method to combine CLIP embeddings, tweet text, and LLMs to generate accessibility captions for images. The paper’s approach is easy to understand and combines important features for generating contextual and useful accessibility descriptions for images shared on Twitter. Finally, I like that the paper evaluates the performance of the proposed approach both with quantitative metrics as well as via a user study that aims to assess how users perceive and compare accessibility descriptions generated from the proposed method and baseline approaches.

### Weaknesses
I have several concerns with the paper, mainly related to the lack of gold standards for accessibility captions, the lack of important and adequate methodological details, the paper’s evaluation, the paper’s approach to releasing data, and the paper’s ethical considerations.

First, there is a disconnection between the paper’s motivation and how the paper evaluates the performance of the proposed method. I agree with the paper’s motivation that the user-generated accessibility captions are of questionable quality, given that most users are unaware of best practices for generating accessibility captions. On the other hand, however, the paper collects user-generated accessibility captions and treats them as gold standards (i.e., ground truth captions). This is problematic as in the evaluation, the paper compares the generated captions from their approach and compares them with captions that are of questionable quality. Therefore, it is not clear what is the actual performance of the proposed methods. A way to potentially mitigate this issue is to apply the proposed approach to other datasets released by previous research that include gold-standard captions (i.e., captions that adhere to the best practices for generating accessibility descriptions for images).

Second, I am puzzled about how the BLEU@4 score is calculated in the evaluation. To the best of my knowledge, the BLEU score ranges from 0 to 1 and aims to assess the precision of the n-grams included in the generated text compared to the ground truth. In the paper’s evaluation, the paper mentions that the proposed approach has a BLEU@4 score of around 1.8. I suggest to the authors to clarify how they calculated the BLEU scores (e.g., if they used a modified version) and better describe how we can interpret these BLEU@4 values.

Third, the paper lacks important and adequate details on the paper’s methodology. Particularly, the paper refers to several appendices so that the reader can get more information, however, there are no appendices in the manuscript. This hurts the readability of the paper and does not allow us to assess the quality and robustness of the presented results in the paper. I suggest including the appendices so that we can understand how the paper conducted various steps of the research. In particular, I would have liked to read more on how the paper conducted the user study, how they recruited users, what is their background and expertise with regards to the best practices for generating accessibility descriptions, etc. All these details are paramount for understanding the quality of the presented research.

Fourth, I have some concerns about the paper’s approach to releasing the dataset. Given the recent changes to Twitter’s API, it became extremely hard to rehydrate tweets based on their IDs. So by simply releasing the Twitter IDs and the media URLs, interested researchers will not be able to reproduce the paper’s results and further use this dataset for further studying this problem. I suggest to the authors to consider releasing more attributes from the dataset (specifically the tweet’s text) so that interested researchers can reproduce the paper’s results without relying on the closed and expensive new Twitter APIs.

Fifth, the paper does not properly explain how the qualitative assessment is done (in Section 6.4), which does not allow the reader to understand if it’s done in a systematic way or how representative/generalizable the insights are. I suggest to the authors to include more details on how the samples for the quantitative analysis are selected and, more importantly, how the qualitative assessment is undertaken (e.g., are the people experts in the domain of accessibility description generation, are they aware of the best practices, etc.)

Finally, the paper does not discuss the ethical considerations when conducting this research. This is important as the paper conducts a user study and shows participants’ images shared on Twitter. For instance, did the paper ensure that there are no harmful images in the dataset and that no participants were exposed to harmful information?

### Questions
1. What is the rationale for using user-generated captions as gold standards and do you have an idea how this affects the presented results?
2. How is the BLEU@4 score calculated and did you use a modified version of the metric? 
3. How is the user-study conducted and what are the background/expertise of the recruited participants? Also, have you obtained an IRB approval before conducting the user study? How did you ensure that participants were not exposed to harmful information?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
