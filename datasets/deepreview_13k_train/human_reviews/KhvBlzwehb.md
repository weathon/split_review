# ActiView: Evaluating Active Perception Ability for Multimodal Large Language Models

- Decision: Reject
- Scores: 5, 6, 3, 3

## Abstract
Active perception, a crucial human capability, involves setting a goal based on the current understanding of the environment and performing actions to achieve that goal. Despite significant efforts in evaluating Multimodal Large Language Models (MLLMs), active perception has been largely overlooked. Since comprehensively assessing active perception is challenging, we focus on a specialized form of Visual Question Answering (VQA) that eases the evaluation yet challenging for existing MLLMs. Given an image, we restrict the perceptual field of a model, requiring it to actively zoom or shift its perceptual field based on reasoning to answer the question successfully. We conduct extensive evaluation over 27 models, including proprietary and open-source models, and observe that the ability to read and comprehend multiple images simultaneously plays a significant role in enabling active perception. Results reveal a significant gap in the active perception capability of MLLMs, indicating that this area deserves more attention. We hope that our benchmark could help develop methods for MLLMs to understand multimodal inputs in more natural and holistic ways.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper takes an "Active Perception" perspective for multimodal LLMs and proposes an evaluation benchmark where VQA is chosen as the proxy task.  Given an image, the task is to actively zoom in or out or shift perceptual field based on reasoning to answer the questions successfully.  Experiments are performed on several models and the results reveal a performance gap.

### Strengths
1. Active perception / active vision has been a long standing research field but has been sidelined by static dataset-based training pipelines (for not very convincing reasons). Active perception is rooted in neuroscience, cognitive psychology, and biology.  This paper brings a fresh perspective.
2. The paper is well written -- figures and tables help the flow.
3. Several models are tested and experimental settings are sound and transparent.

### Weaknesses
1. For both zooming or shifting, the image resolution/ratio will either remain the same (for example, zooming from a 400x300 image into a 80x60 patch) or will be resized (as stated in line 330 onwards). But sometimes, segmentation might be necessary instead of looking at the entire w x h patch.  This has not been explored.  While I understand that the benchmark only contains zoom/shift for now, what are some other operations that could be integrated into the benchmark?
2. The benchmark could be made a lot more comprehensive in terms of size: there are 1625 evaluation instances which means that approximately getting 16 questions wrong leads to a 1% performance drop.  In Table 1, the drop in performance compared to Full Image doesn't seem very statistically significant if it's just a few percentage points.
3. The benchmark could be made a lot more comprehensive in terms of tasks: why just VQA? Why not extend the annotations to other tasks such as captioning, vision-language inference (see NLVR2, or SNLI-VE etc.), image-text retrieval, etc.

### Questions
1. This is an ICLR submission, but to me this could be a CVPR/ICCV/ECCV paper as it is a "pure vision" paper.  I'd like the authors to provide more insights into what value the work could bring to representation learning and if the work has broader impact beyond vision.  This is **not** a criticism of the paper (which is why I haven't listed it above as a weakness), but I'd like to engage into a conversation about this.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces ActiView, a benchmark designed to evaluate the active perception abilities of multimodal large language models (MLLMs) through a visual question answering (VQA) format. Active perception involves comprehending the reasons for sensing, selecting what to perceive, and deciding on the methods, timing, and locations needed to achieve that perception. The study, which tested 27 models, found that the ability to handle multiple images simultaneously is vital for effective active perception. While all models outperformed random guessing, they still fell short of human performance. The authors highlight variations in performance among model types and the capacity of single-image models to leverage multi-view information. ActiView establishes a framework for assessing and enhancing MLLM active perception, underscoring its significance for future research.

### Strengths
1. This paper explores the active perception capabilities of MLLMs and introduces a novel benchmark “ActiView”.  
2. The authors present three distinct evaluation pipelines—Zooming, Shifting, and Mixed—specifically designed to assess the models' active perception abilities.  
3. The paper includes comprehensive experiments and analyses that yield insightful conclusions.

### Weaknesses
1. Evaluation Pipelines: The current evaluation pipelines rely on a fixed image splitting strategy, resulting in notable discrepancies between the evaluation pipeline and the ideal active perception behaviors. For example, in the Zooming pipeline, the model cannot perform additional zooming on the selected sub-image. Similarly, in the Shifting pipeline, the viewpoint movement is constrained to a predetermined granularity. This limitation prevents the model from dynamically adjusting its focus or viewpoint based on the content of the initial observation, which is a core aspect of true active perception. The fixed grid approach also introduces an artificial constraint, potentially biasing the evaluation towards models that are better suited to this specific type of input rather than those with more general active perception capabilities.

2. Insufficient Detail Analysis: As observed in Table 2, several models, such as Gemini-1.5-pro and Claude 3.5 Connect, exhibit superior performance on ‘full images’ compared to the ‘zooming’. A more detailed analysis of the underlying reasons for this discrepancy is warranted. It is unclear whether this performance drop is due to the models' inability to integrate information across multiple views, a failure to identify the most relevant sub-regions, or some other factor. The lack of analysis makes it difficult to pinpoint the specific weaknesses of these models in the context of active perception.

3. According to the prompts provided in the appendix I, it appears that the Mixed pipeline accounts for direct response scenarios (allowing models to specify the number of parts to zoom in or respond with "none" if no zooming is needed). However, the Zooming pipeline does not allow for a 'none' response. An explanation for this inconsistency would be beneficial. This discrepancy raises questions about the comparability of results across the different evaluation pipelines and whether the Zooming pipeline is truly capturing the active perception behavior intended by the authors.

### Questions
See the weknesses section for more details.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a new benchmark for multimodal large language models (MLLMs) that focuses on their active perception capabilities. To answer a fine-grained question about the image, models are presented either with a global image view and need to zoom into a specific part of the image, or with a local view that does not necessarily include the required information requiring the model to shift to over adjacent views looking for the correct information. Several closed and open models, 27 in total, are evaluated on this new benchmark.

### Strengths
- Active perception is an important research topic that is required for build autonomous agents that can search and find relevant information in our world.
- The paper evaluates a large amount of MLLMs of different kinds, making it a very comprehensive study
- The proposed dataset is the first of a kind that requires both shifting and zooming in an active perception setting.

### Weaknesses
 - All three pipelines are quite similar to each other. Zooming allows access to the full image and proper selection by the model, while shifting restrict access to the global view and a gradual access to image parts without active selection. Lastly, the mixed pipeline is very similar to the zooming setting, also giving access to the global image view. It is not clear why the mixed pipeline requires the model to discard images. Is it to make it artificially distinct or more difficult? Given that the paper highlights both settings as a key novelty of the provided benchmark (previous benchmark only evaluated one of the two), this small distinction between the pipelines diminishes the value of this contribution.
- The shifting pipeline does not give the model agency over which views it wants to request. Instead, it uses a pre-defined order for the views, i.e., the model just decides "next view" or "stop", without any penalty of requesting more views. The optimal policy is likely to simply request all views to have all available information. One ablation should include "All views" for the Shifting pipeline.
- The experimental results in Table 2 reveal weaknesses of the proposed benchmark:
  * There is not much difference in the zooming pipeline when comparing full image vs. zooming. A significant amount of models even perform better with the full image. This result suggests that zooming is not really necessary for the proposed benchmark.
  * The same is true for a smaller subset of models for the shifting pipeline where single view is better than one or multiple Shifting settings. As acknowledged in the results discussion, the experimental results also do not always follow the difficulty scaling of the setting, e.g., Gemini-1.5-pro achieves its best performance on Shifting-H.
  * These observations raise concerns about one of the main claims of the paper, i.e., that the images-question pairs from the proposed benchmark truly require active perception to be solved.
- The results in Tab. 4 tell a similar story to the concerns of Tab. 2. For multi-image models, all models except for InternVL2-8B achieve close to the GT Acc. on Zooming regardless of their Recall with GPT-4o showing the second highest drop in performance despite having the highest Recall. This suggests that Recall does not have a significant impact on the performance. Similarly for Shifting-R, Gemini-1.5-pro has a low Recall and a 5% drop in performance, while mPLUG-Owl3 has a high Recall and a 9% drop is performance (overall trends are a bit harder to spot because of the ordering).
- L. 475 states a hypothesis that the order of input views helps models in the hard settings as relevant images are more recent. However, if this is true, this is a design flaw of the setting which is supposed to be harder than the others. One option could have been to restrict the number of views a model can request, but it relates to an earlier point that the model cannot actually choose which view to request.
- Tab. 13 shows that adding more views hardly makes a difference which is counter-intuitive. It also suggests that either the image-question pairs or the setting do not really requiring active perception. Having more views and limiting the number of views or accounting for it in the evaluation metric could improve this.
- Case (b) in Fig. 5 showcases the problems above: The models shift through all views with the last one containing the relevant information, then make a wrong decision. From an active perception point of view, the models did everything correctly. Hence, this negative result did not measure their active perception capabilities.

### Questions
Please address the points raised in the Weaknesses section. Here are additional relevant questions:
- L. 269 explains that the dataset consists of 314 images with 325 questions, but Tab. 1 denotes 1,625 instances. Could you please explain this discrepancy? What is counted as an instance?
- The Shifting-R setting randomly selects an initial view. Is it randomly selected once for each image and the same initial view given to each model, or does each model receive a different randomly selected initial view?
- How is the adjacent view selected for the Shifting tasks? Is the same order given to all models?
- L. 420 states: "We obtain the random choice result of 33.95%, averaged over 10k runs." How was this random choice calculated? Why does it require making multiple runs? Another important baseline is an LLM (text-only) evaluation to measure the amount of common sense answers.
- What exactly is meant by the "Single View" column in Tab. 2? Which view is given for this experiment?
- L. 460 states that redundant information might distract a model. Why could this be the case? If the model is presented with the right information multiple times it should rather reinforce the correct answer. Can you provide an example? An ablation where all 4 views is given to the model could help better understand this issue.

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
4

### Summary
This paper proposes a benchmark, named ActiView, to evaluate active perception in Multimodal Large Language Models (MLLMs). The active perception is evaluated from two aspects: zooming and shifting. They observe that the ability to read and comprehend multiple images simultaneously plays a significant role in enabling active perception

### Strengths
1. Evaluating the active perception capabilities of MLLMs is crucial for their real-world applications, and this aspect has not been sufficiently addressed in previous benchmarks.

2. The authors have carefully annotated their dataset, organizing it into eight sub-categories to enable a thorough and nuanced evaluation of MLLMs.

3. The experimental analysis is comprehensive and clearly presented.

### Weaknesses
1. The scale of this dataset is too small, only with 314 images, as shown in Table 1.

2. The dataset primarily focuses on categories related to object relationships, attributes, and locations. Previous datasets have been released that cover areas such as object detection, counting, image event extraction, and image hallucination detection. While this dataset addresses active perception, the categories and types of questions it includes have already been covered in earlier datasets, resulting in a lack of novelty.

3. Where is InstructBLIP? Its Q-former can extract instruction-related visual features, playing an active perception role.

### Questions
Instead of evaluating the active perception of image content by MLLMs using shifting and zooming, can you evaluate it in other ways?

### Soundness
2

### Presentation
3

### Contribution
2
