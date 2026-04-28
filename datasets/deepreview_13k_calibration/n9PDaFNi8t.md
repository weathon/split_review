# OS-ATLAS: Foundation Action Model for Generalist GUI Agents

- Decision: Accept
- Avg Score: 7.50
- Scores: 6, 8, 8, 8

## Abstract
Existing efforts in building GUI agents heavily rely on the availability of robust commercial Vision-Language Models (VLMs) such as GPT-4o and GeminiProVision. Practitioners are often reluctant to use open-source VLMs due to their significant performance lag compared to their closed-source counterparts, particularly in GUI grounding and Out-Of-Distribution (OOD) scenarios. To facilitate future research in this area, we developed \action—a foundational GUI action model that excels at GUI grounding and OOD agentic tasks through innovations in both data and modeling.
We have invested significant engineering effort in developing an open-source toolkit for synthesizing GUI grounding data across multiple platforms, including Windows, Linux, MacOS, Android, and the web. Leveraging this toolkit, we are releasing the largest open-source cross-platform GUI grounding corpus to date, which contains over 13 million GUI elements. This dataset, combined with innovations in model training, provides a solid foundation for \action to understand GUI screenshots and generalize to unseen interfaces.
Through extensive evaluation across six benchmarks spanning three different platforms (mobile, desktop, and web), \action demonstrates significant performance improvements over previous state-of-the-art models. Our evaluation also uncovers valuable insights into continuously improving and scaling the agentic capabilities of open-source VLMs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The work introduces OS-ATLAS, a foundational GUI action model for GUI grounding and Out-Of-Distribution (OOD) agentic tasks. The authors synthesize large-scale multi-platform GUI grounding data. The OS-ATLAS model trains on this data and further fine-tunes with action datasets to address specific agent tasks. The model demonstrates significant performance improvements over previous models and shows the effectiveness of the synthetic GUI grounding dataset. The author also promises to open-source the data and related models, which will significantly impact the development of the GUI agent.

### Strengths
1. The work proposes a pretraining-then-fine-tuning framework for GUI grounding and agentic tasks, which is natural and unifies the training and evaluation process of these tasks.
2. The work synthesizes a large-scale multi-platform GUI grounding data for pertaining and promises to open-source the data.
3. The experimental results showed significant improvement, demonstrating their effectiveness.

### Weaknesses
1. The authors propose synthesizing large-scale GUI grounding datasets across platforms. However, the number of instances in Table 1 is not similar for each platform, especially for desktop (54K).
2. There are some missing details: how to ensure the correctness of the synthetic data, the specifics of action tuning and the format of the inputs and outputs, and the precise meaning of "thought."

### Questions
See the Weakness part.

### Soundness
3

### Presentation
2

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
This paper presents a project that aims to replace commercial VLMs such as GPT-4o in serving as the base model for GUI agents, with a special focus on GUI grounding and atomic action execution. The project involves a large scale grounding and action dataset, and a trained model named OS-Atlas. Benchmarking on various grounding and atomic action datasets show SOTA performance.

### Strengths
The main claim of the paper is to serve as an open-source alternative to commercial VLMs like GPT-4o in building GUI agents. The claim is well supported, with the condition that all the data, code, and model are open-sourced as promised.

Specifically, the contribution mainly involves (1) a dataset with 2.3 million screenshots on various platforms and operating systems; (2) OS-Atlas (4B/8B) model that achieves SOTA performance on GUI grounding and atomic action execution.

Having a good base model and data would be beneficial for the community on future GUI research.

### Weaknesses
1. The contribution and novelty limited to the main claim of serving as an open-source alternative to commercial VLMs. Such VLMs like GPT-4o are not designed specifically for GUI scenarios, and fail to address GUI specific challenges. So does this work.

1.1. The study does not touch any GUI specific challenges, such as specific visual and text distribution, cross-system differences, long action planning, and so on.

1.2. It also does not present new evaluations that are more suitable for GUI. For example, setting up an emulator-style benchmark with the data synthesis toolkit.

Nonetheless, those aspects are beyond the claim of the paper, and future research on related topics could benefit from the data and model released by this study.

2. Extra analyses would be beneficial:

2.1. There could be more analyses on the data and model scaling, to help future study understand the amount of extra data and compute needed if the application needs further model enhancement or finetuning. The existing scaling analyses in Figure 3 and Sec. 4.2. are somewhat noisy and fail to give clear directions.

2.2. To better support the claim on being effective “universally across all GUIs,” there could be more discussion on the per-task and environment performance. It remains unclear why certain tasks perform better or worse on web/desktop/mobile and different operating systems. Do such differences attribute to model, data, or task setting? And what are the corresponding data and compute needed to improve on a specific setting of interest.

### Questions
Please see weaknesses for questions, mostly on the analyses part. The released data and model would be a good contribution to the community, looking forward to seeing it being released.

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
The paper aims to enhance foundation model for GUI agent research. The authors introduce a GUI grounding synthesis tool and collect a large-scale dataset using the toolkit. Using the datasets, OS-Atlas is developed, which is a cross-platform foundation action model for GUI. Detailed results and evaluations are also discussed.

### Strengths
- Open-source toolkit and data are available for the research community, which is currently lacking in GUI agent research area
- Data collection and modeling processes are extensive and well-planned and motivated.

### Weaknesses
 - I would appreciate more details about the toolkit, particularly on its usability and how other researchers could potentially customize it for their own use cases.

### Questions
- Could the authors comment on the usability of the toolkit and how other researchers could potentially customize it for their own use cases.
- Any discussions on choosing a pertaining + fine-tuning over mixing grounding and action data?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a high-performance GUI Agent, OS-ATLAS, trained on a synthetic grounding dataset and operating within a unified action space. Experiments on grounding tasks and agent tasks demonstrate that OS-ATLAS significantly outperforms previous state-of-the-art models.

### Strengths
This paper produces a large-scale, open-source corpus of screenshots covering multiple platforms and proposes a high-performance GUI Agent that significantly outperforms previous VLM-based GUI action models, making a substantial contribution to the field of vision-based GUI Agents. Additionally, the paper is logically coherent, relatively complete in content, and well-organized.

### Weaknesses
Experimental Concerns

1. Table 4 and Table 5 lack the results of state-of-the-art methods. It would be more appropriate to include these SOTA results for comparison with OS-ATLAS to demonstrate that it outperforms previous methods. Specifically, OdysseyAgent achieves 65.22% AMS (or SR, as referred to in this paper) on the GUI-Odyssey benchmark, which outperforms OS-ATLAS (4B/8B).

2. OS-ATLAS (8B) performs worse than OS-ATLAS (4B) on the AndroidControl-Low/High and GUI-Odyssey benchmarks. Moreover, OS-ATLAS (8B) exhibits poorer performance on the AndroidControl-High and GUI-Odyssey benchmarks compared to SeeClick, which uses Qwen-VL as the base model and a lower fixed input resolution (448x448). It would be beneficial to provide an explanation for this performance gap.

### Questions
Which benchmark is used in Figure 5?

### Soundness
3

### Presentation
3

### Contribution
3
