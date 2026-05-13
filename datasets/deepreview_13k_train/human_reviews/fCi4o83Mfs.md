# Can Multimodal Foundation Models Perform Visual Temporal Reasoning?

- Decision: Accept
- Scores: 5, 8, 8, 6

## Abstract
Existing benchmarks often highlight the remarkable performance achieved by state-of-the-art Multimodal Foundation Models (MFMs) in leveraging temporal context for video understanding.
However, *how well do the models truly perform visual temporal reasoning*?
Our study of existing benchmarks shows that this capability of MFMs is likely overestimated as many questions can be solved by using a single, few, or out-of-order frames.
To systematically examine current visual temporal reasoning tasks, we propose three principles with corresponding metrics:
(1) *Multi-Frame Gain*,
(2) *Frame Order Sensitivity*,
and (3) *Frame Information Disparity*.
Following these principles, we introduce **TVBench**, **T**emporal Reasoning **V**ideo Understanding **Bench**mark, a novel benchmark crafted to rigorously assess MFMs' temporal reasoning capabilities in video understanding.
TVBench comprises 1,484 carefully curated, *human-annotated* questions spanning six tasks (i.e. *action count, direction, rotation, shape & trend, velocity & frequency, and visual cues*), applied to 1,417 videos, including 805 self-recorded and -generated videos, that encompass human-centric, real-world, and simulated scenarios. 
Our comprehensive evaluation reveals a human-model performance gap of 57.3% with the best-performing model.
Moreover, our in-depth analysis uncovers more fundamental limitations beyond this gap in current MFMs. While they can accurately recognize events in isolated frames, they fail to interpret these frames as a continuous sequence.
We believe TVBench will serve as a crucial testbed for evaluating the next-generation MFMs and as a call to the community to develop AI systems capable of comprehending the human world dynamics through the video modality.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper tackles the problem of benchmarking temporal reasoning using multimodal foundation models. First, the paper establishes some principles that temporal reasoning benchmarks must follow in order to test temporal reasoning capabilities, and shows that existing benchmarks fail to cater to these principles. Second, a new manually annotated benchmark, comprising six question types with some counterfactual modifications, is proposed. Third, several existing models are benchmarked demonstrating a big difference between human performance and best model's performance. And finally, some ablation studies are presented that show how one can improve models capabilities on this benchmark.

### Strengths
The paper is written well and easy to follow. It addresses an important area in video understanding research, where several benchmarks are known to have shortcomings in actually requiring all the frames of a video [1].
- The benchmark is manually curated in a three-stage process, potentially yielding very high-quality QA annotations
- Several models including proprietary ones lag significantly behind humans. This verifies that the benchmark is indeed difficult for existing models.
- A commendable effort is made in conceptualizing the principles defining how to check whether a benchmark requires temporal reasoning, and its shown that TVBench is way ahead of other benchmarks in adhering to these principles as shown in Tables 1-4
- Some of the ablations / analysis about existing models' capabilities are interesting, i.e. the plateauing at 8 frames compared with humans, exploiting common sense shortcuts etc.

[1]: Revealing Single Frame Bias for Video-and-Language Learning

### Weaknesses
The main weakness in my opinion is that the defined principles and ways of measuring benchmarks' adherence to these principles is not very rigorous.

1: Single frame insufficiency: 
- Why is the definition limited to a single frame? What about QA pairs that can be answered in just a few frames, say 2 frames? In the abstract, it's argued that such a scenario is bad for temporal reasoning benchmark, however, this principle will consider such a question as good.
- In the second implementation, a single hand-picked frame is compared with uniformly sampled 16 frames. This seems a bit unfair to the 16 frame case. Shouldn't we compare hand-picked 16 frames with hand-picked 1 frame to get a true sense of single frame insufficiency? 

2: Frame order sensitivity:
The definition assumes that frame order sensitivity is essential for a good temporal reasoning benchmark. However, a powerful model human can easily figure out the temporal order in a lot of cases. So, I don't know if this needs to be a hard requirement.

 
3: Frame contribution parity:
Implementation-wise, again why only a single frame is considered? The proposed implementation will not give any signal for a QA pair requiring 2 frames.

For example, a benchmark that simply contains state transition questions requiring exactly 2 frames will get perfect scores on these three principles. However, such a benchmark is not very valuable. In effect, these principles can be considered necessary conditions (second one is a bit questionable), but not sufficient conditions for a benchmark to be considered as requiring temporal reasoning.

Lastly, the way of evaluating these principles using pre-existing models creates a chicken and egg problem, as the models themselves may not be capable of answering the said questions. For example, a very hard benchmark that GPT-4o cannot answer will fail all the principles if we use GPT-4o to evaluate the principles.

A couple of unrelated issues are:
- Many of the proposed question types already are part of existing works, so it’s unclear how this benchmark would be any different in satisfying the principles. Is the difficulty coming from the annotation process and counterfactuals?
- The benchmark may contain a lot of unrealistic questions because of (i) counterfactuals and (ii) simulated data that are used to artificially make the benchmark harder. These may affect the usefulness in real-world applications.

### Questions
Audio inputs (speech) are not discussed in this benchmark. What happens if audio (speech) is included as part of video inputs to the models? Will the results on principles and and on TVBench change?

### Soundness
2

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper investigates whether current multimodal foundation models can perform visual temporal reasoning, which is a complex task requiring models to incorporate visual and temporal information simultaneously. The authors show that current benchmarks on video understanding may be insufficient to truly test the model's capabilities in visual temporal reasoning and introduce TVBench which consists of challenging video and question pairs that expose a significant gap between multimodal foundation models and humans, hence exhibiting limitations in current multimodal models.

### Strengths
- The paper tackles an important aspect of video understanding, which with benchmarks that are not carefully designed, might be overestimated. 
- The dataset seems to consist of well designed and curated data, as their design philosophy matches the results on the three metrics they propose. This is likely due to the rigorous quality check, and the diversity of videos (including simulations) that the authors include in the data.
- Intensive experiments and the analyses provide valuable insights into the performance of multimodal foundation models on video data.

### Weaknesses
 - If the authors could include an experiment to test the effect of language prior - i.e. the model's accuracy when only given the text part of the dataset questions, and report the difference, that might also help reinforce the soundness of their benchmark design.
- If the authors could provide some information on the resolution and scale of the videos, that might be helpful especially because the authors discuss models not benefiting from more than 8 frames.



### Questions
1. What would happen if corresponding accuracy is zero in the denominator for the three metrics? Might need an epsilon term, or it might just be sufficient to subtract the two accuracies.
2. Why might there be a performance plateau beyond 8 frames? Is it in the design of common foundation models? Is it likely due to there being too much information to process (for example, the way the models process more than 8 images) ? Do various models show the plateau behavior exactly at 8 frames? What about at smaller frames? 
3. How does the performance of zoomed-in views differ when only tested on simulation videos with less noise?

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper present a new benchmark for visual temporal reasoning. They start by defining three principles for video temporal understanding, namely SINGLE FRAME INSUFFICIENCY, FRAME ORDER SENSITIVITY and  FRAME CONTRIBUTION PARITY. Three principles are then quantified by a metric to reflect the headroom provided by indivisual benchmarks. Finally, a new new benchmark named TVBench with 1484 carefully curated examples are presented and a diverse set of general purpose MFMs are benchmarked against TVBench.

The paper is easy to follow and the key concepts are delivered sound and clear. I appreciate the details the authors provided in the appendix about the analysis and the dataset.

### Strengths
The paper is easy to follow and the key concepts are delivered clearly. The authors start by setting three principles and studied the existing video benchmarks around these three principles quantitatively, revealing the opportunities and curating datasets around them, I think the approach to the problem and processes are rigorous and effective. Their final results on evaluating MFMs on their datasets also show big opportunties for current system to improve in terms of temporal reasoning.

### Weaknesses
I have some concerns and questions for discussion.

* Clarification on Table 6. It is not very clear to me what "True" & "False" stand for in the table. More explanation and details on the experiment setups are needed. This leads to the question of how the conclusion "More Capable Models Are More Likely to Exploit Shortcuts Through Common Sense." is drawn. Does "True" and "False" mean different split of datasets? If so, those videos and their QAs are different, how could we compare their relative performance drop and reach the conclusion?

* L479 "Models Excel in First-Person Over Third-Person Perspective Temporal Reasoning Video Understanding." The conclusion of model excels FPV over TPV videos on comparing experiment results of 88 FPV QA v.s. 668 TPV QA. Since these are two set of different videos and QAs, it is hard to compare the final score side by side and draw the above conclusion in my opinion. More rigorous study or careful experiment design is needed, for instance, creating a matched set of FPV and TPV videos covering the same scenarios would make more sense.

* References to the visual temporal reasoning principles are needed. Some principles discussed in the manuscript for temporal reasoning in video understandings have been studied and revealed in previous literatures, e.g. "Single Frame Insufficiency" has been discussed in [1]; "Frame Order Sensitivity" has been explored/discussed in many literature, e.g. [2]; [3][4] studied "FRAME CONTRIBUTION PARITY" as well. Having a brief literature review section for each principle, and discuss the difference and contributions of current work could strengthen the manuscript.

### Questions
* The author seem not mention it in the paper - will the benchmark be made publicly available at some point?
* The author selectively evaluate some proprietary MFMs in Table5. It would be interesting to report the results of different model sizes in the same model family  (e.g. Gemini 1.5 pro v.s. Gemini 1.5 flash; Claude 3.5 Sonnet v.s. Opus) to understand the scaling effect of current SOTA MFMs on the proposed benchmarks.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces a novel video benchmark specifically designed to assess the temporal reasoning capabilities of multimodal foundation models. The benchmark is thoughtfully formulated, encompassing a wide range of dynamic and continuous reasoning scenarios over time. By evaluating state-of-the-art video foundation models, the paper highlights fundamental challenges these models face in Video Question Answering (VideoQA). This work provides valuable insights into the limitations of current multimodal models in handling temporal visual tasks, promising to advance research in both the video and large language model (LLM) communities. However, despite these contributions, I still have some concerns and will adjust my rating depending on whether they can be further addressed.

### Strengths
- Well-Established Benchmark: The benchmark is rigorously constructed with three quantitative principles that emphasize the complexity of temporal reasoning tasks, ensuring a challenging and relevant evaluation.

- Extensive and Comprehensive Coverage: The benchmark includes a wide range of tasks and scenarios, providing thorough coverage of diverse temporal reasoning challenges, which enhances the evaluation scope and relevance.

- In-Depth SOTA Model Comparison: The paper presents an extensive and detailed comparison of state-of-the-art video foundation models, providing valuable insights into their capabilities and limitations for video question answering.

- Clear and Cohesive Writing: The paper is well-written, presenting its ideas and findings in a clear and organized manner, making it accessible and informative for a broad audience.

### Weaknesses
 - Sensitivity in Mathematical Formulation: The mathematical formulation of the three principles appears sensitive to certain parameters, particularly the choice of human-picked frames and the number of input frames. For instance, using 16 frames as the multiple-frame input seems arbitrary; different frame counts could significantly impact evaluation scores and model comparison across benchmarks. This choice requires further justification, along with ablation studies on multi-frame input numbers within the three principles, to confirm robustness and fairness.

- Data Imbalance Across Tasks: The sample sizes across the six tasks are imbalanced, with some categories, like Visual Cues, containing only 70 questions—significantly fewer than other categories. This imbalance could impact the benchmark's representativeness and reliability. Addressing this imbalance would improve the benchmark's overall consistency and rigor.

- Fairness in Benchmark Comparisons: Comparisons with other benchmarks may not be entirely fair due to the random sampling of 200 QAs for evaluations. This approach may inadvertently filter out complex temporal reasoning questions. To ensure fairness and maintain the benchmark's integrity, evaluating all QAs from other benchmarks would be preferable.

- Insufficient Text-Only Baseline in Table 5: The current text-only baseline presented in Table 5 may not fully capture the model's reasoning capabilities. Converting video content into textual descriptions for input into a model like GPT-4 would offer a more meaningful comparison with visual inputs. Including this enhanced baseline would provide deeper insights and enrich the discussion in Table 5.

### Questions
- Will the benchmark be publicly available?

- How do you generate the queries for each task in the benchmark? Please include this information in the main paper, which may be inspiring to the readers.

- Why not reporting the results of open-source models after fine-tuning them on the temporal reasoning questions. e.g, a training set of the proposed benchmark? It is possible that the model learns to reason from dynamics in the video after fine-tuning. Please justify this.

### Soundness
3

### Presentation
3

### Contribution
3
