# Discovering Clone Negatives via Adaptive Contrastive Learning for Image-Text Matching

- Decision: Accept
- Scores: 3, 8, 6, 8

## Abstract
In this paper, we identify a common yet challenging issue in image-text matching, i.e., clone negatives: negative image-text pairs that are semantic-consistent with the positives, which leads to ambiguous and suboptimal matching results. To address this, we propose Adaptive Contrastive Learning (AdaCL), which introduces two margin parameters with a modulating anchor to dynamically strengthen the compactness between positives and mitigating the impact of clone negatives. The modulating anchor is selected based on the distribution of negative samples without explicit training, allowing for progressive tuning and enhanced in-batch supervision. Extensive experiments on image-text matching, noisy correspondence learning, CLIP pre-training, and text-based person search demonstrate the superiority of AdaCL in image-text matching. Furthermore, we extend AdaCL to weakly-supervised image-text matching by substituting human-annotated descriptions with automatically generated captions, increasing the number of potential clone negatives. AdaCL demonstrates robustness with the generated captions, alleviating the reliance on crowd-sourced annotations and laying a foundation for scalable vision-language contrastive learning.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper addresses a challenge in image-text matching referred to as clone negatives, which are negative image-text pairs that are semantically consistent with the positive pairs, leading to ambiguous and suboptimal matching results. To tackle this issue, the authors propose Adaptive Contrastive Learning (AdaCL), which employs two margin parameters with a modulating anchor to dynamically enhance the compactness between positives while mitigating the influence of clone negatives. The modulating anchor is selected based on the distribution of negative samples without explicit training, facilitating progressive tuning and improved in-batch supervision. Experiments on two benchmark datasets underscore the effectiveness of AdaCL.

### Strengths
1. The paper introduces a novel approach to address the issue of clone negatives in image-text matching, which is a pertinent problem in the domain.
2. The proposed Adaptive Contrastive Learning (AdaCL) framework dynamically adjusts the compactness between positives, showing potential for enhanced performance in image-text matching tasks.

### Weaknesses
1. The experimental results are not convincing. The main contribution of the paper is the improvement of Contrastive Learning, with CLIP being the most representative of this field. To prove the effectiveness of the paper, a comparison within the OpenCLIP framework using larger datasets (e.g., LAION) should have been conducted, rather than experiments on the relatively small-scale COCO dataset.
2. The proposed method appears to be somewhat complex, which goes against the inherently simple and scalable nature of contrastive learning. Additionally, the paper does not provide an analysis of the introduced hyperparameters or the potential increase in overall complexity.
3. The authors do not clearly explain why clone negatives pose a problem within the paradigm of contrastive learning. Clone negatives refer to texts that are aligned with the image but are not as accurate as the ground-truth text. Hence, the logits of clone negatives should naturally be lower than those of the ground-truth, which aligns with the basic optimization framework of contrastive learning. The authors should provide more empirical evidence or theoretical analysis demonstrating why standard contrastive learning fails to handle clone negatives adequately.

### Questions
The method figure (Figure 2) is unclear, and neither the figure caption nor the text adequately explains what the "reference clone negatives" refer to.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper focused on solving the task of Image-Text Mathing (ITM) especially the key challenge of clone negatives: the captions that have consistent semantics with the GT sentences, but with less coarse-grained information. To solve this, the Adaptive Contrasvite Learning (AdaCL) method is proposed, which introduces supervision of the clone negatives, and can dynamically penalize the clone negatives. This will enlarge the distance between the positives and the clone negatives.

### Strengths
1. The authors focus on a critical issue of clone negatives in the field of Contrastive Learning under the background of Vision-Language Models and Image-Text Matching Tasks.   
2. Experiments are well performed, which show effectiveness of AdaCL.

### Weaknesses
1. More pre-trained models and more down-stream tasks could be test to further demonstrate the effectiveness of the proposed method.

2. Spelling error(s): 
p2 077 andand
p2 Fig 1(b) T2 -> T3
p1 034 action-level -> global level
p6 274 double curly braces “}” -> just one “}”, delete the last one

3. Sequential adverbs: 
p4 205 There are “Two conditions”. I can see the “First”, but where is the “Second”?
It should be before p4 214 ”(Second, )to achieve this”. 

4. Meaning of subscript: 
p4 208 What does the subscript “u” mean? What is its abbreviation? Is it “unique(==specific)”?
And what about p4 210 the “u-” in k∈M_u-? Is it “not unique”? I can’t sure. 

5. Inconsistencie(s): 
p4 Sec 3.2 one anchor + one pos + M neg ==> Why not all M neg? Because Sec 3.2 and Sec 3.3 are connected. 
p5 Sec 3.3 one anchor + one pos + (M-1) neg
p6 Algorithm 1 a mini-batch of N pos + M neg??? ==> Why not one pos + M neg?
  May be the authors want to say “a mini-batch of N, in which 1 pos and M neg”?
  So, N==1+M?

6. p5 254 what is the superscript of j in Eq. (8)? Is it the same as Eq. (7) or Eq. (3)?

7. p5 263 Why Eq. (9) is that? Can you give us a concrete deduction? And what about p(C=0|s)? Can you give a specific formulation?  

8. p10 509 How to correctly understand the heat map, since a sentence contain ALL WORDS, and every mentioned instance in the image SHOULD be highlited. So, what does these Attention Map mean indeed? What Information can I get from them? Or what should we expect from them?

### Questions
Please refer to weakness above.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper recognises the clone negative issue in image-text matching, where negative image-text pairs are semantically consistent with the positives. To address this issue, the authors modulate the softmax function of original contrastive losses with anchors that are selected from each in-batch similarity score based on Gaussian discriminant analysis. The proposed method, called Adaptive Contrastive Learning, demonstrates superiority in both supervised and weakly-supervised image-text matching.

### Strengths
1. The motivation of this work is clear. The issue of clone negatives is well illustrated and intriguing, which is common and significant in matching images and texts.

2. The proposed method is extensively verified under both supervised and weakly supervised settings, exhibiting superior performance under several benchmarks.

3. The authors provide comprehensive ablation studies and analyses, with both quantitative and qualitative verification.

### Weaknesses
1. The method is not applied to or compared with the recent CLIP-style models, which I believe would strengthen the significance and soundness of this work.

### Questions
1. From what I understand, this method is matching images with texts. Then why is FasterRCNN, an object detection model, used in the experiments?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors of this paper propose a new method to improve cross-modal learning by adding a conditioning factor to the loss function to alleviate what the authors call "clone negatives". The proposed method is effective from the experimental results. However, the concept of clone negatives is more like the False-negative problem mentioned in some existing studies. For this reason, the concept of clone negatives still needs further discussion.

### Strengths
1. The author's idea of ​solving the false-negative problem is clear.
2. The experiments are rich and the proposed method is effective.

### Weaknesses
1. The authors proposed a new concept, namely clone negative examples. However, this is actually the false-negative problem, which is not a new topic. For example, there has been similar research in [1,2].
2. The authors should enrich the caption of Figure 2 to make the core idea clear and concise.
3. Line325: “Comparisons of Image-text matching” should be “Comparisons of image-text matching”
4. The 2024 baselines are missing.
5. Line 954,955: Missing citations.
6. There are usually three mainstream benchmarks for text-based person search tasks. I suggest the author add the results of RSTPReid. Also, does the authors‘ R@ refer to the Recall accuracy? However, in the text-based person search task, the Rank accuracy is usually used as the evaluation indicator.

Reference:

[1] Li H, Bin Y, Liao J, et al. Your negative may not be true negative: Boosting image-text matching with false negative elimination[C]//Proceedings of the 31st ACM International Conference on Multimedia. 2023: 924-934.

[2] Li Z, Guo C, Feng Z, et al. Integrating language guidance into image-text matching for correcting false negatives[J]. IEEE Transactions on Multimedia, 2023, 26: 103-116.

### Questions
See weakness.

### Soundness
3

### Presentation
3

### Contribution
3
