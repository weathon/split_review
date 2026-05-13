# STELLA: Leveraging Structural Representations to Enhance Protein Understanding with Multimodal LLMs

- Decision: Reject
- Scores: 3, 5, 10, 3, 8, 6

## Abstract
Protein biology centers on the intricate relationships among sequence, structure, and function (text), with structure understanding being a crucial aspect for uncovering protein biological functions. Traditional methods based on protein language models (pLMs) often focus on specific aspects of biological function prediction but do not account for the broader, dynamic context of protein research—an important component for addressing the complexity of protein biology. Modern large language models (LLMs) excel in human-machine interaction, language understanding and generation, at a human-like level. By bridging structural representations with the contextual knowledge encoded within LLMs, STELLA leverages the strengths of LLMs to enable versatile and accurate predictions in protein-related tasks. It showcases the transformative potential of multimodal LLMs as a novel paradigm besides pLMs in advancing protein biology research by achieving state-of-the-art performance in both functional description and enzyme-catalyzed reaction prediction tasks. This study not only establishes an innovative LLM-based paradigm to understand proteins, but also expands the boundaries of LLM capabilities in protein biology. To foster collaboration and inspire further innovation, the codes, datasets, and pre-trained models are made publicly available at the anonymous GitHub repository https://anonymous.4open.science/r/STELLA-DF00.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper introduces STELLA, a multimodal large language model (LLM) designed to enhance protein understanding by integrating structural representations with natural language processing. By enhancing LLM capabilities with protein structural information, STELLA aims to improve predictions of protein/enzyme functions. Comprehensive experiments were conducted to evaluate STELLA's performance on function prediction and enzyme name prediction tasks. The authors provide open access to the code and datasets for further research.

### Strengths
1. **Novelty**: STELLA presents a novel approach by combining protein structural data with LLMs.
2. **Open Access**: Open access to the code and datasets encourages collaboration and further innovation in the field.

### Weaknesses
1. **Usefulness**: Frankly, I don't find this work very useful practically. Usually, users who have the structure data of a protein already know its function. Even if not, they can use foldseek to find a list of structurally similar proteins, and infer its function from the annotations of these proteins (manually or using GPT-4o). The authors have not compared their method with this straightforward baseline.
2. **Technical contribution**: This work replaces the protein sequence encoder in existing work with a protein structure encoder. It reaffirms the superiority of ESM3 and Llama-3.1. Beyond that, I have not seen many significant technical contributions or insights that could inspire future work.

### Questions
1. Could you compare STELLA with the FoldSeek/Blastp + GPT-4o baseline, where the input of GPT-4o are the descriptions and e-values of the FoldSeek/Blastp-retrieved proteins?
2. How do you evaluate the accuracy on the EP task, considering enzymes can have alternative names? Here are a few examples: Lactase vs β-Galactosidase, Lipase vs Triacylglycerol Lipase, Catalase vs Hydrogen Peroxide Oxidoreductase, Alcohol Dehydrogenase vs ADH, Hexokinase vs ATP:D-hexose 6-phosphotransferase.
3. Could you reiterate the motivation of your work, i.e., what are the limitations of existing work and how STELLA contributed to the community?

### Soundness
3

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This manuscript proposed STELLA, a multimodal LLM that integrates structural protein representations with LLMs to enhance protein understanding. It addresses the main limitation of traditional methods of solely depending on structural data and lacking the ability to incorporate iterative feedback from domain experts. This authors also developed the OPI-Struc dataset, conducted comprehensive evaluation, and provided open access to the code, datasets and models.

### Strengths
1. The proposed STELLA is an innovative approach that harnesses the capabilities of LLMs enriched with structural information. It has great potential to learn complex structure-function relationships from large datasets by integrating structural data with vast biochemical knowledge. It is also beneficial to bridge machine-readable protein language and human-readable natural language.

2. This paper present well-developed OPI-Struc dataset, and comprehensive evaluations. It takes into account the newer release of Swiss-Prot to assess the inference performance on unseen data, dataset options with or without permutations, and proper data split.

3. This paper is well written and well organized, with clear figure demonstration, tables, and good readability. It is easy for readers to follow.

### Weaknesses
1. For the important metrics, FP_{eval_FTQA(_v2401)} and EP_{eval}, STELLA performs slightly worse than the start-of-the-art methods. For metrics FP_{eval_MCQA}, although STELLA enables responding to this kind of questions, we lack baselines to demonstrate STELLA's superior performance. In addition, multiple-choice Q&A may not be a common use case for this model in practice.

2. There's a significant gap between metric FP_{eval_MCQA_1X} and metric FP_{eval_MCQA_4X}. It would be beneficial to include discussions and insights for this observation, and how to further reduce the sensitivity to the permutation.

3. (minor) This paper mentions the ability to incorporate iterative feedback from domain experts. Although this is only possible with the integration of LLM-based multi-turn dialogue (which we show in the paper), it might be useful to demonstrate this using some "expert-feedback" examples.

### Questions
Please kindly refer to section "Weaknesses".

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
10

### Rating Number
10

### Confidence
3

### Summary
This paper introduces a new approach for protein function prediction by integrating proteins LLMs (e.g., ESM3) with NLP LLMs (Llama-3.1) to essentially “translate” from a structure-based representation into a natural language one. Part of this work involved creating a new dataset for training and evaluation.

### Strengths
* Integrating and translating between LLMs in entirely different domains, e.g., protein structure and natural language, is a new and highly promising direction. While such multimodal integration is common in vision and NLP, there’s been virtually no work in the space of protein structure and NLP (function), which this paper pioneers.
* To accomplish the authors create a new dataset, which they call Open Protein Instructions for Structures (OPI-Struc), a new effort into its own right to be able to train this model and assess it rigorously.
* The core idea of using a structure-based embedding to translate protein structures into a common latent space with NLP-based function annotations is clever and is sufficiently interesting and promising that it may become a whole new research direction.
* Evaluations are done rigorously, there’s not a tendency to try to inflate the results (great!), and some ablations are performed to assess different contributions to model performance.

### Weaknesses
 * The paper largely builds on an existing framework for vision-NLP integration (LLaVA) by modifying it to the protein domain. Given how different proteins are from vision, it is likely that much further advancement can be had by innovating architecturally. However, this is a minor quibble as this paper pushes the frontier of protein multimodal integration and it makes sense to start with known architectures.
* The actual results are a bit underwhelming. The model does not really push the state of the art. Nonetheless, I consider this a minor issue as it introduces a new way of performing protein function prediction which I am sure can be improved substantially in the future.

### Questions
Please fill in some of the currently missing technical details, even if the code will be available. For instance what ESM3 model is used is not described (there are multiple).

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper presents a multimodal model, STELLA, which integrates the tertiary structure of proteins into LLM, enabling LLM to understand PDB data to some extent. Through natural language instructions, STELLA can provide information about the protein in the input PDB. The model was trained and tested on the OPI-Struc dataset, achieving comparable results in function prediction and enzyme prediction.

### Strengths
The proposed model can conduct multi-round dialogues, presenting potential advantages in the interaction between experts and machines.

### Weaknesses
1. The authors state: "However, the PDB entries still lack detailed functional annotations except for function keywords." To my knowledge, each PDB co-crystal structure comes from a high-level research paper, which contains detailed research on the protein in the PDB. I am unsure what the authors mean by "lack detailed functional annotations."

2. The authors state: "these methods rarely incorporate iterative feedback from domain experts, a critical factor for refining predictions and improving their accuracy." While STELLA does support multi-round dialogues, it does not achieve optimal performance in Function Prediction (FP) and Enzyme Name Prediction (EP) tasks, showing no advantage over other methods that do not support multi-round dialogues. This seems to contradict the authors' claim.

3. The authors state: "Traditional methods often struggle to integrate the fine-grained structural details needed for accurate enzyme prediction, particularly when trying to model the influence of both local and global structural factors." Firstly, STELLA does not outperform the so-called "Traditional methods" in the EP task. Secondly, STELLA does not seem to mention how it handles "local and global structural factors."

4. Prot2Text is a baseline in this paper. Compared to Prot2Text, STELLA lacks sequence information, and the protein structure encoder and LLM backbone are different, but there is not much difference otherwise. I would like to know why the sequence information was removed. Moreover, as shown in Table 2, STELLA does not have an advantage over Prot2Text in the FP task.

5. As shown in Table 5, STELLA does not perform well in the EP task, falling below CDConv and New IEConv.

6. Figure 3 and Figure 4 do not seem to provide any useful information. Additionally, the authors use "Fig. X" when referencing figures, but the caption of the figures is "Figure. X."

### Questions
See Weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
STELLA offers a valuable protein function prediction tool powered by large language models, potentially having a significant impact on the field of bioinformatics. Key contributions include the possibility of predicting protein function using structure information and advanced LLM capabilities, demonstrating STELLA’s effectiveness in function prediction. STELLA can facilitate research in life science and has the potential to provide another layer of information besides folding structures like AlphaFold.

### Strengths
Overall, this submission is structured clearly and defines the biological question it aims to address. STELLA  originality is based on its innovative approach to bridging structural representations with LLM capabilities, which allows it to interpret complex protein structures and respond to diverse contextual queries. This provides another layer of protein functionality besides its folding structure like emerging popular tools such as AlphaFold. This submission demonstrates solid technical foundation such as showing results based on a two-stage multimodal instruction tuning process, combinations trying of models, and comparable improvements from previous similar SOTA models.

### Weaknesses
The metrics used in the evaluation section may not fully capture the biological relevance and accuracy of protein function predictions (just comparing generated answer vs ground truth description of protein function). The BLEU score, for instance, may not reflect nuanced but critical differences in function. Moreover, I am quite concerned about the limitation of the OPI-Struc dataset. Although the authors mentioned these target on Function and Enzyme, it is better to evaluate the tasks based on more diverse types of classification of proteins (functional protein used as virulence factors in bacteria vs functional protein in mitochondria in mice). How the future impacts of STELLA, especially how confident the interpretation of the protein, should be further discussed. The false interpretation of protein function may lead to the wrong direction of biotech operation, which results in a significant waste of funding.

### Questions
1. Could the authors share insights on why ESM3 was preferred over other potential encoders, this will provide reasons for future studies to choose ESM3 as a protein encoder. 
2. Could the authors provide clarification on why STELLA performs comparably to Prot2TextLARGE in some metrics but underperforms in others (e.g., ROUGE and BERT-score for specific tasks)? Adding an explanation would be helpful to understand the specific cases or factors influencing these results.
3.. On Table 3, since ESM3, and Prot2Text these models cannot be evaluated using acc@MCQA_1x and acc@MCQA_4x, is it worth putting these results into a table?
4. A few sentences describing future user usage will be appreciated. How do researchers in the science field use STELLA and more importantly how confident the results from STELLA can guide the direction of research and even decision formation?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 6

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces STELLA for protein function and enzyme-catalyzed reaction prediction. The work combined multiple existing tools to generate the workflow. While the idea is in principle sound, the novelty is not well described.

### Strengths
STELLA integrates protein structure data with LLMs to enhance protein function and enzyme prediction tasks.
It provides comprehensive evaluations, utilizing different datasets and metrics, which adds credibility to the performance claims.
By sharing the code, datasets, and pre-trained models, the study facilitates collaboration and fosters further research in the field.
The presentation, including graph demonstration and writtent text, is clear.

### Weaknesses
The paper does not clearly differentiate STELLA from existing multimodal models like Prot2Text and other protein prediction frameworks. A clearer outline of unique contributions and improvements over prior methods would strengthen the work.
The benchmark results are not superior to state-of-the-art results from existing multimodal models.
The paper may include more demonstrations from biological side.

### Questions
While STELLA seems to enhance function prediction, I wonder if the model’s reasoning behind those predictions is easy to interpret. What measures, if any, have been taken to make its outputs understandable, especially for biologists who need to validate its findings?
Given that STELLA relies heavily on structured protein data, how does it perform when dealing with less common protein structures? In my experience, we often work with proteins that lack precise structure or even sequence information in certain regions. How well could STELLA handle incomplete protein data?
Does STELLA show a significant enough improvement over other established models to justify its scientific meaning and contribution?
I’m curious about the model’s scalability because of the interactive demonstration. Can STELLA efficiently handle large-scale datasets or high-throughput predictions?

### Soundness
3

### Presentation
4

### Contribution
2
