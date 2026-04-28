# PerceptionCLIP: Visual Classification by Inferring and Conditioning on Contexts

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 5, 5, 8

## Abstract
Vision-language models like CLIP are widely used in zero-shot image classification due to their ability to understand various visual concepts and natural language descriptions. 
However, how to fully leverage CLIP's unprecedented human-like understanding capabilities to achieve better performance is still an open question.
This paper draws inspiration from the human visual perception process: when classifying an object, humans first infer contextual attributes (e.g., background and orientation) which help separate the foreground object from the background, and then classify the object based on this information.
Inspired by it, we observe that providing CLIP with contextual attributes improves zero-shot image classification and mitigates reliance on spurious features. 
We also observe that CLIP itself can reasonably infer the attributes from an image.
With these observations, we propose a training-free, two-step zero-shot classification method \methodname{}. 
Given an image, it first infers contextual attributes (e.g., background) and then performs object classification conditioning on them.
Our experiments show that \methodname{} achieves better generalization, group robustness, and interpretability.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper is inspired by human visual perception, where humans first discern contextual attributes, such as background and orientation, to distinguish objects, and then classify them. Similarly, when CLIP is provided with these contextual attributes, it improves in zero-shot image classification and reduces dependence on irrelevant features. Authors found that CLIP can deduce these attributes from an image itself and based on this fact to propose PerceptionCLIP. PerceptionCLIP first determines contextual attributes from an image and then classifies the object based on these attributes. Experiments are done on CLIP's zero-shot classification settings and show clear improvements over the original CLIP.

### Strengths
- The paper is well written and easy-to-follow. While the concept of utilizing background information for image classification isn't groundbreaking in literature, its application to CLIP could be innovative.
- The experiments show clear advantages of using contextual attributes over the traditional 80 templates.

### Weaknesses
 - The authors assert at least twice that PerceptionCLIP mirrors human perception. However, I'm not entirely convinced. Authors gave the preliminary that: “humans first infer contextual attributes (e.g., background and orientation) which help separate the foreground object from the background, and then classify the object based on this information.” Yet, there's no evidence indicating that PerceptionCLIP actively separate foreground from background during classification, or that such separation is utilized the model. It's possible that PerceptionCLIP utilizes background attributes differently.
- The authors refer to background information as spurious features (e.g. Figure 1). To my knowledge, it is not completely correct. Though they can sometimes overlap, they are not the same. Background information is a broader concept, while spurious features specifically refer to misleading patterns that a model might incorrectly learn as being important. In addition, the GradCAM in Figure 1 primarily emphasizes the foreground, consistent with [a], without highlighting any reduced reliance on spurious features. It's more accurate to state that it offers enhanced focus on foreground objects.
- When I like the idea of Textual descriptions for contextual attributes Sec 4.1., I could not find how exactly you map Z using the proposed annotation function alpha to attribute text descriptions. Also, why do you say this annotation function model human preferences in captioning? Authors may also want to clarify the p value associated with the textual descriptions.  I imagine that these descriptions can also easily obtained using LLMs (e.g. ChatGPT).
- The name of the proposed metric can be easily confused with the original CLIP score. How about naming it as Attribute-CLIP.

### Questions
Post-rebuttal:

I genuinely appreciate your great efforts put into this rebuttal!

I read the (updated) paper one more time, the authors' responses to me thoroughly, and the responses to other reviewers.
While PercentionCLIP is indeed powerful and but answer of "why does it work" is not fully addressed via the GradCAM visualization as raised by W2 of reviewer vx4m. 

I would like to keep my rating for now and may change later after discussing with other reviewers.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Inspired by the human perception process that the contextual attributes are separated from the foreground objects, this paper proposes a training-free, two-step zero-shot classification method PerceptionCLIP to first infer the contextual attributes (e.g., background) and then performs object clas- sification conditioning on them. A proof-of-concept investigations reveal that conditioning on ground-truth contextual attributes improves CLIP’s zero-shot classification. The proposed PerceptionCLIP demonstrates performance gain and improved interpretability on several datasets.

### Strengths
The idea of imitating human perception process to improve the generalization and group robustness of the image classification model is insightful for the community.
The proposed method is extensively evaluated on 11 datasets.

### Weaknesses
1. Collecting the contextual attributes requires either pre-knowledge for the test image or a large dataset containing captions, which hinders the generalization ability of the proposed method in the real world. For instance, contextual attributes for the CelebA dataset are manually defined, e.g., gender, age, etc. To collect the contextual attributes for the remote sensing dataset EuroSAT, the authors first retrieve similar images and captions from a large image+text dataset LAION-400M, then ask GPT-4 to summarize the contextual attributes. What if we do not have external datasets to provide captions?

2. The qualitative results in Figure 4 indicate that introducing the contextual attributes reduces reliance on the spurious features and the model focuses more on the core features. It would be fairer to provide a quantitative evaluation, e.g., counting the percentage of model attention on the core features versus on spurious feature on all test set in ImageNet, and compare the ratio of different models.

3. The performance gain seems marginal on most of the datasets. For instance, in Table 4, the performance gain is only around 2% on ImageNet, ImageNetV2, ImageNet-A and ImageNet-Sketch. Besides, since introducing a random attribute or even a wrong attribute can improve the accuracy in Table 2, it would be interesting to include the results of the wrong attribute and random attribute in Table 4 as well.

4. The results in Table 7 are not consistent among different backbones. It is hard to get any conclusion on which method is better.

### Questions
In Table 7, why lower gap between the Avg and Worst is better?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper explores text-prompting in CLIP, to make the inference process more ``human-like”. The authors show that their two-phased prompting process improves (i) performance, and (ii) robustness against specious features (shortcuts).

### Strengths
- In this work, prompting is class-independent; which makes it easily applicable to numerous datasets. 
- Authors systematically evaluate the prowess of CLIP in inferring contextual attributes
- The performance gain on domain-specific and out-of-distribution ImageNet datasets shows promise in the claims and approach of the authors
- This work allows for building domain-specific (yet, class independent) augmentations with the possibility of human-in-loop intervention
- The approach presented is elegant and interpretable

### Weaknesses
 - If I understand correctly, Figure 3 gives only the score (x100) of the correct class in different scenarios. Is this *completely* informative? I think it can be easily misleading. What if the model provides relatively higher scores to some of the wrong classes as well? Can the authors analyse the score distribution of the wrong classes? Reporting the mean of CLIP_score@topK might be a good start to understanding the false positives.
- I appreciate the visualisation study provided by GradCAM as a qualitative analysis but I am not confident of the calculation of “core” versus “spurious” features [1]. 
- Can the authors also report the random accuracy for Tables 4 and 5? It is important to have a random baseline (that is, random string in place of the inferred context having the same token (and not string) length) here to isolate the effect of “registers” versus actually using the context [1]. 
- The authors have not provided the code for reproducing the paper; implementation details are missing.

**TL;DR**: The authors make strong claims about reducing the reliance on shortcuts, however, the missing baselines and analyses do not make me confident of their approach. However, some analyses seem misrepresented/miscommunicated. If the authors can answer my questions, I’d be open to changing the score.

Some clarity formatting and typographical errors to rectify:

- Overall, the paper is well-written and ideas well-presented
- The paper, at some points, deviates from standard ICLR formatting:
  - “interleaved” figures and tables (minor inconvenience)
  - Unlabelled table: “Conditioning on ground-truth contextual attributes improves classification accuracy”
- Minor typographical errors:
  - Section 5.1: “Intuitively, we classify an image using both – possible classes and the ground-truth contextual attributes”
  - Remove the asterisk in the author list of “Distributionally robust neural networks“

### Questions
Please refer to weaknesses above

### Soundness
2 fair

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors show that adding text that describes the context of an object in an image can improve the performance of CLIP-based zero-shot classification. In addition, they show that said context can be inferred using CLIP itself.

### Strengths
1- The paper shows some evidence towards towards the fact that CLIP representations do capture the context as well as the foreground objects, making the alignment with text prompts better when the appropriate context is included in the text.
2- Although the improvements in performance are not large in many of the benchmarks, they come at little cost, probably making it applicable in practice.

### Weaknesses
I haven’t found any major weakness in this work (although it is not fully within my expertise).

Some minor issues:
- For some of the experiments I couldn’t find if they employed ClassAttr or PureAttr.
- In Algo 1, I assume it should be “Set of classes Y” rather than “class Y”, and that the sum is over y \in Y.

### Questions
Some minor issues:
- For some of the experiments I couldn’t find if they employed ClassAttr or PureAttr.
- In Algo 1, I assume it should be “Set of classes Y” rather than “class Y”, and that the sum is over y \in Y.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
