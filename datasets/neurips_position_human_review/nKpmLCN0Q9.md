# Position: Agentic Systems Constitute a Key Component of Next-Generation Intelligent Image Processing

- Decision: Reject
- Scores: 7, 6, 5

## Abstract
This position paper argues that the image processing community should broaden its focus from purely model-centric development to include agentic system design as an essential complementary paradigm. While deep learning has significantly advanced capabilities for specific image processing tasks, current approaches face critical limitations in generalization, adaptability, and real-world problem-solving flexibility. We propose that developing intelligent agentic systems, capable of dynamically selecting, combining, and optimizing existing image processing tools, represents the next evolutionary step for the field. Such systems would emulate human experts' ability to strategically orchestrate different tools to solve complex problems, overcoming the brittleness of monolithic models. The paper analyzes key limitations of model-centric paradigms, establishes design principles for agentic image processing systems, and outlines different capability levels for such agents.

## Human Reviews

## Human Reviewer 1

### Rating
7

### Rating Number
7

### Confidence
4

### Summary
This paper advocates for adopting agentic system designs as a complementary paradigm to traditional model-centric approaches in image processing. It argues that agentic systems, capable of dynamically selecting and integrating various image processing tools, can enhance generalization, adaptability, and practical application flexibility beyond the capabilities of deep learning models alone.

### Strengths
The paper clearly and convincingly argues for the need to shift towards agentic systems in image processing, effectively highlighting current model limitations. It thoroughly discusses the theoretical foundations and practical benefits of agentic systems, backed by relevant literature and detailed conceptual frameworks. The authors also thoughtfully address potential alternative viewpoints.

### Weaknesses
The paper could further benefit from concrete empirical examples or preliminary studies demonstrating the practical effectiveness of agentic systems in specific image processing scenarios. Additionally, a discussion on the computational costs and practical feasibility of implementing complex agentic systems in real-world applications would strengthen the argument.

### Questions
Can the authors provide concrete examples or preliminary empirical evidence of agentic systems effectively outperforming traditional model-centric approaches in real-world image processing tasks?

How do the authors envision addressing potential computational challenges or efficiency concerns related to deploying agentic systems at scale?

### Presentation
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper takes the position that research in the area of image processing should pursue agentic AI as the basis for advanced image processing techniques, as opposed to end-to-end ML-based solutions that try to solve the problem in one pass.  The argument is that an autonomous agent can learn to mix and match different techniques that adapt to the particular input and task.  The authors identify levels of flexibility and autonomy from level 0 (basic tools used by a person) to level 5 (fully autonomous agent able to decide what modifications to make and how to execute them).

### Strengths
The paper does a good job of describing a vision for what capabilities and qualities an intelligent image processing system should possess. The taxonomy of image processing systems enables the reader to understand the context and differentiate their vision from existing approaches.

The paper is a well-supported argument for a long-term vision for image processing systems.

When completing the review, one of the most difficult questions to answer was whether this paper was arguing for or against a position in machine learning, or whether it was arguing that a specific technical approach was superior to another.  Given the alternative view discussion and the introduction, it feels like this is arguing for one technical approach over another.  However, these "technical approaches" are very broad, and the argument could be summarized as "in a field that has primarily focused on low-level engineering-driven solutions, a focus on agentic AI could enable revolutionary new capabilities."  So this could be a strength or a weakness.

### Weaknesses
1. The alternative position outlined in the paper is both real and yet also feels like a straw man to some degree.  I've marked it as well-considered and addressed, because both the alternative view and the counter-arguments to it are also woven implicitly into the introduction.  But there may be more sophisticated alternative views.

2. While the levels of capability are well-described by the paper. There are no concrete examples given of how those levels would address a specific task.  This makes it challenging for the reader to understand their differences on a specific task.  For example, consider the task of removing a shadow in an image from someone's face.  These would be my interpretations of how the different levels would work

level 0: manual pixel-level manipulation using photoshop like tools
level 1: auto-segmentation or fill capability directed by the user
level 2: auto-pipelining of several steps, quality judged by the user
level 3: iterative exploration with some type of automatic quality evaluation to allow strategy adjustment
level 4: system recalls prior processes that can adapt to new situations
level 5: system predicts the desired modifications and execute them prior to the user seeing the image

### Questions
1. It feels like more sophisticated alternative views might exist, including, for example, that a completely autonomous image processing system might be dangerous in the sense that people would never know how the actual original image appeared.  What are the author's thoughts on this?

2. Could the authors provide their vision of a concrete image processing task solved by levels 0 to 5?

### Presentation
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a position that the image processing community should focus more on an LLM-based agentic system beyond an end-to-end model.
This is because the agentic AI system can coordinate low-level image processing operators or specialized deep models to plan a better solution like a human. 
Besides, this paper also introduces the basic concepts of the AI agent and shows a blueprint of the agentic image processing system, as well as the demanding problems the community should resolve.

### Strengths
- Agentic image processing this paper advocated is a promising direction for future research and real-world applications.

- Clear introduction of the background and challenges of previous end-to-end deep image processing models.

- A clear and detailed blueprint of Agentic image processing is given.

- point out several demanding problems, e.g., Cognitive Architecture.

### Weaknesses
- The quantitative evidence is lacking here. Hard to know the current status of the LLM-based agentic image system compared to specialized deep models and human performance. 

- The agentic system discussed in this paper is too general; better to have specific image processing cases as examples and a focus.

### Questions
NA

### Presentation
3
