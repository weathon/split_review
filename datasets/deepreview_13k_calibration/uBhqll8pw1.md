# On Inherent 3D Reasoning of VLMs in Indoor Scene Layout Design

- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 5, 3, 3

## Abstract
Large vision-language models (VLMs) such as GPT-4o, Llama-3.2 have shown remarkable capabilities in visual understanding and reasoning, prompting us to test their off-the-shelf ability to reason and act as a 3D design assistant. This study investigates VLMs’ visual reasoning capabilities using 3D indoor scene layout synthesis i.e. placement of furniture in a room, as a test-bed. We study three key primitive abilities in this context: (1) communication of spatial locations, (2) reasoning about free space and object collision, and (3) reasoning about object alignment, orientation, and functionality, each crucial to creating a VLM agent-based scene layout synthesis pipeline. We evaluate five state-of-the-art VLMs, both proprietary and open, on a new dataset incorporating 3400 questions that assess VLMs’ current visual reasoning abilities in our context. Our findings reveal several remarkable insights: (1) VLMs consistently prefer normalized coordinates for spatial communication over absolute coordinates or pointing with image markers. (2) Contrary to expectations, VLMs perform best with simplified sketch based scene representation or, most strikingly, with no visual input at all, compared to detailed renderings. (3) Free space reasoning remains challenging, with performance only slightly above random guessing, though frontier models show significant improvement with collision checking tools. Surprisingly, free space reasoning with clear visible collisions in the image can also fail. (4) Reasoning about object alignment, size, orientation and functionality together compounds errors leading to near chance performance on our dataset. These findings serve to offer insights into current potential and limitations of using VLMs off-the-shelf towards developing advanced visual assistants capable of understanding and manipulating 3D environments.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper evaluates large vision-language models (VLMs) for their inherent 3D reasoning abilities in the context of indoor scene layout tasks, focusing on key spatial tasks like locating objects, reasoning about free space, and managing object alignment. Findings reveal that VLMs are often better at symbolic reasoning than at directly utilizing visual inputs, and they struggle with complex spatial tasks, such as preventing collisions and ensuring functional alignment in room layouts.

### Strengths
1. Task Decomposition. The study clearly breaks down scene reasoning into essential sub-tasks, making the evaluation framework easy to follow and understand.

2. Insight into VLM Shortcomings. The paper provides useful insights into the current limitations of VLMs, especially their over-reliance on language-based rather than visual-based reasoning, which highlights areas for further model improvement.

### Weaknesses
1. Unclear Positioning. The paper’s approach to 3D generation is somewhat ambiguous, as it abstracts the problem into a simplified 2D scene layout task. This positioning may limit the relevance of the findings to true 3D reasoning, as spatial complexity is reduced to single-plane reasoning rather than robust 3D spatial understanding.

2. Limited Dataset and Task Scope. The study focuses on a single-room setup using standardized indoor layouts and simplified tasks based on the 3D-FRONT dataset. This narrow scope fails to represent real-world 3D complexities, such as handling overlapping or interleaved objects, which are common in actual environments. For example, scenarios involving stacked furniture or layered decor, where objects partially obscure each other, are not addressed, limiting the study’s applicability to more realistic 3D spatial tasks.

3. Over-Reliance on Symbolic Reasoning. VLMs in this study default to symbolic rather than visual reasoning. This reliance raises concerns about their effectiveness in spatially complex tasks that require direct interpretation of visual inputs, thus questioning the applicability of the findings to tasks that need strong visual comprehension.

4. Single Data Source. The evaluation relies heavily on the 3D-FRONT dataset and does not incorporate diverse datasets that could better assess generalization. A wider range of data sources covering various spatial configurations and room types would provide a more comprehensive measure of VLMs’ 3D reasoning capabilities.

5. Incomplete Model Evaluation. The paper’s contribution focuses on defining new tasks and evaluating existing models, yet it lacks a broader comparison with other mainstream VLMs. A more thorough evaluation across a wider variety of models, potentially with an online leaderboard, would enhance the paper’s contributions by establishing a clearer benchmark for future research.

### Questions
1. Free-Space Reasoning with Minimal Visual Inputs. The study notes that VLMs often perform better with minimal or no visual inputs. Can the authors elaborate on why simplified visual representations or text-only prompts might lead to improved accuracy, and how this insight might influence future VLM design?

2. Evaluation Strategy for Task Complexity. For tasks where symbolic reasoning seems to dominate, have the authors considered introducing hybrid evaluation strategies that encourage models to rely more on visual inputs? Could certain prompt engineering or visual cues shift the balance towards true visual reasoning?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work designs three categories of 3D reasoning question-answering tasks situated in simulated bedrooms to evaluate Vision Language Models (VLMs) on their capabilities as potential assistants for indoor scene layout design. The authors designed questions in different types and different input modalities. Their experiments benchmarked a variety of commonly used proprietary and open-source VLMs. Their findings indicate that VLMs generally struggle to answer spatial-reasoning questions (type S2 and S3 in their paper) based on visual inputs and tend to rely only on text input. They also find that the VLMs can reason normalized coordinates much better than absolute coordinates and simple grid-like coordinate marks. The authors hope this benchmark and their discoveries can benefit the development of next-generation VLMs.

### Strengths
1) Accessing the spatial reasoning capabilities of VLMs has recently become an important direction, and this paper approaches it from the perspective of indoor scene layout design, which is a kind of novelty given that most of the literature in this area is very recent.

2) The experiments are extensive. The authors incorporated 3400 questions across various types and tested five modalities for five state-of-the-art VLMs ranging from proprietary to public models.

### Weaknesses
1. Lack of in-depth analysis. While the authors' efforts in exposing the limitations of the current VLMs are appreciated, it would grant the paper more impact on the community if they could further analyze possible reasons for these models' failures in 3D reasoning and even design new methods to try to mitigate these failures. [1], which is also referred to in the paper, is a great example. This will help the paper better meet the expectations of a top-tier conference like ICLR. Currently, the paper only indicates "underscore the need for improved training methodologies and data curation" in the conclusion without elaboration.

2. Inclusion of 3D LLMs. While the paper acknowledges this as a limitation, given the context of the tasks (3D reasoning / spatial reasoning), the reviewer believes it is important to include 3D LLMs in the experiments. The current evaluation focuses on 2D image inputs, which does not fully leverage the 3D nature of the simulated environments. This limits the scope of the benchmark and its relevance to true 3D understanding.

3. Diversity in room appearances. While details about the prompts and multiple images are provided in the paper, all the rooms seem to have the same appearance (square shape, wooden floor, and light brown walls). Including more shapes, colors, and textures in the dataset could improve the quality, realism, and generalizability of the dataset. The lack of variation in the visual environment may lead to models overfitting to these specific conditions, limiting their real-world applicability.

4. Embodied view is skipped for task type 3, limiting the experiment’s design and findings to scenarios where top-down or perspective views are available, such as indoor scene layout design. This reduces applicability to broader spatial reasoning tasks in embodied AI, where these views may not be accessible.

### Questions
1. Different prompting techniques can impact VLM performance. From the paper, it appears that the wording for specific question types remains the same. Have you tried using chain-of-thought prompting or applying visual prompts to the input images? Are there alternative phrasings for the questions in the dataset?

2. How should people leverage these findings from this paper in training a VLM with better spatial reasoning ability?

3. other minor issues:

> line 151 combaining -> combining
> 
> line 297, please revise. The sentence contains obvious grammar mistakes.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper systematically studies the ability of off-the-shelf VLM to reason about spatial relations. The authors design problems from 3 aspects, namely coordinate communication, free-space reasoning and complex joint reasoning to evaluate the performance of the VLM. Experiments show that VLM struggles at specific cases like absolute coordinates or markers as well as inherent error for reasoning as in the free-space understanding case.

### Strengths
1. The paper attempts to systematically evaluate VLM's ability to understand spatial relations rather than designing a pipeline for a specific case.
2. Extensive experiments are conducted to derive systematic conclusions.

### Weaknesses
1. The major issue with this work is the overclaiming of evaluating VLM for 3D reasoning while the efforts are all made on 2D. The experiments are limited to 2D floorplan layouts, which does not fully capture the complexities of 3D spatial reasoning. The paper does not explore how VLMs handle depth perception, occlusion, or varying viewpoints in a true 3D environment.
2. Since the efforts are all made on 2D, it is worth noticing that the findings in the paper are mostly well-studied in the previous literatures[1,2,3]. The paper's conclusions about VLM's limitations in spatial reasoning largely overlap with existing findings on visual grounding and multi-modal hallucination. The specific challenges identified, such as difficulties with absolute coordinates and spatial relationships, have been previously documented in the context of 2D image understanding.
3. The paper is poorly written, with bunch of typos in the main text and tables, making it hard to follow.

### Questions
1. Since the paper claims to study the problem in the 3D domain, it is suggested that the evaluation of the model should focus more on how to provide the right 3D representations or how to formulate the questions. For example, different angles of the rendered scene with no pre-defined coordinate systems to ask questions about spatial relations like left and right.
2. It seems like the paper is solely studying VLM's performance in a limited 2D domain, it would be beneficial if the authors could provide a clarification on how the task is different from or harder than assessing VLM on unlimited domains of images.

Other issues:
1. Tab. 2 missing the final Avg. score. The caption is not sufficient for readers to understand the score marked as red and bolded.
2. "an With, ..." in Ln. 297, I assume "an " should not be there.
3. Inconsistent formatting of Table. Tab. 5 does not have bolded text and red text, and Tab. 3 does not have red text.


I am open to discussion if I misunderstood the intention or content of the paper.

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper systematically benchmarks current VLMs on various spatial reasoning tasks using layout, with an application in indoor scene synthesis. The results highlight several findings, including that these VLMs tend to prefer normalized coordinates and struggle to interpret complex visual representations. Additionally, the task heavily relies on language processing.

### Strengths
* Understanding and reasoning about indoor layouts is an important task with many valuable applications in various industries. 
* The paper is well-written and easy to understand.

### Weaknesses
My main concern is about the motivation behind the tasks and the contribution of the key findings. The paper mentions that “Contrary to expectation, VLMs perform best with simplified sketch-based scene representations or, most strikingly, with no visual input at all, compared to detailed renderings.” However, this result isn’t entirely surprising. I think It raises questions about the choice of using VLMs for layout reasoning, as the tasks appear to be solvable using text alone, which aligns with the results showing better performance with text input/sketches. In that case, it seems more about testing the OCR capabilities of VLMs. Additionally, converting layouts to text appears to require less effort than rendering 3D. It would be helpful to clarify why VLMs are really necessary for these layout tasks.

My second concern is about the quantity and quality of the dataset. Having only 25 QAs per task seems insufficient. Additionally, it’s unclear whether steps were taken to ensure that the visual prompting is presented in a way that VLMs can recognize, for example, specific markers or axes designed for layouts. In some figures, the markers and numbers appear to be entirely occluded. 

Finally, as already noted in the limitations, the tasks mainly focus on 2D reasoning rather than 3D, which makes the title somewhat misleading.

### Questions
* What is the motivation for using VLMs for layout reasoning?
* Would including axis and units as visual prompts be beneficial?
* It would be great to include human performance on each of the setups.

### Soundness
2

### Presentation
2

### Contribution
2
