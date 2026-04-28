# Time-Accurate Speech Rich Transcription with Non-Fluencies

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 6, 5, 5

## Abstract
Speech is a hierarchical collection of text, prosody, emotions, dysfluencies, etc. Automatic transcription of speech that goes beyond text (words) is an underexplored problem.
We focus on transcribing speech along with non-fluencies (dysfluencies). The current state-of-the-art pipeline \citep{lian2024ssdmscalablespeechdysfluency} suffers from complex architecture design, training complexity, and significant shortcomings in the local sequence aligner, and it does not explore in-context learning capacity. In this work, we propose SSDM 2.0, which tackles those shortcomings via four main contributions:
(1) We propose a novel \textit{neural articulatory flow} to derive highly scalable speech representations.
(2) We developed a \textit{full-stack connectionist subsequence aligner} that captures all types of dysfluencies.
(3) We introduced a mispronunciation prompt pipeline and consistency learning module into LLM to leverage dysfluency \textit{in-context pronunciation learning} abilities.
(4) We curated Libri-Dys \citep{lian2024ssdmscalablespeechdysfluency} and open-sourced the current largest-scale co-dysfluency corpus, \textit{Libri-Co-Dys}, for future research endeavors.
In clinical experiments on pathological speech transcription, we tested SSDM 2.0 using nfvPPA corpus primarily characterized by \textit{articulatory dysfluencies}.
Overall, SSDM 2.0 outperforms SSDM and all other dysfluency transcription models by a large margin. See our project demo page at \url{https://berkeley-speech-group.io/SSDM2.0/}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this work, the authors tackle the problem of fine-grained speech transcription along with non-fluencies (dysfluencies). Towards this, they present a new system SSDM 2.0 (that builds on top of SSDM, Lian et al. 2024) with some key modifications including a new articulatory feature-driven flow-based model, a full-stack connectionist subsequence aligner for improved coverage of dysfluencies and mispronunciation in-context learning using LLMs. This system consistently outperforms SSDM on multiple evaluation benchmarks.

### Strengths
* The problem is well-motivated and the authors propose multiple new and innovative techniques (SSDM 2.0) to tackle the problem of time-accurate transcription of speech with dysfluencies.
* The authors open-source a large dysfluency corpus (Libri-Co-Dys) to encourage further work in this domain.
* SSDM 2.0 is significantly more performant (both in terms of accuracy and efficiency) compared to prior state-of-the-art (SSDM).

### Weaknesses
 * The writing could be improved overall, especially the main technical parts in Sections 3, 4.
  * Rather than diving right into the details of each module in Section 3, it would have been useful for the reader to first get a complete description of the full SSDM 2.0 framework and the role of each module (neural articulatory flow, full-stack CSA, etc.) in the overall pipeline before learning about individual details. The current structure makes it difficult to understand how the different components fit together to achieve the overall goal. A high-level overview with a clear system diagram would greatly improve readability and comprehension before delving into the specifics of each module.
  * Notation can be made cleaner in many places (e.g., inconsistent definition of H with H \in R^{K \times T} in Section 3.1 and H \in R^{T \times K} in Section 3.2), and illustrative examples would be useful especially for full-stack CSA. The inconsistent notation for H is confusing and needs to be resolved. Furthermore, the explanation of the full-stack CSA lacks clarity and would benefit from a concrete example illustrating its operation, especially how it handles dysfluencies and mispronunciations. The current description is too abstract and difficult to follow.
  * There are also many references to Lian et al. 2024 which disrupts the overall flow and makes it less self-contained. The frequent references to the previous work make it difficult to understand the current contribution without constantly referring to another paper. The paper should be more self-contained, providing sufficient background information and context to understand the proposed method without relying heavily on external references.

* The authors should motivate the gestural scores in H, right in Section 3.1 -- How is it rule-generated, what is K, why is it sparse and how does H relate to articulatory gestures? Since X is already articulatory data, how does the information in H differ from that in X?  More about H only appears scattered across Sections 3.2 and 3.3. The introduction of gestural scores H is not well-motivated. The relationship between H and the articulatory data X is unclear, and the explanation of how H is generated and its properties (sparsity, dimensionality K) is insufficient. The paper should clearly articulate the motivation behind using H and how it provides a more useful representation than X.

* Can the authors further motivate their choice of using a count encoder + index generator to identify active regions? One could devise alternate schemes like using discretized binary gates (using Gumbel softmax) for every element in X_i to denote whether or not it is part of an active region. It would be useful to know if the proposed design was motivated by some articulatory or speech production priors. The rationale behind using a count encoder and index generator for identifying active regions is not clearly explained. The authors should compare this approach with alternative methods, such as using discretized binary gates, and justify their design choice based on articulatory or speech production priors. The current explanation lacks sufficient detail and motivation.

* From the proposed SSDM 2.0 architecture and the demo page, the LLM responses are descriptive and in natural language. Apart from objective measures of F1/WPER, did the authors consider evaluating these free-form responses containing pronunciation feedback via a human evaluation? The evaluation of the LLM responses is limited to objective metrics. Given that the responses are in natural language and provide pronunciation feedback, a human evaluation would be necessary to assess the quality and usefulness of the feedback. The paper should include a human evaluation to complement the objective metrics.

* Libri-Co-Dys (with multiple dysfluencies) is presumably harder than Libri-Dys (with a single dysfluency). However, the F1 scores using SSDM 2.0 on Libri-Dys appear to be no worse than that on Libri-Co-Dys (across 30, 60, 100 training data settings). Could the authors comment on this? The similar performance on Libri-Dys and Libri-Co-Dys is counterintuitive and requires further explanation. The authors should provide a detailed analysis of why the model performs similarly on both datasets, despite the expected difference in difficulty.

* Is there any fraction of Libri-Co-Dys that does not contain dysfluencies? If not, it is useful to check how SSDM 2.0 performs on fluent instances. Please comment. The lack of fluent speech in Libri-Co-Dys is a limitation. The authors should evaluate the model's performance on fluent speech to assess its generalizability and robustness. This is important to understand the model's behavior in the absence of dysfluencies.

* Minor comment: There are no arrows coming out of 3 and 4 (inside yellow circles) in Figure 4 (under Pre-Alignment Training).

* Section 6.8 could be moved entirely to Appendix A.5.

* The authors should do a careful editorial pass of the draft. Listing some examples of typos below:
  * ARTCULATORY --> ARTICULATORY (Title of Section 3.2)
  * Traing Data --> Training data (Section 6.2)
  * Title of Section 6.4 does not parse

### Questions
* The authors should motivate the gestural scores in H, right in Section 3.1 -- How is it rule-generated, what is K, why is it sparse and how does H relate to articulatory gestures? Since X is already articulatory data, how does the information in H differ from that in X?  More about H only appears scattered across Sections 3.2 and 3.3.

* Can the authors further motivate their choice of using a count encoder + index generator to identify active regions? One could devise alternate schemes like using discretized binary gates (using Gumbel softmax) for every element in X_i to denote whether or not it is part of an active region. It would be useful to know if the proposed design was motivated by some articulatory or speech production priors.

* From the proposed SSDM 2.0 architecture and the demo page, the LLM responses are descriptive and in natural language. Apart from objective measures of F1/WPER, did the authors consider evaluating these free-form responses containing pronunciation feedback via a human evaluation?

* Libri-Co-Dys (with multiple dysfluencies) is presumably harder than Libri-Dys (with a single dysfluency). However, the F1 scores using SSDM 2.0 on Libri-Dys appear to be no worse than that on Libri-Co-Dys (across 30, 60, 100 training data settings). Could the authors comment on this?

* Is there any fraction of Libri-Co-Dys that does not contain dysfluencies? If not, it is useful to check how SSDM 2.0 performs on fluent instances. Please comment.

* Minor comment: There are no arrows coming out of 3 and 4 (inside yellow circles) in Figure 4 (under Pre-Alignment Training).

* Section 6.8 could be moved entirely to Appendix A.5.

* The authors should do a careful editorial pass of the draft. Listing some examples of typos below:
  * ARTCULATORY --> ARTICULATORY (Title of Section 3.2)
  * Traing Data --> Training data (Section 6.2)
  * Title of Section 6.4 does not parse

### Soundness
4

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper presents a novel approach to transcribing speech that includes non-fluencies (such as repetitions, blocks, and sound replacements) beyond traditional text transcription. The authors introduce SSDM 2.0, which improves upon previous models by offering a highly scalable speech representation system called Neural Articulatory Flow, a comprehensive Full-Stack Connectionist Subsequence Aligner (FCSA) for aligning dysfluent speech with text, and a new method for in-context pronunciation learning that enhances dysfluency detection. Additionally, they open-source the largest co-dysfluency corpus, Libri-Co-Dys, for future research. SSDM 2.0 outperforms existing dysfluency transcription models while reducing training complexity significantly. The paper demonstrates the scalability and efficiency of the proposed system in both single and co-dysfluency transcription tasks.

### Strengths
1. The paper introduces SSDM 2.0, a novel model that goes beyond traditional transcription to accurately capture non-fluencies, filling a gap in existing speech transcription research. It introduces creative components like Neural Articulatory Flow for scalable speech representation and the Full-Stack Connectionist Subsequence Aligner for precise dysfluency alignment.
2. SSDM 2.0 is thoroughly evaluated with rigorous experimentation across multiple datasets.
3. The paper clearly defines its focus on time-accurate dysfluency transcription and outlines the shortcomings of previous models.
4. The model’s ability to transcribe co-dysfluencies has broad implications for fields such as speech therapy, language learning, and automatic speech recognition.

### Weaknesses
The paper includes a great deal of detail. However, there are several aspects that could be further clarified:
1. The evaluation details of the HuBERT and Soundstorm models in Table 1 are not explained in the paper. For instance, the original HuBERT paper only tested on the LibriSpeech and LibriLight datasets. How was the HuBERT model in this paper trained, and what training data was used? Specifically, were the dysfluent labels used during training of the HuBERT model, or was it used as a fixed feature extractor? The paper mentions a two-linear probe for frame-level phoneme classification, but the specifics of how this probe is trained and integrated with the HuBERT features are unclear. Furthermore, the paper should clarify if the phoneme labels used are standard phonemes or dysfluency-specific phonemes.
2. The Acoustic Encoder of the model is WavLM, but Table 1 only shows results for HuBERT. Since WavLM generally outperforms HuBERT, the authors should consider adding more experiments comparing WavLM with NAF. It is unclear why WavLM results are omitted from Table 1, and a direct comparison is necessary to understand the relative performance of NAF against a strong baseline like WavLM. The paper should also clarify whether WavLM is used as a fixed feature extractor or if it is fine-tuned during the training process.
3. While the paper introduces many new modules, the comparison of baseline models could be more diverse. For example, the authors could include results from directly using a speech encoder (e.g., HuBERT, Whisper encoder) to extract speech representations as input for the LLM, followed by fine-tuning with LoRA. This would provide a clearer understanding of whether the added modules effectively improve the model's performance. Specifically, the paper should explore if a simpler approach of directly using a pre-trained speech encoder, followed by a lightweight fine-tuning method like LoRA, can achieve comparable results. This would help isolate the contribution of the proposed modules.
4. Although many new modules are proposed, there is a lack of comprehensive ablation studies to verify whether each module is necessary. For example, Equation 11 includes six different loss terms, but there are no corresponding experiments demonstrating whether each loss term contributes to performance improvement. While some related experiments are included later in the paper, they remain incomplete. The paper should provide a detailed breakdown of the impact of each loss term, including experiments where each term is individually ablated and in combinations, to understand their relative importance and potential interactions.

### Questions
1. How was the HuBERT model trained in this paper, and what specific training data was used, given that the original HuBERT paper only evaluated on LibriSpeech and LibriLight datasets?
2. Why does Table 1 only show results for HuBERT when the Acoustic Encoder is WavLM, and can the authors provide additional comparisons between WavLM and NAF, considering WavLM generally outperforms HuBERT?
3. Could the authors include more diverse baseline model comparisons, such as using a speech encoder like HuBERT or Whisper encoder with fine-tuning via LoRA, to better assess the impact of the new modules on performance improvement?
4. Can the authors provide more comprehensive ablation studies to verify the necessity of each proposed module, including experiments showing the impact of each loss term in Equation 11 on model performance?

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
2

### Summary
This paper proposes a framework named SSDM 2.0 to better transcribe the speech with dysfluencies. This framework includes Neural Articulatory Flow (NAF) to extract scalable and efficient dysfluency-aware speech representation, Full-Stack Connectionist Subsequence Aligner(FCSA) for dysfluency alignments, and Mispronunciation In-Context Learning and Consistency Learning in langauge
model for dysfluency transfer. On top of that, the author open-sources a large simulated speech co-dysfluency corpus called Libri-Dys-Co.

Experiments are designed to evaluate the scalability and efficacy of the proposed NAF representation and the performance of SSDM 2.0 in detecting dysfluencies in speech.

### Strengths
* Novel methodology. The paper proposes multiple new methodologies such as Neural Articulatory Flow which encodes semi-implicit speech representations that align closely with human speech production and Fullstack Connectionist Subsequence Aligner(FCSA) which develops a comprehensive alignment mechanism capable of handling diverse dysfluencies, improving the precision of non-fluency detection. The proposed methods are shown to significantly reduce computational complexity, allowing the model to scale effectively with larger datasets. 
* Comprehensive evaluation. The author designs evaluation and benchmarks to cover proposed methods.
* Contribution of new resources. This paper open-sources a large-scale co-dysfluency corpus (Libri-Co-Dys) with over 6,000 hours of annotated speech, providing a valuable resource for future research in dysfluency transcription and detection.
* Potential real world application: The proposed framework could accurately transcribe and detect dysfluencies and has significant implications for speech therapy, language screening, and spoken language learning.

### Weaknesses
 * The writing style of this paper comes with overly formal language and verbose phrasing. One instance is the beginning of section 3: "Notwithstanding, the neural gestural system proposed by Lian et al. (2024) is encumbered by complex design and challenges in equilibrating multiple training objectives such as self-distillation." The usage of "notwithstanding", "encumbered" and "equilibrate" is not necessary and they all have synonyms that are commonly used. The phrasing of the sentence is not concise. Making the paper overall less comprehensible to the readers.
*  Framework complexity. Even though the paper claims that SSDM 2.0 has 10x less training complexity of its precedent work SSDM, the integration of NAF, FCSA, and NICL adds more layers of complexity to the model. There is lack of complexity comparison of other types of baseline systems to provide a reference of where it stands in all viable options.
* The presentation of the paper needs to improve:
  + Many concepts mentioned in this paper are not self-contained and the reader has to refer to other papers. For instance, AAI.
  + Given the layers of complexity brought by multiple different modules/methods in the framework, an overview of the it should be first given based on Figure 2 before breaking it down to individual components.
* Lack of ablation studies. Table 1 only shows difference with or without neural articulatory flow loss and post-interpretable training, there is no assessment of the significance of other proposed components.
* Lack of real-world data. There is a over-reliance on synthetic data which arises questions about how the system performs in real world scenarios.

### Questions
+ I suggest removing the claim of complexity improvement from the paper if there is no enough space to explore in details.
+ In section 6.7, I think a more fair baseline would be SSDM 2.0 removing the NICL tuning steps.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents a novel pipeline to model and identify speech disfluencies. In tandem it presents a sizable dataset containing disfluent utterances for further work in the field.

### Strengths
The paper offers several novel techniques to assist in ongoing work for modeling speech disfluencies. I particularly find their development of the neural articulatory flow model fruitful for in-depth modeling of patient vocalizations during therapy. Each method utilized in their pipeline is of significant interest for a standalone paper on the topic, and has sizable justification for consideration in work in this field. In addition, their development of a dysfluency corpus is incredibly important for the field of dysfluency modeling (most datasets are rather sparse and limited in coverage, there is a critical need in the research community for more datasets for study).

### Weaknesses
This paper has a significant organizational issue that makes it difficult for an outside reader to follow. The vast majority of necessary information for a researcher outside disfluent speech research to understand the paper has been relocated to the appendix. This makes reading and evaluation of the paper rather difficult. For example, the researchers have chosen nfvPPA as a primary case study for their experiments in a field that could just as well consider Parkinsons and other variants of Aphasia as a case study. This information is not presented to the reader in the paper proper; it is instead moved to Appendix A.2. This is information that should be more clearly presented.

While this would not be an issue for a specialized conference, ICLR is general enough that consideration should be made for outside researchers to follow. Care should be made for establishing clear cases of dysfluency and conditions that cause it. As well, given that articulation modeling is a key subject of the paper, it should be presented clearly in the background section.

### Questions
Suggestion: reconsider what elements in the main paper and which elements in the appendix should be moved. Please take consideration that your colleagues may not have knowledge of dysfluency research or even models of language production.

Could you clarify why your models consider codecs? If was difficult to follow why these should serve as the audio input format.

Have you considered the potential bias involved in evaluating speech production and how it would dovetail with use of Speech LMs? While in aphasic cases this is more clear cut, I'm suspicious about how the work may mislabel dialect speakers as dysfluent speakers.

### Soundness
3

### Presentation
3

### Contribution
2
