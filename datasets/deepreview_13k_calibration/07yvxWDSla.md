# Synthetic continued pretraining

- Decision: Accept
- Avg Score: 8.00
- Scores: 8, 8, 8, 8

## Abstract
Pretraining on large-scale, unstructured internet text enables language models to acquire a significant amount of world knowledge.
However, this knowledge acquisition is \emph{data-inefficient}---to learn a given fact, models must be trained on hundreds to thousands of diverse representations of it.
This poses a challenge when adapting a pretrained model to a small corpus of domain-specific documents, where each fact may appear rarely or only once.
We propose to bridge this gap with \emph{synthetic continued pretraining}: using the small domain-specific corpus to synthesize a large corpus more amenable to learning, and then performing continued pretraining on the synthesized corpus.
We instantiate this proposal with EntiGraph, a synthetic data augmentation algorithm that extracts salient entities from the source documents and then generates diverse text by drawing connections between the sampled entities.
Synthetic continued pretraining with EntiGraph enables a language model to answer questions and follow generic instructions related to the source documents without access to them.
If, instead, the source documents are available at inference time, we show that the knowledge acquired through our approach compounds with retrieval-augmented generation.
To better understand these results, we build a simple mathematical model of EntiGraph, and show how synthetic data augmentation can ``rearrange'' knowledge to enable more data-efficient learning.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper addresses the problem of data inefficiency in pretraining language models. Current pretraining corpora may not generalize effectively and models may benefit from structured, repeated, diverse representations of knowledge. 

The proposed is a two-step process that (1) extracts entities from the corpus and then (2) extracts relationship information amongst a subset of the entities.

Experimentation uses the QuALITY corpus and dataset, which is a benchmark for long-document reading comprehension. Evaluation compares with relevant baselines like training on the original QuALITY corpus and a corpus containing rephrasings.

### Strengths
* The problem the work addresses is important.
* Experimental results show that this method scales better than simple paraphrasing or direct pretraining, and that retrieval-augmented generation further boosts performance of this model. 
* The authors also present a theoretical model explaining EntiGraph’s log-linear scaling pattern, providing insights into the mechanics of synthetic data’s impact on learning efficiency.
* Paper is clear and well-written.

### Weaknesses
While the experiments focus on the QuALITY corpus, it remains unclear how well this would apply to other domain-specific corpora or more complex fields (e.g., legal or math data).

### Questions
It says “We generate data for pairs D_{Ei, Ej} and triplets D_{Ei, Ej, Ek} in our experiments”. I wonder if the authors have any intuition about how performance changes with the size of subset k.

### Soundness
4

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
3

### Summary
This paper proposes a method to continue pretraining LLM with a synthetic data augmentation method. The method is based on expanding the training corpus with many verbalizations of the entity graph present in the training corpus. It moves from a sparsely verbalized entity graph to a more densily verbalized one by using only the source documents and prompting LLMs to generate the new tokens.

The paper shows that the method is beneficial for downstream tasks in closed- and open-book QA as well as RAG. 

Overall, I think the paper is worthy of acceptance, it propose a clean method with good results and the experiments are fairly convincing.

### Strengths
The paper does a good job at demonstrating the benefit of the synthetically generated data, by including relevant natural baselines. 
The proposed method seem to work well and can be useful for continued pre-training tasks.

### Weaknesses
The work relies on commercial and closed-source models (GPT4) for generating the synthetic data, making this work non-reproducible. Since the data generation process is the central contribution, it would have been interesting to have insights about how well different models can perform this data generation task. Specifically, the paper lacks an ablation study on the impact of the generation model's capabilities on the quality of the synthetic data and the downstream task performance. This is a critical omission given the reliance on a powerful, but inaccessible, model like GPT-4. The paper proposes only extrinsic evaluation of the generated data but does not provide intrinsic measures, i.e., how good is the generated text? For example, metrics such as perplexity, BLEU score against a reference corpus (if available), or even human evaluation of the generated text's fluency and factuality would be beneficial. Without these, it's difficult to assess the quality of the generated data independently of its impact on downstream tasks. In my opinion, section 6 is not particularly useful. It is unnecessarily mathematical, based on simplistic assumptions and does not bring useful insights (For many continuously increasing lines, there anyway exists a mixture-of-exponential that fit it)

### Questions
For the data generator, what type of models are necessary to have good performance? (why use GPT4 and not open-source models)
The paper shows that the generated data is useful, but how does it look like? (is it good quality text, factual, natural looking, ...) 
What is the significance of section 6?

### Soundness
4

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
The paper proposes "synthetic continued pretraining" to enhance language models' domain adaptation efficiency, particularly when adapting to a small corpus of domain-specific documents. The authors introduce EntiGraph, a synthetic data augmentation algorithm that constructs a knowledge graph from the entities in the original corpus and synthesizes diverse text to enhance the pretraining process. The approach was evaluated using a reading comprehension dataset, QuALITY, showing notable improvements in model performance with both closed-book and open-book scenarios.

### Strengths
1. The proposed EntiGraph approach for generating synthetic data is well-motivated and demonstrates clear improvements in downstream performance, as shown by the experimental results.
2. The paper includes comprehensive evaluations, including closed-book QA, instruction following, and open-book settings. The results show a significant performance improvement over baselines, validating the effectiveness of synthetic pretraining.
3. The authors provide a theoretical analysis of EntiGraph's effectiveness, which aligns well with empirical observations and provides a deeper understanding of its scaling properties.

### Weaknesses
1. The evaluation relies on the QuALITY dataset, which may not be representative of all types of small corpora. A broader range of datasets, particularly from diverse domains, would make the results more generalizable. The current evaluation lacks a systematic exploration of how the method performs across different text types, such as technical reports, legal documents, or creative writing, which could exhibit varying entity densities and relational structures, potentially impacting the effectiveness of EntiGraph.

2. Although the authors attempt to mitigate hallucinations by grounding synthetic data generation in the original corpus, the risk of generating inaccurate information is inherent in using a language model for synthetic generation. This aspect needs further empirical examination, such as quantitative metrics to evaluate hallucination rates. The paper should include a more detailed analysis of the types of errors introduced during the synthetic data generation process, for example, by categorizing errors as factual inaccuracies, logical inconsistencies, or semantic drift from the original text.

3. The approach relies on using strong language models like GPT-4 for synthetic data generation. The practical feasibility of using this approach might be limited if users do not have access to such models due to their computational cost. The paper does not explore the sensitivity of the method to the quality of the language model used for synthetic data generation, and it would be beneficial to see how performance degrades when using smaller or less capable models.

4. While the paper includes useful baselines such as "Rephrase CPT," more comparisons with alternative data augmentation or synthetic generation methods from recent literature could strengthen the claim that EntiGraph is an effective strategy. The paper should compare against methods that use back-translation, paraphrasing, or other techniques for generating synthetic data, and also explore methods that focus on improving the quality of the synthetic data by using techniques like adversarial training or reinforcement learning.

### Questions
1. How sensitive is the synthetic pretraining process to the specific hyperparameters used for entity extraction and relation analysis? Would tuning these parameters significantly affect the generated corpus quality?

2. How does the synthetic corpus compare to a manually curated dataset in terms of quality and impact on downstream tasks?

3. Could EntiGraph be used effectively in scenarios where entities are ambiguous or domain-specific (e.g., medical or legal texts)?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper addresses how to train LLMs in a data scarce regime, given that LLMs require O(1000) examples of a fact to actually "learn" it. This has applications both to niche corpora (e.g., mathematics textbooks) as well as to training larger models once all human text is exhausted. The authors propose to use a pre-trained LLM to (1) extract entities and summaries from a comparatively small, niche corpus, and (2) use the extracted entities to generate rephrased assertions about those entities, to facilitate learning by a second (here, smaller) LLM. They experiment with a 1.3M token reading comprehension dataset, and test the approach against several baselines, including closed-book tests on the LLM used to extract entities and the rephrased text used to train the second LLM. Finally, the authors present a mathematical model through which they attempt to understand the training behavior of this data augmentation system.

### Strengths
The experiments are convincing that the EntiGraph approach improves the LLM's ability to accurately answer questions about a small corpus. In particular the closed-book results in Figure 3 show that the EntiGraph approach leads to far more salient claims per false claim than any of the other models, including GPT-4, or training the LLM (Llama 3 8B). The benefit is substantially less in the open-book RAG case, but there is still substantial improvement. The theoretical model to explain how the model improves QA accuracy with increasing tokens provides some good intuition as to how the model learns. 

Overall the text is clear and easy to read.

### Weaknesses
I still have reservations that there is some amount of distillation of GPT-4 into their Llama 3 8B: it seems possible to me that a RAG-prompted GPT4 could generate additional information that is somehow "unlocked" by the RAG prompt, but which the closed-book version was unable to access. At the risk of anthropomorphizing, this is akin to a human getting a visual or audio cue and suddenly recalling whole complex memories. It would make the paper stronger to dig into the results of entity extraction and the generated text to see whether it is rephrasing/paraphrasing, or whether possibly actual new information is injected.

Even so, it would have helped this reader to have pointed out the significance of the closed book experiments earlier on. It isn't stated explicitly until the Limitations section.

I don't feel particularly qualified to check your proofs of theorems, and moreover I think the main value of the theoretical model is to help the reader understand intuitively why the approach works (these may be connected observations). Is all of the theory necessary? Perhaps a simulation would do as well?

Another issue is that much of the benefit of the approach vanishes (though not completely) when using a RAG model directly. Is this approach worth the extra training, given the modest gains? The core problem, really, is how many examples LLMs take to learn anything well. This paper finds a way to side-step that successfully, but doesn't solve it directly.

### Questions
The paper could be more robust if you had more than just the QuALITY dataset. It is a perennial problem to find hard datasets to work with, so I understand this may be all there is for now, but given the chance I would attempt to reproduce the results on a different set. The authors mention linear algebra (a much harder topic, I think): is there any corpus for that subject?

The presentation of how exactly you generate the text to train Llama 3 8B with EntiGraph is still a little fuzzy to me, in particular it would be nice to see some examples of what you generated. It is helpful to have the prompts, but some output always grounds the presentation. 

Finally, I imagine GPT-4t made errors in producing the training data--did you search for these? Even at a quick glance how often did it make errors, and what, if anything, did you do to filter them out?

### Soundness
4

### Presentation
3

### Contribution
3
