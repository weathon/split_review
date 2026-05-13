# WorldSimBench: Towards Video Generation  Models as World Simulators

- Decision: Reject
- Scores: 6, 5, 8, 5

## Abstract
Recent advancements in predictive models have demonstrated exceptional capabilities in predicting the future state of objects and scenes.
However, the lack of categorization based on inherent characteristics continues to hinder the progress of predictive model development.
Additionally, existing benchmarks are unable to effectively evaluate higher-capability, highly embodied predictive models from an embodied perspective.
In this work, we classify the functionalities of predictive models into a hierarchy and take the first step in evaluating World Simulators by proposing a dual evaluation framework called \mname.
\mname ~includes \textbf{\upstream} and \textbf{\downstream}, encompassing human preference assessments from the visual perspective and action-level evaluations in embodied tasks, covering three representative embodied scenarios: \mc, \ad, and \arm.
In the \upstream, we introduce the \dataset, a video assessment dataset based on fine-grained human feedback, which we use to train a \evaluator{} that aligns with human perception and explicitly assesses the visual fidelity of World Simulators.
In the \downstream, we assess the video-action consistency of World Simulators by evaluating whether the generated situation-aware video can be accurately translated into the correct control signals in dynamic environments.
Our comprehensive evaluation offers key insights that can drive further innovation in video generation models, positioning World Simulators as a pivotal advancement toward embodied artificial intelligence.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents an evaluation of large scale video predictive models, also referred in the literature as world simulators. It first claims to categorize based on “degree of embodiment” or output modality, like text, images or actions. They divide this framework into a perceptual evaluation, and an embodied or manipulative one. The former uses a model trained on human collected data to score the outputs, whereas the latter, puts it in a loop with a trained video to action model and evaluates on task success.

### Strengths
- Its important and timely to categorize the contribution of world simulators, which makes this work useful. 
- Using an HF-embodied dataset to learn a model of human preference, seems more scalable than actual human evaluation, although it might need to be updated frequently enough or kept hidden to avoid data contamination. 
- In my understanding, the core contribution of this work is two fold: 1) the HF embodied dataset that tries to score the visual perceptual quality, based on human feedback. 2) Doing a closed loop evaluation by producing actions based on the predicted video.  
- The idea of using world simulators as an evaluation, seems similar to line of work 1x has been doing on world modelling (https://github.com/1x-technologies/1xgpt).  It maybe useful to discuss this perspective. Just a comment, doesn't take anything away from the contribution of the work.

### Weaknesses
- This paper has a lot of jargon which sometimes makes it a bit hard to follow. 
- The term of degree of embodiment has been used quite vaguely, which if I understand correctly is meant to be the output modality, whether its text, images or videos. Presenting it that way would be more straightforward and easy to understand. 
- Embodiment has also been used very again in the Section 4.1.1 to define as an axis of evaluation for perceptual quality like obeying physical laws, which is different from the degree of embodiment term used before.

### Questions
- Given the hierarchical evaluation, and various axes of variation in embodiment, did the perceptual evaluation show any insights that existing benchmarks at s2 level did not? I was unable to point out a clear comparison between these and previous benchmarks, besides the HF-embodied dataset. I understand that it adds various other layers of evaluation like perspectivity and speed, but what aspects of it went unreflected previous benchmarks that this one addresses.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The training of video generation models in WorldSimBench involves fine-tuning multi-modal large models on the HF-Embodied Dataset, which provides multi-dimensional human feedback on visual quality, instruction alignment, and embodiment. Using techniques like LoRA for efficient parameter tuning, the models optimize for perceptual, instruction consistency, and embodiment losses to enhance their alignment with human preferences and physical consistency across various tasks. Human Preference Evaluator, trained on HF-Embodied Dataset, plays a key role by scoring generated videos and providing iterative feedback, enabling the models to improve continuously in producing realistic, instruction-compliant, and task-appropriate video outputs across scenarios like open-ended environments, autonomous driving, and robotic manipulation.

### Strengths
1. Comprehensive dual evaluation framework assessing models on both visual quality and action-level performance.

2. Detailed human feedback dataset (HF-Embodied Dataset) provides multi-dimensional evaluation criteria for realism and task alignment.

3. Efficient training approach with LoRA and Human Preference Evaluator enables targeted, adaptive improvements without extensive computational resources.

4. Versatile benchmarking across diverse scenarios (open-ended environments, autonomous driving, and robotic manipulation) to ensure robustness in varied real-world applications.

### Weaknesses
1. The data for the different scenarios was not trained together, potentially limiting the model's ability to generalize across multiple embodied contexts and requiring individual training processes for each environment, which could hinder efficiency and scalability.

2. There is a relative lack of qualitative results in the study, which would have provided richer insights into how well the models handle nuanced, complex interactions or specific visual challenges within each scenario, potentially limiting the interpretability of performance beyond numerical metrics.

3. Some contributions, such as integrating evaluations across different embodied scenarios, might feel more like a survey. While valuable, these elements primarily build on existing consensus in the field and might not introduce new methods or substantial innovations in evaluation techniques.

4. The role of the Human Preference Evaluator, though useful in aligning generated content with human preferences, has potential that remains underexplored. The paper mainly employs it for evaluation without exploring its broader applications. Additionally, it is not a general-purpose evaluator, as adapting it to a new dataset requires re-collecting data and retraining, which limits its flexibility and scalability.

### Questions
See Weaknesses

### Soundness
3

### Presentation
3

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
This paper introduces a hierarchy for classifying predictive models based on their capabilities and level of embodiment. This categorization aims to advance research and development in the field and provides a framework for evaluating world simulators. A new evaluation framework called WorldSimBench is proposed, which includes two types of evaluations: explicit perceptual evaluation and implicit manipulative evaluation. The paper conducts extensive testing across multiple world simulator models and analyzes the results in detail. Further, A large dataset called HF-Embodied Dataset is developed, which includes human feedback on 3D environments across various scenarios and dimensions and enables the evaluation of world simulators and has broader applications in video generation models, such as alignment.

### Strengths
Explicit Perceptual Evaluation: This assesses the visual quality, condition consistency, and embodiment of the generated content through human preference evaluation. The HF-Embodied Dataset, containing fine-grained human feedback, is used to train a Human Preference Evaluator.

Implicit Manipulative Evaluation: This assesses the World Simulator’s performance by converting the generated videos into control signals and evaluating their effectiveness in embodied tasks within three scenarios: Open-Ended Embodied Environment (OE), Autonomous Driving (AD), and Robot Manipulation (RM).

Comprehensive Evaluation: WorldSimBench provides a holistic assessment of World Simulators by considering both visual and action aspects, addressing the limitations of existing benchmarks that focus only on aesthetic quality or task completion.

Human-Centric Evaluation: The use of human preference evaluation and fine-grained feedback allows for a more intuitive and accurate reflection of the quality and characteristics of the generated videos, including their adherence to physical rules.

Diverse Scenarios: The evaluation covers three representative embodied scenarios, providing a comprehensive benchmark for evaluating World Simulators across a range of real-world tasks.

Open-Source Dataset: The HF-Embodied Dataset is open-source and can be used for various applications beyond evaluating World Simulators, such as alignment and other video generation tasks.

### Weaknesses
Limited Scope: The evaluation primarily focuses on physical rules and 3D content within the context of embodied intelligence, specifically robots. The evaluation of World Simulators in other scenarios with more complex physical rules and diverse entities requires further exploration.

Static Evaluation Limitations: The evaluation of World Simulators using static benchmarks may not fully capture their dynamic nature and real-time requirements in interactive environments. Further research is needed to develop more effective evaluation methods for dynamic scenarios.

Limited Generalizability of Video-to-Action Models: The performance of video-to-action models in converting generated videos into control signals may vary depending on the specific task and environment. Developing more robust and generalizable video-to-action models is crucial for the practical application of World Simulators.

### Questions
Could the generated videos help improve the performance of VLA models?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduced WorldSimBench, a dual evaluation framework for assessing World Simulators by conducting thorough evaluations through Explicit Perceptual Evaluation and Implicit Manipulative Evaluation, and examined several video generation models as World Simulators in several simulators.

### Strengths
1. This paper provides a solid overview of the world simulator.
2. The dataset construction involves the introduction of costly human preference annotations, which adds meaningful data to the study.
3. The experimental design is quite comprehensive, covering a wide range of aspects.

### Weaknesses
1. First, this article integrates video generation with downstream tasks, but this kind of idea has been around for a long time. For example, this is not the first paper to apply video generation to robotic tasks; the first one should be UniPi. Additionally, the authors did not innovate on the paradigm of combining with downstream tasks, and the overall approach still references the video-action mapping method from SuSIE. Furthermore, even following SuSIE's methodology, it should not be applied to video generation since SuSIE is a framework for goal image generation. The authors should have used the UniPi framework here, although this would lead to a drop in results.

2. There are issues with the evaluation metrics. For example, in the CALVIN task, the common practice is to test using an evaluation method of 1000/100 (1000 times for standard evaluation and 100 times for the UniPi method), which ensures coverage of all 34 task categories. However, the authors only used 20 evaluations, resulting in a significant number of generated tasks not being tested, leading to a lack of strong credibility in the current results. Moreover, there is no comparison with SOTA methods.

3. The most valuable aspect of the entire article is the generation of human feedback annotations. However, the authors did not leverage this feedback for further optimization, merely stopping at obtaining a score. If they could use the human feedback annotation data to enhance alignment in downstream tasks through RLHF, the innovation of this article would be more substantial.

4. In the methods section of Figure 3, there is a gap between the authors' testing of RM performance. The authors still used the original annotations from the dataset and did not apply a high-level planner to break down tasks. This results in a gap between the framework and experimental parts. Such an organizational structure exaggerates the generality of the method, but when solving practical problems, traditional methods are still employed. This indicates that the framework's design is not advancing the task further; it merely replaces it with a better video generation model, which still stems from the performance improvements of Open-Sora.

### Questions
I understand that the authors intend to establish a comprehensive new paradigm for video generation that can address many issues, especially the downstream video-to-action problem. However, the article should focus more on how to better utilize human feedback annotations to improve the downstream video-to-action problem. Without discussing this point, most of the content mentioned in the article is already existing and established, resulting in a lack of substantial innovation.

### Soundness
2

### Presentation
3

### Contribution
2
