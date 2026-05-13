# Synergy Learning with Small Models promotes LLM Zero-Shot Tabular Prediction

- Decision: Accept
- Scores: 5, 8, 8, 5

## Abstract
Recent development in large language models (LLMs) has demonstrated impressive zero-shot proficiency on unstructured textual or multi-modal tasks across various domains. However, despite with inherent world knowledge, their application on structured tabular data prediction still lags behind, primarily due to the numerical insensitivity and modality discrepancy that brings a gap between LLM reasoning and statistical machine learning. Unlike textual or vision data (e.g., electronic health records, medical images), tabular data is often presented in heterogeneous numerical values (e.g., blood test reports). This ubiquitous data format requires intensive expert annotation, and its numerical nature limits LLMs' ability to effectively transfer untapped domain expertise. In this paper, we propose SERSAL, a general loop of thought prompting method by synergy learning with small models to unconditionally enhance zero-shot tabular prediction for LLMs. Specifically, SERSAL utilizes the LLM's zero-shot outcomes as original soft annotations, which are dynamically leveraged to teach a better small student model in a semi-supervised manner. Reversely, the outcomes from the trained small model are used to teach the LLM to further refine its real capability. Such mutual process can be repeatedly applied for continuous progress. Comprehensive experiments on widely used domain tabular datasets show that, without access to gold labels, applying SERSAL to OpenAI GPT reasoning process attains substantial improvement compared to linguistic prompting methods, which serves as an orthogonal direction for tabular LLM, and increasing prompting bonus is observed as more powerful LLMs appear.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors propose a framework for refining a pretrained LLM for zero-shot tabular prediction. In particular, the authors propose to iteratively refine a given LLM's tabular prediction capability via a small "student" tabular prediction model (FT-Transformer), where at each iteration, the LLM is prompted to generate noisy labels for an unlabeled training dataset, the tabular prediction model is trained on the noisy labels based on the DivideMix approach, and the predictions from the trained tabular prediction model is used to fine-tune the LLM. Focusing primarily on tabular prediction datasets from the medical domain, the authors conduct several experiments using GPT-3.5 and GPT-4, and compare the resulting performance of their approach against those of alternative prompting methods.

### Strengths
- The limited generalizability/transferability of LLMs to the tabular domain, which is discussed as the main motivation for the paper, is a well-known issue and an active area of research.
- The idea of using an LLM as noisy labelers and combining it with semi-supervised learning methods designed to handle noisy labels is  interesting.
- Several ablation experiments are considered to investigate the impact of different design choices (e.g., soft vs. hard labels from the LLM, early stopping), and empirically validate the assumption that high LLM confidence scores tend to correlate with the accuracy of the LLM-generated labels.

### Weaknesses
 - Overall, there appears to be a misalignment in the motivation for the paper (i.e., improving the zero-shot generalizability of LLMs for tabular prediction) and what is proposed in the paper. My interpretation of what is really being addressed in the paper is "How can we leverage LLMs as noisy labelers to train a downstream *tabular prediction model* (e.g., FT-Transformer) when we only have access to an *unlabeled* training set. In particular, the following are my specific concerns:
    - While the proposed iterative process also involves fine-tuning the LLM, predictions on any test set are generated using the downstream tabular prediction model, as presented in line 13 of Algorithm 1 ($\theta^{*(t)}$ denotes the parameter of the downstream model and not the LLM).
    - The proposed approach is not really "zero-shot" in that while the training dataset does not include the ground-truth labels, the dataset is still being used to explicitly train the tabular prediction (and also the LLM for that matter).
    - The Introduction discusses limitations of LLMs in handling heterogeneous numerical features, but the paper does not directly address how to resolve this problem for LLMs. 
    - As such, the title and the overall framing of the work appear ill-conceived, as the work is not really enhancing the "zero-shot tabular prediction for LLMs".
- In Section 2.2, the overall description of how the DivideMix approach is being applied to the considered context would benefit from better clarity and details (even if pushed to the Appendix given space constraints). For example, how is the early stopping being performed within the adapted DivideMix algorithm? What are the hyperparameters in the phrase "hyper-parameter selection for the teaching process" and how are they being selected in the absence of a validation set?
- In the experiments, the proposed approach is compared against alternative zero-shot (vanilla zero-shot, zero-shot CoT, TabLLM, LIFT) and few-shot prompting strategies for generating tabular predictions from off-the-shelf LLMs, which do not seem to be the most relevant baselines here. The proposed approach involves directly *fine-tuning* the LLM as opposed to being a new "prompting" strategy (not to mention that it's not even really the LLM that's generating the final predictions), and while TabLLM and LIFT were both originally proposed for fine-tuning the LLM for tabular prediction, these baselines are only considered in the zero-shot prompting regime.
    - On a related note, since TabLLM and LIFT were considered in the zero-shot setting, this would mean that the only difference between them and the vanilla zero-shot prompting baseline is really in the prompt format and the set of instructions. The AUC values in Table 2 seem to indicate that the prediction results are highly sensitive to such choices. It is well-known in the literature that LLMs are highly sensitive to the choices of the prompt [1] and the tabular feature serialization method [2,3], so the results should appropriately account for these concerns to ensure a fair comparison.
- The datasets considered in the main evaluations (Section 3.1) are publicly available datasets, with most of them having been around for a long time. As such, there is a potential risk that these datasets have been part of the LLM pretraining corpus, which limits the generalizability of the findings. While the authors do conduct an ablation study in Section 3.6 involving a randomly generated dataset (denoted as "Fake") and demonstrate that the proposed approach can fail if the model does not have relevant domain knowledge, it seems important that the evaluations are also carried out on either (i) private datasets or (ii) public datasets that have been released after the pretraining-data cutoff dates for the LLMs, which still come from a domain that the LLMs would carry relevant domain knowledge. For example, would the LLM still generate high-quality confidence scores if we were to test on a new medical diagnosis dataset released in the future? It appears important that the LLM confidence scores are reasonably well-calibrated for this approach to work in the first place; otherwise, the error will only compound over several iterations of the proposed algorithm.
- In Figure 2 and Table 4, why are the results shown only for the ECD and LI datasets? Do similar trends hold for the other datasets?

### Questions
Please see my comments in the Weaknesses section.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This study focused on training a small model to effectively promote LLMs to enhance their zero-shot predictions performance on healthcare tabular data. The study was motivated by the observations that, in the literature, most of the related studies have been primarily focused on either the medical imaging data or the text data. While, healthcare tabular data may pose their unique challenges, where it is common to have widely heterogenous distributions across different variables. The proposed idea of synergy learning is to first deploy LLM to generate some noisy annotations to allow the small model to learn and generate tuning promotes to refine LLM for the task; and we iterate this "synergy learning" to continuous improve the model's final performance. The authors conducted detailed experiments with some publicly healthcare tabular datasets to validate the performance of their proposed approach. Additionally, the authors have also investigated the generalizability of the proposed approach over other domains via evaluations with 3 classification datasets and 1 generated dataset, aiming to simulate the scenario for a unknown domain.

### Strengths
1/ The manuscript is, in general, well written, Objectives and motivations of the study were clearly explained. Details of the experiments were provided. Key findings were appropriately summarized in tables and figures.

2/ I share the same belief that the size of the LLMs continues to go. It will become infeasible to retrain or fine tune the entire LLMs for specific domains. The use of small models to learn from LLMs and/or to promote LLMs is indeed a promising direction to explore.

3/ The study proposed an interesting synergy learning mechanism. In the proposed mechanism, small model first learn from the noisy annotations from LLMs with low confidence, then, after quality controls, the learned small model generate promotes aiming to refine LLMs' predictions; while the refined LLMs will again generate slightly more confident labels to further train the small model. The proposed synergy learning process is interesting and sound.

4/ The team has evaluated the performance of the proposed approach over 10 healthcare datasets focusing on different disease. This helps to show the stability of the proposed approach's performance over healthcare tabular data.

5/ Also, to demonstrate the potential generalizability of the proposed approach to other domains (other than healthcare), it was also evaluated over 3 binary classification datasets and also 1 simulated dataset.

Overall the quality of the manuscript is good. Nevertheless, there are still some areas for improvements as mentioned next.

### Weaknesses
1/ Better explanation on background knowledge for our general LLM audiences

The proposed SERSAL prompting for LLMs on tabular prediction task bears an essentially different mechanism compared to prevailing textual prompting methods, requiring relevant knowledge on noisy label learning theory for general audiences in LLM research fields, it will be better to detail the inherent mechanism on why a better small model can be obtained by learning from the LLM noisy outputs. Specifically, the paper should elaborate on the theoretical underpinnings of using noisy labels from LLMs to train a small model, including concepts like the memorization effect of neural networks and how methods like DivideMix exploit this effect to differentiate between clean and noisy labels. A more detailed explanation of how the loss function is adapted to handle noisy labels would also be beneficial.

2/ Dependency on initial LLM performance?

As pointed out in the Limitation Section (Appendix A), the proposed SERSAL prompting requires the LLMs with latent knowledge in the target domain to be effective, though a randomly generated dataset (Fake dataset in Table 5) is evaluated to partially answer SERSAL unusability on unreasonable data domain, but the case of reasonable data with very low initial accuracy and how to handle such datasets is not discussed (the fault tolerance limit or the least initial LLM performance that SERSAL can be accepted). The paper should include a more thorough analysis of the sensitivity of SERSAL to the initial performance of the LLM. It is important to understand the lower bounds of LLM performance for SERSAL to be effective and how the method behaves when the initial LLM predictions are only slightly better than random guessing. This should include a discussion of how the quality of the initial noisy labels impacts the final performance of the small model.

3/ Lack of detailed computational complexity analysis

The current manuscript did not analyze the computational complexity in detail which may be important for the usability of SERSAL on large-scale datasets. As one of the key novelty of the study is to enable the use of small models to enhance the learning efficiency of large models. Do think that detailed computational complexity studies are needed to justify this point. The analysis should consider the computational cost of each step in the SERSAL process, including the LLM annotation, training the small model, and fine-tuning the LLM. This should be broken down into time complexity and memory complexity, and should also consider the impact of different hyperparameters on the overall computational cost. Furthermore, the analysis should discuss the scalability of the approach with respect to the size of the dataset and the complexity of the tabular data.

4/ Some reference formatting issue

There are several instances of the misuse of LaTeX citation commands `\citep` and `\cite` in the paper (e.g., Line 65, 76, 85 and the caption of Fig. 1).

Please carefully correct the relevant LaTeX commands during the rebuttal phase.

### Questions
1/ Point 1 under weaknesses

It is interesting to aggregate LLM knowledge in a small tabular model in SERSAL process, could you give a detailed mechanism explanation on why a better performed small model can be learned from LLM outputs?

2/  Point 2 under weaknesses

Wonder how sensitive the effectiveness of SERSAL prompting is to the initial LLM performance on the target dataset, or how to apply SERSAL on the data domain where the initial performance is not good?

3/ Point 3 under weaknesses

Could provide the detailed computational complexity analysis of SERSAL in its real-world applications?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes a new method, SERSAL, using synergy learning to improve LLMs for zero-shot tabular prediction. SERSAL designs a loop which includes (1) soft LLM pseudo labelling (2) small models training with DivideMix (3) quality control (4) LLM fine-tuning. With one-loop training, SERSAL demonstrates new state-of-the-art zero-shot performance on 9 out of 10 tabular prediction datasets in the medical domain and 3 other binary classification datasets in other domains. Experiments also demonstrate improvements with more (3 loops) training by SERSAL.

### Strengths
This paper is overall very well written with clear methodology, experiments, and strong results.

The proposed method SERSAL designs a loop to enhance LLM capabilities in zero-shot tabular prediction. The idea of incorporating the semi-supervised learning DivideMix to address/mitigate noisy labels from LLMs and improve the performance of LLMs with small models (which are trained by DivideMix) is very interesting. Experiments also demonstrate the superior performance of SERSAL and the potential for further improvement with more loops of training, and better foundation LLMs (e.g. GPT-3.5 -> GPT4) across multiple domains.

Superior zero-shot performance across multiple datasets across multiple domains. Reasonable design and setup of experiments.

### Weaknesses
The type of tasks is restricted to binary classification. The method may have potential in more complicated tasks and more types of input data (beyond just tabular data) but these are not demonstrated or discussed in this paper.

The experiments on the effectiveness of multi-loop SERSAL are quite light (compared to experiments with one-loop SERSAL). Experiments with more loops and more datasets will be useful.

Elaboration on DivideMix in Section 3 will help improve the readability and understanding of the methodology.

### Questions
1. Transformer is still a relatively large model. It will be useful to see how small models like CNN, RNN, or even RF, SVM may work and accelerate the loops.

2. Table 4, please consider changing Loop 0,1,2 to Loop 1,2,3 to avoid confusion. 

3. Table 4, should the performance of N-loop SERSAL be the same as (N+1)-loop 0-shot LLM, because (N+1)-loop 0-shot LLM is the fine-tuned LLM from N-loop SERSAL?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors propose SERSAL, a general loop of thought prompting method by synergy learning with small models to unconditionally enhance tabular prediction for LLMs in an unsupervised way. This paper mainly solves the medical tabular prediction tasks.

### Strengths
1. The direction of applying synergy learning with small models and LLMs to enhance tabular prediction in an unsupervised way is promising and important.  
2. The paper is easy to follow.  
3. The proposed method is novel.

### Weaknesses
1. Does the paper mainly to solve traditional tabular prediction tasks or medical prediction tasks? If it's former, it seems that the used tabular data does not contain regression and multi-class classification, as discussed in [1]. So how does it behave on traditional tabular data, especially on regression and multi-class classification tasks? If it's latter, how do the authors ensure the safety of processing medical data with Large Language Models (LLMs), especially when adapting to real-world healthcare scenarios where data security is crucial [2], and the data is used for fine-tuning the LLMs? Furthermore, while the paper positions medical tabular prediction tasks as the central focus, the proposed method appears to be more suited for general tabular learning rather than specialized medical prediction. This is because there is a lack of incorporation of specific medical domain knowledge within the paper. Could the authors give more explanations?
[1] Revisiting Deep Learning Models for Tabular Data. NeurIPS 2021.
[2] Large language models encode clinical knowledge. Nature 2023.

2. I am uncertain whether it would be more appropriate to refer to the setting as unsupervised rather than zero-shot. In the context of zero-shot learning, as illustrated in TabLLM [3] and GTL [4], zero-shot implies that in target dataset, no training instances (x) that are similar to test instances are provided. In this paper, in target dataset, training instances from the same distribution without labels are provided for training. What is the definition of zero-shot used in this paper? Does 'no label' equate to 'zero-shot'? This distinction is important because the method leverages unlabeled data from the target distribution, which is not typical of a zero-shot setting.
[3] TabLLM: Few-shot Classification of Tabular Data with Large Language Models.
[4] From Supervised to Generative: A Novel Paradigm for Tabular Deep Learning with Large Language Models.


3. Is the annotation of samples by LLMs done on a sample-by-sample basis? If so, this process seems to require a high cost. Could you provide the time cost, especially considering the API call overhead for large language models?

4. Is TabLLM in Table 2 be tested in a zero-shot scenario? If so, it seems that TabLLM is better than GPT-3.5. Could you please explain why this might be the situation, given that GPT 3.5 has a more extensive knowledge base compared to TabLLM? It is unclear how TabLLM, which is a prompting method, can outperform the base LLM itself in a zero-shot setting.

5. What is the meaning of TabLLM + SERSAL (GPT-3.5) in Table 2, what is the role of each component? It is not clear how the TabLLM prompting method interacts with the SERSAL framework and what the specific contribution of each component is.

6. Recently, generative models pertained on a large set of tabular data have also demonstrated zero-shot capabilities on tabular prediction tasks [4]. I suggest that these models should be considered as baseline models since they can be seen as powerful tools for zero-shot performance on new tasks. The lack of comparison with these models makes it difficult to assess the true novelty and performance of the proposed method.
[4] From Supervised to Generative: A Novel Paradigm for Tabular Deep Learning with Large Language Models.

### Questions
1. Does the paper mainly to solve traditional tabular prediction tasks or medical prediction tasks? If it's former, it seems that the used tabular data does not contain regression and multi-class classification, as discussed in [1]. So how does it behave on traditional tabular data? If it's latter, how do the authors ensure the safety of processing medical data with Large Language Models (LLMs), especially when adapting to real-world healthcare scenarios where data security is crucial [2], and the data is used for fine-tuning the LLMs? In addition, while the paper seems to position medical tabular prediction tasks as the central focus, the proposed method appears to be more suited for general tabular learning rather than specialized medical prediction. This perception arises from the lack of incorporation of specific medical domain knowledge within the paper. Could the authors give more explanations?  
[1] Revisiting Deep Learning Models for Tabular Data. NeurIPS 2021.   
[2] Large language models encode clinical knowledge. Nature 2023.  

2. I am uncertain whether it would be more appropriate to refer to the setting as unsupervised rather than zero-shot. In the context of zero-shot learning, as illustrated in TabLLM [3] and GTL [4], zero-shot implies that in target dataset, no training instances (x) that are similar to test instances are provided. In this paper, in target dataset, training instances from the same distribution without labels are provided for training. What is the definition of zero-shot used in this paper? Does 'no label' equate to 'zero-shot'?  
[3] TabLLM: Few-shot Classification of Tabular Data with Large Language Models.   
[4] From Supervised to Generative: A Novel Paradigm for Tabular Deep Learning with Large Language Models.   


3. Is the annotation of samples by LLMs done on a sample-by-sample basis? If so, this process seems to require a high cost. Could you provide the time cost?  

4. Is TabLLM in Table 2 be tested in a zero-shot scenario? If so, it seems that TabLLM is better than GPT-3.5. Could you please explain why this might be the situation, given that GPT 3.5 has a more extensive knowledge base compared to TabLLM?     

5. What is the meaning of TabLLM + SERSAL (GPT-3.5) in Table 2, what is the role of each component?    

6. Recently, generative models pertained on a large set of tabular data have also demonstrated zero-shot capabilities on tabular prediction tasks [4]. I suggest that these models should be considered as baseline models since they can be seen as powerful tools for zero-shot performance on new tasks.   
[4] From Supervised to Generative: A Novel Paradigm for Tabular Deep Learning with Large Language Models.

### Soundness
3

### Presentation
2

### Contribution
3
