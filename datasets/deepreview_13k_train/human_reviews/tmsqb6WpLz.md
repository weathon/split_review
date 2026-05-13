# Dissecting learning and forgetting in language model finetuning

- Decision: Accept
- Scores: 5, 5, 5, 8

## Abstract
Finetuning language models on domain-specific corpus is a common approach to enhance their domain knowledge and capability. While improving performance on domain tasks, it often brings a side-effect of forgetting of the model's general abilities. In this study, we analyze the effects of finetuning on language models by dissecting its impacts on the modeling of topic, style, and factual knowledge in text. Our method uses instruction-following LLMs such as ChatGPT to auto-generate controlled-variable text examples which we use to probe the model. Our findings reveal that finetuning results in significant shifts in the language model's topic and style priors, while actual knowledge learning only contributes to a small fraction of the total probability change. Analysis shows that the adaptation of topic and style priors behave akin to learning simple features: they are learned rapidly and require little model capacity. They are also learned independently and primarily at the beginning of a text sequence. In contrast, factual knowledge is learned stably but slowly and requires significant model capacity to learn. The research offers insights and understanding into the finer dynamics of learning and forgetting in language models, and can potentially inform future research on improving domain adaptation and addressing the challenges of forgetting in continual learning of language models.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
- This paper presents a detailed analysis of the effects of fine-tuning of large language models on domain-specific downstream tasks/datasets.
- In doing so, authors break down the probability distribution of a text into its fundamental factors i.e., topic, style and factual knowledge, and study the effects of fine-tuning on the probability distribution over these three factors.
- It has been shown that in the early cycles of fine-tuning, the language model easily captures the topic and style information of the underlying text data thus introducing learning bias, which ultimately leads to an increase in the forgetting of the previous knowledge. However, the model is able to capture the factual knowledge in the later cycles of fine-tuning and also requires significant model capacity as compared to the model capacity required for capturing topic and style information.
- Extensive experimental evaluation asserts the claims made by authors and opens a new research direction in continual learning research.

### Strengths
- Quality
	- The motivation is well-founded and the claims are sound.
	- Experimental analysis is very detailed and explanatory.
- Clarity
	- Paper is clearly presented and easy to follow.

### Weaknesses
 - Quality
	- As the topic of a document can be determined by the factual knowledge it contains then it might be redundant to keep the topic as a relevant factor in the text generation process and only style and factual knowledge might suffice which then could directly align with the syntax and semantics of the underlying text respectively.
- Significance
	- This paper presents a detailed technical analysis of the fine-tuning process of a language model on domain-specific downstream tasks/datasets. However, the outcomes of the study conform with the expected outcomes of fine-tuning a model on domain-specific data and hence this paper misses to provide any significant gainful insight into the fine-tuning process due to the following reasons:
		- In the PubMed dataset, as academic style is present across all abstracts with different factual knowledge, it is expected that the model will readily adapt to the academic style first before capturing the diverse type of factual knowledge.
		- Just like in topic modeling, the topic of a document is a broad sentiment and can be easily determined using a set of keywords. So, it will be easy for the model to detect/understand the topic of a document before reading the whole document and capturing the factual knowledge inside it. Therefore, it is expected for the model to easily understand the topic and style factors before capturing the factual knowledge inside it.
	- I am keen to hear the response of the authors on this and hope that they can change my point of view.

### Questions
- The C4 dataset could possibly contain the documents written in the "academic" style although in a different domain. Similarly, the C4 dataset could also contain documents related to the biomedical domain although having different factual information. So, it is possible that the model is adapting fast to the academic style and biomedical domain topic because it has already seen them in the pretraining data, but the diverse factual information in the PubMed dataset is new for the model, and that is why model is possibly taking time to capture that knowledge. Have authors taken this into consideration in their analysis of the finetuning process?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper dissects the effect of fine-tuning on learning and forgetting of language style, topic, and factual knowledge. The authors use instruction-following LLMs to automatically construct corpus with controlled factors above. The authors performed extensive analysis across different LM types and summarized several empirical findings, among which they show topic and style priors are easy to learn but factual knowledge is not.

### Strengths
- The method how the analysis is performed is novel. Creating training and evaluation corpora with controlled differences (topics, style, factual knowledge) by prompting instruction following LLMs is interesting and inspiring.  
- The analysis is extensive and is performed under various configurations (like the choice of LM, size of the training corpora)
- The outcomes of analysis are interesting and relevant to future research that study lifelong learning of LMs.

### Weaknesses
 - Although other configurations are very extensive, the choice of training and evaluation corpora and exclusively original or variants of PubMed and C4. 
- The three text-generating factors (styles, topics, facts) may not always be clearly separable of extensive enough in every corpora. The authors discussed this limitation in their limitation section.
- Clarity issue: I feel the plots very hard to read because the captions are too generic and not self-contained. I suggest to briefly summarize the findings or implications in the captions.
- Clarity issue: some legends in plots such as Figure 4 are not explained in text (e.g. readers may be confused about "C4 -factuals" before they associate them with "C4-counterfactual" in Table 1)
- Though the authors pointed out the hardness of learning factual knowledge without learning style and topic bias, the authors' attempts failed to improve such performance at the end of Sec. 3. I suggest to provide some future directions about how the analysis will be beneficial the challenge of learning factual knowledge above.
- The authors focused on evaluation of LM loss throughout the paper. I think this is fine for style and topics, but factual knowledge, evaluating LM loss is not clean enough because only a few tokens in a sentence are related to facts. The authors could create cloze-style  or question answering evaluation sets that focus exclusively on generation of factual knowledge.
- There is a "side note" in page 7: "When capacity is limited, the topic ratio and factual ratio simultaneously reduce on Pubmed in Figure 6." I did not see topic ratio reduces in Figure 6. Is this information supposed to be told by Figure 6?

### Questions
- There is a "side note" in page 7: "When capacity is limited, the topic ratio and factual ratio simultaneously reduce on Pubmed in Figure 6." I did not see topic ratio reduces in Figure 6. Is this information supposed to be told by Figure 6?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper investigates the impact of finetuning language models on domain-specific texts and how it affects their general performance. The authors show that finetuning alters the model's preferences for topics and styles significantly, learning these features quickly and with minimal capacity. Factual knowledge, however, is acquired more slowly and requires greater capacity. The study's insights into language model learning dynamics could guide future enhancements in domain adaptation and help address the challenge of model forgetting during continuous learning.

In this study, the authors fine-tuned three models in increasing scales (GPT2-XL, LLaMa2 7B, and 13B) on PubMed abstracts with different scales of datasets up to 1M abstracts.

### Strengths
1. Investigating the changes language models undergo after finetuning continues to be a highly relevant and evolving area of study, despite prior coverage in academic literature.

2. The research offers key empirical insights into the differential impact of finetuning on language models, revealing a more pronounced effect on style and topic preferences compared to factual knowledge. These findings enhance our understanding of language model training dynamics and are instrumental in formulating more effective training methodologies.

3. The researchers conducted extensive experiments on three language models of considerable size, particularly from an academic perspective.

### Weaknesses
The assertion that each prediction by a language model can be broken down into components of writing style, topic, and factual knowledge requires further justification or explanation. The paper should present a stronger argument or provide additional evidence to substantiate this claim. The decomposition seems overly simplistic, potentially ignoring complex interactions between these factors and other latent variables that influence text generation. For instance, the model's understanding of syntax and semantics, which are crucial for coherent text, are not explicitly accounted for in this framework. Furthermore, the assumption that these three components are independent or can be easily disentangled is not rigorously defended. The paper needs to address how this decomposition handles cases where style, topic, and factual content are intertwined or mutually dependent, such as in creative writing or nuanced technical discourse.

The primary message or conclusion of the paper is ambiguous. The authors need to clarify the central thesis to ensure that readers can grasp the main contribution of the work. What is the takeaway from this research? The lack of a clear, concise statement of the main findings makes it difficult to assess the significance and novelty of the study. The paper should explicitly state the key insights gained from the experiments and their implications for the field. Without a well-defined conclusion, the reader is left to interpret the results, which can lead to different and potentially inaccurate understandings of the study's contributions.

While the prose is generally lucid, the paper's structure, particularly the introduction, could use refinement to enhance its readability and impact.

### Questions
* The basis of the method assumes that p(x)=p(topic,style,factual), but is there a justification to that decomposition? what about arithmetic? how does it fall to this decomposition?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper studies the effects of finetuning on an LM. The authors disentangle the effects of the finetuning along three “dimensions”: topic, style, and factual knowledge. To achieve that, they leverage ChatGPT to generate a series of texts that are only different in one of those facets. Provided such texts, one can estimate log-likelihood ratio of different styles (for instance), by calculating differences of cross-entropies of the model on the texts.
The generated texts were verified by human judgements. 

The experimental study is performed using two corpora (BioMed and C4) and three LMs (GPT-2 XL, LLaMa 2 - 7B & 13B). 

The paper reports the following findings: (a) topic and style changing rapidly,(b) topic and style biases are independent, (c) topic and style require minimal capacity to be learned, in contrast to knowledge, (d) mixing in unbiased data only reduces the biases to a certain degree.

### Strengths
* I find the topic of the investigation quite novel. I believe that the approach taken is original and innovative, in particular building a corpus that allows disentangling style/topic/factual knowledge. I also like the way LoRa was used to measure the capacity required for learning different facets.
* The authors are sharing the data and code.
* The reported experiments have provided some applicable insights, e.g. wrt the data mixing.

### Weaknesses
 * Using synthetic data, generated by ChatGPT, might introduce some hidden biases. It is not given that the same findings could be found if we had natural data. Specifically, the controlled nature of the generated text might not fully capture the nuances and complexities present in naturally occurring text, potentially skewing the observed effects of finetuning. For instance, the stylistic variations introduced by ChatGPT might be more artificial and less diverse than those found in real-world writing, leading to an oversimplified view of style learning.
* It is not clear if the same approach can be generalized to any other characteristics? The paper focuses on topic, style, and factual knowledge, but it remains uncertain whether the methodology can be applied to other text characteristics such as sentiment, formality, or even more fine-grained linguistic features. The assumption that these characteristics can be independently manipulated and measured using the proposed log-likelihood ratio approach requires further validation. For example, can the same disentanglement be achieved for characteristics that are more intertwined, such as sentiment and style?

Typos:
* “by just changing the order of decomposition in 1” -> “...in Eq. 1”

### Questions
* I wonder if there are other factorizations which can be studied in the same setup, apart from style/topic/knowldge?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
