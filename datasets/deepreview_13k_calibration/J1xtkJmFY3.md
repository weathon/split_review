# ZerOmics: Toward General Models for Single-Cell Analysis with Instruction Tuning

- Decision: Reject
- Avg Score: 4.67
- Scores: 5, 3, 6

## Abstract
A variety of analysis tasks in single-cell (SC) multi-omics are crucial for precision medicine and clinical research. To address these tasks, existing methods are typically pre-trained on large-scale datasets to obtain general representations, followed by fine-tuning on specific tasks and labeled datasets. However, their task-specific heads often lack generalizability, significantly limiting performance in zero-shot scenarios. Inspired by the success of large language models (LLMs), we propose ZerOmics, the first zero-shot method that guides LLMs to perform various SC tasks without relying on specific downstream data. To enable LLMs to establish a correct and comprehensive understanding of SC data, ZerOmics employs a dual-alignment strategy. Specifically, ZerOmics aligns SC expression data with the well-organized gene corpus, thereby generating robust SC embeddings. These embeddings are then incorporated into instructions designed for various SC analysis tasks to tune the LLM, achieving alignment between SC data and the LLM. Extensive experiments across various sequencing technologies and tissues demonstrate that ZerOmics provides a comprehensive and general solution for SC analysis, achieving performance comparable to or even surpassing the state-of-the-art (SOTA) supervised and fine-tuned methods.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This work presents a method to encode single cell expression data as a token to an LLM enabling it to be finetuned with these new tokens for tasks such as cell type classification. The single cell sample representation is learned by a denoising autoencoder and then this representation is linearly transformed into the dimension of a token embedding for a language model.

### Strengths
This work tackles an interesting problem of enabling language models to reason about the modality of single cell genomics. The experiments performed compare against supervised baselines. 
There are many ablation studies performed to explore what aspects of the method are working.

### Weaknesses
I expected to see more exploration into the method of incorporating a single cell observation. This work only discusses a single approach (besides the gene2vec ablation) while I'm sure the research team experienced many configurations that didn't work. It would be nice to have experiments with these alternatives as well.

Edit: After reviewing comments from Reviewer 1RvP I agree that the method does not appear to be zero-shot due to pre-training for each task as confirmed by the statement "To assess the performance in a zero-shot setting, SC datasets are split into a training set for pre-training and tuning, and a test set for evaluation".

I now believe a re-framing of the paper should occur to prevent confusion. The method is not as simple as taking the SC sample embedding for a single cell and putting it in a prompt as the current framing implies.

### Questions
None

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors present ZerOmics, a zero-shot method to guide LLMs to assist with single-cell (SC) tasks. The authors propose to combine SC expression data with textual information (gene corpus) via summation, to produce embeddings with more information content. They then insert these embeddings into a set of instructions used to finetune an LLM (LLaMA2-13B) on different SC tasks: cell type annotation (CTA), rare cell identification (RCI) and tumor cell identification (TCD). Finetuning is carried out using a mixture of universal and task-specific LoRAs. Results suggest that ZerOmics improves the cell classification tasks across most of the investigated datasets. The authors provide ablation on different parts of their architecture (Gene text embedding, SC tokenizer, Mixture of LoRAs), as well as comparison to different baseline methods for each task.

### Strengths
The authors introduce an architecture which combines SC embeddings with textual information about the genes/datasets, in an effort to produce more informative, robust embeddings, which could help alleviate the natural heterogeneity in SC, the well-know batch effect issues and the high-dimensional nature of SC by introducing constraints via additional textual information. I think the main novelty here is focusing on using a general purpose LLM for different SC tasks, by using the instruction tuning paradigm where they format tasks as prompts with SC+Text embeddings included in the instruction. The first introductory section of the paper is clear, situating the work well with regards to the relevant literature in my opinion. The author's also investigate results on three different SC tasks (CTA, RCI and TCD), as well as on 9 different datasets, which is a strong point in their favour.

### Weaknesses
In my opinion there main weakness of the paper lies in the experimental design, both in the pipeline itself and in the splitting of the datasets:

- I don't think this approach can truly be called zero-shot: from what I understand, there's a first pretraining of the SC model to combine the SC embedding with the Text embeddings (obtained from a frozen LLM). Then there's the instruction-tuning of the LLM on different tasks (CTA, RCI and TCD), where both universal and task specific LoRAs are used. They then test on held-out datasets, but only for tasks and on classes the LLM was explicitly trained for. This is fundamentally different from true zero-shot learning where a model should be able to handle completely new tasks without task-specific training. This contradicts the paper's claim it's generalisable to unseen tasks. The use of task-specific LoRAs during instruction tuning, even if frozen later, means the model is explicitly trained on the specific tasks (CTA, RCI, TCD) it is then evaluated on, which is not a zero-shot setting in the traditional sense. A true zero-shot approach would involve evaluating the model on completely new tasks without any task-specific training of the model.

- This raises the issue of memorisation in the model. Because LLaMa is fine-tuned using instructions that include the learned combined SC+Text embeddings and a task description which contains a curated list of possible answers, this experimental design is explicitly showing the model how to combine embedding-answer pair, which sounds more like memorisation where the model learns how to associate certain embedding patterns with labels from the training set, then inferring true meaningful biological relationships. The ablation results in Table 5 actually strengthen this concern, as the model performs significantly better when using both abstracts and task-specific components (85.56% accuracy on CTA-PBMC68K) compared to using just gene embeddings (79.71% with GeneCompass, 65.85% with Gene2vec). Moreover, removing either the text components or task-specific LoRAs leads to substantial performance drops. This pattern suggests the model's strong performance depends heavily on matching text descriptions with expression patterns during the instruction tuning phase, rather than learning to understand the underlying biology.

- The author's claim that using candidate answers encourages the model to compare and contrast different options, but I find this statement ish misleading, as it implies that merely providing candidate answers automatically leads to improved model reasoning through comparison. In reality, LLMs do not inherently engage in comparative reasoning without additional mechanisms specifically designed to facilitate this process. The cited paper Kim et al. 2024 demonstrates that only with an explicit prompting framework—where candidate answers are iteratively evaluated and refined—can such comparative reasoning effectively enhance prediction accuracy. Therefore, to support their claim, the authors should clarify how ZerOmics specifically leverages candidate answers to encourage genuine comparison or else acknowledge that additional prompt engineering would be necessary to achieve this effect.

- In line with the above points, the instruction set contains the actual abstract of the paper where the dataset is described (in addition to the SC+T embedding and task description), which seems like it could be an important source of data leakage. I would like to see how removing the abstract from the instruction prompt changes the results, to check if this might the case or not. Scientific abstracts frequently contain explicit descriptions of cell type markers, expression patterns associated with specific cell populations, and relationships between gene expression and cellular phenotypes. For instance, an abstract studying T cell populations might state "CD4+ T cells were identified by high expression of CD4 and IL7R." This directly links cell type identity to specific gene expression patterns. Similarly, abstracts often describe how cell types were validated using specific marker genes, or detail expression-based criteria used for cell type assignment. Given that this information is provided in the instruction prompt alongside the cell's expression data, the model could potentially learn to match these text-described patterns rather than discovering true biological relationships from the expression data alone. This makes it impossible to determine whether the model is actually learning to understand single-cell data or is simply exploiting detailed biological knowledge provided in the abstracts.

- It's very unclear to me from the text how the datasets are split into train-test. It seems like the authors are training and testing on the same datasets, with the argument that batch effect is so strong this is the same as testing on a completely different dataset. If this is the case, as I think it is from the description, then I strongly disagree. Yes, batch effect can be very strong, but to make the argument that this is equivalent to testing on a completely different dataset then at a minimum I'd like to see embeddings showing me relative distance between the datasets. This contradicts the paper's claim that the method is generalisable to unseen datasets. The paper states that type 2 (training/fine-tuning) and type 3 (evaluation) datasets "are split from the same evaluation datasets, sharing the same sampling conditions and sequencing processes." This directly contradicts the claim of independence, highlighting my original concern. To demonstrate true independence and generalization capability, evaluation should be performed on datasets from completely separate experiments with different sampling conditions. Without clear metrics quantifying dataset independence or clear evidence that evaluation datasets truly come from different experimental conditions, the authors haven't adequately addressed my core concern about whether their method genuinely generalizes across datasets.

- No confidence intervals or other estimates of uncertainty are included. I encourage the author's to include confidence intervals on their results, either through cross validation or bootstrapping.

### Questions
Based on the perceived weaknesses I expanded on above, here's a list of questions to be addressed by the authors, as well as some more general comments included below: 

Zero-shot claims:

- Could you clearly justify why you are calling this approach "zero-shot" when you use task-specific LoRAs and instruction tuning for each type of task (CTA, RCI, TCD)?
- Can you demonstrate the model performing well on a completely new type of task it wasn't instruction-tuned for? The experiment on cell pathway inference in 4.3 isn't conclusive as you acknowledge the gene corpus used in pre-training explicitly contains descriptions of these biological processes. This could therefore just be another example of memorisation. 
- Furthermore, you don't compare your results to LangCell which has zero-shot capability. I would expect to see LangCell's zero-shot performance as the baseline comparison in this instance. 

Memorisation issues:

- How do you ensure your model is learning meaningful biological relationships rather than just memorizing embedding-answer pairs during instruction tuning? What controls or ablation studies have you done to demonstrate the model isn't simply pattern matching against its training data?

Comparative reasoning:

- What specific mechanisms in your architecture enables comparative reasoning between candidate answers? Have you performed experiments showing that providing candidate answers improves performance through comparison rather than just constraining the output space?

Data leakage:

- Have you tested model performance without including dataset abstracts in the instruction prompts? What controls have you implemented to ensure the model isn't leveraging information from the abstracts rather than learning from the SC data?

Dataset splitting:

- Can you provide a clear description of your train-test split methodology?
- Can you demonstrate through embedding analysis that the batch effect differences are comparable to true dataset differences?

Ablation:

- Is the ablation done in a zero-shot setting or after fine-tuning? This significantly affects the interpretation of the ablation study results, so needs to be clearly highlighted in the text. 

Generalisation:

- Have you tested the model on truly independent datasets from different studies/labs?

Further comments:

- Lines 120 - 121: “Gene expression data are often affected by many non-biological factors and the information they reveal is not as profound as text data”. 

I suggest you might want to rephrase this statement, which implies text data contains more information than the actual SC data. Gene expression data is a reflection of the huge biological complexity inherent to our cellular machinery. Furthermore, cell-specific gene expression profiles are more idiosyncratic to a specific cell, whereas textual descriptions tend to be a lot more general, so what exactly is meant by “gene expression data is not as profound as text data” here? 

- Line 158 - 161: "Genes that are highly expressed in most cells,
such as housekeeping genes, may exhibit lower expression levels in this context. In contrast, genes that are lowly expressed but crucial for identifying cell states, such as transcription factors, may exhibit higher expression levels."

I believe this statement is factually incorrect: Quantile normalisation doesn't inherently lower the expression value of highly expressed genes or increase the value of lowly expressed ones. Instead, it preserves the ranking between genes in each sample, as well as forcing expression values to follow the same distribution across samples. Could you expand or explain this point? 

Line 202 - 206: "Multi-modal mask learning for semantic alignment. Cell expression and gene text embeddings reveal distinct levels of biomedical information within SC data. Using multi-modal learning to align their semantic spaces inspires the model to extract more comprehensive representations. For computational efficiency, ZerOmics utilizes the broadcasting to directly add Z\_T to Z\_E, which is then encoded to the contextual SC embeddings that contain the gene functional semantics, ..." 

Am I correct to interpret broadcasting as elementwise summation of the SC and Text embedding? This should be clarified in the text. Can you really call this semantic alignment if what you're doing to align them is to broadcast them together via direct summation?

- Lines 301 - 303: “Three challenging single-cell tasks -- cell type annotation, rare cell identification and tumor cell discovery” 

CTA are a staple task that has repeatedly been shown to be accurately predicted even by simple logistic regression based methods (see [1] and [2]). While interesting and important, cell type annotation is not a particularly challenging task so I would rephrase this statement. 

- Line 072: "inadequately designed task-specific heads" - why are they inadequately designed? What do you do to design a better task-head? How do you test this better design? 

- Line 133: "elevatable" What does this mean? 

- As a general comment, I would say the text is quite clear until section 3.2, but the rest is quite confusing to read and I suggest the author's might try to rework these sections to gain clarity. 

[1] https://www.biorxiv.org/content/10.1101/2023.10.19.563100v1

[2] https://www.biorxiv.org/content/10.1101/2023.10.16.561085v1

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces ZerOmics, a novel zero-shot approach that leverages large language models (LLMs) to tackle single-cell analysis tasks without requiring downstream task-specific data. ZerOmics emphasizes a dual-alignment strategy to align single-cell (SC) expression data with gene corpus text embeddings, enabling a broader, zero-shot capability. Results indicate that ZerOmics matches or exceeds performance from established supervised and fine-tuned methods, showcasing notable generalizability.

### Strengths
The idea of incorporating gene text embedding is intuitive.

Utilizing LLMs in single-cell data analysis is an important open problem which has attracted a lot of attention recently and ZerOmics provides a promising technical roadmap.  

ZerOmics demonstrates strong experimental performance across diverse SC tasks, indicating a high level of effectiveness.

### Weaknesses
1. The ablation study on gene text embedding can be more thorough. 

2. ZerOmics currently focuses on tasks like cell type annotation, which may not fully highlight the model's zero-shot potential across tasks requiring diverse output formats. It would be helpful to explore the model’s performance on tasks less dependent on natural language formulations, such as regression tasks.

### Questions
1. In the pre-training stage, how can the model predict the gene items? How does the model handle instances where multiple masked genes share identical expression bins?

2. Can the author explore the performance of ZerOmics with other types of gene embeddings, such as those obtained from existing single-cell foundation models?

3. Related to the last question, What is the necessity of the first scmodel pre-training part? Could a simpler model, like a single-layer MLP tokenizer, generate single-cell embeddings from expression values directly? More ablation on this could clarify the SC model’s role.

4. How does the author choose the 10 samples for few shot learning? Does the diversity of samples affect the model's performance?

5. Does ZerOmics perform well in scenarios where task objectives extend beyond natural language-compatible tasks, such as regression? Testing on such tasks would demonstrate broader applicability.

6. A recent study (https://www.biorxiv.org/content/10.1101/2023.10.16.562533) addresses similar issues in zero-shot single-cell analysis. Could the authors provide a comparative analysis, covering both methodological differences and performance on shared tasks?

### Soundness
3

### Presentation
3

### Contribution
4
