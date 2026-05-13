# Adapters for Altering LLM Vocabularies: What Languages Benefit the Most?

- Decision: Accept
- Scores: 6, 8, 6, 5

## Abstract
Vocabulary adaptation, which integrates new vocabulary into pre-trained language models (LMs), enables expansion to new languages and mitigates token over-fragmentation.
However, existing approaches are limited by their reliance on heuristic or external embeddings.
We propose \adt{}, a novel method for vocabulary adaptation using adapter modules that are trained to learn the optimal linear combination of existing embeddings while keeping the model's weights fixed. \adt{} offers a flexible and scalable solution without requiring external resources or language constraints. 
Across 11 languages---with various scripts, resource availability, and fragmentation---we demonstrate that \adt{} outperforms the original Mistral model \citep{mistral7b} and other baselines across various multilingual tasks.
We find that Latin-script languages and highly fragmented languages benefit the most from vocabulary adaptation.
We further fine-tune the adapted model on the generative task of machine translation and find that vocabulary adaptation is still beneficial after fine-tuning and that \adt{} is the most effective method. Models at \href{https://huggingface.co/collections/h-j-han/vocadt-67084ac852855267504fd0c6}{\texttt{Huggingface Hub}}
}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper introduces VocADT, an adapter-based method for vocabulary adaptation in pre-trained language models. New embeddings for an expanded vocabulary are learned by placing adapter modules between the new vocabulary and the original language model embeddings, enabling the model to use new tokens without modifying its main weights. The weights of the adapter module are initialized by (i) copying original embeddings of overlapping tokens, (ii) averaging embeddings where partitioned tokens in the original vocabulary subset exist, and (iii) randomly initializing the rest. An auxiliary loss is introduced to keep the embeddings of overlapping tokens close to their original values, preserving established representations for these tokens in the language model. The robustness of VocADT's impact on LLM performance for downstream tasks is tested by fine-tuning all model parameters after vocabulary adaptation. Detailed results are provided, evaluating 11 languages across 3 language groups — Latin, Mixed, and Cyrillic. VocADT is compared with three baseline methods: ZeTT, FOCUS, and OFA. Results show that, across languages and tasks, VocADT outperforms the original LM (Mistral). Latin languages benefit most from vocabulary adaptation, with language grouping strategies playing a minor role. Additionally, the auxiliary loss improves performance for Mixed-group languages but not for Latin languages. Finally, following ALMA, the authors fine-tune the full model to evaluate MT performance, showing that VocADT improves performance compared to the original Mistral baseline.

### Strengths
1. The introduction of VocADT, an efficient, adapter-based approach to vocabulary adaptation without relying on external embeddings, is novel.
2. The comprehensive experimental evaluation covers a wide range of multilingual tasks and scripts across 11 languages. It compares the proposed method against three baselines to assess the benefits of vocabulary adaptation and the robustness of VocADT.
3. The paper is well-structured and clearly presented.
4. VocADT’s method for efficient adaptation without altering main model weights is well-motivated, especially for cross-lingual transfer and adaptation to low-resource languages.

### Weaknesses
1. Given that grouping Mixed-scripts and Cyrillic scripts had little impact on performance, it would have been more interesting to see if grouping all languages could have achieved identical results, demonstrating the language scalability of the method. The lack of this experiment leaves a gap in understanding the method's behavior across diverse language families and tokenization schemes. Specifically, it is unclear whether the observed performance is due to the specific grouping strategy or if the method is inherently robust to different language groupings, which is crucial for practical applications in multilingual settings.
2. The auxiliary loss, intended to retain original embeddings for overlapping tokens, lacks analysis across alpha values; further exploration in non-Latin languages might have improved performance. The current evaluation only considers a single non-zero alpha value (0.1), which may not be optimal for all languages or tasks. A more thorough analysis of the impact of different alpha values, especially in languages where the auxiliary loss did not improve performance, is needed to understand the trade-offs between preserving original embeddings and adapting to new vocabulary.
3. The paper evaluates the proposed method on Mistral alongside several baselines. However, including at least one additional candidate LM would have strengthened the results. The current evaluation is limited to a single base model, which makes it difficult to generalize the findings to other language models with different architectures or pre-training data. Testing the method on a different model would provide a more robust assessment of its effectiveness and applicability.

### Questions
1. Adaptation improves performance for fragmented Greek but less so for similarly fragmented Korean. Does this suggest vocabulary adaptation may not be effective for highly fragmented languages, and that other properties of Greek contribute to the improvements?
2. Was any ablation conducted comparing initialization methods (e.g., one-hot vs. multi-hot) for the adapter module and their impact on downstream task performance?
3. How effective would VocADT be for mixed-script or multilingual groups with shared vocabulary at different scales? Exploring grouping strategies in larger, mixed-language models could provide valuable insights into scalability for multilingual setups.

### Soundness
3

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
The authors propose a new vocabulary adaptation method that enables new words to be added to a pretrained LLM's vocabulary. The proposed approach uses adapters to learn embeddings for new words. The new embeddings are linear combinations of the existing embeddings. The approach is tested on 11 languages, showing that the best results are achieved for highly fragmented and Latin script based languages.

### Strengths
1. The methodology is clearly explained with reference to the prior work.
2. The experiment design of this paper is well-crafted and supports the claims of the paper.

### Weaknesses
1. The motivation behind restricting the new embedding to a linear combination of original embeddings has not been explained.
2. Since the approach requires some amount of training, the authors should report the computational cost of their approach compared to the baselines.
3. The results in Appendix B shows significant difference among performance gains of different languages. The authors should perform analysis to determine why this happens. Does the amount of new pretraining data used for vocabulary adaptation affect the results?

### Questions
1. Can you give an example where the case 3 mentioned in section 3.2 happen?

### Soundness
3

### Presentation
3

### Contribution
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
The article introduces VocADT, a method to conduct vocabulary adaptation with adapters. This method enables the training of new vocabularies while keeping all parameters of the original model fixed. Experimental results demonstrate that VocADT outperforms existing baselines. The study finds that languages with Latin scripts and those with severe fragmentation benefit the most from vocabulary adaptation. Additionally, the article validates that incorporating new languages through vocabulary adaptation improves performance in machine translation tasks.

### Strengths
1. The method proposed in this article allows for vocabulary adaptation by keeping the original model completely frozen and training only the adapter, which is highly efficient.

2. Experimental results demonstrate that the method presented in this paper can effectively improve the performance.

3. The article provides a detailed analysis of the MT task, offering a more accurate assessment of the model on cross-lingual tasks.

### Weaknesses
1. The article does not clearly explain or analyze the advantages of VocADT compared to heuristic-based methods and those relying on external embeddings or networks. This causes a disconnect between the claims about existing methods' shortcomings in the introduction and the proposed method. Specifically, the paper lacks a detailed comparison of how VocADT's learned embedding combinations outperform methods that rely on simple averaging or external resources for initializing new embeddings. The introduction mentions limitations of heuristic methods but does not provide concrete examples of scenarios where these methods fail, making it difficult to assess the true novelty of VocADT.

2. In VocADT, the initialization of embeddings and the use of auxiliary loss are very similar to existing work, raising concerns about the novelty of the paper. The paper does not sufficiently distinguish how the adapter-based approach fundamentally differs from existing methods that also use similar initialization techniques and auxiliary losses. The use of an adapter module, while a different mechanism, needs more justification in terms of its unique contribution beyond simply providing a different way to combine existing embeddings.

3. The design of the adapter in this paper assumes that the new embeddings are solely linear combinations of the old embeddings. This assumption could negatively impact performance. For example, languages with Latin scripts may perform better under this assumption, while languages with greater differences, such as Korean, might not fit this assumption effectively. The paper does not explore the potential limitations of this linear combination approach for languages with significantly different tokenization characteristics or semantic structures, and it does not provide any analysis of the potential impact of this limitation on the performance of the model across diverse languages.

### Questions
1. Can you further explain the limitations of heuristics-based methods and methods that rely on external embeddings? For example, what does it mean when the introduction states that "heuristics-based methods often lack adaptability"?

2. Is your proposed method, VocADT, effective for low-resource languages?

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
4

### Summary
This paper proposes a method to address the vocabulary adaptation problem in multilingual NLP, and investigates the impacts of language scripts after vocabulary adaptation. After experiments using Mistral-7b on 11 languages, they find that the method proposed achieves better or on par with the vanilla model and the baseline methods. And the Latin-script and severe fragmented languages by Mistral-7b tokenizer benefit the most after vocabulary adaptation.

### Strengths
The findings about the impact of language scripts are interesting, which are the Latin-script and severe fragmented languages by Mistral-7b tokenizer benefit the most after vocabulary adaptation.

### Weaknesses
- [addressed]**Lack of novelty**: The method proposed is an incremental work, which combines the heuristic methods like OFA in the initialization and language adapters like MAD-X. It incorporates additional parameters and computation for the adapter and 8.5B(3.5B+5B) multilingual corpora in adaptation. Moreover, the incorporated auxiliary loss is not effective in Figure 5. The improvement seems little other than the "en-el" when using this auxiliary loss ($\alpha=0.1$).

- **Missing details and additional experiments to support the findings**: only Mistral-7b is used in this work. It is better to conduct experiments on other base models like llama or gemma to improve the generalization of the findings. The detail settings for baseline methods are unknown in this paper.

- **Writing is not clear**: 
  1) Line 067: ";" --> "?"
  2) Figure 1:  "Vocab Adaptor" --> "Vocab Adapter"
  3) Line 148: "lightweight": I cannot agree with this for the additional parameters and computation from the adapter training.
  4) The Figure 3 is confusing and hard to follow: a) The y-axis of 3(a) left part are increase rate(%), thus the negative results are missing like "id-en", "belebele" on Indonesian? b). The mismatched legends for left and right part, which are "VocADT-multi(ours), ZETT-mono"(left) and "mono, multi, mistral"(right). These results will be better to report on Tables.

### Questions
1) The number of tokens to train baseline methods is unknown. Is it same with the VocADT?
2) It can be found that the language Korean also suffers from severe fragment in Figure 3, while the improvement on Korean is little. How to interpret this phenomenon?

### Soundness
2

### Presentation
2

### Contribution
3
