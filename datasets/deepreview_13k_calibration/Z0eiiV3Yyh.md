# FlexCAD: Unified and Versatile Controllable CAD Generation with Fine-tuned Large Language Models

- Decision: Accept
- Avg Score: 5.00
- Scores: 3, 6, 6

## Abstract
Recently, there is a growing interest in creating computer-aided design (CAD) models based on user intent, known as controllable CAD generation.
Existing work offers limited controllability and needs separate models for different types of control, reducing efficiency and practicality.
To achieve controllable generation across all CAD construction hierarchies, such as sketch-extrusion, extrusion, sketch, face, loop and curve,
we propose \sysname, a unified model by fine-tuning large language models (LLMs).
First, to enhance comprehension by LLMs, we represent a CAD model as a structured text by abstracting each hierarchy as a sequence of text tokens.
Second, to address various controllable generation tasks in a unified model, we introduce a hierarchy-aware masking strategy.
Specifically, during training, we mask a hierarchy-aware field in the CAD text with a mask token.
This field, composed of a sequence of tokens, can be set flexibly to represent various hierarchies.
Subsequently, we ask LLMs to predict this masked field.
During inference, the user intent is converted into a CAD text with a mask token replacing the part the user wants to modify, which is then fed into \sysname to generate new CAD models. 
Comprehensive experiments on public dataset demonstrate the effectiveness of \sysname in both generation quality and controllability.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This paper proposed, flexCAD, a unified and versatile model for controllable CAD generation across all hierarchies using LLMs. FlexCAD addresses various limitations in existing CAD generation models. Previous models typically lack comprehensive control across CAD hierarchies and require separate models for different tasks. The proposed model leverages a structured text representation of CAD models and a hierarchy-aware masking strategy to control the generation across various levels (e.g., sketch, face, loop, extrusion). Experiments show that FlexCAD outperforms existing models on various metrics. 

Contributions: 
- FlexCAD is the first to leverage LLMs for controllable CAD generation. 
- FlexCAD greatly improves generation quality and controllability, showing its effectiveness on the sketch-level and extrusion-level controllable generation tasks.

### Strengths
- FlexCAD improves generation quality and controllability in some metrics and demonstrates its effectiveness on the sketch-level and extrusion-level controllable generation tasks.

### Weaknesses
 - Novelty is limited. The training methods being used are very standard tuning methods for LLM. 
- FlexCAD is the first to leverage LLMs for controllable CAD generation (based on the author's statement). Previous baseline "SkexGen: Autoregressive Generation of CAD Construction Sequences with Disentangled Codebooks" and "Hierarchical Neural Coding for Controllable CAD Model Generation (ICML 2023)" already use transformer architecture. 
- It would be stronger if FlexCAD can show improvement with larger margin given FlexCAD is not the best among all metrics. 
- No discussion on ethics and potential risk of this research.

### Questions
- Can the authors provide some analysis on why full model fine-tuning performs worse than LoRA on some metrics? 
- For FlexCAD, does it use few-shot or zero-shot at inference time?

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
3

### Summary
This paper proposes a unified CAD generation model that leverages large language models with a hierarchy-aware masking strategy, achieving fine-grained controllability across multiple CAD construction hierarchies and outperforming existing methods in generation quality and user-intent alignment. 
In detail, FlexCAD represents CAD models as structured text, transforming CAD construction hierarchies into sequences of text tokens, which improves comprehension by LLMs. During training, the hierarchy-aware masking replaces specific fields in CAD text with a mask token, enabling the model to predict missing parts based on user intent.
The model demonstrates significant performance improvements over existing methods like SkexGen and Hnc-CAD.

### Strengths
1. The proposed FlexCAD model effectively enables controllable CAD generation across all hierarchies, addressing a significant gap in CAD modeling by unifying control within a single framework. It achieves superior performance on the DeepCAD dataset compared to existing baselines, highlighting the method's robustness and effectiveness.
2. The paper is well-organized and clearly written, making the methodology and contributions easy to understand and follow.
3. The authors provide extensive ablation studies to analyze the impact of LLM pre-training and hierarchy-aware tokenization. These experiments demonstrate that fine-tuning pre-trained LLMs with LoRA yields the best results, underscoring the advantages of leveraging pre-trained models for CAD representation—a promising insight for future research in CAD and design automation.

### Weaknesses
1. The evaluation is limited to the DeepCAD dataset, which restricts the generalizability of the results. Testing FlexCAD on additional CAD datasets, particularly those with different structural complexities and design paradigms, would better demonstrate its robustness and adaptability across diverse design scenarios. The current evaluation does not explore how the model performs with datasets that have different levels of geometric detail or varying types of CAD operations, which is a crucial aspect for real-world applicability.
2. The paper lacks references to relevant recent work, such as “OpenECAD: An Efficient Visual Language Model for Editable 3D-CAD Design” and “CadVLM: Bridging Language and Vision in the Generation of Parametric CAD Sketches,” which address related challenges in CAD generation and infilling. Including these would strengthen the context and positioning of the work by acknowledging alternative approaches and highlighting the specific advantages of the proposed method in relation to the broader landscape of CAD generation research. The absence of these comparisons makes it difficult to fully assess the novelty and impact of FlexCAD.


### Questions
1. During training, what is the average mask ratio per training sample, and is there any observed relationship between performance and the mask ratio?
2. Given that a single masked input can produce multiple possible outputs, as shown in Figure 5, which output is selected for the final evaluation?

### Soundness
3

### Presentation
3

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
This paper presents FlexCAD, a unified model for controllable CAD generation, enhancing the ability to generate CAD models based on user intent. Unlike existing methods requiring separate models for different controls, FlexCAD enables controllable generation across multiple CAD construction hierarchies (e.g., sketch, extrusion, face). The authors fine-tune large language models (LLMs) and represent CAD models as structured text, abstracting each hierarchy into a sequence of text tokens for better comprehension. A hierarchy-aware masking strategy is introduced, masking specific fields during training to predict the masked parts based on user input during inference. In general, this paper is well organized.

### Strengths
+ Novel use of LLMs for CAD design
+ The authors propose a unified framework based on fine-tuning LLMs to bridge LLMs and CAD models, including dividing CAD models into multiple hierarchies and representing CAD models with sequential tokens and 
+ The authors introduce a hierarchy-aware masking strategy to achieve controllable generation based on the mask-and-prediction method
+ Experimental results show the proposed method achieves good results and verify the effectiveness of each component

### Weaknesses
 - The motivation of using LLMs for CAD generation is not very clear. The authors are recommended to clarify why LLMs are the good choice to do this task. 

- The ablation study in Tab 3 is clear to make a comparison among different foundation models, pre-training, and fine-tuning. However, could LLaMA-3 do CAD generation in a zero-shot manner? How helpful is the proposed fine-tuning method compared with the zero-shot setting?

- The evaluation for prompt-result alignment is unclear, e.g., intent understanding and instruction following. 

- Some experimental details may be missing, e.g., the instructions used to prompt GPT-4o.



### Questions
- Does the proposed method inherit some advantages of LLMs, such as instruction following and in-context learning? 

- The proposed method assumes users skilled at the defined hierarchies so that they can transform their intent into mask-based instructions during inference. Can users express their intent using natural language and then the transformation task is given to LLMs?

- Does the fine-tuned model strictly follow the grammar of CAD structured text? If not, is there any failure case which may not be parsed into a valid CAD model? How about the percentage? 

- Compared with prior work, is there any drawback to using LLMs? How about the efficiency?

### Soundness
3

### Presentation
3

### Contribution
3
