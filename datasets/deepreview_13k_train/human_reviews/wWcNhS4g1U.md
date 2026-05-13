# The Scene Language: Representing Scenes with Programs, Words, and Embeddings

- Decision: Reject
- Scores: 6, 5, 5, 3

## Abstract
We introduce the \reprFull, a visual scene representation that concisely and precisely describes the structure, semantics, and identity of visual scenes.
It represents a scene with three key components: a \prog that specifies the hierarchical and relational structure of entities in the scene,
\words in natural language that summarize the semantic class of each entity, and
\embds that capture the visual identity of each entity.
This representation can be inferred from pre-trained language models via a training-free inference technique, given text or image inputs.
The resulting scene can be rendered into images using traditional, neural, or hybrid graphics renderers.
Together, this forms a robust, automated system for high-quality 3D and 4D scene generation.
Compared with existing representations like scene graphs, our proposed \reprFull generates complex scenes with higher fidelity, while explicitly modeling the scene structures to enable precise control and editing.
Project page: \url{https://ai.stanford.edu/~yzzhang/projects/scene-language/}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper utilizes the formal structure of the LISP language to define scenarios, allowing for precise expression of scenes and benefiting tasks such as generation and editing.

### Strengths
The value of accurate coding is self-evident. The performance in tasks is remarkable and addresses issues where traditional language instructions are difficult to follow effectively.

### Weaknesses
- However, overly precise definitions can significantly reduce flexibility. For example, "a child with golden hair is gazing out the window from the desk" is a very common and simple description in traditional language, but defining it using LISP is extremely challenging. Although embedding methods exist, I doubt whether this would completely degrade into pure embeddings, failing to effectively leverage the advantages of formal languages.

- The downside of using a LISP-like language for definitions is the extremely long textual information. This not only significantly increases memory consumption but also makes training more difficult. While the article uses a very clever method to circumvent this issue, it could lead to difficulties in subsequent work.

- Direct comparisons with previous work are unfair because this article is more akin to a combination of 3D assets, while previous work involves direct generation. The former relies on the latter. Essentially, they are different tasks, so a fair comparison should be: GPT-4 or a rule-based model directly decomposing prompts and generating combinations.

### Questions
Refer to weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors propose "Scene Language," a pipeline for producing -- and later rendering -- a compositional scene representation from a text prompt or image. In contrast with GraphDreamer, which is compared against as an "exemplar approach," the authors task a language model with generating a precise, text-based code representation to define scene layout. The authors experiment with the application of multiple "rendering modules" to realize the code-based representations into explicit scenes, requiring only minor prompting modifications. To evaluate their method, the authors conduct a perceptual study measuring prompt alignment and counting accuracy.

### Strengths
1. The paper is well-written.
2. The pipeline outputs are visually appealing and appear generally well-aligned with the prompt texts.
3. The task is interesting and relevant to the ICLR community.

### Weaknesses
1. The authors make several unsupported claims, detailed below:

    a. "In summary, our contributions are as follows... Empirical results on text- and image-conditioned scene generation and editing tasks." Neither image-conditioned scene generation nor editing were empirically evaluated. The only such evaluation involved text-conditioned scene generation: "We perform a user study to compare with prior methods on the text-conditioned 3D generation task and report the percentages of user preferences for prompt alignment."

    b. "Compared with existing methods, our Scene Language produces 3D and 4D scenes with significantly higher fidelity, preserves complex scene structures, and enables easy and precise editing." 4D generation was not included in any evaluations or method comparisons.

    c. "Together, this forms a robust, fully automated system for high-quality 3D and 4D scene generation." The authors neither evaluate pipeline robustness nor include any discussion of it. 
2. The authors' choice of evaluations raises concerns:

    a. Rather than evaluate their pipeline on an existing setting, the authors opt to pick their own evaluation set of nine prompts, each of which includes a number ("8-layer", "5x5", "four", etc.). On this set, the authors measure "counting accuracy (0 for inaccurate and 1 for accurate)". They "compare with GraphDreamer (Gao et al., 2024) as an exemplar approach," but note that when the GraphDreamer "raw scene graph output contains too many objects, (they) rerun the graph generation and add 'The maximum number of objects is three.' in text prompt to avoid reaching memory limitation during optimization." This casts doubt on the significance of the results. Is the proposed method generally applicable, or does it only excel in counting-related scenarios with four or more objects?

    b. The authors display an image-to-scene comparison with GraphDreamer in Figure 6 and remark "Compared with our method, which preserves both structure and visual content from input images, GraphDreamer only reconstructs semantics from input images and leaves out entity poses and identities, due to the information loss in the intermediate scene graph representation." However, it is not clear why GraphDreamer (which is inherently semantic) was chosen for this comparison when the authors could have evaluated against a monocular reconstruction method.
3. The authors prominently feature the use of embeddings as a contribution of their work. However, except for serving as UUIDs, they seem only to be meaningfully employed in the image-to-scene task where a segmentation model is used to localize regions to apply textual inversion to. The authors' characterization of the embeddings as describing "the attributes and identity of the output entity, like a specific color of a 'pawn'." is an interesting idea but does not appear to align with their use in the paper: the black-and-white chess pieces clearly do not share shapes. It does not seem as though the authors have taken the idea far enough, and as it stands, could be removed from the pipeline to no discernible effect.

### Questions
1. Regarding the image-to-scene task, since the LLM is already employed to describe the objects in the scene in order to prompt SAM, the textual-inversion step seems unnecessary or at the least deserving of an ablation study. Have the authors evaluated its effectiveness over using only LLM descriptions?
2. The Gaussians and Minecraft lecture-hall samples in Figure 9 seem to have very similar layouts. This is confusing given that the renderers require different scene-generation prompts ("To prompt LM to generate Minecraft-compatible outputs, we remove rotation matrix and reflection matrix from the system prompt in Appendix E.1 and change the function header for primitive call to the follows:") and so must be the results of distinct LLM calls. Do the authors have intuition as to why the layouts appear so similar? How much layout variability is observed between successive calls?
3. Is any differentiable rendering done with Mitsuba? It appears to be employed only as a generic physically based renderer and it's unclear why it was chosen over a more standard graphics engine.

Addl. Comments:
1. The use of Lisp-like syntax in Figure 2 is confusing as the authors "prompt LMs to generate a Python program." The authors should consider using the actual syntax throughout to improve clarity.
2. The "chessboard at game start" is incorrectly configured as the queens are not on their color.
3. The staircase code edit in Figure 5 displays the wrong values.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The research paper introduces a new scene language representation designed to provide detailed information about a scene. This representation operates on three levels: programs that define the scene's composition and structural relationships between objects in the scene, semantic words that provide objects present in the scenes, and feature embeddings that capture instance-specific properties. These different layers provide a framework to describe a scene completely. They use this representation for scene generation and editing during rendering.

### Strengths
The paper is well-written, with a clear motivation and a thorough description of the proposed method. The application of scene editing is an important problem, highlighting the practical importance of the approach.

### Weaknesses
1) The examples presented in the paper seem relatively simple. Including more realistic, real-world scenes could better demonstrate the effectiveness of the scene language representation in handling complexity. For instance, incorporating indoor or outdoor scenes with multiple objects and occlusions would provide a valuable setup to showcase the approach’s robustness and highlight its results in more challenging conditions.
2) Quantifying the correctness or accuracy of the scene language generation step would add valuable insight. Specifically, it would be beneficial to measure various aspects of the scene language generation process, as outlined in Section 5. 

3) It would also be valuable to demonstrate how noise and errors in the scene language are managed during generation. For instance, if the scene language contains inaccuracies, such as incorrect or impossible relationships between objects, it would be useful to illustrate how these issues are addressed to ensure coherent generation results.

### Questions
Providing feedback on questions discussed in the weaknesses will be helpful.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper proposes a visual scene representation paradigm named Scene Language, which involves an ensemble of programs, words, and embeddings to describe the structure, semantics, and identity of visual scenes. A training-free inference technique is developed to infer the proposed scene representation from pre-trained language models. And a generic rendering module is utilized to render the scene into images using traditional, neural, or hybrid graphics renderers. Experimental results show that the proposed Scene Language generates complex scenes with higher fidelity while explicitly modeling the scene structures to enable precise control and editing.

### Strengths
1 The proposed method is applicable to multiple downstream scene generation/editing tasks. It is a training-free approach with the capability to generate and edit 3D and 4D scenes.

2 The visualization results show the superiority of the proposed method over competitors.

3 The paper is well-written with figures and tables nicely presented.

### Weaknesses
1 My biggest concern is that the manuscript seems to have incremental novelty since the proposed method relies on most existing models/tools and uses them straightforwardly. For example, the proposed scene representation is constructed directly using pretrained language models and is used for scene rendering using the existing rendering methods, e.g., 3D Gaussians.

2 Moreover, the proposed Scene Language looks more like an engineering improvement on GraphDreamer, breaking down complex scenes into independent entities for generation. The newly introduced embedding term also appears to have little effect. For example, in Figure 1, the referenced object should be made of metal material, while the modified object only captures information of blue color.

3 The pretrained language models are usually not ready for addressing specific downstream tasks and may produce inaccurate answers. However, the proposed method does not seem to incorporate some adaptation modules and give deep analysis.

4 The experiments also incorporate insufficient comparisons: (1) The authors should also report the FLOPs over the GraphDreamer for comprehensive comparisons. (2) If the provided image cannot describe the entire scene (e.g., occlusion), Scene Language cannot program the entire scene. Thus the comparisons to image-to-3D approaches should be included. (3) This paper lacks the ablation study on the proposal terms of descriptions on scene.

### Questions
See details in the weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2
