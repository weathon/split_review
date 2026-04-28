# ViCor: Bridging Visual Understanding and Commonsense Reasoning with Large Language Models

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 6, 5, 3

## Abstract
In our work, we explore the synergistic capabilities of pre-trained vision-and-language models (VLMs) and large language models (LLMs) on visual commonsense reasoning (VCR) problems. 
We find that VLMs and LLMs-based decision pipelines are good at different kinds of VCR problems. Pre-trained VLMs exhibit strong performance for problems involving understanding the literal visual content, which we noted as visual commonsense understanding (VCU). For problems where the goal is to infer conclusions beyond image content, which we noted as visual commonsense inference (VCI), VLMs face difficulties, while LLMs, given sufficient visual evidence, can use commonsense to infer the answer well. 
We empirically validate this by letting LLMs classify VCR problems into these two categories and show the significant difference between VLM and LLM with image caption decision pipelines on two subproblems. 
Moreover, we identify a challenge with VLMs' \textit{passive} perception, which may miss crucial context information, leading to incorrect reasoning by LLMs. 
Based on these, we suggest a collaborative approach, named \textbf{ViCor}, where pre-trained LLMs serve as problem classifiers to analyze the problem category, then either use VLMs to answer the question directly or \textit{actively} instruct VLMs to concentrate on and gather relevant visual elements to support potential commonsense inferences. 
We evaluate our framework on two VCR benchmark datasets and outperform all other methods that do not require in-domain fine-tuning.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper explores using vision-language models and language models for visual commonsense reasoning.  The VCR problem is categorized into two parts: (1) visual commonsense understanding (VCU) and (2) visual commonsense inference (VCI).  The paper identifies that VLMs may struggle with VCI and therefore, the paper employs LLMs to aid and collaborate VLMs for better VCR.  Experimental results are demonstrated for two VCR datasets (VCR from Zellers et al. and AOKVQA from Schwenk et al.)

### Strengths
1. This paper provides strong empirical results when combining proprietary language models such as GPT with vision-language models for solving VCR problems.
2. I wouldn't want to dismiss the paper as "combination of multiple proprietary blackboxes" (although it probably is that) -- the paper does demonstrate that there are novel ways to leverage these tools for solving challenging problems in vision.  
3. The paper is well written and well explained to someone who is already familiar with the advances in this domain. See Weakness 4 for the flip side.

### Weaknesses
1. Experiments could be more exhaustive -- for instance, why not expand the experiments into more VCR datasets such as OKVQA (Marino et al.), VisualComet (Park et al.), V2C (Fang et al)?  
2. The pipeline doesn't seem to be specific to VCR and could be used for any VQA dataset (eg. VQAv2, GQA, CLEVR, etc.) -- it's not clear whether the proposed method also improve performance on these datasets.  In practice, questions to a real-time system could be of any type (those about commonsense or those about simple perception) -- so it would be important to improve performance on both.
3. In Table 1, it is unclear how each dataset is divided into two parts VCU and VCI for evaluation.
4. The paper is well written and well explained to someone who is already familiar with the advances in this domain, but this assumption could have limiting effects on who learns from the paper -- one of the advantages of publishing NLP papers in ICLR is a wider reach to the broad ML community (and a large part of this community does not work on NLP or LLMs).

### Questions
1. Please define "Sup" and "ICL" for readers -- the acronyms may be common in the active LLM research community, but you cannot assume that readers are part of this active community, especially since in-context learning is only a couple of years old.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper suggests current visual-language model(VLM) often perceives the image passively and does not provide crucial contextual information to LLM for answering questions. Thus it category the commonsense VQA into two categories: visual commonsense understanding (VCU) and visual commonsense inference（VCI). For the harder VCI problems, the paper proposes to prompt LLM to generate questions and query VLM to obtain related visual information. The proposed method improves the baseline in-context learning performance on the knowledge-based VQA task.

### Strengths
The proposed method is well-motivated. Current pre-trained VLMs do not extract visual context based on the input questions. The proposed method can address this problem.

### Weaknesses
Existing methods, such as BLIP2, instructBLIP, and mini-GPT4, align the visual context with the LLM inputs embedding instead of input words and achieve better performance. It is not clear why the proposed method uses words(caption or VQA result) to transfer information from the VLM to LLM.

The paper lacks implementation details of the proposed model and compared methods. BLIP2 has a different setting to obtain the answer to the original one.

### Questions
- What is the j in o_j represent? How is the range of j determined?
- How are the in-context examples obtained? From training set or manually written?
- The BLIP-2 can directly generate the answer for visual questions. How does the BLIP-2 perform in this setting?
- The instructBLIP is not trained on the VCR dataset. What is it zero/few-shot performance on VCR?
- What is the LLM size of the compared baseline? Do they have a similar number of parameters to the proposed model?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a vision-language joint reasoning framework, ViCor, to achieve the synergy between a pretrained vision-language model (VLM) and an LLM. ViCor has outperformed other prompting-LLM-based approaches on two visual commonsense reasoning benchmarks, namely VCR and A-OKVQA. 

Concretely, ViCor involves using an LLM as a problem categorizer (high- vs. low-confidence; understanding vs. inference). Then the LLM also acts as a commander to query appropriate visual clues from the VLM. These manners of directing information flows according to the question property is demonstrated to be effective in harnessing complementary benefits of both VLM and LLM.

However, ViCor still underperforms supervised finetuning methods, which is left for future work.

### Strengths
This paper provides important insights about the comparative advantages of VLMs and LLMs, and introduces an effective framework where they can collaborate. Concretely, VLMs are better at recognizing literal visual content. Their contrastive pretraining has equipped them with strong image-text alignment capabilities. However, VLMs lack commonsense or world knowledge. Thus VLMs could be benefit from LLMs providing texts including meaningful visual clues to compute alignment scores. On the other hand, LLMs posses a wealth of  commonsense and world knowledge, and are better at expanding or decomposing problems. But LLMs do not have direct access to visual information, thus would require a VLM to act at their commands.
Studies in this paper have attempted to revealed that:
- VLM as the decision model is suboptimal due to the lack of overall reasoning ability, unless the task is as simple as recognizing the literal visual content.
- LLM as the decision model works only when it partners with a VLM and queries the VLM with **visual-clue**-rich texts rewritten from the original textual question.
- The collaborative paradigm between VLM and LLM mitigates mistakes originated from a) easily overlooked visual clues in the surroundings, b) lack of explicit mentions of relevant visual factors in the question, c) misdirecting objects in the foreground.

### Weaknesses
 - Judging from Table1, the number of examples studied is very small. It is unclear if the evidence derived from the results is robust.
- No multiple runs across decoding configs (e.g. temperature, selection of in-context examples). This limits the robustness and generality of the findings.
- Judging from Table1's LLM section: I'm having a hard time drawing conclusive insights from these results. LLM+Caption wins in two columns, LLM+Caption+VQA wins in two columns, while LLM+Caption+LLMclue wins in 4 columns. None of the settings is consistently stronger. Nor do the results suggest a consistent way to choose settings based on the problem category.

I believe that demonstrating how LLM and VLM can wisely collaborate in reasoning tasks is a direction worth pursuing. Therefore, I don't question the motivation of this paper. However, this paper only produced preliminary results on small validation sets and with a single set of decoding configurations. So, the results might lack generality and comprehensiveness. More comprehensive experiments across larger datasets and multiple seeds/decoding configurations would significantly strengthen the arguments the authors have sought to put forth.

### Questions
- Sec5.2 "BLIP2-FlanT5 XL for visual question answering": I'm having a hard time understanding the LLM+VQA workflow. I didn't see a corresponding VQA module in Fig2. Moreover, the paragraph between Eq6&7 explained why a VQA model often faces diffifulties, so I thought you have deemed a VQA model inadequate. Could you clarify whether you include a VQA model due to its comparative advantages under certain circumstances, or simply as a baseline? Also, could you update Fig2 and show where a VQA model would fit in the workflow?
- Sec6.3 "VQA does not understand the intention of the visual factor without the context of the main question": Have you tried concatenating the original question and the question about the visual factor as joint inputs to the VQA model?
- Table2: What is ICL? (Image-contrastive learning?)
- It appears that the categorization of VCU/VCI is solely determined by the LLM. Have you considered any measure to empirically test the reliability of this classification?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper dissects the visual common sense reasoning task into two sub-problems: visual common sense understanding and visual common sense inference.
A method that connects these two sub-tasks is proposed based on VLM and LLM.
The experiments are conducted on the VCR and A-OKVQA datasets.

### Strengths
- The studied problem - visual common sense reasoning, is useful and practical for evaluating large models' reasoning capabilities.
- The finding that the captions cannot be used for answering questions is interesting to know.

### Weaknesses
 - The re-definition of visual common sense reasoning is not convincing at all.
There is a large overlap between the two sub-problems of visual common sense understanding and visual common sense inference. 
Moreover, reasoning and understanding are also very close.

- Even with this new definition, the authors still perform their experiments on the VCR dataset, which is extremely confusing.

- There is no explicit definition of VCI.

- In fact, the definition of VCU is no different from that of image text retrieval.

- Fig.4, I think, should be changed with a table rather than drawing a table.

### Questions
See the weakness part.
Overall, I think this paper is far from the acceptance bar of ICLR.

### Soundness
1 poor

### Presentation
1 poor

### Contribution
1 poor
