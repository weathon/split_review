# Behind the Magic, MERLIM: Multi-modal Evaluation Benchmark for Large Image-Language Models

- Decision: Reject
- Scores: 6, 5, 6, 5, 3

## Abstract
Large Vision and Language Models have enabled significant advances in fully supervised and zero-shot visual tasks. These large architectures serve as the baseline to what is currently known as Instruction Tuning Large Vision and Language models (IT-LVLMs). IT-LVLMs are general-purpose multi-modal assistants whose responses are modulated by natural language instructions and visual data. Despite this versatility, IT-LVLM effectiveness in fundamental computer vision problems remains unclear, primarily due to the absence of a standardized evaluation benchmark. This paper introduces a Multi-modal Evaluation Benchmark named $\textup{\benchname}$, a scalable test-bed to assess the capabilities of IT-LVLMs on fundamental computer vision tasks. $\textup{\benchname}$ contains over 300K image-question pairs and has a strong focus on detecting cross-modal “hallucination” events in IT-LVLMs. Our results bring important insights on the performance of state-of-the-art IT-LVMLs including limitations at identifying fine-grained visual concepts, object hallucinations across tasks, and biases towards the language query. Our findings also suggest that these models have weak visual grounding, but manage to make adequate guesses from global visual patterns or language biases contained in the LLM component.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Authors propose a new benchmark for “IT-LVLMs”, where the main contribution is to remove objects from images and thereby detect “hidden” hallucinations, where the model answer is correct but not grounded in the image. The benchmark tests object recognition, counting, and object relationship. Authors test multiple VLMs, each on several prompts.

### Strengths
The paper is well written and understandable, it shows all the relevant details. Missing or incorrect grounding of VLMs is a relevant research question and the approach to simply delete objects and check if the model notices the deletion is clever. Using open-ended answers fits to real use cases of VLMs (compared to testing with multi-choice).

### Weaknesses
The paper is well written and understandable, it shows all the relevant details. Missing or incorrect grounding of VLMs is a relevant research question and the approach to simply delete objects and check if the model notices the deletion is clever. Using open-ended answers fits to real use cases of VLMs (compared to testing with multi-choice).

The work is missing examples. There is only one datapoint shown in figure 1. Please add some randomly picked samples for each of the tasks, to give a better qualitative overview of the dataset.

In figure 1, the tennis racket is still somewhat visible even after deletion, at least the edges of the shape can be detected. However authors verify that an object detector cannot easily find those instances in Appendix A1. Maybe looking at some more edits will show in more details how good this editing works. An alternative approach would be e.g. to use image inpainting but this might lead to other artifacts.

In chapter 3.2 the authors go back to yes/no binary choice questions. This is understandable due to difficulties of posing such questions in an open-ended manner, however asking open questions is more fitting to how a VLM would be used in practice. Maybe it would have been possible to evaluate in a similar manner to 3.1 with making the model list relations and parsing the nouns.

As noted by the authors in line 364 some of the models are already somewhat old, e.g. MiniGPT-4 is ~18 months old at the time of submission. Maybe they could have been replaced by newer models like PaliGemma, or LLaVA 1.6 instead of 1.5. However since the focus is the benchmark this is only a small weakness.

In line 369 consider citing the models with model name instead of author name for clarity.

The citations are messy, e.g. in line 116 they need brackets. In line 201 Li et al. is duplicate. This repeats through the entire work. In general use \cite if the authors are the subject of a sentence, otherwise use \citep to put them into brackets.

In line 443 reference the supplementary material directly by chapter as a clickable reference instead of just as “in the supplementary material”.

The total number of unedited images is somewhat low with less than 10k images, however it’s enough for a benchmark.

In summary I believe if the authors add more clarification and examples, the work is valuable for publication.

However my biggest concern was whether the inpainting actually works well enough. To verify this, I scrolled through the dataset images and found that it can fail quite often. 102331_1 and 107094_0 show cases were humans were only half-erased and still visible. In 100723_3 a person is erased but replaced with meaningless noise. So at least a part of the hallucinations is potentially cases where the object is still visible. These are just two examples but it happens more often, it seems the inpainting AI is not strong enough to reliable produce data of real-world quality.

### Questions
Some details on the output processing could still be added to the supplementary: How exactly are the yes/no answers evaluated, e.g. lowercase, remove dots, then compare to the string “yes”? How are the number answers turned into integers?

Why use only one prompt in 3.3?

Figure 4: Why would models be worse on the edited images? If I understood correctly you mask one of the objects and reduce the count by one. It is not obvious to me why it would be more difficult to count 3 apples after one apple was removed, than to count 4 apples.

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
4

### Summary
This paper proposes a new dataset  MERLIM to evaluate the zero-shot ability of large vision-language models for fundamental vision tasks, i.e., object recognition, object relationship and object counting. The authors also introduce a inpainting procedure to study the hallucination issues. The authors evaluate the popular LVLMs in the proposed MERLIM.

### Strengths
1. The proposed dataset focues on the fundamental object-level  vision tasks for LVLMs, which was seldom explored by previous works.
2. The paper intends to study two types of hallucinations and identify the potential reasons.
3. The authors comprehensively evaluate the popular LVLMs, e.g., BLIP-2, InstructBLIP, LLaVA, in the proposed dataset.

### Weaknesses
1. My biggest concern is the data sources all come from the COCO images, which would lead to the bias for LVLMs.
2. The title does not convey the necessary information of the paper. I suggest the authors to add the key motivations in the submission, such as "for evaluating the hallucination in visual objects".
3. The details of inpating process is not well presents. For example, how to choose the edited objects? And how many objects are edited in an image?
4. From Figure 1, it seems that the edited image lose the natural structual in the edited part. Could the authors provide more examples for the edited images?

### Questions
1. Some typos should be fixed, e.g. in line 023, "IT-LVMLs" -> "IT-LVLMs"; in line 156, "300.664" -> "300,664"; in line 301, delete "!" and "?". The submission should be carefully checked.
2. What is the version of Qwen-VL. Its performance in Figure 2 and 3 is much lower than BLIP-2, Instruct BLIP, which seems strange.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a new evaluation benchmark for Instruction Tuning Large Vision and Language models (IT-LVLMs), dubbed MERLIM, containing over 300K image-question pairs. This benchmark focused on three types of tasks: Object Recognition, Object Counting, and Relationship Understanding. Besides, this benchmark enables to identify two types of hallucinations: Regular Hallucinations and Hidden Hallucinations, the latter of which is newly introduced in this paper. In experiments, the authors have evaluated many IT-LVLMs, obtaining several insights on the performance of state-of-the-art IT-LVMLs.

### Strengths
- The newly introduced evaluation aspect *Hidden Hallucinations* can help better understand the Hallucination issue of IT-LVLM.
- The analyses on the performance of state-of-the-art IT-LVMLs are beneficial.
- This paper is clearly-written, with a well-structured presentation of MERLIM, including its detailed design and evaluation methodology.

### Weaknesses
 - The included tasks such as Object Recognition and Object Counting seem to have overlaps with previous benchmarks [1]. It would be better if the authors could include detailed comparisons between the proposed benchmark and existing ones. It may be helpful to more thoroughly analyze the dataset.
- The field of LVLMs is constantly developing. Many models evaluated in the paper may not be that strong nowadays. It would be better if the authors could include more recent and advanced models like LLAVA-NEXT, etc.

### Questions
Do the authors have any plans to expand or adapt MERLIM to include new tasks or modalities as IT-LVLM capabilities evolve?

### Soundness
3

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
3

### Summary
This paper introduces MERLIM, a novel multi-modal Benchmark for evaluating IT-LVLMs for hidden hallucinations through several basic computer vision tasks.

### Strengths
This paper propose the concept of hidden hallucinations in LVLM, a phenomenon  that has been overlooked in the community. This brings insights on the performance of state-of-the-art IT-LVMLs including limitations at identifying fine-grained visual concepts.

### Weaknesses
1. The writing of this article needs to be strengthened. Figure 1 highlights the finding of "hidden hallucinations", but this is not elaborated in detail in the abstract. I was wondering if "hidden hallucinations" is the key point of this paper?
2. The focus of the article is not clear. The core of the article seems to be the discovery of the phenomenon of hidden hallucinations. However, in the experiments, too much emphasis appears to have been placed on the mention of fundamental visual tasks. Nevertheless, there are already benchmarks for evaluating fundamental visual tasks nowadays.

### Questions
1. The article seems to have two focal points, one is to conduct evaluations on fundamental computer vision problems, and the other is on hidden hallucinations. Which is the focus of this paper? From my perspective, you are trying to demonstrate the language bias and limitation of vision groundings in LVLM from the phenomenon called "hidden hallucinations" through several computer vision problems (Object Recognition, Object Counting, and Inter-object Relationship Understanding), is my understanding right?
2. What is the difference between IT-LVLM and LVLM? Why does the article emphasize IT-LVLM instead of directly using the term LVLM which is widely used?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper introduces MERLIM, a multi-modal evaluation benchmark for assessing Instruction Tuning Large Vision and Language Models (IT-LVLMs) on fundamental computer vision tasks. While the paper aims to provide a scalable test-bed to evaluate IT-LVLMs, it relies heavily on reusing and editing images from the MS-COCO dataset, which significantly diminishes the novelty and contribution of the work as a new benchmark. The paper also fails to incorporate evaluations of newer models that have emerged in the past year, limiting its relevance and timeliness. Additionally, the lack of open-sourcing the benchmark data hinders its practical utility and community adoption.

### Strengths
- The paper try to address a pertinent issue in the field of MLLMs, which is the need for a standardized evaluation benchmark to assess their performance on computer vision tasks.

- The focus on identifying hallucination events in MLLMs is a valuable contribution, as it highlights a critical challenge in the reliability of these models.

- The paper provides a detailed analysis of several MLLMs, shedding light on their limitations and potential areas for enhancement.

### Weaknesses
 - The paper's reuse of MS-COCO images and ground-truth annotations as the primary dataset for the benchmark is a significant concern.  This approach potentially introduces biases and data leakage, which can affect the evaluation's fairness and accuracy.  A new benchmark should ideally utilize a fresh dataset to provide an unbiased assessment of model performance.

- The paper does not include evaluations of newer MLLMs that have emerged since the initial submission, which is a critical oversight given the rapid advancements in the field.  This limits the benchmark's relevance and timeliness.

- The lack of open-sourcing the benchmark data is a substantial drawback.  Open-sourcing is a standard practice that fosters transparency, reproducibility, and collaborative improvement.  Benchmarks like POPE, NExT-GQA, and HallusionBench have demonstrated the value of open-sourcing by enabling broader community engagement.

### Questions
- Regarding the lack of open-sourcing the benchmark data, could the authors explain the rationale behind this decision?  


- How does MERLIM compare to other existing benchmarks in terms of its ability to detect and quantify hallucination events?     Could the authors provide a comparative analysis to highlight the unique aspects of MERLIM?

### Soundness
2

### Presentation
2

### Contribution
2
