# LVLM-COUNT: Enhancing the Counting Ability of Large Vision-Language Models

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 6, 3, 6

## Abstract
Counting is a fundamental skill for various visual tasks in real-life applications, requiring both object recognition and robust counting capabilities. Despite their advanced visual perception, large vision-language models (LVLMs) struggle with counting tasks, especially when the number of objects exceeds those commonly encountered during training. We enhance LVLMs’ counting abilities using a divide-and-conquer approach, breaking counting problems into sub-counting tasks. Unlike prior methods, which do not generalize well to counting datasets on which they have not been trained, our method performs well on new datasets without any additional training or fine-tuning. We demonstrate that our approach enhances counting capabilities across various datasets and benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper addresses the problem of counting objects in images using large vision-language models (LVLMs), which often struggle with counting tasks, particularly when the object count exceeds typical values encountered during training. The authors propose a method named LVLM-Count, which aims to enhance LVLMs' counting abilities through a divide-and-conquer approach. LVLM-Count is structured in four stages: (1) Area Detection, where regions containing relevant objects are identified; (2) Target Segmentation, in which these regions are segmented to highlight individual objects; (3) Object-aware Division, where regions are divided into sub-images without cutting through the segmented objects; and (4) Counting Aggregation, where the LVLM counts objects in each sub-image and combines the results to produce the final count. The proposed approach is claimed to generalize well to new datasets without additional training or fine-tuning, showing improved performance on various datasets and benchmarks compared to prior methods.

### Strengths
This paper explores a relatively novel approach by focusing on enhancing counting capabilities in large vision-language models (LVLMs) using a training-free methodology. By leveraging the power of LVLMs, the authors propose an effective paradigm that does not rely on additional training or fine-tuning, which is particularly advantageous in scenarios where labeled data is limited or unavailable. The method demonstrates a creative approach to addressing challenges in object counting, especially in cases with a high number of objects and significant object overlap. By employing a divide-and-conquer strategy, the proposed LVLM-Count effectively manages the complexity of densely populated scenes, providing a practical and scalable solution for counting tasks that would typically challenge standard vision models. The paper’s emphasis on a training-free framework in conjunction with LVLMs is both innovative and valuable, offering a flexible counting solution that could be adapted to various applications without the need for retraining.

### Weaknesses
This paper also presents some limitations, as acknowledged in the final section. The proposed method heavily relies on the accuracy of the initial stages—specifically, object detection and instance segmentation. If either of these stages is inaccurate, it could significantly affect the downstream steps, potentially compromising the overall performance. This dependency raises questions about the robustness of the method on more challenging datasets, especially those with high levels of occlusion or camouflage, where accurate detection and segmentation are inherently more difficult. Additionally, the comparison with existing methods is relatively limited. To strengthen the paper’s persuasiveness, it would be beneficial for the authors to include more comprehensive comparisons with other state-of-the-art counting methods. Lastly, the paper would benefit from further ablation studies, such as an investigation into the impact of each stage in the pipeline. For instance, an ablation study examining the effect of including or excluding the target segmentation stage could provide insights into its significance within the proposed approach. These additions could help validate the robustness and effectiveness of the method across diverse scenarios.

### Questions
The questions are in weakness part.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper aims to improve the counting ability of large VLMs. The paper proposes to split a counting task into sub-tasks by dividing the input image into smaller parts, counting objects in the smaller parts, and then aggregating the counts. The authors show that the proposed approach can generalize to unseen datasets.

### Strengths
The results obtained and demonstrated in the paper seem strong.

### Weaknesses
The main weaknesses of the paper lie in the lack of enough support for the claims made. In particular, the authors should address the following questions/comments in their responses and revisions:

1. In several places in the paper (e.g. lines 61-62), the authors mention that pipeline detects "the objects of interest". Are there even more than one types of objects to be counted in these datasets? If yes, how are objects of different categories handled? All the visual examples in the paper involve only a single type of object. 

2. In line 349, the authors talk about "simple" and "complex" counting questions. What do these mean in this context?

3. Lines 241-242 say "In out experiments, we specify which approach we use for each dataset". Having different approaches for different datasets (outside of a few hyper-parameters) defeats the point of proposing a single approach for a problem. This is problematic, particularly because one of the selling-points of this paper is the claim that the proposed approach generalizes across datasets. 

4. The introduction mentions "industry, healthcare, and environmetal monitoring" as the areas of application. It would have been useful if the paper actually included some real-world examples from these domains to demonstrate the utility of the proposed approach.

### Questions
Please see the weaknesses section.

Edit: Updated rating from 3 to 6 after reading the authors' responses and updated manuscript.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes LVLM-Count, a prompt-based, training-free counting approach that enhances object counting performance with large vision-language models (LVLMs).  For addressing limitations with current LVLMs, such as their challenges with high-count tasks and complex counting questions, this method employs a four-stage pipeline: (1) area detection, (2) target segmentation, (3) object-aware division, and (4) target counting. This enables LVLMs to effectively segment, process, and count large numbers of objects across diverse datasets, showcasing robust generalization.

### Strengths
A simple and intuitive pipeline for counting with LVLM

Good presentation along with clear drawn figures.

A newly introduced Emoji-Count benchmark is introduced, though the generation of this data is not complex but still useful as a testbed.

Good performance margin achieved.

### Weaknesses
W1: At the very beginning, the authors should define more clearly what means by large number of objects, 10s, 100s, or 1000s, per image. As this defines the scope of this work in terms of crowdedness.

W2: The key idea of this work, divide-and-conquer, can be hardly considered novel for two reasons: 1) in this context, counting by definition is a process of adding the number of objects from region to region. It is essential a process of summing up across regions; 2) Such an idea has appeared in the counting literature such as [Ref 1] where there is also a need for avoiding repeatedly computing regions within an image. As a result, this whole method pipeline is not sufficiently novel -- it is more like a baseline design of using LVLM for counting.
- [Ref 1] Xiong H, Lu H, Liu C, Liu L, Cao Z, Shen C. From open set to closed set: Counting objects by spatial divide-and-conquer. InProceedings of the IEEE/CVF international conference on computer vision 2019 (pp. 8362-8371).

W4: It is inconsistent than different examples are used from Fig 3 to Fig 5 when discussing individual components. From these examples, little challenges are visible with counting, and I am impressed that simply counting the mask of GroundingDINO would achieve good performance, even not bother LVLM such as GPT-4o. For example, simply counting the mask number in Fig 4(c) can give us very accurate count. I would suggest the authors use the same example with proper challenges involved and considered in this work, across all these sections.

W5: This method uses a number of pretrained models such as LLMs, GroundingDINO, and GPT-4o, Real-ESRGAN. One concern is about efficiency. The authors should conduct an efficiency analysis in both training and inference, which is now missing.

W6: Except the comparison with previous works, I suggest a couple of baseline methods should be included in this work:
1) LLM + GroundingDINO: After target segmentation step (Sec 3.2), directly counting the masks by SAM. This can be use to validate the significance of region division, a key aspect of this work. This complements to the ablation result of using GPT-4o in Table 4 (Appendix).

2) Passing the SAM's mask to GPT-4o to count: This will directly compare the proposed object aware division algorithm.

3) To compare with Ref 1's strategy on avoiding repeated counting at the region level

W7: In ablation study, it is suggested that the authors examine the effect of using super-resolution on the regions.

W8: Please clarify what LLM is used in this work?

W9: Except those datasets used, another good test is PASCAL VOC. This should add different test cases on top. The authors can consider to evaluate.

### Questions
Please check weaknesses above

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes LVLM-Count, a plug-in method for current LVLM to enhance the visual perception on counting ability. The method uses an extra module with object-aware division, which can divide multi objects without cutting through objects of interest. Also the paper proposes a dataset for testing the counting ability of LVLMs. Compering other method, the proposed method achieves good performance on different benchmarks.

### Strengths
This paper provides good thinking and novel insights for a very important domain about LVLMs: visual counting ability of LVLM.

* The paper proposes a novel and simple method for dividing objects without cutting, which is meaningful for visual perception and the inference logic of LVLMs.

* The paper can deal with complex scenarios and achieve high performance on large mount of objects.

* The proposed benchmark looks very interesting.

### Weaknesses
I have some concerns about the paper and hope the authors can address them:

* The motivation and method looks good but the experiment results may not support them very well. In the section of experiments (Section 4), there should be some ablations about the designed method. Specifically, it's unclear how much each component of the proposed method contributes to the overall performance. For example, what is the performance gain from object-aware division compared to a naive division strategy, and how does the area detection module impact the final counting accuracy? These ablations are essential to validate the design choices.

* The metrics of evaluation may not be enough for well evaluating a LVLM's counting ability. Maybe there are two situations about counting: 1) we need an approximate number of objects. 2) we need an exact number of objects. Current metrics may can only evaluate the first case. So I think you could add more metrics on all benchmarks, such as Accuracy (right cases / total cases, same with EA, but EA is only used for one benchmark). Also you can set different ranges of the Acc, e.g., you can firstly set Acc_{+-0} which means that the answer must be the exact number of objects without any difference. Then you can set Acc_{+-3} which means that the answer is acceptable with in +-3 error numbers. Following this you can set Acc_{+-5}, Acc_{+-10}. This would provide a more granular understanding of the counting performance across different error tolerances.

* The method you proposed is actually a plug-in method for any LMLM. So it is a little weak that you only combine it with one LVLM (GPT4o). You should involve more LVLMs such as LLaVA series, Genimi, etc. This would demonstrate the generalizability and robustness of the proposed method across different architectures and model capabilities. The current evaluation is limited by only using one model.

* The outputs of the LVLM are always natural languages, how do you make sure that every response is about the counting? how do you avoid the problem of the model giving irrelevant responses? It's crucial to address how the system ensures the LVLM focuses solely on counting and avoids generating extraneous information. The paper should detail the prompting strategy or any other mechanism used to enforce this.

* In addition to the very incomplete quantitative results, there are also very few qualitative results. The qualitative results are only tested on one dataset. I would like to see the qualitative results and accuracy of image_00001.png, image_00005.png, image_00013.png, image_00036.png, image_00068.png in emoji_benchmark.

The main problem is the incompleteness of the experimental part. If the authors have a positive response, I will consider raising my rating.

### Questions
The main evaluations have been listed. I hope the authors can think about the following questions:

* How can the counting ability of LVLMs be better utilized?

* As LVLMs become more and more powerful, will the method proposed in the paper soon become outdated?

* The proposed method seems to work well when there are a large number of objects, so what is its upper limit? Is it okay when there are 500 objects? How about 1000 objects? So what are the advantages of the proposed method?

### Soundness
3

### Presentation
2

### Contribution
3
