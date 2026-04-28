# HumanTOMATO: Text-aligned Whole-body Motion Generation

- Decision: Reject
- Avg Score: 6.00
- Scores: 5, 5, 6, 8

## Abstract
\vspace{-1em}

This work targets a novel text-driven \textbf{whole-body} motion generation task, which takes a given textual description as input and aims at generating high-quality, diverse, and coherent facial expressions, hand gestures, and body motions simultaneously.
Previous works on text-driven motion generation tasks mainly have two limitations: they ignore the key role of fine-grained hand and face controlling in vivid whole-body motion generation, and lack a good alignment between text and motion.
To address such limitations, we propose a \underline{T}ext-aligned wh\underline{O}le-body \underline{M}otion gener\underline{AT}i\underline{O}n framework, named \ModelName, which is the first attempt to our knowledge towards applicable holistic motion generation in this research area. 
To tackle this challenging task, our solution includes two key designs: (1) a Holistic Hierarchical VQ-VAE (\textit{aka} H${}^{2}$VQ) and a Hierarchical-GPT for fine-grained body and hand motion reconstruction and generation with two structured codebooks; 
and (2) a pre-trained text-motion-alignment model to help generated motion align with the input textual description explicitly.
Comprehensive experiments verify that our model has significant advantages in both the quality of generated motions and their alignment with text.
\vspace{-1.8em}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper is the first work that can generate whole-body motion from text description. This paper first proposes a Holistic Hierarchical Vector Quantization (H$^2$VQ) scheme to model the correlation between body and hand. Authors notice that facial expression is largely independent of body and hand, so they train a conditional VAE to generate facial motion independently. This scheme is reasonable, which is also verified in the task of SMPL-X reconstruction. Compared with the H$^2$VQ and facial cVAE, the text-to-motion alignment module is more interesting. If the author can release this module as claimed in their manuscript, this module will bring some meaningful progress to the community of text2motion.

### Strengths
The authors propose a promising task and give a thoughtful solution. From the results, we can easily judge the effectiveness of the proposed method. The writing is also very fluent.

### Weaknesses
1. The title '3.1.2 Evaluation' somehow is easily misleading. In this section, you introduced the evaluation metrics and compared methods. How about changing to 'Evaluation Details'?
 2. I feel that the focus of this article is on how to generate physical movements in the hands. The discussion about facial cVAE is limited, and I have not found any experiments to analyze this module. 
 3. Although it's hard to find compared methods in text-aligned whole-body motion generation, the authors can compare solely body generation results with previous works. But I didn't find this part. There are too few methods for comparison.



### Questions
My questions have been listed in the above Weaknesses. I have one more question on this paper: From visual results, I noticed some physically implausible artifacts, such as foot sliding. Can you give some discussion on this point?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposed a framework for whole-body motion generation from text. It includes several core designs: 1) a holistic hierarchical VQ-VAE based on RVQ for body and hand motion reconstruction; 2) a hierarchical GPT for predicting fine-grained body and hand motions; 3) a pre-trained text-motion-alignment model used as a prior for text-motion generation stage explicitly; 4) a text-motion alignment supervision in the GPT preditor. Comprehensive experiments verify that the proposed model has significant advantages both quantitively and qualitatively.

### Strengths
The authors pioneered the task of whole-body motion (including the face and hand motion) generation from speech. To generate fine-grained hand and face motions, two core technique designs were introduced: 1) a holistic hierarchical VQ-VAE based on RVQ for body and hand motion reconstruction; and 2) a hierarchical GPT-based generation. To achieve a good alignment between text and motion, a text-motion retrieval model is pre-trained and used as a prior for the text-motion generation stage explicitly. Extensive quantitative and qualitative experiments were conducted to demonstrate the efficiency of the proposed method.

### Weaknesses
1. The technical contribution of this paper seems somewhat limited in the following:
(1) the pipeline of the method is similar to the T2M-GPT where a VQ-VAE is used for motion reconstruction and a transformer-based GPT model is used for motion generation, while the tasks are different; 
(2) the pretraining of a motion encoder and a text encoder via aligning text and motion in a contrastive way is also not new such as TMR, and further using it to replace the clip is natural in the prediction stage. 
2. From the example of the visualizations, the textual description for facial motions focused on emotion (like happily, angrily), but the generated face shown in the paper is static, rather than dynamic motions, which lacks the demonstration of the emotion dynamics.

### Questions
Except for the above weaknesses, there are a few questions as follows: 
1. In Table 2, about the H2VQ, what is the size of the codebooks for reconstructing the body and hand motion? Besides, for vanilla VQ-VAE and RVQ, do you separately model the hand and body motions and then combine the motion as body-hand motions? How is the performance for VQ-VAE and RVQ when increasing from 1024 to 4096?
2. Regarding facial generation,  what the text embedding is used? Clip or TMR?
3. Since the hand & body, and face motions are separately modeled, how is the coherence of the generated motions?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper focuses on the text-driven whole-body motions generation, including facial expressions, hand gestures, and body movements. The proposed framework consists of a holistic hierarchical VQ-VAE to compress the whole-body motion into two-level discrete codes. It also features a hierarchical-GPT model that predicts the discrete motion codes from input textual descriptions in an auto-regressive manner. Additionally, the author proposes a pre-trained text-motion-alignment model to enhance the alignment between given text and generated motions.

### Strengths
1. The paper is the first to target the text-driven whole-body motions generation task, aiming at generating high-quality, diverse, and coherent facial expressions, hand gestures, and body motions.

2. The paper introduces a novel framework for text-driven whole-body motion generation, featuring a Holistic Hierarchical Vector Quantization for learning informative and compact representations at low bit rates, along with a Hierarchical-GPT for predicting hierarchical discrete codes for body and hand motions in an autoregressive manner.

3. The paper proposes a pre-trained text-motion alignment model, which serves to provide textual embeddings instead of commonly used CLIP embeddings. Furthermore, it offers motion-text alignment supervision during the training process.

### Weaknesses
In my view, the proposed H2VQ and Hierarchical-GPT just extend the model introduced in T2M-GPT by incorporating hand gesture modeling. These modifications are rather straightforward. Firstly, in the context of vector quantization, they integrate the hand pose vector quantization with the body pose using a hierarchical strategy rather than directly quantizing the whole body pose. Secondly, The T2M-GPT has been modified to decode the body pose code and hand pose code alternately, rather than directly outputting the whole body pose code. The utilization of TMR for encoding textual descriptions is a more intelligent choice compared to CLIP embedding, and the incorporation of motion-text alignment supervision appears to be beneficial during the training. However, it's important to note that text-motion alignment has been employed in various previous works, including TEMOS, and the proposed TMR merely adopts a contrastive learning way through a retrieval target. The paper presents a substantial amount of contributions, but the technical designs lack novelty and a certain level of appeal from my perspective. As a result, I would recommend a rating of marginally above the acceptance.

### Questions
1. Currently, is it feasible or essential to generate diverse and realistic human poses and facial expressions using the available datasets? To my knowledge, most of the existing datasets lack diversity and realism in hand poses and facial expressions. From visualization results, I can discern certain minor distinctions in hand poses, although they may not be highly realistic, and I cannot find the differences in the generated facial expressions.

2. How about the comparison with a simple baseline that directly combines SOTA models for facial expression, hand pose, and body pose generation?

Minor Fix:

1. On page 3, where it mentions, "where $F$ and $d$ denote the number of frames and the dimension ...", it may be advisable to replace $F$ with $L$ to maintain consistent notation.

2. On page 4, there is a repetition of the sentence: "In the encoding phase, we input hand and body motions, ...".

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposed to solve the novel task of text-driven whole-body motion generation, which generates body, hand, and face motion simultaneously given a text description. The proposed method includes a holistic hierarchical VQ-VAE for hand and body motion encoding, a hierarchical GPT for hand and body motion generation, a cVAE for facial expression, and a pretrained text and motion alignment model. The paper also proposed to evaluate the alignment between text and motion with a novel evaluation metric TMR-R-Precision(256) and TMR-Matching Score. Experiments were conducted on the Motion-X, GRAB, and HumanML3D datasets.

### Strengths
- This is the first paper to generate holistic and vivid motions with body, hand, and facial expressions.
- The authors pretrained a text-motion retrieval to align the text and motion embedding, bypassing the semantic gap between CLIP-based text embedding and motion.
- The proposed methods show a clear advantage against SOTA motion generation methods in common metrics, except for multi-modality and diversity.

### Weaknesses
### Major issue

- The paper emphasized generating “vivid motions,” and the key for a motion to be vivid is to have vivid facial expressions. However, the proposed solution does not show promising results in facial expression generation. The facial expression part is not evaluated against any baseline method, and the facial cVAE is disconnected from the other parts of the proposed method. The lack of quantitative evaluation for the facial expression generation makes it hard to assess the effectiveness of this module. Furthermore, the paper does not detail how the facial expressions are synchronized with the body and hand motions, which is crucial for achieving truly vivid and coherent motion.

### Minor issues

- In section 2.1, $F$ should be $L$?
- In section 2.2, the sentence is repeated twice
    
    > In the encoding phase, we input hand and body motions, yielding hand and body tokens through the hand encoder EncH(·) and the body encoder EncB(·),  respectively.
    >
- In Appendix C.1, Algorithm 1, line 4 in the for loop, $\hat{z}^B=..., \hat{z}^B));\mathcal{C}^B);$ the second $\hat{z}^B$ should be $z^B$.

### Questions
- What’s the reason behind the name hierarchical-GPT? The model seems to interleave instead of hierarchical to me.
- Why is it that in H2VQ, the hand is encoded before the body, and in Hierarchical-GPT, the body token is predicted before the hand? Is there any reason besides empirical performance advantages?
- To what extent can the method generalize to OOD text descriptions?
- In the supplementary video, in the T2M-GPT examples, the characters are all moving backward. Please confirm if the examples are rendered correctly.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
