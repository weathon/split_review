# 3DAxisPrompt: Promoting the 3D Grounding and Reasoning in GPT-4o

- Decision: Reject
- Scores: 3, 3, 3, 6

## Abstract
Multimodal Large Language Models (MLLMs) exhibit impressive capabilities across a variety of tasks, especially when equipped with carefully designed visual prompts. However, existing studies primarily focus on logical reasoning and visual understanding, while the capability of MLLMs to operate effectively in 3D vision remains an ongoing area of exploration.
In this paper, we introduce a novel visual prompting method called 3DAxisPrompt to elicit the 3D understanding capabilities of MLLMs in real-world scenes. More specifically, our method leverages the 3D coordinate axis and masks generated from the Segment Anything Model (SAM) to provide explicit geometric priors to MLLMs and then extend their impressive 2D grounding/reasoning ability to real-world 3D scenarios. Besides we also provide a thorough investigation of the potential visual prompting formats and conclude our findings to reveal the potential and limits of 3D understanding capabilities in GPT-4o. Finally, we build evaluation environments with four datasets, {\it i.e.} ShapeNet, ScanNet, FMB, and nuScene datasets, covering various 3D tasks. Based on this, we conduct extensive quantitative and qualitative experiments, which demonstrate the effectiveness of the proposed method. Overall, our study reveals that GPT-4o, with the help of 3DAxisPrompt, can effectively perceive an object’s 3D position in real-world scenarios. Nevertheless, a single prompt engineering approach does not consistently achieve the best outcomes for all 3D tasks. This study highlights the feasibility of leveraging MLLMs for 3D vision grounding/reasoning with prompt engineering techniques.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper focuses on significantly enhancing the understanding of 3D spatial information by mature LLMs like GPT-4-O through the use of different forms of prompts.

### Strengths
This paper focuses on significantly enhancing the understanding of 3D spatial information by mature LLMs like GPT-4-O through the use of different forms of prompts.

### Weaknesses
This paper focuses on significantly enhancing the understanding of 3D spatial information by mature LLMs like GPT-4-O through the use of different forms of prompts.

This paper focuses on significantly enhancing the understanding of 3D spatial information by mature LLMs like GPT-4-O through the use of different forms of prompts. However, I have the following questions: 1. To what extent does this method improve some 2D LLMs, such as LLAVA-NEXT? 2. In addition to the benchmarks listed in the paper, can this method be applied to more benchmarks? I need more confidence and evidence of improvements on widely recognized benchmarks. 3. This method seems a bit too simplistic; please restate its innovativeness and necessity, as well as how it differs from similar approaches. If necessary, more visualizations can be provided.

### Questions
This paper focuses on significantly enhancing the understanding of 3D spatial information by mature LLMs like GPT-4-O through the use of different forms of prompts. However, I have the following questions: 1. To what extent does this method improve some 2D LLMs, such as LLAVA-NEXT? 2. In addition to the benchmarks listed in the paper, can this method be applied to more benchmarks? I need more confidence and evidence of improvements on widely recognized benchmarks. 3. This method seems a bit too simplistic; please restate its innovativeness and necessity, as well as how it differs from similar approaches. If necessary, more visualizations can be provided.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
The authors proposed 3DAxisPrompt, which is a prompting method for 3D grounding questions for multimodal large language models (MLLM). The prompting basically consists of two parts: 1) add the 3D axis to the point cloud and render observation images from multiple views of the point data; 2) add masks/boundboxes generated from SAM in the rendered image to provide explicit geometric priors.The authors test the proposed prompting on GPT-4o (ChatGPT interface) on 20 scenes from each test dataset (ShapeNet, ScanNet, FMB and nuScenes) and show that such prompting can help GPT-4o interpret 3D space.

### Strengths
- The paper is well-written and lucidly presented.
- The related work section provides a comprehensive overview of MLLMs and prompting techniques.
- The prompting method is straightforward and easy to apply.
- The authors demonstrate the efficacy of the 3DAxisPrompt on a limited set of scenarios through indoor localization/route planning on ScanNet, outdoor localization on nuScenes, and robot action prediction on FMB dataset.

### Weaknesses
 - Limited contribution: The primary contribution of this paper is the 3DAxisPrompt prompting method for MLLM, along with testing GPT-4o on such prompts. The prompting method is straightforward and simple. While it is generally beneficial to present a simple method, I anticipate an in-depth analysis demonstrating its essentiality and key to resolving the problem. However, the paper lacks scientific investigation into why MLLM can perform 3D grounding with the proposed prompting and does not provide a novel perspective on the problem. The paper’s structure resembles a technical report rather than a conference contribution.
- Evaluation issues:
    - Quantitative evaluation of adding 3D axis: The proposed 3DAxisPrompt comprises two parts, but there is no quantitative evaluation of the first part (adding 3D axis) presented in the paper.
    - Baseline methods: There is no baseline shown in table 1 and 2 and it is hard to interpret the numbers in the tables.
    - Scientific validity and significance: The evaluation of the proposed 3DAxisPrompt is not scientifically valid or significant. The paper evaluates the proposed 3DAxisPrompt on only a single pre-trained MLLM model (GPT-4o) on a very limited set of scenes. It is challenging to ascertain the scientific significance of the results obtained from such a limited set of scenes. Furthermore, without testing on other MLLM models, it remains uncertain whether the proposed prompting can generalize.

### Questions
Typo:
- L349: rend -> trend.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces 3DAxisPrompt, a new visual prompt method to enhance 3D understanding and reasoning in MLLMs. It explores various visual prompts, including 3D axes, tri-view images, 2D contours, and 3D edge points. Experiments are conducted on several self-designed tasks, such as indoor/outdoor localization, route planning, robot action prediction, and coarse object generation.

### Strengths
The paper explores a range of visual prompts (coordinate axis, masks, bounding boxes, marks, color highlights) for 3D grounding and reasoning, tested on several self-designed tasks like indoor localization, robot action prediction, and route planning.

### Weaknesses
1. The term "3D grounding ability" seems overstated, as the paper only assesses its own indoor localization tasks without referencing established benchmarks like ScanRefer or Referit3D.

2. The paper lacks comparisons with existing methods on standard benchmarks, which are essential to reveal its limitations or gaps relative to current learning-based and prompt-based 3D grounding approaches, such as LLM-Grounder [1]. By only testing its performance in isolation, the study fails to demonstrate an advantage over other methods. It would be more convincing if the authors:
- Provide results comparison on comprehensive, widely accepted benchmarks (e.g., compare directly with public 3D grounding, 3D detection, or 3D QA datasets),
- Demonstrate real-life applications, as seen in works like PIVOT, by applying the method to practical scenarios.

3. The paper lacks an in-depth analysis of view selection in real-world settings. For instance, real-world 3D axes often cannot be perfectly aligned with point clouds. Is there a systematic study on this effect or a solution for optimal view selection? Additionally, could zooming in and applying axis prompts improve localization accuracy? Addressing these technical details would enhance the paper’s guidance on effectively using axis prompts.

### Questions
See the weakness.

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a novel approach to enhance the capabilities of Multimodal Large Language Models (MLLMs) in understanding and reasoning about 3D environments. The authors propose a new prompting mechanism, 3DAxisPrompt, which integrates 3D geometric priors by embedding 3D coordinate axes and meshes into the scene. This method aims to extend the existing 2D grounding and reasoning capabilities of MLLMs into the 3D space without requiring further fine-tuning.
The paper discusses various visual prompting techniques and their effectiveness in improving visual grounding, highlighting the limitations of current methods in fully activating the fine-grained 3D perception capabilities of MLLMs. The authors conduct comprehensive evaluations using different datasets to assess the performance of their proposed method, demonstrating its potential to enhance the understanding of spatial relationships in 3D contexts.

### Strengths
1. The proposed visual prompting method 3DAxisPrompt is novel and has been proven to enhance the 3D understanding capabilities of MLLMs. With the proposed technique, the MLLM can be directly adapted to localization, route planning, and action prediction without the need for additional training.
2. The authors conducted extensive quantitative and qualitative experiments across multiple datasets (ShapeNet, ScanNet, FMB, and nuScene), to show the effectiveness of their proposed method in various 3D tasks. 
3. The methodology is well-defined and clearly stated, which allows for reproducibility and further investigation by peer researchers.

### Weaknesses
1. How are the 3D axes set? Does the origin always lie in the same corner of the scene?  What if the axes are not well aligned with the scene's boundaries? In Figure 3-3, I noticed that the output of Y(=7.08) seems not very accurate compared with the other aligned ones. 
2.  The idea is very interesting. However, I still need to point out that the runtime of the model inference is not efficient enough for the practical problems (planning, localization, etc.) discussed in the paper. 
3.  The phenomenon that the MLLM has the capability to perceive the object's 3D position is interesting. However, the pipeline requires external models like SAM to first get the masks/other auxiliary markers to highlight the target object. Step back and think about the whole pipeline, it only proves that the MLLM can do a very simple task--- given a cartesian coordinate system represented by 3 orthogonal axes and a 3D point, MLLM is asked to output the coordinates of this 3D point.  I think it would be interesting to experiment with the simplest case mentioned above to see if the MLLM can output the arbitrary 3D point's coordinates and how accurate it is.  So that we can better understand if the semantics in the 3D scene help in the localization process. 
4. It would be more interesting if more types of coordinate systems could be tested. For example, polar coordinate systems and cylindrical coordinate systems. We can also test on some self-defined coordinate systems, for example, with log-scaled axes.   
I am curious about how MLLM possesses such spatial sensing capability without direct training. I wonder if there are many images of cartesian frames contained in the training data.

### Questions
Please refer to the weakness part.

### Soundness
3

### Presentation
4

### Contribution
3
