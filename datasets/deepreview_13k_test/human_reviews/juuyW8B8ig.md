# Language-Informed Visual Concept Learning

- Decision: Accept
- Scores: 8, 5, 5, 6

## Abstract
Our understanding of the visual world is centered around various concept axes, characterizing different aspects of visual entities.
While different concept axes can be easily specified by language, \eg, \texttt{color}, the exact visual nuances along each axis often exceed the limitations of linguistic articulations, \eg, a particular style of painting.
In this work, our goal is to learn a language-informed visual concept representation,
by simply distilling large pre-trained vision-language models.
Specifically, we train a set of concept encoders to encode the information pertinent to a set of language-informed concept axes,
with an objective of reproducing the input image through a pre-trained Text-to-Image (T2I) model.
To encourage better disentanglement of different concept encoders, we
anchor the concept embeddings to a set of text embeddings obtained from a pre-trained Visual Question Answering (VQA) model.
At inference time, the model extracts concept embeddings along various axes from new test images, which can be remixed to generate images with novel compositions of visual concepts.
With a lightweight test-time finetuning procedure, it can also generalize to novel concepts \emph{unseen} at training.
Project page at {\footnotesize\url{https://cs.stanford.edu/~yzzhang/projects/concept-axes}}.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors use multiple visual encoders to disentangle various visual concepts from images. These visual concepts are defined as vector axes based on natural language description. The proposed framework performs a simple training on a synthetic dataset that learns disentangled vectors for each concept. These disentangled vectors can be combined with language (similar to textual inversion paper) to generate images containing combined concepts. They show how their method disentangles and generates new images with variably joined concepts better than existing work.

### Strengths
1. The paper explores an interesting idea of separating concepts in images in the visual domain in a novel manner
2. Interesting use of a VQA model to augment their training setup
3. Good use of diagrams to explain idea 
4. Clearly showcase qualitative improvements for selected cases

### Weaknesses
1. The generality of method on real world images (i.e. where visual concepts are not that easily disentangled) is unclear
2. Limited evaluation (only one set of quantitative numbers)
3. Some missing details (refer questions below)

* Table 1: Are you reporting CLIP score and human evaluation on same table?? 
Please point out CLEARLY that these are two different metrics in the Table caption. Or please separate into two Tables. This is highly confusing.

--- 
The authors sufficiently respond to raised concerns in rebuttal. 
1. The generality of the method (on real world images) is verified with multiple qualitative and quantitative evaluated added to appendix during rebuttal. 
2. Additional quantitative evaluation with comparison to more baselines are presented. 
3. The requested missing details are provided adequately. 

Due to these reasons, I vote to accept this paper.

### Questions
* Immediate question - why don't concept axis vectors collapse to same as text embeddings? Explain this more. 
* DeepFloyd - please cite appropriately 
* Consider more discussion on Textual Inversion (as related work), maybe in supplementary at least. Highlight cases where this is better than directly using text. 
* The work in [1] explores language defined concept axes in video domain - maybe an interesting comparison to discuss in related work  
* Please include BLIP-based baseline results also in Table 1
* Can you add more CLIP-score based (or a different new metric based) evaluations for other task (like concept extrapolation)? More quantitative evaluation could really strengthen the paper

[1] Ranasinghe, K., & Ryoo, M., Language-based Action Concept Spaces Improve Video Self-Supervised Learning, NeurIPS 2023

### Soundness
2 fair

### Presentation
3 good

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
This paper proposed a new framework for Visual Concept Learning. By introducing a set of concept encoders, concept embeddings could be extracted from the input image, which could be recomposed later to produce desired image. The experiments showed that these concept embeddings could capture the visual nuances and they are disentangled with each other. Besides, this framework can learn the shared concepts across instances(images), in other words, it is more efficient than previous methods.

The paper proposes a new framework for VCL task that avoids massive human annotation, and could boost the research in related fields. It also drew the attention to the research direction of using continuous embeddings (instead of relying on generic words) as the visual concept descriptors. The concept is commendable, although the depiction falls short of perfection and would greatly benefit from additional elaboration and intricate explanations.

### Strengths
a. Proposed the idea to use BLIP-2 generated embeddings as “anchor” (pseudo ground-truth embeddings) to “separate” the entangled concept embeddings.
 
b. This work proposed a framework to tackle Visual Concept Learning without human annotation, which is much more efficient than the previous works.
 
c. Unlike most of the Textual Inversion techniques, this work could capture the concept appearing in different images. Therefore, it does not require a retraining on each image. Also, the learning efficiency is higher because it can learn from a larger pool of images.

### Weaknesses
a. The datasets used for the experiment were small and simple. It is not guaranteed that the claimed conclusions could be maintained when this framework is applied on more complex datasets (with much more concepts). The idea of using anchors to ensure that the embeddings are disentangle is great, however more experiments on larger datasets should be done to prove it. Given that there are only 2 to 3 concepts in each domain, the sparsity of concepts might be one of the reasons why the embeddings are disentangle.
 
b. The effectiveness of L^{anchor} is not fully explained. The L^{anchor} is omitted during the test-time optimization procedure to avoid “over-committing to the coarse text anchors”. However, in the ablation experiment, the paper claims “disabling L^{anchor} deteriorates the performance”. It seems kind of contradictory, the paper should explain more about why “disabling L^{anchor}” is desired during one phase but it leads to unsatisfactory results in general evaluation.
 
c. The ablation test is not fully explained. In “Editing Category” column, the results of “w/o Encoder & L^{anchor}_k” is actually higher than the results of “w/o L^{anchor}_k” in two metrics. This does not fully conform to the conclusion, quote, “and further removing the encoder decreases the overall decomposition performance”.
 
d. It is hard for this framework to generalize to new “concept”. From what I understood, this framework could effectively generalize to new “mode” of seen “concept” (like new style or new color), but not to new “concept”. When applied to new concepts, e.g. “size” or “shape”, the corresponding concept encoders need to be trained. Also, from my perspective, we can’t only train the concept encoder of the new concepts. Because the sentence template “a photo of <e1> with <e2> color and <e3>  and <e4>...” needs to cover at least the majority of the concepts appeared to generate an image close enough to the original input image. Based on this understanding, when this framework is extended to new concepts, the trained concept encoders (of the seen concepts) need to be retrained together with the new ones. This setting is not more efficient than previous methods.

### Questions
a. On page 5, in sentence “text encoder c_{theta} of the T2I diffusion model…”, it should be “part of the text encoder c_{theta}”. Because a text encoder should take “text” as input rather than “text embeddings”. The original sentence might be confusing.
 
b. On page 5, in formula (1), there is no explanation about the N and U notation. I assume they represent “multivariate normal distribution” and “uniform distribution” respectively. It would be more clear to annotate.
 
c. On page 5, in sentence “so that they can directly inserted into the text embeddings”, it seems that a “be” is missed.
 
d. The paper should mention the backbone T2I model earlier. It is first mentioned on page 5, it would be better to do it earlier.
 
e. It would be better if the choice of using “12 CLIP layers” over “6 out of 12 tokens like Gal et al. 2023” is explained more in detailed.
 
f. More details could be added about the test-time lightweight finetuning process.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors claim that their proposed model can learn a language-informed visual concept representation, by simply distilling large pre-trained vision-language models.

### Strengths
The authors claim that their proposed model can learn a language-informed visual concept representation, by simply distilling large pre-trained vision-language models.

### Weaknesses
1. What is concept representation learning? Is concept learning just the mutual translation of text and images?

2. In the experiments, the authors primarily focus on conducting investigations using synthetic datasets. However, it raises concerns about the generalizability of the conclusions/findings obtained from synthetic datasets to real-world datasets.

3. The concept learning should focus more on the understanding of concepts, especially at different granularities of the same concept.

### Questions
Please refer to Weakness.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents a method for learning concepts by distilling knowledge in a text-to-image generative model. The method assumes concept axes, in each of which specific information of an input image is encoded (like colors, materials, and object categories). The method learns a designated encoder for each concept axis with generated images. For training the encoders, the method uses an anchor loss for each axis based on a VQA model to further disentangle the axes and a reconstruction loss. The method is evaluated qualitatively and quantitatively (CLIPScore and human evaluation).

### Strengths
(1) The paper is well-written. I can easily follow what is done in the method.

(2) The method is simple and can be trained in 12 hours only with less than 1000 generated images, yet outperforming the similar existing methods. 

(3) The image generation results are really nice compared to the existing approaches.

### Weaknesses
(1) The performance of the method is mostly shown in qualitative evaluations. The quantitative evaluation only shows the performance of image generation by modifying some concept axes (and human evaluation). I think the paper would be better if it came with an objective quantitative evaluation of the obtained concepts themselves in some ways (though I didn’t come up with any good approaches for this). 

(2) Related to (1), I’m not sure if CLIPScore is really sensitive to arbitrary combinations of concepts. Some references or experimental results may help understand the experiment. 

(3) The paper’s purpose is not sufficiently clear. Is it to learn concepts for image generation? Or is it for some other downstream tasks?

### Questions
I would like to have some responses for (1)-(3) in the weakness section.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
