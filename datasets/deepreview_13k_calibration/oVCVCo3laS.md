# DualTime: A Dual-Adapter  Language Model for Time Series Multimodal Representation Learning

- Decision: Reject
- Avg Score: 5.20
- Scores: 5, 5, 5, 6, 5

## Abstract
The recent rapid advancements in language models (LMs) have garnered attention in time series multimodal representation learning. However, existing contrastive learning-based and prompt-based LM approaches tend to be biased, often assigning a primary role to time series modality while treating text modality as secondary.
We classify these approaches under a temporal-primary paradigm, which overlooks the unique and critical task-relevant information provided by the text modality, failing to fully leverage mutual benefits and complementarity of different modalities.
To fill this gap, we propose a novel textual-temporal multimodal learning paradigm that enables either modality to serve as the primary one while being enhanced by the other, thereby effectively capturing modality-specific information and fostering cross-modal interaction. In specific, we design DualTime, a language model composed of dual adapters to implement temporal-primary and textual-primary modeling simultaneously. Within each adapter, lightweight adaptation tokens are injected into the top layers of LM to encourage high-level cross-modal interaction. The shared LM pipeline by dual adapters not only achieves adapter alignment but also reduces computation resources and enables efficient fine-tuning. Empirically, DualTime demonstrates superior performance, achieving notable improvements of 7\% accuracy and 15\% F1 in supervised settings. Furthermore, the few-shot label transfer experiments validate DualTime's expressiveness and transferability.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces DualTime, which employs a dual-adapter architecture such that time-series and text modalities can each serve as primary modes. It introduces learnable tokens into the top layers of the LM backbone to facilitate multimodal fusion. The method leads to improvements over baseline methods, showing the method's effectiveness in leveraging information from both modalities.

### Strengths
1. Detailed experiments are conducted to present the effectiveness of the method, including both supervised fine-tuning and unsupervised learning with linear probing. The experiments show the method is able to learn general representations for the given task.
2. Few-shot transfer is further investigated, proving the generalizable features learned from the method, though the experiments are conducted in an in-dataset setting and it is unclear if it is useful for cross-domain transfer.

### Weaknesses
The novelty of the adapter and fusion mechanism is more or less limited. From the results, it seems like the gap between DualTime (text), where text serves as a primary mode, and DualTime is small. What are the implications of this pattern?

### Questions
What is the design choice for the LMs? e.g., why does the main backbone (GPT-2) need to be different from the text encoders used to encode secondary text inputs (BERT)? Are there any ablations about the main backbone?

### Soundness
3

### Presentation
3

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
This paper introduces DualTime, a parameter-efficient dual-adapter language model designed for multimodal representation learning that integrates both time series and textual data. Unlike prior models that often prioritize time series or text as the primary modality, DualTime employs a balanced textual-temporal paradigm, enabling each modality to enhance the other. By using two adapters within a shared language model backbone, the model captures high-level cross-modal interactions, achieving improvements of 7% in accuracy and 15% in F1 score on the PTB-XL ECG and TUSZ EEG datasets in supervised learning settings.

### Strengths
This paper presents an new approach to multimodal time-series learning through the introduction of the DualTime model, offering a fresh perspective that could inspire further exploration in balanced multimodal learning. It is well-structured and clearly presents the problem setting and results.

### Weaknesses
### Benchmarking in Diverse Domains and Foundation Models
Although DualTime performs well on the PTB-XL and TUSZ datasets, these are both medical datasets. It would be interesting to know DualTime’s performance and generalizability on additional domains beyond healthcare. A broader selection of multimodal dataset from other fields would provide more robust evidence of DualTime's effectiveness in multimodal time-series learning. Additionally, evaluating the model's architectural adaptability with other language models or LLMs could further demonstrate its potential generalization across different foundation models.



### Questions
The current experiment results lack sufficient evidence to show DualTime's general "Time Series Multimodal" capability. Beyond the text and time-series modality, how does DualTime perform with other modality combinations, such as visual and time-series or in non-medical domains?  Experiment results behind these questions could be important to claim DualTime's Time Series Multimodal capabilities.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper introduces DualTime, a novel multimodal language model designed for time series representation learning. The key contributions and highlights of the paper are as follows:

Textual-Temporal Multimodal Learning Paradigm: The paper proposes a new paradigm that treats both time series and text modalities equally, aiming to fully leverage their complementary information. This paradigm is designed to capture the intricate interactions between different modalities. DualTime consists of two multimodal adapters: a temporal-primary multimodal adapter and a textual-primary multimodal adapter. Each adapter treats one modality as primary and enhances it with the other modality. This dual-adapter design allows each modality to serve as the primary modality, improving the model's ability to capture unique and shared semantics.

Comprehensive Evaluation: The paper includes extensive experiments, ablation studies, and sensitivity analyses to validate the model's effectiveness, robustness, and efficiency. It also explores the impact of different textual encoders and discusses the model's extensibility to more modalities.

### Strengths
Novel Paradigm: The introduction of a textual-temporal multimodal learning paradigm that treats both time series and text modalities equally is a significant departure from existing approaches, which typically prioritize time series as the primary modality. Specifically, the authors propose two novel designs:
(1) Dual Adapter Design: The dual-adapter architecture, where each adapter treats one modality as primary and enhances it with the other, is an innovative approach to multimodal fusion. This design allows for a more comprehensive understanding of the interactions between modalities.
(2) High-Level Multimodal Fusion: The use of learnable adaptation tokens to achieve high-level multimodal fusion within the top layers of the language model is a novel technique that enhances the model's ability to capture complex semantics.

Comprehensive Experiments: The paper includes extensive experiments on public real-world datasets, demonstrating DualTime's superior performance in supervised, unsupervised, and few-shot learning scenarios. The results show consistent improvements in accuracy and F1 score across various tasks.

### Weaknesses
Consider stronger baselines for text-based methods. GPT-4o and the LLaMA series models serve as robust baselines for text-based approaches. BERT and GPT-2 are now outdated in the realm of NLP. Given that GPT-2 has performed reasonably well, I am curious about the capabilities of GPT-4o. While these models do have more parameters, they are easily accessible and offer low latency. In practical applications, they are excellent candidates.

From my perspective, I recommend the author use state-of-the-art pre-trained checkpoints, such as LLaMA-3, for the experiments. GPT-2 is outdated and insufficient for validating the capabilities of modern language models. While the paper seems more suited to 2022, it is now 2024, and demonstrating success with GPT-2 does not effectively showcase its relevance to current models.

### Questions
N/A

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents DualTime, a novel multimodal language model designed for time series representation learning. It integrates both temporal and textual modalities to enhance the model's performance in disease detection and classification tasks. The authors argue that existing methods often overlook the unique information provided by text, which can lead to sub-optimal outcomes. By employing a dual adapter framework, DualTime aims to effectively explore the complementary information in multimodal inputs. The experimental results demonstrate that DualTime consistently outperforms other methods across various proportions of labeled data, showcasing its robustness and effectiveness.

### Strengths
1)This paper presents an innovative dual-adapter framework in the field of multimodal learning, treating text and time series modalities equally for the first time. This approach not only addresses the limitations of existing methods in handling multimodal data but also demonstrates the potential of effectively integrating both modalities' information for disease detection and classification. Notably, the introduction of learnable adapter tokens facilitates the extraction of high-level multimodal semantics, which is a novel contribution to the existing literature. The proposed problem has important research implications and application value.
2)The experimental design of the paper is rigorous, covering multiple real-world datasets (such as PTB-XL and TUSZ) and employing various evaluation metrics (accuracy, precision, recall, and F1 score) for comprehensive assessment. The results indicate that DualTime consistently outperforms other baseline methods across different proportions of labeled data, enhancing the credibility of the findings through systematic validation.
3)The paper is well-structured and logically coherent, with concepts articulated in an easily understandable manner. The authors clearly outline the research background, objectives, and significance in the introduction, and provide detailed descriptions of the design and implementation of DualTime in the methods section. Additionally, the use of figures and tables effectively supports the textual content, making complex concepts more digestible.

### Weaknesses
1) The paper mentions that the choice of adaptive token length and the number of network layers significantly impacts model performance, but lacks a systematic analysis of these parameter choices. It is recommended that the authors provide additional results on parameter sensitivity analysis to help readers understand how to optimize the model. Specifically, the paper should explore how different token lengths affect the model's ability to capture both short-term and long-term dependencies in the time series data. Furthermore, a detailed analysis of the impact of the number of layers on the model's capacity to learn complex multimodal representations is needed. This analysis should include not only the performance metrics but also computational cost and training time. 
2) DualTime employs a dual-adapter design that treats the textual modality and temporal modality as primary and auxiliary modalities, respectively, facilitating dynamic fusion at a high level through learnable adapter tokens. This method shares a pre-trained language model, enhancing the capture of complementary information between the two modalities and improving the model's learning efficiency and performance. To further demonstrate the effectiveness and advancement of this fusion method, experiments should be conducted comparing it with other fusion approaches, such as simple concatenation, weighted fusion, and attention mechanisms. The paper should also investigate the impact of different fusion strategies on the model's ability to handle noisy or incomplete data in either modality. A more detailed analysis of the fusion process, including visualization of the learned attention weights or adapter token representations, would also be beneficial.

### Questions
How does DualTime ensure that the integration of textual and temporal modalities does not lead to overfitting on specific datasets? What strategies are employed to enhance the model's generalization capabilities across diverse datasets, particularly in practical applications? Do the authors plan to extend this work to other types of time series data (beyond EEG and ECG), and if so, what adjustments would be necessary?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors propose DualTime, a method for integrating clinical notes and electrocardiograms into a prediction model. The architecture uses per-modality adapters with time-series-first and text-first representations, which are later merged in a final prediction. The authors also include an unsupervised learning mechanism which should lead to better aligned representations and better predictive performance.

### Strengths
- Interesting work on multi-modal time-series that seem to achieve good performance in practice in two datasets.
- Code is shared which means experiments are reproducible.
- Experiments under multiple angles are included: fully supervised, different ratios of unsupervised+supervised data, few-shot learning.

### Weaknesses
The paper can be improved across many angles:
- there is notation and formulas that are unnecessary and needed not be there, whereas there are points that could have been clarified in the manuscript (see comments).
- only two datasets are used without an explanation to why that is the case. I find that especially problematic since the paper sells the idea that they do "multi-modal time series learning" whereas the two datasets used include the same modalities. Specifically, the paper focuses on paired clinical notes and ECG data, limiting the generalizability of the method to other multimodal scenarios.
- baselines have a frozen language model backbone without a clear motivation for why; instead, authors should have included results for the baselines as they were proposed in the literature vs. a version where the LM backbone is frozen (if desired). This choice looks like a severe misrepresentation of baseline models' performance. The authors should provide a clear justification for this design choice, and ideally include results for the baselines as originally proposed, to allow for a fair comparison.
- ablation did not cover the case where unsupervised learning is not used at all, and did not include a delta (without unsup. learning vs. with unsup. learning). The absence of this ablation makes it difficult to quantify the contribution of the unsupervised learning component to the overall performance of the model.

### Questions
- Interesting way to motivate your work using unimodal classifiers in Figure 1b. Could you please clarify what exactly is the "unimodal classification experiment" (line 79) in one sentence? I.e., what is that you are predicting, and what kind of model / architecture do you use to do that?
- Regarding the unsupervised learning part of your experiments, I missed an ablation of that. You should include experiments where you only use supervised learning, vs. unsupervised plus supervised learning, to show how much you gain from adding these contrastive learning procedure. A delta here ($\Delta$) with and without unsupr. learning would be nice to have.
- You only use two datasets. Why? Does that have to do with the (implicit) assumption you make about the data, that is you have pairs of (clinical notes, ECGs) for each patient throughout time? What about other modalities?
- In lines 92-94, I believe the last two challenges are actually one challenge: that of integrating and fusing diverse multi-modal signals.
- In line 151-152 you state "Each adapter implements multimodal fusion in the topmost M (M ≤ L) transformer blocks of the language model." That is confusing, you don't need to say the M ≤ L part (I had the impresssion for a while that there was a typo). Also, you only adapt the last layer. You could remove all this notation by just saying this, or clearly stating here that $M=1$.
- Are Equations 1, 2, 3 implementing something different from a standard Transformer layer? If it is not, please just state that these layers are standard Transformer layers. If it is, please clearly state somewhere what these differences are (I don't think there are differences).
- For Equations 6, 7, 8, are you using any standard adapter architectures introduced in the literature? If you are, please state that clearly including a citation to the paper. If not, please clearly indicate where your architecture differs from the literature.
- The patch+stride transformation of the time series signal to use in a language model described in lines 197-200 is proposed in this work or was proposed in previous work? If it was proposed in previous work, please state that and add a citation.
- Instead of including equations describing standard Transformer blocks, I believe it would be more relevant to include: an alternative equation 4 where you describe the transformations "TemEnc" and "Proj" in more detail; an equation where you show how $\tilde{X}$ is transformed into $E_t$ (lines 198-200); an alternative equation 9 where you also show what you mean by "Proj" (linear transformation matrix?); there is maybe no need for another separate equation, but add the statement where you show how you compute $\tilde{T}^l_T$ similarly to what you do in Equation 5 for the text-first part of the model.
- Add citations for the datasets in line 258 and explain what you mean by "publicly available". Do you need any credentialing? Is a link to download the datasets available for everyone? Please include the link to download the data, or to the dataset download website.
- Also, please explain what is the difference between an ECG and an EEG and write down what these acronyms mean in the main paper (when describing the datasets). You could also clearly state that are the tasks you have under each dataset in the main paper: at least how many classes do you predict.
- In lines 294-295 you state "Note that we make minimal adjustments to some baselines for our experiments, such as freezing the major parameters of GPT-2 or BERT, only replacing and fine-tuning the output layer for our tasks". Why do you do that? You do not have the baselines you are referring to in the citations, then. This is a major issue, especially if you do not explain why you do this. Do you want to have baseline models with a similar number of trained parameters to your models? Then please add the exact number of trained parameters in each model. I believe you should always include the baselines fully finetuned, if that is how they were proposed in the original work. You may wish to include your frozen baselines as well, but the original baselines should be included. Moreover, if parameter efficiency is an angle in your work, make that clear from the beginning in the introduction (and possibly in the title of the manuscript). You can provide a table comparing the number of trainable parameters and total parameters for each model, including your models and baselines. That would make the picture more complete.
- I think the experiments described in Section 3.3 need much more clarification. You say "First, we train each model in an unsupervised manner." That is too vague. By "which model" do you mean all models evaluated in Fig.3a and in Fig.3b? For the DualTime models that you propose, the way you do that is clear (trained using Eq. 12). For all the other models in Fig.3a and Fig.3b, how did you do that?

### Soundness
2

### Presentation
2

### Contribution
2
