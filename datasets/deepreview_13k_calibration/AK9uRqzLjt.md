# $\texttt{LLaPA}$: Harnessing Language Models for Protein Enzyme Function

- Decision: Reject
- Avg Score: 4.75
- Scores: 6, 5, 5, 3

## Abstract
Identifying protein enzyme functions, crucial for numerous applications, is challenging due to the rapid growth in protein sequences. Current methods either struggle with false positives or fail to generalize to lesser-known proteins and those with uncharacterized functions. To tackle these challenges, we propose $\texttt{LLaPA}$: a Protein-centric $\underline{L}$arge $\underline{L}$anguage and $\underline{P}$rotein $\underline{A}$ssistant for Enzyme Commission (EC) number prediction. $\texttt{LLaPA}$ uses a large multi-modal model to accurately predict EC numbers by reformulating the EC number format within the LLM self-regression framework. We introduce a dual-level protein-centric retrieval: the $\textit{protein-level}$ retrieves protein sequences with similar regions, and the $\textit{chemical-level}$ retrieves corresponding molecules with relevant reaction information. By inputting the original protein along with the retrieved protein and molecule into the LLM, $\texttt{LLaPA}$ achieves improved prediction accuracy, with enhanced generalizability to lesser-known proteins. Evaluations on three public benchmarks show accuracy improvements of $\textbf{17.03\\%}$, $\textbf{9.32\\%}$, and $\textbf{38.64\\%}$. These results highlight $\texttt{LLaPA}$'s ability to generalize to novel protein sequences and functionalities. Codes are provided in the supplement.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a method called LLaPA, a protein-centric large language model designed to identify protein enzyme functions by predicting EC numbers. It employs a multi-modal approach, reformulating the EC number format within a self-regression framework.

### Strengths
To enhance prediction accuracy, LLaPA introduces a novel encoding scheme that replaces the radix point with a Latin letter. Additionally, LLaPA incorporates a two-tiered retrieval engine: (1) at the protein level, it retrieves proteins with similar regions to predict the "First Three EC Numbers"; (2) at the chemical level, it identifies corresponding molecules for the "Full" EC Numbers.

### Weaknesses
1. More literature is required. The GearNet and ESM-GearNet are state-of-the-art methods for predicting EC number. GearNet is a geometric pretraining method to learn the protein structure encoder based on the contrastive learning framework. ESM-GearNet learn the joint representation learning on protein sequences and structures. These two methods both employed the structure information, different with the baseline methods in this paper. Although the authors argued that only 6.66% of protein sequences in their training dataset possess corresponding 3D structure, the corresponding 3D structures are easy to achieve by Alphafold2. The authors should introduce GearNet and ESM-GearNet as baseline methods.
2. This paper does not provide sufficient details about the Protein Prior Knowledge Module and the Chemical Reaction Prior Knowledge Module, merely mentioning them without further explanation. To make this clear, a figure or pipline is needed to illustrate what prior knowledge is retrieved and how these modules integrate with the rest of the system.
3. The connection between the multi-modal protein and chemical modules is unclear, as it appears that the models are designed for different targets. It is better to provide a specific example or diagram to show how these modules interact, or how the different targets are reconciled in the final prediction.
4. The architecture of the main LLaPA model should be described in more detail to clarify the flow of data through the model and how different parts of the model are trained.

### Questions
Can you feed the protein structure information into a language model?

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
The paper presents LLaPA, a LLM framework designed to enhance the prediction of protein function. LLaPA features a dual-level protein-centric retrieval system that retrieves similar protein sequences and relevant molecules, thereby improving EC number prediction. The framework's performance is evaluated on three public benchmarks, demonstrating improvements over existing methods.

### Strengths
1. The paper identifies a valid limitation in the prediction of EC numbers by LLMs due to their specific format and proposes a novel solution. 
2. The authors effectively demonstrate that the reformulation of EC numbers leads to improved feature quality in Section 4.3, enhancing the model's generalizability and reliability.
3. The framework shows significant performance improvements over existing methods on public benchmarks.

### Weaknesses
1. The results indicate a substantial increase in performance due to the dual-layer retrieval engine, but it is unclear how how does performance change when each layer is used separately or in combination? The paper notes that improvements are most significant in the Halogenase and Multi datasets, suggesting that additional data is particularly beneficial for less familiar proteins. How does the retrieval mechanism adapt to different types of proteins, especially those with rare EC numbers or those that are evolutionarily distant from the proteins in the training set?
2. The paper states that information about molecules is crucial for predicting "Full EC Numbers," while protein information is key for "First Three EC Numbers" predictions. A deeper analysis is needed to understand the mechanistic reasons behind this observation. How do molecules and proteins contribute differently to the prediction of full versus partial EC numbers? The comparison with "LLaPA without SMILES" and "LLaPA without protein" variations is insightful. However, the paper should provide a more detailed analysis of the role of SMILES in the context of the model. How does SMILES information integrate with the protein data to enhance predictions?
3. The paper does not provide sufficient evidence that the predicted EC numbers are indeed more accurate due to the proposed method rather than other factors.

### Questions
1. The author mentioned that replacing the “.” character improved prediction results, how do you establish a correlation between the proximity of the “.” character to numbers in the embedding space and the difficulty in predicting EC numbers? Is the improvement observed with the replacement of “.” with “A” and “Z” applicable to all types of protein sequences, or are there specific conditions under which it works better? Does this character replacement provide any insights into how the model understands or processes the EC number prediction task?
2. The improvements in F-1 scores are indeed impressive; however, it is crucial to understand whether these improvements are statistically significant. The paper should provide p-values or confidence intervals to substantiate the claim that the observed improvements are not due to chance but are a result of the model's inherent superiority.
3. Could the significant discrepancy between Acc-1 and Acc-2 within the Multi dataset potentially reflect biases or a lack of representativeness in the dataset itself, rather than just limitations of the LLaPA model? Besides Acc-1 and Acc-2, are there other metrics or methods that could be used to assess the model's generalization capabilities when dealing with enzymes associated with rare EC numbers? Besides collecting more data, has the author explored other methods to reduce the discrepancy between Acc-1 and Acc-2?

### Soundness
2

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
3

### Summary
This paper introduces LLAPA, a retrieval-augmented multimodal language model designed to facilitate enzyme EC number prediction. LLAPA retrieves similar protein sequences and related molecular sequences as additional features, augmenting the original protein sequence, and applies a multimodal training approach akin to those used in vision-language models (VLMs). The comprehensive results and analyses presented are good.

### Strengths
1. The observation that large language models (LLMs) struggle with predicting numbers and decimal points is intriguing, and the authors propose an innovative solution by examining the embedding space of each character. I find this approach very inspiring.

2. Retrieving similar proteins and molecules to support the classification task is generally a strong idea.

3. The experimental results are solid, and the analysis of each part in the model is comprehensive.

### Weaknesses
1. Using related proteins and molecules as additional information for classification tasks is generally a good idea. However, I am concerned about potential data leakage between the retrieval database and test set, which could significantly contribute to the improved performance.

2. LLAPA appears to adopt popular multimodal understanding frameworks (e.g., LLaVa) for EC number prediction tasks. However, I am somewhat unclear on the motivation for using pretrained large language models in this context. It seems feasible to use the retrieved and encoded embeddings as additional features to train a classifier directly, rather than framing the classification task as a dialogue task. Since there doesn’t appear to be any multi-turn or other natural language elements, LLAPA doesn’t seem to function as a protein assistant (e.g., providing enzyme function explanations or reasoning details).

3. Some parts of the presentation, particularly the model details, are unclear.

### Questions
1. Please provide more details on LLAPA. For example, how are the MMseqs2 hyperparameters set? How many sequences and molecules do you retrieve, and what is the computational cost for training and inference? These details would enhance our understanding.

2. I would like clarification on the training and inference procedures. In lines 324–328, is the curated dataset used as a training set or solely for MMseqs2 retrieval? How do you prevent data leakage between the MMseqs2-retrieved sequences and the test set? Additional explanation on training and inference would improve clarity.

3. Data leakage could also arise in the molecular retrieval process, as LLAPA uses prior protein knowledge bases and UniProtKB annotations; test set sequences may already appear in these databases. Please add clarifications on this point.

4. The motivation behind using pretrained LLMs and a multimodal training scheme is somewhat unclear. I encourage the addition of baseline comparisons, such as ESM2 + retrieval or the original Vicuna-7b, to illustrate the advantages of pretrained LLMs. It also feels unconventional to frame a classification task as a dialogue. Why not use a linear probe for classification?

5. Some minor typos need correction. For example, in Figure 4, “one of generated…” should be labeled as “<molecule>” rather than “<protein>.”

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper proposes LLM for EC number prediction, namely LLaPA. Other than feeding enzyme and reaction embeddings into some neural networks (such as MLP or CLIP networks), LLaPA projects enzyme and reaction embeddings into language tokens using two projectors, then uses a fine-tuned LLM to predict/retrieval EC numbers.

### Strengths
1. Results are really strong.
2. As a protein engineer, having an interactive LLaPA for EC prediction would be great.

### Weaknesses
1. Line125-126, typo 'two-tired' -> 'two-tiered'.
2. No codes? Access to the model? (I'd consider to change my score if authors provide the model access/codes)
3. Line 243-246, 'We emphasize that the retrieve logic in the inference phase is reasonable, as proteins with high sequence identify cutoff values typically exhibit similar enzyme functions. Therefore, their molecules in the corresponding chemical enzyme reactions should possess similar catalytic information'. It is a strong statement, you'd better have citations to support you statement.
4. Paper is not easy to follow, too many third-level titles, feel a bit unorganized.
5. As a researcher working on AI for computational biology, I have to say this paper is not novel. Even though the results are really strong (as they claimed), but I dont find the overall approach exciting. Basically, the authors fine-tuned LLMs with new protein-function prompting and trained two language token projectors. LLMs are powerful, but only fine-tuning them for down-streamed tasks lacks novelty and excitement for AI in computational biology.

### Questions
Major: No codes? Access to the model? (I'd consider to change my score if authors provide the model access/codes)

### Soundness
3

### Presentation
2

### Contribution
2
