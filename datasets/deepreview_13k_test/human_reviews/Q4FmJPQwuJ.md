# CrossTVR: Multi-Grained Re-Ranker for Text Video Retrieval with Frozen Image Encoders

- Decision: Reject
- Scores: 5, 5, 6

## Abstract
State-of-the-art text-video retrieval (TVR) methods commonly use CLIP and cosine similarity for efficient retrieval. 
Meanwhile, cross attention methods, which employ a transformer decoder to compute attention between text queries and video frames, offer a more comprehensive interaction between multimodal information.
Complementary to the existed one-stage text video retrieval approaches above, we propose a re-ranker called CrossTVR that further explores the fine-grained and comprehensive interaction between text and all the vision tokens of a given video at the frame level and the video (clips or segments) level. 
Furthermore, we employ the frozen CLIP model strategy for fine-grained retrieval, enabling scalability to larger pre-trained vision models like ViT-G and resulting in further improved retrieval performance.
Subsequently,  a two-stage text-video retrieval architecture can be proposed.
In the first stage, we leverage existed TVR methods with cosine similarity network to efficently obtain text video candidate pairs.
In the second stage, the proposed re-ranker is applied for fine-grained retrieval. 
Experimental results on text-video retrieval datasets demonstrate the effectiveness and scalability of the proposed re-ranker when combined with existing mainstream one-stage text-video retrieval approaches.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a multi-grained re-ranker for text video retrieval with frozen image encoders, named CrossTVR. Although experimental results have demonstrated the effectiveness of this paper, the main contributions of this paper are not clear enough.

### Strengths
1.The authors develop a novel method to capture comprehensive and fine-grained text-video interaction cues, which uses a multi-grained video text cross attention transformer module to enhance the retrieval process.
2.The corresponding experiments validate the effectiveness of the proposed method on five public text-video retrieval benchmarks and show a significant improvement in solution acceptance rates.

### Weaknesses
1.	The Abstract is not well written and it is not easy to understand the contributions. Recommended to rewrite and well present your contributions. 
2.	For the first stage, this paper uses an existing cosine similarity network, the novelty is limited for me.
3.	For the technique part, the motivation for multi-grained video text cross-attention is unclear. How to enhance the fine-grained correspondences by the cross-attention module.
4.	Furthermore, what specific attention mechanism is being employed? Please explain this work's fundamental research insight. 
5.	The main contributions of this paper are not clear enough to show the advantages and the novelty is not well explained. Please summary the main contributions in the introduction section.
6.	The organization of this manuscript is a mess, especially the order of the discussion of Tables 1 to 5. The related discussion should be even clearer.
7.	In addition, the authors should revise the manuscript thoroughly. Here are some data errors and typos as listed below (including but not limited to). The authors need to make the necessary changes.
1)	In Table 5, there are data errors that need to be corrected.
2)	In the 4.2 section, ‘moreover, our method, which leverages CLIP-VIP, achieves …’

### Questions
None

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper puts forward a new method for text-video retrieval. The core contribution of the study revolves around a multi-grained re-ranker that is designed to effectively retrieve relevant videos using text as a query. The paper also proposes a design strategy for the cross attention module by collaborating with different cosine similarity based methods, which further enhances the retrieval efficiency. And the experiments show good performance.

### Strengths
1. The paper is articulated with clarity and precision.
2. The multi-grained re-ranker is an innovative approach that can potentially enhance text-video retrieval's efficacy. Furthermore, the use of frozen image encoders in the context of text-video retrieval is a commendable attempt at exploring uncharted territories.

### Weaknesses
1. Explain the specific implementation and mechanism of video-level and frame-level cross attention. And how do these components operate and interact.
2. Although frozen vision encoder reduce computational costs, this approach may limit the model's flexibility and ability to adapt to different tasks.
3. There are some formatting errors, i.e Figure 4.

### Questions
1. Please elaborate on how to match and align between video and text.
2. In addition to TS2Net, the results of other existing methods are given to better evaluate the performance improvement and advantages of this method

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper aims at text-video retrieval in the domain of vision-and-language pretraining and understanding. Similar to general information retrieval or multimedia retrieval system, the authors proposed a two-stage or coarse-to-fine retrieval framework. In the first stage, the consine similarity network is trained with contrastive learning loss. Thus, a general text and video matching score could be obtained by such a model. The main contribution is the proposed re-ranker for fine-grained ranking in the second stage. Specifically, the authors proposed a novel cross attention module called multi-grained text-video cross attention in order to compute text-frame level attention and text-video level attention respectively. Finally, this prototype has been verified on several popular text-video retrieval benchmarks.

### Strengths
1. The motivation of this work is clear and is easy to follow. 

2. I think the overall technology roadmap is in the right way which includes: (a) a course-to-fine retrieval framework for the sake of efficiacy and effiency trade-off; (b) freezing the image encoders to make the training process practical and affordable;

3. The proposed  multi-grained text-video cross attention mechanism is brilliant and makes sense. Specifically, spatial text attention module is proposed at the frame level in order to discover small objects or entities. And temporal text attention is designed to capture subtle movement.

### Weaknesses
1. It seems that the experimental results do not include retrieval performance (e.g. stage 1 / stage 2/ pre- and post-processing), which is important in terms of a cross-modal retrieval topic. 

2. Again, in terms of a retrieval task, it is important to verify the effectiveness under a huge database setting. However, the most large dataset only contains 118,081 videos which is much less than industiral scales such as YouTube. At least, more distractors should be included if scaling positive text-video pairs is a concern. 

3. I think the visualization is not enough. For example, the retrieval results of different work or the effect of proposed re-ranking could be included as supplementary materials if space limitation is a concern.  Besides, the visualization should verify the effectiveness of proposed saptial text attention and temporal text attention.

### Questions
Besides the problems in the above weaknesses part, there are a few other questions listed as follows.

[Q1] The token selector is employed as a trade-off between missing detailed information and bringing redundant information issues. The implementation of such a module is a MLP followed by a Softmax Layer, which predicts each token's importance score and selects the M most informative tokens as output. The question is what is the ground truth (GT) for such predictions? It seems that it is even impossible for human beings to label. Note that this is not a single label classfication problem. 

[Q2] From the ablation study Table 6, the hard negative mining module makes little contribution to the final results, which is below my expectation. Is there any possible explanations?

[Q3] It is quite often to incorporate query expansion for the sake of increasing recall. Is it still effective after the 2nd stage re-ranking? It is not a necessary ablation study but could be considered as a option.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
