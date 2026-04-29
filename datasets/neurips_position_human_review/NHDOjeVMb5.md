# Text Embeddings Should Capture Implicit Semantics, Not Just Surface Meaning

- Decision: Reject
- Scores: 4, 7, 6

## Abstract
\textit{This position paper argues that the text embedding research community should move beyond surface meaning and embrace implicit semantics as a central modeling goal.}
Text embedding models have become foundational in modern NLP, powering a wide range of applications and drawing increasing research attention.
Yet, much of this progress remains narrowly focused on surface-level semantics. 
In contrast, linguistic theory emphasizes that meaning is often implicit, shaped by pragmatics, speaker intent, and sociocultural context.
Current embedding models are typically trained on data that lacks such depth and evaluated on benchmarks that reward the capture of surface meaning. 
As a result, they struggle with tasks requiring interpretive reasoning, speaker stance, or social meaning. 
Our pilot study highlights this gap, showing that even state-of-the-art models perform only marginally better than simplistic baselines on implicit semantics tasks.
To address this, we call for a paradigm shift: embedding research should prioritize more diverse and linguistically grounded training data, design benchmarks that evaluate deeper semantic understanding, and explicitly frame implicit meaning as a core modeling objective, better aligning embeddings with real-world language complexity.

## Human Reviews

## Human Reviewer 1

### Rating
4

### Rating Number
4

### Confidence
5

### Summary
The authors' position aims to inform the audience about today's textual embedding models, which lack knowledge of implicit semantics. Indeed, all the current models have been trained on tasks, datasets, and with training procedures not designed to handle such information. Hence, the authors inspect the main definitions of implicit semantics on three different linguistic levels (i.e., Utterance, Speaker, and Society), survey the actual panorama of text-embedding models available, and design a novel benchmark to assess the evidence of existing gaps on those models, which includes datasets (still an ongoing work as a pilot study) and renewed evaluation approaches. The proposal highlights a decrease in performance on the experimentation of the current models, discussing shortcomings in the adopted training procedure, existing datasets, and evaluation frameworks. The authors claim to include implicit semantics directly as a model objective of text embeddings, despite enforcing training procedures and designing focused benchmarks to bridge the existing gap, deviating from the contemporary research direction.

### Strengths
- The structure of the paper is simple, concise, and effective.
- The authors' position is timely and exciting given the current literature.
- The reasoning and experimentation to support the position of the paper are well-designed.
- The topic is certainly relevant to the community (or at least to different sub-areas).
- The surveyed work in describing today's panorama of available text embedding models is comprehensive and highly relevant as a further research tool.
- The paper is well-written and easy to follow.

### Weaknesses
- The paper presents a lot of repetition regarding its central objective and suggested solutions throughout all the sections, which is space-consuming and weighs down the reading.
- Figure 1 is misleading or not comprehensively presented if compared with the results shown in Table 1.
- The proposal lacks meaningful examples to highlight the actual influence of implicit semantics (Section 2.1, 2.2).
- Final sections reflect some inconsistencies. In section 4, the authors state that training processes fail to capture implicit semantics, while they primarily discuss datasets and tasks, with training approaches only defined as titles for subsections. In section 5, the authors' focus remains on the task rather than inspecting benchmarks, except for the Semantic Textual Similarity (STS) task.
- Lacking information on the novel refined dataset and the engaged procedure to train or evaluate models (Appendix A.1 just lists a bunch of different tasks never explained to the reader, also by including a further level of implicit semantics analysis outside the three ones presented before).

Minor: Some inaccuracies in section 7 (please see Questions)

### Questions
1) Do the authors consider the concept of LLMs from text embedding as different (from what emerges in 7.3, line 307)?
2) Is the example in section 2.1 more related to the emotions conveyed rather than implicit semantics? (The unexpected event of passing the test is related to astonishment). Moreover, the sentence "Sam quit smoking" already presents in the surface semantics of the verb quit implies that something has reached an end. Is there a formal definition that further justifies this sample or a different one?
3) What emerges is that tasks like IR, RAG, and some multi-tasking were not designed to handle implicit semantics, which is quite normal since their interest lies in retrieving documents. Can the authors elaborate?
4) Why do the authors say that many models barely surpass Bag-of-Tokens, while the performances of most of the models, as depicted in Table 1, show a large margin of difference? Are these results showing that existing models, especially contextualized embedding models, can already manage implicit semantics?
5) How do the authors intend to improve the model's learning of implicit semantics by using synthetic data generated by models that have not yet learnt them?

### Presentation
4

---

## Human Reviewer 2

### Rating
7

### Rating Number
7

### Confidence
4

### Summary
This is a position paper that argues the text embedding research community should shift its focus from surface-level semantics to implicit semantics as a core modeling objective. The authors state that while current text embedding models have made significant progress, they are primarily trained and evaluated on tasks that only capture shallow meaning, such as lexical overlap and syntactic variation. Drawing on linguistic theory, the paper proposes a three-tier framework for implicit meaning: utterance level (pragmatics), speaker level (stance), and society level (sociolinguistics). The paper includes a pilot study that demonstrates a performance gap, showing that state-of-the-art models perform only marginally better than a Bag-of-Tokens baseline on tasks that require implicit understanding. To address this gap, the authors call for a paradigm shift, advocating for the use of more diverse, linguistically grounded training data and the development of new benchmarks that explicitly evaluate deeper semantic understanding.

### Strengths
1. The paper has a clear and compelling argument that is well-supported by linguistic theory. It effectively highlights a critical, often overlooked, limitation in the current field of text embedding research.
2. The inclusion of a pilot study provides concrete evidence to back the central claim. The "performance gap" shown in Figure 1, where top models perform significantly worse on implicit semantics tasks compared to surface meaning tasks, is a powerful visual and empirical demonstration of the problem.
3. The three-tier framework (utterance, speaker, society) for implicit meaning is a strong organizational tool that helps the reader understand the different facets of the problem. It moves the discussion beyond a vague notion of "deeper meaning" into a specific, actionable analysis.
4. The paper provides a thorough review of existing text embedding models, training processes, and benchmark suites, effectively showing how these current practices reinforce the focus on surface semantics and neglect implicit meaning.

### Weaknesses
1. Limited Pilot Study: The empirical evidence is limited to a single "pilot study". While compelling, a more extensive experimental section with a wider range of models and datasets, and a more detailed description of the methodologies would strengthen the argument.
2. Lack of a Proposed Solution: The paper outlines what should be done, such as creating new benchmarks and using better training data, but it does not provide a concrete example of a new model architecture or training method that successfully captures implicit semantics. The proposed solutions are high-level recommendations rather than a detailed technical proposal.

### Questions
1. You mention the performance gap between current models and the Bag-of-Tokens baseline on implicit semantics tasks. Could you provide more detailed insights into the experimental setup and dataset choices used for your pilot study? A deeper understanding of your methodology might help clarify why the performance gap exists and whether it could be addressed through model adjustments
2. Given the focus on implicit semantics, how do you envision overcoming the challenge of ensuring that new, linguistically grounded datasets reflect the complexity of real-world language while also being scalable for large-scale training?
3. While your paper advocates for more diverse training data, what are some specific data augmentation strategies or techniques you foresee as being effective in training models to capture implicit meaning, such as pragmatics, stance, and sociocultural context?

### Presentation
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This position paper argues that current text embedding models, despite strong performance on benchmarks like MTEB, primarily capture surface-level semantics such as lexical overlap, syntactic variation, and topical similarity, while failing to represent deeper implicit meaning shaped by pragmatics, speaker stance, and sociocultural context. 
Drawing from linguistic theory, the authors propose a three-tier framework for implicit meaning: (1) utterance-level pragmatic inference, (2) speaker-level stance-taking, and (3) society-level sociolinguistic signals. 
They present a pilot study using seven datasets across these tiers, showing that state-of-the-art embeddings perform only marginally better than a Bag-of-Tokens baseline, in contrast to their high scores on conventional benchmarks. 
The paper advocates for curating more linguistically and culturally diverse training data, designing benchmarks that explicitly target implicit semantics, and reframing implicit meaning as a core modeling objective for embedding research.

### Strengths
* The paper addresses a timely and arguably underexplored gap in embedding research: the limited ability of current models to capture implicit meaning.
* The strong theoretical grounding in pragmatics, stance-taking, and sociolinguistics, clearly integrated into the motivation.
* It presents a well-structured problem framing that distinguishes surface-level semantics from deeper, context-dependent meaning.
* The empirical pilot study spans multiple semantic tiers (utterance, speaker, society) and model families (encoder-only, LLM-based, multimodal, proprietary).
* The authors proposes actionable high-level directions for the community, including richer training data, targeted benchmarks, and reframing modeling goals.

### Weaknesses
* From my perspective, the identified gap is largely application-specific. For many general-purpose LLM uses, the surface-level semantics captured by current embeddings are often sufficient, making the proposed shift less universally necessary.
* Empirical study is small-scale, using repurposed datasets rather than introducing a dedicated benchmark for implicit meaning.
* No concrete methodological innovations; contributions are primarily conceptual and programmatic.
* The paper does not fully address annotation cost, bias risks, or validation challenges for generating implicit meaning data, especially when using LLMs.

### Questions
* How would you design implicit semantics benchmarks to ensure broad coverage without becoming overly task-specific?
* Should implicit semantics be a universal goal for all embedding models, or should it be pursued only for application domains where it is clearly beneficial?
* Can you provide concrete downstream examples where improved implicit meaning capture in embeddings leads to measurable performance gains over current approaches?

### Presentation
3
