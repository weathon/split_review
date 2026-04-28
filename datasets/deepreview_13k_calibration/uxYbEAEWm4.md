# Knowledge Lift Alignment Fine Tuning

- Decision: Reject
- Avg Score: 3.67
- Scores: 3, 5, 3

## Abstract
We present a visual tuning framework, \textbf{K}nowledge \textbf{L}ift \textbf{A}lignment \textbf{F}ine \textbf{T}uning (KLAFT), 
which enhances the expressive image captioning capabilities of Pre-trained Language Models (PLMs), including LLMs and VLMs.
As this task involves generating more detailed and comprehensive captions than basic image descriptions,
the core idea behind KLAFT is that fine-grained alignment could exploit the capabilities of PLMs and a given target domain dataset.
This idea motivates and challenges us to explore the framework that deeply understands both given images and text for this alignment and tuning PLMs towards expressive image captioning.
This direction modifies the attention mechanism (Modified Attention Mechanism, MAM) and develops both a Topic Control Mechanism (TCM) and their training objectives.
The innovation of KLAFT lies in its approach to addressing the disparities in knowledge - visual versus textual via MAM
and source versus target domain via TCM.
As these hidden spaces are conceptualized as distinct sub-networks within the PLM, each possessing specific knowledge,
KLAFT's unique contribution is in aligning and adjusting the weights of these sub-networks in a fine-grained manner,
and fine-tuning this PLM.
Our empirical studies demonstrate that KLAFT significantly improves expressive captioning tasks by aligning and amplifying target knowledge, with the potential for Parameter-Efficient Fine-Tuning (PEFT) at low computational cost.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This work present a visual tuning framework, Knowledge Lift Alignment Fine Tuning (KLAFT), which enhances the expressive image captioning capabilities of Pretrained Language Models (PLMs). The innovation of KLAFT lies in its approach to addressing the disparities in knowledge - visual versus textual via MAM and source versus target domain via TCM. These hidden spaces are conceptualized as distinct sub-networks, each possessing specific knowledge, KLAFT adjusts the weights of these sub-networks in a fine-grained manner. The empirical studies demonstrate that KLAFT improves expressive captioning tasks by aligning and amplifying target knowledge.

### Strengths
- The work propose design a Topic Control Mechanism (TCM) to emphasize the target domain-specific knowledge. Combined with Token Topic Modeling (TTM), Masked Region Modeling (MRM), and Text Image Matching (TIM), KLAFT highlights the target related
knowledge (i.e., the knowledge lift).

- The propsoed KLAFT improves expressive captioning tasks by aligning and amplifying target knowledge, with the potential for
Parameter-Efficient fine tuning (PEFT) at low computational cost.

### Weaknesses
 -  The writting of this work is quite poor. The inroduction part does not clearly introduce the background and motivation of the problem to be solved. The approach part is also not written in a concise and well-organized manner.

- The approaches compared in this work are not proposed recently. As a result, the validity and innovation of the proposed modules is not convincing.

- The authors did not conduct sufficient ablation experiments for different loss functions and did not give more qualitative analysis.

### Questions
See the weaknesses.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes Knowledge Lift Alignment Fine-Tuning (KLAFT) to enhance the expressiveness of image captioning capabilities in pretrained Vision-Language Models (VLMs). KLAFT primarily introduces a Topic Control Mechanism (TCM) combined with Token Topic Modeling (TTM) to enable topic-guided tuning and decoding for VLMs. The proposed method is evaluated across various settings.

### Strengths
* Increasing the expressiveness of the generation process in VLMs is a promising research direction.
* The proposed TCM/TTM approach is intriguing and shows potential.
* The performance gains over baseline models are satisfactory.

### Weaknesses
 * The presentation of the paper lacks clarity. I’ve outlined some key issues below:
  * The term "KEIC" appears three times—once in Figure 1, once in the title of Section 4, and again in the conclusion. These are critical sections. I assume "KEIC" should actually be "KLAFT."
  * Some typos or unclear sentences can a problem, e.g. ``tokes`` appears multiple times.
  * The image in Table 1 is not clear, and Figure 1 also lacks effective delivery and clarity.
  * I assume all the citations use ``\cite{}``. I think most citations should likely use ``\citet{}`` for smoother integration.
  * And some other issues, see question section as well.
* Overall, the claims around the design of the Mapping Layer (MaL) and the Modified Attention Mechanism (MAM) may be overstated. These components are fairly common in VLMs, and MAM appears to be a direct adaptation from one of the primary baselines, VisualGPT. The flexibility and generalization claims for MaL are not sufficiently substantiated, as many existing methods also achieve similar adaptability. The dynamic integration of attention masks in MAM, while interesting, lacks a detailed analysis of its novelty compared to existing attention mechanisms in models like VisualGPT. The paper needs to provide a more rigorous justification for the design choices of MaL and MAM, demonstrating clear advantages over existing techniques.
* The choice of main baselines seems outdated, although results from some recent VLMs (e.g., LLaVA, BLIP2) are also included. The core evaluation should be against more contemporary models, and the inclusion of older baselines should be justified by a specific need to demonstrate backward compatibility or a similar purpose.

* In Figure 1 (left), a plot of token distributions is shown, but there is no information about the dataset. What are the source and target domains? How were these lines plotted? Given the significance of comparing the two domains, this should be one of the most important analyses in the paper. The lack of clarity on the data used and the plotting methodology undermines the analysis.
* I get the main idea of TCM. Yet, there are some phrases in the paper making the details of TCM unclear to me:
  * In line 234, ``distribution over tokes, $\mathbf{V}$``. What is  $\mathbf{V}$? It only appears once in the paper. The variable $\mathbf{V}$ is not defined, making it difficult to understand the context of the distribution.
  * In the paragraph following Eq (5), the term $b_z$ is mentioned twice, though it doesn’t appear in Eq (5). This inconsistency makes it challenging to understand Equation (5) fully. Additionally, the variable $w$ is not explained in the paragraph. The lack of clear definitions for $b_z$ and $w$ makes the explanation of the equations unclear and hard to follow.
* In lines 338-339, it's stated that three hyperparameters are all set to 0.1, which seems to be less commonly done. What is the rationale for this choice? Is there any ablation study to support it? The paper should provide a more detailed explanation of the hyperparameter selection process, including ablation studies to justify the chosen values.
* In Sec. 5.2, the authors compare S4 to S3 to showcase the effectiveness of TCM. Yet, these two settings differ a lot:
  * S3: "seq2seq under fine-tuning GPT-2 over 100% training data (COCO+Conceptual Captions)"
  * S4: "prefix 100% training data with frozen setting (only COCO)"
  * Given the differences in both tuning paradigm and datasets, how can TCM’s impact be fairly assessed in this context? The comparison between S3 and S4 is not a fair assessment of TCM's impact due to the significant differences in fine-tuning paradigms and datasets. This makes it difficult to isolate the effect of TCM.
* Could you provide more details on human evaluation?

### Questions
* In Figure 1 (left), a plot of token distributions is shown, but there is no information about the dataset. What are the source and target domains? How were these lines plotted? Given the significance of comparing the two domains, this should be one of the most important analyses in the paper.
* I get the main idea of TCM. Yet, there are some phrases in the paper making the details of TCM unclear to me:
  * In line 234, `"distribution over tokes, $\mathbf{V}$. What is  $\mathbf{V}$? It only appears once in the paper.
  * In the paragraph following Eq (5), the term $b_z$ is mentioned twice, though it doesn’t appear in Eq (5). This inconsistency makes it challenging to understand Equation (5) fully. Additionally, the variable $w$ is not explained in the paragraph.
* In lines 338-339, it's stated that three hyperparameters are all set to 0.1, which seems to be less commonly done. What is the rationale for this choice? Is there any ablation study to support it?
* In Sec. 5.2, the authors compare S4 to S3 to showcase the effectiveness of TCM. Yet, these two settings differ a lot:
  * S3: "seq2seq under fine-tuning GPT-2 over 100% training data (COCO+Conceptual Captions)"
  * S4: "prefix 100% training data with frozen setting (only COCO)"
  * Given the differences in both tuning paradigm and datasets, how can TCM’s impact be fairly assessed in this context?
* Could you provide more details on human evaluation?

*I'm open to adjusting my rating after the authors' response.*

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a Knowledge Lift Alignment Fine Tuning (KLAFT) framework to improve the image captioning capability of multimodal LLMs. More specifically, this paper aims to encourage the generated captions to be detailed and comprehensive. To achieve that, this paper explores fine-grained alignment and designs MAM and TCM attention mechanisms. Experiments and quantitative comparisons are conducted on commonly used benchmark datasets, including MS COCO and Conceptual Captions.

### Strengths
1. Improving the quality of captions generated from VLMs has great potential for several real-world applications, such as manufacturing and healthcare.
2. The proposed framework is reasonable to address the considered task.

### Weaknesses
1. As described in the Abstract, the goal of this paper is to generate detailed and comprehensive captions. However, the benchmark datasets adopted by this paper (e.g., MS COCO) are typically coarse-grained with relatively short captions. As we know, current VLMs, like LLaVA, are good at generating detailed and fine-grained image captions. Is using COCO to evaluate the detailed caption capability of VLMs suitable? My concern lies in adopting such traditional image captioning benchmarks (e.g., COCO), which cannot properly measure the detailed caption capability of VLMs and reflect the actual improvement of the proposed method.
2. What are the differences between the source and target domains claimed in this paper? Does the difference lie in the visual domain shift? Does the difference lie in the caption style? Does the difference lie in the amount of (labeled) data? More clarification and explanation are encouraged to make this paper more easy to read.
3. The proposed method is trained by multiple training objectives. It is complicated to model training and balance the weights of each loss function (in Eq.(9)). How does this paper design experiments to determine the weight of each loss term? Is the model training sensitive to different weights of loss terms?
4. The visual presentation of this paper has some room to improve. For example, the image in Table 1 is out of the table. In addition, for Table 3, it is better to directly indicate the meaning of each row in the table instead of just mentioning it in the captions.

### Questions
Please refer to the Weaknesses. The following is a minor question.

1. Considering the fast-evolving nature of the VLM development, are some recently proposed and commonly used multimodal LLMs, such as VILA or InternVL-2, also applicable to this proposed fine-tuning framework?

### Soundness
2

### Presentation
1

### Contribution
2
