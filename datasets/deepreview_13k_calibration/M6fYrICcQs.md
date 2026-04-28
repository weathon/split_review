# Chain-of-region: Visual Language Models Need  Details for Diagram Analysis

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
Visual Language Models (VLMs) like GPT-4V have broadened the scope of LLM applications, yet they face significant challenges in accurately processing visual details, particularly in scientific diagrams. 
This paper explores the necessity of meticulous visual detail collection and region decomposition for enhancing the performance of VLMs in scientific diagram analysis. We propose a novel approach that combines traditional computer vision techniques with VLMs to systematically decompose diagrams into discernible visual elements and aggregate essential metadata. Our method employs techniques in OpenCV library to identify and label regions, followed by a refinement process using shape detection and region merging algorithms, which are particularly suited to the structured nature of scientific diagrams. This strategy not only improves the granularity and accuracy of visual information processing but also extends the capabilities of VLMs beyond their current limitations. We validate our approach through a series of experiments that demonstrate enhanced performance in diagram analysis tasks, setting a new standard for integrating visual and language processing in a multimodal context.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper developed a new method called "Chain-of-Regions." This method is to help language models to accurately understand the visual information present in a figure such as scientific graphs or diagrams. While general models like GPT have great capabilities to understand images accurately, some gaps need to be filled. The novelty of this paper lies in that the authors adopted traditional CV techniques (not deep learning models) to decompose the image before feeding the broken-down parts into the visual language model.

The proposed CoR method involves a three-step process. The first step (Region Initialization) is to break down regions using connected components analysis offered by OpenCV. This initially identified regions further analyzed in the second step (Region Splitting). The second step further identifies detailed components in each region by checking whether common geometric shapes exist or unstructured shapes that can be identified from the liquid filling analogy. Lastly, the third step (Region Merging) finally checks how many regions can be practically processed in order to make it computationally efficient enough.

Based on the proposed CoR method, the authors report significant improvement in performance in region segmentation. The authors also conducted various ablation studies that confirms each step's contribution to the overall performance enhancement. With regard to implementation, the refreshing point is that this CoR method can be run on CPU only.

### Strengths
1) The novel and refreshing contribution of this paper is that employing old computer vision techniques in a smart way can be very helpful with modern visual language models. Inspired by this paper, future studies may look into such possibilities to replace certain parts of the language model pipeline.

2) The nice thing about the CoR method is that it can be solely run on CPUs (because it only uses OpenCV's connected component analysis and shape detection algorithm), which means it's very cost-effective and probably fast too.

3) The results look solid, as shown by the extensive ablation studies.

4) Another nice property of this method is that it can be used in a Plug-and-Play fashion with the existing visual language model pipeline. This is actually a good property because it can actually have some practical impact in this ever-growing LLM era. The proposed method's versatility in identifying different shapes also makes it easily adopted in the operating pipeline as a new component.

5) Lastly, this proposed method is clearly a white-box approach, which is transparent in showing why the regions were split in a certain way.

### Weaknesses
1) One thing that I find a bit short is the theoretical justification of why the authors made certain technical and/or methodological choices. I think the implementation and the practical implications are strong, but the authors fall short of explaining why their approach works better. The three steps of Region Initialization, Region Splitting, and Region Merging make sense to me, but having a more well-written formal justification of these steps would make the paper rock solid. Specifically, the paper lacks a discussion on how the choice of connected component analysis impacts the downstream performance compared to other segmentation methods. A more rigorous analysis of why this specific method was chosen over alternatives is needed. Furthermore, the paper does not provide a formal definition of what constitutes a 'region' and how this definition influences the subsequent steps. This lack of formalization makes it difficult to assess the generalizability of the approach.

2) While the authors compare the CoR method with SAM2, I wonder how the CoR method performs compared to other specialized models for processing scientific diagrams. While impressive, the results would be more robust if the authors could present a bit more head-to-head comparisons with competing models and/or approaches. The paper should include a comparison with models specifically designed for scientific diagram understanding, such as those that use graph neural networks or other structured representation learning techniques. This would provide a better understanding of the relative strengths and weaknesses of the proposed method.

3) The results are unanimously great, which is good of course, but it also makes me wonder what is the boundary condition and where this approach fails. Currently, the results look just too good. Knowing when and where a model fails is very helpful for future studies to build upon. In addition, the limitations that the authors acknowledge at the end are just nominal---there may be some other geometric shapes in our library. I want to hear about the real limits of this approach. The paper needs to explore failure modes more thoroughly, including cases where the connected component analysis fails to properly segment regions, or where the shape detection algorithms are inadequate. A more detailed analysis of the types of diagrams where the method struggles is needed to fully understand its limitations.

4) Compared to Steps 1 and 2, I think Step 3 (Region Merging) needs a bit more clarification. It involves budget parameter B, but I don't find much justification or rigorous discussion on the choice of B. Discussing at least the trade-off between a large and a small B would be nice. The paper should include a sensitivity analysis of the budget parameter B, showing how different values impact the performance and computational cost. A more rigorous discussion on the optimal choice of B, considering the trade-off between granularity and computational efficiency, is necessary.

5) Since this paper's core novelty lies in the combination of a traditional method with a modern VLM, the authors need to explain better how the output of OpenCV and CoR is fed into and/or interacted with the VLM. The paper lacks a detailed explanation of how the region information (bounding boxes, segmentation masks, etc.) is encoded and passed to the VLM. A more thorough description of the interface between the OpenCV module and the VLM is needed, including the specific data structures and formats used.

### Questions
1) How does the proposed method fare on parsing out real-world scientific diagrams?

2) Did you consider using other operators or functionalities of OpenCV as alternatives to the connected components analysis and the shape detection algorithm?

3) The structured splitting part of Step 2 involves identifying commonly used geometric shapes. What shapes are included in the library, and how comprehensive are they in your assessment?

4) All the performance reported in the paper is about accuracy (correct me if I am wrong). However, the authors push cost and computation efficiency (CPU only) as the main strengths of their approach. Do you have any hint of comparisons about those computational complexities and how they scale?

5) As I mentioned in the weaknesses, I am particularly interested in learning more about the interface between OpenCV and VLM. How did you ensure the regions detected by OpenCV are correctly interpreted by the VLM downstream? Were there any possibilities of conflict between the two modules?

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
2

### Summary
This paper presents a method for scientific diagram understanding that combines traditional CV methods (i.e., region initialization, splitting, and merging) with VLM prompting. The approach is evaluated on two both MMMU scientific diagrams and a small-scale diagram segmentation dataset. Results indicate the superiority of the proposed method.

### Strengths
- I appreciate how this work recognizes that a key challenge of diagram understanding is parsing the details and proposes a method combining classical CV methods to complement VLMs.
- The authors benchmarked a wide array of prompting strategies in their first experiment.
- The overall narrative is easy to follow.

### Weaknesses
I want to preface this by saying that I am a relatively junior reviewer, so please take my comments with a grain of salt.
- The authors mentioned they developed some structured detectors to identify and parametrize visual elements in diagrams. The performance of the method also seems to depend on the diagram having homogeneous colors and structured patterns. This raises questions about the generalizability of the approach. In experiment 1, the authors only evaluated the method on MMMU alone. Therefore, I wonder how this partially heuristics-based method would fare on other datasets. Some extra experiments might be helpful for demonstrating the power of the method.
- Some crucial details about Experiment 2 (on segmentation) seem to be missing. How many diagrams are there exactly in the dataset used in experiment 2? The authors wrote "100+", but this seems very unrigorous... In addition, how were these diagrams selected? I noticed all examples shown for exp 2 are in grayscale, which leads me to wonder if they were specifically chosen to play to the strengths of the proposed method that is largely heuristics-based. In addition, only SAM2 was compared against CoR. Perhaps it would be helpful to include some additional baselines?

### Questions
1. How many diagrams are there exactly in the dataset used in experiment 2? The authors wrote "100+", but this seems very unrigorous... In addition, how were these diagrams selected? I noticed all examples shown for exp 2 are in grayscale, which leads me to wonder if they were specifically chosen to play to the strengths of the proposed method that is largely heuristics-based.
2. Can the authors provide a decomposition of the number of charts for each category in experiment 1 for the sake of clarity? 
3. What is a rough cost comparison of the different prompting approaches in Experiment 1? If CoR is very expensive compared to other approaches, would some form of inference-time scaling (e.g., generating multiple responses and using majority voting) improve baseline method performance? I'm not sure if this is a valid thing to do, so please feel free to argue if this is a bad idea.

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
3

### Summary
This paper introduces the Chain-of-Regions (CoR) technique to enhance VLM's fine-grained recognition and reasoning capabilities for scientific charts. It demonstrates performance across disciplines including mathematics, architecture, and electronics. This paper combines established computer vision techniques with emerging topics in cross-modal understanding. I appreciate the approach of combining traditional computer vision methods to assist in enhancing the model’s performance, and indeed, the work shows a thorough consideration of various experimental details. The following  are some suggestions that may help the authors improve this work.
Traditional computer vision techniques, including the use of OpenCV, tend to be relatively sensitive to parameters. Yet, in the paper, it seems that authors have not analyzed the sensitivity of these parameters or how the understanding of diagram may vary across different scenarios.
Additionally, the rule-based reverse engineering appears to lack sufficient robustness—there has not been a comprehensive investigation to form the systematic theoretical framework for pixel recognition, segmentation, extraction, and integration. I suggest strengthening the discussion on this point.
Notably, sequential segmentation and rule-based combination are insufficient, as they may disrupt semantic context. I suggest that authors incorporate innovative algorithms in future work to further explore the interrelationships between different pixel regions.
In terms of writing, I suggest that the authors provide more pseudocode for the operations instead of directly presenting OpenCV code.
The parameter “Budget B” may also introduce uncertainty in the interpretation of subsequent diagram, but the authors have not provided much discussion on this.
In the Region Input of Appendix A1, we obtained the Output of different VLMs. It seems that this output is scanned from left to right. However, if the rotation angles of these images differ, what would the result be in that case?

### Strengths
This paper combines established computer vision techniques with emerging topics in cross-modal understanding. I appreciate the approach of combining traditional computer vision methods to assist in enhancing the model’s performance, and indeed, the work shows a thorough consideration of various experimental details.

### Weaknesses
The limitations of this paper lie in the potential impact of parameter sensitivity on the final interpretation, as well as whether the overall framework is adequately supported by methodological foundations.

Traditional computer vision techniques, including the use of OpenCV, tend to be relatively sensitive to parameters. Yet, in the paper, it seems that authors have not analyzed the sensitivity of these parameters or how the understanding of diagram may vary across different scenarios.

Additionally, the rule-based reverse engineering appears to lack sufficient robustness—there has not been a comprehensive investigation to form the systematic theoretical framework for pixel recognition, segmentation, extraction, and integration. I suggest strengthening the discussion on this point.

Notably, sequential segmentation and rule-based combination are insufficient, as they may disrupt semantic context. I suggest that authors incorporate innovative algorithms in future work to further explore the interrelationships between different pixel regions.

In terms of writing, I suggest that the authors provide more pseudocode for the operations instead of directly presenting OpenCV code.

The parameter “Budget B” may also introduce uncertainty in the interpretation of subsequent diagram, but the authors have not provided much discussion on this.

In the Region Input of Appendix A1, we obtained the Output of different VLMs. It seems that this output is scanned from left to right. However, if the rotation angles of these images differ, what would the result be in that case?

### Questions
Traditional computer vision techniques, including the use of OpenCV, tend to be relatively sensitive to parameters. Yet, in the paper, it seems that authors have not analyzed the sensitivity of these parameters or how the understanding of diagram may vary across different scenarios.
Additionally, the rule-based reverse engineering appears to lack sufficient robustness—there has not been a comprehensive investigation to form the systematic theoretical framework for pixel recognition, segmentation, extraction, and integration. I suggest strengthening the discussion on this point.
Notably, sequential segmentation and rule-based combination are insufficient, as they may disrupt semantic context. I suggest that authors incorporate innovative algorithms in future work to further explore the interrelationships between different pixel regions.
In terms of writing, I suggest that the authors provide more pseudocode for the operations instead of directly presenting OpenCV code.
The parameter “Budget B” may also introduce uncertainty in the interpretation of subsequent diagram, but the authors have not provided much discussion on this.
In the Region Input of Appendix A1, we obtained the Output of different VLMs. It seems that this output is scanned from left to right. However, if the rotation angles of these images differ, what would the result be in that case?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents Chain-of-Region, a prompting method that enhances the capabilities of VLMs in scientific diagram analysis. This is achieved by cropping out regions of the diagram with traditional computer vision techniques based on heuristics and incorporating the extracted information into a master query. The effectiveness of this method is verified by evaluating the QA accuracy and the segmentation results on the MMMU dataset.

### Strengths
1. Practical methodology. This paper proposes a practical method for leveraging VLMs in scientific diagram analysis, allowing for plug-and-play generalization across models.
2. Significant performance gain. The method shows notable performance gains when applied to state-of-the-art models like GPT-4o.
3. Clear presentation. The paper is generally well-written, with clear figures that aid comprehension.

### Weaknesses
1. Limited generalizability. The method contains various heuristics tailored for scientific diagrams, limiting its applicability to more complex images. The reliance on OpenCV-based algorithms for region proposal makes it difficult to extend this method to images with more complex structures or textures. For instance, the current approach might fail on diagrams with overlapping elements or non-uniform backgrounds. Extending this method for segmenting such images can be very challenging, if not impossible.
2. Unclear intuition. The rationale for how adding information from regions enhances QA task performance is not clear. While the example in Fig. 1 demonstrates how prompts lead the VLM to predict values based on the numbers in the prompts, I can’t see how they can aid the reasoning of various types of diagrams, such as the node-link diagram in Fig. 2. The paper lacks a detailed analysis of how the spatial information from the cropped regions is utilized by the VLM to improve reasoning. Providing more examples of the QA results and analyzing them can help better clarify this. Specifically, it is unclear how the VLM leverages the pixel location data of the cropped regions to improve its understanding of the diagram's structure and relationships between elements.
3. Unfair evaluation. The evaluation in Sec. 4.2 appears biased, as ground truth annotations favor the proposed method. The human labels only include foreground masks, penalizing methods that incorporate background masks, even when the cropped regions are identical (see the masks for K(s+1)/s(s+2)(s+3) as an example). A more appropriate evaluation method would use the area of the ground truth $|M_{GT_{i}}|$ as the denominator in the mIoU calculation.

### Questions
1. Why are background masks included in the region initialization? They appear to contain minimal information in the provided examples. Also, would they be regarded as the “main regions with large area size” in the VLM-assisted structure recognition?
2. How beneficial is the unstructured split and merge approach for analyzing scientific diagrams? Illustrations requiring this method are often considered single entities, as shown with the server in Fig. 6.

### Soundness
3

### Presentation
3

### Contribution
2
