# AutoGUI: Scaling GUI Grounding with Automatic Functionality Annotations from LLMs

- Decision: Reject
- Scores: 6, 8, 3, 3

## Abstract
User interface understanding with vision-language models has received much attention due to its potential for enabling next-generation software automation.
However, existing UI datasets either only provide large-scale context-free element annotations or contextualized functional descriptions for elements at a much smaller scale.
In this work, we propose the **AutoGUI** pipeline for automatically annotating UI elements with detailed functionality descriptions at scale.
Specifically, we leverage large language models (LLMs) to infer element functionality by comparing the UI content changes before and after simulated interactions with specific UI elements. To improve annotation quality, we propose LLM-aided rejection and verification, eliminating invalid and incorrect annotations without human labor.
We construct an **AutoGUI-704k** dataset using the proposed pipeline, featuring multi-resolution, multi-device screenshots, diverse data domains, and detailed functionality annotations that have never been provided by previous datasets.
Human evaluation shows that the **AutoGUI** pipeline achieves annotation correctness comparable to trained human annotators. Extensive experimental results show that our **AutoGUI-704k** dataset remarkably enhances VLM's UI grounding capabilities, exhibits significant scaling effects, and outperforms existing web pre-training data types. We envision AutoGUI as a scalable pipeline for generating massive data to build GUI-oriented VLMs. AutoGUI dataset can be viewed at this anonymous URL: https://huggingface.co/AutoGUI.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents the AutoGUI pipeline for auto-annotating UI element functionality using LLMs, reducing manual work by identifying functions through simulated interaction data. The AutoGUI-704k dataset, constructed by the proposed pipeline, enhances Vision-Language Models in UI understanding. Results show that the dataset improves VLM grounding accuracy, approaching human performance, with automated rejection and verification effectively reducing errors. Human evaluation further demonstrates that the AutoGUI pipeline achieves annotation correctness comparable to trained human annotators.

### Strengths
1．AutoGUI pipeline provides a scalable solution to manual UI annotation by using LLMs for functionality labeling, reducing labor and advancing VLM understanding of UI elements.
2.  The pipeline annotates functionality based on UI dynamics, using LLMs to analyze content changes triggered by interactions. This approach enables functionality labeling without manual intervention, capturing detailed functional nuances.
3. AutoGUI-704k dataset covers Web, Mobile device types and UI contexts, valuable for advancing VLM research. The LLM-aided rejection and verification process ensures data quality, reducing manual correction and enhancing annotation reliability.

### Weaknesses
1. The experiments focus on specific test sets and benchmarks but lack an analysis of the finetuned model’s generalization across diverse UI types and applications. This may affect the pipeline’s robustness in handling various UI designs, platforms, and complex interactions in real-world settings.

2. Although there are some human checks, the pipeline relies heavily on LLMs for rejection and verification. This raises concerns about whether LLM-based processes alone can consistently maintain high-quality annotations as the dataset scales.

### Questions
See the weaknesses.

### Soundness
3

### Presentation
3

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
This paper develops a new dataset creation pipeline for collecting Graphical User Interface (GUI) element functionality annotations, which they name AutoGUI. It is focused on obtaining high quality annotations of UI interactions in terms functionality descriptions of the different elements in the UI. Ultimately, they focus on obtaining high-quality tuples of (UI Screenshot, UI Element, Functionality). The pipeline first collects UI trajectories by simulating user interactions when interacting with the elements of the UI. Then, each pair of interactions is analyzed by an LLM to identify its functionality (by observing differences between the UI elements and accessibility tree before and after the interaction). They propose a rejection based LLM filtering to discard unsatisfactory functionality annotations. The pipeline mainly focuses on processing websites or Android UI samples. Using the described pipeline, authors use it to collect the AutoGUI-704k dataset. Finally, they finetune a number of VLM baselines on the proposed dataset to show how they improve in the UI grounding and reasoning tasks.

### Strengths
- The paper is well written and easy to read.
- The figures presented in the paper are useful for helping understand the presented pipeline with real examples.
- The AutoGUI pipeline offers good advantages over most of its competitors (as shown in Table 1), specially for 1) its scalability and automation (removing the need for costly human annotation), 2) contextualized functionality annotations, 3) dataset size, and 4) coverage of both web and android
- The analysis on data quality comparing different ablations of the method with human annotations helps strengthen the contribution of AutoGUI.
- Sufficient and relevant benchmarks are selected for evaluating the finetuned VLMs in UI grounding tasks.
- Results show that the proposed dataset helps improving GUI grounding performance.

### Weaknesses
 - The dataset would enjoy more advantages if it contained more platforms other than websites and Android UI. For instance, extending it to other operating systems, and new UI applications.
- The number of baselines appears quite limited. I would like to see the performance of state-of-the-art VLMs (boths open and closed source). Results from closed GPT4o, Claude 3.5 Sonnet, or Gemini would help in comparing methods on the presented benchmarks. Similarly, there are a number of powerful open-source models like Llama3.2 [1], MolMo [2], or larger versions of Qwen2VL, like its 70B variant.
- Authors could have performed more fine tuning experiments. Only QwenVL and Slime models have been finetuned. Finetuning more models would help strengthen the contribution of this dataset. For instance, they provide results on Llava, which they could also finetune. 
- We can't see the benefits of the proposed dataset in comparison with other datasets in terms of performance.

### Questions
- Is it easy to scale AutoGUI to new platforms such as IOS, and computer OS UIs?
- Is it easy to scale AutoGUI to multiple languages?
- Have the authors analyzed the overlap between train and test data to avoid any contamination?
- How does the proposed dataset compare with the other datasets of Table 1 in terms of performance (e.g. benchmark evaluations in Table 4). Are results substantially better in comparison to the same models finetuned on other datasets.
- How does it affect the resolution of the input image when solving this task for VLMs?

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
5

### Summary
This paper proposes a scalable and automatic UI data annotation pipeline that annotates GUI elements with detailed functionality descriptions. It also proposes a series of filters to improve the annotation quality including hand-written rules and LLM-based rejectors and verifiers. The paper shows that the collected annotations achieves high correctness comparable to the trained human annotator, thus reducing the burden of collecting GUI data. The experiments on the collected AutoGUI dataset show its effectiveness in GUI grounding task.

### Strengths
Quality & Clarity

The paper points out the shortcomings of current GUI datasets and proposes a data collection pipeline to address them. The collected data is first analyzed for correctness to ensure its quality, and its effectiveness is subsequently demonstrated through experiments. The writing is logically structured and clearly expressed.

### Weaknesses
Limited Evidence: The experiments cannot fully demonstrate the effectiveness of AutoGUI data.

1. This paper evaluates AutoGUI data on 6 benchmarks as shown in Table 4. The effectiveness of AutoGUI data can be assessed by comparing the results of *Qwen-VL-AutoGUI702k* and *SeeClick* as they use the same base model. The results on *FuncPred* benchmark are excluded from consideration as *FuncPred* is derived from AutoGUI dataset and shares the same data distribution with it. In the remaining 5 benchmarks, *Qwen-VL-AutoGUI702k* performed worse than *SeeClick* in 3 of them (VWB EG, RefExp, and ScreenSpot). The paper attributes this performance gap to the absence of data from Apple devices and desktop software in the AutoGUI dataset. However, the *ScreenSpot* benchmark has 3 subsets including Web, Desktop and Mobile, and there is a lack of experiments on the Web subset in *ScreenSpot* to support this argument.
In summary, the existing experiments cannot prove the effectiveness of AutoGUI training data.

2. Also the Table 4:
  a) By comparing the results of *Qwen-VL-AutoGUI702k* and *Qwen-VL-AutoGUI702k\**, it is observed that the introduction of SeeClick training data improves the performance of Qwen-VL on all benchmarks;
  b) By comparing the results of *SeeClick* and *Qwen-VL-AutoGUI702k*, it is observed that the introduction of AutoGUI data reduces the performance of Qwen-VL on *RefExp*, and did not significantly improve the performance on *ScreenSpot*.
These 2 results indicate that the role of AutoGUI data is not as significant as SeeClick training data.

3. The paper identifies 3 annotation types in existing UI grounding training data (see Fig.2), but only two of them (Brief Function & HTML Code) are chosen in the experiments (see Table 5). An additional experiment on the Visual appearance and category annotation type would provide a more complete demonstration.

Limited Significance
1. This paper mentions that the ultimate goal of the research is to enable next-generation software automation. However, the work presented here focuses solely on the GUI grounding task, lacking exploration of practical application scenarios.
2. The experimental results indicate that the proposed AutoGUI dataset has not led to substantial advancements in GUI grounding task compared to previous work. (As shown in Table 4, apart from the self-built FuncPred benchmark, this study shows improvement only on *VWB EG* and *ScreenSpot* with minimal gains compared to the state-of-the-art.)

### Questions
See Weaknesses.

### Soundness
1

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
The paper introduces AutoGUI, an automatic annotation pipeline designed to scale the grounding of GUI elements by leveraging LLMs' annotation. The authors address the limitations of existing UI datasets, which either lack contextual functional descriptions or are limited in scale. The proposed AutoGUI pipeline automatically collects UI interaction trajectories and uses LLMs to annotate UI elements based on the observed changes in UI content before and after an interaction. For annotation quality, the authors implement LLM-aided rejection and verification mechanisms to filter out invalid or incorrect annotations w.o. human intervention.

### Strengths
1. Addressing the data scarcity in UI understanding is highly significant for advancing VLMs in GUI-oriented applications. The ability to automatically generate large-scale, high-quality GUI datasets can accelerate research and development.
2. The AutoGUI-704k provides 704,000 high-quality samples featuring multi-resolution, multi-device screenshots, diverse domains, and detailed functionality annotations. It demonstrate practical applications.
3. Experiments show that models trained on the AutoGUI-704k dataset significantly enhance UI grounding capabilities of VLMs, exhibit scaling effects with increased data size, and outperform models trained on existing (manual) GUI datasets.

### Weaknesses
My concerns about this paper mainly revolve around the following three points:

1. **Evaluation on the FuncPred Test Set:** The authors state that the FD metric ("FuncPred is the test split from our collected functionality dataset. This benchmark requires a model to locate the element specified by its functionality description") is essentially a test set drawn from the same format as their training data. It is expected that scaling up their dataset shows effectiveness on this test set. Additionally, further improvement in performance after continued training with the SeeClick data is also reasonable. However, on the **VisualWebBench**, adding the SeeClick data for continued training results in a performance gain that surpasses that achieved with the authors' full dataset:
    - **Data Quality Concerns:** Since the SeeClick data is of the type focusing purely on element grounding (e.g., ScreenSpot), does this partially reflect that the data generated by the proposed method may be of lower quality? Specifically, the fact that SeeClick, which focuses on simpler grounding tasks, leads to better performance on VisualWebBench than the full AutoGUI dataset raises questions about the quality and relevance of the functional annotations in AutoGUI for general grounding tasks. The superior performance of SeeClick on VisualWebBench suggests that the functional annotations, while useful for FuncPred, might not be as effective for broader visual grounding tasks.
    - **Performance Drop on RefExp:** Moreover, after training, the performance on the RefExp benchmark shows inferior performance for unknown reasons, yielding lower results than training with only SeeClick data. This performance drop is concerning because it suggests that the AutoGUI dataset, despite its scale, may be introducing noise or biases that negatively impact performance on tasks requiring precise spatial reasoning, which is crucial for RefExp. This raises questions about the dataset's ability to generalize across different types of grounding tasks.
2. **Performance Fluctuations with Finetuned Qwen-VL (Tab. 4):** In the main exp, regarding the experiments with finetuned Qwen-VL, it can be observed from Qwen-VL-AutoGUI702k that when finetuned using AutoGUI702k, there is significant performance fluctuation compared to the SeeClick baseline, with a range reaching up to ±20%. The substantial performance variations observed when fine-tuning Qwen-VL with AutoGUI702k, compared to the SeeClick baseline, are not adequately explained. Such large fluctuations suggest that the training process might be unstable or that the AutoGUI dataset introduces inconsistencies that are not present in the SeeClick data. This variability makes it difficult to assess the true impact of the proposed dataset and raises concerns about the reliability of the results.
3. **Unclear Process in Removing Invalid Samples:**
    - **Insufficient Explanation of Hand-Written Rules:** Authors mentions "hand-written rules" used in the process of removing invalid samples, but these rules are not well explained or detailed. The lack of transparency regarding these rules makes it difficult to assess their effectiveness and potential biases. Without detailed information, it's impossible to determine whether these rules are robust enough to handle the variety of errors that can arise in UI annotation.
    - **Lack of Justification for LLM Predictability Scores:** The process of obtaining predictability scores from the LLM outputs lacks sufficient rationale. For instance, why does the scoring range from 0 to 3? More explanation is needed on how this scoring system handles errors, biases, and ambiguous cases. The rationale behind the 0-3 scoring range is unclear, and it is not evident how this specific range effectively mitigates errors, biases, and ambiguities in the LLM-generated annotations. The absence of a clear justification for this scoring system undermines the credibility of the data cleaning process.

### Questions
My assessment is primarily based on the solidity of the experiments in this paper. I'll try to adjust my assessment after reading the rebuttal.

### Soundness
2

### Presentation
3

### Contribution
2
