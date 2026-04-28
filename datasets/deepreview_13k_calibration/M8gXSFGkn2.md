# Do Egocentric Video-Language Models Truly Understand Hand-Object Interactions?

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 8, 8, 6

## Abstract
Egocentric video-language pretraining is a crucial paradigm to advance the learning of egocentric hand-object interactions (EgoHOI). 
Despite the great success on existing testbeds, these benchmarks focus more on closed-set visual concepts or limited scenarios.
Due to the occurrence of diverse EgoHOIs in the real world, we propose an open-vocabulary benchmark named \textbf{EgoHOIBench} to reveal the diminished performance of current egocentric video-language models (EgoVLM) on fined-grained concepts, indicating that these models still lack a full spectrum of egocentric understanding.
We attribute this performance gap to insufficient fine-grained supervision and strong bias towards understanding objects rather than temporal dynamics in current methods.
To tackle these issues, we introduce a novel asymmetric contrastive objective for EgoHOI named \textbf{EgoNCE++}. 
For video-to-text loss, we enhance text supervision through the generation of negative captions by leveraging the in-context learning of large language models to perform HOI-related word substitution. 
For text-to-video loss, we propose an object-centric positive video sampling strategy that aggregates video representations by the same nouns. 
Our extensive experiments demonstrate that EgoNCE++ significantly boosts open-vocabulary HOI recognition, multi-instance retrieval, and action recognition tasks across various egocentric models, with improvements of up to \textbf{+26.55\%}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper focuses on understanding hand-object interactions using egocentric video-language models (EgoVLMs). The authors introduce a new benchmark called EgoHOIBench to evaluate EgoVLMs' ability to distinguish between similar HOI descriptions by changing verbs or nouns. They then propose EgoNCE++, an asymmetric contrastive learning objective to improve the models' sensitivity to nuanced changes in HOI-related language by using LLM-generated negative samples to enhance text supervision and preserve object-centric video representations. The paper shows that EgoVLMs generally behave better at object recognition while struggling with action. The experiments show that EgoNCE++ enhances performance across three EgoVLMs and improves generalization on seven downstream EgoHOI tasks.

### Strengths
1. The paper is clear and well-motivated. The authors first diagnose current EgoVLMs' capability on the proposed EgoHOIBench benchmark and then propose a method to address the problem. This makes the paper easy to follow and provides insights to readers.
2. The proposed EgoHOIBench provides a targeted evaluation for current egocentric video-language models regarding the capability of understanding hand-object interactions with variations in verbs and nouns. The authors also provide an inspiring analysis of the current EgoVLM and find their common failure to understand actions.
3.  The paper conducts extensive experiments and shows the proposed EgoNCE++ consistently improves model performance across various state-of-the-art EgoVLMs, highlighting its versatility and effectiveness.
4. The authors release the codes that promote reproducibility.

### Weaknesses
The major concern about this paper is its novelty. The idea of strengthening fine-grained compositional understanding by constructing hard-negative examples is not novel e.g. (Yuksekgonul et al., 2023). What are the major differences between the proposed method and previous works?

### Questions
Please see weakness section for the questions.

### Soundness
3

### Presentation
3

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
This paper introduces a novel way to identify HOIs in EgoVLMs, which addresses the limitation of current egocentric models regarding verb recognition. They propose EgoHOIBench, a new benchmark designed to evaluate understanding in EgoVLMs, that can evaluate EgoVLM’s capabilities in understanding variations of HOI combinations. In addition, their experiment demonstrates a stronger robustness towards recognizing nouns through their analysis of EgoHOIBench performance on HOI-verbs and HOI-nouns. Furthermore, they propose EgoNCE++, an asymmetric contrastive learning objective to address these limitations by enhancing model robustness in handling fine-grained verb and noun variations within HOIs for egocentric video-language pretraining, which successfully fulfills their aim to preserve the object-centric nature of the feature space without additional visual data usage or architectural changes.

### Strengths
•	The paper pinpoints the current weakness that existing benchmarks in egocentric vision with EgoHOI are limited. While some of them are only emphasized in kitchen scenarios, the others fail to provide effective supervision for understanding the nuances of HOI combinations that make our current model “a lack of fine-grained negative supervision during pretrained process”. 

•	The author discovers this critical gap and gives out their own solution in making EgoHOIBench, a benchmark specifically designed to test HOI comprehension in egocentric contexts, which is designed to more effectively evaluate the ability of EgoVLMs to select the correct sentence from multiple HOI-related options using video-text matching.

•	Compared with InfoNCE and EgoNCE, which often sample easy negative pairs without employing hard negative mining for text, and distinguish EgoHOIs based on verb-noun variation, EgoNCE++ incorporates asymmetric video-to-text and text-to-video losses, which enables the model to better understand HOI combinations by generating negatives through HOI-related word changes and preserves object-centric feature properties by clustering video representations based on similar nouns.

•	The paper is well-written and also the experiments are well-structured by covering a large range of benchmarks in Egocentric Vision tasks across commonly used datasets: Open-vocabulary recognition, multi-instance retrieval, and action recognition.

### Weaknesses
•	The paper introduces EgoNCE++ as an asymmetric contrastive learning objective. Figure 3 shows the visualization of LaViLa’s feature space indicating both video and text feature space exhibit the object-centric property and suggests that video-noun matching is easier than video-verb matching since noun-anchored embeddings form tighter clusters, while verb-anchored embeddings are more dispersed. It remains unclear how the verb-anchored embeddings change after applying EgoNCE++. A visualization of the feature space after the application of EgoNCE++ would be beneficial to understand the impact of the proposed loss function on the verb-anchored embeddings.

•	The paper mentions that it utilizes the LLaMA-3-8B model to generate HOI candidates through in-context learning. While the use of a large language model is interesting, it would be important to quantify the computational cost associated with this approach. An analysis of the performance gains versus computational expense (FLOPs) would be necessary to understand the trade-offs of this approach compared to simpler negative sampling techniques.

•	EgoNCE++ works significantly well on the author’s self-designed benchmarks EgoHOIBench, but it seems that for other datasets the improvement is marginal: EK100-MIR, CharadesEgo shown in Figure.5; EK-100-MIR and EGTEA in Table 9 for zero-shot setting; LaViLa and LaViLa++ in Table 10 and Table 7. The limited improvement on other datasets raises concerns about potential overfitting to the EgoHOIBench dataset. It is also unclear if the model is truly learning a generalizable representation of HOIs or if it is primarily optimizing for the specific nuances of the EgoHOIBench dataset, which focuses on fine-grained HOI comprehension.

### Questions
Questions are written with weakness.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
In this paper, the authors propose a new dataset, named EgoHOIBench, which consists of multiple choice questions for video clips in which there are two settings for verb and noun understanding. There are 10 choices for each case in which the verb or the noun respectively have been changed to create a hard negative. The paper finds that current Egocentric VLMs are unable to handle this change and so a new loss, named EgoNCE++ in which an asymmetric objective forces the model to understand minor differences in text yet for video groups the representations via their noun representations. The results show that for the EgoHOIBench, training current Egocentric VLMs with the new objective leads to an improvement in performance as well as for other downstream tasks.

### Strengths
* The results of the different Egocentric VLMs on downstream tasks after being trained with the new EgoNCE++ objective are good with nice increases in performance.
* Creating and proposing an asymmetric loss with EgoNCE++ is interesting and makes a lot of sense in how these two settings need to be treated differently whereas in the past this has not necessarily been true.
* There are a lot of results (and qualitative figures within the appendix) to showcase the method and struggles of the current methods without the EgoNCE++ objective.

### Weaknesses
# Weaknesses
* One potential reason for the new loss doing so well on the constructed HOI-Bench is as the benchmark has been designed in the same way as the loss function. A model that has been trained using a loss with negatives that represent the same style of negatives that are in the ground truth answers is certainly going to do better. The fact that the negatives are generated using an LLM or the vocabulary of the dataset, and then used to train a model which is then evaluated on a dataset generated in the same way, raises concerns about the generalizability of the results. This is especially true given that the negative samples are generated by replacing either the verb or the noun, which is exactly how the benchmark is constructed.
* Models seem to already do well on noun focused tasks, so it isn't clear to me why there is a large focus on still clustering videos based on similar noun representations only. The justification for this is not strong enough, as it is not clear why verb representations should be ignored when clustering videos, especially given that the task is to understand both verb and noun interactions. This seems to be an unnecessary constraint on the model's representation learning.
* Currently, the method section (Section 3) is lacking some important information regarding how the negatives are generated beyond an LLM/using the vocabulary of the dataset. Also, if there is any checking that is done to reduce/remove false negatives. The description of the negative generation process is too high-level, and it is not clear how the LLM is prompted to generate semantically distinct negatives. Furthermore, the claim that a synonym list is used to remove false negatives is not sufficiently detailed. It is not clear how this list is used and what happens if a generated negative is not in the synonym list but is still a false negative.
* The details of how HoI-bench is collected within the main paper is very scarce. The appendix includes some more information, but is still quite lacking. Details of why the number of videos were chosen, number of captions, any choice of category within Ego4D etc. is missing. The lack of clarity on the data collection process makes it difficult to assess the quality and representativeness of the dataset. The specific criteria used to filter videos and the rationale behind the number of captions per video are not well explained.
* Instead of defining a new metric to look at the positive/negative similarities within equation 6/figure 7. A histogram could have been used instead which might have given a clearer picture (again using the max negative). It's less intuitively clear from the figure what the numbers represent, especially as these have been multiplied by 100, emphasising the small differences even further.

# Additional Comments
Table 3 is inconsistent with how it uses lower case and upper case compared to the rest of the paper. Additionally, 'ours' is used here instead of EgoNCE++.

### Questions
1. Has an investigation/analysis been carried out regarding the fact that the loss is designed in the same way as the answers within the dataset? An outcome of this can be seen within Table 4 perhaps, where the choice of generator leads to a large increase in results for HOIBench, but is marginal for the EK-100-MIR task.
2. What does it mean by the sentence not made excessively difficult? Is this because false negatives could be introduced via semantic matching? If so, what is used to prevent this?
3. Why cluster videos based on similar noun representations only, instead of a mix of verb and noun representations? 
4. How are negatives introduced into the video-to-text loss to ensure that false negatives are not included? It is mentioned that either vocabulary from the dataset or an LLM is used to generate the negatives, but there is no information on how this is done. Is this the same as the collection information for HOI-Bench
5. Were all videos chosen for HOI-Bench from the validation set in a similar fashion to EgoMCQ? Or were some videos excluded? How was 10 settled on as the number of captions?
6. When constructing the dataset, has any care been taken to ensure that the LLM used to generate the questions isn't hallucinating? Were any measures put in place to remove noise and ensure a cleaner outcome for the dataset? Also, has any human checking/evaluation been carried out to get a sense of how clean the data is?
7. Has an ablation been carried out in which EgoNCE++ (ours in Table 3) is used for the loss and InfoNCE is used for the V2T loss?
8. For figure 6, has this been evaluated with how the number of negatives scales for the base models without the EgoNCE++ loss? It would be interesting to see how this compares for both models.
9. Has a histogram of positive/negative similarities been created instead of using the new PND metric in Figure 7?
10. It would be interesting to see Figure 3 after the EgoNCE++ objective has been applied if this has been created to see how this differs.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
* Current EgoVLMs, used to understand hand-object interactions in first-person views, can be easily misled by minor changes in interaction descriptions (e.g., changing verbs or nouns).
* A benchmark was created to highlight the limitations of EgoVLMs, particularly their struggle with recognizing verbs compared to nouns, often due to insufficient fine-grained supervision.
* An asymmetric contrastive objective was introduced to improve video-language alignment:
 Video-to-Text Objective utilizes enhanced text supervision with negative captions generated by large language models or HOI-related vocabulary substitutions.
Text-to-Video Objective focuses on an object-centric feature space that clusters video representations based on shared nouns.
* The proposed approach, EgoNCE++, significantly improves EgoVLM performance, especially in tasks like multi-instance retrieval, action recognition, and temporal understanding.

### Strengths
1. The study tackles a key shortcoming in egocentric video-language models (EgoVLMs), which is their limited ability to distinguish subtle changes in interaction descriptions. This issue has significant implications for understanding hand-object interactions, a critical area in ego-centric vision applications.

2. The work introducing a specialized benchmark to evaluate EgoVLMs under challenging scenarios is a valuable contribution. This benchmark exposes performance gaps that were previously under-explored, providing a robust foundation for future research and model improvements.

### Weaknesses
1. The proposed asymmetric contrastive objective may lack the degree of methodological novelty expected. Similar objectives and contrastive learning techniques have been explored in other contexts as follows:
 * (a) The use of negative mining in contrastive learning is well explored in [1], where it aims to find better hard negatives to benefit contrastive learning.
 * (b) In the field of using augmented captions in multimodal contrastive learning is explored in [2].
 * (c) The use of LLM to generate more text for learning is explored in [3].


2. Since the model is trained and evaluated on a benchmark specifically designed for the study, it’s unclear if these gains will translate to other existing benchmarks or real-world applications. As shown in Tables 3 and 4, the gain over the existing dataset using the proposed dataset is limited. This creates the risk of overfitting to a controlled benchmark, which could raise questions about generalizability.

### Questions
1. How does the proposed asymmetric contrastive objective compare with other contrastive techniques in video-language modeling? Could you clarify what specific elements make it novel in this context?

2. Can you elaborate on the robustness of the generated negative captions? Have you evaluated how biases in large language models might affect the model's performance?

3. How does the proposed benchmark compare to existing ones since the improvement is not significant on the existing dataset, and do you anticipate any limitations when applying it to real-world scenarios or other egocentric datasets?

### Soundness
3

### Presentation
3

### Contribution
2
