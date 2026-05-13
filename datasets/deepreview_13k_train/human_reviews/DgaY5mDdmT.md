# MLLMs Know Where to Look: Training-free Perception of Small Visual Details with Multimodal LLMs

- Decision: Accept
- Scores: 5, 8, 8

## Abstract
Multimodal Large Language Models (MLLMs) have recently achieved promising performance on visual question answering (VQA)---a fundamental task affecting various downstream applications and domains. Given MLLMs' potential integration into many critical VQA applications, it is important to understand the limits of their perception. In this work, we study whether MLLMs can perceive small details as well as large details in images. In particular, we observe that their accuracy in answering visual questions is very sensitive to the size of the visual subject of the question. We further show that this effect is causal by observing that human visual cropping can significantly mitigate this sensitivity. Next, we study the attention patterns of MLLMs when answering visual questions, and intriguingly find that they consistently know where to look, even when they provide the wrong answer. Based on these findings, we then construct automatic visual cropping methods that leverage the internal knowledge of any MLLM itself, in the form of attention and gradient maps, to help it better perceive the small visual subject of any question. We study our proposed methods on two MLLMs and seven visual question answering benchmarks, and show that they can significantly improve MLLMs accuracy without requiring any training. Our findings suggest that MLLMs should be used with caution in detail-sensitive applications, and that visual cropping is a promising direction to improve their performance.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper studies the perception limitations of Multimodal Large Language Models (MLLMs) when dealing with small visual details in images, and proposes training-free visual cropping methods to mitigate these limitations. The key contributions are: (1) demonstrating that MLLMs struggle with perceiving small visual details despite knowing where to look in images, (2) showing this limitation is causal through intervention studies with visual cropping, and (3) developing automatic visual cropping methods that leverage MLLMs' internal attention and gradient information to improve their perception without any additional training.
The paper makes a valuable contribution by rigorously analyzing an important limitation of MLLMs and providing practical solutions. However, there are some points that need clarification and potential improvements that could strengthen the work.

### Strengths
* This paper propose an interesting problem that MLLM seems know which areas should be focused but still fails to solve the related problem successfully all the time. By conducting intervention study, the problem is validated.

* The proposed methods are intuitive and straightforward to the problem mentioned and make good use of the finding from the pilot study.

### Weaknesses
 * The evaluation part is not so well done given the baseline is just no croping without any other fair comparison. V* (star) may be a good baseline since they tried to address a similar problem like this paper brought about. 

* The existing approach seems achieve limited improvement by up to ~4% even compared to no-crop setting across all 8 benchmarks.

* The role of model architecture in determining perception limitations isn't explored

### Questions
* Like mentioned in the first point of  weakness, How will traditional grounding algorithms help address the problem  under similar setting? Why viscrop instead of that? 

* How does the method handle cases where the visual subject spans multiple regions of interest?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper identifies a drawback of MLLMs in VQA when questions concern small-sized objects in the images. It shows empirically that MLLMs perform worse on such questions, and that their performance is due to perception issues but often they are able to attend correctly to the relevant regions of the image (localization). With these two insights, they propose a method based on visual cropping which computes attention maps of the MLLM through various methods, and uses these attention maps to derive a cropped version of the image which is appended to the original image and passed through the MLLM. They show empirically that on VQA datasets involving fine-grained questions (e.g. TextVQA), this inference-time approach outperforms the base MLLM, while maintaining performance on general VQA datasets.

### Strengths
This paper identifies an important problem in MLLMs, specifically their lack of sensitivity to small details in images in a VQA context. Moreover, it pairs this with an original and useful insight -- that often the MLLM can attend correctly to the relevant region of the image, even if it produces the wrong answer. This observation may not have been recognized previously. Moreover they turn this analysis into a practical method which generates an attention map and uses this to crop the image. The method has several advantages -- it is intuitive, fits well into the framework of pretrained MLLMs, and works at inference-time without further training.

Empirical results on Table 2 are convincing and show that their method significantly outperforms the base MLLM on detail-sensitive datasets. 

The paper is also written well and has good clarity.

### Weaknesses
I wonder whether the drawback of MLLMs for small-sized objects for vision-language tasks has been noted before. For example, some work is mentioned in Lns 287-288 on training MLLMs with higher-resolution patches. It would be good to understand related work that has addressed the problem of small-sized objects for MLLMs generally and/or VQA specifically. This could potentially be added to the related work. 

The method assumes that there is a single relevant location of attention in the image; this is not always true,  for example in questions that ask about spatial relationships between objects. The authors note this when they discuss limitations. It is not inconceivable that the approach could be extended to such questions if attention maps are sufficiently informative.

### Questions
(Sec. 3) Human-crop is a very strong intervention where the crop is tight around the ground-truth object. It would be nice to see how accuracy improves for more realistic crops. For example, one experiment -- crop around objects in the "small" dataset s.t. the proportion of its size in the image is equal to the average proportion value in the "medium" and "large" datasets. Does the accuracy improve, maybe matching the accuracy of the medium and large splits?

(Sec. 4) Is this a standard way to calculate attention in transformers? If I am understanding right -- I am not sure how interpretable attention values are in later layers, where the input tokens have already been transformed significantly. How does this method compare to prior work on attention in MLLMs/vision transformers? Also, it would be nice, if feasible, to evaluate variants of GradCam for transformers as another attention method. These are mentioned in the related work. 

(Sec. 4) It'd be interesting to get more intuition on when the MLLM produces correct attention when giving an incorrect answer, and when it does not. I imagine that in the exit or bicycle number case in Fig. 2, it seems reasonable to produce correct attention. In the car question I'm a bit surprised this works since it's just asking about existence of the object -- proper localization seems to imply that the model also perceived the car correctly.

(Sec. 6) A simple baseline here would be to provide a random crop; crop the image at a random location, perhaps half the size of the original image, and provide this as additional input to the MLLM. This would reinforce the analysis in Sec. 4, and show that the accurate localization of the MLLM provides informative crops. It would be nice to show the results of such a baseline.

Minor questions
- What is the "input image resolution" in line 356? Is that the size of the patches input to the MLLM, or the image resolution? Clarifying since the multiples are >= 1.
- What is the reason for the oscillatory behavior in Fig. 3?

### Soundness
3

### Presentation
4

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
This paper studies the attention patterns of MLLMs when answering visual questions, and investigate into do MLLMs know where to look at, i.e. the perception problem v.s localization problem. Based on these findings, this paper introduces an automatic visual cropping methods leveraging attention and gradient maps, to help it better perceive the small visual subjects. The proposed methods is evaluated on two MLLMs and seven VQA benchmark and demonstrates significant improvement.

### Strengths
1. This paper studied the perception v.s localization problem for small visual objects and introduced insightful findings. 
2. It introduced a training-free method to help MLLMs better perceive the small visual subject of any question.
3. Experimentally, it demonstrated significant improvement in 7 benchmarks and on two MLLMs.

### Weaknesses
1. To help the model keep the global visual information, the cropped object introduced extra tokens. As illustrated in paper's Table 4, it indeed introduced some computational latency. But I suggest the author could try this approach (Matryoshka Query Transformer for Large Vision-Language Models (NeurIPS 24)) on the cropped object to save the visual tokens, as the re-scaled cropped objects intuitively don't have much visual detailed information. 
2. The improvement on general VQA benchmarks such as large visual concepts are not as significant as on small visual concepts.

### Questions
1. I'm curious to see, have the authors tried and explore methods to add the cropped visual object to the original image instead of concatenating two images together. Would that bring to on par or better performance with current approach and save the computation cost. 
2. I incline to accept this paper unless I saw critical drawbacks that I missed from other reviewers.

### Soundness
4

### Presentation
4

### Contribution
3
