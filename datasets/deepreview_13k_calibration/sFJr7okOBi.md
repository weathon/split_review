# NL2ProGPT: Taming Large Language Model for Conversational Protein Design

- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 5, 5, 3

## Abstract
Large Language Models (LLMs), like ChatGPT, excel in cross-modal tasks thanks to their powerful abilities in natural language comprehension, generalization, and reasoning. Meanwhile, the wealth of human-curated protein knowledge in text form presents a unique opportunity for LLMs to contribute to advanced protein design. In this work, we propose a new LLMs-based framework, namely NL2ProGPT, for macromolecular protein sequence generation that bridges the domain gap between natural and protein languages. Specifically, we first combine the protein functions and properties to create specific text guidelines for designing the protein, ensuring it follows precise controls. Second, to form a more informative and generalizable protein description, we explicitly inject protein structural information by clustering the embeddings from pre-trained protein language models. Third, we train a reward model to align the protein language model with the Rosetta energy function, following an RLAIF (reinforced learning from AI feedback) fashion. We empirically verify the effectiveness of NL2ProGPT from three aspects: (1) outperforms existing protein sequence design methods in different evaluations; (2) exhibits more than 90\% consistency in text-to-protein generation; (3) has effective exploration potential in disordered regions.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes to train a joint model on both the protein and text modalities (optionally with RL with some rewards around generality and consistency). The model is then used to generate proteins, sometimes with textual constraints that are key to the authors' approach.

The models are evaluated with respect to several related works on both the generality and consistency dimensions.

### Strengths
I think the idea of building joint protein text representations for controllable protein generation is important and has a lot of promise.

### Weaknesses
-Overall I have some questions about the paper below that I feel are critical to my understanding both to understand the method and make sure the evaluation is fair. 

(1) I don't quite understand how ChatGPT is used to generate the text descriptions. It says something like:

"We then feedthese constructed templates into ChatGPT OpenAI (2023) to obtain diverse protein text descriptions
by using several prompts. These descriptions constitute the training dataset for text-protein pairs,
serving as a foundation for further research and analysis."

In Section 4.1 it also says:
"Our training dataset comprise 1,001,890 text-protein sequence pairs in total."

Are these training examples from the above process with ChatGPT? If so, how did you do any verification on the quality of this dataset? The description of the process is vague, and it's unclear how much human oversight was involved in curating the text descriptions. The reliance on ChatGPT for generating a large portion of the training data raises concerns about potential biases or inaccuracies in the text descriptions, which could negatively impact the model's performance and generalization capabilities. It is not clear if the authors performed any filtering or validation on the generated text to ensure it accurately reflects the corresponding protein sequences.

(2) Given that some of them models use text as inputs like the authors' approach and some do not e.g. Progen I am a bit confused as to how all the models are compared e.g. is each model fed a different input and what are these inputs? It's unclear if the models are being compared under equivalent conditions. Specifically, for models that do not take text as input, are they generating protein sequences without any constraints, and if so, is this a fair comparison to models that are explicitly conditioned on text? The paper needs to clarify the specific inputs provided to each model during the evaluation phase to ensure a fair comparison.

(3) When evaluating for generality and consistency are the metrics used the same as that were used for RL? (in which case it would be unfair since the model would be overfitting on the reward). Some clarification would be great. If the evaluation metrics are the same as the reward function used during RL training, it raises serious concerns about overfitting. The model might be optimizing for the specific metrics used as rewards, rather than learning a generalizable representation of protein sequences. This could lead to inflated performance on these metrics, while not necessarily indicating a better model overall. It is important to use distinct evaluation metrics that were not part of the RL training process to assess the true generalization capability of the model.

### Questions
See questions above.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work studies the problem of protein design with large language models (LLMs), where the input to their model is a natural description of protein features that contain both functional and structural information via preprocessing with existing MSA tools and pre-trained protein language model (e.g., ESM2). The framework — NL2ProGPT also consists of two steps of self-supervised fine-tuning on GPT2 and reinforcement learning from AI feedback (with protein-based and cluster-based rewards) to improve the model's prediction.
They evaluate the quality of proteins generated by the proposed framework and show relatively good performance on closeness to the real-data distribution and high consistency. The authors also provide interesting findings on exploring disordered regions and case studies to understand cluster representations further.

### Strengths
1. The problem of protein design is important. With the rapid growth of LLMs, utilizing LLMs for protein design is a timely and interesting problem.
2. The design of the NL2ProGPT framework seems to be novel in terms of integrating existing techniques used for LLMs with natural languages and techniques specified for protein learning.
3. As measuring the generation of protein is still open research, the paper makes a good effort in quality evaluation and shows a good performance of the proposed method.
4. I appreciate the effort of the authors in providing the case study

### Weaknesses
 - Correctness/Soundness of the framework:
    - Evaluation: the method seems to use the same model in the framework for evaluation. For instance, they use ESM2 to embed the structure with reward constraints to an ESM-based cluster and use ESMFold (built on ESM2) for structure prediction evaluation. Also, they use the consistency (with Rosetta) reward in Step 3 to constrain the model and evaluation. This may raise the question of model performance benefits from the inductive bias of these pretrained models and tools. Specifically, the use of ESM2 embeddings for both clustering and as input to ESMFold for structure prediction creates a potential circularity in the evaluation. The structural information used to guide the generation is also used to assess the quality of the generated structures, which could inflate the reported performance. The Rosetta consistency reward, while a valid metric, further biases the model towards solutions that are consistent with Rosetta's scoring function, potentially limiting the exploration of novel protein structures.
    - The paper claims to embed the structural information into the description, but it’s doubtful how much the structure is preserved. First, though the ESM2 paper claims their embeddings have structural information, it is still implicit. Second, though the case study shows some insight into the cluster representation, it’s unclear how much information UMAP (into 2-D) and k-mean can preserve, as we know the loss of information after the dimension reduction and the difficulty of clustering. The reduction of high-dimensional ESM2 embeddings to 2D via UMAP, followed by k-means clustering, inevitably leads to information loss. This raises concerns about whether the clusters accurately represent the underlying structural diversity and if the model is truly learning to generate proteins with specific structural features or merely fitting to the artifacts of the clustering process. The implicit nature of structural information within ESM2 embeddings further compounds this issue, making it difficult to ascertain the extent to which the model is genuinely incorporating structural constraints.
- Results:
    - In Figure 2, it doesn’t seem the proposed method achieves the best performance in any measure. For instance, a similar approach — ESM2-MR model is closer to the GT and performs better in the first one. The fact that ESM2-MR, a method that reconstructs masked sequences, outperforms the proposed method in some metrics raises questions about the effectiveness of the proposed approach in de novo protein design. The performance gap suggests that the model may not be fully leveraging the natural language input to guide protein generation effectively.
    - As NL2ProGPT is not the first approach combining natural language and protein (e.g., ProteinDT [1], ProGen family [2]), this raises the question of motivation in which scenario the proposed method is necessary. The paper needs to clearly articulate the specific advantages of NL2ProGPT over existing methods like ProteinDT [1] and the ProGen family [2], which also combine natural language and protein sequence generation. Without a clear justification for its necessity, the contribution of the proposed method is diminished.
- Novelty/Originality: while I appreciate the novelty in integration methods for protein design, each framework component seems to be incremental in the design for protein learning.
- Writing or Presentation: Overall, the paper is easy to follow, but the presentation is not at the quality of the top conference and should be improved.
    - Typos: there are a few typos, such as missing space right before the citation on page 1 (ProGEn-2Nij), (ref2015Park), page 6 (-2(base)), …. These typos somewhat indicate that the paper was not properly proofread.
    - I can not find the appendix or detailed description of the model, settings, and template. It should be more useful for understanding to provide the sample template.
    - (Optional) The writing should be improved to be more concise. Some sentences and claims are  vague and less precise, e.g., “This training process helps us understand the distribution of combined sequences.”  or “Overall, our generated protein sequences may have a higher success rate when performing wet experiments.” Furthermore, the notations, e.g. aw can also be improved for consistency.
    - I didn’t find the description/definition of the TM score in the paper.
    - Minor: For Figure 1, step 1, the figure of ChatGPT seems to be a cropped version of the ChatGPT official icon without modification.

### Questions
Together with previous questions, I have some clarification questions:

1. For structure embedding, have you considered other methods, such as explicitly embedding structure from AlphaFold generation, which some recent papers use?
2. For step 1, how do you improve the diversity with ChatGPT? Do you also input the protein sequence to ChatGPT?
3. For step 2, what are the input and output? From the figure, it seems like a pretraining step with self-supervision (next-token prediction). Still, the description in the paper says it’s p(a|w), meaning predicting amino acids from the description. Can you elaborate on this step?
4. For step 2, what is the initial state of GPT2? Which checkpoint is that? 
5. For step 4, how do you control the diversity of generated sequences given an input protein?
6. How well do they cluster in 2-d of UMAP?
7. Terminology: why do you call it conversational protein design? It may be confusing to the dialog or conversation-based LLM.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a new LLMs-based framework “NL2ProGPT” for macromolecular protein sequence generation that bridges the domain gap between natural and protein languages. The authors train a reward model to align the protein laguage model with the Rosetta energy function, following an RLAIF fashion, and empirically verify the effectiveness of NL2ProGPT.

### Strengths
The authors have provided detailed explanations of their proposed methods and presented promising results.

### Weaknesses
The authors claim that:

“most existing methods mainly utilize protein sequential or structural information to model the intrinsic properties of protein, lacking the kind of controllable generation in a conversational way like LLMs.” 

It is unclear what advantages can be brought by “generation in a conversational way.”

### Questions
Misc: 

The citations should be enclosed by parentheses, such as using the“\citep{}” command instead of “\cite{}”.

Typo in Table 1: “OntoProtien”, “NL2ProGTP”

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper trains a P(protein sequence | metadata) model, where metadata encompasses both natural language descriptions of target attributes of the protein and some control tags for structural features based on clustering structures of natural proteins. There are some interesting modeling ideas, such as fine-tuning GPT-2 and using an RL objective to reward sequences with low Rosetta energy. Samples from the model are evaluated using various sanity checks using protein structure prediction models, etc.

### Strengths
The paper draws on a number of modeling techniques that are popular in the modern toolbox: RLAIF, fine-tuning foundation models, using protein structure prediction tools to provide eval metrics that are cheaper than wet-lab experiments.

### Weaknesses
The paper's title/abstract/intro/conclusion have lots of language about the promise of a  'conversational' natural language interface for designing proteins. However, the paper does not explore such text descriptions. It just uses a simple text rendering for converting protein database entries obeying a certain schema into text. For example, "Provides a protein that contains {domain description}, belongs to {family}, {ESM class} and {ONTO class}.<p>{protein sequence}" (Fig 1). There are significant resources available for true natural language descriptions of proteins. For example, Uniprot entires have one-line name fields and also longer description fields. Further, there are lookup tables available that map GO terms, EC numbers, Pfam families, etc to free text descriptions.

Similarly, the paper seems to over-state the novelty of structured-guided design with language models. The paper says "…none of them enables the sequence generation given target structures due to the lack of structural constraints." This ignores the significant body of work using RFDiffusion+ProteinMPNN. Further, the paper's claim that it is doing structure-guided design is quite weak: they take embeddings from an ESMFold model (which presumably encode some structure information), map them down to 2 (!!) dimensions, and then cluster these. Conditioning on a cluster id is the only way that structural information is provided. The confirmation that the generated sequences have desired structures in Table 2 is quite simplistic and anecdotal.

I found the RLAIF setup quite confusing. How does it make sense to use Rosetta energy as an absolute reward function? Doesn't this need to be relative to proteins having a similar fold, similar length, etc?

The paper fine-tunes GPT-2 (which was not pretrained on protein sequences) on only 1M examples of proteins. It's unclear why this generative model was used. Why not train something from scratch, or why not train on more proteins? No ablations about the impact of using GPT-2 pretraining are provided.

### Questions
I found it very surprising that no recent papers from the Baker lab were cited (RFDiffusion, ProteinMPNN, etc) were cited. These are really important contributions to the field and highly related to your paper. Can you please comment on these?

I am extremely confused about why you did k-means on the 2-dimensional UMap representations. Can you provide more background about why this approach is more 'intuitive and reliable'? 

I don't understand how the rosetta energy function was used as a reward, since the energy needs to somehow be normalized by the energy of ground truth proteins with the desired attributes. You say, "Generally, protein structures with lower scores are more likely to be closer to the native structure." What is 'native structure' and how is it used?

The rewards in eqs (9) and (10) have an optimum when the model just generates cluster centers, which will severely hurt diversity. When presenting your various eval metrics, I'm curious what would have happened if you had considered a simple baseline approach that just memorized a few exemplars.

I don't understand the overall evaluation setup. What does 'We randomly generate 1000 protein sequences from these models'. What metadata did you condition on? Was it 1000 different sets of metadata? How do you make this comparison fair when using models like ESM that don't have the ability to condition on metadata?

The "Protein credibility prediction" paragraph should mention that progen also confirms  wet-lab experiments.

The citation format is incorrect. It appears that there are many places where you should have been using natbib \citet{}.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
