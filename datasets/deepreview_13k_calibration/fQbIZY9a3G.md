# RiTTA: Modeling Event Relations in Text-to-Audio Generation

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5

## Abstract
Despite significant advancements in Text-to-Audio (TTA) generation models achieving high-fidelity audio with fine-grained context understanding, they struggle to model the relations between audio events described in the input text. However, previous TTA methods have not systematically explored audio event relation modeling, nor have they proposed frameworks to enhance this capability. In this work, we systematically study audio event relation modeling in TTA generation models. We first establish a benchmark for this task by: (1) proposing a comprehensive relation corpus covering all potential relations in real-world scenarios; (2) introducing a new audio event corpus encompassing commonly heard sounds; and (3) proposing new evaluation metrics to assess audio event relation modeling from various perspectives. Furthermore, we propose a finetuning framework to enhance existing TTA models' ability to model audio events relation.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper primarily introduces a benchmark for the relationships between multiple audio events, with its main contribution being the creation of a new dataset and the establishment of several novel evaluation metrics.

### Strengths
1. Compared to previous work, the authors' most significant contribution lies in the development of a comprehensive dataset that assesses the relationships between multiple audio events.
2. Using temporal relationships as an example, the authors provide a detailed explanation of the dataset construction process and propose new evaluation metrics. They also conduct experiments using both the pre-trained TTA model and the fine-tuned version.

### Weaknesses
1. I am unclear as to why RiTTA was submitted to the generative model track, as the primary contribution clearly stems from the new dataset and evaluation metrics related to the benchmark, rather than from advances in generative modeling.
2. In terms of innovation, the authors are not the first to explore audio event relationship modeling. RiTTA extends temporal relationships to four types of relationships, but the overall process appears to be data-driven. However, merely using the TTA model to model complex relationships is insufficient. As demonstrated in Figure 7, there is a performance decline with "not" relationships. I was expecting a novel TTA framework capable of jointly modeling relationships between different audio events. Unfortunately, RiTTA only fine-tunes the TTA model, which limits its novelty.
3. Regarding the core contribution—the dataset—there are several potential shortcomings. First, the dataset construction process does not seem to require significant effort. Second, the dataset itself feels somewhat toy. While the authors attempt to enhance its randomness, expanding each example to five events via ChatGPT is far from sufficient (only 5?); 500 events might be a more appropriate target. Additionally, the use of only one-channel audio for spatial relationships could limit the dataset’s diversity.

### Questions
1. The authors provide a detailed explanation of the dataset construction process using temporal relationships as an example, but I am still curious about how other relationships, such as spatial relationships, were constructed. How were the corresponding text-audio pairs created for these? Further clarification would be beneficial.
2. Should out-of-domain scenarios be considered when forming the test set?
3. I could not find the RiTTA dataset in the supplemental materials.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
1

### Summary
1.	Benchmark Construction: Created an audio event relation corpus for TTA tasks, covering common spatial, temporal, count, and compositional relations. Additionally, an audio event category corpus encompassing various everyday sounds was established to provide foundational data for studying event relation modeling in TTA.
2.	Evaluation Framework: Proposed a multi-stage relation-aware evaluation framework (MSR-RiTTA) that quantifies a model’s ability to capture audio event relations from multiple perspectives, offering more targeted metrics than existing TTA evaluation standards.
3.	Fine-Tuning Framework: Developed a fine-tuning strategy aimed at enhancing current TTA models’ capacity to model audio event relations, showing significant improvement in benchmark tests.

### Strengths
The paper presents a substantial contribution to the field of Text-to-Audio (TTA) generation by introducing the RiTTA framework, which systematically addresses the modeling of audio event relations—a previously underexplored area. It proposes an innovative multi-stage, relation-aware evaluation framework (MSR-RiTTA) to more accurately assess the performance of TTA models in capturing complex spatial, temporal, count, and compositional relationships. The research is rigorous in its dataset construction and experimental validation, demonstrating clear improvements in TTA models’ relation modeling abilities. This work stands out for its originality, methodological clarity, and significant potential impact, expanding TTA applications in areas like virtual reality and immersive media.

### Weaknesses
The paper benchmarks seven recent TTA models (such as AudioLDM and Tango) but focuses primarily on single-strategy models, and without testing in more complex scenarios like audio events in virtual reality or interactive environments. This limits the framework’s applicability across different model types and environments. A wider variety of model types, such as multimodal generation models or models optimized for extended audio sequences, and more diverse application datasets, like multi-event VR audio environments are recommended.

The description of the fine-tuning strategy is too general, lacking detailed information on training settings, parameter tuning strategies, and specific experimental procedures. The lack of details such as specific hyperparameter settings, number of iterations, and choice of loss function also weakens persuasiveness.

### Questions
Refer to the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposed an audio event relation corpus for text-to-audio generation and a new evaluation benchmark. TTA models finetuned in this corpus got better generation of the audio event relations.

### Strengths
The proposed corpus is important for research on audio event relations, which can be used for TTA with good quality and comprehension.

### Weaknesses
I have some concerns about this work:

1. The corpus only contains 25 categories, which seems to not easily generate to other categories with relations. Previous training metarials like AudioCaps and Clotho have over 100 classes.

2. The paper targets on mono-channel audio, but in this case, the spatial distance makes little sence. How can you accurately measure whether the event is from 1m or 7m? I think multi-channel audio would also be interesting, e.g. a car driving from left to right.

3. The FAD and FD used feature embeddings from pretrained on VGGish model. However, this model is known as its poor performance. Even though some baselines may use this tool, I think modern backbone models should be considered.

### Questions
1. Except the 25 categories, what are the results of other audio events with relations?  TTA is more like an open-set problem, so unseen labels' evaluation is needed.

2. What are the results on the previous test data from the baseline models? Will the finetuning affect the original results?

3. Can the model handle other lengths of audio instead of 10s?

### Soundness
3

### Presentation
3

### Contribution
3
